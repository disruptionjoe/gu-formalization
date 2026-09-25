---
title: "K481 — K152 Inverse Cross-Norm Budget"
status: active_research
status_axis: operational_state
doc_type: conditional_inverse_same_form_cross_budget
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K481 — K152 inverse cross-norm budget

Classification: INTERNAL_STRUCTURAL_ONLY.

```gu-typed-objects
result: inverse K473 cross-norm acquisition budget for a requested floor
carrier: one complete same-form M-orthogonal two-block K162 split LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Gram M=S* S ON=k162_complete_complement
real_structure: CAR adjoint, momentum conjugation and K162 signed flavor transport
grading: two diagonal blocks, cross block and requested complete-complement floor
action_owner: repository-construction; native floor and cross certificates absent
target: requested K463 complete-complement floor MAP-TYPE=not-a-map
```

## Theorem

For authenticated same-form lower floors `alpha,gamma` and a requested root
floor `t`, K473 can be inverted before numerical cross evaluation:

```text
mu^2 < (alpha-t)(gamma-t).
```

This is the exact strict acquisition budget. The rational control uses
`alpha=5`, `gamma=8`, `t=3` and selected `mu=3`; the maximum strict squared
budget is `10`, the realized slack is `1`, and the outward lower root remains
above `3`.

## Bookends

The advance is operational: a native packet can decide how accurately its
cross norm must be bounded from the desired consumer floor, rather than first
performing an unpriced calculation. Equality is the strongest contrary case
and is rejected because it has zero strict margin. The weak seam remains
authentication of the leaf floors, complete partition and cross norm.

No native K162 data, K457 evaluation or K152 interval is released.

## Reproduction

```bash
python3 tests/channel-swings/k481_k152_inverse_cross_budget.py
python3 tests/channel-swings/k481_k152_inverse_cross_budget_probe.py
```
