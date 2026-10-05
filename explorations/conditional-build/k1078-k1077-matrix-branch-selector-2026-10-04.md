---
title: "K1078 matrix branch selector"
status: active_research
doc_type: conditional_matrix_branch_selector
created: 2026-10-04
claim_ceiling: exact commuting finite-matrix branch recovery; no source-owned Hessian or dimensional mass
manifest: lab/process/k1078-k1077-matrix-branch-selector.json
probe: tests/channel-swings/k1078_k1077_matrix_branch_selector_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1078 matrix branch selector

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> selector, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: commuting normalized Hessian blocks yield affine frequency branches and exact intercept-to-slope selectors
carrier: common A-orthonormal normal modes LAYER=observed CHIRALITY=N/A
pairing: simultaneous eigenvalues b_j,c_j of A^-1B,A^-1C ON=candidate_action
real_structure: real finite-dimensional phase space
grading: joint eigenspaces, with unresolved basis inside repeated joint pairs
action_owner: repository-construction -- no source/action-owned A,B,C packet
target: K1077 commuting horn MAP-TYPE=evaluation
```

On the K1077 commuting horn, every joint eigenvector has

```text
omega_j(lambda)^2 = b_j lambda+c_j,
u_j = c_j/b_j                 (b_j>0).
```

Two distinct known spatial modes recover `b_j` and `c_j` exactly. The producer
recovers `(b,c,u)=(2,6,3)` and `(3,15,5)` from modes `lambda=3,11`.

An invertible field redefinition transforms `A,B,C` by one congruence and
preserves the generalized branch spectrum and each ratio `u_j`. A spatial
ruler change instead rescales the coefficient multiplying `lambda`; absolute
dimensional mass therefore still requires an independently owned ruler. If a
joint eigenvalue pair is repeated, the action selects its joint subspace but
not a preferred basis inside it.

Thus field normalization is not the missing selector, while spatial scale and
source/action ownership remain genuine burdens. The producer passes `9/9`;
the hostile probe rejects `10/10` branch, gauge, ruler, degeneracy, ownership
and promotion mutations.

## Next condition

Construct a two-spatial-mode test that detects the noncommuting horn before any
branchwise mass inference is attempted.
