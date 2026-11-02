import requests,time
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/'
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
g=['0305409000','0306902000','0306904000','0300000000','0305400000','0306900000']
for t,gg in [('0221A6DLPD0.px',g),('0031A6DTPH2.px',['0305409000','0306902000','0306904000'])]:
    for f in ['csv','json']:
        time.sleep(4)
        q={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':gg}}],'response':{'format':f}}
        p=s.post(B+t,json=q,timeout=120); print('\n##',t,f,p.status_code,len(p.content)); print(p.content.decode('utf-8','replace')[:2400])
