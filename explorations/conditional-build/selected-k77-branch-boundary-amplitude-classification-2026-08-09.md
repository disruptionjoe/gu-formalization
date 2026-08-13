---
title: "Selected K77 branch boundary-amplitude classification"
status: conditional_result
doc_type: construction_result
created: "2026-08-09"
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
---

# Selected K77 branch boundary-amplitude classification

## Result

Both exact nonzero stationary branches have nonzero endpoint momentum, but
that fact has different consequences on two different gauge objects.

For the residual right-`tau_A0` adjoint orbit, the branch fields are aligned:

```text
Theta = t Phi1,
P = (-312 b^2 - t) Phi1.
```

Therefore `[Theta,P]=0` on each branch. The scalar Hamiltonian vanishes for
all 16,384 Clifford generators on each branch. This is an exact zero moment
map on that named orbit, not an inference from rank.

For the primitive epsilon variation obtained after integration by parts, the
two endpoint values are independent. The same nonzero coefficient pairs with
all fourteen grade-one endpoint parameters, giving rank 14 per endpoint and
rank 28 for their direct sum. It is therefore a live endpoint charge unless a
boundary condition removes it or an edge mode dresses it.

The exact endpoint coefficients are

```text
p_+ = (-3 + 2 sqrt(3))/416 > 0,
p_- = (-3 - 2 sqrt(3))/416 < 0.
```

They are distinct Galois conjugates. Neither the bulk equation nor the source
chooses between them.

## Layer-0 split

| Object | Exact result | Meaning |
|---|---|---|
| residual `tau_A0` adjoint orbit | `[Theta,P]=0` | both branches are uncharged on the aligned orbit |
| primitive epsilon endpoint orbit | rank `14+14` | both branches carry nonzero endpoint charge |
| charged boundary symmetry | two Galois-related sectors | both survive; amplitude labels charge |
| minimal edge completion | unique coefficients `(-1,+1)` | both survive as dressed boundary cotangent values |
| zero-charge/Neumann-like horn | requires `p=0` | excludes both nonzero branches |

Thus “bare gauge” is not a sufficient classification. One must say whether it
means the residual adjoint stabilizer orbit or the derivative-bearing
primitive-epsilon endpoint orbit.

## Symplectic composition

The one-cell preboundary form reproduces the earlier exact horn theorem. The
unextended endpoint orbit is not characteristic. Adding the minimal edge pair
forces coefficients `c_0=-1`, `c_3=+1`; the resulting six-dimensional form has
rank four and kernel two, exactly the endpoint gauge orbit. Since the branch
coefficient is nonzero, tensoring this cell with the fourteen grade-one slots
does not change the classification.

This does not construct a global BFV phase space. A trace space,
polarization, complete functional gauge group, common analytic domain and
global branch section remain unbuilt.

## Source return

`SOURCE_CONFIRMS_FULL_TILTED_BULK_GRAMMAR_AND_BOUNDARY_DEBT__SOURCE_SILENT_BOUNDARY_GAUGE_ORBIT_POLARIZATION_AND_EDGE_SELECTION`

The source supports the tilted bulk grammar and acknowledges boundary debt.
It does not choose the physical endpoint orbit, the charged/edge/zero-charge
horn, a BFV polarization, either algebraic branch or its amplitude.

## Controls and scope

- Primary exact probe: `51/51 PASS`.
- Independent Sage/FLINT route: `20/20 PASS`.
- A planted misaligned momentum gives a nonzero adjoint moment map.
- Identifying the two endpoint parameters deliberately drops rank from 28 to
  14, showing why endpoint independence matters.
- The generic v0.102 charged fixture remains valid away from the aligned
  branch; it is not retracted.
- Selected Spin-native, two `U(32,32)` halves and full `U(64,64)` remain
  distinct action parents.
- P1/P2/P3 are unchanged and unused.

No verdict, residue, booked quotient, datum, canon statement or public posture
changes. The construction closes the branch-level boundary-horn amplitude
classification only.

## Next gate

Construct the global functional trace space and BFV polarization for the
primitive-epsilon endpoint orbit, comparing the charged and minimal-edge
horns. Keep action-parent selection and the complete functional tangent
separate before Hessian/BV/common-domain work.
