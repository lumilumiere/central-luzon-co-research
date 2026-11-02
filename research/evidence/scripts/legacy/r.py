c20=dict(M=293244,B=78260,C=156056,A=462928); c24=dict(M=306594,B=81012,C=162724,A=483452); p20=dict(M=288295,B=76808,C=155154)
N20,N24=109033245,112727776
w=dict(COD_c=dict(M=161117,B=66328,C=132000,A=247647),COD_t=dict(M=168365,B=67636,C=134184),OSM_c=dict(M=209274,B=70807,C=134291),OSM_t=dict(M=212208,B=72032,C=135764))
for k,v in w.items():
    s=v['M']+v['B']+v['C']
    print(k,'sum',s,'/census',round(s/527560,3),'/proj',round(s/520257,3),{u:(round(v[u]/c20[u],3),round(v[u]/p20[u],3)) for u in 'MBC'})
print('Mab+Ang id6316',161117+247647,round((161117+247647)/(293244+462928),3),'Ang',round(247647/462928,3))
print('nat 6316',round(110194183/N20,4))
print('Pampanga incl Angeles',round(2637218/(2437709+462928),3),'Tarlac',round(1361480/1503456,3),'R3',round(11483752/12422172,3))
print('rest of Pampanga',2637218-161117-247647,2437709-293244,round((2637218-161117-247647)/(2437709-293244),3))
print('rest of Tarlac',1361480-66328-132000,1503456-78260-156056,round((1361480-66328-132000)/(1503456-78260-156056),3))
import sys
for y,n,N,c,r in ((2020,111467164,N20,c20,dict(M=296492,B=80015,C=159555,A=476635)),(2024,115359880,N24,c24,dict(M=306846,B=82809,C=165127,A=None))):
    f=n/N; print(y,'nat factor',round(f,4),{u:(round(r[u]/c[u],4),round(r[u]/c[u]/f,4)) for u in r if r[u]})
    if r['A']: print('  M+A',r['M']+r['A'],round((r['M']+r['A'])/(c['M']+c['A']),4),round((r['M']+r['A'])/(c['M']+c['A'])/f,4))
print('LMB M+A',166.80+63.43,'COD M+A',97.548+121.029,round((97.548+121.029)/(166.80+63.43),3),'Ang COD/LMB',round(121.029/63.43,3))
print('mapillary pred %',round(62.3/1477.2*100,1),round(3.9/674.5*100,1))
print('OSM gaps M',343258-306846,331613-296492)
