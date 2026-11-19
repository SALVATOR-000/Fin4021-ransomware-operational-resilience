#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract every quoted source passage from a run's sealed answers and check it against the frozen text versions.

Usage: python3 -I verify_quotes.py <run dir, e.g. 推演记录/A1> <sources/text dir> <output dir>

A "citation" is a passage in straight double quotes that sits in a line (or under a parent line) naming a
document ID (R01-R16d, PH01). The nearest page reference before the quote in that line, or in the parent line,
is taken as the stated page. Each quote is normalised (case, whitespace, quote marks, dashes, line-end hyphens)
and searched:
  OK            found on the stated page (or inside a stated range, or across a page break at its end)
  OK-NOPAGE     found in the stated document; no page was stated
  PAGE          found in the stated document but on another page
  DOC           not in the stated document but found in another one
  FRAGMENTS     quote contains an ellipsis; every fragment of 4+ words is found in the stated document
  NOT-FOUND     not found as written: check by hand
Quotes of more than 25 words are flagged. Standard library only.
"""
import sys, os, re, json, glob, csv

RUN, TEXT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[‐-―−]', '-', s)
    s = re.sub(r'-\s*\n\s*', '-', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


def squash(s):  # also ignore hyphens and spaces entirely (line-end hyphenation, OCR spacing)
    return re.sub(r'[\s\-]', '', s)


DOCS = {}
for fn in sorted(os.listdir(TEXT)):
    raw = open(os.path.join(TEXT, fn), encoding='utf-8').read()
    m = re.match(r'\[Document ID: ([^\]]+)\]', raw)
    if not m:
        continue
    parts = re.split(r'=== PDF page (\d+)[^=]*===', raw)
    pages = {int(parts[i]): norm(parts[i + 1]) for i in range(1, len(parts), 2)}
    DOCS[m.group(1)] = {'pages': pages, 'sq': {n: squash(t) for n, t in pages.items()}}
IDS = sorted(DOCS, key=len, reverse=True)
ID_RE = re.compile(r'\b(' + '|'.join(re.escape(i) for i in IDS) + r')\b')
PAGE_RE = re.compile(r'(?:PDF\s+)?(pp?|pages?)\.?\s*(\d+)(?:\s*(?:-|–|—|to|and)\s*(\d+))?', re.I)


def find(doc, q):
    """pages of `doc` where normalised quote q occurs (also across a page break)."""
    d = DOCS[doc]; sq = squash(q); hits = []
    ns = sorted(d['pages'])
    for n in ns:
        if q in d['pages'][n] or sq in d['sq'][n]:
            hits.append(n)
    if not hits:
        for a, b in zip(ns, ns[1:]):
            if sq in d['sq'][a] + d['sq'][b]:
                hits.append(a); hits.append(b)
    return sorted(set(hits))


def pages_stated(text):
    out = []
    for m in PAGE_RE.finditer(text):
        a = int(m.group(2)); b = int(m.group(3)) if m.group(3) else a
        if b < a or b - a > 20:
            b = a
        out.append((a, b))
    return out


rows = []
files = sorted(glob.glob(os.path.join(RUN, 'C0*', '*.raw.md'))) + sorted(glob.glob(os.path.join(RUN, 'C0*', 'CEO.final.md'))) + sorted(glob.glob(os.path.join(RUN, 'Q25', '*.md')))
for fp in files:
    card = os.path.basename(os.path.dirname(fp)); role = os.path.basename(fp).split('.')[0]
    kind = 'CEO final' if fp.endswith('CEO.final.md') else ('Q25' if card == 'Q25' else 'original')
    text = open(fp, encoding='utf-8').read()
    unit = None; parent_doc = None; parent_pages = []; parent_indent = -1
    for line in text.split('\n'):
        mu = re.match(r'\s*(?:#+\s*|UNIT\s+|\*\*)?(Q\d\d[ab])\b', line)
        if mu:
            unit = mu.group(1)
        indent = len(line) - len(line.lstrip(' '))
        ids_here = ID_RE.findall(line)
        if ids_here and indent <= max(parent_indent, 0) or (ids_here and not line.lstrip().startswith(('-', '*')) ):
            parent_doc = ids_here[0]; parent_pages = pages_stated(line); parent_indent = indent
        elif indent <= parent_indent and not ids_here and line.strip():
            if not line.lstrip().startswith('-'):
                parent_doc = None; parent_pages = []; parent_indent = -1
        for mq in re.finditer(r'"([^"\n]{12,})"', line):
            q = mq.group(1)
            if len(q.split()) < 3:
                continue
            before = line[:mq.start()]
            ids_b = ID_RE.findall(before)
            doc = ids_b[-1] if ids_b else (ids_here[0] if ids_here else (parent_doc if indent > parent_indent >= 0 or parent_doc else None))
            if not doc:
                continue
            pg = pages_stated(before[before.rfind(doc):] if doc in before else before) or (parent_pages if not ids_b else [])
            qn = norm(q).strip(' .,;:')
            words = len(q.split())
            frags = [f.strip(' .,;:') for f in re.split(r'\.\.\.|…|\[[^\]]*\]', qn) if len(f.split()) >= 4]
            hits = find(doc, qn)
            status, where = None, hits
            if hits:
                if not pg:
                    status = 'OK-NOPAGE'
                elif any(a - 0 <= h <= b + 1 for (a, b) in pg for h in hits):
                    status = 'OK'
                else:
                    status = 'PAGE'
            elif len(frags) >= 1 and (len(frags) > 1 or len(frags[0].split()) < len(qn.split())) and all(find(doc, f) for f in frags):
                status = 'FRAGMENTS'; where = sorted({h for f in frags for h in find(doc, f)})
            else:
                other = [d for d in DOCS if d != doc and find(d, qn)]
                status = 'DOC' if other else 'NOT-FOUND'; where = other
            rows.append({'file': os.path.relpath(fp, RUN), 'card': card, 'role': role, 'kind': kind, 'unit': unit or '', 'doc': doc,
                         'pages_stated': ';'.join(f'{a}' if a == b else f'{a}-{b}' for a, b in pg), 'status': status,
                         'found_on': ';'.join(map(str, where)), 'words': words, 'over25': words > 25, 'quote': q})

with open(os.path.join(OUT, 'citations.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
c = Counter(r['status'] for r in rows); ck = Counter((r['kind'], r['status']) for r in rows)
print('total', len(rows), dict(c)); print(dict(ck)); print('over 25 words', sum(r['over25'] for r in rows))
