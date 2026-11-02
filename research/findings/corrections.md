# Corrections to earlier read-outs — Central Luzon industrial district POC

**Date:** 2026-11-02 PHT. Earlier chat read-outs were not saved to the repository. These corrections are kept so nobody reuses superseded statements.

| # | Earlier statement | Correction |
|---|---|---|
| 1 | Boundary dispute offered as a possible cause of area gaps | Geometry differences are documented. The cause is not established, and most Mabalacat OSM-only area lies in COD-AB Angeles |
| 2 | Population tested against census for the checklist | The gate compares the combined total with the Admin3 projection sum, or explained |
| 3 | "Failed the census check" | Replaced by the gate reading plus municipal diagnostics, kept separate |
| 4 | "Fails for Mabalacat, not for Bamban or Capas" | Replaced. The gate is combined. Municipal 20% comparisons are diagnostics only |
| 5 | R2025A inputs "Not found" | Inputs documented, except the exact boundary file |
| 6 | 2024 national census 112,729,484 from secondary source | PSA table: 112,727,776. 2020: 109,033,245. The difference with secondary figures is not explained |
| 7 | "Google is stronger" | Withdrawn. Counts differ and reverse at ≥0.874. No accuracy ranking |
| 8 | Mapillary 10.9% and 3.9% as deep-learning prediction | Those were labelled ways. Predicted length is 62.3 km (4.2%), 3.9 km (0.6%), 0 km |
| 9 | Planet "best" source, "little unclassified" | Not established. Arterial classes only. The restriction blocks only this optional dataset |
| 10 | Planet 89.2% "global" | HDX states no geography |
| 11 | Microsoft licence "CLDA", no full text | README states CDLA Permissive 2.0 with a link. The difference is between channels |
| 12 | Keep ODbL layers separate | Withdrawn. Separation does not automatically settle duties |
| 13 | Mabalacat sensitivity "35,000–36,000" | 35,121 (2020) and 36,412 (2024), R2025A, COD-AB versus OSM |
| 14 | Connectivity "reproduced" | Rerun gave 13,386 ways, not 13,384. The first run's snapshot is Unverified |
| 15 | "Neither would change the recommendations" (unperformed tests) | Withdrawn. Effect unknown |
| 16 | Row 6.1 foot-traffic as a planned source | Its files contain no Philippine foot-traffic data |
| 17 | Checklist RDO 21B for Mabalacat treated as given | Secondary sources point to RDO 21A; needs official confirmation |
| 18 | Register held in chat only | Superseded by JD-01; `data-source-register.csv` is now authoritative |
| 19 | Google counts "the best fit that does not use census data" | Wrong for Capas and Bamban, where Microsoft is lower. Google has the smaller worst case only |
| 20 | "Misallocates" or "misplaces people" wording for the barangay test | It is an aggregate share mismatch. It does not establish where individual people live |
| 21 | Weak connectivity (98.8% of ways) described as the connectivity result | Directed test: largest strong component 96.3% of nodes and 96.7% of edges, with 670 strong components |
| 22 | Permit value unit "inferred, unconfirmed" | Supported by PSA's April 2024 release (value in thousand pesos), seen via excerpt; not read from table metadata |
| 23 | R2025A all-touched and id 49861 on OSM "not performed" | Performed 2026-11-02 (see `population.md`) |
| 24 | HDX general terms "unread" | Read at docs.humdata.org: dataset licences govern use, and personal data is prohibited |
| 25 | Checklist row 2.6 "≤1 major disconnected component" treated as a test of the graph | It is an unsourced assumption; see `validation-standards.md` |
| 26 | Reproduction script matched barangay names across municipalities | Bug found by the sum check; names repeat, so matching is now per municipality. Published figures were unaffected |
