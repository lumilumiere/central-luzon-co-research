import requests,gzip,io,zlib,csv,sys,os,time
import numpy as np, geopandas as gpd, pandas as pd, shapely
d=sys.argv[1]; a=gpd.read_file(f'{d}/aoi_cod.gpkg')
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
base='https://storage.googleapis.com/open-buildings-data/v3/'
r=s.get(base+'polygons_s2_level_4_gzip/339_buildings.csv.gz',headers={'Range':'bytes=0-1999999'},timeout=120); print(r.status_code,len(r.content),r.headers.get('Content-Range'))
t=zlib.decompressobj(31).decompress(r.content).decode('utf8','replace'); L=t.splitlines(); print(L[0]); print(L[1][:300]); print('rows in 2MB',len(L))
t0=time.time()
R=s.get(base+'points_s2_level_4_gzip/339_buildings.csv.gz',stream=True,timeout=120)
import gzip as gz
class W:
    def __init__(s,r): s.r=r.raw; s.r.decode_content=False
    def read(s,n=-1): return s.r.read(n)
    def readable(s): return True
out=[];n=0
for ch in pd.read_csv(gz.GzipFile(fileobj=W(R)),chunksize=500000):
    n+=len(ch); m=ch[(ch.longitude.between(120.2,120.65))&(ch.latitude.between(15.15,15.45))]; out.append(m[['latitude','longitude','area_in_meters','confidence','full_plus_code']])
    if n%5000000<500000: print(n,round(time.time()-t0),flush=True)
df=pd.concat(out); print('rows',n,'bbox rows',len(df),round(time.time()-t0)); df.to_parquet(f'{d}/ob_corr.parquet')
for r in a.itertuples():
    q=df[shapely.contains_xy(r.geometry,df.longitude.values,df.latitude.values)]
    print(r.adm3_name,'GOB count',len(q),'area_km2',round(q.area_in_meters.sum()/1e6,2),'median',round(q.area_in_meters.median(),1),'conf q',q.confidence.quantile([.05,.25,.5,.75,.95]).round(3).tolist(),'>=.763',int((q.confidence>=.763).sum()),'>=.817',int((q.confidence>=.817).sum()),'>=.874',int((q.confidence>=.874).sum()),'min conf',round(q.confidence.min(),3))
