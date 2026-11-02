"""OSM land-use area and building-tag counts by municipality via ohsome (Overpass returned 502 and non-JSON for this query).
Usage: python -I osm_landuse.py <aoi_cod.gpkg> <out.csv>"""
import json,sys,csv,time,requests
import geopandas as gpd
a=gpd.read_file(sys.argv[1]).to_crs(4326); s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
fc={'type':'FeatureCollection','features':[{'type':'Feature','id':r.adm3_name.replace(' ','_'),'properties':{'id':r.adm3_name},'geometry':json.loads(gpd.GeoSeries([r.geometry.simplify(0.0002)]).to_json())['features'][0]['geometry']} for r in a.itertuples()]}
def q(kind,f):
    r=s.post(f'https://api.ohsome.org/v1/elements/{kind}/groupBy/boundary',data={'bpolys':json.dumps(fc),'filter':f},timeout=170); r.raise_for_status(); time.sleep(.5)
    return {g['groupByObject']:g['result'][-1] for g in r.json()['groupByResult']}
rows=[]
for lab,kind,f,div in [(f'landuse_{x}_km2','area',f'landuse={x} and geometry:polygon',1e6) for x in ['industrial','commercial','retail','residential','farmland','forest']]+[('buildings_all','count','building=* and geometry:polygon',1),('buildings_with_use_tag','count','building=* and building!=yes and geometry:polygon',1),('buildings_with_levels','count','building:levels=* and geometry:polygon',1),('buildings_with_height','count','height=* and building=* and geometry:polygon',1),('transit_route_relations','count','type:relation and route in (bus,minibus,share_taxi,train)',1),('bus_stops','count','(highway=bus_stop or public_transport=platform) and geometry:point',1)]:
    r=q(kind,f)
    for k,v in r.items(): rows.append((k,lab,round(v['value']/div,2),v['timestamp']))
    print(lab,{k:round(v['value']/div,2) for k,v in r.items()},flush=True)
csv.writer(open(sys.argv[2],'w',newline='')).writerows([('unit','metric','value','osm_snapshot')]+rows)
