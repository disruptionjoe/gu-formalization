---
title: "K1904: Separated dephasing environments and the classical-phase boundary"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum and controlled-environment mathematics; no native GU or continuum bath identification
scripts:
  - tests/channel-swings/k1904_spacelike_dephasing_locality.py
  - tests/channel-swings/k1904_spacelike_dephasing_locality_probe.py
---

# K1904: Separated dephasing environments and the classical-phase boundary

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
result: joint spectral measure of commuting vacuum-relative unitaries
carrier: four fixed-occupation logical modes with commuting environment algebras LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and state expectation ON=conditional_target
real_structure: complex conjugation and CAR star; no native K/C identification
grading: finite occupation sectors and even fermion parity
action_owner: repository-construction -- supplied finite interactions or quantum channels
target: conditional coherence, causal implementation and memory demands MAP-TYPE=intertwiner
```

## Question, assumptions and exact result

K1903 constructs a four-mode Schur channel C with no classical phase law.
Can independent spatially separated occupation-controlled couplings to a
shared, possibly entangled quantum environment realize it? The answer is no
for the precise controlled-unitary model below. This does not identify
no-signalling with localizability for general channels.

Let n_j be commuting fermion occupation projections and let A_j be mutually
commuting unital environment algebras. At site j choose unitaries U_j0,U_j1
in A_j and apply

    W_j=(1-n_j) tensor U_j0 + n_j tensor U_j1.

The initial system and environment are uncorrelated, with arbitrary environment
state omega, including entangled states across the local algebras. No hopping,
postselection, conditioning on measurement outcomes or communication between
sites is included during this layer. The algebras commute across different
sites; within each A_j the two unitaries need not commute.

Write V0=product_j U_j0 and R_j=U_j0* U_j1. In the one-particle sector,
the branch with occupied mode j acts on the environment as V0 R_j. Thus

    D_jk=omega(R_k* R_j).

The R_j are mutually commuting normal unitaries. The commutative C*-algebra
they generate has a joint spectral probability measure mu for the restricted
state omega. Consequently

    D_jk = integral z_j conjugate(z_k) d mu(z),  |z_j|=1.       (1)

This is a classical phase correlation, regardless of entanglement in omega.
The proof does not require a product bath state, finite bath dimension,
commuting Hamiltonians within a site, or a tensor-factor decomposition of the
bath. It requires the actual integrated relative unitaries to lie in mutually
commuting algebras. Microcausality can supply this hypothesis for appropriately
localized even interactions with spacelike-separated supports; an arbitrary
finite dilation cannot supply it by assertion. Time-ordered overlapping or
causally connected interaction regions are different hypotheses.

Conversely every finite classical phase mixture is realized by a shared
classical environment label and commuting diagonal R_j. For an arbitrary
probability law, multiplication by z_j on L2(mu), in the unit vector 1, gives
(1). This is an algebraic realization, not a relativistic field construction
or a thermal-resource claim. Equation(1) classifies this declared single-layer
model exactly on the one-particle sector.

## Operational consequence and robust version

Reuse K1903's C=V*V, columns (1,0),(0,1),(1,1)/sqrt2,(1,i)/sqrt2,
and its H=B*B, delta=6-4sqrt2. Every channel in(1) has
tr(H D)>=delta, while tr(H C)=0. On the normalized equal-superposition
input, the bounded observable H produces expectations >=delta/4 versus0.
Its measurement may require recombination in a common causal future.
There is no inference that the four spatial parties perform this measurement
locally at spacelike separation.

If actual relative unitaries R_j are within operator norm epsilon of commuting
unitaries S_j on the SAME Hilbert space with the SAME state, then each
correlation entry differs by at most2epsilon. The exact off-diagonal absolute
sum of H is10sqrt2; therefore

    tr(H D_R) >= delta -20sqrt2 epsilon.                       (2)

An exact realization of C cannot be uniformly closer than
(6-4sqrt2)/(20sqrt2) to such a commuting family. This is a distance-to-a-
specified-commuting-model estimate, NOT a theorem deriving that distance from
small commutators. No dimension-independent almost-commuting theorem is used.
Experimental entrywise error adds the separate10sqrt2 times error margin.

## Why dropping commutation changes the causal question

A shared qubit initialized in |+> illustrates the danger. Alice's encoded
logical occupation a controls Z on the memory. Later Bob's logical occupation
controls X on the same memory. Bob starts in |+>. If a=0, his final state is
|+>; if a=1 it is |->, after tracing the memory. Thus Bob's X expectation
is +1 versus -1. Both site logical qubits may be encoded in two fermion modes
with exactly one fermion, making the preparations and X observable even,
number-preserving operations; this example does not rely on forbidden odd
local fermionic coherence. The common memory and ordered noncommuting gates
carry a perfect forward signal. Calling both interactions spacelike local
would be false. A physically transported memory with adequate delay is a
causal repair, not a counterexample to(1).

Nonclassicality on a restricted one-particle sector alone does not prove
signalling for an unspecified extension to every occupation sector. The
counterexample above is an explicitly supplied extension and intervention.
Conversely the theorem excludes one controlled-local realization class,
not every causal quantum channel, entangled field environment, or GU theory.

## Context and verification

The distinction between localizable and causal operations is established in
[Beckman et al.](https://authors.library.caltech.edu/records/v9xay-ydw79).
[Lonigro and Chruscinski](https://www.frontiersin.org/journals/quantum-science-and-technology/articles/10.3389/frqst.2022.1090022/full)
study classicality of dephasing processes; their multi-time definition must
not be conflated with the single-time phase-mixture property used here.
The proof above is self-contained; no novelty claim is made. K1905 supplies
the timed-memory construction released by this obstruction.

## Source ceiling and validation

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN.
These supplied positive-Hilbert constructions identify none of their missing
native full20 injection, separate K/C forms, accessibility or physical state.
LT-SM8, LT-GR6b and AC-F1, source polarities, physics-ledger and canon verdicts
remain unchanged. The result has independent quantum-mathematical scope.
No novelty, external expert acceptance, formal proof, continuum field energy,
microscopic bath selection, GU prediction or GU falsification is claimed.

The analytic proof carries general statements. Exact producer controls and a
separate probe rederive finite matrices, partial traces, generator identities
and bounds. Mathematical input faults are tested after a passing baseline;
report and dependency-pin faults are counted separately. Inline hostile review
checks the strongest overclaim, a contrary construction and the weakest
transfer/reproducibility seam. A finite control does not establish the general
spectral, tensor-factorization or continuity argument by itself.
