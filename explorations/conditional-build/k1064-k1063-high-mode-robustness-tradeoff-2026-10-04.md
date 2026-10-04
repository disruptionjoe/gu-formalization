---
title: "K1064 high-mode robustness tradeoff"
status: active_research
doc_type: conditional_fourth_mode_design_limit
created: 2026-10-04
claim_ceiling: analytic high-fourth-mode robustness limit and finite checked design fixtures for the supplied horns; no preparation or detector ownership
manifest: lab/process/k1064-k1063-high-mode-robustness-tradeoff.json
probe: tests/channel-swings/k1064_k1063_high_mode_robustness_tradeoff_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1064 high-mode robustness tradeoff

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> apparatus-design result, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: higher fourth prepared modes trade preparation range for improved quadratic-horn error tolerance
carrier: fixed lambda={3,8,15} plus lambda_n=n(n+2) LAYER=observed CHIRALITY=N/A
pairing: l1-normalized residual contrasts ON=repository_owned_candidate_holdout
real_structure: real positive dispersion frequencies
grading: analytic asymptotic limit plus finite verified fixtures; no global monotonic theorem
action_owner: repository-construction -- mode preparation and dimensional scale remain unowned
target: K1062 four-mode error threshold MAP-TYPE=evaluation
```

Keep the first three modes and replace `lambda_4=24` by
`lambda_n=n(n+2)`. The verified symmetric thresholds `eta/gamma` are

```text
n=4:   0.00241504213401009...
n=5:   0.00368990763714931...
n=8:   0.00565583028187488...
n=16:  0.00747440808182522...
n=64:  0.00900622958869220....
```

As `n` tends to infinity, the normalized fourth barycentric weight vanishes
and the first three weights converge to the normalized three-node
second-divided-difference witness. Therefore

```text
lim eta/gamma = 0.00955587804121949....
```

The listed fixtures increase, but no global monotonicity theorem is claimed.
Even the asymptotic route spends a higher-mode preparation and stays below a
one-percent response-normalized component budget; it supplies neither a ruler
nor detector ownership.

The producer passes `12/12`; the hostile probe rejects `10/10` family,
fixture, limit, monotonicity, ownership, scope and promotion mutations.

## Next condition

Choose a physically preparable fourth mode and own its response floor, error
box, dimensional scale and complete measured-systematics record.
