---
title: "K291 Order-Seven Native Interior Remainder"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-21"
claim_ceiling: "Native-density-weighted two-node tensor remainder for one K284 transverse shape box, uniform in x,y,u,z; no disjoint native tube integral, exterior bound, action-column value, residual, K152 interval, or physical claim."
manifest: lab/process/k291-order-seven-native-interior-remainder.json
producer: tests/channel-swings/k291_order_seven_native_interior_remainder.py
probe: tests/channel-swings/k291_order_seven_native_interior_remainder_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: NATIVE_DENSITY_LOCAL_SHAPE_REMAINDER_FINITE__DISJOINT_TUBE_ATLAS_AND_CORNER_SHARPENING_OPEN
canon_verdict_change: none
---

# K291 Order-Seven Native Interior Remainder

## GU-COMPARATOR-ROUTING

- `comparison_type`: `internal_structural`
- `external_calibration_anchor_ids`: `[]`
- `route_owner`: `gu-formalization`
- `route_artifact`: `lab/process/k291-order-seven-native-interior-remainder.json`
- `route_verdict`: `native_density_local_remainder_finite__complete_tube_open`

## Classification

`conditional-build`

## GU typed objects

```gu-typed-objects
result: a rigorous native-density-weighted two-node tensor remainder ceiling for one K284 transverse shape box
carrier: the complete four-group order-seven K179 size-four occurrence family
rule: fourth-order product composition of K284/K286 R4 with K290 groupwise rest factors, followed by the positive six-axis Gauss-Legendre telescope
scope: one t-centered K284 shape box, uniform on the full x interval and y,u,z cube
missing_measure_object: a disjoint native dr dc atlas or multiplicity rule for the overlapping K284 t-centered union
claim_ceiling: local native-density remainder only; no complete tube or exterior integral, action column or K152 interval
```

## Composition

For each coherent group `G`, K291 uses the complete identity

```text
D^4(R4 G) = sum_(j=0)^4 binom(4,j) D^j R4 D^(4-j)G.
```

The four group enclosures are summed only after this composition. Applying the
same positive two-node coefficient as K287 gives a complete four-group
fourth-derivative ceiling `1.1249973182e-15` and a six-axis normalized local
shape-average error below `2.168399176e-35`. Multiplication by the shape-box
volume and the full x-width gives `4.379047263e-63`; the `y,u,z` cube has unit
volume because its exact density is already inside K290.

The dominant product-rule contribution places one derivative on R4 and three
on the rest factor. Within the raw rest-factor bank, the right old-kernel
corner bound is largest. A weighted corner split is therefore the first
sharpening target if the complete tube composition needs it.

## Exact boundary

K284's t-centered transverse boxes overlap in native `(r,c)` coordinates.
K291 therefore does not sum the local ceiling into a complete native tube
integral. The next gate is a disjoint native `dr dc` atlas or an exact
multiplicity rule, together with a split-corner weighted rule for the dominant
old-kernel majorant. Radial and projective-gap exterior composition follows
only after that interior measure is well-defined.

The producer passes seven replay checks and the independent probe rejects
eight hostile mutations. Source, physics ledger, canon, paper and public
posture remain unchanged.
