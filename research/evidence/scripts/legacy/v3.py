import sys,json,re,requests,time,hashlib
d,e=sys.argv[1:3]
j=json.load(open(f'{d}/0221A6DLPD0.px.json',encoding='utf8')); lab=j['dimension']['Geographic Location']['category']['label']
pick={k:v for k,v in lab.items() if re.search('Angeles',v,re.I)}; print(pick,len(lab))
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
if pick:
    r=s.post('https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px',json={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':list(pick)}}],'response':{'format':'csv'}},timeout=120); print(r.status_code,r.text.splitlines()[1:] if r.ok else r.text[:200])
Q='[out:json][timeout:100];way["highway"~"^(motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|tertiary_link|unclassified|residential|living_street|road)$"](15.16,120.24,15.43,120.64);out skel;'
J=None
for ep in ['https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.private.coffee/api/interpreter']:
    try:
        r=s.post(ep,data={'data':Q},timeout=110); print(ep,r.status_code,len(r.content))
        if r.status_code==200 and r.content[:1]==b'{': J=r.json(); break
    except Exception as x: print(ep,type(x).__name__)
if J:
    open(f'{e}/osm_ways_skel.json','wb').write(r.content); print(J['osm3s'],hashlib.sha256(r.content).hexdigest())
    p={}
    def f(x):
        p.setdefault(x,x)
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    for w in J['elements']:
        for b in w['nodes'][1:]: p[f(b)]=f(w['nodes'][0])
    sz={}
    for w in J['elements']:
        k=f(w['nodes'][0]); sz[k]=sz.get(k,0)+1
    v=sorted(sz.values(),reverse=True); print('ways',len(J['elements']),'comps',len(v),v[:5],round(v[0]/sum(v),4))
try:
    q=s.get('https://data.humdata.org/api/3/action/package_show?id=2020-census-popn-by-sex-age-group-and-mun-admin3',timeout=40); print(q.status_code)
    t=q.json()['result']; print({k:str(t.get(k))[:220] for k in ['title','dataset_source','dataset_date','last_modified','license_title','data_update_frequency']},[(x['name'],x.get('size'),x.get('last_modified')) for x in t['resources']])
except Exception as x: print(repr(x)[:200])
