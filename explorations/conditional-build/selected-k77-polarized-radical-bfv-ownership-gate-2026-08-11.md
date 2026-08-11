---
artifact_type: construction_and_composition_result
created: 2026-08-11
run_id: RUN-20260811-111511-gu-k77-polarized-radical-bfv-ownership
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_version: "0.172"
result: ZERO_FERMION_SELECTED_BRANCH_HAS_NO_ACTION_OWNED_GAUGE_OR_EDGE_IMAGE_MATCHING_IM_NSHARP__MOVING_CROSS_TERMS_VANISH__EDGE_QUOTIENT_LEAVES_EXACT_OBSERVED_DIM256_FERMION_RADICAL__RESTRICTION_ROUTE_STOPS_AT_THIS_BRANCH__OPERATOR_COMPLETION_RISES
grade: "EXACT principal Green and finite symplectic/BFV composition at the zero-fermion selected real-K77 branch; nonzero-fermion and global analytic BV domains open"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 polarized-radical BFV ownership gate

## Plain-English result

The action's existing gauge symmetry does **not** explain away the Green
radical found in v0.171 on the zero-fermion branch.

The mismatch is structural. The radical is a rank-128, frequency-dependent
subspace of the barred fermion trace carrier and remains visible to the
observation map. At zero fermion, ordinary gauge symmetry has zero fermion
trace. Small gauge also vanishes at the boundary, while unrestricted boundary
gauge is charged rather than redundant until edge variables are added. The
existing edge construction adds only bosonic/edge directions; after quotienting
its exact gauge kernel, the polarized fermion sector still has an exact
256-dimensional radical.

The full moving preboundary form does not rescue this specialization. Its
boson--fermion cross terms are linear in the background fermions and vanish at
`psi=bar psi=0`, leaving the degenerate polarized fermion block as a direct
summand.

So the cheap restriction route stops on the zero-fermion selected branch. This
is not a no-go for a nonzero-fermion coupled BV complex, and it is not a no-go
for changing the operator. The source-admitted wedge-Shiab/nonzero-southeast
operator completion now becomes the highest-information next construction.

## Layer 0

| phrase | object tested | object kept distinct |
| --- | --- | --- |
| Green radical | `im Nsharp(k)` inside the pure barred rank-1920 trace carrier | an action-owned gauge orbit |
| small gauge | total-field ordinary-gauge variation with parameter vanishing at the boundary | unrestricted boundary symmetry |
| boundary characteristic | edge-extended bosonic/connection gauge orbit | characteristic propagation of the fermion symbol |
| moving mixed term | a term linear in `psi` or `bar psi` | a nonzero zero-fermion coupling |
| quotient | algebraic removal of a radical | a BV/coisotropic quotient derived by the action |

The shared word `characteristic` does not identify the propagation and
presymplectic senses. Their carriers, dependence and base points differ.

## Exact composition

The v0.171 packet gives, at each of three admitted strict-center samples,

```text
rank Nsharp = 128
dim ker Nsharp = 1792
rank(observer . Nsharp) = 128.
```

The source-typed ordinary-gauge rules are

```text
s psi = c psi,
s bar psi = -bar psi c.
```

At `psi=bar psi=0`, their pure fermion boundary image has rank zero. Hence it
cannot equal `im Nsharp`. Boundary-vanishing gauge has zero complete tangential
boundary trace, while unrestricted boundary gauge has the already-computed live
moment map and is not a characteristic direction before edge extension.

For the v0.165 moving form,

```text
Theta_F = 1/2 (bar psi A(q) delta psi - delta bar psi A(q) psi).
```

Every `delta A` cross term in `d Theta_F` contains `psi` or `bar psi`; all
vanish on the zero-fermion branch. Restricting the independent dual fermions to
`ker Nsharp x ker N` therefore gives

```text
dimension = 2(1920-128) = 3584
rank      = 2(1920-256) = 3328
radical   = 256.
```

The all-ten minimal edge form has dimension 60, rank 40 and an owned
20-dimensional gauge kernel. Its direct sum with the polarized fermion block
has dimension 3644, rank 3368 and kernel 276. Quotienting the owned edge gauge
kernel leaves dimension 3624, rank 3368 and the same 256-dimensional fermion
radical. No fermionic edge carrier was constructed, and the observation map is
still rank 128 on each tested `im Nsharp`.

## What this changes

The following candidate identification is rejected at tested scope:

```text
im Nsharp = existing action-owned small-gauge/BFV characteristic image.
```

The zero-fermion restriction route may not proceed by calling the radical
gauge, quotienting it, or relying on generic moving mixed terms. The next
construction should change or complete the source operator and then recompute
its symbol, Green adjoint and domain burden.

The following remain open:

- a nonzero-fermion full coupled characteristic/BV comparison;
- a source-derived fermionic edge complex or frequency-dependent ghost lift;
- a modified observation that is basic for a genuinely owned quotient;
- global Sobolev/BV/Calderon closure and nonlinear constraint propagation;
- the source-admitted wedge-Shiab/nonzero-southeast operator completion.

No new field, parameter, selector, quotient or datum is booked. P1/P2/P3,
verdicts, residue, canon and public posture do not move.

## Specialist pre-assessment and hostile review

- **Layer-0 semantics:** demanded carrier, base-point, boundary-class and
  dependence equality before any gauge identification.
- **Symplectic geometry:** separated charged Hamiltonian boundary symmetry
  from characteristic gauge and computed the residual kernel after the owned
  edge quotient.
- **Variational geometry:** specialized the full moving preboundary form before
  reading its cross terms; they vanish at zero fermion.
- **Hyperbolic/operator theory:** retained `ker N` as one-sided evolution data
  while rejecting its promotion to an action domain.
- **BRST/BV:** used the action-owned differential and did not manufacture a
  frequency-dependent ghost lift.
- **Real Clifford/Krein:** retained the conditional real-K77 parent and inferred
  no positivity, chirality or index.
- **Source criticism:** recorded the source's independent fields and its silence
  on this quotient.
- **Contrary path:** preserved the operator-changing route and the nonzero-
  fermion branch.

The three-charge hostile review returns `SCOPED_ADVERSE`: the equality claim
fails on the zero-fermion branch, but the broader coupled and operator-changing
routes survive.

## Progress meter

```text
Ledger v0.172 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
  - existing ordinary-gauge/small-gauge image does not own im Nsharp at zero fermion
  - existing edge quotient and moving cross terms do not remove the zero-fermion radical
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - source-admitted operator completion and recomputed domain
  - nonzero-fermion coupled BV comparison if independently justified
```

## Next gate

`CONSTRUCT_THE_SOURCE_ADMITTED_REAL_K77_WEDGE_SHIAB_NONZERO_SOUTHEAST_OPERATOR_COMPLETION__RECOMPUTE_ITS_SEMISIMPLICITY_CHARACTERISTIC_KERNEL_GREEN_ADJOINT_AND_SELECTED_ACTION_COMPATIBILITY__KEEP_THE_NONZERO_FERMION_COUPLED_BV_BRANCH_SEPARATE`.

Probe:
`tests/channel-swings/selected_k77_polarized_radical_bfv_ownership_gate_probe.py`.
