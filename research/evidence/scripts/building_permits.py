"""PSA approved building permits, annual, 2022-2024, for the corridor.
Fetches all geographies, then filters and derives pesos per m2. Value is inferred as thousand pesos.
Usage: python -I building_permits.py <raw_out.csv> <filtered_out.csv>"""
import csv,io,re,sys,requests
U='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/2G/CONS/BGP/0022G4GBPC1.px'
q={'query':[{'code':'Period','selection':{'filter':'item','values':['0']}},{'code':'Geolocation','selection':{'filter':'all','values':['*']}}],'response':{'format':'csv'}}
r=requests.post(U,json=q,headers={'User-Agent':'geo-access-check/0.1'},timeout=180); r.raise_for_status()
t=r.content.decode('latin-1'); open(sys.argv[1],'w',encoding='utf8').write(t)
rows=[x for x in csv.reader(io.StringIO(t)) if len(x)>5][1:]
K=r'^(Tarlac|Pampanga|Capas|Bamban|Mabalacat City|City of Angeles|Philippines|Region III.*)$'
num=lambda a: float(a) if re.match(r'^-?[0-9.]+$',a) else None
per=lambda v,a: round(v*1000/a) if v and a else ''
out=[['year','geography','total_number','total_floor_area_m2','total_value_thousand_php','php_per_m2_total','res_number','res_floor_area_m2','res_value_thousand_php','nonres_number','nonres_floor_area_m2','nonres_value_thousand_php','php_per_m2_nonres']]
for x in rows:
    n=x[2].strip(' .')
    if re.match(K,n,re.I):
        v=[num(a) for a in x[3:12]]; out.append([x[0],n,v[0],v[1],v[2],per(v[2],v[1]),v[3],v[4],v[5],v[6],v[7],v[8],per(v[8],v[7])])
csv.writer(open(sys.argv[2],'w',newline='')).writerows(out); print(len(out)-1)
