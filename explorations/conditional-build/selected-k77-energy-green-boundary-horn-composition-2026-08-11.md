---
artifact_type: construction_and_scope_result
created: 2026-08-11
run_id: RUN-20260811-182311-gu-k77-energy-green-boundary-horn-composition
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_version: "0.179"
result: BOTH_DOUBLED_MAJORANA_HORNS_ARE_ACTION_GREEN_ISOTROPIC_ON_THE_EXACT_INCOMING_ENERGY_HALF__ONE_SIDED_INDEPENDENT_DUAL_OBSTRUCTION_RETRACTED_AS_WRONG_OBJECT
grade: "exact full-carrier two-prime finite graded-linear algebra with four firing plants; local flat principal boundary compatibility only"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
fork_assumed: none
fork_note: "Real K77 and both action-pairing horns are labelled conditional comparators."
source_return: SOURCE-SILENT
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
---

# Selected K77 energy/Green boundary-horn composition

## Plain-English result

The completed K77 equation has a precise incoming half at a spatial boundary:
960 of its 1,920 components carry negative energy flux. The first calculation
appeared to show that this half failed the action boundary condition for both
candidate pairings. That calculation was exact—and answered the wrong
question. It treated the barred field as independent after the Majorana
reality relation had already been required.

Composing the reality relation changes the boundary object. On the correctly
doubled Majorana graph, the action boundary form vanishes on the incoming half
for both complete pairing horns, exactly over two finite fields. So the local
flat energy boundary condition and the fermion action are algebraically
compatible. This does not choose between the horns, globalize the boundary
condition, or derive a physical chiral quotient.

## Adaptive preflight

- **Layer 0/source:** independent barred fields, Majorana-reduced fields and
  spatial incoming modes are separate objects; source return is mandatory.
- **Symmetric hyperbolic:** the incoming carrier is `ker(E+1)` for the exact
  involutive spatial evolution.
- **Supergeometry/Grassmann:** owns the doubled odd-field Green signs.
- **Symplectic/BV-BFV:** owns isotropy after the physical graph pullback and
  prevents a one-sided coefficient from becoming a domain theorem.
- **Krein/reality:** owns the two complete Spin-natural pairing horns.
- **Exact computation:** checks the full 1,920-dimensional carrier over
  `GF(1009)` and `GF(1013)` with four firing plants.

## The load-bearing Layer-0 correction

For a spatial normal coefficient `D_n` and pairing `P`, the independent-dual
one-sided form is `P D_n`. Restricted to `ker(E+1)`, it has rank `960` in both
horns and both primes. This reproduces the K95 obstruction class.

The physical Majorana domain is instead the graph
`bar=P conjugate(psi)` in doubled barred/unbarred field space. Pulling back the
graded Green form produces

```text
P^T D_n + D_n^T P.
```

For the symmetric/anti-adjoint horn it vanishes by anti-adjointness. For the
skew/self-adjoint horn it vanishes by skewness plus self-adjointness. The
restriction to the 960-dimensional incoming half therefore has rank zero for
both horns. The full-rank one-sided result remains useful as a planted
wrong-object control; it is not the physical no-go.

## Exact result

| object | symmetric/anti-adjoint | skew/self-adjoint |
| --- | ---: | ---: |
| one-sided `P D_n` on incoming half | 960 | 960 |
| doubled Majorana Green pullback | 0 | 0 |

The incoming and outgoing eigenspaces each have rank `960` and together span
all `1,920` components. Both primes reproduce every rank. A non-invariant
pairing plant yields rank `832`, while the zero-carrier plant is rejected by
the independently verified rank-960 eigenspace.

## What moved and what did not

Closed:

- local flat algebraic compatibility between the exact incoming energy half
  and both doubled Majorana action graphs;
- the false inference from the one-sided K95-style obstruction to the
  reality-reduced physical domain.

Still open:

- variable-coefficient and global observed transport of the incoming graph;
- whether the selected action owns or selects the spatial projector rather
  than merely admitting it;
- horn and conditional-`p` selection;
- ambient `Y^14`, null BFV, unrestricted moving terms, observation,
  cohomology, chirality, mirror removal, index and count.

Selected Spin, the two `U(32,32)` halves and the full `U(64,64)` parent remain
distinct. P1/P2/P3 are unchanged and unused. No verdict, residue, quotient,
canon verdict or public posture changes.

## Frontier

```text
headline_delta: none
frontier_conditions_closed: 2
  - both exact action-pairing horns admit the incoming energy half after the required doubled Majorana pullback
  - the one-sided independent-dual obstruction is fenced to the object it actually computes
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - variable/global transport and action ownership of the incoming projector
  - ambient/null BFV, horn/p selection, observation and physical cohomology
```

## Next gate

`GLOBALIZE_THE_COMMON_DOUBLED_MAJORANA_INCOMING_RELATION_TO_THE_VARIABLE_COEFFICIENT_OBSERVED_SYSTEM_AND_TEST_ACTION_OWNERSHIP_OR_TRANSPORT_OF_ITS_PROJECTOR__KEEP_NULL_BFV_AMBIENT_Y14_HORN_P_AND_PHYSICAL_COHOMOLOGY_SEPARATE`.

Probe:
`tests/channel-swings/selected_k77_energy_green_boundary_horn_composition_probe.py`.
