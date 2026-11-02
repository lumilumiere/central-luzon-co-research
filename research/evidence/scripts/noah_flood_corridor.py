"""Share of each municipality in NOAH 100-year flood hazard classes, rasterised to a 20 m EPSG:32651 grid.
Higher class wins where polygons overlap. Usage: python -I noah_flood_corridor.py <noah_dir> <aoi_cod.gpkg> <out.csv>"""
import sys,csv,glob,os
import numpy as np,geopandas as gpd,rasterio.features as F
from affine import Affine
d,aoi,out=sys.argv[1:4]; a=gpd.read_file(aoi); rows=[]
for prov,names in (('Tarlac',['Bamban','Capas']),('Pampanga',['Mabalacat City'])):
    shp=glob.glob(f'{d}/{prov}/**/*.shp',recursive=True)[0]
    for n in names:
        g=a[a.adm3_name==n]; u=g.to_crs(32651).geometry.iloc[0]
        f=gpd.read_file(shp,mask=g.geometry.iloc[0],columns=['Var']).to_crs(32651); print(n,f.shape,flush=True)
        x0,y0,x1,y1=u.bounds; c=20.; W=int((x1-x0)/c)+1; H=int((y1-y0)/c)+1; T=Affine(c,0,x0,0,-c,y1)
        m=F.rasterize([u],out_shape=(H,W),transform=T,fill=0,default_value=1,dtype='uint8').astype(bool); h=np.zeros((H,W),'uint8')
        for v in (1,2,3):
            s=f[f.Var==v].geometry
            if len(s): h=np.maximum(h,F.rasterize(((q,v) for q in s),out_shape=(H,W),transform=T,fill=0,dtype='uint8'))
        t=int(m.sum())
        for v in (1,2,3):
            k=int(((h==v)&m).sum()); rows.append((n,'100yr',v,round(k*c*c/1e6,2),round(100*k/t,1))); print(rows[-1],flush=True)
        rows.append((n,'100yr','any',round(int(((h>0)&m).sum())*c*c/1e6,2),round(100*int(((h>0)&m).sum())/t,1))); print(rows[-1],flush=True)
csv.writer(open(out,'w',newline='')).writerows([('unit','return_period','hazard_var','km2','pct_of_cod_area')]+rows)
