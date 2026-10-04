---
title: "K973 K972 quadratic Zeno boundary"
status: active_research
doc_type: conditional_short_time_boundary
created: 2026-10-03
claim_ceiling: quadratic short-time theorem for positive spectral states with finite variance
manifest: lab/process/k973-k972-quadratic-zeno-boundary.json
probe: tests/channel-swings/k973_k972_quadratic_zeno_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K973 quadratic short-time boundary

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: finite spectral variance forces quadratic survival loss and excludes exact linear exponential onset
carrier: positive spectral probability state with finite second moment LAYER=observed CHIRALITY=N/A
pairing: positive expectation and modulus-squared survival ON=declared_measure
real_structure: characteristic-function conjugation
grading: degree-zero; no BV or gauge grading
action_owner: UNTYPED -- structural theorem on supplied spectral dynamics
target: physical short-time consequence of K972 MAP-TYPE=evaluation
```

If `m=E[omega]` and `E[omega^2]<infinity`, dominated Taylor expansion gives

```text
phi(t)=1+i m t-(1/2)E[omega^2]t^2+o(t^2).
```

Multiplication by the conjugate expansion yields

```text
|phi(t)|^2=1-Var(omega)t^2+o(t^2).
```

The K966 target amplitude `exp(-a|t|)` instead has survival

```text
exp(-2a|t|)=1-2a|t|+o(|t|).
```

For `a>0`, its loss is linear rather than quadratic. Therefore a positive
autonomous spectral state with finite second moment cannot realize the exact
target. The symmetric two-atom control `phi(t)=cos(t)` reproduces the
quadratic coefficient `Var=1`, while the exponential control reproduces the
linear coefficient `2a`.

This is the usual short-time/Zeno mechanism stated only for the declared
spectral-parent class. It is not a universal no-go for nonunitary reduced
dynamics. K974 quantifies how the spectral second moment must grow in an approximation.
