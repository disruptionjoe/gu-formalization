---
title: "K1898: Exact stochastic pulse energy and coherence"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: massless rank-four R1 control with supplied classical scalar noise; exact mean free excitation energy and coherence, no 3D white-noise or native GU transfer
scripts:
  - tests/channel-swings/k1898_stochastic_pulse_energy_coherence.py
  - tests/channel-swings/k1898_stochastic_pulse_energy_coherence_probe.py
---

# K1898: Exact stochastic pulse energy and coherence

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
result: exact colored-noise and white-noise coherence with finite energy and explicit heating and budget laws
carrier: massless rank-four Dirac field on R with two components per propagation direction LAYER=toy CHIRALITY=N/A
pairing: positive L2 and free filled negative-energy CAR sea ON=declared_massless_1D_sea
real_structure: complex fermions and real scalar random potentials
grading: CAR parity and two right/two left propagation channels
action_owner: repository-construction -- supplied classical pulse law independent of field state
target: causal averaged dynamics, neutral coherence and excitation energy MAP-TYPE=intertwiner
```

## 1. Exact transport, not a three-dimensional approximation

Use the massless one-dimensional control of
[K1896](k1896-local-phase-vacuum-boundary-2026-10-21.md):
h=-ic diag(1,1,-1,-1) partial_x, c=1/24, on L2(R,C4).
For a real smooth scalar potential V(t,x), the r=+/- characteristic solution is

```
psi_r(t,x)=exp(-i Phi_r(t,x-rc t)) psi_r(0,x-rc t),
Phi_r(t,z)=integral_0^t V(s,z+rc s) ds.                  (1)
```

The interaction-picture map is multiplication by exp(-i Phi_r).
Each channel has spin multiplicity two. For compact smooth Phi, or the
Schwartz profiles below, its expected free sea excitation energy is exactly

```
E_exc[Phi] = c/(2pi) sum_(r=+,-) integral |partial_z Phi_r|^2 dz. (2)
```

To derive (2), opposite energy signs restrict incoming momentum q to the
interval between0 and -k. For one channel, multiplicity2 and the Fourier
convolution factor (2pi)^-1 give a factor1/pi. Particle plus hole energy on
that interval integrates to c k^2/2 for each sign of k. Thus each r contributes
c/(2pi) integral k^2 |(exp(-i Phi_r)-1)_hat(k)|^2 dk.
Parseval and |partial exp(-i Phi)|^2=|Phi'|^2 prove (2).
The constant already includes both particles and holes; it is half the
K1896 common-phase coefficient for each r, and adding both recovers that result.

This is conditional independent mathematics. SC-META-53 remains UNCERTAIN;
SC-OP-04 ASSERTS candidate grammar and SC-MAS-01 / SC-CHI-02 ASSERT the
stylized mass toy, not this stochastic massless reduction. LT-SM8/AC-F1 and
all source/physics/canon verdicts are unchanged. No native full20 bridge,
physical noise law, bath or vacuum selection is asserted.

## 2. Colored noise: exact coherence and the missing expectation condition

Take V(s,x)=xi(s) theta(x) with supplied state-independent real noise.
Let F_r(z)=integral xi(s)theta(z+rcs) ds on a finite interval.
For a centered Gaussian process with covariance C(s,u),

```
K_r(z,w)=integral ds du C(s,u) theta(z+rcs) theta(w+rcu),
eta_r(z,w)=exp[-(K_r(z,z)+K_r(w,w)-2K_r(z,w))/2],       (3)
mean E = c/(2pi) sum_r integral dz ds du C(s,u)
                   theta'(z+rcs)theta'(z+rcu).          (4)
```

Formula(3) is the multiplier of the neutral two-point coherence kernel in
the interaction picture. For genuine bounded observables, smear that kernel
against test functions; a single scalar visibility factor applies only when
the phase multiplier is constant on their supports. Unsmeared fields are
operator distributions, not bounded CAR generators. The Gaussian
characteristic function gives (3), and Tonelli/applied quadratic-form
integrability gives (4). Positive semidefinite C makes the integrated variance
nonnegative even if individual entries of C have either sign. Finite absolute
integral of |C| and theta' in L2 is a sufficient condition for finite (4).
The full channel is a mixture of CAR automorphisms and generally not quasifree.

For the binary smooth pulse xi(s)=+/-a g(s), define
G_r(z)=integral g(s)theta(z+rcs) ds. Then

```
eta_r(z,w)=cos(a[G_r(z)-G_r(w)]),
mean E=a^2 c/(2pi) sum_r ||G_r'||_2^2
      <= a^2 c/pi ||g||_1^2 ||theta'||_2^2.             (5)
```

This supplies an all-order exact coherence and energy law, distinct from
K1896's short-time expansion. One sign persists for the whole pulse; in
general the average is not a Markov semigroup.

A useful countercontrol takes any nonzero compact smooth g,theta for which
G_r' is nonzero and a random integer amplitude A with
P(A=+n)=P(A=-n)=3/(pi^2 n^2), n>=1. These probabilities sum to1.
Every realized smooth pulse has finite energy, every corresponding sea state
is normal, and their countable mixture is normal, but E[A^2]=infinity.
Equation(5) proves infinite mean energy. This is an actual ensemble failure,
not evidence against finite mixtures or the compact-amplitude theorem in
[K1897](k1897-smooth-pulse-energy-2026-10-21.md).

## 3. Released white-noise model: finite energy at every finite time

Supply one Brownian motion B_s and the Stratonovich scalar drive
V(s,x) ds=sigma theta(x) circ dB_s. The exact characteristic phase is

```
Phi_r(t,z)=sigma integral_0^t theta(z+rcs) dB_s.        (6)
```

The integrand is deterministic, so Ito and Stratonovich agree here. For
compact smooth theta, finite time gives a smooth spatial phase modification
with compact support: differentiate in z in the Ito integral and use the
finite Sobolev moments of every order. In particular its H1 norm is finite
almost surely. The corresponding unitary is sea-implementable by the 1D
criterion; stochastic averaging gives a normal CP unital map.

Brownian independent stationary increments and deterministic autonomous
transport prove a strongly continuous Markov semigroup on the CAR algebra.
This is a random-unitary semigroup, not a claim of a bounded generator on
the entire algebra. Pathwise support moves only along x=z+rct, so the full
averaged dynamics preserves the cone of speed c. A common classical noise
can correlate distant systems but local even nonselective interventions
still cannot affect a spacelike observable: every path has the support
property, and averaging preserves the commutator identity.

Ito isometry now yields the exact finite-time laws

```
eta_r(t;z,w)=exp[-sigma^2/2 integral_0^t
                  (theta(z+rcs)-theta(w+rcs))^2 ds],   (7)
mean E(t)=c sigma^2 t/pi ||theta'||_2^2.                (8)
```

Thus temporal white noise is a finite-energy causal model in this 1D control,
with explicit linear vacuum heating. It is NOT a white-noise limit theorem
in 3D; K1897's smooth-pulse bounds give no uniform control of that limit.
No statement about all stationary states follows from heating this vacuum.
For two initially independent regions, common and independent noise differ
in cross-coherence via their covariance, while both retain causal support.
The measurable relation is between the supplied covariance and neutral
coherence, not a GU prediction.

## 4. Energy cost of coherence loss

For d=|z-w|>0, Cauchy--Schwarz on the interval between z,w gives
|Phi_r(z)-Phi_r(w)|^2 <= d ||Phi_r'||_2^2. Hence a centered Gaussian law obeys

```
mean E >= c/(pi d) [-log eta_r(z,w)].                  (9)
```

Here total energy may include an unequal second propagation channel, so only
one channel's contribution was used. For the homogeneous-in-time white law
(6), both channels have the same total energy. Applying the interval bound
inside(7) sharpens this to

```
mean E(t) >= 2c/(pi d) [-log eta_r(t;z,w)].             (10)
```

For a binary pulse, the corresponding bound is
mean E >= c/(2pi d) [arccos eta_r]^2, with arccos in[0,pi].
This uses the smallest possible phase difference consistent with the signed
coherence; phase wrapping does not evade the bound. These are rigorous
one-dimensional necessary costs for this mechanism, not universal
thermodynamic lower bounds or proven sharp optimizers. Finite smeared
measurements must use(3)/(7)'s actual kernel or justified plateau regions.

## 5. Explicit finite-energy control and a long-duration discriminator

For theta(x)=exp(-x^2/(2l^2)), l>0, use the 1D model on R. This spatial
profile is Schwartz but not compact. Its derivative norm is sqrt(pi)/(2l).
A deterministic constant-sign pulse of amplitude a on[0,T] gives
G_r'=[theta(x+rcT)-theta(x)]/(rc), hence

```
E_binary(T)=2a^2 l/(sqrt(pi)c) [1-exp(-c^2 T^2/(4l^2))],
E_white(T)=c sigma^2 T/(2sqrt(pi)l).                   (11)
```

The first pulse has sharp temporal endpoints, allowed by the exact 1D
transport proof; it is NOT an example satisfying K1897's smooth compact
3D hypotheses. The Gaussian overlap integral proves(11). At small T the
binary energy is a^2 c T^2/(2sqrt(pi)l); at long T it saturates while white
noise continues linear heating. Equal short-time strengths therefore do not
make the two operational models interchangeable. Smooth compact temporal
pulses use(5); they do not require this rectangular control.

## 6. Verification and hostile review

Exact checks derive the characteristic PDE, sign symmetry, energy factors,
Gaussian overlap and limits, covariance quadratic forms and expectation
counterexample normalization. An independent Fourier calculation and Ito
variance arithmetic probe the formulas; deliberate coefficient, sign,
ensemble-tail and report/pin corruptions must fail after a clean baseline.
Numerical quadrature may illustrate Gaussian limits but is not the proof.

Hostile review separated covariance-kernel visibility from bounded smeared
observables, scalar versus channelwise multiplicity, pointwise and mean
energy, correlated noise and signalling, and 1D versus 3D. It retained
unbounded generator/domain cautions, actual pulse duration and imported
probabilities. No remaining claim of universal optimality, GU derivation,
microscopic bath or external specialist acceptance is made.
