---
title: "K2107: Finite-time arrival and contact resources"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, relativistic apparatus or physical recovery
scripts:
  - tests/channel-swings/k2107_parity_arrival_resources_probe.py
---

# K2107: Finite-time arrival and contact resources

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
result: conditional mathematical construction with explicit domain and approximation limits
carrier: fixed spatial wavepacket tensor finite memory-pointer code and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_positive_Hilbert_space
real_structure: complex adjoint; no source-selected real form
grading: even number-controlled pointer flips
action_owner: repository-construction -- supplied nonnegative covariant kinetic apparatus
target: operational instrument error and singular-contact coefficient cost MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and object boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. These
supplied positive Hilbert apparatus/algebra models are not equation9.16.
K2021 supplies local R0/R1; a source-selected positive observed algebra,
state and dynamics still need construction. LT-SM8/LT-GR6b, source-register,
ledger0.263 and canon remain unchanged. Native2+1, total/observed chirality,
full20 and K/C accessibility are distinct debts. This is reverse-scaffold
conditional mathematics, with no GU recovery, novelty or external certification.

## 1. Stationary scattering does not give a finite-time instrument for free

Use [K2105](k2105-semibounded-parity-mediator-2026-10-26.md), with G=I for
x<=0 and G=W for x>=L. Fix a normalized spatial preparation phi independent
of the code/reference, let phi_T=exp(-iTH0)phi, and define

    epsilon_i = integral_(x>0) |phi(x)|² dx,
    epsilon_f = integral_(x<L) |phi_T(x)|² dx.        (1)

Compare the actual isometry chi -> G exp(-iTH0)G*(phi tensor chi) with
chi -> phi_T tensor W chi. Insert G exp(-iTH0)(phi tensor chi). Unitarity
bounds the first difference by ||(G*-I)(phi tensor chi)||<=2sqrt(epsilon_i).
The second is <=2sqrt(epsilon_f), since G-W vanishes on x>=L. Thus

    ||actual-ideal|| <= delta=2(sqrt(epsilon_i)+sqrt(epsilon_f)). (2)

The estimate is uniform over normalized code/reference chi; any pointer
readout and spatial trace are contractive. For normalized diamond distance
D=one-half diamond norm, the full recorded parity channels obey

    D <= min(1,delta).                               (3)

The factor follows by comparing pure dilations and using trace-distance
contractivity, then convexity. This is a fixed preparation channel bound.
For a correlated initial spatial-code state one may use its actual spatial
marginals to get a statewise bound by the same two-step argument, with the
free marginal at T. It is not a uniform channel bound over all correlations
without a uniform preparation restriction. No spatial tail is silently
replaced by its square: norm error here is proportional to square roots.

## 2. Explicit Gaussian resource and waiting limit

Let phi have position mean -a<0, position variance sigma², momentum mean
p0>0 and zero position-momentum covariance, with amplitude proportional to
exp[-(x+a)²/(4sigma²)+ip0x]. Free evolution gives

    mu_T=-a+p0 T/m,
    sigma_T²=sigma²+T²/(4m² sigma²),
    epsilon_i=erfc(a/(sqrt2 sigma))/2,
    epsilon_f=erfc((mu_T-L)/(sqrt2 sigma_T))/2.       (4)

These are exact integrals of the normalized Gaussian; positive energy of
p² does not impose positive momentum. For fixed preparation and T->infinity,

    epsilon_f -> erfc(sqrt2 sigma p0)/2 >0.          (5)

Waiting alone cannot send the negative-momentum probability to zero.
Preparing larger p0 sigma or a different momentum distribution changes the
resource, not the waiting time alone. A nonzero compactly supported initial
packet also cannot be compactly supported after any fixed nonzero free time:
the free kernel expresses its evolved amplitude as a nonvanishing quadratic
phase times an entire Fourier transform of a compactly supported function.
Vanishing on an open exterior interval forces it to vanish identically.
This statement concerns compact initial support, not every L² state.

At fixed T, sigma_T² is minimized at sigma²=T/(2m), where sigma_T²=T/m.
That minimizes final variance ONLY; it need not minimize the two-tail error
or total energy for fixed a,L. For example choose the final mean L+b,
p0=m(a+L+b)/T. The free kinetic expectation then is

    E0=m(a+L+b)²/(2T²)+1/(4T).                      (6)

The actual product-input H energy is not automatically E0, since initial
Gaussian tails meet the interaction. Because D=p+A,

    sqrt(<H>) <= sqrt(E0)+||A(phi tensor chi)||/sqrt(2m)
               <=sqrt(E0)+||A||_infinity sqrt(epsilon_i)/sqrt(2m). (7)

Here chi is any normalized internal input; the last bound is uniform in chi.
The last inequality uses compact support of A inside[0,L]; bounded smooth
A and Gaussian domain justify it. Equation(7) distinguishes free preparation
energy from covariant apparatus energy, and neither is a total work budget
for building or resetting the apparatus.

## 3. Released result: an exact long-time instrument error floor

A nonzero limit in the upper bound(3) would not by itself prove that the
actual channel has an error floor. A direct construction does. Fix a nonzero
normalized phi in C_c-infinity supported strictly in x<0, with arbitrary
internal code/reference input and pointer initially |0>. Then G*phi=phi.
Set q=integral_(p<0)|phi_hat(p)|² dp. For this preparation the full recorded
channel converges in diamond norm as T->infinity to

    I_infinity=(1-q) I_parity + q I_blank,
    I_blank(rho)=|0><0| tensor rho.                  (9)

Consequently its normalized diamond distance from I_parity tends EXACTLY q.
For the upper bound use convexity and the distance bound1 between channels;
for the lower bound choose any odd-memory input, whose ideal pointer is1
but whose blank pointer is0. Thus this is a channel discrepancy, not only
a nonzero estimate for a wavepacket tail.

Proof of convergence. On Schwartz phi, X(T)/T=X/T+P/m. The Weyl relation
for its characteristic function implies convergence to the momentum law
P/m: the exp(isX/T) factor tends I strongly and its scalar commutator
phase tends1. Therefore the distribution functions converge at0, since
phi_hat has no atom at0. The moving threshold L/T has the same limit by
sandwiching between arbitrarily small positive/negative constants. Hence
the left mass tends q, right mass tends1-q, and the fixed transition-zone
mass tends0. Replace G by I on x<0 and W on x>=0. The isometry error is
at most twice the square root of the transition-zone mass, uniformly over
code/reference. Spatial trace of this step multiplier gives the exact
left/right mixture; pointer readout then gives(9). This proves diamond
convergence by the same dilation argument as(3).

Because phi is compact, its Fourier transform is entire and nonzero, so
both positive and negative half-line masses are strictly positive:0<q<1.
No fixed such preparation becomes a perfect instrument merely by waiting.
This does not prevent arbitrarily small q using changed, highly right-moving
preparations; momentum boosts shift its Fourier density and can send q to0.
It also does not exclude a different apparatus with reflectors or recapture.
The theorem concerns this open-line, passive covariant-kinetic instrument.

## 4. A contact costs coefficients, not necessarily input energy

For one nonnegative monotone flip profile theta over length ell, theta rises
by pi/2. On the occupied X=-1 channel, ||A(x)||=2theta'(x). Therefore

    ||A||_infinity >= pi/ell,
    integral ||A(x)||² dx >= pi²/ell.                (8)

The first is area versus maximum, the second Cauchy--Schwarz. A constant
profile attains the integral bound with nonsmooth edges; smooth compact
profiles approach but cannot attain a nonzero constant with zero endpoint
values. Coefficient A² and derivative cost diverge under shrinking support.
By contrast a state G phi has exactly <H>=<phi,H0 phi>, by conjugation.
That does NOT show it can be prepared at fixed work cost or within a bounded
control budget. K2105's point domain is a well-defined nonnegative mathematical
limit, not a free hardware idealization.

## 5. Released positive-energy domain stress test

K2105 supplies nonnegative energy, while
[K2106](k2106-neutral-unbounded-domains-2026-10-26.md) supplies the exact
neutral-autonomy classification and a nonnegative squared-boundary example
that fails it. These are logically distinct tests: a stable Hamiltonian can
mix the accessible charge sectors through its domain. Neither theorem
selects the physical observation algebra of equation9.16. Composition with
K2101's smeared massive-field capture still requires the SAME local registers,
state preparation, drift and reference dynamics; matching labels do not
supply an interface. Retain relativistic propagation and source-selected
observation as substantive open constructions.

## 6. Verification

Exact tests derive Gaussian normalization, its free variance and long-time
standardized mean, the variance optimum, profile area/integral cost, and
covariant-energy correction on an explicit Gaussian/profile pair. An exact
finite spatial/control model checks the isometry bound for every code input
via its singular values. All memory matrix units test the blank/parity mixture,
and an odd input attains its exact limiting error q. Faults change
spreading, free transport, profile area or omitted coefficient data. These
controls do not establish a universal optimum over preparations or a causal
relativistic apparatus; the analytic proofs above establish their stated scope.

The explicit A=2x Gaussian energy control has unbounded noncompact A; it
does not certify the compact-support tail estimate(7), which follows from
the stated norm inequality. Prior positive-energy localization results in
[K2060](k2060-positive-energy-localization-2026-10-25.md) remain available;
this nonrelativistic model supplies no new relativistic localization theorem.
