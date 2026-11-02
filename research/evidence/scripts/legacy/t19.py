import os,sys,time
os.environ.update(GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR',CPL_VSIL_CURL_CHUNK_SIZE='2097152',CPL_VSIL_CURL_CACHE_SIZE='268435456',GDAL_HTTP_TIMEOUT='60',GDAL_HTTP_MAX_RETRY='3',GDAL_HTTP_RETRY_DELAY='2',VSI_CACHE='TRUE',VSI_CACHE_SIZE='268435456',OGR_SQLITE_JOURNAL='OFF')
import geopandas as gpd,pyogrio
d=sys.argv[1]; a=gpd.read_file(f'{d}/aoi_cod.gpkg'); au=a.to_crs(32651)
u='/vsicurl/https://downloads.ohsome.org/hdx/mapillary_road_surface/heigit_phl_roadsurface_lines.gpkg'
t=time.time(); i=pyogrio.read_info(u); print({k:i[k] for k in('crs','features','fields','geometry_type')},round(time.time()-t),flush=True)
t=time.time(); m=gpd.read_file(u,bbox=tuple(a.total_bounds),engine='pyogrio'); print(m.shape,round(time.time()-t),flush=True)
m.to_parquet(f'{d}/mapillary_aoi.parquet'); print(m.drop(columns='geometry').head(2).T.to_string()[:2200])
m=m.to_crs(32651)
for r in au.itertuples():
    c=m.clip(r.geometry); c=c.assign(L=c.length/1000); print(r.adm3_name,len(c),'km',round(c.L.sum(),1))
    for col in c.columns:
        if col not in('geometry','L') and c[col].nunique()<=7: print('  ',col,c.groupby(col,dropna=False).L.sum().round(1).to_dict())
