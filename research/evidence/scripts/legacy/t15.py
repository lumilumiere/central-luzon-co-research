import requests,sys,re,time,json
import pandas as pd
d=sys.argv[1]
print(pd.read_excel(f'{d}/proj.xlsx',sheet_name='Metadata',header=None).to_string(max_colwidth=400)[:3500])
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/'
q={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':['0305409000']}}],'response':{'format':'px'}}
t=s.post(B+'0221A6DLPD0.px',json=q,timeout=120).content.decode('utf-8','replace'); i=t.find('NOTEX='); j=t.find('DATA='); n=re.sub(r'"\s*"','',t[i:j]); print(n[:3500])
time.sleep(3)
q={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':['0305409000','0306902000','0306904000']}}],'response':{'format':'csv'}}
print(s.post(B+'0031A6DTPH2.px',json=q,timeout=120).content.decode('utf-8','replace'))
d2=json.load(open(f'{d}/0031A6DTPH2.px.json')); lab=d2['dimension']['Geographic Location']['category']['label']
print('barangay rows',{m:sum(1 for k in lab if k.startswith(m) and not k.endswith('000')) for m in ['0305409','0306902','0306904']})
ad=pd.read_excel(f'{d}/cod_ab.xlsx',sheet_name='phl_admin4')
print('COD adm4',ad[ad.adm3_pcode.isin(['PH0305409','PH0306902','PH0306904'])].groupby('adm3_name').agg(n=('adm4_pcode','count'),km2=('area_sqkm','sum')).round(2).to_dict())
print('sample adm4',ad[ad.adm3_pcode=='PH0305409'][['adm4_name','adm4_pcode','area_sqkm']].head(3).to_string())
# Overpass: named corridors + drivable connectivity sample + admin relations
ep='https://overpass-api.de/api/interpreter'
def op(Q,to=100):
    for e in [ep,'https://maps.mail.ru/osm/tools/overpass/api/interpreter']:
        try:
            r=s.post(e,data={'data':Q},timeout=to); print(e,r.status_code,len(r.content))
            if r.status_code==200 and r.content[:1]==b'{': return r.json()
        except Exception as x: print(e,'ERR',type(x).__name__)
    return None
R=op('[out:json][timeout:90];rel["boundary"="administrative"]["name"~"^(Capas|Bamban|Mabalacat|City of Mabalacat|Mabalacat City)$"](15.0,120.1,15.6,120.8);out tags bb;')
if R: 
    print(R['osm3s'])
    for e in R['elements']: print(e['id'],{k:v for k,v in e['tags'].items() if k in('name','admin_level','ref','ref:psgc','source','wikidata')},e.get('bounds'))
R=op('[out:json][timeout:90];way["highway"]["name"~"MacArthur|SCTEX|Subic.*Clark|Clark.*Tarlac|TPLEX|McArthur",i](15.1,120.2,15.46,120.68);out tags center;')
if R:
    import collections
    c=collections.Counter((e['tags'].get('name'),e['tags'].get('highway'),e['tags'].get('ref')) for e in R['elements']); print(c.most_common(25))
R=op('[out:json][timeout:90];way["highway"~"^(motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|tertiary_link|unclassified|residential|living_street|road)$"](15.16,120.24,15.43,120.64);out skel;',120)
if R:
    print('ways',len(R['elements'])); p={}
    def f(x):
        p.setdefault(x,x)
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    size={}
    for w in R['elements']:
        n=w['nodes']; 
        for a in n[1:]: p[f(a)]=f(n[0])
    for w in R['elements']:
        r=f(w['nodes'][0]); size[r]=size.get(r,0)+1
    v=sorted(size.values(),reverse=True); print('weak comps',len(v),'largest',v[:5],'share',round(v[0]/sum(v),4))
