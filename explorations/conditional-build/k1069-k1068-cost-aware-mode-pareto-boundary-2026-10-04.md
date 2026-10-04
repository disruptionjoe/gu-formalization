---
title: "K1069 cost-aware mode Pareto boundary"
status: active_research
doc_type: conditional_mode_cost_pareto_theorem
created: 2026-10-04
claim_ceiling: conditional Pareto theorem for increasing preparation costs; no cost model or apparatus choice
manifest: lab/process/k1069-k1068-cost-aware-mode-pareto-boundary.json
probe: tests/channel-swings/k1069_k1068_cost_aware_mode_pareto_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1069 cost-aware mode Pareto boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> design theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: least feasible fourth mode is uniquely cost-minimal for every strictly increasing preparation cost
carrier: K1066 monotone fourth-mode family LAYER=observed CHIRALITY=N/A
pairing: tolerance versus preparation cost ON=repository_owned_candidate_holdout
real_structure: ordered integer modes and scalar cost
grading: conditional Pareto theorem; physical cost function unmeasured
action_owner: repository-construction -- apparatus cost and target remain unowned
target: K1067 inverse design MAP-TYPE=evaluation
```

Let `E(n)` be K1066's strictly increasing tolerance and suppose physical
preparation cost `C(n)` is strictly increasing. For an independently fixed
target `rho<E_infinity`, K1067 supplies the least feasible integer

```text
n_min = min{n>=4 : E(n)>=rho}.
```

Every smaller mode fails the tolerance, while every larger mode costs more.
Therefore `n_min` is the unique minimum-cost feasible fourth-mode design. This
turns the K1067 table into a Pareto frontier without assigning any invented
cost values.

The theorem does not select `rho`, measure `C(n)`, or compare the extra-mode
cost against the three-mode curvature-calibration cost. Without those inputs,
neither `n=4`, a higher mode, nor the three-mode route is physically preferred.

The producer passes `8/8`; the hostile probe rejects `9/9` premise, target,
minimality, withheld-input, scope and promotion mutations.

## Next condition

Reconcile the completed candidate mathematics with every still-unowned
apparatus and GU-action row.
