---
title: "Eric/Curt Wave 3D-B1: the naive spacetime-H1 section domain is not closed"
status: active_research
doc_type: exploration
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: RUN-20260731-223801-gu-formalization-ecw3d-b1-direct
registry: lab/process/eric-curt-wave3d-b1-h1-closedness-kill.json
probe: tests/channel-swings/eric_curt_wave3d_b1_h1_closedness_kill_probe.py
---

# Eric/Curt Wave 3D-B1: the naive spacetime H1 section domain is not closed

## Result first

One explicitly frozen variable-coefficient Lorentz/spin section realization
fails the first analytic domain test. The actual W131 Lorentz-null symbol
admits a nonzero characteristic vector `q` in `ker Gamma`. A boundary-vanishing
Fourier sequence built on `q` is Cauchy in the `L2` operator graph norm
but its isotropic spacetime `H1` norm diverges. Therefore the operator with
the imposed ECW3D-A positive Green polarization and naïve `H1` domain is
not closed.

This is a precise domain kill, not a universal Lorentzian no-go. Time-slice
energy spaces, anisotropic graph spaces, and maximal-dissipative boundary
realizations remain open. So do the full nonlinear Euler operator and
constraint-propagation estimate.

The exact probe passes **21 exact + 10 planted = 31 checks**. Curt remains a
formally separate `(7,7)` rival inside the Eric lane. The pre-registered rule
remains `TG-1 AND TG-2 AND TG-3`; it is false, so no third lane is promoted.

## What was frozen

### Geometric construction used

This swing uses the program-native W131 gamma-traceless vector-spinor carrier
and right-`H`/Krein packet, not a standard positive-Hilbert Dirac default.
The section itself is an explicitly admitted standard Lorentz/spin test
geometry:

\[
M=\mathbb R_t\times S^1_x\times[0,1]_y\times S^1_z,
\qquad
g_a=a(y)^{-2}(-dt^2+dx^2)+dy^2+dz^2,
\]

with

\[
a(y)=1+\tfrac14\cos(2\pi y),
\qquad \tfrac34\le a(y)\le\tfrac54.
\]

In the adapted W131 frame, `y,x,z` use positive ambient tangent indices
`0,1,2`, while `t` uses negative index `9`. The metric supplies the tetrad

\[
e_t=a(y)\partial_t,\quad e_x=a(y)\partial_x,
\quad e_y=\partial_y,\quad e_z=\partial_z.
\]

This is one construction-grade test section. It is not an existence theorem
for a global Lorentz/spin section on arbitrary `X`.

### Operator and boundary data

Let `P=P_(ker Gamma)` be the W131 gamma-trace projector and let

\[
D_a=P\,\gamma(e^\mu)\nabla_{e_\mu}\,P.
\]

The metric-compatible vector-plus-spin connection contributes a smooth
zeroth-order matrix `B_a(y)`. It depends only on the compact `y` direction of
this stationary model and is bounded. The W131 equivariance theorem keeps
`P`, the connection, and the native right-`H` structure compatible.

At both boundary components we impose the positive Green spectral sector
constructed in ECW3D-A, with the appropriate outward normal. This sector is
right-`H` invariant. It is explicit extra analytic data: ECW3D-A proved that
the native algebra admits both opposite sectors and selects neither.

The tested domain is

\[
\mathcal D_{H^1,+}=\{u\in H^1(M,\ker\Gamma):
\operatorname{tr}u\text{ lies in the imposed outward-positive Green sector}\}.
\]

## Exact characteristic vector

Let

\[
c=\gamma_x+\gamma_t=\gamma(dx+dt).
\]

Since `dx+dt` is Lorentz-null, `c^2=0`. Choose a spinor seed `r` with
`s=cr` nonzero, and define the vector-spinor `q` by putting the same spinor
`s` in its `x`- and `t`-vector slots and zero elsewhere. Then

\[
\Gamma q=(\gamma_x+\gamma_t)s=c^2r=0,
\qquad
\sigma_{D_a}(dx+dt)q=cq=0.
\]

The executable representation obtains exactly zero for both residuals. Its
native antilinear partner `Jq` is independent, remains in `ker Gamma`,
and is killed by the same null symbol. The transverse `dy` symbol does not
kill `q`.

## Closedness counterexample

Fix a real smooth compactly supported time cutoff `psi` on `R_t` with unit
`L2` norm, and set

\[
u_N(t,x,y,z)=\psi(t)\sin(\pi y)
\sum_{k=1}^{N}\frac{1}{k}e^{ik(t+x)}q.
\]

Every `u_N` is smooth, lies in `ker Gamma`, and has zero trace at
`y=0,1`. Hence it satisfies the imposed boundary polarization without
using either Green sector to manufacture the obstruction.

The oscillatory `t+x` derivatives cancel in the principal operator because

\[
a(y)(\gamma_t\partial_t+\gamma_x\partial_x)
e^{ik(t+x)}q
=ika(y)(\gamma_t+\gamma_x)q=0.
\]

What remains is the fixed time-cutoff derivative, the transverse derivative,
and the smooth connection term:

\[
D_a u_N=
\left(P\gamma_tP\,\psi'(t)\sin(\pi y)q
+P\gamma_yP\,\psi(t)\pi\cos(\pi y)q
+B_a(y)\psi(t)\sin(\pi y)q\right)
\sum_{k=1}^{N}\frac{1}{k}e^{ik(t+x)}.
\]

Orthogonality already follows from the `S1_x` Fourier modes. The fixed cutoff
derivative and bounded connection term contribute only a constant to the
same coefficient tail, so

\[
\lVert u_N-u_M\rVert_{L^2}^2+
\lVert D_a(u_N-u_M)\rVert_{L^2}^2
\le C\sum_{k=M+1}^{N}\frac1{k^2}\longrightarrow0.
\]

Thus `u_N` is graph-Cauchy. But either null-direction derivative gives

\[
\lVert\partial_x u_N\rVert_{L^2}^2
=C_x\sum_{k=1}^{N}k^2\frac1{k^2}=C_xN\longrightarrow\infty,
\]

and the same holds for `partial_t u_N`; for real `psi`, the cutoff cross term
vanishes after integration. The `L2` graph limit therefore does not belong to
spacetime `H1`. Hence

\[
D_a:\mathcal D_{H^1,+}\subset L^2\longrightarrow L^2
\]

is not closed.

The cutoff derivative and bounded connection term cannot repair the failure:
they are controlled by the same convergent `sum k^-2` tail. Neither can the imposed boundary
polarization, because the entire sequence has zero boundary trace.

## Layer-0 object dictionary

| shared term | objects kept separate | disposition |
|---|---|---|
| closed domain | a closed unbounded operator on isotropic spacetime `H1`; a well-posed time-slice energy or maximal-dissipative generator | `HOMONYM` |
| selected polarization | one imposed positive Green sector; a sector forced by native GU data | `HOMONYM` |
| constraint preservation | pointwise `ker Gamma`/right-`H` compatibility; nonlinear Euler constraint propagation | `HOMONYM` |
| variable-coefficient section | this explicit stationary slab; a global Lorentz/spin section on arbitrary `X` | `HOMONYM` |

The kill lives on the explicitly chosen isotropic spacetime-`H1` side. It
does not silently default from that failed standard analytic realization to a
no-go for every program-native Krein/energy construction.

## Constraint/parameter surplus

The frozen construction supplies four explicit choices: the slab geometry,
the nonconstant coefficient `a(y)`, the positive Green sector, and the
isotropic `H1` domain. It is required to satisfy actual-carrier closure,
right-`H` compatibility, the boundary condition, and operator closedness.
It fails the last requirement exactly, so there is no positive surplus to
score: the candidate domain is killed.

The energy-domain surplus remains `UNCOMPUTABLE`. A new candidate must first
fix a time function, energy norm, incoming/outgoing boundary flux, nonlinear
operator, and constraint estimate.

## Non-regression matrix

| family | result |
|---|---|
| gravity | no section Einstein equation or stationary background constructed |
| gauge | W131 metric-connection compatibility retained; no gauge-quotient energy domain |
| odd matter | naïve spacetime-`H1` realization killed; Einstein--Dirac energy domain open |
| Higgs/Yukawa | untouched |
| quantum/domain | polarization imposed; maximal dissipativity, propagator, and BFV phase space open |
| cosmology | untouched |
| `P1,P2,P3` | unconsumed |

## Curt rival and third-lane gate

Curt's literal real `(7,7)` track still needs its own section operator,
right-structure, Green polarization, domain, and same-space discriminator.
The shared complex matrix algebra cannot transport the real analytic domain.

- `TG-1`: partial literal-real non-equivalence, source convention uncleared;
- `TG-2`: no separate complete Curt dynamics;
- `TG-3`: no common-domain discriminator.

Therefore `TG-1 AND TG-2 AND TG-3` remains false and Curt is not promoted.

## What remains and next gate

The immediate next gate is
`ECW3D-B2-ENERGY-MAXIMAL-DISSIPATIVE-CONSTRAINT-DOMAIN`:

1. freeze a time function and a time-slice energy/graph space;
2. freeze incoming/outgoing Green boundary data compatible with right-`H`;
3. prove or kill a coercive energy estimate and maximal dissipativity; and
4. only then test preservation of the full nonlinear Euler constraints.

Still unearned: a global Lorentz/spin section on arbitrary `X`, a closed
energy realization, self-adjointness or maximal dissipativity, nonlinear
constraint propagation, a propagator, and a physical BFV phase space.
