---
artifact_type: conditional_build_result
created: 2026-08-08
status: SOURCE_VARIABLE_PRINCIPAL_WARD_TARGET_NARROWED_FROM_RANK4_TO_RANK3
source_return: SOURCE-CORRECTS
ledger: lab/process/conditional-physics-ledger-v0.86.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 principal Ward and gamma-epsilon reconciliation

## Result in plain English

The next moving-operator calculation was aimed at one direction too many.

The source says augmented torsion is the difference between an independent
connection `varpi` and an epsilon-rotated reference connection. On a physical
metric diffeomorphism orbit, the direct torsion change from the metric is
`-C_q xi`, while the direct torsion change from `varpi` is `+C_q xi`. Those
pieces cancel exactly in all four columns.

But `varpi` also changes the curvature part of the raw GU residual. That
surviving curvature packet has rank three for timelike, spacelike and null
covectors. A moving Shiab/Hodge/curvature/density/observation response is
therefore still required, but only on the three nonzero connection-orbit
directions.

The fourth direction in v0.85 came entirely from tying the diffeomorphism
parameter to the conditional grade-one lift `gamma_epsilon(xi-flat)`. The
primary sources do not make that identification. The construction is not
deleted; it is returned to its proper status as an internal-gauge or future
soldering proposal.

## Layer 0

| phrase | object used here | object kept separate |
| --- | --- | --- |
| source epsilon | `H`-valued gauge transformation and reference-connection variable | physical spacetime soldering field |
| gamma-epsilon | dependent grade-one Clifford lift | source-quoted diffeomorphism law |
| direct torsion response | `kappa delta T` | full raw-Upsilon response |
| full varpi response | curvature derivative plus direct torsion derivative | direct `+C_q xi` alone |
| moving operator | response of Shiab/Hodge/curvature/density/observation coefficients | invariant-branch target transport already proved zero |
| Ward packet | unreduced principal source-variable orbit | full Frechet, BV/BFV or physical equation complex |

This distinction also corrects the initial hypothesis for this wave. Direct
metric-plus-varpi torsion cancels, but full metric-plus-varpi raw-Upsilon does
not. The exact calculation, not the preregistered expectation, sets the
result.

## Exact theorem

Let `D_q` be the four-dimensional metric diffeomorphism symbol, `L_q` the
symmetric-frame spin Levi-Civita symbol, and `C_q=L_qD_q`. Then in every
causal class

```text
rank D_q = 4,
rank L_q = 9,
rank C_q = 3.
```

Write `R` for the full raw-Upsilon derivative in a horizontal `varpi`
direction. On the four orbit columns,

```text
metric direct torsion       = -C_q,
varpi direct torsion        = +C_q,
source-variable remainder   = R(C_q)-C_q,
rank source remainder       = 3.
```

The connection kernel and source-remainder supports are

```text
timelike:  kernel (1,0,0,0), supports 0,1,1,1
spacelike: kernel (0,1,0,0), supports 13,0,2,2
null:      kernel (1,0,0,1), supports 14,7,7,14.
```

The source remainder vanishes on each kernel. The conditional gamma response
is injective of rank four and is nonzero on that same kernel. Consequently

```text
source-minimal required moving operator rank = 3,
gamma-extended required moving operator rank = 4.
```

The v0.85 rank-four packet is reproduced exactly; it is retyped rather than
discarded.

## What the earlier zero-operator theorem does and does not say

The invariant-branch theorem in
`selected-invariant-constituent-operator-naturality-2026-08-07.md` proves that
shared target transport of two already-cancelled invariant constituents is
zero. Its tangent keeps those inputs invariant. The current diffeomorphism
packet contains an independent source-variable curvature derivative of rank
three. These are different tangent classes, so the former zero cannot be used
to cancel the latter nonzero packet.

## Constraint surplus

The reconciliation removes one unsupported identification and fits no
coefficient. It does not add a field, datum, quotient or parameter. The
source-minimal construction burden loses one column; the residual parameter
ledger is unchanged.

## Specialist assessment

- **Differential geometry:** `C_q` has rank three; its one-dimensional kernel
  is already harmless in the source-minimal orbit.
- **Representation/Clifford geometry:** the grade-one gamma lift is genuinely
  rank four and therefore cannot be treated as the same map as the grade-two
  spin connection orbit.
- **Variational PDE:** the surviving rank-three object is the curvature part
  of the principal Frechet packet; lower-order completion remains open.
- **Symplectic geometry:** removing an unsupported tangent is necessary, but
  neither surviving rank nor Ward cancellation yields a reduced covariant
  phase-space class.
- **Krein/operator theory:** no adjoint, positivity, Green identity or common
  domain follows from the finite rank calculation.
- **Complex/path-integral lens:** no contour, determinant or measure is
  selected.
- **Source criticism:** the source confirms epsilon's gauge role and is
  silent on gamma-epsilon as a physical diffeomorphism law.
- **Repo archaeology:** v0.54, v0.84 and v0.85 become mutually consistent once
  their tangent classes are kept separate.

## Progress meter

```text
Ledger v0.86 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Scoped quotients ranked — 5

headline_delta: none
frontier_conditions_closed: 3
  - source epsilon and conditional gamma-epsilon soldering are separated
  - direct metric/varpi torsion cancellation is exact on four columns
  - the physical moving-operator target is narrowed from rank four to rank three
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - construct the rank-three moving Shiab/Hodge/curvature/density/observation packet and complete lower-order transverse/internal-epsilon Frechet response
  - derive K*, formal adjoint and Green concomitant, then test the stationary Gram complex
```

No verdict, residue, quotient, external datum, canon or public posture moves.
P1/P2/P3 remain unused. Curt remains formally separate.

## Verification

- exact composed Python route: `62/62 PASS`;
- independent Sage/QQ route: `38/38 PASS`;
- planted controls reject zero-operator transfer, rank-three-as-rank-four and
  reduced-physics promotion.

## Next gate

`CONSTRUCT_RANK3_MOVING_SHIAB_HODGE_CURVATURE_DENSITY_OBSERVATION_PACKET__THEN_COMPLETE_LOWER_ORDER_TRANSVERSE_AND_PRIMITIVE_INTERNAL_EPSILON_FRECHET__DERIVE_K_STAR_FORMAL_ADJOINT_GREEN`.
