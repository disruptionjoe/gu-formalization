---
title: "K1162 independent symbol family control"
status: active_research
doc_type: independent_symbol_rank_growth_control
created: 2026-10-05
claim_ceiling: exact finite positive control; no source ownership or differential complex
manifest: lab/process/k1162-independent-symbol-family-control.json
probe: tests/channel-swings/k1162_independent_symbol_family_control_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1162 independent symbol family control

> **GU-COMPARATOR-ROUTING — scope before inference.** This control shows
> what a genuinely new symbol can do. It is not a GU constraint construction.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp independent-versus-shared-factor rank control
carrier: R8 finite control carrier LAYER=toy CHIRALITY=N/A
pairing: standard positive form on the surviving quotient ON=finite-control-carrier
real_structure: real finite coefficient space
grading: independent coordinate symbols versus descendants of one coordinate
action_owner: comparator
target: nonzero positive quotient after independent constraints MAP-TYPE=quotient
```

Let `q_j:R8->R` record coordinate `j`. Stacking `q_1,...,q_m` has rank `m`
for every `m=1,...,6` and leaves a positive quotient of dimension `8-m`.
By contrast, arbitrarily many scalar descendants of `q_1` remain rank one.

Thus K1161 is a factorization boundary, not a general prohibition on rank
growth. A source-owned field-valued operator can add rank only by supplying
new symbol directions, not by relabeling derivatives of one finite channel.
Producer and probe pass `10/10` and `11/11`.
