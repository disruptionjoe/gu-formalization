---
title: "VRS-4 moving-J total-descent conditional theorem"
status: active_research
doc_type: reverse_superposition_conditional_descent_theorem
created: "2026-08-14"
lane_id: SRC-RES-COH-01
claim_grade: "TYPED CONDITIONAL QUOTIENT THEOREM AND CURRENT OBSTRUCTION INVENTORY; NO INSTANTIATED TOTAL COMPLEX OR PHYSICAL COHOMOLOGY"
registry: lab/process/superposition-vrs4-moving-j-total-descent-conditional-theorem.json
probe: tests/channel-swings/superposition_vrs4_moving_j_total_descent_probe.py
canon_verdict_change: none
---

# VRS-4 moving-J total-descent conditional theorem

## Result first

For a real total deformation complex

```text
G --K_total--> E_total --L_total--> R_total,
L_total K_total = 0,
```

a moving family `J_E` defines a complex structure on the physical quotient
`ker(L_total)/closure(im(K_total))` only if there are typed companion maps
`J_G` and `J_R` such that

```text
J_E^2 = -1 on ker(L_total),
J_E K_total = K_total J_G,
L_total J_E = J_R L_total,
J_E closure(im K_total) = closure(im K_total),
J_E Dom(L_total) = Dom(L_total),
```

and every boundary trace/Green condition defining the physical domain is
`J_E`-invariant. A descended nondegenerate or positive pairing additionally
requires its own basicness, domain and compatibility conditions. These are
necessary and sufficient algebraic/topological descent conditions once the
closed complex and domains exist.

The current moving associated-spinor `J10` does not yet meet that theorem. The
repository owns `sJ10=[c,J10]` and fibrewise associated-bundle covariance, plus
conditional observed-symbol complex linearity. It does not own extensions of
`J10` across the bosonic, ghost and charged boundary sectors; total `K/L`;
invariance of a common closed Green domain; or a descended positive pairing.

The exact disposition is

```text
GENERAL_TOTAL_DESCENT_THEOREM_ESTABLISHED
__MOVING_J10_REMAINS_FIBREWISE_GAUGE_COVARIANT_ONLY
__TOTAL_INTERTWINERS_BOUNDARY_DOMAIN_AND_PAIRING_TYPE_MISSING.
```

## Why moving covariance is not quotient descent

The identity `sJ=[c,J]` says that `J` transforms naturally with the moving
split. It does not say that one fixed endomorphism is basic on gauge orbits,
nor does it construct `J_G`, `J_R`, or the boundary component of `J_E`.
Quotient descent is controlled by the two intertwining squares above. The
previous exact rank-eight mixed-gauge failure shows why fixed `J10` cannot
replace them.

## Sector-by-sector status

| sector | current status | required before descent |
|---|---|---|
| associated fermion | moving `J10` fibrewise exact | extension to the actual total fermion operator/domain |
| bosonic field tangent | no selected square-minus-one map | typed `J_E` component and `K/L` compatibility |
| ghosts/reducibility | algebraic BFV data is incomplete/properness-sensitive | companion `J_G` through the full reducible complex |
| residual/antifield | real Hessian receiver only | companion `J_R` and action-owned intertwiner |
| charged boundary | indispensable on the live branch | `J`-invariant BFV/Green boundary domain |
| pairing | action pairings are not positive physical metrics | basic nondegenerate pairing, positivity and completion |

## Exact controls

The probe constructs a finite exact complex with compatible `J_G,J_E,J_R` and
checks that `J_E` induces square `-1` on the quotient. It then fires independent
negative controls for the `K` intertwiner, `L` intertwiner, invariant boundary
domain, and pairing compatibility. These controls establish the theorem's
logical independence; they do not instantiate the GU total complex.

## Exhaustion and next gate

VRS-4 returns a conditional theorem with missing data, not a kill of `H-Q*`.
It closes the present reverse typing sequence VRS-1 through VRS-4 and makes the
forward dependency exact:

1. VRS-5 must construct and held-out validate `O_SR1C`, then the minimal
   compatible two-jet and full fixed-`varpi` metric row.
2. If a legal stationary background survives, VRS-6 must instantiate one
   bulk-fermion-ghost-boundary `K_total/L_total` and test the conditions above.
3. Only VRS-7 may test descended positivity, common domain, evolution and the
   final `H-Q*` versus `H0` fork.

No physical cohomology, Hilbert space, superposition, Born rule or empirical
prediction follows here.
