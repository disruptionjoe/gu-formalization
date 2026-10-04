---
title: "K1051 finite-mode scale-gauge obstruction"
status: active_research
doc_type: conditional_dispersion_scale_gauge_nonidentifiability_theorem
created: 2026-10-04
claim_ceiling: exact scale symmetry for any supplied mode set under unknown common readout gain; no GU action no-go or empirical score
manifest: lab/process/k1051-k1050-finite-mode-scale-gauge-obstruction.json
probe: tests/channel-swings/k1051_k1050_finite_mode_scale_gauge_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1051 finite-mode scale-gauge obstruction

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
result: absolute scale is a common-gain gauge for the complete supplied dispersion family
carrier: any collection of stationary modes with one common ruler and mass coefficient LAYER=observed CHIRALITY=N/A
pairing: positive candidate quotient energy ON=repository_owned_candidate_action
real_structure: positive real frequencies and common affine readout
grading: exact candidate-family nonidentifiability theorem; no physical calibration
action_owner: repository-construction -- source coefficient, dimensional scale and detector remain unowned
target: K1050 absolute mass/ruler interpretation MAP-TYPE=not-a-map
```

Write `r=s^2>0`, `m=m^2>0` and

```text
omega_lambda(r,m) = sqrt(r lambda + m),
y_lambda = g omega_lambda(r,m) + b,  g>0.
```

For every `c>0`,

```text
omega_lambda(cr,cm) = sqrt(c) omega_lambda(r,m).
```

Therefore the parameter transformation

```text
(r,m,g,b) -> (cr,cm,g/sqrt(c),b)
```

leaves every readout `y_lambda` unchanged simultaneously. This is not a
two-mode limitation: it holds for any finite or infinite collection of modes
sharing the same coefficients. Every affine-invariant spectrum-shape statistic
can depend on the dimensionless ratio `mu=m/r`, but not on the absolute ruler
or mass coefficient.

K1050's third mode removes the additive-offset ambiguity and can identify
shape. It cannot remove this scale gauge. Reopening absolute mass
identification requires an independently owned dimensional scale or a common
gain calibrated against an external standard.

The deterministic producer passes `11/11`; the hostile probe rejects `12/12`
dispersion, readout, symmetry, scope, fixture and promotion mutations.

## Next condition

Prove exactly whether the three-mode affine invariant identifies `mu=m/r`.
