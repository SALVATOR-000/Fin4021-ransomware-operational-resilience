# -*- coding: utf-8 -*-
"""Build the Lan Tidal run package (version A) from the frozen whitelist.

Usage: python3 -I build_lantidal_package.py <project dir> <pdf2txt binary> <package dir> [pdf2png binary]
- sources/pdf: byte-identical copies of the 19 frozen files, named by exercise ID + title.
- sources/text: text versions (PDF text layer, one block per PDF page). R05 is a scan with
  no text layer, so its text version is the OCR transcription kept beside the scan.
- cards/, prompts/: copied verbatim from the approved script (line ranges below).
"""
import sys, os, re, json, shutil, hashlib, subprocess

PROJ, PDF2TXT, PKG = sys.argv[1:4]
PDF2PNG = sys.argv[4] if len(sys.argv) > 4 else None
SRC = os.path.join(PROJ, 'Primary source', '原文')
SCRIPT = os.path.join(PROJ, '岚汐银行-72小时勒索软件桌面推演.txt')

# (exercise ID, role-facing title, version line, frozen file name)
W = [
 ('R01', 'Cap. 653 Protection of Critical Infrastructures (Computer Systems) Ordinance', 'e-Legislation verified copy, version date 2026-09-10',
  'L1 Cap. 653 Protection of Critical Infrastructures (Computer Systems) Ordinance (2026-09-10 版, EN, 电子法例经核证整章).pdf'),
 ('R02', 'OCCICS Code of Practice (Generic)', 'Version 1.0, 2026-01-01', 'L2 OCCICS Code of Practice v1.0 (2026-01-01, EN).pdf'),
 ('R03', 'HKMA Sectoral Code of Practice for Designated AIs under Cap. 653', 'dated 2026-06-02', 'H7 HKMA Code of Practice for Designated AIs under Cap. 653 (2026-06-02, EN).pdf'),
 ('R04', 'HKMA SPM TM-C-1 Supervisory Approach on Cyber Risk Management', 'V.1, 2024-11-29', 'H3 HKMA SPM TM-C-1 Supervisory Approach on Cyber Risk Management (2024-11-29, EN).pdf'),
 ('R05', 'HKMA circular Incident response and management procedures', '2010-06-22, scanned original', 'H4 HKMA 通函 Incident response and management procedures (2010-06-22, EN, 扫描件).pdf'),
 ('R06', 'HKMA SPM OR-2 Operational Resilience', 'V.1, 2022-05-31', 'H1 HKMA SPM OR-2 Operational Resilience (EN).pdf'),
 ('R07', 'HKMA SPM TM-G-2 Business Continuity Planning', 'V.2, 2022-05-31', 'H15 HKMA SPM TM-G-2 Business Continuity Planning (2022-05-31, EN).pdf'),
 ('R08', 'HKMA SPM TM-G-1 General Principles for Technology Risk Management', 'V.1, 2003-06-24', 'H2 HKMA SPM TM-G-1 General Principles for Technology Risk Management (EN).pdf'),
 ('R09', 'HKMA SPM TM-E-1 Risk Management of E-banking', 'V.4, 2024-10-25', 'H16 HKMA SPM TM-E-1 Risk Management of E-banking (2024-10-25, EN).pdf'),
 ('R10', 'Cap. 486 Personal Data (Privacy) Ordinance', 'e-Legislation verified copy, version date 2022-10-01', 'L6 Cap. 486 Personal Data (Privacy) Ordinance (2022-10-01 版, EN, 电子法例经核证整章).pdf'),
 ('R11', 'PCPD Guidance on Data Breach Handling and Data Breach Notifications', 'June 2023', 'H10 PCPD Guidance on Data Breach Handling and Data Breach Notifications (2023-06, EN).pdf'),
 ('R12', 'HKMA SPM SA-2 Outsourcing', 'V.1, 2001-12-28', 'H17 HKMA SPM SA-2 Outsourcing (2001-12-28, EN).pdf'),
 ('R13', 'HKMA circular Operational Resilience - Sustaining and Uplifting', '2026-06-01', 'H18 HKMA 通函 Operational Resilience Sustaining and Uplifting (2026-06-01, EN).pdf'),
 ('R14a', 'HKMA circular Good practices for operational resilience', '2026-04-01, circular', 'H19 HKMA 通函 Good practices for addressing vulnerabilities related to operational resilience (2026-04-01, EN).pdf'),
 ('R14b', 'HKMA circular Good practices for operational resilience - Annex', '2026-04-01, annex to R14a', 'H19 HKMA 通函 Good practices for addressing vulnerabilities related to operational resilience - Annex (2026-04-01, EN).pdf'),
 ('R16a', 'PCPD Data Breach Notification Form', 'Revised 06/2023', 'H13 PCPD Data Breach Notification Form (EN).pdf'),
 ('R16b', 'HKMA circular Customer Data Protection', '2014-10-14', 'H9 HKMA 通函 Customer Data Protection (2014-10-14, EN).pdf'),
 ('R16c', 'Cap. 455 Organized and Serious Crimes Ordinance', 'e-Legislation verified copy, version date 2025-09-19', 'L3 Cap. 455 Organized and Serious Crimes Ordinance (2025-09-19 版, EN, 电子法例经核证整章).pdf'),
 ('R16d', 'Cap. 575 United Nations (Anti-Terrorism Measures) Ordinance', 'e-Legislation verified copy, version date 2019-06-20', 'L4 Cap. 575 United Nations (Anti-Terrorism Measures) Ordinance (2019-06-20 版, EN, 电子法例经核证整章).pdf'),
]
OCR_R05 = 'H4 HKMA 通函 Incident response and management procedures (2010-06-22, OCR 文字版).md'

for d in ('sources/pdf', 'sources/text', 'sources/scan_images', 'cards', 'prompts', 'facilitator'):
    os.makedirs(os.path.join(PKG, d), exist_ok=True)

sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
rows = []
for rid, title, ver, fn in W:
    base = f'{rid} {title}'
    pdf = os.path.join(PKG, 'sources/pdf', base + '.pdf')
    shutil.copyfile(os.path.join(SRC, fn), pdf)
    assert sha(pdf) == sha(os.path.join(SRC, fn))
    txt = os.path.join(PKG, 'sources/text', base + '.txt')
    tmp = txt + '.tmp'
    out = subprocess.run([PDF2TXT, pdf, tmp], capture_output=True, text=True).stdout
    m = re.search(r'of (\d+); empty: \[(.*?)\]', out)
    pages, empty = int(m.group(1)), [x for x in m.group(2).split(',') if x.strip()]
    head = f'[Document ID: {rid}] [Title: {title}] [Version: {ver}] [PDF pages: {pages}]\n'
    if rid == 'R05':
        body = open(os.path.join(SRC, OCR_R05), encoding='utf-8').read()
        body = body[body.index('## PDF page 1'):]
        body = re.sub(r'(?m)^>.*\n?', '', body)                       # letterhead footer notes
        body = re.sub(r'(?m)^## PDF page (\d+)\s*$', r'=== PDF page \1 ===', body)
        body = re.sub(r'(?m)^#{2,4}\s*', '', body).replace('  \n', '\n')  # markdown heading marks / hard breaks
        head += ('[This PDF is a scan with no text layer. The text below is an OCR transcription made for searching; '
                 'paragraph wrapping is normalised. The PDF is the authoritative copy: check any quotation against the PDF.]\n')
        kind = 'OCR transcription (scan has no text layer)'
    else:
        body = open(tmp, encoding='utf-8').read()
        head += '[Text layer of the PDF with the same name, one block per PDF page. The PDF is the authoritative copy.]\n'
        kind = 'PDF text layer' + (f'; empty pages: {",".join(empty)}' if empty else '')
    os.remove(tmp)
    open(txt, 'w', encoding='utf-8').write(head + '\n' + body.strip('\n') + '\n')
    rows.append(dict(rid=rid, title=title, ver=ver, frozen=fn, pdf=os.path.basename(pdf), txt=os.path.basename(txt),
                     pages=pages, sha=sha(pdf), txt_sha=sha(txt), kind=kind, size=os.path.getsize(pdf)))

# page images for scanned documents without a text layer (R05)
scans = []
if PDF2PNG:
    for r in rows:
        if r['kind'].startswith('OCR'):
            subprocess.run([PDF2PNG, os.path.join(PKG, 'sources/pdf', r['pdf']), os.path.join(PKG, 'sources/scan_images'), r['rid'], '1100'], check=True, capture_output=True)
scans = sorted(os.listdir(os.path.join(PKG, 'sources/scan_images')))

# role-facing manifest (English); roles see the same information through the list_sources tool
L = ['# Allowed source manifest (version A)', '',
     'These are the only documents a role may use. Roles reach them through the source tools (list_sources, search, read_page, view_scan_page).',
     'Text versions mark each page as `=== PDF page N ===`. The PDF is the authoritative copy.', '',
     '| Document ID | Title | Version | PDF pages | File name (pdf/ and text/) | Text version |', '|---|---|---|---|---|---|']
for r in rows:
    L.append(f"| {r['rid']} | {r['title']} | {r['ver']} | {r['pages']} | {r['rid']} {r['title']} | {r['kind']} |")
L += ['', 'Scan images (scan_images/): ' + ', '.join(scans)]
open(os.path.join(PKG, 'sources', 'SOURCE_MANIFEST.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# cards and prompts, verbatim from the approved script
S = open(SCRIPT, encoding='utf-8').read().split('\n')
ln = lambda a, b: '\n'.join(S[a - 1:b]) + '\n'
for i in range(8):
    a = 69 + i * 5
    assert S[a - 1].startswith(f'C0{i + 1} ·'), S[a - 1][:20]
    open(os.path.join(PKG, 'cards', f'C0{i + 1}.txt'), 'w', encoding='utf-8').write(ln(a, a + 4))
assert S[109].startswith('• Q25')
open(os.path.join(PKG, 'cards', 'Q25 (after C08 is locked).txt'), 'w', encoding='utf-8').write(ln(110, 110))
for name, a, b, first in [('common', 114, 148, 'You are taking part'), ('SEC', 150, 156, 'You are SEC'), ('LC', 158, 165, 'You are LC'),
                          ('COM', 167, 173, 'You are COM'), ('CEO', 175, 182, 'You are the CEO'), ('CEO wrap-up (after each card)', 184, 200, 'Using this card')]:
    assert S[a - 1].startswith(first), (name, S[a - 1][:30])
    open(os.path.join(PKG, 'prompts', name + '.txt'), 'w', encoding='utf-8').write(ln(a, b))
# reading note (script section 七) and the English handoff format
i0 = next(n for n, l in enumerate(S) if l.startswith('Reading note. '))
i1 = next(n for n in range(i0, len(S)) if S[n].strip() == '')
open(os.path.join(PKG, 'prompts', 'reading note (after the common prompt).txt'), 'w', encoding='utf-8').write('\n'.join(S[i0:i1]) + '\n')
s0 = next(l for l in S if l.startswith('You are taking part in a simulated tabletop exercise run by a facilitator.'))
open(os.path.join(PKG, 'prompts', 'system prompt (in the role definition).txt'), 'w', encoding='utf-8').write(s0 + '\n')
open(os.path.join(PKG, 'facilitator', 'handoff format.txt'), 'w', encoding='utf-8').write(
    'Handoff entries are written in English. All times are Hong Kong time (HKT).\n\n'
    'Every entry:\n'
    'Upstream unit | Final action | Owner | HKT time or trigger | Recipient and channel | '
    'Status (executed in simulation / scheduled / not executed / cannot be verified)\n\n'
    'Added to every LC handoff (C04, C07, C08):\n'
    'C01 awareness time (HKT) | Designation status | Actual notification: time (HKT), channel, form used, receipt status\n\n'
    'Added to the C08 LC handoff:\n'
    'Production changes actually executed in this run: upstream unit | change | system | HKT time (or "none")\n')
json.dump(rows, open(os.path.join(PKG, 'package.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(PKG, '运行包校验.sha256'), 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(f"{r['sha']}  sources/pdf/{r['pdf']}\n")
    for r in rows:
        f.write(f"{r['txt_sha']}  sources/text/{r['txt']}\n")
    for d in ('sources/scan_images', 'cards', 'prompts', 'facilitator'):
        for fn in sorted(os.listdir(os.path.join(PKG, d))):
            f.write(sha(os.path.join(PKG, d, fn)) + f'  {d}/{fn}\n')
    f.write(sha(os.path.join(PKG, 'sources', 'SOURCE_MANIFEST.md')) + '  sources/SOURCE_MANIFEST.md\n')
for r in rows:
    print(r['rid'], r['pages'], r['kind'], '|', r['title'][:50])
