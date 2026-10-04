---
title: "K983 K982 system-only nonidentifiability"
status: active_research
doc_type: conditional_endpoint_nonidentifiability_result
created: 2026-10-03
claim_ceiling: endpoint operational equivalence for equal reduced channels only
manifest: lab/process/k983-k982-system-only-nonidentifiability.json
probe: tests/channel-swings/k983_k982_system_only_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K983 system-only endpoint nonidentifiability

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: equal reduced channels are indistinguishable by every one-time system-only endpoint experiment
carrier: arbitrary system plus optional inert test ancilla LAYER=observed CHIRALITY=N/A
pairing: arbitrary supplied positive preparation/effect pairing ON=reduced_channel_endpoint
real_structure: inherited from the tested state/effect space
grading: degree-zero operational probabilities
action_owner: N/A -- theorem compares models only after their reduced channel families agree
target: empirical identifiability boundary for K980's microscopic horns MAP-TYPE=evaluation
```

If two microscopic models induce the same reduced channel `D_t`, then for
every state `rho`, effect `E`, and inert ancilla,

```text
tr[E (D_t tensor id)(rho)]
```

is identical. Their reduced-channel diamond distance is zero. K981 therefore
cannot be selected over another exact realization by endpoint system
tomography, Bell-assisted channel tomography, interference visibility or the
K956/K957 endpoint anchors alone.

This theorem is deliberately scoped. Equality of one-time channel families
does not by itself assert equality of arbitrary multi-time process tensors.
The consequence needed here is narrower: a microscopic-horn holdout must
cross the reduced-channel equivalence class through an environment record,
clock record, multi-time intervention sensitive to memory, or another
action-specific observable.
