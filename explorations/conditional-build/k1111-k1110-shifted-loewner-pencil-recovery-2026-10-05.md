---
title: "K1111 shifted-Loewner pencil recovery"
status: active_research
doc_type: conditional_shifted_loewner_pencil_recovery
created: 2026-10-05
claim_ceiling: exact pole-shift recovery under owned affine part and finite order
manifest: lab/process/k1111-k1110-shifted-loewner-pencil-recovery.json
probe: tests/channel-swings/k1111_k1110_shifted_loewner_pencil_recovery_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1111 shifted-Loewner pencil recovery

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> rational inverse theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_LOEWNER_PENCIL_INVERSE`.

```gu-typed-objects
result: exact pole recovery from ordinary and shifted cross-Loewner matrices
carrier: one physical plus finitely many diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: positive auxiliary Gram form ON=conditional_block_hessian
real_structure: real diagonal simple-pole pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1110 Loewner identifiability boundary MAP-TYPE=evaluation
```

For

```text
S(z)=alpha*z+beta-sum_k w_k/(z+d_k),
```

take two disjoint `m`-node sets. After subtracting the owned affine part, the
ordinary and shifted cross-Loewner matrices are

```text
R_ij=(S(x_i)-S(y_j))/(x_i-y_j)-alpha
    =V_X diag(w) V_Y^T,

P_ij=alpha(x_i+y_j)+beta-(x_iS(x_i)-y_jS(y_j))/(x_i-y_j)
    =V_X diag(w*d) V_Y^T.
```

When the exact pole count is `m`, the shifts are distinct and the square
Cauchy factors are nonsingular, `det(P-dR)=0` has roots exactly `d_k`. For the
K1098 fixture on left modes `{0,1}` and right modes `{2,3}`, the normalized
pencil polynomial is

```text
d^2-4d+3=(d-1)(d-3).
```

Thus the shifts `1,3` are recovered exactly. The theorem requires the affine
part and pole order as independently owned inputs. It neither supplies those
inputs nor identifies a GU Hessian, functional domain or physical mode set.

The producer passes `12/12`; the hostile probe rejects `13/13` mutations.
