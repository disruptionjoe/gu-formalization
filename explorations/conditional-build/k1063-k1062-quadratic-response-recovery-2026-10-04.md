---
title: "K1063 quadratic response recovery"
status: active_research
doc_type: conditional_four_mode_response_recovery_certificate
created: 2026-10-04
claim_ceiling: exact linear-response recovery rows and component-error amplification inside the supplied quadratic model; no physical calibration ownership
manifest: lab/process/k1063-k1062-quadratic-response-recovery.json
probe: tests/channel-swings/k1063_k1062_quadratic_response_recovery_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1063 quadratic response recovery

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> calibration calculation, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: recover the nonzero linear response and its component-error amplification after horn feasibility
carrier: four-mode quadratic design matrices for mu in {1,4} LAYER=observed CHIRALITY=N/A
pairing: least-squares coefficient row against detector readings ON=repository_owned_candidate_holdout
real_structure: real finite-dimensional readout fit
grading: exact coefficient interface; no physical calibration record
action_owner: repository-construction -- detector and preparation remain unowned
target: K1062 nonzero-response premise MAP-TYPE=evaluation
```

For each horn, fit `y=A lambda+g x_mu+B`. The coefficient row `r_mu` is
defined by

```text
r_mu dot 1=0,  r_mu dot lambda=0,  r_mu dot x_mu=1.
```

The minimum-Euclidean-norm rows give

```text
r_1=(-41,33,37,-29)/20,       ||r_1||_1=7,
||r_4||_1=10.2246196659792....
```

Thus `g_hat=r_mu dot y` obeys the exact componentwise bound

```text
|g_hat-g| <= eta ||r_mu||_1.
```

After residual feasibility has selected a horn, the strict inequality
`|g_hat|>eta||r_mu||_1` certifies nonzero linear response. It does not by
itself select the horn or supply an independently characterized detector; the
mass-four fit is also more error-amplifying than the mass-one fit.

The producer passes `13/13`; the hostile probe rejects `11/11` mode, row,
amplification, recovery, scope and promotion mutations.

## Next condition

Ask whether preparing a higher fourth eigenmode can materially relax K1062's
tight `0.2415%` response-normalized component budget.
