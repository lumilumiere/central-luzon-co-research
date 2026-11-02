import json,sys,os,time
import geopandas as gpd, pyogrio, pandas as pd
d=sys.argv[1]
p=json.load(open(f'{d}/hdx_planet.json',encoding='utf8'))['result']
for k in ['title','dataset_source','dataset_date','last_modified','license_id','license_title','license_other','caveats','data_update_frequency','methodology_other','notes']: print(k,':',str(p.get(k))[:1500])
a=gpd.read_file(f'{d}/aoi_cod.gpkg')
print(pyogrio.list_layers(f'{d}/planet_road.gpkg'))
print(pyogrio.read_info(f'{d}/planet_road.gpkg'))
g=gpd.read_file(f'{d}/planet_road.gpkg',bbox=tuple(a.total_bounds)); print(g.shape,g.crs,list(g.columns)); print(g.drop(columns='geometry').head(3).T.to_string()[:1800])
g=g.to_crs(32651); au=a.to_crs(32651)
for r in au.itertuples():
    c=g.clip(r.geometry); print(r.adm3_name,'planet rows',len(c),'km',round(c.length.sum()/1000,1))
    for col in [x for x in c.columns if any(s in x.lower() for s in('surface','pred','pass','width')) and c[x].dtype==object][:5]:
        print('  ',col,(c.assign(L=c.length/1000).groupby(col,dropna=False).L.sum().round(1)).to_dict())
os.environ['GDAL_DISABLE_READDIR_ON_OPEN']='EMPTY_DIR'
t=time.time()
try:
    m=gpd.read_file('/vsicurl/https://downloads.ohsome.org/hdx/mapillary_road_surface/heigit_phl_roadsurface_lines.gpkg',bbox=tuple(a.total_bounds),engine='pyogrio')
    print('mapillary',m.shape,m.crs,list(m.columns),round(time.time()-t)); m.to_parquet(f'{d}/mapillary_aoi.parquet')
    print(m.drop(columns='geometry').head(2).T.to_string()[:2000])
    m=m.to_crs(32651)
    for r in au.itertuples():
        c=m.clip(r.geometry); L=c.length/1000
        print(r.adm3_name,'km',round(L.sum(),1))
        for col in [x for x in c.columns if x in('combined_surface_osm_priority','combined_surface_DL_priority','predicted_label','surface','pred_label')]:
            print('  ',col,c.assign(L=L).groupby(col,dropna=False).L.sum().round(1).to_dict())
        for col in [x for x in c.columns if 'mapillary' in x.lower() or 'prediction' in x.lower() or 'n_of' in x.lower()][:6]:
            print('  ',col,c[col].describe().to_dict() if c[col].dtype!=object else '')
except Exception as e: print('mapillary err',repr(e)[:400], time.time()-t)
