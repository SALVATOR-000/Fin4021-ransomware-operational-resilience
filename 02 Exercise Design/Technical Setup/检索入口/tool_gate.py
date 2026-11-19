#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PreToolUse gate for exercise role agents: logs every tool call a role attempts and
blocks everything except the read-only source tools.

Usage (from the agent definition's hook): python3 -I tool_gate.py --role SEC
Reads the hook input (JSON) on stdin. Exit 0 = allow, exit 2 = block (stderr goes back to the role)."""
import sys, os, json, datetime, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('--role', required=True); a = ap.parse_args()
try:
    cfg = json.load(open(os.path.join(HERE, 'current_run.json'), encoding='utf-8'))
except Exception:
    cfg = {'run': 'UNCONFIGURED', 'log_dir': os.path.join(HERE, '..', '读取记录')}
try:
    d = json.load(sys.stdin)
except Exception:
    d = {}
name = d.get('tool_name', '')
ALLOWED_EXACT = {'SubagentHandback'}          # how a role hands its answer back to the facilitator
allowed = name.startswith('mcp__sources__') or name in ALLOWED_EXACT
rec = {'ts_hkt': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds'),
       'run': cfg.get('run'), 'role': a.role, 'agent_id': d.get('agent_id'), 'agent_type': d.get('agent_type'),
       'tool': name, 'decision': 'allow' if allowed else 'BLOCK',
       'input': {k: (v if isinstance(v, (int, float, bool)) else str(v)[:300]) for k, v in (d.get('tool_input') or {}).items()} if name != 'SubagentHandback' else '(answer text not copied here)'}
p = os.path.join(cfg.get('log_dir'), str(cfg.get('run')), f'{a.role}.tool_gate.jsonl')
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, 'a', encoding='utf-8') as f:
    f.write(json.dumps(rec, ensure_ascii=False) + '\n')
if not allowed:
    sys.stderr.write(f'Blocked: the tool {name} is not available to exercise roles. Use only the source tools (list_sources, search, read_page, view_scan_page).\n')
    sys.exit(2)
sys.exit(0)
