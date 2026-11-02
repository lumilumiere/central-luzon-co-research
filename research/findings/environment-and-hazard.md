# Environment, terrain and hazard — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. These layers are not scored (`03` §7). They are sampled only because they cost little and could flag a site. No ecological or habitat figure is claimed.

## Terrain

Copernicus DEM GLO-30, tile N15 E120, read by HTTP range: https://registry.opendata.aws/copernicus-dem/. Script: `evidence/scripts/corridor_layers.py`.

| Elevation (m), surface model | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Median | 188.1 | 315.7 | 99.4 |
| 95th percentile | 505.8 | 799.4 | 423.5 |

This is a surface model and includes canopy. The licence text is unread.

## Land cover

ESA WorldCover 2021 v200, CC BY 4.0, stated global accuracy 76.7%: https://esa-worldcover.org/en/data-access

| % of cells | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Tree | 55.8 | 72.7 | 38.3 |
| Grass | 20.4 | 12.8 | 23.5 |
| Crop | 17.8 | 9.7 | 17.9 |
| Built | 3.0 | 3.0 | 18.4 |

## Flood

NOAH 100-year flood maps, third-party Hugging Face mirror of official products: https://huggingface.co/datasets/bettergovph/project-noah-hazard-maps. Files: `Flood/100yr/Tarlac.zip` (SHA-256 `7ae951b4…`) and `Pampanga.zip` (`0d6eddf4…`). Script: `evidence/scripts/noah_flood_corridor.py`, rasterised on a 20 m EPSG:32651 grid, higher class wins.

| % of COD-AB area | Capas | Bamban | Mabalacat |
|---|---|---|---|
| Low | 8.6 | 6.3 | 15.6 |
| Medium | 10.0 | 8.0 | 10.5 |
| High | 8.8 | 7.4 | 8.2 |
| Any hazard | 27.4 | 21.6 | 34.2 |

- Hazard classes follow metadata Var 1, 2, 3, considering depth and velocity. LiDAR data covers 18 major river basins only.
- The mirror carries a NOAH licence file (ODC-ODbL). The official host was reachable, but a scripted file route was not confirmed.
- Other return periods and landslide files were listed, not measured.

## Seismic

HazardHunterPH is a point-report tool with an all-rights-reserved footer and no bulk route on its page: https://hazardhunter.georisk.gov.ph. `www.georisk.gov.ph` gave an SSL error and was not bypassed.

## Ecology

Protected Planet terms bar redistribution and sub-licensing, and direct commercial users to IBAT: https://www.protectedplanet.net/en/legal. The automated page summary of the commercial clause was unclear, so a person should read it. Data was not downloaded. GBIF responds, but occurrence records are not habitat evidence. Key Biodiversity Areas was not reached.

## Not searched

Water, energy, CO₂, air, noise, heat and waste sources were not searched in depth (RD-012).
