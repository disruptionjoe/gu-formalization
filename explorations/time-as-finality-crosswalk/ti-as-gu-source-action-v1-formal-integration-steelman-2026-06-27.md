---
title: "V1: Temporal Issuance as GU Source Action - Formal Integration Steelman"
date: 2026-06-27
status: exploration
doc_type: crosswalk
verdict: OPEN_GATED_STEELMAN_ONLY
optional_executable:
  - tests/temporal_issuance_source_action_steelmen_checker.py
depends_on:
  - explorations/time-as-finality-crosswalk/ti-as-gu-source-action-three-steelmen-2026-06-27.md
  - explorations/shiab-selector-search-2026-06-26.md
  - explorations/time-as-finality-crosswalk/record-issuance-boundary-selector-2026-06-26.md
  - active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md
external_context:
  - ../../../temporal-issuance/explorations/E087-online-issuance-formal-object-v0-1-2026-06-25.md
---

# V1: Formal Integration Steelman

## Steelman Statement

The GU source action is the admissible extension process that Temporal Issuance calls
`Issue[S]`. On this reading, source-side issuance does two jobs that bulk algebraic selectors
have failed to do:

1. it selects a member of the residual shiab family left open by Spin(9,5) equivariance and
   right-H linearity;
2. it supplies the end or boundary datum, such as a spectral section or `P_ge_0` projection,
   needed to make a noncompact `Y14` index well-defined.

The observer-facing record is not the source action. The record is the lossy audit trail of a
source-side admissible extension. The strong version therefore requires a real GU carrier:

```text
Issue[S](Gamma_n, e_n, w_n)
  where e_n includes a source-geometric family coordinate, boundary carrier, or curvature datum.
```

## Why This Is The Strongest Version

This version directly targets the repo's current wall: the source action gates shiab selection,
the noncompact index, RS/BRST stabilization, and theta/dark-energy coefficients.

It also respects the negative results. It does not say "records select the shiab." It says:

```text
records can audit a source-side extension;
only a source-side extension with GU geometric content can select.
```

That is compatible with the Temporal Issuance effect gate and with the GU boundary-selector
verdict.

## Minimal Interface Contract

The narrow bridge must fill this contract:

| GU field | Temporal Issuance field | required extra structure |
|---|---|---|
| typed source constraints | `Gamma_n` | GU source variables, not observer records |
| candidate shiab family | `CandExt(Gamma_n)` | family coordinates on the residual 4-real-dimensional space |
| admissibility | `Adm_n(e_n)` | source-natural criterion, not target fitting |
| source action / step | `Issue[S](Gamma_n,e_n,w_n)` | present witness selecting or constraining a member |
| boundary section | recordable trace `tau_n` plus carrier | holonomy, connection, curvature, spectral section, or K-class |
| observer physics | `Project[O] + Finalize[R] + Lose[K]` | readout only; cannot by itself promote the source claim |

## Test Steps

### Test 1: Shiab Family Selection

Parameterize a toy residual family with the four H-linear coordinates:

```text
(contract_+-, wedge_+-, contract_-+, wedge_-+)
```

Apply three rule classes:

1. record-only finality;
2. issuance tag with no family-coordinate functional;
3. issuance with an explicit source-side family-coordinate functional.

Expected result:

- classes 1 and 2 leave the family unselected;
- class 3 can select, but only because it adds the missing source carrier.

This is a useful result even if negative: it prevents "Temporal Issuance" from being used as a
name for a selector that has not been written.

### Test 2: Boundary / Index Regularization

Use the boundary split already isolated by the repo:

```text
S3 boundary toy: eta = 0, shiab-blind
lens-space boundary toy: eta can be nonzero, index regularization can move
```

Expected result:

- boundary data can matter for the index;
- the same toy remains blind to shiab family coordinates unless a source-to-boundary curvature
  map is supplied.

### Test 3: Signed Readout Compatibility

Model issuance traces as evidence-monoid generators and verify:

```text
provenance grows monotonically;
signed scalar readout may decrease;
the decrease is readout-side, not source-side reversal.
```

This allows non-monotone generation or chirality readouts without turning provenance into a
non-monotone source process.

## Kill Criteria

Kill or demote this version if any of the following occurs:

- `NO_UNIQUE_FAMILY_SELECTION_WITHOUT_SOURCE_CARRIER`: no admissible issuance rule selects a
  viable shiab member unless a family-coordinate/source-action carrier is added.
- `APS_RELABELLING_ONLY`: the spectral section is just standard APS data with no new issuance
  content.
- `NO_BOUNDARY_HOLONOMY_CARRIER`: record finality supplies no holonomy, connection, curvature,
  or spectral-section-valued datum.
- `CANON_CONTRADICTION`: the rule contradicts shiab existence, the residual family computation,
  or weak-field canon.

## Current Verdict

V1 is the most useful immediate version, but it is an interface contract, not a result. It
survives only as:

```text
Temporal Issuance could realize the GU source action if Issue[S] is equipped with a GU-native
source-geometric carrier.
```

Without that carrier, V1 reduces to the already documented record-finality audit layer.

## Machine-Readable Summary

```json
{
  "artifact": "TI_GU_SOURCE_ACTION_V1_FORMAL_INTEGRATION",
  "status": "OPEN_GATED",
  "claim_promotion": false,
  "survives_as": "interface_contract_not_selector",
  "required_carriers": [
    "family_coordinate_functional",
    "boundary_holonomy_or_connection",
    "source_derived_curvature_or_K_class"
  ],
  "kill_criteria": [
    "NO_UNIQUE_FAMILY_SELECTION_WITHOUT_SOURCE_CARRIER",
    "APS_RELABELLING_ONLY",
    "NO_BOUNDARY_HOLONOMY_CARRIER",
    "CANON_CONTRADICTION"
  ]
}
```
