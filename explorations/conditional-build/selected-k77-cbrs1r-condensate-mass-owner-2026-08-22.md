---
title: "Selected-K77 CBRS-1R even-condensate quadratic owner"
status: active_research
doc_type: exact_condensate_action_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1r-condensate-mass-owner.json
probe: tests/channel-swings/selected_k77_cbrs1r_condensate_mass_owner_probe.py
grade: "EXACT RECONSTRUCTION-GRADE POINTWISE MINIMAL EVEN-CONDENSATE OWNER OBSTRUCTION; NO SOURCE CONDENSATE, GLOBAL VACUUM OR SPECTRUM"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPOSITORY_FREEZES_THE_EVEN_CONDENSATE_OWNER_AND_DERIVES_THE_OBSTRUCTION__SOURCE_SILENT_ON_THE_CONDENSATE_AND_CLASS
canon_verdict_change: none
---

# Selected-K77 CBRS-1R even-condensate quadratic owner

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1R exact minimal even-condensate action and complete J4 tangent obstruction
carrier: complete 230650-dimensional real CBRS-1P T-plus-independent-Spin-connection carrier extended by one real body-valued even scalar LAYER=ambient CHIRALITY=N/A
pairing: selected K77 action-density pairing with the existing quadratic owner multiplied by phi squared and a unit symmetric double-well potential ON=pointwise_condensate_extended_carrier
real_structure: normalized real K77 J4 radical branches plus the real algebraic scalar phi
grading: Clifford and form grades inherited unchanged; phi is Z2-even and is not a Grassmann-odd fermion or Clifford-grade selector
action_owner: repository-construction
target: body stationarity complete field-plus-condensate Hessian and intrinsic MET(X) row MAP-TYPE=evaluation
```

## Result first

CBRS-1R freezes the smallest nontrivial body-valued owner suggested by
CBRS-1Q. Split the selected first action uniquely by homogeneity as

```text
S_B(T) = C3(T) + Q2(T),
```

where `C3` is cubic and `Q2` is quadratic, and add one real even scalar with
the target-blind unit action

```text
S_R(T,phi) = C3(T) + phi^2 Q2(T) + (phi^2-1)^2/4.
```

The scalar owns both the quadratic coefficient and its double-well potential.
No coefficient is fitted to a J4 radical, Hessian eigenvalue, desired density
or metric row.

The class does not reopen CBRS-1. The normal-J4 pair produces four exact real
field-plus-condensate saddles, one for each J4 radical sign and each sign of
`phi`. The base-J4 pair has negative exact continuation discriminant and no
real nonzero condensate saddle on its frozen ray. At every real normal-J4
saddle, the complete `230651`-dimensional Hessian has rank `230611`, nullity
`40`, and kernel exactly equal to the inherited broken diagonal-Spin gauge
orbit. The scalar supplies no extra zero and the non-orbit quotient is zero.

The full intrinsic `MET(X)` equation closes the apparent rescue. Every real
normal-J4 condensate saddle has strictly positive nonzero total action density
and zero graph-visible connection momentum, so its intrinsic metric row is
nonzero. None of the four J4 bodies becomes fully metric stationary.

## Frozen action and exact radial solve

Let `T0` be any nonzero critical point of `C3+Q2`, with action density `I0`.
Euler homogeneity gives

```text
Q2(T0) = 3 I0,       C3(T0) = -2 I0.
```

For a continuation with `T=r T0` and `phi` nonzero, the complete field Euler
equation and the scalar equation reduce exactly to

```text
r = phi^2,
6 I0 r^2 + r - 1 = 0.
```

This is not merely a reduced-ansatz stationary check. All complete field and
independent connection Euler rows scale by the same homogeneity relation, so
an original zero row remains zero on the transported branch.

For the normal-J4 density

```text
I_N = (101117 + 2732 sqrt(1366))/6096384,
Delta_N = 1 + 24 I_N > 0,
r_N = 2/(1+sqrt(Delta_N)) = 0.8547035090... .
```

Both original radical signs and both choices `phi=plus-or-minus sqrt(r_N)`
give exact real saddles, four in total. For the base-J4 density

```text
I_B = 5(43687 - 4177 sqrt(4177))/6390144,
Delta_B = 1 + 24 I_B = -3.2491308662... < 0.
```

Neither base-J4 radical sign has a real nonzero continuation in the frozen
class. Complex roots are not real body-valued condensates and are not retained.

## Complete tangent without a second 140-class replay

At a real continuation, `T=rT0` and `phi^2=r`. Every complete `T`/connection
Hessian block is therefore exactly `r` times the CBRS-1P Hessian. The mixed
scalar column is controlled by the quadratic gradient. Using

```text
H_B(T0) T0 = -grad Q2(T0)
```

and quotienting the already proved diagonal gauge kernel gives the exact
one-dimensional Schur complement

```text
H_phi/field = 2(2-r).
```

For `r=r_N`, this is `2.2905929819...`, strictly positive. Hence the complete
rank rises by one while the nullity is unchanged:

| branch | dimension | rank | nullity | non-orbit quotient |
| --- | ---: | ---: | ---: | ---: |
| normal J4 sign minus, phi sign minus | 230651 | 230611 | 40 | 0 |
| normal J4 sign minus, phi sign plus | 230651 | 230611 | 40 | 0 |
| normal J4 sign plus, phi sign minus | 230651 | 230611 | 40 | 0 |
| normal J4 sign plus, phi sign plus | 230651 | 230611 | 40 | 0 |

The exact probe also differentiates the displayed five-variable reduced action
independently and finds a full-rank `5x5` Hessian. The full theorem is stronger:
it imports CBRS-1P's complete rank/kernel equality and adds one nonzero Schur
direction, rather than inferring the large tangent from the reduced matrix.

## Full metric variation

At the real saddle, the total on-shell density simplifies to

```text
I_R = (1-r)(3-r)/12 = 0.02597533768... > 0.
```

The scalar potential is part of this density. It cannot be dropped when
varying the metric. The J4 graph-visible independent-connection momentum stays
zero under the homogeneous transport. CC-01 therefore leaves the nonzero
density contribution in the intrinsic metric row. Field-plus-condensate
stationarity does not become `MET(X)` stationarity.

The base-J4 pair fails even earlier, at real body stationarity. Thus the frozen
owner yields zero fully metric-stationary J4 bodies.

## Retrieval, controls and hostile review

Repository retrieval found older conventional condensate potentials, mirror-
gap channels, scalaron auxiliaries and the CBRS-1Q even-condensate plant. None
contains this action-owned promotion of the selected K77 quadratic term, the
normal/base discriminant split, or the complete Schur reduction. Those older
objects remain differently typed comparators or neighboring constructions.

- **Strongest fitting objection:** the zero-Schur condition would require
  `r=2`, which together with stationarity forces `I0=-1/24`. Neither J4
  density has that value. Choosing a potential coefficient branch by branch
  to force it would be exactly the forbidden post-result tuning.
- **Strongest metric objection:** omitting the double-well contribution from
  the on-shell density would compute the wrong `MET(X)` owner. The exact
  nonzero density is load-bearing.
- **Strongest collapse objection:** `phi=0` removes the quadratic action owner.
  Its large cubic-origin degeneracy is action collapse, not a recovered
  physical metric tangent.
- **Strongest parity/source objection:** `phi` is a new real even repository
  field. It is neither the Grassmann-odd source fermion nor a source-attested
  Higgs, condensate or bosonized field.
- **Strongest tangent objection:** the scalar reduced Hessian cannot certify
  the complete tangent by itself. The conclusion uses the exact CBRS-1P
  kernel theorem plus the universal nonzero Schur complement.
- **Strongest geometric objection:** this remains a pointwise ultralocal
  action class. It supplies no nonhomogeneous solution, analytic domain,
  global stabilizer, BV quotient or spectrum.

No ledger verdict, canon, source ownership, residue, particle assignment,
prediction, confirmation or public posture changes.

## Reverse-scaffold consequence

Close the minimal positive ultralocal condensate-induced quadratic owner. Its
normal-J4 saddles are field stationary but fail the full metric equation; its
base-J4 rays are not real; and its complete real tangent has only gauge kernel.

Continue with `CBRS-1S`: before solving, freeze one genuinely nonminimal
target-blind even owner whose derivative, indefinite or otherwise intrinsic
nonfactorizing coupling can enter the metric equation without a fitted
counterterm. Require its own potential, real body stationarity, complete
`MET(X)` variation and full admitted tangent. An affine shift, decoupled scalar,
flat multiplier, branch-dependent coefficient or zero-action prefactor is not
a reopener. Do not tune J4, mix the full commutant after the result, or advance
to CBRS-2.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1r_condensate_mass_owner_probe.py
```

The exact probe passes `42/42` after native propagation.
