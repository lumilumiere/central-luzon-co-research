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

Gevaert, Buunk and van den Homberg 2024 (IEEE JSTARS 17:12579–12590, CC BY 4.0) audit Google, Microsoft, Overture and OSM in Tanzania and the Philippines: https://research.utwente.nl/en/publications/auditing-geospatial-datasets-for-biases-using-global-building-dat-2/.
- **Abstract findings:**
    - Accuracy in both countries is lower than expected.
    - Google (confidence above 0.7) and OSM give the best balance of false negatives and false discoveries, with Google more consistent across tiles.
    - Biases differ by dataset and area.
    - Each new region and application should be audited.
- **Not read:** the full text returned 403 or was not served to tools in the closeout pass, so the Philippine study area and its numbers are not read.
- **Not corridor validation.**

Sirko et al. 2021 (https://arxiv.org/pdf/2107.12283, primary read) describes the Open Buildings method:
- Confidence thresholds are set per S2 cell to target 80%, 85% and 90% precision at 0.5 IoU.
- Confidence filtering raises precision with an unknown effect on recall.
- Some low scores come from large buildings split into several detections.
- Its headline evaluation is for Africa.

A secondary study reports that Microsoft and Google both claim roughly 70% recall: https://drops.dagstuhl.de/storage/00lipics/lipics-vol277-giscience2023/LIPIcs.GIScience.2023.35/LIPIcs.GIScience.2023.35.pdf

**Counts are not accuracy.** Google's higher count could reflect more detections, false positives or splitting, so no source is ranked.

**Status: blocked by a specific external dependency (B-15).**
- No independent corridor reference footprints were found in the searches performed.
- Agreement between the datasets is agreement between model outputs, so it was not computed as a stand-in for accuracy.
- Measuring accuracy needs the reference sample specified in [T-09](../acquisition/request-templates.md#t-09-building-reference-sample-acquisition-specification-not-a-request), or LGU assessor data. See [closeout §6](closeout-partial-items.md#6-building-quality--blocked-by-a-specific-external-dependency).

## Barangay use

Building-count shares are tested in `population.md`.

## Selection

See RD-005.
