# Background research — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. Product claims below are vendor statements unless stated, and are not independently established. No partner was contacted.

## Prior art and comparable tools

| Tool | Category | What it reportedly does | Evidence type |
|---|---|---|---|
| SiteZeus | Franchise site selection | Revenue forecasting and franchise development workflow | Competitor-written comparison ([GrowthFactor](https://www.growthfactor.ai/resources/blog/sitezeus-alternatives)) |
| Placer.ai | Foot-traffic analytics | Visit estimates from device data; no site scoring | Same publisher |
| Esri ArcGIS Business Analyst | GIS site analysis | Drive-time trade areas and demographics | Same publisher; Esri product pages not read |
| Buxton | Consultative analytics | Engagement-based site recommendations | Same publisher |
| Kalibrate | Fuel and convenience network planning | C-store forecasting | Same publisher |
| UrbanSim | Land use and transport scenarios | Land-use and accessibility feedback | [Vendor page](https://www.urbansim.com/scenario-modeling) |
| UrbanFootprint | Scenario sketch planning | Sketch transport and emissions indicators | [Curriculum docs](https://urbanfootprintcurriculum.readthedocs.io/en/latest/ufintro.html) |
| Reference MVP (`delatorrecj/matrix`, MIT licence) | Scenario simulator, Iloilo pilot | SUMO kernel, five dimensions, confidence bands, explicit validation gates | Repository read; its own validation gates are internal |

**Independent validation of these tools: Not found.** The positioning of this POC is traceable, single-site franchise checks with qualitative confidence. That differs from foot-traffic products, which need device data the POC lacks.

## Precedents from the reference MVP

From its repository, read 2026-11-02:
- Manual download and parsing of BIR zonal XLS files.
- Scraping public descriptions of local public transport route plans (LPTRP).
- Barangay socioeconomic data from Project CCHAIN on HDX.
- Flood from LiPAD WFS.
- A literature-derived corridor back-test with an internal NRMSE ≤ 0.30 gate, withheld until demand was calibrated.

These are methods to copy where they fit, not data for this corridor:
- CCHAIN covers 12 cities; whether any is in this corridor is Not found.
- A Mabalacat LPTRP was Not found; FOI records show route requests to the regional transport office.

## Reviewer and partner categories (no contact made)

- Transport engineers and planners: university transport centres and transport-science societies.
- Cost engineers: AACE-practising estimators or civil engineering societies.
- Franchise practitioners: franchise associations and franchise development consultants.
- Industrial or retail economists: academic or bank research units.
- Geospatial data specialists: national mapping or statistics regional offices.
- Privacy counsel: Data Privacy Act practitioners.
- LGU planning offices: municipal or city planning and development offices.

## Environmental and ecological data for future work

Recorded, not scored: terrain, land cover, flood, landslide, protected areas, biodiversity occurrences, surface water, forest change, air quality and climate (register rows ENV-01 to ENV-12). Additional official flood source: LiPAD/DREAM river-basin flood maps for the Pampanga basin, which includes Tarlac per [DREAM's basin report](https://dream.upd.edu.ph/assets/Publications/UP-DREAM-River-Reports/FMC/DREAM-Flood-Forecasting-and-Flood-Hazard-Mapping-for-Pampanga-River-Basin.pdf). Coverage of these municipalities: Not tested.

## Remaining research questions exposed by the inventory

1. Can store-level sales or visits be obtained under a data-sharing agreement, and in what schema?
2. Are corridor AADT stations held in DPWH's traffic application, and for which years?
3. What do the 2012 JICA station counts show, read manually from the PDF?
4. Is the NCTS TIA guideline adopted by any LGU in the corridor?
5. Which RDO currently governs each municipality, and what are the official zonal schedules?
6. How complete are building footprints against a manual reference sample?
7. Which franchise cost and return definition will the validators accept?
