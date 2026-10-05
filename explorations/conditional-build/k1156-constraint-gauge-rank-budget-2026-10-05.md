---
title: "K1156 constraint-gauge rank budget"
status: active_research
doc_type: positive_cohomology_rank_budget_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional necessary condition; no source map or functional realization
manifest: lab/process/k1156-constraint-gauge-rank-budget.json
probe: tests/channel-swings/k1156_constraint_gauge_rank_budget_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1156 constraint-gauge rank budget

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a general
> linear-algebra theorem used on a source-native Hessian later. It does not
> manufacture a source boundary map. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: constraint-codomain plus gauge-image rank budget
carrier: finite symmetric-form carrier LAYER=source-print CHIRALITY=N/A
pairing: symmetric H restricted to ker Q ON=constrained-carrier
real_structure: real finite coefficient space
grading: gauge image inside Hessian kernel and constraint kernel
action_owner: comparator -- source ownership required separately for Q and d
target: rad(H|ker Q)=im d MAP-TYPE=restriction
```

Let `H:V->V*` be symmetric, `d:G->V` obey `Hd=0`, and let
`Q:V->W` obey `Qd=0`. If

```text
rad(H restricted to ker Q)=im d,
```

then K1152 gives

```text
rank(Q restricted to ker H)=dim ker H-rank d.
```

Because this rank is at most `rank Q` and at most `dim W`, every successful
constraint satisfies the sharp necessary budget

```text
rank d + dim W >= dim ker H.                              (1)
```

For a combined constraint `Q=(Q_i)_i`, replace `dim W` by
`sum_i dim W_i`. Thus constraint output capacity and owned gauge image are
complementary resources for removing the nongauge Hessian radical. Target
dimension is only a ceiling: meeting (1) does not prove actual rank,
ownership, compatibility, positivity, propagation, or a common functional
domain. Producer and probe pass `8/8` and `8/8`.
