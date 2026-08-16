---
title: "Selected-K140 native I1B T=0 graph/parameter-cone obstruction"
status: active_research
doc_type: exact_finite_frequency_graph_parameter_cone_and_uniform_equivalence_gate
created: "2026-08-16"
registry: lab/process/selected-k140-native-i1b-t0-graph-parameter-cone-obstruction.json
probe: tests/channel-swings/selected_k140_native_i1b_t0_graph_parameter_cone_obstruction_probe.py
grade: "K140 CONSTRUCTS THE EXACT ACTION-DERIVED FINITE-FREQUENCY GRAPH REDUCTION WHEREVER THE DISTORTION BLOCK IS INVERTIBLE, BUT PROVES THAT IT IS NEITHER A CONSTRAINT PROJECTOR ON THE COMPLETE HOMOGENEOUS DN MODULE NOR A UNIFORM PRINCIPAL REDUCTION OF THE ORIGINAL FIXED-KAPPA_1 EQUATIONS. ON THE EXACT NULL METRIC-SUPPORT PACKET, THE FIVE JORDAN COEFFICIENT RANKS OF C^-1 A ARE 4,3,1,0,0, SO THE RECONSTRUCTION RETAINS POSITIVE FREQUENCY DEGREES THROUGH TWO EVEN THOUGH EVERY POSITIVE DEGREE CANCELS IN A* C^-1 A. AFTER RESTORING THE ORDER-TWO METRIC BLOCK, THE GRAPH MAP REACHES ORDER FOUR INSTEAD OF THE RELATIVE DN ORDER ONE. THE JOINT SCALING KAPPA_1=RHO MU RESTORES ORDERS -1 AND +1 ONLY ON PARAMETER CONES BOUNDED AWAY FROM MU=0 AND THE 27 SPACELIKE SHELL RATIOS. FIXED KAPPA_1 FORCES MU TO ZERO IN THE ULTRAVIOLET, WHERE THE FULL NULL INVERSE HAS A FIFTH-ORDER MU POLE AND THE METRIC GRAPH A THIRD-ORDER POLE. K132'S 24-VERSUS-11 TANGENTIAL TEST AND FOUR-DIMENSIONAL NOETHER IMAGE ALSO EXCLUDE AN ACTION-OWNED PRINCIPAL CONSTRAINT REDUCTION. THE FIVE-CLASS FIXED-FREQUENCY GEOMETRY REMAINS EXACT; ITS FIVE-BY-FIVE DENCKER MATRIX FOR THE ORIGINAL UV CALCULUS REMAINS UNDEFINED."
target_claim: K139_NEXT_GATE__ACTION_OWNED_CONSTRAINT_OR_SEMICLASSICAL_CALCULUS_SELECTION__PROJECTOR_EQUIVALENCE_TANGENTIAL_PRESERVATION_AND_TYPED_SUBPRINCIPAL_GATE
target_verdict: EXACT_FINITE_FREQUENCY_GRAPH_EXISTS__RECONSTRUCTION_JORDAN_RANKS_4_3_1_0_0__SCHUR_POSITIVE_DEGREES_CANCEL_BUT_GRAPH_DOES_NOT__JOINT_PARAMETER_CONE_HAS_CORRECT_ORDER__FIXED_KAPPA_UV_RECOVERY_SINGULAR_AT_MU_ZERO__NO_ACTION_OWNED_PRINCIPAL_CONSTRAINT_PROJECTOR__ORIGINAL_FIVE_BY_FIVE_DENCKER_REMAINS_UNDEFINED
canon_verdict_change: none
---

# Selected-K140 native I1B T=0 graph/parameter-cone obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, mixed-order Fourier-graph and
> parameter-dependent symbol calculation. Ordinary Einstein, Higgs/VEV,
> family-index, chirality, anomaly, symmetry-breaking and familiar particle-
> spectrum constructions do not adjudicate it without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K140 binds the selected displayed `comm/symi/symi` `I1B` Hessian at
`T=0`, fixed nonzero `kappa_1`, the complete real `Omega1(Cl(7,7))` carrier,
and the exact null metric-support packet used by K135--K139. It distinguishes
an exact fixed-frequency graph reduction from an ultraviolet principal
equivalence. It does not rule out a new action term, gauge fixing, boundary
law, compact-frequency effective theory, or explicitly inequivalent
parameter-dependent model.

## Result in plain English

K139 left two possible bridges to the five-class null bundle: an action-owned
constraint projector or a parameter-dependent calculus. K140 tests both.

At every Fourier covector where

```text
C(rho,n)=i rho C_1(n)+kappa_1 K                           (1)
```

is invertible, the distortion Euler equation gives the exact graph

```text
T=-C(rho,n)^(-1) A(rho,n) g.                             (2)
```

With native block extraction `E(g,T)=g` and graph inclusion `R(g)=(g,T(g))`,
`E R=I` and `P=R E` obeys `P^2=P`. This is action-derived finite-frequency
elimination, not a fitted projector. The full finite-frequency kernel is
isomorphic to the metric Schur kernel wherever (1) is invertible. K138's five
classes therefore remain exact.

The obstruction is uniform order. On the exact null packet, let
`L=K C_1(n)`. K135 gives `L^5=0`. Re-executing its packet and composing the
finite inverse with the metric image gives

```text
rank(L^j K A), j=0,...,4 = (4,3,1,0,0),                 (3)
rank(A* L^j K A)        = (1,0,0,0,0).                  (4)
```

Thus every positive Jordan degree cancels in the Schur form (4), but the
reconstruction itself retains degrees one and two. After the order-two
scaling of `A(rho,n)` is restored, (2) reaches frequency order four. The DN
weights require a relative order-one map from metric to distortion. Exact
Schur cancellation is therefore insufficient to make the graph a bounded
principal-symbol equivalence.

There is one honest parameter-dependent repair. Put

```text
mu=kappa_1/rho,       kappa_1=rho mu,
C=rho(i C_1(n)+mu K).                                (5)
```

On a closed cone with `mu` bounded away from zero and the spacelike exceptional
ratios, `C^-1` has order `-1` and `C^-1 A` has the expected order `+1`.
But this is a joint large-mass/high-frequency family. For the original action
with fixed nonzero `kappa_1`, `rho->infinity` forces `mu->0`. The complete
null inverse has coefficients through `mu^-5`; after composition with the
metric image the graph still has a `mu^-3` pole by (3). No estimate on the
closed cone is uniform through the fixed-action recovery limit.

The constraint route also closes at the current action grade. K132's complete
Noether inventory owns only four metric diffeomorphisms. Its exact 56D
tangential control has 24 normal-null rows but only 11 common normal/tangential
null rows, and nonzero `kappa_1 K` turns principal-null rows into live
algebraic equations. No action-derived complex removes K139's further
`106629` principal quotient directions.

## 0. Pre-wave answers

1. **Fork.** The original fixed-`kappa_1` differential action and the joint
   parameter family `kappa_1=rho mu` are distinct calculi. Both are retained.
2. **Cheapest decisive condition.** A principal graph equivalence must have
   the DN-relative order one uniformly in the recovery limit. Equations
   (3)--(5) decide this exactly.
3. **Positive route.** The fixed-frequency graph is exact, and a compact
   shell-avoiding `mu` annulus supports a well-ordered parameter family.
4. **Claim ceiling.** Neither object supplies a five-carrier Dencker
   connection for the original fixed-mass ultraviolet calculus.

## 1. Exact graph algebra

Write the full frozen Hessian as

```text
H = [[0,A*],[A,C]].                                      (6)
```

Where `C` is invertible, elementary block algebra gives

```text
ker H = R ker(-A* C^-1 A),
R g = (g,-C^-1 A g).                                    (7)
```

Equation (7) is an exact solution-module isomorphism at that frequency. It is
not a differential constraint: it uses the inverse of a frequency-dependent
block, fails at every spacelike shell, and is unbounded in the fixed-action
null ultraviolet limit. The natural graph projector projects the finite
coefficient space onto (7); it does not descend from the `106634`-dimensional
homogeneous principal quotient.

The distinction between (3) and (4) is load-bearing. Looking only at the
metric Schur form hides the positive-degree distortion reconstruction. A
five-dimensional metric radical can therefore stay exact while the full
field inclusion lacks the symbol order needed for microlocal transport.

## 2. Parameter-cone classification

For fixed `kappa_1`, the inverse expansion is

```text
C^-1 = sum_(j=0)^4 rho^j kappa_1^(-j-1) (-i)^j L^j K.  (8)
```

The full inverse reaches `j=4`; the metric graph reaches `j=2`. Under (5),
each inverse term becomes `rho^-1 mu^(-j-1)`, so the expected differential
order is restored while the constants have poles at `mu=0`.

The exact spacelike exceptional squared `mu` values are

```text
1,2,3,4,5,6,7,8,9,10,11,12,13,16,25,36,48,49,64,81,
88,100,120,121,144,160,168.                              (9)
```

A compact annulus separated from zero and (9) is a valid parameter-dependent
symbol region. It is not the ultraviolet limit of the original fixed-
`kappa_1` action, because that limit runs directly into `mu=0`.

## 3. Constraint, tangential and Dencker verdict

An action-owned constraint reduction would require a differential identity or
Noether/KT complex whose kernel is preserved by normal, tangential and lower-
order evolution. The current action supplies none beyond metric
diffeomorphism. Principal nullity alone cannot provide it:

```text
normal kernel in exact 56D block:                 24,
common normal/tangential kernel:                  11,
owned metric diffeomorphisms:                      4,
additional DN quotient directions beyond five: 106629.          (10)
```

Consequently the fixed-frequency graph is not an invariant projector from the
homogeneous DN principal module, and the joint parameter cone does not recover
the original fixed-action ultraviolet system. The five-by-five action Dencker
endomorphism sought by K138--K140 remains undefined for that original
calculus, not zero.

## 4. Twenty-lens reassessment

The live hypotheses were:

```text
H_A the finite graph is already a uniform principal reduction;
H_B the action owns constraints selecting it;
H_C a joint parameter cone has correct order but is singular in the
    fixed-action recovery limit;
H_D no exact five-class reduction exists at any frequency.
```

| lens | strongest hypothesis | decisive reason |
| --- | --- | --- |
| source criticism | `H_C` | the displayed action fixes `kappa_1`; it does not scale it with frequency |
| Layer-0 semantics | `H_C` | fixed-frequency graph and principal constraint are different objects |
| exact Clifford algebra | `H_C` | reconstruction ranks are `4/3/1/0/0` |
| Schur algebra | `H_C` | positive degrees cancel only after left composition by `A*` |
| DN theory | `H_C` | graph order four exceeds relative order one |
| semiclassical analysis | `H_C` | `mu`-cones restore order away from zero |
| singular perturbations | `H_C` | fixed mass forces the excluded `mu->0` limit |
| microlocal systems | `H_C` | no uniform graph bundle exists in that limit |
| Noether theory | `H_C` | only four diffeomorphisms are owned |
| BV/KT theory | `H_C` | no distortion constraint tower is selected |
| tangential compatibility | `H_C` | only 11 of 24 normal-null rows survive |
| representation theory | `H_C` | no invariant `106634 -> 5` principal map is supplied |
| Green/domain theory | `H_C` | the 27 shell ratios remain singular |
| differential geometry | `H_C` | K138's finite five-bundle remains exact |
| identifiability | `H_C` | a different projector would be an added choice |
| hostile falsification | `H_C` | recovery fails at the parameter boundary |
| philosopher of science | `H_C` | preserve the valid effective family without conflation |
| pragmatic sequencing | `H_C` | next test is a bounded annulus, not another UV claim |
| heterodox analysis | `H_C` | band-limited nonlocal dynamics may still be meaningful |
| wild frontier | `H_C` | an explicitly inequivalent large-mass theory stays open |

Vote: `H_A=0`, `H_B=0`, `H_C=20`, `H_D=0`.

## 5. Reverse scaffold and next gate

```text
R0 physical propagation needs a closed action-owned reduced operator.
R1 K138: exact covariant five-class finite-frequency null bundle.
R2 K139: not the complete homogeneous DN principal module.
R3 K140: exact graph exists, but fixed-kappa reconstruction is nonuniform.
R4 K140: joint kappa=rho mu cone restores order only away from the recovery
   boundary and spacelike shells.
R5 K141: on one compact shell-avoiding mu annulus, test the graph Green form,
   Riesz/projector covariance and subprincipal leakage as an explicitly
   band-limited parameter family.
R6 only after R5: ask whether that effective family has a closed domain.
```

K141 must keep its parameter annulus explicit, avoid all 27 shell ratios, and
state that it is not an ultraviolet equivalence theorem for fixed
`kappa_1`. It may compute the induced graph Green/subprincipal object only if
the projector is smooth and uniformly bounded on that annulus. Joe input is
not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k140_native_i1b_t0_graph_parameter_cone_obstruction_probe.py
```
