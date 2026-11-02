"""Inspect the two Kaggle bundles named in checklist rows 6.1 and 6.2. Usage: python -I inspect_kaggle.py <kaggle_dir>"""
import hashlib,io,sys,zipfile,re
import pandas as pd
d=sys.argv[1]
for n in ['tech','smart']:
    b=open(f'{d}/{n}.zip','rb').read(); print('##',n,len(b),hashlib.sha256(b).hexdigest())
z=zipfile.ZipFile(f'{d}/tech.zip')
p='Mashvisor_Enterprise_Sample_Data/Mashvisor_Enterprise_Sample_Data/'
print(z.read(p+'Mashvisor_Enterprise_Sample_Data_README.md').decode('utf8','replace')[:1300])
for f in ['Property_and_Comps_Snapshot.csv','STR_Monthly_Performance_ZIP.csv']:
    c=pd.read_csv(io.BytesIO(z.read(p+f))); print(f,c.shape,list(c.columns)[:25]); print(c.head(2).T.to_string()[:900])
    txt=' '.join(c.astype(str).fillna('').values.ravel().tolist()); print('philippines mentions',len(re.findall('philippin|manila|tarlac|pampanga',txt,re.I)))
    for col in c.columns:
        if re.search('state|city|zip',col,re.I): print(col,c[col].astype(str).value_counts().head(5).to_dict())
for f in [x for x in z.namelist() if x.endswith('.json')]:
    t=z.read(f).decode('utf8','replace'); print(f,len(t),'PH mentions',len(re.findall('philippin|manila|tarlac|pampanga',t,re.I)),t[:220])
print([x for x in z.namelist() if x.endswith('.png')])
s=pd.read_csv(io.BytesIO(zipfile.ZipFile(f'{d}/smart.zip').read('smart_mobility_dataset.csv'))); print(s.shape,list(s.columns)); print(s.describe(include='all').T.iloc[:,:8].to_string()[:2600])
print(s.iloc[:,0:3].head(3).to_string())
for c in ['Latitude','Longitude']:
    if c in s: print(c,s[c].min(),s[c].max())
