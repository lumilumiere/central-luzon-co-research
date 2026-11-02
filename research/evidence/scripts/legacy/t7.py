import requests,json,time,re,sys,itertools
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/'
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
for t in ['0221A6DLPD0.px','0031A6DTPH2.px']:
    time.sleep(3)
    r=s.get(B+t,timeout=60); j=r.json(); print('\n###',t,r.status_code,j.get('title'))
    print(json.dumps(j)[:500])
    q=[]
    for v in j['variables']:
        ks=v.get('values') or []; tx=v.get('valueTexts') or []
        print(' var',{k:(val if not isinstance(val,list) else f'[{len(val)}] {val[:5]}') for k,val in v.items()})
        idx=[i for i,x in enumerate(tx) if re.search(r'(Capas|Bamban|Mabalacat)',x,re.I)]
        if idx:
            print(' matches',[(ks[i],tx[i]) for i in idx]); q.append({'code':v['code'],'selection':{'filter':'item','values':[ks[i] for i in idx]}})
    if not q: continue
    time.sleep(3)
    p=s.post(B+t,json={'query':q,'response':{'format':'json-stat2'}},timeout=120); print(' post',p.status_code,len(p.content)); 
    if p.status_code!=200: print(p.text[:400]); continue
    d=p.json(); ids=d['id']; val=d['value']; print(' source',d.get('source'),'updated',d.get('updated'),d.get('note'))
    cats=[[d['dimension'][i]['category']['label'][k] for k,_ in sorted(d['dimension'][i]['category']['index'].items(),key=lambda kv:kv[1])] for i in ids]
    for c,v in zip(itertools.product(*cats),val): print('  ',c,v)
