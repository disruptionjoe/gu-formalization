---
title: "K182 order-four coherent Gram wave"
document_role: active_research
doc_type: conditional_native_K139_K182_order_four_coherent_gram_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned canonical exterior-coordinate assembly for all 24 K179 order-four exchange paths, rigorous finite global outward intervals for all 40 self/cross Gram entries including the 34 entries in seven multi-path groups, and localized cancellation-first positive lower witnesses for all 13 coherent group norms on the fixed equal-coupling point control; no order-five-through-twelve numerical prefix, complete action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is evaluated
manifest: lab/process/k182-order-four-coherent-gram-wave.json
solver: tests/channel-swings/k182_order_four_coherent_gram.py
probe: tests/channel-swings/k182_order_four_coherent_gram_probe.py
target_claim: INTERNAL_TARGET:K179_ORDER_FOUR_COHERENT_GRAM_GATE
target_claim_verdict: ALL_THIRTEEN_GROUPS_ASSEMBLED__ALL_GRAM_ENTRIES_OUTWARDLY_ENCLOSED_AFTER_EXTERIOR_PROJECTION__ALL_GROUP_NORMS_CERTIFIED_NONZERO__ORDER_FIVE_NUMERICAL_GATE_OPEN
canon_verdict_change: none
---

# K182 order-four coherent Gram wave

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
couplings one, and the three normalized K162 zero-bath seed orbits. K182
consumes K179's coefficient-complete exchange family and K181's point/exterior
normalization. It changes no operator, extension, state, polarization, domain
or scalar center.

```gu-typed-objects
result: all 24 coefficient-complete paths at order four map to 13 canonical output groups; every path is completely normalized and antisymmetrized specieswise before any interval operation, all 40 unique Gram entries are outwardly enclosed, and localized complete-sum intervals certify all 13 coherent groups are nonzero
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-four output sector; distinct seed/output signatures are orthogonal and each common-signature path pair is paired only after complete normalized specieswise exterior projection ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering and real positive contracted resolvent kernels
grading: conserved incidence charges, hard-core impurity state, bath species, bath number four, K179 path/contraction identity, contracted position, ordered momentum provenance and specieswise exterior parity
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W=(E_R-256)I-X, and K179 fixes the coefficient-complete family; no source/GU action selects the physical extension, state, domain, polarization or scalar center
target: close the complete order-four coherent Gram gate without claiming a higher-order action column or physical state MAP-TYPE=intertwiner
```

## Inline preflight bookend

K181 leaves exactly 24 order-four terms. Retrieval against K179 groups them
by `(seed_impurity, output_signature)` into 13 orthogonal outputs: six
singletons and seven coherent multi-path groups, with group sizes two, three
or four. The 24 records use contracted positions one or three and retain their
individual K179 coefficient, old position, output-letter order and surviving
momentum provenance.

The incumbent question is the first complete coherent exchange-vector gate
needed by the K171/K168 action column. The strongest independently framed
physics challenger remains the state/positivity bridge (`SC-META-53`,
`LT-SM8`), but its physical action, domain and state selector are still absent;
the K179 order-four internal gate is executable without inventing them. The
source register and v0.263 physics ledger therefore remain unchanged:
`SC-META-53` is `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`.

The route census compared direct five-dimensional cubature, divided-
difference reduction, canonical exterior-coordinate assembly, entrywise
determinant bounds, Cauchy bounds after complete projection, localized
interval witnesses and independent full-half-line quadrature. Direct
entrywise bounds were rejected because they erase determinant zeros and
cross-path cancellation. The selected route fixes one canonical species-slot
basis per output, forms every complete exterior coordinate, proves a global
integrable majorant, encloses every Gram entry, and uses local complete-sum
boxes for positive lower witnesses. Gauss--Laguerre in the positive `asinh`
coordinate is kept separate as a normalization/interference control and is
not the outward proof.

## 1. Canonical exterior coordinates

For one K179 term `t`, let `L_t=(ell_1,...,ell_4)` be its ordered output
species, let `nu_t=(j_1,...,j_4)` be its surviving momentum provenance, and
let `c_t in {+1,-1}` be its exact W coefficient. For canonical momenta grouped
by species, K182 defines

```text
Psi_t(x) = c_t (2*pi)^(-3) / sqrt(product_s m_s!)
           * sum_(pi in product_s S_(m_s)) sgn(pi)
             int_R dp_old product_(r=1)^5 D_r(p)^(-1),
D_r = 256 + sum_(j<=r) sqrt(1+p_j^2).
```

The permutation sends the canonical momentum slots for each species into the
ordered positions `L_t`; the surviving positions are exactly `nu_t` and the
remaining position is K179's recorded contracted variable. A coherent output
is

```text
Psi_G = sum_(t in G) Psi_t,
||Psi_G||^2 = sum_(s,t in G) <Psi_s,Psi_t>.
```

Thus coefficients, exterior signs and cross-path interference are assembled
before any interval operation. K182 never encloses determinant entries and
then subtracts them.

## 2. Global outward Gram enclosure

Each cumulative denominator is allocated by weighted AM--GM among `256` and
energies actually present in that denominator. For contracted position one,
the resulting energy exponents are

```text
(alpha_1,alpha_2,alpha_3,alpha_4,alpha_5)
  = (1.20,0.75,0.65,0.60,0.60).
```

For contracted position three they are

```text
(alpha_1,alpha_2,alpha_3,alpha_4,alpha_5)
  = (0.90,0.90,1.20,0.60,0.60).
```

The contracted exponent exceeds one. Every exterior squared exponent exceeds
one. Therefore every factor is finite using

```text
int_R (1+p^2)^(-a/2) dp
  = sqrt(pi) Gamma((a-1)/2) / Gamma(a/2),  a>1.
```

The complete exterior sum is formed first and then bounded by its number of
permutations. This yields one finite `U_t >= ||Psi_t||^2` for every path.
Only afterwards K182 applies

```text
|<Psi_s,Psi_t>| <= sqrt(U_s U_t).
```

All 40 unique self/cross entries across the 13 groups are therefore enclosed;
34 self/cross entries belong to the seven multi-path groups and six are the
singleton self-controls. The broad coherent upper endpoints range from
`9.307425024879368e-9` to `1.261953157450171e-6`. These global intervals alone
have zero lower endpoint; K182 does not call them nonzero certificates.

## 3. Localized nonzero witnesses

For a positive canonical momentum box, every outer energy has a monotone
interval. The contracted positive axis is divided into 128 cells on `[0,1]`
and 128 cells on every dyadic octave through `2^40`; reflection supplies the
negative axis. On each contracted cell all five denominators are bounded
simultaneously. Beyond the cutoff, if the contracted position is `r=1` or
`r=3`, respectively,

```text
product_j D_j^(-1) <= E_old^(-5),
product_j D_j^(-1) <= (D_1 D_2)^(-1) E_old^(-3),
```

and the elementary power tail closes the integral. Every species permutation
and every K179-signed path is then added as one interval. No summand is squared
or paired before the complete coherent coordinate is present.

The resulting complete-coordinate intervals exclude zero in one explicit box
for each output. Consequently all 13 coherent groups are nonzero. Multiplying
the squared amplitude floor by the four-dimensional box volume gives rigorous
group norm-square lower bounds from `5.187463839453910e-57` to
`4.346367334812746e-55`, except the four-path seed-zero mixed group whose
deliberately tiny box gives `1.060673805386460e-57`. Combined with the global
upper bounds, these are honest but intentionally wide full-norm intervals.
Their purpose is existence plus complete Gram bookkeeping, not a sharp action
coefficient.

## 4. Independent same-family control

A separately implemented quadrature uses full-half-line Gauss--Laguerre in
`p=sinh(t)`, explicitly including momentum reflection. Orders `(14,28)` and
`(16,32)` for exterior and contracted coordinates agree groupwise within
`5.18e-2` relatively. Every fine value lies inside its rigorous global
interval. Representative fine squared norms are

```text
seed 0 mixed four-path group: 4.183427831416617e-14
double-1 and double-2 two-path groups: 1.512611477094638e-15
seed 1/2 mixed three-path groups: 5.33505745064144e-15
```

The complete seedwise order-four controls are

```text
seed 0: 4.485950126835545e-14
seed 1: 1.806747693898397e-14
seed 2: 1.806747693898400e-14.
```

The seed-one/seed-two equality is a flavor-swap control. These values check
normalization, signs and interference; they are not the outward proof and are
not substituted for the certified wide intervals.

## 5. Higher-order replay and exact stop

The canonical group/exterior map is structurally defined for every K179 term
through order twelve. The numerical majorants in this packet are deliberately
implemented only for the order-four contracted-position classes `{1,3}`.
Order five changes the class: its 32 paths occupy 12 groups, all 12 are
multi-path, contracted positions are `{2,4}`, and 64 unique Gram entries plus
160 exterior summands per point must be controlled.

In plain terms, contracted positions 2 and 4 are the next numerical gate.

The growth is not hidden. At order twelve the family has 1,152 paths, 33
groups, 35,352 unique Gram entries, a maximum group size of 120, and
19,609,920 exterior summands per evaluation point. A literal extension of the
order-four enumerator is therefore not an honest scale route. The next gate is
to derive integrable cancellation-first majorants for positions two and four,
evaluate the 12 order-five groups, and determine the representation/compression
needed before scaling further.

No order-five-through-twelve numerical prefix, complete K171/K168 action
columns, `R_ref` residual, complement or flux floor, scalar-center floor or
K152 interval is claimed.

The K171/K168 action columns therefore remain explicitly unevaluated.

## Inline postflight bookend

The strongest overclaim would be to call the independent quadrature a sharp
certificate or to infer action-column convergence from one positive order.
The strongest mistyping would be to pair raw ordered kernels before their
specieswise exterior projections. The weakest reproducibility seam is the
width of the global Cauchy bounds; the localized intervals prove nonzero but
do not yet provide action-useful lower normalization.

The exact K179 pin, all 24 path identities, 13 groups, 40 Gram entries, 13
localized witnesses, independent control, flavor-swap equality, higher-order
census and downstream fences are machine checked. This is a repository-
internal conditional construction, not a source result or physical state.
`SC-META-53` remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain
unchanged at `NEEDS`. Repository-wide priority and unrelated channel order are
unchanged.

## Reproduction

```bash
python3 tests/channel-swings/k182_order_four_coherent_gram.py --quick
python3 tests/channel-swings/k182_order_four_coherent_gram.py --demo
python3 tests/channel-swings/k182_order_four_coherent_gram_probe.py
python3 tests/channel-swings/k182_order_four_coherent_gram_probe.py --selftest
```
