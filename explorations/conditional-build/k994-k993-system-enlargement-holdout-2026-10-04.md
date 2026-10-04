---
title: "K994 K993 system enlargement holdout"
status: active_research
doc_type: conditional_preregistered_holdout
created: 2026-10-04
claim_ceiling: frozen unscored pairwise holdout after imported enlargement
manifest: lab/process/k994-k993-system-enlargement-holdout.json
probe: tests/channel-swings/k994_k993_system_enlargement_holdout_probe.py
target_claim: NONE-NOT-A-KILL
---

# K994 frozen gap-one system-enlargement holdout

Classification: `INTERNAL_PREREGISTERED_HOLDOUT`.

```gu-typed-objects
result: frozen gap-one coherence discriminator for one Brownian and one compound-Poisson horn
carrier: supplied qutrit with Q=diag(-1,0,1) LAYER=observed CHIRALITY=N/A
pairing: imported positive trace pairing and coherence readout ON=repository_stochastic_model
real_structure: computational-basis conjugation with real symmetric phase laws
grading: gap two for calibration and gap one for holdout
action_owner: UNTYPED -- no GU action owns the enlarged charge sector or readout
target: pairwise nonrecord holdout MAP-TYPE=evaluation
```

Freeze `gamma=0.7`, `T=2`, and the K987 angle `theta=pi/4`. Calibrate both
horns only on their shared gap-two coherence

```text
phi_T(2)=exp(-2 gamma T)=0.06081006262521797.
```

The held-out gap-one values are

```text
Brownian:          exp(-gamma T/2),
compound-Poisson: exp[-gamma T/(1+cos(theta))].
```

They are strictly different and no microscopic record is required. This is a
pairwise holdout only. It uses a new qutrit charge sector, does not identify a
general phase law, has no data, permits no refit, and remains unscored until a
GU-owned action, physical quotient, positive pairing and gap-one observable
make the experiment native.
