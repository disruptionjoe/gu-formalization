---
title: "K199 order-six first a/c-corners wave"
document_role: active_research
doc_type: conditional_native_K139_K199_order_six_first_ac_corners_result
created: 2026-09-13
date: 2026-09-13
claim_ceiling: rigorous outward determinant certificate for the first enlarged 63/128<=a,c<=65/128 square; no farther a,c complement, regularizer derivative envelope, Duffy/Jacobi remainder, complete positive-core error, outward order-six total, accurate prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation
manifest: lab/process/k199-order-six-first-ac-corners-wave.json
solver: tests/channel-swings/k199_order_six_first_ac_corners.py
probe: tests/channel-swings/k199_order_six_first_ac_corners_probe.py
target_claim: INTERNAL_TARGET:K198_FIRST_ENLARGED_A_C_SQUARE_GATE
target_claim_verdict: FIRST_ENLARGED_A_C_SQUARE_CERTIFIED__FARTHER_COMPLEMENT_AND_DUFFY_JACOBI_COMPOSITION_OPEN
canon_verdict_change: none
---

# K199 order-six first a/c-corners wave

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
and complete K184--K198 order-six determinant family. K199 changes no operator,
extension, state, domain, polarization or scalar center. It tests only the four
one-step corner boxes omitted by K198.

```gu-typed-objects
result: deterministic directed-Arb certificate over 524288 unique corner cells, representing 1048576 exact-transpose chart instances, with minimum lower bound 0.10160239635350186
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 coherent path-pair assembly and K186 specieswise determinant factorization remain unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times, sequential confluent divided differences, normalized Bessel K1 kernel, exact two-chart max-gap coordinates, one common scale-radial-three-shape cell supplying all entries before an outward complete-determinant enclosure, exact transpose symmetry, adaptive exact shape-axis subdivision, order-16 Taylor arithmetic and python-flint 0.9.0 / FLINT 3.6.0 Arb balls
grading: K186 exact Cauchy--Vandermonde skeleton, K188 four-region split, K190 exact coalescent scaled-q spine, K191/K192 outward radial/coalescent union, K193 shifted-entry identity and local face charts, K194 shared-scale ray, K195 exact compact ratios and coordinate star, K196 exact max-gap atlas and two open product blocks, K197 complete fixed-a,c q-to-1 corridor, K198 first symmetric a/c side-strip cross, K199 four-corner test, complete 53-pattern and 468-occurrence formula propagation, independent 200-digit controls and withheld complement/cubature release
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, K179 fixes the coefficient family, K184 fixes the time Grams, and K185/K188/K186--K199 fix boundary majorants, factorization and the tested coordinate region; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: certify the four one-step corner boxes and compose them exactly with K198's cross; retain farther shells as the next input before any Duffy/Jacobi differentiation MAP-TYPE=intertwiner
```

## Inline preflight bookend

K198 certified the first symmetric side-strip cross but deliberately omitted
the four boxes where both `a` and `c` leave K197's core. K199 keeps K198's 32
exact q slabs and the complete scale/radial grid, tests each corner separately,
and bisects the longer shape axis only if a complete-grid parent loses sign.
The joined enlarged square was rejected as an enclosure shortcut: a registered
representative cell has lower bound `-0.005929487132204682`. Each narrow corner
remained positive on the route scout, so the failure is dependency loss rather
than a regularizer counterexample.

The strongest source-to-physics challenger remains the positive physical
state/domain and quotient. `SC-META-53` is `UNCERTAIN`; `LT-SM8`, `LT-GR6b`,
`RA-F1` and `AC-F1` remain `NEEDS`. K199 constructs none of their missing
action-owned objects and earns no source or physical credit.

## 1. Four one-step corner boxes

The deterministic manifest records the four row-chart products

```text
[63/128,505/1024] x [63/128,505/1024]
[63/128,505/1024] x [519/1024,65/128]
[519/1024,65/128] x [63/128,505/1024]
[519/1024,65/128] x [519/1024,65/128]
```

for every `8227/10240<=q<=1`, `1<=t<=8`, and
`31/256<=x<=1/8` cell. One shared `(t,w,a,q,c)` interval supplies every
shifted entry, the common normalization and the complete determinant. Exact
row/column transpose supplies the companion chart instances.

All 32 q slabs and all four corners per slab pass without shape subdivision:
128 accepted corner tiles, 524,288 unique directed-Arb cells and 1,048,576
row/column chart instances by exact transpose. The global size-three corner
range is

```text
0.10160239635350186 <= R <= 1.6750051233762688,
maximum shifted-entry tail <= 0.00047089144223947955.
```

The maximum adaptive depth used is zero. All 1,056 independent 200-digit
boundary controls lie inside that outward range. The baseline probe passes
48/48 checks, catches all 28 planted hostile mutations, and the serialized
single-thread source replay reconstructs the manifest exactly.

## 2. Exact remaining gate

Even if the four boxes pass, K199 closes only the first enlarged
`63/128<=a,c<=65/128` square. It does not cover farther parts of `(0,1)^2`.
Successive adaptive symmetric shells therefore remain necessary before the
program may differentiate the common-cell regularizer and compose the
coordinate-chain Duffy/Jacobi cubature remainder.

The complete positive-radius core error, outward order-six total, accurate
prefix, action columns, residual/floor gates, scalar center and K152 interval
remain open. No source, ledger, canon, paper, release, public-posture,
physical-selection, Born, prediction or confirmation verdict changes.

## Reproduction

```bash
_local/cas-venv/bin/python tests/channel-swings/k199_order_six_first_ac_corners.py --write --progress
_local/cas-venv/bin/python tests/channel-swings/k199_order_six_first_ac_corners_probe.py --progress
_local/cas-venv/bin/python tests/channel-swings/k199_order_six_first_ac_corners_probe.py --no-replay --selftest
```

## Inline postflight bookend

- **Strongest advance:** all four one-step corner boxes are strictly positive
  over the complete accepted q and scale/radial grids, so their exact union
  with K198 closes the first enlarged `63/128<=a,c<=65/128` square.
- **Strongest overclaim:** “K199 proves the complete determinant-positive
  ordered-shape atlas.” Refused: all farther `a,c` shells remain untested.
- **Strongest contrary construction:** the joined full square loses interval
  sign on a registered representative cell; the separately scoped corners are
  the admitted dependency-preserving route.
- **Weakest reproducibility seam:** the certificate requires a complete
  single-thread pass over every accepted corner product cell; the independent
  replay is exact but intentionally expensive.
- **Next route:** continue adaptive symmetric outer shells, then derive the
  regularizer derivative and weighted Duffy/Jacobi remainder envelopes.
