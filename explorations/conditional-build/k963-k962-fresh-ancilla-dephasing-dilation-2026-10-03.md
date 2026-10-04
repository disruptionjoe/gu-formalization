---
title: "K963 K962 fresh-ancilla dephasing dilation"
status: active_research
doc_type: conditional_fresh_ancilla_dilation_result
created: 2026-10-03
claim_ceiling: exact collision-model construction with explicit freshness resource only
manifest: lab/process/k963-k962-fresh-ancilla-dephasing-dilation.json
probe: tests/channel-swings/k963_k962_fresh_ancilla_dephasing_dilation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K963 fresh-ancilla dephasing dilation

```gu-typed-objects
result: exact fresh-qubit collision dilation with coherence lambda^n and remote-marginal invariance
carrier: system qubit tensor a one-pass sequence of prepared qubit ancillas LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert adjoint, ancilla state and partial trace ON=repository_collision_model
real_structure: computational-basis conjugation with complex unitary phase
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction with supplied fresh ancillas, not Weinstein source or GU action
target: resource-backed contrary realization of K960 dephasing MAP-TYPE=evaluation
```

K963 constructs the strongest simple contrary model to K962. A system qubit
collides once with each fresh environment qubit in state `|0>` through
`U_theta=exp(-i theta Z_S tensor Y_E)`. Tracing that ancilla multiplies system
coherence by `lambda=cos(2 theta)`. Choosing
`theta=(1/2) arccos(lambda)` gives the exact K956 phase-damping channel, and
`n` independent fresh collisions give `lambda^n`. Because each collision is a
local trace-preserving operation, a remote marginal is unchanged.

This does not evade K962 with a finite closed reservoir. Unbounded time needs
an unbounded tape or an explicit reset/repreparation mechanism. Preparation,
partial trace, clocking and the probability semantics are imported resources,
not consequences of the unitary interaction and not GU-owned inputs.
