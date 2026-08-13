---
artifact_type: construction_and_scope_result
created: 2026-08-11
run_id: RUN-20260811-191942-gu-k77-variable-incoming-projector-descent
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_version: "0.180"
result: ACTION_DERIVES_THE_VARIABLE_INCOMING_PROJECTOR_FAMILY__BOUNDARY_GEOMETRY_SELECTS_THE_MEMBER__BOTH_DOUBLED_MAJORANA_HORNS_TRANSPORT__GLOBAL_ANALYTIC_CLOSURE_OPEN
grade: "exact polynomial associated-bundle and connection-naturality theorem composed with immutable full-rank-1920 spatial-Clifford and Green receipts; local variable-coefficient principal IBVP data conditional on standard regularity"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
fork_assumed: none
fork_note: "Real K77 and both action-pairing horns remain labelled conditional comparators."
source_return: SOURCE-SILENT
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
---

# Selected K77 variable incoming-projector descent

## Plain-English result

The missing spatial projector does not have to be supplied as another external
datum. Once the observed system and an oriented unit spatial boundary normal
are given, the action's own time and normal principal coefficients determine
the evolution matrix

```text
E_n = D_t^-1 D_n
```

and the incoming projector is the exact polynomial

```text
Pi_in(n) = (I-E_n)/2.
```

Because the completed K77 spatial generators satisfy the Clifford relations,
`E_n^2=I` for every unit spatial normal. The polynomial is therefore a
rank-960 projector on the full rank-1,920 carrier. It moves correctly when the
normal and local spin frame move, its connection derivative is tensorial, and
its flux is negative in the transported positive principal energy.

The ownership split is precise. The action derives the **map from an oriented
unit normal to a projector**. The observed boundary geometry supplies the
boundary hypersurface and outward normal that select one member. Reversing the
normal swaps incoming and outgoing. The action still does not select a unique
physical boundary, a pairing horn, conditional `p`, or a global spacetime
domain.

Both doubled-Majorana action horns remain Green-isotropic after transport. The
one-sided independent-dual form stays nonzero and is retained as the firing
wrong-object control.

## Layer 0

| phrase | exact object | not established |
| --- | --- | --- |
| projector family | `n -> (I-D_t^-1 D_n)/2` from the action principal coefficients | a unique selected boundary or normal |
| global descent | an associated-bundle projector with connection-natural derivative | global-in-time PDE well-posedness |
| variable principal domain | smooth constant-rank negative-flux data on noncharacteristic charts | nonlinear constraint propagation or a global Fredholm domain |
| Majorana Green compatibility | the doubled odd-field pullback for both complete horns | horn or `p` selection |
| observed spatial boundary | a timelike boundary with outward unit spacelike conormal | the ambient `Y^14` or null-characteristic BFV problem |

## Exact construction

The immutable v0.173 certificate gives exact spatial Clifford relations for
the completed full carrier; v0.167 makes the actual normal symbol an
associated-bundle morphism; v0.179 gives the exact `960+960` split and both
doubled-horn Green ranks zero. The new composition is formal:

```text
E_i = U_ij E_j U_ij^-1
Pi_i = (I-E_i)/2 = U_ij Pi_j U_ij^-1.
```

For a moving frame with `Omega=(dU)U^-1`,

```text
nabla Pi_i = dPi_i - [Omega,Pi_i] = U (dPi_0) U^-1.
```

Writing the transported positive energy as

```text
H_i = U^-T H_0 U^-1,
D_t,i = H_i,
D_n,i = H_i E_i,
```

shows that `D_t^-1 D_n=E_i`, `D_n` is symmetric, and on the incoming image

```text
Pi_in^T D_n Pi_in = - Pi_in^T H Pi_in.
```

Thus the projector is derived from the action coefficient pair, not fitted
independently.

## Adaptive specialist assessment

- **Layer-0/source:** separates source grammar, repository construction,
  projector family, selected member and analytic domain.
- **Principal-bundle geometry:** the polynomial functional calculus makes
  descent automatic once the action coefficient descends.
- **Symmetric-hyperbolic/analytic:** smooth coefficients and a positive Gram
  energy provide local chartwise estimates; global-in-time closure still
  needs regularity, bounded geometry, compatibility and global hyperbolicity.
- **Supergeometry/Grassmann:** the physical boundary test remains the doubled
  Majorana graph, not the one-sided independent-dual map.
- **Symplectic/BV-BFV:** pointwise Green isotropy closes, while unrestricted
  boundary charges and null BFV do not.
- **Krein/reality:** both complete action-pairing horns transport and neither
  is selected.
- **Exact computation:** a noncommuting rational three-patch fixture, moving
  rational unit normal and six firing plants pass `63/63`.

## What moved and what did not

Closed:

- an independently supplied incoming projector is unnecessary on the
  noncharacteristic observed branch;
- the action derives the full moving projector family from `D_t,D_n`;
- associated-bundle and connection-level transport are exact; and
- both doubled-Majorana Green identities survive the transport.

Still open:

- selection or physical existence of a particular global boundary geometry;
- global-in-time and nonlinear constraint-compatible well-posedness;
- source-derived BV differential, boundary invariance and physical mirror
  cohomology;
- ambient `Y^14`, null BFV, unrestricted moving terms, horn/`p` selection,
  observation, chirality, index and count.

Selected Spin, the two `U(32,32)` halves and full `U(64,64)` remain distinct.
P1/P2/P3 are unchanged and unused. No verdict, residue, quotient, canon verdict
or public posture changes.

## Frontier

```text
headline_delta: none
frontier_conditions_closed: 3
  - independent-projector gap closed by the action polynomial
  - moving associated-bundle and connection transport exact
  - both doubled-Majorana Green identities transport
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - source-derived constraint/BV invariance and physical mirror cohomology
  - global-in-time estimates, null BFV, horn/p selection and index/count
```

## Next gate

`COMPOSE_THE_ACTION_DERIVED_INCOMING_PROJECTOR_FAMILY_WITH_THE_SOURCE_DERIVED_CONSTRAINT_BV_DIFFERENTIAL_AND_OBSERVATION_PULLBACK__TEST_BOUNDARY_INVARIANCE_AND_PHYSICAL_MIRROR_COHOMOLOGY__KEEP_GLOBAL_IN_TIME_ESTIMATES_NULL_BFV_HORN_P_AND_INDEX_COUNT_SEPARATE`.

Probe:
`tests/channel-swings/selected_k77_variable_incoming_projector_descent_probe.py`.
