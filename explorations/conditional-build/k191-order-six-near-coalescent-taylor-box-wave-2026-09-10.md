---
title: "K191 order-six near-coalescent Taylor-box wave"
document_role: active_research
doc_type: conditional_native_K139_K191_order_six_near_coalescent_taylor_box_result
created: 2026-09-10
date: 2026-09-10
claim_ceiling: rigorous repository-owned outward positivity boxes for every K186 size-two and size-three regularizer on minimum cross argument 2^-200 through 1/4 when each row and column spread is at most 1/512 of the local cell base, using an exact normalized divided-difference identity, symbolic Cauchy determinant cancellation and order-16 directed-Arb Taylor tails; no arbitrary gap-ratio cover, Duffy/Jacobi chain-rule remainder, complete positive-core error, outward order-six total, accurate prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation
manifest: lab/process/k191-order-six-near-coalescent-taylor-box-wave.json
solver: tests/channel-swings/k191_order_six_near_coalescent_taylor_box.py
probe: tests/channel-swings/k191_order_six_near_coalescent_taylor_box_probe.py
target_claim: INTERNAL_TARGET:K190_BIVARIATE_CONFLUENT_DIVIDED_DIFFERENCE_TAYLOR_BOX_GATE
target_claim_verdict: NEAR_COALESCENT_FINITE_GAPS_ARE_OUTWARDLY_POSITIVE_ON_THE_1_OVER_512_RELATIVE_SPREAD_BOX__THE_RESIDUAL_GAP_RATIO_SIMPLEX_AND_DUFFY_JACOBI_COMPOSITION_REMAIN_OPEN
canon_verdict_change: none
---

# K191 order-six near-coalescent Taylor-box wave

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
and complete K184--K190 order-six determinant family. K191 changes no operator,
extension, state, domain, polarization or scalar center. It enlarges K190's
fully coalescent point spine to one explicitly bounded finite-gap neighborhood.

```gu-typed-objects
result: all 53 K186 size-two and size-three regularizer patterns are outwardly positive on 1,648 contiguous radial cells covering minimum cross argument 2^-200 through 1/4 when each row and column spread is at most 1/512 of the local cell base; minimum directed-Arb lower bounds are 0.7670892463065684 and 0.07694420125335455 for sizes two and three
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 coherent path-pair assembly and K186 specieswise determinant factorization remain unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times, sequential confluent divided differences, normalized Bessel K1 kernel, exact Cauchy determinant cofactors, order-16 Taylor arithmetic and python-flint 0.9.0 / FLINT 3.6.0 Arb balls
grading: K186 exact Cauchy--Vandermonde skeleton, K188 four-region split, K190 exact coalescent scaled-q spine, 1,648-cell directed-Arb near-coalescent cover, 53-pattern and 468-occurrence conditional propagation, two 200-digit finite-gap controls and withheld residual-gap/cubature release
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, K179 fixes the coefficient family, K184 fixes the time Grams, K185/K188 fix boundary majorants and K186/K187/K189/K190 fix factorization, endpoint class, raw-kernel failure and coalescent coordinates; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: certify the first honest nonzero-gap neighborhood of K190's spine while preserving determinant cancellation, then expose the exact residual gap-ratio domain that must be covered before Duffy/Jacobi composition MAP-TYPE=intertwiner
```

## Inline preflight bookend

K190 removes the formal `0/0` at complete row and column coalescence, but its
positive Arb values are point certificates. K191 asks the next narrower
question: can a whole finite radial and gap-ratio box be enclosed without
forgetting the shared kernel dependence among four or nine determinant entries?

The strongest independently framed source-to-physics challenger remains the
positive physical quotient/count/chirality bridge. `SC-META-53` is
`UNCERTAIN`; ledger rows `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`. The
result below is a reusable determinant certificate, not a physical verdict.

Three interval routes were tested. Raw entrywise determinant balls reproduce
K189's correlation loss. Centering only the Bessel determinant still loses the
exact normalized Cauchy cancellation near zero. The selected route splits the
normalized kernel into the exact Cauchy core plus a rigorously enclosed Bessel
correction and expands the complete determinant around that core.

## 1. Exact normalized identity

Fix a positive cell base `x` and dimensionless nodes

```text
T_i = T_* + x r_i,
U_j = U_* + x c_j,
T_* + U_* = x(1+w).
```

With

```text
F_x(y) = x K1(x(1+y)),
D_ij = [r_0,...,r_i][c_0,...,c_j] F_x(w+r+c),
```

successive row and column Newton transforms give the exact regularizer

```text
R_m = det(D_ij) product_(a,b) (1+w+r_a+c_b).
```

The common radial scale cancels before interval evaluation. At zero offsets
this reduces exactly to K190's scaled-jet Hankel form.

## 2. Cancellation-preserving Taylor enclosure

Write

```text
F_x(y) = G(y) + H_x(y),       G(y)=(1+y)^-1.
```

For the pure Cauchy matrix `A` of divided differences, its determinant and the
normalizing product cancel exactly:

```text
product_(a,b)(1+w+r_a+c_b) det(A) = 1.
```

K191 therefore never asks interval arithmetic to rediscover that cancellation.
It evaluates the exact Cauchy cofactors for the terms linear in the correction
matrix `B`, and bounds the quadratic and cubic determinant residuals directly.
Each entry of `B` is an order-16 Taylor polynomial in `w,r,c`. Complete
monotonicity of `K1` supplies a signed Lagrange tail at the maximum admitted
argument. All rational node-polynomial ranges are computed exactly before
conversion to 120-digit Arb balls.

## 3. Outward box certificate

The certified domain is

```text
2^-200 <= minimum cross argument <= 1/4,
0 <= each row spread <= (cell base)/512,
0 <= each column spread <= (cell base)/512.
```

Adaptive subdivision uses eight cells on almost every dyadic radial band,
sixteen on `[2^-4,2^-3]` and sixty-four on `[2^-3,2^-2]`, for 1,648
contiguous cells total. Every size-two and size-three cell is strictly positive.

| Size | minimum `R_m` lower | maximum `R_m` upper | maximum entry-tail radius |
| --- | ---: | ---: | ---: |
| 2 | `0.7670892463065684` | `1.2329107536934316` | `2.4530697027193643e-11` |
| 3 | `0.07694420125335455` | `1.9230557987466455` | `7.750348707037974e-08` |

The widest cells near the top of the radial range remain positive without
assuming `R_m<=1`. That comparison is neither needed nor claimed.

## 4. Family propagation and independent controls

K186 contains 45 size-two patterns with 404 occurrences and eight size-three
patterns with 64 occurrences. Because the certificate depends only on size and
the stated node box, all 53 patterns and all 468 occurrences inherit it while
all 234 signed entries and 18 coherent groups remain intact.

Independent 200-digit Decimal divided differences at minimum cross argument
`2/25` give

| Size | control value | containing generic interval |
| --- | ---: | ---: |
| 2 | `0.9691391589199145922428842` | `[0.953900219174102, 1.046099780825898]` |
| 3 | `0.9420649596082352124610693` | `[0.630978727247566, 1.369021272752434]` |

These controls check a genuinely nonzero gap. They do not carry the proof.

## 5. Honest boundary and continuation

K191 does not cover a row or column spread greater than `1/512` of its local
radial base. The residual gap-ratio simplex must be stratified, with the same
normalized divided-difference model recentered on noncoalescent faces. Only a
union covering every K186 time-node pattern can be composed with the
Duffy/Jacobi chain rule and weighted cubature remainder.

No complete positive-core error or complete outward order-six total is
serialized. The accurate certified prefix remains through order five. No
K171/K168 action column, `R_ref` residual, complement or flux floor, selected
scalar center or K152 interval is evaluated. No source-native physical model,
Born rule, prediction or confirmation follows.

## Reproduction

```bash
_local/cas-venv/bin/python tests/channel-swings/k191_order_six_near_coalescent_taylor_box.py --summary
_local/cas-venv/bin/python tests/channel-swings/k191_order_six_near_coalescent_taylor_box.py --write --summary
_local/cas-venv/bin/python tests/channel-swings/k191_order_six_near_coalescent_taylor_box_probe.py
_local/cas-venv/bin/python tests/channel-swings/k191_order_six_near_coalescent_taylor_box_probe.py --selftest
```

The independent probe checks the exact rational Cauchy controls, complete
manifest topology, deterministic replay and all withheld-release fences. It
passes 17/17 baseline checks and catches 18/18 planted mutations.

## Inline postflight bookend

K191 achieves the intended intermediate result: the coalescent spine is no
longer merely pointwise evidence but has a rigorous outward nonzero-gap
neighborhood over the entire radial range used by the K188 core. The Run stops
honestly at the first uncovered region: larger relative time gaps. The next
work is a gap-stratified recentering wave, not a premature Duffy/Jacobi total or
physical interpretation.
