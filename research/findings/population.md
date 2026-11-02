# Population — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. **Boundary:** COD-AB v03 unless stated. **Masking:** pixel-centre unless stated. NoData (−99999) and non-finite cells are excluded, and cell values are summed in EPSG:4326 source CRS. Scripts: `evidence/scripts/legacy/t3.py`, `t12.py`, `t18.py`, `z.py`, `barangay_distribution_test.py`.

## Observed counts and projections

Sources:
- PSA `0221A6DLPD0`: https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px
- HDX projection (2015 census base): https://data.humdata.org/dataset/philippines-population-projection-2020-2025-admin3

| Persons | Capas | Bamban | Mabalacat | Sum | Angeles |
|---|---|---|---|---|---|
| Census 2020 | 156,056 | 78,260 | 293,244 | 527,560 | 462,928 |
| Census 2024 (1 July) | 162,724 | 81,012 | 306,594 | 550,330 | 483,452 |
| Projection, mid-2020 | 155,154 | 76,808 | 288,295 | 520,257 | Not used |
| Projection, mid-2024 | 164,171 | 81,240 | 314,076 | 559,487 | Not used |

National census totals in this table: 109,033,245 (2020) and 112,727,776 (2024).

## Checklist gate, combined study area

`05` line 163: the combined population must be within 20% of the Admin3 projection sum, "or explained". This limit is an unsourced working assumption (D-009). Comparator: 520,257 persons, 2020.

| Id 6316, 2020 | Combined total | Ratio to projection | Reading | Reproducibility |
|---|---|---|---|---|
| COD-AB, pixel-centre | 359,445 | 0.691 | Outside 20% | Retained raster, rerun |
| COD-AB, all-touched | 370,185 | 0.712 | Outside 20% | Retained raster, rerun |
| OSM, pixel-centre | 414,372 | 0.796 | Just outside | Retained raster, rerun |
| OSM, all-touched | 420,004 | 0.807 | Inside, not comparable | Retained raster, rerun |

**Reading:** the gate is not met on COD-AB polygons, and "explained" is not available because the cause is Not found. The OSM rows do not share the comparator's geography, and all-touched sums count shared-edge cells twice.

## Municipality diagnostics

These are diagnostics, not a checklist gate. Row 4.4 asks only to record ratios.

| Ratio to census 2020, id 6316 | Capas | Bamban | Mabalacat |
|---|---|---|---|
| COD-AB, pixel-centre | 0.846 | 0.848 | 0.549 |
| COD-AB, all-touched | 0.860 | 0.864 | 0.574 |
| OSM, pixel-centre | 0.861 | 0.905 | 0.714 |
| OSM, all-touched | 0.870 | 0.920 | 0.724 |

| Other raster sums | Capas | Bamban | Mabalacat | Status |
|---|---|---|---|---|
| Id 49861, 2020, COD-AB | 132,437 | 66,035 | 160,557 | Logged |
| R2025A 2020, COD-AB | 159,555 | 80,015 | 296,492 | Logged |
| R2025A 2020, OSM | 166,101 | 78,817 | 331,613 | Logged |
| R2025A 2024, COD-AB | 165,127 | 82,809 | 306,846 | Logged |
| R2025A 2024, OSM | 171,901 | 81,573 | 343,258 | Logged |

**Not performed, effect unknown:** id 49861 on OSM polygons, and R2025A with all-touched masking.

Other id 6316 checks, pixel-centre:
- Mabalacat + Angeles: 408,764 of 756,172, or 0.541. Moving their shared border cannot explain the gap.
- Angeles alone: 0.535.
- Pampanga with Angeles: 0.909. Tarlac: 0.906. Region III: 0.924.
- National: 110,194,183, or 1.0106 of census.
- Rest of Pampanga: 1.039. So the shortfall concentrates in the two cities.

## R2025A inputs

Sources: release statement and census sheet (`evidence/results/worldpop_r2025a_phl_inputs_excerpt.csv`).

- 2010 census, level 3, 41,954 units. 2020 census, level 4, 42,058 units. Nested units 38,911.
- "Modelled with second timepoint only" is marked `[YES]`.
- The 2024 census is not listed as an input.
- The statement says official boundaries were matched, but no Philippine boundary file is named: **Not found**.
- National totals align to UN WPP 2024 at January 1.
- WorldPop warns that Global2 may not capture high urban densities well, and that uncertainty rises further from input years.

| Ratio to census, then divided by national factor | Capas | Bamban | Mabalacat | Angeles | Mabalacat + Angeles |
|---|---|---|---|---|---|
| 2020 (factor 1.0223) | 1.0224, then 1.0001 | 1.0224, then 1.0001 | 1.0111, then 0.989 | 1.0296, then 1.0071 | 1.0224, then 1.0001 |
| 2024 (factor 1.0233) | 1.0148, then 0.9916 | 1.0222, then 0.9989 | 1.0008, then 0.978 | 1.0203, then 0.9970 | 1.0128, then 0.9897 |

- **2020 is agreement with an input census, not validation.**
- **2024 is a check against a census not listed as an input, but it inherits the 2020 distribution.** Reference dates also differ, and no adjustment was applied.

## Barangay distribution test (new)

**Question:** how well does each layer reproduce each barangay's share of its municipality's 2024 population?

- **Reference counts:** PSA `0031A6DTPH2`, total population, 1 July 2024, 62 barangays, joined to COD-AB Admin 4 by code with no misses.
- **Measure:** misallocation = half the sum of absolute share differences within a municipality. It reads as the share of people who would need reassigning.
- **Method:** rasters are pixel-centre sums. Google points use published coordinates. Microsoft uses mean vertex.

| Misallocation % | Capas (20) | Bamban (15) | Mabalacat (27) | Independent of census input? |
|---|---|---|---|---|
| R2025A 2024 | 1.6 | 2.3 | 4.7 | No: 2020 barangay census is an input |
| Microsoft count | 6.6 | 7.4 | 18.8 | Yes |
| Google count, ≥0.763 | 11.2 | 8.0 | 9.9 | Yes |
| Google count, ≥0.65 | 10.1 | 8.6 | 11.0 | Yes |
| Id 6316 (2020 raster) | 19.3 | 16.0 | 58.9 | Year differs; inputs Not found |
| Barangay area | 58.2 | 48.7 | 54.6 | Yes |

Spearman rank correlation is in `evidence/results/barangay_distribution_test_2026-11-02.csv`.

**Reading:**
- R2025A has the best fit, as expected given its input.
- Among layers that do not use census inputs, Microsoft has lower misallocation in Capas and Bamban, and Google in Mabalacat. Google at ≥0.65 has the smaller worst case (11.0% against 18.8%), which is why it is the working fallback.
- These two footprint layers differ by less than the gap to id 6316 in every municipality, so the ranking between them is weak.
- This tests barangay totals only. Nothing tests distribution inside a barangay.

## Selection

See RD-003 and RD-004. No baseline is ingested, validated or model-ready.
