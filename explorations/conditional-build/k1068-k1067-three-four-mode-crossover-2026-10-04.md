---
title: "K1068 three/four-mode crossover"
status: active_research
doc_type: conditional_detector_route_crossover_certificate
created: 2026-10-04
claim_ceiling: exact candidate-route crossover under matched response normalization; no apparatus score
manifest: lab/process/k1068-k1067-three-four-mode-crossover.json
probe: tests/channel-swings/k1068_k1067_three_four_mode_crossover_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1068 three/four-mode crossover

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> apparatus-route comparison, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: exact curvature values where the three-mode and named four-mode component-error budgets cross
carrier: supplied three-mode and K1066 four-mode horn families LAYER=observed CHIRALITY=N/A
pairing: matched response-normalized component-error budgets ON=repository_owned_candidate_holdout
real_structure: positive real common quadratic transfer
grading: exact conditional route comparison; no measured calibration
action_owner: repository-construction -- transfer ownership and apparatus remain unowned
target: K1058 and K1066 calibration routes MAP-TYPE=evaluation
```

Use K1058's exact three-mode budget

```text
eta_3(tau)=0.0102940997633828...
           -0.438235401419703... tau
```

and K1066's four-mode budget `E(n)`. The comparison assumes that the
three-mode gain unit equals the independently certified response floor used
for `eta/gamma` on the four-mode route. Under that matched normalization,
`eta_3(tau)=E(n)` at

| fourth mode | crossover `tau` |
| --- | ---: |
| `n=4`, `lambda=24` | 0.0179790532755852... |
| `n=8`, `lambda=80` | 0.0105839680374571... |
| `n=16`, `lambda=288` | 0.00643419420800405... |
| `n=64`, `lambda=4224` | 0.00293876343746661... |
| asymptotic fourth mode | 0.00168453237637074... |

Below a row's crossover the three-mode route tolerates more component error;
above it that four-mode route does. This does not create physical dominance:
three modes require an owned curvature box, while four modes require an extra
preparation, certified response floor and exact common-quadratic transfer
model.

The producer passes `13/13`; the hostile probe rejects `12/12` normalization,
budget, crossover, route, scope and promotion mutations.

## Next condition

State the cost-aware decision rule without inventing a preparation-cost model.
