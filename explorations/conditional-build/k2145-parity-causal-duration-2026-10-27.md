---
title: "K2145: Causal duration and recorded-channel error for regional parity"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source selection, apparatus construction or GU recovery
scripts:
  - tests/channel-swings/k2145_parity_causal_duration_probe.py
---

# K2145: Causal duration and recorded-channel error for regional parity

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
result: Causal duration and recorded-channel error for regional parity
carrier: massive real scalar Fock space on R and arbitrary independent apparatus LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form, free energy and trace distance ON=declared_carrier
real_structure: real coefficients and complex adjoint as stated
grading: one regional canonical-mode parity, not global or fermion parity
action_owner: repository-construction -- explicit conditional object below
target: causal approximation error with explicit finite-energy witnesses MAP-TYPE=intertwiner
```

## 1. Fixed operational convention

Use [K2143](k2143-local-canonical-parity-2026-10-27.md): m>0, real normalized
f in C_c^infinity(R), R=I-2|f><f|, regional parity V, projections K_±=(I±V)/2.
The target instrument is I_f(rho)=sum_± |±><±| tensor K_±rho K_±; unread it is
Phi_f(rho)=(rho+Vrho V)/2. It measures local canonical parity, not global
particle parity. All inputs and outputs below use one FIXED Schrödinger Cauchy
coordinate identification. The target is Phi_f itself, not free evolution
composed with Phi_f. If a different target includes free evolution, Bob's witness
and causal regions must be transported and the bound recomputed.

Let Psi_T be an actually causal channel implemented during0<=t<=T, with initially
independent apparatus. Apparatus correlations across its sites are allowed. Its
precise needed property is: an input intervention in A cannot change the output
algebra in B when dist(A,B)>T, in units c=1. This is an operational assumption
on the real spacetime dynamics, not a consequence of algebra-local Kraus membership.
The standard distinction is explained by
[Fewster–Verch](https://arxiv.org/abs/1810.06512) and
[Bostelmann–Fewster–Ruep](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.025017).
We specialize its witness to the actual K2143 instrument; no novelty claim.

## 2. From signalling to a quantitative error bound

Choose real h,g in C_c^infinity with disjoint supports A,B and

    a=<f,h> !=0, b=<f,g> !=0, c_g=<Rg,omega^-1 Rg> >0.

Alice's two field inputs are vacuum and U_A(lambda)vacuum, with
U_A=exp(-i lambda pi(h)); Bob observes the norm-one Weyl W_B(t)=exp(i t phi(g)).
K2143 gives the difference of Bob's target expectations

    Delta = exp(-t^2 c_g/4) |sin(t lambda a b)|.                      (1)

The two actual Bob expectations agree if T<dist(A,B). If each field output
has half trace distance at most epsilon from its target, each expectation differs
by at most2epsilon, so Delta<=4epsilon. Consequently

    epsilon >= (1/4) exp(-t^2 c_g/4) |sin(t lambda a b)|.             (2)

The same lower bound holds for the complete recorded instrument and arbitrary-reference
half-diamond error: discarding record cannot increase trace distance, and these
unreferenced inputs are allowed tests. The witness does not prove a matching upper bound.
Taking lambda->infinity and t=pi/(2|lambda ab|) proves unrestricted error>=1/4.
Every witness has finite energy, but that supremum uses unbounded energies.
Tiny nonzero spatial tails can therefore matter at unrestricted diamond norm;
this does not assert a uniform fixed-energy tail bound.

## 3. Finite input energy, not controller work

The displaced vacuum has energy lambda^2 Q_h/2, where
Q_h=<h,omega^2 h>=m^2||h||^2+||h'||^2. For any E>0 choose
lambda=sqrt(2E/Q_h) and t=pi/(2|lambda ab|). Both inputs have mean free energy<=E.
The energy-constrained half-diamond error, with the constraint on field input, obeys

    epsilon_E >= (1/4) exp[-pi^2 c_g Q_h/(32 E a^2 b^2)]             (3)

whenever T<dist(A,B). This is an explicit strictly positive witness, not the optimum.
The bound prices field input energy only; it does not quantify state preparation,
probe energy, readout, reset or total controller work.
For exact implementation, take any two separated nonzero patches of f. Their
separation can approach diam(supp f), so necessarily T>=diam(supp f).
Necessity is not sufficiency or a microscopic implementation.

## 4. Widening support trades baseline against causal duration

For f_L=L^-1/2 f(x/L), dilate fixed nonzero-overlap h,g likewise, with base
separation d0>0. Then a,b are fixed, Q_hL=m^2||h||^2+L^-2||h'||^2, and
c_gL<=||g||^2/m because R_L is orthogonal. Hence for T<d0 L,

    epsilon_E >= C_L := (1/4) exp[-pi^2 Q_hL ||g||^2/(32 m E a^2 b^2)]. (4)

C_L tends a positive C_infinity. For any fixed tolerance below C_infinity,
sufficiently large L requires T>=d0 L. K2143 independently proves
p_L=v/(16m^4 L^4)+O(L^-6), v=mu4-mu2^2>0. On THIS fixed-profile dilation family,

    T >= d0 (v/(16m^4 p_L))^(1/4) (1+O(p_L^(1/2)))                 (5)

in the preceding error regime. This is not a universal noise-duration law.
[K2146](k2146-fixed-support-parity-ultraviolet-2026-10-27.md) tests a distinct
fixed-support, increasing-frequency family; its noise tends to zero without
support growth. One cannot transfer (5) between those families.

## 5. A communication-dependent finite-mode counterconstruction

A finite nearest-neighbor oscillator chain illustrates an escape from instantaneous
implementation without claiming a continuum apparatus. Take canonical site modes a_j
and real normalized f_j. A real orthogonal matrix O can be decomposed into adjacent
Givens rotations, with first row f. Its number-preserving Gaussian lift B can be
chosen so B* a_1 B=sum f_j a_j. The circuit B, followed by a supplied controlled
endpoint parity and then B*, yields controlled parity of the f mode. With memory
|+> and X readout its EXACT Kraus operators on the entire finite oscillator Fock
space are (I±V_f)/2. A recursive adjacent rotation sequence needs n-1 gather gates
and n-1 inverse gates, plus endpoint control. No Fock cutoff is needed for this
algebraic identity; the probe checks the three-mode orthogonal action and memory
instrument finite controls, not the infinite-domain theorem by truncation.

The beam-splitter generators are selfadjoint second quantizations of finite
Hermitian matrices; endpoint number and its controlled phase have their usual
selfadjoint domains. This establishes abstract unitaries. Their spatially local
relativistic realization, unavoidable KG drift, gate durations, field/controller
energy and continuum convergence are UNSUPPLIED. Communication time and microscopic
locality cannot be inferred from a circuit diagram. Pre-entanglement or delayed
record comparison does not remove the unread witness in (1).

## Acceptance and source boundary

The adjacent probe checks finite exact identities, certificate arithmetic and altered-input
controls. Universal statements use the written arguments and independent internal specialist
review; finite controls do not prove continuum claims. No external-expert certification,
proof-assistant verification, remote CI or novelty claim is made. SC-OP-04 ASSERTS candidate
operator grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action
prerequisite. LT-SM8/LT-GR6b, ledger0.263, source polarity and canon are unchanged.
