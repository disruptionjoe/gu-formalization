---
title: "K1093 Schur physical Hessian theorem"
status: active_research
doc_type: conditional_schur_physical_hessian
created: 2026-10-04
claim_ceiling: exact finite block-elimination and positivity theorem for a supplied harmonic plus auxiliary Hessian
manifest: lab/process/k1093-k1092-schur-physical-hessian.json
probe: tests/channel-swings/k1093_k1092_schur_physical_hessian_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1093 Schur physical Hessian theorem

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> finite effective-Hessian theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_EFFECTIVE_OPERATOR_THEOREM`.

```gu-typed-objects
result: eliminating a coupled auxiliary or coexact sector gives a Schur-complement physical Hessian
carrier: harmonic sector H direct_sum auxiliary sector A after exact gauge removal LAYER=toy CHIRALITY=N/A
pairing: positive block Hilbert pairing ON=conditional_reduced_hessian
real_structure: real symmetric or complex Hermitian blocks
grading: harmonic and auxiliary/coexact blocks
action_owner: repository-construction -- no source-selected GU functional Hessian
target: K1092 noninvariant harmonic mixing MAP-TYPE=quotient
```

Write a self-adjoint Hessian after exact gauge removal as

```text
L = [[A,B],[B*,D]]
```

on `H direct_sum A`, with `D` invertible. Solving the auxiliary equation gives
`y=-D^-1 B* x`; substitution yields the effective physical Hessian

```text
L_eff = A - B D^-1 B*.
```

The raw compression `A=P_H L P_H` is therefore correct only when the mixing
vanishes or when no elimination is intended. If `D>0`, block congruence gives
the exact positivity equivalence

```text
L>=0 iff L_eff>=0.
```

For the K1092 physical/auxiliary block `A=D=2`, `B=1`, the full nonzero
eigenvalues are `1,3`, the raw harmonic compression is `2`, and the physical
Schur value is `3/2`. The producer passes `11/11`; the hostile probe rejects
`10/10` formula, fixture, positivity and ownership mutations.

This result tells a future BV/BFV construction which operator to test. It does
not supply the functional domain, gauge fixing, boundary data or positivity
owner needed to perform that reduction in GU.
