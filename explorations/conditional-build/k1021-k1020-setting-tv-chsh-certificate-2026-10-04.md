---
title: "K1021 setting-source total-variation CHSH certificate"
status: active_research
doc_type: conditional_setting_source_certificate
created: 2026-10-04
claim_ceiling: sharp local ceiling from supplied conditional setting-source variation bounds only
manifest: lab/process/k1021-k1020-setting-tv-chsh-certificate.json
probe: tests/channel-swings/k1021_k1020_setting_tv_chsh_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1021 setting-source total-variation CHSH certificate

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: sharp total-variation correction to the predictable-input CHSH local ceiling
carrier: event-ready binary CHSH trials with conditional setting laws pi_i LAYER=observed CHIRALITY=N/A
pairing: total variation from the uniform four-pair law ON=repository_quantum_control
real_structure: real probability simplex with adapted past filtration
grading: exact conditional probability theorem
action_owner: UNTYPED -- the setting source and independence premise are not GU owned
target: memory-robust local ceiling MAP-TYPE=evaluation
```

Let `u=(1/4,1/4,1/4,1/4)` and suppose the setting-pair law on
trial `i`, conditioned on the past, obeys

```text
TV(pi_i,u) = (1/2) sum_j |pi_i(j)-1/4| <= epsilon_i.
```

The mass removed from any one coordinate is at most total variation, so
`min_j pi_i(j) >= max(0,1/4-epsilon_i)`. K1014's exact predictable-input
ceiling therefore gives

```text
b_i <= min(1,3/4+epsilon_i).
```

For `epsilon_i<=1/4`, this is sharp: the law
`(1/4-epsilon_i,1/4+epsilon_i,1/4,1/4)` has variation
`epsilon_i`, and a deterministic local strategy places its unique losing pair
on the depleted coordinate. With arbitrary inter-trial memory, the valid
sequential test is

```text
sum_i [W_i-(3/4+epsilon_i)] > sqrt(n log(1/alpha)/2).
```

This converts an audited conditional variation bound into a score correction.
It does not construct or certify the setting source, prove its independence
from the devices, establish locality, or produce a GU observable.
