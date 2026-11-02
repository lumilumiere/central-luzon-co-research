import io,zipfile,requests,sys,json,os
import geopandas as gpd, pandas as pd, rasterio
from rasterio.env import Env
d=sys.argv[1]
class R(io.RawIOBase):
    def __init__(s,u):
        s.u=u; s.p=0; r=requests.get(u,headers={'Range':'bytes=0-0','User-Agent':'Mozilla/5.0'},allow_redirects=True,timeout=60); s.n=int(r.headers['Content-Range'].split('/')[1]); s.f=r.url
    def seekable(s):return True
    def readable(s):return True
    def seek(s,o,w=0):
        s.p={0:o,1:s.p+o,2:s.n+o}[w]; return s.p
    def tell(s):return s.p
    def read(s,k=-1):
        if k<0:k=s.n-s.p
        if k==0 or s.p>=s.n:return b''
        r=requests.get(s.f,headers={'Range':f'bytes={s.p}-{min(s.p+k,s.n)-1}'},timeout=120); s.p+=len(r.content); return r.content
base='https://data.humdata.org/dataset/caf116df-f984-4deb-85ca-41b349d3f313/resource/'
for nm,u in {'shp':base+'4e4067d6-3fc8-4d2c-91ea-330c3d4f8e8e/download/phl_admin_boundaries.shp.zip','gdb':base+'3fa0dbcf-e07d-4506-9821-ba15baa6da07/download/phl_admin_boundaries.gdb.zip'}.items():
    z=zipfile.ZipFile(R(u))
    print(nm,len(z.infolist()))
    for i in z.infolist()[:60]:
        if nm=='shp' or i.file_size>5e6: print('  ',i.filename,i.file_size,i.compress_size,i.compress_type)
print('---- gb simplified')
g=gpd.read_file(f'{d}/gb_adm3_simpl.geojson'); print(g.shape,list(g.columns),g.crs)
m=g[g.shapeName.str.contains(r'Capas|Bamban|Mabalacat',case=False)]
print(m.drop(columns='geometry').to_string()); 
mm=m.to_crs(32651); print(mm.assign(km2=mm.area/1e6)[['shapeName','km2','shapeID']].to_string()); print(m.total_bounds)
print('---- worldpop header via /vsicurl')
os.environ.update(GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR',CPL_VSIL_CURL_ALLOWED_EXTENSIONS='.tif')
with rasterio.open('/vsicurl/https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/PHL/phl_ppp_2020.tif') as r:
    print(r.profile); print(r.bounds,r.res,r.tags(),r.block_shapes,r.compression)
