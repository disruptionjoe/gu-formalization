---
artifact_type: construction_result
created: 2026-08-08
status: COUPLED_COMPLEX_REQUIRED__VERTICAL_ONLY_COMPLEX_MISTYPED__COMMON_TWO_LAYER_HESSIAN_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS__TWO_LAYER_FULL_VARIABLE_ACTION_GRAMMAR_AND_DIFFEO_ORTHOGONAL_TARGET__SOURCE-SILENT__COMMON_TWO_LAYER_HESSIAN_AND_SELECTED_PHYSICAL_COMPLEX
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_coupled_euler_complex_scope_probe.py
  - tests/channel-swings/selected_k77_coupled_euler_complex_scope_independent.sage
registry: lab/process/selected-k77-coupled-euler-complex-scope.json
---

# Selected K77 coupled Euler-complex scope gate

## Result first

The ten metric-section equations v0.80 retained are real and necessary, but
they are **not yet a closed ten-variable selected-action Euler complex**.
That next-gate wording was a Layer-0 mistake.

The repository had already built more of the relevant action than v0.80
composed:

- the completed first layer has `34` source variables (`10` metric plus `24`
  connection variables) coupled through a nondegenerate `196`-dimensional
  adjacent grade-one bank;
- exact Schur elimination gives a `34 x 34` Ward-basic symbol with rank `30`
  and gauge radical exactly rank `4` for timelike, spacelike and null
  covectors at the normalized generic coefficient;
- its physical symbol cohomology is therefore zero at that coefficient;
- the exceptional first-layer `N2` pair is already typed by compact null
  rotation as helicity `+/-1`, not Einstein helicity `+/-2`;
- the separate second-layer `10 x 10` metric diagnostic reproduces the exact
  transverse-traceless helicity-two polynomial, but its full off-TT Ward
  defect has rank `4`; and
- adding that metric block to the Ward-basic first layer leaves the same
  rank-four defect.  A gauge-basic Einstein block cannot cancel it.

Therefore the next object is the **full selected two-layer Hessian on a common
field space and common stationary background**, including every second-layer
metric--connection, grade-one, matter and observation-jet cross block.  Its
diffeomorphism differential, Ward adjoint and null cohomology must be derived
from the action.  A ten-by-ten fit or direct sum is not admissible.

This is a scoped route correction, not a kill of GU or of the ten metric
equations.

## 1. Layer 0: what changed type

| phrase | exact object | disposition |
| --- | --- | --- |
| ten metric equations | independent metric-section Euler coordinates under the complete receiver | retained |
| closed vertical complex | a purported action-invariant subsystem on only those ten coordinates | not established; current wording retracted |
| first-layer physical symbol | Schur-reduced `34 x 34` coupled source symbol | exact in its declared finite bank |
| Schur reduction | elimination of a nondegenerate `196 x 196` algebraic block | not a gauge, BV or symplectic quotient |
| second-layer metric block | background-subtracted `10 x 10` diagnostic pullback of selected `I2B` | TT-correct, nonbasic off TT |
| combined action complex | Hessian of both selected layers on their common variables/background | unbuilt |
| Einstein complex | standard GR comparator with null helicity-two cohomology | target, not an additive repair term |

The error was not retaining the ten equations.  It was treating retained
coordinates as though the action had proved their dynamical closure.

## 2. Exact first-layer facts already in the repo

For each causal covector orbit, the exact first-layer construction has:

| orbit | source variables | adjacent-grade bank | live cross rank | effective rank | gauge rank | physical middle cohomology |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| timelike | 34 | 196 | 13 | 30 | 4 | 0 |
| spacelike | 34 | 196 | 15 | 30 | 4 | 0 |
| null | 34 | 196 | 15 | 30 | 4 | 0 |

The exact identities are

\[
H_1D=0=D^TH_1,
\qquad
\operatorname{rank}H_1=30,
\qquad
\ker H_1=\operatorname{im}D.
\]

The separately factored exceptional coefficient `N2` enlarges the null kernel
by two, but its quotient rotation has polynomial `x^2+1`.  The Einstein target
has `x^2+4`.  This closes the tempting “two modes therefore two gravitons”
shortcut inside the completed first-layer bank.

## 3. Exact second-layer obstruction

At the rational test point `s=2`, the selected second-layer metric block `H2`
satisfies

```text
shape H2             = 10 x 10
rank H2              = 10
rank D               = 4
rank(H2 D)           = 4
TT plus/cross value  = exact selected C4*s*(s+M2), including norm
```

Embedding `H2` into the first ten coordinates of the coupled source space
gives

\[
(H_1+\operatorname{diag}(H_2,0_{24}))D
=\operatorname{diag}(H_2,0_{24})D,
\]

with rank four.  The naive combined operator is not Ward-basic.

This does not kill the second layer.  The norm-square Euler operator varies
the first-layer residual, its coefficients and the variables on which that
residual depends.  The missing connection and observation cross terms are
precisely where Ward cancellation may live.  A metric-only restriction cannot
decide that.

## 4. Why an attractive repair would teach nothing

Let `C` range over symmetric `10 x 10` matrices and demand

\[
CD=-H_2D.
\]

The exact linear map from the `55` independent coefficients of `C` to its
gauge columns has rank `34`.  A solution exists, but the solution set has
affine dimension

\[
55-34=21.
\]

So a hand-built Ward completion is easy and radically nonunique.  Constraint
surplus is negative unless the action derives the missing blocks.  Likewise,
adding any gauge-basic block `B` with `BD=0`—including the standard Einstein
comparator—cannot cancel `H2D`.

## 5. Non-algebraic lens disposition

- **Microlocal PDE:** ranks and null cohomology are only principal-symbol
  gates.  Strong hyperbolicity, constraint propagation and a common Green
  domain remain open until the coupled symbol exists.
- **Variational bicomplex:** both action layers must be varied on the same jet
  bundle and stationary background; a direct sum of separately restricted
  Hessians is not the Hessian of the selected action.
- **Symplectic/BV-BFV:** Schur elimination is not presymplectic reduction.
  Gauge may be quotiented only after the action-derived characteristic
  distribution and boundary moment map are known.
- **Krein/operator theory:** finite exact inertia or rank gives neither a
  positive physical energy nor a common closed right-H domain.
- **Complex/real structure:** the exact real K77 calculation does not choose a
  Lorentzian contour, reflection positivity structure or quantum measure.
- **Representation theory:** the generic first layer has no physical symbol
  class and the exceptional one is helicity one; the second-layer TT
  helicity-two diagnostic survives but has not descended through the coupled
  action.

## 6. Seven-axis disposition

- **Layer 0:** retained coordinate sector and closed action subsystem are now
  separated.
- **L1 source:** source confirms two layers, two connections and the
  diffeomorphism-orthogonal target; it is silent on the completed complex.
- **L2 algebra:** first-layer ranks, second-layer defect, naive-sum defect and
  21-dimensional completion freedom are exact.
- **L3 geometry:** the common field/jet carrier and stationary background for
  both layers remain to be assembled.
- **L4 variation:** the second layer must be differentiated through the full
  first-layer residual; the metric block alone is not an Euler owner.
- **L5 gauge/BV:** first layer is Ward-basic; the isolated second layer and
  naive sum are not.  No new quotient is booked.
- **L6 analytic:** hyperbolicity, Green/Krein domain, contour and boundary BFV
  remain downstream.
- **L7 physical:** no selected graviton, Einstein equation, cosmology or
  quantum claim is promoted.

## 7. Controls and progress

The composed SymPy route passes `56/56`; the independent Sage/QQ route passes
`15/15`.  Plants reject vertical closure from retained coordinates, Schur-as-
BV, direct-sum composition, a 21-parameter fit as construction, dimension-only
gravitons, and finite-rank-to-hyperbolicity promotion.

```text
new fitted coefficient/selector: 0
new external datum:              0
new scoped quotient:             0
P1/P2/P3 consumed:               0

Ledger v0.81 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: NONE
frontier_conditions_closed: 4
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Closed are the vertical-only closure reading, the first-layer generic
helicity-two route, the naive two-layer sum, and fitted Ward repair.  Opened is
the full common-field two-layer Hessian.  Remaining are that Hessian/Ward
complex, its microlocal/Green/Krein analysis, and boundary BV-BFV descent.

## Next gate

`FULL_SELECTED_TWO_LAYER_COMMON_FIELD_STATIONARY_HESSIAN_CROSS_BLOCKS_AND_WARD_COMPLEX`.

Write both selected action layers on one field/jet bundle and one stationary
background.  Differentiate the norm-square layer through every live
first-layer variable, including connection/difference, grade-one, matter,
moving Levi-Civita/Shiab/Hodge/frame and observation jets.  Then construct the
full diffeomorphism generator and Ward adjoint.  Only an action-derived
Ward-basic complex proceeds to characteristic cohomology, strong-hyperbolic
reduction, common Green/Krein domain and boundary BFV.
