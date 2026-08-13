---
title: "Selected K77 I2B constrained-observer Euler/Ward stratification"
status: exploration
created: 2026-08-12
canon_verdict_change: none
---

# Selected K77 I2B constrained-observer Euler/Ward stratification

## Result

The conditional observer completion of the current `SC-ACT-04` principal
response has an exact constrained Euler equation, but its ability to select an
observer is state-dependent.

Let `x` be the 16 real coefficients of the complete live response, ordered as
four principal rows of four moving-Higgs coordinates.  For a unit timelike
observer `u`, use

```text
H(u)       = i B gamma(u),
H(u)^-1    = -i gamma(u) B,
S_u(x)     = 1/2 Re Tr(H(u)^-1 R(x)^dagger H(u) R(x))/128.
```

The inverse side is load-bearing.  In an adapted Lorentz frame, the exact
observer-tensor coefficient matrices are

```text
C_00 = diag(-8 I4, +8 I12),
C_11 = C_22 = C_33 = -8 I16,
C_ab = 0 for a != b.
```

Writing

```text
A = x_0^2+x_1^2+x_2^2+x_3^2,
B_live = x_4^2+...+x_15^2,
```

the raised tensor has eigenvalues

```text
lambda_time  = -8 A + 8 B_live,
lambda_space =  8 A + 8 B_live  (multiplicity three),
gap          = -16 A.
```

The constrained observer equation is the eigenline equation

```text
Pi_(u-perp) C(x) u = 0.
```

It therefore has two exact strata:

- `A>0`: the timelike line is simple.  The constrained action Hessian on the
  three-dimensional observer fibre is `-16 A I3`.  This is an isolated local
  extremum of the conditional principal action and supplies a state-dependent
  line without adding a continuous observer datum.
- `A=0`: the raised tensor is `8 B_live I4`.  Even for a nonzero response the
  action is exactly observer-flat and selects no line.

The negative Hessian sign is not a positivity or stability theorem in the
indefinite action.  It establishes local nondegeneracy only.

## Ward identity versus observer equation

Changing `u` while holding the response fixed, and moving `u`, the response
and the Spin frame together, are different operations.

For each of the three boost directions and every one of the eight live
Clifford masks, exact infinitesimal sharp covariance holds:

```text
delta(X sharp_u) = [kappa, X sharp_u].
```

Trace cyclicity therefore gives a zero simultaneous-orbit derivative on all
`3 x 16^2 = 768` live pairings.  That is the co-moving Ward identity.  The
fixed-field constrained equation instead produces the eigenline and Hessian
above.  The Ward identity does not erase the state-dependent Euler equation.

## Layer-0 and source fence

- `SC-ACT-04` asserts the bosonic residual-square equation; the source does
  not print `H_u`, this observer tensor or its variation.
- `SC-META-50` admits the number of temporal dimensions as sectoral input; it
  does not supply a unit observer field.
- This tensor is the derivative of the conditional observer-completed
  principal action.  It is not yet the physical stress-energy tensor.
- The simple eigenspace is a **line**.  Since `S_-u=S_u`, no time arrow or ray
  is selected.
- RB4's moving associated family, this Euler equation, a coupled
  metric/section/gauge contact tensor, a BV quotient and a closed analytic
  domain remain different objects.
- Source `C^(32,32)+C^(32,32)`, derived
  `U(32,32)xU(32,32)`, full `U(64,64)` and independently varied connections
  remain distinct.

## Hostile scope

The strongest objection is adapted-frame circularity.  A coordinate
calculation that puts the candidate line at `e0` cannot by itself prove that
the geometry reconstructs the line.  Two controls prevent the strongest
version of that objection:

1. v0.216 already proves exact diagonal Spin/frame naturality; and
2. the simple-eigenline condition is the invariant spectral statement that
   the raised observer tensor has gap `-16 A`.

That is enough for a **local associated-family selection theorem** on `A>0`.
It is not enough for a global physical observer: the complete arbitrary-field
action, observation-section contact, overlap compatibility and a common line
across the nonlinear solution remain unbuilt.  The `A=0` stratum is a firing
counterexample to any unconditional selection claim.

## Accounting

No datum, residue, quotient or P1/P2/P3 entry moves.  The previously unbooked
three-function observer cost is conditionally avoided only on the `A>0`
principal stratum.  It remains open on the flat stratum and before global
coupled completion.

## Verification

`selected_k77_i2b_constrained_observer_euler_ward_probe.py` passes
`51 exact + 3 planted = 54`.  It computes all ten observer-tensor blocks,
the constrained Hessian, simple and flat fixtures, the corrected finite boost,
the `u -> -u` arrow obstruction and the 768-pairing Ward theorem.

## Next gate

Compose this observer tensor with the moving metric/Hodge/Shiab/projector and
observation-section contact terms of the full `SC-ACT-04` Euler map.  Test
whether the simple timelike line persists, becomes the eigenline of a genuine
physical stress/current tensor, or is destroyed by coupled contact.  The
`A=0` stratum is the mandatory control.  Only after that may the conditional
observer cost be removed globally or priced as external.
