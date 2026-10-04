---
title: "K1031 positive quotient descent criterion"
status: active_research
doc_type: conditional_positive_quotient_descent
created: 2026-10-04
claim_ceiling: exact finite-dimensional descent criterion for a positive quotient, observable and effect
manifest: lab/process/k1031-k1030-positive-quotient-descent.json
probe: tests/channel-swings/k1031_k1030_positive_quotient_descent_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1031 positive quotient descent criterion

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact positive-quotient, observable and effect descent criterion
carrier: finite-dimensional complex carrier V with positive-semidefinite Hermitian form M LAYER=toy CHIRALITY=N/A
pairing: quotient pairing <[x],[y]>=x*My on V/ker(M) ON=repository_quantum_control
real_structure: complex carrier with Hermitian adjoint
grading: exact finite-dimensional theorem with firing representative-dependence control
action_owner: UNTYPED -- neither M nor the quotient is selected by a GU action
target: physical state/effect interface MAP-TYPE=quotient
```

Let `M=M*>=0` on a finite-dimensional complex carrier `V` and let
`N=ker(M)`. Then

```text
<[x],[y]> = x* M y
```

is well defined and positive definite on `V/N`. A linear map `A` descends to
that quotient exactly when `A(N) subset N`. Its descended operator is
self-adjoint when `A* M=M A`, and it is an effect when the Hermitian-form
inequality `0<=M A<=M` also holds.

The exact control uses `M=diag(1,2,0)`. Its quotient has dimension two and
the diagonal effect with quotient eigenvalues `(1,1/2)` passes. The bad map
`A e_3=e_1` fails descent: shifting a representative by the null vector
`e_3` changes the output class.

This theorem supplies a gate, not a GU quotient. The source action asserted
by SC-ACT-01 does not by itself select `M`, prove that its radical is precisely
gauge, or show that physical effects preserve it. Those are native inputs a
candidate action must still own.
