import Mathlib

namespace GUFormalization.CWGlobalNorm

/-- Exact fixed-invariant boost. Native operator binding is checked separately. -/
theorem boost_square (R : ℝ) (hR : R ≠ 0) :
    (R + 16/R)^2 - (R - 16/R)^2 = 64 := by
  field_simp
  <;> ring

/-- Coefficient ratio after clearing its positive denominator. -/
theorem ratio_identity (R : ℝ) (hR : R ≠ 0) :
    (R^2/50 + 9/25 + 128/(25*R^2))*R^2 =
      R^4/50 + 9*R^2/25 + 128/25 := by
  field_simp
  <;> ring

/-- This lower bound supplies the growth core; packet localization is not encoded. -/
theorem ratio_lower (R : ℝ) :
    R^2/50 ≤ R^2/50 + 9/25 + 128/(25*R^2) := by
  have h : 0 ≤ (128 : ℝ)/(25*R^2) := by positivity
  linarith

/-- Square-root variables cancel the apparent two-decay kernel corner. -/
theorem kernel_numerator (x y : ℝ) : 4*x*y ≤ (x+y)^2 := by
  nlinarith [sq_nonneg (x-y)]

/-- Companion-system decay relation; descriptor embedding remains a premise. -/
theorem decay_relation (mu delta q : ℝ) (h : delta = mu^2) :
    delta*q = -mu*(-mu*q) := by rw [h]; ring

/-- Degree counts and held mass-shell arithmetic, not a scalarizer formalization. -/
theorem arithmetic :
    2 + 2*19 - 1 = (39 : ℕ) ∧
    (64 : ℚ) > 36 ∧ (10 : ℚ)^2 = 64 + 36 ∧
    (36 : ℚ)/4 = 9 := by norm_num

end GUFormalization.CWGlobalNorm
