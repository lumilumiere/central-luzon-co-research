# Research record — Central Luzon industrial district POC

**Updated:** 2026-11-02, closeout pass. **State:** research record on branch `co-research-report`. The overview for general readers is the [root README](../README.md).

This is research, not implementation. Nothing is ingested, calibrated, validated, approved or model-ready. Research decisions in [`decisions.md`](decisions.md) are AI-selected working choices unless marked as Joshua's (JD rows). The database was not touched.

## Navigation

| Path | Purpose |
|---|---|
| [`requirements-checklist.md`](requirements-checklist.md) | Every requirement, with one status each |
| [`acquisition/external-actions.md`](acquisition/external-actions.md) | One list of external actions for Joshua: what each unblocks and what proceeds without it |
| [`data-source-register.csv`](data-source-register.csv) | Authoritative register, 124 rows, with separate access, suitability, permission and evidence-quality statuses |
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
| [`findings/closeout-partial-items.md`](findings/closeout-partial-items.md) | Closeout of the six partial items |
| [`findings/jica-2012-counts.md`](findings/jica-2012-counts.md) | 2012 JICA counts and travel times, transcribed and checked (historical only) |
| [`findings/primary-source-audit.md`](findings/primary-source-audit.md) | Which findings rest on primary versus secondary sources |
| [`findings/corrections.md`](findings/corrections.md) | Corrections to earlier findings |
| [`findings/unsuccessful-searches.md`](findings/unsuccessful-searches.md) | Searches that found nothing usable |
| [`acquisition/request-templates.md`](acquisition/request-templates.md) | Unsent request templates and acquisition specifications |
| [`evidence/`](evidence/) | Scripts, queries, metadata, results, session extracts, environment lock |
| [`evidence/inputs/`](evidence/inputs/README.md) | Packed copies of volatile, redistributable inputs (OSM snapshots, boundary clips, Microsoft corridor lines, Overture places) |
| [`evidence/queries/queries.md`](evidence/queries/queries.md) | Queries, endpoints and observation times behind material results |
| [`evidence-manifest.csv`](evidence-manifest.csv) | Provenance, locations, versions, hashes |
| `local-data/` (git-ignored, not in repository) | Raw third-party data and source documents |

**Status terms:**
- **Requirement status (checklist):** Completed; Searched, no suitable evidence found; Blocked; Deferred; Still incomplete (RD-023).
- **"Not found":** no suitable source was found in the searches performed. It is not a claim that none exists.
- **Access:** the brief's vocabulary, from Metadata page accessible to Not tested, with reason.
- **Suitability:** Suitable for evaluation, Conditional, Unsuitable, Not assessed.
- **Permission:** Terms read at source, Metadata only, Unresolved, Restricted, Permission or payment required, Not applicable.
- **Evidence status:** Retained file, Logged result, Reproducible procedure, Missing evidence, Unverified.

## Reproducing

See [`methods.md`](methods.md). Scripts expect `local-data/` populated from the manifest's URLs and checksums. Inputs that live endpoints cannot return again are packed in [`evidence/inputs/`](evidence/inputs/README.md), and the packed copies were checked to reproduce the published results. PSA responses are not packed while their terms are unread.
