---
title: "K1231--K1235 Bell source-state identifiability boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: INTERNAL_CONDITIONAL_MATHEMATICS
direction: observed_to_native
claim_effect: none
---

# K1231--K1235 Bell source-state identifiability boundary

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
result: affine local-channel two-qubit law, source-state counterexamples, minimum holdout certificate and unseal boundary
carrier: imported two-qubit density operators and affine qubit channel LAYER=observed CHIRALITY=N/A
pairing: imported trace/Born state-effect pairing ON=repository_quantum_control
real_structure: real Bloch vectors u,v, real correlation tensor T, transfer M and translation t
grading: process-calibration records versus independent source-characterization and sealed holdout records
action_owner: UNTYPED -- no GU or instantiated apparatus owner for any operational primitive
target: source-owned off-frame Bell probability table MAP-TYPE=evaluation
```

## Question and ceiling

K1226--K1230 correctly declare a `Phi+` Bell source and require source-fidelity
evidence, but the exact logical separation had not been measured. Do the
eighteen affine-process reads determine K1229's four Bell probabilities once
the same channel module is used? No. Those reads identify channel coordinates
inside a declared frame; the two-qubit source contributes independent local
and correlation data that never enter the process trials.

This packet is finite-dimensional operational mathematics. Every state,
channel, analyzer and Born rule is imported. It changes no source claim,
physics-ledger row, canon, paper, public posture, prediction or confirmation.

## K1231: general affine local-channel law

Write a general two-qubit state as

```text
rho=[I tensor I+u.sigma tensor I+I tensor v.sigma
     +sum_ij T_ij sigma_i tensor sigma_j]/4.
```

Applying the affine channel `r -> M r+t` to the first arm gives

```text
u'=M u+t,       v'=v,       T'=M T+t v^T.
```

The `t v^T` term follows because a nonunital trace-preserving channel sends
`I` to `I+t.sigma`. Binary analyzers `a,b` therefore obey

```text
p(x,y|a,b)=[1+x a.(M u+t)+y b.v
             +xy a^T(M T+t v^T)b]/4.
```

K1229 is the valid specialization `u=v=0`, `T=diag(1,-1,1)` for `Phi+`.
It is not the consequence of knowing `M,t` alone.

## K1232: exact same-channel counterexamples

Keep the K1223 channel, K1229 analyzers and both local source marginals zero.
The four Bell states and the maximally mixed source are all physical and share
those marginals, yet their correlation reads are respectively

```text
99/1625, 51/1625, -99/1625, -51/1625, 0.
```

They give five distinct positive normalized holdout tables. In particular,
the K1229 table cannot be inferred from a common calibrated channel, or even
from that channel plus maximally mixed source marginals. The independent
premise is the source correlation tensor in the authenticated analyzer frame.

## K1233: minimum certificate for one holdout pair

Every normalized binary-pair table has the unique form

```text
p_xy=(1+xA+yB+xyC)/4,
A=sum_xy x p_xy, B=sum_xy y p_xy, C=sum_xy xy p_xy.
```

The three nonconstant columns of the four-outcome Hadamard matrix have rank
three. Thus exactly three independent statistics determine one fixed analyzer
pair:

```text
A=a.(M u+t),  B=b.v,  C=a^T(M T+t v^T)b.
```

A separately certified `Phi+` preparation supplies their special values. A
more general source need not undergo full tomography if these three quantities
are certified on characterization data disjoint from the sealed holdout.

## K1234: joint dimension floors

An affine qubit channel has twelve real linear coordinates. A general
two-qubit state has fifteen Bloch coordinates `(u,v,T)`. Process calibration
has a zero Jacobian block on all fifteen source coordinates. Full joint linear
identification therefore has the direct floor `12+15=27` in authenticated
frames. For the one K1229 analyzer pair, the three source-sensitive functionals
above have rank three, so the corresponding joint floor is `12+3=15`.

This is a parameter-identifiability statement, not hardware authentication.
The SPAM-frame gauge from K1227 and cross-branch basis registration remain
separate physical-owner obligations.

## K1235: corrected unseal boundary

K1229's `Phi+` formula remains exact under its declared premise. Before
unsealing, however, the common-owner instance must contain an independent
source-state certificate for `A,B,C` (or a stronger certified preparation),
using records disjoint from the holdout. The holdout may not estimate the
source quantities it is supposed to test. Hardware/configuration identity,
authenticated process SPAM, raw attempts, sealed inclusion, randomization,
drift/loss/locality bounds, count/alpha allocation and a systematic ceiling
remain required as in K1226--K1230.

Delayed-choice entanglement swapping remains a separate reserved, unscored
family. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; and
LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`.

## Reproduction and hostile controls

Five producers check the exact affine transformation, five physical-state
counterexamples, the rank-three probability transform, the 15/27-dimensional
floors and the integrated unseal firewall. Five probes mutate the
load-bearing terms, ranks, independence rule and protected-status boundary.
