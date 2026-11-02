# Population — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. **Boundary:** COD-AB v03 unless stated.

**Method:**
- Masking is pixel-centre unless stated. NoData (−99999) and non-finite cells are excluded.
- Cells are summed in the EPSG:4326 source CRS.
- All raster figures below were **recomputed on 2026-11-02** from retained rasters by [`../evidence/scripts/reproduce_core.py`](../evidence/scripts/reproduce_core.py) and [`../evidence/scripts/reproduce_supplement.py`](../evidence/scripts/reproduce_supplement.py). Results: [`../evidence/results/reproduction_2026-11-02.csv`](../evidence/results/reproduction_2026-11-02.csv), [`../evidence/results/reproduction_supplement_2026-11-02.csv`](../evidence/results/reproduction_supplement_2026-11-02.csv).

## Observed counts and projections

Sources:
- PSA `0221A6DLPD0`: https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px
- PSA `0031A6DTPH2` (barangays, 1 July 2024): https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0031A6DTPH2.px
- HDX projection (2015 census base): https://data.humdata.org/dataset/philippines-population-projection-2020-2025-admin3

| Persons | Capas | Bamban | Mabalacat | Sum | Angeles |
|---|---|---|---|---|---|
| Census 2020 total | 156,056 | 78,260 | 293,244 | 527,560 | 462,928 |
| Census 2024 total (1 July) | 162,724 | 81,012 | 306,594 | 550,330 | 483,452 |
| 2024 household population (barangay sum) | 162,480 | 80,472 | 306,550 | 549,502 | Not used |
| Projection, mid-2020 | 155,154 | 76,808 | 288,295 | 520,257 | Not used |

**Checks:**
- Barangay totals sum exactly to municipal totals.
- Total and household population differ by under 0.7%.
- The projection is not a count, and the dates differ: census 1 May 2020 and 1 July 2024; projection mid-year; WorldPop R2025A aligned to UN WPP January 1 estimates.

## Checklist gate (combined study area)

`05` line 163 requires the combined total within 20% of the Admin3 projection sum, "or explained". The 20% is an unsourced working assumption (D-009); see [`validation-standards.md`](validation-standards.md).

| Ratio to projection sum 520,257 | COD-AB, pixel-centre | COD-AB, all-touched | OSM, pixel-centre | OSM, all-touched |
|---|---|---|---|---|
| Id 6316 (checklist raster) | 0.691 | 0.712 | 0.796 | 0.807 |
| Id 49861 (2020 constrained) | 0.690 | 0.707 | 0.792 | 0.804 |

**Reading:**
- Neither product meets the gate on COD-AB polygons, and no explanation is available.
- The OSM columns use different geography from the comparator, and all-touched sums count shared-edge cells twice.

## Municipality diagnostics (not a gate)

| Persons | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Id 6316, COD-AB, pixel-centre | 132,000 | 66,328 | 161,117 |
| Id 6316, OSM, all-touched | 135,764 | 72,032 | 212,208 |
| Id 49861, COD-AB, pixel-centre | 132,437 | 66,035 | 160,557 |
| R2025A 2020, COD-AB | 159,555 | 80,015 | 296,492 |
| R2025A 2024, COD-AB, pixel-centre | 165,127 | 82,809 | 306,846 |
| R2025A 2024, COD-AB, all-touched | 166,408 | 84,644 | 312,862 |
| R2025A 2024, OSM, pixel-centre | 171,901 | 81,573 | 343,258 |

Across four boundary and masking cases, id 6316 is 0.846–0.870 of the 2020 census in Capas, 0.848–0.920 in Bamban and 0.549–0.724 in Mabalacat. Mabalacat + Angeles together are 0.541 on COD-AB.

## R2025A inputs

From the WorldPop census sources sheet (excerpt in [`../evidence/results/worldpop_r2025a_phl_inputs_excerpt.csv`](../evidence/results/worldpop_r2025a_phl_inputs_excerpt.csv)):
- 2020 census at 42,058 units.
- Flagged "modelled with second timepoint only".
- 2024 census not listed as an input.
- National totals aligned to UN WPP 2024.
- Philippine boundary file: **Not found**.

| Ratio to census, then divided by national factor | Capas | Bamban | Mabalacat | Angeles | Mabalacat + Angeles |
|---|---|---|---|---|---|
| 2020 (national factor 1.0223) | 1.0224, then 1.0001 | 1.0224, then 1.0001 | 1.0111, then 0.9890 | 1.0296, then 1.0071 | 1.0224, then 1.0001 |

**Reading:** this is agreement with a model input, not validation. The 2024 comparison uses a census not listed as an input, but inherits the 2020 pattern.

## Barangay share comparison

**Question:** how closely does each layer's split of a municipality's population across its barangays match PSA 2024 barangay shares?

**Measure:** share mismatch = half the sum of absolute differences between layer shares and census shares, across a municipality's barangays.

**What the measure means:**
- It is a property of **aggregate shares**.
- 4.7% means the layer's barangay shares differ from census shares by 4.7 percentage points in total, counting each over-share once.
- **It does not establish where individual people live**, and says nothing about distribution inside a barangay.

**Join:** COD-AB Admin 4 codes are `PH` plus the PSA code, so all 62 barangays joined. Two barangay names repeat across the municipalities, so names must only be matched within a municipality. A reproduction script first broke this rule and produced wrong sums, which was found and fixed.

| Share mismatch % (vs total population) | Capas (20) | Bamban (15) | Mabalacat (27) | Uses census input? |
|---|---|---|---|---|
| R2025A 2024 | 1.6 | 2.3 | 4.7 | Yes, 2020 barangay census |
| Microsoft footprint count | 6.6 | 7.4 | 18.8 | No |
| Google count, ≥0.65 | 10.1 | 8.6 | 11.0 | No |
| Id 6316 (2020) | 19.3 | 16.0 | 58.9 | Inputs Not found |

Against household population the figures change by 0.1–0.2 points at most (see the reproduction CSV).

**Reading:**
- R2025A matches best, as expected given its input.
- Between the footprint layers, Microsoft is lower in Capas and Bamban and Google in Mabalacat. Google at ≥0.65 has the smaller worst case (11.0% against 18.8%).
- The differences between footprint layers are small next to the gap to id 6316.

## Selection

See RD-003 and RD-004 in [`../decisions.md`](../decisions.md). No baseline is ingested, validated or model-ready.
