---
title: "K1166 stacked constraint rank split"
status: active_research
doc_type: exact_finite_constraint_rank_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional necessary theorem; no source coupling or functional realization
manifest: lab/process/k1166-stacked-constraint-rank-split.json
probe: tests/channel-swings/k1166_stacked_constraint_rank_split_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1166 stacked constraint rank split

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a general
> finite-dimensional theorem used on separately typed source-native channels.
> It does not identify either channel with a K132 bulk constraint.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact stacked-channel rank identity
carrier: K=ker H with supplied gauge image im d LAYER=toy CHIRALITY=N/A
pairing: symmetric H restricted to a future constrained kernel ON=typed-future-candidate
real_structure: finite real vector spaces
grading: Hessian kernel, gauge image, first channel, second-channel complement
action_owner: N/A -- theorem only
target: radical-capture necessity MAP-TYPE=evaluation
```

For linear maps `q:K->W_q` and `ell:K->W_ell`, project the image of
`(q,ell)` onto `im q`. Its kernel is exactly the image of `ell` on
`K intersect ker q`. Rank-nullity gives

`rank(q,ell)|K = rank q|K + rank ell|(K intersect ker q)`.

Equivalently, the overlap defect
`delta=rank q+rank ell-rank(q,ell)` is nonnegative. If
`rad(H|ker(q,ell))=im d`, then the stack must be injective on `K/im d`, so
its rank is `dim K-rank d` and necessarily
`dim K-rank d <= dim W_q+dim W_ell`.

The exact six-dimensional fixture has channel ranks two and three, stacked
rank four, and overlap defect one. The theorem is necessary only: it supplies
no source coupling, propagation, common domain, positivity, or physical
quotient. Producer and hostile probe pass `10/10` and `12/12`.
