"""Compare candidate distribution layers with PSA 2024 household population shares by barangay.
misallocation = 0.5*sum(|layer share - census share|) within a municipality: share of people who would need reassigning.
Usage: python -I barangay_distribution_test.py <dl> <dl3> <dl5> <out_dir>"""
import json,sys,gzip
import numpy as np,pandas as pd,geopandas as gpd,rasterio,shapely
from rasterio.mask import mask
sys.stdout.reconfigure(encoding='utf8',errors='replace')
dl,dl3,dl5,o=sys.argv[1:5]
g=gpd.read_file(f'{dl5}/aoi_cod_adm4.gpkg'); g['psgc']=g.adm4_pcode.str[2:]
j=json.load(open(f'{dl}/0031A6DTPH2.px.json',encoding='utf8')); ids=j['id']; print(ids,j['size'],j.get('updated'),j.get('source'))
geo=j['dimension']['Geographic Location']['category']; order=sorted(geo['index'],key=geo['index'].get); n=j['size'][1]
par=j['dimension'][ids[1]]['category']; pl=[par['label'][k] for k in sorted(par['index'],key=par['index'].get)]; print(pl)
import requests,csv,io,time
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
rows=[]
for pre in ['0305409','0306902','0306904']:
    codes=[k for k in order if k.startswith(pre) and not k.endswith('000')]; lab={geo['label'][k].strip():k for k in codes}
    time.sleep(3); r=s.post('https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0031A6DTPH2.px',json={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':codes}}],'response':{'format':'csv'}},timeout=120); r.raise_for_status()
    t=r.content.decode('latin-1').lstrip('Feff'); open(f'{o}/psa_0031A6DTPH2_{pre}.csv','w',encoding='utf8').write(t)
    for x in list(csv.reader(io.StringIO(t)))[1:]:
        if x and x[0].strip() in lab: rows.append((lab[x[0].strip()],x[0].strip(' .'),float(x[1]),float(x[2]),float(x[3])))
p=pd.DataFrame(rows,columns=['psgc','psa_name','p0','p1','p2'])
print(len(p),p.head(3).to_string()); m=g.merge(p,on='psgc',how='outer',indicator=True); print(m._merge.value_counts().to_dict()); print(m[m._merge!='both'][['adm4_name','adm4_pcode','psgc','psa_name']].to_string()[:1200])
# name fallback for unmatched codes
g2=g.copy()
def nk(s): 
    import re
    s=s.lower(); s=re.sub(r'\(.*?\)|pob\.?|poblacion|barangay|brgy\.?','',s); s=s.replace('sto.','santo').replace('sta.','santa').replace('ñ','n'); return re.sub(r'[^a-z0-9]','',s)
g2['k']=g2.adm3_pcode.str[2:]+g2.adm4_name.map(nk); p2=p.copy(); p2['k']=p2.psgc.str[:7]+p2.psa_name.map(nk)
c=g2.merge(p,on='psgc',how='left'); miss=c[c.psa_name.isna()]
print('code matched',int(c.psa_name.notna().sum()),'unmatched',len(miss))
if len(miss):
    f=miss[['adm4_pcode','k']].merge(p2,on='k',how='left'); print('name matched',int(f.psa_name.notna().sum())); mp=dict(zip(f.adm4_pcode,f.psgc)); g['psgc']=g.apply(lambda r: mp.get(r.adm4_pcode) if (r.adm4_pcode in mp and isinstance(mp.get(r.adm4_pcode),str)) else r.psgc,axis=1)
d=g.merge(p,on='psgc',how='inner'); print('final join',len(d),'of',len(g),len(p)); col='p0'; print('population column label',pl[0])
d=d.rename(columns={col:'census'}); d['census']=pd.to_numeric(d.census,errors='coerce')
def zs(f):
    with rasterio.open(f) as r:
        out=[]
        for q in d.geometry:
            x,_=mask(r,[q],crop=True,nodata=r.nodata); v=x[0]; out.append(float(v[(v!=r.nodata)&np.isfinite(v)].sum()))
    return out
d['r25_2024']=zs(f'{dl5}/wp/phl_pop_2024_CN_100m_R2025A_v1.tif'); d['id6316_2020']=zs(f'{dl3}/phl_ppp_2020.tif')
ob=pd.read_parquet(f'{dl}/ob_corr.parquet')
d['gob065']=[int(shapely.contains_xy(q,ob.longitude.values,ob.latitude.values).sum()) for q in d.geometry]
hi=ob[ob.confidence>=.763]; d['gob0763']=[int(shapely.contains_xy(q,hi.longitude.values,hi.latitude.values).sum()) for q in d.geometry]
xs=[]
for f in ['132303013','132303031']:
    with gzip.open(f'{dl}/ms/{f}.csv.gz','rt',encoding='utf8') as h:
        for l in h:
            c=json.loads(l)['geometry']['coordinates'][0]; a=[t[0] for t in c]; b=[t[1] for t in c]
            if 120.2<min(a)<120.65 and 15.15<min(b)<15.45: xs.append((sum(a)/len(a),sum(b)/len(b)))
xs=np.array(xs); d['ms']=[int(shapely.contains_xy(q,xs[:,0],xs[:,1]).sum()) for q in d.geometry]
d['area']=d.to_crs(32651).area/1e6
L=['r25_2024','id6316_2020','gob065','gob0763','ms','area']; res=[]
for u,t in list(d.groupby('adm3_name'))+[('All three, within municipality',None)]:
    if t is None: continue
    s=t.census/t.census.sum()
    for k in L:
        a=t[k]/t[k].sum(); res.append(dict(unit=u,layer=k,barangays=len(t),misallocation_pct=round(50*float((a-s).abs().sum()),1),spearman=round(float(a.rank().corr(s.rank())),3),max_abs_share_gap_pct=round(100*float((a-s).abs().max()),1)))
r=pd.DataFrame(res); r.to_csv(f'{o}/barangay_distribution_test_2026-11-02.csv',index=False)
print(r.pivot(index='layer',columns='unit',values='misallocation_pct').to_string()); print(r.pivot(index='layer',columns='unit',values='spearman').to_string())
print('census sum by muni',d.groupby('adm3_name').census.sum().to_dict())
d.drop(columns='geometry')[['adm3_name','adm4_name','adm4_pcode','psgc','census','r25_2024','id6316_2020','gob065','gob0763','ms','area']].to_csv(f'{o}/barangay_layer_table_local.csv',index=False)
