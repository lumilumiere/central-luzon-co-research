import sys,requests,glob,os
import numpy as np,geopandas as gpd,pandas as pd,rasterio,shapely
from rasterio.mask import mask
from shapely.geometry import LineString
from shapely.ops import polygonize,unary_union
d=sys.argv[1]
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
j=s.post('https://overpass-api.de/api/interpreter',data={'data':'[out:json][timeout:100];rel(id:13407320,15585455,15585456);out geom;'},timeout=140).json()
P={}
for e in j['elements']:
    ls=[LineString([(q['lon'],q['lat']) for q in m['geometry']]) for m in e['members'] if m['type']=='way' and m.get('geometry') and m['role'] in('outer','')]
    P[e['tags']['name']]=unary_union(list(polygonize(unary_union(ls))))
a=gpd.read_file(f'{d}/aoi_cod.gpkg'); C={r.adm3_name.split()[0]:r.geometry for r in a.itertuples()}
ob=pd.read_parquet(f'{d}/ob_corr.parquet')
cen={'Mabalacat':(293244,306594),'Bamban':(78260,81012),'Capas':(156056,162724)}
for yr,f,ix in [(2020,'phl_pop_2020_CN_100m_R2025A_v1.tif',0),(2024,'phl_pop_2024_CN_100m_R2025A_v1.tif',1)]:
    with rasterio.open(f'{d}/wp/{f}') as r:
        for n in C:
            o=[]
            for lab,g in (('COD',C[n]),('OSM',P[n])):
                x,_=mask(r,[g],crop=True,nodata=r.nodata); x=x[0]; v=x[(x!=r.nodata)&np.isfinite(x)]; o.append((lab,round(float(v.sum())),round(float(v.sum())/cen[n][ix],3)))
            print(yr,n,o,'census',cen[n][ix])
for n in C:
    c=int(shapely.contains_xy(C[n],ob.longitude.values,ob.latitude.values).sum()); q=int(shapely.contains_xy(P[n],ob.longitude.values,ob.latitude.values).sum()); print('GOB',n,'COD',c,'OSM',q)
