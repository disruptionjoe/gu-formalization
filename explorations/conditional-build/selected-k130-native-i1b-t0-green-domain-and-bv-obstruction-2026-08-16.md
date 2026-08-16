---
title: "Selected-K130 native I1B T=0 Green/domain and BV obstruction"
status: active_research
doc_type: exact_tracked_carrier_characteristic_green_radical_mixed_order_domain_obstruction
created: "2026-08-16"
registry: lab/process/selected-k130-native-i1b-t0-green-domain-and-bv-obstruction.json
probe: tests/channel-swings/selected_k130_native_i1b_t0_green_domain_and_bv_obstruction_probe.py
grade: "K130 TOTALIZES THE SERIALIZED 196-PLUS-24 DISTORTION CARRIER, NOT THE UNSERIALIZED ALL-GRADE SOURCE CARRIER. THE C PRINCIPAL AND GREEN COEFFICIENTS HAVE RANKS 24,24,22 AND RADICALS 196,196,198 ON TIMELIKE, SPACELIKE AND NULL CONORMALS. EVERY CONORMAL IS THEREFORE CHARACTERISTIC ON THIS TRACKED CARRIER. KAPPA_1 K IS ZERO ORDER: NONZERO KAPPA REMOVES THE ZERO-MOMENTUM ALGEBRAIC KERNEL BUT CANNOT CHANGE THE PRINCIPAL RANK, GREEN RADICAL, OR SUPPLY A NONCHARACTERISTIC CALDERON/SYMMETRIC-HYPERBOLIC DOMAIN. THE COUPLED HESSIAN IS MIXED ORDER, WITH A OF ORDER TWO AND C OF ORDER ONE, SO NO UNWEIGHTED COMMON CLOSED DOMAIN OR SCHUR/BV-BFV REDUCTION IS SELECTED. K131 MUST BUILD AN ACTION-OWNED CONSTRAINT SPLITTING, DOUGLIS-NIRENBERG WEIGHTS, BOUNDARY CLASS AND RADICAL REDUCTION BEFORE ANY CLOSED INVERSE OR PHYSICAL COHOMOLOGY."
target_claim: K129_NEXT_GATE__FULL_COVARIANT_CHARACTERISTIC_GREEN_COMMON_DOMAIN_AND_COUPLED_BV_BFV
target_verdict: TRACKED_CARRIER_GREEN_RADICAL_EXACT__EVERY_CONORMAL_CHARACTERISTIC__ZERO_ORDER_KAPPA_CANNOT_REPAIR_PRINCIPAL_OR_BOUNDARY_DEGENERACY__MIXED_ORDER_COMMON_DOMAIN_UNSELECTED__K131_CONSTRAINT_SPLIT
canon_verdict_change: none
---

# Selected-K130 native I1B T=0 Green/domain and BV obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, tracked-carrier principal-symbol, variational Green,
> mixed-order and constraint-domain calculation. Ordinary Einstein-action,
> fermionic K77, particle-spectrum, Higgs/VEV, family-index, chirality,
> anomaly and symmetry-breaking constructions do not adjudicate it without an
> explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this result binds the serialized `Cl1 full plus horizontal-Cl2`
distortion carrier of the source-native `I1B` Hessian at K127's local
Ricci-flat `T=0` fixed-boundary germ. It does not claim an all-grade source
totalization, a fermionic four-field domain, a source-global vacuum or a
selected physical boundary theory.

## Result in plain English

K129 identified

```text
C=kappa_1 K+E(D_B).
```

K130 now composes the dimensions that were held separately from the causal
ranks. The serialized distortion carrier is

```text
V_tr = V_Cl1 + V_hCl2,       dim V_tr = 196+24 = 220.       (1)
```

The derivative block changes parity. Its same-grade diagonal blocks vanish,
and its two cross directions each have rank `12,12,11`. Therefore both the
principal coefficient and its Green boundary coefficient have

```text
rank       = 24, 24, 22,
radical    = 196,196,198                                  (2)
```

on timelike, spacelike and null conormals. Thus the tracked distortion system
has no noncharacteristic conormal at all. The nonnull/null distinction remains
real—the null radical is two dimensions larger—but it is not an
invertible-versus-singular split.

## 1. Exact Green packet

Write the cross symbol as `R(n):V_Cl1 -> V_hCl2`. Formal variation of the
first-order `d_BT` Hessian gives the boundary coefficient, up to the fixed
nondegenerate pairing identifications and orientation sign,

```text
J(n) = [[0, R(n)^*],[-R(n),0]].                       (3)
```

Consequently `rank J(n)=2 rank R(n)` and
`rad J(n)=ker R(n) plus ker R(n)^*`. Equation (2) follows without choosing a
basis, projector or pseudoinverse. The exact probe also builds rational
positive witnesses for ranks `12` and `11` and fires wrong-rank and
same-grade-contamination plants.

The algebraic term `kappa_1 K` contains no normal derivative. It contributes
to the bulk Hessian but not to the Green concomitant. Hence

```text
J_C(n)=J_E(n)                                             (4)
```

for every `kappa_1`. Nonzero `kappa_1` can remove the zero-momentum algebraic
kernel, as K129 proved, but it cannot change (2), turn a characteristic
conormal into a noncharacteristic one, or select a boundary Lagrangian.

## 2. Analytic and mixed-order disposition

Three tempting routes are now excluded at the current carrier and grade.

1. **Elliptic/Calderon:** the principal symbol is singular for every nonzero
   conormal, so the ordinary elliptic Calderon route is unavailable.
2. **Unreduced symmetric hyperbolic:** the coefficient of every candidate
   time conormal has a radical of dimension at least `196`, so it is not a
   positive invertible time matrix on all `220` variables. A constrained
   hyperbolic formulation may still exist after an owned split.
3. **Direct Green polarization:** equation (3) is presymplectic, not
   symplectic, on the full trace carrier. A Lagrangian boundary condition is
   not defined until its radical is retained as constraint data or reduced by
   an action-owned complex.

The older K77 four-field domain packets do not repair this. Their nonnull
normal symbol has a distinct `1920`-dimensional carrier and rank `1920`.
Porting its inverse, symmetrizer or Majorana graph to (1) would be a carrier
and action-owner error.

The coupled quadratic Hessian is also not one ordinary first-order operator:

```text
H = [[0,A*],[A,C]],       ord(A)=2,       ord(C)=1.       (5)
```

Any closed realization must therefore state compatible
Douglis--Nirenberg/Sobolev weights, boundary traces, the operative adjoint and
constraint propagation. A formal inverse of a chosen realization of `C`
would make `-A* C^-1 A` roughly third order on its reducible complement; it
does not erase `ker A`, the Green radical, the null TT characteristics or
K127's Weyl leakage. No unweighted common domain, global inverse or physical
spectrum follows from (5).

## 3. BV-BFV consequence and next gate

The exact tracked radical is now data that a BV-BFV construction must explain,
not permission to quotient. At `T=0`, tensorial connection gauge motion adds
no independent `d chi` distortion column. The metric block retains its four
diffeomorphism directions, plus two further null TT principal
characteristics. The distortion radical is much larger and has not been
identified with ordinary gauge symmetry.

K131 must therefore construct, or obstruct, all of the following as one owned
packet:

```text
1. a covariant differential-algebraic constraint split of V_tr;
2. propagation of the 196/196/198 Green radicals;
3. Douglis-Nirenberg weights and closed bulk domains for (5);
4. an action-owned boundary class and operative A*;
5. the minimal BV/Koszul-Tate generators and BFV edge data;
6. only then, a legal reduced inverse or cohomology.
```

The all-grade source carrier remains a later totalization. No ledger, datum,
quotient, canon, public posture, particle interpretation, phenomenology or GU
truth-status claim changes. Joe input is not required.

## K131 successor classification

K131 constructs the exact fixed-stratum quotient: the causal
`(ker R,ker R*,radical,reduced)` dimensions are
`(184,12,196,24)`, `(184,12,196,24)` and `(185,13,198,22)`.
The null rank jump obstructs one regular constant-rank radical bundle across
all conormals. The mixed operator admits the relative DN weight family
`(s_g,s_T)=(1+a,a)`, `(t_g,t_T)=(2-a,1-a)`, but the normal symbol alone does
not propagate constraints and the distortion radical is not the image of an
action-owned gauge generator at `T=0`. Use K132's all-grade tangential and
subprincipal Noether-complex gate; do not promote the stratified quotient to
a global KT/BFV resolution or physical cohomology.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k130_native_i1b_t0_green_domain_and_bv_obstruction_probe.py
```
