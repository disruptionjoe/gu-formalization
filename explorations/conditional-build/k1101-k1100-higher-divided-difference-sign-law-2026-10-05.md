---
title: "K1101 higher divided-difference sign law"
status: active_research
doc_type: conditional_higher_divided_difference_sign_law
created: 2026-10-05
claim_ceiling: exact alternating higher divided-difference law for positive diagonal Stieltjes branches
manifest: lab/process/k1101-k1100-higher-divided-difference-sign-law.json
probe: tests/channel-swings/k1101_k1100_higher_divided_difference_sign_law_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1101 higher divided-difference sign law

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> scalar rational-function theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_STIELTJES_SIGN_HIERARCHY`.

```gu-typed-objects
result: alternating higher divided-difference signs for positive Stieltjes corrections
carrier: one physical plus finitely many diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1099 three-mode witness MAP-TYPE=evaluation
```

For the K1098 class

```text
S(x)=alpha x+beta-sum_i w_i/(x+d_i),  w_i>=0,
```

take distinct ordered points `x_0,...,x_k` in the common positive domain.
The elementary divided-difference identity

```text
(1/(x+d))[x_0,...,x_k]=(-1)^k/prod_j(x_j+d)
```

gives, for every `k>=2`,

```text
S[x_0,...,x_k]
  =(-1)^(k+1) sum_i w_i/prod_j(x_j+d_i).
```

Therefore `(-1)^(k+1) S[x_0,...,x_k]` is strictly positive exactly when at
least one coupling weight survives. The sign alternates at every higher order;
it is not merely a second-difference concavity statement.

For the K1098 fixture on modes `0,1,2,3,4`, the branch values are
`8/3,11/2,118/15,121/12,428/35`. The order-two, order-three and order-four
divided differences are respectively

```text
-7/30,  19/360,  -5/504.
```

The producer passes `9/9`; the hostile probe rejects `9/9` mutations. The
alternating sequence detects positive mixing inside the frozen model class,
but does not identify the auxiliary multiplicity, shifts or weights and does
not supply a source-selected GU Hessian, physical spectrum or measured mode.
