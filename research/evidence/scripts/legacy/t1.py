import pandas as pd, sys
d=sys.argv[1]
x=pd.ExcelFile(f'{d}/cod_ab.xlsx'); print(x.sheet_names)
for s in x.sheet_names:
    df=x.parse(s); 
    print('---',s,df.shape,list(df.columns)[:30])
    c=[k for k in df.columns if str(k).lower() in('adm3_name','adm3_en','adm3_pcode')]
    if any('adm3' in str(k).lower() for k in df.columns):
        nc=[k for k in df.columns if 'adm3' in str(k).lower() and ('name' in str(k).lower() or '_en' in str(k).lower())]
        if nc:
            m=df[df[nc[0]].astype(str).str.contains(r'^(?:Capas|Bamban|Mabalacat|City of Mabalacat|Mabalacat City)',case=False,regex=True)]
            print(m.iloc[:8].T.dropna().to_string()[:3500])
x=pd.ExcelFile(f'{d}/proj.xlsx'); print(x.sheet_names)
for s in x.sheet_names:
    df=x.parse(s,header=None); print('---',s,df.shape); print(df.head(8).to_string()[:1800])
    m=df[df.apply(lambda r:r.astype(str).str.contains(r'Capas|Bamban|Mabalacat',case=False).any(),axis=1)]
    print(m.to_string()[:2500])
