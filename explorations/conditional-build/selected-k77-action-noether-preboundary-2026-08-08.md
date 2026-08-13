---
artifact_type: construction_and_composition_result
created: 2026-08-08
status: LOCAL_SELECTED_ACTION_NOETHER_EXACT__COMPACT_SUPPORT_PRESYMPLECTIC_BASIC__UNRESTRICTED_BOUNDARY_MOMENT_MAP_LIVE
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 action Noether and preboundary composition

## Result in plain English

The physical symmetry cancellation has now survived the transition from the
raw residual to the **local selected action**.

This required two additions that the raw equation did not contain:

1. the K77 residual pairing and volume density must move with the physical
   frame; and
2. the action's independent epsilon equation and its endpoint Green term must
   be inserted before taking the physical matched-`q` pullback.

With all of them present, the local action Euler covector annihilates the
matched-`q` physical graph in timelike, spacelike and null classes. The result
is nonvacuous: an exact control uses a nonzero residual and nonzero action
density, and its density, field and pairing contributions are all separately
nonzero before their sum cancels. Freezing either the pairing or density
fails.

Antisymmetrizing the action-owned endpoint potential gives a sharp boundary
answer. Transformations whose parameter vanishes at the boundary are
characteristic directions of the presymplectic form. Unrestricted endpoint
transformations are not: their contraction is the variation of a nonzero
boundary moment map. They are physical boundary symmetries unless a later
source/action domain or edge-mode construction changes that disposition.

This closes the local action Noether/basicness gate. It does not construct a
global BFV phase space, choose a polarization or boundary domain, or solve the
common Green/Krein analytic problem.

## 1. Layer 0

| phrase | object closed here | object kept distinct |
| --- | --- | --- |
| raw Ward identity | `D Upsilon R_phys=0` | the selected-action Euler identity |
| primitive epsilon Euler | generally nonzero action equation | an off-shell zero identity |
| dependent epsilon motion | matched-`q` compensator in the physical graph | arbitrary independent epsilon variation |
| moving action scalar | density times the indefinite K77 residual pairing | a positive Hilbert norm |
| Green potential | action-owned endpoint field-space one-form | its antisymmetrized two-form |
| small physical transformation | parameter vanishing on the boundary | charged endpoint transformation |
| local moment map | `i_R Omega=-delta Q_boundary` | global BFV reduction, charge algebra or polarization |

The `U(64,64)` phrase is also kept typed. The operative construction remains
the selected Spin-native grade-`1+2+5` parent. The product of two
`U(32,32)` Weyl-half groups and the full `U(64,64)` comparator remain distinct
rival action parents.

## 2. Source return

Weinstein supplies the norm-square/adjoint arena, two-connection augmented
torsion, moving Shiab and primitive epsilon grammar. The inspected source does
not print this exact matched-`q` action Euler identity or select which
boundary transformations are gauge.

```text
SOURCE-CONFIRMS:
  norm-square, two-connection, moving-Shiab and epsilon grammar.

REPO-DERIVES:
  local matched-q action Euler-Noether composition and boundary moment-map
  disposition.

SOURCE-SILENT:
  physical boundary class, edge completion, global BFV/polarization and
  common closed Green/Krein domain.
```

## 3. Exact action composition

For the residual-square layer, write locally

```text
L_2 = rho (1/2) Upsilon^T K Upsilon.
```

Under a physical frame generator `A` and density weight `c`, the exact
transport law is represented by

```text
delta Upsilon = A Upsilon + c Upsilon,
delta K       = -A^T K - K A,
delta rho     = -2 c rho.
```

On a nonzero exact rational residual the three terms

```text
(delta rho) Q,
rho <delta Upsilon,Upsilon>_K,
(rho/2)<Upsilon,(delta K)Upsilon>
```

are separately nonzero and sum to zero. This is the control that prevents the
stationary `Upsilon*=0` specialization from making the theorem vacuous.

For the first action, the action-owned primitive epsilon covector is the prior

```text
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S.
```

The selected endpoint momentum is the exact `E_B-E_T` bank, with normal rank
ten and two opposite independent endpoint restrictions. The rejected generic
constitutive guess `p=K T` is not used. Exact integration by parts supplies
the endpoint sign, and the moving Shiab and lower Cartan terms are forced by
their rank-three omission defects. Composed with the physical metric/Cartan
graph, the action Euler contraction is zero in all three causal classes.

The new proof is functorial: it composes immutable exact K77 action and graph
receipts with a fresh exact universal variational calculation. It does not
replay the 16,384-direction Clifford evaluator and makes no new full-bank rank
or support claim. Main calculation: `56/56 PASS`; independent Sage/QQ:
`18/18 PASS`.

## 4. Antisymmetrization and boundary charge

With the opposite endpoint orientation, the local action Green potential has
the model form

```text
Theta = p_0 delta g_0 - p_2 delta g_3,
```

where `p` denotes the action-owned `E_B-E_T` endpoint bank. Its field-space
exterior derivative obeys

```text
i_(R_eta) Omega = -delta Q_eta,
Q_eta = p_0 eta_0 - p_2 eta_3.
```

For `eta_0=eta_3=0`, the contraction vanishes. For unrestricted endpoint
parameters the exact control is nonzero. Deleting the boundary distinction or
quotienting every endpoint transformation as gauge fires the planted test.

Thus the local result is:

```text
compact-support / boundary-vanishing physical transformations: basic
unrestricted endpoint transformations: live moment map / surface charge
```

No sixth scoped quotient is booked. The boundary class is not yet selected.

## 5. Specialist and hostile review

- **Differential geometry:** the metric-bundle lift, Cartan response, moving
  Shiab, pairing and density move before restriction to the physical graph.
- **Symplectic geometry:** invariance and horizontality are separated. The
  live moment map is not erased as a bulk defect or silently quotiented.
- **Variational PDE:** exact integration by parts and the nonzero-residual
  control rule out algebraic-transpose and stationary-vacuity errors.
- **Real Clifford/Krein:** the action pairing remains indefinite. No positive
  energy or real-form port is inferred.
- **Analytic/path-integral:** local formal variation selects no domain,
  contour, measure, determinant, propagator or reflection positivity.
- **Source criticism:** the result is repository-derived and the source's
  boundary silence is retained.
- **Constraint accounting:** zero new fields, parameters, selectors,
  quotients or data; P1/P2/P3 remain unused.

The hostile review narrows “complete action Noether theorem” to a local
proof-level composition. Global adjoint-bundle patching, a physical boundary
class and common analytic domain remain unproved.

## 6. Seven-axis disposition

- **Layer 0:** residual/action, Euler/Ward, Green/presymplectic and
  small/boundary transformations are separated.
- **L1:** all action owners and source loci are identified.
- **L2:** density, pairing, primitive epsilon and endpoint covectors share one
  local selected-action first variation.
- **L3:** nonzero-residual cancellation, Euler contraction, Green identity and
  moment map are exact over rationals with firing omissions.
- **L4:** matched-`q` timelike/spacelike/null local graphs close; global bundle
  and boundary-class descent remain open.
- **L5:** local Euler-Noether and compact-support presymplectic basicness close;
  unrestricted BFV/edge completion remains open.
- **L6:** no common closed, positive, hyperbolic or self-adjoint domain.
- **L7:** no Einstein, Standard Model, spectrum, cosmology or quantum claim.

## 7. Progress and next gate

```text
Ledger v0.100 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
  - local selected-action Euler-Noether identity on the matched-q graph
  - compact-support basicness versus unrestricted boundary moment map
frontier_conditions_opened: 0
remaining_named_conditions: 1
```

No verdict, residue, quotient, fork, canon, public posture or datum changes.

Next:

`SOURCE_OR_ACTION_SELECT_PHYSICAL_BOUNDARY_CLASS__THEN_GLOBAL_TAU_A0_BFV_OR_EDGE_MODE_COMPLETION_POLARIZATION_AND_COMMON_GREEN_KREIN_DOMAIN`.
