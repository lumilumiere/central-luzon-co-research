import requests,json
s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0'
r=s.get('https://hub.worldpop.org/rest/data/pop',timeout=60); j=r.json()
for e in j['data']: print(e.get('alias'),'|',e.get('name'))
