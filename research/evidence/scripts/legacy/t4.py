import requests,json,re,sys,time,os
import geopandas as gpd
from shapely.geometry import Polygon,Point
d=sys.argv[1]; s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0 (research access check)'
a=gpd.read_file(f'{d}/aoi_cod.gpkg')
# geofabrik poly
t=s.get('https://download.geofabrik.de/asia/philippines.poly',timeout=60); print('poly',t.status_code,len(t.text))
rings=[];cur=None
for l in t.text.splitlines()[1:]:
    p=l.split()
    if len(p)==1 and p[0]!='END': cur=[]
    elif len(p)==2: cur.append((float(p[0]),float(p[1])))
    elif p==['END'] and cur is not None: rings.append(Polygon(cur)); cur=None
print('rings',len(rings),[r.bounds for r in rings][:3])
for r in a.itertuples(): print(r.adm3_name,'within extract poly:',any(q.contains(r.geometry) for q in rings))
# pbf header
h=s.get('https://download.geofabrik.de/asia/philippines-latest.osm.pbf',headers={'Range':'bytes=0-4095'},timeout=60); print('pbf',h.status_code,len(h.content))
import zlib
b=h.content; n=int.from_bytes(b[:4],'big'); print(b[4:4+n][:40]); blob=b[4+n:]
print(re.findall(rb'[ -~]{6,}',b[:600])); 
m=re.search(rb'\x78[\x9c\x01\xda]',blob)
try:
    raw=zlib.decompressobj().decompress(blob[m.start():]); print(re.findall(rb'[ -~]{6,}',raw))
except Exception as e: print('z',e)
# geofabrik page
g=s.get('https://download.geofabrik.de/asia/philippines.html',timeout=60).text
print(re.sub(r'<[^>]+>',' ',g)[:1400])
