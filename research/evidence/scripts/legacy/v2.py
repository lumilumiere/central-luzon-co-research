import sys,gzip,json,time,requests,hashlib,re
import pandas as pd,geopandas as gpd,shapely
d=sys.argv[1]; e=sys.argv[2]
a=gpd.read_file(f'{d}/aoi_cod.gpkg')
gb=gpd.read_file(f'{d}/gb_adm3_simpl.geojson'); gb=gb[gb.shapeName.isin(['Bamban','Capas','Mabalacat City'])].to_crs(32651); print('gb km2',dict(zip(gb.shapeName,(gb.area/1e6).round(2))))
g=gpd.read_file(f'{d}/planet_road.gpkg',bbox=tuple(a.total_bounds)).to_crs(32651); au=a.to_crs(32651)
print([c for c in g.columns][:40])
for r in au.itertuples():
    c=g.clip(r.geometry); c=c.assign(L=c.length/1000); print('planet',r.adm3_name,len(c),round(c.L.sum(),1), c.groupby('osm_tags_highway').L.sum().round(1).to_dict() if 'osm_tags_highway' in c else '')
rows=[]
for q in ['132303013','132303031']:
    with gzip.open(f'{d}/ms/{q}.csv.gz','rt',encoding='utf8') as f:
        for l in f:
            j=json.loads(l); c=j['geometry']['coordinates'][0]; xs=[x[0] for x in c]; ys=[x[1] for x in c]
            if 120.2<min(xs)<120.65 and 15.15<min(ys)<15.45: rows.append((sum(xs)/len(xs),sum(ys)/len(ys)))
df=pd.DataFrame(rows,columns=['x','y']); print('ms bbox rows',len(df))
o=gpd.read_file(f'{e}/aoi_osm.gpkg')
for r in a.itertuples():
    n=int(shapely.contains_xy(r.geometry,df.x.values,df.y.values).sum()); w=o[o.name==r.adm3_name.split()[0]].geometry.iloc[0]; print('MS',r.adm3_name,n,'OSM poly',int(shapely.contains_xy(w,df.x.values,df.y.values).sum()))
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
Q='[out:json][timeout:100];way["highway"~"^(motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|tertiary_link|unclassified|residential|living_street|road)$"](15.16,120.24,15.43,120.64);out skel;'
for ep in ['https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter']:
    r=s.post(ep,data={'data':Q},timeout=120); print(ep,r.status_code,len(r.content))
    if r.status_code==200 and r.content[:1]==b'{': break
J=r.json(); open(f'{e}/osm_ways_skel.json','wb').write(r.content); print(J['osm3s'],hashlib.sha256(r.content).hexdigest())
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
for u in ['https://data.humdata.org/api/3/action/package_show?id=2020-census-popn-by-sex-age-group-and-mun-admin3']:
    q=s.get(u,timeout=40); print(q.status_code)
    if q.status_code==200:
        t=q.json()['result']; print({k:str(t.get(k))[:220] for k in ['title','dataset_source','dataset_date','last_modified','license_title','data_update_frequency']},[(x['name'],x.get('size'),x.get('last_modified')) for x in t['resources']])
