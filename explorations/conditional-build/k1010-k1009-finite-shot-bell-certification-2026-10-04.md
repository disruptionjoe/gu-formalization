---
title: "K1010 finite-shot Bell certification"
status: active_research
doc_type: conditional_statistical_certification_budget
created: 2026-10-04
claim_ceiling: iid bounded-correlator concentration certificate and ownership disposition only
manifest: lab/process/k1010-k1009-finite-shot-bell-certification.json
probe: tests/channel-swings/k1010_k1009_finite_shot_bell_certification_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1010 finite-shot Bell certification

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: finite-shot confidence penalty for a four-correlator CHSH estimate
carrier: four imported iid streams of plus-or-minus-one outcomes LAYER=observed CHIRALITY=N/A
pairing: empirical averaging plus imported probability semantics ON=repository_quantum_control
real_structure: real bounded random variables
grading: four predeclared CHSH setting pairs
action_owner: UNTYPED -- sampling independence detectors and systematic errors are not GU owned
target: finite statistical error budget before Bell scoring MAP-TYPE=evaluation
```

Let each of the four CHSH correlators be estimated from `n` independent
`[-1,1]` outcomes, and let `S_hat` be their signed sum. Hoeffding plus a union
bound gives, with probability at least `1-alpha`,

```text
|S_hat-S| <= beta(n,alpha)
             =4 sqrt(log(8/alpha)/(2n))
             =sqrt(8 log(8/alpha)/n).
```

Therefore `S_hat>2+beta(n,alpha)` certifies `S>2`. If the declared true
margin is `m=S-2>0`, it is sufficient to take

```text
n >= 8 log(8/alpha)/m^2
```

shots per correlator. For K1009's ideal `p=1`, `V=2/5` point and
`alpha=1/20`, `m=2(sqrt(29)/5-1)` and the bound gives `n=1711` per
correlator, `6844` total shots.

This certificate assumes iid trials, bounded correctly assigned outcomes,
predeclared settings, randomization compatible with the Bell protocol and no
unbudgeted systematic drift. If the total systematic CHSH uncertainty is
`sigma_sys`, the operational condition becomes
`S_hat>2+beta+sigma_sys`. GU still must own the physical quotient, positive
state/effect pairing, local observable algebras, generator, preparation,
settings, locality, detector semantics and systematic-error model before the
calibration anchor is scored. No source, ledger, prediction, confirmation,
canon or public verdict moves.
