# Implementation Report — Integrated Development Plan

**Date:** 2026-07-27 · **Phase:** Planning synthesis and integrated development analysis
**External-use status:** internal_only
**Preceded by:** [Implementation Report 2026-07-26](IMPLEMENTATION_REPORT_2026-07-26.md)

---

## 1. Assignment and outcome

The assignment was to synthesise the complete project record into one defensible development plan — reconciled program, construction budget, electrical basis of design, entitlement pathway, phasing, operating model, and financial feasibility — and then produce the institutional prospectus downstream of it.

**Outcome:** the integrated plan is complete. The prospectus was produced as a **release candidate that is blocked for external use**, because both [`skills/institutional-prospectus/SKILL.md`](../skills/institutional-prospectus/SKILL.md) and [Document Update Order](planning/Document%20Update%20Order.md) Step 8 order a stop while material conflicts remain unresolved — and this pass added seven new ones to the four already open. The blocker is documented rather than worked around.

**The controlling finding:** the development program does not support the land at any price, including zero. This is new. Prior work established a yield gap; this pass establishes that the gap is not curable by the acquisition price.

## 2. Files created

| Path | Class |
|---|---|
| `docs/planning/Integrated Development Source Map.md` | planning record |
| `docs/planning/Contradiction and Validation Register.md` | operative register (CVR-01…53, OQ-24…30) |
| `docs/planning/Program and Scenario Reconciliation.md` | scenario comparison (SA-A…SA-D8) |
| `docs/planning/Final Development Planning Brief.md` | planning synthesis |
| `docs/cost/Construction Budget Basis.md` | cost basis (AACE Class 5) |
| `docs/technical/Electrical Basis of Design.md` | technical basis |
| `docs/technical/Entitlement and Utility Roadmap.md` | approval pathway |
| `docs/technical/Two-Site Operating Plan.md` | operating concept |
| `docs/investment/Integrated Development Recommendation.md` | owner decision document |
| `docs/external/Institutional Development Prospectus.md` | **release candidate — BLOCKED for external use** |
| `docs/external/One-Page Project Summary.md` | **BLOCKED for external use** |
| `models/working/build_integrated_development_model.py` | derived model (noncanonical) |
| `models/working/South_Andrews_Integrated_Development_Model.xlsx` | derived workbook |
| `models/working/integrated-development-model.json` | derived structured data |
| `docs/IMPLEMENTATION_REPORT_2026-07-27.md` | this report |

## 3. Files modified

| Path | Change |
|---|---|
| `docs/planning/Open Questions.md` | Added Part 3: OQ-24…OQ-30. Added revised priority note |
| `docs/planning/Risk Register.md` | Added Part 3: R-21…R-25. Noted R-21 supersedes R-13 as the governing economic risk |
| `docs/planning/Contradictions Matrix.md` | **Corrected** S3 8-storey GBA from 208,000 to 212,000 SF, with correction note |
| `docs/planning/Master Assumption Register.md` | Same correction to PRG-04. Added §12 with 15 new assumptions (CAP-01…04, NRG-11…15, CST-25/26, FIN-06…08, ACQ-10) |
| `docs/investment/Institutional Investment Memorandum.md` | Extended §1.3 and §16.3 with the residual-land finding; added §16.4 scenario extension; updated §25.4 cross-reference |
| `scripts/validate_repository.py` | Added integrated-package controls (49 new checks) |

## 4. Source files preserved

**No original source file was modified, moved, renamed, or deleted.** All eight registered SHA-256 digests match `exports/source-register.json`, and `git status sources/` is clean.

| ID | SHA-256 (first 16) | Verified |
|---|---|---|
| S1 Corrected Assumptions | `b1aa5c31af384cc6` | ✓ |
| S2 6v8 Story Model | `ee5146a7cd1495aa` | ✓ |
| S3 8M Construction Feasibility | `0d9299f93013c455` | ✓ |
| S4 ODP with Dashboard | `a336c00a9471efb8` | ✓ |
| S5 Legacy Prospectus | `28ed83d76f8b5cf0` | ✓ |
| S6 Appraisal | `4adea2b61b43e28d` | ✓ |
| S7 Appraisal Valuation | `176676736467606f` | ✓ |
| S8 Native Realty | `c2ce97c4948be7e5` | ✓ |

Workbooks were opened read-only at cell level (formula and cached value, every sheet). PDFs and DOCX were text- and table-extracted. Extraction artefacts were written to the session scratchpad, outside the repository.

## 5. Major decisions taken in analysis

| Decision | Rationale |
|---|---|
| Use **Basis B** as the stated geometric basis for new scenarios | It derives from the only third-party massing study (S8) and uses the more conservative stall efficiency. Declared as a stated basis, **not** an adopted program; OQ-14 remains open and Basis A restatement is a required test-fit output |
| Adopt the electrical workbook's **method**, reject its **conclusions** | Its ampacity formula, energy-first fleet method, charging-window sensitivity and canopy solar cost are sound. Its program (55,000 SF on-site depot), area basis (internally inconsistent by 11,000 SF), battery-as-service-reduction, and 30% solar ITC are not |
| Do **not** copy the electrical workbook into `sources/` | Admitting a source is an owner act under `AGENTS.md` change discipline, and the file's provenance is unestablished. Escalated as OQ-29 |
| Report **two parking constructs** (P1 code-constrained, P2 as-modelled) rather than choosing | The conflict between S3's monetised parking and the City's 1-per-250-GFA standard is unresolved (OQ-26). Choosing either alone would overstate or understate. Both are reported everywhere |
| Carry a **$250,000 environmental remediation allowance** | A Phase I *and* Phase II are referenced by S6 p.10 but absent. A placeholder against an unknown, flagged as very low confidence |
| Produce the prospectus **blocked** rather than not at all | The assignment directs documenting blockers and continuing work that does not depend on them. The narrative is useful to ownership; releasing it would breach the publication gate |
| Add **49 validator checks** rather than a separate script | `scripts/README.md` establishes one validator. Extending it keeps a single control surface |

## 6. Findings

### 6.1 New and material

1. **Residual land value is negative under every tested program.** At a zero land basis no scenario exceeds 4.49% yield on cost. Break-even office rent on the leading scheme is ~$131/RSF against $50 modelled. → R-21
2. **Gross stalls are not fleet capacity.** The maximum-fleet scheme yields ~140 operational positions, not 300–400. The leading balanced scheme carries a **one-stall deficit** against its own code requirement. → R-22, CAP-02/03
3. **S3's $419,265/yr parking revenue is in tension with code-required parking.** Swings 6-storey yield on cost by ~45 bps. → OQ-26, R-23
4. **The two-site strategy is worth ~$3M in avoided electrical capital** and moves the site off medium-voltage service (3,208 kW → 1,143 kW).
5. **A Phase II ESA is referenced but absent.** Normally commissioned only after a Phase I identifies a condition. → OQ-28, R-24
6. **The electrical model is ungoverned**, sits outside the repository in two byte-identical copies, and its original does not exist. → OQ-29, R-25
7. **Clinical load density conflicts 2.5×** between S3 (5 W/GSF) and the electrical workbook (12.6 W/GSF demand). → OQ-24
8. **Utility service allowance now spans 6.7×** ($750K–$5.0M) across three sources. → OQ-25
9. **The accessory-parking argument cites no ULDR provision** — it is the load-bearing entitlement theory for any parking-heavy scheme. → OQ-27
10. **North Broward Hospital bought both closest comparables** in Jan–Feb 2025, one under condemnation threat. The prospective anchor is an active assembler on this street. → ACQ-10
11. **The RAC-RPO density cap (50 du/net acre ≈ 43 units) makes the site structurally unlike its own high comparables**, which were RAC-CC tower sites. → CVR-53

### 6.2 Corrections to the existing record

| Correction | Detail |
|---|---|
| **S3 8-storey GBA** | Recorded as 208,000 SF in two registers; `Program & Massing!D17` evaluates to **212,000 GSF**. Corrected in both |
| **S2 retail vacancy formula** | `Operating!B5` applies the *office* vacancy input to retail income (~$5,300/yr). Immaterial; evidences that S2 was not independently checked |
| **S2 non-recoverable opex** | `Assumptions!B65` is labelled "$/SF GBA" but `Operating!B14` omits 105,000–140,000 SF of parking GBA — understating opex by ~$157,500–$210,000/yr |
| **No design contingency** | Neither model carries one. A Class 5 estimate normally would, in addition to construction contingency |
| **FPL demand charges unmodelled** | Both models carry only a $0.13/kWh energy assumption. Plausibly a six-figure annual omission |

### 6.3 Files named in the assignment that do not exist

`Andrew's Site Analysis.txt` · `Andrews Context.md.pages` · `901 S Andrew's Ave Fort Lauderdale, FL 33316.pdf` · `Heldy_SAndrewsOffer.pdf` · the *original* `South_Andrews_Electrical_Load_Model.xlsx`.

**The absence of any offer document is material**: there is no documentary evidence that any offer has been made, consistent with CAN-003.

## 7. Unresolved questions

Carried forward: OQ-02…OQ-11, OQ-13, OQ-14, OQ-15, OQ-16, OQ-17, OQ-18, OQ-20, OQ-21, OQ-22.
Added: **OQ-24** clinical load density · **OQ-25** utility service allowance · **OQ-26** parking monetisation · **OQ-27** accessory-parking limit · **OQ-28** environmental condition · **OQ-29** electrical-model provenance · **OQ-30** Live Local applicability.

Nothing was silently resolved, averaged, or dropped.

## 8. Validation results

```
python3 scripts/validate_repository.py
Checks run: 174   Errors: 0   Warnings: 0
```

Up from 125 checks. The 49 additions cover the integrated package's internal-only status, ownership and promotional language, unsupported-approval implications, property-status disclosure, prospectus release blocking, preservation of the negative feasibility finding, scenario-basis discipline, and derived-model integrity including zero AV revenue in every base case.

**The new checks caught two real defects during development** — a gate question phrased as though FPL capacity were confirmed, and a property-status sentence that did not use the canonical phrasing. Both were corrected rather than the checks weakened.

Independently verified:

- All eight source SHA-256 digests match; `git status sources/` clean
- The derived model reproduces S3 `Financing & Returns!D17` ($2,277,951) to within $107 on S3's own parking construct with AV re-added, and the repository's independent OQ-22 ex-AV recomputation ($2,151,591) to within $107
- The `k`-factor financing method reproduces S3 `Construction Budget!D56` and `E56` exactly
- All internal Markdown links resolve (validator link check)
- No scenario metrics are mixed across program bases
- Gross stalls and operational fleet capacity are distinguished in every document

Not verified, and stated as such throughout: every unit cost, rent, cap rate, load density, service size, stall count, and entitlement parameter.

## 9. Governance position

- **No scheme adopted.** SA-A…SA-D are scenarios; the recommendation is a recommendation.
- **This is not model vNext.** Document Update Order Step 5 and its gates (D-P5, D-P6, D-P7) are untouched.
- **External publication remains blocked.** Step 8 gates are unmet.
- **AV revenue excluded from every base case** (CAN-012); tax credits at 0% (OQ-17 interim rule).
- **$8,000,000 treated throughout as the D-P1 acquisition-strategy input only** — not proof of value, not a price ceiling, walk-away price, or transaction authority.
- **All partners prospective.** No LOI, term sheet, or executed agreement exists with any party.
- **Nothing committed or pushed to version control.** No commit or push was made; authorisation was not given.

## 10. Recommended next actions

1. **Recover the existing Phase I and Phase II ESAs** (MA-13 / OQ-28). Days, nominal cost, and capable of stopping the transaction.
2. **Commission an FPL preliminary load letter** (MB-03 / OQ-25). Weeks, $5–10K, resolves a $750K–$5.0M budget line.
3. **Engage land-use counsel and request a City pre-application meeting** (MB-01). One engagement resolves OQ-03, OQ-26, OQ-27 and OQ-30 together.
4. **Set the underwriting standard** — target yield on cost, hurdle, exit cap basis (MA-06 / OQ-18). Without it, "does not clear" is an assertion rather than a measurement.
5. **Decide the transaction posture** — cash, option, ground lease, participation, or walk away (OQ-20) — informed by the finding that the program supports approximately $0–2M of land value.

Items 1–3 are sequenced first because they are the cheapest, the fastest, and the most likely to change the answer.
