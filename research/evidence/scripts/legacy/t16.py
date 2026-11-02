import requests,sys,re,json,collections
import geopandas as gpd
from shapely.geometry import LineString,Polygon
from shapely.ops import polygonize,unary_union
d=sys.argv[1]; s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
def op(Q,to=120):
    for e in ['https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.kumi.systems/api/interpreter']:
        try:
            r=s.post(e,data={'data':Q},timeout=to); print(e,r.status_code,len(r.content))
            if r.status_code==200 and r.content[:1]==b'{': return r.json()
        except Exception as x: print(e,'ERR',type(x).__name__)
R=op('[out:json][timeout:100];way["highway"]["name"~"MacArthur|SCTEX|Subic.*Clark|Clark.*Tarlac|TPLEX|McArthur",i](15.1,120.2,15.46,120.68);out tags center;')
if R:
    print(R['osm3s']); print(collections.Counter((e['tags'].get('name'),e['tags'].get('highway'),e['tags'].get('ref')) for e in R['elements']).most_common(14))
R=op('[out:json][timeout:100];rel["boundary"="administrative"]["name"~"^(Capas|Bamban|Mabalacat|City of Mabalacat|Mabalacat City)$"](15.0,120.1,15.6,120.8);out tags geom;',150)
if R:
    print(R['osm3s']); a=gpd.read_file(f'{d}/aoi_cod.gpkg').to_crs(32651)
    for e in R['elements']:
        t=e['tags']; ls=[LineString([(p['lon'],p['lat']) for p in m['geometry']]) for m in e['members'] if m['type']=='way' and m.get('geometry') and m['role'] in('outer','')]
        ps=list(polygonize(unary_union(ls))); g=gpd.GeoSeries(ps,crs=4326).to_crs(32651).union_all() if ps else None
        print(e['id'],t.get('name'),t.get('admin_level'),t.get('ref'),t.get('ref:psgc'),'km2',round(g.area/1e6,2) if g else None)
        if g is not None:
            for r in a.itertuples():
                if r.adm3_name.split()[0]==t.get('name','').replace('City of ','').split()[0]:
                    print('   vs COD IoU',round(g.intersection(r.geometry).area/g.union(r.geometry).area,3))
