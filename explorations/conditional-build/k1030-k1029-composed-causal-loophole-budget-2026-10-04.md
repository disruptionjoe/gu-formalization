---
title: "K1030 composed causal Bell loophole budget"
status: active_research
doc_type: conditional_composed_causal_bell_budget
created: 2026-10-04
claim_ceiling: model-based all-trials forecast after explicit detector, setting, causal-compromise and record allowances
manifest: lab/process/k1030-k1029-composed-causal-loophole-budget.json
probe: tests/channel-swings/k1030_k1029_composed_causal_loophole_budget_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1030 composed causal Bell loophole budget

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: composed all-trials detector, setting, causal-compromise, record and finite-shot budget
carrier: K1018 noisy-lossy event-ready CHSH trials with supplied operational allowances LAYER=observed CHIRALITY=N/A
pairing: recorded win frequency against corrected predictable local ceiling ON=repository_quantum_control
real_structure: real probability and deterministic audit budgets
grading: exact conditional composition plus imported-model shot forecast
action_owner: UNTYPED -- state, herald, settings, causal events, detectors and records are not GU owned
target: operational Bell certification interface MAP-TYPE=evaluation
```

K1021, K1028 and K1024 compose as

```text
w_hat_recorded > 3/4+epsilon+q(1/4-epsilon)+R/n
                 + sqrt(log(1/alpha)/(2n)).
```

At K1018's imported point
`p=1,V=2/5,eta=49/50,alpha=1/20`, take supplied bounds
`epsilon=q=R/n=1/1000`. The causally compromised fraction adds the sharp
penalty `0.000249`; the effective margin is `0.0064466140...`. The smallest
integer satisfying the stated Hoeffding--Azuma budget is

```text
n = 36,043 all-trials shots.
```

This is a forecast, not an empirical score. It assumes the imported loss
model and supplied setting, predictable pre-score causal-compromise indicators,
and record budgets. The native
packet still needs a GU-owned quotient and positive pairing, action-owned
preparation/generator, physical herald, fresh settings, commuting local
observables, measured two-way spacelike event records, detector response and
complete audited systematics.
