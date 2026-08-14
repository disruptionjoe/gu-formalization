---
artifact_type: exact_selected_action_endpoint_charge_and_reduction_obstruction
created: 2026-08-14
status: SELECTED_ACTION_ENDPOINT_SPLIT_CHARGE_NONZERO__COTANGENT_DESCENT_FAILS_AT_FROZEN_FIXTURE__LARGER_CHARGED_EDGE_HORN_RETAINED
source_return: SOURCE_OWNS_MOVING_FRAME_AND_SOURCE_SHAPED_ACTION_GRAMMAR__REPO_DERIVES_SELECTED_ENDPOINT_51_PLUS_40_CHARGE_DECOMPOSITION__SOURCE_SILENT_STABILIZER_ZERO_LEVEL_BFV_MASTER_EQUATION_AND_ANALYTIC_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-endpoint-stabilizer-charge-gate.json
canon_verdict_change: none
---

# Selected K77 endpoint stabilizer-charge gate

## Result first

The actual frozen selected-action endpoint covector does **not** descend to
the 40-dimensional moving W/mirror polarization orbit.

The predecessor proved the exact criterion: a full-frame covector descends to
`T*(Spin(7,7)/H_split)` iff it annihilates all 51 directions of
`h_split=so(1,3)+so(6,4)`.  The present calculation evaluates the action-owned
endpoint momentum directly:

```text
P = E_B-E_T,
Q_X = P([X,T]),
X in so(7,7).
```

On the same frozen exact selected-action fixture that established the endpoint
bank, the complete decomposition is

```text
51 split components: 15 nonzero, squared fingerprint 1525648/9
40 mixed components: 15 nonzero, squared fingerprint 2364016/9
```

All values are exact real rationals.  Every one of the 91 analytic contractions
agrees with an independent exact five-point differentiation of the underlying
selected action.  Because the split support is nonempty, the necessary
annihilation test fails.  The reduced orbit moment map is therefore not
admissible on this fixture.

This does not kill the boundary route.  It selects the preregistered fallback:
retain the larger charged endpoint/edge completion and treat vanishing of the
full split moment-map section as a genuine constraint/reduction condition.
Only its zero level can descend to the 40-dimensional orbit.  The full
91-ghost BFV charge and master equation must now be constructed on the larger
edge carrier before any codimension-one analytic domain is attempted.

## Layer 0

| object | exact status | not established |
| --- | --- | --- |
| source `epsilon` | full moving labelled frame | selected W or mirror member |
| selected distortion `T` | frozen action fixture | every action background |
| endpoint momentum `E_B-E_T` | exact action derivative bank | arbitrary fitted cotangent covector |
| stabilizer charge support | 15 nonzero coordinates at the fixture | 15 globally independent constraints |
| orbit cotangent descent | fails because split charge survives | failure of the larger edge horn |
| zero moment level | necessary reduction locus | constructed regular quotient |
| full edge/BFV continuation | retained and required | closed master equation or physical cohomology |

The support count is deliberately not called a rank.  A moment-map section
may have fifteen nonzero coordinates at one point without those coordinates
defining fifteen globally independent constraint functions.

## Exact charge theorem at the selected fixture

After the tilted left quotient, the source-shaped distortion transforms
homogeneously.  For any grade-two generator `X`, its infinitesimal orbit
direction is `[X,T]`.  Pairing that direction with the exact action endpoint
covector gives the Hamiltonian component

```text
Q_X=(E_B-E_T)([X,T]).
```

Using the base axes `{0,7,8,9}`, the 91 generators separate canonically into
51 base-base/normal-normal stabilizer directions and 40 base-normal mixed
directions.  Fifteen components in each block are nonzero.  In particular,
the split values include the nonzero base-base charge `Q_(0,9)=72`; a single
such witness is already sufficient to reject cotangent descent.  The complete
support and rational fingerprints are frozen in the machine-readable registry
and exact probe.

The independent check does not reuse the analytic Euler formula for its final
comparison.  For every generator it differentiates the underlying action in
the `B` and `T` slots by exact five-point evaluation and subtracts the two
derivatives.  All 91 values agree.

## Broad route-changing lens census

- **Symplectic reduction — selected:** the stabilizer moment map is the exact
  descent obstruction; its nonzero value decides the gate without a ghost
  construction.
- **Variational bicomplex — selected:** `E_B-E_T` is used as the action-owned
  endpoint covector, rather than a generic or fitted momentum.
- **Representation theory — decisive:** the reductive `51+40` split gives the
  only correctly typed charge decomposition.
- **BRST/BFV — route switch:** nonzero stabilizer charge forbids the reduced
  orbit horn at this point; the larger edge carrier must carry the complete
  91-ghost algebra and zero-level constraint.
- **Constraint geometry — caution:** support 15 is not automatically constraint
  rank 15; regularity and reducibility remain open.
- **Source criticism — strict:** source grammar supplies the moving frame and
  action ingredients, while the exact endpoint decomposition is repository-
  derived and the source supplies no BFV/domain selection.
- **Analytic/PDE — deferred:** a boundary domain cannot repair a failed
  algebraic reduction and waits for the larger BFV complex.
- **Philosophy of science — anti-fitting:** the split charges cannot be set to
  zero by definition, and forty independent orbit variables are not added to
  rescue descent.

The direct moment-map route dominated broad rank search and premature BFV
construction.  The fallback was fixed in advance: on any surviving split
charge, retain the larger edge horn and derive the zero-level constraint.
That trigger fired.

## Hostile boundary

The strongest overclaim would be that no reduced polarization phase space can
exist.  The exact result is fixture-relative: the present selected-action
endpoint point is not in the zero level.  Another solution or boundary locus
could lie on `mu_split=0`, but this must be derived and its regularity checked.

The strongest contrary construction is the already-built conditional
group-valued edge completion.  It remains viable and is now the required
carrier rather than a rival to an available reduced-orbit horn.  The result
does not prove that the full BFV master equation closes, that the constraint
is first class on a functional phase space, or that a positive/closed analytic
domain exists.

The weakest seam is global constraint geometry: fifteen nonzero coordinate
values at the fixture establish non-descent but do not determine the rank,
singularities or reducibility of the full moment-map zero locus.

## Progress and next gate

No ledger verdict, residue, datum, quotient, generation count, canon claim or
public posture changes.  Configuration ownership remains closed, while the
reduced cotangent owner is rejected at the current fixture.

Next construct the full 91-ghost BFV charge on the retained charged edge
completion, including the stabilizer zero-level constraint and all structure
constants, and verify the classical master equation.  Only after closure may
a codimension-one analytic domain be constructed.  Do not choose W or mirror,
call the orbit physical cohomology, assume constraint regularity, or begin the
analytic domain early.

## Reproduction

```sh
uv run --with sympy==1.14.0 python \
  tests/channel-swings/selected_k77_endpoint_stabilizer_charge_gate_probe.py
```

The exact probe replays the selected-action bank and validates the registry.
