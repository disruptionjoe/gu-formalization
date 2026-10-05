---
title: "K1124 acyclic positivity control"
status: active_research
doc_type: typed_acyclic_cohomology_control
created: 2026-10-05
claim_ceiling: distinct-carrier homological control; no transfer to I1B
manifest: lab/process/k1124-k590-acyclic-positivity-control.json
probe: tests/channel-swings/k1124_k590_acyclic_positivity_control_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1124 acyclic positivity control

> **GU-COMPARATOR-ROUTING — scope before inference.** This is an internal typed
> control, not a transfer between K77 and I1B carriers. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: acyclic-cohomology positivity control
carrier: K590 factorized corrected carrier complex LAYER=toy CHIRALITY=N/A
pairing: arbitrary descended form on homology ON=zero_cohomology
real_structure: K590 finite real factorized carrier
grading: degree two, one and zero with dimensions 10752,46592,35840
action_owner: repository-construction -- K590 factorized finite action-coupled complex only
target: physical-state interpretation MAP-TYPE=evaluation
```

K590 has homology dimensions `(0,0,0)`. Every form on zero cohomology is
vacuously positive, but zero cohomology contains no nonzero state, effect or
observable. Exactness alone therefore does not satisfy the physical request
for a positive, nontrivial cohomology.

This is a deliberately separate control. K590 is a K77 factorized finite
homogeneous-orbit complex and is not the K128/K129 I1B causal-symbol carrier.
It neither solves nor obstructs every functional I1B BV/BFV completion. The
producer passes `9/9`; the hostile probe rejects `9/9` mutations.
