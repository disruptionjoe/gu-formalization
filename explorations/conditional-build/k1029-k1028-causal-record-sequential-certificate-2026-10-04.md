---
title: "K1029 causal-record sequential Bell certificate"
status: active_research
doc_type: conditional_causal_record_certificate
created: 2026-10-04
claim_ceiling: memory-robust Bell certificate from supplied setting, locality-compromise and record-error bounds
manifest: lab/process/k1029-k1028-causal-record-sequential-certificate.json
probe: tests/channel-swings/k1029_k1028_causal_record_sequential_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1029 causal-record sequential Bell certificate

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: composed setting, causal-compromise, record and finite-shot Bell threshold
carrier: event-ready all-trials CHSH-game sequence with adapted audit bounds LAYER=observed CHIRALITY=N/A
pairing: recorded win frequency against a corrected predictable local ceiling ON=repository_quantum_control
real_structure: real conditional probabilities and deterministic error budgets
grading: exact pathwise composition plus Hoeffding-Azuma tail
action_owner: UNTYPED -- settings, causal records and record audit are not GU owned
target: sequential rejection threshold MAP-TYPE=evaluation
```

Let K1021 give the good-trial ceiling
`b=min(1,3/4+epsilon)`. If predictable indicators `c_i`, fixed before `W_i`,
mark trials lacking the K1027 certificate with `sum_i c_i <= qn`, and at most
`R` recorded wins differ from truth, then arbitrary inter-trial device memory
is allowed by

```text
w_hat_recorded > b+q(1-b)+R/n
                 + sqrt(log(1/alpha)/(2n)).
```

The pathwise form is
`sum E[W_i|past] <= sum b_i + sum c_i(1-b_i)`, so the result does not assume
iid devices. The statistical theorem consumes trial-level bounds on setting
variation, pre-score causal compromise and record corruption. It does not
estimate any of them from data or construct their apparatus; post-selecting
the compromised set after seeing trial scores is outside scope.
