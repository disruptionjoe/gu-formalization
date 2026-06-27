---
title: "V2: Temporal Issuance as GU Source Action - Wolfram and Signed-Readout Steelman"
date: 2026-06-27
status: exploration
doc_type: crosswalk
verdict: OPEN_GATED_STEELMAN_ONLY
optional_executable:
  - tests/temporal_issuance_source_action_steelmen_checker.py
depends_on:
  - explorations/time-as-finality-crosswalk/ti-as-gu-source-action-three-steelmen-2026-06-27.md
  - active-research/signed-readout/theorem-statement-v1-2026-06-23.md
  - explorations/time-as-finality-crosswalk/record-issuance-boundary-selector-2026-06-26.md
  - explorations/time-as-finality-crosswalk/effect-typed-witness-transport-bidirectional-crosswalk-2026-06-25.md
external_context:
  - ../../../temporal-issuance/explorations/E087-online-issuance-formal-object-v0-1-2026-06-25.md
  - ../../../temporal-issuance/explorations/E080-gu-effect-typed-witness-transport-2026-06-25.md
---

# V2: Wolfram and Signed-Readout Steelman

## Steelman Statement

Temporal Issuance is the source-side computational process that introduces admissible structure
into the shared geometric process. In a Wolfram-style lens, the missing GU source action is the
missing local rewrite rule. The shiab family is a set of equivalent or underdetermined bulk
descriptions until a source rule and observer cut make a readout definite.

Boundary projections, spectral sections, and records are observer cuts through the generated
process. They can be irreversible and lossy. They can produce signed or phase-sensitive
readouts. But they cannot replace the local source rule unless they carry path-dependent
geometric data.

## Wolfram Translation

| GU / TI object | Wolfram-style reading |
|---|---|
| source action | local rewrite rule |
| shiab family | underdetermined bulk descriptions / branch-equivalent encodings |
| source-side issuance | rule-generated admissible extension |
| boundary projection `P_ge_0` | observer cut / irreversible coarse-graining |
| spectral section | selected boundary slice of modes |
| eta invariant | global asymmetry of the observer boundary |
| signed readout | lossy scalar extracted from monotone provenance |
| missing holonomy carrier | no path-dependent labels on the generated graph |

This lens strengthens the boundary-selector verdict: the boundary idea is structurally right,
but it is an observer/finality object until a source rewrite rule induces it.

## Test Steps

### Test 1: Rule-Generated Family Examples

Use a minimal finite rewrite toy:

```text
state = residual shiab family coordinate
rule = admissible extension operation
observer = projection/finality map
```

The decisive comparison is:

- fixed observer projection over a pre-existing family;
- source rule that generates or constrains the family coordinate.

Expected result:

```text
projection/finality can expose a chosen branch;
only a rule with source-family content can generate selection.
```

### Test 2: Signed-Readout Object

Instantiate the signed-readout theorem on a two-generator evidence monoid:

```text
x_plus  weight +1
x_minus weight -1
```

Verify:

```text
0 <= [x_minus] in provenance order;
positive and negative provenance components grow;
scalar readout drops from 0 to -1.
```

This is the correct formal home for "monotone provenance, non-monotone readout." It does not
turn final records into source issuance.

### Test 3: Boundary Finalization Carrier

Ask whether the finalization object contains:

```text
pi_1(boundary) -> U(n)
connection / curvature
spectral-section-valued datum
path-dependent transport
```

Expected result from current artifacts: no. Current record finality has audit value but no
boundary holonomy carrier.

## Kill Criteria

Kill or demote V2 if:

- `FIXED_RULE_OR_FIXED_LATENT_ABSORBS`: issuance reduces to fixed computation, fixed law, or
  fixed latent graph disclosure.
- `SIGNED_READOUT_ONLY`: the only nontrivial result is signed readout over monotone provenance.
- `NO_HOLONOMY_ON_RECORD_GRAPH`: finalization records cannot carry path-dependent geometric
  transport.
- `OBSERVER_CUT_USED_AS_SOURCE_RULE`: an observer projection is treated as source action.

## Current Verdict

V2 is the best explanatory layer. It explains why:

- bulk selectors fail;
- boundary objects partially succeed;
- signed readouts can be non-monotone without source reversal;
- a record-only boundary does not select the shiab.

It does not solve GU. Its live role is to prevent category mistakes while defining the next
source-carrier search.

## Machine-Readable Summary

```json
{
  "artifact": "TI_GU_SOURCE_ACTION_V2_WOLFRAM_SIGNED_READOUT",
  "status": "OPEN_GATED",
  "claim_promotion": false,
  "survives_as": "observer_rule_separation_and_signed_readout_testbed",
  "required_carriers": [
    "source_rewrite_rule",
    "path_dependent_holonomy_or_transport",
    "non_projection_family_selection"
  ],
  "kill_criteria": [
    "FIXED_RULE_OR_FIXED_LATENT_ABSORBS",
    "SIGNED_READOUT_ONLY",
    "NO_HOLONOMY_ON_RECORD_GRAPH",
    "OBSERVER_CUT_USED_AS_SOURCE_RULE"
  ]
}
```
