# Licensing, privacy and access procedures — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT. This is research, not legal advice, and no legal clearance is claimed. An accessible download does not establish permission to use or redistribute.

## Terms read at the source

| Source | Terms | Key obligations |
|---|---|---|
| OSM (Geofabrik, Overpass, ohsome) | [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) | §4.4: a publicly used derivative database must be ODbL or compatible. §4.5: collective databases and produced works are not themselves derivative databases, though ODbL still applies to the OSM part |
| OSMF guidance | [Produced Work guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Produced_Work_-_Guideline); [Collective Database guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline) (board-endorsed 2016-06-17) | Maps or images made from OSM can carry any licence, with attribution. Separate distinct layers may be added. Whether a combined dataset is collective or derivative depends on how data is combined |
| Google Open Buildings v3 | CC BY 4.0 or ODbL, user's choice ([page](https://sites.research.google/gr/open-buildings/)) | Attribution |
| Microsoft footprints, GitHub channel | [CDLA Permissive 2.0](https://cdla.dev/permissive-2-0/) per README | Share the agreement text with the data; §3 places no restriction on Results |
| Microsoft, Planetary Computer channel | ODbL-1.0 in collection metadata | Channels differ; treat as unresolved for that channel |
| WorldPop | [CC BY 4.0](https://hub.worldpop.org/data/licence.txt) | Attribution |
| COD-AB, geoBoundaries | CC BY 3.0 IGO ([legal code](https://creativecommons.org/licenses/by/3.0/igo/legalcode)) | Include the licence or its URI; no added restrictions |
| HDX platform | [HDX Terms of Service](https://docs.humdata.org/about/hdx-terms-of-service) | Users must follow each dataset's licence; datasets may not contain personal data |
| ESA WorldCover | CC BY 4.0 | Attribution |
| NOAH hazard maps | ODC-ODbL, per the NOAH licence file copied on the mirror | Share-alike |
| HeiGIT Planet road surface | HDX `license_other` field | Non-commercial; redistribution subject to Planet Labs terms |
| Protected Planet | [Terms](https://www.protectedplanet.net/en/legal) | No redistribution; commercial users are directed to IBAT |

## Unresolved, with the exact question and evidence

| Source | Question | Evidence | Tried |
|---|---|---|---|
| PSA OpenSTAT | Do the published terms allow commercial use and redistribution of derived tables? | A search-engine excerpt of `openstat.psa.gov.ph/Terms` says tables are "Open Data with Creative Commons Attribution License (cc-by)", and the Open Data Product Agreement asks for acknowledgement. Page text not read | OpenSTAT Terms, About and regional office pages all returned 403 on 2026-11-02. An archive lookup was refused by session controls and not retried. No browser tool is available in this session |
| BIR zonal values | Reuse terms for published schedules | None found | Portal is a scripted shell |
| Microsoft on Planetary Computer | Which licence governs this channel | ODbL there; CDLA on GitHub | Both read |
| Kaggle uploads | Uploader rights | Labels are uploader claims | Listings read |
| Overture | Per-provider terms for places | [Attribution page](https://docs.overturemaps.org/attribution/) | Read |
| ODbL in combined outputs | Would a store-scoring table built from OSM and other data be a derivative database? | Turns on how data is combined (ODbL §4.4–4.5; OSMF guidelines) | Legal review needed |
| Franchise data from companies | Permitted uses, confidentiality, retention | No agreement exists | Joshua's outreach |

**Restriction on an optional source only:** the Planet road-surface restriction does not affect OSM roads.

**Separation is not a licensing solution:** keeping layers in separate files does not automatically settle obligations. What matters is whether outputs are produced works, collective databases or derivative databases.

## Privacy and confidentiality

- **Scope:** the Data Privacy Act (RA 10173) covers processing of personal information of Philippine residents ([text](https://lawphil.net/statutes/repacts/ra2012/ra_10173_2012.html)).
- **Anonymised data:** a secondary source cites NPC Advisory Opinion No. 2017-27 for the view that genuinely anonymised data falls outside the Act, provided the processor cannot access the identifiable records. The opinion itself was not read: **Unverified**.
- **Before anonymisation:** NPC Advisory Opinion 2019-032 (secondary copy) treats data received before anonymisation as covered.
- **Implications:**
    - Phone-derived mobility data needs a privacy review and a clear lawful basis, even if delivered aggregated.
    - Store sales are company records, not personal data, but confidentiality terms are needed.
    - No customer-level data should be requested.
- **Research exemption:** whether the Act's research and statistical provisions apply to this commercial POC: **Not found**.

## Access procedures

- **FOI (EO 2, 2016, §9):** written request with name, contact details, valid identification and a description of the information. Response within 15 working days, extendable, with non-response deemed denial ([text](https://lawphil.net/executive/execord/eo2016/eo_2_2016.html)). The eFOI portal covers participating agencies.
- **Agency-specific practice:** documented turnaround for each agency (PSA, BIR, DPWH, LTFRB, LGUs): **Not found**.
- **Templates:** see [`../acquisition/request-templates.md`](../acquisition/request-templates.md). Nothing has been sent.

## Status groups

| Group | Sources |
|---|---|
| Terms read at source | OSM, Google, Microsoft GitHub, WorldPop, CC BY-IGO text, HDX platform terms, WorldCover |
| Metadata only | COD-AB and geoBoundaries licence fields, HeiGIT Mapillary, Overture, NOAH (mirror), Copernicus DEM |
| Unresolved | PSA, BIR, Microsoft Planetary Computer, Kaggle labels, ODbL in combined outputs |
| Restricted | HeiGIT Planet, Protected Planet |
| Permission or payment required | ITE, commercial mobility, company data |
