---
title: "K1092 Ward identity insufficiency counterexample"
status: active_research
doc_type: conditional_ward_insufficiency
created: 2026-10-04
claim_ceiling: exact positive finite counterexample showing gauge Ward annihilation does not imply harmonic-sector invariance
manifest: lab/process/k1092-k1091-ward-insufficiency.json
probe: tests/channel-swings/k1092_k1091_ward_insufficiency_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1092 Ward identity insufficiency counterexample

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> finite counterexample, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_COUNTEREXAMPLE`.

```gu-typed-objects
result: the linear Ward identity kills the gauge image but need not preserve physical harmonic representatives
carrier: R --d0--> R3 --d1--> R with d0=(1,0,0)^T and d1=(0,0,1) LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_gauge_hessian
real_structure: real finite complex
grading: gauge e1, harmonic e2 and coexact e3 sectors
action_owner: repository-construction -- no GU stationary action
target: K1091 harmonic-invariance criterion MAP-TYPE=evaluation
```

On K1091's complex take

```text
L = [[0,0,0],[0,2,1],[0,1,2]].
```

This symmetric Hessian is positive semidefinite with eigenvalues `0,1,3`, and
it obeys the linear gauge Ward identity `L d0=0`. Nevertheless

```text
L e2 = 2 e2 + e3,
d1 L e2 = 1,
[L,P_H] != 0.
```

Thus gauge annihilation controls only `im(d0)`. It does not prevent mixing of
the harmonic carrier with `im(d1*)`, and it does not by itself define a
physical cohomology spectrum. The raw compression `P_H L P_H=2P_H` is an
algebraic compression, not the restriction of the original equations to an
invariant subspace.

The producer passes `10/10`; the hostile probe rejects `10/10` positivity,
Ward, spill, commutator, inference and ownership mutations. The counterexample
does not refute SC-ACT-01/02/06; it isolates one additional test their future
functional complex must pass.
