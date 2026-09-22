---
title: "K290 Order-Seven Native Rest Derivative Bank"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Rigorous fourth-order shape-derivative bank for the complete native rest factor on the K284 tube; no composed native tube integral, exterior bound, action-column value, residual, K152 interval, or physical claim."
manifest: lab/process/k290-order-seven-native-rest-derivative-bank.json
producer: tests/channel-swings/k290_order_seven_native_rest_derivative_bank.py
probe: tests/channel-swings/k290_order_seven_native_rest_derivative_bank_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: NATIVE_REST_FACTOR_FOURTH_DERIVATIVE_BANK_FINITE__COMMON_REGULARIZER_COMPOSITION_PENDING
canon_verdict_change: none
---

# K290 Order-Seven Native Rest Derivative Bank

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k290-order-seven-native-rest-derivative-bank.json`
- `route_verdict`: `native_rest_derivative_bank_finite__composition_pending`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: finite componentwise mixed shape-derivative envelopes through order four for the complete native rest factor in all 24 order-seven size-four occurrences
carrier: the four coherent six-entry K179 Gram groups on sixteen positive primitive cumulative-time increments
measure: (2*pi)^-9 exp(-256*x*L) x^15 y(1-y) product(r_i c_i) on the K284 x/r/c tube and the complete y,u,z cube
separated_factor: the common K284/K286 size-four regularizer R4
retained_factors: the size-four Cauchy skeleton, complete size-three Bessel determinant, both old-position kernels and native density
claim_ceiling: rest-factor derivative bank only; no complete native tube integral, exterior bound, action column or K152 interval
```

## Endpoint-safe construction

The old kernels cannot be bounded separately at `y=0` or `y=1`. K290 first
pairs them with the exact native density as

```text
[y 2K1(T_old)] [(1-y) 2K1(U_old)].
```

For derivative order `m`, the integer-order Bessel recurrence is combined
with

```text
q^nu K_nu(q) <= 2^(nu-1)(nu-1)!
```

and the exact homogeneous maximum

```text
sup y a^m/(y+r a)^(m+1)
  = m^m / ((m+1)^(m+1) r^m).
```

This gives finite bounds at every split corner without deleting a primitive
variable. The size-four Cauchy determinant retains all 24 Leibniz terms; the
companion size-three determinant retains all six. The final rest-factor rule
retains all `6^m` labelled derivative allocations through order four.

## Result and boundary

For one occurrence the order-zero-through-four rest bounds are approximately

```text
1.64625e-33, 4.01388e-31, 1.08387e-28,
3.60418e-26, 1.61873e-23.
```

Each coherent group has weights `[1,-2,2,1,-2,1]`; K290 records the signed
value interval before taking derivative absolute bounds. The raw fourth-order
factor majorant is largest for the right endpoint-safe old-kernel piece. This
is a diagnosis of the conservative proof, not a lower bound or an impossibility
result for a sharper weighted rule.

The producer passes eight structural checks and the independent replay rejects
eight hostile mutations. Source, physics ledger, canon, paper and public
posture remain unchanged.
