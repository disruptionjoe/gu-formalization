---
title: "K2079: Smooth detector pulses and explicit resource accounting"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: internally reviewed conditional mathematics; no GU verdict or novelty claim
scripts:
  - tests/channel-swings/k2079_smooth_detector_energy.py
  - tests/channel-swings/k2079_smooth_detector_energy_probe.py
---

# K2079: Smooth detector pulses and explicit resource accounting

**Internally reviewed, conditional mathematics (2026-10-26).** An independent
read-only operator/PDE agent reviewed the continuum domains, causal support,
energy bounds and finite-species scattering transfer. This is not external
expert or proof-assistant certification, a GU derivation or a novelty claim.

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
result: smooth prepared-state pulse energy and a supplied sourced-field resource bound
carrier: full complex Dirac1408 Hilbert carrier with a two-state memory LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive L2 norm and supplied Born rule ON=declared_complex_completion
real_structure: complex completion without source-real identification
grading: free energy signs; optional separately imported CAR parity
action_owner: repository-construction -- bounded internal control and explicitly supplied classical source
target: energy bounds and limits of Fock transfer MAP-TYPE=intertwiner
```

## 1. Object and question

Reuse [K2077](k2077-controlled-detector-response-2026-10-25.md):
H0=alpha.D+m beta on L2(R3,C4 tensor C352), m>0, domain H1,
P=1_(H0>0), Q=I-P, and B=A tensor sigma_y on the internal multiplicity
and an extra two-state memory. A is an orthogonal projector. B commutes with
all free Clifford matrices, ||B||<=1, and acts trivially on position. Let
0<=chi<=1 be smooth, equal to1 on the ball B_(L+T), and zero outside
B_(L+T+rho), with G=||grad chi||_infinity<=2/rho. Take g>=0 smooth,
supported in(0,T), with integral theta=pi/2. The new potential is

    V(t,x)=g(t) chi(x) B.

The positive Gaussian preparation of K2077, WITHOUT prechirp, has
E2=||H0 psi||=2m and norm tail tau=||1_(|x|>L)psi||<4/(mL), uniformly
over its internal qubit and untouched finite ancillary systems. These are inherited
analytic estimates, not newly sampled ones. The objective is resource accounting
for this same pulse, not K2073's different derivative generator.

SC-OP-04 ASSERTS candidate grammar; SC-OP-05 is UNCERTAIN about southeast
alternatives; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56
DISAVOWS the odd-action prerequisite. None selects this Hilbert/Born/control
completion. LT-SM8/GR6b, source register, ledger and canon remain unchanged.

## 2. Smooth pulse preserves the earlier measurement consumer

The homogeneous reference is Uref(t)=exp(-itH0) exp(-i B integral_0^t g).
It commutes with P. Both actual and reference propagators have speed1: the
bounded-potential Dyson series composes only free causal propagation and local
multiplication, with total free duration t. On initial data supported in B_L,
the reference trajectory stays in the chi=1 plateau throughout[0,T]. Duhamel
therefore proves equality of the two trajectories on this datum. Truncating the
initial vector is legitimate in L2, even if its hard cutoff is not H1. Thus

    ||(U-Uref)psi||<=2tau, at all times0<=t<=T.

K2077's exact internal A-perpendicular no-click property survives temporal
smoothing, and theta=pi/2 supplies the same ideal final rotation. Final record
TV error and negative-sector probability remain <=4tau^2. No instantaneous
kick approximation is used. The actual click effect remains supported on
both sides in the causal expansion of supp chi. Every outcome is retained.

## 3. Graph norm and tail-sensitive signed work

Smooth bounded V with bounded spatial derivatives preserves H1. This can be
proved directly by solving the H1 Duhamel equation: multiplication is bounded
on H1, its time norm is integrable, and free evolution preserves H1. Since B
commutes with the Clifford matrices,

    [H0,V(t)]=-i g(t) alpha.grad chi B,
    ||[H0,V(t)]||<=g(t)G.                              (1)

This is false for a general noncommuting internal matrix; the control probe
includes that contrary case. Put D=supp grad chi, outside the entire plateau.
The actual evolution of the truncated B_L initial datum has no support in D
at any time<=T. Unitarity of the remaining tail gives

    ||1_D U(t)psi||<=tau.                              (2)

The graph-commutator integral (first for smooth vectors, then by H1 closure)
therefore gives the stronger prepared-state estimate

    ||H0 U(t)psi|| <= E2+G tau integral_0^t g
                     <=2m+theta G tau = M.            (3)

For the signed free energy, the derivative is
- g(t)<Upsi,alpha.grad chi B Upsi>. Its absolute value is bounded by
g(t)G tau^2, since the Hermitian multiplier is supported in D on both sides.
Consequently, throughout the pulse,

    |<H0>_t-<H0>_0| <= theta G tau^2.                 (4)

No derivative of g is required for(3)--(4). In particular, this is not the
larger generic switching-work bound obtained by integrating ||partial_t V||.
The ideal reference preserves H0, so(4) measures the actual change against
both the initial and reference energy. For an entangled internal state, (2)
is a vector norm on the tensor product and the same proof applies; mixtures
with the stated uniform bounds follow by convexity.

The negative free-energy first moment is separately bounded by

    Eminus=<Upsi,|H0|Q Upsi> <=2tau M.                 (5)
    |<|H0|>_t-<|H0|>_0| <=theta G tau^2+4tau M.       (6)

Equation(5) uses sector norm<=2tau and Cauchy-Schwarz; (6) uses
|H0|=H0+2|H0|Q and initial P positivity. Small signed work does NOT imply
small absolute energy by itself. At L=2000/m, T=rho=1/m, tau<1/500,
using theta<11/7 gives

    M/m < 3511/1750,
    signed-work/m < 11/875000,
    Eminus/m < 3511/437500,
    absolute-mean change/m < 14055/875000.

These conservative sufficient bounds coexist with K2077's record/leakage
probability<1/62500 and its all-outcome tensor Bell result. They do not bound
a quantum apparatus Hamiltonian or identify a source physical vacuum.

## 4. A supplied classical field resource, with its assumptions exposed

There is no apparatus energy determined by V alone. Specify a real classical
field phi=g(t)chi(x)/lambda, lambda!=0, canonical Klein-Gordon energy and mass
mu_c>=0. Supply the external source

    J=(partial_t^2-Delta+mu_c^2)phi.

Then phi is an explicit smooth compact-spacetime solution of this sourced
classical equation, vanishing with its time derivative before and after the
pulse. Its lab-frame coupling is the declared density interaction lambda phi B.
This specifies a conditional controller; it neither derives a Lorentz-covariant
GU coupling nor solves backreaction or the work/energy cost of the source J.
The field energy is exactly

    Ephi(t)=[g'(t)^2 I0 + g(t)^2 (I1+mu_c^2 I0)]/(2lambda^2),
    I0=integral chi^2, I1=integral |grad chi|^2.         (7)

Take b(s)=exp[-1/(s(1-s))] on0<s<1 and zero otherwise, Z=integral_0^1 b,
g(t)=theta b(t/T)/(TZ). This is C-infinity at both endpoints. On[1/4,3/4],
b>=exp(-16/3), so Z>=exp(-16/3)/2. Also b<=exp(-4) and
|b'|<=16exp(-4): write y=1/[s(1-s)]>=4 and use y^2 exp(-y)<=16exp(-4).
The elementary exponential series bound exp(4/3)<4 gives

    ||g||_infinity <8theta/T,
    ||g'||_infinity <128theta/T^2.                    (8)

With R=L+T+rho, V_R=4pi R^3/3 and
V_shell=4pi[R^3-(L+T)^3]/3, I0<=V_R and I1<=4 V_shell/rho^2. Hence

    sup Ephi <= theta^2/(2lambda^2) *
       [16384 V_R/T^4 + 64(4 V_shell/rho^2+mu_c^2 V_R)/T^2]. (9)

The spatial/switching resources are finite and explicit; (9) is deliberately
loose, not an optimization. Taking lambda arbitrarily large makes this
particular supplied field energy small at fixed V, demonstrating why no
coupling-independent apparatus cost follows. Changing field normalization has
the same issue. Do not equate(4), (7), and an experimentally measured total
energy budget.

## 5. Smooth CAR endpoint transfer and a memory-type boundary

If one additionally treats the two memory labels as two fermionic species,
B has eigenvalues0,+1,-1 in a finite multiplicity space. One constant internal
unitary diagonalizes B and commutes with H0 and its sea. The field one-particle
evolution is then a finite direct sum of scalar smooth compact pulses
0,+g chi,-g chi. The established smooth scattering result in
[K1897](k1897-smooth-pulse-energy-2026-10-21.md), based on
[Langmann and Mickelsson](https://arxiv.org/abs/hep-th/9509034), applies blockwise
at speed1 after a unit/time rescaling: every finite weighted off-diagonal
scattering moment is finite after the pulse. Finite direct sums preserve that
property. This is a reuse of its analytic theorem with checked hypotheses,
not a new proof of regularization or a numerical field-energy bound.

**Species are not a shared two-state memory.** Fock(H tensor C2) is naturally
a fermionic two-species construction, not Fock(H) tensor C2. In a finite
n-mode regulator their dimensions are2^(2n) and2^(n+1), respectively; n=1
is an accidental equality, n=2 already gives16 versus8. In the continuum,
the particle-number grading and observable algebras also differ. Thus this
endpoint implementability does not itself lift K2077's shared-ancilla
measurement. K1896's instantaneous phase obstruction is avoided by temporal
smoothing, but not by pretending a species index is an apparatus.

## Checks and review boundary

The producer emits exact rational resource bounds and pins inherited inputs.
The separate probe checks the commutator identity on actual Clifford matrices,
the noncommuting-matrix countercontrol, exact exponential-series bounds,
tail/signed/absolute energy arithmetic and
species dimensions. Finite numerical controls corroborate only their stated
instances. The support, domain and field-resource arguments above are the
load-bearing continuum reasoning. Baseline-first mutations change mathematical
coefficients or constructions, never validation predicates. Independent internal
operator/PDE review accepted the conditional argument after correcting the
coverage description: no pulse-area reference-rotation test was performed.
The bound on B is stated as <=1, which suffices without a nonzero-projector
assumption. The original provisional checkpoint is superseded by this reviewed
version; source, physics-ledger and canon verdicts do not change. A shared
detector-field implementation and total source-work account remain substantive
next inputs.
