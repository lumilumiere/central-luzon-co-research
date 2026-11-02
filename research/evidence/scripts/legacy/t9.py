import requests,time,json,sys
B='https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/'
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
q={'query':[{'code':'Geographic Location','selection':{'filter':'item','values':['0305409000','0306902000','0306904000']}}],'response':{'format':'px'}}
p=s.post(B+'0221A6DLPD0.px',json=q,timeout=120); print(p.status_code); t=p.content.decode('utf-8','replace')
i=t.find('DATA='); print(t[:i][:3500])
d=sys.argv[1]
s2=requests.Session(); s2.headers['User-Agent']='Mozilla/5.0'
for al in ['G2_CN_POP_R25A_100m','cic2020_100m','G2_UC_POP_R24B_100m','G2_CN_POP_R24B_100m','G2_CN_POP_2024_100m']:
    r=s2.get(f'https://hub.worldpop.org/rest/data/pop/{al}?iso3=PHL',timeout=60); j=r.json().get('data',[])
    print('\n##',al,r.status_code,len(j),[x.get('popyear') for x in j][:20])
    for x in j:
        if str(x.get('popyear')) in ('2020','2024'):
            print({k:x.get(k) for k in ['id','title','doi','date','popyear','category','data_file','url_summary','license','notes']}, str(x.get('desc'))[:300], x.get('files'))
