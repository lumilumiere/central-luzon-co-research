import requests,json,sys,re
import geopandas as gpd, pandas as pd
d=sys.argv[1]; s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
a=gpd.read_file(f'{d}/aoi_cod.gpkg')
t=s.get('https://openbuildings-public-dot-gweb-research.uw.r.appspot.com/public/tiles.geojson',timeout=60); open(f'{d}/ob_tiles.geojson','wb').write(t.content)
g=gpd.read_file(f'{d}/ob_tiles.geojson'); print(g.shape,list(g.columns),g.crs)
hit=g[g.intersects(a.union_all())]; print(hit.drop(columns='geometry').to_string())
for r in a.itertuples(): print(r.adm3_name,g[g.intersects(r.geometry)].iloc[:,0].tolist(), 'fully in one tile:',bool((g.contains(r.geometry)).any()))
for tk in hit.iloc[:,0]:
    for base,suf in [('v3/polygons_s2_level_4_gzip','_buildings.csv.gz'),('v3/points_s2_level_4_gzip','_buildings.csv.gz')]:
        u=f'https://storage.googleapis.com/open-buildings-data/{base}/{tk}{suf}'
        h=s.head(u,timeout=40); print(u,h.status_code,h.headers.get('Content-Length'),h.headers.get('Last-Modified'),h.headers.get('Accept-Ranges'))
u='https://storage.googleapis.com/open-buildings-data/v3/score_thresholds_s2_level_4.csv'
r=s.get(u,timeout=40); print(u,r.status_code,len(r.content))
if r.status_code==200:
    import io; c=pd.read_csv(io.BytesIO(r.content)); print(c.columns.tolist()); print(c[c.iloc[:,0].astype(str).isin(hit.iloc[:,0].astype(str))].drop(columns=[x for x in c.columns if 'geometry' in x]).T.to_string())
# Microsoft
def qk(lat,lon,z=9):
    import math
    x=(lon+180)/360; sl=math.sin(math.radians(lat)); y=.5-math.log((1+sl)/(1-sl))/(4*math.pi)
    X=int(x*2**z);Y=int(y*2**z); return ''.join(str(((X>>i)&1)+2*((Y>>i)&1)) for i in range(z-1,-1,-1))
b=a.total_bounds; print('bbox',b); ks={qk(la,lo) for la in (b[1],b[3]) for lo in (b[0],b[2])}; print(ks)
for f in ['ms_links.csv','ms_links_new.csv']:
    m=pd.read_csv(f'{d}/{f}',dtype=str); m=m[m.Location=='Philippines']; print(f,m.shape,m.UploadDate.value_counts().to_dict() if 'UploadDate' in m else '')
    print(m[m.QuadKey.isin(ks)].to_string()[:1500])
# planetary computer
r=s.post('https://planetarycomputer.microsoft.com/api/stac/v1/search',json={'collections':['ms-buildings'],'bbox':[120.3,15.2,120.5,15.3],'limit':5,'query':{'msbuildings:region':{'eq':'Philippines'}}},timeout=60); print('stac',r.status_code)
j=r.json(); print(len(j.get('features',[])),str(j)[:600])
for f in j.get('features',[])[:3]: print(f['id'],f['properties'],list(f['assets']),str(f['assets'].get('data'))[:300])
r=s.get('https://planetarycomputer.microsoft.com/api/sas/v1/token/bingmlbuildings/footprints',timeout=40); print('sas',r.status_code,str(r.text)[:160])
