---
title: "K1053 sharp relative-gap resolution certificate"
status: active_research
doc_type: conditional_three_mode_relative_gap_error_certificate
created: 2026-10-04
claim_ceiling: sharp adjacent-gap transfer threshold for the frozen candidate horns; no measured detector or complete systematic budget
manifest: lab/process/k1053-k1052-sharp-relative-gap-resolution-certificate.json
probe: tests/channel-swings/k1053_k1052_sharp_relative_gap_resolution_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1053 sharp relative-gap resolution certificate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: sharp relative adjacent-gap tolerance for the frozen affine-invariant mass-horn statistic
carrier: three ordered candidate frequencies and their two adjacent gaps LAYER=observed CHIRALITY=N/A
pairing: positive ratio of measured adjacent gaps ON=repository_owned_candidate_holdout
real_structure: positive real gaps and exact algebraic threshold
grading: mathematical calibration target; no detector, coverage event or measured record
action_owner: repository-construction -- apparatus resources remain unowned
target: K1052 dimensionless shape discriminator MAP-TYPE=evaluation
```

Let the two true adjacent gaps be `a` and `b`, so `D=b/a`. If they are
measured independently with relative errors bounded by `rho<1`, then

```text
D_hat in [D(1-rho)/(1+rho), D(1+rho)/(1-rho)].
```

The mass-one candidate has `D_1=1`; write

```text
D_4 = (sqrt(19)-2sqrt(3))/(2sqrt(3)-sqrt(7)) > 1.
```

Their measured intervals are disjoint exactly when

```text
((1+rho)/(1-rho))^2 < D_4,
```

or equivalently

```text
rho < (sqrt(D_4)-1)/(sqrt(D_4)+1)
    = 0.0223229795291687...
```

At equality the intervals touch, so the threshold is sharp for this error
model. The rational fixture `rho=1/50` retains a positive gap. This target is
tighter than K1044's two-mode component-frequency tolerance and belongs to a
different transfer model: it controls the two adjacent differences directly.

The deterministic producer passes `11/11`; the hostile probe rejects `11/11`
model, interval, threshold, fixture, systematics and promotion mutations.

## Next condition

Propagate independent component readout errors through the shared middle
frequency rather than assuming independent gap errors.
