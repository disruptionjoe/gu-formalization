---
title: "K1098 multi-auxiliary Stieltjes branch law"
status: active_research
doc_type: conditional_multi_auxiliary_stieltjes_law
created: 2026-10-04
claim_ceiling: exact finite diagonal multi-auxiliary Schur law and strict-concavity criterion
manifest: lab/process/k1098-k1097-multi-auxiliary-stieltjes.json
probe: tests/channel-swings/k1098_k1097_multi_auxiliary_stieltjes_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1098 multi-auxiliary Stieltjes branch law

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> auxiliary-sector theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_STIELTJES_REDUCTION`.

```gu-typed-objects
result: positive diagonal auxiliary elimination gives an affine branch minus a Stieltjes sum
carrier: one physical plus finitely many auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1097 one-auxiliary law MAP-TYPE=evaluation
```

Take

```text
A(lambda)=alpha lambda+beta,
D(lambda)=diag(lambda+d_i),
B=(b_i),
w_i=b_i^2>=0.
```

On the common positive domain `lambda>-min_i d_i` with every `d_i>0`, the
physical Schur branch is

```text
S(lambda)=alpha lambda+beta-sum_i w_i/(lambda+d_i).
```

Its first two derivatives are

```text
S'=alpha+sum_i w_i/(lambda+d_i)^2,
S''=-2 sum_i w_i/(lambda+d_i)^3.
```

Thus `S` is strictly concave exactly when at least one coupling survives, and
within this constant-coupling diagonal class it is affine exactly when every
`w_i` vanishes. The correction
`R=sum_i w_i/(lambda+d_i)` is completely monotone, so higher derivative signs
are fixed as well.

The fixture `alpha=2`, `beta=5`, weights `(1,4)` and shifts `(1,3)` gives
values `8/3,11/2,118/15` at `lambda=0,1,2`. The producer passes `13/13`; the
hostile probe rejects `12/12` mutations. The theorem does not identify a GU
auxiliary sector or extend automatically to noncommuting functional blocks.
