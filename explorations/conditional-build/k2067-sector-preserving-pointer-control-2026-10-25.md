---
title: "K2067: Sector-preserving controls and positive-energy pointer readout"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive graph with imported pointer preparation and measurement; no source apparatus, causal laboratory or physical quotient
scripts:
  - tests/channel-swings/k2067_sector_preserving_pointer_control.py
  - tests/channel-swings/k2067_sector_preserving_pointer_control_probe.py
---

# K2067: Sector-preserving controls and positive-energy pointer readout

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: local bounded-control readout restriction and a lower-bounded derivative-pointer construction with quantitative costs
carrier: massive complex1408 graph H_D,+ tensor C352 on R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric and imported Born rule ON=declared_observed_graph
real_structure: complex completion; no source-real admissibility of the multiplicity qubit inferred
grading: energy sector and chosen multiplicity qubit, not physical fermion parity
action_owner: repository-construction -- K2062 massive graph with explicitly added derivative control
target: prepared-qubit measurement through compressed scalar position MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Bounded local Hermitian controls preserving the
fixed massive positive-energy sector at every intermediate time cannot change scalar
position readout at a common final time. A derivative coupling can perform an
arbitrarily accurate prepared-qubit readout on the same graph while keeping its
Hamiltonian lower bounded. Its explicit price is a larger propagation cone, supplied
pointer preparation and a momentum-dependent control. A finite parameter choice
certifies CHSH greater than2 without postselection. This is a conditional apparatus
construction, not source-selected physics or a claim of novelty for pointer models.

## 1. Inputs, prior work and the exact question

Use [K2062](k2062-bounded-local-multiplier-rigidity-2026-10-25.md)'s H0=C.D+m beta,
m>0, P=1_(H0>0), and [K2065](k2065-position-measurement-compatibility-2026-10-25.md)'s
Hplus=H_D,+ tensor C352, with C352=C2 tensor C176. Fix the positive Hilbert metric.
The qubit Pauli operators commute with H0 and P. Scalar readout is F_f=P f(X) P.
K2065 already supplies the abstract internal Bell extension; it supplies no control
which turns that extension into position records.
[K96](k96-observed-infinite-pointer-hamiltonian-record-wave-2026-09-02.md) already
constructs controlled translation with an unbounded-below Hamiltonian on a different
pointer. Generic controlled translation is therefore reused structure. The present
question imposes the same massive graph, energy positivity and explicit local-control
restrictions. No transfer of K96's compactly supported pointer or quotient is assumed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about rival
southeast terms; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56 DISAVOWS
an odd-action prerequisite. None supplies this Hilbert state, qubit, derivative
interaction, Born rule, tensor copies, preparation or apparatus. LT-SM8/GR6b and the
source real/dual/physical quotient remain open; source, ledger and canon are unchanged.
This is a reverse operational construction, with no GU confirmation credit.

## 2. Entire local bounded-control class is readout-blind

Let V_x(t,X) be a setting-dependent bounded Hermitian matrix multiplier, measurable
in t with locally integrable essential-supremum norm. Suppose EVERY two-sided
propagator U_x(t,s) of H0+V_x preserves Ran P. K2062 then gives

    V_x(t,X)=I4 tensor B_x(t) almost everywhere,
    U_x(T,0)=exp(-i H0 T) [I tensor W_x(T)],

where W_x is the time-ordered unitary of B_x. Arbitrary noncommutativity among B_x(t)
is allowed. Since W_x commutes with H0 and every scalar F_f,

    U_x(T,0)* F_f U_x(T,0)=exp(i H0 T) F_f exp(-i H0 T).

All settings, including different scalar response functions, remain postprocessings
of ONE freely evolved position POVM. K2065's Bell-locality result therefore applies.
The total elapsed time T is the same for all settings, with idle free evolution
included. Different observation times, final-time-only sector echoes, nonlocal or
unbounded controls are not covered. This is a new operational consequence of the
existing commutant theorem, not another proof of that theorem.

A quantitative version needs no unproved commutator-stability theorem. Suppose an
actual bounded control differs from a readout-blind B_x(t) by W_x(t) with
r_x=integral ||W_x(t)||dt. Duhamel gives ||U_x-U_x^0||<=r_x. For any effect 0<=F<=I,
centering at I/2 gives ||U_x*FU_x-(U_x^0)*FU_x^0||<=r_x. The compressed initial-sector
readout obeys the same bound even when the perturbation leaks out of that sector.
Using K2065's resource inequality on Alice's two settings gives

    CHSH <= min(2 sqrt(2), 2+4 sqrt(r_0^2+r_1^2)).

This lower-bounds distance from the full readout-blind dynamics, not leakage alone.
A small [P,V] without a norm approximation to B is not asserted to imply this bound.

## 3. A derivative control and its exact energy/domain boundary

Choose Z on the multiplicity qubit and real |lambda|<1. On the full carrier take

    H_lambda=H0+lambda D1 Z,
    U_lambda(T)=exp(-i H0 T) exp(-i a D1 Z),  a=lambda T.

The symbols commute with P. Their positive-sector eigenvalues are
E_p +/- lambda p1, E_p=sqrt(|p|^2+m^2), so

    inf spectrum(H_lambda|Hplus)=m sqrt(1-lambda^2)>0.

This follows by minimizing sqrt(p1^2+m^2)-|lambda p1| with transverse momentum zero;
wavepackets approaching the minimizing momentum prove sharpness. For |lambda|>1
the positive-sector Hamiltonian is unbounded below. At |lambda|=1 it is nonnegative
with infimum0, but the natural operator domain is larger than H1 on the cancelling
branch. The common H1 self-adjoint domain statement here is only for |lambda|<1:
(1-|lambda|)E_p <= E_p +/- lambda p1 <= (1+|lambda|)E_p proves equivalence of graph
norms, and the full carrier has the analogous absolute-eigenvalue bounds.

The coupling is a local FIRST-ORDER differential operator, not a bounded multiplier.
It commutes with the sector and evades section2's hypothesis explicitly. In direction
n, the principal eigenvalues are +/-1 +/- lambda n1, so the full-carrier maximum
characteristic speed is1+|lambda|. An elementary symmetric-hyperbolic energy estimate
gives that propagation cone; along e1 the extreme speed is attained at principal
symbol level. Thus any nonzero lambda in THIS family violates the original speed-one
cone. Hilbert positivity and tensor no-signalling do not establish relativistic
spacelike laboratories. We do not claim every sector-preserving apparatus must pay
this same cost or alter the fixed H0 to conceal it.

## 4. Normalized same-graph pointer and finite resource certificate

In a standard Dirac basis choose unit chi in C2 and

    u(p)=[sqrt((E_p+m)/(2E_p)) chi;
          (sigma.p) chi/sqrt(2E_p(E_p+m))],
    g_s(p)=(2 pi s^2)^(-3/4) exp(-|p|^2/(4s^2)),
    phi=Fourier_inverse(g_s u),  s>0.

Then ||phi||=1, P phi=phi, and phi is Schwartz. Since u(-p)=beta u(p), its position
density is even. Its x1 variance sigma_x^2 is bounded by

    sigma_x^2 <= 1/(4s^2)+4/m^2.                         (1)

For a proof write u=P(p)u0/sqrt(c), c=(1+m/E_p)/2>=1/2. We have
||partial_1 P||<=1/(2m), |partial_1 c|<=1/(2m), hence
||partial_1 u||<2/m. Normalization gives Re<u,partial_1u>=0; Parseval separates the
Gaussian derivative term1/(4s^2) from the bounded spinor derivative term. The parity
identity makes the first moment zero. This conservative bound is not optimal.

Prepare exp(i H0 T)phi at time0, independently of the setting. This explicit free
prechirp leaves momentum density and positive energy unchanged and cancels the common
free evolution at readout. It is a supplied preparation resource, not a source law.
The two branches at time T are T_a phi and T_-a phi, with T_a phi(x)=phi(x-a e1).
Reading x1>0 gives the effective qubit effect

    E_Z=(1-epsilon) Pi_+ + epsilon Pi_-,
    epsilon=integral_(x1>a) ||phi(x)||^2 dx <= sigma_x^2/a^2.   (2)

Orthogonal qubit labels remove cross terms. Rotate the qubit before the same
coupling to measure any chosen axis. This changes the setting but not phi or T.
Two tensor copies with a multiplicity singlet and the usual four axes give exactly

    S=2 sqrt(2) (1-2epsilon)^2.                          (3)

All outcomes are included. With s=m, lambda=1/2, T=20/m, a=10/m, equations(1)-(3)
give epsilon<=17/400, visibility>=183/200, and

    S >= 2 sqrt(2) (183/200)^2 >2.

The positive-sector lower spectral edge is sqrt(3)m/2. Jensen gives mean free energy
<=sqrt(m^2+3s^2)=2m. The control energy mean equals the same value on this preparation
because mean p1=0 for every internal qubit state. The full propagation cone is3/2.
Increasing T at fixed s and lambda decreases the supplied-preparation error bound;
there is no finite-temperature, source apparatus or laboratory-spacing assertion.
The Gaussian Fourier data make phi real-analytic in x, so a nonzero phi cannot
vanish on an open halfspace. This particular finite-a measurement is never exactly
sharp, even though its error can be made arbitrarily small.

## 5. Prepared-subspace accuracy is not uniform operator accuracy

For the halfspace effect F and U_a=exp(-iaD1 Z), the full Hplus effect is diagonal
in Z, with entries T_a* F T_a and T_-a* F T_-a. Its operator-norm distance from
I_D tensor Pi_+ is exactly1: on the plus qubit translate any normalized positive-energy
packet arbitrarily far into the wrong halfspace. Translation preserves Ran P and its
readout expectation tends to0 by L2 tail convergence. The difference has norm at least1
and at most1 since both terms are effects. There is no contradiction with(2), which
restricts to one declared prepared spatial state. An experimental error claim must
state that preparation class; it cannot be exported as a uniform observable identity.

## 6. Verification, hostile review and remaining question

Exact finite Clifford, spectral, qubit and pointer controls exercise the algebra and
resource arithmetic. The separate finite translation probe checks both output branches,
rotated settings and CHSH from actual probabilities; real faulty couplings/signs fail.
Written proofs above carry measurable-time, common-domain, continuum and tail claims.
Upstream actual1408 reduction is hash-pinned reuse. This is same-author checking, not
independent specialist, proof-assistant or novelty certification.

The strongest overclaim would identify our multiplicity qubit with source spin or
claim relativistic causality from unitary tensor no-signalling. The strongest contrary
route is a final-time echo, nonlocal bounded control, or a different principal-symbol
family preserving a fixed speed-one cone. The weakest bridge remains physical real/bar,
state and apparatus ownership. These are explicit next constructions, not disproven
classes. K96 and standard von Neumann pointer theory already own the generic idea;
see [Pointers for Quantum Measurement Theory](https://arxiv.org/abs/2203.11144) for
background, with no transfer of an unseen theorem into the argument here.
