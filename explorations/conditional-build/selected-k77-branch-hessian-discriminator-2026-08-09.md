---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: NAIVE_RECONSTRUCTION_HESSIAN_SELECTOR_FALSIFIED__SOURCE_VARPI_RESTRICTIONS_SAME_INERTIA__BOTH_BRANCH_PORTS_REQUIRED
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 branch-Hessian discriminator

## Plain English result

The two nonzero source-action branches initially appeared to have different
stability types: one displayed second-derivative matrix is a saddle and the
other is negative definite. That difference is real arithmetic, but it is not
a physical branch selector. The calculation varied a reconstructed connection
coordinate that is not independently owned by the source, and neither branch
is stationary in that direction. Away from a critical point, a nonlinear
coordinate change can change the Hessian's rank; the exact probe does so.

Restricting instead to the scalar `varpi` direction the source actually owns
gives the same invariant verdict on both branches:

- first transgression action: both quadratic coefficients are negative;
- separate `||Upsilon||^2` action: both coefficients are positive and rank one,
  up to the nonzero parent pairing orientation.

The coefficients are not numerically equal, so this is not permission to copy
one branch's complete operator to the other. It means only that the scalar
source slice does not select between them. Both full branch ports remain
necessary.

## Exact discriminator

For

```text
I1 = 7 t [624(b^2 + bt + t^2/3) + t]
Upsilon = 312(b+t)^2 + t,
```

both algebraic points obey `dI1/dt=0` and `dI1/db != 0`. Their displayed
two-coordinate determinants are `588(3-2 sqrt(3))<0` and
`588(3+2 sqrt(3))>0`. Under `b=b0+x+c x^2`, the `xx` entry gains
`2c dI1/db`; exact `c` makes either determinant zero. The apparent Morse
difference is therefore not an invariant of the source problem.

On the source `t` line the first-action coefficients are

```text
14(sqrt(3)-2),  -14(sqrt(3)+2),
```

both negative with positive ratio `7-4 sqrt(3)`. At a zero of `Upsilon`, the
residual-square Hessian is `dUpsilon tensor dUpsilon`; its source-line
coefficients are `7-4 sqrt(3)` and `7+4 sqrt(3)`, both positive.

## Parent and analytic boundary

The shared scalar line exists inside the selected Spin carrier, both separate
`U(32,32)` halves and the full `U(64,64)` comparator. Nothing here selects one.
The exact boundary symplectomorphism also survives, but it does not identify
bulk Hessians. No Krein positivity, principal symbol, contour, domain, vacuum
selection or quantum measure follows.

## Accounting and next gate

```text
new fields/coefficients/selectors/bundle classes/quotients: 0
P1/P2/P3 consumed: 0
conditions closed/opened/remaining: 1 / 0 / 6
```

Primary certificate: `46/46 PASS`. Independent Sage/FLINT: `15/15 PASS`.

Next port the actual first-action epsilon/Cl1 cross and the residual-square
metric/varpi/epsilon Jacobian to **both** stationary branches and each retained
parent. Do not transfer real Hessian or positivity data by Galois analogy.
