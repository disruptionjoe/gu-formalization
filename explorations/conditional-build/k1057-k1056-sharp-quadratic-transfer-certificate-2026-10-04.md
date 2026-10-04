---
title: "K1057 sharp quadratic-transfer certificate"
status: active_research
doc_type: conditional_three_mode_quadratic_nonlinearity_certificate
created: 2026-10-04
claim_ceiling: sharp normalized quadratic-curvature threshold for the supplied three-mode horns; no measured transfer audit
manifest: lab/process/k1057-k1056-sharp-quadratic-transfer-certificate.json
probe: tests/channel-swings/k1057_k1056_sharp_quadratic_transfer_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1057 sharp quadratic-transfer certificate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. It does not transfer to
> a source-native GU mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: sharp symmetric normalized quadratic-curvature tolerance for the frozen three-mode horns
carrier: modes lambda={3,8,15} with mu in {1,4} LAYER=observed CHIRALITY=N/A
pairing: adjacent transformed-gap ratio ON=repository_owned_candidate_holdout
real_structure: positive real frequencies and common quadratic transfer
grading: exact calibration target; no physical detector or curvature measurement
action_owner: repository-construction -- apparatus resources remain unowned
target: K1056 nonlinear transfer obstruction MAP-TYPE=evaluation
```

Use

```text
y = g(x+t x^2)+b,  g>0,  |t|<=tau.
```

For three ordered frequencies,

```text
D_mu(t)=D_mu(0) [1+t(x_2+x_3)]/[1+t(x_1+x_2)].
```

This is strictly increasing in `t` wherever the transformed gaps stay
positive. Thus the candidate intervals are disjoint exactly when

```text
D_4(-tau) > D_1(tau).
```

For the frozen modes, `x_1=(2,3,4)` and
`x_4=(sqrt(7),2sqrt(3),sqrt(19))`. Cross multiplication makes the quadratic
terms cancel exactly. The unique positive touching boundary is

```text
tau_* = 0.023489886326011417315440696757877859... .
```

The units are inverse normalized frequency; this is not a dimensionless
percent until the frequency normalization is physically owned. At equality
the prediction intervals touch, so strict separation requires `tau<tau_*`.

The deterministic producer passes `12/12`; the hostile probe rejects `12/12`
model, monotonicity, threshold, fixture, scope and promotion mutations.

## Next condition

Compose this curvature tolerance with K1054's independent component-readout
error rather than spending both budgets separately.
