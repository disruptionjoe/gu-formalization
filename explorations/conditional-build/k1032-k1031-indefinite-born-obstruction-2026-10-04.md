---
title: "K1032 indefinite Born-pairing obstruction"
status: active_research
doc_type: conditional_indefinite_born_obstruction
created: 2026-10-04
claim_ceiling: necessary positivity obstruction for a mixed-sign full carrier, preserving positive subquotient repairs
manifest: lab/process/k1032-k1031-indefinite-born-obstruction.json
probe: tests/channel-swings/k1032_k1031_indefinite_born_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1032 indefinite Born-pairing obstruction

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: mixed-sign full-carrier obstruction to a Born probability pairing
carrier: finite-dimensional complex carrier with nondegenerate Hermitian form of inertia (p,q), p,q>0 LAYER=toy CHIRALITY=N/A
pairing: supplied indefinite Hermitian form ON=repository_quantum_control
real_structure: complex carrier with congruence-invariant Hermitian inertia
grading: exact necessary obstruction with explicit positive and negative controls
action_owner: UNTYPED -- no invariant positive sector or quotient is source-selected
target: physical state/effect interface MAP-TYPE=not-a-map
```

A nondegenerate Hermitian form of inertia `(p,q)` with both `p,q>0` cannot be
a positive probability pairing on its full carrier. Sylvester inertia is
unchanged by invertible congruence, and the exact `diag(1,-1)` control has one
vector of norm `+1` and another of norm `-1`.

The conclusion is deliberately narrow. It does not exclude an invariant
positive subspace, nor K1031's positive-semidefinite form followed by quotient
of its exact radical. Either repair is extra physical structure: the candidate
must select it and prove that its generator and effects preserve it.

SC-META-53 remains `UNCERTAIN`: the source says the unbounded-spectrum problem
is not known and proposes maximal-compact shielding. SC-ACT-01 remains
`ASSERTS` for the classical first-order action. K1032 neither refutes those
source claims nor upgrades shielding into a positive physical quotient.
