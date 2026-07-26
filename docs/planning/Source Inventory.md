# Source Inventory

**Status:** Current operative source inventory · **Last reviewed:** 2026-07-26
**Governing documents:** `AGENTS.md`, `docs/governance/SOURCE_AUTHORITY.md`, `docs/governance/WORKFLOW.md` (Phase 1 output)
**Related:** [Source Authority Register](Source%20Authority%20Register.md) · [Missing Research Register](Missing%20Research%20Register.md) · [Document Dependency Graph](Document%20Dependency%20Graph.md)

Complete inventory of every file in `sources/`, plus governance and skills. Every source was opened and read in full during this session (all workbook sheets and formulas inspected read-only; no source modified, moved, or renamed). Do not infer content from filenames — the "Content summary" column reflects actual inspection.

Source IDs (S1–S8) are used across all planning documents.

---

## sources/current/

### S1 — `sources/current/South_Andrews_Corrected_Assumptions.md`
- **Format / size / dates:** Markdown, 5.6 KB; file modified 2026-07-26. No internal date; references the September 2025 appraisal as existing.
- **Purpose:** Grounded review separating Verified Facts, Appraisal Opinions, and Project Hypotheses; corrects over-reliance on the $11.1M appraisal; supports an ~$8M opening offer.
- **Provenance:** Owner/analyst working document (unsigned).
- **Authority:** Controlling tier 2 (per AGENTS.md hierarchy, below explicit current owner decisions). Scope: assumption classification, appraisal interpretation, investment position.
- **Content summary:** $11.1M appraisal supports land value but does not validate the Hub concept; appraisal comps critiqued (condemnation-influenced sale, hospital-assemblage sale, superior downtown entitlements); verified constraints (enhanced review above 6 stories, ~12 stories possible under RAC-RPO subject to review, Zone AE); not-yet-verified items (max FAR, height pathway, TDRs, Live Local, OZ strategy); assumption register skeleton; recommends visual fact/opinion/hypothesis tagging.
- **Dependencies:** Derives from S6 (appraisal). Documents depending on it: both current models implicitly; all planning documents.
- **Conflicts:** None material against governance; it is the source that *frames* conflicts.
- **Integrity notes:** None.
- **Confidence:** High as a classification framework; its factual claims trace to S6.
- **Recommended action:** Keep as controlling. Add an internal date/author line when the owner next revises it.

### S2 — `sources/current/South Andrews 6v8 Story Model.xlsx`
- **Format / size / dates:** XLSX, 23.8 KB; file modified 2026-07-26; internal basis date "Q3 2026" (`Assumptions!A2`). 6 sheets: Summary, Assumptions, Program, Budget, Operating, Returns. No hidden sheets; no external links; fully formula-driven.
- **Purpose:** 6-story vs 8-story construction & returns comparison at $8.0M land, 35,000 SF plate.
- **Provenance:** Owner/AI session model ("Owner directive this session" notes).
- **Authority:** Controlling tier 3. Scope: scenario comparison at its stated program basis.
- **Content summary:** 6-story = L1 + 3 parking + 2 office → 210,000 GBA, 59,500 RSF, 340 stalls; 8-story = L1 + 4 parking + 3 office → 280,000 GBA, 89,250 RSF, 440 stalls. TDC $71.52M / $94.97M; stabilized NOI $2.738M / $3.820M; yield on cost 3.83% / 4.02%; stabilized value at 6.25% cap $43.8M / $61.1M; development profit **−$27.7M / −$33.9M**; unlevered 10-yr IRR 1.24% / 1.85%. AV staging lease toggle = 0 (base case excludes; "no LOI exists"). Solar 300/340 kW with 30% ITC captured; BESS 600 kWh; 32 L2 + 8 DCFC.
- **Dependencies:** Cites "Project Constitution," "Decision Log," "Operational Study," "Feasibility Study," "Site Analysis," "Plan 3 / Andrews Mobility Nexus" — none in repo (see [Missing Research Register](Missing%20Research%20Register.md) MA-01, MA-02, MA-16, MA-17).
- **Conflicts:** Program basis, rents, unit costs, ITC treatment vs S3 (see [Contradictions Matrix](Contradictions%20Matrix.md)).
- **Integrity notes:** (a) `Assumptions!D53` tags $36/RSF rent as "FACT" — an overclaim; under repository classifications it is at most *source-derived but not independently verified* (cites an "Operational Study" not in repo). (b) `Assumptions!D7` site area FACT is corroborated (S6). (c) Formulas independently traced this session: Budget/Operating/Returns arithmetic is internally consistent; cached values match formula logic. (d) Summary governance note documents the "Mobility Nexus" framing tension explicitly.
- **Confidence:** Medium-high as a *model*; inputs are planning-level.
- **Recommended action:** Keep controlling within scope. Reconcile program basis with S3 after test-fit (MB-02). Reclassify the "FACT" rent tag in any derived work.

### S3 — `sources/current/South_Andrews_8M_Construction_Feasibility.xlsx`
- **Format / size / dates:** XLSX, 35.7 KB; file modified 2026-07-26. 8 sheets: Assumptions, Program & Massing, Construction Budget, Energy & Mobility, Financing & Returns, Sensitivity, Sources, Executive Dashboard. No hidden sheets; no external links; formula-driven; includes internal source register with URLs.
- **Purpose:** Construction feasibility at $8.0M land on the Native Realty massing basis (28,000 SF ground/parking plate, 24,000 SF office plate), with core-vs-tenant-ready cost split and partner-gap framing.
- **Provenance:** Owner/AI session model; title "SOUTH ANDREWS HEALTHCARE & MOBILITY HUB — CONSTRUCTION FEASIBILITY" (uses the current project name).
- **Authority:** Controlling tier 4. Scope: construction feasibility at its stated program basis.
- **Content summary:** 6-story = 231 stalls / 40,800 RSF office; 8-story = 308 stalls / 61,200 RSF. Core all-in $59.54M / $76.19M; tenant-ready $69.46M / $90.48M. NOI $2.278M / $3.099M at $50/RSF office rent. Core yield on cost 3.83% / 4.07% vs 7.0% target ⇒ **annual partner/grant/master-lease gap $1.89M / $2.23M (core), $2.58M / $3.23M (tenant-ready)**; value gap −$28.1M to −$47.7M at 7.25% cap. 40 L2 ports installed, 80/120 EV-ready, DCFC stub-outs only; solar 150/200 kW, BESS 500/1000 kWh; **zero tax credits underwritten** (30C placed-in-service deadline 6/30/2026; §48E changed). Land sensitivity $8.0M/$8.75M/$9.5M. Explicit disclaimer: "Preliminary feasibility model only."
- **Dependencies:** S6 (appraisal facts), S8 (plates, offer strategy), S5 (program logic), `South_Andrews_Electrical_Load_Model.xlsx` (**missing**, MA-11), WGI/DOE/NREL-cited benchmarks, IRS pages, Waymo/Zoox/Tesla/Freebee pages (context only).
- **Conflicts:** Program basis and inputs vs S2.
- **Integrity notes:** (a) Best-documented model in the repo — its `Sources` sheet is a model for provenance. (b) "NLR Solar" / nlr.gov citation appears to be a mis-typed NREL reference — flag, do not rely on the URL. (c) Formulas traced; internally consistent; the ROUNDDOWN stall method is intentionally more conservative than S8's 340 SF/stall.
- **Confidence:** Medium-high as a model; inputs planning-level.
- **Recommended action:** Keep controlling within scope. Recover MA-11. Treat its no-credit tax position and S2's 30%-ITC position as an escalated conflict (OQ-17).

### S4 — `sources/current/Andrews ODP with Dashboard.docx`
- **Format / size / dates:** DOCX, 58.8 KB; file modified 2026-06-26; internal: "Version 1.0 · Status: Governing," issued prior to Schematic Design.
- **Purpose:** Owner's Development Program — governing manual translating research into decisions (program, principles, phasing, risks, open questions OQ-01…OQ-13).
- **Provenance:** "Prepared by the Owner's Representative for the Investment Committee."
- **Authority:** Current but subordinate (SOURCE_AUTHORITY.md): institutional program logic and project requirements only; may not override corrected assumptions, newer models, or owner decisions.
- **Content summary:** Uses the **historical name** "South Andrews Clinical & Mobility Center" and address form 901–915. Healthcare-anchored, parking-enabled thesis; convertible CIP flat-plate podium (12-ft floor-to-floor, 100 psf, external removable ramps, universal grid); medtail ground floor; medical co-working master tenant; phasing (P1 parking+medtail, P2 clinical/co-working, P3+ optionality); zoning table (RAC-RPO, 110 ft/~10 stories by right, 150 ft via bonuses, 50 du/ac, no max FAR, 0-ft build-to, 1/250 parking); risk register R-1…R-12; permanent design principles (Ch.13); explicitly surfaces the thesis conflict (OQ-01) and the appraisal branding item (OQ-12); declares subordination to a Project Constitution and Decision Log **not present in the repo**.
- **Dependencies:** The five-report research library, Constitution, Decision Log — all missing (MA-01…MA-09, MA-12).
- **Conflicts:** Project name and address form vs AGENTS.md; "110 ft by right" framing vs the >6-story discretionary-review reading (S1, S8); program areas intentionally TBD vs the sized programs in S2/S3.
- **Integrity notes:** Internally consistent and disciplined (FACT/ASSUMPTION/FORECAST/JUDGMENT tagging), but its evidentiary base is largely the missing research library, so many of its FACTs are one-remove citations.
- **Confidence:** High for program logic and requirements; medium for any specific figure.
- **Recommended action:** Keep as subordinate context. A future ODP v2 should be regenerated from the ratified canon under the current project name (see [Document Update Order](Document%20Update%20Order.md)).

## sources/legacy/

### S5 — `sources/legacy/Institutional Development Prospectus Vol0.docx`
- **Format / size / dates:** DOCX, ~1.0 MB (embedded imagery); file modified 2026-06-26.
- **Purpose:** Legacy external narrative (Vol 0 executive brief) for the "South Andrews Clinical & Mobility Center."
- **Provenance:** Ownership-branded partner brief; governed by ODP Vol 1.
- **Authority:** Legacy narrative — structure, tone, and re-verified evidence only (SOURCE_AUTHORITY.md). Naming, program, figures, conclusions **not controlling**.
- **Content summary:** Healthcare-gateway vision; three demand drivers (parking deficit, clinical spillover, medtail niche); Broward Health expansion (188,000 SF MOB opening 2027; GME 365 residents; 18,000+ FTE statewide physician shortage); deliberately states no return targets and no program areas ("sized during design, not before"); discloses near-term MOB softening; labels renderings illustrative.
- **Dependencies:** ODP (S4); the missing research library at one further remove.
- **Conflicts:** Historical project name; otherwise deliberately unquantified.
- **Integrity notes:** Notably disciplined for a marketing document (explicit return-related disclosure; "we have chosen not to estimate" economic impact).
- **Confidence:** N/A as evidence; useful as structure/tone precedent.
- **Recommended action:** Keep in legacy untouched. Reuse its disclosure patterns in any future prospectus; never its name or unverified figures. **Never use it merely because it is more polished** (CLAUDE.md rule).

## sources/reference/

### S6 — `sources/reference/Andrew’s Appraisal.pdf`
- **Format / size / dates:** PDF, 2.4 MB, 56 pages; effective value date 2025-09-18; report date 2025-09-25. Appraiser: AEI (AEI Files/CoStar/PwC data; AEI pre-survey questionnaire).
- **Purpose:** Fee-simple as-is market value of the subject land.
- **Provenance:** Seller/lender-side appraisal. Branded **"Agora Mediterranean Market"** — the seller's own retail/restaurant redevelopment concept name for the property ("the owner intends to modernize/develop into a retail/restaurant center," p.1).
- **Authority:** Third-party reference within appraisal scope only. Never the sole authority for a planning decision.
- **Content summary:** Subject 917 S Andrews Ave (assemblage 901–917), folio 50-42-15-01-0711, legal description LAUDERDALE 2-9 D LOT 1 W1/2 & LOTS 2-4, 32-35 + vacated alleys; owner Highlands Equity Investments LLC; 38,207 SF / 0.8771 ac, 100% usable per ALTA survey; corner, 275 ft / 170 ft frontages; RAC-RPO; FEMA Zone AE entire site (map 12011C0557J, 7/31/2024); moderate slopes; no known adverse encumbrances (assumption); 2024 assessment $1,894,400, taxes $39,268. HBU as vacant and improved: **Mixed-Use** redevelopment; existing buildings interim use. Value: land-sales comparison only (cost/income N/A), 4 comps within 1 mile ($226–$664/SF; two small S Andrews lots incl. condemnation-negotiation and hospital-assemblage sales; two superior RAC-CC downtown sites), conclusion **$11,100,000 ($290/SF)**; exposure/marketing 12 months; owner operating statements and related-party leases rejected as evidence; previously listed $12.0M, not currently listed.
- **Dependencies:** Ibarra 2015 boundary survey (missing, MA-10); Phase I/II ESAs (missing, MA-13); Highland Contractors estimate (missing, MA-14); AEI Zoning Report (missing, MA-15).
- **Conflicts:** $11.1M vs $8.0M working offer (documented critique in S1 §4 and S8 p.7); its "Agora" branding vs project identity (resolved factually — same folio and legal description; see [Contradictions Matrix](Contradictions%20Matrix.md) row C-1e).
- **Integrity notes:** Minor typos ("Sale 1 2/3/205," template artifacts "[stable/moderate growth/declining]" left unfilled on p.20–21) — cosmetic, but evidence of template production; does not change the value conclusion's status as a third-party opinion.
- **Confidence:** High for site facts; the value conclusion is an **appraisal opinion**, not a verified market-clearing price.
- **Recommended action:** Keep as reference. Preserve filename (curly apostrophe) until owner authorizes renaming (SOURCE_AUTHORITY.md).

### S7 — `sources/reference/Appraisal Valuation .xlsx`
- **Format / size / dates:** XLSX, 69.6 KB; file modified 2026-06-25. 15 sheets (Cover, IC Tear Sheet, Feasibility Dashboard, Assumptions, Source Document Register, Evidence Map, Residual Land Value, Land Value Reality Check, Negotiation Waterfall, Buildable Area, Residual Value Curve, Rate Destruction Map, Constraint Scorecard, Tornado Sensitivity, Mobility Hub Economics). Named-range driven; scenario toggle (Conservative/Base/Aggressive); no hidden sheets.
- **Purpose:** Analyst IC workbook testing whether $11.1M is supported by development economics (residual land value method).
- **Provenance:** Analyst-prepared ("Institutional Underwriting Workbook & Investment Committee Package"); own internal source register and evidence map.
- **Authority:** Third-party/analyst reference. Its *method* is useful; its multifamily program is **not** the project program.
- **Content summary (Base scenario values):** FAR-6 multifamily program (229,242 GSF, 246 units, 271 stalls); total dev cost ex-land $95.0M; stabilized value $120.6M at 5.35% cap; **supported land value $8.96M ($234/SF), 80.7% coverage of the appraisal → verdict "CAUTION — NEGOTIATE."** Mobility Hub module (200 transient / 100 fleet / 50 EV "per brief"): NOI $1.07M, capitalized $14.3M at 7.5%, hub residual land value **$0.81M** — i.e., a pure hub program supports almost no land value. Explicit address/parcel reconciliation note (917 vs 901-903-915 vs 901 treated as same assemblage; confirm with title).
- **Dependencies:** S6, Ibarra survey (missing), a "project brief" (unidentified — possibly MA-12/MA-17 era).
- **Conflicts:** Its residual method prices a *different* (multifamily) program; its cap rates and costs differ from S2/S3 by design.
- **Integrity notes:** (a) `Cover!C16` expands RAC-RPO as "Residential Permitted Overlay" — **incorrect**; the district is "Residential and Professional Office" (S6 zoning section). (b) Evidence Map discipline (✓ vs Analyst) is exemplary. (c) Formulas traced; verdict is formula-driven, not hardcoded.
- **Confidence:** Medium; scenario-dependent by construction.
- **Recommended action:** Keep as reference for negotiation analytics. Preserve filename (trailing space before `.xlsx`) until owner authorizes renaming.

### S8 — `sources/reference/NativeRealty_905 S Andrews - Development Feasibility & Massing Study.pdf`
- **Format / size / dates:** PDF, 484 KB, 9 pages; prepared June 2026 by Michelle Speroni, Native Realty (buyer representation); file modified 2026-07-25.
- **Purpose:** Buyer-side feasibility, massing, zoning, and valuation study; offer strategy.
- **Provenance:** Buyer's broker. **Important scope note:** written for a **car-rental-operator client thesis** ("The South Andrews Mobility Hub"; "for a car rental operator, it is rare"), not the healthcare-anchored program.
- **Authority:** Third-party reference within its buyer-representation scope. Its zoning read and offer strategy are usable context; its rental-fleet program is **not** the project program.
- **Content summary:** Site: 3 parcels, one owner (Highlands Equity Investments LLC), one folio; 275/170 ft frontages; Hardy Park north; 1959-era buildings (Marty's Bar & Grill + two) as interim use; FLL 2.8 mi, Brightline 1.8 mi, I-95 1.5 mi. Zoning RAC-RPO: up to 12 stories; >6 stories = enhanced Level III site plan & design review (discretionary, not prohibition); 50 du/net acre; 1/250 parking; form-based envelope, no single FAR — confirm at pre-application. Standalone garage/rental is not an enumerated principal use → structure as accessory parking to a permitted principal use. Massing: ~28,000 SF efficient plate, ~340 SF/stall ≈ 82 stalls/level; Scenario A Mobility Hub 9 stories, ~575–600 stalls, 24,000 SF office cap, ~229,500 SF total; Scenario B residential (~43 units, ~245 stalls); Scenario C hotel (~130 keys, ~330 stalls). Valuation: appraisal comps critiqued (condemnation threat, hospital assemblage, superior RAC-CC zoning); **open at $8.0M ($209/SF), room to ~$8.75M; defensible range $7.65–9.0M ($200–235/SF)**; at $8.0M land ≈16% of a $45–50M project. Next steps: offer → pre-application during feasibility → obtain existing Phase I/II ESAs → architect test fit. Full disclaimer: planning-level, not an appraisal/zoning determination.
- **Dependencies:** S6 (cited: AEI appraisal 9/25/2025), Broward County Property Appraiser, ULDR §47-13, SRAC master plan.
- **Conflicts:** Rental-fleet framing vs healthcare anchor (AGENTS.md scope: project is not rental-car-led); its $45–50M project cost context vs S2/S3's $59–95M totals (different programs); filename says "905" while text says 901–917.
- **Integrity notes:** Filename address ("905") does not match report text (901–917) — treat text as controlling within the document.
- **Confidence:** Medium-high for zoning process and negotiation logic; program is client-specific context.
- **Recommended action:** Keep as reference. Adopt its zoning-process read (pending MB-01 verification) and offer rationale; never adopt its rental-fleet narrative.

## sources/raw/
- Empty (`.gitkeep` only). **Observed fact.** Intended for unprocessed intake per repo conventions; transaction paper (MA-18) and recovered documents should land here first.

## Governance & skills (context, not sources)
- `AGENTS.md` — operating contract; source hierarchy; current identity/scope. **The repository's operative constitution.**
- `CLAUDE.md` — Claude working rules (inventory before synthesis; conflict table before drafting; no legacy narrative merely for polish).
- `docs/governance/SOURCE_AUTHORITY.md`, `PROJECT_GLOSSARY.md`, `CLAIMS_AND_EVIDENCE_POLICY.md`, `WORKFLOW.md`.
- `skills/source-reconciliation/SKILL.md`, `skills/financial-model-audit/SKILL.md`, `skills/institutional-prospectus/SKILL.md`.

---

## Organization issues and Phase 1 treatment
1. Two filenames deviate from clean conventions and are **intentionally preserved** pending owner authorization: `Andrew’s Appraisal.pdf` (curly apostrophe), `Appraisal Valuation .xlsx` (trailing space).
2. `NativeRealty_905 …` filename address conflicts with document text (901–917).
3. `.DS_Store` artifacts are ignored under Phase 1; the tracked `sources/.DS_Store` artifact was removed from the repository index. No evidence source was removed.
4. The ODP and 6v8 Model cite a governing layer and research library absent from the repository. D-P9 makes current governance operative while the missing layer remains tracked for recovery.
5. `derived/workbooks/` and `derived/documents/` now establish generated-work boundaries. No derived extraction supersedes an original.
