---
title: "K287 Order-Seven Tensor Jacobi Remainder"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Two-node tensor Gauss-Jacobi remainder for the normalized uniform K284 tube only; no native K179 occurrence or scale/radial measure, exterior arbitrary-gap domain, action-column value, native K152 interval, or physical claim."
manifest: lab/process/k287-order-seven-tensor-jacobi-remainder.json
producer: tests/channel-swings/k287_order_seven_tensor_jacobi_remainder.py
probe: tests/channel-swings/k287_order_seven_tensor_jacobi_remainder_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: NORMALIZED_TUBE_JACOBI_REMAINDER_CERTIFIED_BUT_NOT_ONE_PPM__NATIVE_MEASURE_AND_EXTERIOR_DOMAIN_OPEN
canon_verdict_change: none
---

# K287 Order-Seven Tensor Jacobi Remainder

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k287-order-seven-tensor-jacobi-remainder.json`
- `route_verdict`: `normalized_tube_remainder_certified__native_measure_and_exterior_domain_open`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: a certified two-node tensor Gauss--Jacobi remainder for the normalized uniform K284 shape tube
carrier: K284 complete center-preconditioned size-four determinant chart, with K286 fourth derivatives
measure: normalized uniform product measure on each six-dimensional transverse shape box
quadrature: Jacobi alpha=beta=0, two nodes per axis, 64 positive tensor nodes
target: test whether the certified local tube admits a determinant-preserving resolving quadrature before widening the gap domain
claim_ceiling: normalized local-tube proxy only; no native K179 occurrence or scale/radial measure, exterior arbitrary-gap coverage, action column, or native K152 interval
```

## Preflight bookend

K286 closes the finite fourth-derivative prerequisite. The cheapest rigorous
consumer is the positive two-node Gauss-Jacobi rule with
`alpha=beta=0`—the Gauss-Legendre special case—on each independent transverse
coordinate. For the normalized one-dimensional average on `[-h,h]`, its exact
remainder coefficient is `h^4/270`. Positivity and norm one of every remaining
integral and quadrature operator let the six-dimensional tensor error telescope
as the sum of six one-axis errors. Every node evaluates the full common
determinant ratio; no entrywise determinant approximation is introduced.

## Result

With `h=1/32768` and K286's componentwise fourth derivative upper
`2.4697068096092027e13`, the certified normalized-average errors are:

- one axis: `< 7.9338118175e-8`;
- all six axes: `< 4.7602870905e-7`.

Relative to K284's positive global lower `0.1255775360161132`, the remainder
ratio is `< 3.790715475e-6`. The rule therefore gives a finite and small local
tube error, but it does **not** meet the deliberately explicit one-part-per-
million resolving threshold used for this discriminator. The correct result is
not “quadrature failed”: it is that the current conservative uniform bank plus
two-node rule leaves a roughly 3.8-ppm local certificate. A sharper
coordinate-aware fourth bank or higher positive rule may improve that number.

## Measure and decision boundary

The certified measure is the normalized uniform product measure on one K284
shape box. It is **not the native K179 occurrence measure**. K287 does not
serialize the occurrence weights, projective-scale measure, radial measure, or
the exterior arbitrary-gap domain. Consequently it cannot emit an action-
column value, residual, exterior gap, or K152 interval and does not authorize
domain widening.

The next exact input is a consumer composition: attach the native occurrence,
scale, and radial weights to this local rule and bound the exterior domain. If
the 3.8-ppm local ceiling dominates that consumer, sharpen the fourth-order
bank or increase the positive Jacobi order before widening the gap tube.

## Postflight bookend

Strongest overclaim: `4.76e-7` is the order-seven action-column error. It is
only a normalized local-tube average. Strongest contrary case: a failed 1-ppm
threshold makes the tube useless. It does not; the error is finite, positive-
rule certified, and can be compared only after native weights are known.
Weakest propagation seam: substituting occurrence or exterior-domain weights
without a new proof would erase the exact measure boundary.

Source, physics ledger, canon, paper, and public posture remain unchanged.
