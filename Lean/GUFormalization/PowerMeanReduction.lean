import Mathlib.Algebra.Order.Chebyshev
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Finite power-mean reduction

This file isolates the finite inequality used by the A1 reduced-potential
argument. It proves only the arithmetic kernel. The spectral realization,
the 96+96 carrier, and every physical interpretation remain in the owning
research artifact.
-/

namespace GUFormalization

open scoped BigOperators

/-- For a finite real family, the square of the quadratic sum is bounded by
the family cardinality times the quartic sum. -/
theorem powerMeanReduction {ι : Type*} [Fintype ι] (x : ι → ℝ) :
    (∑ i, x i ^ 2) ^ 2 ≤ (Fintype.card ι : ℝ) * ∑ i, x i ^ 4 := by
  have h : (∑ i, x i ^ 2) ^ 2 ≤
      ((Finset.univ : Finset ι).card : ℝ) * ∑ i, (x i ^ 2) ^ 2 := by
    simpa using
      (sq_sum_le_card_mul_sum_sq (s := Finset.univ) (f := fun i => x i ^ 2))
  have hs : (∑ i, (x i ^ 2) ^ 2) = ∑ i, x i ^ 4 := by
    apply Finset.sum_congr rfl
    intro i _hi
    ring
  simpa [hs] using h

/-- The exact 96-cell instance used by each A1 parity block. -/
theorem powerMeanReduction96 (x : Fin 96 → ℝ) :
    (∑ i, x i ^ 2) ^ 2 ≤ 96 * ∑ i, x i ^ 4 := by
  simpa using powerMeanReduction x

/-- Constant absolute magnitude attains the power-mean bound. -/
theorem powerMeanUniformEquality {ι : Type*} [Fintype ι] (c : ℝ) :
    (∑ _i : ι, c ^ 2) ^ 2 =
      (Fintype.card ι : ℝ) * ∑ _i : ι, c ^ 4 := by
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  ring

end GUFormalization
