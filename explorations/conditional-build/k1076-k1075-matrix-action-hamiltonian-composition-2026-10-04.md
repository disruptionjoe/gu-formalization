---
title: "K1076 matrix action/Hamiltonian composition"
status: active_research
doc_type: conditional_matrix_action_hamiltonian_theorem
created: 2026-10-04
claim_ceiling: exact finite-matrix action-to-Hamiltonian composition; no source-owned GU Hessian or functional domain
manifest: lab/process/k1076-k1075-matrix-action-hamiltonian-composition.json
probe: tests/channel-swings/k1076_k1075_matrix_action_hamiltonian_composition_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1076 matrix action/Hamiltonian composition

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> candidate-action theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_COMPOSITION`.

```gu-typed-objects
result: finite-rank positive action Hessian composes exactly with a Hamiltonian generator and conserved pairing
carrier: n-component real quotient modes LAYER=observed CHIRALITY=N/A
pairing: S(lambda)=diag(lambda B+C,A^-1) ON=repository_owned_candidate_action
real_structure: real finite-dimensional phase space
grading: supplied physical quotient coordinates; no functional BV grading
action_owner: repository-construction -- no source-owned GU Hessian
target: K1074 scalar affine stiffness law MAP-TYPE=evaluation
```

Let `A` be positive definite, let `B,C` be symmetric, and put

```text
L_lambda = 1/2 qdot^T A qdot - 1/2 q^T(lambda B+C)q.
```

For canonical momentum `p=A qdot`, the phase generator and Hamiltonian pairing
are

```text
K(lambda) = [[0,A^-1],[-(lambda B+C),0]],
S(lambda) = diag(lambda B+C,A^-1).
```

Direct block multiplication gives
`K(lambda)^T S(lambda)+S(lambda)K(lambda)=0` without a commutation assumption
on `A,B,C`. Given `A>0`, the energy is positive exactly on modal regions where
`lambda B+C>0`. K1074 is the one-component special case.

The result upgrades the scalar selector to the first finite-rank Hessian object
that a native action could instantiate. It does not supply such an action,
quotient, stationary background or common functional domain. The producer
passes `9/9`; the hostile probe rejects `9/9` identity, positivity, ownership
and scope mutations.

## Next condition

Determine exactly when one mode-independent field basis diagonalizes the
kinetic-normalized gradient and mass blocks.
