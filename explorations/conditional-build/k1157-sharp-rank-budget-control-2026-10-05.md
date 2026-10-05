---
title: "K1157 sharp rank-budget control"
status: active_research
doc_type: positive_cohomology_rank_budget_sharpness
created: 2026-10-05
claim_ceiling: exact finite-dimensional sharpness family; no source ownership or functional domain
manifest: lab/process/k1157-sharp-rank-budget-control.json
probe: tests/channel-swings/k1157_sharp_rank_budget_control_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1157 sharp rank-budget control

> **GU-COMPARATOR-ROUTING — scope before inference.** This exact control
> proves sharpness of K1156. It is not a GU constraint construction.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp family for every gauge-versus-constraint rank allocation
carrier: R8 with six-dimensional Hessian kernel LAYER=toy CHIRALITY=N/A
pairing: H=diag(0^6,2,3) ON=finite-control-carrier
real_structure: real finite coefficient space
grading: variable gauge image inside fixed Hessian kernel
action_owner: comparator
target: positive nonzero constrained quotient MAP-TYPE=quotient
```

Take `H=diag(0^6,2,3)`. For every `r=0,...,6`, let the gauge image be
`span(e1,...,er)` and let `Q` record the remaining kernel coordinates
`e_(r+1),...,e6`. Then

```text
rank d = r,  dim W = 6-r,  rank d + dim W = dim ker H = 6,
rad(H|ker Q)=im d,
dim((ker Q/im d))=2,
```

and the quotient pairing is positive. Every allocation in K1156's budget is
therefore attainable. No stronger inequality follows from dimensions alone;
source ownership and every functional gate remain separate. Producer and
probe pass `12/12` and `12/12`.
