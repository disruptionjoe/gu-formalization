---
title: "K1172 sharp repair-allocation controls"
status: active_research
doc_type: exact_three_resource_sharpness_family
created: 2026-10-05
claim_ceiling: exact coordinate sharpness family; no source ownership or functional domain
manifest: lab/process/k1172-sharp-repair-allocation-controls.json
probe: tests/channel-swings/k1172_sharp_repair_allocation_controls_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1172 sharp repair-allocation controls

> **GU-COMPARATOR-ROUTING — scope before inference.** These controls show
> that K1171 is dimensionally sharp. They are not GU constructions.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp controls for every Hessian-gauge-constraint allocation
carrier: R12 LAYER=toy CHIRALITY=N/A
pairing: positive diagonal block plus a zero Hessian kernel ON=control-fixture
real_structure: ordinary real coordinates
grading: positive Hessian block, gauge radical and constrained kernel complement
action_owner: N/A -- controls only
target: resource-identity sharpness MAP-TYPE=quotient
```

For every nonnegative triple `(h,g,c)` with `h>=1` and `h+g+c=12`, take
`H` positive diagonal on the first `h` coordinates and zero on the rest.
Let `im d` span the next `g` kernel coordinates and let `Q` record the final
`c` kernel coordinates. Then

`rad(H restricted to ker Q)=im d`

and the quotient pairing is positive of dimension `h`. All 78 allocations
are realized, including constraint-heavy `(2,0,10)`, balanced `(4,3,5)` and
gauge-heavy `(2,10,0)` controls. Thus dimensions alone cannot prefer one
repair resource or strengthen K1171. Producer and hostile probe pass `10/10`
and `12/12`.
