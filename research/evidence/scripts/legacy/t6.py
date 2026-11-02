import requests,json,time,re
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB'
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
hits=[];n=0
def walk(p,depth=0):
    global n
    if depth>4: return
    r=s.get(B+p,timeout=40); n+=1
    if r.status_code!=200: print('ERR',r.status_code,p); time.sleep(1); return
    try: j=r.json()
    except: return
    if not isinstance(j,list): return
    for e in j:
        q=p+'/'+e['id']
        if e['type']=='l': 
            walk(q,depth+1); time.sleep(.15)
        elif re.search(r'popul|census|household',e['text'],re.I): hits.append((q,e['text']))
r=s.get(B,timeout=40); top=r.json(); print([ (e['id'],e['text']) for e in top])
for e in top:
    if re.search(r'popul|demog|census',e['text'],re.I): walk('/'+e['id'])
print(n)
for h in hits: print(h)
