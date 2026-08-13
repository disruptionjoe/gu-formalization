---
title: "Selected K77 I2B residual-owner and two-connection tangent source return"
date: 2026-08-12
status: SOURCE_COLLISION_COMPLETE
source_return: SOURCE_CORRECTS_SC_ACT_04_OWNER_TYPING__LITERAL_I2B_SQUARES_PRINTED_ENDPOINT_UPSILON__ACTION_CONSISTENCY_LEAVES_CORRECTED_E_ACT_SQUARE_AS_SEPARATE_RIVAL
---

# Source return

## Question

The v0.201--v0.224 Higgs chain called

```text
Upsilon_path = Shiab(F_B + 1/2 D_B T + 1/3 T wedge T) + kappa *T
```

the source-owned `SC-ACT-04` residual.  It then proposed cancelling the
remaining translation Euler covector with a Frechet response of a geometric
background `F0(A,g,epsilon)`.  This return checks both typings against the
already extracted draft formulas.

## What the released source displays

For `A=B+T`, the first action contains the path-average curvature

```text
Fbar = F_B + 1/2 D_B T + 1/3 T wedge T.
```

Its displayed translation variation is instead written using the endpoint

```text
Upsilon_print = Shiab(F_A) + * kappa T.
```

The second action is then printed as

```text
I2B = ||Upsilon_B||^2.
```

The repository has already proved that, for the selected noncyclic Shiab on
the full translation domain, the printed endpoint is not the derivative of
the first action.  The variationally owned covector is the third object

```text
E_act = Shiab(Fbar) + L_T^! Shiab^! T + * kappa T.
```

Accordingly there are two live readings of `I2B`:

1. the **literal draft reading**, which squares `Upsilon_print`; and
2. an **action-consistent corrected reading**, which would square `E_act`.

The path-average bracket by itself is neither one.  It remains a legitimate
repository construction, but its attribution as literal `SC-ACT-04` ownership
is withdrawn.

## Two-connection tangent ownership

The source varies `varpi` as `varpi+s alpha` while the gauge-rotated reference
connection is held fixed in the displayed translation derivative.  In the
coordinates `A=B+T`, this is

```text
delta B = 0,
delta T = alpha,
delta A = alpha.
```

Therefore a term depending only on `B`, the metric, or the observation
section at fixed `B` has zero derivative in this independent translation
direction.  Such a term cannot cancel a nonzero `T`-Euler coefficient merely
by being called the geometric background.  It could contribute only if its
actual definition depends on `A/T`, or if the source action derives a coupled
tangent graph or BV reduction.

## Disposition

- `SOURCE-CORRECTS`: literal `SC-ACT-04` squares the printed endpoint
  `Upsilon`, not the one-third path-average bracket.
- `REPO-CORRECTS-SOURCE-VARIATION`: the action-consistent `E_act` remains a
  separate rival because the printed endpoint is not the first-action
  derivative for the selected Shiab.
- `SOURCE-CONFIRMS-FULL-TRANSLATION-DIRECTION`: the displayed variation is not
  restricted to the four-real Higgs tangent.
- `SOURCE-SILENT`: no coupled `delta B=L delta T` graph, odd BV quotient, or
  background-only cancellation of the translation equation is published.

No verdict, canon statement, datum, quotient, or public posture changes here.
