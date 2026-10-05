---
title: "K1096 Schur-affinity classification"
status: active_research
doc_type: conditional_schur_affinity_classification
created: 2026-10-04
claim_ceiling: exact scalar classification of when affine physical and auxiliary blocks retain an affine Schur-reduced branch
manifest: lab/process/k1096-k1095-schur-affinity-classification.json
probe: tests/channel-swings/k1096_k1095_schur_affinity_classification_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1096 Schur-affinity classification

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> scalar pencil theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_SCHUR_CLASSIFICATION`.

```gu-typed-objects
result: exact necessary and sufficient condition for an affine scalar Schur branch
carrier: one physical plus one auxiliary real mode LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric affine pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1094 non-affinity obstruction MAP-TYPE=evaluation
```

Let

```text
A(lambda)=a0+a1 lambda,
B(lambda)=b0+b1 lambda,
D(lambda)=d0+d1 lambda,
S(lambda)=A(lambda)-B(lambda)^2/D(lambda).
```

Suppose first that `d1 != 0`. If `S` is affine on any open interval on
which `D` is nonzero, the polynomial
`A D-B^2` must be divisible by `D`. At the unique root
`lambda_*=-d0/d1` of `D`, its remainder is

```text
-B(lambda_*)^2 = -(b0 d1-b1 d0)^2/d1^2.
```

Hence the reduced branch is affine exactly when

```text
b0 d1-b1 d0=0.
```

Equivalently `B=cD`, and then `S=A-c^2D` is affine. This includes a
nontrivial repair of K1094: `A=10+5 lambda`, `D=2+lambda`, and
`B=4+2 lambda=2D` give the positive reduced branch `S=2+lambda`. K1094's
fixture instead has `B=1`, so the determinant is one and the rational term
survives.

If `d1=0` and `d0 != 0`, the quadratic coefficient of `S` is
`-b1^2/d0`; the reduced branch is affine exactly when `b1=0`. Thus a
constant auxiliary block tolerates constant mixing, while a moving auxiliary
block tolerates affine mixing only when the mixing tracks that block exactly.

The producer passes `14/14`; the hostile probe rejects `9/9` mutations. The
classification supplies an exact survival test for a future physical Hessian,
but it does not provide that Hessian, its BV/BFV quotient or a measured mode.
