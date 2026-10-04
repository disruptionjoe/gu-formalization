---
title: "K1016 assigned no-click CHSH threshold"
status: active_research
doc_type: conditional_detector_efficiency_theorem
created: 2026-10-04
claim_ceiling: exact threshold for one supplied state, witness, loss and assignment model
manifest: lab/process/k1016-k1015-assigned-noclick-chsh-threshold.json
probe: tests/channel-swings/k1016_k1015_assigned_noclick_chsh_threshold_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1016 assigned no-click CHSH threshold

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact symmetric detector-efficiency threshold after fixed no-click assignment
carrier: event-ready binary CHSH trials with independent equal-efficiency local loss LAYER=observed CHIRALITY=N/A
pairing: ideal zero-marginal Bell expectation plus classical detector mixture ON=repository_quantum_control
real_structure: real correlator table and Bernoulli detection flags
grading: conditional exact theorem for one imported state/witness/loss model
action_owner: UNTYPED -- state, detectors, locality and trial protocol are not GU owned
target: all-trials detection completion MAP-TYPE=evaluation
```

K1015 forbids discarding no-clicks without analysis. A constructive completion
is to retain every event-ready trial and map every local no-click to `+1`.
Assume the maximally entangled CHSH optimum, zero ideal one-party marginals,
and independent setting-independent equal detector efficiency `eta`. Then

```text
E'_xy = eta^2 E_xy + (1-eta)^2,
S_eta = 2 sqrt(2) eta^2 + 2(1-eta)^2.
```

The single-detection terms vanish because the ideal marginals are zero. Exact
factorization gives

```text
S_eta > 2  iff  eta > 2/(1+sqrt(2)) = 0.8284271247...
```

At zero efficiency the fixed assignments saturate the local value two; at the
threshold the expression equals two; at unit efficiency it equals `2sqrt(2)`.
This is not an optimal threshold over nonmaximally entangled states, other
inequalities, correlated losses or setting-dependent detector behavior. It
constructs no GU detector, state, action or empirical result.
