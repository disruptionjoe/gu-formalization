---
artifact_type: construction_result
created: 2026-08-11
grade: EXACT_SCOPED_TWO_PRIME_SPIN_CLIFFORD_PORT_GATE
canon_verdict_change: none
---

# Selected K77 first-jet fermion-symbol port gate

## Result first

The v0.28 observation first jet does **not** port literally to the fermion
principal symbol.  Its exact `4+10` field shear is invertible, but it is not
`O(7,7)`-orthogonal, so there is no fixed-Clifford-metric Spin lift of that raw
matrix.  The Levi-Civita spin connection is first order in the metric but
zeroth order in the fermion, so it cannot alter the fermion principal symbol
either.

The route itself survives in a more precisely typed form.  Exact rational
Spin transports, tested as both an opposite-sign boost and a same-sign
rotation over `GF(1009)` and `GF(1013)`, move the Clifford anchor and the
`H640` graph together.  A fixed `H640` graph then leaks by rank 128, while the
co-moving graph has leakage rank zero.  The transformed symbol equals the
conjugated original, both K77 pairings are preserved, and the full rank-1,920
carrier remains the control.

This is a local conditional witness for an `epsilon_IG`-owned moving
Spin/Clifford prolongation.  It is not yet the canonical map from the actual
observation-section jet to that prolongation.

## Plain English

The previous geometry supplied a perfectly valid change of field coordinates,
but a spinor needs more than an invertible coordinate change: it needs a change
that preserves the Clifford metric.  The raw observation shear fails that
test.  Holding the spin frame fixed therefore creates the observed leak.

There is nevertheless an exact repair class.  Rotate or boost the Clifford
frame and carry the candidate 640-dimensional fermion space with it; the leak
then disappears without fitting a residual or adding a parameter.  The next
question is whether the source action and observation geometry canonically
produce exactly this co-moving frame, rather than merely allowing it.

## Layer 0

| object | type | disposition |
|---|---|---|
| `M(J)=[[I,J^T],[0,I]]` | invertible field/equation-dual shear | valid bosonic first-jet map; not a raw Spin lift |
| Levi-Civita spin connection | metric-first-order coefficient multiplying the fermion | fermion-zero-order; cannot change its principal symbol |
| K77 orthogonal frame transport | `O(7,7)` map with Spin lift | exact local conditional witness |
| moving Clifford anchor and `H640` graph | associated transported family | exact zero-leakage under the witness |
| actual `J -> epsilon_IG` map | action-owned prolongation | unbuilt |

“First order” must name the differentiated field.  First order in a metric or
section variable does not imply principal order in the fermion equation.

## Exact certificate

For each exact field:

- `rank(H640)=640` and the ambient control has rank 1,920;
- ten transverse residuals are independent and each has rank 128;
- `rank(J)=4`, `rank(M(J))=14`, and the K77 orthogonality defect has rank 8;
- three nontrivial raw spatial tilts each leak by rank 128 on fixed `H640`;
- an invertible reparametrization preserves the ten-dimensional residual span;
- the Levi-Civita coefficient has fermion-principal response rank zero;
- boost and rotation satisfy exact vector orthogonality, Spin inverse, gamma
  covariance, symbol covariance, graph split and both pairing identities;
- fixed-graph leakage is 128 and co-moving leakage is zero.

The cross-prime fingerprints are identical.  No complexified
signature-dependent inference is used.

## Constraint-surplus and boundary

The witness is a pure frame transport and adds no field coefficient, selector
or datum.  `P1/P2/P3` remain unused.  Pairing preservation is not horn
selection, BV cohomology, a closed domain, positivity, index, chirality or
generation count.  The witness also does not choose between a full
`U(64,64)` presentation and two `U(32,32)` halves.

Eight ledger rows migrate in evidence/distance only: `RA-D4`, `RA-E3`,
`RA-E5`, `RA-F1`, `RA-F2`, `RA-G2`, `LT-SM3`, and `AC-F1`.  Headline counts,
residue, forks, five quotients, canon and public posture do not move.

## Next gate

Construct or kill the canonical action-owned map from the actual observation
section jet to a K77-orthogonal `epsilon_IG` Clifford anchor and moving `H640`
graph.  Retest all 40 mixed directions, both pairing horns and the full
rank-1,920 carrier.  Only then insert the surviving lower-order sixteen-cell
Higgs/Yukawa system and derive BV/Koszul--Tate and analytic domains.
