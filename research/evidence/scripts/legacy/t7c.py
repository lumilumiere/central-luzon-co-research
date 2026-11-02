import json,re,sys
for t in ['0221A6DLPD0.px','0031A6DTPH2.px']:
    d=json.load(open(f'{sys.argv[1]}/{t}.json')) if __import__('os').path.exists(f'{sys.argv[1]}/{t}.json') else None
    if not d: print('missing',t); continue
    val=d['value']; print(t,type(val),len(val),d['id'],d['size'],d.get('status') and list(d['status'].items())[:6])
    g=d['dimension']['Geographic Location']['category']; lab=g['label']; ix=g['index']
    print(type(ix), list(ix.items())[:4] if isinstance(ix,dict) else ix[:4])
    order=sorted(ix,key=ix.get) if isinstance(ix,dict) else ix
    n=d['size'][1]
    get=(lambda k:val.get(str(k))) if isinstance(val,dict) else (lambda k:val[k] if k<len(val) else 'OOR')
    for i,k in enumerate(order):
        l=lab[k].strip()
        if re.search(r'(^|\W)(Capas|Bamban|Mabalacat|Tarlac|Pampanga)(\W|$)',l,re.I) and not re.search(r'^(Tarlac)$',l) or l in('Tarlac','Pampanga'):
            print(i,repr(k),repr(l),[get(i*n+j) for j in range(n)])
