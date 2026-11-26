import Mathlib

namespace GUFormalization.PairedResponse

-- Coordinate arithmetic underlying subtraction of two affine CK jets.
theorem affine_jet_injective (a x y c : ℚ) (ha : a ≠ 0)
    (h : a * (x + c) = a * (y + c)) : x = y := by
  have hz : a * (x - y) = 0 := by nlinarith
  rcases mul_eq_zero.mp hz with h0 | h0
  · exact (ha h0).elim
  · linarith

theorem affine_four_jet_injective (a : ℚ) (x y c : Fin 4 → ℚ)
    (ha : a ≠ 0)
    (h : ∀ i, a * (x i + c i) = a * (y i + c i)) : x = y := by
  funext i
  exact affine_jet_injective a (x i) (y i) (c i) ha (h i)

theorem rational_boost_identity : (5 / 4 : ℚ)^2 - (3 / 4 : ℚ)^2 = 1 := by
  norm_num

theorem boost_polarization_multipliers :
    (5 / 4 + 3 / 4 : ℚ)^2 = 4 ∧ (5 / 4 - 3 / 4 : ℚ)^2 = 1 / 4 := by
  norm_num

-- u absorbs the common spinor-norm and Fourier-Jacobian factor.
theorem common_scalar_cannot_normalize_both (u : ℚ)
    (hp : 4 * u = 1) (hm : u / 4 = 1) : False := by
  linarith

-- Necessary scalar inequality if Gram normalization could erase Hermitian part.
theorem half_gram_cancellation_bound (h2 a k : ℝ)
    (h : h2 + (a-k)^2 ≤ k^2 / 4) : 4*h2 ≤ h2+a^2 := by
  nlinarith [sq_nonneg (3*k-4*a)]

-- Casimir projector denominator separating geometric spin5 from6 and7.
theorem spin5_projector_denominator : ((30:ℚ)-42)*(30-56)=312 := by
  norm_num

end GUFormalization.PairedResponse
