---
artifact_type: build_result_and_scope_narrowing
created: 2026-08-11
status: MOVING_FIRST_JET_ANTIDUALIZER_EXACT_CONDITIONALLY__GRAPH_SELECTION_AND_ANALYTIC_DOMAIN_OPEN
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 moving anti-dualizer via the complete Darboux owner

## Result in plain English

The moving-normal mixed terms found by v0.165 are a real defect in the naive
exchange map, but they are not a no-go for every moving algebraic reality.
The complete action boundary potential itself dictates the repair.

For

```text
Theta = p_i dq^i
        + 1/2 (bar^T A(q) dpsi - dbar^T A(q) psi),
```

define

```text
u   = psi,
v   = A(q)^T bar,
P_i = p_i + 1/2 bar^T (partial_i A) psi.
```

Then, coefficientwise and exactly,

```text
Theta = P_i dQ^i + 1/2 (v^T du - dv^T u).
```

The half in the momentum correction is forced within this first-jet ansatz.
No square root of `A`, positive metric, fitted projector or new datum is used.
Pulling the constant exchange involution back through this exact Darboux map
gives a moving algebraic anti-dualizer that is involutive and anti-symplectic.

That is the constructive win. The equally important negative result is that it
works for **every supplied symmetric graph `S`**. It transports the existing
`Sym(15)` family and therefore leaves at least 120 coordinates unselected. It
repairs the motion; it does not choose the physical domain.

## Prior-art correction

This is not a wholly new cotangent-lift theorem. Ledger v0.68 already proved
the general complete Green-potential cotangent lift, its three-chart cocycle,
and all ten K77 normal momentum compensators in
`selected-k77-green-potential-splitting-basicness-2026-08-08.md`.

The new result is the composition that had not been made:

1. v0.68 supplies the complete cotangent-lift mechanism;
2. v0.165 supplies the independent-dual symmetrized Green potential and the
   failed naive moving exchange;
3. this Run specializes the lift to `v=A^T bar`, proves the forced half-shear,
   pulls back the exchange anti-dualizer, and measures its failure to select.

That distinction matters: the repository already owned the coordinate
mechanism, but had not applied it to the boundary-reality obstruction it later
created.

## Layer 0

| phrase | proved object | object still open |
| --- | --- | --- |
| moving anti-dualizer | finite first-jet anti-symplectic involution after a complete cotangent lift | source-selected physical K77 reality |
| anti-linear lift | conjugate-linear extension of a real-coefficient algebraic map | Krein-positive fundamental symmetry or closed operator domain |
| fixed locus | finite Lagrangian graph | Calderon, Lopatinski or maximal-dissipative trace space |
| action-owned correction | the `A,dA` dressing and forced half-shear | selection of the symmetric graph `S` |
| gauge compatibility | commutant subcase and small-gauge invariant graph | unrestricted charged boundary symmetry and BFV edge completion |

## Exact theorem and controls

The main exact fixture uses a genuinely moving, non-symmetric, invertible
two-by-two coefficient. The complete potential identity, inverse coordinate
map, anti-symplectic pullback, involutivity and Lagrangian fixed locus all pass
symbolically over the rationals.

The controls fire:

- omitting the momentum shear destroys potential equality;
- freezing `A` deletes a live first-jet term;
- moving to a point where `A` is singular destroys the inverse chart; and
- ordinary gauge compatibility is asserted only in the commuting coefficient
  subcase, not for an arbitrary moving matrix.

The exact probe passes `46/46`, zero failures.

## What this does not yet establish

The actual nonlinear selected K77 normal Green coefficient has not yet been
typed as one global real invertible bundle map with compatible overlap data.
The finite theorem therefore supplies a conditional local construction, not
the physical domain itself.

Still open:

- global invertibility and overlap descent of the actual coefficient;
- the true Krein/Grassmann anti-linear operator domain;
- a Calderon or maximal-dissipative projector;
- unrestricted BFV charge/edge completion;
- observation descent, mirror removal, chirality, index and count; and
- any source- or action-owned selector of the 120-coordinate graph family.

## Progress meter

```text
Ledger v0.166 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84 continuous + >=19 function-valued + 9 discrete forks
Five scoped conditional quotients ranked

headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Next:

`IDENTIFY_THE_ACTUAL_SELECTED_K77_NORMAL_GREEN_COEFFICIENT_AS_A_GLOBAL_INVERTIBLE_REAL_BUNDLE_MAP_AND_TEST_DARBOUX_DESCENT_ON_OVERLAPS__THEN_CONSTRUCT_THE_CALDERON_OR_MAXIMAL_DISSIPATIVE_PROJECTOR_AND_UNRESTRICTED_BFV_EDGE_COMPLETION__DO_NOT_SUPPLY_A_GRAPH`.

Main probe:
`tests/channel-swings/selected_k77_moving_antidualizer_darboux_probe.py`.
