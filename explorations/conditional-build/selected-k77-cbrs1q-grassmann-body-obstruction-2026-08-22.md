---
title: "Selected-K77 CBRS-1Q Grassmann-body obstruction"
status: active_research
doc_type: exact_superalgebra_body_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1q-grassmann-body-obstruction.json
probe: tests/channel-swings/selected_k77_cbrs1q_grassmann_body_obstruction_probe.py
grade: "EXACT POINTWISE SUPERALGEBRA BODY THEOREM FOR AN EVEN BILINEAR GRASSMANN-ODD EXTENSION; NO SOURCE OPERATOR, BV, GLOBAL VACUUM OR SPECTRUM"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_INDEPENDENT_BARRED_UNBARRED_FERMION_FIELDS_AND_BILINEAR_ACTION_GRAMMAR__REPOSITORY_DERIVES_THE_BODY_OBSTRUCTION__SOURCE_SILENT_ON_A_NONZERO_ODD_SADDLE_CONDENSATE_AND_COMPLETE_K77_OPERATOR
canon_verdict_change: none
---

# Selected-K77 CBRS-1Q Grassmann-body obstruction

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
result: CBRS-1Q exact Grassmann-body obstruction for the minimal bilinear coupled-fermion class
carrier: four CBRS-1P real J4 bosonic point carriers extended over a finite supercommutative coefficient algebra by independent barred and unbarred odd fields LAYER=ambient CHIRALITY=N/A
pairing: even bilinear fermion action psibar D(b) psi composed with the selected bosonic action ON=pointwise_superfield_carrier
real_structure: rational Grassmann algebra for the theorem fixtures plus the CBRS-1P normalized real K77 branch registry
grading: Z2 super-parity and Grassmann degree kept distinct from Clifford grade and q-mod-J4 component grade
action_owner: repository-construction
target: body projection of the coupled Euler and Hessian equations MAP-TYPE=evaluation
```

## Result first

CBRS-1Q closes the minimal coupled-fermion extension as a route to a **real**
non-orbit metric tangent on the four J4 branches. Freeze the even action class

```text
S(b, psibar, psi) = S_B(b) + psibar D(b) psi,
```

where `psi` and `psibar` are independent Grassmann-odd classical fields and
`b` denotes all even bosonic coordinates. Let `body` be the quotient that
sets the nilpotent ideal to zero. Then

```text
body(psibar (dD/db) psi) = 0,
body(psibar (dD/db))     = 0,
body((dD/db) psi)        = 0,
body(psibar (d2D/db2) psi) = 0.
```

Thus the body of the coupled bosonic Euler equation is exactly the bosonic
Euler equation, the body of both even/odd mixed Hessian blocks is zero, and the
even-even body Hessian is exactly `H_B`. A nonzero fermion kernel may survive
in the odd block, but it cannot enlarge the real even-body kernel.

CBRS-1P proves that each complete `230650`-dimensional J4 bosonic Hessian has
rank `230610`, nullity `40`, and kernel exactly equal to the 40-dimensional
broken diagonal-Spin gauge orbit. Applying the body theorem therefore leaves
zero real non-orbit metric body dimension on every branch.

## Why this is not the zero-fermion replay

The earlier current-order theorem evaluated the same even bilinear grammar at
`psi=psibar=0`. CBRS-1Q admits a genuinely nonzero odd saddle. In the exact
fixture,

```text
psi_0    = theta_0,
psibar_0 = theta_1,
x        = -(psibar_0 psi_0)/2,
D(x,y)   = diag(x,1+y).
```

Both fermion Euler rows vanish by nilpotence. The coupled bosonic equation
`2x+psibar_0 psi_0=0` also vanishes. The backreaction and the correction `x`
are nonzero, so the fixture is not the zero-field solution; nevertheless both
have zero body. Its mixed super-Hessian entries are nonzero odd elements whose
body is zero, while the even body Hessian keeps exactly its original gauge
zero and no new physical even null.

This sharpens the earlier result: allowing a nonzero Grassmann-odd saddle does
not revive a real metric tangent inside the minimal bilinear class.

## Exact theorem

Let `A=A_0+A_nil` be a supercommutative algebra over a characteristic-zero
field and let

```text
body : A -> A/A_nil
```

be its body map. For odd `psi,psibar`, their product lies in the even
nilpotent ideal, so every bilinear current has zero body. Differentiating the
action gives

```text
E_b      = dS_B/db + psibar (dD/db) psi,
E_psibar = D(b) psi,
E_psi    = psibar D(b).
```

The body equations are therefore

```text
body(E_b) = dS_B/db at body(b),
body(H_bb) = H_B at body(b),
body(H_b,psi) = body(H_b,psibar) = 0.
```

The conclusion does not require `D` to be invertible or known explicitly. It
also does not say the fermion block has no kernel. It says only that an odd
kernel and its nilpotent backreaction are not a real even metric direction.

## Route and prior-art controls

Repository retrieval found no prior artifact applying the body projection to
a nonzero odd saddle on the CBRS-1P J4 branches. The closest result is the
2026-08-10 zero-fermion direct-sum theorem; CBRS-1Q extends rather than reruns
it. The older full-carrier stationary residual and `64x64` Schur work remain
useful for locating fermion modes, but a `D(varpi)` determinant search cannot
change the body theorem.

The probe implements an exact rational Grassmann algebra with four generators:

- odd squares vanish and distinct generators anticommute;
- the body map is multiplicative;
- eight deterministic bilinear fixtures have zero current body and zero mixed-
  block body;
- the explicit nonzero odd saddle closes all Euler rows exactly; and
- the four CBRS-1P rank/nullity/gauge-kernel rows are imported from their
  native registry rather than recomputed.

## Contrary classes

Two planted controls genuinely move the real body equation:

1. replacing the odd fields with commuting c-number spinors gives a nonzero
   body current; and
2. promoting `psibar psi` to an independently body-valued even condensate or
   bosonized auxiliary field also gives a nonzero body source.

Both plants fire. They prove that super-parity and object ownership, rather
than an accidental coefficient cancellation, carry the theorem. They are not
escapes inside the admitted class:

- a commuting spinor changes the field parity and is not the source fermion;
- an even condensate or auxiliary field adds a new bosonic owner, potential,
  stationarity equation and Hessian; and
- changing `S_B`, adding a counterterm or choosing a commutant coefficient
  after the J4 result likewise defines a new action class.

## Hostile review and ceiling

- **Strongest parity overclaim:** a Grassmann-odd classical saddle is not a
  c-number fermion condensate. The latter is an even composite expectation or
  auxiliary field and is explicitly outside this theorem.
- **Strongest kernel overclaim:** a fermion zero mode may exist even when the
  real metric body quotient is zero. Finite odd kernel, stationary kernel,
  characteristic kernel and BV cohomology remain distinct.
- **Strongest geometric overclaim:** this is pointwise superalgebra on the four
  constant J4 bodies, not a spacetime-nonhomogeneous solution, global
  stabilizer, analytic domain or spectrum.
- **Strongest source seam:** the source supplies nearby independent barred and
  unbarred bilinear grammar, but no complete K77 `D`, nonzero odd saddle,
  condensate action or selection of these J4 branches.
- **Strongest propagation seam:** the theorem imports CBRS-1P's exact kernel
  equality. It does not rerun the 140 transport classes, reinterpret a rank-
  bad prime, or claim anything beyond the real even-body quotient.

No ledger verdict, canon, source ownership, residue, particle assignment,
prediction, confirmation or public posture changes.

## Reverse-scaffold consequence

The minimal bilinear Grassmann-odd extension cannot supply CBRS-1's missing
real metric tangent. Continue with `CBRS-1R`: freeze one materially distinct,
target-blind **even** owner before solving it—an action-derived condensate,
bosonized auxiliary field, or another independently specified bosonic action
class—and require its own body stationarity, full metric variation and complete
tangent. The actual `D(varpi)` determinant locus remains useful for fermion
mode ownership, but it is not a metric-body reopener by itself.

Do not reinterpret a commuting-spinor plant as a fermion vacuum, tune J4, add
a counterterm, mix the full `{1,J4,J10,Omega}` commutant after reading the
result, or advance to CBRS-2.

Reproduce with:

```bash
python3 \
  tests/channel-swings/selected_k77_cbrs1q_grassmann_body_obstruction_probe.py
```
