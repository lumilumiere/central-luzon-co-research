# Requirement-completion checklist — Central Luzon industrial district POC

**Updated:** 2026-11-02.

**Status terms:**
- **Completed:** a substantive deliverable exists.
- **Partial:** a deliverable exists with stated gaps.
- **Blocked:** needs an external action, after alternatives were tried.
- **Deferred:** out of the current scope by a recorded decision.
- **Not applicable:** not research.

Research completion is not implementation. Nothing here is ingested, calibrated or validated.

**Sources of requirements:**
- Original data-access assignment.
- `06` co-researcher brief (infrastructure, historical).
- `09` franchise brief.
- `05` ingest checklist.
- D-009.
- Joshua's expanded instruction (consider every dataset).
- The completion instruction of 2026-11-02.

Scope groups follow RD-015.

## A. Current franchise scope (`08`, `09`)

| # | Requirement | Status | Deliverable or blocker |
|---|---|---|---|
| A1 | Carry-over layers: population (coverage, freshness, access, licence, format, quality, single-site fit, alternatives) | Completed | [`findings/population.md`](findings/population.md); register POP-* |
| A2 | Carry-over layers: building footprints and intensity | Partial | [`findings/buildings.md`](findings/buildings.md); corridor accuracy Not found; use and floor area Not found |
| A3 | Carry-over layers: land values (BIR) | Blocked | B-01; RDO corrections in [`findings/land-values-and-costs.md`](findings/land-values-and-costs.md) |
| A4 | Carry-over layers: discount rate | Partial | Candidates and method in [`findings/model-inputs-and-financial.md`](findings/model-inputs-and-financial.md); dated official yield Not found |
| A5 | Carry-over layers: foot-traffic priors (`05` row 6.1) | Completed (assessed as unsuitable) | [`findings/franchise-and-foot-traffic.md`](findings/franchise-and-foot-traffic.md) |
| A6 | Franchise store locations | Partial | OSM and Overture compared; company lists blocked (B-11) |
| A7 | Store sales or proxies | Blocked | B-11; national disclosures only |
| A8 | Store-level foot traffic | Blocked | B-11 |
| A9 | Post-opening data | Blocked, with assessment done | [`findings/post-opening-data.md`](findings/post-opening-data.md); schema and template prepared |
| A10 | Track B: franchise validation practice and acceptable accuracy | Partial | [`findings/validation-standards.md`](findings/validation-standards.md); a published franchise accuracy standard is Not found |
| A11 | Track B: single-site traffic assessment and Philippine guidelines | Completed | NCTS proposed TIA guidelines read; adoption status Not found |
| A12 | Track B: predicted versus actual after opening | Completed (methods) | Validation standards §3; data blocked |
| A13 | Track C: redistribution and commercial terms | Partial | [`findings/licensing-and-privacy.md`](findings/licensing-and-privacy.md); PSA and BIR unresolved (B-03) |
| A14 | Track C: Data Privacy Act implications | Partial | Same file; NPC opinions read only via secondary sources |
| A15 | Track C: typical terms for sharing franchise data | Partial | Terms to settle listed in [`acquisition/request-templates.md`](acquisition/request-templates.md); no published standard found |
| A16 | Track D: franchise cost and return measures | Completed (candidates) | RD-016; Joshua decides |
| A17 | Track D: retail and restaurant trip generation | Partial | ITE rates borrowed; Philippine rates Not found |
| A18 | Track D: franchise cost and revenue benchmarks | Partial | National disclosures and derived values; local benchmarks Not found |
| A19 | Track D: link between levers and franchise demand | Partial | Employment density benchmarks (UK); direct evidence Not found |
| A20 | BEH-01 to BEH-03 inputs (in franchise scope by D-017) | Partial | Roads, trip and mode findings; counts blocked (B-06) |
| A21 | Single-site fit of each layer | Completed | Barangay test, flood screening, store density |

## B. Shared baseline research

| # | Requirement | Status | Deliverable or blocker |
|---|---|---|---|
| B1 | Original assignment: boundary access per municipality | Completed | [`findings/boundaries.md`](findings/boundaries.md) |
| B2 | Original assignment: roads access per municipality | Completed | [`findings/roads-and-transport.md`](findings/roads-and-transport.md) |
| B3 | Original assignment: buildings access per municipality | Completed (access) | Buildings note |
| B4 | Original assignment: population access per municipality | Completed | Population note |
| B5 | Record in the source register | Completed | [`data-source-register.csv`](data-source-register.csv) (the original spreadsheet was never found; superseded by JD-01) |
| B6 | Scope discrepancy handling | Completed | [`decisions.md`](decisions.md) RD-001, RD-015 |
| B7 | Consider every referenced dataset | Completed | Register, with families and classifications |
| B8 | Identifiers and crosswalks | Completed | 62/62 barangay join; per-municipality name matching |
| B9 | D-009: buffer | Completed (research) | Validation standards §2; recommendation, not adopted |
| B10 | D-009: coverage ≥95% | Completed (research) | Same |
| B11 | D-009: disconnected components | Completed (research) | Same, with directed test |
| B12 | D-009: population tolerance | Completed (research) | Same |
| B13 | Official boundary and dispute status | Blocked | B-02 |
| B14 | Employment and socioeconomic sources | Partial | [`findings/employment-and-socioeconomic.md`](findings/employment-and-socioeconomic.md); municipal jobs Not found |
| B15 | Building permits and development intensity | Completed | Land values and costs note |
| B16 | Reproduce material calculations | Completed | [`methods.md`](methods.md); `evidence/results/reproduction_*` |
| B17 | Evidence preservation with hashes | Completed | [`evidence-manifest.csv`](evidence-manifest.csv) |
| B18 | Request templates and acquisition specifications | Completed (unsent) | [`acquisition/request-templates.md`](acquisition/request-templates.md) |
| B19 | Background: prior art, reviewer categories, open questions | Completed | [`findings/background-research.md`](findings/background-research.md) |

## C. Infrastructure and longer-term research

| # | Requirement | Status | Deliverable or blocker |
|---|---|---|---|
| C1 | `06` Track A gaps: jobs, traffic counts, construction costs, blueprint | Partial | Jobs blocked; counts blocked with dated JICA source; permit costs found; blueprint held (D-002) |
| C2 | `06` Track B: traffic calibration standards; SUMO with sparse data | Partial | TAG and FHWA criteria read; SUMO sparse-data literature beyond netconvert notes Not found |
| C3 | `06` Track B: early-stage cost accuracy | Partial | AACE bands via secondary summaries only |
| C4 | `06` Track C: FOI process | Completed | EO 2 §9 read; agency turnaround Not found |
| C5 | `06` Track D: trip, freight, mode priors for the corridor | Partial | Freight and mode Not found |
| C6 | `06` Track D: government unit costs | Deferred | DPWH costs are infrastructure-only (D-015) |
| C7 | Prior art and competitors | Completed | Background note |
| C8 | Validation partner map | Completed (categories only) | No contact |
| C9 | Ecological sources (ECOL-00) | Completed (inventory) | Register ENV-*; not scored |
| C10 | Environmental layers (DEM, flood, hazard) | Completed (sampled) | [`findings/environment-and-hazard.md`](findings/environment-and-hazard.md) |
| C11 | Societal, water, energy, emissions and construction-phase data | Deferred | RD-012; not scored |
| C12 | Stand-in blueprint | Not applicable | A project build task (D-002), not research |

## Not research (not done, by instruction)

Database setup, ingestion, SUMO network construction, model runs, outreach, purchases and publishing to Joshua's repository.
