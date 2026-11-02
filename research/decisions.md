# Research decisions — Central Luzon industrial district POC

**Date:** 2026-11-02. **Status:** working record.

This file separates two kinds of decision.

- **JD** rows are Joshua's own decisions, as recorded in the notes or relayed to the researcher. They are copied here for reference and are not changed.
- **RD** rows are research decisions made by the AI researcher under Joshua's updated direction. They are working choices. **None of them is Joshua-approved** unless a later JD row says so.

Nothing here rewrites the freeze or the decision log. `03-poc-decision-freeze.md`, `07-decision-log.md` and the other notes stay as historical records and were not edited.

## Joshua's decisions used here

| ID | Decision | Source |
|---|---|---|
| JD-01 | Research direction updated: consider every referenced dataset, register research in the repository, and choose priorities, sources and working datasets without repeated approval. This supersedes the spreadsheet-only restriction and waiting on routine research choices. It does not authorise database changes, purchases, outreach or publishing repository changes. | Relayed in the research instruction of 2026-11-02 |
| JD-02 | Build a labelled stand-in blueprint and hold the FOI request until after the quiet validation review. | D-002 |
| JD-03 | Franchise brief replaces the hold; BEH-01 to BEH-03 and `05` item 6.1 are in franchise scope in `08` and `09`, with their tags elsewhere unchanged. | D-017 |
| JD-04 | Keep scenarios A and B, levers L01, L02, L03, L09, and Behavioral plus Economic scoring. | `08` answers 6, 7, 8 |
| JD-05 | Ask franchise companies for store locations first and sales later. | `08` answer 10 |
| JD-06 | The post-opening check uses foot-traffic data (`05` item 6.1) as a stand-in, labelled Low. | `08` answer 9 |
| JD-07 | The Phase 8 limits are working assumptions, not sourced standards. | D-009 |
| JD-08 | Joshua owns model selection and pipeline architecture. | `06`, `09` ground rules |

## Research decisions

### RD-001 — Working scope

- **Chosen:** the franchise location check in `08` and `09` governs research: help a franchising company decide whether to open at a specific location in Capas, Bamban or Mabalacat, under scenarios A and B, with a before check and an after check, scored on Behavioral and Economic. This repository record covers every dataset the project mentions, and classifies each one against that scope.
- **Supporting references:**
    - D-017 is the latest explicit scope decision and states `09` replaces the hold for the franchise brief.
    - `08` records CEO confirmation of subject, area, buyers, decision and two checks.
    - JD-04 keeps scenarios, levers and scoring.
- **Conflicting or historical instructions:**
    - `03` remains LOCKED on an infrastructure decision, Before only, with AFTER-* not required (§2, §9).
    - `08` says nothing overrides the freeze until Joshua decides how to apply the change.
    - D-015 tags the road phase, BEH models and much of Phase 6 as "Beyond POC / later". D-017 pulls some of these back for `08` and `09` only.
    - `09` omits road rows from its reading list, although BEH-03 needs a road network.
    - `07` "Open" leaves the fate of `01` to `05` undecided.
- **Assumptions:** dates and explicit decisions outrank tags. A later explicit decision outranks a general label. The freeze is a historical lock on the infrastructure version, not a statement that the franchise work may not proceed.
- **Consequences:**
    - Roads and boundaries are treated as required, because the franchise-scope models need them.
    - Infrastructure-only items such as DPWH road costs and the budget cap are classified as future work.
    - No tag or note was changed.
- **Would change this:** a Joshua decision on how to apply the scope change, a written confirmation that differs from `08`, or removal of BEH-01 to BEH-03.

### RD-002 — Provisional boundary

- **Chosen:** COD-AB v03 municipal polygons as a labelled analytical placeholder, with OSM polygons as sensitivity and Mabalacat plus Angeles reported together as a border-robust check.
- **Why:** valid geometry, stable identifiers, barangay polygons that join 62 of 62 to PSA codes, and R2025A 2020 sums that reproduce census totals to 0.01% on Bamban, Capas and Mabalacat + Angeles after national scaling.
- **Rejected:** OSM as primary (it overlaps 41.95 km² of COD-AB Angeles and has no authority). geoBoundaries as independent evidence (same lineage).
- **Limits:** Bamban and Mabalacat disagree with PSA land area. Not a legal boundary or a site boundary.
- **Would change this:** an official polygon, or a confirmed correction to the Mabalacat–Angeles line.

### RD-003 — Population totals and distribution

- **Chosen for evaluation:** PSA 2024 municipal and barangay counts for totals. R2025A 2024 only to distribute population inside a barangay, rescaled to PSA totals. PSA 2020 as a check year.
- **Why:** barangay share mismatch (aggregate shares, not individual locations) is 2.3% in Bamban, 1.6% in Capas and 4.7% in Mabalacat for R2025A, against 16.0%, 19.3% and 58.9% for id 6316. Recomputed on 2026-11-02.
- **Limit:** R2025A is alpha and used the 2020 barangay census as input. Its fit is not independent validation.
- **Fallback:** Google building-count shares, which do not use census inputs (at 0.65: Bamban 8.6%, Capas 10.1%, Mabalacat 11.0%). Microsoft is lower in Capas (6.6%) and Bamban (7.4%) but higher in Mabalacat (18.8%), so Google is chosen for its smaller worst case, and because it has confidence values.
- **Would change this:** an R2025A revision, or a local check that favours another layer.

### RD-004 — Checklist raster

- **Chosen:** classify WorldPop id 6316 as unsuitable for zone-level use, and keep it only as a comparator. This does not change the checklist row, which stays as Joshua wrote it.
- **Why:** the combined gate is not met on COD-AB polygons (0.691 of the projection sum, or 0.712 all-touched). Mabalacat stays 0.549–0.724 of the census in all four tested cases. Barangay share mismatch in Mabalacat is 58.9% (aggregate shares). Id 49861 on OSM polygons, previously not performed, gives 0.792–0.804 of the projection sum: the same pattern.
- **Limit:** the cause is Not found. Bamban and Capas stay within 20% as diagnostics.

### RD-005 — Buildings

- **Chosen:** Google Open Buildings v3 as primary, under its CC BY 4.0 option. Microsoft via GitHub as fallback. Overture and OSM buildings as comparators.
- **Why:** clearest licence route and the only source of per-footprint confidence in this corridor. This is **not** a claim of higher accuracy: no corridor accuracy evidence was found.

### RD-006 — Site inputs

- **Chosen:** no site is assumed. Any technical test before a real location arrives uses labelled synthetic test points.
- **Would change this:** a real candidate location from Joshua or a franchise company.

### RD-007 — Roads

- **Chosen:** Geofabrik OSM as primary, pinned by date and MD5. HeiGIT Mapillary stays optional. HeiGIT Planet stays held until commercial use is settled. Local `lanes` and `maxspeed` need documented class defaults.
- **Why:** the Planet restriction applies to that dataset only.

### RD-008 — Store locations

- **Chosen:** Overture places as the discovery layer, OSM as cross-check, and the union for competition counts. Company lists replace both when received (JD-05).
- **Why:** Overture lists more places, but shows 0 Alfamart where OSM shows 13, so neither is safe alone.
- **Limit:** no ground truth. Store-locator scraping was not attempted.

### RD-009 — Employment

- **Chosen:** keep `05` row 4.6 as a Low-band proxy, assign no value yet, and use DTI competitiveness scores and building permits as context only.
- **Why:** a walk of 3,560 OpenSTAT table entries found no municipal employment or establishment table.

### RD-010 — Land values

- **Chosen:** target RDO 17A for Capas and Bamban and RDO 21A for Mabalacat, using official BIR files only. Third-party zonal sites are leads, not sources.
- **Why:** secondary sources place Mabalacat under 21A, and the checklist's 21B looks wrong. Those secondary sources also conflict, so this needs official confirmation.
- **Checklist note:** rows 5.1 and 5.2 stay as written; the correction is recorded here.

### RD-011 — Cost and discount inputs

- **Chosen:** PSA permit-implied ₱/m² as the local building-cost prior. No discount rate is locked. The 10% social rate is recorded as a borrowed public-sector reference only.
- **Why:** a franchise investor's cost of capital is not a public-project hurdle rate.
- **Limit:** the permit value unit is inferred as thousand pesos.

### RD-012 — Research limits

- **Chosen:** record environmental, ecological, societal and lifecycle datasets, and sample only terrain, land cover and flood, because they cost little and can flag a site. Water, energy, CO₂, air, noise, heat, waste, social and DURING sources were not searched in depth.
- **Why:** they are not scored, levers L04–L08 are frozen out, and an open-ended search would not change any current decision.

### RD-013 — Foot traffic

- **Chosen:** classify `05` rows 6.1 and 6.2 as unsuitable, on direct file inspection. JD-06 remains Joshua's decision, but its named source has no usable data, so the after check has no source today. No replacement is treated as chosen.
- **Temporary approach:** none is defensible from public data. See blocker B-11.
- **Would change this:** company sales or visit data, or a purchased and privacy-reviewed mobility source, either of which needs Joshua.

### RD-014 — Evidence storage

- **Chosen:** third-party raw data and geometry go in `research/local-data/`, which is git-ignored. Tracked files hold scripts, queries, metadata, excerpts and our own result tables. Planet data is under `local-data/restricted/`. Full conversation logs are excluded.
- **Why:** several licences are unresolved or share-alike, and unresolved terms cannot be assumed to allow redistribution.

## Name-safety

Findings use "Central Luzon industrial district POC". The development authority and project brand are not named, following the notes' name-safe rule. Publisher names of datasets are kept, as citations require.

## Completion pass, 2026-11-02 (AI-selected, not Joshua-approved)

### RD-015 — Requirement scope categories

- **Chosen:** requirements are tracked in three groups in [`requirements-checklist.md`](requirements-checklist.md): current franchise scope, shared baseline, and infrastructure or longer-term.
- **Effect:** the longer-term dimensions (environmental, ecological, societal, construction-phase) are researched as data sources only. They do not become scored features.
- **Why:** `03` §7 and `08` answer 8 keep them as placeholders.

### RD-016 — Working franchise financial interpretation

- **Chosen for evaluation:**
    - Store-level franchisee view.
    - Measures: investment, four-wall EBITDA, payback, break-even sales, NPV and ROI over the agreement term, tested at 5 and 10 years.
    - A private discount rate built from a risk-free rate plus equity premium, with Damodaran January 2026 data for the Philippines as the premium reference.
- **Rejected:** the 10% social discount rate as the franchise rate (a public-project hurdle); building-permit ₱/m² as fit-out cost (declared building values only).
- **Limits:** Joshua's definition (`08` question 2) overrides this. No rate is locked, because a dated official yield is Not found.
- Details: [`findings/model-inputs-and-financial.md`](findings/model-inputs-and-financial.md).

### RD-017 — D-009 recommendations

- **Recommended:**
    - Replace the 2–5 km buffer with an influence rule.
    - Revise "coverage ≥95%" into separate extent and completeness measures.
    - Revise "≤1 major component" into a directed strong-component test.
    - Replace the 20% projection check with census rescaling plus barangay share tests.
- **Status:** recommendations only. D-009 says these are Joshua's working assumptions, and the checklist is unchanged.
- Evidence: [`findings/validation-standards.md`](findings/validation-standards.md).

### RD-018 — Post-opening data

- **Chosen:** no public source is treated as observed sales or visits. Proxies stay labelled as proxies, and synthetic data is never used as validation.
- **Prepared:** a minimum schema and request templates, unsent.
- **Effect:** AFTER-01 functions remain impossible until company or purchased data exists.

### RD-019 — Reproduction environment

- **Chosen:** a fresh Python 3.14 environment with pinned packages ([`evidence/requirements-lock.txt`](evidence/requirements-lock.txt)).
- **Reproduced:** all material population, barangay, boundary and footprint calculations from retained files, with results in `evidence/results/reproduction_*`.
- **Integrity versus validation:** a matching file hash is an integrity check only. The calculations were re-executed to check them.

### RD-020 — Directed routability diagnostic

- **Chosen:** report strong connectivity on a directed graph from OSM `oneway` tags, and stop reporting weak connectivity as routability.
- **Why:** weak connectivity (98.8% of ways) overstated what a router can use (96.3% of nodes in the largest strong component).
