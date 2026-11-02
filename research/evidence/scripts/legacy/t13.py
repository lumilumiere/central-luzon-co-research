import gzip,json,sys,requests,re
import numpy as np, geopandas as gpd, pandas as pd, shapely
from shapely.geometry import shape
d=sys.argv[1]; a=gpd.read_file(f'{d}/aoi_cod.gpkg'); au=a.to_crs(32651)
rows=[];n=0;keys={};firsts=[]
for q in ['132303013','132303031']:
    with gzip.open(f'{d}/ms/{q}.csv.gz','rt',encoding='utf8') as f:
        for l in f:
            n+=1
            j=json.loads(l)
            if len(firsts)<2: firsts.append(l[:400])
            p=j.get('properties',{})
            for k in p: keys[k]=keys.get(k,0)+1
            c=j['geometry']['coordinates'][0]; xs=[x[0] for x in c]; ys=[x[1] for x in c]
            if 120.2<min(xs)<120.65 and 15.15<min(ys)<15.45:
                rows.append((sum(xs)/len(xs),sum(ys)/len(ys),p.get('height'),p.get('confidence'),json.dumps(j['geometry'])))
print('total rows',n,keys); print(firsts)
df=pd.DataFrame(rows,columns=['x','y','height','conf','g'])
gs=gpd.GeoSeries([shape(json.loads(x)) for x in df.g],crs=4326); df['area']=gs.to_crs(32651).area.values
for r in a.itertuples():
    m=shapely.contains_xy(r.geometry,df.x.values,df.y.values); s=df[m]
    print(r.adm3_name,'MS count',len(s),'area_km2',round(s.area.sum()/1e6,2),'median_m2',round(s.area.median(),1),'conf==-1',int((s.conf==-1).sum()),'conf dist',s.conf[s.conf>=0].describe().round(3).to_dict() if (s.conf>=0).any() else None,'height -1',int((s.height==-1).sum()),'h>0',int((s.height>0).sum()),'h stats',s.height[s.height>0].describe().round(2).to_dict())
print('invalid sample',int((~gs.iloc[:20000].is_valid).sum()))
