---
title: "K1047 joint ruler/frequency certificate"
status: active_research
doc_type: conditional_joint_ruler_frequency_certificate
created: 2026-10-04
claim_ceiling: sharp candidate-horn separation surface for supplied ruler and component-frequency error bounds; no measured apparatus
manifest: lab/process/k1047-k1046-joint-ruler-frequency-certificate.json
probe: tests/channel-swings/k1047_k1046_joint_ruler_frequency_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1047 joint ruler/frequency certificate

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
result: sharp joint squared-ruler and relative-frequency separation surface
carrier: K1046 horn intervals with two separately bounded frequency readings LAYER=observed CHIRALITY=N/A
pairing: multiplicative confidence-free error intervals ON=repository_owned_candidate_holdout
real_structure: positive real frequencies and exact fourth-root threshold
grading: mathematical calibration target; no physical detector, coverage event or ruler ownership
action_owner: repository-construction -- measurement resources remain unowned
target: K1046 interval holdout MAP-TYPE=evaluation
```

Let

```text
R(delta) = [(5-4delta)/(2-delta)] / [(8+4delta)/(5+delta)]
beta      = ((1+epsilon)/(1-epsilon))^2.
```

The measured mass-one interval stays above the measured mass-four interval
exactly when `beta^2<R(delta)`. Thus the sharp joint surface is

```text
0 <= delta < 3/5,
epsilon < [R(delta)^(1/4)-1] / [R(delta)^(1/4)+1].
```

At `delta=0`, this reduces exactly to K1044's
`epsilon<9-4 sqrt(5)`. At the independent control
`delta=1/10, epsilon=1/25`, `R=391/266`, `beta^2=28561/20736`, and the
measured intervals retain a positive gap. Ruler uncertainty and modewise
frequency transfer are separate systematic inputs; this certificate measures
neither one.

The deterministic producer passes `11/11`; the hostile probe rejects `13/13`
error-model, surface, reduction, fixture, systematics and promotion mutations.

## Next condition

Identify which clock-transfer components cancel and which remain observable.
