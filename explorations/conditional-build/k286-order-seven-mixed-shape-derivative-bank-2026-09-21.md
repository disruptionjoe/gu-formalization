---
title: "K286 Order-Seven Mixed Shape-Derivative Bank"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Componentwise and Euclidean-operator derivative envelopes through order four on K284's transverse tube only; no native occurrence measure, Jacobi remainder, action-column value, native K152 interval, or physical claim."
manifest: lab/process/k286-order-seven-mixed-shape-derivative-bank.json
producer: tests/channel-swings/k286_order_seven_mixed_shape_derivative_bank.py
probe: tests/channel-swings/k286_order_seven_mixed_shape_derivative_bank_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: MIXED_SHAPE_DERIVATIVES_THROUGH_ORDER_FOUR_CERTIFIED__NATIVE_MEASURE_AND_ACTION_COLUMN_OPEN
canon_verdict_change: none
---

# K286 Order-Seven Mixed Shape-Derivative Bank

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k286-order-seven-mixed-shape-derivative-bank.json`
- `route_verdict`: `mixed_shape_derivatives_through_order_four_certified__native_measure_open`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: componentwise mixed derivative envelopes through total order four on every K284 tube cell
carrier: K284 complete center-preconditioned size-four determinant chart on 2,048 scale/radial cells
coordinates: r0, r1, r2, c0, c1, c2
derivative_rule: Hermite--Genocchi entry derivatives plus all determinant Leibniz assignments and the complete sixteen-factor normalization product rule
target: supply the finite fourth-order bank needed by a determinant-preserving local Jacobi remainder
claim_ceiling: derivative bank only; no native K179 occurrence measure, composed Jacobi remainder, action-column value, or native K152 interval
```

## Preflight bookend

K284 provides a genuine bounded six-dimensional tube and K285 proves its first
shape gradients. The next route-changing question is whether the complete
common determinant chart has finite higher mixed derivatives through the order
needed by a two-node Jacobi rule. The structural route differentiates the
underlying Hermite--Genocchi entries and complete determinant product rather
than independently ranging sixteen near-cancelling matrix entries.

For an order-`m` entry derivative, complete monotonicity bounds the repeated-
node simplex average by the `(row+column+m)`-th Bessel derivative divided by
`row! column!`. The determinant bound retains all 24 permutation terms and all
`4^m` labelled derivative-to-row assignments. The positive Cauchy
normalization retains the full sixteen-factor product rule. Their binomial
product gives every component of `D^m R`, `m=1,...,4`; Frobenius domination
then turns the componentwise bank into an explicit Euclidean operator bound.

## Result

All 2,048 cells have finite positive bounds through order four. The global
componentwise absolute upper bounds are:

| total order | componentwise upper | Euclidean operator-norm upper |
|---:|---:|---:|
| 1 | `1.6887422292e8` | `4.1365567685e8` |
| 2 | `9.3712994477e9` | `5.6227796686e10` |
| 3 | `4.9010008981e11` | `7.2029708575e12` |
| 4 | `2.4697068096e13` | `8.8909445146e14` |

Ten independent 300-digit central mixed-difference controls, including pure
and genuinely mixed fourth differences at both ends of the projective scale,
lie inside the componentwise bounds. They are diagnostics; the proof is the
Hermite--Genocchi/product enclosure on every cell.

The bounds are deliberately conservative. In particular, order one is much
looser than K285's coordinate-aware first-gradient packet because K286 uses
one uniform component bound that is valid for every repeated and mixed index
pattern. That cost buys a complete finite bank without silently identifying a
componentwise maximum with an operator norm.

## Postflight bookend

K286 releases a positive determinant-preserving fourth-order Jacobi
calculation on the certified tube. Strongest overclaim: this bank supplies the
native K179 integration measure. It does not; occurrence weights and the
scale/radial measure remain separate. Strongest contrary case: the large
fourth derivative makes any local rule useless. K287 must multiply the bound
by the actual tube radius to decide that. Weakest reproducibility seam: later
work must retain all 24 determinant terms and the complete normalization
product rather than using sampled finite differences as proof.

Source, physics ledger, canon, paper, and public posture remain unchanged.
