---
title: "K1139 sharp negative-capture graph criterion"
status: active_research
doc_type: exact_minimal_rank_constraint_positivity_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional minimal-rank criterion; no source map or physical quotient
manifest: lab/process/k1139-sharp-negative-capture-graph-criterion.json
probe: tests/channel-swings/k1139_sharp_negative_capture_graph_criterion_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1139 sharp negative-capture graph criterion

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests
> whether a future source-native constraint actually captures the negative
> Hessian sector. A spectral selector used as a control is not source-owned.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp graph-contraction criterion for minimal-rank nonnegative restriction
carrier: finite nondegenerate positive-plus-negative Hessian splitting LAYER=source-print CHIRALITY=N/A
pairing: Hessian positive blocks D-minus and H-plus ON=constraint-kernel
real_structure: real symmetric bilinear form
grading: negative spectral block versus positive spectral block
action_owner: comparator -- future action-owned Q must be tested against this criterion
target: K1123 causal 6-6-4 rank floors MAP-TYPE=restriction
```

Write a nondegenerate Hessian as

```text
H = (-D_minus) direct-sum H_plus,
```

with both displayed blocks positive definite. A constraint of the minimal
possible rank `n_-(H)` has block form `Q=[Q_minus,Q_plus]`. If its kernel is
nonnegative, `Q_minus` must be invertible. Then the kernel is the graph
`v_minus=-B v_plus`, where `B=Q_minus^{-1}Q_plus`, and its Hessian is exactly

```text
H_plus - B* D_minus B.                              (1)
```

Therefore the restriction is nonnegative exactly when `B` is a contraction
between the two weighted positive forms. Rank is only the entrance fee. The
fixture `H=diag(-2,-1,3,4)` gives two rank-two constraints: `B=diag(1,1)`
passes with restricted diagonal `(1,3)`, while `B=diag(2,1)` fails with
`(-5,3)`. Repeated exact controls at negative indices `6,6,4` likewise give
equal-rank passing and failing selectors. A projector onto the negative
spectral space is a useful positive control, not an action-derived GU map.
The producer passes `12/12`; the hostile probe rejects `10/10` mutations.
