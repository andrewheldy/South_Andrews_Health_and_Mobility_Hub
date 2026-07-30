# Missing Research Register

**Status:** Current operative missing-dependency register · **Last reviewed:** 2026-07-29
**Governing documents:** `AGENTS.md`, `docs/governance/SOURCE_AUTHORITY.md`, `docs/governance/WORKFLOW.md`
**Related:** [Source Inventory](Source%20Inventory.md) · [Open Questions](Open%20Questions.md) · [Implementation Roadmap](Implementation%20Roadmap.md)

This register records everything the repository *references or requires but does not contain*. It has two parts:

- **Part A — Referenced-but-absent documents.** Files that existing sources cite as governing or evidentiary, but which are not in `sources/` or `docs/`.
- **Part B — Research and diligence not yet performed.** Studies the project needs before material claims can be promoted beyond working assumptions.

Classification: unless noted, every entry is an **open question** under the AGENTS.md evidence classifications.

---

## Part A — Referenced-but-absent documents

> Observed fact: the Owner's Development Program (`sources/current/Andrews ODP with Dashboard.docx`) declares itself "Subordinate to Project Constitution and Project Decision Log" and cites a five-report research library. **None of these documents exist in this repository.** The 6v8 Story Model also cites a "Project Constitution," "Decision Log," "Operational Study," "Feasibility Study," and "Site Analysis" in its source notes. The repository's operative constitution today is `AGENTS.md` + `docs/governance/`. This is the largest knowledge-integrity gap in the repository.

| ID | Missing document | Cited by | What it is claimed to contain | Recommended action |
|---|---|---|---|---|
| MA-01 | **Prior Project Constitution** | ODP; 6v8 Model | Historical governing principles and decision framework | **Missing but expected to exist.** D-P9 makes current governance operative; recover as historical evidence and reconcile before any supersession |
| MA-02 | **Prior Project Decision Log (Decisions 001–003)** | ODP | Historical foundational decisions | **Missing but expected to exist.** Current owner decisions are recorded separately; recover the prior log as historical evidence |
| MA-03 | **Prior README § Document Hierarchy** | ODP precedence table | Historical document-precedence statement | **Missing but expected to exist.** D-P9 supersedes any claim that it is currently operative; recover for historical context |
| MA-04 | **Design Standards** | ODP Ch.13 ("should migrate into the Design Standards document") | Permanent design principles | Create later from ODP Ch.13 during implementation phase |
| MA-05 | **Open Questions file (original OQ-01…OQ-13)** | ODP Ch.14 ("extends the project's Open Questions file") | Original open-question tracker | Superseded by [Open Questions](Open%20Questions.md) in this planning set |
| MA-06 | **Underwriting Standards** | ODP Ch.11 ("built to the project's Underwriting Standards") | Required model outputs, confidence conventions | Recreate as part of financial-model reconciliation work |
| MA-07 | **Healthcare Market & HBU Analysis ("Market Study")** | ODP (HBU "Highest" rating, 10.4% vacancy, co-working shift, medtail segments, $180k+ HHI demographics, Live Local guidance) | The demand evidence for the healthcare thesis | **High priority.** Locate and add; until then every Market-Study-derived claim is *source-derived but not independently verified* at one remove (cited via ODP only) |
| MA-08 | **Feasibility & Benchmark Study** | ODP (FlexPark/WGI, 9th Ave Parkade, Lavin Pavilion, Lennar, Hoag, Moffitt, CHOP failure case, convertibility premium 10–15% / up to 32%, phasing logic) | Benchmarks and failure cases behind structural strategy | Locate and add; same caveat as MA-07 |
| MA-09 | **Site Intelligence Report** | ODP (ULDR table: 110 ft/150 ft heights, 50 du/ac, 0-ft build-to, QOZ, utilities, mobility-hub funding) | Zoning/utility/site research | Locate and add; zoning figures remain unverified vs. City until Zoning Verification Letter (MB-01) regardless |
| MA-10 | **Boundary Survey (John Ibarra & Assoc., 10/2/2015, Inv. 15-003948)** | Appraisal p.10 (data sources); Appraisal Valuation workbook `Source Document Register` S-2; ODP ("Boundary Survey controls parcel geometry") | Parcel geometry, frontages, building footprints | **High priority.** Obtain the survey PDF; it is named as the controlling document for parcel geometry but is absent. Also note it is a 2015 survey — an update is a diligence item (MB-10) |
| MA-11 | **South_Andrews_Electrical_Load_Model.xlsx** | 8M Construction Feasibility `Sources!A8` ("Existing electrical load model base plan"); its 9.6 kW/port and 1,500 kWh/kW-yr factors | EV/solar/building load model | **High priority.** Locate and add to `sources/`; the 8M workbook's energy figures currently trace to a file that cannot be inspected |
| MA-12 | **Andrews_Context.md** | ODP Table 24 ("a separate context file (Andrews_Context.md) … describe an autonomous-vehicle / robotaxi 'Mobility Nexus'") | The competing Mobility-Nexus thesis text | Locate for the historical record; classify as **rejected scenario** narrative per ODP resolution |
| MA-13 | **Phase I & Phase II Environmental Site Assessments** | Appraisal p.10 (listed among information sources); Native Realty study step 3 ("obtain and review the existing Phase I and Phase II") | Environmental condition of the site | **High priority.** Obtain from seller/appraiser file; existence is asserted by two third-party sources but the reports are not in the repo |
| MA-14 | **Highland Contractors Inc. construction estimate** | Appraisal p.10 (data sources) | Seller-side construction estimate (for the Agora retail concept) | Obtain if available; classify as third-party/seller context only |
| MA-15 | **AEI Zoning Report** | Appraisal p.10 ("available separately from this Appraisal report") | Appraiser's zoning review | Obtain from AEI file |
| MA-16 | **"Operational Study" / "Site Analysis" / "Feasibility Study" cited in 6v8 Model** | 6v8 Model `Assumptions` column E (e.g., E8, E24, E28, E33, E53, E56, E69) | Programming basis, cost premiums, rent evidence, parking pricing survey | Determine whether these are MA-07/MA-08/MA-09 under other names or separate documents; until resolved, the affected inputs are working assumptions with untraceable citations |
| MA-17 | **"Plan 3" (session plan referenced by 6v8 Model governance note)** | 6v8 Model `Summary!A15` | The framing decision behind the "Andrews Mobility Nexus" session | Locate session record or record as unrecoverable; the framing is superseded by AGENTS.md identity rules |
| MA-18 | **Current listing / offer correspondence** | Native Realty study ("current listing", "three commercial assets"); appraisal ("previously listed at $12,000,000 but is currently not listed") | Listing status and any offer/LOI paper trail | Add transaction documents to `sources/raw/` as they are generated. **Extended 2026-07-29:** S9 §12 refers to a "draft $7.5 million purchase offer and entitlement rider." **No offer, LOI, term sheet, or rider exists anywhere in the repository** (CVR-03), and the $7.5M basis is not a ratified decision (OQ-31 / D-P13 pending). Do not draft the instrument before that decision |
| MA-19 | **Primary-source captures behind the Toothaker context file (S9)** | S9 §15 (LinkedIn profile, TOOTHAKER.org firm site, The Florida Bar attorney directory, UF Bob Graham Center biography, Best Lawyers, Super Lawyers, South Florida Business & Wealth, History Fort Lauderdale) | The public-record basis for S9's professional, educational, and Florida Bar claims | **Capture to `sources/raw/` with retrieval dates.** S9's factual base is currently uninspectable in the repository — the same defect recorded for the electrical load model (CVR-01). Florida Bar standing and discipline history must additionally be rechecked on the day of any engagement |

---

## Part B — Research and diligence not yet performed

Priority: **Critical** = gates owner decisions or design spend; **High** = gates entitlement/financing; **Medium** = gates later phases.

| ID | Missing research | Why it is needed | Gates | Priority | Related OQ |
|---|---|---|---|---|---|
| MB-01 | **Zoning Verification Letter + City pre-application (DRC)** | All height/FAR/parking figures originate from research reports, not a City determination. Height claims conflict across sources (110 ft "by right" vs Level III review above 6 stories vs 12-story ceiling) | Massing, program, both scenarios | Critical | OQ-03, OQ-11 |
| MB-02 | **Architect/parking test-fit** | The two current models use irreconcilable floor plates (35,000 SF vs 28,000/24,000 SF); stall counts differ by ~50% | Program, parking counts, all financials | Critical | OQ-02, OQ-14 |
| MB-03 | **FPL will-serve / load study** | $750K (6v8) vs $1.5–1.8M (8M) utility allowances; imaging tenancy and DCFC expansion gated on capacity; 1.5/2.0 MVA targets are planning-only | Imaging, EV expansion, MEP design | Critical | OQ-04 |
| MB-04 | **Traffic study** | Separated AV ingress/egress concept on secondary streets is unvalidated; curb cuts subject to City approval | Site plan, entitlement | High | OQ-05 |
| MB-05 | **Stormwater / civil hydrology design (Zone AE)** | Entire site in FEMA AE; ODP calls stormwater the most critical utility-engineering challenge and entitlement-gating | Entitlement | High | OQ-06 |
| MB-06 | **Geotechnical borings** | Soils "reported typical" is an appraisal-level assumption only | Foundation design | High | OQ-07 |
| MB-07 | **Healthcare leasing evidence: MOB rent comps + absorption** | Rent conflict $36/RSF ("FACT"-tagged, overclaimed) vs $50/RSF (illustrative); 10.4% vacancy caveat unrefreshed | Revenue model, feasibility conclusion | Critical | OQ-15 |
| MB-08 | **Medical co-working operator LOI outreach** | Anchor-tenant strategy depends on an unnamed operator; no LOI exists | Financing, Phase 2 | High | OQ-08 |
| MB-09 | **Parking demand & utilization study** | $2,400/space/yr (6v8) vs $275/mo × 55% monetized (8M) rest on a pricing survey that is not in the repo | Parking revenue | High | OQ-16 |
| MB-10 | **Updated title commitment + survey update** | Survey is dated 2015; encumbrances "no known adverse" is an appraisal assumption | Closing | Medium | OQ-09 |
| MB-11 | **Phase I ESA (refresh) — plus recovery of existing Phase I/II** | Existing reports referenced but absent (MA-13); age unknown | Closing, financing | Medium | OQ-13 |
| MB-12 | **Insurance quotes (flood + HVHZ + coastal)** | "Higher insurance costs" verified as a risk but never quantified in any source | Opex, feasibility | Medium | — |
| MB-13 | **Tax counsel: QOZ structuring; §48E solar/storage and §30C charger credit eligibility** | Direct conflict: 6v8 underwrites 30% ITC; 8M underwrites 0% citing 2025–2026 law changes and the 6/30/2026 30C placed-in-service deadline | Capital stack, solar/BESS economics | Critical | OQ-17 |
| MB-14 | **Public incentives scan: MPO mobility-hub grants, TIF, P3 avenues** | Cited as capital-stack avenues to test (ODP Ch.11); both models show a yield gap that grants/partner support must help close | Feasibility | High | — |
| MB-15 | **AV-operator market soundings (Waymo, Zoox, Tesla, Freebee)** | All four are context-only today (8M `Sources` sheet: "No partnership or site demand assumed"); staging-lease toggle adds $300K/yr NOI only if a lease is signed | Phase 3 optionality valuation | Medium | — |
| MB-16 | **Construction escalation & GC market pricing** | Unit costs conflict across models ($105 vs $115 garage; $310 vs $290 shell; $75 vs $135 TI); all are planning allowances pending GC validation | Budget | High | OQ-10, OQ-18 |
| MB-17 | **Hospital-demand verification (Broward Health MOB, GME program)** | 188,000 SF MOB / 365 residents / 2027 opening are source-derived via ODP & legacy prospectus, not independently verified | Healthcare thesis evidence | High | — |
| MB-18 | **Live Local Act / TDR / bonus-height counsel review** | Listed as "not yet verified" in Corrected Assumptions §5; legislative volatility flagged in ODP R-5 | Height strategy | Medium | OQ-03 |
| MB-19 | **Appraisal reconciliation memo ($11.1M vs $8.0M offer vs $8.96M residual)** | Three defensible-but-different land values exist; negotiation strategy should be documented as an owner decision | Acquisition | High | OQ-12 (context), OQ-20 |
| MB-20 | **Economic-impact analysis** | Legacy prospectus explicitly declines to state figures until analysis exists ("we have chosen not to estimate them here") | External communications, City package | Medium | — |
| MB-21 | **Land-use counsel written opinion** — use characterization; accessory-parking ratio limit; height pathway and review level against the actual ULDR text; parking methodology and shared-parking availability; Live Local preemption; applicant identity; and the purchase-contract feasibility, entitlement, and closing-milestone structure | Previously folded inside MB-01. Broken out 2026-07-29 because it is a distinct instrument, it precedes and shapes MB-01, and it is the single purchase that can close OQ-03, OQ-26, OQ-27, OQ-30 and OQ-32 together. The controlling height text in evidence is truncated mid-word; the accessory-parking argument is uncited; no shared-parking provision is quoted in any source | Offer structure, entitlement strategy, program scale, acquisition decision | **Critical** | OQ-03, OQ-26, OQ-27, OQ-30, OQ-32, OQ-33 |

---

## Reading guide

- Nothing in Part B may be replaced by an assumption promoted to fact. Until an item lands, downstream claims stay at their current classification.
- When a Part A document is recovered, add it to `sources/` under the appropriate class, register it in [Source Inventory](Source%20Inventory.md), and re-run the affected rows of the [Contradictions Matrix](Contradictions%20Matrix.md).
