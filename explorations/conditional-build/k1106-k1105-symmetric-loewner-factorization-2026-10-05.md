---
title: "K1106 symmetric Loewner factorization"
status: active_research
doc_type: conditional_symmetric_loewner_factorization
created: 2026-10-05
claim_ceiling: exact positive finite-rank Loewner-kernel theorem for positive diagonal Stieltjes branches
manifest: lab/process/k1106-k1105-symmetric-loewner-factorization.json
probe: tests/channel-swings/k1106_k1105_symmetric_loewner_factorization_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1106 symmetric Loewner factorization

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> scalar rational-function theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_LOEWNER_FACTORIZATION`.

```gu-typed-objects
result: positive finite-rank Loewner kernel for affine-minus-Stieltjes branches
carrier: one physical plus finitely many diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1105 finite-mode identifiability boundary MAP-TYPE=evaluation
```

For

```text
S(x)=alpha*x+beta-sum_i w_i/(x+d_i),
alpha>=0, w_i>0, d_i>0,
```

define the symmetric Loewner kernel by

```text
K_S(x,y)=(S(x)-S(y))/(x-y),
K_S(x,x)=S'(x).
```

Direct division gives

```text
K_S(x,y)=alpha+sum_i w_i/((x+d_i)(y+d_i)).
```

At nodes `x_1,...,x_n`, let `V_ji=1/(x_j+d_i)`. Then

```text
K_X=alpha*11^T+V diag(w_i) V^T.
```

Every finite matrix is therefore positive semidefinite. When the shifts are
distinct and `alpha>0`, the rational functions `1,1/(x+d_1),...,1/(x+d_m)`
are linearly independent, so `rank K_X=min(n,m+1)` on distinct regular nodes.

For the K1098 fixture with `alpha=2`, shifts `(1,3)`, weights `(1,4)` and
nodes `(0,1,2)`,

```text
K_X = [[31/9, 17/6, 13/5],
       [17/6, 5/2, 71/30],
       [13/5, 71/30, 511/225]].
```

Its leading principal minors are `31/9`, `7/12`, and `2/2025`; hence it is
positive definite of rank three. This exposes affine-plus-two-pole complexity
inside the frozen conditional class. It does not select a GU Hessian or provide
physical derivatives, modes or a detector.

The producer passes `11/11`; the hostile probe rejects `11/11` mutations.
