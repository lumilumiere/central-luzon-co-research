"""Corridor store and POI test: OSM via Overpass, Overture places and buildings via DuckDB range reads.
Usage: python -I stores_poi.py <aoi_cod.gpkg> <out_dir>"""
import json,re,sys,hashlib,requests
import geopandas as gpd,pandas as pd,shapely
a=gpd.read_file(sys.argv[1]); o=sys.argv[2]
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
BR=r"jollibee|mcdonald|chowking|mang inasal|greenwich|kfc|7-eleven|7 eleven|alfamart|puregold|ministop|lawson|dali|savemore|waltermart|mercury drug|generika|tgp|the generics|red ribbon|goldilocks|starbucks|shakey|max's|bonchon|potato corner|angel's burger|minute burger|burger king|jco|dunkin|julie's|tokyo tokyo|andok|baliwag|cebuana|palawan|bdo|bpi|landbank|petron|shell|caltex|seaoil|phoenix"
Q='[out:json][timeout:110];(nwr["shop"](15.16,120.24,15.43,120.64);nwr["amenity"~"^(restaurant|fast_food|cafe|pharmacy|bank|fuel|marketplace)$"](15.16,120.24,15.43,120.64);nwr["brand"](15.16,120.24,15.43,120.64););out tags center;'
r=None
for ep in ['https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter']:
    r=s.post(ep,data={'data':Q},timeout=125); print(ep,r.status_code,len(r.content))
    if r.status_code==200 and r.content[:1]==b'{': break
J=r.json(); open(f'{o}/osm_poi.json','wb').write(r.content); print(J['osm3s'].get('timestamp_osm_base'),hashlib.sha256(r.content).hexdigest())
rows=[]
for e in J['elements']:
    c=e.get('center') or e; t=e.get('tags',{})
    rows.append(dict(lon=c.get('lon'),lat=c.get('lat'),name=t.get('name',''),brand=t.get('brand',''),shop=t.get('shop',''),amenity=t.get('amenity','')))
df=pd.DataFrame(rows).dropna(subset=['lon','lat']); txt=(df.name+' '+df.brand).str.lower(); df['branded']=txt.str.contains(BR,regex=True); df['has_brand_tag']=df.brand!=''
res=[]
for p in a.itertuples():
    q=df[shapely.contains_xy(p.geometry,df.lon.values,df.lat.values)]
    food=q.amenity.isin(['restaurant','fast_food','cafe']); shop=q['shop']!=''
    res.append(dict(unit=p.adm3_name,source='OSM',total=len(q),food_service=int(food.sum()),shops=int(shop.sum()),brand_tag=int(q.has_brand_tag.sum()),name_matches_brand_list=int(q.branded.sum())))
    print(res[-1])
pd.DataFrame(res).to_csv(f'{o}/osm_poi_counts.csv',index=False)
print(df[shapely.contains_xy(a.union_all(),df.lon.values,df.lat.values)&df.branded].assign(k=lambda x:(x.brand.where(x.brand!='',x.name)).str.lower()).k.value_counts().head(25).to_dict())
