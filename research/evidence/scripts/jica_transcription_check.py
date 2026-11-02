"""Arithmetic checks on the manual transcription of the 2012 JICA survey tables
(evidence/results/jica_2012_transcription.csv, read from rendered pages of jica_1000012767_02.pdf).
Each component pair must sum to its printed total; each run's travel time must equal arrival minus departure;
the printed averages are compared with the mean of the runs. Run from research/: python -I evidence/scripts/jica_transcription_check.py"""
import csv
R = list(csv.DictReader(open('evidence/results/jica_2012_transcription.csv', encoding='utf8')))
v = lambda **k: int(next(r for r in R if all(r[a] == b for a, b in k.items()))['value'])
fails = 0
def eq(label, a, b):
    global fails; ok = a == b; fails += not ok; print('ok  ' if ok else 'FAIL', label, a, b)
for s in ['17', '19', '27', '24']:
    eq(f'station {s} entrance+exit=total', v(station_code=s, entrance_exit='Entrance') + v(station_code=s, entrance_exit='Exit'), v(station_code=s, entrance_exit='Total'))
eq('station 26 SB+NB=total', v(station_code='26', direction='Southbound') + v(station_code='26', direction='Northbound'), v(station_code='26', direction='Total'))
for ee in ['Entrance', 'Exit', 'Total']:
    eq(f'station 28 {ee} SB+NB', v(station_code='28', entrance_exit=ee, direction='Southbound') + v(station_code='28', entrance_exit=ee, direction='Northbound'), v(station_code='28', entrance_exit=ee, direction='Total'))
for d in ['Southbound', 'Northbound', 'Total']:
    eq(f'station 28 entrance+exit {d}', v(station_code='28', entrance_exit='Entrance', direction=d) + v(station_code='28', entrance_exit='Exit', direction=d), v(station_code='28', entrance_exit='Total', direction=d))
sec = lambda t: (lambda h, m, s: 3600 * h + 60 * m + s)(*map(int, t.split(':')))
runs = [r for r in R if r['table'] == '5.5-1' and r['station_code'].startswith('run')]
for r in runs:
    dep, arr = r['note'].split(';')[0].replace('departure ', '').split(' arrival ')
    eq(f"{r['station_code']} arrival-departure", (sec(arr) - sec(dep)) % 86400, sec(r['value']))
for d in ['EDSA to Clark Airport', 'Clark Airport to EDSA']:
    m = sum(sec(r['value']) for r in runs if r['direction'] == d) / sum(r['direction'] == d for r in runs)
    printed = sec(next(r for r in R if r['station_code'] == 'avg' and r['direction'] == d)['value'])
    print('info', d, 'mean of runs', f'{int(m)//3600}:{int(m)%3600//60:02d}:{int(m)%60:02d}', 'printed', printed, 'diff s', round(printed - m))
print('transcription arithmetic failures:', fails)
