---
artifact_type: construction_result
created: 2026-08-09
status: SOURCE_SHAPED_SCALAR_JET_BRANCH_EXACT__ZERO_LOCAL_COEFFICIENT_FREEDOM__GLOBAL_REALISATION_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_curvature_vev_trace_probe.py
  - tests/channel-swings/selected_k77_curvature_vev_trace_independent.sage
registry: lab/process/selected-k77-curvature-vev-trace-closure.json
---

# Selected K77 curvature/VEV trace closure

## Result first

The v0.107 metric-trace demand can be closed **inside the existing source
first action at scalar-jet grade**. No second dark-energy field, fixed
cosmological constant, counterterm or free coefficient is required.

The decisive Layer-0 correction is that Weinstein's movable dark-energy
carrier is the equivariant connection distortion already represented by
`T_omega` in the source action. The previous instruction to construct “another
action sector” risked counting this field twice. What the homogeneous finite
fixture had actually omitted was the derivative-curvature part of `F_B`.

Restore its selected invariant scalar cell as

```text
r (Phi1 wedge Phi1).
```

On the nonzero-distortion horn, the exact branch is

```text
B* =  Phi1/208,
T* = -Phi1/104,
r* =  1/129792.
```

It solves the reduced connection equation, the complete finite raw residual,
and the metric-volume trace equation. The three-by-three constraint Jacobian
has full rank, so three field values minus three independent equations leaves
zero local freedom.

The cancellation is transparent:

```text
noncurvature first-action density = +7/21632
derivative-curvature density      = -7/21632
total                             =  0.
```

Consequently their two rank-one metric-volume covectors cancel
coefficientwise in all ten `Sym2(T*X)` directions. This is the first exact
construction in the current chain that realizes Weinstein's curvature/
distortion tracking shape rather than appending an independent cosmological
term.

## Layer 0

| object | construction used | not identified with |
| --- | --- | --- |
| dynamic VEV carrier | source-native equivariant connection distortion `T_omega` | a new scalar, fixed `Lambda`, or fitted counterterm |
| curvature cell | first-jet scalar component of the derivative part of `F_B` | an independent zero-order algebraic field |
| zero trace | cancellation of the selected action's gimmel-volume covector | the observed Einstein equation or measured dark energy |
| Bianchi pass | local algebraic commutator for the invariant curvature cell | global connection, holonomy or atlas descent |
| constraint surplus | three local field values and three independent equations | a global functional quotient or residue discharge |
| action parent | conditional selected Spin-native K77 parent | either `U(32,32)` half or full `U(64,64)` |

The 2021 `T_omega` and later `theta` displays are `SAME-CARRIER`, not yet a
coefficientwise global identification. Their trivialisation and conjugation
placement differ. That remaining map does not license a second field.

## Exact construction

The homogeneous action used in v0.106 was

```text
L0(b,t)=7 t (624 b^2 + 624 b t + 208 t^2 + t).
```

The source action contains full curvature, not only the algebraic `B wedge B`
piece. In the selected invariant scalar receiver,

```text
Shiab(Phi1 wedge Phi1) = 312 Hodge(Phi1),
<Phi1, Shiab(Phi1 wedge Phi1)> = 4368.
```

Restoring the derivative-curvature coefficient therefore gives

```text
L(b,t,r)=7 t (624 b^2 + 624 b t + 208 t^2 + t + 624 r).
```

On the `t != 0` horn, the independent reduced equations are

```text
2b+t = 0,
312(b+t)^2+t+312r = 0,
624b^2+624bt+208t^2+t+624r = 0.
```

The second is the scalar coefficient of the full raw source residual. The
third is the metric-volume trace equation. Eliminating `b` and `r` leaves

```text
-t(104t+1)=0,
```

so the nonzero horn is unique. The constraint Jacobian determinant is `-624`.

There is also a `t=0, r=-b^2` family. It is a valid algebraic control but not
the dynamic-VEV horn and is not promoted.

## Full finite checks

The construction was then returned to the exact selected Clifford/exterior
engine rather than left as a scalar polynomial:

- all 1,470 admitted low-grade `B` directions vanish;
- all 1,470 admitted low-grade `T` directions vanish;
- the full finite raw residual vanishes;
- the selected first-action density vanishes;
- the prior `r=0` branch remains a nonzero-action, metric-noncritical control;
- the invariant curvature cell obeys the necessary local algebraic Bianchi
  commutator; and
- all ten metric-volume components cancel, not only a sampled trace entry.

## What was learned about the external datum and source action

This closure consumes no external datum. More importantly, it shows that the
source action already contains the right *kind* of curvature/distortion
relationship to close the local trace. The missing ingredient was a field
configuration—a derivative-curvature jet—not an extra parameter.

The information gain is therefore a positive constraint-surplus result:

```text
3 local values - 3 independent equations = 0 residual local freedom.
```

That is not a declaration that the curvature jet exists globally. The next
construction must realize it as an actual connection curvature on `Y14`, with
the full derivative Euler equation, Bianchi identity, patching and observation
descent. Failure there would kill this branch without undoing the finite
algebra.

## Mandatory scope fences

- **Variational bicomplex:** `r` is a first-jet coordinate of `B`. Imposing a
  separate pointwise `E_r=0` would mistype it as a new field. The source's full
  connection variation must supply the derivative Euler test.
- **Symplectic geometry:** a local stationary jet is not yet a background for
  the common Hessian, presymplectic current or BV complex.
- **Bianchi/integrability:** the algebraic commutator passes, but global
  curvature realization, holonomy and atlas descent are open.
- **Microlocal PDE:** no principal propagation, constraint evolution or Green
  domain follows.
- **Krein/operator:** no positive fundamental symmetry or maximal domain is
  constructed.
- **Complex/path integral:** zero action density and first variation do not
  select a contour, reflection-positive measure or quantum saddle.
- **Cosmology:** `r*=1/129792` is a dimensionless normalization in this finite
  fixture, not the observed dark-energy magnitude, radiative screening or a
  prediction for `w(z)`.
- **Representation:** the result belongs only to the selected Spin-native
  parent. The two `U(32,32)` halves and full `U(64,64)` remain comparators.

## Source return

`SOURCE_CONFIRMS_DYNAMIC_DARK_ENERGY_USES_THE_EXISTING_EQUIVARIANT_CONNECTION_DISTORTION_CARRIER__SOURCE_SILENT_SCALAR_JET_BRANCH_AND_GLOBAL_REALISATION`.

The source confirms the carrier and curvature/distortion tracking grammar. It
does not publish this branch, coefficient, cancellation or global geometry.

## Validation

- main exact route: `43/43 PASS`;
- independent Sage/QQ route: `16/16 PASS`;
- hostile review: candidate survives only at local scalar-jet grade;
- P1/P2/P3 remain unchanged and unused;
- no verdict, residue, booked quotient, canon or public posture moves.

## Next gate

Construct a local connection jet and patchwise `Y14` curvature realizing
`r(Phi1 wedge Phi1)`, derive the full derivative `B` Euler equation by
integration by parts, and test Bianchi/atlas/observation descent. If that
passes, select the 321-versus-1,571 tangent and assemble the complete Hessian
and BV complex on this stationary background.
