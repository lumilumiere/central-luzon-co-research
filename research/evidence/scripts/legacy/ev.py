import json,re,sys
f=sys.argv[1]; pats=sys.argv[2:]
rows=[]
for ln,l in enumerate(open(f,encoding='utf8')):
    try:j=json.loads(l)
    except: continue
    m=j.get('message') or {}
    c=m.get('content')
    if m.get('role')!='user' or not isinstance(c,list): continue
    for b in c:
        if isinstance(b,dict) and b.get('type')=='tool_result':
            t=b.get('content'); t=''.join(x.get('text','') for x in t if isinstance(x,dict)) if isinstance(t,list) else str(t)
            for p in pats:
                for mm in re.finditer(p,t):
                    a=max(0,mm.start()-int(120)); e=min(len(t),mm.end()+int(220))
                    print(f'[L{ln} /{p}/] {j.get("timestamp","")} ',t[a:e].replace('\n',' | ')); break
