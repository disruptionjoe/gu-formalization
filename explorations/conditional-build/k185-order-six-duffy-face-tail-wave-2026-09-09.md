---
title: "K185 order-six Duffy face and radial-tail wave"
document_role: active_research
doc_type: conditional_native_K139_K185_order_six_time_gram_duffy_face_and_radial_tail_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned enumeration of all 1,864 determinant Leibniz support terms behind K184's 234 factorial-free order-six time-Gram entries, exact rational minimax AM--GM allocations with every primitive-time load at most two thirds, an equivalent Gamma-shape-six radial and Dirichlet/Duffy angular measure with every parameter at least one third, and explicit proof-safe whole-domain, simplex-face-strip and large-radius tail bounds on the fixed equal-coupling point control; the determinant-preserving compact-core cubature error remains open, so no accurate certified order-six prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is obtained
manifest: lab/process/k185-order-six-duffy-face-tail-wave.json
solver: tests/channel-swings/k185_order_six_duffy_face_tail.py
probe: tests/channel-swings/k185_order_six_duffy_face_tail_probe.py
target_claim: INTERNAL_TARGET:K184_ORDER_SIX_DUFFY_FACE_AND_TAIL_GATE
target_claim_verdict: ALL_234_TIME_GRAMS_AND_1864_LEIBNIZ_SUPPORT_TERMS_HAVE_EXACT_INTEGRABLE_DUFFY_WEIGHTS__ALL_SIMPLEX_FACES_AND_LARGE_RADIUS_TAIL_EXPLICITLY_BOUNDED__COMPACT_DETERMINANT_QUOTIENT_ERROR_OPEN
canon_verdict_change: none
---

# K185 order-six Duffy face and radial-tail wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: K184's fixed K139/K156 hard-core `C3` impurity control with auxiliary
chart `lambda=256`, equal couplings one and the three normalized K162 zero-bath
seed orbits. K185 changes no operator, extension, state, domain, polarization
or scalar center. Determinants are expanded only to certify a positive error
majorant; every numerical target remains the original complete determinant.

```gu-typed-objects
result: all 234 time-Gram entries and their 1,864 determinant Leibniz support terms admit exact rational minimax AM--GM allocations; every one of fourteen primitive-time loads is at most 2/3, so the equivalent radial weight has Gamma shape six and every Dirichlet/Duffy angular parameter is at least 1/3; explicit proof-safe face-strip and radial-tail errors leave only the compact determinant-core quadrature error open
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 specieswise Andreief reduction and coherent path-pair assembly are unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times and real Bessel K1 determinant kernels
grading: K184 coherent group and Gram-entry identity, left/right path, old positions, species determinant permutations, fourteen primitive increments, eight reciprocal support factors, rational allocation load and radial/angular weight
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W=(E_R-256)I-X, K179 fixes the coefficient family, and K184 fixes the exact time Grams; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: remove the singular-face and large-variable error obstruction from the K184 order-six determinant quadrature without mistaking an absolute error majorant for a narrow determinant evaluation MAP-TYPE=intertwiner
```

## Inline preflight bookend

K184 leaves one sharply typed analytic obstruction: its exact time-only Gram
formula has a proved `rho^5` radial origin, but no complete allocation of the
eight reciprocal Bessel singularities across the fourteen primitive times.
Without that allocation, neither theta/simplex faces nor the large-variable
tail can carry an outward error.

The incumbent question is whether every K184 entry admits a weighted Duffy
measure with explicit face and tail control. The strongest independently
framed source-to-physics challenger remains the positivity/state bridge:
`SC-META-53` is explicitly `UNCERTAIN`, while ledger-v0.263 row `LT-SM8`
still needs an action-owned physical quotient, domain and positive state-space
pairing. `RA-F1` and `AC-F1` remain downstream of a typed count observable and
physical chiral carrier. Their first executable discriminator cannot be run
without those absent constructions. They do not displace the present complete
internal input to K171/K168.

The route comparison included direct fourteen-dimensional boxes, tensor
Laguerre, sparse grids, pathwise momentum refinement, termwise cumulative-time
majorants and determinant-preserving weighted cubature. K184 already retired
the pathwise momentum route. Boxes and unweighted sparse grids encounter the
same singular faces. The selected route expands determinants only to derive a
finite positive majorant, solves the reciprocal-support allocation exactly,
and then returns to complete determinants for numerical work.

## 1. Complete reciprocal-support hypergraph

Each K184 Gram entry contains two old-position factors and six exterior
species factors. Expanding only the determinants' finite permutation sums
therefore yields eight positive `2 K_1` factors per term. Across all 234
entries there are exactly 1,864 Leibniz terms.

Write the primitive times as

```text
x = (s1,...,s7,v1,...,v7).
```

Every Bessel argument is a sum over one explicit support: `T_i`, `U_j`, or
`T_i+U_j`. Since

```text
(x K_1(x))' = -x K_0(x) < 0,   lim_(x->0+) x K_1(x)=1,
```

we have `K_1(x) <= 1/x` for every positive `x`. The common factors reduce to
`pi^-8` after combining `(2*pi)^-8` with all eight Bessel factors.

## 2. Exact minimax AM--GM allocation

For factor `a` with primitive-variable support `S_a`, choose nonnegative
weights `w_(a,i)` satisfying

```text
sum_(i in S_a) w_(a,i) = 1.
```

Weighted AM--GM gives

```text
1 / sum_(i in S_a) x_i
  <= product_(i in S_a) (w_(a,i) / x_i)^w_(a,i).
```

Let `alpha_i=sum_a w_(a,i)`. The solver minimizes `max_i alpha_i`, rationalizes
the solution, and replays every factor sum and variable load exactly. A
separate Hall bottleneck calculation over all 255 nonempty subsets of the
eight factors proves the same optimum:

```text
max_(A subset factors) |A| / |union_(a in A) S_a|.
```

Thus the rational solution is minimax-optimal, not merely feasible. The 1,864
terms split as follows:

```text
maximum load 4/7 : 1,374 terms
maximum load 7/12:   206 terms
maximum load 3/5 :   208 terms
maximum load 5/8 :    18 terms
maximum load 2/3 :    58 terms.
```

Every `alpha_i <= 2/3`. Therefore every Dirichlet parameter
`beta_i=1-alpha_i >= 1/3`, and every primitive face is integrable.

## 3. The weighted rho/Duffy measure

After applying the allocation, one Leibniz term is bounded by

```text
pi^-8 C_w exp(-256 sum_i x_i) product_i x_i^(-alpha_i),
C_w = product_(a,i) w_(a,i)^w_(a,i).
```

Put `x_i=rho z_i`, with `z` on `Delta_13`. Since every factor contributes
unit weight, `sum_i alpha_i=8`, hence

```text
sum_i beta_i = 14 - 8 = 6.
```

The radial/angular factorization is therefore

```text
rho^5 exp(-256 rho) d rho
  times product_i z_i^(beta_i-1) dDelta_13.
```

This is a Gamma shape-six radial law and a term-specific Dirichlet angular
law. The latter recursively factors into weighted Jacobi coordinates under a
standard Duffy map. Every Jacobi endpoint parameter is positive because every
primitive `beta_i` is at least `1/3`. This proves the requested rho-Laguerre
plus theta/simplex Duffy weight for all entries; it does not yet certify the
quadrature remainder of the determinant quotient.

## 4. Explicit proof-safe face and tail errors

The manifest carries the exact rational allocations and two levels of bound.
The sharpened gamma-formula controls evaluate

```text
pi^-8 256^-6 C_w product_i Gamma(beta_i)
```

and range from `4.70e-16` to `6.54e-15` after coherent-group summation. They
are floating controls, not the outward claim.

The proof-safe rational ceiling uses only elementary inequalities. For
`1/3 <= beta <= 1`, split the Gamma integral at one:

```text
Gamma(beta) < 3 + exp(-1) < 27/8.
```

Together with `pi>3` and `w^w<=1`, each Leibniz term is at most

```text
(27/8)^14 / (3^8 256^6) = 1.3471720091785483e-11.
```

The complete proof-safe coherent-group ceilings range from `4.85e-10` to
`4.36e-9`. These are still broad, but improve K184's proved pathwise group
ceilings by factors from `6.59e5` to `4.96e6`.

The radial tail at `rho>1/4` has Gamma survival factor

```text
Q(6,64) = exp(-64) sum_(k=0)^5 64^k/k!.
```

The finite Taylor lower bound gives `e>8/3`, so the proof uses
`exp(-64)<(3/8)^64`. The resulting group-tail ceilings range from
`2.57e-30` to `2.32e-29`.

For one Dirichlet coordinate with parameter `beta>=1/3` and total parameter
six, its beta-density denominator is at least `1/64`, while the integral over
`z_i<delta` is at most `3 delta^(1/3)`. A union bound over fourteen faces gives

```text
P(any z_i < delta) <= 2688 delta^(1/3).
```

At `delta=2^-180`, the proof-safe face-strip group ceilings range from
`1.13e-24` to `1.02e-23`. Thus every singular face and the infinite radial
tail now has an explicit error. The weights can also integrate those faces
directly rather than excising them.

## 5. Honest release boundary

The Gamma-formula majorants improve K184's pathwise certificate by roughly
`6.80e11` to `2.75e12`, but those values are numerical controls. Even the
proof-safe global ceilings remain many orders above the order-six QMC scale.
More importantly, neither global majorant evaluates the signed determinant
sum. The compact determinant-core error remains open.

Consequently the accurate certified prefix remains through order five. The
next gate is to factor every size-two/three Bessel determinant into its
ordered-time Vandermonde factors or certified divided differences, then
interval the bounded Duffy/Jacobi quotient on `rho<=1/4` and
`z_i>=2^-180`. That preserves the cancellations the majorant intentionally
forgets.

The source and physics-ledger statuses remain unchanged: `SC-META-53` remains
`UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`. No complete K171/K168 action
column, `R_ref` residual, complement or flux floor, scalar-center floor, K152
interval, physical/source selection, Born derivation, prediction,
confirmation, canon, paper, release or public-posture conclusion follows.

## Inline postflight bookend

- **Strongest advance:** all 1,864 singular support terms now have exact
  minimax weights and every simplex face plus the radial tail has a finite,
  explicit proof-safe error.
- **Strongest negative result:** the resulting global absolute ceiling is not
  a narrow order-six norm; it still discards determinant cancellation.
- **Strongest structural switch:** the unresolved boundary is now a bounded
  determinant quotient on a compact weighted core, not a singular face or
  infinite-domain tail.
- **Strongest overclaim:** “the Gamma-formula control certifies the order-six
  values.” Refused; only the rational ceiling carries the outward claim.
- **Strongest contrary route:** direct determinant interval boxes may avoid a
  divided-difference factorization, but near coincident times they risk the
  same subtraction loss K181--K184 were designed to avoid.
- **Weakest reproducibility seam:** the next rule must interval the factored
  determinant quotient itself; replaying allocation weights alone cannot
  certify the signed compact-core integral.

All seven admitted arcs were attempted and completed through their declared
release test. The complete support graph, rational minimax allocations,
Gamma/Dirichlet factorization, proof-safe bounds, independent sampled AM--GM
checks, release replay and hostile-review surfaces are present. The newly
isolated compact-core determinant error is the exact next dependency; no
compatible action-column work is released before it closes.

## Reproduction

```bash
python3 tests/channel-swings/k185_order_six_duffy_face_tail.py --summary
python3 tests/channel-swings/k185_order_six_duffy_face_tail.py --write --summary
python3 tests/channel-swings/k185_order_six_duffy_face_tail_probe.py
python3 tests/channel-swings/k185_order_six_duffy_face_tail_probe.py --selftest
```
