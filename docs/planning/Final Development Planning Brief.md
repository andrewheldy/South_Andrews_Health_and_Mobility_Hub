# Final Development Planning Brief

**Status:** Integrated planning synthesis for owner review · **Prepared:** 2026-07-27
**External-use status:** internal_only
**Governing documents:** `AGENTS.md`, [`docs/governance/SOURCE_AUTHORITY.md`](../governance/SOURCE_AUTHORITY.md), [`docs/governance/WORKFLOW.md`](../governance/WORKFLOW.md)
**Related:** [Integrated Development Recommendation](../investment/Integrated%20Development%20Recommendation.md) — the decision document · [Project Canon](Project%20Canon.md) · [Contradiction and Validation Register](Contradiction%20and%20Validation%20Register.md)

This brief is the connective tissue of the integrated development package: it states what was examined, what was concluded, and how the pieces constrain one another. The owner-level decision sits in [Integrated Development Recommendation](../investment/Integrated%20Development%20Recommendation.md).

---

## 1. The package

| Document | Question it answers |
|---|---|
| [Integrated Development Source Map](Integrated%20Development%20Source%20Map.md) | What was inspected, what authority it carries, and what does not exist |
| [Contradiction and Validation Register](Contradiction%20and%20Validation%20Register.md) | Where the evidence conflicts and which source governs |
| [Program and Scenario Reconciliation](Program%20and%20Scenario%20Reconciliation.md) | What can physically and operationally be built |
| [Construction Budget Basis](../cost/Construction%20Budget%20Basis.md) | What it costs, at what confidence, with what excluded |
| [Electrical Basis of Design](../technical/Electrical%20Basis%20of%20Design.md) | What service is required and what the load workbook actually says |
| [Entitlement and Utility Roadmap](../technical/Entitlement%20and%20Utility%20Roadmap.md) | What approvals are needed, in what order, with what risk |
| [Two-Site Operating Plan](../technical/Two-Site%20Operating%20Plan.md) | What belongs on South Andrews and what belongs elsewhere |
| [Integrated Development Recommendation](../investment/Integrated%20Development%20Recommendation.md) | What the owner should do |
| [`models/working/`](../../models/working/build_integrated_development_model.py) | The reproducible arithmetic behind all of it |

## 2. What was done

The repository was audited in the order required by [`docs/governance/WORKFLOW.md`](../governance/WORKFLOW.md). Every workbook was inspected at cell level — formula and cached value, every sheet. Every PDF and DOCX was extracted in full. Source integrity was verified by SHA-256 before and after; **all eight registered hashes match and `sources/` is unmodified.**

A derived model was then built that reproduces S3's published stabilised NOI to within $107 before any analyst judgment is applied, which establishes that the new analysis is faithful to the controlling workbook rather than a parallel invention.

**Four sources named in the assignment brief do not exist anywhere**, including any offer document — confirming that no transaction has been documented. The electrical load model exists only as an ungoverned file outside the repository, in two byte-identical copies.

## 3. The five findings that matter

### 3.1 The project does not fail on land price

Both current models already showed a 3.8–4.1% yield against a 7.0% target. Extending that to a residual land analysis shows why that gap cannot be negotiated away: **at a land basis of zero, no scheme exceeds 4.49% yield on cost.** Break-even office rent on the leading scheme is $131/RSF against $50 modelled. The maximum land price the program can support is approximately **$0–2M**, against an $8.0M working input.

### 3.2 Gross stalls are not fleet capacity, and the difference is decisive

Neither current model deducts the building's own code-required parking before reporting stalls. Applying the 1-per-250-GFA standard in evidence:

- The **maximum-fleet scheme** yields ~140 operational fleet positions, not the 300–400 contemplated.
- The **leading balanced scheme is one stall short of its own requirement** — it has no surplus parking, no monetisable parking, and no deck capacity for staging.

This second point is new, material, and unflattering to the leading hypothesis. It also means S3's $419,265 of annual parking revenue is in tension with the building's own code compliance (CVR-31 / OQ-26).

### 3.3 The two-site strategy is right, and it is worth about $3M in electrical capital alone

Moving depot functions off site reduces the required service from 3,208 kW to 1,143 kW — from medium-voltage primary to conventional 480 V secondary. That avoids owner-side transformers, a vault, medium-voltage switchgear, and roughly $1.1M of battery that exists largely to hold the medium-voltage case down. It also avoids housing vehicles at **$544,977 per operational fleet position**.

But no depot site exists, and roughly **$3.15M of mobility-specific budget would be stranded** without one.

### 3.4 The electrical workbook is sound in method and wrong in program

Its ampacity formula, energy-first fleet method, charging-window sensitivity, canopy solar cost and demand-charge warning are all correct and adopted. But it models a 55,000 SF on-site depot the project should not build, treats one floor plate as the entire clinical program, contains an 11,000 SF internal area inconsistency, subtracts battery capacity from the service size in a way no engineer can stamp, and reinstates a 30% solar tax credit the repository has already ruled out. **Its method was adopted; its conclusions were not.**

It also surfaces a genuine unresolved conflict: **clinical load density of 5 W/GSF (S3) against 12.6 W/GSF (workbook)** — a 2.5× difference driving the entire service size (OQ-24).

### 3.5 Entitlement risk and capital risk fall together

The height-review trigger sits above six storeys. The accessory-parking argument — the load-bearing legal theory for any parking-heavy scheme — is asserted in S8 without a single ULDR citation. Both risks decline as the scheme gets smaller, at the same time as the capital at risk declines and the marginal return on scale collapses to 2.12% for the 8-storey increment.

**The smallest defensible scheme is the best scheme on entitlement, on electrical, on capital at risk, and on marginal return simultaneously.** That convergence is the clearest signal in the analysis.

## 4. How the constraints interlock

| If this changes | Then this must change |
|---|---|
| Program basis resolved (OQ-14) | Every area, stall, cost and load figure restates |
| City refuses shared parking (OQ-26) | SA-B loses its parking revenue; yield falls ~45 bps; the case for SA-C strengthens further |
| Accessory-parking ratio capped (OQ-27) | SA-A becomes unpermittable; SA-C is unaffected |
| Clinical load density resolved at the higher figure (OQ-24) | Service size and FPL allowance rise; imaging becomes harder to add later |
| FPL capacity is constrained (OQ-25) | DC fast charging and imaging are both foreclosed; the deferral strategy becomes mandatory rather than prudent |
| Phase II ESA discloses a condition (OQ-28) | The $250K remediation allowance is wrong by an unknown margin; acquisition may stop |
| Live Local preempts density (OQ-30) | The entire alternative-use analysis reopens; residential becomes a serious contender |
| A health-system anchor signs | The single most powerful lever: $1.6–2.3M/yr of incremental NOI would change the answer |

## 5. Governance position of this package

- **No scheme is adopted.** SA-A through SA-D are scenarios; the recommendation is a recommendation.
- **Both program bases remain live.** OQ-14 is not resolved by this work. Every figure names its basis.
- **AV and fleet revenue are excluded from every base case** per CAN-012.
- **Solar and storage tax credits are underwritten at 0%** per the OQ-17 interim rule.
- **The $8,000,000 figure is treated throughout as the D-P1 acquisition-strategy input only** — not proof of value, not a price ceiling, walk-away price, or transaction authority.
- **Every partner organisation is prospective.** No LOI, term sheet, or executed agreement exists with any party.
- **No source file was modified.** Derived work is in `models/working/`, correctly classified as noncanonical.
- **This is not model vNext.** [Document Update Order](Document%20Update%20Order.md) Step 5 remains open, and its gates (D-P5, D-P6, D-P7) are untouched by this work.

## 6. Corrections owed to existing registers

| Register | Correction |
|---|---|
| [Contradictions Matrix](Contradictions%20Matrix.md) §C | S3 8-storey GBA is **212,000 GSF**, not 208,000 (`Program & Massing!D17`) |
| [Master Assumption Register](Master%20Assumption%20Register.md) PRG-04 | Same correction |
| [Open Questions](Open%20Questions.md) | Add OQ-24 through OQ-30 |
| [Risk Register](Risk%20Register.md) | Add R-21 through R-25 |

These are applied in this cycle where the document is a live register, and flagged where the document is a ratified artefact requiring owner action.

## 7. The honest summary

The site is good. The thesis is right. The price is wrong, and the program is too large.

South Andrews is genuinely well suited to a healthcare-facing mobility and clinical use: a 275-foot corner on a hospital corridor, protected open space to the north, downtown and airport proximity, Opportunity Zone status, and a district permitting the uses contemplated. Ground-floor medical retail materially strengthens the entitlement story, and the two-site operating logic is correct.

None of that generates enough rent to service $8 million of land plus $40–86 million of construction. The disciplined path is to stop treating acquisition as the first step, spend $100–200K closing the four gates that could change the answer, and test whether a healthcare anchor, a public source, or a different transaction structure can carry what the real-estate economics cannot.
