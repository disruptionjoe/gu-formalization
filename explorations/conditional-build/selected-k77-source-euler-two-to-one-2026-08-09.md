---
artifact_type: construction_result
created: 2026-08-09
status: SOURCE_EULER_TWO_TO_ONE_FAMILY_EXACT__V0108_UNIQUENESS_RETRACTED__LOCAL_ONE_JET_REALISABLE
source_return: SOURCE-CORRECTS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_source_euler_two_to_one_probe.py
  - tests/channel-swings/selected_k77_source_euler_two_to_one_independent.sage
registry: lab/process/selected-k77-source-euler-two-to-one.json
---

# Selected K77 source-Euler two-to-one family

## Result first

The previous exact rational point survives, but its claimed uniqueness does
not. The source action does something both more modest and more physically
apt: it identifies the curvature-side and distortion-side quantities strongly
enough to leave **one common amplitude rather than two independent ones**.
It does not derive the amplitude.

The correction is Layer 0. Weinstein's displayed source fields are
`(epsilon,varpi,g)`. The connection `B` is derived from `epsilon`, while
`T=varpi-B`. Varying `varpi` moves `T` at fixed `B`; varying `epsilon` moves
`B` and `T` oppositely and supplies the `Xi=D Upsilon` companion. The v0.108
equation obtained from arbitrary `B` at fixed `T` is not among those source
directions.

## Exact invariant family

Write the scalar cells as

```text
F_B   = f (Phi1 wedge Phi1),
D_B T = u (Phi1 wedge Phi1),
T     = t Phi1.
```

The source translation residual and metric-volume trace are

```text
312(f+u+t^2)+t = 0,
624(f+u/2+t^2/3)+t = 0.
```

Their coefficient matrix on `(f,u)` has rank two and determinant `-97344`.
The complete solution is

```text
f = t^2/3,
u = -t/312 - 4t^2/3.
```

Thus three invariant values minus two equations leave one local amplitude.
This is the precise constraint-surplus form of Weinstein's stated bar: two
problems become one. It is not a first-principles magnitude prediction.

The v0.108 values

```text
b=1/208,  t=-1/104,  r=1/129792,  s=dT=0
```

give `f=b^2+r=t^2/3` and
`u=2bt+s=-t/312-4t^2/3`, so their exact cancellation remains valid. The
extra equation `2b+t=0`, together with `s=0`, merely selects this convenient
representative from the invariant family.

## Local geometric realization

The family is not only scalar arithmetic. At a point in normal gauge choose

```text
B_i(p)=0,
partial_i B_j(p)=F_ij/2,
T_i(p)=t Phi1_i,
partial_i T_j(p)=U_ij/2.
```

Antisymmetrization gives the prescribed `F_B` and `D_B T`. An explicit
noncommuting rational matrix fixture verifies the endpoint curvature, the
`1/2,1/3` path-average curvature, and the differential Bianchi identity at
the point. Noncommuting constant transitions on three patches give identical
direct and sequential conjugation for both covariant two-forms.

This is a local connection/`T` one-jet theorem. It does not include the affine
`g^-1 dg` term of nonconstant transitions, higher jets, or an open-neighborhood
solution.

## What is corrected and what remains

- Retained: all exact v0.108 arithmetic at its rational point.
- Retracted: “three source equations,” “zero local freedom,” and uniqueness of
  that point as a source-field vacuum.
- Established: an exact one-amplitude source-Euler family and a local
  connection/`T` one-jet with point Bianchi and constant-transition descent.
- Open: nonconstant atlas descent; the epsilon equation and formal
  prolongation `Xi=D_omega Upsilon`; open-neighborhood/global existence;
  observation descent; amplitude selection; magnitude, screening and FLRW;
  the 321-versus-1,571 tangent, Hessian, BV and common domain.

The one local amplitude is not booked as an added global residue until its
functional ownership and quotient status are reconciled. P1/P2/P3 remain
unchanged and unused. The selected Spin-native parent, two `U(32,32)` halves,
and full `U(64,64)` comparator remain distinct.

## Validation

- primary exact route: `45/45 PASS`;
- independent Sage/QQ route: `18/18 PASS`;
- an explicit normal-gauge family member fires the planted claim that the two
  source equations imply `2b+t=0`;
- point Bianchi is not promoted to a neighborhood theorem;
- constant-transition descent is not promoted to nonconstant atlas descent.

## Next gate

Construct nonconstant three-patch connection descent including `g^-1 dg`,
then write the epsilon equation and `Xi=D_omega Upsilon` as an actual formal
prolongation on the source family. Decide whether the family extends off one
jet and whether source geometry or boundary/global conditions select its
amplitude. Only then choose the 321-versus-1,571 tangent and resume Hessian/BV.
