---
artifact_type: exact_residual_first_connection_jet_theorem
created: 2026-08-14
status: POINTWISE_REAL_RESIDUAL_ZERO_JET_EXISTS_FOR_EVERY_DEPENDENT_BZ__CURVED_BZ_FORCES_NONZERO_FIRST_PROLONGATION_TARGET__OPEN_BACKGROUND_STILL_MISSING
lane_id: SRC-RES-COH-01
source_claims: [SC-ACT-01, SC-ACT-04, SC-ACT-05]
probe: tests/channel-swings/selected_k77_zorro_source_residual_point_jet_prolongation_probe.py
registry: lab/process/selected-k77-zorro-source-residual-point-jet-prolongation.json
hostile_review: lab/process/hostile-reviews/2026-08-14-selected-k77-zorro-source-residual-point-jet-prolongation-review.md
canon_verdict_change: none
ledger_row_changes: none
---

# Canonical-Zorro source-residual point jet and prolongation gate

## Result first

The canonical Zorro connection's curvature is **not** a pointwise algebraic
obstruction to the source equation.  At any point `y`, hold the distinguished
connection `B_Z` dependent and use the source-owned independent connection
`varpi`.  Choose

```text
varpi_y = (B_Z)_y,                 so T_y=0,
Alt(partial varpi)_y = -varpi_y wedge varpi_y,
```

which makes

```text
F_varpi(y)=0,
Upsilon_B(y)=Shiab(F_varpi(y))+Hodge(T_y)=0.
```

This is a universal real connection-jet construction.  It uses no inverse,
rank assumption or fitted coefficient in Shiab and introduces no new field or
external datum.  An exact nonabelian matrix control has curved `B_Z`, equal
connection values, zero `F_varpi`, and a nonzero distortion derivative.

The important result is the next-order cost.  Because the connection values
agree while their curvatures do not,

```text
Alt(D T)_y = F_varpi(y)-F_BZ(y) = -F_BZ(y).
```

At `T=F_varpi=0`, differentiation of the residual reduces to

```text
D Upsilon_B
  = Shiab(D_varpi F_varpi) + Hodge(D T).
```

Thus curved canonical geometry forces a live target for the second `varpi`
jet.  A residual-zero germ exists only if the actual K77 differentiated-Shiab
image, with Bianchi and symmetric second-jet compatibility imposed, contains
`-Hodge(DT)`.  That image question—not the old `b Phi1` fit—is now the first
honest possible obstruction.

## What this corrects

The preceding wave proved that neither nonzero homogeneous `b Phi1` branch is
a background for the canonical Zorro/DeWitt connection metric.  It did not
prove the source action lacks a pointwise solution, because `B_Z` is dependent
while `varpi` has its own first jet.  The construction here uses precisely
that missing freedom.

Conversely, it would be an equal error to call this a vacuum.  A one-point jet
does not provide an open solution, stationary first-action field tuple,
formal power series, analytic germ, global atlas, domain, or boundary law.

## Layer 0

| object | result here | not established |
| --- | --- | --- |
| `B_Z` | dependent canonical Zorro connection | an independently fitted source field |
| `varpi` | independent source connection | `B_Z` or a second Zorro connection |
| `T=varpi-B_Z` | homogeneous difference; value zero, derivative nonzero | an independently varied torsion tensor |
| residual zero | one real point jet | an open stationary background |
| first prolongation | explicit target `-Hodge(DT)` | target membership in the actual K77 differentiated-Shiab image |
| `I2B` | stationary automatically at true bosonic residual zero | a square of the total boson--fermion residual |

## Exact connection-jet proof

For a connection with point values `A_i` and first derivatives `A_{i,j}`,

```text
F_A(i,j)=A_{j,i}-A_{i,j}+[A_i,A_j]
```

up to the fixed derivative-index convention.  Once the values are fixed to
`A_i=(B_Z)_i`, the antisymmetric derivative part is still free.  Setting it
to the negative commutator makes every `F_A(i,j)` zero.  This is allowed
because `varpi` is an independent connection variable, not the Levi-Civita
connection reconstructed from the metric.

The exact control uses three noncommuting `2 x 2` rational matrices.  All
three `B_Z` curvature components are nonzero, every `varpi` curvature
component vanishes, and all three alternating distortion derivatives equal
minus the corresponding `B_Z` curvature.  Freezing the independent first jet
fires the curvature control.

The two connections are not gauge-conjugate at the point: gauge conjugation
cannot carry nonzero curvature to zero.  The theorem is instead about the
source's independent connection coordinate.

## The flat-patch shortcut is killed

Do not extend the point construction by simply declaring `varpi` flat on a
whole patch.  If `F_varpi=0` and `Upsilon_B=0`, then invertibility of the Hodge
mass term gives `T=0`.  Hence `varpi=B_Z` and `F_BZ=F_varpi=0`, contradicting
a curved canonical `B_Z`.

So a curved solution, if it exists, must be nonflat and must use the
differentiated Shiab term to compensate the forced `DT`.  This is a scoped
kill of one shortcut, not a no-go for the source equation.

## Variational composition

At an actual bosonic residual zero,

```text
d I2B = (D Upsilon_B)^! Q_B Upsilon_B = 0,
H_I2B = (D Upsilon_B)^! Q_B (D Upsilon_B).
```

Zero independent barred and unbarred fermions also contribute no tadpole to
the first-order total residual.  These facts remain conditional on extending
the point jet to one action-owned background.  Other independent `I1` metric,
observation and preboundary equations have not been proved here and must not
be inferred from the `varpi` residual alone.

## Hostile ceiling

The three strongest overclaims all fail:

1. pointwise residual zero is not an open solution;
2. the finite identity-Shiab plant is only a firing control, not evidence that
   the actual K77 target is in the image; and
3. `I2B` stationarity at residual zero does not settle the complete first
   action or its boundary problem.

No canon verdict, ledger row, residue, quotient, external datum, W/mirror,
chirality, generation count, positivity or public posture changes.

## Next exact gate

Freeze the constructed real point jet and compute the actual selected-K77 map

```text
j^2 varpi  ->  j^1 Upsilon_B,
```

with the symmetric second-jet identities and connection Bianchi identity
included.  Test whether its image contains `-Hodge(DT)` for the canonical
Zorro curvature module.  If it does, append the remaining first-action metric,
observation and fixed-boundary Euler rows on the same jet.  If it does not, the
result is the first reconstruction-scoped nonexistence certificate for an
open residual-zero germ.

The exact probe passes all checks.
