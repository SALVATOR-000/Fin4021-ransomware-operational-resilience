import json, glob, os, re, sys, collections
from datetime import datetime, timezone, timedelta
P, OUT = sys.argv[1], sys.argv[2]
HKT = timezone(timedelta(hours=8))
EMAIL = re.compile(r'[\w.+-]+@gmail\.com')
SR = re.compile(r'<system-reminder[^>]*>.*?</system-reminder[^>]*>', re.S)
def hkt(s):
    try: return datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(HKT).strftime('%Y-%m-%d %H:%M:%S')
    except Exception: return '?'
def clean(t): return EMAIL.sub('[email redacted]', SR.sub('', t or '')).strip()
def load(f):
    out=[]
    for l in open(f, encoding='utf-8'):
        try: r=json.loads(l)
        except Exception: continue
        if r.get('type') in ('user','assistant'): out.append(r)
    return out
def tool_line(b, full):
    i=b.get('input') or {}; n=b.get('name','?')
    if n=='Bash': s=(i.get('description') or '')+' | '+(i.get('command') or '')
    elif n in ('Read','Write','Edit','NotebookEdit'): s=i.get('file_path','')
    elif n=='Agent': s='subagent_type='+str(i.get('subagent_type'))+' | '+str(i.get('description'))+' | prompt: '+str(i.get('prompt',''))
    else: s=json.dumps(i, ensure_ascii=False)
    lim = 20000 if (full or n in ('Agent','SendMessage','AskUserQuestion')) else 400
    s=clean(s)
    if len(s)>lim: s=s[:lim]+' …[truncated, %d chars in all]'%len(s)
    return '`[tool call: %s]` %s' % (n, s)
def render(recs, title, meta_lines, role_mode):
    lines=['# '+title,'']+meta_lines+['']
    turn=0; st=collections.Counter(); models=collections.Counter()
    for r in recs:
        m=r.get('message') or {}; c=m.get('content'); t=hkt(r.get('timestamp',''))
        if r['type']=='user':
            parts=[]
            if isinstance(c,str): parts=[('text',c)]
            elif isinstance(c,list):
                for b in c:
                    if not isinstance(b,dict): continue
                    if b.get('type')=='text': parts.append(('text',b.get('text','')))
                    elif b.get('type')=='tool_result': st['tool results omitted']+=1
                    elif b.get('type')=='image': parts.append(('text','[image attachment: not included]')); st['images not included']+=1
            for _,x in parts:
                x=clean(x)
                if not x: st['system-only inputs omitted']+=1; continue
                if r.get('isMeta') and not x.startswith('The coordinator sent a message while you were working:'): st['harness (isMeta) inputs omitted']+=1; continue
                if r.get('isCompactSummary') or x.startswith('This session is being continued from a previous conversation'):
                    lines += ['','---','### CONTEXT SUMMARY inserted by Claude Code after compaction (%s HKT) — not typed by the user'%t,'',x,'']; st['compaction summaries']+=1; continue
                turn+=1
                who = 'INPUT from facilitator session' if role_mode else 'USER'
                lines += ['','---','### Turn %d — %s (%s HKT)'%(turn,who,t),'',x,'']
        else:
            mdl=m.get('model') or '?'; models[mdl]+=1
            if isinstance(c,list):
                for b in c:
                    if not isinstance(b,dict): continue
                    if b.get('type')=='text' and clean(b.get('text','')):
                        lines += ['','**%s (%s, %s HKT)**'%('ROLE OUTPUT' if role_mode else 'CLAUDE', mdl, t),'',clean(b['text']),'']; st['assistant text outputs']+=1
                    elif b.get('type')=='tool_use' and b.get('name')=='SubagentHandback':
                        lines += ['','**%s (%s, %s HKT)**'%('ROLE OUTPUT returned to the facilitator' if role_mode else 'HANDBACK', mdl, t),'',clean(str((b.get('input') or {}).get('message',''))),'']; st['handback outputs']+=1
                    elif b.get('type')=='tool_use': lines += [tool_line(b, role_mode),'']; st['tool calls']+=1
                    elif b.get('type')=='thinking': st['thinking blocks omitted']+=1
    return lines, turn, st, models
sessions=[]
for f in glob.glob(P+'/*.jsonl'):
    recs=load(f)
    if not recs: continue
    sessions.append((recs[0].get('timestamp',''), f, recs))
sessions.sort()
idx=['# Claude Code transcripts: index','',
 'Source: the Claude Code session files for this project (`~/.claude/projects/-Users-…-FIN-4021-Group-Project/*.jsonl` and their `subagents/` folders), converted by `conv.py` (included). Times are Hong Kong time.','',
 'What each file contains: every message typed by the user, every visible text reply by Claude, and one line per tool call. Role-agent files also show the full input of each tool call. Not included: hidden reasoning ("thinking") blocks, harness-injected system reminders, and the raw results returned by tools (file contents, command output, source pages); the files those results came from are in the evidence package. Email addresses are redacted.','',
 '## Main sessions','','| ID | File | Session ID | First to last record (HKT) | Models | User turns | Claude text outputs | Tool calls | Sub-agents |','|---|---|---|---|---|---|---|---|---|']
sub_idx=['','## Sub-agent sessions (role agents and helper agents)','','| ID | File | Parent | Agent type | Working folder | First to last record (HKT) | Models | Effort | Inputs | Outputs | Tool calls |','|---|---|---|---|---|---|---|---|---|---|---|']
notes=[]
for n,(t0,f,recs) in enumerate(sessions,1):
    sid=os.path.basename(f)[:-6]; d=f[:-6]
    title='?'
    try: title=json.load(open(d+'/custom-title.json')).get('customTitle','?')
    except Exception: pass
    subs=sorted(glob.glob(d+'/subagents/agent-*.jsonl'), key=lambda x:(load(x) or [{}])[0].get('timestamp',''))
    name='S%02d_%s_%s.md'%(n, hkt(t0)[:10], sid[:8])
    meta=['- Session ID: `%s`'%sid,'- Title in Claude Code: %s'%title,'- First record: %s HKT; last record: %s HKT'%(hkt(recs[0].get('timestamp','')),hkt(recs[-1].get('timestamp',''))),'- Client version: %s'%recs[0].get('version','?')]
    lines,turn,st,models=render(recs,'Session S%02d (main session)'%n,meta,False)
    lines[2+len(meta):2+len(meta)]=['- Models: '+', '.join('%s (%d messages)'%kv for kv in models.items()),'- Counts: '+'; '.join('%s %d'%kv for kv in st.items())]
    open(os.path.join(OUT,name),'w',encoding='utf-8').write('\n'.join(lines)+'\n')
    idx.append('| S%02d | [%s](%s) | `%s` | %s to %s | %s | %d | %d | %d | %d |'%(n,name,name.replace(' ','%20'),sid[:8],hkt(recs[0].get('timestamp',''))[5:16],hkt(recs[-1].get('timestamp',''))[5:16],', '.join(models),turn,st['assistant text outputs'],st['tool calls'],len(subs)))
    for k,sf in enumerate(subs,1):
        srecs=load(sf)
        if not srecs: notes.append('S%02d sub-agent file %s has no user or assistant records.'%(n,os.path.basename(sf))); continue
        aid=os.path.basename(sf)[6:-6]; am={}
        try: am=json.load(open(sf[:-6]+'.meta.json'))
        except Exception: pass
        atype=am.get('agentType') or am.get('subagent_type') or '?'
        cwd=srecs[0].get('cwd','').split('FIN 4021 Group Project')[-1].strip('/') or '(project root)'
        sname='S%02d-A%02d_%s_%s.md'%(n,k,re.sub(r'[^A-Za-z0-9-]','',atype) or 'agent',aid[:8])
        sysp=''
        for l in open(sf,encoding='utf-8'):
            if '"prompt_snapshot"' in l:
                try:
                    a=json.loads(l).get('attachment') or {}; sp=a.get('systemPrompt')
                    sysp=clean('\n\n'.join(sp) if isinstance(sp,list) else str(sp or ''))
                    break
                except Exception: pass
        smeta=['- Parent session: S%02d (`%s`)'%(n,sid),'- Effort setting recorded for this agent: %s (model picked: %s)'%(am.get('effort','not recorded'),am.get('pickedEffortModel','not recorded')),'- Agent ID: `%s`'%aid,'- Agent type: %s'%atype,'- Agent metadata: `%s`'%json.dumps(am,ensure_ascii=False)[:600],'- Working folder at start: %s'%cwd,'- First record: %s HKT; last record: %s HKT'%(hkt(srecs[0].get('timestamp','')),hkt(srecs[-1].get('timestamp','')))]
        sl,sturn,sst,smodels=render(srecs,'Session S%02d-A%02d (sub-agent: %s)'%(n,k,atype),smeta,True)
        if sysp: sl += ['','---','## System prompt given to this agent (as recorded in the session file)','',sysp[:12000],'']
        sl[2+len(smeta):2+len(smeta)]=['- Models: '+', '.join('%s (%d messages)'%kv for kv in smodels.items()),'- Counts: '+'; '.join('%s %d'%kv for kv in sst.items())]
        open(os.path.join(OUT,sname),'w',encoding='utf-8').write('\n'.join(sl)+'\n')
        sub_idx.append('| S%02d-A%02d | [%s](%s) | S%02d | %s | %s | %s to %s | %s | %s | %d | %d | %d |'%(n,k,sname,sname,n,atype,cwd,hkt(srecs[0].get('timestamp',''))[5:16],hkt(srecs[-1].get('timestamp',''))[5:16],', '.join(smodels),am.get('effort','n/r'),sturn,sst['assistant text outputs']+sst['handback outputs'],sst['tool calls']))
open(os.path.join(OUT,'00 INDEX.md'),'w',encoding='utf-8').write('\n'.join(idx+sub_idx+['','## Conversion notes','']+['- '+x for x in notes])+'\n')
print('\n'.join(idx[9:]+sub_idx[4:])); print(notes)
