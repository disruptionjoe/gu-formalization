---
title: "K1894: One-way quantum dynamics and the price of exact shielding"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite GKLS classification and bounded nonlocal continuum extension; no local spacetime interaction, derived bath or native GU quantization
scripts:
  - tests/channel-swings/k1894_semicausal_quantum_dynamics.py
  - tests/channel-swings/k1894_semicausal_quantum_dynamics_probe.py
---

# K1894: One-way quantum dynamics and the price of exact shielding

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
result: one-way completely positive quantum coupling with entanglement, exact unitary-marginal rigidity and a quantitative disturbance bound
carrier: finite complex quantum factors with four-mode dual-rail embedding and K1892 continuum CAR splitting LAYER=toy CHIRALITY=N/A
pairing: standard positive trace and Hilbert pairing ON=finite_factors_and_continuum_CAR_algebra
real_structure: complex star algebra with Hermitian Hamiltonian and completely positive Lindblad generator
grading: total fermionic parity preserved by even dual-rail bilinears; logical excitation distinct from particle number
action_owner: repository-construction -- finite and bounded continuum GKLS cascade; no source-owned bath
target: all-state autonomous visible marginal, forward influence and information-disturbance boundary MAP-TYPE=restriction
```

## Decision and evidence boundary

[K1893](k1893-quantum-hamiltonian-shielding-2026-10-21.md) classifies exact
Hamiltonian shielding. Does irreversible dynamics permit a meaningful one-way
coupling? Yes, if the autonomous visible law is allowed to be noisy. If its
entire quantum algebra must retain a purely unitary law, complete positivity
forces decoupling in the finite factor setting. Restricting the protected
algebra to a classical center instead allows informative readout with an exact
coherence cost.

This begins with an explicitly supplied finite quantum model, not a quantization
of the classical nonlinear source flow or an invariant finite Fourier truncation
of K1892. Section6 supplies a bounded nonlocal continuum extension and a causal
countercontrol. The local continuum native bath/domain problem remains open. SC-OP-04 ASSERTS
candidate grammar; SC-MAS-01/SC-CHI-02 ASSERT a stylized mass toy; SC-OP-05 and
SC-META-53 remain UNCERTAIN. LT-SM8/AC-F1, all source/physics-ledger/canon verdicts,
and the full20 injection/K-C pairing/observable debts are unchanged.

K115 already constructs classical diffusion-refresh feed-forward. The result
here concerns a noncommutative quantum factor, positivity, entanglement and a
parity-correct encoding, not a relabeling of that classical detector.
Invariant subalgebras and semicausal generators have established general theory:
[Hasenoehrl and Caro, 2109.03847](https://arxiv.org/abs/2109.03847) and
[2202.06812](https://arxiv.org/abs/2202.06812). These are prior-art context;
the elementary identities below are derived directly. No novelty is claimed.

## 1. Unitary visible dynamics is a stringent constraint

Use the finite Heisenberg GKLS convention

```
G(X)=i[H,X]+sum_k (Lk^* X Lk - {Lk^* Lk,X}/2).           (1)
```

Suppose G(X)=i[Hv tensor I,X] for EVERY X in B(Fv) tensor I.
For any such X, the exact dissipation identity is

```
Gamma(X) = G(X^*X)-G(X^*)X-X^*G(X)
         = sum_k [Lk,X]^* [Lk,X].                       (2)
```

The prescribed target derivation satisfies Leibniz, so the left side vanishes.
Every right summand is positive; hence [Lk,X]=0 for every k,X. Thus
`Lk=I tensor Mk`. All their dissipators vanish on the visible algebra, and
`H=Hv tensor I+I tensor Kh` by the matrix-unit argument. The total generator is
the sum of the independent visible Hamiltonian and hidden GKLS generators.
Conversely this split gives the prescribed target law.

Therefore an exactly unitary autonomous FULL quantum factor cannot supply a
new informative hidden record in this model. Initially correlated states can
already contain information; they do not evade this generator theorem or imply
new communication. The hypothesis is equality for all observables/states, not
agreement of one stationary density matrix. The theorem concerns finite GKLS
and a full factor; it is not asserted for arbitrary unbounded infinite-volume
or non-Markovian dynamics. For an even algebra with center, commutants can carry
sector-controlled coefficients as K1893 explains.

## 2. Quantitative consumer: near-unitarity bounds dissipative coupling

Let E(X)=G(X)-i[Hv tensor I,X] on the visible factor and assume the induced
operator norm bound `||E(X)|| <= epsilon ||X||` for ALL visible X. For a visible
unitary U, E(I)=0 and (2) gives

```
0 <= sum_k [Lk,U]^*[Lk,U]
   = -E(U^*)U-U^*E(U),
||sum_k [Lk,U]^*[Lk,U]|| <= 2 epsilon.                  (3)
```

For every unit vector psi,
`sum_k ||[Lk,U]psi||^2 <= 2 epsilon`.
This bounds genuine dissipative noncommutation, not an arbitrary norm of a
Hamiltonian interaction. The error assumption is uniform on the factor, not
one measured coherence or one state. Equation (3) is a necessary condition,
not a reconstruction or approximate decoupling theorem for total dynamics.
The center-reading example below saturates this coefficient for a Pauli U.

## 3. Exact one-way cascade with a noisy visible marginal

Let A act on a visible factor and B on a hidden factor, so they commute with
each other and their adjoints. Set

```
L=A+B, Hc=(B^* A-A^* B)/(2i).                            (4)
```

For visible X the cross terms of the dissipator in (1) are
`(B^*[X,A]+[A^*,X]B)/2`. The Hamiltonian contributes their negative.
Consequently

```
G(X tensor I) = D_A(X) tensor I.                        (5)
```

For a hidden Y the surviving cross term is instead

```
G(I tensor Y)=I tensor D_B(Y)
             + A^*[Y,B]+[B^*,Y]A.                     (6)
```

Thus hidden-to-visible influence is absent but visible-to-hidden influence
can be nonzero. The finite semigroup is completely positive and trace
preserving by (1). Equation (5), exponentiated in finite-dimensional linear
space, is equivalently

```
Tr_h exp(t G_*)(rho) = exp(t D_A*)(Tr_h rho)              (7)
```

for EVERY joint density matrix, including correlated/entangled inputs.
It is not a product-preparation approximation. Removing Hc or reversing its
sign breaks the cancellation. This is a constructed irreversible repair,
not a violation of section1: D_A is generally dissipative, not a derivation.

## 4. A solved entangling example and actual fermionic realization

Take A=sigma_- tensor I and B=I tensor sigma_-, with rates set to1 in arbitrary
time units. From |10><10|, the exact Schrödinger solution is

```
rho(t)=exp(-t)(|10>-t|01>)(<10|-t<01|)
       + [1-(1+t^2)exp(-t)] |00><00|, t>=0.             (8)
```

Substitution into the master equation verifies it. The second coefficient
starts at0 and has derivative `(t-1)^2 exp(-t)>=0`; thus (8) is positive
and normalized. The visible excitation is exp(-t), independent of the hidden
preparation by (7). The hidden excitation generated by this input is
`t^2 exp(-t)`, with maximum4 exp(-2) at t=2. Its partial transpose has the
{00,11} principal minor `-t^2 exp(-2t)<0` for every t>0, so the joint state is
entangled at every finite positive time. This is quantum feed-forward, not
only a copied classical label. It supplies no superluminal or spatial claim:
the two factors and Markovian connection have no assigned spacetime separation.

Bare odd annihilators on distinct fermionic subsystems anticommute and cannot
be substituted for the commuting A,B in (4). Use two modes per logical qubit,
with logical |0>=|10>, |1>=|01>, and

```
A=a1^* a2, B=a3^* a4.                                  (9)
```

Both are even, act on disjoint mode pairs and commute. The one-particle sector
of each pair reduces A,A^*,B,B^*,L,Hc. In visible-first Jordan-Wigner order the
four encoded basis indices are10,9,6,5. The exact isometry U satisfies
`L_f U=U L`, `L_f^* U=U L^*`, `H_f U=U Hc`.
Thus (8) is a genuine parity-preserving finite CAR realization. Encoding,
noise and directional Hamiltonian are supplied data, not source-selected GU
interactions or spacetime locality.

## 5. Informative nondemolition center and coherence price

Set A=Z_v, B=sigma_- on a hidden logical qubit, with (4). Then

```
G(Z_v)=0, G(X_v)=-2X_v, G(Y_v)=-2Y_v.                  (10)
```

Starting the hidden qubit in |0>, the initial derivative of its X expectation
is -2 for visible Z=+1 and +2 for Z=-1. The detector immediately acquires
information about Z while leaving the entire visible diagonal algebra fixed.
This does not preserve the full factor: the off-diagonal coherence decays as
exp(-2t). The target channel is the exact dephasing channel with probabilities
`(1+exp(-2t))/2` for I and `(1-exp(-2t))/2` for Z. Its generator error from the
zero derivation is norm epsilon=2; (2) for X_v equals4I, saturating (3).

A standard pure-dephasing, supplied GKLS readout can therefore retain one
classical observable and transmit its information, but cannot be cited as
unchanged quantum evolution. No microscopic bath, fluctuation-dissipation law,
physical energy cost or uniquely selected probabilities have been derived.

## 6. Continuum follow-through: bounded extension, explicit locality failure

The one-way construction does extend to the actual infinite K1892 CAR algebra
at a precise, limited level. Choose bounded even A in the observed CAR subalgebra
and bounded even B in CAR(H_h), using the reducing split from K1893. They commute
with the opposite full CAR subalgebra. Set L=A+B and Hc as in (4). This gives a
bounded GKLS generator K on the full C-star algebra. Compose it with the free
strongly continuous CAR group: the bounded perturbation theorem gives a strongly
continuous semigroup with generator delta_0+K on Dom(delta_0). The Lie-Trotter
products of the free automorphism and exp(tK) converge strongly on algebra
elements, uniformly on compact time intervals. Each product is completely
positive and unital, hence so is the limit. This is an algebraic positive-state
construction; no Fock vacuum, energy lower bound or microscopic bath is selected.

The observed algebra is invariant under BOTH factors of every Trotter product.
On it the generator is exactly delta_target+D_A. Thus the all-state autonomous
marginal survives in the continuum without assuming an invariant finite-mode
subspace of the free dynamics. The bounded source operators are genuinely
interacting and may be nonlocal under the normalized j embedding. This extension
does not claim that (8)'s finite time solution holds for free-evolving wavepackets.

A concrete causal test shows why this is not yet a local continuum quantum model.
Take mutually orthonormal smooth compact target modes f,g,h, with f in region F
and g,h in a disjoint region G. Choose the even observed jump
`A=b(f)^* b(g)`. For n_f=b(f)^*b(f), the dissipative contribution is exactly

```
D_A(n_f) = n_g (1-n_f).                                 (11)
```

Start in vacuum or in the two-particle state b(g)^*b(h)^*|0>. These states have
the same even total parity and are related by an even pair-creation unitary
localized in G. Their n_f expectations and free initial derivatives agree,
because f is disjoint from the remote modes and the target free generator is
local differential. Equation (11) makes their n_f derivatives differ by1.
For sufficiently small positive t, their expectations differ by t+o(t), while
F and G remain outside each other's target speed1/24 cone. Hidden B does not
remove this violation, because the visible law is autonomous.

This is a valid even-observable, even-intervention countercontrol. It excludes
THIS nonlocal finite-rank jump as an exact target-causal interaction, not all
open quantum dynamics and not GU. A pointlike or properly causal local field
interaction requires its own ultraviolet/domain construction; replacing it by
smeared finite-rank modes does not earn that transfer. The result supplies both
a genuine bounded continuum quantum dynamics and the exact missing locality
condition, rather than treating subsystem no-signalling as spacetime causality.

## Verification and hostile review

The producer verifies symbolic arbitrary real coupling amplitudes, all visible
matrix units, the complete exact solution, the positive-weight derivative,
NPT witness, center response, dissipation identity and dual-rail CAR reduction.
The separate probe independently constructs the Schrödinger generator and
partial trace on all16 matrix units, checks correlated input and exact forward
transfer/ODE, and rebuilds the CAR encoding by bit occupations. It starts with
a clean baseline, then plants the wrong Hamiltonian sign, a missing coherent
term, wrong jump, odd-for-even encoding, a reversed spatial jump, a population report fault and a pin
fault. Mathematical checks and report/pin checks are counted separately.

Hostile review checked sign convention, arbitrary initial correlations,
complete positivity versus Hamiltonian energy, quantum versus classical center,
odd versus even CAR embeddings, all-time claims versus first derivatives,
finite factors versus continuum field algebras, and selected noise versus a
source-owned environment. No blocking finding remains in this scope. No
independent-agent, expert or proof-assistant acceptance is claimed.

The resulting source-facing demand is concrete: specify the accessible algebra
and whether its law is exactly unitary, noisy but autonomous, or only classical
and nondemolition. These hypotheses admit different interactions. K1893 supplies
an actual bounded hidden continuum quantum interaction; the bounded continuum cascade
extension is nonlocal and its explicit causal countercontrol leaves the local
continuum construction and native bridge open.
