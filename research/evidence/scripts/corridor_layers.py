"""Corridor sample of terrain and land cover via HTTP range reads of public COGs.
Usage: python -I corridor_layers.py <aoi_cod.gpkg> <aoi_osm.gpkg> <out.csv>"""
import os,sys,csv
os.environ.update(GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR',CPL_VSIL_CURL_ALLOWED_EXTENSIONS='.tif',GDAL_HTTP_TIMEOUT='90',GDAL_HTTP_MAX_RETRY='3',GDAL_HTTP_RETRY_DELAY='3')
import numpy as np,geopandas as gpd,rasterio
from rasterio.mask import mask
a=gpd.read_file(sys.argv[1]); rows=[]
dem='/vsicurl/https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N15_00_E120_00_DEM/Copernicus_DSM_COG_10_N15_00_E120_00_DEM.tif'
wc='/vsicurl/https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_N15E120_Map.tif'
CL={10:'tree',20:'shrub',30:'grass',40:'crop',50:'built',60:'bare',70:'snow',80:'water',90:'wetland',95:'mangrove',100:'moss'}
with rasterio.open(dem) as r:
    print('DEM',r.crs,r.res,r.bounds,r.nodata,r.dtypes,r.profile.get('blockxsize'))
    for p in a.itertuples():
        x,_=mask(r,[p.geometry],crop=True,nodata=-9999,filled=True); v=x[0]; v=v[v>-9000]
        row=(p.adm3_name,p.adm3_pcode,'elevation_m',int(v.size),*[round(float(q),1) for q in (v.min(),np.percentile(v,50),np.percentile(v,95),v.max())]); rows.append(row); print(row,flush=True)
with rasterio.open(wc) as r:
    print('WC',r.crs,r.res,r.bounds,r.nodata,r.dtypes,r.profile.get('blockxsize'))
    for p in a.itertuples():
        x,_=mask(r,[p.geometry],crop=True,nodata=0,filled=True); v=x[0]; v=v[v>0]; t=v.size; u,c=np.unique(v,return_counts=True)
        d={CL.get(int(k),str(k)):round(100*int(n)/t,1) for k,n in zip(u,c)}
        rows.append((p.adm3_name,p.adm3_pcode,'worldcover_pct',t,str(d))); print(p.adm3_name,t,d,flush=True)
csv.writer(open(sys.argv[3],'w',newline='',encoding='utf8')).writerows([('unit','cod_pcode','metric','valid_cells','min_or_dict','p50','p95','max')]+rows)
