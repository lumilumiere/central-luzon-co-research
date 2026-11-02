# Validation standards and recommended checks — Central Luzon industrial district POC

**Access date:** 2026-11-02 PHT.

Standards below come from other jurisdictions unless stated, and are **imported** into this context. No standard here has been adopted by Joshua. The D-009 limits remain his working assumptions until he decides otherwise.

## 1. Published standards found

| Topic | Source | What it says | Applicability here |
|---|---|---|---|
| Link flow validation | [DfT TAG Unit M3.1](https://assets.publishing.service.gov.uk/media/6a033d074fb0713aa63ea802/tag-m3-1-highway-assignment-modelling.pdf), May 2026, Table 2 (primary read) | Individual flows within 100 veh/h below 700 veh/h, within 15% for 700–2,700 veh/h, within 400 veh/h above 2,700 veh/h, and GEH < 5, each for more than 85% of cases | UK highway assignment; needs observed hourly counts, which the corridor lacks |
| Screenline validation | Same, Table 1 | Modelled flows within 5% of counts on all or nearly all screenlines (about 95%); screenlines normally 5 or more links | Same limit |
| Journey times | Same, Table 3 | Modelled times within 15% of surveyed times (or 1 minute if higher) on more than 85% of routes | Usable if travel-time runs are obtained |
| Modelled area | Same, §2.2 | Fully Modelled Area, Area of Detailed Modelling and External Area, set by where interventions have influence | Defines study area by influence, not by a fixed distance |
| Microsimulation calibration | [FHWA Traffic Analysis Toolbox Vol. III, 2019 update](https://ops.fhwa.dot.gov/publications/fhwahop18036/chapter5.htm) | Four criteria against observed variation: 95% of outputs within about a 2-sigma band; two-thirds within 1 sigma including critical intervals; bounded dynamic absolute error; systematic error at most one-third of that threshold | Needs several observed days to build variation envelopes |
| Older microsimulation targets | [FHWA Vol. III 2004, §5, Table 4](https://ops.fhwa.dot.gov/trafficanalysistools/tat_vol3/sect5.htm) (primary, read in the closeout pass) | Reproduces Wisconsin DOT freeway criteria: link flows within 100 veh/h, 15% or 400 veh/h by flow band; GEH < 5, each on > 85% of cases; GEH < 4 and within 5% for the sum of link flows; journey times within 15% or 1 minute on > 85% | One state's criteria, as cited by FHWA. Superseded by the 2019 guidance for FHWA projects |
| State practice | [TxDOT manual §13.5.2](https://www.txdot.gov/manuals/des/tsp/chapter-13-microsimulation-analysis/13-5-calibration/13-5-2-acceptability-criteria.html) | GEH below 3 preferred on state facilities | TxDOT's own practice. **Corrected:** earlier text attributed this to FHWA 2004 |
| Study limits | [TxDOT §13.2.2](https://www.txdot.gov/manuals/des/tsp/chapter-13-microsimulation-analysis/13-2-project-scope/13-2-2-study-limits.html) (secondary summary) | Extend at least one intersection or interchange beyond the farthest in the study area, and far enough to capture queues | Network edge rule, stated in junctions not kilometres |
| Philippine TIA practice | [UP NCTS, *Proposed Philippine Traffic Impact Assessment Guidelines*](https://ncts.upd.edu.ph/wp-content/uploads/2026/04/TIA_Guide_for_the_Philippines.pdf), file dated 2026-04 (primary read) | TIA suggested at 100 or more new peak-hour vehicle trips; minimum study area covers site access points and adjacent intersections, with more set by the approving authority; ITE as a rate source, local rates allowed with evaluator approval | Labelled proposed and non-prescriptive; adoption status Not found |
| Travel model validation | [FHWA Travel Model Validation and Reasonableness Checking Manual, 2nd ed., 2010](https://rosap.ntl.bts.gov/view/dot/55924) | Families of checks for trip generation, distribution and mode choice; described as best practice, not required steps. Page 9-18 lists example state guidelines (for example Michigan's 5% for screenlines and 10% for cutlines) and says they "should not be construed as standards; matching or exceeding the guidelines is not sufficient to determine the validity of a model" | Primary, read in the closeout pass (PDF retrieved). Reinforces that numeric targets are guidelines, not standards |
| Forecast accuracy | [NCHRP Report 934](https://nap.nationalacademies.org/read/25637) (2020), via a companion paper summary (**secondary**) | Reported: 1,291 US and European projects, with measured traffic averaging 6% below forecast and a 17% mean absolute deviation | Context only for pre- versus post-opening traffic comparison, not sales. The primary text was not read (OpenBook pages are images) |
| SUMO calibration with sparse data | [Closeout §1](closeout-partial-items.md#1-sumo-calibration-with-sparse-data--completed) (primary papers and SUMO documentation) | All methods found fit demand to observed counts. Reported errors such as NRMSE 0.08 are measured against the calibration counts themselves | An NRMSE gate on calibration counts is in-sample fit. Validation needs held-out counts |
| Building detection | [Sirko et al. 2021](https://arxiv.org/pdf/2107.12283) (primary read) | Per-S2-cell confidence thresholds targeting 80%, 85% and 90% precision at 0.5 IoU; confidence filtering raises precision, with unknown effect on recall | Thresholds apply to tile 339 as a whole, not to these municipalities |
| Data quality | ISO 19157, via [Brovelli and Zamboni 2018](https://mdpi-res.com/d_attachment/ijgi/ijgi-07-00289/article_deploy/ijgi-07-00289.pdf) | Completeness as omission and commission measured against reference data | No corridor reference building data was found in the searches performed (T-09 specifies one) |
| Cost estimates | AACE 18R-97, secondary summaries only | Class 5 about −20% to −50% and +30% to +100%; Class 4 about −15% to −30% and +20% to +50%; summaries disagree, and 56R-08 covers buildings | AACE text not read; use as indicative bands only |
| Gravity location models | [Suhara et al., *Big Data*](https://journals.sagepub.com/doi/10.1089/big.2020.0161) | Huff model fit transaction data well for groceries, clothing, gas and restaurants | US transaction data; needs store-level observations to test here |
| Drift monitoring | Practitioner sources | Population stability index with 0.10 and 0.25 thresholds, paired with actual-to-expected ratios | Not an industry standard; no retail-specific guidance found |

**Searched; no suitable evidence found** (in the searches performed, which is not proof that none exists):
- Philippine traffic-calibration acceptance criteria.
- A published accuracy standard for franchise sales or return forecasts.
- A standard for population raster agreement with census totals.

Primary versus secondary support for each row is classified in [`primary-source-audit.md`](primary-source-audit.md).

The reference MVP uses its own NRMSE ≤ 0.30 gate for a corridor back-test, an internal threshold rather than a published standard.

## 2. D-009 working assumptions

In this table, "Not found" means no published standard or precedent was found in the searches performed. That shows each threshold is **unsourced in the checklist**. It does not show that no applicable standard exists anywhere.

| Assumption (`05`) | Published standard or precedent | Assessment | Recommendation |
|---|---|---|---|
| 2–5 km study-area buffer (row 1.3) | **Not found** as a fixed distance. TAG defines areas by intervention influence. TxDOT extends to the next junction beyond the study area and to queue ends. The NCTS guide's minimum area is site access points and adjacent intersections | A fixed radius is neither supported nor contradicted. For a single store, the NCTS minimum area is far smaller than 2 km | **Replace** with an influence rule: the TIA minimum area plus the next junction beyond, for site access. For network models, extend to the first major junction or interchange outside the AOI. Keep 2 and 5 km only as sensitivity runs |
| AOI coverage ≥ 95% (Phase 8) | **Not found** as a coverage standard. ISO 19157 measures completeness, without a universal threshold. TAG's 95% is a screenline count rule, a different measure | "Coverage" is undefined: extent coverage is near 100% for national sources, while completeness is unmeasured | **Revise:** report extent coverage, and separately measure omission and commission on a sampled reference set. Keep 95% only as an internal target, labelled as such |
| At most 1 major disconnected road component (Phase 8) | **Not found** as a numeric standard. Common practice keeps the largest strongly connected component; SUMO `netconvert` offers `--remove-edges.isolated` | On the 2026-11-02 OSM bbox sample, the largest strong component holds 96.3% of nodes and 96.7% of directed edges. 28 other strong components have 10 or more nodes. Weak connectivity alone (98.8% of ways) overstated routability | **Revise** to a directed test: report the largest strong component's share and list every strong component of 10 or more nodes inside the AOI, each explained or fixed. The share is not yet a standard |
| Population within 20% of the Admin3 projection sum (Phase 8) | **Not found.** The comparator is a projection from the 2015 census, now superseded by the 2020 and 2024 censuses | A projection is a weaker comparator than the census, and a combined total hides local errors | **Replace:** rescale totals to PSA census counts by municipality, and test distribution with barangay share mismatch against PSA 2024 counts. Report both, and keep the 20% check only for comparison with the original checklist |

## 3. Recommended checks for the evaluation phase

These are research recommendations, not adopted standards:

1. **Roads:**
    - Directed strong-component test on the pinned extract.
    - Tag-completeness tables by class.
    - Junction-based buffer.
    - Travel-time comparison against any observed runs, such as the 2012 JICA MacArthur runs. These are dated, so use them for order-of-magnitude checks only.
2. **Traffic:** if counts are obtained, use TAG link and journey-time tables as an imported benchmark. Report GEH and percent difference, and do not claim pass or fail without counts.
3. **Population:** census rescaling by municipality, barangay share mismatch, and both boundary bases.
4. **Buildings:** a manually digitised random sample of footprints on recent imagery, reporting omission and commission by municipality. This would be a new reference dataset, and would need people and imagery rights.
5. **Trip generation:** ITE rates labelled borrowed. Local counts at comparable stores are the only way to calibrate.
6. **Franchise forecasts:** hold-out testing on existing stores with known sales (Not available today). Report error by store, and do not use synthetic stores as validation.
7. **Post-opening comparison:** actual against predicted per store and period, the actual-to-expected ratio, and drift monitoring on inputs. This needs post-opening data (see [`post-opening-data.md`](post-opening-data.md)).
8. **Uncertainty:** keep UNC-01 Monte Carlo on cost inputs, as decided in D-010. Run one-lever sweeps on demand. Present ranges as parameter uncertainty, not calibrated predictive confidence.
