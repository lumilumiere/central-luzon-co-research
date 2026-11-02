import requests,json,sys,time
import geopandas as gpd
d=sys.argv[1]; a=gpd.read_file(f'{d}/aoi_cod.gpkg').to_crs(4326)
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0 (research access check)'
print(s.get('https://api.ohsome.org/v1/metadata',timeout=60).json().get('extractRegion',{}).get('temporalExtent'))
bp={r.adm3_name.replace(' ','_'):json.loads(gpd.GeoSeries([r.geometry.simplify(0.0002)]).to_json())['features'][0]['geometry'] for r in a.itertuples()}
fc={'type':'FeatureCollection','features':[{'type':'Feature','id':k,'properties':{'id':k},'geometry':v} for k,v in bp.items()]}
base='type:way and highway in (motorway,motorway_link,trunk,trunk_link,primary,primary_link,secondary,secondary_link,tertiary,tertiary_link,unclassified,residential,living_street,service,track,road)'
drv='type:way and highway in (motorway,motorway_link,trunk,trunk_link,primary,primary_link,secondary,secondary_link,tertiary,tertiary_link,unclassified,residential,living_street,road)'
def L(f,**k):
    for t in range(3):
        r=s.post('https://api.ohsome.org/v1/elements/length/groupBy/boundary',data={'bpolys':json.dumps(fc),'filter':f,**k},timeout=170)
        if r.status_code==200: 
            return {g['groupByObject']:g['result'][-1] for g in r.json()['groupByResult']}
        print(r.status_code,r.text[:300]); time.sleep(5)
tt=L(drv); print('ts',{k:v['timestamp'] for k,v in tt.items()})
tot={k:v['value'] for k,v in tt.items()}; print('drivable km',{k:round(v/1000,1) for k,v in tot.items()})
ta=L(base); print('incl service/track km',{k:round(v['value']/1000,1) for k,v in ta.items()})
out={}
for lab,tag in [('oneway','oneway=*'),('lanes','lanes=*'),('maxspeed','maxspeed=*'),('surface','surface=*'),('access','access=*'),('name','name=*'),('ref','ref=*'),('bridge','bridge=*'),('smoothness','smoothness=*')]:
    r=L(f'({drv}) and {tag}'); time.sleep(.5)
    out[lab]={k:round(100*v['value']/tot[k],1) for k,v in r.items()}
    print(lab,out[lab])
for cl,f in [('motorway+link','motorway,motorway_link'),('trunk+link','trunk,trunk_link'),('primary+link','primary,primary_link'),('secondary+link','secondary,secondary_link'),('tertiary+link','tertiary,tertiary_link'),('unclassified','unclassified'),('residential','residential'),('service','service'),('track','track')]:
    r=L(f'type:way and highway in ({f})'); print(cl,{k:round(v['value']/1000,1) for k,v in r.items()})
hier='type:way and highway in (motorway,motorway_link,trunk,trunk_link,primary,primary_link,secondary,secondary_link)'
ht=L(hier)
for lab,tag in [('lanes','lanes=*'),('maxspeed','maxspeed=*'),('oneway','oneway=*'),('surface','surface=*')]:
    r=L(f'({hier}) and {tag}'); print('major',lab,{k:round(100*v['value']/ht[k]['value'],1) for k,v in r.items()})
print('road-class count tags national?')
