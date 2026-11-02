# Roads and transport — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. Scripts: `evidence/scripts/legacy/t10.py`, `t16.py`, `t20.py`, `v3.py`, `osm_landuse.py`.

Keep these three questions separate. Each uses a different snapshot, so do not merge them into one quality figure.

## Missing attributes

ohsome snapshot 2026-07-27T09:00Z, COD-AB polygons simplified 0.0002°. Drivable classes exclude service and track. "Major" means motorway through secondary, with links. Length-weighted.

| % of length with tag | Capas: all / major | Bamban: all / major | Mabalacat: all / major |
|---|---|---|---|
| lanes | 18.4 / 85.0 | 23.4 / 100 | 22.0 / 99.5 |
| maxspeed | 15.7 / 78.6 | 13.7 / 89.2 | 15.3 / 89.1 |
| oneway | 9.1 / 40.3 | 12.1 / 75.1 | 11.3 / 74.2 |
| surface | 23.1 / 77.9 | 38.4 / 99.8 | 34.2 / 88.9 |

A missing `oneway` tag normally means two-way, so a low share is not automatically a defect.

Drivable length: Capas 706.2 km, Bamban 322.2 km, Mabalacat 697.0 km.

## Geographic coverage

- Geofabrik `philippines-261031.osm.pbf`, 2026-10-31T21:23:06Z: all three polygons are inside the extract polygon. This shows the extract's bounds only.
- MacArthur Highway (trunk) and the Subic-Clark-Tarlac Expressway (motorway) are mapped, Overpass 2026-11-01T18:02:59Z.
- Completeness on the ground: **Not tested**. No reference road data was obtained.

## Routability

**Not demonstrated** in the routing sense. Two topology diagnostics exist; neither builds SUMO.

**Undirected (shared nodes):** Overpass 2026-11-02T04:50:34Z, bbox 15.16,120.24,15.43,120.64, drivable classes. 13,386 ways, 39 groups, 13,226 ways (98.8%) in the largest. This ignores one-way direction. The first run (13,384 ways) has no recorded snapshot and is Unverified.

**Directed (new):** Overpass 2026-11-02T08:01:36Z, same bbox and classes, with `oneway` tags, roundabouts and motorways treated as one-way.
- Script: [`../evidence/scripts/directed_connectivity.py`](../evidence/scripts/directed_connectivity.py). Results: [`../evidence/results/directed_connectivity_2026-11-02.csv`](../evidence/results/directed_connectivity_2026-11-02.csv).
- 86,348 nodes and 176,628 directed edges.
- Largest strongly connected component: **96.3% of nodes and 96.7% of directed edges**.
- 670 strong components in total, 28 of them with 10 or more nodes.
- Largest weak component: 97.0% of nodes.
- Not modelled: turn restrictions, access restrictions and bounding-box edge effects.
- Tag reading: 1,778 ways tagged `oneway=yes`, 11,505 untagged (treated as two-way).
- **Reading:** a directed graph from this extract would need repair or trimming of about 3–4% of nodes before routing. Any study-area rule should use strong, not weak, connectivity.

## Surface add-ons

| Source | Capas | Bamban | Mabalacat | Status |
|---|---|---|---|---|
| Mapillary predicted length (km) | 0.0 | 3.9 | 62.3 | Logged; share of way length 0%, 0.6%, 4.2% |
| Planet arterial length (km) | 99.0 | 45.2 | 83.6 | Rerun; restricted |

- Mapillary dataset date 2024-11-07, with corridor OSM edits to 2024-07-15 and imagery from 2016-04 to 2022-04.
- Planet covers motorway to secondary classes only in this corridor. Its 89.2% accuracy figure has no stated geography.

## Observed traffic

- DPWH operated 2,849 traffic survey stations nationwide when a JICA report was prepared (PDF metadata dated 2013): 1,350 automated (578 in-ground, 772 on-ground) and 1,499 manual, with 15 vehicle classes. Source: https://openjicareport.jica.go.jp/pdf/12122081_02.pdf, Chapter 6. Only part of that report was read, and whether its "Study Area" includes this corridor was not established. Corridor stations are **Not found**.
- FOI records show AADT released on request: https://foi.gov.ph/requests/annual-average-daily-traffic-aadt-and-traffic-growth-rate. No open corridor table was found.
- SCTEX whole-road average daily traffic: 70,538 (2019), 56,362 (2021), 70,894 (2022) vehicles, from a press report: https://malaya.com.ph/business-news/sctex-posts-record-high-p3-26b-revenue. Context only. These are whole-road figures, and the averaging method is not stated.

## Trip rates, freight, mode shares

- Regidor 2006 reviews Philippine trip rates, many derived from ITE 1997. Two URLs returned 404, so only search excerpts were read. Excerpts mention a 1997 industrial park table with AM and PM per-hectare values; these are **Unverified** and not reproduced as figures.
- Dagupan City mall theses exist, and their numbers were not read.
- Freight trip rate per hectare or employee for the Philippines: **Not found**. Row 6.4 stays a placeholder with no value (D-007).
- Corridor mode shares: **Not found**.
- Household survey: MUCEP is Metro Manila-based, and the relevant volume was not located.

## Transit

- GTFS: 2013-era Metro Manila feeds only.
- OSM route relations crossing each polygon: Capas 1, Bamban 28, Mabalacat 38. Stops: 3, 0, 2. Too sparse for stop-level use.

## Selection

See RD-007. No road network is built or validated.
