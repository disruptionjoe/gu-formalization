---
title: "K361--K363 order-eight projective neighborhoods"
status: exploration
claim_verdict: internal_structural_and_numerical_control_only
date: 2026-09-23
claim_ceiling: positive-width maximum-chart pilot cells, exact measure-only zero-strip angular majorants, and an exhaustive disjoint K350-reachable face-neighborhood owner rule; the uniform integrand-weighted boundary envelope, recursive cover, tails and complete hybrid integrals remain open
manifests:
  - lab/process/k361-order-eight-positive-width-projective-cells.json
  - lab/process/k362-order-eight-zero-strip-angular-majorants.json
  - lab/process/k363-order-eight-global-face-neighborhood-ownership.json
producers:
  - tests/channel-swings/k361_order_eight_positive_width_projective_cells.py
  - tests/channel-swings/k362_order_eight_zero_strip_angular_majorants.py
  - tests/channel-swings/k363_order_eight_global_face_neighborhood_ownership.py
probes:
  - tests/channel-swings/k361_order_eight_positive_width_projective_cells_probe.py
  - tests/channel-swings/k362_order_eight_zero_strip_angular_majorants_probe.py
  - tests/channel-swings/k363_order_eight_global_face_neighborhood_ownership_probe.py
---

# K361--K363 order-eight projective neighborhoods

Classification: `INTERNAL_STRUCTURAL_AND_NUMERICAL_CONTROL_ONLY`.

K361 makes the first genuine positive-width projective interval step. Each of
K358's `578` maximum-coordinate charts receives one exact rational ratio box
strictly inside `(0,1)^(c-1)`, and all `2,998` program-chart uses point to
those cells. One cell at every reachable codimension is executed with the
complete K352-preconditioned evaluator on
`rho in [1/4096,5/16384]`. All thirteen controls preserve the `2,400` ordered
descriptors and `23` coherent groups, have positive cumulative-argument floors,
contain the direct complete evaluator at the cell midpoint and give finite
radial/projective Peano pilot uppers. They are pilots, not a chart cover.

K362 separates geometry from the still-missing functional bound. On one chart,
the angular density satisfies

```text
(1 + sum r)^(-c) <= 1.
```

Therefore a specified depth-`s` intersection of one-sided strips
`0 <= r_i <= epsilon` has angular mass at most `epsilon^s`, also capped by the
exact chart mass `1/c!`. The union of all coordinate-zero strips is bounded by
`min(1/c!,(c-1)epsilon)`. These are exact measure bounds and vanish with their
declared epsilon order. They do not control growth of the K352-preconditioned
integrand as a ratio reaches zero.

K363 fixes `epsilon=1/64` and defines
`L_epsilon(t)={i:t_i<=epsilon*max_j t_j}`. For each hybrid, the largest
K350-reachable mask contained in this low-coordinate set owns the point;
canonical axis order breaks remaining ties. If there is no such mask, the
interior owns the point. Exhausting all `524,286` low-coordinate subsets across
the eighteen hybrid domains proves that every pattern has one owner, every
face owner is reachable, and `v8`/`v9` remain interior-only.

## Exact continuation

The next gate is not more ownership geometry. It is a uniform
determinant-preserving bound for the complete K352-preconditioned integrand on
each owned strip whose closure touches a ratio zero. K349 controls individual
scaled Bessel derivatives and K353 proves radial integrability, but those facts
have not yet been composed through the full determinant/coherent-group
assembly in the projective boundary coordinate. Only after that composition
may the positive interior be recursively subdivided, radial tails joined and
the eighteen K348 hybrid integrals emitted.

K361 passes `9/9` controls and rejects `12/12` hostile mutations. K362 passes
`8/8` and rejects `10/10`. K363 passes `9/9` and rejects `11/11`.

SC-META-53 remains `UNCERTAIN`; RA-F1, LT-SM8, LT-GR6b and AC-F1 remain
`NEEDS`. No source, ledger, canon, paper, public or physical posture changes.
