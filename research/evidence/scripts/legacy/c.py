import re,sys
d=sys.argv[1]
for k in ['Mabalacat','Capas','Bamban']:
    h=open(f'{d}/cmci_{k}.html',encoding='utf8',errors='replace').read()
    h=re.sub(r'<select.*?</select>','',h,flags=re.S); h=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S); t=re.sub(r'<[^>]+>',' ',h); t=re.sub(r'\s+',' ',t); i=t.find('You are here'); print(k,len(t),t[i:i+1500]); print()
h=open(f'{d}/cmci_Mabalacat.html',encoding='utf8',errors='replace').read(); print(re.findall(r'<script[^>]*src="([^"]+)"',h)[:12]); print(re.findall(r'(\w+\.php[^"\' ]*)',h)[:30])
