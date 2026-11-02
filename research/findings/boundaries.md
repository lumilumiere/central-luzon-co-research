# Boundaries — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. Scripts: `evidence/scripts/legacy/t3.py`, `v1.py`.

The municipal union is an analytical placeholder. It is not an approved development boundary. The exact site polygon is unresolved (`03` §3, §12; `05` row 1.5).

## Documented geometry

| km² | COD-AB `area_sqkm` | COD-AB EPSG:32651 | geoBoundaries simplified | OSM | PSA land area (LMB 2019) |
|---|---|---|---|---|---|
| Capas | 446.48 | 446.96 | 446.79 | 440.80 | 448.04 |
| Bamban | 207.48 | 207.69 | 207.99 | 177.48 | 344.14 |
| Mabalacat | 97.55 | 97.64 | 97.62 | 149.66 | 166.80 |
| Angeles | 121.03 | Not used | Not used | Not tested | 63.43 |

Sources:
- COD-AB v03: https://data.humdata.org/dataset/cod-ab-phl
- geoBoundaries: https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM3/
- OSM relations 15585456, 15585455, 13407320, fetched 2026-11-02T04:48:34Z
- PSA table `0221A6DLPD0`

Further COD-AB results:
- Union 752.29 km² in EPSG:32651, one polygon, no holes.
- All 1,642 Admin 3 polygons valid.
- Barangays: Capas 20, Bamban 15, Mabalacat 27. All match PSA codes.
- Capas and Mabalacat are about 4.3 km apart; Bamban links them.

OSM compared with COD-AB:

| km² | OSM only | COD-AB only | IoU | Where OSM-only area falls in COD-AB |
|---|---|---|---|---|
| Mabalacat | 62.67 | 10.65 | 0.543 | Angeles 41.95; Bamban 17.14; Magalang 2.37; Mexico 1.22 |
| Bamban | 12.22 | 42.44 | 0.751 | Concepcion 8.00; Capas 3.07; Porac 0.99 |
| Capas | 21.53 | 27.69 | 0.895 | Bamban 8.66; San Jose 8.32; Concepcion 4.18 |

COD-AB Angeles is 1.91 times its PSA land area. COD-AB Mabalacat + Angeles is 218.58 km², against 230.23 km² in PSA land area, a ratio of 0.949. This points to the Mabalacat–Angeles line as a question. It does not prove a cause.

## Unconfirmed explanation

- A Bamban–Mabalacat dispute was reported as the subject of mandamus and certiorari petitions before the Supreme Court in 2011: https://philstar.com/nation/2011/07/09/703823/tarlac-board-opposes-mabalacat-cityhood-amid-boundary-row
- RA 10164 §2 (2012) keeps the city within its metes and bounds, without prejudice to any dispute: https://lawphil.net/statutes/repacts/ra2012/ra_10164_2012.html
- Current status: **Not found**. No figure here treats any legal boundary as resolved.
- The dispute is not established as the cause of any area gap. Most of Mabalacat's OSM-only area lies in COD-AB Angeles, not Bamban.

## Sensitivity

| R2025A, COD-AB then OSM | Capas | Bamban | Mabalacat |
|---|---|---|---|
| 2024 persons | 165,127 / 171,901 | 82,809 / 81,573 | 306,846 / 343,258 |

| Footprints, COD-AB then OSM | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Google ≥0.65 | 76,827 / 80,383 | 37,523 / 36,842 | 95,257 / 108,917 |
| Microsoft | 35,920 / 37,455 | 17,737 / 17,530 | 29,753 / 35,391 |

## Identifier join

- COD-AB municipal `PH0306904`; PSA `0306904000`; HDX projection `PH036904000`.
- COD-AB barangay codes are `PH` plus the 10-digit PSA code, which joined 62 of 62.
