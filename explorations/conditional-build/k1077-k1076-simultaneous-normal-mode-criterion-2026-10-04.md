---
title: "K1077 simultaneous normal-mode criterion"
status: active_research
doc_type: conditional_simultaneous_normal_mode_theorem
created: 2026-10-04
claim_ceiling: exact finite-rank simultaneous-normal-mode equivalence; no unbounded-operator or GU-source theorem
manifest: lab/process/k1077-k1076-simultaneous-normal-mode-criterion.json
probe: tests/channel-swings/k1077_k1076_simultaneous_normal_mode_criterion_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1077 simultaneous normal-mode criterion

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> action-Hessian theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: one mode-independent normal basis exists exactly on the commuting normalized Hessian horn
carrier: n-component real quotient modes LAYER=observed CHIRALITY=N/A
pairing: positive kinetic matrix A and affine stiffness lambda B+C ON=candidate_action
real_structure: real finite-dimensional phase space
grading: A-orthogonal simultaneous spectral decomposition
action_owner: repository-construction -- supplied matrices are not source-selected
target: K1076 matrix action Hessian MAP-TYPE=evaluation
```

Define the `A`-self-adjoint operators

```text
X=A^-1 B,     Y=A^-1 C.
```

There is one `lambda`-independent `A`-orthonormal basis diagonalizing every
`lambda X+Y` if and only if `[X,Y]=0`. The forward implication is immediate.
For the reverse implication, conjugation by `A^(1/2)` turns `X,Y` into
commuting ordinary self-adjoint matrices, so the finite-dimensional simultaneous
spectral theorem applies and transports the basis back.

This criterion is load-bearing. An affine operator pencil does not imply
affine individually labelled frequency branches when its coefficient blocks do
not commute. The theorem is finite-dimensional: common domains, closures,
unbounded commutators, quotient degeneration and continuous spectrum remain
open in a functional application. The producer passes `8/8`; the hostile probe
rejects `9/9` criterion, control, scope and ownership mutations.

## Next condition

On the commuting horn, recover each branch's slope, intercept and
mass-to-speed ratio while separating normalization gauges.
