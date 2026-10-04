---
title: "K978 K977 collision uniform convergence"
status: active_research
doc_type: conditional_collision_uniform_convergence_result
created: 2026-10-03
claim_ceiling: uniform coherence-factor approximation for one supplied collision interpolation only
manifest: lab/process/k978-k977-collision-uniform-convergence.json
probe: tests/channel-swings/k978_k977_collision_uniform_convergence_probe.py
target_claim: NONE-NOT-A-KILL
---

# K978 collision-model uniform convergence

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: fresh-collision interpolation converges uniformly with explicit O(h) coherence error and singular resource scaling
carrier: system qubit tensor a step-indexed one-pass fresh-qubit tape LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert adjoint, prepared ancilla state and partial trace ON=repository_collision_family
real_structure: computational-basis conjugation
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction with imported clock and freshness, not Weinstein source or GU action
target: strongest continuous-time contrary repair to K976-K977 MAP-TYPE=evaluation
```

K964 is exact only at grid times. For the left-continuous interpolation

```text
lambda_h(t)=exp(-2 gamma h floor(t/h)),
lambda(t)=exp(-2 gamma t),
```

write `t=h floor(t/h)+r` with `0<=r<h`. Then on every fixed finite horizon,

```text
|lambda_h(t)-lambda(t)|
 = exp(-2 gamma h floor(t/h))(1-exp(-2 gamma r))
 <= 1-exp(-2 gamma h)
 <= 2 gamma h.
```

The repair therefore converges uniformly and remains exact on the grid. It
does not produce a bounded autonomous microscopic parent. The explicit
collision angle and rate are

```text
theta_h=(1/2) arccos(exp(-2 gamma h)),
g_h=theta_h/h ~ sqrt(gamma/h),
h g_h^2 -> gamma,
```

while a horizon `T` consumes `floor(T/h)` one-pass ancillas (up to endpoint
convention). The continuum law is recovered together with a rapid-refresh and
singular-coupling resource, not from grid equality alone.
