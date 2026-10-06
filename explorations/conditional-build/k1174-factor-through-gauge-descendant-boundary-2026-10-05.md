---
title: "K1174 factor-through gauge-descendant boundary"
status: active_research
doc_type: exact_gauge_image_factorization_boundary
created: 2026-10-05
claim_ceiling: exact finite-symbol image theorem; no classification of every source gauge or KT generator
manifest: lab/process/k1174-factor-through-gauge-descendant-boundary.json
probe: tests/channel-swings/k1174_factor_through_gauge_descendant_boundary_probe.py
target_claim: SC-ACT-06
---

# K1174 factor-through gauge-descendant boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This distinguishes
> reparameterizations of the owned metric-diffeomorphism image from genuinely
> new field-space gauge directions. It does not assert that none exist.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: factor-through gauge-image rank ceiling
carrier: finite field space with base generator d0 LAYER=source-print CHIRALITY=N/A
pairing: future K132 quotient pairing ON=typed-future-candidate
real_structure: finite real symbols
grading: gauge parameters, gauge-for-gauge kernel and field-space image
action_owner: source-action -- only the current metric diffeomorphism image is owned
target: enlarged gauge/KT repair MAP-TYPE=homomorphism
```

For any finite family `d_j=d0 A_j`, the combined generator satisfies

`D=[d_1 ... d_m]=d0 A`, so `im D subset im d0` and `rank D<=rank d0`.

Gauge-for-gauge maps `r` with `d0 r=0` add parameter redundancy rather than
field-space image. A six-dimensional exact control has base rank two and five
factor-through columns still of rank two; a genuinely independent generator
adds two directions and raises the combined rank to four.

For K132, factor-through descendants of the current rank-four generator pay
none of the `98372/98372/106536` deficit. A pure-gauge repair would need total
gauge ranks `98376/98376/106540`, hence parameter-fibre dimensions at least as
large. Closed image, common domain, properness and physical cohomology remain
separate. Producer and hostile probe pass `12/12` and `11/11`.
