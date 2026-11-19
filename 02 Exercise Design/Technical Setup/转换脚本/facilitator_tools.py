#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Facilitator tools for the Lan Tidal tabletop runs (A1-A3, B1-B3).

The facilitator (the main Claude session) sends messages to the role agents by hand.
These tools keep that step checkable:
  build    write the exact text the facilitator intends to send to a role for a card
  collect  after the role has answered: check that the role received exactly that text,
           save the role's submitted answer byte-for-byte, and log times and checksums
  startup  report what a role agent loaded at start-up (attachments, model, effort)
Nothing here scores or edits an answer.  Standard library only; run with python3 -I.
"""
import sys, os, json, glob, hashlib, datetime, argparse

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REC = os.path.join(PROJ, '推演记录')
TRANSCRIPTS = os.path.expanduser('~/.claude/projects/-Users-zehaoliu-FIN-4021-Group-Project')
HKT = datetime.timezone(datetime.timedelta(hours=8))
ROLES = ('SEC', 'LC', 'COM', 'CEO')
sha = lambda b: hashlib.sha256(b).hexdigest()


def pkg_dir(run):
    return os.path.join(REC, '岚汐运行包（A版）' if run.startswith('A') or run.startswith('DRY') else '岚汐运行包（B版）')


def rd(path):
    return open(path, encoding='utf-8').read()


def block(path):
    return rd(path).rstrip('\n')


def run_dir(run, card=None):
    d = os.path.join(REC, run) if card is None else os.path.join(REC, run, card)
    os.makedirs(d, exist_ok=True)
    return d


def handoff_text(run, card, role):
    """Handoff entries for one role and card, written by the facilitator into <run>/<card>/handoff.<ROLE>.txt.
    No file means no handoff for that role on that card."""
    p = os.path.join(run_dir(run, card), f'handoff.{role}.txt')
    return block(p) if os.path.exists(p) else None


def build(run, card, role):
    P = pkg_dir(run)
    card_txt = block(os.path.join(P, 'cards', f'{card}.txt')) if card != 'Q25' else block(os.path.join(P, 'cards', 'Q25 (after C08 is locked).txt'))
    first = card == 'C01'
    parts = []
    if first:
        parts += [block(os.path.join(P, 'prompts', 'common.txt')),
                  block(os.path.join(P, 'prompts', 'reading note (after the common prompt).txt')),
                  block(os.path.join(P, 'prompts', f'{role}.txt'))]
    parts.append(card_txt)
    if role != 'CEO':
        h = handoff_text(run, card, role)
        parts.append(f'Facilitator handoff to {role} for {card}: none.' if h is None else f'Facilitator handoff to {role} for {card}:\n{h}')
    else:
        if card != 'Q25':
            for r in ('SEC', 'LC', 'COM'):
                rawp = os.path.join(run_dir(run, card), f'{r}.raw.md')
                missp = os.path.join(run_dir(run, card), f'{r}.missing.txt')
                if os.path.exists(rawp):
                    parts.append(f'Sealed {r} answer for {card}:\n<<<\n{rd(rawp)}\n>>>')
                elif os.path.exists(missp):
                    parts.append(f'Sealed {r} answer for {card}: MISSING. {block(missp)}')
                else:
                    sys.exit(f'no sealed answer or missing marker for {r} {card}')
            hs = []
            for r in ('SEC', 'LC', 'COM'):
                h = handoff_text(run, card, r)
                hs.append(f'{r}: none.' if h is None else f'{r}:\n{h}')
            parts.append(f'Facilitator handoffs given to the roles for {card}:\n' + '\n'.join(hs))
            parts.append(block(os.path.join(P, 'prompts', 'CEO wrap-up (after each card).txt')))
    msg = '\n\n'.join(parts)
    out = os.path.join(run_dir(run, card), f'input.{role}.txt')
    open(out, 'w', encoding='utf-8').write(msg)
    return out, msg


def find_transcript(agent_id):
    hits = glob.glob(os.path.join(TRANSCRIPTS, '*', 'subagents', f'agent-{agent_id}.jsonl'))
    if len(hits) != 1:
        sys.exit(f'transcript for agent {agent_id}: {len(hits)} found')
    return hits[0]


def load_rows(fp):
    return [json.loads(l) for l in open(fp, encoding='utf-8') if l.strip()]


def text_of(row):
    c = (row.get('message') or {}).get('content')
    if isinstance(c, str):
        return c
    if isinstance(c, list) and c and all(isinstance(b, dict) and b.get('type') == 'text' for b in c):
        return '\n'.join(b.get('text') or '' for b in c)
    return None


def turns(rows):
    """Each facilitator message with the SubagentHandback that answers it: list of (msg_row, msg_text, hb_row or None, hb_text or None)."""
    out, cur = [], None
    for n, r in enumerate(rows):
        if r.get('type') == 'user':
            t = text_of(r)
            if t is not None and not t.lstrip().startswith('<system-reminder>'):
                if cur is not None:
                    out.append(cur + (None, None))
                cur = (n, t)
        elif r.get('type') == 'assistant' and cur is not None:
            for b in (r.get('message') or {}).get('content') or []:
                if isinstance(b, dict) and b.get('type') == 'tool_use' and b.get('name') == 'SubagentHandback':
                    out.append(cur + (n, (b.get('input') or {}).get('message')))
                    cur = None
                    break
    if cur is not None:
        out.append(cur + (None, None))
    return out


def ts(row):
    return datetime.datetime.fromisoformat(row['timestamp'].replace('Z', '+00:00'))


def models_efforts(rows, a, b):
    models, efforts = set(), set()
    for r in rows[a:b + 1]:
        m = (r.get('message') or {}).get('model')
        if m:
            models.add(m)
        s = json.dumps(r, ensure_ascii=False)
        i = 0
        while True:
            i = s.find('"effort"', i)
            if i < 0:
                break
            efforts.add(s[i:i + 40].split(',')[0].split('}')[0])
            i += 8
    return sorted(models), sorted(efforts)


def collect(run, card, role, agent_id, turn_no, resumed=0):
    fp = find_transcript(agent_id)
    rows = load_rows(fp)
    T = turns(rows)
    if turn_no + resumed > len(T):
        sys.exit(f'{role}: only {len(T)} facilitator message(s) in the transcript, turn {turn_no + resumed} asked')
    mrow, mtext, hrow, htext = T[turn_no - 1]
    resume_rows = []
    if resumed:  # the turn was interrupted; the answer follows the last of `resumed` facilitator resume messages
        assert hrow is None, 'turn was answered; nothing to resume'
        for k in range(resumed):
            r_m, r_t, hrow, htext = T[turn_no + k]
            resume_rows.append({'row': r_m, 'received_hkt': ts(rows[r_m]).astimezone(HKT).isoformat(timespec='seconds'), 'text': r_t})
    intended = rd(os.path.join(run_dir(run, card), f'input.{role}.txt'))
    exact = mtext == intended
    contained = intended in mtext
    i = mtext.find(intended)
    wrapper = {'prefix': mtext[:i], 'suffix': mtext[i + len(intended):]} if contained and not exact else {}
    rec = {'run': run, 'card': card, 'role': role, 'agent_id': agent_id, 'turn': turn_no, 'transcript': fp,
           'message_row': mrow, 'received_hkt': ts(rows[mrow]).astimezone(HKT).isoformat(timespec='seconds'),
           'input_sha256': sha(intended.encode('utf-8')), 'input_received_exact': exact, 'input_contained_in_received': contained,
           'platform_wrapper': wrapper, 'resume_messages': resume_rows}
    if not contained:
        # show where the texts part, to make a deviation easy to describe
        k = next((j for j in range(min(len(mtext), len(intended))) if mtext[j] != intended[j]), min(len(mtext), len(intended)))
        rec['first_difference_at_char'] = k
        rec['intended_there'] = intended[max(0, k - 60):k + 60]
        rec['received_there'] = mtext[max(0, k - 60):k + 60]
    if hrow is None:
        rec['submitted'] = False
    else:
        raw = htext if isinstance(htext, str) else json.dumps(htext, ensure_ascii=False)
        name = 'CEO.final.md' if role == 'CEO' else f'{role}.raw.md'
        if card == 'Q25':
            name = f'{role}.Q25.raw.md'
        out = os.path.join(run_dir(run, card if card != 'Q25' else 'Q25'), name)
        if os.path.exists(out) and rd(out) != raw:
            sys.exit(f'{out} exists with different content; not overwriting')
        if not os.path.exists(out):  # a sealed answer is written once and then left read-only
            open(out, 'w', encoding='utf-8').write(raw)
            os.chmod(out, 0o444)
        d = (ts(rows[hrow]) - ts(rows[mrow])).total_seconds()
        models, efforts = models_efforts(rows, mrow, hrow)
        rec.update({'submitted': True, 'handback_row': hrow, 'submitted_hkt': ts(rows[hrow]).astimezone(HKT).isoformat(timespec='seconds'),
                    'answer_seconds': round(d), 'raw_file': os.path.relpath(out, PROJ), 'raw_sha256': sha(raw.encode('utf-8')),
                    'raw_chars': len(raw), 'models': models, 'efforts': efforts,
                    'source_calls': sum(1 for r in rows[mrow:hrow + 1] if r.get('type') == 'assistant' for b in ((r.get('message') or {}).get('content') or [])
                                        if isinstance(b, dict) and b.get('type') == 'tool_use' and str(b.get('name', '')).startswith('mcp__sources__')),
                    'other_tool_attempts': sorted({b.get('name') for r in rows[mrow:hrow + 1] if r.get('type') == 'assistant' for b in ((r.get('message') or {}).get('content') or [])
                                                   if isinstance(b, dict) and b.get('type') == 'tool_use'
                                                   and not str(b.get('name', '')).startswith('mcp__sources__') and b.get('name') != 'SubagentHandback'})})
    idx = os.path.join(run_dir(run), '记录索引.jsonl')
    prev = [json.loads(l) for l in open(idx, encoding='utf-8')] if os.path.exists(idx) else []
    prev = [p for p in prev if not (p['card'] == card and p['role'] == role)]
    with open(idx, 'w', encoding='utf-8') as f:
        for p in prev + [rec]:
            f.write(json.dumps(p, ensure_ascii=False) + '\n')
    return rec


def startup(agent_id):
    fp = find_transcript(agent_id)
    rows = load_rows(fp)
    att = []
    for r in rows:
        a = r.get('attachment')
        if isinstance(a, dict):
            att.append(a.get('type'))
    blob = '\n'.join(json.dumps(r, ensure_ascii=False) for r in rows)
    meta = json.load(open(fp[:-6] + '.meta.json')) if os.path.exists(fp[:-6] + '.meta.json') else {}
    return {'agent_id': agent_id, 'agent_type': meta.get('agentType'), 'picked_model': meta.get('pickedEffortModel'),
            'launched_with_defaults': meta.get('launchedWithDefaults'), 'attachment_types': sorted(set(t for t in att if t)),
            'has_instructions_attachment': 'instructions' in att, 'mentions_MEMORY.md': blob.count('MEMORY.md'),
            'mentions_预期': blob.count('监管侧预期'), 'mentions_PH01_file': blob.count('PH01 playbook')}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    b = sub.add_parser('build'); b.add_argument('run'); b.add_argument('card'); b.add_argument('role', choices=ROLES); b.add_argument('--show', action='store_true')
    c = sub.add_parser('collect'); c.add_argument('run'); c.add_argument('card'); c.add_argument('role', choices=ROLES); c.add_argument('agent_id'); c.add_argument('turn', type=int); c.add_argument('--resumed', type=int, default=0)
    s = sub.add_parser('startup'); s.add_argument('agent_id')
    a = ap.parse_args()
    if a.cmd == 'build':
        out, msg = build(a.run, a.card, a.role)
        print(f'{out} | {len(msg)} chars | sha256 {sha(msg.encode("utf-8"))}')
        if a.show:
            print('-----8<-----'); print(msg); print('-----8<-----')
    elif a.cmd == 'collect':
        print(json.dumps(collect(a.run, a.card, a.role, a.agent_id, a.turn, a.resumed), ensure_ascii=False, indent=1))
    elif a.cmd == 'startup':
        print(json.dumps(startup(a.agent_id), ensure_ascii=False, indent=1))
