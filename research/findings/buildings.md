# Buildings — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. **Boundary:** COD-AB v03. Scripts: `evidence/scripts/legacy/t13.py`, `t14.py`, `overture_corridor.py`, `osm_landuse.py`.

No source here supports floor area, building use, employment or industrial intensity. Footprint area is not floor area.

## Observed counts

| Footprints | Capas | Bamban | Mabalacat | Source date |
|---|---|---|---|---|
| Google v3, ≥0.65 | 76,827 | 37,523 | 95,257 | Inference May 2023 |
| Google v3, ≥0.763 | 44,357 | 22,079 | 56,638 | Tile 80% precision threshold |
| Google v3, ≥0.817 | 25,862 | 13,050 | 32,838 | Tile 85% |
| Google v3, ≥0.874 | 8,874 | 4,635 | 10,964 | Tile 90% |
| Microsoft | 35,920 | 17,737 | 29,753 | Upload 2026-08-13; row counts match 2023-04-25 items |
| Overture | 77,861 | 40,767 | 94,683 | 2026-10-21.0 |
| OSM polygons | 64,574 | 33,701 | 76,821 | ohsome latest on 2026-11-02 |

Thresholds are for all of S2 tile 339, not these municipalities.

**Precise statement:**
- At ≥0.65, Google lists 2.1–3.2 times Microsoft's count.
- At ≥0.874, Google lists fewer than Microsoft in all three.
- Google footprint medians are 49.0–54.0 m² against Microsoft's 73.6–99.8 m².
- Differences could reflect detection, false positives, splitting or imagery date. **No source is ranked on accuracy**, because corridor accuracy is Not found.

Overture source mix, by first source:

| | OSM | Google | Microsoft |
|---|---|---|---|
| Capas | 64,524 | 11,543 | 1,794 |
| Bamban | 33,668 | 6,350 | 749 |
| Mabalacat | 76,784 | 15,693 | 2,206 |

## Attributes

- Google: confidence and area. No height, use or per-building image date.
- Microsoft: `height` and `confidence` are `-1` for every corridor record.
- Overture: height on 6 of 213,311 records, floors on 256.
- OSM: use tags on 5,730 of 175,096 buildings (3.3%), levels on 257, height on 7.

Building use and floor area: **Not found** as an open source. PSA permits give municipal floor area for new permits only (see `land-values-and-costs.md`).

## Quality evidence

Gevaert et al. 2024 audits global building datasets in Tanzania and the Philippines: https://research.utwente.nl/en/publications/auditing-geospatial-datasets-for-biases-using-global-building-dat/. Only the abstract was read, so its numbers are Not read. It is not corridor validation.

## Barangay use

Building-count shares are tested in `population.md`.

## Selection

See RD-005.
