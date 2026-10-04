---
title: "K1052 affine spectrum-shape identifiability"
status: active_research
doc_type: conditional_three_mode_dimensionless_shape_identifiability_theorem
created: 2026-10-04
claim_ceiling: exact injectivity of the adjacent-difference statistic in the supplied dimensionless dispersion family; no absolute scale or detector ownership
manifest: lab/process/k1052-k1051-affine-spectrum-shape-identifiability.json
probe: tests/channel-swings/k1052_k1051_affine_spectrum_shape_identifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1052 affine spectrum-shape identifiability

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
result: three affine-readout modes identify the dimensionless mass-to-ruler ratio in the supplied dispersion family
carrier: ordered stationary modes lambda1<lambda2<lambda3 LAYER=observed CHIRALITY=N/A
pairing: adjacent frequency-difference ratio ON=repository_owned_candidate_action
real_structure: positive real square-root spectrum
grading: exact injectivity theorem for candidate spectrum shape; no absolute parameter or apparatus ownership
action_owner: repository-construction -- source selection and measured preparation remain unowned
target: K1051 invariant parameter mu=m/r MAP-TYPE=evaluation
```

Let `mu=m/r>0`, `x_i=sqrt(lambda_i+mu)` and

```text
D_mu = (x_3-x_2)/(x_2-x_1)
     = [(lambda_3-lambda_2)/(lambda_2-lambda_1)]
       [(x_2+x_1)/(x_3+x_2)].
```

The rationalized form gives the exact logarithmic derivative

```text
d(log D_mu)/dmu
  = 1/(2 x_1 x_2) - 1/(2 x_2 x_3)
  = (x_3-x_1)/(2 x_1 x_2 x_3) > 0.
```

Thus `D_mu` is strictly increasing for every ordered three-mode set and is
injective in the dimensionless spectrum shape `mu`. Its upper limit is the
bare eigenvalue-gap ratio

```text
(lambda_3-lambda_2)/(lambda_2-lambda_1).
```

For the frozen modes `{3,8,15}`, the limit is `7/5`. At `mu=1`, the
frequencies are exactly `(2,3,4)`, so `D=1`; strict monotonicity proves
`D=1` iff `mu=1`. At `mu=4`, K1050's exact radical is greater than one.

The result sharpens the ownership statement: three modes do identify
`m^2/s^2` inside the supplied candidate family despite common gain and offset.
They do not identify absolute `m^2` or `s^2` because K1051's scale gauge
remains exact.

The deterministic producer passes `13/13`; the hostile probe rejects `14/14`
parameter, formula, monotonicity, range, fixture and promotion mutations.

## Next condition

Derive the sharp adjacent-gap transfer accuracy needed to separate the frozen
`mu=1` and `mu=4` candidates.
