---
title: "K1058 joint nonlinearity-component budget"
status: active_research
doc_type: conditional_joint_detector_systematics_certificate
created: 2026-10-04
claim_ceiling: sharp joint quadratic-curvature and component-readout budget for the supplied horns; no measured detector audit
manifest: lab/process/k1058-k1057-joint-nonlinearity-component-budget.json
probe: tests/channel-swings/k1058_k1057_joint_nonlinearity_component_budget_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1058 joint nonlinearity-component budget

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is a
> conditional apparatus calculation, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: exact shared budget between quadratic transfer curvature and independent component error
carrier: frozen three-mode candidate frequencies LAYER=observed CHIRALITY=N/A
pairing: adjacent measured-gap ratio ON=repository_owned_candidate_holdout
real_structure: positive real common transfer plus independently bounded residuals
grading: sharp mathematical systematics surface; no measured detector
action_owner: repository-construction -- apparatus and source action remain unowned
target: K1057 curvature-only certificate MAP-TYPE=evaluation
```

Let

```text
y_i=g(x_i+t x_i^2)+b+zeta_i,
|t|<=tau,  |zeta_i|<=g eta.
```

The shared middle reading makes the two gap errors correlated. The attainable
worst corners are `(+eta,-eta,+eta)` for the mass-one maximum and
`(-eta,+eta,-eta)` for the mass-four minimum. Hence separation is exact when

```text
[(1+7tau)+2eta]/[(1+5tau)-2eta]
  < [(b_4-7tau)-2eta]/[(a_4-5tau)+2eta].
```

Both quadratic terms cancel on cross multiplication. With
`a_4=2sqrt(3)-sqrt(7)` and `b_4=sqrt(19)-2sqrt(3)`, the sharp boundary is

```text
eta_*(tau)=
 [(1+5tau)(b_4-7tau)-(1+7tau)(a_4-5tau)]
 / [2(2+a_4+b_4)].
```

It is exactly affine and decreasing in `tau`. Its intercept is K1054's
`0.0102940997633828...`; it reaches zero at K1057's
`tau_*=0.0234898863260114...`. At `tau=0.01`, only
`eta<0.00591174574918578...` remains. Curvature and component error therefore
spend one common budget; they cannot each be set independently at their
single-systematic maxima.

The deterministic producer passes `12/12`; the hostile probe rejects `12/12`
model, extremum, boundary, limiting-case, scope and promotion mutations.

## Next condition

Test whether one redundant nonzero mode restores exact horn identification
under a common quadratic transfer without requiring small curvature.
