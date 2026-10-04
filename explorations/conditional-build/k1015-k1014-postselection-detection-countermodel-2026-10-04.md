---
title: "K1015 postselection detection countermodel"
status: active_research
doc_type: conditional_local_detection_counterexample
created: 2026-10-04
claim_ceiling: explicit low-efficiency local postselection counterexample only
manifest: lab/process/k1015-k1014-postselection-detection-countermodel.json
probe: tests/channel-swings/k1015_k1014_postselection_detection_countermodel_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1015 postselection detection countermodel

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: fully local hidden-variable model with perfect CHSH wins after joint-detection postselection
carrier: four hidden-variable values and local setting-dependent detection flags LAYER=observed CHIRALITY=N/A
pairing: classical conditional frequency on retained trials ON=repository_quantum_control
real_structure: finite probability space lambda=(u,v) in {0,1}^2
grading: counterexample to unqualified no-click discarding
action_owner: UNTYPED -- detector response and event-ready outcome assignment are not GU owned
target: detection/postselection obligation MAP-TYPE=evaluation
```

Let `lambda=(u,v)` be uniform on `{0,1}^2`. Alice detects iff her local setting
equals `u`; Bob detects iff his local setting equals `v`:

```text
D_A(x,lambda)=1[x=u],       D_B(y,lambda)=1[y=v].
```

Choose local outputs `a=0` and, on Bob's detected setting, `b=u*v` (other
local outputs may be fixed arbitrarily). For every input pair `(x,y)`, joint
detection occurs only when `lambda=(x,y)`, with probability `1/4`, and the
retained outputs obey

```text
a xor b = x*y.
```

Each side detects with probability `1/2`; joint detection is `1/4`; the
postselected win rate is exactly one. Every response and detection flag uses
only the local setting and shared hidden variable, so the model is local.

Therefore K1013/K1014 require an event-ready trial definition with no
unaccounted discarding, or a separately proved detection analysis. This
low-efficiency construction proves no optimal efficiency threshold and says
nothing empirical about an actual apparatus. GU still owns no detector model,
locality theorem or measurement protocol, and no protected verdict moves.
