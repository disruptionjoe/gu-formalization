import Mathlib

/-!
# Finite Shiab multiplicity certificate

This module checks the finite Schur-overlap deduction from the already supplied
irreducible decomposition tables for
`Λ² V ⊗ S±` and `V ⊗ S±`.  It does not construct those decompositions, prove
the D7 representation theory behind them, select GU's Shiab, or identify a
physical real form.
-/

namespace GUFormalization.ShiabMultiplicityCertificate

/-- The two complex chiralities used by the supplied decomposition table. -/
inductive Chirality where
  | plus
  | minus
  deriving DecidableEq, Fintype

/-- Only the six irreducible labels occurring in the supplied four rows. -/
inductive Irrep where
  | spinPlus
  | spinMinus
  | vectorSpinPlus
  | vectorSpinMinus
  | twoFormSpinPlus
  | twoFormSpinMinus
  deriving DecidableEq, Fintype

/-- Complex dimensions attached to the supplied D7 labels. -/
def irrepDimension : Irrep → ℕ
  | .spinPlus | .spinMinus => 64
  | .vectorSpinPlus | .vectorSpinMinus => 832
  | .twoFormSpinPlus | .twoFormSpinMinus => 4928

/-- Multiplicity table for `Λ² V ⊗ S±`. -/
def sourceMultiplicity : Chirality → Irrep → ℕ
  | .plus, .spinPlus | .plus, .vectorSpinMinus
  | .plus, .twoFormSpinPlus => 1
  | .minus, .spinMinus | .minus, .vectorSpinPlus
  | .minus, .twoFormSpinMinus => 1
  | _, _ => 0

/-- Multiplicity table for `V ⊗ S±`. -/
def targetMultiplicity : Chirality → Irrep → ℕ
  | .plus, .spinMinus | .plus, .vectorSpinPlus => 1
  | .minus, .spinPlus | .minus, .vectorSpinMinus => 1
  | _, _ => 0

/-- Dimension reconstructed from one supplied finite multiplicity row. -/
def tableDimension (multiplicity : Irrep → ℕ) : ℕ :=
  ∑ irrep : Irrep, multiplicity irrep * irrepDimension irrep

/-- Schur-overlap multiplicity derived from the supplied source and target
decomposition rows. -/
def homMultiplicity (source target : Chirality) : ℕ :=
  ∑ irrep : Irrep,
    sourceMultiplicity source irrep * targetMultiplicity target irrep

theorem source_dimension_plus :
    tableDimension (sourceMultiplicity .plus) = 91 * 64 := by
  decide

theorem source_dimension_minus :
    tableDimension (sourceMultiplicity .minus) = 91 * 64 := by
  decide

theorem target_dimension_plus :
    tableDimension (targetMultiplicity .plus) = 14 * 64 := by
  decide

theorem target_dimension_minus :
    tableDimension (targetMultiplicity .minus) = 14 * 64 := by
  decide

/-- The supplied rows have no same-chirality common constituent. -/
theorem chirality_preserving_blocks_zero :
    homMultiplicity .plus .plus = 0 ∧
      homMultiplicity .minus .minus = 0 := by
  decide

/-- Each chirality-flipping block has the two supplied common constituents:
the spinor trace channel and the vector-spinor channel. -/
theorem chirality_flipping_blocks_two :
    homMultiplicity .plus .minus = 2 ∧
      homMultiplicity .minus .plus = 2 := by
  decide

/-- Summing the four complex chiral blocks gives the full-Dirac value four. -/
theorem fullDiracMultiplicity :
    homMultiplicity .plus .plus + homMultiplicity .plus .minus +
      homMultiplicity .minus .plus + homMultiplicity .minus .minus = 4 := by
  decide

/-- The natural chirality-flipping block is not unique up to scale at the
level of the supplied complex decomposition certificate. -/
theorem naturalBlockNotMultiplicityOne :
    homMultiplicity .plus .minus ≠ 1 := by
  decide

end GUFormalization.ShiabMultiplicityCertificate
