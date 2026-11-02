# Land values, costs and financial inputs — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. Scripts: `evidence/scripts/building_permits.py`, `osm_landuse.py`.

## BIR zonal values

**Official files were not obtained.** The current page returns a scripted shell, so a person needs to open it: https://www.bir.gov.ph/zonal-values

### Checklist correction

| Municipality | Checklist | Evidence | Working target |
|---|---|---|---|
| Capas, Bamban | RDO 17 | RAO 002-09 (2 February 2009), digest excerpt: RDO 17A includes Bamban and Capas | RDO 17A |
| Mabalacat | RDO 21B | Search excerpt of RAO 006-19 (21 October 2019) lists Mabalacat under RDO 21A. The fetched digest page shows only part of this text | RDO 21A |
| Clark Freeport parts | Not listed | RAO 006-19 created RDO 21C for the zone | Check if a site falls there |

Sources:
- https://www.digest.ph/taxation/splitting-of-revenue-district-office-rdo-no-17-tarlac-city-tarlac-rdo-no-21-san-fernando-city-pampanga-rdo-no-23-cabanatuan-city-and-rdo-no-113-davao-city-and-redefining-their
- https://www.digest.ph/taxation/creation-of-a-revenue-district-office-at-clark-freeport-zone-in-pampanga-and-delineation-of-its-areas-of-jurisdiction

Both are secondary, and current jurisdiction needs official confirmation. Third-party zonal sites conflict on RDO and value ranges, so no peso figure from them is recorded. Zonal values are tax values, not rents.

## PSA approved building permits (new)

Table `0022G4GBPC1`: https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/2G/CONS/BGP/0022G4GBPC1.px

This gives municipal development activity and a local cost prior. Method: `evidence/scripts/building_permits.py`. The filtered extract stays in git-ignored `local-data/derived/` because PSA terms are unread; only the cited figures below are published.

| Year | Municipality | Permits | Floor area (m²) | ₱/m², all | Non-res permits | Non-res ₱/m² |
|---|---|---|---|---|---|---|
| 2024 | Capas | 200 | 27,012 | 15,128 | 37 | 12,893 |
| 2024 | Bamban | 73 | 20,901 | 10,081 | 48 | 9,184 |
| 2024 | Mabalacat | 754 | 703,714 | 12,441 | 178 | 11,422 |
| 2023 | Capas | 368 | 48,750 | 14,244 | 59 | 15,226 |
| 2023 | Bamban | 91 | 21,997 | 10,242 | 49 | 8,505 |
| 2023 | Mabalacat | 795 | 204,028 | 15,707 | 155 | 15,754 |
| 2022 | Capas | 696 | 205,039 | 6,638 | 157 | 6,664 |
| 2022 | Bamban | 52 | 37,016 | 11,767 | 24 | 11,186 |
| 2022 | Mabalacat | 743 | 179,876 | 11,522 | 67 | 12,185 |

- **Method:** value divided by floor area.
- **Unit:** value is inferred as thousand pesos. The px unit request returned 404, so this inference is unconfirmed.
- **Limits:** these are declared permit values, not audited costs or completions. Small municipal samples swing widely by year.
- **Not a franchise fit-out cost.**

## Unit costs

DPWH Detailed Unit Price Analysis is issued by department order, such as https://dpwh.gov.ph/DPWH/sites/default/files/issuances/do_031_s2024.pdf (not read). Road costs are infrastructure inputs tagged later under D-015, so they are classified as future work.

## Discount rate and horizon

No value is locked (RD-011).

- NEDA's social discount rate was reported as cut from 15% to 10%, July 2017: https://ptvnews.ph/govt-fast-tracks-approval-of-infra-projects-to-boost-growth/. Current official status: **Not found**. This is a public-project rate, borrowed if used.
- A market site showed about 8.10% on the 10-year government bond in late October, with the exact day unconfirmed. This is **Unverified**.
- BSP pages returned 403. Sources found conflict on the 2026 policy path.
- Horizon and budget cap have no sourced value.

## Zoning and parcels

- Official CLUP or zoning files for Capas, Bamban or Mabalacat: **Not found** on official hosts. FOI records and third-party uploads exist: https://foi.gov.ph/requests/bamban-tarlac-and-mabalacat-pampanga-clup
- OSM land use, ohsome snapshot on 2026-11-02, as weak context:

| km² | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Industrial | 2.78 | 1.30 | 1.61 |
| Commercial | 0.03 | 0.09 | 0.24 |
| Retail | 0.03 | 0.05 | 0.12 |
| Residential | 2.52 | 2.26 | 7.05 |

Partial volunteer mapping, not legal land use.
