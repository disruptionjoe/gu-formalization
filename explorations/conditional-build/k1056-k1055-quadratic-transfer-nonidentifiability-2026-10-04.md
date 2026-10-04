---
title: "K1056 quadratic-transfer nonidentifiability"
status: active_research
doc_type: conditional_detector_nonlinearity_nonidentifiability_theorem
created: 2026-10-04
claim_ceiling: exact countermodel for the supplied dispersion family under unknown monotone quadratic transfer; no detector evidence or GU action no-go
manifest: lab/process/k1056-k1055-quadratic-transfer-nonidentifiability.json
probe: tests/channel-swings/k1056_k1055_quadratic_transfer_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1056 quadratic-transfer nonidentifiability

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: arbitrary unknown quadratic detector transfer erases the supplied dimensionless mass-shape parameter
carrier: normalized positive dispersion modes x_mu(lambda)=sqrt(lambda+mu) LAYER=observed CHIRALITY=N/A
pairing: modewise detector readout ON=repository_owned_candidate_holdout
real_structure: positive real frequencies and monotone quadratic maps
grading: exact candidate-family countermodel; no physical detector characterization
action_owner: repository-construction -- scale, transfer and measured record remain unowned
target: K1052 affine spectrum-shape statistic MAP-TYPE=not-a-map
```

For any `mu>0`, define

```text
x_mu(lambda) = sqrt(lambda+mu),
T_mu(x) = x^2-mu.
```

Then `T_mu'(x)=2x>0` on the positive frequency domain, yet

```text
T_mu(x_mu(lambda)) = lambda
```

for every mode simultaneously. Thus the mass-one and mass-four horns can
produce the same complete readout sequence under different admissible
strictly increasing quadratic transfers. The obstruction is not removed by a
fourth mode, a finite number of modes, or an infinite exact mode sequence.

K1052's positive theorem is therefore conditional on a common affine transfer
or another calibrated transfer class. It is not enough to say that gain and
offset are common: quadratic curvature is a distinct nuisance parameter.

The deterministic producer passes `12/12`; the hostile probe rejects `12/12`
dispersion, transfer, scope, fixture, interpretation and promotion mutations.

## Next condition

Bound one normalized quadratic-curvature parameter and derive the sharp range
that preserves separation of the frozen three-mode horns.
