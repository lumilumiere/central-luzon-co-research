"""Record an HTTP access test for each candidate source. Plain GET, one attempt, no retries or bypass.
Usage: python -I access_tests.py <urls.tsv> <out.csv>"""
import csv,sys,time,requests
from datetime import datetime,timezone
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
rows=[]
for l in open(sys.argv[1],encoding='utf8'):
    l=l.strip()
    if not l or l.startswith('#'): continue
    k,u=l.split('\t')[:2]; t=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    try:
        r=s.get(u,timeout=30,stream=True,allow_redirects=True); b=r.raw.read(2048,decode_content=True) if r.status_code<400 else b''
        rows.append((k,u,t,'GET',r.status_code,r.url if r.url!=u else '',r.headers.get('Content-Type','')[:50],r.headers.get('Content-Length',''),r.headers.get('Last-Modified',''),''))
        r.close()
    except Exception as e: rows.append((k,u,t,'GET','ERR','','','','',type(e).__name__))
    print(rows[-1][0],rows[-1][4],rows[-1][7],rows[-1][9],flush=True); time.sleep(.4)
w=csv.writer(open(sys.argv[2],'w',newline='',encoding='utf8')); w.writerow(['key','url','tested_utc','method','status','final_url','content_type','content_length','last_modified','error']); w.writerows(rows)
