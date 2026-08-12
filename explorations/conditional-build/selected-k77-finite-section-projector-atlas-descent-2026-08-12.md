---
artifact_type: construction_result
created: 2026-08-12
run_id: RUN-20260812-003609-gu-k77-finite-section-projector-atlas-descent
grade: EXACT_SCOPED_TWO_PRIME_FINITE_GRAPH_PROJECTOR_AND_ATLAS_DESCENT
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 finite section projector and atlas descent

## Result first

The finite nonlinear observation-section reduction exists canonically on the
open graph chart where the induced metric is nondegenerate.  If

```text
L_J = (I,J)^T : H -> H + V,
G_J = L_J^T eta L_J = eta_H + J^T eta_V J,
```

then the section owns the exact K77 graph projector

```text
P_J = L_J G_J^-1 L_J^T eta.
```

Algebraically, `P_J^2=P_J`, `P_J^T eta=eta P_J`, `P_J L_J=L_J`, and
`rank(P_J)=4`.  The formula introduces no coefficient, field or datum.  For
the actual rank-four observation jet used by the receiver, the induced Gram
matrix is nondegenerate with Lorentzian inertia `(1,3)` over `QQ`.

The projector descends exactly under both block-stabilizer changes and
genuinely mixed K77 atlas changes.  For a mixed transition
`g=((a,b),(c,d))`, the graph coordinate transforms fractionally,

```text
J' = (c+dJ)(a+bJ)^-1,
P_J' = g P_J g^-1.
```

This was checked for three nontrivial mixed Cayley transitions over each of
`GF(1009)` and `GF(1013)`.  Dropping the fractional denominator fails, as do
the Euclidean projector and the unnormalized `L_J L_J^T eta` shortcuts.

## The load-bearing correction

The canonical finite object is the projector, equivalently the graph plane or
K77 Grassmannian/coset point.  It is **not** a preferred global `O(7,7)`
matrix.  If `g` is one local orthogonal lift, then `gk` is another for every
block-stabilizer element `k in O(H) x O(V)`, and both give the same projector:

```text
g P_0 g^-1 = (gk) P_0 (gk)^-1.
```

The exact probe exhibits this ambiguity three times in each field.  A local
normalized representative may be chosen near the zero section, and its
first derivative is exactly v0.187's forty-dimensional Cartan/Spin lift.  A
global representative or Spin lift requires a principal-bundle
trivialization/orientation lift and is not supplied by the projector.  The
next action question is therefore not “find the missing canonical matrix”;
it is whether the source-owned `epsilon_IG` carries the required local
stabilizer cocycle and completes the larger complex-Cartan flag.

## Domain and null boundary

The determinant of `G_(tJ)` is nonzero at `t=0`, so every section jet has a
real analytic neighborhood in this graph chart.  The actual rational receiver
stays in the Lorentzian `(1,3)` component.  This is local analytic existence,
not a global atlas or domain theorem.

The chart has a real boundary: mapping the positive horizontal direction to
a unit negative vertical direction makes `G_J` rank three.  The graph then
contains a null direction and the metric-orthogonal projector is undefined.
This planted case fires over both exact fields.  It is a boundary between
nondegenerate graph charts, not evidence that the finite reduction fails on
its admitted domain.

## Layer 0

| object | type | disposition |
|---|---|---|
| `Graph(J)` | finite rank-four nondegenerate observation plane | canonical section reduction |
| `P_J` | eta-self-adjoint idempotent | exact, atlas-natural, no frame choice |
| local `g_J` | normalized `O(7,7)` representative | exists locally; ambiguous by block stabilizer |
| local Spin lift | double-cover lift of a chosen oriented local `g_J` | local and sign/stabilizer dependent |
| v0.187 `q(J)` | derivative of the local reduction at the zero section | exact tangent, 40 dimensions |
| complete `epsilon_IG` | action-owned complex-Cartan/soldering flag | still unbuilt |

## Exact certificate and controls

The 39-check probe passes with no failure.  Per exact field it verifies the
rank-four graph and projector, eta self-adjointness, graph ownership,
orthogonal complement, all forty tangent directions, one block overlap,
three genuinely mixed overlaps and three stabilizer-equivalent lifts.  It
also fires four control classes: naive mixed transition, Euclidean adjoint,
missing Gram normalization and the null-graph boundary.  The two fields
reproduce the same structural fingerprint.

## Source, surplus and physics boundary

Weinstein's material confirms that observation/pullback is a rich geometric
operation and assigns gauge-rotated Levi-Civita to the contorsion slot.  It
does not state this exact graph projector, atlas law or stabilizer cocycle.
The result is repository-derived.

Constraint surplus is positive in the narrow construction sense: the existing
forty graph coordinates must satisfy projector, metric, rank, tangent and
overlap identities without any additional parameter.  This does not derive a
source action, a preferred pairing horn, chirality, generations, the Higgs,
an Euler equation, BV cohomology or a global analytic domain.  P1/P2/P3 remain
unused.  Full `U(64,64)` and the two `U(32,32)` halves remain distinct.

Eight ledger rows migrate in evidence/distance only: `RA-D4`, `RA-E3`,
`RA-E5`, `RA-F1`, `RA-F2`, `RA-G2`, `LT-SM3`, and `AC-F1`.  Headline counts,
residue, forks, five booked quotients, canon and public posture do not move.

## Next gate

Compose the local projector/lift cocycle with the selected action's
`epsilon_IG`, gauge-rotated Levi-Civita and complete complex-Cartan flag.  The
construction must show that the action owns the stabilizer transition rather
than selecting a frame by convention.  Only after that closes should the
campaign insert the surviving zero-order Higgs chain and solve the complete
sixteen-cell lower-order Riccati, barred-adjoint and BV/Koszul--Tate system.
