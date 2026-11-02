# Methods and reproduction — Central Luzon industrial district POC

## Environment

- Python 3.14 virtual environment; packages pinned in [`evidence/requirements-lock.txt`](evidence/requirements-lock.txt).
- Key packages: geopandas, rasterio, shapely, pyogrio, pandas, numpy, duckdb, networkx, requests, openpyxl, and pymupdf (added in the closeout pass for rendering PDF pages).
- **Volatile inputs are packed** in [`evidence/inputs/`](evidence/inputs/README.md): Overpass snapshots, OSM and COD-AB municipal polygons, the Microsoft corridor lines and Overture places. Copy them into `local-data/raw/` to rerun without live endpoints. Queries and observation times are in [`evidence/queries/queries.md`](evidence/queries/queries.md).
- Run scripts with `python -I` from the `research/` folder unless stated.
- Raw inputs live in git-ignored `local-data/`. On a fresh clone, rebuild them from the URLs and checksums in [`evidence-manifest.csv`](evidence-manifest.csv).

## Calculations that drive selections

| Calculation | Script | Inputs | Result | Reproduced? |
|---|---|---|---|---|
| Boundary areas, IoU, overlap with Angeles | [`evidence/scripts/reproduce_core.py`](evidence/scripts/reproduce_core.py) | COD-AB admin3, OSM relations | `evidence/results/reproduction_2026-11-02.csv` | Yes, 2026-11-02 |
| Barangay crosswalk (62/62) and total versus household population | Same | COD-AB admin4, PSA `0031A6DTPH2` | Same | Yes |
| Raster sums: id 6316 and R2025A 2024, two boundaries, two masking rules, national sums | Same | WorldPop rasters | Same | Yes |
| Combined gate ratios | Same | As above, plus projection sum | Same | Yes |
| Barangay share mismatch | Same | As above, plus Google points and Microsoft quadkeys | Same | Yes |
| R2025A 2020 scaling; id 49861 on both boundaries | [`evidence/scripts/reproduce_supplement.py`](evidence/scripts/reproduce_supplement.py) | WorldPop rasters | `evidence/results/reproduction_supplement_2026-11-02.csv` | Yes; id 49861 on OSM newly performed |
| Directed connectivity | [`evidence/scripts/directed_connectivity.py`](evidence/scripts/directed_connectivity.py) | Overpass ways with tags, 2026-11-02T08:01:36Z | `evidence/results/directed_connectivity_2026-11-02.csv` | New |
| Road tag completeness | `evidence/scripts/legacy/t10.py` | ohsome 2026-07-27 | Session extract L0421 | Logged; rerunnable with the same `time` parameter |
| Building permits ₱/m² | [`evidence/scripts/building_permits.py`](evidence/scripts/building_permits.py) | PSA `0022G4GBPC1` | Local table; cited figures in findings | Yes |
| Store counts and brand comparison | `stores_poi.py`, `overture_corridor.py`, `brand_compare.py` | OSM 2026-11-02, Overture 2026-10-21.0 | `evidence/results/*` | Yes; Overture releases expire |
| Terrain, land cover, flood shares | `corridor_layers.py`, `noah_flood_corridor.py` | Copernicus DEM, WorldCover, NOAH mirror | `evidence/results/*` | Yes |
| Packed-input checks (Microsoft counts, directed connectivity, brand comparison) | [`evidence/scripts/pack_inputs.py`](evidence/scripts/pack_inputs.py), then `directed_connectivity.py` and `brand_compare.py` on the packed files | `evidence/inputs/` (OSM ways reduced to topology tags; 6 Overture name cells blanked) | Assertions pass; both results are identical | Yes, closeout pass |
| 2012 JICA transcription checks | [`evidence/scripts/jica_transcription_check.py`](evidence/scripts/jica_transcription_check.py) | [`evidence/results/jica_2012_transcription.csv`](evidence/results/jica_2012_transcription.csv) | `evidence/results/jica_2012_transcription_check.txt`: 20 of 20 pass | Yes, closeout pass |

## Integrity and validation are different checks

- A matching SHA-256 hash shows a file is unchanged. It does not show a calculation is right.
- Calculations were re-executed in the rebuilt environment, and the results matched the previously reported figures.
- The re-execution also caught one reproduction-script error (barangay names matched across municipalities), which was fixed. The published figures were unaffected.

## Masking and aggregation rules

- **Pixel-centre:** a cell counts if its centre falls inside the polygon. Sums may undercount at edges.
- **All-touched:** every cell the polygon touches counts. Neighbouring units then double count shared cells.
- **Counts per cell are summed, never interpolated.** Rasters stay in EPSG:4326 for sums. Vectors are reprojected to EPSG:32651 for areas.

## Not reproduced

| Item | Reason |
|---|---|
| Mapillary surface figures | File (906 MB) not retained; logged result only |
| ohsome tag shares | Not rerun this pass; rerunnable |
| First connectivity run | Snapshot not recorded; superseded |
| Overture building counts | Extract not retained, and release 2026-10-21.0 will expire. Context only, not used for selection |
| PSA-based figures from packed inputs alone | PSA responses not packed (terms unread, B-03); rerun the saved queries |
