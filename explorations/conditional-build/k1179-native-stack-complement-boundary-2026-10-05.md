---
title: "K1179 native stack complement boundary"
status: active_research
doc_type: exact_native_stack_complement_boundary
created: "2026-10-05"
claim_ceiling: strongest-favorable direct-sum ceiling; no common carrier or owned stack
manifest: lab/process/k1179-native-stack-complement-boundary.json
probe: tests/channel-swings/k1179_native_stack_complement_boundary_probe.py
target_claim: SC-ACT-06
---

# K1179 native stack complement boundary

> K1179 applies K1166's exact overlap law to the K1178 ledger. Named native
> objects do not earn additive rank until their complements are measured on
> one typed carrier.

For `K=ker H` and an ordered stack `Q_1,...,Q_m`,

```text
rank(Q_1,...,Q_m)|K
 = sum_j rank(Q_j | K intersect ker Q_1 intersect ... intersect ker Q_(j-1)).
```

Thus every new row pays only its sequential complement rank. A factor-through
row pays zero regardless of its name, target size, order or parameter count.

As an intentionally over-favorable ceiling, grant `650+915+1470+1571=4606`
with no overlap and full transport. K132 still lacks
`93766/93766/101930` directions. Actual overlap, type failure or transport
failure can only increase those residuals.

Admission now requires a common K132 carrier, source-owned coupling, causal
symbol, measured sequential complement ranks, `Qd=0`, and the K1150 functional
packet. The producer passes `12/12`; the hostile probe rejects `12/12`.
