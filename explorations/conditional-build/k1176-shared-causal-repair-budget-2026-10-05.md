---
title: "K1176 shared causal repair budget"
status: active_research
doc_type: exact_shared_causal_repair_budget
created: "2026-10-05"
claim_ceiling: exact finite-symbol necessity under a stratum-independent rank ceiling; no source construction
manifest: lab/process/k1176-shared-causal-repair-budget.json
probe: tests/channel-swings/k1176_shared_causal_repair_budget_probe.py
target_claim: SC-ACT-06
---

# K1176 shared causal repair budget

> K1173 priced the causal strata separately. K1176 asks what one uniformly
> bounded repair packet must be able to carry across all three. It does not
> assert that the ranks of an actual differential are constant by stratum.

## Theorem

Let the favorable K132 deficits be

```text
D_timelike = D_spacelike = 98372,   D_null = 106536.
```

Suppose one proposed packet has stratum-independent ceilings `H,G,C` on added
Hessian rank, genuinely new gauge-image rank and genuinely new constraint rank.
If it repairs every causal stratum, then each K1173 inequality holds, hence

```text
H + G + C >= max_s D_s = 106536.
```

The null stratum dominates. At the shared floor the nonnull inequalities have
slack `106536-98372=8164`.

If the ranks actually vary with causal type, no maximum shortcut is licensed:
retain all three pointwise K1173 inequalities. This distinction prevents a
uniform design budget from being misreported as a measured symbol rank.

The producer passes `10/10` controls and the hostile probe rejects `10/10`
mutations. SC-ACT-06 and all protected dispositions remain unchanged.
