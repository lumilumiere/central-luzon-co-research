# Closeout of partial research items — Central Luzon industrial district POC

**Date:** 2026-11-02 PHT.

**Why this pass:** the previous report listed six items as partial while also saying independently executable research was complete. This note resolves each item with findings, or with the searches run, the alternatives rejected and the exact unresolved dependency.

**Status terms** (used in the checklist from this pass on):
- **Completed:** a substantive deliverable exists, and its limits are stated.
- **Searched; no suitable evidence found:** the searches listed were run and found nothing usable. This is not a claim that no such source exists.
- **Blocked by a specific external dependency:** a named outside action is needed.
- **Deferred with a documented reason.**
- **Still incomplete:** research that could continue with the tools available here but was not finished.

Values below are in [`../evidence/results/closeout_values_2026-11-02.csv`](../evidence/results/closeout_values_2026-11-02.csv), with local-copy hashes. Downloaded documents stay in git-ignored `local-data/raw/documents/closeout/`, and their hashes are in the manifest.

## 1. SUMO calibration with sparse data — Completed

| Source (read in full unless stated) | Setting and data | What it shows | Relevance here |
|---|---|---|---|
| [SUMO `routeSampler` documentation](https://sumo.dlr.de/docs/Tools/Turns.html), read 2026-11-02 | Tool documentation | Samples routes to match edge counts, turn counts or OD counts. The documentation says the problem is underdetermined, so with few counts the chosen solution "may appear implausible". It recommends `--mismatch-output` to find inconsistent counts, and a multi-step approach rather than `--optimize full` | The standard SUMO route for fitting demand to counts. It needs counts, which the corridor lacks |
| [Kappenberger and Stuckenschmidt 2025](https://doi.org/10.52825/scp.v6i.2590), SUMO Conference Proceedings vol. 6, CC BY 3.0 DE | Mannheim, 11.33 km². 8 hourly induction loops, 13 cameras with 10-minute turn counts, map-matched trajectories | CMA-ES tuning of route probabilities fed to `routeSampler`. In the 3-hour scenario the error fell from ARE 0.83 / NRMSE 0.89 (random routes) to 0.40 / 0.52 (map matching), 0.19 / 0.27 (weighted) and 0.04 / 0.08 (optimised). Optimisation took about 15 h (3-hour scenario) and 148 h (24-hour). Errors are measured against the same loops used for calibration | Shows that "data-scarce" in this literature still means continuous loop and camera counts. A low NRMSE against calibration counts is in-sample fit, not validation. That distinction matters for the reference MVP's NRMSE ≤ 0.30 gate |
| Same paper, review section | Other public SUMO scenarios | InTAS (Ingolstadt) reports NRMSE 0.33; another Ingolstadt scenario reports ARE of 13–18% | Context for what published scenarios achieve with dense sensors |
| [Salawavidana et al. 2026](https://doi.org/10.31705/TRF.2026.1), Transport Research Forum, University of Moratuwa | Two signalised junctions in Sri Lanka. Video, 15-minute aggregates, nine vehicle classes, mixed non-lane-based traffic | SUMO defaults assume lane-disciplined traffic. After calibration: MAPE < 15% and GEH < 5, with exceptions in shared-lane queues. The parameters were transferred to a second junction | The closest setting to Philippine mixed traffic found. Junction scale only, and needs video counts |
| [Yavuz and Özen 2024](https://doi.org/10.20858/sjsutst.2024.122.17), SJSUTST vol. 122 | Turkish urban network with mini-roundabouts; video counts | `routeSampler` fitted to video turn counts. FHWA-style targets used: GEH < 5 on 85% of links, and GEH < 4 for the sum | Shows a small-network workflow from short video surveys |
| Philippine SUMO calibration studies | Searched: "SUMO Philippines jeepney calibration", "traffic microsimulation Philippines" | **Searched; no suitable evidence found.** The JSTOPSIM jeepney-stop microsimulation (PIDS listing) and Palmiano et al. 2004 were found as titles only. Their tools and calibration were not read | — |

**Conclusion:**
- Every method found calibrates against observed counts, from 15-minute video counts to continuous loop data.
- None makes calibration possible with zero current counts.
- The 2012 JICA counts ([`jica-2012-counts.md`](jica-2012-counts.md)) are historical and must not be used as calibration targets.
- The smallest data that would support a calibration attempt is short video counts at a few junctions or access roads (request T-01 or a commissioned survey).

## 2. Trip rates, mode shares and freight rates

| Item | Status | Findings and searches |
|---|---|---|
| Philippine retail or restaurant trip rates | **Searched; no suitable evidence found** | Searched: Philippine and Metro Manila fast-food and convenience-store trip generation, NCTS and EASTS papers, DPWH and MMDA guidance. Found: Palmiano 1999 (EASTS) on the need for traffic impact study in Metro Manila malls, title and summary only; it reports no restaurant or store rates in what was read. Regidor 2006 full text returned 404. The NCTS proposed TIA guide cites ITE as the rate source and allows local rates with approval. ITE values stay borrowed and secondary (B-13) |
| Corridor mode shares | **Searched; no suitable evidence found** | Searched: MUCEP and MMUTIS modal split, JICA Greater Capital Region reports. The MUCEP Policy Formulation manual (JICA 12247664, 2015) was downloaded and has no modal share table. A search summary of MMUTIS gives jeepney 32%, bus 19% and car 16% of Metro Manila work trips. That is secondary, 1996 and Metro Manila only, so it is not used |
| Road freight cost | **Completed (borrowed regional value)** | [Suarez et al., JEASTS vol. 14, Table 6](https://doi.org/10.11175/easts.14.159), a survey of 36 trucking and manufacturing firms on 45 Luzon routes (2 firms in the Clark zone, 1 in Tarlac). 2019 unit cost: 9.67 US cents per ton-km on all routes, 7.15 on Northern Luzon routes, and 20.44 on Southern Luzon routes. Costs rose 1.4% a year from 2015 to 2019. **Limits:** 2019 prices in US cents with no conversion or inflation applied; route averages, not corridor rates. The 2015 column prints a minimum (6.28) above the Northern Luzon average (5.63), which is unexplained |
| Freight trip rates (trips per establishment) | **Searched; no suitable evidence found** | Same searches. `05` row 6.4 stays a placeholder |

## 3. Retail rents and store operating costs

| Item | Status | Findings and searches |
|---|---|---|
| Retail rent, Pampanga, Clark or Tarlac | **Searched; no suitable evidence found** | Searched: Colliers, Leechiu and Santos Knight Frank retail reports for Pampanga, Clark and Angeles, plus property press. Rejected: Colliers' Central Luzon ₱550–750 per m² per month, because the excerpt does not say it covers retail and the earlier reading was office. Also rejected: individual asking rents on listing sites (about ₱600 per m² plus ₱170 common-area dues), because they are single unverified listings |
| Company-level cost ratios | **Completed (company level, primary)** | Philippine Seven [SEC Form 17-A FY2025 summary](https://edge.pse.com.ph/downloadHtml.do?file_id=1894881): gross profit margin 27.11% (2024) and 27.09% (2025); net profit margin 4.30% and 3.79%; gross revenue ₱90.11 billion (2024). These are company figures across company-owned and franchise operations, not franchisee store costs |
| Store-level rent and operating lines | **Blocked by a specific external dependency** | The rent and store-expense notes are in the full 17-A attachment. Its PSE Edge link is a Cloudflare-protected content URL (`/cdn-cgi/content?id=…`). It was not followed, so as not to work around the protection. **Action:** a person downloads the attachment in a browser. Franchisee-level costs still need company data (T-07) |

## 4. Dated financial-rate reference — Completed

- **Main reference:** the Philippine 10-year local-currency government bond yield was **8.076%** at the close of **2026-10-29**. The 5-year yield was 7.946% on the same date.
    - Source: [AsianBondsOnline](https://asianbondsonline.adb.org/philippines/), the Asian Development Bank's bond market site, observed 2026-11-02T09:40:02Z. The page copy is retained locally with its hash.
- **Why the 10-year:** the working horizon is 5 and 10 years (RD-016). The 10-year yield matches the longer horizon and the 5-year the shorter.
- **Limit:** this comes from a multilateral publisher, not a Philippine government page.
    - The Bureau of the Treasury site answered tools with a bot-check page, which was not bypassed.
    - The BSP site returned a script shell with no content.
    - The same AsianBondsOnline page still showed the policy rate as 5.000%, dated 2026-08-27, so its policy rate field was stale.
- **Policy rate:** 5.50% after the Monetary Board decision of **2026-10-22**, per [Daily Tribune](https://tribune.net.ph/2026/10/22/bsp-delivers-jumbo-50-basis-point-rate-hike). This is secondary press, and the BSP release was not read.
- **Illustration, updated, not adopted:** 8.08% + 1.0 × 6.69% ERP (Damodaran, January 2026) ≈ 14.8%.

## 5. Agency request procedures and turnaround

| Item | Status | Findings and searches |
|---|---|---|
| General procedure | **Completed** | EO 2 (2016) §9: 15 working days, extendable, with non-response deemed denial. Read from the text on lawphil, a non-official host. Requests go through the eFOI portal for onboarded agencies. A press quote of a Palace statement gives an extension of up to 20 working days (35 in total). That figure is secondary |
| Documented turnaround format | **Completed** | Agencies publish FOI summary reports with an "average processing time" column. The DICT reports for 2018 and 2022 were downloaded and show the format. Examples: DICT 2018-Q1 eFOI average 1.00 day; NTC 2018-Q1 8.13 days. These are examples only, not target agencies |
| Turnaround for target agencies (PSA, DPWH, BIR, NAMRIA, LTFRB, LGU planning offices) | **Searched; no suitable evidence found** | Searched by agency name with "FOI summary report" and "average processing time". None of their reports surfaced, and PSA regional pages returned 403. A search excerpt of a PSA regional citizen's charter (Region IV-A) gives about 15 hours of processing for data requests. That is secondary and from another region. **Dependency:** a person checks each agency's Transparency Seal page in a browser (B-12) |

## 6. Building quality — Blocked by a specific external dependency

**Evidence found:**
- **Gevaert, Buunk and van den Homberg 2024** (IEEE JSTARS 17:12579–12590, CC BY 4.0) audited Google Open Buildings, Microsoft, Overture and OSM in the Philippines and Tanzania.
    - **What was read:** the repository record and abstract.
    - **Abstract findings:**
        - Accuracy in both countries is lower than expected.
        - Google (confidence above 0.7) and OSM give the best balance of false negatives and false discoveries, with Google more consistent across tiles.
        - Biases differ by dataset and area.
        - Each new application and region should be audited.
    - **Full text not read:** the University of Twente repository PDF and TechRxiv returned 403, and IEEE did not serve the PDF to tools. The Philippine study area and its numbers are therefore **not read**.
- **Sirko et al. 2021:** Africa thresholds, read in full. See [`buildings.md`](buildings.md).
- **Okyere et al. 2025 (arXiv) and Gonzales 2023:** Ghana, Kenya, Venezuela, Germany, the US and Ethiopia. Search summaries only, no Philippine data.

**Independent reference data for the corridor:** searched; no suitable evidence found. No open LGU, assessor or national-mapping building layer for Capas, Bamban or Mabalacat surfaced.

**Why it stays blocked:**
- Accuracy needs reference footprints.
- Agreement between Google, Microsoft and Overture is agreement between model outputs, not accuracy.
- Measuring that agreement is deferred because it would not change source selection.

**Dependency:** one of the following, both needing Joshua's decision (B-15):
- A manually digitised random sample on imagery whose licence permits it, which needs people and imagery rights.
- LGU or assessor building data obtained by request.

## 7. What changed elsewhere

- Checklist statuses, blockers, register rows, the root README and the external-action list ([`../acquisition/external-actions.md`](../acquisition/external-actions.md)) are updated to match.
- Primary versus secondary support for each finding is in [`primary-source-audit.md`](primary-source-audit.md).
