# Acquisition specifications and request templates — Central Luzon industrial district POC

**Status:** drafts only. **Nothing has been sent.** Joshua decides whether and when to send any request. No purchase, outreach or contract term has been accepted.

## Official request route

Executive Order No. 2 (2016), §9 ([text](https://lawphil.net/executive/execord/eo2016/eo_2_2016.html)):
- **Request contents:** a written request stating the requester's name and contact information, valid proof of identification or authorisation, and a reasonable description of the information sought, with its purpose.
- **Response time:** the agency must respond within 15 working days of receipt. That period may be extended where an extensive search or voluminous records are involved.
- **Deemed denial:** failure to respond within the period counts as a denial.
- **Channel:** eFOI at https://foi.gov.ph covers participating agencies. Others take requests through their FOI officers.

Documented turnaround beyond the rule: **Not found**. Past eFOI records show AADT and route data being requested from transport agencies.

## Templates

Each template follows the same structure. Placeholders are in brackets.

### T-01 Traffic counts (AADT)

- **To:** public works regional office for Central Luzon, through eFOI.
- **Request:** "Annual average daily traffic and classified counts for national road stations within Capas, Bamban and Mabalacat City, including MacArthur Highway and access roads, for [years], with station coordinates, counting method, vehicle classes and survey dates."
- **Format wanted:** CSV or XLSX, with station location.
- **Purpose:** non-commercial research for the Central Luzon industrial district POC [adjust if use is commercial].
- **Minimum acceptable:** one recent year of station AADT.

### T-02 Zonal values

- **To:** revenue district offices RDO 17A and RDO 21A, or a download from the official zonal-value page by a person.
- **Request:** "Current schedule of zonal values, with department order number and effectivity date, for barangays of [municipality]."
- **Minimum acceptable:** official XLS or PDF with the order number.

### T-03 Boundaries

- **To:** national mapping agency or PSA.
- **Request:** "Official municipal and barangay boundaries for Capas, Bamban and Mabalacat City, with reference date and status of any boundary dispute."
- **Minimum acceptable:** shapefile or GeoPackage with metadata.

### T-04 Zoning

- **To:** municipal or city planning and development offices.
- **Request:** "Approved Comprehensive Land Use Plan and zoning map, with ordinance number, in GIS format if available."

### T-05 Public transport routes

- **To:** regional transport franchising office, or LGU LPTRP office.
- **Request:** "Local Public Transport Route Plan routes for Mabalacat City, Capas and Bamban, with route descriptions or geometry."

### T-06 Employment

- **To:** PSA regional statistical office for Central Luzon.
- **Request:** "Number of establishments and employment by city or municipality and industry, latest year available, for Capas, Bamban and Mabalacat City."

### T-07 Store data (company data sharing, not FOI)

- **To:** franchise company, via Joshua.
- **Request:** store list and periodic sales per the minimum schema in [`../findings/post-opening-data.md`](../findings/post-opening-data.md).
- **Terms to settle first:** confidentiality, permitted uses, retention, pseudonymous store IDs, no customer-level data, a privacy review, and publication limits.

### T-08 Mobility data (vendor or partnership)

- **To:** vendor or data partnership, via Joshua.
- **Specification:** visits per place or area per week, with methodology, panel size, geography, dates and licence.
- **Terms to settle first:** Data Privacy Act basis, aggregation level, commercial-use terms, price.

## Acquisition specification summary

| Need | Minimum | Preferred | Blocks without it |
|---|---|---|---|
| Traffic counts | 1 year AADT at 3+ corridor stations | Hourly classified counts and travel-time runs | BEH-03 validation |
| Zonal values | Official schedule per RDO | Plus market comparables | ECO-FIN-01 land input |
| Store sales | 12 months after opening, several stores | Pre-opening forecasts stored | AFTER-01 |
| Employment | Municipal establishments and jobs | Barangay level | L02 |
| Boundaries | Official municipal polygon | Barangay polygons | Final AOI |
