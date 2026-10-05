---
title: "K1094 affine branch reduction obstruction"
status: active_research
doc_type: conditional_affine_branch_reduction_obstruction
created: 2026-10-04
claim_ceiling: exact scalar Schur counterexample showing affine unreduced Hessian blocks need not yield affine physical branches
manifest: lab/process/k1094-k1093-affine-branch-reduction-obstruction.json
probe: tests/channel-swings/k1094_k1093_affine_branch_reduction_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1094 affine branch reduction obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> reduced-pencil theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_SPECTRAL_OBSTRUCTION`.

```gu-typed-objects
result: auxiliary elimination can turn an affine positive Hessian pencil into a non-affine physical branch
carrier: one harmonic plus one auxiliary real mode LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_reduced_hessian_pencil
real_structure: real symmetric two-mode pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU pencil or quotient
target: K1088 affine branch law after K1093 reduction MAP-TYPE=evaluation
```

Consider the positive affine unreduced pencil

```text
L(lambda) = [[lambda+2,1],[1,lambda+2]],  lambda>=0.
```

Its eigenvalues are the affine positive branches `lambda+1` and `lambda+3`.
But if the second coordinate is auxiliary, K1093 gives

```text
L_eff(lambda) = lambda+2 - 1/(lambda+2).
```

This branch is not affine: at `lambda=0,1,2` its exact values are
`3/2,8/3,15/4`, with second finite difference `-1/12`; analytically
`L_eff''=-2/(lambda+2)^3`. Zero mixing restores the affine branch, and a
lambda-independent invertible auxiliary block with constant mixing merely
shifts the intercept. A lambda-dependent eliminated block is therefore an
additional survival condition for K1088's intercept-to-slope reading.

The producer passes `11/11`; the hostile probe rejects `10/10` pencil,
positivity, Schur, non-affinity, repair and ownership mutations. This is an
exact counterexample to an inference, not a no-go theorem for GU.
