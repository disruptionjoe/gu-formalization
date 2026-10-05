---
title: "K1099 three-mode auxiliary-mixing witness"
status: active_research
doc_type: conditional_three_mode_mixing_witness
created: 2026-10-04
claim_ceiling: exact three-mode divided-difference discriminator and finite-data non-identifiability boundary for the diagonal Stieltjes class
manifest: lab/process/k1099-k1098-three-mode-mixing-witness.json
probe: tests/channel-swings/k1099_k1098_three_mode_mixing_witness_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1099 three-mode auxiliary-mixing witness

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> three-mode classifier, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_MODE_CLASSIFIER`.

```gu-typed-objects
result: three exact modes detect nonzero positive constant auxiliary mixing inside the K1098 class
carrier: one physical plus finite diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian or apparatus
target: K1098 reduced branch MAP-TYPE=evaluation
```

For three ordered modes `x0<x1<x2` in the positive auxiliary domain, the
second divided difference of the K1098 branch is

```text
S[x0,x1,x2]
  = -sum_i w_i/((x0+d_i)(x1+d_i)(x2+d_i)).
```

It is strictly negative exactly when at least one positive weight is nonzero.
For K1098's modes `0,1,2`, the ordinary second difference is `-7/15`, hence
the second divided difference is `-7/30`.

This is a discriminator, not a full inverse solution. The same three values
`8/3,11/2,118/15` are produced by a one-auxiliary model with

```text
d=1, w=7/5, alpha=32/15, beta=61/15.
```

Three exact modes therefore detect mixing within the frozen positive diagonal
class but do not identify auxiliary multiplicity, shifts or weights. A zero
witness excludes positive constant mixing only after that model class and the
exact sample values are independently owned.

The producer passes `11/11`; the hostile probe rejects `11/11` mutations.
Physical use still requires prepared modes, an error model, a dimensional
ruler, a detector record and a source/action-owned reduced Hessian.
