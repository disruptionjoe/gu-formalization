---
title: "K289 Order-Seven Common-Primitive Composition Boundary"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Exact common-primitive dependency theorem for the 24 order-seven size-four occurrences; no native weighted remainder, arbitrary-gap exterior bound, action-column value, residual, K152 interval, or physical claim."
manifest: lab/process/k289-order-seven-common-primitive-composition-boundary.json
producer: tests/channel-swings/k289_order_seven_common_primitive_composition_boundary.py
probe: tests/channel-swings/k289_order_seven_common_primitive_composition_boundary_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: K287_COMMON_SIZE_FOUR_FACTOR_IS_NATIVE_BUT_REST_FACTOR_RETAINS_EIGHT_INTERNAL_SPLITS__COMMON_PRIMITIVE_RULE_REQUIRED
canon_verdict_change: none
---

# K289 Order-Seven Common-Primitive Composition Boundary

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k289-order-seven-common-primitive-composition-boundary.json`
- `route_verdict`: `common_size_four_factor_native__shared_primitive_rest_factor_open`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: an exact dependency theorem separating K287's common size-four factor from the split-dependent native rest factor in every one of its 24 K179 occurrences
carrier: complete order-seven K179 coherent Gram family on sixteen positive primitive time increments
common_chart: (x,y,r0,r1,r2,c0,c1,c2,u0,u1,u2,u3,z0,z1,z2,z3)
target: decide whether K287 can be assigned a native weighted occurrence error before exterior arbitrary-gap work
claim_ceiling: dependency and next-chart theorem only; no weighted remainder, exterior bound, action column or native K152 interval
```

## Exact dependency theorem

The size-four factors all use cumulative positions `(1,3,5,7)`. Their row and
column nodes are

```text
T1=x(y+r0+r1+r2), T3=x(y+r1+r2), T5=x(y+r2), T7=xy,
U1=x(1-y+c0+c1+c2), U3=x(1-y+c1+c2),
U5=x(1-y+c2), U7=x(1-y).
```

Every kernel argument is an odd-position cross sum `T_i+U_j`; `y` cancels.
Thus K284/K287 genuinely control the same size-four factor in all 24 native
occurrences, uniformly in `y` and in the eight internal split variables.

That does not make the K287 remainder native. Each occurrence also has one
size-three determinant on even cumulative positions chosen from `(2,4,6,8)`.
For example,

```text
T_(2k)=x*(later pair-ratio sums + current pair ratio*(1-u_(k-1))),
```

and similarly for `U_(2k)` with `z`. All 24 companion determinants therefore
retain internal split variables. Both old-position kernels also retain one
split variable because every old-position pair is drawn from `2,4,6`.

The audit covers all 24 occurrences, six per coherent group. It finds six
distinct companion position patterns, each repeated in four species-labelled
groups, and the six old-position pairs `(2,2),(2,4),(2,6),(4,4),(4,6),(6,6)`,
each occurring four times. Therefore
neither the signed occurrence sum `4` nor the absolute sum `36` can replace
entrywise integration.

## Consequence and next gate

K287 remains a valid uniform error for the common size-four factor. It is not a
native weighted occurrence error until the rest factor is controlled on the
same primitives. The minimum next chart is all sixteen variables above, with
the complete six-entry coherent group sum retained before absolute enclosure.

On the K284 `x/r/c` tube, the next calculation must bound values and mixed
derivatives of both old-position kernels, the companion size-three determinant,
the exact Cauchy--Vandermonde skeleton, and the native density, then compose
them with K286. Only after that common-tube result may the domain split into
radial exterior (`x` outside `[31/256,1/8]`) and projective-gap exterior (`r,c`
outside the K284 tube). The `y,u,z` variables are native interior variables,
not an exterior tail.

Source, physics ledger, canon, paper, and public posture remain unchanged.
