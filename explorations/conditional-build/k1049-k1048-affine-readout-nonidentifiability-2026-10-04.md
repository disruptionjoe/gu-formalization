---
title: "K1049 affine-readout nonidentifiability"
status: active_research
doc_type: conditional_two_mode_affine_readout_countermodel
created: 2026-10-04
claim_ceiling: exact two-point apparatus nonidentifiability under an unknown common positive affine readout; no horn or GU verdict
manifest: lab/process/k1049-k1048-affine-readout-nonidentifiability.json
probe: tests/channel-swings/k1049_k1048_affine_readout_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1049 affine-readout nonidentifiability

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
result: exact positive-affine countermodel for any two ordered frequency pairs
carrier: two positive ordered frequencies per supplied horn LAYER=observed CHIRALITY=N/A
pairing: raw readout coordinate ON=repository_owned_candidate_holdout
real_structure: positive real gain with unrestricted common additive offset
grading: candidate apparatus nonidentifiability; not a physical detector model
action_owner: repository-construction -- readout calibration remains unowned
target: K1048 offset boundary MAP-TYPE=evaluation
```

For any ordered pairs `u_1<u_2` and `v_1<v_2`, the unique map

```text
g = (v_2-v_1)/(u_2-u_1) > 0,
b = v_1-g u_1
```

satisfies `g u_i+b=v_i` for both points. In particular, one positive affine
readout maps the fixed-scale mass-one pair `(sqrt(2),sqrt(5))` exactly to the
mass-four pair `(sqrt(5),sqrt(8))`.

Therefore two prepared modes cannot discriminate the candidate horns if both
common gain and common offset are free. The exact reopener is to calibrate or
bound the offset, or to prepare a third mode and use an affine-invariant
statistic. This is an apparatus countermodel only: both mass horns and the
spatial ruler remain imported.

The deterministic producer passes `10/10`; the hostile probe rejects `12/12`
theorem, horn-map, residual, conclusion, reopener, scope and promotion
mutations.

## Next condition

Freeze a nonzero three-mode statistic invariant under common affine readout.
