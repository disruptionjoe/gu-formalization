---
title: "Selected K77 I2B moving-Q_u contact and full fixed-background Euler"
status: conditional-construction
created: 2026-08-12
channels: [Build, Compose, Source, Verify]
source_disposition: SOURCE-CONFIRMS-SC-ACT-04__SOURCE-SILENT-EXACT-QU-AND-BACKGROUND-REPAIR
free_object_delta: "zero; the result emits a two-shape demand on an already-unbuilt background response"
---

# Selected K77 I2B moving-`Q_u` contact and full fixed-background Euler

## Result

The observer-owned pairing from v0.223 closes the one normal-contact equation
that the trace comparator left unresolved.  For

```text
Upsilon_B = (rho+r^2/3) S_q + kappa r H_q,
```

the four Hodge-active coefficients are exactly

```text
e0 = e1 = e2 = 0,
e3 = (2r/9)(160r^2+480rho+9kappa^2).
```

Thus `e3` is the restricted radial Euler equation itself and vanishes on the
shifted nonzero branch

```text
rho = -r^2/3 - 3kappa^2/160.
```

This is a genuine closure, not the old null-residual blindness: under `Q_u`
the displaced-torsion direction has norm `2`.

## Full connection variation does not yet close

The same exact calculation was run on every one of the `196` real
fixed-background connection cells.  The four monomial coefficient vectors
have supports

```text
14, 0, 12, 2
```

and rank three.  On the shifted branch the active `e3` combination cancels,
but twelve diagonal cells remain:

```text
(0,0):      kappa^2(3kappa-44r)/40,
(i,i):     -3kappa^2(kappa+12r)/40,    i=1,...,11.
```

For nonzero `kappa`, simultaneous cancellation requires

```text
3kappa-44r = 0,
kappa+12r  = 0.
```

The coefficient determinant is `80`, so the only common solution is the
trivial `kappa=r=0`.  A scalar rescaling of pure `I2B` cannot repair two
independent shapes.

## What the adverse result means

This is not a no-go for GU, for the Higgs construction, or for `SC-ACT-04`.
The calculation deliberately holds the background residual owner
`F0(A,g,epsilon)` fixed while varying the connection.  The actual derivative
of that geometric background has not been constructed.  Its connection,
metric, observation-section and moving-Shiab response could contribute the
two missing diagonal shapes.

The result therefore converts a vague “complete coupled Euler” gap into a
small exact interface contract:

> The missing source-action/background completion must have image containing
> two independent transverse diagonal shapes with the displayed coefficient
> ratios.

If a source-owned response supplies them, recompute the full Euler equation.
If its image has rank below two or the wrong fixed ratios, that completion is
obstructed.  No cancellation term may be fitted merely because the target is
known.

## Controls and composed directions

- All four radial Levi-Civita first-jet directions have zero `Q_u` pairings
  against both residual components; they do not cancel the twelve cells.
- The constrained observer gradient vanishes at the selected rest line.
- Simultaneous observer/frame transport remains a Ward-zero direction.
- These closures do not imply a global domain, preboundary class, BV quotient
  or physical spectrum.

The principal carrier remains two `C^(32,32)` Weyl halves.  Their block
subgroup, the full `U(64,64)` parent and independent connection fields are
distinct objects.  This calculation introduces no new carrier or datum.

## Source/action fence

The source supports a second-layer bosonic residual norm square and a distinct
`Q_B` slot.  It does not print this repository's `Q_u`, the twelve-cell Euler
covector, or a background Frechet term that cancels it.  It also leaves the
relation between first- and second-layer actions as sequential, alternative
or redundant rather than licensing an arbitrary fitted sum.  Consequently
`I1` is not appended here as a repair term.

## Reproduction

```sh
uv run --isolated --no-project --cache-dir /private/tmp/gu-qb-cache \
  --with sympy==1.14.0 --with numpy -- \
  python -u tests/channel-swings/selected_k77_i2b_moving_qu_contact_full_euler_probe.py
```

The deterministic probe passes `45/45`, including three firing plants.

## Next gate

Construct the exact Frechet derivative of `F0(A,g,epsilon)` under the owned
connection, metric, section and Shiab variations.  Project its Euler image
onto the two displayed diagonal shapes before attempting any larger action or
spectrum calculation.
