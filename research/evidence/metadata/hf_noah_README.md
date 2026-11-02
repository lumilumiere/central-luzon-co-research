---
license: odbl
task_categories:
  - other
language:
  - en
tags:
  - geospatial
  - disaster-risk-reduction
  - hazard-mapping
  - philippines
  - flood
  - landslide
  - storm-surge
  - gis
  - climate
size_categories:
  - 10GB<n<100GB
---

# Project NOAH Hazard Maps

### Dataset Summary

The Project NOAH (Nationwide Operational Assessment of Hazards) Hazard Maps is a comprehensive collection of geospatial datasets covering natural hazard assessments across the Philippines. The dataset includes three major hazard types:

1. **Flood Hazard Maps** - Flood inundation maps for 5-year, 25-year, and 100-year rainfall return periods
2. **Landslide Hazard Maps** - Shallow landslide susceptibility, structurally-controlled landslide hazards, and debris flow/alluvial fan delineations
3. **Storm Surge Hazard Maps** - Storm surge advisory maps for four severity levels based on simulations of 721 historical tropical cyclones (1951-2013)

The dataset covers all 81 provinces of the Philippines with province-level granularity, totaling approximately 23GB of geospatial data in ESRI Shapefile format.

### Languages

The dataset documentation and metadata are in English. Geographic feature names are in Filipino and English.

## Dataset Structure

### Data Instances

The dataset is organized into three main directories:

```
project-noah-downloads/
├── Flood/
│   ├── 5yr/           # 5-year return period flood maps
│   ├── 25yr/          # 25-year return period flood maps
│   ├── 100yr/         # 100-year return period flood maps
│   └── metadata_flood.txt
├── Landslide/
│   ├── LandslideHazards/      # Merged landslide hazard maps
│   ├── DebrisFlowAlluvialFan/ # Debris flow and alluvial fan maps
│   └── metadata_landslide.txt
├── Storm Surge/
│   ├── StormSurgeAdvisory1/   # SSA 1 (2.01m to 3m)
│   ├── StormSurgeAdvisory2/   # SSA 2 (3.01m to 4m)
│   ├── StormSurgeAdvisory3/   # SSA 3 (4.01m to 5m)
│   ├── StormSurgeAdvisory4/   # SSA 4 (>5m)
│   └── metadata_stormsurge.txt
├── PMTiles/
│   ├── noah_hazard_maps.pmtiles   # Combined all-hazard map (4.8 GB)
│   └── layers/
│       ├── flood_5yr.pmtiles      # 5-year flood return period (486 MB)
│       ├── flood_25yr.pmtiles     # 25-year flood return period (563 MB)
│       ├── flood_100yr.pmtiles    # 100-year flood return period (969 MB)
│       ├── landslide.pmtiles      # Landslide susceptibility (2.7 GB)
│       ├── debris_flow.pmtiles    # Debris flow and alluvial fan (20 MB)
│       ├── storm_surge_ssa1.pmtiles  # Storm surge SSA 1 (59 MB)
│       ├── storm_surge_ssa2.pmtiles  # Storm surge SSA 2 (65 MB)
│       ├── storm_surge_ssa3.pmtiles  # Storm surge SSA 3 (66 MB)
│       └── storm_surge_ssa4.pmtiles  # Storm surge SSA 4 (64 MB)
└── NOAH_License.pdf
```

Each province is provided as a separate ZIP archive containing ESRI Shapefiles (.shp, .shx, .dbf, .prj, etc.).

Example shapefile attributes for flood hazard:
```json
{
  "Var": 3,
  "geometry": "POLYGON ((121.0 14.5, 121.1 14.5, ...))"
}
```

### Data Fields

#### Flood Hazard Maps
- `Var`: Hazard classification indicator (Integer)
  - `1`: Low hazard (0-0.5 meters flood depth)
  - `2`: Medium hazard (>0.5-1.5 meters flood depth)
  - `3`: High hazard (>1.5 meters flood depth)

Hazard levels consider both flood depth and velocity. Areas with shallow but fast-flowing water may have higher hazard levels than depth alone would indicate.

#### Landslide Hazard Maps
- `HAZ`: Hazard classification indicator (Integer)
  - `1`: Low hazard - Build only with continuous monitoring
  - `2`: Medium hazard - Build only with slope protection and intervention; continuous monitoring
  - `3`: High hazard - No dwelling zone

#### Storm Surge Hazard Maps
- `HAZ`: Hazard classification indicator (Integer)
  - `1`: Low hazard (0.2m < max depth < 0.5m, and 0 < max depth × velocity < 0.5 sq.m/s)
  - `2`: Medium hazard (0.5m < max depth < 1.5m, or 0.5 < max depth × velocity < 1.5 sq.m/s)
  - `3`: High hazard (max depth > 1.5m, or max depth × velocity > 1.5 sq.m/s)

Storm Surge Advisory (SSA) levels correspond to peak storm tide heights:
- SSA 1: 2.01m to 3m
- SSA 2: 3.01m to 4m
- SSA 3: 4.01m to 5m
- SSA 4: More than 5m

### Known Data Gaps

`Flood/100yr/TawiTawi.zip` is present in the dataset but is an empty ZIP archive (22 bytes, no files inside). No flood hazard data is available for Tawi-Tawi province at the 100-year return period.

### Data Splits

The dataset is organized by hazard type and scenario rather than traditional train/validation/test splits:

| Hazard Type | Scenarios | Provinces | Description |
|-------------|-----------|-----------|-------------|
| Flood | 3 (5yr, 25yr, 100yr) | 80 | Return period-based flood maps |
| Landslide | 2 (Hazards, Debris Flow) | 82 | Susceptibility and runout maps |
| Storm Surge | 4 (SSA 1-4) | 67 | Advisory level-based inundation maps |

## PMTiles

The dataset includes pre-built [PMTiles](https://protomaps.com/blog/pmtiles) files — a single-file, cloud-optimized vector tile format — derived from all shapefiles. They are stored in `PMTiles/` via Git LFS.

`noah_hazard_maps.pmtiles` (4.8 GB) is a combined file with 9 named vector tile layers:

| Layer | Hazard | Attribute | Values |
|---|---|---|---|
| `flood_5yr` | Flood 5-year return period | `Var` | 1 / 2 / 3 |
| `flood_25yr` | Flood 25-year return period | `Var` | 1 / 2 / 3 |
| `flood_100yr` | Flood 100-year return period | `Var` | 1 / 2 / 3 |
| `landslide` | Landslide hazard zones | `HAZ` | 1 / 2 / 3 |
| `debris_flow` | Debris flow and alluvial fan | `HAZ` | 1 / 2 / 3 |
| `storm_surge_ssa1` | Storm surge advisory 1 (2.01m to 3m) | `HAZ` | 1 / 2 / 3 |
| `storm_surge_ssa2` | Storm surge advisory 2 (3.01m to 4m) | `HAZ` | 1 / 2 / 3 |
| `storm_surge_ssa3` | Storm surge advisory 3 (4.01m to 5m) | `HAZ` | 1 / 2 / 3 |
| `storm_surge_ssa4` | Storm surge advisory 4 (5m and above) | `HAZ` | 1 / 2 / 3 |

Values correspond to hazard levels: 1 = Low, 2 = Medium, 3 = High.

Individual per-layer files are also available under `PMTiles/layers/` as checkpoints from the conversion process.

### Viewing

Browse the combined PMTiles file in the [PMTiles viewer](https://pmtiles.io/#map=5.44/11.447/123.548&url=https%3A%2F%2Fhuggingface.co%2Fdatasets%2Fbettergovph%2Fproject-noah-hazard-maps%2Fresolve%2Fmain%2FPMTiles%2Fnoah_hazard_maps.pmtiles).

### Usage with MapLibre GL JS

Load the file directly from HuggingFace using the [pmtiles](https://www.npmjs.com/package/pmtiles) protocol plugin for [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/).

```html
<script src="https://unpkg.com/maplibre-gl/dist/maplibre-gl.js"></script>
<script src="https://unpkg.com/pmtiles/dist/pmtiles.js"></script>
```

```js
const protocol = new pmtiles.Protocol();
maplibregl.addProtocol("pmtiles", protocol.tile);

const map = new maplibregl.Map({ container: "map", /* ... */ });

const PMTILES_URL =
  "pmtiles://https://huggingface.co/datasets/bettergovph/project-noah-hazard-maps/resolve/main/PMTiles/noah_hazard_maps.pmtiles";

map.on("load", () => {
  map.addSource("noah", { type: "vector", url: PMTILES_URL });

  // Flood attribute: Var (1=Low, 2=Medium, 3=High)
  // source-layer options: flood_5yr, flood_25yr, flood_100yr
  map.addLayer({
    id: "flood-100yr",
    type: "fill",
    source: "noah",
    "source-layer": "flood_100yr",
    paint: {
      "fill-color": ["match", ["get", "Var"], 1, "#93c5fd", 2, "#3b82f6", 3, "#1d4ed8", "transparent"],
      "fill-opacity": 0.65
    }
  });

  // Landslide / debris flow attribute: HAZ (1=Low, 2=Medium, 3=High)
  // source-layer options: landslide, debris_flow
  map.addLayer({
    id: "landslide",
    type: "fill",
    source: "noah",
    "source-layer": "landslide",
    paint: {
      "fill-color": ["match", ["get", "HAZ"], 1, "#fde68a", 2, "#f59e0b", 3, "#b45309", "transparent"],
      "fill-opacity": 0.65
    }
  });

  // Storm surge attribute: HAZ (1=Low, 2=Medium, 3=High)
  // source-layer options: storm_surge_ssa1, storm_surge_ssa2, storm_surge_ssa3, storm_surge_ssa4
  map.addLayer({
    id: "storm-surge-ssa1",
    type: "fill",
    source: "noah",
    "source-layer": "storm_surge_ssa1",
    paint: {
      "fill-color": ["match", ["get", "HAZ"], 1, "#99f6e4", 2, "#2dd4bf", 3, "#0f766e", "transparent"],
      "fill-opacity": 0.65
    }
  });
});
```

### PMTiles conversion process

The shapefiles were converted to PMTiles using a Docker-based pipeline. The full conversion script is available at [j4ckofalltrades/project-noah-hazard-maps-pmtiles](https://github.com/j4ckofalltrades/project-noah-hazard-maps-pmtiles).

**Prerequisites:** Docker, ~6 GB free disk space beyond the source data.

```bash
# Build the image
docker build -t noah-pmtiles .

# Run the conversion (takes several hours)
docker run --rm -v $(pwd):/data noah-pmtiles shp_to_pmtiles.sh
```

**Stage 1 — Parallel tippecanoe runs:** Each of the 9 layers gets its own `tippecanoe` process running in parallel. Shapefiles are streamed from ZIP archives through named FIFOs directly into `tippecanoe`; no intermediate GeoJSON files are written to disk. Only one unzipped shapefile lives on disk at a time per layer. Each completed layer is saved as `layers/<layer>.pmtiles` and acts as a checkpoint — re-running skips layers whose files already exist.

Landslide shapefiles use inconsistent field names across provinces (`GRIDCODE`, `GRID`, `ALLUVIAL`, etc.). The script uses `ogrinfo` to detect the first numeric field per file and aliases it to a normalised output name via `ogr2ogr` SQL.

**Stage 2 — tile-join merge:** `tile-join -pk` merges all 9 per-layer PMTiles into `noah_hazard_maps.pmtiles`. The `-pk` flag bypasses `tile-join`'s default 500 KB tile size limit.

**Stage 3 — Verify:** `pmtiles show` runs automatically after the merge and prints the tile type, bounds, zoom range, and layer names.

To resume an interrupted run, delete the checkpoint for any layer you want to regenerate and re-run:

```bash
rm layers/landslide.pmtiles
docker run --rm -v $(pwd):/data noah-pmtiles shp_to_pmtiles.sh
```

To verify an existing output file manually:

```bash
docker run --rm -v $(pwd):/data noah-pmtiles -c "pmtiles show /data/noah_hazard_maps.pmtiles"
```

Expected output includes tile type `Vector Protobuf (MVT)`, bounds covering the Philippines (~116–127°E, 4–21°N), zoom range 0–14, and all 9 layer names.

## Dataset Creation

### Source Data

This data was sourced from the downloadable products of [Project NOAH](https://drive.google.com/drive/folders/1ALE4-E9c-4AGjm1fqiPprWHrLUskeY9o?usp=drive_link).

### Methodology

#### Flood Hazard Maps

Implemented by **PAGASA**. The modelling process covers three steps: data preparation, catchment delineation, and simulation. Rainfall data from synoptic stations across the Philippines was used to compute total accumulated rainfall and rainfall intensities for each return period. Accumulated values were interpolated and weighted to produce a 24-hour accumulated rainfall per municipality.

Flooding was simulated using **Flo-2D GDS Pro**, a FEMA-approved flood routing software that models water flow over complex topography using a grid-element system. LiDAR data specifically covers the 18 major river basins; other areas use additional topographic sources.

#### Landslide Hazard Maps

Implemented by research scientists from the **National Institute of Geological Sciences (NIGS), University of the Philippines** under the sub-program "Enhancing Philippine Landslide Hazard Maps with LiDAR and High-Resolution Imagery". Landslide hazards are merged outputs from three models:

- **Matterocking and Conefall** — runout zones of structurally controlled landslides; Conefall extents are classified as high-hazard
- **SINMAP (Stability Index Mapping)** — shallow landslide susceptibility; areas with SI between 0 and 1.0 are classified as high-hazard
- **Flow-R** — debris flow extents, classified as high-hazard

Low-to-medium hazard areas are clipped when merging with debris flow extents to prevent overlap. Source elevation data is 1-meter resolution LiDAR and 5-meter resolution IfSAR-derived DEMs.

#### Storm Surge Hazard Maps

Implemented by **PAGASA** in cooperation with NIGS under the sub-program "System to Identify, Quantify and Map the Storm Surge Threat to Philippine Coasts". The project simulated **721 tropical cyclones** that entered the Philippine Area of Responsibility from **1951–2013** using the **Japan Meteorological Agency (JMA) storm surge model**. Maximum tide levels from WXTide were added to the simulation results.

Storm tide levels were categorized into four SSA groups (SSA 1: 2.01–3m; SSA 2: 3.01–4m; SSA 3: 4.01–5m; SSA 4: 5m and above). Each SSA time series was used for inundation modelling with **FLO-2D**. Basemap is a **1:20,000 scale Digital Terrain Model from NAMRIA**, covering all 67 coastal provinces.

### Citations

When using this dataset, cite the relevant peer-reviewed publications alongside Project NOAH as the primary source.

#### Landslide Hazard Maps

- Rabonza, M.L., Felix, R.P., Lagmay, A.M.F., Eco, R.N., Ortiz, I.J., and Aquino, D.K. (2015). Shallow landslide susceptibility mapping using high-resolution topography for areas devastated by super typhoon Haiyan. *Landslides*, 13(1), pp. 201–210.
- Alejandrino, A.M.F. Lagmay, and R.N. Eco (2015). Shallow Landslide Hazard Mapping for Davao Oriental, Philippines Using a Deterministic GIS Model. In: *Communicating Climate Change and Natural Hazard Risk and Cultivating Resilience: Case Studies for a Multidisciplinary Approach* (Ed. Y.Y. Kontar). Springer, Berlin.
- Luzon, P.K., Montalbo, K., Galang, J., Sabado, J.M., Escape, C.M., Felix, R., and Lagmay, A.M.F. (2016). Hazard mapping related to structurally controlled landslides in Southern Leyte, Philippines. *Natural Hazards and Earth System Sciences*, 16, 875–883.
- Rodolfo, K., Eco, N., Lagmay, A.M.F. et al. The December 2012 Mayo River debris flow triggered by Super Typhoon Bopha in Mindanao, Philippines: Lessons learned and questions raised. *NHESS* (in press).
- Norini, G., Zuluaga, M.C., Ortiz, I., Aquino, D.T., and Lagmay, A.M.F. (2016). Delineation of alluvial fans from Digital Elevation Models with a GIS algorithm for the geomorphological mapping of the Earth and Mars. *Geomorphology*, 273, pp. 134–149.

For the Landslide Hazard Map Atlas (87 volumes covering 81 provinces of the Philippines), cite as:
> [Authors] (2015). *Landslide Hazard Map Atlas: [Province]* (A.M.F.A. Lagmay, Ed.). Quezon City: University of the Philippines Press.

#### Storm Surge Hazard Maps

- Lapidez, J.P., Tablazon, J., Dasallas, L., Gonzalo, L.A., Cabacaba, K.M., Ramos, M.M.A., Suarez, J.K., Santiago, J., Lagmay, A.M.F., and Malano, V. (2015). Identification of storm surge vulnerable areas in the Philippines through the simulation of Typhoon Haiyan-induced storm surge levels over historical storm tracks. *Natural Hazards and Earth System Sciences*, 15, 1473–1481. doi:10.5194/nhess-15-1473-2015
- Lagmay, A.M.F. and Kerle, N. (2015). Typhoons: Storm-surge models helped for Hagupit. *Nature*, 519, 414. doi:10.1038/519414b
- Tablazon, J., Caro, C.V., Lagmay, A.M.F., Briones, J.B.L., Dasallas, L., Lapidez, J.P., Santiago, J., Suarez, J.K., Ladiero, C., Gonzalo, L.A., Mungcal, M.T.F., and Malano, V. (2015). Probabilistic storm surge inundation maps for Metro Manila based on Philippine public storm warning signals. *Natural Hazards and Earth System Sciences*, 15, 557–570. doi:10.5194/nhess-15-557-2015
- Lagmay, A.M.F., Agaton, R.P., Bahala, M.C., Briones, J.T., Cabacaba, K.M.C., Caro, C.V.C., Dasallas, L.L., Gonzalo, L.I.L., Ladiero, C.N., Lapidez, J.P., Mungcal, M.T.F., Puno, J.V.R., Ramos, M.C., Santiago, J., Suarez, J.K., and Tablazon, J.P. (2015). Devastating storm surges of Typhoon Haiyan. *International Journal of Disaster Risk Reduction*, 11, pp. 1–12.

### Annotations

### Personal and Sensitive Information

This dataset does not contain personal or sensitive information. It consists entirely of geospatial hazard zone delineations at the provincial and municipal level.

## Additional Information

### Licensing Information

The downloadable products of Project NOAH hosted in this server are open data licensed under the Open Data Commons Open Database License (ODC-ODbL). The full details of the license can be found here: https://opendatacommons.org/licenses/odbl/1.0/.

You are free to download, copy, transmit, redistribute, and adapt our data provided that Project NOAH and its contributors are always properly attributed. Please refer to the accompanying readme file for citations and references on how to use the data.

If you alter or build upon our data, you may only distribute the result under the same license (ODC-ODbL).
