---
title: "Scalar closure and a growing mode in the selected native I1B germ"
status: active_research
claim_verdict: conditional_theorem
doc_type: native_action_scalar_closure_and_linearized_mode_theorem
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: SC-META-53
probe: tests/channel-swings/native_i1b_scalar_closure_probe.py
manifest: lab/process/native-i1b-scalar-closure.json
claim_ceiling: "Selected flat K77 first-bosonic-action germ; no global GU background, physical domain or nonlinear scalar truncation constructed"
---

# Scalar closure and a growing mode in the selected native I1B germ

A varying radial distortion fails an omitted equation of the selected
`I1B` action. Adding its single isotropic bivector companion still admits
no nonconstant one-coordinate solution on fixed flat geometry. Allowing the
horizontal and vertical components to differ produces a scalar mode that
satisfies every linearized metric and distortion equation and grows at
rate `|kappa_1| sqrt(17/113)` at zero spatial momentum.

The metric equation removes a uniform transverse candidate but leaves this
relative horizontal/vertical mode. This is a local classical instability of
the **selected flat action germ if these perturbations are admitted**.
It does not establish a source-global background, a physical GU state or a
verdict on quantum positivity. SC-META-53 remains UNCERTAIN.

> **2026-10-08 geometry scope correction.** This constant-coefficient
> ambient completion is not the canonical Zorro geometry over a flat
> observing metric. The latter retains fibre curvature, and its observing-
> metric variation differs from moving the fibre point. The exact mode above
> remains a result of the declared surrogate; its transfer to GU requires a
> separate derivation. See the [end-to-end §3.1 assessment](../nguyen-gu-critique/section-3-1-end-to-end-assessment-2026-10-08.md#the-actual-reconstructed-geometry-over-a-flat-observing-metric).

> **GU-COMPARATOR-ROUTING — scope before inference.** This uses the selected
> K77 completion of the first bosonic action and its coupled variation.
> No ordinary Einstein action, scalar-electrodynamics control, observed
> two-field action or sum with I2B is substituted. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` within the selected action germ.

```gu-typed-objects
result: nonlinear radial closure obstruction and exact coupled linearized growing scalar mode
carrier: ten horizontal metric variations and real Omega1 Cl(7,7) distortion at the selected flat T=0 germ LAYER=ambient+source-print BRIDGE=selected_flat_I1B_completion CHIRALITY=N/A
pairing: Clifford trace and Hodge action pairing; separate reduced homogeneous energy ON=metric_plus_distortion_variations
real_structure: real Cl(7,7) fields with conjugate complex Fourier amplitudes
grading: horizontal versus vertical form directions and Clifford grades; not physical ghost parity
action_owner: source-action -- first bosonic I1B with the repository-selected comm/symi/symi Shiab and flat germ
target: full normal Euler equations and scalar constraint propagation MAP-TYPE=restriction
```

## Action and normalization

In native coordinates `varpi=B_LC(g)+T`, the first action is

```text
I1B = <T,S(F_B)> + (1/2)<T,S(D_B T)> + (1/3)<T,S(T wedge T)>
      + (kappa/2)<T,*T>.
```

The action and its printed endpoint are distinguished in the
[source reinspection](../../lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md).
Here the action is differentiated; cyclicity of the Shiab pairing is not
assumed. At the selected flat `T=0` germ its full quadratic operator is

```text
H = [[0,A*],[A,kappa K+E(partial)]],
A = D_g[S_g(F_B)],       E(q) = (raw(q)-raw(q)^T)/2,
raw(q)_{UV} = <U,S(q wedge V)>.
```

This is the [K128](selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-2026-08-16.md)
and [K129](selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md)
operator, using [K135's curvature-injection convention](selected-k135-native-i1b-t0-coupled-shell-green-domain-2026-08-16.md).
`A*` is its formal bulk adjoint. Compactly supported variations justify
integration by parts; no boundary domain is selected.

The coframe has plus-first signature `(+--- ++++++ ----)`. Index `0` is
horizontal time, `i=1,2,3` are horizontal spatial directions, and
`I=4,...,13` are vertical directions. The Shiab is `comm/symi/symi`, and
`Phi1=sum e^mu gamma_mu`. These are selected K77 conventions, not a
resolution of SIGNATURE-AMBIENT or a uniqueness theorem for the Shiab.

## The omitted equations of a radial restriction

Hold the geometry flat and take `T=phi(t) Phi1`. Its restricted derivative
density vanishes, but its normal bivector Euler rows are `-11 phi'` on
each `e^mu gamma_0 gamma_mu`, `mu!=0`. Full distortion stationarity therefore
requires `phi'=0` and `kappa phi+312 phi^2=0`. These constant roots concern
distortion stationarity only, not the metric equation at nonzero `T`.

The smallest isotropic derivative companion is

```text
T = phi Phi1 + v sum_(mu!=0) e^mu gamma_0 gamma_mu.
```

Varying before restriction gives three necessary full distortion rows:

```text
F := kappa phi+312 phi^2-(260/3)v^2 = 0,
kappa phi+312 phi^2+11v'-88v^2 = 0,
-11phi'-(kappa+(568/3)phi)v = 0.                         (1)
```

The first row varies the longitudinal grade-one component independently;
it would be lost by varying only the scalar pullback. Subtracting the first
two rows gives `v'=(4/33)v^2`. Differentiating `F=0` and using the other
equations gives, wherever `v!=0`,

```text
118976 phi^2+816 kappa phi+kappa^2 = 0.                  (2)
```

For fixed real `kappa`, this nonzero polynomial has finitely many roots.
Continuity forces `phi` constant on an interval with `v!=0`. Then `F=0`
forces `v^2` constant, contradicting `v'=(4/33)v^2`. Thus `v=0` everywhere
and `phi` is constant. This proof includes `kappa=0`. It excludes only this
declared ansatz, not arbitrary distortion backgrounds or dependencies.

## Independent horizontal and vertical components

At the flat `T=0` germ allow six linearized amplitudes:

```text
h_11=h_22=h_33=psi(t),   other h_ab=0,
T = a e^0 gamma_0
    + b sum_i e^i gamma_i + d sum_I e^I gamma_I
    + u sum_i e^i gamma_0 gamma_i + w sum_I e^I gamma_0 gamma_I.
```

Every omitted metric equation is still tested. In distortion order
`(a,b,d,u,w)`, direct Clifford evaluation gives

```text
K = diag(1,3,10,-3,-10),       A_psi = (0,-12,-60,0,0)^T,
E = [[0, 0,  0, 0,  0],
     [0, 0,  0, 3, 30],
     [0, 0,  0,30, 80],
     [0,-3,-30, 0,  0],
     [0,-30,-80,0,  0]].
```

Dividing transverse rows by their multiplicities yields

```text
(b+5d)'' = 0,
kappa a = 0,
kappa b-4psi''+u'+10w' = 0,
kappa d-6psi''+3u'+8w' = 0,
-kappa u-b'-10d' = 0,
-kappa w-3b'-8d' = 0.                                  (3)
```

The first line is the metric equation. For nonzero exponential modes it
forces `b=-5d`, not `b=d`. Generally `b+5d` is affine in time; its constant
and linear integration data remain a distinct zero-frequency sector.
Setting those data to zero is a solution-sector choice, not a gauge symmetry.

This is more than a compressed matrix test. A basis element
`e^mu gamma_J` has label `J xor {mu}`. A raw derivative at `q=e0` flips
that label by `{0}`: exterior and Clifford indices match in each Phi
insertion, while the Hodge complements cancel upon pairing. The set
`{0,{0}}` closes under the raw coefficient and its transpose and contains
28 distortion basis elements. Mass preserves the label. The scalar metric
image is in that block. The probe checks the full ten metric and 28
distortion rows against the six-column inclusion. All other Clifford rows
vanish by this selection rule, as in
[K132](selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md).

## A surviving growing mode

For `kappa!=0`, the determinant of the coupled exponential coefficient is

```text
det H(z) = 21600 kappa^2 z^4 (113z^2-17kappa^2).         (4)
```

For either sign of nonzero `kappa`, put `gamma=|kappa| sqrt(17/113)`.
An exact mode is

```text
d = exp(gamma t),          b = -5d,             a = 0,
u = -(5/kappa)d',          w = (7/kappa)d',
psi = 135 d/(17 kappa).                                (5)
```

Every row of (3) vanishes on substitution. The scalar characteristic kernel
is one-dimensional, while the five-field distortion block is invertible
there. This is a characteristic of the coupled metric-distortion system,
not a distortion-kernel mode surviving by omission. The distortion is
nonzero, whereas source frame gauge
motion of a connection difference vanishes at `T=0`. Its linearized metric
curvature is nonzero, whereas a flat-background metric diffeomorphism has
zero linearized curvature. Those action-owned gauge motions do not remove it.

The distortion-only mode with `a=0`, `b=d` and `u=w` has exponent
`z=kappa/11`; it is uniform over the thirteen directions transverse to time.
It differs from the full radial ansatz in (1). Its exponent is absent from
(4): metric coupling removes that apparent instability and leaves (5).
Neither promoting a distortion-only pole to a physical GU mode nor claiming
that metric coupling removes every growing mode is warranted.

At `kappa=0`, the same matrix has rank four at nonzero `z`, with undetermined
directions. This degenerate system is not a positive regular continuation of
the elimination used above.

## Energy and spatial dependence

The `u,w` equations follow from the distortion action density

```text
L = (kappa/2)(3b^2+10d^2-3u^2-10w^2)
    -u(3b'+30d')-w(30b'+80d').
```

Eliminating them and imposing the zero-affine branch `b=-5d` gives

```text
L_red = (565/(2kappa))(d')^2+(85kappa/2)d^2,
E_red = (565/(2kappa))(d')^2-(85kappa/2)d^2.              (6)
```

Its Euler equation again gives `d''=(17/113)kappa^2 d`. The remaining normal
equation reconstructs `psi` as in (5); it has not been replaced by a
restricted variation. This conserved homogeneous energy density is indefinite
for either sign of `kappa`. For positive `kappa` the kinetic coefficient is
positive and the potential is inverted. This is not an inference from an
off-shell Lorentzian Hessian sign to a negative quantum probability.

There is also a covariant horizontal continuation. Set `m^2=17kappa^2/113`,
`q^2=m^2`, `P_a^b=delta_a^b-q_a q^b/m^2`, and `slash(q)=q^a gamma_a`.
The polarization amplitudes are

```text
h_ab = -135/(17kappa) (eta_ab-q_a q_b/m^2) d,
T_a^(1) = -5 P_a^b gamma_b d,        T_I^(1) = gamma_I d,
T_a^(2) = -(5/kappa)(slash(q) wedge_Cl gamma_a)d,
T_I^(2) =  (7/kappa)(slash(q) wedge_Cl gamma_I)d.
```

Here `wedge_Cl` is the Clifford bivector product, not the form wedge.
Lorentz covariance extends the polynomial operator identity from the time
axis. A separate exact substitution tests `kappa=113` and
`q=(25,36i,0,0)`, with `q^2=1921`: every distortion row and all ten metric
rows vanish. This is a spatially oscillating mode with real growth rate 25.

For real spatial momentum `p`, the dispersion is
`gamma(p)^2=m^2-|p|^2`. Smooth Fourier packets supported strictly inside
`|p|<m` give horizontally square-integrable growing solutions; conjugate
packets give real fields. Vertical normalizability, the source observation
map and a global physical domain remain unconstructed. No normalizable
physical state on the actual Observerse is claimed.

## Consequence for the positivity construction

The radial restriction fails nonlinear normal equations. Its enlarged
scalar sector satisfies the full linearized normal equations but contains
the explicit instability (5). That relative mode, including its metric
and bivector companions, is a concrete test for a proposed physical
constraint. The metric condition in (3) alone is insufficient.

A positive-domain construction must derive an additional propagated
condition excluding these modes or supply a different background or action
completion that changes their equations. Deleting them by declaration would
add unowned physical-state data. Nonflat/nonzero-distortion backgrounds,
other source-natural Shiabs and source-derived boundary laws remain open.

Upstream through `1829f4a3` supplies positive finite-cutoff BRST controls in
[K1468--K1472](k1468-k1472-null-order-wick-cocycle-and-brst-boundary-2026-10-08.md).
Those operators are not identified with this action. Transferring their
positivity would require a map intertwining actions, constraints and domains.
K1145/K1150 physical admission and H59 remain open.

## Reproduction

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_i1b_scalar_closure_probe.py
```

The 29 exact checks include direct Clifford evaluation, all omitted linear
rows, the nonlinear radial compatibility polynomial, action elimination and
a nonzero-spatial-momentum check. This is symbolic and analytic verification,
not an independent external review, a nonlinear consistent truncation theorem
or a canon promotion.
