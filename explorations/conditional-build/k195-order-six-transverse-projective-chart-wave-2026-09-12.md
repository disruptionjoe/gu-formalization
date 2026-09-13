---
title: "K195 order-six transverse projective coordinate-star wave"
document_role: active_research
doc_type: conditional_native_K139_K195_order_six_transverse_projective_coordinate_star_result
created: 2026-09-12
date: 2026-09-12
claim_ceiling: rigorous repository-owned transverse coordinate-star for the K186 size-two and size-three regularizers on 31/256<=x<=1/8 and 1<=s<=8, with exact compact ratio coordinates, positive Jacobian, 13,312 directed-Arb cells across the a, b and c axes, exact common intersection with K194 and the inherited K193/K192 face join, and 24 independent 200-digit controls; no open three-dimensional transverse neighborhood, complete max-gap atlas, Duffy/Jacobi derivative envelope, complete positive-core error, outward order-six total, accurate prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation
manifest: lab/process/k195-order-six-transverse-projective-chart-wave.json
solver: tests/channel-swings/k195_order_six_transverse_projective_chart.py
probe: tests/channel-swings/k195_order_six_transverse_projective_chart_probe.py
target_claim: INTERNAL_TARGET:K194_TRANSVERSE_ORDERED_SHAPE_ATLAS_GATE
target_claim_verdict: EXACT_COMPACT_RATIO_COORDINATES_AND_THREE_TRANSVERSE_AXIS_SWEEPS_CERTIFIED__PRODUCT_CHART_MAX_GAP_ATLAS_AND_DUFFY_JACOBI_COMPOSITION_REMAIN_OPEN
canon_verdict_change: none
---

# K195 order-six transverse projective coordinate-star wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: K186's fixed K139/K156 hard-core `C3` impurity control, auxiliary chart
`lambda=256`, equal couplings one, three normalized K162 zero-bath seed orbits,
and complete K184--K194 order-six determinant family. K195 changes no
operator, extension, state, domain, polarization or scalar center. It builds
three transverse coordinate sweeps through the K194 projective ray.

```gu-typed-objects
result: the K194 projective ray admits exact compact shape coordinates and a rigorously positive three-axis transverse coordinate-star; 1,024 size-two and 12,288 size-three directed-Arb cells are strictly positive on 1<=s<=8 and 31/256<=x<=1/8, with minimum lower bounds 0.8809314856771806 and 0.15007268290327777
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 coherent path-pair assembly and K186 specieswise determinant factorization remain unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times, sequential confluent divided differences, normalized Bessel K1 kernel, exact compact projective ratio map, one common scale-radial-shape-axis cell supplying all entries before an outward complete-determinant enclosure, order-16 Taylor arithmetic and python-flint 0.9.0 / FLINT 3.6.0 Arb balls
grading: K186 exact Cauchy--Vandermonde skeleton, K188 four-region split, K190 exact coalescent scaled-q spine, K191/K192 outward radial/coalescent union, K193 exact shifted-entry identity and local face charts, K194 shared-scale ray, K195 exact projective coordinates and three joined transverse axis sweeps, complete 53-pattern and 468-occurrence formula propagation, 24 independent 200-digit controls and withheld product-atlas/cubature release
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, K179 fixes the coefficient family, K184 fixes the time Grams, K185/K188 fix boundary majorants and K186--K194 fix factorization, endpoint class, coalescent coordinates, shifted local operator and projective ray; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: retain K194's projective scale while varying each compact ordered-shape ratio through an outward interval, prove their common intersection and exact face join, and expose the missing product-chart complement before Duffy/Jacobi differentiation MAP-TYPE=intertwiner
```

## Inline preflight bookend

K194 proves positivity only on
`(r1/r0,c0/r0,c1/c0)=(1/2,4/5,1/2)`. The strongest source-to-physics
challenger remains the positive physical state/domain and quotient:
`SC-META-53` is `UNCERTAIN`, while `LT-SM8`, `LT-GR6b`, `RA-F1` and `AC-F1`
remain `NEEDS`. This result supplies none of their action, quotient,
cohomology, count-observable or chiral-carrier debts.

The route census compared total positivity, an independent-coordinate hull,
direct product boxes, common-cell interval arithmetic, exact ratio geometry,
and adaptive axis sweeps. Andreief proves pointwise positivity but supplies no
quantitative cubature error. Independent and even small product boxes lose too
much determinant dependence. The selected coordinate-star route therefore
tests each transverse direction without pretending their Cartesian product is
certified.

## 1. Exact compact projective coordinates

Define

```text
r0=s/32,  r1=s*a/32,  c0=s*b/32,  c1=s*b*c/32.
```

On `s>0`, `b>0`, the inverse is
`s=32r0`, `a=r1/r0`, `b=c0/r0`, `c=c1/c0`. The exact Jacobian is

```text
det d(r0,r1,c0,c1)/d(s,a,b,c) = s^3 b / 1048576 > 0.
```

Thus `0<a,c<1` is exactly the ordered interior `r0>r1>0`, `c0>c1>0` in
this chart. K194 is the section `(a,b,c)=(1/2,4/5,1/2)`.

## 2. Directed-Arb transverse coordinate star

K195 holds two shape variables at the K194 value while varying the third over

```text
511/1024 <= a <= 513/1024,
8187/10240 <= b <= 8197/10240,
511/1024 <= c <= 513/1024.
```

For every scale/radial/shape-axis cell, one shared interval tuple supplies all
shifted divided-difference entries and the common normalization before the
complete determinant is enclosed. Taylor centers are quantized outward to a
`1/512` grid and the radius is enlarged to contain the full argument interval;
this reduces repeated Bessel evaluations without weakening enclosure.

| Size | Sweeps | Outward cells | Minimum `R_m` lower | Maximum `R_m` upper |
| --- | --- | ---: | ---: | ---: |
| 2 | `b` | 1,024 | `0.8809314856771806` | `0.99165658418384` |
| 3 | `a`, `b`, `c` | 12,288 | `0.15007268290327777` | `1.6275342239748118` |

All 13,312 cells are strictly positive and each scale, radial and varying-axis
interval is contiguous. The three size-three sweeps meet on the complete K194
ray; at `s=1` they contain the exact K193 fully active face center, whose K192
join is inherited from the predecessor certificate. Twenty-four independent
200-digit divided-difference controls at scale endpoints and shape endpoints
lie inside the global outward ranges.

## 3. Honest boundary and continuation

A coordinate star is a union of three two-dimensional surfaces in the
four-dimensional gap space. It proves directional transverse stability but
contains no open three-dimensional shape neighborhood. In particular, the
failed product-box scout is not a counterexample: it is another dependency-
loss event in the enclosure.

The exact next input is a two-chart max-gap atlas. Use `max(r0,c0)` as scale,
compactify the balance ratio separately on the row-dominant and column-
dominant charts, preserve complete determinants, and cover the product-shape
complement. Only then differentiate the common-cell model and compose the
derivatives with K185's Duffy/Jacobi weights and K188's endpoint split.

## Reproduction

```bash
_local/cas-venv/bin/python tests/channel-swings/k195_order_six_transverse_projective_chart.py --summary
_local/cas-venv/bin/python tests/channel-swings/k195_order_six_transverse_projective_chart.py --write --summary
_local/cas-venv/bin/python tests/channel-swings/k195_order_six_transverse_projective_chart_probe.py
_local/cas-venv/bin/python tests/channel-swings/k195_order_six_transverse_projective_chart_probe.py --no-replay --selftest
```

The probe checks the exact coordinate map and Jacobian, 13,312 cell counts and
lower bounds, all joins, 24 independent controls, complete-family propagation,
deterministic replay, and every withheld-release fence.

## Inline postflight bookend

K195 turns the K194 ray into three rigorously joined transverse axis sweeps and
identifies the first honest multidimensional obstacle: product cells still
destroy too much determinant dependence. No source, physics-ledger, canon,
paper, release, Born, prediction, confirmation or public-posture effect follows.
