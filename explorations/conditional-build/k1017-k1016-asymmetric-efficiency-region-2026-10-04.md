---
title: "K1017 asymmetric efficiency region"
status: active_research
doc_type: conditional_detector_efficiency_surface
created: 2026-10-04
claim_ceiling: exact unequal-efficiency surface for the K1016 model only
manifest: lab/process/k1017-k1016-asymmetric-efficiency-region.json
probe: tests/channel-swings/k1017_k1016_asymmetric_efficiency_region_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1017 asymmetric efficiency region

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact asymmetric detector-efficiency CHSH region
carrier: K1016 event-ready Bell trials with local efficiencies eta_A and eta_B LAYER=observed CHIRALITY=N/A
pairing: zero-marginal Bell expectation plus fixed no-click assignments ON=repository_quantum_control
real_structure: real two-parameter efficiency square
grading: conditional exact region inside the imported independent-loss model
action_owner: UNTYPED -- local detector responses and efficiencies are not GU owned
target: asymmetric all-trials detection completion MAP-TYPE=evaluation
```

With independent setting-independent local efficiencies `eta_A,eta_B`, fixed
`+1` no-click assignment gives

```text
E'_xy = eta_A eta_B E_xy + (1-eta_A)(1-eta_B),
S = 2[sqrt(2) eta_A eta_B + (1-eta_A)(1-eta_B)].
```

Thus violation is exact when

```text
sqrt(2) eta_A eta_B + (1-eta_A)(1-eta_B) > 1.
```

The symmetric slice recovers K1016. If Alice is perfect, Bob needs
`eta_B>1/sqrt(2)`. This is a detector-design decision surface, not a proof
that an apparatus has independent, setting-independent loss. Correlated or
hidden-state-dependent loss can invalidate the forecast even though counting
every trial preserves the empirical CHSH test itself.
