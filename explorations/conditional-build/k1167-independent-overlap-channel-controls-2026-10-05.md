---
title: "K1167 independent and overlapping channel controls"
status: active_research
doc_type: exact_stacked_channel_positive_and_negative_controls
created: 2026-10-05
claim_ceiling: exact coordinate controls; no classification of the actual epsilon-channel overlap
manifest: lab/process/k1167-independent-overlap-channel-controls.json
probe: tests/channel-swings/k1167_independent_overlap_channel_controls_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1167 independent and overlapping channel controls

> **GU-COMPARATOR-ROUTING — scope before inference.** These coordinate
> fixtures show every overlap regime is possible. They do not decide the
> relation between the source moment map and invariant lock.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp independent, partial-overlap and duplicate channel fixtures
carrier: real coordinate space R6 LAYER=toy CHIRALITY=N/A
pairing: standard coordinate pairing ON=control-fixture
real_structure: ordinary real coordinates
grading: first channel, second channel, overlap defect
action_owner: N/A -- controls only
target: stacked-rank sharpness MAP-TYPE=evaluation
```

Fix a rank-two first channel on the first two coordinates. Three rank-three
second channels then realize:

- full independence: stacked rank five and `delta=0`;
- one shared direction: stacked rank four and `delta=1`; and
- complete duplication of a rank-two second channel: stacked rank two and
  `delta=2`.

Thus additive target dimensions are attained only after independence is proved
on the actual kernel. Two names, two constructions, or two output lists do not
establish it. The favorable K132 application may grant `delta=0` as a ceiling,
but must not report that grant as source-derived. Producer and hostile probe
pass `7/7` and `10/10`.
