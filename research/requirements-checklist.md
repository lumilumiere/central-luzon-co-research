# Requirement-completion checklist — Central Luzon industrial district POC

**Updated:** 2026-11-02, closeout pass.

**Status terms (RD-023):** one status per item.
- **Completed:** a substantive deliverable exists, and its limits are stated.
- **Searched; no suitable evidence found:** the searches listed in the deliverable were run and found nothing usable. This is not a claim that no source exists.
- **Blocked:** a specific external dependency is named, with its blocker ID.
- **Deferred:** out of the current scope, for a documented reason.
- **Still incomplete:** research that could continue with the tools available here but was not finished.

Items that had two different states are split into lettered parts, so no item carries a mixed status. Research completion is not implementation: nothing here is ingested, calibrated or validated.

**Sources of requirements:**
- The original data-access assignment.
- The `06` co-researcher brief (infrastructure, historical).
- The `09` franchise brief.
- The `05` ingest checklist.
- D-009.
- Joshua's expanded instruction to consider every dataset.
- The completion instruction of 2026-11-02.
- The closeout instruction of 2026-11-02.

Scope groups follow RD-015. External actions are listed in [`acquisition/external-actions.md`](acquisition/external-actions.md).

## A. Current franchise scope (`08`, `09`)

| # | Requirement | Status | Deliverable, or dependency |
|---|---|---|---|
| A1 | Population layer (coverage, freshness, access, licence, format, quality, single-site fit, alternatives) | Completed | [`findings/population.md`](findings/population.md); register POP-* |
| A2a | Building footprints: access, licence, counts, fields | Completed | [`findings/buildings.md`](findings/buildings.md) |
| A2b | Building footprint accuracy in the corridor | Blocked (B-15) | Reference sample T-09 or LGU data; [closeout §6](findings/closeout-partial-items.md#6-building-quality--blocked-by-a-specific-external-dependency) |
| A2c | Building use and floor area | Searched; no suitable evidence found | Buildings note; PSA permits give new-permit floor area only |
| A3 | Land values (BIR) | Blocked (B-01) | RDO corrections in [`findings/land-values-and-costs.md`](findings/land-values-and-costs.md) |
| A4 | Discount rate inputs | Completed | Dated 10-year yield 8.076% (ADB, close of 2026-10-29), Damodaran ERP, method. Joshua chooses the rate ([closeout §4](findings/closeout-partial-items.md#4-dated-financial-rate-reference--completed)) |
| A5 | Foot-traffic priors (`05` row 6.1) | Completed (assessed as unsuitable) | [`findings/franchise-and-foot-traffic.md`](findings/franchise-and-foot-traffic.md) |
| A6a | Franchise store locations from open sources | Completed | OSM and Overture compared |
| A6b | Company store lists | Blocked (B-11) | T-07 |
| A7 | Store sales or proxies | Blocked (B-11) | National disclosures only; T-07 |
| A8 | Store-level foot traffic | Blocked (B-11) | T-08 |
| A9 | Post-opening data | Blocked (B-11) | Assessment, schema and template done: [`findings/post-opening-data.md`](findings/post-opening-data.md) |
| A10a | Track B: franchise validation practice | Completed | [`findings/validation-standards.md`](findings/validation-standards.md) §3 |
| A10b | Track B: a published accuracy standard for franchise forecasts | Searched; no suitable evidence found | Validation standards §1 |
| A11 | Track B: single-site traffic assessment and Philippine guidelines | Completed | NCTS proposed TIA guidelines read. Adoption by any LGU: searched; no suitable evidence found |
| A12 | Track B: predicted versus actual after opening (methods) | Completed | Validation standards §3. The comparison itself waits on A9 |
| A13 | Track C: redistribution and commercial terms | Blocked (B-03, B-04, B-05) | [`findings/licensing-and-privacy.md`](findings/licensing-and-privacy.md) |
| A14 | Track C: Data Privacy Act implications | Blocked (B-12, B-05) | RA 10173 read. The NPC opinion compendiums (2020–2021 and 2023) on privacy.gov.ph returned 403 in the closeout pass. A search found no NPC opinion on aggregated location or foot-traffic data. A person reads the compendiums in a browser, then counsel reviews |
| A15 | Track C: typical terms for sharing franchise data | Searched; no suitable evidence found | No published standard terms found. Terms to settle are listed in [`acquisition/request-templates.md`](acquisition/request-templates.md) T-07 |
| A16 | Track D: franchise cost and return measures | Completed (candidates) | RD-016. Joshua decides |
| A17 | Track D: Philippine retail and restaurant trip generation | Searched; no suitable evidence found | [Closeout §2](findings/closeout-partial-items.md#2-trip-rates-mode-shares-and-freight-rates). ITE rates stay borrowed and secondary |
| A18a | Track D: company-level cost and revenue benchmarks | Completed | 17-A margins (primary), Jollibee release, 7-Eleven press figures ([`findings/model-inputs-and-financial.md`](findings/model-inputs-and-financial.md)) |
| A18b | Track D: retail rents in the corridor | Searched; no suitable evidence found | [Closeout §3](findings/closeout-partial-items.md#3-retail-rents-and-store-operating-costs) |
| A18c | Track D: store-level operating costs | Blocked (B-12, B-11) | Full 17-A attachment (browser); franchisee costs need T-07 |
| A19 | Track D: link between levers and franchise demand | Searched; no suitable evidence found | Only UK employment densities found (borrowed) |
| A20 | BEH-01 to BEH-03 inputs: current observed counts | Blocked (B-06) | Network findings done; T-01 or T-10 |
| A21 | Single-site fit of each layer | Completed | Barangay test, flood screening, store density |

## B. Shared baseline research

| # | Requirement | Status | Deliverable, or dependency |
|---|---|---|---|
| B1 | Original assignment: boundary access per municipality | Completed | [`findings/boundaries.md`](findings/boundaries.md) |
| B2 | Original assignment: roads access per municipality | Completed | [`findings/roads-and-transport.md`](findings/roads-and-transport.md) |
| B3 | Original assignment: buildings access per municipality | Completed | Buildings note (accuracy is A2b) |
| B4 | Original assignment: population access per municipality | Completed | Population note |
| B5 | Record in the source register | Completed | [`data-source-register.csv`](data-source-register.csv), 124 rows (the original spreadsheet was never found; superseded by JD-01) |
| B6 | Scope discrepancy handling | Completed | [`decisions.md`](decisions.md) RD-001, RD-015 |
| B7 | Consider every referenced dataset | Completed | Register, with families and classifications |
| B8 | Identifiers and crosswalks | Completed | 62/62 barangay join; per-municipality name matching |
| B9 | D-009: buffer | Completed (research) | Validation standards §2: no published standard was found in the searches performed; recommendation only |
| B10 | D-009: coverage ≥95% | Completed (research) | Same |
| B11 | D-009: disconnected components | Completed (research) | Same, with the directed test |
| B12 | D-009: population tolerance | Completed (research) | Same |
| B13 | Official boundary and dispute status | Blocked (B-02) | T-03 |
| B14 | Municipal employment and establishments | Blocked (B-06) | Searched (3,560 OpenSTAT entries); PSA holds establishment data; T-06 |
| B15 | Building permits and development intensity | Completed | Land values and costs note (the unit is supported by an excerpt only) |
| B16 | Reproduce material calculations | Completed | [`methods.md`](methods.md); `evidence/results/reproduction_*` |
| B17 | Evidence preservation: extracts, queries, timestamps, versions, hashes | Completed | [`evidence-manifest.csv`](evidence-manifest.csv), [`evidence/inputs/`](evidence/inputs/README.md), [`evidence/queries/queries.md`](evidence/queries/queries.md). PSA extracts are not packed because of B-03 |
| B18 | Request templates and acquisition specifications | Completed (unsent) | T-01 to T-10 in [`acquisition/request-templates.md`](acquisition/request-templates.md) |
| B19 | Background: prior art, reviewer categories, open questions | Completed | [`findings/background-research.md`](findings/background-research.md) |
| B20 | Primary-source audit | Completed | [`findings/primary-source-audit.md`](findings/primary-source-audit.md) |
| B21 | Visual reading of the 2012 JICA tables | Completed | [`findings/jica-2012-counts.md`](findings/jica-2012-counts.md); 20/20 checks |
| B22 | Correct unsupported absence claims | Completed | Corrections 27–34; wording rule in RD-023 |
| B23 | One external-action list for Joshua | Completed | [`acquisition/external-actions.md`](acquisition/external-actions.md) |

## C. Infrastructure and longer-term research

| # | Requirement | Status | Deliverable, or dependency |
|---|---|---|---|
| C1a | `06` Track A: current traffic counts | Blocked (B-06) | 2012 JICA counts are historical comparators only (RD-021) |
| C1b | `06` Track A: construction cost indicators | Completed | PSA permit ₱/m² (not fit-out cost) |
| C1c | `06` Track A: jobs | Blocked (B-06) | Same as B14 |
| C2 | `06` Track B: calibration standards and SUMO with sparse data | Completed | Validation standards §1; [closeout §1](findings/closeout-partial-items.md#1-sumo-calibration-with-sparse-data--completed) |
| C3 | `06` Track B: early-stage cost accuracy (AACE) | Blocked (B-13) | Secondary summaries only; the standard is paid |
| C4a | `06` Track C: FOI process | Completed | EO 2 §9; eFOI channel; turnaround report format |
| C4b | `06` Track C: turnaround for target agencies | Searched; no suitable evidence found | A browser check of Transparency Seal pages remains (B-12) |
| C5a | `06` Track D: freight cost prior | Completed | Suarez et al., Luzon 2019 (TR-20) |
| C5b | `06` Track D: corridor mode shares | Searched; no suitable evidence found | Closeout §2 |
| C5c | `06` Track D: freight trip rates | Searched; no suitable evidence found | Closeout §2 |
| C6 | `06` Track D: government unit costs | Deferred | DPWH costs are infrastructure-only (D-015) |
| C7 | Prior art and competitors | Completed | Background note |
| C8 | Validation partner map | Completed (categories only) | No contact made |
| C9 | Ecological sources (ECOL-00) | Completed (inventory) | Register ENV-*; not scored |
| C10 | Environmental layers (DEM, flood, hazard) | Completed (sampled) | [`findings/environment-and-hazard.md`](findings/environment-and-hazard.md) |
| C11 | Societal, water, energy, emissions and construction-phase data | Deferred | RD-012; not scored in the franchise scope |
| C12 | Stand-in blueprint | Deferred | A project build task (D-002), not research |

## Count by status

| Status | Items |
|---|---|
| Completed | 40 |
| Searched; no suitable evidence found | 9 |
| Blocked | 15 |
| Deferred | 3 |
| Still incomplete | 0 |

## Not research (not done, by instruction)

Database setup, ingestion, SUMO network construction, model runs, outreach, purchases and publishing to Joshua's repository.
