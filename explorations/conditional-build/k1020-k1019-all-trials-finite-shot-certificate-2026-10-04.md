---
title: "K1020 all-trials finite-shot certificate"
status: active_research
doc_type: conditional_all_trials_bell_certificate
created: 2026-10-04
claim_ceiling: finite-shot local-realism rejection plus model-based shot forecast only
manifest: lab/process/k1020-k1019-all-trials-finite-shot-certificate.json
probe: tests/channel-swings/k1020_k1019_all_trials_finite_shot_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1020 all-trials finite-shot certificate

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: memory-robust CHSH-game certificate retaining every no-click trial
carrier: heralded event-ready binary trials with fresh uniform settings LAYER=observed CHIRALITY=N/A
pairing: empirical all-trials win frequency against the local ceiling ON=repository_quantum_control
real_structure: bounded real supermartingale differences
grading: exact inference theorem plus conditional independent-loss forecast
action_owner: UNTYPED -- heralding, settings, locality, detectors and systematics are not GU owned
target: finite all-trials Bell certification MAP-TYPE=evaluation
```

Herald a trial before choosing settings, map every no-click locally to `+1`,
and retain every trial. Under fresh uniform settings independent of the local
devices, arbitrary inter-trial memory still obeys

```text
w_hat > 3/4 + sqrt(log(1/alpha)/(2n)).
```

The empirical certificate needs no fair-sampling assumption because no trial
is discarded. Predicting its sample size does require a detector model. Under
K1018's independent equal-efficiency forecast at
`p=1,V=2/5,eta=49/50,alpha=1/20`, the expected win margin is
`0.0086956140...`, and the smallest sufficient integer budget is
`n=19,810` total heralded trials.

This closes only the mathematical postselection repair. GU still supplies no
event-ready herald, fresh measurement-independent setting source, spacelike
locality proof, detector response, state/effect pairing, action, or complete
statistical/systematic budget. No empirical or GU score is assigned.
