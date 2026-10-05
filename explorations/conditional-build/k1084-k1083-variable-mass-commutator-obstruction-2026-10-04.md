---
title: "K1084 variable-mass commutator obstruction"
status: active_research
doc_type: conditional_variable_coefficient_commutator_obstruction
created: 2026-10-04
claim_ceiling: exact smooth flat-torus obstruction for constant positive principal block and multiplication mass
manifest: lab/process/k1084-k1083-variable-mass-commutator-obstruction.json
probe: tests/channel-swings/k1084_k1083_variable_mass_commutator_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1084 variable-mass commutator obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> operator obstruction, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_OBSTRUCTION`.

```gu-typed-objects
result: a spatially varying positive mass block generically destroys the fixed Fourier/internal normal-mode premise
carrier: smooth sections of the trivial R^r bundle over T3 LAYER=observed CHIRALITY=N/A
pairing: positive L2 pairing with constant principal block B ON=candidate_action
real_structure: real smooth matrix coefficients
grading: differential order two, one and zero in the commutator
action_owner: repository-construction -- counterexample is not a GU Hessian
target: K1083 translation-invariant premise MAP-TYPE=evaluation
```

For `H0=-B Delta` with constant `B>0` and multiplication by `C(x)`, direct
Leibniz expansion gives

```text
[H0,C]f = (CB-BC) Delta f - B(Delta C)f
           - 2B sum_a (partial_a C)(partial_a f).
```

On a connected flat torus this commutator vanishes on all smooth sections iff
`C` is constant and `[B,C]=0`: the first-order principal coefficient forces
every derivative of `C` to vanish, then the second-order coefficient forces
the matrix commutator to vanish.

The uniformly positive pointwise-commuting example
`B=diag(1,2)`, `C(x)=diag(2+cos(x)/2,3)` still fires. At `x=pi/2` on
`f=(cos x,0)`, the first component of `[H0,C]f` is exactly `-1`. Thus
positivity and pointwise commutation do not license affine Fourier branches.
The producer passes `9/9`; the hostile probe rejects `10/10` identity,
witness, inference and scope mutations.

Variable principal matrices, curvature and boundary conditions require their
own commutator/domain calculation; this is not a global action no-go.
