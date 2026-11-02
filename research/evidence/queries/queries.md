# Queries behind material results — Central Luzon industrial district POC

Each query is also embedded in the script named, which is the authoritative copy. Observation times are UTC unless marked PHT.

## Overpass (OSM)

| Use | Endpoint | Query | Observed snapshot | Saved response |
|---|---|---|---|---|
| Directed connectivity | `https://overpass-api.de/api/interpreter`, with two fallbacks in the script | [`overpass_directed_connectivity.txt`](overpass_directed_connectivity.txt) | `timestamp_osm_base` 2026-11-02T08:01:36Z | Reduced copy [`../inputs/osm/osm_ways_topology_2026-11-02.json`](../inputs/osm/osm_ways_topology_2026-11-02.json). The full response is local, SHA-256 `5f5a5580f9d38e14278e4e167bc01fa98151b9dfca86090c5ecb145ffe333a1b` |
| Store and amenity counts | Same | In `../scripts/stores_poi.py` (`nwr["shop"]`, selected `amenity` values and `nwr["brand"]` in bbox 15.16,120.24,15.43,120.64; `out tags center`) | 2026-11-02 | [`../inputs/osm/osm_poi.json`](../inputs/osm/osm_poi.json) |
| Municipal relations | Same | In `../scripts/legacy/v1.py` | 2026-11-02 | [`../inputs/osm/osm_rel.json`](../inputs/osm/osm_rel.json) |

Overpass always answers with current data. Rerunning a query gives a newer snapshot, so the saved responses are the reproducible inputs.

## ohsome (OSM history)

- **Script:** `../scripts/legacy/t10.py`, which calls `POST https://api.ohsome.org/v1/elements/length/groupBy/boundary`.
- **Inputs:** `bpolys` are the COD-AB municipal polygons simplified at 0.0002°. The drivable filter is in the script.
- **Time:** the script sent no `time` parameter, so ohsome used its latest data, timestamped 2026-07-27 in session extract L0421.
- **To reproduce:** add `time=2026-07-27` to each request. ohsome serves history, so the same snapshot can be requested again while the service runs.
- **Status:** logged result; not rerun in this pass.

## PSA OpenSTAT (PXWeb API)

| Table | Endpoint | Body | Local response SHA-256 (not committed, B-03) |
|---|---|---|---|
| `0031A6DTPH2`, 2024 barangay population | `POST https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0031A6DTPH2.px` | `{"query":[{"code":"Geographic Location","selection":{"filter":"item","values":[<barangay codes for prefix>]}}],"response":{"format":"csv"}}`, one call each for prefixes 0305409, 0306902 and 0306904 (`../scripts/barangay_distribution_test.py`) | Manifest rows E0162–E0164 (full hashes) |
| `0221A6DLPD0`, 2020 census and land area | `POST …/DB/1A/PO_2024/0221A6DLPD0.px` | Same form with municipal codes (`../scripts/legacy/v3.py`) | Manifest row E0159 |
| `0022G4GBPC1`, building permits | `POST https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/2G/CONS/BGP/0022G4GBPC1.px` | In `../scripts/building_permits.py` | Manifest row E0161 |

PSA responses are not committed because PSA's reuse terms are unread (B-03). The census tables are published statistics and the queries can be rerun while PSA keeps them online. The municipal totals used in results are printed in `../results/reproduction_2026-11-02.csv`.

## Web pages read for dated values (closeout, 2026-11-02)

| Value | URL | Observed (UTC) | Local copy SHA-256 (not committed) | Extract |
|---|---|---|---|---|
| Philippine 10-year local-currency government bond yield | https://asianbondsonline.adb.org/philippines/ | 2026-11-02T09:40:02Z | Manifest row for `closeout/abo_philippines_2026-11-02.html` | [`../results/closeout_values_2026-11-02.csv`](../results/closeout_values_2026-11-02.csv) |
| Philippine Seven FY2025 SEC Form 17-A summary page | https://edge.pse.com.ph/downloadHtml.do?file_id=1894881 | 2026-11-02 | Manifest row for `closeout/pse_sevn_17a_fy2025.html` | Same |
