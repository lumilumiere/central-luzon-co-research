"""Reproduce the calculations that drive source selection, from files in research/local-data/.
Writes evidence/results/reproduction_2026-11-02.csv. Run from research/: python -I evidence/scripts/reproduce_core.py
Checks: identifiers and crosswalk, boundary areas and overlaps, raster sums (two masking rules, two boundaries),
national sums, combined gate ratio, barangay share mismatch (total and household population), footprint counts."""
import csv,gzip,json,os,sys,warnings
warnings.filterwarnings('ignore')
import numpy as np,pandas as pd,geopandas as gpd,rasterio,shapely
from rasterio.mask import mask
L='local-data'; out=[]
def rec(group,metric,unit,value,note=''): out.append((group,metric,unit,value,note)); print(group,metric,unit,value,note,flush=True)
c=gpd.read_file(f'{L}/raw/cod/phl_admin3.shp'); rec('boundary','COD admin3 polygons','count',len(c)); rec('boundary','COD admin3 invalid','count',int((~c.is_valid).sum()))
a=gpd.read_file(f'{L}/raw/cod/aoi_cod.gpkg'); o=gpd.read_file(f'{L}/raw/osm/aoi_osm.gpkg'); au=a.to_crs(32651); ou=o.to_crs(32651)
rec('boundary','COD union area','km2 EPSG:32651',round(au.union_all().area/1e6,2))
for r in au.itertuples():
    n=r.adm3_name.split()[0]; b=ou[ou.name==n].geometry.iloc[0]
    rec('boundary',f'{r.adm3_name} {r.adm3_pcode} area','km2',round(r.geometry.area/1e6,2),'COD-AB')
    rec('boundary',f'{r.adm3_name} OSM area','km2',round(b.area/1e6,2),'OSM 2026-11-02')
    rec('boundary',f'{r.adm3_name} IoU COD vs OSM','ratio',round(r.geometry.intersection(b).area/r.geometry.union(b).area,3))
ang=c[c.adm3_name=='Angeles City'].to_crs(32651).geometry.iloc[0]
rec('boundary','Mabalacat OSM area inside COD Angeles','km2',round(ou[ou.name=='Mabalacat'].geometry.iloc[0].intersection(ang).area/1e6,2))
# identifiers: COD admin4 to PSA barangay codes
g4=gpd.read_file(f'{L}/raw/cod/aoi_cod_adm4.gpkg'); g4['psgc']=g4.adm4_pcode.str[2:]
# Labels repeat across municipalities (for example Dolores, San Francisco), so match names within each municipality only.
lab=json.load(open(f'{L}/raw/psa/0031A6DTPH2.px.json',encoding='utf8'))['dimension']['Geographic Location']['category']['label']
parts=[]
for pre in ['0305409','0306902','0306904']:
    q=pd.read_csv(f'{L}/raw/psa/psa_0031A6DTPH2_{pre}.csv',encoding='utf8',header=0); q.columns=['label','total','household','households']; q['label']=q['label'].astype(str).str.strip(' .')
    code={v.strip(' .'):k for k,v in lab.items() if k.startswith(pre) and not k.endswith('000')}
    q['psgc']=q.label.map(code); parts.append(q.dropna(subset=['psgc']))
P=pd.concat(parts)
dup=sum(pd.Series([v.strip(' .') for k,v in lab.items() if k[:7] in('0305409','0306902','0306904') and not k.endswith('000')]).duplicated())
rec('identifiers','barangay names repeated across the three municipalities','count',int(dup),'reason for per-municipality matching')
m=g4.merge(P,on='psgc',how='outer',indicator=True); rec('identifiers','barangay code join both','count',int((m._merge=='both').sum()),f"cod_only={int((m._merge=='left_only').sum())} psa_only={int((m._merge=='right_only').sum())}")
for mun,pre in [('Mabalacat City','0305409'),('Bamban','0306902'),('Capas','0306904')]:
    t=P[P.psgc.str.startswith(pre)]; rec('population',f'{mun} 2024 barangay total population sum','persons',int(t.total.sum())); rec('population',f'{mun} 2024 barangay household population sum','persons',int(t.household.sum()))
# rasters
R6=f'{L}/raw/worldpop/phl_ppp_2020.tif'; R24=f'{L}/raw/worldpop/phl_pop_2024_CN_100m_R2025A_v1.tif'
def zs(path,geoms,at):
    with rasterio.open(path) as r:
        res=[]
        for g in geoms:
            x,_=mask(r,[g],crop=True,nodata=r.nodata,all_touched=at); v=x[0]; res.append(float(v[(v!=r.nodata)&np.isfinite(v)].sum()))
        return res
def natsum(path):
    t=0.
    with rasterio.open(path) as r:
        for _,w in r.block_windows(1):
            b=r.read(1,window=w); t+=float(b[(b!=r.nodata)&np.isfinite(b)].sum())
    return t
cen20={'Mabalacat':293244,'Bamban':78260,'Capas':156056}; cen24={'Mabalacat':306594,'Bamban':81012,'Capas':162724}; proj20=520257
for lab_,path in [('id6316_2020',R6),('R2025A_2024',R24)]:
    for bnd,G in [('COD',{r.adm3_name.split()[0]:r.geometry for r in a.itertuples()}),('OSM',{r.name:r.geometry for r in o.itertuples()})]:
        for at in (False,True):
            v=dict(zip(G,zs(path,list(G.values()),at))); rule='all-touched' if at else 'pixel-centre'
            for k,x in v.items(): rec('raster',f'{lab_} {bnd} {rule} {k}','persons',round(x))
            if lab_=='id6316_2020': rec('gate',f'id6316 {bnd} {rule} combined / projection 2020','ratio',round(sum(v.values())/proj20,3))
            else: rec('check',f'R2025A 2024 {bnd} {rule} combined / census 2024','ratio',round(sum(v.values())/sum(cen24.values()),3))
    rec('raster',f'{lab_} national sum','persons',round(natsum(path)))
# barangay share mismatch
d=g4.merge(P,on='psgc'); geoms=list(d.geometry)
d['r25']=zs(R24,geoms,False); d['w6316']=zs(R6,geoms,False)
ob=pd.read_parquet(f'{L}/raw/google/ob_corr.parquet'); d['gob']=[int(shapely.contains_xy(q,ob.longitude.values,ob.latitude.values).sum()) for q in geoms]
xs=[]
for f in ['132303013','132303031']:
    with gzip.open(f'{L}/raw/microsoft/{f}.csv.gz','rt',encoding='utf8') as h:
        for l in h:
            cc=json.loads(l)['geometry']['coordinates'][0]; X=[t[0] for t in cc]; Y=[t[1] for t in cc]
            if 120.2<min(X)<120.65 and 15.15<min(Y)<15.45: xs.append((sum(X)/len(X),sum(Y)/len(Y)))
xs=np.array(xs); d['ms']=[int(shapely.contains_xy(q,xs[:,0],xs[:,1]).sum()) for q in geoms]
for ref in ['total','household']:
    for mun,t in d.groupby('adm3_name'):
        s=t[ref]/t[ref].sum()
        for k in ['r25','w6316','gob','ms']:
            rec('barangay',f'{mun} share mismatch {k} vs {ref}','percent',round(50*float((t[k]/t[k].sum()-s).abs().sum()),1))
for r in a.itertuples():
    rec('buildings',f'{r.adm3_name} Google >=0.65 count','footprints',int(shapely.contains_xy(r.geometry,ob.longitude.values,ob.latitude.values).sum()))
    rec('buildings',f'{r.adm3_name} Microsoft count','footprints',int(shapely.contains_xy(r.geometry,xs[:,0],xs[:,1]).sum()))
csv.writer(open('evidence/results/reproduction_2026-11-02.csv','w',newline='',encoding='utf8')).writerows([('group','metric','unit','value','note')]+out)
