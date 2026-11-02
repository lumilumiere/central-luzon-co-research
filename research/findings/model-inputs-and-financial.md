# Model inputs and financial research — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT.

Value types used below:
- **Observed:** measured locally.
- **Derived:** calculated by this research from cited inputs.
- **Borrowed:** published for another place.
- **Assumption:** not sourced.

No value here is adopted. Joshua owns model selection, and `08` question 2 (the franchise cost and return definition) is still open.

## 1. Trip generation

| Value | Type | Source, year, place | Units | Comparability and limits |
|---|---|---|---|---|
| 467.48 weekday trips; 33.03 PM peak trips | Borrowed | ITE *Trip Generation* 11th ed., land use 934 (fast-food with drive-through), quoted in a [US permit file](https://permits.puyallupwa.gov/Portal/Permit/GetFile/122417); ITE itself not read | Vehicle trip ends per 1,000 ft² GFA | US suburban; Low |
| 470.95 weekday (10th ed., 67 studies, range 98.89–1,137.66) | Borrowed | ITE via [CEQA attachment](https://files.ceqanet.opr.ca.gov/276247-1/attachment/dSTFh-SA4kmIeTLBbmqtvR7W4AYbwGP8oeNDDdVnI-S8D_AZJmrZ5_TVSWyFTI5RberAlyR-RbTByOUA0) | Same | Wide range shows site dependence; Low |
| About 49–52 PM peak trips | Borrowed | ITE 851 (convenience market, 24 h), 9th and 10th eds., via [municipal schedules](https://www.cityofferndale.org/DocumentCenter/View/2993/2026---Downtown-TIF-Schedule) | Per 1,000 ft² GFA | Edition unclear; Low |
| Pass-by 50% AM and 55% PM for land use 934 | Borrowed | ITE *Trip Generation Handbook*, via the same permit file | Share of trips | Reduces new trips; Low |
| Philippine retail or restaurant trip rate | Not found | [Regidor 2006](https://www.journals.upd.edu.ph/index.php/pej/article/view/1800) review: full text returned 404; excerpts say local practice relies on ITE | — | — |
| TIA trigger: 100 or more new peak-hour vehicle trips | Guidance | [NCTS proposed TIA guidelines](https://ncts.upd.edu.ph/wp-content/uploads/2026/04/TIA_Guide_for_the_Philippines.pdf), 2026 file, Philippines | Vehicle trips per peak hour | Proposed; adoption Not found |
| Industrial or employee trip rates | Not found as Philippine values | Industrial park excerpt in Regidor 2006 cites a 1997 study; numbers Unverified | — | — |
| Freight trip rate | Not found | A Klang Valley container-trailer model exists; coefficients not read | — | `05` row 6.4 stays a placeholder |

Converting ITE rates from ft² to m² (×10.764 per 1,000 ft²) is a unit step, not a localisation.

## 2. Mode shares and travel behaviour

- **Corridor mode shares: Not found.**
- MMUTIS (1996) put public transport at about 78% of Metro Manila trips. This comes via a [2011 blog](https://d0ctrine.com/2011/11/18/transport-mode-shares-in-metro-manila/), so it is secondary, dated, and borrowed geography.
- MUCEP (2013–2014) modal split figures were not located in the report library.
- **JICA Clark–Metro Manila railway study:** traffic surveys ran 12–30 October 2012. They include 18- and 24-hour classified counts at the Dau Access Road, Sta. Ines Access Road and a bridge in Angeles, and timed runs between EDSA and Clark Airport averaging about 25 km/h on MacArthur Highway. Source: https://openjicareport.jica.go.jp/pdf/1000012767_02.pdf
    - The station table's columns scramble in text extraction, so station counts are not quoted here.
    - This is observed data, but dated, and would need manual reading.

## 3. Employment and demand proxies

| Value | Type | Source, year, place | Units | Limits |
|---|---|---|---|---|
| Restaurants and cafés 18 (range 10–30); high street retail 19; food superstores 17; general industrial 36; warehousing 70 | Borrowed | [HCA Employment Density Guide, 3rd ed.](https://assets.publishing.service.gov.uk/media/5a7dedd8e5274a2e8ab44baf/employ-den.pdf), November 2015, UK (primary read) | m² per FTE (net or gross internal area, by class) | UK floorspace and staffing; the guide says retail density depends more on turnover than floor area; Low |
| Municipal employment | Not found | 3,560 OpenSTAT entries walked | — | — |
| DTI competitiveness scores | Observed index | [CMCI](https://cmci.dti.gov.ph/) profiles | Index | Not convertible to jobs |
| Approved building permits 2024: Capas 200, Bamban 73, Mabalacat 754 | Observed | [PSA `0022G4GBPC1`](https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/2G/CONS/BGP/0022G4GBPC1.px) | Permits | Intentions, not completions |
| FIES 2023 income; GVA in trade and food service 2019–2023 | Observed, province and HUC | PSA OpenSTAT tables `1E/IE`, `3S/C3` (titles only) | Pesos | Above municipal level |

## 4. Costs, revenues and occupancy

| Value | Type | Source, year, place | Limits |
|---|---|---|---|
| Building permit value per floor area 2024: Capas ₱15,128, Bamban ₱10,081, Mabalacat ₱12,441 per m² | Derived | PSA table above. The thousand-peso unit is supported by PSA's April 2024 release, which reports PhP 38,999,355.17 thousand | Declared building values, **not franchise fit-out or equipment cost** |
| 7-Eleven Philippines 2024 system-wide sales about ₱93.45 billion | Borrowed (company figure via press) | [Investing.com summary of results slides](https://ng.investing.com/news/company-news/philippine-seven-q4--fy-2024-slides-138-annual-growth-despite-q4-headwinds-93CH-1870132) | Secondary; filing not read |
| 7-Eleven stores: 4,130 at end-2024, after 399 openings and 37 closures | Borrowed (press) | [Manila Times, 2025-04-14](https://manilatimes.net/2025/04/14/business/corporate-news/7-eleven-ph-profit-rises-94-to-p38b/2091483) | Secondary |
| About ₱64,800 per store per day | **Derived** | 93.45e9 ÷ 365 ÷ 3,949, where 3,949 is the average of 3,768 opening and 4,130 closing stores | National average across formats; secondary inputs; opening count derived from openings and closures |
| 7-Eleven planned capex: ₱5.5 billion for 500 stores (2025); ₱4–5 billion for 400 stores (2026) | Borrowed (company plans via press) | [Philstar 2024-10-17](https://philstar.com/business/2024/10/17/2393022/7-eleven-sets-p6-billion-capex-eyes-500-stores-2025); [BusinessWorld](https://www.bworldonline.com/?p=745178) | Plans, not unit cost; may include non-store capex. The quotient (about ₱10–12.5 million per new store) is derived and illustrative only |
| Jollibee Group: 3,382 Philippine stores, end-2024; group system-wide sales ₱390.3 billion; Philippine business system-wide sales +10.1% | Borrowed (company release) | [Jollibee Group FY2024 release](https://www.jollibeegroup.com/?p=3365) | Philippine sales in pesos not given, so no per-store figure is derived |
| Franchise package prices | Borrowed (brand pages and blogs) | Various; for example a [government-hosted list](https://balinkbayan.gov.ph/wp-content/uploads/2024/05/List-of-Legitimate-franchise-businesses-in-the-Philippines-CFO-BaLinkBayan.pdf) | Conflicting; not used |
| Retail rent, Pampanga or Clark | Not found | Colliers press gives ₱550–750 per m² per month for **office** in Central Luzon, 2025 ([Manila Bulletin](https://mb.com.ph/2026/03/23/central-luzon-emerges-as-philippines-next-real-estate-hotspotcolliers)) | Office, not retail; not used |
| Operating cost ratios (COGS, labour, royalties) | Not found for the Philippines | — | — |

## 5. Financial definitions (working interpretation, AI-selected)

These are research decisions for evaluation only (RD-016), and do not replace Joshua's definition.

- **Unit of analysis:** one store, from the franchisee's side, compared under scenarios A and B.
- **Initial investment:** franchise fee + construction or fit-out + equipment + pre-opening costs + initial working capital.
- **Annual revenue:** store sales.
- **Operating cost:** cost of goods + labour + occupancy + royalty and marketing fees (as a share of sales) + utilities and other.
- **Four-wall EBITDA:** revenue minus store-level operating costs, before corporate overhead.
- **Measures:**
    - Payback = investment ÷ annual cash flow.
    - Break-even sales = fixed costs ÷ contribution margin ratio.
    - NPV = discounted cash flows minus investment.
    - ROI = cumulative cash flow ÷ investment over the term.
    - Cash-on-cash = annual pre-tax cash flow ÷ initial cash invested.
- **Horizon:** the franchise agreement term. A practitioner excerpt seen in search results gives 5–10 years for Philippine initial terms; the page was not read, so this is **Unverified**. Evaluate at 5 and 10 years as sensitivity.
- **Discount rate:** a private cost of capital, not the 10% social rate.
    - Damodaran's [January 2026 country risk data](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html) gives the Philippines a total equity risk premium of 6.69%, a country risk premium of 2.46%, and Moody's Baa2.
    - A dated official 10-year government yield is Not found; a late-October 2026 market figure of about 8.10% is Unverified.
    - Policy rate 5.00% after the 27 August 2026 decision, per [Manila Bulletin](https://mb.com.ph/2026/08/27/bsp-sees-no-need-for-another-rate-hikefor-now) (secondary). The October 22 decision is Not found.
    - Illustration only: risk-free + 1.0 × total ERP ≈ 8.1% + 6.7% ≈ 14.8%. **Not adopted.**
- **Legal context:** franchise arrangements are generally treated as technology transfer arrangements under the IP Code (secondary practitioner sources). Royalty treatment affects cash flows, and needs legal review before it is modelled.

## 6. What cannot be filled today

Local trip rates, mode shares, freight rates, municipal jobs, store sales, store operating costs, retail rents, and official yields. Each is recorded as Not found or Unverified, with request specifications in [`../acquisition/request-templates.md`](../acquisition/request-templates.md).
