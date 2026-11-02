import json,re,sys,requests,zipfile,io,os
d=sys.argv[1]
j=json.load(open(f'{d}/kaggle_techsalerator_files.json',encoding='utf8')); print(len(j['datasetFiles']))
for f in j['datasetFiles']: print(f['totalBytes'],f['name'],f.get('creationDate'))
t=json.load(open(f'{d}/kaggle_techsalerator.json',encoding='utf8')); print(t.get('description')[:3200]); print(t.get('currentVersionNumber'),t.get('ref'),[ (v.get('versionNumber'),v.get('creationDate')) for v in t.get('versions',[])][:5])
s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
os.makedirs(f'{d}/kaggle',exist_ok=True)
for n,sl in [('tech','techsalerator/foot-traffic-and-mobility-data-for-philippines'),('smart','ziya07/smart-mobility-traffic-dataset')]:
    r=s.get(f'https://www.kaggle.com/api/v1/datasets/download/{sl}',timeout=120,allow_redirects=True); print(n,r.status_code,len(r.content),r.headers.get('content-type'),r.url[:90])
    if r.status_code==200 and r.content[:2]==b'PK':
        open(f'{d}/kaggle/{n}.zip','wb').write(r.content); z=zipfile.ZipFile(io.BytesIO(r.content)); print(z.namelist()[:20])
for k in ['Mabalacat','Capas','Bamban']:
    h=open(f'{d}/cmci_{k}.html',encoding='utf8',errors='replace').read(); h=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S); h=re.sub(r'<option.*?</option>','',h,flags=re.S); t=re.sub(r'<[^>]+>',' ',h); t=re.sub(r'\s+',' ',t); i=t.find('Select LGU'); print(k,t[i:i+2600]); print()
