# Blockers and evidence gaps — Central Luzon industrial district POC

**Date:** 2026-11-02, updated in the closeout pass. "Not found" in this file means no suitable source was found in the searches performed. Each entry lists what is blocked, what was tried, the impact, the workaround, and who must act. Only items needing unavailable credentials, external permission, spending, outreach or unavailable facts are escalated.

| ID | Blocked | Tried | Impact | Workaround and limits | Needs |
|---|---|---|---|---|---|
| B-01 | Official BIR zonal value files | `bir.gov.ph` page returns a scripted shell with no files. Legacy URL returned no content. Third-party sites found and rejected as sources | Land values, ECO-FIN-01 | None defensible. Third-party figures conflict | A person downloads the current schedules for RDO 17A and 21A, and confirms the RDO for each municipality |
| B-02 | Boundary authority and cause of area gaps | Compared COD-AB, OSM, geoBoundaries, PSA land area. PSA site 403. Dispute reports read; no ruling found | Every clipped total and density | COD-AB placeholder with sensitivity (RD-002) | Official polygon or LGU or legal confirmation |
| B-03 | PSA and BSP terms unread (HDX resolved 2026-11-02 via docs.humdata.org) | PSA OpenSTAT Terms, About and regional pages return 403; BSP 403; archive lookup refused by session controls and not retried; no browser tool in this session. A search excerpt says PSA tables are CC BY | Permission status of PSA tables and BSP data | Technical evaluation continues, recorded as unresolved. No redistribution assumed | A person reads the PSA and BSP terms in a browser |
| B-04 | Commercial status and licence channels | Read Planet field, Microsoft README and Planetary Computer metadata | Planet stays held. Microsoft Planetary Computer route stays held | Use OSM roads and Microsoft via GitHub | Joshua states whether this use is commercial; legal view on ODbL for combined outputs |
| B-05 | ODbL obligations for combined outputs | Read licence statements | OSM, Mapillary, Overture buildings, NOAH | Google under CC BY 4.0 for buildings. Keeping layers separate does not by itself settle obligations | Legal review before production use or redistribution |
| B-06 | Current observed traffic counts, corridor mode shares, freight trip rates, municipal employment, local trip rates | Searched DPWH, FOI records, JICA library, PSA catalogue (3,560 entries), journals, MUCEP manual. Regidor 2006 full text returned 404. The 2012 JICA counts and travel times were transcribed in the closeout pass (historical only). A Luzon road freight **cost** was found (TR-20). No suitable source was found for the other items in the searches performed | BEH-01 to BEH-03 calibration and validation, L02, L03 | Keep Low-band placeholders with no invented values. JICA 2012 and SCTEX whole-road figures are context only | Requests T-01, T-05, T-06 or the survey T-10; Joshua decides ([external actions](acquisition/external-actions.md) 9–10) |
| B-07 | Sites refusing or failing | PEZA and georisk.gov.ph SSL errors, not bypassed. BLGF 403. Earth Engine and Foursquare need accounts | Ecozone data, fiscal data, 2.5D heights, Foursquare | Alternatives recorded in the register | Credentials, or a person opens the sites |
| B-08 | No real candidate location | None in the repository | Site-level results cannot be real | Labelled synthetic test points (RD-006) | Joshua or a franchise company supplies locations |
| B-09 | Zoning and land-use plans | Searches found FOI records and third-party uploads only | C4 and site screening | OSM land use as weak context | LGU or FOI request; held under outreach limits |
| B-10 | Franchise cost and return definition, discount rate, unit benchmarks | Searched filings, trade sources, press. FY2025 filing located but its attachment was not read | ECO-FIN-01 cannot be finalised | Candidate measures recorded, none chosen (RD-011) | Joshua defines cost and return (`08` question 2) |
| B-11 | Store sales, foot traffic, post-opening data | Inspected Kaggle bundle. Searched vendors and public sources | AFTER-01 has no source; JD-06 stand-in has no data | None from public data. Full Techsalerator or Veraset access needs purchase or partnership and a privacy review | Joshua's outreach or purchase decision |

## Unresolved evidence items

| Item | Status |
|---|---|
| Current Bamban–Mabalacat dispute status | Not found |
| R2025A Philippine boundary file | Not found |
| Id 6316 input census and boundaries | Not found; report read only to 100,000 characters |
| Independent R2025A validation for the Philippines | Not found in searches run |
| Corridor building accuracy | Blocked (B-15) |
| Microsoft imagery dates for corridor | Not found |
| Mapillary `pred_label` meaning | Not found |
| Geography of Planet 89.2% accuracy | Not found |
| Road completeness on the ground | Not tested |
| Routability | Not demonstrated; directed strong-component diagnostic done (largest component 96.3% of nodes) |
| Municipal employment | Not found |
| R2025A all-touched masking | Performed 2026-11-02: 2024 COD-AB combined 1.025 of census (pixel-centre 1.008) |
| Id 49861 on OSM polygons | Performed 2026-11-02: 0.792 (pixel-centre) and 0.804 (all-touched) of the projection sum |
| First connectivity run snapshot | Unverified, superseded |
| 2026-11-01 OSM geometry behind logged R2025A OSM sums | Not retained. The retained 2026-11-02 areas match to two decimals, so identity is unverified |

## Added 2026-11-02 (completion pass)

| ID | Blocked | Tried | Impact | Workaround and limits | Needs |
|---|---|---|---|---|---|
| B-12 | No browser tool in this session | Checked for tools; none available. Closeout pass: Bureau of the Treasury (bot-check page, not bypassed), BSP (script shell), PSA release PDF (403), Gevaert 2024 PDF (403), Philippine Seven 17-A attachment (protected link, not followed), agency Transparency Seal pages, NPC opinion compendiums (403) | PSA, BSP, BIR terms and files; official yield and policy-rate pages; agency FOI turnaround; company rent lines; Philippine building-audit figures | Search excerpts and the ADB yield recorded and labelled | A person with a browser ([external actions](acquisition/external-actions.md) 4–8) |
| B-13 | Paid or account-gated standards and data: ITE manual, AACE 18R-97 text, ISO 19157, NCHRP 934 PDF, Earth Engine, Foursquare, EOG night lights. The FHWA 2010 manual was retrieved in the closeout pass and removed from this list | Secondary summaries used and labelled | Benchmarks remain borrowed and unverified against the primary text | Imported values are labelled ([primary-source audit](findings/primary-source-audit.md)) | Purchase or accounts: Joshua's decision |
| B-14 | **Resolved 2026-11-02 (closeout).** Manual reading of 2012 JICA station counts | Pages rendered and read visually; 20 of 20 arithmetic checks pass | Figures available as historical comparators only | — | — |
| B-15 | Corridor building accuracy | No independent reference footprints found in the searches performed; Gevaert 2024 full text not served | No building source can be ranked on accuracy | Choose on licence and fields; do not rank by counts | A reference sample (T-09) or LGU assessor data; Joshua decides ([external actions](acquisition/external-actions.md) 13) |
