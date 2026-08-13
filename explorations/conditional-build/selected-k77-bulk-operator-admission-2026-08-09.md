---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: MIXED_ORDER_ACTION_GRAMMAR_EXACT__COMPLETE_OPERATOR_AND_DMAX_DMIN_UNOWNED
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 bulk-operator admission gate

## Plain English result

The new boundary phase space is coherent, but the repository is not yet
entitled to ask it for a bulk domain. The missing bulk object is not merely a
technical closure of a matrix already in hand. The written action has metric,
connection and gauge-frame variables entering at different derivative orders,
and the blocks already computed were made on different earlier backgrounds or
restricted parents.

The exact dependency audit gives the smallest safe mixed-order weights

```text
g : 2       varpi : 1       epsilon : 1
```

for the first-action density after gauge-covariant reduction. This yields the
safe linearized-Euler block bound

```text
             delta g   delta varpi   delta epsilon
E_g              4          3              3
E_varpi           3          2              2
E_epsilon         3          2              2
```

The residual-square layer is at most second order in all three variables at a
zero-residual branch. This is an **admission grammar**, not proof that the
fourth- or third-order coefficients survive exact variation. Those coefficients
must now be computed; covariance or integration by parts may lower them.

The immediate gain is procedural and mathematical: a one-order scalar operator
cannot be presumed, the H7/H8 trace cannot define it backward, and six exact
owners are now named before any `Dmax/Dmin` theorem is admissible.

## 1. Layer 0

| phrase | object here | not the same as |
| --- | --- | --- |
| action jet order | highest derivative in the written density | order of the Euler operator after cancellations |
| raw epsilon order | coordinate expansion before gauge covariance | independent covariant principal data |
| DN weight | safe mixed-order bookkeeping | nonzero principal coefficient or ellipticity |
| pointwise parent stationarity | zero local first variation in 229,376 directions | global tangent, Hessian or selected parent |
| partial stationary Gram | prior 34-field metric-varpi covector symbol | complete first-plus-second action operator |
| strong H7/H8 carrier | kinematic boundary cotangent target | graph trace of `Dmax/Dmin` |
| bosonic branch | zero-fermion action background | coupled matter fluctuation operator |

## 2. Source dependency and covariant reduction

The source action owns `T=varpi-B(g,epsilon)` and the packet

```text
F_B + (1/2)d_B T + (1/3)T wedge T.
```

In raw coordinates `B` and `T` contain first derivatives of `g` and epsilon,
so `F_B` and `d_B T` display second derivatives. Curvature covariance removes
derivative epsilon from `F_B`. The exact identity

```text
F_A = F_B + d_B T + T wedge T
```

then reduces the packet's independent orders to `(g2,varpi1,epsilon1)`.
The source residual `Upsilon` has the already-built first-order response in all
three fields, so its stationary norm-square Hessian is bounded by order two.

For a density with field weights `m_i`, the linearized Euler block has the safe
bound `m_i+m_j`. Exact enumeration gives the unique componentwise-minimal
symmetric DN weight `(2,1,1)`. Uniform `(1,1,1)` misses the `g-g` bound;
uniform `(2,2,2)` is compatible but over-regular and does not prove a scalar
fourth-order operator.

## 3. Ownership audit

What is owned:

- two local QQ(sqrt(3)) source-stationary branches;
- pointwise stationarity for the selected Spin directions, both separate
  `U(32,32)` halves, and the even-plus-half-exchanging full `U(64,64)`
  comparator;
- a prior rank-91 epsilon/Cl1 first-action cross;
- a prior 34-field metric-varpi stationary Gram symbol;
- the strong relative H7/H8 boundary carrier.

What prevents operator admission:

1. the complete first-action Hessian must be ported to both current branches;
2. the complete residual Jacobian and stationary Gram must be ported likewise;
3. the parent-specific global tangent/Hessian family is unbuilt;
4. no bulk gauge-fixing and ghost operator is owned;
5. no field Riesz or explicitly covector-valued graph calculus is selected;
6. no closed ultrahyperbolic realization exists.

The two old Hessian results remain evidence, but not plug-compatible operator
blocks. The hostile review caught that they live on predecessor backgrounds.

## 4. Specialist synthesis

- **Variational bicomplex:** compute branch-specific Hessian coefficients; do
  not promote density order to Euler order.
- **Douglis--Nirenberg/microlocal:** `(2,1,1)` is the correct minimal audit
  weight, but the actual principal family and characteristic strata remain open.
- **Symplectic/BV--BFV:** retain the H7/H8 phase space as a target and derive its
  soldering from the complete Hessian rather than imposing it.
- **Krein operator:** keep the equation covector language until a Riesz or
  covector graph realization is constructed.
- **Gauge geometry:** epsilon's bulk equation, endpoint momentum and ghost
  complex must be assembled together.
- **Representation/Clifford:** pointwise compatibility does not choose between
  the Spin parent, two halves and full comparator.
- **Source criticism:** the action grammar is authorial; the DN weights and
  ownership matrix are repository constructions.
- **Complex/path integral:** operator admission precedes contour and measure;
  neither is inferred.

## 5. Source return and accounting

```text
SOURCE-CONFIRMS:
  two-connection first action, residual and Xi redundancy grammar.

SOURCE-SILENT:
  mixed-order gauge-fixed operator, parent-specific Hessian, Dmax/Dmin,
  Green/Krein realization and coupled BV-BFV.
```

```text
new fields/coefficients/selectors/bundle classes/quotients: 0
P1/P2/P3 consumed: 0
```

Primary certificate: `43/43 PASS`. Independent Sage/FLINT: `15/15 PASS`.

## 6. Progress and next gate

```text
Ledger v0.117 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 0
remaining_named_conditions: 6
```

Closed: the actual operator is not yet admissible as a one-scalar-order object,
and the H7/H8 carrier is explicitly typed as a kinematic target rather than an
operator-derived trace. The six remaining conditions are the owners above.

Next:

`CONSTRUCT_BRANCH_AND_PARENT_INDEXED_FULL_SOURCE_VARIABLE_HESSIAN_PRINCIPAL_COEFFICIENTS__PORT_G_VARPI_EPSILON_BLOCKS_TO_BOTH_STATIONARY_BRANCHES__SELECT_OR_RETAIN_PARENT_FAMILY__THEN_ADD_BULK_GAUGE_FIXING_GHOST_COMPLEX_AND_TEST_DMAX_DMIN`.
