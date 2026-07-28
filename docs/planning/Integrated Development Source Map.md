# Integrated Development Source Map

**Status:** Current operative source map for the integrated development plan · **Prepared:** 2026-07-27
**External-use status:** internal_only
**Governing documents:** `AGENTS.md`, [`docs/governance/SOURCE_AUTHORITY.md`](../governance/SOURCE_AUTHORITY.md), [`docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md`](../governance/CLAIMS_AND_EVIDENCE_POLICY.md)
**Related:** [Source Inventory](Source%20Inventory.md) · [Contradiction and Validation Register](Contradiction%20and%20Validation%20Register.md) · [Program and Scenario Reconciliation](Program%20and%20Scenario%20Reconciliation.md) · [Missing Research Register](Missing%20Research%20Register.md)

This map records what was inspected for the integrated development plan, what authority each source carries, and — importantly — which sources named in the assignment brief **do not exist**. It supplements rather than replaces [Source Inventory](Source%20Inventory.md), which remains the repository's canonical inventory.

---

## 1. Inspection method

Every workbook was opened read-only at cell level, with both the stored formula and the cached value captured for every populated cell across every sheet. Every PDF and DOCX was text- and table-extracted in full. No original source file was opened for write, moved, renamed, or modified. Source integrity was verified before and after by SHA-256 against `exports/source-register.json`; **all eight registered hashes match**, and `git status sources/` is clean.

Extraction artefacts are working files held outside the repository in the session scratchpad; the reproducible derived analysis is committed at [`models/working/build_integrated_development_model.py`](../../models/working/build_integrated_development_model.py).

## 2. Controlling sources inspected (integrity verified)

| ID | Source | Class | SHA-256 (first 16) | What it controls | What it does **not** control |
|---|---|---|---|---|---|
| S1 | `sources/current/South_Andrews_Corrected_Assumptions.md` | Current controlling | `b1aa5c31af384cc6` | Fact/opinion/hypothesis separation; the standing critique of the appraisal; the verified-vs-unverified entitlement list | Program areas, costs, rents. Contains no quantified program |
| S2 | `sources/current/South Andrews 6v8 Story Model.xlsx` | Current controlling | `ee5146a7cd1495aa` | Basis A program (35,000 SF uniform plate); its own cost/revenue inputs; 10-year unlevered return construct | Height entitlement (its "by-right 110 ft" note is contested); rent (its `$36/RSF` is mis-tagged FACT) |
| S3 | `sources/current/South_Andrews_8M_Construction_Feasibility.xlsx` | Current controlling | `0d9299f93013c455` | Basis B program (28,000/24,000 SF plates); granular cost architecture; tax-credit treatment; energy planning loads | Parking revenue realisability (see CVR-31); its base NOI contains prohibited AV revenue |
| S4 | `sources/current/Andrews ODP with Dashboard.docx` | Current, subordinate | `a336c00a9471efb8` | Institutional program logic, design standards intent, risk framing | Any figure that conflicts with S1–S3; its governance precedence table is superseded by D-P9 |
| S5 | `sources/legacy/Institutional Development Prospectus Vol0.docx` | Legacy | `28ed83d76f8b5cf0` | Structure and tone reference only | Naming, program, figures, conclusions |
| S6 | `sources/reference/Andrew’s Appraisal.pdf` | Third-party reference | `4adea2b61b43e28d` | Site facts (area, frontage, folio, flood, zoning district, taxes); the $11.1M fee-simple opinion at 2025-09-18 | Office/medical rents, medical demand, cap rates for this program — **it contains none.** Its market section is entirely retail |
| S7 | `sources/reference/Appraisal Valuation .xlsx` | Third-party reference | `176676736467606f` | Analyst residual/negotiation context | Project program or value. Its RAC-RPO expansion is wrong; its programs differ from ours |
| S8 | `sources/reference/NativeRealty_905 S Andrews - Development Feasibility & Massing Study.pdf` | Third-party reference | `c2ce97c4948be7e5` | The only third-party massing basis (28,000 SF plate, ~340 SF/stall); the accessory-parking use pathway; the $8.0M offer strategy | Entitlement certainty. Buy-side advocacy, June 2026, expressly "not a zoning determination." Its own "Honest Read" concedes discretionary approval |

## 3. Sources named in the assignment brief that **do not exist**

Searched across the repository, `~/Documents`, `~/Downloads`, and `~/Desktop`.

| Named in brief | Search result | Treatment |
|---|---|---|
| `Andrew's Site Analysis.txt` | **Not found anywhere.** Cited by S2 `Assumptions!E7,E56` as the basis for parcel records and the parking pricing survey | Register as missing; the parking-pricing input it supports has no traceable basis (MA-16) |
| `Andrews Context.md.pages` / `Andrews_Context.md` | **Not found anywhere.** Cited by S4 Table 24 as the "Mobility Nexus" thesis text | Already tracked as MA-12; classified rejected scenario per D-P2 |
| `901 S Andrew's Ave Fort Lauderdale, FL 33316.pdf` | **Not found anywhere** | Register as missing; content unknown, so no claim may rest on it |
| `Heldy_SAndrewsOffer.pdf` | **Not found anywhere.** No offer or LOI paper exists in the repository | Material: there is **no documentary evidence of any offer having been made**. Consistent with CAN-003 (prospective acquisition) and MA-18 |
| `Institutional Development Prospectus Vol0.docx` | Found at `sources/legacy/` | Legacy only |
| `Appraisal Valuation .xlsx` | Found at `sources/reference/` (note the trailing space in the filename — preserved) | Reference only |
| `South_Andrews_Electrical_Load_Model.xlsx` | **The original is not found.** Two *corrected* versions exist outside the repository — see §4 | See §4; MA-11 remains open |

## 4. The electrical load model — an uncontrolled external file

This is the most significant source-integrity finding of the engagement.

| Item | Finding |
|---|---|
| Location | `~/Downloads/South_Andrews_Electrical_Load_Model_CORRECTED.xlsx` and `…_CORRECTED_1.xlsx` |
| Repository status | **Neither file is in `sources/`.** Neither is registered, hashed, or governed |
| Relationship | Both files are **byte-identical** (SHA-256 `f7cfe13a6b33ac7095a596aa2d01a6d27197c8c23cbb8c96e9dba1861994b400`). `_1` is a duplicate download, not a later revision |
| The *original* it corrects | Not present in any searched location. The "Uploaded" column in its `Reconciliation` sheet is the only surviving evidence of the original's contents |
| Authority | **None.** It is not an owner decision, not a controlling source, not a registered reference. It is an analyst working file |
| Why it still matters | S3 `Sources!A8` cites "South Andrews Electrical Load Model" as the basis for its 9.6 kW/port and 1,500 kWh/kW-yr factors. Those figures currently trace to a file the repository cannot inspect |

**Handling adopted for this plan.** The workbook was inspected read-only in place and its *method* was audited and partially adopted (see [Electrical Basis of Design](../technical/Electrical%20Basis%20of%20Design.md)). Its *program assumptions* were **not** adopted, because they describe a building this project has not chosen to build (§5 below). It was **not** copied into `sources/`: admitting a source is an owner act under `AGENTS.md` change discipline, and the file's own provenance is unestablished. Recommended owner action is at [Contradiction and Validation Register](Contradiction%20and%20Validation%20Register.md) CVR-01.

## 5. The electrical model describes a third program basis

The corrected electrical workbook is built on a program that matches **neither** live basis:

| Element | S2 (Basis A) | S3 (Basis B) | Corrected electrical workbook |
|---|---|---|---|
| Stated total area | 210,000 / 280,000 GSF | 160,000 / 212,000 GSF | "216,000 SF GBA" (`Reconciliation!C5`) |
| Area inputs actually used | — | — | 35,000 office + 10,000 med-tail + 55,000 depot + 105,000 parking = **205,000 SF** |
| On-site fleet depot | None | None | **55,000 SF, 120 vehicles, ~1,444 kW managed** |
| Office/clinical area | 70,000 / 105,000 GSF | 48,000 / 72,000 GSF | **35,000 SF (one floor)** |
| Public DCFC | 8 units | 0 installed (stub-outs) | **8 units / 1,200 kW connected** |

Three defects follow, all confirmed by direct cell inspection:

1. **Internal inconsistency.** Its own stated 216,000 SF GBA does not reconcile with the 205,000 SF its `Inputs` sheet actually sums. An 11,000 SF discrepancy sits inside its own reconciliation tab.
2. **Understated clinical area.** It models 35,000 SF of office/clinical. Under either live basis the 6-storey scheme carries 48,000–70,000 GSF of office. The building load is therefore understated even as the charging load is overstated for a two-site strategy.
3. **A program the project has not adopted.** The 55,000 SF on-site depot is the single largest load in the model and is the exact function the two-site strategy relocates. Adopting this workbook's service conclusion would size South Andrews for a building the owner is being advised not to build.

## 6. Derived artefacts produced by this engagement

| Artefact | Path | Class | SHA-256 (first 16) |
|---|---|---|---|
| Integrated development model (script) | [`models/working/build_integrated_development_model.py`](../../models/working/build_integrated_development_model.py) | model output — noncanonical working model | — |
| Integrated development model (workbook) | `models/working/South_Andrews_Integrated_Development_Model.xlsx` | model output | `59211d3bcce5ab23` |
| Integrated development model (structured data) | `models/working/integrated-development-model.json` | model output | `e560ca82531042d3` |

These are **not** the gated "model vNext" of [Document Update Order](Document%20Update%20Order.md) Step 5. They do not resolve OQ-14, OQ-15, OQ-17 or OQ-18; they declare a stated basis for each and report the alternative alongside. The model reproduces S3 `Financing & Returns!D17` ($2,277,951) to within $107 when run on S3's own parking construct with AV revenue re-added, which establishes that the derivation is faithful to the controlling workbook before any analyst judgment is applied.

## 7. Source hierarchy applied

Applied in the `AGENTS.md` order, with scope discipline:

1. **Explicit current owner decisions** — D-P1, D-P2, D-P8, D-P9, D-P11, D-P12
2. **S1** Corrected Assumptions — within its fact/opinion/hypothesis scope
3. **S2** 6v8 Model — Basis A program and its own inputs
4. **S3** 8M Feasibility — Basis B program and its own inputs
5. **S4** ODP — institutional program logic only
6. **Verified primary sources** — none newly available this cycle
7. **S6/S7/S8** third-party references — each within its professional scope
8. **S5** legacy prospectus — structure and tone only

Higher tier does not confer authority outside scope. S2 outranks S3 by tier, but S3's plate basis derives from the only third-party massing study, which is why OQ-14 remains escalated rather than resolved by hierarchy alone.

## 8. Evidence classification of the principal inputs to this plan

| Input | Classification | Note |
|---|---|---|
| Site area 38,207 SF; frontages 275 ft / 170 ft; folio; Zone AE | verified fact | Strongest corroboration in the repository (S6 + S8 + S1) |
| RAC-RPO district; 1 space per 250 SF GFA; 50 du/net acre | source-derived but not independently verified | S6 zoning fields; City determination outstanding (MB-01) |
| "Above 6 floors and up to 12 floors … shall be reviewed" | source-derived but not independently verified | S6 p.37, and the quoted field is **truncated mid-word** in the source PDF |
| "Level III" review designation | source-derived but not independently verified | Appears **only** in S8; no ULDR text is quoted anywhere in the repository |
| $11,100,000 appraised value | source-derived (third-party opinion) | Never a market-clearing fact; standing critique at S1 §4 |
| $8,000,000 land input | current working assumption | D-P1 acquisition-strategy input only; not proof of value, not a ceiling, walk-away price, or transaction authority |
| All unit costs, rents, cap rates | current working assumption | No GC pricing, no lease comps, no broker survey in the repository |
| All stall counts, GBA, service sizes | model output | Basis-dependent; test-fit and FPL study outstanding |
| Every partner organisation | prospective | No LOI, term sheet, or executed agreement exists in the repository |

## 9. Consequences for this plan

- Two program bases remain live and are never mixed. Every quantitative statement in this package names its basis.
- The electrical conclusion is rebuilt from method, not inherited from the uncontrolled workbook's program.
- No entitlement, utility, demand, partner, or return claim in this package is stated as settled.
- The absence of any offer document confirms the property status: **prospective acquisition; the sponsor does not currently own the property.**
