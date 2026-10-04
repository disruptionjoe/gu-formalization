---
title: "K1048 common-clock cancellation"
status: active_research
doc_type: conditional_clock_transfer_identifiability_certificate
created: 2026-10-04
claim_ceiling: exact classification of common gain, differential transfer and additive offset in the candidate ratio protocol
manifest: lab/process/k1048-k1047-common-clock-cancellation.json
probe: tests/channel-swings/k1048_k1047_common_clock_cancellation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1048 common-clock cancellation

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: clock-transfer ownership correction for the frozen two-mode ratio
carrier: two measured positive frequencies LAYER=observed CHIRALITY=N/A
pairing: squared-frequency ratio ON=repository_owned_candidate_holdout
real_structure: common positive affine readout with modewise multiplicative deviations
grading: apparatus identifiability theorem; no detector constructed
action_owner: repository-construction -- physical transfer law remains unowned
target: K1047 measurement model MAP-TYPE=evaluation
```

For the readout model

```text
y_i = g(1+e_i) omega_i + b,  g>0,
```

a common multiplicative clock gain cancels exactly when `b=0` and the
mode-dependent errors vanish. With `b=0`,

```text
Q_hat = Q ((1+e_2)/(1+e_1))^2,
```

which is precisely the K1044/K1047 transfer model. A common additive offset
does not cancel from the two-mode ratio.

The ownership correction is material: the protocol does not need an absolute
clock scale. It does need stable mode-to-mode transfer plus either calibrated
or bounded additive offset. A gain `g=7/3` control leaves `Q=5/2` exactly
unchanged.

The deterministic producer passes `7/7`; the hostile probe rejects `9/9`
readout, cancellation, transfer, offset, fixture, ownership and promotion
mutations.

## Next condition

Test whether two modes can survive a fully uncalibrated common affine readout.
