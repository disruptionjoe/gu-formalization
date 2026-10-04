---
title: "K1044 frequency-resolution certificate"
status: active_research
doc_type: conditional_sharp_relative_frequency_certificate
created: 2026-10-04
claim_ceiling: sharp common relative-frequency tolerance for the frozen candidate holdout; no physical detector or clock ownership
manifest: lab/process/k1044-k1043-frequency-resolution-certificate.json
probe: tests/channel-swings/k1044_k1043_frequency_resolution_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1044 frequency-resolution certificate

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: sharp componentwise relative-frequency tolerance for disjoint candidate-horn ratio intervals
carrier: two measured mode frequencies per supplied candidate horn LAYER=observed CHIRALITY=N/A
pairing: multiplicative error intervals on the positive frequency line ON=repository_owned_candidate_holdout
real_structure: positive real frequencies and exact algebraic threshold
grading: mathematical calibration target; no physical clock or detector certification
action_owner: repository-construction -- measurement resources remain unowned
target: relative-error propagation to the squared-frequency ratio MAP-TYPE=evaluation
```

If each measured frequency differs from its true value by at most relative
error `epsilon<1`, the squared-frequency ratio expands by at most

```text
beta = ((1+epsilon)/(1-epsilon))^2.
```

The two horn intervals are disjoint exactly when `beta<5/4`, equivalently

```text
epsilon < 9 - 4 sqrt(5) = 0.0557280900008412...
```

At equality the intervals touch. The exact threshold is the small root of
`epsilon^2-18 epsilon+1=0`. A five-percent fixture has a strictly positive
remaining interval gap.

This value is a calibration target, not evidence that any physical clock or
frequency detector attains it. Preparation, drift, scale uncertainty and
model discrepancy remain separate systematic rows.

The deterministic producer passes `11/11`; the hostile probe rejects `11/11`
error-model, threshold, fixture, systematics and promotion mutations.

## Next condition

Reconcile the frozen holdout and sharp target at candidate, GU-source and
scorable grades.
