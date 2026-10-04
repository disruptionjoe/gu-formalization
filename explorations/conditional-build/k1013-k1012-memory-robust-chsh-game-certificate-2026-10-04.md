---
title: "K1013 memory-robust CHSH-game certificate"
status: active_research
doc_type: conditional_sequential_bell_certificate
created: 2026-10-04
claim_ceiling: finite-sample local-realism rejection under fresh uniform settings and event-ready binary trials only
manifest: lab/process/k1013-k1012-memory-robust-chsh-game-certificate.json
probe: tests/channel-swings/k1013_k1012_memory_robust_chsh_game_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1013 memory-robust CHSH-game certificate

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: a total-trial CHSH-game certificate robust to arbitrary inter-trial device memory
carrier: event-ready binary trials with fresh uniform setting pairs LAYER=observed CHIRALITY=N/A
pairing: conditional probability and supermartingale concentration ON=repository_quantum_control
real_structure: bounded win indicators W_i in {0,1}
grading: finite-sample rejection of the declared local model class
action_owner: UNTYPED -- randomness locality timing detectors and trial definition are not GU owned
target: memory-robust Bell inference boundary MAP-TYPE=evaluation
```

For uniformly random setting bits `x,y`, define a win by
`a xor b=x*y`. With the standard sign convention,

```text
w=Pr(win)=1/2+S/8.
```

Allow the devices arbitrary memory of all earlier trials. Under locality and
fresh settings independent of the devices, every conditional local strategy
still satisfies

```text
E[W_i | F_(i-1)] <= 3/4.
```

The bounded supermartingale Hoeffding--Azuma inequality gives

```text
Pr(w_hat-3/4 >= t) <= exp(-2 n t^2).
```

Thus

```text
w_hat > 3/4 + sqrt(log(1/alpha)/(2n))
```

rejects that local model class at level `alpha` without an iid-device
assumption. At K1009's exact `p=1`, `V=2/5` point,
`S=2 sqrt(29)/5` and `w=1/2+sqrt(29)/20`; for `alpha=1/20`, the sufficient
integer budget is `n=4039` total event-ready trials.

This does not close measurement independence, spacelike locality, setting
generation, binary/event-ready outcome assignment, detection or
postselection. It is a conditional inference theorem, not a GU prediction or
a claim that an experiment is loophole-free.
