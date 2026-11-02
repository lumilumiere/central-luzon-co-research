import sys,json,re,time,requests,hashlib
import pandas as pd,geopandas as gpd,shapely
from shapely.geometry import LineString
from shapely.ops import polygonize,unary_union
d=sys.argv[1]; e=sys.argv[2]
x=pd.read_excel(f'{e}/g2.xlsx',header=None,dtype=str); print('second-timepoint-only flag counts',x.iloc[3:,23].value_counts(dropna=False).to_dict())
j=json.load(open(f'{d}/0221A6DLPD0.px.json',encoding='utf8')); print(list(j)[:8])
lab=j['dimension']['Geographic Location']['category']['label'] if 'dimension' in j else {}
pick={k:v for k,v in lab.items() if re.search(r'^\W*(Philippines|Angeles|Region III|Central Luzon|Tarlac|Pampanga)',v.strip(),re.I)}; print(pick)
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
codes=list(pick)
if codes:
    time.sleep(2)
    r=s.post('https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px',json={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':codes}}],'response':{'format':'csv'}},timeout=120); print(r.status_code); print(r.text[:1800])
    open(f'{e}/census_extra.csv','w',encoding='utf8').write(r.text)
# OSM relations, retained this time
Q='[out:json][timeout:100];rel(id:13407320,15585455,15585456);out geom;'
r=s.post('https://overpass-api.de/api/interpreter',data={'data':Q},timeout=140); print('overpass',r.status_code,len(r.content)); J=r.json(); open(f'{e}/osm_rel.json','wb').write(r.content); print(J['osm3s']['timestamp_osm_base'],hashlib.sha256(r.content).hexdigest())
rows=[]
for el in J['elements']:
    ls=[LineString([(q['lon'],q['lat']) for q in m['geometry']]) for m in el['members'] if m['type']=='way' and m.get('geometry') and m['role'] in('outer','')]
    g=unary_union(list(polygonize(unary_union(ls)))); rows.append({'name':el['tags']['name'],'relid':el['id'],'ref':el['tags'].get('ref'),'version_meta':el.get('version'),'geometry':g})
o=gpd.GeoDataFrame(rows,crs=4326); o.to_file(f'{e}/aoi_osm.gpkg',driver='GPKG'); print(o.drop(columns='geometry').to_string()); print('utm km2',(o.to_crs(32651).area/1e6).round(2).tolist())
a=gpd.read_file(f'{d}/aoi_cod.gpkg'); au=a.to_crs(32651); ou=o.to_crs(32651)
for r_ in au.itertuples():
    n=r_.adm3_name.split()[0]; b=ou[ou.name==n].geometry.iloc[0]
    print(n,'COD km2',round(r_.geometry.area/1e6,2),'OSM',round(b.area/1e6,2),'OSM-only km2',round(b.difference(r_.geometry).area/1e6,2),'COD-only km2',round(r_.geometry.difference(b).area/1e6,2),'IoU',round(r_.geometry.intersection(b).area/r_.geometry.union(b).area,3))
# overlap between OSM polygons and which COD unit the OSM-only part falls in
c=gpd.read_file(f'{d}/cod/phl_admin3.shp').to_crs(32651)
for r_ in ou.itertuples():
    dif=r_.geometry.difference(au[au.adm3_name.str.startswith(r_.name)].geometry.iloc[0])
    hit=c[c.intersects(dif)].copy(); hit['km2']=hit.geometry.intersection(dif).area/1e6; print(r_.name,'OSM-only lies in',hit[hit.km2>.5][['adm3_name','km2']].round(2).values.tolist())
# reproduce from retained files
ob=pd.read_parquet(f'{d}/ob_corr.parquet'); print('ob rows',len(ob),'min conf',ob.confidence.min())
for r_ in a.itertuples():
    q=ob[shapely.contains_xy(r_.geometry,ob.longitude.values,ob.latitude.values)]; print('GOB',r_.adm3_name,len(q),[int((q.confidence>=t).sum()) for t in (.763,.817,.874)],round(q.area_in_meters.sum()/1e6,2))
    w=o[o.name==r_.adm3_name.split()[0]].geometry.iloc[0]; q2=ob[shapely.contains_xy(w,ob.longitude.values,ob.latitude.values)]; print('   OSM poly',len(q2),int((q2.confidence>=.763).sum()))
