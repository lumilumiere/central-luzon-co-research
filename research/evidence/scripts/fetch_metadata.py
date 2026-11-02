"""Fetch candidate-source metadata to files and print a compact view. Usage: python -I fetch_metadata.py <out_dir>"""
import json,re,sys,time,requests
o=sys.argv[1]; s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
def save(n,r): open(f'{o}/{n}','wb').write(r.content)
for n,sl in [('kaggle_techsalerator','techsalerator/foot-traffic-and-mobility-data-for-philippines'),('kaggle_smartmobility','ziya07/smart-mobility-traffic-dataset'),('kaggle_pop','jocelyndumlao/philippines-population-projection-2020-to-2025')]:
    r=s.get(f'https://www.kaggle.com/api/v1/datasets/view/{sl}',timeout=40); print(n,r.status_code,len(r.content),r.headers.get('content-type'))
    try:
        j=r.json(); save(n+'.json',r); print({k:(str(v)[:400]) for k,v in j.items() if k.lower() in('title','subtitle','licensename','licenses','totalbytes','lastupdated','creatorname','ownername','usabilityrating','tags','url','downloadcount','viewcount','description','keywords')})
    except Exception as e: print('notjson',r.text[:300])
    q=s.get(f'https://www.kaggle.com/api/v1/datasets/list/{sl}',timeout=40); print(' files',q.status_code,q.text[:900]); open(f'{o}/{n}_files.json','wb').write(q.content)
    time.sleep(1)
for k in ['Mabalacat','Capas','Bamban']:
    r=s.get('https://cmci.dti.gov.ph/lgu-profile.php',params={'lgu':k},timeout=40); save(f'cmci_{k}.html',r)
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',r.text,flags=re.S); t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t); print(k,len(t),t[:1800]); print()
r=s.get('https://huggingface.co/api/datasets/bettergovph/project-noah-hazard-maps',timeout=40); save('hf_noah.json',r); j=r.json(); print({k:str(j.get(k))[:300] for k in ['id','lastModified','tags','cardData','downloads','gated']})
r=s.get('https://huggingface.co/api/datasets/bettergovph/project-noah-hazard-maps/tree/main',timeout=40); print(r.status_code,r.text[:900]); save('hf_noah_tree.json',r)
