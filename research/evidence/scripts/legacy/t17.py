import json,sys,requests
import geopandas as gpd,pyogrio
from shapely.geometry import LineString
from shapely.ops import polygonize,unary_union
d=sys.argv[1]
p=json.load(open(f'{d}/hdx_planet.json',encoding='utf8'))['result']
for k in ['title','dataset_source','organization','dataset_date','last_modified','license_id','license_title','license_other','caveats','data_update_frequency','methodology_other','notes']:
    v=p.get(k); v=v.get('title') if isinstance(v,dict) else v; print(k,':',str(v)[:1300])
a=gpd.read_file(f'{d}/aoi_cod.gpkg'); au=a.to_crs(32651)
i=pyogrio.read_info(f'{d}/planet_road.gpkg'); print({k:i[k] for k in ('crs','features','fields','geometry_type')})
g=gpd.read_file(f'{d}/planet_road.gpkg',bbox=tuple(a.total_bounds)); print(g.shape); print(g.drop(columns='geometry').head(2).T.to_string()[:1400])
g=g.to_crs(32651)
for r in au.itertuples():
    c=g.clip(r.geometry); c=c.assign(L=c.length/1000); print(r.adm3_name,len(c),'km',round(c.L.sum(),1))
    for col in c.columns:
        if col in('geometry','L'): continue
        if c[col].nunique()<=8: print('  ',col,c.groupby(col,dropna=False).L.sum().round(1).to_dict())
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
r=s.post('https://overpass-api.de/api/interpreter',data={'data':'[out:json][timeout:100];rel["boundary"="administrative"]["name"~"^(Capas|Bamban|Mabalacat|City of Mabalacat|Mabalacat City)$"](15.0,120.1,15.6,120.8);out geom;'},timeout=140); print(r.status_code,len(r.content)); j=r.json(); print(j['osm3s']['timestamp_osm_base'])
for e in j['elements']:
    t=e['tags']; ls=[LineString([(q['lon'],q['lat']) for q in m['geometry']]) for m in e.get('members',[]) if m['type']=='way' and m.get('geometry') and m['role'] in('outer','')]
    ps=list(polygonize(unary_union(ls))); G=gpd.GeoSeries(ps,crs=4326).to_crs(32651).union_all() if ps else None
    print(e['id'],t.get('name'),t.get('admin_level'),t.get('ref'),t.get('ref:psgc'),t.get('source'),'km2',round(G.area/1e6,2) if G is not None else None)
    if G is not None:
        for q in au.itertuples():
            if q.adm3_name.split()[0] in t.get('name',''): print('   vs COD IoU',round(G.intersection(q.geometry).area/G.union(q.geometry).area,3))
