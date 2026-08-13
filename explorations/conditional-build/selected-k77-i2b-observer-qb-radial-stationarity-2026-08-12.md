---
title: "Selected K77 I2B observer-Q_B radial stationarity composition"
status: conditional-construction
created: 2026-08-12
run_id: RUN-20260812-223314-gu-i2b-observer-qb-radial-stationarity
lane: 1
channels: [Build, Compose, Source, Verify]
source_disposition: SOURCE-CONFIRMS-QB-SLOT__SOURCE-SILENT-EXACT-QU
free_object_delta: "zero if the conditional observer equation globalizes; no datum is booked"
---

# Selected K77 I2B observer-`Q_B` radial stationarity composition

## Result

The observer-Hermitian pairing that repaired the four-real principal response,
composed through the already-owned Hodge adapter, also gives a nondegenerate
exact pairing on the actual source-action residual family.  This is the first
test in this chain where the same Hodge-adapted candidate pairing
has survived both the kinetic and background-potential sectors.

For

```text
Upsilon_B(r) = a S_q + b H_q,
a = rho + r^2/3,
b = kappa r,
```

and the conditional observer form `H_u=i B gamma(u)`, the exact residual Gram
at a unit basis observer is

```text
             S_q   H_q
S_q          160     0
H_q            0     2.
```

The predecessor trace-`H_q` comparator instead gives

```text
             S_q   H_q
S_q          192     0
H_q            0     0.
```

Thus the old nonzero-but-null displaced-torsion direction was not an invariant
property of the residual.  It was a property of the trace-owned comparator.
The Hodge-adapted observer completion sees it with nonzero norm.

## Exact observer dependence

For an observed vector `u=sum_mu u_mu e_mu`, all four basis Grams are the same
and every cross term vanishes.  Hence

```text
c(u) = u0^2+u1^2+u2^2+u3^2,
Gram_u = c(u) diag(160,2).
```

The held-out rational boost `(u0,u1)=(5/3,4/3)` gives the exact factor
`41/9`, namely `(6560/9,0,82/9)`.  This fixed-field change is not a covariance
defect: v0.218 already proves simultaneous field/frame transport is Ward-zero.
It is the distinct variation needed for the observer Euler equation.

On the future unit hyperboloid,

```text
u0^2-|v|^2=1,    c(u)=1+2|v|^2.
```

For positive residual energy, constrained variation therefore selects the
rest line `v=0`; the supplied time orientation chooses its future sign.  This
is a local conditional selection relative to the residual frame, not yet a
global observer section or time arrow theorem.

## The potential changes—and stays predictive

The composed local action is

```text
I_u(r) = c(u) [80 (rho+r^2/3)^2 + kappa^2 r^2].
```

Its radial Euler equation factors exactly as

```text
dI_u/dr = (2/9)c(u) r [160 r^2 + 480 rho + 9 kappa^2].
```

The nonzero stationary branch is therefore

```text
r^2 = -3 rho - 9 kappa^2/160,
```

not the trace-comparator branch `r^2=-3 rho`.  It exists only when

```text
rho < -3 kappa^2/160,
```

and its exact radial Hessian is `(640/9)c(u)r^2`, positive whenever the branch
is real and nonzero.  This is useful constraint surplus: a pairing introduced
to repair kinetic rank independently changes the vacuum equation and imposes
a threshold.  It was not adjusted to preserve the old branch.

The branch energy is

```text
-3 rho kappa^2 - 9 kappa^4/320 > 0,
```

so the constrained observer Hessian at the rest line is positive as well.
The action no longer hides a nonzero branch behind zero Krein length.

## What this closes

- one conditional `Q_u` now works on the principal kinetic response and on
  the actual `S_q/H_q` residual family;
- the displaced-torsion direction is non-null under that same pairing;
- the restricted radial branch and its existence threshold are exact;
- the nonzero branch locally selects a future observer representative after
  time orientation; and
- the already-built radial Levi-Civita and q-row section variations add zero
  first-order action derivative, while simultaneous Lorentz motion remains a
  Ward direction.

No new field, coefficient, datum, quotient or boundary condition was added.
The observer `u`, `rho` and `kappa` were already present in the composed
predecessors.  Zero data cost is conditional on the local observer equation
globalizing; it is not booked here.

## What remains open

The source prints a `Q_B` slot but does not identify it with this
Hodge-adapted `Q_u`.
Accordingly this is a conditional construction, not source attribution.  The
following remain open:

1. recompute the Hodge-adapted `e3` normal-contact coefficient with moving
   `Q_u`, rather than transferring the old trace-comparator coefficient;
2. vary the complete connection, metric, section, Shiab and gauge owners on
   the shifted stationary background;
3. prove the locally selected observer line descends globally and belongs to
   a common Green/Krein domain;
4. build the preboundary/presymplectic class and gauge/BV quotient; and
5. derive the scalar, Yukawa, photon and mass spectrum after observation.

The two `C^(32,32)` carrier halves, their possible
`U(32,32)xU(32,32)` block subgroup, the full `U(64,64)` parent and independent
connection fields remain distinct.  Neither the pairing nor this calculation
turns two carrier halves into two connections.

## Adaptive preflight and review

The preflight used invariant theory, variational calculus, principal-bundle
geometry, symplectic geometry, Krein/operator theory, hyperbolic analysis,
source criticism and a contrary-path review.  The hostile review passed the
calculation only at local conditional grade.  It specifically rejected
identifying `Q_u` with the source's `Q_B`, transferring the old `e3` contact
coefficient, or treating local observer selection as a global arrow/domain.

## Reproduction

```sh
uv run --isolated --no-project --cache-dir /private/tmp/gu-qb-cache \
  --with sympy==1.14.0 --with numpy -- \
  python -u tests/channel-swings/selected_k77_i2b_observer_qb_radial_stationarity_probe.py
```

The deterministic probe passes `44 exact + 4 planted = 48`, with zero
failures.
