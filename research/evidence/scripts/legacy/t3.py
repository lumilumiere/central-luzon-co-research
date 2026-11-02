import io,zipfile,requests,sys,os,hashlib
import geopandas as gpd, numpy as np, rasterio
from rasterio.mask import mask
from shapely import make_valid
d=sys.argv[1]
class R(io.RawIOBase):
    B=1<<23
    def __init__(s,u):
        s.p=0; r=requests.get(u,headers={'Range':'bytes=0-0','User-Agent':'Mozilla/5.0'},timeout=60); s.n=int(r.headers['Content-Range'].split('/')[1]); s.f=r.url; s.c={}
    def seekable(s):return True
    def readable(s):return True
    def seek(s,o,w=0):
        s.p={0:o,1:s.p+o,2:s.n+o}[w]; return s.p
    def tell(s):return s.p
    def blk(s,i):
        if i not in s.c:
            s.c={k:v for k,v in s.c.items() if k>=i-1}
            a=i*s.B; s.c[i]=requests.get(s.f,headers={'Range':f'bytes={a}-{min(a+s.B,s.n)-1}'},timeout=300).content
        return s.c[i]
    def read(s,k=-1):
        if k<0:k=s.n-s.p
        o=b''
        while k>0 and s.p<s.n:
            b=s.blk(s.p//s.B); j=s.p%s.B; c=b[j:j+k]; o+=c; s.p+=len(c); k-=len(c)
        return o
u='https://data.humdata.org/dataset/caf116df-f984-4deb-85ca-41b349d3f313/resource/4e4067d6-3fc8-4d2c-91ea-330c3d4f8e8e/download/phl_admin_boundaries.shp.zip'
if not os.path.exists(f'{d}/cod/phl_admin3.shp'):
    z=zipfile.ZipFile(R(u))
    for e in ['shp','dbf','shx','prj','cpg']:
        z.extract(f'phl_admin3.{e}',f'{d}/cod')
g=gpd.read_file(f'{d}/cod/phl_admin3.shp'); print(g.crs,g.shape,list(g.columns))
print('invalid national:',(~g.is_valid).sum())
m=g[g.adm3_pcode.isin(['PH0306902','PH0306904','PH0305409'])].copy()
print(m.drop(columns='geometry').T.to_string())
print('valid',m.is_valid.tolist(),'parts',m.geometry.apply(lambda x:len(getattr(x,'geoms',[x]))).tolist(),'verts',m.geometry.apply(lambda x:sum(len(p.exterior.coords) for p in getattr(x,'geoms',[x]))).tolist())
mu=m.to_crs(32651); print('utm km2',(mu.area/1e6).round(3).tolist(), 'names',mu.adm3_name.tolist())
for i,a in mu.iterrows():
    for j,b in mu.iterrows():
        if i<j: print(a.adm3_name,b.adm3_name,'shared boundary km',round(a.geometry.boundary.intersection(b.geometry.boundary).length/1000,2),'overlap km2',round(a.geometry.intersection(b.geometry).area/1e6,4),'gap_dist_m',round(a.geometry.distance(b.geometry),1))
un=mu.union_all(); print('union type',un.geom_type,'parts',len(getattr(un,'geoms',[un])),'km2',round(un.area/1e6,2),'holes',sum(len(p.interiors) for p in getattr(un,'geoms',[un])))
print('bbox wgs84',m.total_bounds.round(5).tolist()); print('per muni',{r.adm3_name:[round(x,4) for x in r.geometry.bounds] for r in m.itertuples()})
gb=gpd.read_file(f'{d}/gb_adm3_simpl.geojson'); gb=gb[gb.shapeName.isin(['Bamban','Capas','Mabalacat City'])].to_crs(32651)
for r in mu.itertuples():
    b=gb[gb.shapeName==r.adm3_name].geometry.iloc[0]
    print(r.adm3_name,'COD vs gb_simpl: IoU',round(r.geometry.intersection(b).area/r.geometry.union(b).area,4),'km2 diff',round((b.area-r.geometry.area)/1e6,3))
m.to_file(f'{d}/aoi_cod.gpkg',driver='GPKG')
nb=g.to_crs(32651); uu=un.buffer(1)
nn=nb[nb.intersects(uu)]; print('neighbours',[(a,b) for a,b in zip(nn.adm3_name,nn.adm2_name)])
with rasterio.open(f'{d}/wp/phl_ppp_2020.tif') as r:
    print(r.profile); print(r.bounds,r.res,r.tags(),r.compression,'ovr',r.overviews(1))
    t=0
    for p in m.itertuples():
        a,_=mask(r,[p.geometry],crop=True,nodata=r.nodata,all_touched=False); a=a[0]; v=a[(a!=r.nodata)&~np.isnan(a)]; s=float(v.sum()); t+=s
        print(p.adm3_name,'wp sum',round(s),'cells',v.size,'cellmax',round(float(v.max()),2),'cells>0',int((v>0).sum()))
    print('total',round(t))
    print(hashlib.md5(open(f'{d}/wp/phl_ppp_2020.tif','rb').read()).hexdigest())
