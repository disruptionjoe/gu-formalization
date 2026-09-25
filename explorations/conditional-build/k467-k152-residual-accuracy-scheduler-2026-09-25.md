---
title: "K467 — K152 Residual Accuracy Scheduler"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K467 — K152 residual accuracy scheduler

> **GU-COMPARATOR-ROUTING — scope before inference.** This conditional
> consumer budget is not a physical GU result. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Composition

For target deficit `d`, positive shifted value `a` and exterior gap `g`, K270
allows shifted form-dual energy

`E_budget = d*a*g / ((a+g)(a-d))`.

K466 turns this into the M-dual requirement `eta_M^2 <= c E_budget`. With
K457's finite norm `sqrt(Q_12)` and norm tail `epsilon_tail`, the sufficient
finite-payload requirement is

`sqrt(Q_12)+epsilon_tail <= sqrt(c E_budget)`.

Thus the 59,586 entries are not evaluated until a quantitative K162 packet
supplies `c` and the K152 target supplies `a,g,d`. The exact control
`a=3,g=2,d=1,c=5/3` gives `E_budget=3/5`, M-dual square budget `1`, and
`Q_12 <= (1-3011499/838860800)^2`.

## Reproduction

Run `python3 tests/channel-swings/k467_k152_residual_accuracy_scheduler_probe.py`.
