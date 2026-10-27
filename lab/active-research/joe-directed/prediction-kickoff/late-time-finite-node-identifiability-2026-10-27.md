---
title: "Finite late-time distances: exact interpolation and a sharp variation test"
status: exploration
claim_verdict: internally_reviewed_conditional_mathematics
doc_type: conditional_geometric_identifiability_result
created: "2026-10-27"
target_claim: NONE-NOT-A-KILL
target_claim_note: "A conditional FLRW observation interface; no source claim or whole GU family is adjudicated."
probe: tests/channel-swings/late_time_finite_node_identifiability_probe.py
canon_verdict_change: none
---

# Finite late-time distances: exact interpolation and a sharp variation test

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: finite-node FLRW interpolation and sharp log-expansion variation requirement
carrier: a supplied observed four-dimensional FLRW metric, standard redshift z, positive H(z), and dimensionless distance nodes m=D_M/r_d and h=D_H/r_d LAYER=observed CHIRALITY=N/A
pairing: ordinary real point evaluation and radial integration; a later likelihood requires its own covariance ON=observed distance carriers
real_structure: real positive radial distances and real constant spatial curvature
grading: none; no Krein, Clifford or family grading is transported
action_owner: repository-construction; the geometric theorem has no variational owner, while the reused scalar action is only its named conditional local horn
target: MAP-TYPE=evaluation; characterize finite-node realizability and the additional quantitative assumption that produces an exclusion inequality
```

## Result and actual advance

Under a supplied standard FLRW observation convention, any finite collection
of strictly increasing positive transverse comoving distances and positive
radial distances can be matched by a smooth expanding history, for every
curvature in the declared increasing-distance branch. Smoothness alone does
not bound the variation between nodes. This is a finite-data statement, not
the claim that the continuous FLRW consistency relation has no content.

A single quantitative addition changes the result. If an independently
justified bound `|d log H/dz| <= L` is supplied on an interval, two radial
endpoint values and the transverse-distance increment obey a sharp pair of
inequalities. Every allowed area is realized in the positive log-Lipschitz
class. The same formulas give a unique minimum required variation `L_min`.
A future conditional background can therefore be rejected when its derived
bound is smaller than that demand, without first predicting an acoustic ruler
or an entire early universe.

The new repository derivation is the constructive finite-node theorem,
its sharp variation requirement, and the complete local vacuum-horn
initial-data counterconstruction below. The underlying distance-curvature identity and
AP cancellation are established results. No cosmological novelty, numerical
GU forecast, data fit, source derivation or ledger movement is claimed.

## Frozen observation assumptions and known baseline

Use `a(t_0)=1`, `1+z=1/a(t)`, `H=dot(a)/a>0`, constant present spatial
curvature `K` with dimensions length^-2, and standard null propagation in
that physical metric. The supplied comoving ruler `r_d>0` is constant, with
no numerical calibration required. Define

```text
m(z) = D_M(z)/r_d,       h(z) = c/[r_d H(z)],
kappa = -K r_d^2,        F_AP(z) = m(z)/h(z).
```

On the increasing transverse-distance branch,

```text
m' = h sqrt(1+kappa m^2),
I_kappa(m) = integral_0^m du/sqrt(1+kappa u^2),
I_kappa(m(z)) = integral_0^z h(u) du.                 (1)
```

`I_kappa` is `asinh(sqrt(kappa)m)/sqrt(kappa)` for positive kappa,
`m` for zero kappa, and `asin(sqrt(-kappa)m)/sqrt(-kappa)` for negative
kappa. The last formula uses `0 <= m < 1/sqrt(-kappa)` and the branch
before the transverse-distance maximum. After the closed-FLRW turnover,
`m'` is negative although `h` stays positive; (1) with its positive square
root does not cover that branch. It is transverse **comoving** distance
whose monotonicity is imposed, not angular-diameter distance.

The rearrangement `kappa=((m'/h)^2-1)/m^2` is the familiar curvature
identity. Clarkson, Bassett and Lu derive its continuous null test and
explain the derivative and observational independence requirements in
[their primary paper, equations (2)–(3)](https://arxiv.org/html/0712.3457v2).
It is reused here. Combining AP with uncalibrated supernova distance shape
to reconstruct relative expansion also predates this work; see
[Blake et al., sections 1 and 4](https://arxiv.org/html/1108.2637v1).
Using supernovae additionally requires the stated distance-duality and
source-calibration assumptions; no such data are used in this note.

## Theorem 1: finite-node smooth realizability

Let `0=z_0<z_1<...<z_n`, `0=m_0<m_1<...<m_n`, and `h_i>0`.
The value `h_0` may be any supplied positive number. Fix any real kappa
with `1+kappa m_n^2>0`. There exists a positive `C-infinity` function
`h` on the observed interval such that

```text
h(z_i)=h_i,    m(z_i)=m_i,    m'=h sqrt(1+kappa m^2),    m(0)=0.
```

**Proof.** On interval `i`, set

`J_i=I_kappa(m_{i+1})-I_kappa(m_i)>0`.

It suffices to construct a positive smooth function with endpoints
`a=h_i`, `b=h_{i+1}` and integral `J_i`. Choose a small positive baseline
epsilon below both endpoints. Add nonnegative smooth endpoint cutoffs,
equal to one near their respective endpoint and zero outside arbitrarily
small disjoint endpoint neighborhoods, with coefficients `a-epsilon` and
`b-epsilon`. Choose epsilon and those neighborhoods sufficiently small
that the resulting integral is strictly below `J_i`. Add a nonnegative
interior smooth bump of integral one with coefficient equal to the missing
area. The result is positive, equals the specified constant near each
endpoint, and has exactly the required integral.

Construct each interval this way. All derivatives at the shared nodes are
zero, so the pieces join smoothly. Set `chi(z)=integral_0^z h` and
`m(z)=I_kappa^-1(chi(z))`. Monotonicity keeps chi inside the inverse
branch throughout each interval. This proves the assertion. With
`H=c/(r_d h)` and `dt/dz=-1/[(1+z)H]`, it supplies a smooth expanding
FLRW metric on the observed interval. QED.

Consequences, with exact scope:

- Every kappa in `(-1/m_n^2,infinity)` is geometrically compatible with
  these finite nodes. This statement concerns this branch and unrestricted
  expansion, not a curvature posterior under a specified model.
- Arbitrary positive AP values at distinct positive redshifts also admit
  a flat realization: choose any increasing positive `m_i`, set
  `h_i=m_i/F_i`, and apply the theorem.
- Nonincreasing `m_i` cannot be realized on this branch with positive h.
  A closed-FLRW turnover is a distinct counterexample to extending this
  monotonicity conclusion to all FLRW branches.
- No matter equation, energy condition, stable perturbation theory, or
  native GU completion is asserted. If desired, a formal effective stress
  tensor can be defined from the Einstein tensor of the constructed metric;
  that does not impose a physical matter model or positivity condition.

Crucially, surveys estimate parameters over finite redshift windows using
templates and tracer/perturbation assumptions. Their reported effective
redshifts are not a license to insert arbitrarily narrow features into a
full survey likelihood. Theorem 1 applies to the explicit **point-evaluation
compression** above. It does not prove that arbitrary histories fit the
underlying clustering, lensing, supernova, CMB or growth observations.

## Theorem 2: one variation bound gives a sharp test

On one interval of length `Delta>0`, let `a=h(z_i)>0`, `b=h(z_{i+1})>0`
and `J=I_kappa(m_{i+1})-I_kappa(m_i)`. Supply `L>=0` independently of
the held-out data. The function class is positive continuous h with
`log h` Lipschitz with constant L, equivalently `|h'|<=L h` almost
everywhere. Since the ruler is constant, this is exactly the same bound
on `|d log H/dz|`.

For `L>0`, a member with the required endpoints and integral exists
**if and only if**

```text
|log(b/a)| <= L Delta,
J_minus <= J <= J_plus,
J_minus = [a+b-2 sqrt(ab) exp(-L Delta/2)]/L,
J_plus  = [2 sqrt(ab) exp(+L Delta/2)-a-b]/L.          (2)
```

For `L=0`, the condition is exactly `a=b` and `J=a Delta`.

**Necessity and sharpness.** With `t=z-z_i`, the log-Lipschitz property
at the two endpoints gives the pointwise envelopes

```text
h_minus(t) = max(a exp(-Lt), b exp(-L(Delta-t))),
h_plus(t)  = min(a exp(+Lt), b exp(+L(Delta-t))).
```

Endpoint compatibility is necessary and sufficient for these envelopes
to have the prescribed endpoints and `h_minus<=h_plus`. Their switches
are `(Delta-log(b/a)/L)/2` and `(Delta+log(b/a)/L)/2`. Direct integration
gives (2). Both envelopes are positive log-Lipschitz functions with bound
L and attain their respective integrals.

**Sufficiency.** For `0<=theta<=1`,
`h_theta=(1-theta)h_minus+theta h_plus` has the prescribed endpoints.
The inequalities `-L h<=h'<=L h` are preserved by positive linear
combination, so `h_theta` belongs to the same class. Its integral is
`(1-theta)J_minus+theta J_plus`, exhausting the closed interval. QED.

For multiple intervals, the conditions must hold with **one shared
kappa**. Concatenating the functions gives a global positive log-Lipschitz
history (with the maximum of declared interval bounds). This is an exact
feasibility characterization for this class. All smooth histories obey
the same exclusions, but boundary extremizers can have kinks. The bounds
are sharp limits for smooth functions on a single interval; smooth
boundary attainment or compatibility of saturated pieces at shared nodes
is not asserted. A full smooth dynamics problem can impose more constraints.

The formulas use dimensionless observed distance ratios. No numerical
`r_d` or `H_0` is needed. If a family supplies `Omega_k`, the conversion
is `kappa=Omega_k (H_0 r_d/c)^2`; the single amplitude nuisance and
curvature must remain tied consistently across intervals.

## Minimum required variation: the direct successor quantity

For fixed endpoints and curvature, define `L_0=|log(b/a)|/Delta`.
At `L=L_0`, the interval in (2) collapses to the unique exponential
bridge area

```text
J_0 = Delta (b-a)/log(b/a)   if a!=b,
J_0 = a Delta              if a=b.
```

For `L>L_0`, `J_minus` strictly decreases toward zero and `J_plus`
strictly increases without bound. This follows directly from their
pointwise envelopes: for every interior t both lower candidates decrease
strictly and both upper candidates increase strictly with L. Thus:

- if `J=J_0`, `L_min=L_0`;
- if `0<J<J_0`, a unique `L_min>L_0` solves `J_minus(L_min)=J`;
- if `J>J_0`, a unique `L_min>L_0` solves `J_plus(L_min)=J`.

The class is feasible exactly when `L>=L_min`. Any positive finite node
data have a finite required variation; unconstrained smoothness imposes
no common upper bound on it. For a fixed shared kappa, the largest
interval `L_min` is the required common variation budget. If kappa is
allowed to range, feasibility must be profiled over that **one common
allowed curvature**, with its nuisance relations preserved.

A concrete exact control takes `a=b=Delta=1`, `L=2 log 2`. The allowed
area is `[1/(2 log 2),1/log 2]`. The synthetic area `3/(4 log 2)` passes;
`1/(4 log 2)` and `2/log 2` fail. Both failing areas remain realizable
without the declared variation bound by Theorem 1. These are synthetic
controls, not DESI measurements or confidence levels.

## The local scalar horn: the full vacuum constraint still leaves unbounded slopes

The current ledger [LT-GR2e](../../../process/conditional-physics-ledger-v0.263.json)
retains an action-owned cosmological solution and held-out observables as
an open construction. Its cited [local scalar-horn result](../../../../explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md)
supplies, in its own convention,

`alpha R + lambda Box R = 2 rho_vac`, with `lambda=3 beta^2/kappa_action`.

Here `alpha` is an action coefficient; `kappa_action` is not the spatial
curvature kappa above. This is a trace equation, not the complete metric,
matter, observation and initial-state system. We first identify the
trace-level freedom, then check whether the full homogeneous vacuum metric
constraint of this particular local action removes it.

On its regular `lambda!=0` branch, take flat FLRW, constant rho_vac,
signature `(-,+,+,+)`, and set `P=dot R`. The trace-only system is

```text
dot H = R/6-2H^2,
dot R = P,
dot P = (alpha R-2 rho_vac)/lambda - 3H P.            (3)
```

This smooth vector field has a local solution for arbitrary finite initial
`H_0>0`, `R_0`, `P_0`. Choose any real s and
`R_0=6(2+s)H_0^2`. At `z_0=0`, standard redshift gives

`(d log H/dz)_0 = -dot H_0/H_0^2 = -s`.

Thus the trace alone cannot imply any finite universal L. It would be
premature to stop here: the missing homogeneous metric equation can be
computed for the inherited local action itself.

Write its scalar variable as `u` to distinguish it from cosmic time:

```text
I_sc = integral sqrt(-g) [(alpha+beta u)R + kappa_action u^2/2 - rho_vac].
```

The algebraic equation `u=-beta R/kappa_action` gives the equivalent
metric action, for fixed nonzero `kappa_action`,

```text
f(R) = alpha R - b R^2/2 - rho_vac,
b = beta^2/kappa_action != 0,     F=f_R=alpha-bR.
```

This is metric f(R) variation, not Palatini variation or the complete
ambient GU action. Its vacuum equation is

`F R_ab - f g_ab/2 + (g_ab Box - nabla_a nabla_b)F=0`.

The flat-FLRW 00 equation follows directly by using
`R_00=-3(dot H+H^2)` and the derivative contribution `3H dot F`:

```text
3 F H^2 = (F R-f)/2 - 3H dot F
        = -bR^2/4 + rho_vac/2 + 3b H P.             (4)
```

The factor `rho_vac/2` follows the action's displayed normalization.
The standard metric f(R) equations and their conventions are independently
available in [De Felice and Tsujikawa, equations (2.4), (2.15)–(2.16)](https://arxiv.org/html/1002.4928v2).
Those field equations are prior art; the specific substitution and freedom
analysis here are a new repository calculation, without a novelty claim.

Define

`C=3(alpha-bR)H^2+bR^2/4-rho_vac/2-3bHP`.

Equation (3), with `lambda=3b`, gives the exact propagation identity
`dot C=-4HC`. Consequently, for **every** fixed `H_0>0` and real `R_0`,
the finite initial value

`P_0=[3(alpha-bR_0)H_0^2+bR_0^2/4-rho_vac/2]/(3bH_0)`

satisfies `C_0=0`; the locally unique smooth solution preserves it.
The trace and 00 equation then imply the isotropic spatial metric equation;
its residual is exactly `(4/3)C` after the trace substitution.
This is an actual local homogeneous vacuum solution of the declared
f(R) action, rather than a solution of its trace alone. The probe also
checks the spatial Friedmann equation independently after substitution.

It follows that the unbounded initial-slope construction survives the full
vacuum equations of this local horn. Even imposing `F_0>0` leaves an
unbounded direction: `R_0<alpha/b` for `b>0`, or `R_0>alpha/b` for
`b<0`. Continuity preserves `H>0` and `F>0` for a sufficiently short
interval. Thus fixed coefficients, fixed vacuum source, fixed `H_0>0`,
and a positive F alone imply no finite uniform bound on
`|(d log H/dz)_0|`. The singular `b=0` branch is excluded.

The size of the existence interval can depend on the initial data. This
does not prove extension to a fixed survey interval, stability, physical
matter content, a source-native observation map or arbitrary node fitting
by this f(R) family. In particular, the finite-dimensional full-horn
solution family does **not** inherit Theorem 1's freedom to interpolate
every dataset. It can be tested once coefficients and a physical initial
state/domain are specified. The demonstrated missing input for a uniform
L is a restriction on that solution family or initial data, not the mere
instruction to calculate its already available 00 constraint. The full
ambient GU action and matter sector may impose additional restrictions.

Two existing corrections remain decisive. The
[sigma-sign package](../../../process/sigma-dark-energy-sign-nonselection-package.json)
does not select a physical cosmological sign or an equation of state.
The [B3-DE likelihood disposition](../../../../explorations/conditional-build/b3-de-likelihood-scope-disposition-2026-08-23.md)
retains the empirical likelihood information while rejecting literal
pointwise use of CPL coordinates. Nothing here restores a forced no-phantom
condition, dismisses crossing evidence, or relabels Mannheim as native GU.
The [earlier Weyl-only result](../mannheim-compatibility/mannheim-gu-compatibility-and-desi-2026-10-27.md)
is reused solely for its scoped FLRW nonselection boundary.

## Consequential next calculation and acceptance ceiling

The next useful conditional late-time candidate must export its physical
metric/redshift convention, one curvature or a bounded shared domain, and
either a fixed expansion family or a derivation of an interval bound L.
For example, an independently established deceleration bound can be
converted using `d log H/dz=(1+q)/(1+z)`; no such bound is assumed to
have been supplied by GU here. Apply (2) or compare its L to `L_min`;
then evaluate the surviving family with the actual windows, templates,
nuisance parameters and correlated likelihood. This is a concrete way to
obtain a late-time conditional test before an early-universe ruler derivation.

An observed point outside (2) excludes the declared curvature/variation
class, subject to the observation interface. A point inside it proves only
geometric log-Lipschitz realizability, not a physical solution or empirical
confirmation. A fitted bound, curvature or background must be counted as
fitted. The current artifact makes no empirical significance claim.

The accompanying probe checks exact curvature identities, a finite C2
interpolation control, independent integrals of the exponential envelopes,
synthetic feasibility cases, scaling, action elimination, full homogeneous
vacuum constraint propagation and initial-data algebra.
It deliberately corrupts formulas and requires genuine failed checks after
a clean baseline. These finite checks supplement the written C-infinity
construction, Lipschitz sufficiency and local-ODE arguments; they do not
certify those continuum results by sampling. The probe passes 47 exact finite
checks and rejects 11 altered-equation faults. Independent internal review
accepted the written proofs and their scope; this is not external-expert or
proof-assistant certification. Reproduce with:

`python tests/channel-swings/late_time_finite_node_identifiability_probe.py`
