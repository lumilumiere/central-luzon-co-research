# Research record — Central Luzon industrial district POC

**Updated:** 2026-11-02. **State:** research record on branch `co-research-report`. The overview for general readers is the [root README](../README.md).

This is research, not implementation. Nothing is ingested, calibrated, validated, approved or model-ready. Research decisions in [`decisions.md`](decisions.md) are AI-selected working choices unless marked as Joshua's (JD rows). The database was not touched.

## Navigation

| Path | Purpose |
|---|---|
| [`requirements-checklist.md`](requirements-checklist.md) | Every requirement, with status and deliverable |
| [`data-source-register.csv`](data-source-register.csv) | Authoritative register, 115 rows, with separate access, suitability, permission and evidence-quality statuses |
| [`decisions.md`](decisions.md) | Joshua's decisions and AI research decisions, kept separate |
| [`blockers.md`](blockers.md) | External blockers and evidence gaps |
| [`methods.md`](methods.md) | Environment, reproduction table, masking rules |
| [`findings/boundaries.md`](findings/boundaries.md) | Boundaries |
| [`findings/roads-and-transport.md`](findings/roads-and-transport.md) | Roads and transport |
| [`findings/buildings.md`](findings/buildings.md) | Buildings |
| [`findings/population.md`](findings/population.md) | Population |
| [`findings/employment-and-socioeconomic.md`](findings/employment-and-socioeconomic.md) | Employment and socioeconomic data |
| [`findings/land-values-and-costs.md`](findings/land-values-and-costs.md) | Land values and costs |
| [`findings/franchise-and-foot-traffic.md`](findings/franchise-and-foot-traffic.md) | Franchise and foot traffic |
| [`findings/environment-and-hazard.md`](findings/environment-and-hazard.md) | Environment and hazard |
| [`findings/validation-standards.md`](findings/validation-standards.md) | Standards, D-009 assessment, recommended checks |
| [`findings/licensing-and-privacy.md`](findings/licensing-and-privacy.md) | Licences, privacy, access procedures |
| [`findings/model-inputs-and-financial.md`](findings/model-inputs-and-financial.md) | Candidate model inputs and financial definitions |
| [`findings/post-opening-data.md`](findings/post-opening-data.md) | Post-opening data assessment and minimum schema |
| [`findings/background-research.md`](findings/background-research.md) | Prior art, reviewer categories, open questions |
| [`findings/corrections.md`](findings/corrections.md) | Corrections to earlier findings |
| [`findings/unsuccessful-searches.md`](findings/unsuccessful-searches.md) | Searches that found nothing usable |
| [`acquisition/request-templates.md`](acquisition/request-templates.md) | Unsent request templates and acquisition specifications |
| [`evidence/`](evidence/) | Scripts, queries, metadata, results, session extracts, environment lock |
| [`evidence-manifest.csv`](evidence-manifest.csv) | Provenance, locations, versions, hashes |
| `local-data/` (git-ignored, not in repository) | Raw third-party data and source documents |

**Status terms:**
- **Access:** the brief's vocabulary, from Metadata page accessible to Not tested, with reason.
- **Suitability:** Suitable for evaluation, Conditional, Unsuitable, Not assessed.
- **Permission:** Terms read at source, Metadata only, Unresolved, Restricted, Permission or payment required, Not applicable.
- **Evidence status:** Retained file, Logged result, Reproducible procedure, Missing evidence, Unverified.

## Reproducing

See [`methods.md`](methods.md). Scripts take paths as arguments and expect `local-data/` populated from the manifest's URLs and checksums. Sources such as Overture remove old releases, and live OSM queries return newer snapshots.
