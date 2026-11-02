"""Extract COD-AB admin4 for the three municipalities from the remote national shapefile zip by HTTP range.
Usage: python -I extract_cod_admin4.py <out_dir>"""
import io,sys,zipfile,requests,os
import geopandas as gpd
d=sys.argv[1]
class R(io.RawIOBase):
    B=1<<23
    def __init__(s,u):
        s.p=0; r=requests.get(u,headers={'Range':'bytes=0-0','User-Agent':'geo-access-check/0.1'},timeout=60); s.n=int(r.headers['Content-Range'].split('/')[1]); s.f=r.url; s.c={}
    def seekable(s): return True
    def readable(s): return True
    def seek(s,o,w=0): s.p={0:o,1:s.p+o,2:s.n+o}[w]; return s.p
    def tell(s): return s.p
    def blk(s,i):
        if i not in s.c:
            s.c={k:v for k,v in s.c.items() if k>=i-1}; a=i*s.B; s.c[i]=requests.get(s.f,headers={'Range':f'bytes={a}-{min(a+s.B,s.n)-1}'},timeout=300).content
        return s.c[i]
    def read(s,k=-1):
        if k<0: k=s.n-s.p
        o=b''
        while k>0 and s.p<s.n:
            b=s.blk(s.p//s.B); j=s.p%s.B; c=b[j:j+k]; o+=c; s.p+=len(c); k-=len(c)
        return o
u='https://data.humdata.org/dataset/caf116df-f984-4deb-85ca-41b349d3f313/resource/4e4067d6-3fc8-4d2c-91ea-330c3d4f8e8e/download/phl_admin_boundaries.shp.zip'
z=zipfile.ZipFile(R(u)); os.makedirs(f'{d}/cod4',exist_ok=True)
print([ (i.filename,i.file_size,i.compress_size) for i in z.infolist() if 'admin4' in i.filename],flush=True)
for e in ['dbf','shx','prj','cpg','shp']:
    z.extract(f'phl_admin4.{e}',f'{d}/cod4'); print(e,flush=True)
g=gpd.read_file(f'{d}/cod4/phl_admin4.shp'); print(g.shape,g.crs,list(g.columns)[:14])
m=g[g.adm3_pcode.isin(['PH0305409','PH0306902','PH0306904'])]; print(m.groupby('adm3_name').size().to_dict(),int((~m.is_valid).sum())); m.to_file(f'{d}/aoi_cod_adm4.gpkg',driver='GPKG')
