---
artifact_type: construction_and_composition_result
created: 2026-08-08
status: COMMON_METRIC_VARPI_EQUATION_DUAL_GREEN_EXACT__PHYSICAL_PULLBACK_ZERO__ACTION_NOETHER_OPEN
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 common physical equation-dual and Green extension

## Result in plain English

The metric and connection parts of the current K77 construction now have one
common first-order equation dual and one common local Green identity.

The independent field coordinates are

```text
10 metric variables + 24 horizontal varpi variables = 34 variables.
```

The exact metric coefficient bank from v0.97 and the exact `varpi` bank from
v0.96 can therefore be concatenated into one operator

```text
J_common = A_common^mu partial_mu + B_common.
```

Under the conditional real K77 residual pairing `K_loc`, its canonical object
is the **equation dual**

```text
J_common,K^! v
  = -partial_mu((A_common^mu)^T K_loc v)
    + B_common^T K_loc v,                         (1)
```

with local Green concomitant

```text
G_common^mu(u,v)=u^T(A_common^mu)^T K_loc v.       (2)
```

Equation (1) closes coefficientwise over exact rationals and (2) is nonzero.
On the source-native matched-covector physical diffeomorphism graph from
v0.98, the pullback of (1) is exactly zero in timelike, spacelike and null
classes. This is not a rank coincidence: deleting either moving Shiab or the
lower Cartan commutator restores a rank-three defect in every class.

This closes the common **raw-residual equation-dual** gate. It does not yet
derive the complete selected-action Euler/Noether identity. That next step
must move the action pairing and density, insert the already-owned primitive
epsilon Euler/preboundary terms, and only then antisymmetrize the action-owned
Green potential.

## 1. Layer 0

| phrase | object closed here | object kept distinct |
| --- | --- | --- |
| common differential | `D_g Upsilon direct-sum D_varpi Upsilon` on 34 independent coordinates | full independent `D_epsilon Upsilon` |
| physical epsilon motion | dependent four-column compensator inside the matched-q diffeomorphism graph | arbitrary primitive epsilon field variation |
| equation dual | covector-valued formal transpose under `K_loc` | field-valued operator adjoint |
| Green concomitant | local first-variation boundary current | global Green operator or inverse |
| physical pullback | equation dual annihilates the exact raw-residual gauge graph | complete selected-action Euler/Noether identity |
| primitive epsilon Euler | already-owned action covector from v0.25 | raw-residual `D_epsilon Upsilon` coefficient bank |
| presymplectic current | still-unbuilt antisymmetrization/basicness test | the Green one-form itself |

The important correction is procedural. A full arbitrary `D_epsilon Upsilon`
bank is still a legitimate independent-field question, but v0.98 proved it is
not required to close the **dependent physical orbit**. Requiring that larger
object before pulling back the equation dual would defend a superseded queue.

## 2. Source return

Weinstein's source supplies the norm-square/adjoint arena, the two-connection
augmented-torsion grammar and moving epsilon-conjugated insertions. It does not
print the 34-field coefficient operator, `K_loc`, the exact physical pullback,
a field-space Riesz map or a closed analytic domain.

```text
SOURCE-CONFIRMS:
  norm-square/adjoint arena and moving two-connection grammar.

REPO-DERIVES:
  exact common metric-varpi equation dual, local Green identity and
  matched-q physical pullback.

SOURCE-SILENT:
  exact common composition, field-space Riesz representative, complete
  selected-action Noether/preboundary closure and global analytic domain.
```

## 3. Exact construction and efficient replay

The two coefficient banks were already separately certified on the same real
K77 residual carrier:

- metric domain `10`, principal ranks `(9,9,9,9)`, main receipt `54/54`;
- `varpi` domain `24`, principal ranks `(13,13,13,13)`, zero-order rank `24`,
  main receipt `30/30`;
- physical matched-q graph, twelve coefficientwise zero columns, main receipt
  `52/52`.

The new mathematical step is functorial, not another full Clifford search:
concatenation gives a 34-field first-order operator, and integration by parts
applies to the concatenated matrix exactly as to either summand. A fresh exact
rational 34-field calculation verifies every polynomial coefficient of (1)
and (2), including a firing wrong-sign plant. The actual common Green current
is nonzero because its restriction to the metric-zero `varpi` summand is the
already-certified nonzero current.

This wave deliberately does not mega-import both deep predecessor evaluators
into one process. That attempted replay exhausted the evaluator before the new
checks ran. The durable certificate instead uses immutable exact receipts for
the K77 banks plus a lightweight proof-level composition, independently
rechecked in Sage over `QQ`. This changes no scientific claim: it makes the
composition cheaper and reproducible.

Main exact composition: `44/44 PASS`. Independent Sage/QQ: `12/12 PASS`.

## 4. What the physical zero says—and does not say

For the matched-q physical generator `R_phys`, v0.98 proves

```text
D Upsilon . R_phys = 0
```

coefficientwise. Dualizing gives

```text
R_phys^! . (D Upsilon)_K^! = 0.                 (3)
```

Equation (3) is exact for every residual covector. It closes the local
equation-dual pullback and determines which object the action variation must
use next.

It is not yet the action's Noether theorem. The action variation also owns the
moving density/pairing and its epsilon preboundary response. Those pieces
exist in earlier artifacts at generic or fixed-metric grade, but have not yet
been assembled on this exact matched-q graph. Promoting (3) directly to an
action Euler identity would repeat the repo's density-versus-Euler mistake.

## 5. Specialist review

- **Differential geometry:** the direct-sum operator is built before its
  restriction to the dependent physical graph; independent and dependent
  variables are not conflated.
- **Symplectic geometry:** the Green concomitant is a preboundary one-form.
  Antisymmetrization, basicness and BFV reduction remain open.
- **Variational PDE:** the derivative minus sign and boundary derivative are
  checked coefficientwise, not inferred from an algebraic transpose.
- **Real Clifford/Krein:** the result is real K77 and covector-valued. No
  positive fundamental symmetry or field-space Riesz map is invented.
- **Analytic/path-integral:** local formal integration by parts does not select
  a domain, contour, measure, determinant, saddle or reflection positivity.
- **Source criticism:** compatibility is repository-derived rather than
  attributed to Weinstein.
- **Constraint accounting:** no field, coefficient, quotient, scale,
  selector or external datum is added; P1/P2/P3 stay unused.

## 6. Seven-axis disposition

- **L1:** the source adjoint arena and predecessor formulas are located.
- **L2:** all banks use the common real K77 residual carrier; equation dual,
  operator adjoint, Green, Noether and presymplectic objects remain distinct.
- **L3:** direct-sum formal Green and physical pullback identities are exact.
- **L4:** matched-q local timelike/spacelike/null graphs close; global bundle
  and arbitrary primitive epsilon field variation remain open.
- **L5:** equation dual and Green concomitant close; action Euler/Noether and
  presymplectic antisymmetrization remain open.
- **L6:** no common closed domain, positivity or Green inverse is claimed.
- **L7:** no Einstein, Standard Model, spectrum, cosmology or quantum claim.

## 7. Progress and next gate

```text
Ledger v0.99 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 3
  - common 34-field metric-varpi equation dual
  - nonzero common local Green concomitant
  - exact physical matched-q equation-dual pullback
frontier_conditions_opened: 0
remaining_named_conditions: 2
```

No verdict, residue, quotient, fork, canon, public posture or datum changes.
The Spin-native selected parent, two `U(32,32)` Weyl halves and full
`U(64,64)` comparator remain distinct.

Next:

`COMPOSE_MOVING_ACTION_PAIRING_DENSITY_PHYSICAL_EPSILON_EULER_AND_PREBOUNDARY_ON_MATCHED_Q_GRAPH__DERIVE_SELECTED_ACTION_EULER_NOETHER__THEN_ANTISYMMETRIZE_AND_TEST_BASICNESS`.
