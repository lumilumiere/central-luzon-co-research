# 2012 JICA traffic counts and travel times — Central Luzon industrial district POC

**Status:** Completed (visual transcription with arithmetic checks). **Read on:** 2026-11-02 PHT.

**Use:** these are **historical comparators only**. They are 14 years old. They are not calibration targets, not validation data, and not evidence of current traffic.

## Source

- **Report:** *JICA Study on Railway for Clark–Metropolitan Manila for Greater Capital Region*, Final Report, survey appendix (Appendix A).
- **File:** https://openjicareport.jica.go.jp/pdf/1000012767_02.pdf. The PDF was created 2013-06-10, and its SHA-256 is `e1e61cb8b5a91018431cf7b75cedcd39c6545a5defbd08fa5ce90cd5c1c4fb17`.
- **Method:** text extraction scrambled the table columns, so pages 5, 6, 9, 10, 34 and 35 were rendered at 130 dpi with PyMuPDF and read visually. The renders stay in git-ignored `local-data/raw/documents/jica_renders/`.
- **Reuse terms:** JICA's terms were not read. Only cited figures are transcribed here, and the PDF is not committed.

## Pages read

| PDF page | Report page | Heading | Content used |
|---|---|---|---|
| 5 | A-4 | 1.4 Survey Location, Figure 1.4-1 | Station map and inset labels |
| 6 | A-5 | 1.5 Survey Duration and Survey Day and Date, Table 1.5-1 | Survey dates and durations |
| 9–10 | A-8, A-9 | 1.7.1 Traffic Count, Table 1.7-1 *Summary of Traffic Count Result* | Station totals |
| 34–35 | A-33, A-34 | 5.4.2 MacArthur Route, Table 5.5-1 *Survey Result for MacArthur Route* | Travel-time runs |

**Dates and durations:**
- The survey ran 12–30 October 2012 (§1.5).
- Most counts cover 18 hours, 05:00–23:00.
- The Angeles bridge and Clark Airport counts cover 24 hours, 05:00 to 05:00 the next day.

**Units:** vehicles counted over the stated period, all classes combined in the summary table. Classified and hourly detail is referred to "Appendix B", which was not located (see below).

## Corridor stations (Table 1.7-1, PDF page 10)

| Code | Station | Count | Period | Date (Table 1.5-1) |
|---|---|---|---|---|
| 17 | Angeles IC | Entrance 4,644; exit 4,174; total 8,818 | 18 h | Tue 2012-10-30 |
| 19 | Dau IC | Entrance 5,742; exit 6,534; total 12,276 | 18 h | Not listed |
| 26 | Bridge at Angeles | Southbound 15,537; northbound 17,980; total 33,517 | 24 h | Tue 2012-10-30 |
| 27 | Dau Access Road | Entrance 4,580; exit 4,260; total 8,840 | 18 h | Tue 2012-10-30 |
| 28 | Sta. Ines Access Road | Entrance 3,311 (SB 1,888, NB 1,423); exit 3,194 (SB 1,466, NB 1,728); total 6,505 | 18 h | Tue 2012-10-30 |
| 24 | Clark Airport | Entrance 2,280; exit 2,215; total 4,495 | 24 h | Blank in table |

**Location caution:**
- Dau and Sta. Ines are place names in Mabalacat, and Angeles IC and the Angeles bridge are in Angeles City, next to the study area.
- Station coordinates are not given, so the placement of each station is inferred from names and the map, not verified.
- Table 1.7-1 lists stations 25–28 under the NLEX block. Which road the Angeles bridge carries is not stated.

## MacArthur Highway travel-time runs (Table 5.5-1, PDF page 35)

- **Route:** nine runs between EDSA and Clark Airport, 86 km, on 19, 24 and 25 October 2012.
- **Run times:** 2:34:09 to 3:54:04, which is 22–33 km/h.
- **Report averages:** 3:17:05 from EDSA to Clark Airport (26 km/h), and 3:25:07 in the other direction (25 km/h).
- **Per-point speeds:** the text says these were about 15–45 km/h at most points (Figures 5.4-3 and 5.4-4).
- **NLEX runs:** shown on PDF pages 33–34, 6:00–8:27. Their table was not transcribed because it covers the expressway as a whole, not the corridor.

## Transcription checks

[`../evidence/scripts/jica_transcription_check.py`](../evidence/scripts/jica_transcription_check.py) runs on [`../evidence/results/jica_2012_transcription.csv`](../evidence/results/jica_2012_transcription.csv). Its output is in [`../evidence/results/jica_2012_transcription_check.txt`](../evidence/results/jica_2012_transcription_check.txt).

- 20 of 20 checks pass:
    - Every entrance and exit pair, and every southbound and northbound pair, sums to the printed total.
    - Every run's arrival minus departure equals the printed travel time.
- The printed EDSA-to-Clark average matches the mean of its five runs to within 1 second.

**Inconsistencies inside the source, recorded and not corrected:**
1. The printed Clark-to-EDSA average (3:25:07) is 519 seconds longer than the mean of the four listed runs (3:16:27).
2. Station 19 (Dau IC) is missing from Table 1.5-1, so its survey date is not stated. The Figure 1.4-1 inset numbered 19 is labelled "SCTEX Link".
3. Table 1.5-1 lists station 26 as northbound only, while Table 1.7-1 gives both directions.
4. The Clark Airport rows in Table 1.5-1 have no day or date.
5. The text calls the MacArthur table "Table 5.4-2", but its caption reads "Table 5.5-1".

## Appendix B

- **Hourly and classified detail is Not found.** It was searched for in volumes `_01`, `_03` and `_04` of the same report, which were downloaded and their hashes recorded in the manifest.
- Volumes `_05` to `_08` return HTTP 404.
- The search is recorded as **searched; no suitable evidence found**, not proof that Appendix B does not exist.

## Not transcribed (deferred, not needed for the franchise scope)

- Vehicle occupancy (Table 1.7-2).
- Roadside interview shares (Table 1.7-3).
- Station counts outside the corridor.
