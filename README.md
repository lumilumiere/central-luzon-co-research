# Central Luzon industrial district POC — Co-Research Report

**Branch:** `co-research-report`. **Research date:** 2026-11-02 PHT, which is the access date for every source below unless stated. **Contributor:** lumilumiere.

This report stands alone: you do not need the conversation behind it. The project notes in [`geoteron-second-brain/`](geoteron-second-brain/) and [`context/`](context/) are unchanged historical records.

**Read this first:** this is completed *research*, not completed *implementation*. Nothing has been ingested, calibrated, validated, approved or declared model-ready. No baseline, road network, simulation or database exists from this work. A reachable source is not automatically suitable or permitted. Recommendations are provisional, and Joshua owns model selection and implementation choices.

## 1. Assignment and boundaries

**Original assignment:** verify whether the study-area boundary, roads, buildings and population datasets can be obtained and used for Capas and Bamban (Tarlac) and Mabalacat (Pampanga), each checked separately, and record the findings in the existing source spreadsheet.

**Expanded assignment (Joshua's updated direction, relayed 2026-11-02):** consider every dataset the project references, register the research in the repository, and select priorities, sources and working datasets without repeated approval. This replaced the spreadsheet-only rule.

**Boundaries that stayed in force:**
- No database changes, ingestion pipelines, SUMO builds or model runs.
- No outreach, FOI requests, purchases or new contract terms.
- Joshua owns architecture and model selection.
- Use the name "Central Luzon industrial district POC", with no agency or project brand.
- Every figure needs a source, date and place. "Not found" is a valid result.

## 2. Executive summary

**Completed:** a four-dataset access audit, then a 104-row register covering every dataset family the project mentions, with hash-verified evidence and recorded methods.

**Findings that matter most:**

1. **The planned foot-traffic source has no usable data.** The Kaggle bundle in checklist row 6.1 holds a US real-estate sample with no Philippine rows. Row 6.2 is New York data. The post-opening check has no source today.
2. **The checklist population raster performs poorly in Mabalacat.** It misses the combined gate on COD-AB polygons (0.691 of the projection sum), and would misplace 58.9% of Mabalacat's people by barangay.
3. **R2025A fits best but is not validated.** It used the 2020 barangay census as an input, so its fit is partly the input returning.
4. **A checklist land-value entry looks wrong.** Secondary sources put Mabalacat under RDO 21A, not 21B. Official BIR files were not reached.
5. **Boundary gaps are documented, not explained.** Most of Mabalacat's OSM-only area lies in COD-AB Angeles, so a Bamban–Mabalacat dispute is not established as the cause.
6. **Municipal building permits are a useful new source.** They give floor area and value for all three municipalities, 2022–2024.

**Unresolved:** official land values, observed traffic, municipal employment, store sales, post-opening data, several licence terms, a real site location, and the franchise definition of cost and return.

| Register rows | Count |
|---|---|
| Required for working scope | 27 |
| Supporting or alternative | 44 |
| Future work | 22 |
| Unsuitable or superseded | 11 |
| Suitability still Not assessed | 55 |
| Evidence quality Low | 73 |

## 3. Task-by-task completion record

| Task | Status | Reason |
|---|---|---|
| Identify and handle the scope discrepancy | Completed | Working interpretation recorded; Joshua has not confirmed it |
| Boundary access check | Completed | Downloaded and inspected |
| Boundary suitability | Partial | Area conflict and site polygon open |
| Roads access check | Completed | Header read, attributes sampled by API |
| Roads suitability | Partial | Full extract unopened; routability not demonstrated |
| Buildings access check | Partial | Google polygon file not downloaded; Earth Engine and Planetary Computer data not read |
| Buildings suitability | Partial | Counts measured; corridor accuracy Not found |
| Population access check | Completed | Rasters and tables inspected |
| Population suitability | Partial | Distribution tested at barangay level only; R2025A is alpha |
| Record findings in the source spreadsheet | Deferred | Spreadsheet never found; replaced by the repository register under Joshua's updated direction |
| Evidence register and corrections | Completed | See section 11 |
| Investigate R2025A Philippine inputs | Partial | Census inputs found; exact boundary file Not found |
| Inventory every referenced dataset | Completed | 104 rows, each classified with a reason |
| Verify every candidate in depth | Partial | 55 rows remain Not assessed; many are metadata-level |
| Select sources | Partial | Primaries chosen where evidence allows; several needs Unresolved |
| Land values | Blocked | Official files not reached |
| Observed traffic, mode share, freight | Blocked | No open corridor data found |
| Employment | Blocked | No municipal table found |
| Franchise store locations | Partial | Open sources sampled; company lists not obtained |
| Store sales and foot traffic | Blocked | Needs outreach or purchase |
| Post-opening data | Blocked | No source found |
| Validation standards, including testing the four D-009 limits | Not started | Not reached in these passes |
| Legal memo, including the FOI process | Partial | Licensing note exists; legal review needed |
| Model input value table | Partial | Candidates noted; values not adopted |
| Evidence preservation | Completed | Hash-verified; see section 11 |
| Baseline, database, SUMO, models | Not started | Out of bounds for this work |

## 4. Original four dataset groups

Access statuses follow the assignment's vocabulary. Figures below are research diagnostics, not an ingested baseline.

### 4.1 Study-area boundary

The municipal union is a placeholder. It is not an approved development boundary, and the exact site polygon is unresolved.

| Source | Version and date | Access | Suitability | Permission |
|---|---|---|---|---|
| [COD-AB](https://data.humdata.org/dataset/cod-ab-phl) | v03; created 2018-02-09, reviewed 2024-04-01, files 2026-05-28 | Sample inspected | Conditional | CC BY-IGO per HDX field |
| [geoBoundaries](https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM3/) | `PHL-ADM3-30758251`; built 2023-12-12 | Sample inspected | Conditional, same lineage as COD-AB | CC BY 3.0 IGO per API field |
| OSM relations [13407320](https://www.openstreetmap.org/relation/13407320), [15585455](https://www.openstreetmap.org/relation/15585455), [15585456](https://www.openstreetmap.org/relation/15585456) | Fetched 2026-11-02T04:48:34Z | API verified | Sensitivity only | ODbL |
| Official PSA or NAMRIA polygons | Not found | Access attempt failed (`psa.gov.ph` 403) | Not assessed | Unresolved |

| km² | COD-AB | OSM | [PSA land area](https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px) (LMB 2019) |
|---|---|---|---|
| Capas | 446.48 | 440.80 | 448.04 |
| Bamban | 207.48 | 177.48 | 344.14 |
| Mabalacat | 97.55 | 149.66 | 166.80 |

**Documented:** COD-AB's union is one polygon of 752.29 km² (EPSG:32651). Barangay polygons join 62 of 62 to PSA codes. OSM's Mabalacat adds 62.67 km² outside COD-AB: 41.95 km² in COD-AB Angeles and 17.14 km² in COD-AB Bamban. COD-AB Angeles is 121.03 km² against 63.43 km² in PSA land area, while Mabalacat + Angeles is 218.58 km² against 230.23 km².

**Unconfirmed:** a Bamban–Mabalacat dispute was [reported before the Supreme Court in 2011](https://philstar.com/nation/2011/07/09/703823/tarlac-board-opposes-mabalacat-cityhood-amid-boundary-row), and [RA 10164 §2](https://lawphil.net/statutes/repacts/ra2012/ra_10164_2012.html) (2012) leaves disputes open. Current status: Not found. No legal boundary is treated as resolved.

Details: [`research/findings/boundaries.md`](research/findings/boundaries.md).

### 4.2 Roads

| Source | Version and date | Access | Suitability | Permission |
|---|---|---|---|---|
| [Geofabrik OSM](https://download.geofabrik.de/asia/philippines.html) | `philippines-261031.osm.pbf`, 2026-10-31T21:23:06Z, 612,430,134 bytes | Header sampled | Conditional | ODbL 1.0; combined-output duties unresolved |
| [HeiGIT Mapillary surface](https://data.humdata.org/dataset/philippines-road-surface-data) | Dataset date 2024-11-07 | Sample inspected | Conditional, optional | ODbL per HDX field |
| [HeiGIT Planet surface](https://data.humdata.org/dataset/philippines-planet-road-surface-data) | Updated 2026-03-02 | Sample inspected | Not assessed | **Restricted:** non-commercial; held |

Three questions are kept separate, because they use different snapshots:

**Missing attributes** (ohsome snapshot 2026-07-27T09:00Z, length-weighted, COD-AB polygons):

| % with tag: all drivable / major roads | Capas | Bamban | Mabalacat |
|---|---|---|---|
| lanes | 18.4 / 85.0 | 23.4 / 100 | 22.0 / 99.5 |
| maxspeed | 15.7 / 78.6 | 13.7 / 89.2 | 15.3 / 89.1 |
| oneway | 9.1 / 40.3 | 12.1 / 75.1 | 11.3 / 74.2 |
| surface | 23.1 / 77.9 | 38.4 / 99.8 | 34.2 / 88.9 |

**Geographic coverage:** all three municipalities are inside the extract polygon (2026-10-31), and MacArthur Highway and the Subic-Clark-Tarlac Expressway are mapped (Overpass 2026-11-01T18:02:59Z). Completeness on the ground was not tested.

**Routability: not demonstrated.** In a bounding box of 15.16,120.24,15.43,120.64, 13,386 drivable ways form 39 connected groups, with 98.8% in the largest (Overpass 2026-11-02T04:50:34Z). This only tests shared nodes.

The Planet restriction affects that optional dataset only, not OSM roads. Details: [`research/findings/roads-and-transport.md`](research/findings/roads-and-transport.md).

### 4.3 Buildings

| Footprints, COD-AB polygons | Capas | Bamban | Mabalacat |
|---|---|---|---|
| [Google Open Buildings v3](https://sites.research.google/gr/open-buildings/), ≥0.65 (inference May 2023) | 76,827 | 37,523 | 95,257 |
| Google, ≥0.763 (tile 339 80% precision threshold) | 44,357 | 22,079 | 56,638 |
| Google, ≥0.874 (tile 339 90% precision threshold) | 8,874 | 4,635 | 10,964 |
| [Microsoft](https://github.com/microsoft/GlobalMLBuildingFootprints) (upload 2026-08-13; row counts match 2023-04-25 items) | 35,920 | 17,737 | 29,753 |
| [Overture](https://docs.overturemaps.org/attribution/) 2026-10-21.0 | 77,861 | 40,767 | 94,683 |

- Google lists 2.1–3.2 times Microsoft's count at ≥0.65, but fewer than Microsoft at ≥0.874. **No source is ranked on accuracy**, because corridor accuracy is Not found.
- Microsoft `height` and `confidence` are `-1` for every corridor record.
- No open source gives building use or floor area. Footprint area is not floor area.
- Permission: Google is CC BY 4.0 or ODbL, user's choice. Microsoft is CDLA Permissive 2.0 on GitHub but ODbL-1.0 on [Planetary Computer](https://planetarycomputer.microsoft.com/dataset/ms-buildings), and which governs is unresolved.
- Access limits: Google's 1.43 GB polygon file was not downloaded (points file was streamed). Planetary Computer data files and Earth Engine were not read.

Details: [`research/findings/buildings.md`](research/findings/buildings.md).

### 4.4 Population

Sources: [PSA `0221A6DLPD0`](https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px), [PSA `0031A6DTPH2`](https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0031A6DTPH2.px), [HDX projections](https://data.humdata.org/dataset/philippines-population-projection-2020-2025-admin3) (2015 census base), [WorldPop id 6316](https://hub.worldpop.org/geodata/summary?id=6316) (produced 2018-11-01), [R2025A 2024, id 74942](https://hub.worldpop.org/geodata/summary?id=74942) and [2020, id 74938](https://hub.worldpop.org/geodata/summary?id=74938) (produced 2025-09-01, alpha).

| Persons | Capas | Bamban | Mabalacat | Sum |
|---|---|---|---|---|
| Census 2020 | 156,056 | 78,260 | 293,244 | 527,560 |
| Census 2024 (1 July) | 162,724 | 81,012 | 306,594 | 550,330 |
| Projection, mid-2020 | 155,154 | 76,808 | 288,295 | 520,257 |
| Id 6316, 2020, COD-AB | 132,000 | 66,328 | 161,117 | 359,445 |
| R2025A 2020, COD-AB | 159,555 | 80,015 | 296,492 | 536,062 |
| R2025A 2024, COD-AB | 165,127 | 82,809 | 306,846 | 554,782 |

Raster sums use pixel-centre masking, exclude NoData, and are summed in the source CRS.

**Checklist gate (combined study area, unsourced working limit of 20%, or explained):**

| Id 6316, 2020 | Ratio to projection sum 520,257 | Reading |
|---|---|---|
| COD-AB, pixel-centre | 0.691 | Outside |
| COD-AB, all-touched | 0.712 | Outside |
| OSM, pixel-centre | 0.796 | Just outside |
| OSM, all-touched | 0.807 | Inside, not comparable: edge cells double-counted, different geography |

**Municipality diagnostics (not a gate):** across those four cases, id 6316 is 0.846–0.870 of census in Capas, 0.848–0.920 in Bamban and 0.549–0.724 in Mabalacat. Mabalacat + Angeles together are 0.541 on COD-AB, so moving their shared border cannot explain the gap. The cause is Not found.

**R2025A inputs** ([statement](https://data.worldpop.org/repo/prj/Global_2015_2030/R2025A/doc/Global2_Release_Statement_R2025A_v1.pdf), [census sheet](https://data.worldpop.org/repo/prj/Global_2015_2030/R2025A/doc/census/global2_census_data_sources_R2025A_v1.xlsx)): 2020 census at 42,058 units, flagged as second-timepoint-only modelling, with national totals aligned to UN WPP 2024. The 2024 census is not listed as an input. After removing the national factor (1.0223), R2025A 2020 matches census to 0.01% in Capas, Bamban and Mabalacat + Angeles. **That is agreement with an input, not validation.**

**Barangay distribution test:** share of people who would need reassigning to match PSA 2024 barangay shares (62 barangays; COD-AB Admin 4):

| Misallocation % | Capas | Bamban | Mabalacat | Uses census input? |
|---|---|---|---|---|
| R2025A 2024 | 1.6 | 2.3 | 4.7 | Yes, 2020 barangay |
| Microsoft count | 6.6 | 7.4 | 18.8 | No |
| Google count, ≥0.65 | 10.1 | 8.6 | 11.0 | No |
| Id 6316 | 19.3 | 16.0 | 58.9 | Inputs Not found |

This tests barangay totals only, not distribution inside a barangay.

**Not performed, effect unknown:** R2025A with all-touched masking, and WorldPop id 49861 on OSM polygons. Details: [`research/findings/population.md`](research/findings/population.md).

## 5. Additional research under the expanded instructions

Everything in this section went beyond the original four-dataset assignment.

**Foot traffic.** [Techsalerator on Kaggle](https://www.kaggle.com/datasets/techsalerator/foot-traffic-and-mobility-data-for-philippines) (version 1, 2026-04-07) contains a Mashvisor US rental sample and 0 Philippine or corridor term matches. [Smart Mobility](https://www.kaggle.com/datasets/ziya07/smart-mobility-traffic-dataset) (2025-03-04) has 5,000 rows in a New York bounding box.

**Store locations** (inside the same COD-AB polygons):

| | Capas | Bamban | Mabalacat |
|---|---|---|---|
| OSM shops and listed amenities, 2026-11-02 | 328 | 116 | 509 |
| [Overture places](https://docs.overturemaps.org/attribution/) 2026-10-21.0 | 1,284 | 523 | 3,734 |
| Overture, confidence ≥0.8 | 220 | 120 | 649 |

Across the three municipalities, 7-Eleven shows 20 in OSM and 34 in Overture, and Alfamart shows 13 in OSM and 0 in Overture. No ground truth exists, so neither is confirmed.

**Land values.** Official [BIR](https://www.bir.gov.ph/zonal-values) files were not reached. Working targets are RDO 17A for Capas and Bamban and RDO 21A for Mabalacat, from [RAO 002-09 (2009)](https://www.digest.ph/taxation/splitting-of-revenue-district-office-rdo-no-17-tarlac-city-tarlac-rdo-no-21-san-fernando-city-pampanga-rdo-no-23-cabanatuan-city-and-rdo-no-113-davao-city-and-redefining-their) and [RAO 006-19 (2019)](https://www.digest.ph/taxation/creation-of-a-revenue-district-office-at-clark-freeport-zone-in-pampanga-and-delineation-of-its-areas-of-jurisdiction) via secondary digests. These need official confirmation.

**Building permits** ([PSA `0022G4GBPC1`](https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/2G/CONS/BGP/0022G4GBPC1.px), 2024):

| 2024 | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Permits | 200 | 73 | 754 |
| Floor area (m²) | 27,012 | 20,901 | 703,714 |
| Derived ₱/m², all | 15,128 | 10,081 | 12,441 |

Value is inferred as thousand pesos, and that unit is unconfirmed. These are declared permit values, not audited costs, and they swing widely by year.

**Employment.** No municipal table was found across 3,560 [OpenSTAT](https://openstat.psa.gov.ph) catalogue entries. [DTI competitiveness profiles](https://cmci.dti.gov.ph/) give scores, not counts.

**Traffic.** No open corridor AADT was found; [FOI records](https://foi.gov.ph/requests/annual-average-daily-traffic-aadt-and-traffic-growth-rate) show it is released on request. A [press report](https://malaya.com.ph/business-news/sctex-posts-record-high-p3-26b-revenue) gives whole-expressway average daily traffic of 70,894 vehicles (2022), which is context only. Philippine freight trip rate and corridor mode share: Not found.

**Environment (not scored, sampled for site screening only):**

| 2021–2026 layers | Capas | Bamban | Mabalacat |
|---|---|---|---|
| [Copernicus DEM](https://registry.opendata.aws/copernicus-dem/), median elevation (m) | 188.1 | 315.7 | 99.4 |
| [ESA WorldCover 2021](https://esa-worldcover.org/en/data-access), built cells % | 3.0 | 3.0 | 18.4 |
| [NOAH 100-year flood](https://huggingface.co/datasets/bettergovph/project-noah-hazard-maps) (third-party mirror), any hazard % of COD-AB area | 27.4 | 21.6 | 34.2 |

**Discount rate.** None locked. A [2017 report](https://ptvnews.ph/govt-fast-tracks-approval-of-infra-projects-to-boost-growth/) gives a national social discount rate of 10%, a public-project reference rather than a franchise cost of capital. Its current official status: Not found.

Details are in [`research/findings/`](research/findings/).

## 6. Selected, alternative and rejected sources

| Need | Selected (provisional) | Alternative | Rejected or held, and why |
|---|---|---|---|
| Boundary | COD-AB v03, placeholder | OSM as sensitivity | geoBoundaries as independent proof: same lineage |
| Roads | Geofabrik OSM | Overture, HOT export | Planet held: non-commercial |
| Buildings | Google v3 under CC BY 4.0 | Microsoft via GitHub; Overture and OSM | Footprint area as floor area: different measure |
| Population totals | PSA 2024 | PSA 2020 check | HDX projection: superseded, kept for the gate |
| Distribution | R2025A 2024 within units, rescaled to PSA | Google building shares | Id 6316: Mabalacat misallocation 58.9% |
| Stores | Overture plus OSM | Company lists replace both | Store-locator scraping: terms unread |
| Building cost | PSA permit-implied ₱/m² | None | Not a franchise fit-out cost |
| Land values | BIR RDO 17A, 21A (not obtained) | None | RDO 21B for Mabalacat; third-party zonal sites: they conflict and rights are unknown |
| Foot traffic | None | Paid or partnership data, needs Joshua | Both Kaggle rows: no relevant data |

The authoritative list, with reasons, is [`research/data-source-register.csv`](research/data-source-register.csv).

## 7. Scope conflicts and working interpretation

The notes describe two scopes:
- [`03-poc-decision-freeze.md`](geoteron-second-brain/03-poc-decision-freeze.md) remains LOCKED on an infrastructure decision, Before phase only.
- [`08-new-scope-franchise-draft.md`](geoteron-second-brain/08-new-scope-franchise-draft.md) and [`09-co-researcher-brief-franchise-DRAFT.md`](geoteron-second-brain/09-co-researcher-brief-franchise-DRAFT.md) describe a franchise location check with before and after checks.
- [`07-decision-log.md`](geoteron-second-brain/07-decision-log.md) D-015 tags roads and traffic models as "Beyond POC / later". D-017 brings them back for `08` and `09` only.
- `09` omits road rows from its reading list, although BEH-03 needs roads.

**Working interpretation (AI-selected, not confirmed by Joshua):** research follows the franchise scope, because D-017 is the latest explicit decision. Roads and boundaries count as required because the franchise-scope models need them. No historical document was rewritten.

Would change this: Joshua deciding how to apply the scope change, or removing BEH-01 to BEH-03.

## 8. Who decided what

**Joshua's explicit decisions used here:**
- Updated research direction (2026-11-02).
- Hold the FOI request and use a labelled stand-in blueprint (D-002).
- Franchise brief replaces the hold (D-017).
- Keep scenarios A and B, levers L01, L02, L03, L09, and Behavioral plus Economic scoring (`08`).
- Ask companies for locations first and sales later (`08`).
- Use foot-traffic data as the post-opening stand-in (`08`). **Its named source has no usable data, so this needs his review.**
- Phase 8 limits are working assumptions (D-009).

**AI-selected research decisions, none approved by Joshua:**

| ID | Decision |
|---|---|
| RD-001 | Franchise scope as working interpretation |
| RD-002 | COD-AB as placeholder boundary |
| RD-003 | PSA totals, R2025A distribution, Google fallback |
| RD-004 | Id 6316 is a comparator only; checklist row unchanged |
| RD-005 | Google v3 primary buildings |
| RD-006 | No site assumed; synthetic test points only |
| RD-007 | Geofabrik primary roads; Planet held |
| RD-008 | Overture plus OSM for stores |
| RD-009 | Employment proxy kept with no value |
| RD-010 | RDO 17A and 21A targets; official files only |
| RD-011 | Permit-based cost prior; no discount rate locked |
| RD-012 | Limits on environmental and lifecycle research |
| RD-013 | Rows 6.1 and 6.2 unsuitable |
| RD-014 | Raw third-party data stays out of Git |

Full reasoning: [`research/decisions.md`](research/decisions.md).

## 9. Corrections to earlier findings

Earlier chat read-outs were superseded in these ways. The full list is in [`research/findings/corrections.md`](research/findings/corrections.md).

- The boundary dispute is no longer offered as a likely cause of area gaps.
- The population gate compares the *combined* total with the *projection*, not municipalities with the census.
- "Google is stronger" and "best fit without census inputs" are withdrawn. Microsoft is lower in Capas and Bamban.
- Mapillary's 10.9% and 3.9% were labelled ways. Predicted length is 62.3 km (4.2%) in Mabalacat, 3.9 km (0.6%) in Bamban, and 0 km in Capas.
- Planet is not "the best" source, and its restriction blocks only that dataset.
- Keeping ODbL layers separate does not automatically settle licensing duties.
- Claims that unperformed tests would not change recommendations are withdrawn.
- 2024 national census is 112,727,776 in the PSA table, replacing a secondary figure.

## 10. Blockers, dependencies and next actions

| Blocker | Dependency | Workaround | Next action | AI can continue? |
|---|---|---|---|---|
| Official land values | BIR files | None defensible | A person downloads RDO 17A, 21A | External |
| Terms unread | PSA, BSP, HDX pages return 403 | Record as unresolved | A person reads them | External |
| Commercial use, ODbL duties | Joshua; legal view | Use CC BY route for buildings | Joshua decides; legal review | External |
| Boundary authority | Official polygon, dispute status | COD-AB placeholder | LGU or legal confirmation | External |
| Traffic, mode, freight, employment | Agency data | Low-band placeholders, no invented values | Joshua decides on requests | External |
| Zoning plans | LGU or FOI request | OSM land use as weak context | Joshua decides | External |
| Real site location | Joshua or a franchise company | Labelled synthetic test points | Supply a location | External |
| Cost and return definition | Joshua (`08` question 2) | Candidate measures listed | Define it | External |
| Sales, foot traffic, post-opening | Outreach or purchase, privacy review | None from public data | Joshua decides | External |
| Road and building depth | None | Not applicable | Graph and footprint comparisons outside the database | AI can continue |
| Validation standards, D-009 limits | None | Not applicable | Bounded research round | AI can continue |

Full list: [`research/blockers.md`](research/blockers.md).

## 11. Supporting records and reproducible methods

| Record | Purpose |
|---|---|
| [`research/README.md`](research/README.md) | Research record overview |
| [`research/data-source-register.csv`](research/data-source-register.csv) | 104 datasets with separate statuses |
| [`research/decisions.md`](research/decisions.md) | Decision record |
| [`research/blockers.md`](research/blockers.md) | Blockers and evidence gaps |
| [`research/findings/`](research/findings/) | Source assessments |
| [`research/findings/unsuccessful-searches.md`](research/findings/unsuccessful-searches.md) | Failed searches and rejected options |
| [`research/evidence-manifest.csv`](research/evidence-manifest.csv) | Provenance, versions, hashes |
| [`research/evidence/scripts/`](research/evidence/scripts/) | Methods; earlier scripts are in `legacy/` |
| [`research/evidence/results/`](research/evidence/results/) | Result tables |
| [`research/evidence/session-extracts/`](research/evidence/session-extracts/) | Tool outputs behind logged results |

**What is not in this repository:** raw third-party data, the Planet dataset, and full conversation logs. Raw files stayed in a git-ignored local folder, so a fresh clone must re-download them using the manifest's URLs and checksums. Overture removes old releases, and live OSM queries will not return the same snapshot. Before publication, raw Planet sample rows were removed from one extract, and PSA's filtered permit table was kept local because PSA terms are unread. Local file paths in extracts were replaced with a placeholder, and a token-like value was redacted.

## 12. What has and has not been done

| Done | Not done |
|---|---|
| Access tests and samples | Ingestion of any dataset |
| Local diagnostics in temporary analysis files | PostGIS or any database work |
| Source selection for evaluation | Final data or model selection |
| Barangay distribution comparison | Validation of any dataset or baseline |
| Terms reading where reachable | Legal clearance for any dataset |
| Connectivity sample | Road graph, SUMO network or routability test |
| Candidate cost measures | ECO-FIN-01, BEH, UNC or AFTER model work |

No dataset is validated, calibrated or model-ready.
