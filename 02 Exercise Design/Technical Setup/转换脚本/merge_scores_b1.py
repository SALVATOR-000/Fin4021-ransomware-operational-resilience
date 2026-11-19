#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the B1 per-card scoring drafts into the sealed B1 score sheet layout, next to A1's final scores.

Usage: python3 -I merge_scores_b1.py <sealed B1 score sheet.csv> <A1 核验 dir> <B1 核验 dir>

Reads <B1 核验 dir>/评分底稿_C0*.jsonl (96 rows: 48 units x 原答/CEO最终), the sealed sheet (expectation
columns) and A1's final sheets (A1评分底稿_原始作答.csv, A1评分底稿_CEO最终.csv, column "A1").
Writes B1评分底稿_原始作答.csv and B1评分底稿_CEO最终.csv (the sealed 9 columns: expectations copied, A1 and
B1 filled), B1评分底稿_明细.csv (every field) and prints the totals. Never writes to the sealed sheet.
Standard library only.
"""
import sys, os, json, glob, csv, re
from collections import Counter

SHEET, A1DIR, DIR = sys.argv[1], sys.argv[2], sys.argv[3]
sheet = list(csv.reader(open(SHEET, encoding='utf-8-sig')))
header, body = sheet[0], sheet[1:]
units = [r[0] for r in body]
assert len(units) == 48 and header[-2:] == ['A1', 'B1'], header

a1 = {}
for layer, name in (('原答', '原始作答'), ('CEO最终', 'CEO最终')):
    for r in csv.DictReader(open(os.path.join(A1DIR, f'A1评分底稿_{name}.csv'), encoding='utf-8-sig')):
        a1[(r['单元'], layer)] = r['A1']

rows = {}
for f in sorted(glob.glob(os.path.join(DIR, '评分底稿_C0*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        if not line.strip():
            continue
        r = json.loads(line); r['_file'] = os.path.basename(f)
        key = (r['unit'], r['layer'])
        assert key not in rows, key
        rows[key] = r
missing = [(u, l) for u in units for l in ('原答', 'CEO最终') if (u, l) not in rows]
assert not missing, missing
assert len(rows) == 96, len(rows)


def cell(r):
    s = ' / '.join(str(r[k]) for k in ('R判定', 'PH判定', '行动分', '依据分', '决策码', '记录索引'))
    if r['layer'] == 'CEO最终':
        s = f"{r['CO']}（CEO 自标 {r['CEO自标']}） | " + s
    return s


for layer, name in (('原答', '原始作答'), ('CEO最终', 'CEO最终')):
    with open(os.path.join(DIR, f'B1评分底稿_{name}.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh); w.writerow(header)
        for b in body:
            w.writerow(b[:7] + [a1.get((b[0], layer), ''), cell(rows[(b[0], layer)])])

fields = ['unit', 'layer', 'R判定', 'PH判定', '行动分', '依据分', '决策码', 'CO', 'CEO自标', '记录索引', '理由',
          '需组员定', '问题', 'PH依据', 'A1对照', '例子候选', '_file']
with open(os.path.join(DIR, 'B1评分底稿_明细.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader()
    for u in units:
        for layer in ('原答', 'CEO最终'):
            w.writerow({k: rows[(u, layer)].get(k, '') for k in fields})


def exp_code(text, tag):
    m = re.search(tag + r'\s*(Y（混合[^）]*）|Y|N|U|随分支|依分支)', text)
    return ('Y（混合）' if m.group(1).startswith('Y（混合') else m.group(1)) if m else '?'


exp = {b[0]: (exp_code(b[4], 'v2 监管预期'), exp_code(b[5], '手册预期')) for b in body}
print('预期（监管 v2 / 手册）:', dict(Counter(e[0] for e in exp.values())), dict(Counter(e[1] for e in exp.values())))
for layer in ('原答', 'CEO最终'):
    rs = [rows[(u, layer)] for u in units]
    act = sum(r['行动分'] for r in rs if isinstance(r['行动分'], int))
    basis = [r['依据分'] for r in rs]
    bden = sum(isinstance(b, int) for b in basis); bsum = sum(b for b in basis if isinstance(b, int))
    print(f'{layer}: 行动分 {act}/48，依据分 {bsum}/{bden}（待复核 {48 - bden}），'
          f'R判定 {dict(Counter(r["R判定"] for r in rs))}，PH判定 {dict(Counter(r["PH判定"] for r in rs))}，'
          f'需组员定 {sum(bool(r["需组员定"]) for r in rs)}')
    print('   行动分 0:', [r['unit'] for r in rs if r['行动分'] == 0])
    print('   依据分 0:', [(r['unit'], r['R判定'], r['PH判定']) for r in rs if r['依据分'] == 0])
    print('   待复核:', [(r['unit'], r['R判定'], r['PH判定']) for r in rs if not isinstance(r['依据分'], int)])
    if layer == 'CEO最终':
        print('   C/O', dict(Counter(r['CO'] for r in rs)), '自标', dict(Counter(r['CEO自标'] for r in rs)),
              '出入', [r['unit'] for r in rs if (r['CO'], r['CEO自标']) not in (('C', 'CONFIRM'), ('O', 'OVERRIDE'))])
print('原答与 CEO 层 R判定不同:', [u for u in units if rows[(u, '原答')]['R判定'] != rows[(u, 'CEO最终')]['R判定']])
print('原答与 CEO 层 PH判定不同:', [u for u in units if rows[(u, '原答')]['PH判定'] != rows[(u, 'CEO最终')]['PH判定']])
print('原答与 CEO 层分数不同:', [u for u in units if (rows[(u, '原答')]['行动分'], rows[(u, '原答')]['依据分'])
                               != (rows[(u, 'CEO最终')]['行动分'], rows[(u, 'CEO最终')]['依据分'])])
# 手册补缺：监管 N 且手册 Y / Y（混合）
fill = [u for u in units if exp[u][0] == 'N' and exp[u][1].startswith('Y')]
print('监管 N、手册 Y 的单元', len(fill), fill)
for layer in ('原答', 'CEO最终'):
    print(f'   其中 {layer} PH=OK:', [u for u in fill if rows[(u, layer)]['PH判定'] == 'OK'])
print('需组员定:', [(r['unit'], r['layer'], r['问题']) for r in (rows[(u, l)] for u in units for l in ('原答', 'CEO最终')) if r['需组员定']])
print('例子候选:', [(r['unit'], r['layer']) for r in (rows[(u, l)] for u in units for l in ('原答', 'CEO最终')) if r.get('例子候选')])
