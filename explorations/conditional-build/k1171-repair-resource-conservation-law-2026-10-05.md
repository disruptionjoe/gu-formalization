---
title: "K1171 repair-resource conservation law"
status: active_research
doc_type: exact_radical_capture_resource_identity
created: 2026-10-05
claim_ceiling: exact finite-dimensional necessity; no source packet or functional realization
manifest: lab/process/k1171-repair-resource-conservation-law.json
probe: tests/channel-swings/k1171_repair_resource_conservation_law_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1171 repair-resource conservation law

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a general
> finite-dimensional theorem applied later to the source-native K132 symbols.
> It does not manufacture a new Hessian, gauge symmetry or boundary map.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact Hessian-gauge-constraint resource identity
carrier: finite field space V with symmetric Hessian H LAYER=toy CHIRALITY=N/A
pairing: H restricted to a supplied constrained kernel ON=typed-future-candidate
real_structure: finite real vector spaces
grading: Hessian image, gauge image and actual constraint image on ker H
action_owner: N/A -- theorem only
target: radical-capture necessity MAP-TYPE=evaluation
```

Let `H:V->V*` be symmetric, `d:G->V` satisfy `Hd=0`, and `Q:V->W`
satisfy `Qd=0`. If

`rad(H restricted to ker Q)=im d`,

then K1152 gives

`c := rank(Q restricted to ker H)=dim ker H-rank d`.

Since `dim ker H=dim V-rank H`, every successful packet obeys the exact
resource identity

`rank H + rank d + c = dim V`.                                (1)

Consequently a ceiling `c<=C` implies
`rank H+rank d+C>=dim V`. Relative to a frozen baseline `(h0,g0,C0)`,
the added Hessian, genuinely independent gauge and genuinely independent
constraint ranks must sum to at least `dim V-h0-g0-C0`.

The seven-dimensional control uses ranks `(2,2,3)` and has a positive
two-dimensional quotient. Equation (1) counts actual images, not target
dimensions, formal parameter names or factor-through descendants. Producer
and hostile probe pass `11/11` and `11/11`.
