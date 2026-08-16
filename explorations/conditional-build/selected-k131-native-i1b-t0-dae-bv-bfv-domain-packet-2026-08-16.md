---
title: "Selected-K131 native I1B T=0 DAE, weighted-domain, and minimal BV-BFV packet"
status: active_research
doc_type: exact_stratified_constraint_split_douglis_nirenberg_boundary_bv_bfv_obstruction
created: "2026-08-16"
registry: lab/process/selected-k131-native-i1b-t0-dae-bv-bfv-domain-packet.json
probe: tests/channel-swings/selected_k131_native_i1b_t0_dae_bv_bfv_domain_packet_probe.py
grade: "K131 CONSTRUCTS THE MAXIMAL EXACT FINITE-SYMBOL CONSTRAINT PACKET ON K130'S SERIALIZED 220-DIMENSIONAL CARRIER. ON EACH FIXED-RANK CAUSAL STRATUM THE GREEN FORM REDUCES TO A SYMPLECTIC QUOTIENT OF DIMENSION 24,24,22, WITH RADICAL SPLIT DIMENSIONS (184+12),(184+12),(185+13). THE TWO-DIMENSION NULL RANK JUMP OBSTRUCTS ONE SMOOTH CONSTANT-RANK COVARIANT RADICAL BUNDLE ACROSS CONORMALS CROSSING THE NULL STRATUM. THE NORMAL SYMBOL ALONE DOES NOT PROPAGATE ITS LEFT-NULL CONSTRAINTS: TANGENTIAL AND SUBPRINCIPAL COEFFICIENTS ARE REQUIRED. THE MIXED HESSIAN ADMITS THE UNIQUE RELATIVE DOUGLIS-NIRENBERG WEIGHT FAMILY S=(1+A,A), T=(2-A,1-A), INCLUDING H2(G) PLUS H1(T) TO H-1 PLUS L2 AT A=0, BUT THIS DOES NOT SELECT A CLOSED DOMAIN. AT T=0 ONLY THE METRIC DIFFEOMORPHISM NOETHER GENERATOR IS ACTION-OWNED; THE 196/198 DISTORTION RADICAL IS NOT ITS IMAGE. THE ACTION OWNS A FORMAL MIXED GREEN CLASS, BUT NO REGULAR GLOBAL BFV REDUCTION, KT RESOLUTION, NILPOTENT BV COMPLETION, CLOSED INVERSE OR PHYSICAL COHOMOLOGY FOLLOWS. K132 MUST TOTALIZE THE ALL-GRADE SYMBOL AND SUBPRINCIPAL/TANGENTIAL NOETHER COMPLEX STRATUM BY STRATUM."
target_claim: K130_NEXT_GATE__COVARIANT_DAE_SPLIT_RADICAL_PROPAGATION_DN_WEIGHTS_BOUNDARY_CLASS_MINIMAL_BV_KT_BFV
target_verdict: STRATIFIED_SYMBOL_QUOTIENT_EXACT__GLOBAL_CONSTANT_RANK_SPLIT_OBSTRUCTED__DN_RELATIVE_WEIGHTS_EXACT__NORMAL_SYMBOL_PROPAGATION_INSUFFICIENT__DISTORTION_RADICAL_NOT_ACTION_OWNED_GAUGE__GLOBAL_BV_BFV_UNSELECTED
canon_verdict_change: none
---

# Selected-K131 native I1B T=0 DAE, weighted-domain, and minimal BV-BFV packet

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, tracked-carrier symbol-complex, mixed-order domain and
> variational boundary calculation. Ordinary Einstein-action, fermionic K77,
> particle-spectrum, Higgs/VEV, family-index, chirality, anomaly and symmetry-
> breaking constructions do not adjudicate it without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this result binds the serialized `Cl1 full plus horizontal-Cl2`
distortion carrier of the source-native `I1B` Hessian at K127's local
Ricci-flat `T=0` fixed-boundary germ. It classifies finite principal symbols
and formal action-owned Green data. It does not claim an all-grade source
totalization, a propagated global PDE constraint bundle, a selected closed
domain, a physical BFV quotient or cohomology.

## Result in plain English

K130 found a presymplectic normal coefficient on every conormal. K131 now
separates what can be constructed exactly from what still lacks an owner.
For a fixed conormal `n`, let

```text
R(n): V_Cl1 -> V_hCl2,
J(n) = [[0,R(n)^*],[-R(n),0]],
dim(V_Cl1,V_hCl2)=(196,24).                         (1)
```

If `r=rank R(n)`, then

```text
rad J(n) = ker R(n) plus ker R(n)^*,
dim rad J(n) = (196-r)+(24-r),
dim(V_tr/rad J(n)) = 2r.                           (2)
```

Thus the exact causal table is

| conormal | `r` | `ker R` | `ker R*` | radical | reduced dimension |
| --- | ---: | ---: | ---: | ---: | ---: |
| timelike | 12 | 184 | 12 | 196 | 24 |
| spacelike | 12 | 184 | 12 | 196 | 24 |
| null | 11 | 185 | 13 | 198 | 22 |

On any fixed-rank stratum, the quotient in (2) carries the nondegenerate form
induced by `J(n)`. A choice of complements realizes it as paired
`r+r` variables, but that complement is not canonical and is not the
quotient itself.

The decisive obstruction is the null jump. A smooth vector subbundle has
locally constant rank. Since the radical dimension changes from `196` to
`198`, there is no single smooth constant-rank radical subbundle—and hence no
single smooth quotient bundle—over a conormal region crossing the null
stratum. K131 therefore constructs a **stratified finite-symbol reduction**,
not one global covariant differential-algebraic split.

## 1. Constraint propagation is additional data

The left-null rows of `J(n)` are candidate normal constraints. They do not
propagate from the normal symbol alone. For a first-order model

```text
J dt u + B dx u + L u = 0,                           (3)
```

a left-null covector `ell` gives

```text
ell B dx u + ell L u = 0,                            (4)
```

whose content depends on tangential and subprincipal coefficients. The exact
probe gives two systems with the same `J` and different `B`: one has a zero
left-null equation and the other has the live constraint `dx u_1=0`.
Therefore K130's normal ranks do not establish propagation, closure or a
reducibility tower.

The action-owned gauge census is narrower still. The metric block has the
four Ricci-flat diffeomorphism principal directions. At `T=0`, the connection
difference transforms tensorially, so its infinitesimal internal gauge motion
has no independent `d chi` distortion column. The `196/198` distortion
radical is consequently not the image of a known action-owned gauge
generator. Null TT characteristics are also characteristics, not gauge.

## 2. Exact Douglis--Nirenberg weight family

For

```text
H = [[0,A*],[A,C]],       ord(A)=2,       ord(C)=1,   (5)
```

write row weights `(s_g,s_T)` and column weights `(t_g,t_T)`. Requiring the
three live blocks to saturate their order bounds gives

```text
s_g+t_T=2,   s_T+t_g=2,   s_T+t_T=1.                 (6)
```

All solutions are the common-shift family

```text
(s_g,s_T)=(1+a,a),       (t_g,t_T)=(2-a,1-a).        (7)
```

The integer representative `a=0` yields the bounded bulk mapping candidate

```text
H: H^2(g) plus H^1(T) -> H^-1(g-row) plus L^2(T-row). (8)
```

Equation (7) is exact order bookkeeping and fixes the relative regularity:
the metric variable carries one more derivative than the distortion variable.
It does not choose a graph closure, Krein majorant, gauge fixing, boundary
condition, Fredholm realization or inverse.

The source action nevertheless owns the formal boundary class. At the
quadratic germ its polarized Green representative has the typed form

```text
omega_boundary((h,t),(h',t'))
 = B_A(h,t') - B_A(h',t) + <t,J_C(n)t'>,             (9)
```

where `B_A` is the second-order Green concomitant of the actual curvature
linearization and `J_C` is K130's first-order coefficient. Under (8), a
classical trace description requires the metric value and normal derivative
together with the distortion trace; maximal/minimal weak graph domains may
require a different trace completion. Equation (9) selects the action-owned
formal class, not a polarization or operative closed adjoint.

## 3. Minimal BV/Koszul--Tate/BFV disposition

The minimal honest generator table is:

| object | current owner/status |
| --- | --- |
| metric field `h` and distortion field `t` | action-owned quadratic fields |
| diffeomorphism ghost `c` | action-owned through the metric Noether identity |
| metric/distortion antifields | formal Koszul--Tate slots for the Euler rows |
| distortion-radical ghosts | **not supplied**; nullity is not a gauge generator |
| higher ghosts/reducibility maps | **not supplied**; propagation complex absent |
| BFV boundary quotient/edge modes | **not selected**; rank is stratified and characteristic integrability is unproved |

A Koszul--Tate differential may formally send antifields to the Euler
equations, and the known diffeomorphism Noether identity supplies the metric
gauge leg. It cannot resolve the distortion left-null rows without the
tangential/subprincipal compatibility operators from (4). Calling each
radical direction a ghost would confuse a characteristic/constraint kernel
with gauge symmetry and would not prove nilpotency.

Likewise, presymplectic reduction requires an integrable constant-rank
characteristic distribution on the chosen boundary stratum. K131 has neither
constant rank across null conormals nor a proved action-owned generator for
the distortion radical. A stratified BFV construction may still exist after
the missing data are totalized, but no regular global BFV quotient follows.

## 4. Next gate

K132 must totalize the all-grade principal, tangential and subprincipal
source operator and derive its Noether/compatibility sequence. It must work
stratum by stratum, test whether the candidate constraint ranks remain
locally constant there, and determine whether their characteristic
distributions integrate. Only then can it select a closed DN realization,
operative adjoint, KT resolution, BFV edge packet, reduced inverse or
cohomology.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k131_native_i1b_t0_dae_bv_bfv_domain_packet_probe.py
```
