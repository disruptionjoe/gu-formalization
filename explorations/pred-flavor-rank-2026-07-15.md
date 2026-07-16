---
artifact_type: exploration
status: exploration
created: 2026-07-15
run_id: GUH-20260716T001233Z-flavor-rank
title: "PRED-FLAVOR-RANK -- basis-invariant Yukawa freedom after the built GU texture"
result: NO_GO
grade: "Computed finite-dimensional rank certificate on the H28 reduced coefficient space; source-action construction not supplied."
scripts:
  - tests/yukawa-scoping/pred_flavor_rank.py
depends_on:
  - explorations/yukawa-scoping-2026-07-13.md
  - tests/yukawa-scoping/yukawa_trilinear_channels.py
  - tests/W239_track_b_distinctive_prediction_scan.py
---

# PRED-FLAVOR-RANK -- current zero-parameter flavor route

Test: `python tests/yukawa-scoping/pred_flavor_rank.py`.

## Decision Question

Does the built GU-native flavor structure leave a basis-invariant, zero-free-coefficient Yukawa relation
that can be frozen before data confrontation?

## Construction Fork

The primary fork is the GU-native transpose-bilinear channel from H28: the scalar Dirac-Yukawa channel is
unique at the Spin(9,5) level, and the derived generation `Z/3` acts on the three generation slots. In the
charge eigenbasis, the built transpose-bilinear condition is

```text
P^T Y P = Y.
```

This leaves exactly the support

```text
{(0,0), (1,2), (2,1)}.
```

The standard-physics comparison fork is ordinary flavor-basis freedom: after singular-value decomposition,
a generic Dirac Yukawa matrix still has three mass magnitudes. The GU texture reduces support but does not
reduce the number of independent magnitudes.

The Krein/sesquilinear comparison fork, `P^dag Y P = Y`, is also checked; it leaves a diagonal 3-dimensional
texture. It does not create a prediction either.

## Rank Receipt

The full generation Yukawa coefficient space has complex dimension 9. The built GU-native `Z/3` texture
reduces it to complex dimension 3, represented by three coefficients:

```text
y00, y12, y21
```

Allowed left/right basis rephasings remove the three phases of those coefficients. They do not change
magnitudes. Therefore the quotient still has three positive magnitude moduli.

If one overall source normalization is treated as free, two dimensionless ratios remain:

```text
|y12| / |y00|
|y21| / |y00|
```

The certificate also gives a basis-and-scale counterexample: `(1, 2, 5)` and `(1, 3, 7)` are both allowed
GU-texture triples but have inequivalent normalized singular-value ratios.

## Result

`NO_GO` for the current zero-parameter mass/mixing prediction route.

The strongest honest result is:

- GU supplies a real texture hook: `9 -> 3` support reduction.
- The current built structure supplies no coefficient values, no ordering, no mass ratio, and no mixing
  relation.
- Three magnitudes remain free after phase quotient.
- Two dimensionless ratios remain free after discarding one overall source normalization.

This closes the protected primary lane at the current construction grade. It does not prove flavor is
impossible in GU; it says the present built structure is not yet a zero-parameter flavor predictor.

## What Did Not Change

No canon, verdict, claim status, `bar(b)`, H59, generation-count status, public posture, or paper status
changes.

## Residual

The next lawful prediction lane is `PRED-NORM-RANK`: count normalization and field-rescaling invariants among
`kappa`, `Z_U`, `mu_DW`, source normalization, and physical pole parameters, without importing a target
observable to fix the scale.

Priority signal for the daily steward: the protected primary has reached a decision-grade `NO_GO`; activate
`PRED-NORM-RANK` unless a stronger dependency signal arrives first.
