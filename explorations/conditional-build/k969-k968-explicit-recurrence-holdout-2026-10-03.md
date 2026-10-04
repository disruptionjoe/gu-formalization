---
title: "K969 K968 explicit recurrence holdout"
status: active_research
doc_type: conditional_explicit_recurrence_holdout
created: 2026-10-03
claim_ceiling: exact recurrence witness for the named uniform grid only; no universal minimal recurrence or prediction
manifest: lab/process/k969-k968-explicit-recurrence-holdout.json
probe: tests/channel-swings/k969_k968_explicit_recurrence_holdout_probe.py
target_claim: NONE-NOT-A-KILL
---

# K969 explicit recurrence holdout

```gu-typed-objects
result: exact late recurrence separates the K968 finite grid from the K966 continuum after calibration
carrier: K968 finite spectral environment C^N LAYER=observed CHIRALITY=N/A
pairing: positive Euclidean Hilbert pairing ON=repository_finite_approximation
real_structure: conjugation paired across symmetric midpoint frequencies
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction, not Weinstein source or GU action
target: predeclared recurrence-versus-continuum holdout MAP-TYPE=evaluation
```

The K968 midpoint frequencies have spacing `Delta=2 Omega/N`. At

```text
tau_rec = 4 pi/Delta = 2 pi N/Omega,
```

every phase is exactly one, so `f_N(tau_rec)=1`. The continuum parent instead
gives `exp(-2 gamma tau_rec)`. In the control instance,
`tau_rec=754.0554...>T=3`; the continuum value underflows below the reported
precision while the finite grid returns to one.

This supplies a clean calibration/holdout split. Freeze `gamma,T,epsilon`, the
cutoff, atom count and weights using only the calibration interval `[0,T]`;
reserve a predeclared neighborhood of `tau_rec` for the parent discriminator.
The holdout is unscored. The theorem claims neither that `tau_rec` is the
earliest recurrence nor that any physical GU reservoir has this grid.
