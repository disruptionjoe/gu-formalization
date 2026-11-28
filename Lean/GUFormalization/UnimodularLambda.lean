import Mathlib

/-! Finite arithmetic cores only. The report supplies the geometric and PDE proof. -/
namespace GUFormalization.UnimodularLambda

theorem background_unique (A c L₁ L₂ : ℝ) (hA : A ≠ 0)
    (h₁ : A * L₁ + c / 2 = 0) (h₂ : A * L₂ + c / 2 = 0) : L₁ = L₂ := by
  have h : A * (L₁ - L₂) = 0 := by nlinarith
  have := (mul_eq_zero.mp h).resolve_left hA
  linarith

theorem negative_scalar_mass (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    -a / (6 * b) < 0 := by exact div_neg_of_neg_of_pos (neg_neg_of_pos ha) (by positivity)

theorem F_factor (b H r : ℝ) :
    24 * b * H ^ 2 - 6 * b * r * (r + 3 * H) =
      6 * b * (H - r) * (r + 4 * H) := by ring

theorem curvature_factor (H r : ℝ) :
    3 * (r + 3 * H) * (r + 4 * H) = 3 * r ^ 2 + 21 * H * r + 36 * H ^ 2 := by ring

theorem critical_normalization (H : ℝ) :
    3 * (H + 3 * H) * (H + 4 * H) = 60 * H ^ 2 := by ring

theorem positive_F_growth_bound (H r : ℝ) (hH : 0 < H) (hr : 0 < r)
    (hF : 0 < (H - r) * (r + 4 * H)) : r < H := by
  have hp : 0 < r + 4 * H := by linarith
  have := (mul_pos_iff_of_pos_right hp).mp hF
  linarith

theorem vacuum_shift_label (c ell delta : ℝ) :
    (c + delta) + 2 * (ell - delta / 2) = c + 2 * ell := by ring

end GUFormalization.UnimodularLambda
