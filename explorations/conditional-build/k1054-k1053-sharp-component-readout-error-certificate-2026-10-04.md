---
title: "K1054 sharp component-readout error certificate"
status: active_research
doc_type: conditional_three_mode_component_readout_error_certificate
created: 2026-10-04
claim_ceiling: sharp per-frequency additive-error threshold under a common affine readout for the frozen candidate horns; no detector construction
manifest: lab/process/k1054-k1053-sharp-component-readout-error-certificate.json
probe: tests/channel-swings/k1054_k1053_sharp_component_readout_error_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1054 sharp component-readout error certificate

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
result: sharp componentwise additive-readout tolerance for the frozen three-mode discriminator
carrier: three measured candidate frequencies under one common affine transfer LAYER=observed CHIRALITY=N/A
pairing: adjacent difference ratio ON=repository_owned_candidate_holdout
real_structure: positive real gain, unrestricted common offset and independently bounded residuals
grading: exact mathematical calibration target; no physical detector or gain calibration
action_owner: repository-construction -- preparation, transfer audit and record remain unowned
target: K1053 gap-error abstraction MAP-TYPE=evaluation
```

Use the readout model

```text
y_i = g omega_i + b + zeta_i,
g>0,  |zeta_i| <= g eta.
```

The common offset cancels from both adjacent differences. The shared middle
reading makes the two gap errors correlated, but the exact extrema still occur
at cube corners. For the mass-one frequencies `(2,3,4)`,

```text
D_1,max = (1+2eta)/(1-2eta).
```

For the mass-four gaps

```text
a_4 = 2sqrt(3)-sqrt(7),
b_4 = sqrt(19)-2sqrt(3),
```

the exact lower ratio is

```text
D_4,min = (b_4-2eta)/(a_4+2eta).
```

Equating those boundaries cancels the quadratic terms and gives the sharp
component threshold

```text
eta < [sqrt(19)+sqrt(7)-4sqrt(3)]
      / [4+2sqrt(19)-2sqrt(7)]
    = 0.0102940997633829...
```

The fixture `eta=1/100` passes. Here `eta` is measured in gain-normalized
frequency units: this theorem neither calibrates `g` nor constructs a detector
or complete systematic audit.

The deterministic producer passes `13/13`; the hostile probe rejects `13/13`
readout, extrema, threshold, fixture, normalization and promotion mutations.

## Next condition

Reconcile the exact two-mode and three-mode apparatus tradeoff without
laundering dimensionless shape into absolute mass ownership.
