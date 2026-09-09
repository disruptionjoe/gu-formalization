---
title: "K181 order-three determinant exchange wave"
document_role: active_research
doc_type: conditional_native_K139_K181_order_three_exchange_determinant_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned grouping and certified outward numerical enclosures for all eight K179 order-three exchange kernels on the fixed K139--K179 equal-coupling two-edge positive particle/hole point control; four are rank-one species products and four are normalized whole 2x2 determinants with coincident-face cancellation preserved; no coherent multi-path order-four group, higher-order prefix, complete action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is evaluated
manifest: lab/process/k181-order-three-determinant-exchange-wave.json
solver: tests/channel-swings/k181_order_three_determinant_exchange.py
probe: tests/channel-swings/k181_order_three_determinant_exchange_probe.py
target_claim: INTERNAL_TARGET:K179_ORDER_THREE_MIXED_DETERMINANT_OUTWARD_GATE
target_claim_verdict: EIGHT_KERNELS_GROUPED_AND_EVALUATED__WHOLE_DETERMINANT_CANCELLATION_CERTIFIED__ORDER_FOUR_COHERENT_GRAM_GATE_OPEN
canon_verdict_change: none
---

# K181 order-three determinant exchange wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: the fixed K139/K156 hard-core `C3` impurity coupled to four
particle/hole bath species on `L2(R)`, auxiliary chart `lambda=256`, equal
couplings one, and the three normalized K162 zero-bath seed orbits. K181
consumes K179's coefficient-complete family and K180's normalization without
changing the operator, extension, state, polarization, domain or scalar
center.

```gu-typed-objects
result: the complete K179 order-three exchange family has eight orthogonal seed/output groups; four carry rank-one species products and four carry one normalized multiplicity-two exterior factor, whose whole antisymmetric difference is outwardly enclosed with its coincident-face zero preserved
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-three output sector; distinct seed/output signatures are orthogonal and every multiplicity-two species uses the normalized exterior projection ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering and real positive resolvent kernels
grading: conserved incidence charges, hard-core impurity state, bath species, bath number three, K179 path/contraction identity, ordered momentum provenance and specieswise exterior parity
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W=(E_R-256)I-X, and K179 fixes the coefficient-complete family; no source/GU action selects the physical extension, state, domain, polarization or scalar center
target: close the mixed rank-one/2x2 order-three numerical gate and identify the first coherent multi-path successor without claiming a through-order-twelve action column MAP-TYPE=intertwiner
```

## Inline preflight bookend

K180 leaves exactly eight order-three terms. Retrieval from the K179 generator
shows eight distinct `(seed,output_signature)` groups, so there are no
cross-path terms at this order. Four outputs have three different species and
are rank-one controls. Four repeat one species at momentum provenance `p1,p3`
and require one normalized `2x2` exterior determinant. The source register and
v0.263 ledger remain unchanged: `SC-META-53` is `UNCERTAIN`; `LT-SM8`,
`RA-F1` and `AC-F1` remain `NEEDS`.

The route census compared direct five-variable Gram cubature,
Laplace-simplex heat-kernel determinants, analytic contraction of `p2`,
factorization of the antisymmetric difference, and a transformed
Gauss--Legendre control. The selected route contracts `p2`, encloses the
rank-one function by monotonicity, and factors the determinant before any
interval operation.

## 1. Contracted kernel and whole determinant

Put `E_j=sqrt(1+p_j^2)` and

```text
D1=256+E1,
D2=256+E1+E2,
D3=256+E1+E2+E3,
D4=256+E1+E2+E3+E4.
```

With K180's `F` and `J`, define

```text
T(a,b,c)=[J(a,b)-J(a,c)]/(c-b)
        = int_R dp/[(E(p)+a)(E(p)+b)(E(p)+c)].
```

The common unsigned ordered kernel before point normalization is

```text
f(p1,p3,p4)=T(256+E1,256+E1+E3,256+E1+E3+E4)/(256+E1).
```

It is positive and separately decreasing in every `|p_j|`. For a repeated
species the normalized coordinate is formed first:

```text
A(p1,p3,p4)=(f(p_1,p_3,p_4)-f(p_3,p_1,p_4))/sqrt(2).
```

Direct subtraction of the complete positive integrands gives

```text
f13-f31=(E3-E1) int_R
 (512+E1+E3+E2) dp2 /
 [(256+E1)(256+E3)(256+E1+E2)(256+E3+E2)
  (256+E1+E3+E2)(256+E1+E3+E2+E4)].
```

The quotient is positive. Thus the coincident face `E1=E3` is identically
zero before squaring and before any interval enclosure; no cancellation is
reconstructed from separately rounded determinant entries.

## 2. Outward enclosures

The positive axes use two equal cells on `[0,1]` and on each dyadic octave
through `2^40`, giving `551,368` positive-octant cells. Rank-one cell extrema
come from coordinate monotonicity. Determinant cells use the exact energy-gap
interval multiplied by a positive quotient bound; lower bounds restrict the
contracted momentum to `[-1,1]`, while upper bounds cancel the common
cumulative denominator only after the whole difference is formed.

Weighted AM--GM gives

```text
f <= 4*256^(-1/2) (256+E1)^(-1) E3^(-7/8) E4^(-5/8).
```

Elementary one-dimensional power tails close every slab outside the cube.
For `A`, the already-formed identity `|A|^2 <= |f13|^2+|f31|^2` gives twice
the rank tail. After the point factor `(2*pi)^(-5/2)`, the certified squared-
norm intervals are

```text
1.712815441542719e-11 <= ||f||^2 <= 1.867828986007678e-9,
1.515601509941604e-17 <= ||A||^2 <= 3.770619474791643e-9.
```

The determinant lower endpoint is small because it is a rigorous sum over
cells whose energy intervals are disjoint; it is nonzero and carries no
sampling inference.

## 3. Independent same-family control and seed reconstruction

A separate transformed Gauss--Legendre calculation uses `p=sinh(x)`,
`x in [-12,12]`, and ordinary floating arithmetic. Orders 28 and 32 agree to
`3.66e-5` relatively for the rank kernel and `6.47e-5` for the determinant.
The order-32 values

```text
||f||^2 = 2.785886906990316e-11,
||A||^2 = 1.060231347943765e-11
```

lie inside the outward intervals. This is an independent normalization
control, not the proof of the interval.

K179's signs remain attached to the action coordinates. Since all eight
seed/output groups are orthogonal, seed zero has two rank and two determinant
copies, while seeds one and two each have one of each. Their certified squared-
norm intervals are respectively

```text
3.425633914288459e-11 <= ||v_0||^2 <= 1.127689692159864e-8,
1.712816957144230e-11 <= ||v_1||^2=||v_2||^2 <= 5.638448460799320e-9.
```

## 4. Scale replay

The mixed gate closes, but the single-output engine does not scale unchanged.
At order four, 24 terms occupy only 13 coherent seed/output groups. The seven multi-path groups
contain two to four signed terms. Their norms include cross-
path Gram entries between different contracted positions and momentum
provenances. From order five onward every term also has a repeated species.

The next exact object is therefore the seven multi-path order-four groups,
assembled as signed sums before specieswise determinant Gram enclosure. K181
does not declare those paths orthogonal, interval their terms separately, or
claim the K171/K168 action columns, `R_ref` residual, complement/flux floor,
scalar-center floor or K152 interval.

## Hostile result review

- **Strongest overclaim:** “The rank plus one determinant evaluator scales
  through order twelve.” Refused; order four already introduces coherent
  cross-path Gram sums.
- **Strongest cancellation attack:** interval the two determinant entries and
  subtract their bounds. Refused; the exact `(E3-E1)Q` factor is formed first.
- **Strongest normalization attack:** omit `1/sqrt(2)` or treat the four
  repeated outputs as two unrelated particles. The manifest and seed formulas
  pin the normalized exterior coordinate.
- **Strongest tail attack:** regard the finite cube as the Hilbert space. Both
  rank and determinant bounds include analytic all-octant complements.
- **Weakest remaining seam:** order-four paths with the same output signature
  interfere. Their complete signed Gram matrices have not been evaluated.

## Inline postflight bookend

All eight order-three kernels are grouped and evaluated at outward grade. The
four nontrivial normalized determinants retain their coincident-face zero and
agree with an independently implemented same-family quadrature. The scale
replay reaches the first new object at order four: seven coherent multi-path
groups requiring signed cross-path Gram assembly.

No physics mapping, source claim, ledger row, canon, paper, release or public
posture moved. The K171/K168 action columns and every downstream residual,
floor and K152 claim remain open.

## Reproduction

```bash
python3 tests/channel-swings/k181_order_three_determinant_exchange.py --demo
python3 tests/channel-swings/k181_order_three_determinant_exchange.py --quick
python3 tests/channel-swings/k181_order_three_determinant_exchange_probe.py
python3 tests/channel-swings/k181_order_three_determinant_exchange_probe.py --selftest
```
