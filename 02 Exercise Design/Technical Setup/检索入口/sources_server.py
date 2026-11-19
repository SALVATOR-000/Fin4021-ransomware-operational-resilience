#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read-only retrieval entry for the Lan Tidal tabletop exercise (MCP server, stdio).

A role agent gets ONLY this server's tools. The server reads nothing except the
text versions, the manifest and the scan images inside one sources directory,
and it appends every call to a log file.

Usage:  python3 -I sources_server.py --role SEC [--config <current_run.json>]
The config file (written by the facilitator before a run) holds:
  {"run": "A1", "sources": "<abs path to sources dir>", "log_dir": "<abs path>"}
Standard library only (Python 3.9+). Protocol: JSON-RPC 2.0, one message per line.
"""
import sys, os, re, json, base64, datetime, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--role', required=True)
ap.add_argument('--config', default=os.path.join(HERE, 'current_run.json'))
ARGS = ap.parse_args()
CFG = json.load(open(ARGS.config, encoding='utf-8'))
SOURCES, RUN, ROLE = CFG['sources'], CFG['run'], ARGS.role
LOG = os.path.join(CFG['log_dir'], RUN, f'{ROLE}.source_calls.jsonl')
os.makedirs(os.path.dirname(LOG), exist_ok=True)
HKT = datetime.timezone(datetime.timedelta(hours=8))
MAX_PAGES_PER_CALL = 6


def log(event, **kw):
    rec = {'ts_hkt': datetime.datetime.now(HKT).isoformat(timespec='seconds'), 'run': RUN, 'role': ROLE, 'pid': os.getpid(), 'event': event}
    rec.update(kw)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')


# ---- index: built once from <sources>/text; nothing else is ever opened ----
DOCS = {}   # doc_id -> {title, version, npages, pages: {n: raw text}, flat: {n: normalised text}, file}
for fn in sorted(os.listdir(os.path.join(SOURCES, 'text'))):
    if not fn.endswith('.txt'):
        continue
    raw = open(os.path.join(SOURCES, 'text', fn), encoding='utf-8').read()
    m = re.match(r'\[Document ID: ([^\]]+)\] \[Title: ([^\]]+)\] \[Version: ([^\]]+)\]', raw)
    if not m:
        continue
    parts = re.split(r'=== PDF page (\d+)[^=]*===', raw)
    pages = {int(parts[i]): parts[i + 1].strip('\n') for i in range(1, len(parts), 2)}
    DOCS[m.group(1)] = {'title': m.group(2), 'version': m.group(3), 'npages': max(pages) if pages else 0, 'pages': pages,
                        'flat': {n: re.sub(r'\s+', ' ', t) for n, t in pages.items()}, 'file': fn, 'note': raw.split('\n', 2)[1]}
SCANS = {}  # (doc_id, page) -> png path
scan_dir = os.path.join(SOURCES, 'scan_images')
if os.path.isdir(scan_dir):
    for fn in os.listdir(scan_dir):
        m = re.match(r'(\w+) page (\d+)\.png$', fn)
        if m:
            SCANS[(m.group(1), int(m.group(2)))] = os.path.join(scan_dir, fn)

TOOLS = [
    {'name': 'list_sources',
     'description': 'List the documents you are allowed to use: document ID, title, version, number of PDF pages.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'search',
     'description': ('Search the text versions of the allowed documents (case-insensitive). Line breaks inside a page are ignored, so a phrase can be '
                     'searched as written. Returns document ID, PDF page and a short snippet for each hit. A phrase that runs across a page break '
                     'will not match: search a shorter part of it.'),
     'inputSchema': {'type': 'object', 'properties': {
         'query': {'type': 'string', 'description': 'Words or phrase to find. With regex=true, a regular expression.'},
         'doc_id': {'type': 'string', 'description': 'Optional: limit the search to one document ID, e.g. R01.'},
         'regex': {'type': 'boolean', 'description': 'Treat query as a regular expression. Default false.'},
         'max_hits': {'type': 'integer', 'description': 'Maximum hits to return (default 40, at most 200).'}},
         'required': ['query'], 'additionalProperties': False}},
    {'name': 'read_page',
     'description': f'Read the text of one PDF page, or up to {MAX_PAGES_PER_CALL} consecutive pages, of an allowed document.',
     'inputSchema': {'type': 'object', 'properties': {
         'doc_id': {'type': 'string'}, 'page': {'type': 'integer', 'description': 'First PDF page.'},
         'page_to': {'type': 'integer', 'description': 'Optional last PDF page.'}},
         'required': ['doc_id', 'page'], 'additionalProperties': False}},
    {'name': 'view_scan_page',
     'description': ('View the image of one page of a scanned document. Only documents without a text layer have images (R05). Use it to check a '
                     'quotation against the scan.'),
     'inputSchema': {'type': 'object', 'properties': {'doc_id': {'type': 'string'}, 'page': {'type': 'integer'}},
                     'required': ['doc_id', 'page'], 'additionalProperties': False}},
]


def text(s):
    return {'content': [{'type': 'text', 'text': s}], 'isError': False}


def err(s):
    return {'content': [{'type': 'text', 'text': 'ERROR: ' + s}], 'isError': True}


def call(name, a):
    if name == 'list_sources':
        rows = [f'{d} | {v["title"]} | {v["version"]} | {v["npages"]} PDF pages' + (' | scanned: text is an OCR transcription, images via view_scan_page' if any(k[0] == d for k in SCANS) else '')
                for d, v in DOCS.items()]
        return text('Document ID | Title | Version | Pages\n' + '\n'.join(rows)), {'docs': len(rows)}
    if name == 'search':
        q = str(a.get('query', '')).strip()
        if not q:
            return err('empty query'), {}
        did = a.get('doc_id')
        if did and did not in DOCS:
            return err(f'unknown doc_id {did!r}; call list_sources'), {}
        try:
            pat = re.compile(q if a.get('regex') else re.escape(re.sub(r'\s+', ' ', q)).replace(r'\ ', r'\s*'), re.I)
        except re.error as e:
            return err(f'bad regular expression: {e}'), {}
        cap = max(1, min(int(a.get('max_hits') or 40), 200))
        hits, per_doc = [], {}
        for d, v in DOCS.items():
            if did and d != did:
                continue
            for n in sorted(v['flat']):
                t = v['flat'][n]
                for m in pat.finditer(t):
                    per_doc[d] = per_doc.get(d, 0) + 1
                    if len(hits) < cap:
                        s, e = max(0, m.start() - 90), min(len(t), m.end() + 90)
                        hits.append(f'{d} | PDF page {n} | …{t[s:e]}…')
        total = sum(per_doc.values())
        head = f'{total} hit(s) for {q!r}' + (f' in {did}' if did else '') + '. Hits per document: ' + (', '.join(f'{k}: {n}' for k, n in per_doc.items()) or 'none')
        if total > len(hits):
            head += f'. Showing the first {len(hits)}.'
        return text(head + '\n' + '\n'.join(hits)), {'hits': total, 'per_doc': per_doc}
    if name == 'read_page':
        did = a.get('doc_id')
        if did not in DOCS:
            return err(f'unknown doc_id {did!r}; call list_sources'), {}
        p1 = int(a.get('page')); p2 = int(a.get('page_to') or p1)
        v = DOCS[did]
        if p1 < 1 or p2 < p1 or p2 > v['npages']:
            return err(f'{did} has PDF pages 1-{v["npages"]}'), {}
        if p2 - p1 + 1 > MAX_PAGES_PER_CALL:
            return err(f'at most {MAX_PAGES_PER_CALL} pages per call'), {}
        out = [f'[{did}] {v["title"]} ({v["version"]})', v['note']]
        for n in range(p1, p2 + 1):
            out.append(f'=== PDF page {n} ===\n{v["pages"].get(n, "")}')
        return text('\n\n'.join(out)), {'pages': [p1, p2]}
    if name == 'view_scan_page':
        key = (a.get('doc_id'), int(a.get('page') or 0))
        if key not in SCANS:
            have = sorted(f'{d} p{p}' for d, p in SCANS)
            return err('no scan image for that document and page. Available: ' + (', '.join(have) or 'none')), {}
        data = base64.b64encode(open(SCANS[key], 'rb').read()).decode('ascii')
        return {'content': [{'type': 'text', 'text': f'[{key[0]}] scanned PDF page {key[1]}'},
                            {'type': 'image', 'data': data, 'mimeType': 'image/png'}], 'isError': False}, {'image': os.path.basename(SCANS[key])}
    return err(f'unknown tool {name!r}'), {}


def send(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + '\n')
    sys.stdout.flush()


log('server_start', sources=SOURCES, docs=sorted(DOCS), scans=len(SCANS))
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        msg = json.loads(line)
    except Exception:
        continue
    mid, method, params = msg.get('id'), msg.get('method'), msg.get('params') or {}
    if method == 'initialize':
        log('initialize', client=params.get('clientInfo'))
        send({'jsonrpc': '2.0', 'id': mid, 'result': {'protocolVersion': params.get('protocolVersion', '2024-11-05'),
              'capabilities': {'tools': {}}, 'serverInfo': {'name': 'lantidal-sources', 'version': '1.0'}}})
    elif method == 'tools/list':
        send({'jsonrpc': '2.0', 'id': mid, 'result': {'tools': TOOLS}})
    elif method == 'tools/call':
        name, a = params.get('name'), params.get('arguments') or {}
        try:
            res, info = call(name, a)
        except Exception as e:  # never crash on a bad call; report it to the caller and the log
            res, info = err(f'{type(e).__name__}: {e}'), {}
        log('call', tool=name, args=a, ok=not res.get('isError'), **info)
        send({'jsonrpc': '2.0', 'id': mid, 'result': res})
    elif method == 'ping':
        send({'jsonrpc': '2.0', 'id': mid, 'result': {}})
    elif mid is not None:
        send({'jsonrpc': '2.0', 'id': mid, 'error': {'code': -32601, 'message': f'method not found: {method}'}})
