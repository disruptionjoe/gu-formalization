---
artifact_type: conditional_build_result
created: 2026-08-08
status: TRANSVERSE_SIX_PRINCIPAL_AUGMENTED_TORSION_EXACT__MOVING_OPERATOR_WARD_PACKET_OPEN
source_return: SOURCE-CONFIRMS__T_EQUALS_VARPI_MINUS_ROTATED_BLC__SOURCE-SILENT__COMPLETE_PHYSICAL_DG_UPSILON_OPERATOR_BLOCK
ledger: lab/process/conditional-physics-ledger-v0.85.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 metric-transverse augmented-torsion block

## Result in plain English

The six transverse metric directions are no longer arbitrary at principal
order. They are supplied, without fitting, by the source's own
gauge-rotated-Levi-Civita definition of augmented torsion.

Write the source variables as `(g,varpi)` with

```text
T = varpi - B_LC(g).
```

At fixed independent `varpi`, a metric first jet therefore gives
`delta T=-L_q h`. The exact spin Levi-Civita map `L_q` has rank nine on the
ten metric values. Its one-dimensional kernel is `q tensor q`, which lies
entirely inside the four-dimensional diffeomorphism orbit. Consequently its
restriction to the six transverse metric directions is injective, with rank
six, for timelike, spacelike and null covectors.

That closes the direct principal augmented-torsion part of all six transverse
metric columns. It does **not** close the complete metric derivative of the
raw residual. When this actual partial metric block is composed with the
source-`varpi` and conditional gamma-epsilon blocks from v0.84, the remaining
Ward packet has rank four in every causal class. Its coefficients are now
fixed on the four orbit columns: the moving Shiab/Hodge/curvature/density/
observation block must equal their negative. Constructing that operator, not
fitting it, is the next gate.

## Layer 0

| phrase | object constructed | object kept distinct |
| --- | --- | --- |
| ten metric directions | values `h in Sym2(T*X)` | their first and second jets |
| Levi-Civita response | principal `L_q h` | complete nonlinear `D_g B_LC` |
| transverse six | complement of `im D_q` at the symbol | six particles, modes or parameters |
| metric residual block | direct `kappa delta T=-kappa L_qh` constituent | moving Shiab/Hodge/curvature/density/observation |
| Ward defect | exact partial four-column residual packet | proof that a physical operator supplies it |
| source ownership | augmented-torsion difference | the completed K77 coefficient packet |

The one-dimensional kernel of `L_q` does not represent a lost transverse
physical direction: it lies in the diffeomorphism orbit and is removed by the
transverse projector.

## Exact theorem

For each nonzero causal representative, let

```text
D_q : V -> Sym2(V*)
L_q : Sym2(V*) -> V* tensor Lambda2(V*)
P_perp = 1 - D_q (D_q^T D_q)^-1 D_q^T.
```

The exact rational result is

```text
rank D_q       = 4
rank P_perp    = 6
rank L_q       = 9
ker L_q        = span(q tensor q) subset im D_q
rank L_qP_perp = 6.
```

The direct torsion contribution has the same ranks because its embedding in
the raw-residual target is coefficientwise injective. On the causal orbit,
the partial sum

```text
J_g^(delta T) D_q + J_varpi C_q + J_epsilon gamma_q
```

has rank four. Its support counts are

```text
timelike:  14,2,2,2
spacelike: 15,15,4,4
null:      17,7,7,17.
```

Those counts equal the required missing-operator packet supports and are not
particle or generation counts.

## Constraint surplus

The block uses the already-owned metric, Levi-Civita connection, independent
`varpi`, augmented-torsion difference and selected nonzero `kappa`. It adds no
field, continuous coefficient, discrete datum or quotient. Six transverse
principal conditions close with zero adjustable freedom.

The remaining orbit packet is also coefficientwise fixed, but its owner is
not constructed. Ward cancellation alone cannot promote its negative into a
physical Shiab/Hodge operator.

## Specialist and hostile review

- **Differential geometry:** `ker L_q=span(q tensor q)` is gauge-orbit, while
  `L_qP_perp` is injective on all six transverse directions.
- **Representation/Clifford geometry:** the direct block is grade-two; it is
  distinct from the grade-one gamma-epsilon construction.
- **Variational PDE:** this closes the principal torsion input block, not the
  lower-order/full Frechet derivative.
- **Symplectic geometry:** neither a symbol rank nor `J R` target constructs a
  reduced covariant phase space, charge or BFV class.
- **Krein/operator theory:** no residual pairing, adjoint, positivity or
  common domain is assumed.
- **Complex/path-integral:** no contour, determinant, saddle or measure is
  selected.
- **Source criticism:** the source owns `T=varpi-B_LC`; it is silent on the
  completed moving-operator packet.
- **Repo archaeology:** v0.84's fitted four-orbit metric values are superseded
  by the actual direct torsion block wherever that block is claimed; the
  remaining operator packet is retained explicitly rather than hidden.

## Progress meter

```text
Ledger v0.85 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Scoped quotients ranked — 5

headline_delta: none
frontier_conditions_closed: 3
  - the ten-to-six transverse metric decomposition is exact
  - the direct principal augmented-torsion block is rank six transversely
  - the remaining four-column operator Ward packet is coefficientwise typed
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - construct the moving Shiab/Hodge/curvature/density/observation packet and complete lower-order transverse D_g/D_epsilon Upsilon
  - derive K*, formal adjoint and Green concomitant, then form/test the stationary Gram complex
```

No verdict, residue, quotient, external datum, canon or public posture moves.
P1/P2/P3 remain unused. Curt remains formally separate.

## Verification

- exact composed main route: `57/57 PASS`;
- independent Sage/QQ certificate: `30/30 PASS`;
- orbit/transverse, rank-nine, partial/full-Ward and physics-promotion controls
  fire as intended.

## Next gate

`CONSTRUCT_MOVING_SHIAB_HODGE_CURVATURE_DENSITY_OBSERVATION_OPERATOR_PACKET_ON_THE_FOUR_ORBIT_COLUMNS__THEN_COMPLETE_LOWER_ORDER_TRANSVERSE_BLOCK_AND_FULL_JR_ZERO__DERIVE_RESIDUAL_K_ADJOINT_AND_GREEN_CONCOMITANT`.
