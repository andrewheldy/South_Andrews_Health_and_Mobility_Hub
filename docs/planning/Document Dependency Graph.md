# Document Dependency Graph

**Status:** Current dependency reference · **Last reviewed:** 2026-07-26
**Related:** [Source Inventory](Source%20Inventory.md) · [Document Update Order](Document%20Update%20Order.md) · [Repository Knowledge Graph](Repository%20Knowledge%20Graph.md)

Document-level edges: who cites whom, who depends on whom, and where citations point at documents that do not exist (**MISSING**). This graph determines safe update order: a document may only be revised after everything it depends on is settled.

## 1. As-is graph (today)

```mermaid
graph TD
  subgraph GOV["GOVERNANCE (operative constitution)"]
    AGENTS[AGENTS.md]
    CLAUDE[CLAUDE.md]
    SA[SOURCE_AUTHORITY.md]
    GL[PROJECT_GLOSSARY.md]
    CE[CLAIMS_AND_EVIDENCE_POLICY.md]
    WF[WORKFLOW.md]
    SK[skills/ x3]
  end

  subgraph CUR["sources/current"]
    S1[S1 Corrected_Assumptions.md]
    S2[S2 6v8 Story Model.xlsx]
    S3[S3 8M Construction Feasibility.xlsx]
    S4[S4 Andrews ODP.docx]
  end

  subgraph REF["sources/reference"]
    S6[S6 AEI Appraisal.pdf]
    S7[S7 Appraisal Valuation.xlsx]
    S8[S8 Native Realty study.pdf]
  end

  subgraph LEG["sources/legacy"]
    S5[S5 Prospectus Vol0.docx]
  end

  subgraph MISS["MISSING (cited, not in repo)"]
    CONST[["Project Constitution (MA-01)"]]
    DLOG[["Decision Log 001-003 (MA-02)"]]
    LIB[["Research library x5:<br/>Market Study MA-07 · Feasibility/Benchmark MA-08<br/>Site Intelligence MA-09 · Survey MA-10 · plus README MA-03"]]
    ELM[["Electrical_Load_Model.xlsx (MA-11)"]]
    CTX[["Andrews_Context.md (MA-12)"]]
    ESA[["Phase I/II ESAs (MA-13)"]]
  end

  S1 -->|interprets| S6
  S2 -->|cites| CONST & DLOG
  S2 -->|cites 'Operational Study / Site Analysis / Feasibility Study'| LIB
  S3 -->|cites| S6 & S8 & S5
  S3 -->|cites| ELM
  S4 -->|subordinate to| CONST & DLOG
  S4 -->|built from| LIB
  S4 -.->|surfaces conflict with| CTX
  S5 -->|governed by| S4
  S6 -->|relies on| ESA
  S6 -->|survey| LIB
  S7 -->|reviews| S6
  S7 -->|geometry from survey| LIB
  S8 -->|critiques| S6

  AGENTS -->|controls all| CUR & REF & LEG
  SA -->|scopes| CUR & REF & LEG
```

**Reading:** three of four current sources ground themselves in documents that are missing (dashed/red zone). Until MA-01/02/07–11 are recovered or formally succeeded, those citations are one-remove evidence at best.

## 2. To-be graph (after this planning set is ratified)

```mermaid
graph TD
  GOV2[Governance set + AGENTS.md] --> CANON[Project Canon]
  DL[Decision Log] --> CANON
  CANON --> MAR[Master Assumption Register]
  SRC[Source Inventory + Authority Register] --> MAR
  CM[Contradictions Matrix] --> MAR
  MAR --> FIN[Canonical Financial Assumptions]
  MAR --> CON[Canonical Construction Assumptions]
  CANON --> SCOPE[Current Project Scope] --> PROG[Current Development Program]
  CANON --> HCS[Healthcare Strategy] & MOBS[Mobility Strategy] & INF[Infrastructure Strategy]
  FIN & CON & PROG --> MODELS[Reconciled financial model vNext]
  MODELS --> ODP2[ODP v2]
  ODP2 --> PROS[Prospectus vNext]
  PROS --> FRONT[Design/communications surface]
  OQ[Open Questions] -.->|blocks until resolved| MODELS & ODP2 & PROS
  RR[Risk Register] --> ODP2
```

**Rule:** flow is one-way. A downstream document never introduces a value absent upstream; if it needs one, the upstream register changes first (with provenance), then the downstream regenerates.

## 3. Dependency table (who must move when X changes)

| If this changes… | …these must be revisited |
|---|---|
| Owner decision (any D-##) | Project Canon → affected register rows → both models → ODP v2 chain |
| Program basis resolution (OQ-14) | Development Program §1 → all PRG/CST/REV DUAL rows → S2/S3 successor model → everything downstream |
| Rent resolution (OQ-15) | Financial Assumptions → NOI/yield outputs → feasibility statement → partner-gap figures |
| Tax counsel opinion (OQ-17) | Financial Assumptions §4 → solar/BESS net costs → TDC → yield gap |
| FPL study (OQ-04) | Infrastructure Strategy §1 → utility cost line → imaging gate → DCFC gate |
| Zoning Verification Letter (OQ-03) | Canon §4 → Scope scenario table → height decision inputs |
| Recovery of any MA-xx document | Source Inventory + Authority Register + every claim currently cited "via missing doc" |
| Appraisal update / new offer terms | Acquisition rows (ACQ-01…09) → negotiation docs |

## 4. Citation hygiene rules

1. Citations to missing documents must be written as "X *as cited by* [present source]" — never as direct citations.
2. When a missing document is recovered, its direct citations replace the one-remove forms in the next update cycle.
3. Every new document declares its dependencies in a header block so this graph can be regenerated mechanically.
