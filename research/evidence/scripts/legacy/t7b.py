import requests,json,time,re,itertools,sys
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/'
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
out={}
for t,par in [('0031A6DTPH2.px',['0','1','2'])]:
    time.sleep(3)
    q={'query':[{'code':'Geographic Location','selection':{'filter':'all','values':['*']}},{'code':'Parameter','selection':{'filter':'item','values':par}}],'response':{'format':'json-stat2'}}
    p=s.post(B+t,json=q,timeout=180); print(t,p.status_code,len(p.content))
    if p.status_code!=200: print(p.text[:500]); continue
    d=p.json(); json.dump(d,open(f'{sys.argv[1]}/{t}.json','w'))
    continue
    print(d['id'],d['size'])
    g=d['dimension']['Geographic Location']['category']; lab=g['label']; ix=g['index']
    order=sorted(ix,key=ix.get); pdim=d['dimension']['Parameter']['category']; pl=[pdim['label'][k] for k in sorted(pdim['index'],key=pdim['index'].get)]
    print(pl)
    np_=d['size'][d['id'].index('Parameter')]; firstgeo=d['id'].index('Geographic Location')==0
    for i,k in enumerate(order):
        if re.search(r'^\W*(Capas|Bamban|Mabalacat|City of Mabalacat|Tarlac|Pampanga)\b',lab[k].strip(),re.I) or 'Mabalacat' in lab[k]:
            v=[d['value'][i*np_+j] for j in range(np_)]
            print(repr(k),repr(lab[k]),v)
