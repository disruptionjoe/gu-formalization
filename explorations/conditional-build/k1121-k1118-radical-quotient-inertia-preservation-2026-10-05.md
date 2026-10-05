---
title: "K1121 radical-quotient inertia preservation"
status: active_research
doc_type: exact_radical_quotient_inertia_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional and fibrewise necessity; no global physical quotient
manifest: lab/process/k1121-k1118-radical-quotient-inertia-preservation.json
probe: tests/channel-swings/k1121_k1118_radical_quotient_inertia_preservation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1121 radical-quotient inertia preservation

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> reduction boundary, not a conventional gauge-theory import. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: radical-quotient inertia theorem applied after K1118
carrier: finite real Hessian fibre V with gauge image G LAYER=source-print CHIRALITY=N/A
pairing: self-adjoint Hessian form H ON=V
real_structure: real finite-symbol carrier
grading: gauge radical versus nonzero-sign sectors
action_owner: source-action -- K128/K129 at local T=0 grade
target: descended form on V/G MAP-TYPE=quotient
```

If `G` lies in the radical of a self-adjoint form `H`, then `H` descends to
`V/G`, and a basis adapted to `G` shows

```text
inertia(H_bar)=(n_+(H),n_-(H),n_0(H)-dim G).
```

Thus a genuine gauge quotient killed by the Hessian removes only null
directions. It cannot remove one negative direction. The exact control
`diag(-3,0,2,5)` quotiented by its zero coordinate changes inertia from
`(2,1,1)` to `(2,1,0)`.

This closes a false repair of K1118: calling the metric kernel “gauge” does not
turn the mixed Hessian positive. A positive reduction must impose an additional
constraint subspace before quotienting its residual radical. The result is
fibrewise; it supplies no global closed domain, constraint propagation or
physical cohomology. The producer passes `9/9`; the hostile probe rejects
`9/9` mutations.
