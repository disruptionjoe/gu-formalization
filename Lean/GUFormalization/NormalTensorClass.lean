import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
Finite coefficient core only. The written proof supplies the complete four-word
Clifford basis, the plus/reversion K95 comparator adjoint convention, Lie generation, and actual
contraction. This file does NOT prove those representation/geometric premises,
source necessity, physical positivity, or a GU exclusion.
-/
namespace GUFormalization.NormalTensorClass

/-- A coefficient simultaneously real and purely imaginary is zero. The two
laws come from optional C compatibility and plus-comparator sharp-skew in the written
complete real Clifford basis. -/
theorem real_and_skew_conjugate_zero (z : ℂ)
    (reality : star z = z) (skew : star z = -z) : z = 0 := by
  have h : z = -z := reality.symm.trans skew
  have hr := congrArg Complex.re h
  have hi := congrArg Complex.im h
  apply Complex.ext
  · simp only [Complex.neg_re] at hr
    simp only [Complex.zero_re]
    linarith
  · simp only [Complex.neg_im] at hi
    simp only [Complex.zero_im]
    linarith

theorem all_four_coefficients_zero (z : Fin 4 → ℂ)
    (reality : ∀ i, star (z i) = z i)
    (skew : ∀ i, star (z i) = -z i) : z = 0 := by
  funext i
  exact real_and_skew_conjugate_zero (z i) (reality i) (skew i)

/-- The contracted coefficient map has no kernel; its factor10 is nonzero. -/
theorem contraction_injective (z w : Fin 4 → ℂ)
    (equal : ∀ i, 10 * z i = 10 * w i) : z = w := by
  funext i
  have h := equal i
  exact (mul_left_cancel₀ (by norm_num : (10 : ℂ) ≠ 0)) h

/-- Vanishing of both ambient pairs forces the zero tensor parameters. -/
theorem both_ambient_pairs_zero (a b c d : ℝ)
    (plus_re : a + d = 0) (plus_im : b - c = 0)
    (minus_re : a - d = 0) (minus_im : b + c = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 := by
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

/-- Integer character arithmetic; multiplicity derivation is in the exact
probe and written representation proof, not imported as a physics count. -/
theorem block_dimension : 2 * (4 + 8 + 10 + 8 + 4 : Nat) = 68 := by decide
theorem quaternionic_dimension : 2 * (8 + 8 : Nat) = 32 := by decide
theorem sharp_kernel_dimension : 2 * (1 + 3 + 4 + 3 + 1 : Nat) = 24 := by decide
theorem quaternionic_kernel_dimension : 2 * (3 + 3 : Nat) = 12 := by decide
theorem sharp_rank_nullity : (44 + 24 : Nat) = 68 := by decide
theorem quaternionic_rank_nullity : (20 + 12 : Nat) = 32 := by decide

end GUFormalization.NormalTensorClass
