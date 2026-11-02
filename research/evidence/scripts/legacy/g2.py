import sys,pandas as pd
f=sys.argv[1]; x=pd.ExcelFile(f); print(x.sheet_names)
for n in x.sheet_names:
    d=x.parse(n,header=None,dtype=str); print('##',n,d.shape); print(d.head(4).to_string(max_colwidth=60)[:1500])
    m=d[d.apply(lambda r:r.astype(str).str.contains(r'\bPHL\b|Philippines',regex=True).any(),axis=1)]
    for i,r in m.iterrows():
        print('ROW',i,{(str(d.iloc[0,k]) if str(d.iloc[0,k])!='nan' else k):v for k,v in r.items() if str(v)!='nan'})
