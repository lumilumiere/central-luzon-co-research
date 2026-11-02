# Franchise, foot traffic and post-opening data — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. Scripts: `evidence/scripts/inspect_kaggle.py`, `stores_poi.py`, `overture_corridor.py`, `brand_compare.py`.

## Checklist foot-traffic and mobility rows

### Row 6.1: Techsalerator on Kaggle — unsuitable

- Listing: https://www.kaggle.com/datasets/techsalerator/foot-traffic-and-mobility-data-for-philippines (Apache 2.0 label, version 1, 2026-04-07).
- Anonymous bundle download worked: 694,652 bytes, SHA-256 `f4da2093…`.
- **The bundle has no foot-traffic data and no Philippine rows.** It holds a Mashvisor US rental sample (its README says nationwide U.S. coverage, dated February 2026), rental CSV and JSON files for California addresses, and one PNG.
- Philippine or corridor term matches in CSV and JSON files: 0.
- The listing text describes fields that are not in the bundle, and says full access requires contacting the vendor.

**Consequence:** `08` answer 9 and answer 10 rely on this row for priors and as the post-opening stand-in. Joshua's decision stands as recorded, but this source cannot supply it. See B-11.

### Row 6.2: Smart Mobility on Kaggle — unsuitable

- Listing: https://www.kaggle.com/datasets/ziya07/smart-mobility-traffic-dataset (CC0 label).
- 5,000 rows at 5-minute steps from 2024-03-01, latitude 40.60–40.90 and longitude −74.00 to −73.70, which is the New York area.
- Provenance is **Not found**. Coordinates spread evenly across a rectangle, which suggests generated data, though this is an inference.
- `05` already says not to treat it as Capas ground truth. Nothing in it supports corridor priors.

## Store locations

Counts inside the same COD-AB polygons.

| Places | Capas | Bamban | Mabalacat |
|---|---|---|---|
| OSM shops and listed amenities, 2026-11-02T06:09:49Z | 328 | 116 | 509 |
| Overture places, 2026-10-21.0 | 1,284 | 523 | 3,734 |
| Overture, confidence ≥0.8 | 220 | 120 | 649 |

| Brand, total of three municipalities | OSM | Overture | Overture ≥0.8 |
|---|---|---|---|
| 7-Eleven | 20 | 34 | 25 |
| Jollibee | 8 | 14 | 7 |
| McDonald's | 7 | 11 | 7 |
| Chowking | 4 | 7 | 4 |
| KFC | 4 | 4 | 4 |
| Mang Inasal | 3 | 4 | 2 |
| Greenwich | 0 | 4 | 2 |
| Puregold | 4 | 8 | 7 |
| Mercury Drug | 6 | 5 | 3 |
| Alfamart | 13 | 0 | 0 |

- Matching is a case-insensitive pattern on name and brand. Duplicates were not removed.
- There is no ground truth, so neither count is confirmed.
- Overture's Alfamart gap shows it cannot stand alone. Its brand field also has noise, including a Surigao-named record in a Central Luzon box.
- Foursquare OS Places needs an account token, which is unavailable.

## Store sales and visits

- Store-level sales: not public; **Not found**. Joshua plans to ask companies (`08` answer 10).
- Listed-company route: Philippine Seven's FY2025 17-A is at https://edge.pse.com.ph/downloadHtml.do?file_id=1894881, but operating metrics sit in an unread attachment. Per-store daily sales: **Not found**.
- Press reports 4,130 stores at end-2024: https://manilatimes.net/2025/04/14/business/corporate-news/7-eleven-ph-profit-rises-94-to-p38b/2091483. Unverified against the filing.
- Commercial mobility: Veraset covers the Philippines per a World Bank notebook, https://worldbank.github.io/eca-resilience/notebooks/Manila_EDA_QA.html. Access is restricted. Corridor density is unknown.
- Meta Movement Range and Google mobility reports ended and are not store-level.

## Post-opening data

**Not found** from public sources. AFTER-01 has no source until a company shares data or a mobility source is purchased and privacy-reviewed.

## Franchise cost and return

Definition is still open (`08` question 2). Candidate measures from secondary, mostly US sources:

- Payback: total investment divided by annual net profit.
- Four-wall EBITDA: unit-level profit before corporate overhead.
- Cash-on-cash return: annual pre-tax cash flow divided by initial investment.
- Source example: https://www.heritagelawwi.com/franchise-unit-economics-evaluate-franchisee-viability

Their published thresholds conflict and are not repeated here as benchmarks.

## Investment ranges

Only brand pages and blogs were found, with no association benchmark. Figures conflict, such as three different 7-Eleven amounts across sources. Values are not adopted. A government-hosted listing exists: https://balinkbayan.gov.ph/wp-content/uploads/2024/05/List-of-Legitimate-franchise-businesses-in-the-Philippines-CFO-BaLinkBayan.pdf (not read in full).
