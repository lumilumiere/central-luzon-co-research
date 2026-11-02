import os,sys,json,csv
os.environ.update(GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR',CPL_VSIL_CURL_ALLOWED_EXTENSIONS='.tif',GDAL_HTTP_TIMEOUT='90',GDAL_HTTP_MAX_RETRY='3',GDAL_HTTP_RETRY_DELAY='3',GDAL_HTTP_USERAGENT='geo-access-check/0.1')
import numpy as np,geopandas as gpd,rasterio
from rasterio.mask import mask
d,e,x=sys.argv[1:4]
B='/vsicurl/https://data.worldpop.org/GIS/Population/'
R={'id6316_2020_unconstrained':f'{x}/phl_ppp_2020.tif',
   'id49861_2020_constrained':B+'Global_2000_2020_Constrained/2020/BSGM/PHL/phl_ppp_2020_constrained.tif',
   'R2025A_2020':B+'Global_2015_2030/R2025A/2020/PHL/v1/100m/constrained/phl_pop_2020_CN_100m_R2025A_v1.tif',
   'R2025A_2024':B+'Global_2015_2030/R2025A/2024/PHL/v1/100m/constrained/phl_pop_2024_CN_100m_R2025A_v1.tif'}
a=gpd.read_file(f'{d}/aoi_cod.gpkg'); o=gpd.read_file(f'{e}/aoi_osm.gpkg')
G={}
for r in a.itertuples(): G[('COD',r.adm3_name.split()[0])]=r.geometry
for r in o.itertuples(): G[('OSM',r.name)]=r.geometry
c=gpd.read_file(f'{d}/cod/phl_admin3.shp')
print('adm columns',[k for k in c.columns if 'adm' in k][:12])
G[('COD','Angeles')]=c[c.adm3_name=='Angeles City'].geometry.iloc[0]
print(c[c.adm3_name=='Angeles City'][['adm3_name','adm3_pcode','adm2_name','adm1_name','area_sqkm']].values.tolist())
for n in ['Tarlac','Pampanga']:
    G[('COD_adm2',n)]=c[c.adm2_name==n].union_all()
G[('COD_adm1','RegionIII')]=c[c.adm1_pcode=='PH03'].union_all() if 'adm1_pcode' in c else None
print('adm2 members Pampanga',sorted(c[c.adm2_name=='Pampanga'].adm3_name)[:30])
out=[]
for name,p in R.items():
    with rasterio.open(p) as r:
        for k,g in G.items():
            if g is None: continue
            for at in (False,True):
                if k[0] in('COD_adm2','COD_adm1') and at: continue
                try:
                    v,_=mask(r,[g],crop=True,nodata=r.nodata,all_touched=at); v=v[0]; ok=(v!=r.nodata)&np.isfinite(v); s=float(v[ok].sum())
                    out.append((name,k[0],k[1],'all_touched' if at else 'pixel_centre',round(s),int(ok.sum()))); print(out[-1],flush=True)
                except Exception as ex: print('ERR',name,k,at,repr(ex)[:200],flush=True)
        if name=='id6316_2020_unconstrained':
            t=0
            for _,w in r.block_windows(1):
                b=r.read(1,window=w); t+=float(b[(b!=r.nodata)&np.isfinite(b)].sum())
            print('national',name,round(t),flush=True)
csv.writer(open(f'{x}/zonal.csv','w',newline='')).writerows([('raster','boundary','unit','rule','sum_persons','valid_cells')]+out)
