---
title: 'BET-COSMOLOGY: regular initial states and constrained perturbations'
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: BET-COSMOLOGY
tier: T2
expected_delta: Test regular backgrounds and perturbations on the held EXP/COS actions
actual_delta: Held EXP/COS admit regular radiation backgrounds; finite-time zero momentum is generically
  not the exact regular branch. The constrained ideal-fluid perturbation system has three regular amplitudes,
  including independent scalar isocurvature, and exact Einstein constraint propagation. Negative COS mass
  curvature alone gives no unavoidable finite-interval inconsistency. No bet kill, full-CMB acceptance
  or GU inference.
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: Regular scalar background and three constrained perturbation amplitudes
carrier: real scalar plus perfect dust/radiation and scalar metric perturbations on flat FLRW LAYER=toy CHIRALITY=N/A
pairing: positive scalar kinetic and gradient principal form ON=declared_carrier
real_structure: real background and Fourier-conjugate perturbations
grading: none; no native GU chirality transfer
action_owner: repository-construction -- two previously frozen SPECULATIVE scalar potentials
target: regular initial-state and constraint equations MAP-TYPE=evaluation
```

program_target: BET-COSMOLOGY
tier: T2
expected_delta: Test regular background and constrained perturbation completion
actual_delta: Three regular amplitudes and exact constraint propagation; no empirical or source verdict

# Regular initial states do not select a cosmological perturbation prediction

Target BET-COSMOLOGY, T2. Existing EXP and COS actions only; zero new potential
variants or coefficient tuning. Classification CONVENTIONAL_COMPARATOR.

## Result

Both fixed scalar potentials admit a unique regular radiation-era background
for each limiting field value. The finite-start prescription p_i=0 is generally
not exactly that branch; its discrepancy is a decaying momentum mode, not a
new empirical exclusion. On the regular branch, the full constrained
scalar–perfect-fluid linear system has three independent regular amplitudes:
adiabatic, matter-entropy, and frozen-scalar isocurvature. In particular,
regularity does **not** remove the independent scalar seed.

The equations propagate the Einstein constraint exactly and remain regular
when the scalar momentum vanishes. The negative curvature of the cosine
potential does not produce an unavoidable finite-interval inconsistency:
its complete linear transfer is bounded for every fixed finite Fourier band
and positive-time interval. This is not a quantitative small-growth bound,
nonlinear stability theorem, or CMB fit. No bet is killed. No regular-branch acoustic fit is computed here. The existing
finite-start COS compressed-distance survivor remains a diagnostic only; a primordial
covariance and the full photon/baryon/neutrino/recombination likelihood are
still needed to decide empirical viability.

## 1. Object and source ceiling

Keep the November11 real canonical scalar in flat observed FLRW with dust
and radiation, U=V/(3 Mpl² H100²), x=phi/Mpl, p=phidot/(Mpl H100):

    U_EXP=U* exp(-sqrt(2)x),  U_COS=U*(1+cos x),
    U*=.6736²-.1430-2.4728e-5(1+.2271*3.046).

No potential parameter, acoustic root or BAO nuisance optimum is recomputed.
The analytic results apply to any limiting x0 on these fixed smooth
nonnegative potentials, including the interior states relevant to the prior
brackets. The background normalization is imported, not predicted.

SC-COS-50 ASSERTS variable, VEV-capable dark energy with a differential
identity, conditional on the DESI trend continuing. SC-COS-51/52 ASSERTS
an ad-valued connection one-form construction, not these scalar actions.
SC-COS-54 ASSERTS a movable-field relation while leaving the curvature-side
field/action unspecified.
LT-GR2e remains NEEDS. No scalar-to-native observation/action bridge is built.
This result therefore cannot change a source, physics-ledger or matrix
verdict. It is distinct from K2542's prepared f(R) perturbation limit.

The perturbation theorem below deliberately uses perfect pressureless matter
and a perfect radiation fluid with no anisotropic stress. It is a fully
constrained perturbation completion of that declared ideal-fluid comparator,
not a full CMB Boltzmann model. In particular, replacing the earlier effective
background radiation by this fluid does not certify neutrino perturbations.

## 2. The genuine regular radiation branch

Write R=omega_r>0, M=omega_m>=0 and

    q=R a^-4+M a^-3+p²/6+U(x),
    dx/da=p/(a sqrt(q)),
    d(a³p)/da=-3a² U_x/sqrt(q).

A regular radiation branch means x->x0 finite and scalar kinetic energy is
subdominant to R a^-4 as a->0. Consequently a³p->0. It therefore satisfies

    p(a)=-3a^-3 integral_0^a b² U_x(x(b))/sqrt(q(b)) db,
    x(a)=x0+integral_0^a p(b)/(b sqrt(q(b))) db.          (1)

For U C² near x0, put P=p/a² and X=(x-x0)/a⁴. In (1), the X-from-P
map has a bounded O(1) Lipschitz coefficient, while P-from-X and P-from-P
carry O(a⁴) and O(a⁸) factors. Choose a sufficiently small weight on X in
the product norm, then choose a sufficiently short interval; the combined
Volterra map is a contraction on a bounded ball. The R term keeps its
scaled denominator positive. This proves local existence and uniqueness
in the regular class. For analytic EXP/COS, the
solution is analytic in a. Expanding (1) gives

    p= -3 U1 a²/(5 sqrt(R)) + M U1 a³/(4 R^(3/2)) + O(a⁴),
    x= x0-3 U1 a⁴/(20 R) + 11 M U1 a⁵/(100 R²)+O(a⁶), (2)

where U1=U_x(x0). Future continuation to every finite a>0 follows from the
positive radiation term, rho_phi,N=-p², U>=0 and |x_N|<=sqrt(6).

By contrast, starting p_i=0 at a small finite a_i generally differs from (2).
In the radiation asymptotic expansion the homogeneous momentum discrepancy
is C a^-3, with leading C=3 U1 a_i^5/(5 sqrt(R)). If extrapolated backward,
its kinetic energy would grow as a^-6 and violate radiation dominance;
that asymptotic description must not be continued as radiation domination
past the point where it ceases to hold. Stationary potential endpoints give
an exact constant-field exception; an integrated-force cancellation is a
separate possibility at later turning points. This result neither changes
November11's stated finite-time IVP nor proves its late predictions wrong.

## 3. Complete linear equations and Einstein constraint

Set eta=H100 times conformal time, kappa=k/H100 (c=1), Hcal=a'/a,
v=x'=a p; prime denotes d/deta. Then a'=a Hcal and

    m=M a^-3, r=R a^-4,
    v'=-2 Hcal v-3a² U_x,
    Hcal'=Hcal²-(3/2)a²m-2a²r-v²/2.

Use Newtonian gauge

    ds²=a²[-(1+2Phi)deta²+(1-2Phi)dx²]

with zero anisotropic stress. Let y=delta x, z=y', density contrasts d_m,d_r,
and velocity potentials V_m,V_r defined by theta_j=kappa² V_j. Define

    Q=(3/2)a²(m V_m+(4/3)r V_r)+v y/2.

The full first-order evolution is

    Phi'=-Hcal Phi+Q,
    d_m'=-kappa² V_m+3Phi',       V_m'=-Hcal V_m+Phi,
    d_r'=-(4/3)kappa² V_r+4Phi',  V_r'=d_r/4+Phi,
    y'=z,
    z'=-2Hcal z-(kappa²+3a²U_xx)y+4v Phi'-6a²U_x Phi. (3)

The scalar density and pressure perturbations in units 3Mpl²H100² are

    delta rho_phi=(v z-v²Phi)/(3a²)+U_x y,
    delta p_phi  =(v z-v²Phi)/(3a²)-U_x y.

The remaining Einstein00 constraint is

    C=kappa²Phi+3Hcal Q+(3/2)a²(m d_m+r d_r+U_x y)
      +(v z-v²Phi)/2 =0.                               (4)

Direct differentiation using all of (3) and the background gives exactly

    C'=-Hcal C,                                        (5)

so an initially satisfied constraint stays satisfied. Differentiating the
momentum equation also gives the Einstein trace equation

    Phi''+3Hcal Phi'+(2Hcal'+Hcal²)Phi
      =(3/2)a²[r d_r/3+delta p_phi].                    (6)

Nothing divides by p, rho_phi+p_phi, or U_x. The equations are regular at a
frozen scalar or a potential extremum. Their principal scalar kinetic and
gradient signs are canonical regardless of U_xx.

## 4. Regular amplitudes: the missing scalar mode is real

For fixed finite kappa, a=sqrt(R)eta+M eta²/4+O(eta⁵). First eliminate d_r
using (4), which is legitimate since r>0. By (5), reconstructing d_r
from the constraint preserves its continuity equation; that fluid row has
not been discarded. Use scaled velocities
W_m=V_m/eta, W_r=V_r/eta and Z=eta z. The remaining six variables
Y=(Phi,d_m,W_m,W_r,y,Z) obey a regular-singular system

    eta Y'= [A0+O(eta)]Y,

    A0 = [ -1  0  0  2  0  0 ]
         [ -3  0  0  6  0  0 ]
         [  1  0 -2  0  0  0 ]
         [  1  0  0 -2  0  0 ]
         [  0  0  0  0  0  1 ]
         [  0  0  0  0  0 -1 ].                       (7)

Its zero eigenspace has dimension3; the other eigenvalues are -1,-2,-3.
The zero eigenvalue is semisimple and nI-A0 is invertible for every positive
integer n. Analytic recursion therefore gives a unique regular analytic
solution for each vector in ker A0. Conversely bounded solutions contain no
negative-exponent homogeneous mode; their three regular constants are the
same. One can equivalently define the conclusion for the analytic regular
branch alone; no arbitrary singular primordial state is admitted.

The three amplitudes are the common adiabatic curvature, matter-radiation
entropy, and independent scalar displacement. The omitted neutrino/baryon
relative modes belong to a larger CMB model, not this six-variable theorem.
Keeping the unconstrained seven variables would introduce a +1 mode with
nonzero C; counting that as a physical regular mode would be an error.

For the pure adiabatic amplitude Phi0, leading terms are

    Phi=Phi0+O(eta), d_r=-2Phi0+O(eta),
    d_m=-(3/2)Phi0+O(eta), V_m=V_r=Phi0 eta/2+O(eta²),
    y=-3 R U1 Phi0 eta⁴/10+O(eta⁵).                    (8)

The scalar term is required by its forced equation. Setting scalar
perturbations identically to zero on a rolling background is not the
adiabatic solution. The expression y~v Phi0 eta/2 also verifies the common
time-shift form without a singular fluid sound-speed ratio.

For a pure scalar-isocurvature amplitude S, with no leading adiabatic or
matter-entropy amplitude,

    y=S-kappa² S eta²/6+O(eta³),
    Phi=A eta⁴+O(eta⁵), A=-R U1 S/14,
    d_r=4A eta⁴+O(eta⁵), d_m=3A eta⁴+O(eta⁵),
    V_r=2A eta⁵/5+O(eta⁶), V_m=A eta⁵/6+O(eta⁶).      (9)

The O(eta³) field remainder retains dust corrections. Momentum gives
5A=4A/5-3R U1 S/10; Einstein00 gives 21A+3R U1 S/2=0,
which agree. The uniform-total-density curvature tends to zero, while the
finite scalar displacement S cannot be removed by a regular time shift
because v=O(eta³). This is a genuine independent frozen-scalar seed.
At an exact stationary hilltop U1=v=0 the scalar mode is gravitationally
silent at linear order even though U_xx<0; that does not make it absent.

## 5. What the instability test decides

On any interval eta in [eta0,eta1] with eta0>0 and any fixed bounded Fourier
band, (3) is Y'=A(eta,kappa)Y with continuous bounded coefficients. The
background is regular, a>0, and U and its first two derivatives are bounded
on the compact field trajectory. Thus

    ||Y(eta)|| <= exp(integral_eta0^eta ||A|| ds) ||Y(eta0)||. (10)

This includes gravitational/fluid feedback and the scalar's negative mass,
not only a spectator Klein–Gordon equation. Equations (5)–(6) preserve its
physical constraints. Arbitrarily small regular amplitudes stay arbitrarily
small on each fixed finite interval. This rules out an asserted
amplitude-independent finite-time divergence from U_xx<0 alone. It does not
supply a numerically small growth factor or protect against nonlinear,
infinite-time, arbitrary high-frequency or empirically normalized growth.

For regular amplitudes A_ad,A_m,S, any later linear response takes the form
T_ad A_ad+T_m A_m+T_S S. The primordial covariance is an independent positive
semidefinite matrix on these amplitudes. The background acoustic fit fixes
none of its scalar-isocurvature amplitude or cross-correlation. Even if one
chooses pure adiabatic data, its amplitude/spectrum and the full transfer and
likelihood remain to be supplied. Neither a background survivor nor a
negative mass sign is a full CMB acceptance/exclusion.

## 6. Existing literature and next discriminator

The general-potential scalar/fluid perturbation framework and independent
scalar-isocurvature possibility are established, for example in
[Perrotta and Baccigalupi](https://arxiv.org/html/astro-ph/9811156v2).
Our contribution here is applying the constrained regular-branch check to
the exact held EXP/COS state prescription and recording the inference limit.
[The Doran et al. classification](https://arxiv.org/abs/astro-ph/0304212)
uses tracking quintessence; its abstract's no-additional-mode conclusion
cannot replace the frozen-branch calculation (7)–(9).

[Akrami et al.](https://arxiv.org/html/2504.04226v2) performs Bayesian inference
using CMB distance priors. It does not discharge this program's full-CMB
burden; marginalized exponential-slope constraints also do not reproduce the
fixed-slope, fixed-state-family likelihood-ratio test here.

Next useful empirical step: specify the regular scalar primordial covariance
(or explicitly restrict to adiabatic data), propagate the same held potentials
with photon/baryon/neutrino/recombination dynamics, and use a joint CMB
likelihood. This does not require inventing another potential. No extra BAO
profile, hilltop-sign computation, tracking-mode citation or p_i=0 convention
should be passed off as that test. The GU-native source bridge remains a
separate unbuilt datum and is not supplied by any cosmology outcome.

## Reproduction and acceptance ceiling

The companion exact symbolic probe checks the regular coefficients, complete
constraint and trace propagation, limiting mode classification, both regular
seeds, and frozen/incorrect-fluid countercontrols. The Volterra and regular-
singular existence arguments and compact-interval estimate are the analytic
proofs, not claims derived from finite checks. No numerical likelihood,
Boltzmann spectrum, global stability, Lean theorem or GU verdict is claimed.

## Fourier-mode scope

The physical three-mode classification is for kappa > 0 with a regular kappa -> 0 limit. The exactly homogeneous kappa = 0 sector needs separate background/gauge treatment: the 0i equation then has no spatial gradient.

## Preregistration retained


Target BET-COSMOLOGY; T2. Expected delta: distinguish true regular radiation-era initial data from finite-time p_i=0 and determine whether constrained perturbations force failure of either existing fixed scalar comparator. Kill only if all stated admitted completions contradict their requirements; negative Vxx, a finite-time mismatch or missing full-CMB data alone is not a kill. No new potentials, coefficient fitting, BAO/profile repeat, source or matrix transfer.

Reuse the exact EXP/COS actions and physical variables in bet-cosmology-fixed-potentials-2026-11-11.md. Retain Einstein/fluid constraints and adiabatic/independent scalar isocurvature seeds in variables regular at p=0. Source SC-COS-50/51/52/54 and LT-GR2e remain separate: these are speculative scalars, not an owned reduction of the source connection one-form. Required independent review and exact probes precede acceptance. This scope is recorded before the new calculation.

## Acceptance

Independent mathematical and hostile source reviews support internal T2 acceptance. All40 exact symbolic controls pass; no Lean or full-CMB result is claimed.

[Machine evidence](../../lab/process/bet-cosmology-regular-perturbations.json), [probe](../../tests/program-focus/bet_cosmology_regular_perturbations_probe.py), [review](../../lab/process/hostile-reviews/2026-11-24-cosmology-regular-perturbations-review.md).
