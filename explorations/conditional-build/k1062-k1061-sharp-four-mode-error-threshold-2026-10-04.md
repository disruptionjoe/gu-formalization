---
title: "K1062 sharp four-mode error threshold"
status: active_research
doc_type: conditional_four_mode_quadratic_error_certificate
created: 2026-10-04
claim_ceiling: sharp symmetric component-error threshold for the supplied residual certificates; no measured calibration
manifest: lab/process/k1062-k1061-sharp-four-mode-error-threshold.json
probe: tests/channel-swings/k1062_k1061_sharp_four_mode_error_threshold_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1062 sharp four-mode error threshold

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> detector-systematics certificate, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: sharp symmetric component-error versus linear-response boundary for four-mode horn separation
carrier: modes lambda={3,8,15,24} and mu in {1,4} LAYER=observed CHIRALITY=N/A
pairing: paired K1061 residual witnesses ON=repository_owned_candidate_holdout
real_structure: real quadratic readout with independently bounded component errors
grading: exact conditional systematics target; no detector characterization
action_owner: repository-construction -- response floor and measured errors remain unowned
target: K1061 four-mode residual witness MAP-TYPE=evaluation
```

Let

```text
y_i=A lambda_i+g sqrt(lambda_i+mu)+B+e_i,
|e_i|<=eta,  |g|>=gamma>0.
```

The true-horn residual is at most `eta`. The wrong-horn residual is at least
`gamma c-eta`, where `c` is the directed cross contrast. The wrong horn is
therefore excluded exactly when `gamma c>2 eta`. Requiring this in both
directions gives

```text
eta/gamma < 0.00483008426802017.../2
          = 0.00241504213401009....
```

The boundary is sharp for these residual certificates: at equality the two
admissible residual intervals touch. The ratio is normalized component error
per linear-response unit, not absolute frequency or mass accuracy.

The producer passes `10/10`; the hostile probe rejects `8/8` threshold, model,
sharpness, scale, scope and promotion mutations.

## Next condition

Recover `g` and its component-error amplification for each horn so a measured
fit can certify that the nonzero-response premise is actually met.
