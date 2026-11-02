# Post-opening data assessment — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT.

**Problem:** the after check (AFTER-01) needs observations from stores after they open. The stand-in Joshua chose, `05` row 6.1, has no usable data (see [`franchise-and-foot-traffic.md`](franchise-and-foot-traffic.md)).

**Result:** no suitable public source of actual store sales or visits in the corridor was found in the searches performed. That is not a claim that none exists.

## Candidates checked

| Candidate | Category | Geography and dates | Identifiers and metrics | Permitted use | Verdict |
|---|---|---|---|---|---|
| Techsalerator on Kaggle | Claimed visits | Files are a US real-estate sample | None | Apache label; content belongs to another vendor | Rejected: no data |
| Techsalerator full product | Claimed visits | Not verified | Not verified | Purchase and contact required | Not obtainable within bounds |
| Veraset via the Development Data Partnership | Device pings (proxy) | Philippines, 2023 in a World Bank notebook | Pings, not store visits | Partnership access; privacy review | Not obtainable; proxy only |
| Meta Movement Range | Mobility index (proxy) | Admin areas, 2020-03 to 2022-05 | Index | CC BY | Rejected: ended, not store-level |
| Google Community Mobility | Mobility index (proxy) | Province, 2020–2022 | Percent change | Not read | Rejected: ended, not store-level |
| Company disclosures (7-Eleven, Jollibee) | Actual sales, national | National, annual or quarterly | System-wide sales, store counts, same-store growth | Public filings | National benchmark only; not per store |
| VIIRS night lights (EOG) | Proxy | Global, monthly | Radiance | Free account; licence text not confirmed | Too coarse for one store; not tested |
| OSM and Overture place history | Proxy for opening dates | Corridor | Place presence, sometimes `start_date` | ODbL or CDLA | Can date openings roughly; no sales or visits |
| Commercial foot-traffic vendors (xMap, Datarade listings) | Claimed visits | Not verified | Not verified | Purchase | Not obtainable within bounds |
| Field counts at stores | Actual visits | Would be local | Counts by period | Needs consent and people | Not performed (outreach and fieldwork) |
| Company point-of-sale data | Actual sales | Would be local | Sales by store and period | Agreement needed | Joshua's outreach (`08` answer 10) |

## Three categories kept apart

- **Actual sales or visits:** company point-of-sale data, or field counts. **None available.**
- **Proxy observations:** mobility indices, night lights, place listings. They can indicate activity, but are not sales and must never be labelled as observed sales.
- **Synthetic demonstration data:** may be generated to test software. It must be labelled synthetic, and must never be reported as validation.

## Minimum dataset for AFTER-01

| Field | Type | Required | Notes |
|---|---|---|---|
| `store_id` | string | Yes | Stable, pseudonymous |
| `brand`, `format` | string | Yes | For example kiosk, inline, drive-through |
| `lat`, `lon` or address | number or string | Yes | Needed to link to site features |
| `opening_date` | date | Yes | Defines the before and after split |
| `period_start`, `period_end` | date | Yes | Monthly or weekly |
| `net_sales_php` | number | Yes for the Economic check | Excluding VAT, stated |
| `transactions` | integer | Strongly preferred | Customer count proxy |
| `visits` or footfall count | integer | Optional | State the method (counter, ticket) |
| `operating_days`, closures | integer, text | Yes | Adjusts for downtime |
| `gross_floor_area_m2`, seats, parking | number | Preferred | Model features |
| `predicted_*` | number | Produced by the POC | Stored before opening, never back-filled |

- **Minimum coverage:** at least 12 months after opening for each store; several stores for any error estimate. No published minimum count was found.
- **Privacy:** store-level aggregates only, with no customer records. Any phone-derived data needs a privacy review first (see [`licensing-and-privacy.md`](licensing-and-privacy.md)).

## Impossible without such data

- Actual-against-predicted comparison.
- Forecast error and drift metrics.
- Recalibration.
- Any claim that the before check was validated.

Before-check research and the rest of this assignment continue. The request specification is in [`../acquisition/request-templates.md`](../acquisition/request-templates.md).
