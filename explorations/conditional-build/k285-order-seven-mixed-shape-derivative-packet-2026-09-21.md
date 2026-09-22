---
title: "K285 Order-Seven First Shape-Gradient Packet"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Rigorous first derivatives on K284's transverse tube only; no higher mixed-Duffy bank, Jacobi remainder, action-column value, native K152 interval, or physical claim."
manifest: lab/process/k285-order-seven-mixed-shape-derivative-packet.json
producer: tests/channel-swings/k285_order_seven_mixed_shape_derivative_packet.py
probe: tests/channel-swings/k285_order_seven_mixed_shape_derivative_packet_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: ALL_SIX_FIRST_SHAPE_DERIVATIVE_ENVELOPES_CERTIFIED__HIGHER_MIXED_DUFFY_BANK_AND_JACOBI_REMAINDER_OPEN
canon_verdict_change: none
---

# K285 Order-Seven First Shape-Gradient Packet

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k285-order-seven-mixed-shape-derivative-packet.json`
- `route_verdict`: `all_six_first_shape_derivatives_certified_on_k284_tube__higher_mixed_orders_open`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: rigorous first shape-gradient envelopes on every cell of K284's certified transverse tube
carrier: K284 complete center-preconditioned size-four determinant chart on 2,048 scale/radial cells
coordinates: r0, r1, r2, c0, c1, c2
derivative_rule: exact normalization derivative plus Hermite--Genocchi repeated-node entry derivative and completed determinant cofactors
target: serialize the first-order Lipschitz packet needed before a higher mixed-Duffy/Jacobi error calculation
claim_ceiling: first-derivative packet only; no higher mixed-Duffy derivative bank, Jacobi remainder, action-column value or native K152 interval
```

- The native object is K284's complete size-four transverse tube: 2,048
  scale/radial cells and six ordered shape coordinates.
- The derivative object is the six-component first shape gradient of the
  center-preconditioned determinant ratio on every cell.
- The derivative bound differentiates the exact normalization product,
  differentiates each Hermite--Genocchi entry by adding one repeated node,
  and completes every determinant cofactor before taking absolute values.
- The packet is first order only: there is no higher mixed-Duffy derivative
  bank, and it does not compose a Jacobi cubature remainder.

## Preflight

K284 supplies a directed-positive compact transverse tube with exact overlap
to K282 and K283. The next useful question is whether all first shape
derivatives admit finite rigorous envelopes on that whole tube. The
Hermite--Genocchi node derivative identity gives a cancellation-free entry
bound, while the determinant derivative is bounded through completed
cofactors rather than an entrywise determinant perturbation.

## Result

All 2,048 cells and all six shape coordinates have finite certified derivative
envelopes. The global absolute upper bounds are:

| coordinate | certified absolute upper |
|---|---:|
| `c0` | `1405.7786069433268` |
| `c1` | `1362.0769763510966` |
| `c2` | `1069.4020590610867` |
| `r0` | `1405.6413247707108` |
| `r1` | `1362.4738095726445` |
| `r2` | `1071.2745852839005` |

The resulting global L1 gradient upper is below
`7676.647361982766`. Twelve independent 300-digit central-difference controls
are contained by the corresponding certified envelopes. These controls are
diagnostic only; the proof comes from the Hermite--Genocchi and cofactor
enclosures.

The derivative packet is deliberately conservative. Its role is to serialize
a rigorous first-order Lipschitz object over the full K284 tube, not to claim
that the displayed upper bounds are sharp.

## Postflight

K285 closes the first shape-gradient gate on K284's tube. The next coherent
step is to build the higher mixed-Duffy derivative bank actually required by
a determinant-preserving Jacobi remainder and then test whether the resulting
composed error is decision-useful. No action-column value, complete residual,
exterior gap, native K152 interval, source or ledger move, canon change,
paper/public claim, or physical conclusion follows.
