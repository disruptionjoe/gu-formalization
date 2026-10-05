---
title: "K1123 source I1B constraint-rank floor"
status: active_research
doc_type: source_native_causal_symbol_constraint_budget
created: 2026-10-05
claim_ceiling: exact local finite-symbol necessity; no global BV/BFV construction
manifest: lab/process/k1123-k1122-source-i1b-constraint-rank-floor.json
probe: tests/channel-swings/k1123_k1122_source_i1b_constraint_rank_floor_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1123 source I1B constraint-rank floor

> **GU-COMPARATOR-ROUTING — scope before inference.** This applies K1121--K1122
> to the actual K129 source-native symbols. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: causal-symbol constraint-codimension floor after K1118
carrier: K128 h-plus-t Hessian symbol on K127 local Ricci-flat T=0 germ LAYER=source-print CHIRALITY=N/A
pairing: source-native mixed Hessian form ON=metric_plus_distortion_symbol
real_structure: local real causal-symbol carrier
grading: timelike, spacelike and null covectors
action_owner: source-action -- I1B local quadratic germ
target: proposed nonnegative constraint subspace MAP-TYPE=restriction_then_quotient
```

K1118 gives negative-index floors `6,6,4` for timelike, spacelike and null
symbols. K1122 therefore requires any nonnegative constrained carrier to have
typewise codimension at least

```text
timelike 6, spacelike 6, null 4.
```

K1121 separately shows that quotienting the Hessian radical does not pay any
of this budget. Consequently an ordinary gauge-only quotient is insufficient
at every nonzero causal type. The result does not identify the constraints,
prove propagation, or globalize the symbol family; it is the minimum budget a
source-action KT/BFV construction must meet. The producer passes `10/10`; the
hostile probe rejects `8/8` mutations.
