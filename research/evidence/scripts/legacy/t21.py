c20={'Mab':293244,'Bam':78260,'Cap':156056}; c24={'Mab':306594,'Bam':81012,'Cap':162724}
p20={'Mab':288295,'Bam':76808,'Cap':155154}; p24={'Mab':314076,'Bam':81240,'Cap':164171}
w18={'Mab':161117,'Bam':66328,'Cap':132000}; wc20={'Mab':160557,'Bam':66035,'Cap':132437}
r20={'Mab':296492,'Bam':80015,'Cap':159555}; r24={'Mab':306846,'Bam':82809,'Cap':165127}
def t(n,a,b): print(n,{k:round(a[k]/b[k],3) for k in a},'sum',sum(a.values()),'/',sum(b.values()),round(sum(a.values())/sum(b.values()),3))
t('wp2018/c20',w18,c20);t('wpC2020/c20',wc20,c20);t('R25 2020/c20',r20,c20);t('R25 2024/c24',r24,c24);t('proj20/c20',p20,c20);t('proj24/c24',p24,c24);t('wp2018/proj20',w18,p20)
s={'Mab':(1477.2,438.6,161.6),'Bam':(674.5,171.3,26.6),'Cap':(992.7,192.2,0)}
for k,(a,b,c) in s.items(): print(k,'classified %',round(100*b/a,1),'AI %',round(100*c/a,1))
print('MS/GOB',{k:round(a/b,3) for k,a,b in [('Mab',29753,95257),('Bam',17737,37523),('Cap',35920,76827)]})
print('MS total',29753+17737+35920,'GOB total',95257+37523+76827)
print('tile prec80 share',{k:round(a/b,3) for k,a,b in [('Mab',56638,95257),('Bam',22079,37523),('Cap',44357,76827)]})
print('nat WP vs census 2020',round(110194183/109035343,3) )
print('COD vs LMB',{k:round(a/b,3) for k,a,b in [('Mab',97.548,166.80),('Bam',207.478,344.14),('Cap',446.479,448.04)]})
print('OSM vs LMB',{k:round(a/b,3) for k,a,b in [('Mab',149.66,166.80),('Bam',177.48,344.14),('Cap',440.8,448.04)]})
print('sums',97.548+207.478+446.479,149.66+177.48+440.8,166.80+344.14+448.04)
