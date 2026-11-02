# Unsuccessful searches and rejected alternatives — Central Luzon industrial district POC

**Date:** 2026-11-02 PHT. Kept so the same work is not repeated.

## Searches that found nothing usable

| Sought | Tried | Result |
|---|---|---|
| Official BIR zonal files | Current and legacy BIR URLs, web search | Scripted page; no file reached |
| Current official RDO jurisdiction | Web search, digest pages (paywalled text) | Partial, secondary only |
| Municipal employment | 3,560 OpenSTAT entries, web search | Not found |
| Provincial LFS 2024–2025 | Web search, catalogue | Not found; PSA site 403 |
| Corridor AADT | Web search, FOI records | Not found as open data |
| DPWH road GIS | Web search; candidate URL 404 | Not found |
| Philippine freight trip rate | Web search | Not found |
| Corridor mode share or household survey | Web search | Not found |
| Philippine retail trip rates, full text | Regidor URLs 404 | Excerpts only |
| Philippine foot-traffic data, open | Kaggle, web search | None with actual data |
| Franchise association benchmarks | Web search | Not found |
| Per-store daily sales | SEVN filing page, investor PDF, press | Not found; attachment unread |
| CLUP or zoning files | Web search | Third-party uploads and FOI records only |
| Parcel or cadastre data | Web search | No public route found |
| Current social discount rate document | Web search | Press only |
| Dated official bond yield | Web search; BTr and BSP limited | Unverified |
| Anonymised location data under the DPA | Web search | Not found |
| Provincial transit GTFS | Web search | Metro Manila 2013-era only |
| Independent R2025A validation | Web search | Not found |

## Tools or routes that failed

| Route | Result |
|---|---|
| OpenSTAT `?query=` keyword search | Returned nothing; tree walk used |
| Retained `0031A6DTPH2.px.json` for values | Collapsed; CSV by item code used |
| Overture release 2026-07-22.0 | Already removed; 2026-10-21.0 used |
| Overpass land-use query | 502 and non-JSON; ohsome used |
| WorldPop `/vsicurl` | Refused; id 6316 range request stalled |
| HeiGIT Mapillary remote bbox read | Too slow; full file downloaded once |
| ren.ph direct page | 404 |
| HDX RWI page, PSA regional release | 403 |
| Archive lookup of terms pages | Refused by session controls; not retried |
| PX unit metadata for permits | 404 |

## Rejected alternatives

| Alternative | Why rejected |
|---|---|
| Third-party zonal sites as source | Conflicting, rights unknown |
| Store-locator scraping | Terms unread; not needed for evaluation |
| Third-party DPWH web-service notes | Terms unclear |
| Kaggle projection copy | Duplicates HDX; label conflict |
| Id 6316 as distribution layer | Barangay test |
| OSM polygons as primary boundary | Overlaps COD-AB neighbours |
| Planet road surface now | Non-commercial until use is settled |
| 10% as a franchise discount rate | Public-sector hurdle, not a private cost of capital |
| Google footprint area as floor area | Not the same measure |
| Filling employment with a guessed density | No sourced value |
