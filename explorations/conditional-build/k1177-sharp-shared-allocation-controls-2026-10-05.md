---
title: "K1177 sharp shared allocation controls"
status: active_research
doc_type: exact_shared_allocation_sharpness_controls
created: "2026-10-05"
claim_ceiling: exact abstract sharpness controls; no GU source construction
manifest: lab/process/k1177-sharp-shared-allocation-controls.json
probe: tests/channel-swings/k1177_sharp_shared_allocation_controls_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1177 sharp shared allocation controls

> K1177 proves the K1176 shared ceiling cannot be strengthened by dimensions
> alone. It does not choose a physical repair resource.

For every nonnegative triple `(h,g,c)` with `h+g+c=9`, split
`V=V_H direct-sum V_d direct-sum V_Q` with the stated dimensions. Put a
positive identity Hessian on `V_H`, inject the gauge map onto `V_d`, and let
`Q` be identity on `V_Q` and zero elsewhere. Then

```text
Hd=0,  Qd=0,
rad(H|ker Q)=im d,
rank H + rank d + rank(Q|ker H) = 9.
```

There are `binomial(11,2)=55` allocations, including all three pure axes and
the balanced `(3,3,3)` split. Every point on the shared-budget face therefore
has an exact positive coordinate control. Preference among changed-parent,
gauge and constraint repair must come from source ownership, coupling,
closure, propagation or another non-dimensional fact.

The producer passes `11/11` controls and the hostile probe rejects `11/11`
mutations. No protected claim moves.
