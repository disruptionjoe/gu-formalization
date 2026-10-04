---
title: "K1025 composed Bell loophole budget"
status: active_research
doc_type: conditional_composed_bell_budget
created: 2026-10-04
claim_ceiling: model-based finite-shot forecast after explicit detector, setting-source and record-integrity allowances
manifest: lab/process/k1025-k1024-composed-loophole-budget.json
probe: tests/channel-swings/k1025_k1024_composed_loophole_budget_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1025 composed Bell loophole budget

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: composed all-trials detector, setting-source, record-error and finite-shot budget
carrier: K1018 noisy-lossy event-ready CHSH trials with supplied operational allowances LAYER=observed CHIRALITY=N/A
pairing: recorded win frequency against corrected predictable local ceiling ON=repository_quantum_control
real_structure: real probability and deterministic error budgets
grading: exact conditional composition plus imported-model shot forecast
action_owner: UNTYPED -- state, herald, settings, locality, detectors and records are not GU owned
target: operational Bell certification interface MAP-TYPE=evaluation
```

K1021 and K1024 compose with K1020 as

```text
w_hat_recorded > 3/4 + epsilon + R/n
                 + sqrt(log(1/alpha)/(2n)).
```

At K1018's imported point
`p=1,V=2/5,eta=49/50,alpha=1/20`, take the supplied bounds
`epsilon=1/1000` and `R/n<=1/1000`. The independent-loss model predicts
`w=0.7586956140...`, leaving effective margin `0.0066956140...`. The smallest
integer satisfying the stated Hoeffding--Azuma budget is

```text
n = 33,412 all-trials shots.
```

The feasibility condition is visibly `w>3/4+epsilon+R/n`; operational
allowances can consume the entire nominal violation before sampling error is
considered. The empirical inequality may consume audited bounds directly, but
the number 33,412 is only a forecast under imported independent loss,
setting-variation and record-rate assumptions.

The remaining native packet is unchanged in kind but sharper in content: a
GU-owned positive state/effect pairing and action-owned preparation/generator;
a physical pre-settings herald; a fresh independent setting source;
commuting local observables and spacelike locality; detector response; and a
complete audited systematic budget. No empirical score or GU credit follows.
