import sys,json,re,pandas as pd
d=pd.read_excel(sys.argv[1],header=None,dtype=str)
print(d.iloc[:3].T.to_string(max_colwidth=50))
print('PHL row full'); r=d.iloc[175]
for i,v in r.items(): print(i,repr(v))
print(d.iloc[175+1:].dropna(how='all').tail(4).iloc[:,:3].to_string()[:600])
j=json.load(open(sys.argv[2],encoding='utf8')); v=[x for x in j['variables'] if 'Geographic' in x['code']][0]
print({k:t for k,t in zip(v['values'],v['valueTexts']) if re.search(r'^(\W*)(PHILIPPINES|Philippines|Angeles|Region III|Central Luzon|Tarlac|Pampanga)',t.strip(),re.I)})
