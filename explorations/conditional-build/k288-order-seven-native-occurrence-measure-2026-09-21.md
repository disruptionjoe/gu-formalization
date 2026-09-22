---
title: "K288 Order-Seven Native Occurrence Measure"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Exact signed occurrence weights and exact sixteen-primitive cumulative-time measure for the order-seven K179 size-four occurrence family; no native weighted remainder, arbitrary-gap exterior bound, action-column value, residual, K152 interval, or physical claim."
manifest: lab/process/k288-order-seven-native-occurrence-measure.json
producer: tests/channel-swings/k288_order_seven_native_occurrence_measure.py
probe: tests/channel-swings/k288_order_seven_native_occurrence_measure_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: NATIVE_OCCURRENCE_AND_CUMULATIVE_TIME_MEASURE_SERIALIZED__COMMON_PRIMITIVE_WEIGHTED_REMAINDER_OPEN
canon_verdict_change: none
---

# K288 Order-Seven Native Occurrence Measure

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k288-order-seven-native-occurrence-measure.json`
- `route_verdict`: `native_occurrence_measure_serialized__weighted_remainder_open`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: the exact signed occurrence weights and sixteen-positive-time measure for all 24 size-four factors in the complete order-seven K179 coherent Gram family
carrier: K179 order-seven coefficient family after K279 specieswise Andreief reduction, with all 408 K280 upper-triangle Gram entries
measure: sixteen positive primitive cumulative-time increments with density exp(-256 sum(s_i+v_i)), exact (2*pi)^-9 point prefactor and coherent Gram symmetry multiplicity
coordinates: eight pair sums, eight internal split fractions, radial x, left/right base split y and six projective gap ratios
target: replace K287's normalized uniform proxy by the exact native occurrence and cumulative-time measure without dropping companion factors
claim_ceiling: measure and occurrence serialization only; no native weighted Jacobi remainder, arbitrary-gap exterior bound, action column or K152 interval
```

## Preflight bookend

K287's `4.7602870905e-7` error is a normalized average of one size-four
regularizer. The native K179 object is a signed coherent Gram sum. K288 first
restores the exact consumer before judging whether that local error matters.

The 408 stored K280 entries are upper triangular inside sixteen coherent
groups. Native reconstruction gives diagonal entries multiplicity one and
off-diagonal entries multiplicity two. The 24 size-four occurrences have
signed-weight histogram `{-2: 8, +1: 12, +2: 4}`, signed sum `4`, and absolute
sum `36`. The signed sum is not an integral shortcut: the six records in each
of four groups carry different old-position kernels and companion determinants.

## Exact native coordinate measure

Pair the sixteen primitive increments as

```text
a_i = s_(2i+1)+s_(2i+2),  b_i = v_(2i+1)+v_(2i+2),  i=0,...,3.
```

Writing the within-pair splits as `u_i,z_i` contributes the exact Jacobian
`product_i a_i b_i`. Then set

```text
x=a_3+b_3,  y=a_3/x,
r_i=a_i/x,  c_i=b_i/x,  i=0,1,2.
```

The pair-sum Jacobian is `x^7`, so the complete bare measure is

```text
exp(-256*x*L) x^15 y(1-y) product_i(r_i c_i)
  dx dy dr dc du dz,
L = 1 + sum_i r_i + sum_i c_i.
```

The mass replays exactly. Integrating the six ratios gives `(256*x)^-12`,
the `y` integral is `1/6`, the remaining `x` integral is `3!/256^4`, and the
eight split variables have unit cube mass. The result is `256^-16`, exactly
the product of sixteen elementary exponential masses.

## Decision boundary

This is the native occurrence and cumulative-time measure, but not yet the
native weighted K287 remainder. Every occurrence still contains the common
size-four factor, one companion determinant, two old-position kernels, the
Cauchy--Vandermonde skeleton, and the coherent sign. K289 audits their shared
primitive dependencies before any absolute error is assigned.

Source, physics ledger, canon, paper, and public posture remain unchanged.
