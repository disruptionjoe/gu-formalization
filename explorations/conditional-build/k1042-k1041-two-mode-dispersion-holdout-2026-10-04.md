---
title: "K1042 two-mode dispersion holdout"
status: active_research
doc_type: conditional_frozen_two_mode_dispersion_holdout
created: 2026-10-04
claim_ceiling: exact candidate-level holdout on one frozen ruler; no source-selected coefficient, empirical score, prediction or confirmation
manifest: lab/process/k1042-k1041-two-mode-dispersion-holdout.json
probe: tests/channel-swings/k1042_k1041_two_mode_dispersion_holdout_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1042 two-mode dispersion holdout

Classification: `INTERNAL_CONDITIONAL_HOLDOUT`.

```gu-typed-objects
result: a frozen two-mode squared-frequency ratio separates the supplied mass-one and mass-four candidate actions
carrier: K77 quotient modes at spatial eigenvalues one and four LAYER=observed CHIRALITY=N/A
pairing: positive K77 quotient energy ON=repository_owned_candidate_action
real_structure: real stationary wave modes
grading: calibration used lambda=0; holdout uses lambda=1 and lambda=4
action_owner: repository-construction -- common ruler and mass coefficient not source-selected
target: distinct candidate holdout MAP-TYPE=evaluation
```

Freeze `s^2=1` independently of the candidate and preregister

```text
Q = omega(lambda=4)^2 / omega(lambda=1)^2.
```

The mass-one horn gives squared frequencies `(2,5)` and `Q=5/2`; the
mass-four horn gives `(5,8)` and `Q=8/5`. The gap is `9/10` and the midpoint
is `41/20`. K1037's exact controls used only `lambda=0`, so these two nonzero
modes are a distinct candidate-level holdout rather than reused calibration.

The holdout is frozen but unscored. Even a future score would distinguish
supplied repository candidates, not confirm GU, because neither coefficient
nor ruler is source-selected.

The deterministic producer passes `10/10`; the hostile probe rejects `12/12`
preregistration, arithmetic, scoring and promotion mutations.

## Next condition

Prove the sharp error margin for the frozen `Q` decision rule.
