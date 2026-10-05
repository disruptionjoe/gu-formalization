---
title: "K1102 four-mode one-auxiliary identification"
status: active_research
doc_type: conditional_four_mode_one_auxiliary_identification
created: 2026-10-05
claim_ceiling: exact recovery of a one-auxiliary affine-minus-pole branch from four distinct modes
manifest: lab/process/k1102-k1101-four-mode-one-auxiliary-identification.json
probe: tests/channel-swings/k1102_k1101_four_mode_one_auxiliary_identification_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1102 four-mode one-auxiliary identification

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> one-pole inverse theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_ONE_AUXILIARY_INVERSE`.

```gu-typed-objects
result: four exact modes identify one positive auxiliary pole and the affine branch
carrier: one physical plus one auxiliary real mode LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric one-auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1099 three-mode alias MAP-TYPE=evaluation
```

Let

```text
S(x)=alpha x+beta-w/(x+d),  w>0,
```

and take four distinct ordered modes `x_0<x_1<x_2<x_3`. Define

```text
q_0=-S[x_0,x_1,x_2],
q_1=-S[x_1,x_2,x_3].
```

Both are positive, and cancellation of the common middle factors gives

```text
r=q_0/q_1=(x_3+d)/(x_0+d),
d=(x_3-r x_0)/(r-1).
```

Then

```text
w=q_0 prod_{j=0}^2(x_j+d),
alpha x+beta=S(x)+w/(x+d),
```

so the remaining two affine coefficients follow from any two samples. Thus
four exact modes identify the complete one-auxiliary branch.

For K1099's one-auxiliary alias on modes `0,1,2,3`, `q_0=7/30`,
`q_1=7/120`, and `r=4`, recovering

```text
d=1, w=7/5, alpha=32/15, beta=61/15.
```

The K1098 two-auxiliary fixture has fourth value `121/12`; the alias predicts
`607/60`. The exact original-minus-alias residual is `-1/30`, so the fourth
mode rejects the three-mode alias without identifying a general unbounded
hidden sector.

The producer passes `10/10`; the hostile probe rejects `12/12` mutations.
Physical use still requires an independently owned one-auxiliary bound,
prepared modes, an error model, a dimensional ruler and a detector record.
