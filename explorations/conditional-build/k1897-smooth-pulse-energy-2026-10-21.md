---
title: "K1897: All-order energy after a smooth Dirac pulse"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: weighted scattering estimate for a supplied smooth compact pulse and free massive target sea; no active-pulse energy theorem or native GU identification
scripts:
  - tests/channel-swings/k1897_smooth_pulse_energy.py
  - tests/channel-swings/k1897_smooth_pulse_energy_probe.py
---

# K1897: All-order energy after a smooth Dirac pulse

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
result: every finite one-particle excitation energy moment is finite after the pulse ends
carrier: K1896 rank-four massive Dirac target on R3 LAYER=toy CHIRALITY=N/A
pairing: positive complex L2 and free polarized CAR Fock space ON=declared_Dirac_sea
real_structure: Hermitian Clifford matrices and real scalar external potential
grading: positive/negative free spectral projections and CAR parity
action_owner: repository-construction -- externally supplied scalar pulse on the conditional target
target: weighted off-diagonal scattering and ensemble admissibility MAP-TYPE=intertwiner
```

## 1. Endpoint and exact scope

Let h=c(D.p+mu M), c=1/24, mu>0, with the actual four-component
Clifford target checked in [K1896](k1896-local-phase-vacuum-boundary-2026-10-21.md).
Set E=|h|, Q=sign(h), P_±=(1±Q)/2. Supply a real scalar
V in C_c^infinity(R_t x R_x^3), and let U solve i d_t U=(h+V(t))U
on H^1. Bounded smooth V gives a unique unitary evolution on the common
domain. Choose a<b outside its time support and define
S=exp(i b h)U(b,a)exp(-i a h). The sea is P_-.

For every finite m>=0,

```
J_m = ||E^(m/2) P_+ S P_-||_HS^2
    + ||E^(m/2) P_- S P_+||_HS^2 < infinity.              (1)
```

J_0 is total particle-plus-hole count; J_1 is the positive free excitation
energy after the pulse, without subtracting divergent positive terms. These
are moments of the one-particle excitation distribution, NOT automatically
moments of the total many-body energy random variable. This closes the
all-order post-pulse finiteness gap in K1896. It provides an explicit analytic
bound below in terms of regularized operator seminorms, not an evaluated
experimental energy budget or a sharp numerical constant.

This construction imports CAR, a free sea and an external pulse. SC-META-53
is UNCERTAIN, SC-OP-04 ASSERTS candidate operator grammar and SC-MAS-01 /
SC-CHI-02 ASSERT a stylized mass toy. None selects these imports. LT-SM8,
LT-GR6b and AC-F1 remain unchanged; source full20/injection/K-C/accessibility
identification is still open. No source claim or canon verdict moves.

## 2. Input theorem and its hypotheses

Use the finite-order regularization construction of
[Langmann and Mickelsson, Lemma 2.12 and its iteration](https://arxiv.org/pdf/hep-th/9509034),
pages 4--6. For a smooth bounded interaction and Dirac h, each iteration
improves the order of [Q,A] by one. Any finite number p of iterations gives
a unitary time-dependent change of variables T_p, equal to identity where
all interaction jets vanish, with transformed Hamiltonian h+A_p and
[Q,A_p] of order -p. The construction applies on R^3 with spatial decay.
Here mu>0 makes E inverse nonsingular, the scalar h norm is elliptic of
order one, V has all derivatives and compact spacetime support. Its spatial
symbol and all derivatives decay rapidly. Products, commutators with h,
regularized inverses and the finite exponential construction preserve a
localized symbol class. Thus [Q,A_p] has rapid spatial decay as well as
order -p. We use this established construction, without a novelty claim.

The cited unweighted implementability conclusion alone does not prove (1).
The next argument supplies the additional energy weight explicitly.

## 3. Weighted estimate, including the noncompact space

Put W_s=(1+h^2)^(s/2), s>=0. Choose an integer p>s+3/2. The localized
symbol b_s of W_s[Q,A_p] satisfies, for arbitrary N and suitable finite C,

```
|b_s(x,xi)| <= C (1+|x|)^(-N) (1+|xi|)^(s-p).
```

The same symbol estimates hold for the needed derivatives. With N>3/2,
b_s belongs to L2(dx dxi). In Kohn--Nirenberg quantization, Plancherel
identifies the Hilbert--Schmidt norm squared with
(2pi)^(-3) integral tr(b_s* b_s) dx dxi. The momentum integral converges
because 2(p-s)>3. This supplies spatial integrability; negative order
alone on R^3 would NOT suffice. Denote
B_s(t)=||W_s[Q,A_p(t)]||_HS, a finite continuous, integrable function.

The transformed evolution U_p preserves H^s. Indeed h commutes with W_s,
and A_p is order zero, so W_s A_p W_s^-1 is bounded. In the interaction
picture the elementary Gronwall estimate gives

```
||W_s U_p(b,t) W_s^-1|| <= M_s(b,t),
M_s(b,t) = exp(integral_t^b ||W_s A_p(v) W_s^-1|| dv).   (2)
```

The commutator Duhamel identity, first on smooth vectors and then in the
weighted Hilbert--Schmidt ideal, is

```
[Q,U_p(b,a)] = -i integral_a^b U_p(b,t)[Q,A_p(t)]U_p(t,a) dt.
```

Right multiplication by U_p(t,a) preserves HS norm. Consequently

```
||W_s[Q,S]||_HS <= integral_a^b M_s(b,t) B_s(t) dt.      (3)
```

Endpoint T_p(a)=T_p(b)=I identifies the transformed scattering with S;
free endpoint factors commute with Q and W_s. The Bochner integral is
legitimate because its norm is bounded by the integrable right side.
Since [Q,S] has off-diagonal blocks 2S_+- and -2S_-+,

```
J_m = (1/4)||E^(m/2)[Q,S]||_HS^2
 <= (1/4)(integral_a^b M_(m/2)(b,t) B_(m/2)(t) dt)^2.  (4)
```

For energy m=1, p=3 suffices. The borderline p=2 gives a logarithmically
divergent comparison integral and cannot establish the claim. No Dyson
truncation or small-amplitude assumption entered. Any fixed finite amplitude
is allowed; the bound need not be uniform as amplitude grows or duration
shrinks. Higher m uses a deeper finite regularization, not a claim that one
fixed-order remainder controls every moment.

## 4. Released ensemble and composition consequences

A finite mixture of these completed pulses is normal in the same sea
representation, causal under its actual finite-duration evolutions, and has
finite J_m equal to the probability-weighted sum of (1). Implementer phases
cancel in the channel. In particular the +/- binary pulse in K1896 has finite
POST-PULSE excitation energy at all amplitudes. A compact amplitude family
V_lambda=lambda g theta, |lambda|<=L, also has a uniform version of (4):
the finite regularization depends continuously on lambda in the required
symbol seminorms; their maxima and the Gronwall exponent are finite. Any
probability law on that compact interval therefore has finite moments.

More generally it is sufficient that the squared right side of (3) be
integrable over the pulse law. Pathwise finite energy alone does not imply
finite mean energy. [K1898](k1898-stochastic-pulse-energy-coherence-2026-10-21.md)
gives an exact heavy-tailed smooth-pulse counterexample in a separate 1D
model. A countable convex mixture can be normal while its energy is infinite.
The normal state cone is closed under summable positive mixtures; energy is
an unbounded observable. These are distinct conditions.

Every fixed finite concatenation of smooth compact pulses is itself a smooth
compact potential (including overlapping pulses), so (1) applies. There is
no automatic bound for infinitely many pulses, unbounded random amplitudes,
white temporal noise, or a stationary noise limit in three dimensions.

### 4.1 Same-model operational consumer: exact finite-energy decoherence in 3D

The 1D control is not needed to prove that the 3D repair causes genuine noise.
Choose normalized orthogonal smooth spinor packets f1,f2 supported in disjoint
balls of radius r. Fix a duration T. Choose a real compact smooth theta equal
to constants theta1,theta2 on the respective balls enlarged by cT, with an
additional positive margin; choose centers separated enough for these larger
balls to be disjoint. Let g be smooth, supported strictly inside(0,T), and
G=integral g. Supply V_xi=xi a g(t)theta(x), xi=+/-1 equally likely.

Finite propagation keeps each free evolved packet inside its constant-potential
plateau for the full interval. Uniqueness of the Dirac evolution therefore gives

```
U_xi(T,0) f_j = exp(-i xi a theta_j G) exp(-i T h) f_j,
S_xi f_j = exp(-i xi a theta_j G) f_j.                  (5)
```

This is exact at any positive mass, without an adiabatic or Born approximation.
For the bounded neutral CAR observable X=a*(f1)a(f2), the interaction-picture
averaged channel has

```
T(X)=eta X,   eta=cos(a G (theta1-theta2)),
T(X*X)-T(X)*T(X)=(1-eta^2) X*X.                       (6)
```

Equal plateau values give eta=1, the common-phase control. Choose G=1,
theta1=1, theta2=-1, a=pi/4: eta=0 and the two-mode neutral coherence is
fully removed. Both histories satisfy the smooth compact pulse hypotheses,
so their average has finite POST-PULSE sea excitation energy by(4). The
physical evolution preserves speed c throughout the finite duration. Thus one
specified 3D construction simultaneously supplies exact nontrivial even
coherence loss, a causal evolution and finite final sea excitation energy.
It does not merely combine a 3D theorem with a different 1D example.

The full two-mode matrix algebra is invariant under each scattering map,
because both f_j are eigenvectors. On its one-occupation subspace the equal
superposition becomes the diagonal equal mixture for the above parameters;
this is an exact finite CAR control, not a claim that compact f_j are pure
positive-energy particle states. At phase difference pi, eta=-1 and the map
on this coherence is a deterministic sign change, not coherence loss; the
squared modulus and the defect in(6) distinguish these cases. No universal
numerical energy price for the plateau construction is claimed. Its cost is
bounded by(4) for the chosen smooth g,theta. The common random sign and the
accessible CAR algebra are explicit external data, not a GU-derived bath.

### 4.2 Released limit test: finite-duration energy has no uniform impulse bound

Fix a nonconstant real compact smooth theta and a nonnegative smooth g
supported strictly inside(0,1), with integral g=1. Let
V_tau(t,x)=tau^-1 g(t/tau)theta(x), tau>0. Every pulse obeys(1), but

```
liminf_(tau -> 0) J_0(S_tau)=infinity,
liminf_(tau -> 0) J_1(S_tau)=infinity.                  (7)
```

This is an all-order limit obstruction, not a Born asymptotic coefficient.
In rescaled time s=t/tau the Hamiltonian is tau h+g(s)theta. At tau=0
the exact solution is exp(-i G(s)theta), G(s)=integral_0^s g.
For f in H1, variation of constants and unitarity give

```
||U_tau(tau,0)f-exp(-i theta)f||
 <= tau integral_0^1 ||h exp(-i G(s)theta)f|| ds
 <= tau (||hf||+c||grad theta||_infinity ||f||).         (8)
```

The last bound uses 0<=G<=1 and the Hermitian Clifford identity
||D.grad theta||=|grad theta|. By density and unitarity this gives strong
convergence on L2. The free endpoint factor also converges strongly to I,
so S_tau converges strongly to multiplication by exp(-i theta).
The Hilbert--Schmidt norm of each off-diagonal block is lower semicontinuous
under strong convergence: restrict first to any finite orthonormal input
set and sum its squared output norms, then take the supremum. K1896 proves
that the limiting nonconstant phase has infinite off-diagonal HS norm in
3D. The extended lower-semicontinuity inequality proves the first claim in(7).
Finally E>=c mu>0 gives J_1>=c mu J_0 and proves the second.

Thus smoothness repairs each finite pulse but cannot give a uniform finite
particle or energy budget at fixed nonconstant phase as its duration tends
to zero. This rigorously excludes using the post-pulse theorem to justify
an instantaneous finite-energy jump at fixed phase. It does not give a
divergence rate, classify weak-amplitude/rate joint limits, or exclude a
fixed-duration finite-energy colored model. The plateau decoherence example
in section4.1 is one such fixed-duration model.

## 5. Endpoint, locality and representation cautions

The proof requires interaction jets to vanish at both endpoints. During a
pulse the dressing T_p need not be identity; its weighted commutator cannot
be discarded. K1896's massive scalar-potential implementability at an active
time supplies an unweighted condition, and remains valid, but it is not a
finite-energy proof at that time. No claim of intermediate-time infinite or
finite energy is made here. Compressing a finite pulse into an instantaneous
kick destroys the estimates; K1896's divergence is consistent with (4).

Spatial propagation uses the ORIGINAL local Dirac equation, whose scalar
potential cancels in the probability-density balance and whose flux speed
is bounded by c. T_p is a proof device, not a local physical operation. The
scattering S is an interaction-picture endpoint map, not a zero-duration
causal intervention. Finite-mixture causality is inherited pathwise over the
actual pulse duration. No microscopic bath or physical vacuum selection is
constructed.

## 6. Reproduction and hostile review

The producer checks the exact sign-block cancellation identity, weighted
particle/hole trace factor and strict integrability threshold. The separate
probe solves a two-level Sylvester cancellation directly, checks an explicit
rational unitary's particle/hole energy and integrates the radial comparison.
It mutates coefficients/thresholds and reports after first passing the clean
baseline. These finite checks do not prove the imported regularization lemma
or the continuum symbol calculus; sections2--3 identify that proof chain.

The strongest overclaim was replacing normality or all Schatten classes by
energy finiteness. The weighted Duhamel step avoids it. The strongest contrary
case is nonzero endpoint dressing or nonintegrable amplitude laws, retained
explicitly. The weakest transfer is noncompact spatial localization; the L2
symbol bound supplies the needed second decay condition. No independent
expert or formal proof assistant reviewed this result. Numerical energy
budgets, active-pulse energy and native GU identification remain open.
