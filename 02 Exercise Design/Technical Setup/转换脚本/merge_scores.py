#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the per-card scoring drafts (评分底稿_C0x-C0y.jsonl) of one run into the script's CSV layout.

Usage: python3 -I merge_scores.py <剧本.txt> <核验 dir> <run, e.g. A1>
Writes <run>评分底稿_原始作答.csv, <run>评分底稿_CEO最终.csv (9 columns as in script section 5),
<run>评分底稿_明细.csv (every field) and prints the totals. Standard library only.
"""
import sys, os, json, glob, csv, re
from collections import Counter

SCRIPT, DIR, RUN = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(SCRIPT, encoding='utf-8').read().split('\n')
hi = next(i for i, l in enumerate(lines) if l.startswith('单元,卡,主责,判分对象'))
header = lines[hi].split(',')
blank = []
for l in lines[hi + 1:]:
    if not re.match(r'Q\d\d[ab],', l):
        break
    blank.append(l.split(',')[:4])
rows = {}
for f in sorted(glob.glob(os.path.join(DIR, '评分底稿_C0*.jsonl'))):
    for l in open(f, encoding='utf-8'):
        r = json.loads(l); r['_file'] = os.path.basename(f)
        key = (r['unit'], r['layer'])
        assert key not in rows, key
        rows[key] = r
units = [b[0] for b in blank]
for u in units:
    for layer in ('原答', 'CEO最终'):
        assert (u, layer) in rows, (u, layer)
assert len(rows) == 2 * len(units)

def cell(r):
    s = ' / '.join(str(r[k]) for k in ('R判定', 'PH判定', '行动分', '依据分', '决策码', '记录索引'))
    if r['layer'] == 'CEO最终':
        s = f"{r['CO']}（CEO 自标 {r['CEO自标']}） | " + s
    return s

for layer, name in (('原答', '原始作答'), ('CEO最终', 'CEO最终')):
    with open(os.path.join(DIR, f'{RUN}评分底稿_{name}.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh); w.writerow(header)
        for b in blank:
            w.writerow(b + ['', '', '', cell(rows[(b[0], layer)]), ''])
fields = ['unit', 'layer', 'R判定', 'PH判定', '行动分', '依据分', '决策码', 'CO', 'CEO自标', '记录索引', '理由', '需组员定', '问题', '_file']
with open(os.path.join(DIR, f'{RUN}评分底稿_明细.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader()
    for b in blank:
        for layer in ('原答', 'CEO最终'):
            w.writerow({k: rows[(b[0], layer)][k] for k in fields})

for layer in ('原答', 'CEO最终'):
    rs = [rows[(u, layer)] for u in units]
    act = sum(r['行动分'] for r in rs if isinstance(r['行动分'], int))
    basis = [r['依据分'] for r in rs]
    bden = sum(isinstance(b, int) for b in basis); bsum = sum(b for b in basis if isinstance(b, int))
    print(layer, 'R判定', dict(Counter(r['R判定'] for r in rs)), '行动分', f'{act}/{len(rs)}', '依据分', f'{bsum}/{bden}', '待复核', len(rs) - bden,
          '需组员定', sum(bool(r['需组员定']) for r in rs))
    if layer == 'CEO最终':
        print('  C/O', dict(Counter(r['CO'] for r in rs)), '自标', dict(Counter(r['CEO自标'] for r in rs)),
              '出入', [r['unit'] for r in rs if (r['CO'], r['CEO自标']) not in (('C', 'CONFIRM'), ('O', 'OVERRIDE'))])
print('PH判定', dict(Counter(r['PH判定'] for r in rows.values())))
print('原答与CEO层 R判定不同:', [u for u in units if rows[(u, '原答')]['R判定'] != rows[(u, 'CEO最终')]['R判定']])
print('需组员定:', [(r['unit'], r['layer']) for r in (rows[(u, l)] for u in units for l in ('原答', 'CEO最终')) if r['需组员定']])
