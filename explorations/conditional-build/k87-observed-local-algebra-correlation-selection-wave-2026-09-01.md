---
title: "K87 observed local-algebra correlation selection wave"
status: active_research
doc_type: reverse_scaffold_fixed_state_local_algebra_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact fixed-state two-qubit classification showing that distinct common conjugations of two commuting local matrix factors preserve algebraic locality while maximal CHSH spans 2 through 2sqrt(2), including a strict rational intermediate control; no source-selected local net, physical spacelike factorization, Born measurement dynamics, complete BFV descent, Bell prediction, confirmation, or verdict
manifest: lab/process/k87-observed-local-algebra-correlation-selection-wave.json
probe: tests/channel-swings/k87_observed_local_algebra_correlation_selection_probe.py
---

# K87 observed local-algebra correlation selection wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: exact fixed-state classification of how commuting local matrix-factor embeddings select product, intermediate and Tsirelson CHSH faces
carrier: bounded rank-four zero-one-particle sector inside the repository-selected K86 Fock control LAYER=observed CHIRALITY=N/A
pairing: normalized positive vector state and operator expectation ON=repository_owned_quantization_control
real_structure: real four-dimensional matrix witness inside the complex Hilbert representation
grading: zero-one particle tensor grading; distinct from BRST ghost grading
action_owner: repository-construction
target: fixed state plus varying commuting local observable embeddings to maximal CHSH face MAP-TYPE=evaluation
```

## Hold the state fixed

K86 showed that varying the state in one fixed matrix algebra changes the
CHSH value. This packet isolates the other missing owner: the local observable
embedding. Keep the normalized vector `|00>` fixed in the rank-four bounded
sector. Let `U_theta` rotate the span of `|00>,|11>` so that

```text
U_theta |00> = cos(theta)|00> + sin(theta)|11>.              (1)
```

Pull both standard local factors back by the same conjugation:

```text
A_theta = U_theta^* (M2 tensor I) U_theta,
B_theta = U_theta^* (I tensor M2) U_theta.                   (2)
```

For every `theta`, the two algebras in (2) remain matrix factors, and every
element of `A_theta` commutes with every element of `B_theta`. Expectations
in the one fixed state satisfy

```text
<00|U_theta^* O U_theta|00>
  = <psi_theta|O|psi_theta>,
psi_theta = cos(theta)|00>+sin(theta)|11>.                  (3)
```

Nothing about the positive state itself has changed. Only the identification
of which commuting subalgebras count as the two local parties has changed.

## Exact correlation-face classification

For `psi_theta`, the Pauli correlation tensor is

```text
T_theta = diag(sin(2 theta),-sin(2 theta),1).                (4)
```

The two largest eigenvalues of `T_theta^T T_theta` are `1` and
`sin^2(2 theta)`, so the exact maximal CHSH value obeys

```text
S_max(theta)^2 = 4[1+sin^2(2 theta)].                       (5)
```

The same fixed vector therefore lands on three distinct faces as the local
embedding changes:

```text
theta=0:                         S_max=2,
cos(theta)=3/5, sin(theta)=4/5: S_max^2=4[1+(24/25)^2],
theta=pi/4:                      S_max=2sqrt(2).              (6)
```

The middle value is strictly between `2` and `2sqrt(2)`. The probe performs
all conjugations with exact rational matrices for the `3-4-5` control, checks
four cross-commutators and four involutions, and verifies the correlation
tensor and boundary squares. It passes `25/25`; its hostile selftest catches
`17/17` mutations.

## What this does and does not select

Abstract cross-commutation is algebraic locality. It is not evidence that the
factors in (2) are assigned to spacelike-separated laboratories by the
action, causal domain or observation map. A globally entangling conjugation
is exactly why the family is a selection control rather than a physical
local-net construction. The stationary state principle from the sibling K87
packet can select a covariance and still leave this factor assignment open.

The strongest overclaim would report the `pi/4` endpoint as a Bell prediction.
The strongest contrary construction is the `theta=0` factorization of the
same state, which is exactly product and has maximal value `2`. The weakest
seam is the absent source/action-owned causal local net, detector map and full
constraint/domain descent. The result says the local-observable owner is
load-bearing; it does not say every algebraic factorization is physically
admissible.

No Born measurement dynamics, spacelike GU factorization, delayed-choice
score, prediction, confirmation, canon or public posture moves.

## Next condition

Derive the local observable net or detector embeddings from an action-owned
causal domain and observation map, then test their preservation through the
full constraint/BFV/Green quotient. Only after those owners and the physical
state are fixed can a correlation face become a candidate forward export.
