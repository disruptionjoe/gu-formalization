import Mathlib

/-! Finite algebraic core for the receiver-strategy wave.
The analytic support, Lorentz-domain and native Clifford arguments remain
separately reviewed. These lemmas do not establish a physical GU state space.
-/
namespace GUFormalization.ReceiverStrategy

theorem boost_defect_identity (c k r : ℝ) :
    k - (1 + c * r) * (2 * c * k) = -k * (2 * c - 1 + 2 * c ^ 2 * r) := by
  ring

theorem first_owned_dispersion_fails_boost (k r : ℝ) (hk : k ≠ 0) (hr : 0 ≤ r) :
    k - (1 + r) * (2 * k) ≠ 0 := by
  have hp : 0 < 1 + 2 * r := by linarith
  have hid : k - (1 + r) * (2 * k) = -k * (1 + 2 * r) := by ring
  rw [hid]
  exact mul_ne_zero (neg_ne_zero.mpr hk) (ne_of_gt hp)

theorem second_owned_dispersion_fails_boost (k r : ℝ) (hk : k ≠ 0) (hr : 0 ≤ r) :
    k - (1 + 2 * r) * (4 * k) ≠ 0 := by
  have hp : 0 < 3 + 8 * r := by linarith
  have hid : k - (1 + 2 * r) * (4 * k) = -k * (3 + 8 * r) := by ring
  rw [hid]
  exact mul_ne_zero (neg_ne_zero.mpr hk) (ne_of_gt hp)

theorem adjoint_scalar_identity
    (a b c d x₁ x₂ y₁ y₂ u₁ u₂ f₁ f₂ : ℝ)
    (hx₁ : a*x₁+b*x₂=f₁) (hx₂ : c*x₁+d*x₂=f₂)
    (hy₁ : a*y₁+c*y₂=u₁) (hy₂ : b*y₁+d*y₂=u₂) :
    u₁*x₁+u₂*x₂=y₁*f₁+y₂*f₂ := by
  rw [← hx₁, ← hx₂, ← hy₁, ← hy₂]
  ring

theorem kernel_compatible_scalar
    (j₁ j₂ y₁ y₂ z₁ z₂ : ℝ) (h : j₁*z₁+j₂*z₂=0) :
    j₁*(y₁+z₁)+j₂*(y₂+z₂)=j₁*y₁+j₂*y₂ := by
  nlinarith

theorem massless_difference_can_be_nonzero_null :
    (2-1:ℝ)^2-(2-1:ℝ)^2=0 ∧ (2-1:ℝ)≠0 := by
  norm_num

end GUFormalization.ReceiverStrategy
