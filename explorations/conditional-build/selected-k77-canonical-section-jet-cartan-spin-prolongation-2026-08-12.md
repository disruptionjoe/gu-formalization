---
artifact_type: construction_result
created: 2026-08-12
run_id: RUN-20260812-000025-gu-k77-canonical-section-jet-cartan-spin-prolongation
grade: EXACT_SCOPED_TWO_PRIME_ALL40_CARTAN_SPIN_COMPOSITION
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 canonical section-jet Cartan/Spin prolongation

## Result first

The actual observation-section jet now owns the local first-order
observation-plane component that v0.186 left open.  At a K77 split
`TY|_X = H + V`, the jet is a graph slope `J:H->V`.  Requiring a generator to
be purely mixed and K77-orthogonal uniquely forces its reciprocal `H<-V`
block:

```text
q(J)|_(V<-H) = J,
q(J)|_(H<-V) = -eta_H^-1 J^T eta_V,
q(J)^T eta + eta q(J) = 0.
```

There are exactly 40 independent basis directions.  All 40 have exact
128-spinor lifts over `GF(1009)` and `GF(1013)`; 18 are same-sign rotations
and 22 are opposite-sign boosts.  Gamma covariance, chirality preservation
and both pairing-block identities pass in every direction.  These all-40
identities compose with v0.186's exact full-rank-1,920 symbol and moving-H640
controls: fixed H640 leaks by rank 128 while the co-moving graph leaks by rank
zero.

No coefficient was fitted.  A blind K77-skew projection of the raw one-sided
shear returns only half the required graph slope, and omitting the reciprocal
block leaves the previous rank-eight orthogonality defect.  The exact graph
condition, not residual fitting, supplies the normalization.

## What was actually constructed

This is the canonical reductive Cartan lift of the observation graph at first
order, modulo the block stabilizer `O(H) x O(V)`.  Stabilizer motion is frame
gauge at this grade and is not booked as a datum.  The particular rank-four
section jet already used by the observation receiver maps exactly into the
40-dimensional family; its `q(J)` has rank eight over both exact fields.

The result does **not** construct the complete `epsilon_IG` complex-Cartan
flag.  It does not supply a finite nonlinear graph normalization, global atlas
overlap, action coupling of the full reduction, or lower-order BV/Koszul--Tate
closure.

## Layer 0

| object | type | disposition |
|---|---|---|
| raw `M(J)` | one-sided `GL(14)` field/equation-dual shear | valid bosonically; not K77 orthogonal |
| `q(J)` | pure off-diagonal element of `so(7,7)` | uniquely forced by graph slope and K77 metric |
| `S(q)` | even 128-spinor generator | exact all-40 Clifford lift |
| moving H640 | associated graph transported with the anchor | inherited exact full-1,920 covariance |
| `A=-G^-1(dG)/2` | symmetric changing-gimmel coframe compensator | exact in all ten metric directions; not in fixed `so(G)` |
| complete `epsilon_IG` | global complex-Cartan/soldering reduction | still unbuilt |

The ten moving-gimmel compensators satisfy
`dG + A^T G + G A = 0`, but each nontrivial `A` fails the fixed-metric Cartan
condition.  Conflating `A` with `q(J)` would reproduce the exact Layer-0 error
the wave was designed to avoid.

## Exact certificate and computational economy

The probe checks all 40 tangent/Clifford generators over both exact fields.
The complete 1,920-dimensional symbol, H640 leakage and pairing-horn controls
are inherited from the immediately preceding exact two-field certificate and
are composed only after the new all-40 coefficient identities pass.  This
avoids hundreds of redundant sparse `1920 x 1920` multiplications while
retaining a full-carrier control rather than replacing it with a dimension
analogy.

For each field:

- `dim q(H,V)=40`, with `18` rotations and `22` boosts;
- all 560 gamma commutator identities hold;
- every generator preserves chirality and both pairing block types;
- the actual `rank(J)=4` receiver maps exactly to an orthogonal `rank(q)=8`;
- the blind skew plant returns one-half of `J` and the missing reciprocal
  plant retains defect rank eight;
- all ten actual moving-gimmel basis variations have exact coframe
  compensation and are not fixed-metric Cartan motions.

## Constraint surplus and source return

The construction adds no parameter, field or external datum.  It spends the
existing section jet, K77 split and graph condition.  `P1/P2/P3` remain unused.
The source confirms the geometric ingredients and corrects their possible
identification, but is silent on this exact lift.  The theorem is
repository-derived.

Eight ledger rows migrate in distance/evidence only: `RA-D4`, `RA-E3`,
`RA-E5`, `RA-F1`, `RA-F2`, `RA-G2`, `LT-SM3`, and `AC-F1`.  Headline counts,
residue, forks, five quotients, canon and public posture do not move.

## Frontier-packet absorption

The five design packets filed at `b1686d92` were reviewed before dispatch.
None displaces this gate because this result closes the live canonical-map
dependency before lower-order BV/KT.  Their first decisive steps remain
queued: the H0 positivity inertia and dim-13 orientation bit are the strongest
nonconflicting successors; the Nguyen pincer, B5 pairing table and XS-S
four-horn block retain their packet scopes.

## Next gate

Construct or kill the finite nonlinear normalized graph/Cartan lift and its
atlas overlap descent.  Then compose that lift with the selected action's
`epsilon_IG`, gauge-rotated Levi-Civita and complete complex-Cartan flag.
Only after that composition closes should the campaign enter the lower-order
sixteen-cell Riccati and BV/Koszul--Tate system.
