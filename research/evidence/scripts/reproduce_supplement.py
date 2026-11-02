"""Supplementary checks that were previously logged only or not performed.
1. R2025A 2020 municipal and national sums, and the national-scaling comparison with the 2020 census.
2. WorldPop id 49861 (2020 constrained) on COD-AB and OSM polygons, pixel-centre and all-touched.
Census figures are PSA OpenSTAT table 0221A6DLPD0 (2020 counts; national 109,033,245).
Run from research/: python -I evidence/scripts/reproduce_supplement.py"""
import csv,warnings
warnings.filterwarnings('ignore')
import numpy as np,geopandas as gpd,rasterio
from rasterio.mask import mask
L='local-data/raw'; out=[]
def rec(*r): out.append(r); print(*r,flush=True)
a=gpd.read_file(f'{L}/cod/aoi_cod.gpkg'); o=gpd.read_file(f'{L}/osm/aoi_osm.gpkg'); c=gpd.read_file(f'{L}/cod/phl_admin3.shp')
G={'COD':{r.adm3_name.split()[0]:r.geometry for r in a.itertuples()},'OSM':{r.name:r.geometry for r in o.itertuples()}}
G['COD']['Angeles']=c[c.adm3_name=='Angeles City'].geometry.iloc[0]
cen={'Mabalacat':293244,'Bamban':78260,'Capas':156056,'Angeles':462928}; NAT=109033245; proj20=520257
def zs(r,g,at):
    x,_=mask(r,[g],crop=True,nodata=r.nodata,all_touched=at); v=x[0]; return float(v[(v!=r.nodata)&np.isfinite(v)].sum())
def nat(r):
    t=0.
    for _,w in r.block_windows(1):
        b=r.read(1,window=w); t+=float(b[(b!=r.nodata)&np.isfinite(b)].sum())
    return t
with rasterio.open(f'{L}/worldpop/phl_pop_2020_CN_100m_R2025A_v1.tif') as r:
    n=nat(r); f=n/NAT; rec('R2025A_2020','national sum','persons',round(n)); rec('R2025A_2020','national factor vs census 2020','ratio',round(f,4))
    v={k:zs(r,g,False) for k,g in G['COD'].items()}
    for k,x in v.items(): rec('R2025A_2020',f'COD pixel-centre {k}','persons',round(x)); rec('R2025A_2020',f'{k} ratio to census, then divided by national factor','ratio',f'{x/cen[k]:.4f} then {x/cen[k]/f:.4f}')
    mA=v['Mabalacat']+v['Angeles']; rec('R2025A_2020','Mabalacat+Angeles ratio, then divided by national factor','ratio',f'{mA/(cen["Mabalacat"]+cen["Angeles"]):.4f} then {mA/(cen["Mabalacat"]+cen["Angeles"])/f:.4f}')
with rasterio.open(f'{L}/worldpop/phl_ppp_2020_constrained.tif') as r:
    rec('id49861_2020','national sum','persons',round(nat(r)))
    for b in ('COD','OSM'):
        for at in (False,True):
            s=0
            for k in ('Mabalacat','Bamban','Capas'):
                x=zs(r,G[b][k],at); s+=x; rec('id49861_2020',f'{b} {"all-touched" if at else "pixel-centre"} {k}','persons',round(x))
            rec('id49861_2020',f'{b} {"all-touched" if at else "pixel-centre"} combined / projection 2020','ratio',round(s/proj20,3))
csv.writer(open('evidence/results/reproduction_supplement_2026-11-02.csv','w',newline='',encoding='utf8')).writerows([('product','metric','unit','value')]+out)
