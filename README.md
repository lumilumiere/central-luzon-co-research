# Central Luzon industrial district POC — Co-Research Report

**Branch:** `co-research-report`. **Research date:** 2026-11-02 PHT, which is the access date for every source below unless stated. **Contributor:** lumilumiere.

This report stands alone. The project notes in [`geoteron-second-brain/`](geoteron-second-brain/) and [`context/`](context/) are unchanged historical records.

**Read this first:** this is completed *research*, not completed *implementation*.
- Nothing has been ingested, calibrated, validated, approved or declared model-ready.
- No baseline, road network, simulation or database exists from this work.
- A reachable source is not automatically suitable or permitted.
- Recommendations are provisional. Joshua owns model selection and implementation choices.
- Several requirements remain blocked by external dependencies, listed in section 8.

## 1. Assignment and boundaries

**Original assignment:** verify whether the study-area boundary, roads, buildings and population datasets can be obtained and used for Capas and Bamban (Tarlac) and Mabalacat (Pampanga), each checked separately.

**Expanded assignment (Joshua's direction, relayed 2026-11-02):**
- Consider every dataset the project references.
- Register research in the repository.
- Select sources and priorities without repeated approval.
- Complete the research tracks in the co-researcher briefs: data access, validation standards, legal and access process, model inputs, and background.

**Boundaries kept:**
- No database changes, ingestion, SUMO builds or model runs.
- No outreach, FOI filing, purchases or new contract terms.
- No legal clearance is claimed.
- The name "Central Luzon industrial district POC" is used, with no agency or project brand.

Every requirement and its status is in [`research/requirements-checklist.md`](research/requirements-checklist.md).

## 2. Completed work and principal findings

1. **The planned foot-traffic source has no usable data.**
    - The Kaggle bundle named in checklist row 6.1 holds a US real-estate sample with no Philippine rows.
    - Row 6.2 is New York data.
    - No public source of actual store sales or visits was found, so the post-opening check cannot run ([post-opening assessment](research/findings/post-opening-data.md)).
2. **The checklist population raster fails the combined gate.**
    - WorldPop id 6316 gives 0.691–0.807 of the 2020 projection sum, depending on boundary and masking.
    - Its barangay share mismatch in Mabalacat is 58.9%.
    - All figures were recomputed on 2026-11-02 in a rebuilt environment.
3. **R2025A fits best, partly by construction.** It reproduces 2020 census totals to 0.01% after national scaling, because the 2020 barangay census is one of its inputs. That is agreement with an input, not validation.
4. **Roads are not yet routable as extracted.** A directed test of OSM roads (2026-11-02) puts 96.3% of nodes in the largest strongly connected component. The shared-node test (98.8% of ways) overstated routability.
5. **Most D-009 limits have no published standard behind them.** Published practice defines study areas by influence (TAG, NCTS), and validates flows and journey times against counts (TAG: 85% of links, journey times within 15%).
6. **Land values point to different tax districts than the checklist.** Mabalacat appears to fall under RDO 21A, not 21B, and Capas and Bamban under RDO 17A. Official BIR files were not reached.
7. **Municipal building permits are a usable local cost and intensity source** for 2022–2024. The thousand-peso unit is supported by PSA's release convention.
8. **Model inputs are mostly borrowed, and labelled so.** ITE trip rates, UK employment densities and national company figures are recorded with limits. Philippine trip rates, mode shares, freight rates, municipal jobs and store economics are Not found.

## 3. Task status summary

| Area | Status | Notes |
|---|---|---|
| Original four-dataset access | Completed | Section 4 |
| Suitability of the four groups | Partial | Boundary authority, building accuracy and routability open |
| Every-dataset inventory | Completed | 115-row register |
| Validation standards and D-009 | Completed (research) | Recommendations, not adopted |
| Legal, licensing and access process | Partial | PSA and BIR terms unread; legal review needed |
| Model inputs and financial definitions | Partial | Candidates and working interpretation; many local values Not found |
| Post-opening data | Blocked, with assessment done | Schema and template prepared |
| Background research | Completed | Prior art, reviewer categories, open questions |
| Reproduction of material calculations | Completed | One script bug found and fixed |
| Land values, traffic counts, employment, store data | Blocked | External actions in section 8 |
| Implementation (database, ingestion, models) | Not started | Out of bounds |

## 4. Original four dataset groups

### Boundary

| km² | [COD-AB v03](https://data.humdata.org/dataset/cod-ab-phl) | OSM (2026-11-02) | [PSA land area](https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/1A/PO_2024/0221A6DLPD0.px) (LMB 2019) |
|---|---|---|---|
| Capas | 446.48 | 440.80 | 448.04 |
| Bamban | 207.48 | 177.48 | 344.14 |
| Mabalacat | 97.55 | 149.66 | 166.80 |

- **Recommendation:** COD-AB v03 as a labelled placeholder, with OSM as sensitivity.
- **Reasons:** valid geometry, and barangay codes that join PSA 62 of 62.
- **Limits:**
    - Most of Mabalacat's OSM-only area (41.95 km²) lies in COD-AB Angeles.
    - A Bamban–Mabalacat dispute ([2011 report](https://philstar.com/nation/2011/07/09/703823/tarlac-board-opposes-mabalacat-cityhood-amid-boundary-row)) is not established as the cause of the gaps, and its current status is Not found.
- Details: [`boundaries.md`](research/findings/boundaries.md).

### Roads

- **Source:** [Geofabrik OSM](https://download.geofabrik.de/asia/philippines.html), 2026-10-31.
- **Attributes:** on major roads, `lanes` covers 85–100% of length; local coverage is about 18–23% (ohsome, 2026-07-27).
- **Routability:** not demonstrated (directed test above).
- **Alternatives:** the Planet road surface dataset is non-commercial and held; its restriction affects that dataset only.
- Details: [`roads-and-transport.md`](research/findings/roads-and-transport.md).

### Buildings

| Footprints | Capas | Bamban | Mabalacat |
|---|---|---|---|
| [Google v3](https://sites.research.google/gr/open-buildings/) ≥0.65 (May 2023 inference) | 76,827 | 37,523 | 95,257 |
| [Microsoft](https://github.com/microsoft/GlobalMLBuildingFootprints) (2023-04-25 content) | 35,920 | 17,737 | 29,753 |

- Counts are not accuracy, and no source is ranked.
- Google is primary for its CC BY option and confidence field.
- Details: [`buildings.md`](research/findings/buildings.md).

### Population

| Persons | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Census 2024 (1 July, PSA) | 162,724 | 81,012 | 306,594 |
| [R2025A 2024](https://hub.worldpop.org/geodata/summary?id=74942), COD-AB | 165,127 | 82,809 | 306,846 |
| Barangay share mismatch, R2025A / Google / id 6316 (%) | 1.6 / 10.1 / 19.3 | 2.3 / 8.6 / 16.0 | 4.7 / 11.0 / 58.9 |

- **Recommendation:** PSA census totals, with R2025A only to distribute within units. Google building shares as fallback.
- Details and caveats: [`population.md`](research/findings/population.md).

## 5. Dataset recommendations

| Need | Selected (provisional) | Alternative | Rejected or held |
|---|---|---|---|
| Boundary | COD-AB v03 | OSM sensitivity | geoBoundaries as independent proof |
| Roads | Geofabrik OSM | Overture, HOT export | Planet (non-commercial) |
| Buildings | Google v3 (CC BY 4.0) | Microsoft GitHub; Overture; OSM | Footprint area as floor area |
| Population | PSA 2024 + R2025A within units | Google building shares | Id 6316 and id 49861 |
| Stores | Overture places + OSM | Company lists replace both | Store-locator scraping |
| Building cost | PSA permit ₱/m² | None | As franchise fit-out cost |
| Land values | BIR RDO 17A, 21A (not obtained) | None | RDO 21B; third-party zonal sites |
| Foot traffic | None | Paid or partnership, Joshua's call | Both Kaggle rows |
| Traffic validation | None open | 2012 JICA counts (dated, manual reading) | — |

Full register: [`research/data-source-register.csv`](research/data-source-register.csv).

## 6. Validation and financial findings

**Validation** ([`validation-standards.md`](research/findings/validation-standards.md)):

| D-009 assumption | Published standard | Recommendation |
|---|---|---|
| 2–5 km buffer | Not found | Replace with an influence rule |
| Coverage ≥95% | Not found | Split into extent and completeness |
| At most 1 major disconnected component | Not found | Use a directed strong-component test |
| Population within 20% of projections | Not found | Rescale to census and test barangay shares |

Imported benchmarks recorded: TAG M3.1, FHWA 2019 criteria, NCHRP 934 forecast accuracy, AACE bands (secondary), and Sirko et al. building thresholds.

**Financial** ([`model-inputs-and-financial.md`](research/findings/model-inputs-and-financial.md)):
- **Working interpretation (AI-selected):** store-level franchisee view, with investment, four-wall EBITDA, payback, break-even sales, and NPV over a 5- and 10-year term.
- **Discount rate:** a private rate, not the 10% social rate. Damodaran's January 2026 total equity risk premium for the Philippines is 6.69%. A dated official yield is Not found.
- **National reference:** about ₱64,800 per 7-Eleven store-day in 2024, derived from secondary figures.

## 7. Decisions, limitations and corrections

- **Working scope:** the franchise check in `08` and `09`, with infrastructure items kept as history. This is AI-selected and not confirmed by Joshua ([`decisions.md`](research/decisions.md) RD-001).
- **Decisions:** Joshua's explicit decisions (JD rows) are kept apart from AI research decisions (RD-001 to RD-020).
- **Corrections:** 26 are recorded ([`corrections.md`](research/findings/corrections.md)), including:
    - The barangay measure is an aggregate share mismatch, not evidence of where people live.
    - Weak connectivity overstated routability.
    - Earlier "Google is stronger" claims are withdrawn.

## 8. Remaining external dependencies

| Dependency | Exact action needed |
|---|---|
| Official BIR zonal schedules | A person downloads RDO 17A and 21A schedules and confirms jurisdictions |
| PSA and BSP terms | A person reads the terms pages in a browser (403 to tools) |
| Commercial use, ODbL duties | Joshua states the use; legal review |
| Official boundary, dispute status | Agency or LGU request (template T-03) |
| Traffic counts, routes, employment, zoning | Requests T-01, T-04, T-05, T-06 (unsent) |
| Store sales, visits, post-opening data | Company data-sharing or purchase, plus a privacy review (T-07, T-08) |
| Cost and return definition | Joshua decides (`08` question 2) |
| A real candidate location | Joshua or a franchise company |
| 2012 JICA station counts | A person reads Appendix A tables |
| Paid standards and accounts (ITE, AACE, Earth Engine) | Joshua decides on purchase or accounts |

Full list: [`research/blockers.md`](research/blockers.md). Templates: [`research/acquisition/request-templates.md`](research/acquisition/request-templates.md).

## 9. Supporting records

| Record | Purpose |
|---|---|
| [`research/README.md`](research/README.md) | Record overview and navigation |
| [`research/requirements-checklist.md`](research/requirements-checklist.md) | Requirement status |
| [`research/data-source-register.csv`](research/data-source-register.csv) | Dataset register |
| [`research/decisions.md`](research/decisions.md) | Decision record |
| [`research/blockers.md`](research/blockers.md) | Blockers |
| [`research/methods.md`](research/methods.md) | Reproducible methods |
| [`research/findings/`](research/findings/) | Findings |
| [`research/evidence-manifest.csv`](research/evidence-manifest.csv) | Evidence manifest |
| [`research/evidence/`](research/evidence/) | Scripts, results, environment lock |

**Kept out of the repository:** raw third-party data, the restricted Planet dataset and full conversation logs. They are in a git-ignored local folder and can be rebuilt from the manifest's URLs and checksums.

## 10. Implemented, validated, and next steps

**Not implemented or validated:** any ingestion, database, road graph, SUMO network, trip, mode, financial or post-opening model, or validation of any dataset or baseline.

**Next steps the evidence supports:**
1. **Joshua decides:**
    - Scope application.
    - Commercial use.
    - The cost and return definition.
    - Whether to send requests T-01 to T-08.
    - The D-009 recommendations.
2. **Bounded technical evaluation outside the database:**
    - Pin input versions.
    - Build a barangay zone table from PSA 2024 totals on COD-AB polygons.
    - Repair and trim the directed road graph and report its strong-component share.
    - Test with labelled synthetic sites.
3. **When data arrives:** read the 2012 JICA counts, parse official BIR schedules, and run TAG-style link and journey-time checks against any new counts.

**Cannot proceed:** post-opening comparison, traffic calibration, sales forecasting validation and land-value inputs until the external dependencies above are met.
