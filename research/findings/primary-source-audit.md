# Primary-source audit — Central Luzon industrial district POC

**Date:** 2026-11-02 PHT.

**Correction:** the previous report said the validation standards were "read from primary texts". That holds for TAG M3.1, FHWA 2019, the NCTS guide and Sirko 2021 only. NCHRP 934, AACE 18R-97, ISO 19157 and the ITE rates were read only through secondary sources. This table classifies every material finding.

**Classes:**
- **Primary:** the publisher's own document or data, read here.
- **Official text, unofficial host:** a legal text read from a law library, not the official gazette.
- **Secondary:** a summary, press report or search excerpt.
- **Abstract only:** only the abstract or repository record was read.

| Finding | Where used | Class | Primary retrieval this pass | Action on the claim |
|---|---|---|---|---|
| TAG M3.1 link, screenline and journey-time criteria; modelled-area definitions | Validation standards §1–2 | Primary | Already local | None |
| FHWA Toolbox Vol. III 2019, four calibration criteria | Validation §1 | Primary | Web chapter | None |
| FHWA Vol. III 2004 targets | Validation §1 | Was secondary (TxDOT). Now **Primary** | [2004 §5, Table 4](https://ops.fhwa.dot.gov/trafficanalysistools/tat_vol3/sect5.htm), read 2026-11-02 | **Corrected:** Table 4 reproduces Wisconsin DOT freeway criteria (GEH < 5 on > 85% of links; GEH < 4 for the sum; journey times within 15% or 1 minute on > 85%). The "GEH below 3 on state facilities" figure is TxDOT's own practice, not FHWA's |
| FHWA Travel Model Validation and Reasonableness Checking Manual, 2010 | Validation §1 | Was "Not read". Now **Primary** | PDF retrieved (SHA-256 in manifest); page 9-18 read | **Upgraded:** the manual reports example state guidelines (for example Michigan's 5% and 10% screenline and cutline targets) and says they "should not be construed as standards; matching or exceeding the guidelines is not sufficient to determine the validity of a model" |
| TxDOT study-limit rule | Validation §1–2 | Primary for TxDOT practice | — | Labelled as one state's practice, not a standard |
| NCTS proposed TIA guidelines | Validation, inputs | Primary | Already local | None |
| NCHRP 934: 6% below forecast, 17% mean absolute deviation, 1,291 projects | Validation §1 | **Secondary** (companion paper summary) | Attempted: the National Academies OpenBook serves the summary pages as images with no extractable text. PDF download not attempted (account flow) | **Downgraded:** quoted as a secondary report, for context only, not as a benchmark |
| AACE 18R-97 class ranges | Validation §1, README | **Secondary** | Not retrievable without purchase (B-13) | Already "indicative only"; README now marks it secondary |
| ISO 19157 completeness (omission and commission) | Validation §1, buildings | **Secondary** (Brovelli and Zamboni 2018) | Standard is paid (B-13) | Used only as a definition of terms; no threshold claimed |
| Sirko et al. 2021 thresholds | Buildings, validation | Primary | Already local | None |
| Gevaert et al. 2024, Philippine audit of building datasets | Buildings | **Abstract only** | Attempted: repository PDF 403, TechRxiv 403, IEEE PDF not served | Only abstract-level statements are cited. The Philippine numbers are marked Not read |
| "Microsoft and Google both claim about 70% recall" | Buildings | Secondary (Gonzales 2023 citing vendors) | — | Kept as a reported vendor claim |
| Suhara et al., Huff model fit | Validation §1 | Abstract only | — | Labelled abstract only |
| Population stability index thresholds 0.10 and 0.25 | Validation §1 | Secondary (practitioner) | No standard exists to retrieve | Already "not an industry standard" |
| ITE 934 and 851 trip rates; pass-by shares | Model inputs §1 | **Secondary** (permit files quoting ITE) | ITE manual is paid (B-13) | Already "borrowed, ITE not read" |
| HCA employment densities | Model inputs §3 | Primary | Already local | None |
| PSA permits, ₱/m² | Model inputs §4 | Primary data; **unit Secondary** | JSON-stat2 response checked 2026-11-02: no unit metadata. The PSA April 2024 release PDF returns 403 | **Downgraded wording:** the thousand-peso unit is supported only by a search excerpt of a PSA release, and is not confirmed from table metadata |
| Damodaran January 2026 ERP 6.69% and CRP 2.46% | Financial | Primary (data file) | Already local | None |
| 10-year yield | Financial | Primary for ADB's AsianBondsOnline (multilateral publisher) | New this pass | Replaces the unverified "about 8.10%" |
| BSP policy rate 5.50% from 2026-10-22 | Financial | **Secondary** (press) | BSP page returned a script shell | Labelled secondary |
| 7-Eleven 2024 system-wide sales ₱93.45 billion and 4,130 stores; derived ₱64,800 per store-day | Financial | **Secondary** (press) | The FY2025 17-A summary gives company gross revenue and margins, but not system-wide sales or store count | Derived value kept, labelled as derived from secondary inputs |
| Philippine Seven margins | Financial | Primary (17-A summary) | New this pass | Company level only |
| Jollibee 2024 store count and system-wide sales | Financial | Primary (company release) | — | None |
| Franchise term 5–10 years | Financial | **Unverified** (search excerpt) | Not retrieved | Stays Unverified; used only as a sensitivity range |
| MMUTIS mode shares | Model inputs §2 | **Secondary** (blog, search summary) | MUCEP manual checked; no table | Not used |
| Road freight cost, Luzon | Model inputs | Primary | New this pass | — |
| SUMO sparse-data literature | Validation, background | Primary | New this pass | — |
| 2012 JICA counts and travel times | Roads, validation | Primary (visual reading) | New this pass | Historical comparator only |
| ODbL, CC BY-IGO, CDLA, HDX terms, OSM guidelines | Licensing | Primary | Already local | None |
| EO 2 (2016) §9; RA 10173 | Licensing, requests | Official text, unofficial host (lawphil) | Official Gazette copy not retrieved | Wording kept; host noted |
| NPC advisory opinions | Licensing | **Secondary** | Attempted: the 2020–2021 and 2023 compendium PDFs returned 403 | Already labelled; A14 blocked (B-12) |
| PSA OpenSTAT reuse terms ("CC BY") | Licensing | **Secondary** (search excerpt) | PSA terms pages 403 (B-03) | Permission stays Unresolved |
| Colliers Central Luzon rents | Model inputs | Secondary (press) | — | Not used |
| Agency FOI turnaround (DICT and NTC examples) | Requests | Primary (DICT reports) | New this pass | Examples only |

**Net effect:**
- Two items were upgraded to primary: FHWA 2004 and FHWA 2010.
- One attribution was corrected: the GEH < 3 figure is TxDOT's, not FHWA's.
- Two items were downgraded: the NCHRP 934 benchmark, and the wording of the permit unit.
- No recommendation changes. The D-009 recommendations rest on TAG, the 2019 FHWA guidance and the NCTS guide, all primary.
