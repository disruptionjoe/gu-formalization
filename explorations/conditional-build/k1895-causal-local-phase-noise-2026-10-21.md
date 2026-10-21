---
title: "K1895: Causal continuum phase noise and observable coherence"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional target-local CAR Markov dynamics with supplied classical noise; no local source interaction, vacuum regularity or native GU bath
scripts:
  - tests/channel-swings/k1895_causal_local_phase_noise.py
  - tests/channel-swings/k1895_causal_local_phase_noise_probe.py
---

# K1895: Causal continuum phase noise and observable coherence

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
result: exact support-causal continuum completely positive semigroup with nontrivial even coherence loss
carrier: K1892 target complex L2(R3,C4) and its full CAR algebra LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and classical Poisson expectation ON=target_CAR
real_structure: complex star algebra and unitary multiplication by a scalar phase
grading: fermionic parity preserved; even is not synonymous with charge neutral or locally gauge invariant
action_owner: repository-construction -- imported symmetric phase-kick law and K1892 free target generator
target: target-local even observables and nonselective interventions MAP-TYPE=restriction
```

## 1. A concrete repair of the spatial-locality gap

[K1894](k1894-semicausal-quantum-dynamics-2026-10-21.md) extends a quantum
cascade to continuum CAR but its finite-rank hopping jump permits an immediate
remote signal. Here multiplication by a spatial phase supplies a different,
exactly support-preserving jump. The resulting **continuum C-star semigroup**
retains K1892's target speed c=1/24 and changes neutral even coherences.
[K1896](k1896-local-phase-vacuum-boundary-2026-10-21.md) tests the independent
vacuum representation requirement and finds a three-dimensional obstruction.
Neither positive algebraic states nor the present causal theorem asserts a
finite-energy physical model.

K981/K987 already own finite-dimensional compound-Poisson dephasing. Their
characteristic-function formula is reused, not claimed as new. The new question
is continuum local-net preservation under the actual Dirac free group, its
source lift, and the independent vacuum test. Local CAR automorphisms from
multiplication operators are standard; see [Grundling and Neeb](https://arxiv.org/abs/1001.1010).
No novelty claim is made. We derive the support and channel statements below.

SC-OP-04 ASSERTS candidate operator grammar; SC-MAS-01/SC-CHI-02 ASSERT a
stylized curvature-mass toy; SC-OP-05 and SC-META-53 remain UNCERTAIN.
The noise, probability law, accessible algebra and vacuum are additional
choices. Full20 injection and separate K/C pairing remain unconstructed;
LT-SM8/AC-F1, source-register and physics-ledger/canon verdicts do not change.
This is conditional reverse-scaffold mathematics, with no prediction credit.

## 2. Generator and existence on the full continuum algebra

Let H=L2(R3,C4), A=CAR(H), and A(O)=CAR(L2(O,C4)). Use K1892's strongly
continuous free automorphism group alpha_t induced by its constant-mass
Dirac group. It obeys alpha_t(A(O)) subset A(O_{c|t|}), where O_r is the
r-neighborhood. Annihilators are antilinear in their smearing.

For a bounded measurable real theta, put u(x)=exp(i theta(x)), U=M_u.
The unitary U induces beta_u(a(f))=a(Uf). Both beta_u and beta_u^{-1}
preserve each A(O), exactly. For gamma>=0 set

```
K = gamma/2 (beta_u + beta_u^{-1} - 2 Id),  ||K||<=2 gamma,
G = delta_0 + K,  Dom(G)=Dom(delta_0).                     (1)
```

The bounded perturbation theorem gives a strongly continuous semigroup T_t.
More explicitly, on [0,t] sample a Poisson count of mean gamma t, ordered
uniform event times and independent signs +/- with probability1/2. Between
events apply alpha for the elapsed interval; at an event apply beta_u^{+/-1}.
The expectation of this chronological automorphism composition solves the
bounded-perturbation integral equation. The n-event expansion converges in
operator norm after extracting the free isometry, dominated by the Poisson
weights. Thus T_t is unital, completely positive and parity preserving.
It is a genuine dynamics on the infinite CAR algebra; no invariant finite
Fourier truncation is assumed.

Each sample path enlarges support only during free intervals. The sum of
those intervals is t; phase multiplication never enlarges support. Therefore

```
T_t(A(O)) subset A(O_{ct}).                               (2)
```

Norm limits and Bochner integrals remain in this norm-closed local algebra.
For even A in A(O), any even nonselective intervention supported outside
O_{ct} commutes with T_t(A); its dual leaves every expectation of T_t(A)
unchanged. For Kraus operators W_j, use sum W_j*W_j=I and
sum W_j* T_t(A) W_j=T_t(A). This includes arbitrary initial correlations.
Selective conditioning is not a signal. The Poisson clock is exogenous and
state independent: allowing remote interventions to change the clock law
would be a different, potentially signalling model.

Equation(2) proves operational causal support. T_t is not an automorphism,
so one must NOT compute products or unequal-time CAR by replacing every
field with its mean T_t(a). Indeed its multiplicative deficit is

```
K(X*X)-K(X*)X-X*K(X)
 = gamma/2 sum_{sigma=+,-} (beta_u^sigma(X)-X)*
                              (beta_u^sigma(X)-X).       (3)
```

This is generally positive and nonzero. The free derivation cancels out of
(3). A mean field equation alone would lose precisely this noise term.

## 3. Even-coherence consumer and common-noise correlations

For compact normalized disjoint f,g lying in phase plateaux theta_f,theta_g,
X=a(f)*a(g) is neutral and even. The noise part satisfies

```
beta_u(X)=exp(i(theta_f-theta_g))X,
exp(tK)(X)=exp[-gamma t(1-cos(theta_f-theta_g))]X.         (4)
```

Local mode numbers on plateaux are fixed. Pair annihilation is even but has
phase sum rather than phase difference; it need not be fixed by a constant
phase. Thus neither number preservation nor fermionic parity means unchanged
quantum dynamics. Equation(4) is for the noise semigroup, or for a full
observable known to remain a common eigenoperator. It is not asserted after
arbitrary free wavepacket transport through a nonconstant phase.

Two disjoint dual-rail regions have neutral coherences A,B with the same
phase multiplier -i. A shared clock damps A and B individually at gamma,
while AB* is fixed by the noise. Independent clocks instead damp AB* at
2 gamma. This is correlated classical noise without remote control or
signalling. Each shared-clock realization acts as a product unitary on the
two encoded factors, so averaging cannot entangle an initially separable
encoded state. This contrasts with the interacting cascade of K1894.
It can preserve or modify existing correlations; no entanglement generation
is inferred from nonfactorization of the channel.

For the four-periodic finite control, q=exp(-gamma t), the probabilities of
the net signed jump modulo4 are

```
w0=(1+q)^2/4, w1=w3=(1-q^2)/4, w2=(1-q)^2/4.            (5)
```

They are nonnegative, sum to1 and compose by cyclic convolution. The finite
CAR probe checks every matrix unit and even remote controls. These are exact
algebra controls on (1), not a numerical proof of the continuum support claim.

## 4. Full transport consumer in a massless one-dimensional reduction

For the massless one-dimensional target, diagonalize the velocity matrix,
with v_i=+c or -c. The two-point density kernel in component(i,j) obeys the
closed Schrödinger equation

```
partial_t n_ij = -(v_i partial_x+v_j partial_y)n_ij
                + gamma[cos(theta(x)-theta(y))-1]n_ij.
```

The exact characteristic solution is

```
n_ij(t,x,y)=n_ij(0,x-v_i t,y-v_j t)
 * exp{gamma integral_0^t [cos(theta(x-v_i r)-theta(y-v_j r))-1] dr}.  (6)
```

It follows by differentiating along characteristics. It solves the covariance
law for every state; it does not assume the averaged state is quasifree.
In fact mixtures of quasifree states are generally not quasifree. Same-component
number density (x=y) is simply transported. Relative coherences sample the
phase along two actual trajectories. Higher correlations require their own
signed phase sums, not Wick factorization of the mean two-point function.
A constant gradient theta(x)=kappa x gives, for equal velocities,
exp[-gamma t(1-cos(kappa(x-y)))], a direct controlled example of (6).

## 5. Source lift and exact inference boundary

K1892 gives H_source=j H_target direct_sum H_hidden with reducing free
sectors. The source unitary U_s=j M_u j* direct_sum I_hidden induces a CAR
automorphism restricting to beta_u on the observed algebra and fixing the
hidden algebra. Equation(1) therefore lifts to the source CAR with the same
observed autonomous noisy law. The construction is explicit, but j is
nonlocal in source spatial coordinates. No source-local implementation or
microscopic environment has been built. Source/target mixed locality is not
implied by (2).

Also, a local phase may be regarded as a gauge redundancy only after an actual
gauge-invariant physical algebra has been supplied. We use the declared even
CAR algebra, which includes the neutral hopping X. If a later gauge constraint
removes X, its damping is not a physical observable in that different model.
Do not label these supplied kicks a derived gauge interaction.

## Verification and adversarial review

The continuum proof is bounded perturbation plus pathwise support, not a
finite sample. The producer checks exact CAR, phase signs, fixed number,
even coherence, correlated versus independent clocks and cyclic master law.
The separate probe constructs annihilators by occupation bits, checks every
matrix-unit multiplier and cyclic convolution, and first passes its baseline
before corrupting unitarity, loss term, hopping location, report and input pin.

Hostile review checked: antilinear smearing signs; lack of multiplicativity;
clock state independence; even versus neutral algebra; averaging versus Wick
factorization; nonlocal j; gauge redundancy versus physical noise; and noise-only
versus full transport formulas. The first-order characteristic result does
not fix the massive three-dimensional covariance equation. Vacuum regularity
is delegated mathematically to the independent K1896 question, not assumed.
No external expert, proof assistant, native GU, physical bath or novelty claim.
