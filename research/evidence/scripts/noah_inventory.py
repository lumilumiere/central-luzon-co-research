"""List NOAH hazard files for the two provinces on the Hugging Face mirror and read its card. Usage: python -I noah_inventory.py <out_dir>"""
import sys; sys.stdout.reconfigure(encoding='utf8',errors='replace')
import json,sys,requests,urllib.parse as U
o=sys.argv[1]; s=requests.Session(); s.headers['User-Agent']='geo-access-check/0.1'
B='https://huggingface.co/api/datasets/bettergovph/project-noah-hazard-maps/tree/main'
def tree(p):
    r=s.get(f'{B}/{U.quote(p)}',timeout=40); r.raise_for_status(); return r.json()
rows=[]
for top in ['Flood','Landslide','Storm Surge']:
    for e in tree(top):
        print(top,e['type'],e['path'],e.get('size'))
        if e['type']=='directory':
            for f in tree(e['path']):
                nm=f['path']
                if f['type']=='directory':
                    if any(k in nm for k in('Tarlac','Pampanga','Region','Luzon','III','Province')): 
                        for g in tree(nm):
                            if any(k in g['path'] for k in('Tarlac','Pampanga')): rows.append(g)
                elif any(k in nm for k in('Tarlac','Pampanga','PH')): rows.append(f)
for g in rows: print(g['type'],g.get('size'),g['path'],g.get('lfs',{}).get('oid'))
json.dump(rows,open(f'{o}/hf_noah_province_files.json','w'))
r=s.get('https://huggingface.co/datasets/bettergovph/project-noah-hazard-maps/raw/main/README.md',timeout=40); open(f'{o}/hf_noah_README.md','wb').write(r.content); print(r.text[:3500])
r=s.get('https://huggingface.co/datasets/bettergovph/project-noah-hazard-maps/resolve/main/NOAH_License.pdf',timeout=60); open(f'{o}/NOAH_License.pdf','wb').write(r.content); print(r.status_code,len(r.content))
