---
title: "K1189 changed-parent cancellation cost"
status: active_research
doc_type: corrected_changed_parent_cancellation_cost
created: "2026-10-05"
claim_ceiling: exact auxiliary restriction cost; no replacement parent is constructed or source-owned
manifest: lab/process/k1189-changed-parent-cancellation-cost.json
probe: tests/channel-swings/k1189_changed_parent_cancellation_cost_probe.py
target_claim: SC-ACT-06
---

# K1189 changed-parent cancellation cost

> **GU-COMPARATOR-ROUTING — scope before inference.** This preserves K891's
> algebra only as a changed-parent auxiliary condition after K1127/K1129.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `CORRECTION_PROPAGATION`.

```gu-typed-objects
result: exact restriction cost for making the full auxiliary radial carrier Hessian-null
carrier: K887 frozen nonnull radial slice LAYER=source-print+toy BRIDGE=changed_parent_condition CHIRALITY=N/A
pairing: changed Hessian H'=H+C ON=auxiliary_radial_image
real_structure: real SO(6)xSO(7)-equivariant nonnull symbol
grading: radial parameters --G--> connection tangent --(H+C)--> Euler target
action_owner: N/A -- C and the replacement stationary parent are unsupplied
target: SC-ACT-06 necessary changed-parent cost MAP-TYPE=evaluation
```

To make the full radial image Hessian-null for a changed parent `H'=H+C`, one
must have

```text
(H+C)G=0, hence CG=-HG.
```

K887 gives `rank(HG)=8191`, so every such completion has exact restriction
rank `rank(CG)=8191`; any smaller restriction cannot work. The raw response
already annihilates this auxiliary carrier, so the missing obligation is the
Hessian cancellation, not another response cancellation.

K1127/K1129 prevent the old inference from returning: this theorem neither
constructs `C` nor attributes it to the source action, and a changed parent
must replay every K1150 algebraic and functional gate. The producer passes
`16/16`; the hostile probe rejects `12/12` mutations. No protected status
moves.
