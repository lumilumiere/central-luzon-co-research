import sys,glob,os
import geopandas as gpd,numpy as np,rasterio
from rasterio.mask import mask
d=sys.argv[1]; a=gpd.read_file(f'{d}/aoi_cod.gpkg')
c=gpd.read_file(f'{d}/cod/phl_admin3.shp'); ang=c[c.adm3_name=='Angeles City']
for f in sorted(glob.glob(f'{d}/wp/*.tif')):
    with rasterio.open(f) as r:
        print('\n',os.path.basename(f),r.width,r.height,r.dtypes,r.nodata,r.crs.to_epsg(),r.res,r.compression,r.is_tiled,r.block_shapes[0])
        for g in list(a.itertuples())+list(ang.itertuples()):
            x,_=mask(r,[g.geometry],crop=True,nodata=r.nodata); x=x[0]; v=x[(x!=r.nodata)&np.isfinite(x)]
            print('  ',g.adm3_name,round(float(v.sum())),'cells',v.size)
        tot=0
        for _,w in r.block_windows(1):
            b=r.read(1,window=w); tot+=float(b[(b!=r.nodata)&np.isfinite(b)].sum())
        print('   national sum',round(tot))
