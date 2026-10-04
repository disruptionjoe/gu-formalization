---
title: "K1003 exponential optimized-Bell persistence"
status: active_research
doc_type: conditional_exponential_bell_persistence_theorem
created: 2026-10-04
claim_ceiling: imported exponential dephasing consequence only
manifest: lab/process/k1003-k1002-exponential-bell-persistence.json
probe: tests/channel-swings/k1003_k1002_exponential_bell_persistence_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1003 exponential optimized-Bell persistence

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: optimized CHSH violation persists for every finite time under the imported exponential K956 law
carrier: K956 two-qubit Bell-diagonal trajectory LAYER=observed CHIRALITY=N/A
pairing: imported trace expectation with time-adapted Bell settings ON=repository_quantum_control
real_structure: complex two-qubit Hilbert space
grading: finite time versus asymptotic limit
action_owner: UNTYPED -- exponential generator and adaptive settings are imported
target: Bell-survival interval MAP-TYPE=evaluation
```

For `gamma>0`, substitute `lambda(t)=exp(-2 gamma t)` into K1001:

```text
S_max(t)=2 sqrt(1+exp(-4 gamma t)).
```

This is strictly greater than two at every finite `t` and approaches two from
above only as `t` tends to infinity. There is no finite optimized-Bell death
time in this ideal family.

The K959 time

```text
log(1+sqrt(2))/(2 gamma)
```

remains exact for the K957 settings frozen at `lambda=1`. It is a
fixed-witness crossing, not a state-optimal Bell-locality transition. At late
time the optimized excess is only
`S_max-2=exp(-4 gamma t)+O(exp(-8 gamma t))`, so ideal mathematical
violation does not imply finite-resolution observability.
