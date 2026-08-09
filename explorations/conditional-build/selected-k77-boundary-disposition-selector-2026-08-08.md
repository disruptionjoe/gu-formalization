---
artifact_type: construction_and_composition_result
created: 2026-08-08
status: SOURCE_AND_LOCAL_ACTION_DO_NOT_SELECT_BOUNDARY_DISPOSITION__CONDITIONAL_FULL_BOUNDARY_GAUGE_PLUS_NONZERO_MOMENTUM_SELECTS_MINIMAL_EDGE_HORN
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 physical-boundary disposition selector

## Result in plain English

Weinstein's source and the local selected action do **not** by themselves tell
us what to do with transformations that remain nonzero at a boundary.

The source insists on the full tilted inhomogeneous gauge/double-coset grammar,
but it does not say whether its quotient continues to treat boundary
transformations as redundancy. In the same transcript Weinstein says the
upstairs multiple-time problem is a boundary-value problem that he does not
know how to control. The action supplies a nonzero endpoint momentum and a live
boundary charge, but that charge can consistently be treated as a physical
surface symmetry rather than gauge.

There is nevertheless a sharp conditional result. Add two explicit demands:

1. every boundary transformation remains gauge redundancy; and
2. generic nonzero action endpoint momentum remains physically admissible.

Of the four local horns already present in the repository, only the minimal
edge-mode completion satisfies both. Its two signs are fixed uniquely, it adds
no continuous coefficient freedom, and after quotient it adds no net physical
boundary dimensions. This makes it the best construction horn for the next
wave, while the charged-boundary-symmetry horn remains the honest comparator.

The first demand is not yet a source quotation or action theorem. The result is
therefore a conditional selector, not a physical boundary-condition
settlement and not a new external datum.

## 1. Layer 0

| phrase | object here | kept distinct from |
| --- | --- | --- |
| full tilted gauge symmetry | bulk/global inhomogeneous gauge grammar | declaring all endpoint transformations gauge |
| boundary gauge | characteristic direction of the preboundary form | Hamiltonian boundary symmetry with charge |
| boundary condition | restriction of parameters, fields or momenta | extension of boundary field space |
| edge mode | boundary coordinate restoring horizontality | new bulk field or physical particle |
| nonzero action momentum | rank-ten `E_B-E_T` endpoint bank | proof that every value lies in the physical domain |
| local quotient | finite rank-40 reduced symplectic form | global `tau_A0` BFV phase space |

The load-bearing distinction is bulk quotient versus boundary disposition.
On a manifold with boundary, a transformation may become a charged physical
symmetry even when the same transformation is gauge in the bulk.

## 2. Source return

The primary transcript supplies two different facts:

- at `02:19:49--02:22:20`, Weinstein describes the tilted subgroup and says
  that `A/G` is replaced by its double-coset analogue;
- at `01:16:13--01:17:35`, he separates one-time Hamiltonian evolution from
  the upstairs multiple-time boundary problem and says he does not know how to
  push the Hamiltonian construction there.

Neither passage says whether nonvanishing boundary transformations are gauge
redundancy or physical symmetries. Therefore:

```text
SOURCE-CONFIRMS:
  full tilted bulk grammar and the existence of unresolved boundary debt.

SOURCE-SILENT:
  boundary gauge versus charged symmetry, boundary conditions, edge modes,
  BFV polarization and common analytic domain.
```

Importing the bulk double quotient directly as a boundary BFV quotient would
be a Layer-0 error.

## 3. Exact four-horn classification

The action-owned endpoint form has one-normal coordinates
`(g0,g3,p0,p2)` and opposite endpoint orientation. Its unrestricted
transformation obeys

```text
i_R Omega_bulk = -delta(p0 xi0 - p2 xi3),
```

so it is charged rather than characteristic. The four dispositions are:

| horn | all endpoint transformations gauge? | generic nonzero momentum allowed? | disposition |
| --- | --- | --- | --- |
| small-gauge/Dirichlet | no | yes | conditional restriction |
| zero-charge/Neumann-like | yes | no; `p0=p2=0` | conditional restriction |
| charged boundary symmetry | no | yes | live comparator |
| minimal edge completion | yes | yes | unique conditional survivor |

The edge form is

```text
Omega_ext = Omega_bulk
          - delta p0 wedge delta phi0
          + delta p2 wedge delta phi3,
delta_xi phi_i = xi_i.
```

Exact horizontality fixes the two coefficients to `(-1,+1)` uniquely. Equal
signs fail. Direct sum over the ten nonzero endpoint directions gives

```text
unextended phase dimension: 40
extended boundary dimension: 60
characteristic gauge kernel: 20
reduced symplectic dimension/rank: 40/40
new reduced physical dimensions: 0
new continuous coefficient freedom: 0
```

Main probe: `48/48 PASS`. Independent Sage/QQ: `15/15 PASS`.

## 4. What the conditional selector does—and does not—mean

The edge horn is forced only inside the class

```text
FULL_BOUNDARY_GAUGE
AND GENERIC_NONZERO_ACTION_MOMENTUM.
```

Dropping the first predicate leaves the charged-symmetry horn. Dropping the
second leaves the zero-charge horn. Restricting the gauge parameters leaves
the small-gauge horn. The local action therefore does not secretly select the
boundary merely because its endpoint bank is nondegenerate.

The unowned object is a **boundary gauge-status disposition**: are
nonvanishing endpoint transformations redundancy or physical symmetry? This
is a discrete construction fork already implicit in the global-boundary debt.
It is not booked as P4 or added to the residue in this wave, because the actual
global boundary class and even the relevant boundary geometry remain unbuilt.

## 5. Specialist and hostile review

- **Symplectic geometry:** the moment map makes the fork unavoidable. Charged
  symmetries are not quotientable unless the phase space is extended.
- **Variational PDE:** Dirichlet and zero-momentum restrictions are legitimate
  conditional domains, but differentiability alone does not rank them against
  an edge completion.
- **Differential geometry:** full bundle equivariance does not automatically
  type boundary automorphisms as characteristic directions.
- **Source criticism:** the source confirms the bulk grammar and boundary
  debt, not the selector predicate.
- **Analytic/path-integral:** no maximal domain, Green inverse, contour,
  determinant, reflection positivity or measure follows.
- **Constraint accounting:** the edge coefficients have zero remaining
  freedom, but the horn itself depends on one unowned discrete disposition.

The hostile review therefore allows the edge horn to lead the construction
only while the charged-symmetry horn remains a comparator.

## 6. Seven-axis disposition

- **Layer 0:** bulk gauge, boundary gauge, charged symmetry, boundary
  condition, edge extension and BFV quotient are separated.
- **L1:** the four horns and two selector predicates are explicit.
- **L2:** endpoint parameters, momenta and edge coordinates remain typed.
- **L3:** the truth table, coefficients, kernel and quotient dimensions are
  exact over rationals with firing controls and an independent Sage route.
- **L4:** the result is local on the exact ten-direction endpoint bank; actual
  K77 `H`-bundle and full `tau_A0` descent remain open.
- **L5:** the conditional edge form is basic and its reduced form is
  nondegenerate; the physical boundary disposition remains unselected.
- **L6:** no polarization or common Green/Krein domain.
- **L7:** no Einstein, Standard Model, cosmology, positivity or quantum claim.

## 7. Progress and next gate

```text
Ledger v0.101 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 3
  - primary-source boundary-selection check
  - local-action unique-selection check
  - conditional two-predicate horn classification
frontier_conditions_opened: 1
  - own boundary gauge-redundancy versus physical-symmetry disposition
remaining_named_conditions: 2
```

No verdict, residue, quotient, fork registry, canon, public posture or datum
changes.

Next:

`CONDITIONAL_EDGE_HORN_ACTUAL_K77_H_ACTION_TRACE_AND_FULL_TAU_A0_GLOBAL_MOMENT_MAP__KEEP_CHARGED_BOUNDARY_SYMMETRY_AS_COMPARATOR`.
