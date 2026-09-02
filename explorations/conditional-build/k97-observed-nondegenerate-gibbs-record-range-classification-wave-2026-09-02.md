---
title: "K97 observed nondegenerate Gibbs record-range classification wave"
status: active_research
doc_type: reverse_scaffold_nondegenerate_gibbs_record_range_classification_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K96_NONDEGENERATE_GIBBS_RECORD_ALGEBRA_SELECTOR
target_claim_verdict: CONDITIONAL_FINITE_SELECTOR_CLOSED_COARSE_AND_DEGENERATE_AMBIGUITY_CLASSIFIED_PHYSICAL_OWNER_OPEN
claim_ceiling: exact finite-dimensional classification of continuously dynamics-covariant Gibbs-state-preserving conditional expectations onto abelian C-star subalgebras for a simple Hamiltonian, with uniqueness of the energy spectral MASA only under maximality or canonical-trace preservation; no derivation of the Hamiltonian, temperature, Gibbs principle, classicality, maximal resolution, physical coupling, irreversibility, source local algebra, continuum AQFT, microlocal state, Born rule, prediction, confirmation, held-out score or GU verdict
manifest: lab/process/k97-observed-nondegenerate-gibbs-record-range-classification-wave.json
probe: tests/channel-swings/k97_observed_nondegenerate_gibbs_record_range_classification_probe.py
---

# K97 observed nondegenerate Gibbs record-range classification wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: exact finite-M_n classification of covariant Gibbs-preserving abelian conditional-expectation ranges and the maximal-or-tracial spectral-MASA selector
carrier: M_n(C), specialized by the exact probe to n=3 and rho_beta=diag(4,2,1)/7 LAYER=observed CHIRALITY=N/A
pairing: imported canonical normalized trace tau=Tr/n and imported Gibbs/KMS state phi_beta(A)=Tr(rho_beta A) ON=repository_owned_finite_selector_control
real_structure: matrix adjoint and standard complex conjugation
grading: energy spectral projections and their partition lattice; no source BV, BFV or ghost grading
action_owner: repository-construction
target: K96 conditional-expectation record-algebra selection boundary MAP-TYPE=evaluation
```

Scope: this is an exact finite full-matrix-algebra theorem. It classifies the
coarse record ranges left by covariance and Gibbs preservation, then states
the two extra hypotheses that collapse the classification to the energy
spectral MASA. Those hypotheses are not derived physical facts.

## Inline preflight bookend

The route-changing lens census covered finite C-star conditional
expectations, maximal abelian subalgebras, canonical-trace versus Gibbs-state
preservation, continuous dynamical and modular covariance, energy and thermal
degeneracy, beta zero, coarse graining, gap resonance, state faithfulness,
source custody and falsification scope. The dominant route is a classification
theorem plus sharp counterexamples: covariance and state preservation align an
abelian range with energy, but do not by themselves force maximal resolution.

Retrieval found K96's degenerate `M2(C)` `Z/X` nonuniqueness control, its
unbounded translation pointer with no normal Gibbs density, K94's imported
finite Gibbs principle, and K92/K93's locality/action-net ambiguity. It found
no repository theorem classifying all abelian conditional-expectation ranges
for a simple finite Hamiltonian. Standard finite conditional-expectation and
Gibbs facts receive no literature-novelty claim. Positive controls enumerate
every partition of three exact Gibbs weights. Negative controls remove trace
preservation or commutativity, introduce degeneracy or beta zero, or promote
the result to source/continuum/Born ownership.

## Setup

Let

```text
A=M_n(C),                 H=sum_i epsilon_i P_i,             (1)
alpha_t(A)=e^(itH) A e^(-itH),                              (2)
rho_beta=Z^(-1)e^(-beta H)=sum_i r_i P_i,                   (3)
phi_beta(A)=Tr(rho_beta A).                                 (4)
```

Assume `H` has simple spectrum and `beta != 0`. Then the rank-one spectral
projections `P_i` are unique and the faithful Gibbs weights
`r_i=e^(-beta epsilon_i)/Z` are pairwise distinct. No nonresonance assumption
on the energy gaps is made.

Let `E:A -> N` be a genuine C-star conditional expectation: a unital
completely positive idempotent map whose range `N` is a unital C-star
subalgebra and for which

```text
E(BAC)=B E(A) C             for B,C in N.                    (5)
```

Assume that `N` is abelian and

```text
E alpha_t = alpha_t E       for every real t,                (6)
phi_beta E = phi_beta.                                       (7)
```

The word "conditional expectation" in this result includes the original-
product subalgebra and bimodule conditions. A bare unital CP idempotent with a
Choi-Effros operator-system range is outside the theorem.

## Full partition theorem

**Theorem.** Under (1)--(7), there is a unique partition `pi` of
`{1,...,n}` such that, for

```text
Q_B=sum_(i in B) P_i,       r_B=sum_(i in B) r_i,             (8)
N_pi={sum_(B in pi) c_B Q_B},                                (9)
```

one has `N=N_pi`. The expectation is uniquely

```text
E_pi(A)=sum_(B in pi) [Tr(rho_beta Q_B A Q_B)/r_B] Q_B
       =sum_(B in pi) [(sum_(i in B) r_i Tr(P_i A))/r_B] Q_B. (10)
```

**Proof.** Covariance gives `alpha_t(N)=N`. A finite-dimensional abelian
C-star algebra is isomorphic to `C^k`, and its automorphism group permutes its
finitely many minimal projections. The continuous homomorphism
`t -> alpha_t|_N` from connected `R` to that finite permutation group is
constant. Thus every element of `N` commutes with `H`.

Because `H` is simple, its commutant is the energy spectral MASA

```text
D_H={sum_i a_i P_i}.                                        (11)
```

Therefore `N` is a unital subalgebra of `D_H`. Unital subalgebras of `C^n`
are exactly the algebras of functions constant on the blocks of a unique set
partition, proving (8)--(9).

Bimodularity makes `E(Q_B A Q_C)=0` for distinct blocks. On a diagonal block,
the range is one-dimensional, so
`E(Q_B A Q_B)=lambda_B(A)Q_B`. Applying (7) forces

```text
lambda_B(A)=Tr(rho_beta Q_B A Q_B)/r_B,                      (12)
```

which proves (10) and uniqueness. Conversely, every map (10) is a unital CP
idempotent conditional expectation, is `alpha`-covariant, preserves
`phi_beta`, and has range `N_pi`. This completes the classification.

## Spectral-MASA corollary

If the record range is required to be a MASA, the partition must consist of
singletons. Hence

```text
N=D_H=C*(H)=C*(rho_beta),
E(A)=Delta_H(A)=sum_i P_i A P_i.                             (13)
```

There is also a shorter proof showing which assumptions do the work. A
conditional expectation onto a MASA is dephasing in that MASA's rank-one
minimal projections. Gibbs-state preservation forces `rho_beta` to be
diagonal in those projections. Since `rho_beta` has simple spectrum, those
projections are exactly the `P_i`. Thus Gibbs preservation plus the imported
MASA requirement already implies (13); covariance is redundant in this
corollary.

## Canonical-trace corollary

Let `tau=Tr/n`. Maximality need not be assumed if `E` also preserves `tau`.
For (10), canonical-trace preservation holds exactly when

```text
r_i=r_B/|B|                for every i in every B.            (14)
```

Since the finite-beta Gibbs weights are pairwise distinct, (14) forces every
block to be a singleton and again gives (13).

Equivalently, a `tau`-preserving conditional expectation is the orthogonal
projection for the Hilbert-Schmidt pairing and is `tau`-self-adjoint. From
`phi_beta E=phi_beta` one obtains

```text
tau(rho_beta A)=tau(rho_beta E(A))=tau(E(rho_beta)A),         (15)
```

so `E(rho_beta)=rho_beta` and `rho_beta` lies in `N`. But
`C*(rho_beta)` is already a MASA. An abelian algebra containing it can only be
that MASA.

The exact conclusion matching K96's stronger list is therefore:

> An abelian range, canonical-trace preservation and preservation of a
> nondegenerate finite Gibbs state select the energy spectral MASA. Continuous
> covariance is compatible but no longer load-bearing after these assumptions
> are imposed.

## Sharp counterexamples and remaining degeneracy

### Covariance plus Gibbs preservation is not enough

For

```text
H=diag(0,ln 2), beta=1, rho_beta=diag(2/3,1/3),              (16)
```

both the spectral dephasing `Delta_H` and

```text
E_C(A)=phi_beta(A) I                                        (17)
```

are unital CP idempotent C-star conditional expectations, commute with
`alpha_t`, and preserve `phi_beta`. Their ranges are `D_H` and `C I`.
Equation (17) fails canonical-trace preservation, precisely identifying the
condition that eliminates this coarse record algebra.

### Commutativity is load-bearing

The identity map on `M_n(C)` preserves the canonical trace, the Gibbs state
and the dynamics and is a unital CP idempotent conditional expectation. Its
range is the full noncommutative algebra. Thus trace plus state plus covariance
cannot select a record algebra unless classical/abelian range is stipulated.

### Energy degeneracy leaves a basis family

If an eigenspace of `H` has dimension greater than one, `rho_beta` is scalar
on that eigenspace. Every orthonormal basis choice inside it gives a different
`alpha`-covariant, `tau`- and `phi_beta`-preserving MASA dephasing. The K96
`H=0` expectations `E_Z` and `E_X` are the minimal exact instance. The coarser
algebra `C*(H)` also survives. Nondegeneracy is therefore essential.

### Beta zero leaves coarse partitions

At `beta=0`, `rho_0=I/n` and Gibbs preservation is identical to canonical-
trace preservation. Even for simple `H`, every energy partition expectation
in (10) preserves both states and is continuously covariant. It does not force
maximal resolution. Finite nonzero beta is essential to the trace corollary.

## Exact three-level control

The probe takes

```text
H=(ln 2) diag(0,1,2),       beta=1,
rho_beta=diag(4/7,2/7,1/7).                               (18)
```

It enumerates all five partitions of three labels. Every associated `E_pi`
is unital, CP, idempotent, Gibbs preserving and continuously covariant. Only
the singleton partition is canonical-trace preserving. For the explicit
coarse block `pi={{0,1},{2}}`,

```text
E_pi(P_0)=(2/3)(P_0+P_1),  Tr(E_pi(P_0))=4/3 != 1.           (19)
```

The equally spaced energies intentionally retain a repeated gap. Their exact
success proves that gap nonresonance is not an assumption of the theorem.

## Owner accounting

Repository-owned here are the finite partition classification, formula (10),
the MASA and canonical-trace corollaries, the exact three-level enumeration,
and the sharp scalar/full/degenerate/beta-zero boundaries. Imported are the
Hamiltonian, finite nonzero temperature, Gibbs/KMS principle, canonical trace,
state/probability pairing, the abelian-record interpretation and either
maximal resolution or trace preservation. No source-selected owner is added.

## Maximum licensed conclusion

For a simple finite Hamiltonian, continuous covariance and preservation of its
finite nonzero-beta Gibbs state classify abelian conditional-expectation
ranges by partitions of the energy eigenlines. They do not select a unique
record resolution. The energy spectral MASA becomes unique only if maximality
is imposed or canonical-trace preservation is added.

This is a conditional finite-algebra selector theorem, not a physical
derivation of a record algebra. It neither supplies the Hamiltonian or Gibbs
principle nor explains why a physical record must be commutative, maximally
resolved or trace preserving.

## Inline postflight bookend

- Strongest overclaim: saying that nondegenerate Gibbs dynamics physically
  selects records. The theorem selects only relative to an imported
  Hamiltonian/state and explicit abelian-plus-maximal-or-tracial conditions.
- Strongest contrary construction: the scalar expectation and the full
  partition family prove that covariance plus state preservation alone remain
  nonunique even for a simple Hamiltonian and faithful nontracial Gibbs state.
- Weakest reproducibility seam: the classification proof is exact prose-level
  finite operator algebra; the exhaustive `n=3` probe is regression evidence,
  not a proof for arbitrary `n`.

The exact probe and hostile selftest cover partition completeness, Kraus/Choi
positivity, idempotence, state and trace preservation, covariance, degeneracy,
beta zero, owner custody and promotion fences. No source, continuum,
microlocal, Born, prediction, confirmation, canon, paper or held-out status
moves.

## Next condition

Derive, rather than stipulate, an abelian maximally resolved or canonically
trace-preserving record range from a lower-bounded many-body reservoir, local
interaction, source causal/action structure or modular inclusion. Prove the
resulting physical state and reduced asymptotic instrument on a common domain
and test compatibility with the K91 quotient and K96 stable-record control.
