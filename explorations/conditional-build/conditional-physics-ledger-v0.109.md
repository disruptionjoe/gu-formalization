---
title: "Conditional physics ledger v0.109"
status: current
doc_type: ledger_summary
created: "2026-08-09"
---

# Conditional physics ledger v0.109

`82/82` targets remain mapped: `32 SAME`, `19 DIFFERS`, `26 NEEDS`, and
`5 OVER-DETERMINED`. Residue remains `84..86` continuous parameters, at least
19 function-valued slots and nine discrete forks. Five scoped quotients remain
booked.

This version corrects the v0.108 local-freedom claim by returning to the
source field space. Weinstein's first action owns `(epsilon,varpi,g)`, not
independent `(B,T,g)`: `B` is epsilon-derived and `T=varpi-B`. Consequently
the arbitrary `B`-at-fixed-`T` equation that made the v0.108 Jacobian rank
three is a reconstruction condition, not a source Euler equation.

In invariant scalar-jet coordinates

```text
F_B=f(Phi1 wedge Phi1),  D_B T=u(Phi1 wedge Phi1),  T=t Phi1,
```

the source translation residual and metric-volume trace have rank two and
give the exact family

```text
f=t^2/3,
u=-t/312-4t^2/3.
```

Three invariant values minus two equations leave one common amplitude. This
realizes Weinstein's limited “two problems to one” shape locally; it does not
select a dark-energy magnitude. The v0.108 point
`(b,t,r,s)=(1/208,-1/104,1/129792,0)` remains an exact member of the family,
but is not a unique source vacuum.

An explicit rational noncommuting fixture constructs a local connection and
`T` one-jet for the family, verifies endpoint and path-average curvature,
passes differential Bianchi at the point, and descends covariantly across
three constant-transition patches. Nonconstant connection transitions,
the epsilon equation and `Xi=D_omega Upsilon` prolongation, an
open-neighborhood/global solution, observation descent and amplitude
selection remain open.

Seven rows migrate in distance, frontier grade and evidence only: `LT-GR1`,
`LT-GR2b`, `LT-GR2c`, `LT-GR2d`, `LT-GR3`, `LT-GR5`, and `LT-GR6`. No verdict,
reason kind, global residue, booked quotient, datum, canon statement or public
posture changes. The selected Spin-native, two `U(32,32)`-half and full
`U(64,64)` parents remain distinct; P1/P2/P3 remain unused.

Next: construct nonconstant three-patch connection descent including the
affine term, then close the epsilon Euler/formal-prolongation ideal on the
family and test whether it extends off the point or selects the amplitude.
Only afterward select the 321-versus-1,571 tangent and resume Hessian/BV.

Machine ledger: `lab/process/conditional-physics-ledger-v0.109.json`.
