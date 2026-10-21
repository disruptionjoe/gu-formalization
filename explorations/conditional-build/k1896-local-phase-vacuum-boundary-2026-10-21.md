---
title: "K1896: Local phase noise versus the Dirac vacuum"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact rank-four constant-mass target polarization test and one-dimensional control; Born energy estimates and theorem-based all-order massive pulse implementability; no all-order energy or native GU theory
scripts:
  - tests/channel-swings/k1896_local_phase_vacuum_boundary.py
  - tests/channel-swings/k1896_local_phase_vacuum_boundary_probe.py
---

# K1896: Local phase noise versus the Dirac vacuum

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: three-dimensional local phase kicks fail Dirac-sea implementability despite algebraic causality; dimension and temporal-resolution controls
carrier: K1892 rank-four complex Dirac target on R3; explicitly separate massless R1 control LAYER=toy CHIRALITY=N/A
pairing: positive one-particle L2 pairing and polarized CAR Fock representation ON=declared_Dirac_sea
real_structure: complex Hermitian Clifford symbol and filled negative-energy spectral projection
grading: CAR fermion parity; electron/hole relative grading is not source graded-IG
action_owner: repository-construction -- supplied phase kick and chosen free Dirac polarization
target: implementability, excitation count and first-order temporal repair MAP-TYPE=intertwiner
```

## 1. Causality and vacuum admissibility are different demands

[K1895](k1895-causal-local-phase-noise-2026-10-21.md) proves a causal,
completely positive continuum CAR noise model. It does not select a vacuum.
Here choose the free negative-energy Dirac sea of the actual K1892 target.
Every nonconstant smooth compactly supported real phase theta gives a
multiplication kick u=exp(i theta) that **fails unitary implementability in
that representation in three spatial dimensions**, at every constant mass.
The transformed pure quasifree state is not a normal state in the original
irreducible sea representation. This does not invalidate the algebraic CAR
map, all possible representations, all temporal interactions or GU.

The Shale--Stinespring criterion is established theory; see
[Binnenhei](https://arxiv.org/abs/physics/9701009). For a unitary U and a
projection P, the polarized CAR automorphism is implementable iff [P,U] is
Hilbert--Schmidt. Equivalently both off-diagonal blocks are Hilbert--Schmidt;
pure quasifree polarizations in this class are unitarily equivalent. We use
that criterion and derive its actual target integral below. K146's relative
one-edge BdG result has a different operator and ultraviolet behavior; it
neither proves nor contradicts this result. No novelty is claimed.

SC-META-53 remains UNCERTAIN; SC-OP-04 ASSERTS candidate grammar and
SC-MAS-01/SC-CHI-02 ASSERT a stylized mass toy. No source selects this vacuum
or phase noise. LT-SM8/AC-F1, all source/physics-ledger/canon verdicts and the
full20 injection/K-C/accessibility debts remain unchanged.

## 2. Exact spectral test on the actual four-component target

Write h(p)=c(D.p+mu M), c=1/24, mu=24R, M=-i B, with the actual matrices
from K1836/K1840. They are Hermitian, square to I, pairwise anticommute,
have zero trace and tr(G_a G_b)=4 delta_ab. E_p=sqrt(|p|^2+mu^2), so

```
P_+(p)=(I+(D.p+mu M)/E_p)/2,   P_-=I-P_+,
tr(P_+(p) P_-(q))=1-(p.q+mu^2)/(E_p E_q).               (1)
```

The massless zero point is measure zero. Both projections have rank2.
Use the unitary Fourier transform vhat(k)=(2pi)^(-3/2) integral exp(-ik.x)v(x)dx,
v=u-1. The delta part of U vanishes between opposite projections. Thus

```
N_+ = ||P_+ M_u P_-||_HS^2
 = (2pi)^(-3) integral dk |vhat(k)|^2 integral dq
       [1-((q+k).q+mu^2)/(E_(q+k) E_q)].                (2)
```

This nonnegative integral is allowed to be infinite. It is the expected
positive-energy particle count in covariance U P_- U*, not a formal trace
of an infinite filled sea. The reverse block gives the corresponding hole
condition. One divergent block already violates the criterion.

## 3. Ultraviolet asymptotic and a rigorous divergence argument

For q=r n, |n|=1, fixed k and mu,

```
1-((q+k).q+mu^2)/(E_(q+k) E_q)
 = [|k|^2-(n.k)^2]/(2 r^2) + O(r^-3).                  (3)
```

The remainder is uniform on bounded k sets and the sphere for sufficiently
large r. The leading term is independent of mass. Integrating over n gives
4pi |k|^2/(3 r^2). For the explicit incoming-momentum cutoff |q|<=Lambda,

```
N_+(Lambda)/Lambda -> (1/(6pi^2)) integral |grad u(x)|^2 dx
                       = (1/(6pi^2)) integral |grad theta|^2. (4)
```

Here theta is smooth compact support, hence v is Schwartz. To justify the
limit, split into bounded k and its complement. On r>=2(|k|+|mu|+1), the
unit-vector difference representation of (1) bounds the overlap by C|k|^2/r^2;
on the remaining ball it is bounded by2. After radial integration and division
by Lambda>=1, a bound C_mu(|k|^2+|k|^3+1) suffices. This is integrable against
Schwartz |vhat|^2. Dominated convergence and Parseval prove (4). Alternatively,
a compact k set away from0 with nonzero vhat measure plus an angular belt
transverse to k gives a positive uniform multiple of integral dr, already
proving divergence without needing the full asymptotic.

A nonconstant smooth compact phase has positive gradient integral. Therefore
N_+=infinity and the phase kick is not implementable in the chosen sea Fock
space. Making its amplitude small but nonzero does not make it implementable.
Spatial smoothness removes large momentum TRANSFER k, but not the infinitely
many pairs with q large and p=q+k close to q. This identifies why spatial
smearing alone fails.

A useful exact massless control fixes |k|=1. Direct angular integration gives

```
integral_S2 overlap(r n+k,r n) dn
 = 4pi(1-2r/3), 0<=r<=1;
 = 4pi/(3r^2), r>=1.
```

Consequently the inner cutoff integral divided by (2pi)^3 is exactly
Lambda/(6pi^2)-1/(12pi^2) for Lambda>=1. This is a fixed-transfer calculation,
not a normalizable spatial profile or a substitute for the Schwartz proof.

## 4. Energy and weak-kick consequences

Weighting (2)'s integrand by c(E_(q+k)+E_q) gives a positive diagnostic with
leading coefficient

```
W(Lambda)/Lambda^2 -> c/(6pi^2) integral |grad u|^2.      (5)
```

This specifies an incoming-momentum cutoff diagnostic, not an unqualified
energy of a finite-cutoff density matrix. The positive-particle energy alone,
weighted by c E_(q+k), has half that leading coefficient; it diverges, which
already precludes finite excitation energy. The uncut electron-plus-hole
energy agrees with the symmetrized weight whenever finite; variable changes
are justified first for nonnegative integrands. No subtraction cancels this
positive excitation cost.

For u_epsilon=exp(i epsilon theta), the coefficient is exactly proportional
to epsilon^2. At two plateau regions the symmetric-kick decoherence rate is
Gamma=gamma[1-cos(epsilon Delta theta)]. In the weak-kick regime, keeping
Gamma fixed and nonzero keeps gamma epsilon^2 asymptotically nonzero, while
the ultraviolet excitation coefficient scales as gamma epsilon^2 Lambda
and energy as gamma epsilon^2 Lambda^2. This is a joint cutoff/weak-amplitude
coefficient statement; it is not a uniform all-parameter limiting theorem.
It rules out hiding this cost by merely taking weak kicks at compensating
large rate within that regime. Global constant phases have zero overlap and
are the control: they commute with the sea projector, but cannot damp neutral
hopping through a phase difference.

The kick-only Poisson mixture contains a nonzero one-kick contribution at any
t>0. Since normal positive functionals form a hereditary cone, it cannot be
normal in the sea representation if a constituent positive functional is
non-normal. This conclusion is immediate for exp(tK), including the symmetric
+/- kick law. We do not assert that arbitrary averaged free-interleaved
histories can be classified solely by inspecting one history.

## 5. A finite-energy one-dimensional control

Change the declared model to the massless rank-four target on R, with two
right-moving and two left-moving components. For v=u-1 with the following
integrals finite, opposite energy signs occur only when q and q+k straddle0.
The crossing interval has length |k|, spin multiplicity2. Hence

```
N_+ = (1/pi) integral |k| |vhat(k)|^2 dk,
E_exc = (c/pi) integral k^2 |vhat(k)|^2 dk
      = (c/pi) integral |u'(x)|^2 dx.                   (6)
```

The particle and hole numbers are both finite under this condition;
E_exc counts both, while each energy contribution is half the symmetric
integral. In particular every smooth compact phase works in this massless
one-dimensional model. Equation(6) is not a dimensional reduction theorem
for a three-dimensional vacuum.

An explicit smooth noncompact control is u(x)=(x-i a)/(x+i a), a>0.
It has |u|=1 and v=-2ia/(x+ia). Contour integration gives
|vhat(k)|^2=8pi a^2 exp(-2ak) for k>0 and0 for k<0, up to its irrelevant
value at k=0. Thus N_+=2, equal hole number2, and E_exc=2c/a.
Independently |u'|^2=4a^2/(x^2+a^2)^2 integrates to2pi/a.
This phase is not compactly supported and has winding; the formula explicitly
allows it, and opposite chiralities cancel net charge. It is a successful
finite-energy control of the same multiplication mechanism in a different
dimension, not a rescue of the three-dimensional instantaneous kick.

## 6. Released repair: temporal smoothing at Born order

The failure suggests resolving the impulse in time. Supply a classical scalar
potential epsilon g(t) theta(x), with real smooth compact g and theta, on the
same three-dimensional free target. Its first-order scattering off-diagonal
block has kernel

```
B_1(p,q)=-i (2pi)^(-3/2) theta_hat(p-q)
         g_tilde(c(E_p+E_q)) P_+(p)P_-(q),              (7)
g_tilde(omega)=integral exp(i omega t) g(t)dt.
```

This is the first Dyson term, derived by inserting the free spectral
projections into integral exp(i h t) M_theta exp(-i h t) g(t)dt.
There is no time Fourier normalization factor in g_tilde. Repeated integration
by parts gives |g_tilde(omega)|<=C_N(1+|omega|)^(-N) for every N.
Spatial theta_hat is also Schwartz. With k=p-q, at |q|>2|k| the total positive
energy grows at least linearly in |q|; in the complementary region spatial
Schwartz decay controls k and the volume in q. Therefore (7) is
Hilbert--Schmidt and remains so with every finite polynomial energy weight.
Unlike an instantaneous kick, its high relative-energy pair creation is
suppressed. This is an analytic estimate, not a finite-mode cutoff claim.

The exact classical Dirac equation with bounded real scalar potential also
retains speed c by the same energy-flux argument as K1892: the scalar
Hamiltonian term contributes no density source. Those two facts do NOT yet
prove that an all-order stochastic temporally colored model preserves the
sea folium or finite energy, has the desired reduced coherence rate, or is
Markovian. Equation(7) proves only the leading-order repair and exposes the
actual remaining all-order/noise-law obligation. Instantaneous effective
jumps obtained by compressing a finite-duration pulse would require a new
causality check; do not collapse the pulse to zero time after using its filter.

## 7. All-order implementability repair for a massive smooth pulse

For R>0, the checked four Clifford generators span M4(C), hence are unitarily
equivalent to the standard irreducible Hermitian Dirac matrices. Rescale time
tau=c t. The exact Hamiltonian becomes a standard positive-mass Dirac operator
with mass mu=24R and smooth compact external potential
A0(tau,x)=(epsilon/c) g(tau/c) theta(x), A_i=0.
[Deckert and Merkl, Theorem1.5 and Corollary1.4](https://arxiv.org/html/1505.06039v2#S1.SS1)
identify the polarization class by the potential tangent to a Cauchy surface
and implement evolution between those classes. On equal-time surfaces the
tangential potential is zero. The free sea class therefore works at both
ends: every finite-interval pulse propagator is implementable, at all orders.
This imports a theorem with its smoothness, compact support and positive-mass
hypotheses checked; the numerical certificate does not prove it. It establishes
normality, not a finite expectation of excitation energy. The massless case
is not inferred from this positive-mass theorem.

Choose a single independent classical sign xi=+/-1 with probabilities1/2
and retain it through the entire smooth pulse. Average the two exact quantum
evolutions with potentials xi epsilon g theta. Each is causal and sea-normal;
the finite mixture is also causal, completely positive, unital and sea-normal.
Implementer phases cancel in conjugation. This is an explicit colored-noise
repair, not an unspecified all-order hope and not the instantaneous Markov law.

For a neutral plateau coherence X with phase difference Delta theta, start
at a time s with g(s) nonzero. On smooth polynomial observables, the small-h
expansion of the averaged channel relative to free evolution is

```
T_(s+h,s)(X)-alpha_h(X)
 = -epsilon^2 g(s)^2 h^2 (Delta theta)^2 X/2 + O(h^3).    (8)
```

Odd powers of the random sign cancel; the double scalar-potential derivation
provides the displayed term. Smooth compact smearing and potential justify
this short-time expansion. It gives genuine even-coherence disturbance with
no spatial propagation outside the target cone. Resampling the sign at each
intermediate time changes the process; in general these averaged maps do not
compose as a time-homogeneous Markov semigroup. No microscopic bath, all-order
energy estimate, physical calibration or native GU selection is supplied.

## Verification and adversarial review

The producer verifies the actual K1836/K1840 Clifford matrices, trace overlap,
mass-independent expansion, angular/cutoff constants and exact one-dimensional
moments. The probe reconstructs an independent Pauli representation and exact
projectors at rational points, separately integrates the massless angular
formula, and checks the 1D interval and Laplace moments. It first passes the
baseline, then corrupts the overlap coefficient, cutoff coefficient, pulse
curvature, report and pin. A noncommuting free/potential matrix control checks
the second-order binary-pulse formula independently. Numerical angular integrals are convergence controls only; (2)--(7)
and their estimates establish the continuum conclusions.

Hostile review narrowed energy wording to its declared regulator, separated
total versus positive-particle energy, checked mass independence and Fourier
normalizations, retained the noncompact nature of the rational-phase control,
and refused to promote Born energy finiteness to an all-order energy theorem.
The separate all-order implementability statement uses the cited massive
external-field theorem after checking the Clifford, scaling and potential hypotheses. It also checked
that algebraic causality/positive states survive representation failure and
that the kick-only mixture argument is not silently extended to every
free-interleaved process. No external expert or formal proof assistant reviewed
these claims; no native GU, unique vacuum, general no-go or novelty claim.
