---
title: "K2154 Detector control with physical drift retained"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional detector mathematics; no GU recovery or total apparatus cost
scripts:
  - tests/channel-swings/k2154_uncompensated_detector_control_probe.py
---

# K2154 Detector control with physical drift retained

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
result: K2154 Detector control with physical drift retained
carrier: M finite oscillator sites with infinite Fock space and a degenerate qubit record LAYER=toy CHIRALITY=N/A
pairing: positive free Hamiltonian H_W and site-number quadratic forms ON=declared_carrier
real_structure: real canonical coordinates and complex Hilbert adjoint
grading: site oscillator number, not GU or fermion parity
action_owner: repository-construction -- supplied positive Hilbert dynamics and controls
target: full recorded error and mean switching-work bounds MAP-TYPE=intertwiner
```

## Result and supplied apparatus

[K2152](k2152-finite-chain-threshold-detector-2026-10-27.md) implements a threshold
exactly when physical free drift is compensated. Retaining that drift gives an
approximate complete recorded instrument whose error tends to zero as the
supplied controls become faster, at fixed finite site count and input-energy
budget. An explicit bound also prices the sum of absolute mean switching works.
The clock, pure-qubit preparation, readout and reset remain supplied resources.

Reuse M canonical pairs, W=W^T>0 with spectral bounds w_min,w_max,

    H_W=(p^T p+q^T W^2 q)/2-Z >=0, Z=tr(W)/2,
    c_j=(sqrt(nu)q_j+i p_j/sqrt(nu))/sqrt2,
    G=N_nu+M/2, C=max(1/nu,nu/w_min^2), D=max(nu,w_max^2/nu).

K2152 proves G<=C(H_W+Z) and H_W+Z<=DG. The same adjacent gather B sends the
fixed b_f mode to site1, followed by a bounded onsite qubit coupling and B†.
There are at most2(M-1) beam gates, each with generator

    K_j= +/- i g(c_j†c_(j+1)-c_(j+1)†c_j), g>0.

For a hard threshold use K_c=lambda P_k(n1) tensor X for duration pi/(2lambda).
Controls are piecewise constant, zero at the beginning and end. The ideal
Hamiltonian is K(t); the actual Hamiltonian is H_W+K(t). There is no drift
compensation, interaction-picture substitution or physical occupation cutoff.
The ideal instrument is exactly K2152's and its duration obeys

    T <= pi(M-1)/g+pi/(2lambda).                            (1)

The one-particle coupling g does not bound the beam Hamiltonian's Fock norm.
Large g may make an instantaneous total Hamiltonian unbounded below. The
selfadjoint dynamics below still exists; this supplied externally driven
model is not asserted to be a stable autonomous apparatus.

## Number growth with arbitrary control strength

Put x=sqrt(nu)q, y=p/sqrt(nu), B0=nu I-W^2/nu and
kappa=||B0||_op. Direct commutation gives

    i[H_W,G]=(y^T B0 x+x^T B0 y)/2,
    -kappa G <= i[H_W,G] <= kappa G                         (2)

as quadratic forms. Indeed the absolute expectation of the first expression
is at most ||B0|| ||x psi|| ||y psi|| <= kappa<G>.
All stated controls commute with G, including their qubit extension. Thus

    <G>_actual,t <= exp(kappa t)<G>_0,
    <G>_ideal,t = <G>_0,
    E_actual,t <= D exp(kappa t) C(E_in+Z)-Z.                (3)

This controls mean free-field energy and is uniform in control strengths
through their duration. It is not a bound on the total Hamiltonian, a
conditional rare branch, or a continuum limit. An outcome with probability
p>0 has mean field energy at most the unread upper bound divided by p.

## Uniform full-record error at bounded input energy

Let the initial field have mean H_W energy at most E and allow any reference
entanglement. Purify the input and prepare the same qubit |0> in both dynamics.
For the ideal and actual evolved vectors, on a justified core,

    |d<psi_ideal,psi_actual>/dt|
       = |<psi_ideal,H_W psi_actual>|
       <= sqrt(<H_W>_ideal <H_W>_actual)
       <= D exp(kappa t/2)<G>_0.

The middle inequality uses positivity of the FREE H_W, not positivity of
H_W+K. Since the vectors initially coincide,

    ||psi_actual(T)-psi_ideal(T)||^2 <= 2D<G>_0 I(T),
    I(T)=2 expm1(kappa T/2)/kappa if kappa>0, and T if kappa=0.

Pure-state trace distance is at most the vector distance. Common readout and
partial trace contract it. Hence for the COMPLETE recorded instruments,
including every outcome and arbitrary references,

    (1/2)||[(I_actual-I_ideal) tensor id](rho)||_1
        <= min(1,sqrt(2DC(E+Z)I(T))).                       (4)

Only marginal mean input energy is constrained; no energy variance assumption
is hidden. These are energy-constrained channel distances in the established
sense of [Shirokov](https://arxiv.org/abs/1706.00361). The general energy-limited
dynamics framework also studies growth and continuity bounds;
[van Luijk](https://link.springer.com/article/10.1007/s00220-025-05282-w) is nearby
prior art. The constants and detector composition here are derived above;
no novelty claim or replacement of the written domain argument is intended.

### Selfadjoint closures and the limiting argument

For each constant segment take the symmetric real quadratic Hamiltonian,
with its bounded threshold-qubit perturbation, on finite-particle vectors.
It raises total number by at most two and its norm on the number<=n sector
is bounded by a(n+b). Iteration gives a convergent analytic-vector series
for each finite-particle vector at sufficiently small time. Therefore each
segment has a unique selfadjoint closure. This does not rely on a small
relative bound for the beam control or assert one common operator domain D(G).

For estimates, compress with total-number projections P_L. They commute with
G and every ideal control. H_L=P_L H_W P_L remains positive, H_L<=DG, and
(2) survives compression. The finite-dimensional Gronwall and overlap
calculations prove(3)--(4). The compressed operators converge on the common
finite-particle core; essential selfadjointness gives strong resolvent and
unitary convergence for each segment, hence for their finite product.
Pass the overlap bound by strong convergence and the G bound by lower
semicontinuity. Approximate any finite-mean-energy input by number truncations
and purify, then pass to the limit. References are unaffected by every estimate.
This proof approximation does not change the physical Hilbert space.

## Explicit externally switched work account

Treat the record qubit as degenerate. At an instantaneous control jump s the
state is continuous and mean supplied switching work is <Delta K_s>. During
each constant segment the total energy is conserved. With K=0 at both ends,

    W_signed=sum_s <Delta K_s>=E_out-E_in.                  (5)

The G-growth bound makes every segment bounded on the G form space.
Finite-particle vectors are dense there; approximation in that norm passes
expectations of the G-form-bounded free and control quadratics and bounded
onlinear control, extending conservation and(5) to finite-mean-G inputs.
Record pinching leaves the reduced field and its energy unchanged. From
|K_j|<=g N_nu, the two jumps around each of at most2(M-1) beam gates, and
||K_c||<=lambda,

    sum_s |<Delta K_s>|
       <=4(M-1)g exp(kappa T)C(E+Z)+2lambda.                (6)

This is the sum of absolute MEAN switch works, not expected absolute
stochastic work, fluctuations, peak clock energy, or total apparatus expense.
It bounds the specified ideal sudden-switch schedule. Smooth switching would
require its own dynamics and work estimate. Increasing g and lambda reduces
(4) but generally increases(6); this is a sufficient construction, not an
optimal or necessary resource scaling. Starting with the free vacuum,
W_signed=E_out>=0, while individual switches may extract energy.

## Released composition with the optimal soft instrument

For the binary diagonal effect e(n) from [K2153](k2153-diagonal-detector-energy-2026-10-27.md),
set theta(n)=asin(sqrt(e(n))) in[0,pi/2]. After the SAME gather use

    K_soft=(2lambda/pi) theta(n1) tensor Y,
    tau=pi/(2lambda).

It has norm at most lambda and commutes with G. With the usual Pauli Y,
exp(-i theta Y)|0>=cos(theta)|0>+sin(theta)|1>. Undoing B gives the ideal
Kraus sqrt(1-e(n_b)) and sqrt(e(n_b)), realizing K2153's minimum at the
prescribed effects. Equations(1)--(6) hold unchanged with physical drift.
A boundary occupation is coherently rotated, not selected by an unrecorded
classical coin. Both outcomes remain in the return channel.

For the inherited finite-chain signal with energy E_h, choose E>=E_h to
compare vacuum and signal under one bound epsilon from(4). Each click
probability differs from its ideal value by at most epsilon; the equal-prior
error changes by at most epsilon. K2153's exact ideal energy is not automatically
the actual energy: trace-norm proximity alone does not control an unbounded
energy observable. Use(3) for the actual unread energy. This preserves a real
implementation guarantee without silently promoting channel convergence into
energy convergence.

### Why the input-energy restriction is necessary

If W=nu I, then H_W=nu N_nu commutes with every ideal gate. Thus the actual
output contains an extra exp(-i nu N_nu T). Superpositions of occupations
separated by n acquire relative phase nu nT. Taking T_n=pi/(nu n)->0 and
inputs (|0>+|n>)/sqrt2 in a spectator mode orthogonal to the measured mode
(M>=2) makes the ideal and actual outputs orthogonal while the detector record
is unchanged. The input energy is nu n/2. Consequently the family cannot
converge uniformly over unrestricted inputs. This countercontrol preserves
all outcomes rather than hiding phase in a discarded branch.

## Verification and remaining resources

The accompanying probe checks exact number-commutator and form constants,
soft pointer rotation (the classical-mixture comparison is checked in K2153),
reference-retaining records and work
counting, plus a finite compressed dynamical example explicitly classified
as numerical evidence. Analytic-vector, compression and all-Fock error proofs
receive separate independent internal review. No proof assistant, external
certification, remote CI or novelty claim is made.

The next apparatus question is a stable autonomous local controller with its
own clock, state preparation and reset resources, or a controlled continuum
limit of these finite models. The supplied all-occupation nonlinear onsite
control and classical switching do not provide those inputs. Source SC-OP-04
ASSERTS candidate grammar; SC-OP-05/SC-META-53 remain UNCERTAIN; SC-META-56
DISAVOWS the odd-action prerequisite. Scalar detector mathematics does not
supply GU's physical state, grading or observed2+1; ledger and canon are unchanged.
