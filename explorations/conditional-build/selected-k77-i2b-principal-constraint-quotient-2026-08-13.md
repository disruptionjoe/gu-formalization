---
artifact_type: construction_result
created: 2026-08-13
status: PRINCIPAL_MIXED_JET_QUOTIENT_ONTO_DIM14__TARGET_ADMITTED__PROPAGATION_AND_GLOBAL_REALIZATION_OPEN
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: SC-ACT-04
source_return: SOURCE_CONFIRMS_I2B_CONNECTION_GRAMMAR__SOURCE_SILENT_PRINCIPAL_CONSTRAINT_SPLIT_PROPAGATION_AND_REPRESENTATIVE_SELECTION
canon_verdict_change: none
fork_assumed: none
search_space_dim: "two exact 196 by 196 real blocks and their induced quotient; decided wholesale"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
---

# Selected K77 I2B principal constraint quotient

## Result in plain English

The previous result said that a time-time connection second derivative alone
misses fourteen field-equation directions, while adding one time-space mixed
derivative makes the local equation solvable. This wave identifies the exact
reason: the time-time block has a fourteen-dimensional cokernel, and the
time-space block maps onto **all fourteen** missing quotient directions. The
fourteen-cell target is nonzero in the timelike quotient and becomes solvable
precisely after the mixed block is admitted.

This is better typed as a principal evolution/constraint split candidate than
as a missing action coefficient. It does **not** yet say the mixed derivatives
are freely specifiable Cauchy data. The actual PDE must propagate the
constraints, the initial surface must be admissible, and a nonlinear
connection must realize the jet while satisfying Bianchi, overlap,
observation, lower-order and boundary/BV conditions.

## Exact theorem

```text
rank(B00)                              = 182
rank(B01)                               = 28
dim coker(B00)                          = 14
rank(B01 -> coker(B00))                 = 14
dim ker(B01 -> coker(B00))              = 182
rank(B00 | target)                      = 183
rank(B00,B01 | target)                  = 196
dim affine fibre of (B00,B01)x=target   = 196
```

Thus the induced mixed-block map is onto the complete timelike cokernel, and
the target class lies in its image. The theorem is quotient-invariant; it does
not choose a complement or a preferred solution.

## Layer 0 and interpretation

Three objects remain distinct:

1. the fourteen-dimensional quotient of field equations missed by `B00`;
2. a chosen fourteen-column complement inside the rank-28 `B01` block;
3. a physical Cauchy/constraint space after propagation and gauge reduction.

Only the first is canonical at this grade. The second depends on a basis or
section. The third has not been constructed. Likewise, the 196-dimensional
affine solution fibre is field-jet freedom, not 196 new constants in the
theory and not evidence of source selection.

## Hostile review

The review returns
`SCOPED_THEOREM__PRINCIPAL_CONSTRAINT_QUOTIENT_ONLY`. The rank coincidence is
not bookkeeping: exact quotient ranks and target augmentation prove it. But
the phrase “Cauchy data” would outrun the certificate because there is no
constraint-propagation theorem, noncharacteristic domain, nonlinear Bianchi
solution, or BV-reduced phase space here.

## Source return and ledger disposition

Weinstein's source material supports the connection and I2B residual-square
grammar. It does not state this exact `182+14` split, supply its propagation
law, or select a representative jet.

No ledger migration is booked. The 82 rows remain fully mapped with unchanged
verdict, residue, tightness and quotient counts. This result sharpens the
distance on `RA-E1`, `RA-E3`, and `LT-SM6`: do not seek a new local bosonic
coefficient; derive the constraint-propagation/Bianchi/observation system and
then test whether initial or boundary data own the remaining affine freedom.

## Next gate

Construct the principal differential constraint complex for the selected
I2B connection equation and test:

- whether the fourteen quotient equations propagate by a Bianchi/Noether
  identity;
- whether the admitted observed time direction is noncharacteristic for the
  reduced system;
- which part of the 196-dimensional affine fibre is gauge, constrained,
  initial data, or genuine unowned freedom;
- whether nonlinear connection jets descend across the atlas and observation;
- whether the selected action's presymplectic/BV boundary structure owns the
  same split.

Do not return to action-coefficient fitting or promote local mixed-jet
availability to a physical solution.
