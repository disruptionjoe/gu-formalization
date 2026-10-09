---
title: "Constant-background obstruction in the selected native I1B germ"
status: active_research
claim_verdict: conditional_theorem
doc_type: native_action_constant_background_obstruction_theorem
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: SC-META-53
probe: tests/channel-swings/native_i1b_constant_background_probe.py
manifest: lab/process/native-i1b-constant-background.json
claim_ceiling: "Selected flat K77 I1B completion, constant real fields, nonzero kappa; no exclusion of general GU backgrounds or physical sectors"
---

# Constant-background obstruction in the selected native I1B germ

The obvious nonzero constant replacement for the previously unstable flat
background fails the metric equation. Allowing independent horizontal and
vertical distortions, together with both bivector companions of the growing
mode, still leaves only zero distortion. There is no alternative equilibrium
in this five-field constant family about which to calculate stability.

This closes a specific proposed repair of the
[previous scalar instability](native-i1b-scalar-closure-2026-10-08.md).
It does not exclude curved or varying backgrounds, additional Clifford
components, or a source-derived physical restriction on the perturbations.
The positivity question associated with SC-META-53 remains open.

> **2026-10-08 geometry scope correction.** The `rho L` and `L=0`
> conditions below belong to the declared co-moving flat completion. In the
> canonical Zorro reconstruction the independent observing metric `g` and
> fibre point `h` are different variables: constant `g -> s g` leaves
> `Gamma(g)` and the ambient metric at fixed `(x,h)` unchanged, whereas
> `h -> s h` gives the `-8` density derivative. The latter is not automatically
> an observing-metric Euler equation. The ideal and flat-family exclusion
> remain valid under their stated variation; they do not exclude backgrounds
> of the canonical geometry. See the [end-to-end §3.1 assessment](../nguyen-gu-critique/section-3-1-end-to-end-assessment-2026-10-08.md#the-actual-reconstructed-geometry-over-a-flat-observing-metric).

> **GU-COMPARATOR-ROUTING — scope before inference.** This calculation uses
> the selected K77 completion of I1B and its induced metric variation.
> No ordinary Higgs potential, Einstein action, external scalar model or
> sum with I2B is substituted. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` within the selected action completion.

```gu-typed-objects
result: constant radial and diagonal background obstruction and exact five-field stationary ideal
carrier: real constant Omega1 Cl(7,7) distortion and ten horizontal metric variations at the selected flat germ LAYER=ambient+source-print BRIDGE=selected_flat_I1B_completion CHIRALITY=N/A
pairing: Clifford trace and induced Hodge action pairing ON=distortion_coefficients
real_structure: real Clifford coefficients and real nonzero kappa
grading: horizontal and vertical form directions; Clifford grades one and two; no physical ghost grading
action_owner: source-action -- first bosonic I1B with selected comm/symi/symi Shiab and co-moving gimmel packet
target: necessary full-action bulk stationarity conditions for the declared background family MAP-TYPE=restriction
```

## Scope and action

Use the same flat, constant-coefficient local completion as the previous
calculation, with `B_LC=0`, `F_B=0`, and all background field derivatives zero.
The plus-first signature is `(+--- ++++++ ----)`. Index `0` is horizontal
time, `i=1,2,3` are horizontal spatial directions, and `I=4,...,13` are
vertical directions. This selects K77; it does not resolve the source
signature question or construct a global Observerse metric.

The action is

```text
I1B = <T,S(F_B)> + (1/2)<T,S(D_B T)> + (1/3)<T,S(T wedge T)>
      + (kappa/2)<T,*T>.
```

At the constant flat background its scalar density is

```text
L(T) = Q(T) + (kappa/2) N(T),
Q(T) = (1/3)<T,S(T wedge T)>,     N(T) = <T,*T>.
```

`Q` is cubic and `N` quadratic. Variation is performed before restriction;
in particular, the metric equation is not discarded because the background
metric is flat. The relevant full-action normal derivative of the cubic is

```text
dQ_T[U] = (1/3)<U,S(T wedge T)>
          + (1/3)<T,S(U wedge T + T wedge U)>.
```

It is not replaced by the printed residual endpoint. The source/action
distinction and normalization are recorded in the predecessor note.

## The missing metric condition

The selected moving geometry uses

```text
G(g) = g direct-sum D_g,
D_g(k,l) = tr(g^-1 k g^-1 l) - (1/2)tr(g^-1 k)tr(g^-1 l).
```

In the canonical ten-component metric order
`(00,01,02,03,11,12,13,22,23,33)`, direct differentiation gives

```text
rho = d_g log vol_G = (-2,0,0,0,2,0,0,2,0,2).
```

For a second derivation, scale `g -> s g`, `s>0`. The horizontal metric scales
by `s` and the ten-dimensional fibre metric by `s^-2`. Thus
`vol_G -> s^-8 vol_G`, and the conformal density derivative is `-8`.
This is the induced four-plus-ten motion, not uniform scaling of fourteen
metric directions. The probe reconstructs the DeWitt Gram and every entry
of `rho`; it does not merely read the older density receipt.

Transport the coframe, Clifford identification, Phi, Shiab, Hodge and fields
through this one co-moving packet. The algebraic scalar `L` then stays fixed
when its field amplitudes stay fixed. This is a permissible joint variation
of metric and distortion. At a full stationary background it must have zero
first variation, just as independent variations must.

Localize the conformal variation with a compactly supported scalar `f`.
Variations of the Levi-Civita connection, curvature and covariant derivative
produce terms with derivatives of `f`. Their background coefficients are
constant, so their bulk formal adjoints vanish after integration by parts.
The remaining variation is

```text
delta I1B = -8 L(T) integral f vol_G.
```

Consequently **`L(T)=0` is necessary for full stationarity** on this constant
flat completion. This argument does not require the five-field restriction
to be a consistent nonlinear truncation. Equivalently, after the complete
distortion equations vanish, the metric Euler covector is `rho L`;
constant source-graph momentum has zero formal derivative here.

This specializes the existing
[metric Euler construction](selected-k77-direct-metric-euler-2026-08-09.md)
and [parallel-momentum metric test](selected-k77-sr1c-fixed-varpi-metric-stationarity-2026-08-14.md)
to the present flat `B=0` background. Those earlier nonzero-`B` branch
coefficients are not imported. The co-moving description does not cancel a
physical metric variation or supply a gauge quotient.

## Radial and arbitrary diagonal candidates

Under the admissible distortion scaling `T -> c T`, stationarity requires

```text
3Q + kappa N = 0.
```

Combining this with `L=0` gives, for `kappa!=0`,

```text
N=0,     Q=0.                                           (1)
```

For the radial candidate `T=t Phi1`,

```text
L = 1456 t^3 + 7 kappa t^2,
t_* = -kappa/312,
L(t_*) = 7 kappa^3/292032,
delta_conformal I1B density = -7 kappa^3/36504.
```

Thus the known nonzero distortion-stationary root is not a full stationary
background. Its nonzero metric response holds for either sign of nonzero
`kappa`. A Hessian at that point cannot establish stability of an equilibrium.

The same obstruction rejects every nonzero real constant diagonal grade-one
field `T=sum_mu t_mu e^mu gamma_mu`, including independent horizontal and
vertical amplitudes. Its Hodge form is exactly

```text
N = sum_mu t_mu^2.
```

The probe checks the entire fourteen-by-fourteen Gram. Equation (1) therefore
forces every `t_mu=0`; no classification of the cubic critical points is
needed. This positivity belongs to this diagonal subspace, not the complete
Clifford-valued connection carrier.

## Add the companions of the growing mode

The next extension includes the negative Hodge directions that the earlier
time-dependent scalar calculation requires:

```text
T = a e^0 gamma_0 + b sum_i e^i gamma_i + d sum_I e^I gamma_I
    + u sum_i e^i gamma_0 gamma_i + w sum_I e^I gamma_0 gamma_I.
```

All five amplitudes are now constant and independent. Direct exact Clifford
polarization gives

```text
N = a^2 + 3b^2 + 10d^2 - 3u^2 - 10w^2,

Q = 12ab^2 + 120abd + 180ad^2 - 40auw - (140/3)aw^2
    + 4b^3 + 120b^2d + 540bd^2 - 4bu^2 - 80buw - 180bw^2
    + 480d^3 - 40du^2 - 360duw - 480dw^2.                (2)
```

Unlike the diagonal subspace, this real subspace has nonzero Hodge-null
vectors: `(a,b,d,u,w)=(3,1,0,2,0)` is one. Positivity cannot prove the enlarged
obstruction. The actual distortion equations must also be used.

Let `E_x=partial_x(Q+kappa N/2)` for each of the five amplitudes. Each `E_x`
is a pairing of the full normal Euler equation with an allowed distortion
variation, so all five must vanish at any full stationary background in this
family. These are **necessary equations**. No assertion that they exhaust
the other Clifford equations is needed to reject a candidate.

Their homogeneity identity is

```text
3L - sum_x x E_x = kappa N/2.                            (3)
```

For nonzero `kappa`, put `T=kappa X`. Then `E_x(T,kappa)` is `kappa^2`
times the corresponding unit-coupling equation. This covers both signs and
divides by no field amplitude. In the rational polynomial ring the exact
reduced Gröbner basis is

```text
Ideal(partial_a(Q+N/2), partial_b(Q+N/2), partial_d(Q+N/2),
      partial_u(Q+N/2), partial_w(Q+N/2), N)
  = Ideal(a,b,d,u,w).                                    (4)
```

Here the variables are the rescaled amplitudes of `X`. Equations (3) and
`kappa!=0` justify replacing the metric condition `L=0` by `N=0`. Equation
(4) is an exact rational ideal calculation, not a numerical root search or
a test of a finite sample of backgrounds. It proves that the only solution
of these necessary equations is zero, even over the complex numbers.
Hence there is no nonzero real full stationary background in this family.

The probe reconstructs (2) from the sparse Clifford action and cross-checks
its five derivatives against direct full-action receiver variations. Removing
the metric equation restores the rejected radial solution, so the extra
condition is substantive. At `kappa=0`, `(1,0,0,0,0)` satisfies the tested
necessary equations and `L=0`; the theorem explicitly excludes that
degenerate stratum and does not claim its full stability or positivity.

## Consequence and next mathematical test

For nonzero `kappa`, the only equilibrium within the tested constant family
is the flat `T=0` germ. Its previously constructed growing mode is therefore
not repaired by choosing another constant value of these fields. No coupled
stability calculation at a nonzero candidate is licensed by this result.

A further search must leave at least one tested assumption. Curvature or
spatial/time variation can make the curvature term and the source-graph
formal adjoint contribute; additional Clifford components can change the
stationary ideal. A source-derived restriction on allowed perturbations is
another logically separate possibility. None has been constructed here.

For a curved candidate, the next concrete requirement is a compatible
`G(g)`, its full connection and curvature jets, and a distortion field that
satisfies both the normal distortion and metric equations of the same I1B.
The [moving-action evaluator requirement](selected-k123-native-i1b-h-containing-cubic-identifiability-and-evaluator-gate-2026-08-15.md)
explains why assigning an independent curvature number or importing a
four-dimensional scalar potential would not supply that calculation.

## Reproduction and limits

```sh
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_i1b_constant_background_probe.py
```

The probe passes **26 exact checks**. The accompanying
[receipt](../../lab/process/native-i1b-constant-background.json) records
dependency hashes, the polynomial equations, upstream revision and focused
validation. The analytical compact-support argument above supplies the
constant-background metric condition; the finite probe alone is not a
variational-PDE proof.

The calculation is repository-derived within a selected completion. No
global background, closed physical domain, positive quantum state space,
nonlinear scalar truncation, source verdict or canon promotion is claimed.
