"""Compare OSM and Overture counts for selected brands inside the same COD-AB polygons.
Matching is a case-insensitive pattern on name and brand. Usage: python -I brand_compare.py <aoi_cod.gpkg> <osm_poi.json> <overture.parquet> <out.csv>"""
import json,re,sys
import geopandas as gpd,pandas as pd,shapely
sys.stdout.reconfigure(encoding='utf8',errors='replace')
a=gpd.read_file(sys.argv[1]); J=json.load(open(sys.argv[2],encoding='utf8')); o=pd.read_parquet(sys.argv[3])
x=[]
for e in J['elements']:
    c=e.get('center') or e; t=e.get('tags',{})
    if 'lon' in c: x.append((c['lon'],c['lat'],(t.get('name','')+' '+t.get('brand','')).lower()))
s=pd.DataFrame(x,columns=['x','y','t']); o['t']=(o['name'].fillna('')+' '+o.brand.fillna('')).str.lower()
B={'7-Eleven':r'7[- ]?eleven','Jollibee':r'jollibee',"McDonald's":r"mcdonald",'Chowking':r'chowking','Mang Inasal':r'mang inasal','Greenwich':r'greenwich','KFC':r'\bkfc\b','Puregold':r'puregold','Mercury Drug':r'mercury drug','Alfamart':r'alfamart'}
r=[]
for u in a.itertuples():
    p=s[shapely.contains_xy(u.geometry,s.x.values,s.y.values)]; q=o[shapely.contains_xy(u.geometry,o.x.values,o.y.values)]
    for b,k in B.items():
        r.append(dict(unit=u.adm3_name,brand=b,osm=int(p.t.str.contains(k,regex=True).sum()),overture=int(q.t.str.contains(k,regex=True).sum()),overture_conf_ge_0_8=int((q.t.str.contains(k,regex=True)&(q.confidence>=.8)).sum())))
d=pd.DataFrame(r); d.to_csv(sys.argv[4],index=False); print(d.pivot(index='brand',columns='unit',values=['osm','overture','overture_conf_ge_0_8']).to_string()); print(d.groupby('brand')[['osm','overture','overture_conf_ge_0_8']].sum().to_string())
