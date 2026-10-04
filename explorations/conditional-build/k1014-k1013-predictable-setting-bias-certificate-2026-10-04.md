---
title: "K1014 predictable setting-bias certificate"
status: active_research
doc_type: conditional_biased_input_bell_certificate
created: 2026-10-04
claim_ceiling: finite-sample local bound for known predictable CHSH input laws independent of hidden device state
manifest: lab/process/k1014-k1013-predictable-setting-bias-certificate.json
probe: tests/channel-swings/k1014_k1013_predictable_setting_bias_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1014 predictable setting-bias certificate

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact conditional local ceiling and martingale certificate for biased CHSH settings
carrier: event-ready binary trials with known predictable input laws pi_i LAYER=observed CHIRALITY=N/A
pairing: conditional setting probabilities and bounded-win concentration ON=repository_quantum_control
real_structure: four nonnegative input probabilities summing to one per trial
grading: bias-aware rejection of the declared local model class
action_owner: UNTYPED -- the input law and measurement independence are not GU owned
target: setting-randomness error budget MAP-TYPE=evaluation
```

A deterministic local CHSH strategy must lose at least one setting pair and
can choose a strategy that loses only one. For a known next-trial setting law
`pi_i(x,y)`, independent of the hidden device state conditional on history,
the exact conditional local win ceiling is therefore

```text
b_i = 1 - min_(x,y) pi_i(x,y).
```

Consequently

```text
sum_i (W_i-b_i) > sqrt(n log(1/alpha)/2)
```

rejects the local model at level `alpha`. If every pair has probability at
least `q`, the simpler sufficient form is

```text
w_hat > 1-q + sqrt(log(1/alpha)/(2n)).
```

At the K1013 ideal win rate, `q=0.24` and `alpha=1/20`, the sufficient integer
budget becomes `17475` total trials, compared with `4039` at uniform inputs.
The cost is not a GU prediction; it shows that even a one-point minimum-input
deficit must enter the statistical contract.

Known marginal frequencies alone do not prove measurement independence.
Hidden correlation between settings and devices, postselection and detector
semantics remain outside this theorem and outside current GU ownership.
