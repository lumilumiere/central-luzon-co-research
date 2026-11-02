import json,sys
d=sys.argv[1]
for n in ['cod-ab-phl','philippines-road-surface-data','philippines-population-projection-2020-2025-admin3','cod-ps-phl']:
    p=json.load(open(f'{d}/hdx_{n}.json',encoding='utf8'))['result']
    print('=====',n)
    for k in ['title','dataset_source','organization','dataset_date','last_modified','metadata_modified','license_id','license_title','license_other','data_update_frequency','methodology','methodology_other','caveats','dataset_preview','is_requestdata_type','notes']:
        v=p.get(k)
        if isinstance(v,dict): v=v.get('title')
        if v: print(k,':',str(v)[:900])
    for r in p['resources']:
        print('  R',r.get('name'),'|',r.get('format'),'|',r.get('size'),'|',r.get('last_modified'),'|',r.get('url'))
for l in ['ADM1','ADM2','ADM3']:
    print('=====gb',l); g=json.load(open(f'{d}/gb_{l}.json'))
    for k,v in g.items(): print(k,':',str(v)[:200])
w=json.load(open(f'{d}/wp_6316.json'))
print('=====wp', type(w), list(w)[:5] if isinstance(w,dict) else len(w))
for r in w['data']:
    if str(r.get('popyear'))=='2020' or str(r.get('id'))=='6316': print(json.dumps(r)[:1500])
print('=====pc'); c=json.load(open(f'{d}/pc_ms.json'))
for k in ['id','title','license','msft:short_description','deprecated','description','extent','links','item_assets','assets','msft:container','msft:storage_account','summaries']:
    print(k,':',str(c.get(k))[:900])
