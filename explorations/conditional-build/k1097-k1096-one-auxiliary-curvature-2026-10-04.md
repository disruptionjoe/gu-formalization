---
title: "K1097 one-auxiliary reduced curvature"
status: active_research
doc_type: conditional_one_auxiliary_curvature
created: 2026-10-04
claim_ceiling: exact monotonicity, concavity and threshold for one constant-coupling auxiliary Schur branch
manifest: lab/process/k1097-k1096-one-auxiliary-curvature.json
probe: tests/channel-swings/k1097_k1096_one_auxiliary_curvature_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1097 one-auxiliary reduced curvature

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> reduced-branch theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_REDUCED_BRANCH_LAW`.

```gu-typed-objects
result: one positive auxiliary mode produces a strictly increasing concave physical branch
carrier: one physical plus one auxiliary real mode LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1096 non-affine horn MAP-TYPE=evaluation
```

For positive auxiliary denominator and constant nonzero mixing, write

```text
S(lambda)=alpha lambda+beta-g^2/(lambda+d),
lambda>-d, alpha>0, d>0, g!=0.
```

Then

```text
S'(lambda)=alpha+g^2/(lambda+d)^2 > 0,
S''(lambda)=-2g^2/(lambda+d)^3 < 0.
```

The reduction therefore preserves order but introduces strict concavity. It
cannot be absorbed into a new intercept and slope on an interval.

For the exact fixture `alpha=2`, `beta=3`, `g^2=1`, `d=2`, the zero equation
is `(2 lambda+3)(lambda+2)-1=0`, with roots `-5/2` and `-1`. Only `-1`
lies in the domain `lambda>-2`, and the branch is positive for every
`lambda>=0`. At modes `0,1,2` the values are `5/2,14/3,27/4`; their second
finite difference is `-1/12`.

The producer passes `13/13`; the hostile probe rejects `12/12` mutations.
These are exact conditional shape constraints, not a selected GU coefficient,
functional domain or physical spectrum.
