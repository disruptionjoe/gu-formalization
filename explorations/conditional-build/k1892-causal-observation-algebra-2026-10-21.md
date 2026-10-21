---
title: "K1892: Causal observed CAR algebra despite nonlocal reconstruction"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional free whole-space compressed system plus an explicitly imported CAR quantization; no native GU, physical locality identification or unique vacuum
scripts:
  - tests/channel-swings/k1892_causal_observation_algebra.py
  - tests/channel-swings/k1892_causal_observation_algebra_probe.py
---

# K1892: Causal observed CAR algebra despite nonlocal reconstruction

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
result: conditional causal observed field algebra, state extensions and hidden-speed leakage countercontrol
carrier: complexified L2 R16 source and L2 R4 target on R3 LAYER=toy CHIRALITY=N/A
pairing: H-positive source energy and Euclidean target pairing ON=whole_space_L2_and_test_functions
real_structure: complexification of fixed real coefficient equations; CAR statistics separately assumed
grading: fermionic even/odd operator parity, not source graded-IG or particle chirality
action_owner: repository-construction -- constant K1840 conservative equations plus imported CAR algebra
target: observed local algebra and its nonlocal source embedding MAP-TYPE=restriction
```

## 1. The decision and its limits

[K1881](k1881-dynamical-minimum-energy-observation-lift-2026-10-21.md)
constructs a normalized coisometry V from the conditional source system to a
Dirac target, and correctly says its source reconstruction is nonlocal.
That fact alone neither establishes nor refutes microcausality of the
**observed algebra**. The deciding object is the unequal-time anticommutator.
Here it equals the target Dirac propagator and has the slower target cone.
The unnormalized differential observation has a local differential covariance
and the same cone. A concrete leak into an invisible fast source channel
destroys that conclusion, even for arbitrarily small leakage.

We assume the complex CAR algebra of the positive source Hilbert space.
This is an added free-field quantization, not a spin-statistics derivation,
a source-selected physical state, an interacting positive quotient or a
selection of what experimental interventions count as local.
SC-OP-04 ASSERTS candidate grammar and SC-MAS-01/SC-CHI-02 ASSERT a stylized
mass toy; SC-OP-05 and SC-META-53 remain UNCERTAIN. The source's full20
placement/injection/K-C reality/pairing maps remain absent. RA-F1, AC-F1 and
LT-SM8 remain NEEDS; no source, ledger or canon verdict changes.

## 2. Exact transfer and a sharp causal cone

Take constant real R on all of R3 and the first K1840 repair in each of the
four coordinate types. Reuse K1881's established closed operators:

```
P_s=sum A_i partial_i+RC, P_t=sum D_i partial_i/24+RB,
O=sum T_i partial_i+RS, alpha=138/25,
K0=O Odagger=alpha(-Delta+576R²)I,
V=K0^(-1/2) O, j=Vdagger,
U_s(t)=exp(-tP_s), U_t(t)=exp(-tP_t).
```

The zero Fourier point at R=0 has measure zero on R3; V and j extend as
bounded coisometry/isometry. This statement differs from the unbounded
massless raw inverse. K1881 proves

```
V Vdagger=I, U_s(t)j=j U_t(t),
V U_s(t)Vdagger=U_t(t),
O U_s(t)Odagger=K0 U_t(t).                               (1)
```

The last equality is understood on smooth tests, or distributionally.
The new continuum causal argument is elementary: D(n)=sum n_i D_i is
symmetric and D(n)²=|n|²I. Thus the target energy density obeys
`partial_t |y|²+div(y* D_i y/24)=0`, and the outward flux is bounded by
`|y|²/24`. Integrating outside an expanding ball, first for smooth compact
initial data and then by approximation, proves propagation speed at most1/24.
The mass B is skew and contributes no energy source. The massless normal
characteristic solutions achieve that speed. Equivalently,
`P_t²=(Delta-576R²)/576`; its retarded Klein--Gordon representation has the
same support. No sampling of a propagator establishes this support theorem.
The much faster source modes are absent from (1) by exact intertwining.

For a compact smooth forcing J in the source equation, zero initial data give

```
y(t)=integral_0^t U_t(t-s) OJ(s) ds.                     (2)
```

O is local differential, so OJ has no larger spacetime support than J.
The observed retarded response therefore stays in the slow target causal
future, even when the source solution itself has faster components. This is
a statement about the stated linear forcing and fixed observation, not all
physical source interventions or arbitrary interactions.

## 3. The observed field algebra

Use the standard complex Hilbert convention f* g and annihilators a(f)
antilinear in f, with `{a(f),a(g)*}=<f,g>I` and `{a(f),a(g)}=0.
Define `b(f)=a_s(j f)` and evolve the smearing by U_s(t).
Because j is isometric, the b's obey exact target CAR; the universal CAR
construction embeds this algebra faithfully into the source algebra.
For times t,s, (1) gives

```
{b_t(f),b_s(g)*}=<f,U_t(s-t)g>I.                         (3)
```

If compact supports of f and g have distance greater than |s-t|/24, this
vanishes. Odd fields anticommute at this separation; **even observables
commute**, first for finite even polynomials and then for their norm closures.
This is a local algebra in the target spacetime coordinates and cone.
For an even unitary A localized in one target region and a spacelike target
observable B, `A* B A=B`; every state therefore has the same remote B
expectation after this nonselective unitary intervention. More general local
nonselective channels with even Kraus operators and sum A_i* A_i=I give the
same conclusion. Selective conditioning can change conditional correlations;
it is not a remote signal. No particular Bell state or empirical confirmation
is derived from this algebraic fact.

The standard framework is [Bär and Ginoux, *CCR- versus CAR-Quantization on
Curved Spacetimes*, Proposition2.3(iv)](https://nicolas-ginoux.perso.math.cnrs.fr/procquant.pdf):
an isometric Hilbert embedding induces an injective CAR morphism. Their
framework is background, not a substitute for the actual transfer (1),
energy-flux proof and scope distinctions here. The paper also distinguishes
algebraic quantization from selecting states. No novelty claim is made.

For the raw local field c(f)=a_s(Odagger f), smooth compact f is sufficient.
Its unequal-time anticommutator is

```
{c_t(f),c_s(g)*}=<f,K0 U_t(s-t)g>I.                      (4)
```

At equal time this is the local differential distribution K0 delta, not
canonical delta normalization. Applying a differential operator cannot expand
the causal support, so the raw even algebra is causal too. Since Odagger is
differential, c(f) is source-local at a fixed time. Normalizing it changes that
local embedding, even though it preserves target CAR and target causality.

## 4. Nonlocal embedding and what the causal theorem does not say

j has the Fourier symbol `Odagger(xi)/sqrt(alpha(|xi|²+576R²))`.
It is bounded but nonconstant in xi (checked on the actual four-type matrices).
If its translation-invariant distribution kernel were supported at the origin,
it would be a finite linear combination of delta derivatives, hence its
symbol a polynomial. A bounded polynomial symbol is constant. Thus j is
not support-preserving; some target-compact test functions have nonlocal
source images. The R=0 symbol is likewise nonconstant in direction.

Therefore the target local algebra is not automatically a subnet of the
source's spatially local algebra under j. Mixed target/source anticommutators
are `<jf,h>_H` and need not vanish for target/source disjoint coordinate
supports. Equation (3) concerns target-target locality only. An experimental
identification of local interventions must choose and justify the accessible
algebra; a formal coisometry does not do that. This explicitly blocks turning
(3) into a claim that every source-local operation respects the slower cone.

Likewise the slow cone is a model coefficient, not a measured speed of light.
The normal source speeds include +/-1 and +/-1/24; no physical units or
native spacetime identification are supplied.

## 5. Follow-through: state extension without vacuum selection

Let Pi=j jdagger. Intertwining makes its range and ker V reducing for source
evolution. For any target gauge-invariant quasifree covariance 0<=Q_y<=I and
any hidden-sector covariance 0<=Q_h<=I, define on that orthogonal sum

```
Q_s=j Q_y jdagger direct_sum Q_h.
```

It is a positive contraction and compresses to Q_y. The usual quasifree CAR
state construction therefore extends every such target state. If each block
commutes with its own evolution, the extension is stationary. The hidden
block is arbitrary: the observation selects neither a unique vacuum nor a
unique global source state. Different positive target thermal covariances or
hidden occupations are allowed. No interacting state, Hadamard condition,
physical ground-state positivity or native GU quantization follows.
The probe checks an actual covariance with target occupation1/5 and hidden
occupation7/10, including its minimal polynomial and compressed covariance.

## 6. Follow-through: exact hidden-speed leakage countercontrol

In the massless normal subsystem select an actual +1 source eigenvector r
from ker T1, and a nonzero target vector u. Let

```
M=u r^T H, h=r^T H r>0, O_epsilon=T1 partial_x+epsilon M.
```

The pinned matrices verify `M A1=M`, `T1 H^-1 M^T=0`, and
`M H^-1 M^T=h u u^T`. The source +1 eigenspace is H-orthogonal to the
visible slow sector. Consequently the exact covariance is

```
O_epsilon U_s(t) O_epsilon_dagger
  = alpha(-partial_x²) U_t(t)
    +epsilon² h u u^T tau_t,                             (5)
```

where tau_t translates at speed1. For every epsilon!=0, compact tests
centered at separation |t| with sufficiently small supports lie outside the
slow cone yet detect the second term. This is an explicit loss of the slow
causal support, not numerical evidence of leakage. The observation perturbation
fails the exact intertwiner and defines a changed conditional model; it does
not contradict (1)--(4). The leakage amplitude is quadratic but its support
moves discontinuously to the larger cone. Exact causal shielding requires
structural decoupling, not merely small coefficient error.

## 7. Follow-through: the simplest local potential already tests closure

Keep the SAME observation O and add an energy-conserving source scalar
potential i lambda(t,x)I, with real smooth lambda. The matching principal
coefficient on the target is i lambda I. Direct product differentiation gives

```
O (P_s+i lambda)-(P_t+i lambda) O
   = i sum T_i partial_i lambda.                         (6)
```

The actual matrices obey `T(n)H^-1 T(n)^T=alpha|n|²I` for real n.
Thus the defect vanishes exactly when the spatial gradient of lambda vanishes.
An arbitrary time-dependent spatial constant is allowed; a genuinely local
scalar potential fails closure of this FIXED observed dynamics. No all-coupling
exclusion follows: changing O and introducing a covariant connection defines
a different, potentially compatible model. Nor does failure of (6) alone
prove a superluminal signal. It identifies the exact missing term before that
claim can be tested. This cheap calculation consumes the intervention question
without assuming that global phase covariance proves local coupling stability.

## 8. A tested local repair and a classical nonlinear consumer

Arbitrary leakage is not an all-potential obstruction. The exact common
nullspace N=intersection ker(T_i) has dimension4 in every coordinate type,
and S N=0. If Z is its serialized16x4 basis, every

```
W(x,t)=Z J(x,t) Z^T H,    J^T=-J
```

is H-skew and annihilated on the left by every T_i and S. Therefore
`O(W psi)=0` identically, including derivatives of variable coefficients.
This is a six-dimensional pointwise algebra of real skew maps supported on N;
the induced inner product on N identifies it with so(4). A nonzero rank2
example is serialized and checked independently. Such arbitrary smooth local
potentials preserve the original observed equation, with **no target change**.
This is an explicit admissible repair under the same O and energy pairing.
It need not commute with the source free generator, nor need N itself be a
reducing subspace of each source principal matrix; neither is required by
`O W=0` as a differential identity.

There is also an exact CLASSICAL nonlinear consumer. Let P_N be the
H-orthogonal projection onto N, fix one such W0, and put

```
F(psi)= W0 psi / (1+||P_N psi||_H²).
```

W0 annihilates N-perp, so this is a smooth globally Lipschitz function of the
finite-dimensional vector P_N psi, with F(0)=0. Its pointwise Nemytskii map
is globally Lipschitz on source L2_H. The unitary source group and Duhamel
Picard iteration therefore give a global mild L2 solution to
`partial_t psi+P_s psi+F(psi)=0`. The real part of `<psi,F(psi)>_H` vanishes,
so the usual approximation argument preserves source energy. Pointwise F
lies in N, hence `O F=0` as a distribution, even for merely L2 data.
Using the closed intertwiner in Duhamel gives, for initial data in Dom O,

```
O psi(t)=U_t(t) O psi(0).
```

This exact hidden self-coupling leaves the observed classical response
unchanged. It is not a quantization of the nonlinear source flow: a nonlinear
map on one-particle states does not automatically define a CAR automorphism.
No interacting quantum positivity or source-owned nonlinear action is claimed.
The contrast with (5) is now constructive: both an arbitrarily small harmful
leak and an arbitrary local protected family are exhibited on the actual carrier.

## Verification and hostile review

Producer:46 exact matrix groups,4 input pins. Separate probe:89 mathematical
resolvent/CAR/covariance checks,1 reported-speed check and4 pins. It rejects
three mathematical faults (using the minimum-energy inverse as a normalized
embedding, giving the fast mode slow speed, and forgetting the fermionic
tensor sign) plus1 serialized speed fault. Every mutation follows a clean
baseline and fails an explicit assertion. Initial comparisons used structural rather than reduced rational equality.
A broad symbolic simplifier then stalled on the same rational arithmetic and
was interrupted. Exact Gaussian-rational matrix inversion and entry reduction
resolved the issue without changing any coefficient or check. No failed baseline was credited as mutation
power. Finite CAR matrices validate the algebraic control, not continuum
causality; the energy argument proves the latter.

Hostile review checks CAR is an imported premise, distinguishes anticommutation
from even-observable commutation, target locality from source locality,
nonselective interventions from postselection, graph/domain identities from
symbols, and states from physical vacua. The leakage control defeats the
strongest erroneous robustness inference. Blocking findings in this stated
scope: none. No independent-agent, external-expert or proof-assistant review
or novelty is claimed. Interacting stability, actual source-native adapters
and experimentally selected local observable algebras remain substantive work.
