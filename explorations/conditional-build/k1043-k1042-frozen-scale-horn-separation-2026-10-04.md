---
title: "K1043 frozen-scale horn separation"
status: active_research
doc_type: conditional_sharp_additive_holdout_certificate
created: 2026-10-04
claim_ceiling: sharp additive-Q separation conditional on the frozen scale and an honest error radius; no detector certification
manifest: lab/process/k1043-k1042-frozen-scale-horn-separation.json
probe: tests/channel-swings/k1043_k1042_frozen_scale_horn_separation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1043 frozen-scale horn separation

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: sharp additive-error decision certificate for the frozen two-mode ratio
carrier: two candidate Q values with symmetric uncertainty intervals LAYER=observed CHIRALITY=N/A
pairing: ordered real-line interval comparison ON=repository_owned_candidate_holdout
real_structure: exact rational arithmetic
grading: candidate mathematics only; no physical detector record
action_owner: repository-construction -- ruler and apparatus remain unowned
target: mass-horn interval separation MAP-TYPE=evaluation
```

The exact values `5/2` and `8/5` are separated by `9/10`. Symmetric
absolute-`Q` uncertainty intervals are therefore disjoint exactly when their
radius is less than `9/20`; at equality they touch at the midpoint `41/20`.
Above that midpoint the mass-one horn is selected, and below it the mass-four
horn is selected, conditional on the common frozen ruler.

This is sharp arithmetic for the candidate holdout. It does not provide the
preparation, clock, detector, calibration evidence or systematic-error audit
needed to claim that a physical record satisfies the bound.

The deterministic producer passes `10/10`; the hostile probe rejects `10/10`
value, margin, sharpness, scope and promotion mutations.

## Next condition

Translate the `Q` radius into a componentwise frequency-calibration target.
