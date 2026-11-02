"""Walk the PSA OpenSTAT PXWeb tree and list table titles. Rate-limited; keyword search is not supported by this server.
Usage: python -I openstat_catalog.py <out.csv>"""
import csv,sys,time,requests
sys.stdout.reconfigure(encoding='utf8',errors='replace')
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB'; out=[]; errs=[]; w=csv.writer(open(sys.argv[1],'w',newline='',encoding='utf8')); w.writerow(['path','table','title','updated'])
def get(p):
    for t in range(4):
        r=s.get(B+p,timeout=60)
        if r.status_code==200: return r.json()
        if r.status_code==429: time.sleep(15*(t+1)); continue
        errs.append((p,r.status_code)); return None
    errs.append((p,429)); return None
def walk(p,d=0):
    j=get(p); time.sleep(1.1)
    if not isinstance(j,list) or d>4: return
    for e in j:
        q=p+'/'+e['id']
        if e['type']=='l': walk(q,d+1)
        elif e['type']=='t': w.writerow([p,e['id'],e.get('text'),e.get('updated')]); out.append(1)
for e in get(''): print(e['id'],e['text'],flush=True); walk('/'+e['id'])
print('tables',len(out),'errors',errs[:20],len(errs))
