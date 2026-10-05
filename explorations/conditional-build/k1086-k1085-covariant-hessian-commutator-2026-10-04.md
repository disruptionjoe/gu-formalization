---
title: "K1086 covariant Hessian commutator"
status: active_research
doc_type: conditional_covariant_hessian_commutator
created: 2026-10-04
claim_ceiling: exact connection-Laplacian commutator and parallel-potential criterion
manifest: lab/process/k1086-k1085-covariant-hessian-commutator.json
probe: tests/channel-swings/k1086_k1085_covariant_hessian_commutator_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1086 covariant Hessian commutator

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> covariant operator theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_OPERATOR_THEOREM`.

```gu-typed-objects
result: zero covariant kinetic-potential commutator requires a parallel commuting potential
carrier: smooth sections of a Euclidean or Hermitian bundle E over M LAYER=observed CHIRALITY=N/A
pairing: positive L2 bundle pairing ON=conditional_connection_hessian
real_structure: real Euclidean or complex Hermitian, stated per application
grading: differential orders two, one and zero in the commutator
action_owner: repository-construction -- no source-selected GU Hessian
target: K1085 curved functional seam MAP-TYPE=evaluation
```

Let `nabla` be metric-compatible, let `B` be positive, self-adjoint,
invertible and parallel, and set `H0=nabla* B nabla`. For a smooth
self-adjoint multiplication endomorphism `C`, a normal orthonormal frame gives

```text
[H0,C]f = (BC-CB)nabla*nabla f + B(nabla*nabla C)f
           - 2B sum_a (nabla_a C)(nabla_a f).
```

On interior compactly supported smooth sections this vanishes exactly when
`[B,C]=0` and `nabla C=0`. The order-two symbol supplies the first condition;
the order-one symbol and invertibility of `B` supply the second. Thus K1084's
coordinate constancy becomes covariant parallelism, not literal constancy in
an arbitrary frame.

The positive rotating example on the trivial `R2` bundle over `S1`,
`B=diag(1,2)` and `C(x)=R(x)diag(3,5)R(x)^T`, fires on the local jet
`f=0`, `nabla_x f=e1`, `nabla_x^2 f=0` at `x=0`, giving exact witness
`(0,8)`. Positivity alone still does not preserve the internal splitting.

The producer passes `10/10`; the hostile probe rejects `10/10` identity,
criterion, witness, inference and ownership mutations. Boundary-domain
preservation is a separate obligation addressed by K1087.
