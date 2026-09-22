---
title: "K295 Order-Seven Exterior Integrability Boundary"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Bare-measure share of the K292 tube and exact face-integrability audit of the K290 pointwise derivative majorant; no true-integrand divergence or complete exterior bound."
manifest: lab/process/k295-order-seven-exterior-integrability-boundary.json
producer: tests/channel-swings/k295_order_seven_exterior_integrability_boundary.py
probe: tests/channel-swings/k295_order_seven_exterior_integrability_boundary_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: K292_TUBE_BARE_MASS_TINY__K290_POINTWISE_FOURTH_BANK_NONINTEGRABLE_ON_SIMPLEX_FACES__CANCELLATION_PRESERVING_FACE_RULE_REQUIRED
canon_verdict_change: none
---

# K295 Order-Seven Exterior Integrability Boundary

```gu-typed-objects
result: rigorous K292 bare-measure share upper and exact simplex-face integrability audit of the K290 pointwise derivative majorant
carrier: complete order-seven K179 size-four occurrence family in K294 radial-simplex coordinates
measure: K288 native bare measure with one vanishing projective gap retained before absolute integration
action_owner: repository construction from K139/K156/K179; no source-selected GU action, exterior value or physical state is supplied
target: decide whether the certified K290 fourth-order bank can legally extend from the K292 tube to the complete positive-gap domain
```

## Tube share

Using K292's exact native volume, the exact x width and y integral, and valid
coordinate extrema on the entire tube gives

```text
bare mass(K292 tube) / bare mass(complete K288 domain) < 6.198e-27.
```

This is deliberately a bare-measure statement. It does not compare the
coherent determinant integrand inside and outside the tube, but it proves that
the local K293 calculation cannot be treated as a representative full-measure
proxy.

## Why the existing derivative bank cannot simply be extended

For shape-derivative order `m>=1`, K290's endpoint-safe old-kernel estimate
contains `ratio_min^-m`. At a simplex face where one gap is `s`, the native
projective density supplies one power of `s`. The resulting factorwise
majorant behaves like

```text
s^(1-m).
```

It is integrable for `m=0,1`, logarithmically nonintegrable for `m=2`, and
power-law nonintegrable for `m=3,4`. Therefore the K290 fourth-order pointwise
bank cannot be integrated over the K294 simplex exterior.

This does **not** prove divergence of the true coherent integrand. K290 took
absolute factorwise bounds before retaining the coalescent zeros of the
size-three companion determinant and the size-four Cauchy determinant. The
next legal construction is a coalescent-face derivative packet that keeps
those zeros and the native gap weight together before absolute integration,
starting with one vanishing-gap face and its codimension-two intersections.
