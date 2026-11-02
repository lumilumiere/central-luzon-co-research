# Research record — Central Luzon industrial district POC

**Updated:** 2026-11-02. **State:** working record, published on branch `co-research-report`. The report for general readers is the [root README](../README.md).

Nothing here is approved, validated, ingested or model-ready. Research decisions in `decisions.md` are AI-selected working choices unless marked as Joshua's. The database was not touched.

## Working scope

Research follows the franchise location check in `08` and `09`: should a franchise open at a specific location in Capas, Bamban or Mabalacat, under scenarios A and B, with a before check and an after check, scored on Behavioral and Economic. The locked freeze (`03`) and decision log (`07`) stay unchanged as historical records. Reasoning, conflicts and reconsideration triggers are in `decisions.md`, RD-001.

## Main findings

1. **The planned foot-traffic source has no usable data.** Checklist row 6.1's Kaggle files are a US real-estate sample with no Philippine rows, and row 6.2 is New York data. The post-opening check has no source today.
2. **Population:** the checklist raster does not meet the combined gate on COD-AB polygons (0.691 of the projection sum). In Mabalacat, it would misplace 58.9% of people by barangay. R2025A fits best (4.7% in Mabalacat), but it used the 2020 barangay census as input, so that is not independent validation.
3. **Land values:** Mabalacat appears to fall under RDO 21A, not the checklist's 21B, and RDO 17 was split. Official BIR files could not be reached.
4. **New local cost source:** PSA building permits give municipal floor area and value for 2022–2024.
5. **Employment:** no municipal table was found after walking 3,560 PSA catalogue entries.
6. **Stores:** Overture and OSM miss different things, so neither is safe alone.
7. **Boundaries:** gaps are documented, and a dispute is not established as their cause. Most of Mabalacat's OSM-only area lies in COD-AB Angeles.

## Working source choices

| Need | Primary | Fallback or alternative |
|---|---|---|
| Boundary | COD-AB v03, placeholder | OSM relations as sensitivity |
| Roads | Geofabrik OSM | Overture transportation, HOT export |
| Road surface | OSM tags | Mapillary optional; Planet held |
| Buildings | Google Open Buildings v3 | Microsoft via GitHub; Overture and OSM comparators |
| Population totals | PSA 2024 census | PSA 2020 as check |
| Population distribution | R2025A 2024, within units only | Google building-count shares |
| Stores | Overture places plus OSM | Company lists replace both when received |
| Building cost prior | PSA permit-implied ₱/m² | None chosen |
| Land values | BIR RDO 17A and 21A, not yet obtained | None |
| Employment | Unresolved; Low-band proxy with no value | DTI scores as context |
| Traffic validation | Unresolved | SCTEX whole-road figures as context |
| Foot traffic, sales, post-opening | Unresolved | None from public data |
| Flood screening | NOAH via mirror | None |

## Navigation

| Path | Purpose |
|---|---|
| `data-source-register.csv` | Authoritative register, 104 rows, with separate access, suitability, permission and evidence-quality statuses |
| `decisions.md` | Joshua's decisions and AI research decisions, kept separate |
| `blockers.md` | External blockers and evidence gaps |
| `findings/` | Source assessments, corrections, failed searches |
| `evidence/` | Tracked scripts, queries, metadata, results, session extracts |
| `evidence-manifest.csv` | Provenance, locations, versions and hashes |
| `local-data/` | Git-ignored raw third-party data |

Status terms:
- **Access:** the brief's vocabulary, from Metadata page accessible to Not tested, with reason.
- **Suitability:** Suitable for evaluation, Conditional, Unsuitable, Not assessed.
- **Permission:** Terms read at source, Metadata only, Unresolved, Restricted, Permission or payment required, Not applicable.
- **Evidence status:** Retained file, Logged result, Reproducible procedure, Missing evidence, Unverified.

## Reproducing results

Use Python with rasterio, geopandas, pyogrio, shapely, duckdb, pandas and requests. Scripts take paths as arguments. Earlier scripts are in `evidence/scripts/legacy/` and expect the original scratch layout, so map those paths to `local-data/` using `evidence-manifest.csv`.

`local-data/` is not in Git. On a fresh clone, use the URLs and checksums in the manifest. Sources such as Overture remove old releases, and live OSM queries will not return the same snapshot.

## Next recommended step

Run a bounded evaluation outside the database: use the retained inputs to prepare a versioned input manifest and a barangay zone table (PSA 2024 totals on COD-AB polygons, with labelled synthetic test points) to test how a site check would be assembled. This is research preparation, not ingestion.
