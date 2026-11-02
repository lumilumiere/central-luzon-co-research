"""Copy the volatile, redistributable inputs behind material results from local-data/ into evidence/inputs/,
then check that the packed copies reproduce the published figures.
Volatile = a live endpoint (Overpass) or a re-uploaded source (Microsoft) that cannot return the same bytes later.
Versioned downloads (WorldPop, Google v3, COD-AB full file, NOAH, DEM) are not packed; the manifest holds their URLs and SHA-256.
PSA tables are not packed: their reuse terms are unread (blocker B-03).
Naming rule: the assignment keeps agency and project-brand names out of outputs. The names are passed at run time
(EXCLUDED_TERMS, semicolon-separated) so the script itself does not carry them; text that contains one is reduced or blanked.
Run from research/: EXCLUDED_TERMS='...' python -I evidence/scripts/pack_inputs.py"""
import csv, gzip, hashlib, json, os, shutil, sys
import geopandas as gpd, numpy as np, pandas as pd, shapely

TERMS = [t.strip().lower() for t in os.environ.get('EXCLUDED_TERMS', '').split(';') if t.strip()]
if not TERMS: sys.exit('set EXCLUDED_TERMS')
has = lambda s: any(t in s.lower() for t in TERMS)
L, O = 'local-data/raw', 'evidence/inputs'
COPY = ['osm/osm_rel.json', 'osm/aoi_osm.gpkg', 'osm/osm_poi.json', 'cod/aoi_cod.gpkg', 'cod/aoi_cod_adm4.gpkg']
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
for f in COPY:
    os.makedirs(os.path.dirname(f'{O}/{f}'), exist_ok=True); shutil.copyfile(f'{L}/{f}', f'{O}/{f}')
    assert sha(f'{L}/{f}') == sha(f'{O}/{f}'), f
# Overpass ways: keep only what directed_connectivity.py reads (ids, node lists, highway/oneway/junction tags).
J = json.load(open(f'{L}/osm/osm_ways_body_2026-11-02.json', encoding='utf8'))
keep = ('highway', 'oneway', 'junction')
J['elements'] = [{'type': w['type'], 'id': w['id'], 'nodes': w['nodes'], 'tags': {k: v for k, v in w.get('tags', {}).items() if k in keep}} for w in J['elements']]
json.dump(J, open(f'{O}/osm/osm_ways_topology_2026-11-02.json', 'w', encoding='utf8'), separators=(',', ':'))
# Overture places: blank name or brand cells that carry an excluded term (row counts and coordinates unchanged).
p = pd.read_parquet(f'{L}/overture/overture_places_corridor.parquet')
for c in ('name', 'brand'):
    hit = p[c].fillna('').map(has); print(f'overture {c} cells blanked:', int(hit.sum())); p.loc[hit, c] = None
os.makedirs(f'{O}/overture', exist_ok=True); p.to_parquet(f'{O}/overture/overture_places_corridor_redacted.parquet', index=False)
# Microsoft: keep only the lines reproduce_core.py keeps (same bbox filter), byte-identical lines.
os.makedirs(f'{O}/microsoft', exist_ok=True); xs = []
for q in ['132303013', '132303031']:
    with gzip.open(f'{L}/microsoft/{q}.csv.gz', 'rt', encoding='utf8') as h, \
         gzip.GzipFile(f'{O}/microsoft/{q}.corridor.csv.gz', 'wb', mtime=0) as g:
        for l in h:
            cc = json.loads(l)['geometry']['coordinates'][0]; X = [t[0] for t in cc]; Y = [t[1] for t in cc]
            if 120.2 < min(X) < 120.65 and 15.15 < min(Y) < 15.45:
                g.write(l.encode('utf8')); xs.append((sum(X) / len(X), sum(Y) / len(Y)))
xs = np.array(xs)

# Check 1: Microsoft counts per municipality from the packed subset equal the reproduction table.
pub = {r['metric']: r['value'] for r in csv.DictReader(open('evidence/results/reproduction_2026-11-02.csv', encoding='utf8'))}
for r in gpd.read_file(f'{O}/cod/aoi_cod.gpkg').itertuples():
    n = int(shapely.contains_xy(r.geometry, xs[:, 0], xs[:, 1]).sum()); k = f'{r.adm3_name} Microsoft count'
    assert str(n) == pub[k], (k, n, pub[k]); print('ok', k, n)
# Check 2: the packed Overpass ways carry the snapshot timestamp cited in the results.
J = json.load(open(f'{O}/osm/osm_ways_topology_2026-11-02.json', encoding='utf8'))
assert J['osm3s']['timestamp_osm_base'] == '2026-11-02T08:01:36Z'; print('ok overpass snapshot', J['osm3s']['timestamp_osm_base'])
# Check 3: no excluded term in packed text (JSON, GeoPackage, gzip text, and the parquet's text columns;
# parquet ids are hexadecimal UUIDs and are not text names).
for root, _, fs in os.walk(O):
    for f in fs:
        a = os.path.join(root, f)
        if a.endswith('.parquet'):
            q = pd.read_parquet(a); bad = [c for c in ('name', 'brand', 'cat', 'src') if q[c].fillna('').map(has).any()]
        else:
            raw = gzip.open(a).read() if a.endswith('.gz') else open(a, 'rb').read(); bad = has(raw.decode('utf8', 'replace'))
        assert not bad, (a, bad)
print('ok excluded terms absent from packed text')
print('raw sources:', {f: sha(f'{L}/{f}') for f in ['osm/osm_ways_body_2026-11-02.json', 'overture/overture_places_corridor.parquet']})
for root, _, fs in os.walk(O):
    for f in sorted(fs):
        p = os.path.join(root, f).replace(os.sep, '/'); print(p, os.path.getsize(p), sha(p))
