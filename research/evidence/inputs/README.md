# Packed inputs — Central Luzon industrial district POC

These files are copies of inputs that a live endpoint or a re-uploaded source cannot return byte-for-byte later. They are packed so the material results can be rerun without those endpoints. Built and checked by [`../scripts/pack_inputs.py`](../scripts/pack_inputs.py) on 2026-11-02.

This is a research evidence copy. It is not an ingested or approved dataset.

| Path | Source and snapshot | Licence and notice | Used by |
|---|---|---|---|
| `osm/osm_ways_topology_2026-11-02.json` | Overpass API, OSM base timestamp 2026-11-02T08:01:36Z; query in [`../queries/overpass_directed_connectivity.txt`](../queries/overpass_directed_connectivity.txt). **Reduced:** way ids, node lists and the `highway`, `oneway` and `junction` tags only, which is everything the script reads. The full response stays local, SHA-256 `5f5a5580f9d38e14278e4e167bc01fa98151b9dfca86090c5ecb145ffe333a1b` | © OpenStreetMap contributors, [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) | `directed_connectivity.py` |
| `osm/osm_rel.json`, `osm/aoi_osm.gpkg` | Overpass relations for the three municipalities, 2026-11-02, and the polygons built from them | © OpenStreetMap contributors, ODbL 1.0 | `reproduce_core.py`, `reproduce_supplement.py` |
| `osm/osm_poi.json` | Overpass store and amenity nodes, 2026-11-02 | © OpenStreetMap contributors, ODbL 1.0 | `stores_poi.py` |
| `cod/aoi_cod.gpkg`, `cod/aoi_cod_adm4.gpkg` | COD-AB v03 admin3 and admin4 polygons for the three municipalities (HDX `cod-ab-phl`) | [CC BY-IGO](https://creativecommons.org/licenses/by/3.0/igo/), as stated on HDX | `reproduce_core.py` and others |
| `microsoft/132303013.corridor.csv.gz`, `microsoft/132303031.corridor.csv.gz` | Microsoft GlobalMLBuildingFootprints, index upload 2026-08-13, quadkeys 132303013 and 132303031. Only the lines that `reproduce_core.py` keeps (bounding box 120.2–120.65 E, 15.15–15.45 N), unchanged | [CDLA Permissive 2.0](https://cdla.dev/permissive-2-0/), per the GitHub README | `reproduce_core.py` (barangay shares, footprint counts) |
| `overture/overture_places_corridor_redacted.parquet` | Overture Maps places, release 2026-10-21.0, corridor bounding box. **Redacted:** the `name` cell is blank on 6 of 12,184 rows whose name carries an agency or project-brand name that the assignment keeps out of outputs. Rows, brands, categories and coordinates are unchanged. The names are passed to the script at run time, not stored in it. A raw byte scan can still match short letter sequences inside hexadecimal place IDs. Those are identifiers, and no name or brand field carries an excluded term. The original stays local, SHA-256 `bd0a521ce9d04955e44c421cbd0eb3843ff22ca96e1e90ffb2f0918fe34c0412` | [CDLA Permissive 2.0](https://cdla.dev/permissive-2-0/) per Overture attribution page; see the [attribution guide](https://docs.overturemaps.org/attribution/) | `brand_compare.py` (`overture_corridor.py` reads the release directly) |

**Checks run on 2026-11-02 (all passed):**
- Microsoft footprints counted from the packed subset match the published counts: Capas 35,920, Bamban 17,737, Mabalacat 29,753.
- `directed_connectivity.py`, run on the reduced Overpass ways, reproduces `../results/directed_connectivity_2026-11-02.csv` exactly.
- `brand_compare.py`, run on the packed COD polygons, OSM POIs and redacted Overture places, reproduces `../results/brand_compare_2026-11-02.csv` exactly.
- Files copied unchanged have the same SHA-256 as their local source. All hashes are in [`../../evidence-manifest.csv`](../../evidence-manifest.csv).
- No packed text, name or brand field contains an excluded agency or project-brand name (checked by the script).

**To use them:**
- Pass the packed paths as script arguments.
- Or copy them into `research/local-data/raw/<same folder>/`, renaming the Microsoft files to `132303013.csv.gz` and `132303031.csv.gz`.
- See [`../../methods.md`](../../methods.md).

**Not packed, with reasons:**
- WorldPop rasters, Google Open Buildings v3 and NOAH files are versioned downloads. The manifest records their URLs and SHA-256.
- PSA OpenSTAT tables are not packed because their reuse terms are unread (B-03). They can be fetched again with the saved queries.
- Overture building extracts were not retained, so the Overture building counts are logged results only. They are context and do not drive any selection.
- The restricted Planet road-surface data is never packed.
