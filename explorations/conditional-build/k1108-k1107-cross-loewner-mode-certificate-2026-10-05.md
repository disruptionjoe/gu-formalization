---
title: "K1108 cross-Loewner mode certificate"
status: active_research
doc_type: conditional_cross_loewner_mode_certificate
created: 2026-10-05
claim_ceiling: exact derivative-free auxiliary-order lower bound from disjoint finite mode sets
manifest: lab/process/k1108-k1107-cross-loewner-mode-certificate.json
probe: tests/channel-swings/k1108_k1107_cross_loewner_mode_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1108 cross-Loewner mode certificate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> scalar rational-function theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_CROSS_LOEWNER_CERTIFICATE`.

```gu-typed-objects
result: derivative-free cross-Loewner rank certificate on disjoint exact modes
carrier: one physical plus finitely many diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1107 confluent rank certificate MAP-TYPE=evaluation
```

Take disjoint left and right mode sets. The cross-Loewner matrix

```text
D_ij=(S(x_i)-S(y_j))/(x_i-y_j)
    =alpha+sum_k w_k/((x_i+d_k)(y_j+d_k))
```

factors through left and right Cauchy feature matrices. For positive slope and
weights, distinct shifts, and `m+1` distinct regular nodes on each side, its
determinant is nonzero. Thus a nonzero `r x r` determinant certifies at least
`r-1` poles without derivative observations.

For left modes `(0,1,2)` and right modes `(3,4,5)`, the K1098 branch gives

```text
D = [[89/36, 251/105, 7/3],
     [55/24, 157/70, 53/24],
     [133/60, 229/105, 97/45]],
det D = 1/113400.
```

Six exact values therefore certify at least two poles; an independently owned
at-most-two bound would make the order exact. This uses the same `2m+2` values
as K1103 for `m=2`, but supplies a constructive rank witness rather than
parameter recovery or an exclusion of all higher-order aliases.

The producer passes `11/11`; the hostile probe rejects `12/12` mutations.
