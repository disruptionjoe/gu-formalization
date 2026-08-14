---
artifact_type: exact_differentiated_shiab_spencer_gate
created: 2026-08-14
status: SELECTED_K77_SHIAB_SPENCER_TARGET_ADMITTED__SYMMETRIC_SECOND_VARPI_JET_CONSTRUCTED__DEPENDENT_BZ_FIRST_ACTION_EULER_ROWS_TYPE_MISSING
lane_id: SRC-RES-COH-01
source_claims: [SC-ACT-01, SC-ACT-04, SC-ACT-05]
probe: tests/channel-swings/selected_k77_zorro_differentiated_shiab_second_jet_probe.py
registry: lab/process/selected-k77-zorro-differentiated-shiab-second-jet.json
hostile_review: lab/process/hostile-reviews/2026-08-14-selected-k77-zorro-differentiated-shiab-second-jet-review.md
canon_verdict_change: none
ledger_row_changes: none
---

# Selected-K77 differentiated-Shiab second-jet gate

## Result first

The forced first prolongation of the exact residual-zero point jet is
**admitted** for the repository-selected K77 Shiab and the canonical
Levi-Civita Zorro/DeWitt curvature module.  In the ambient orthonormal basis,
the selected `comm/symi/symi` Hodge--Shiab map acts on every basis cell by

```text
F_ij^k  |->  -2 eta_i eta_j eta_k T_k^ij.
```

It is therefore a `1274 x 1274` signed-permutation isomorphism, with `637`
columns of coefficient `+2` and `637` of coefficient `-2`.

At the predecessor point jet

```text
T=F_varpi=Upsilon_B=0,       Alt(DT)=-F_BZ,
```

choose the pure antisymmetric representative

```text
DT_(r;k)^ij = -(1/2) (F_BZ)_(rk)^ij.
```

The unique selected-Shiab inverse of `-DT` obeys differential Bianchi because
the canonical Levi-Civita curvature obeys Riemann pair exchange and algebraic
first Bianchi.  It has the explicit Spencer right inverse

```text
B_(ri);j^k = (C_(r;ij)^k + C_(i;rj)^k)/3,
```

symmetric in the derivative indices `r,i`.  Exact reconstruction gives zero
residual, Bianchi and holonomicity defects.  The canonical witness has `214`
nonzero curvature-derivative cells and `323` nonzero symmetric second-jet
cells.  No free symmetric correction to `DT` is required.

This closes the differentiated-Shiab/Spencer question, not the background.
The remaining action-owned dependent-`B_Z` Euler row is not implied by
`Upsilon_B=0` and must be computed before the point jet is stationary.

## Layer 0

| object | exact result here | not established |
| --- | --- | --- |
| selected Shiab | real signed-permutation isomorphism | source-preferred or unique product |
| inverse target | satisfies differential Bianchi on canonical Levi-Civita curvature | arbitrary distinguished-connection curvature completion |
| second `varpi` jet | explicit symmetric local two-jet | formal power series, analytic germ or open solution |
| first residual prolongation | vanishes exactly | every first-action Euler row |
| fixed boundary graph | preboundary flux vanishes | bulk dependent-connection stationarity |
| source-residual lane | `SR-1B` narrowed | `SR-1`, `SR-2` or positive physical cohomology |

## Exact selected map

The repository-selected product is one of the displayed admissible Shiab
products, not a contraction preferred or recovered from the source notes.
For each `i<j` and every `k`, direct Clifford evaluation produces exactly one
output coordinate.  Since every coefficient is `+2` or `-2`, the map is an
isomorphism without numerical rank estimation or fitted inversion.

Raw surjectivity alone would not solve the gate: a curvature derivative must
also lie in the connection-Spencer image.  The canonical target supplies the
extra structure.  Lowering its endomorphism index gives a Riemann tensor with

```text
R_(ri;jk)=R_(jk;ri),
R_(ri;jk)+R_(rj;ki)+R_(rk;ij)=0.
```

Those identities make the signed Shiab inverse obey the cyclic differential
Bianchi identity.  The displayed `1/3` formula is then an explicit right
inverse of connection-curvature antisymmetrization and proves holonomicity.

## Canonical nonvacuous module

The exact K77 port of the canonical DeWitt vertical curvature has `25`
nonzero external form legs and `107` nonzero spin coefficients.  All nine
trace--traceless external legs remain zero, while the traceless sector is
nonzero.  The witness is therefore not a zero-curvature or identity-Shiab
plant.  Reversing the selected Shiab sign leaves a residual defect, and an
antisymmetric perturbation of the second derivative fails holonomicity.

The analytic argument applies to Levi-Civita curvature with the stated
Riemann symmetries.  The executed coordinate fixture is the canonical
pure-vertical Zorro/DeWitt module.  A rival source-compatible distinguished
connection without those symmetries remains a separate reconstruction.

## First-action row audit

At `T=0`, variations of coefficient-only density, Hodge, Shiab and pairing
factors carry an outer `T` and vanish.  The observation field is a dependent
receiver in the source grammar rather than a new independent action row, and
the selected fixed-Dirichlet graph kills the preboundary flux.

The unresolved bulk term is different.  Varying the primitive epsilon moves
the dependent connection `B_Z=B(epsilon)`, so the action-owned
`E_B-E_T` covector and its metric/observation formal-adjoint chain must be
evaluated on the explicit two-jet.  Residual stationarity does not force this
row to vanish.  The exact first-order control `L=t b'` has `E_t=b'=0` while
`E_b=-t'` is nonzero, which rules out that shortcut.

## Hostile ceiling

This is a local formal two-jet admission for the canonical Levi-Civita
reconstruction.  It is not a complete stationary field tuple, a formal-
integrability theorem, an open solution, a deformation complex or physical
cohomology.  The source owns the connection/distortion/residual grammar but
does not publish this selected product, witness or Euler completion.

No canon verdict, ledger row, residue, quotient, external datum, W/mirror
choice, chirality, generation count, positivity, superposition law, Born rule
or public posture changes.

## Next exact gate

Compute the action-owned bulk `E_B-E_T` row and the primitive-epsilon
metric/observation formal-adjoint chain on this explicit two-jet.  If every
row vanishes, continue the Spencer/formal-integrability tower and assemble one
complete stationary background.  If any row is nonzero, return a stationary-
background obstruction at that precise owner and derivative grade.

Reproduce with:

```bash
sage -python tests/channel-swings/selected_k77_zorro_differentiated_shiab_second_jet_probe.py
```

The exact probe passes `46/46`.
