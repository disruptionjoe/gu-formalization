import Mathlib

/-! Finite algebra used in the actual scalar-normal calculation. The geometric
frame, native matrices/root certificates, analytic ODE existence, boundary
flux estimate and physical interpretation are separate reviewed inputs. -/
namespace GUFormalization.ScalarNormalSchur

variable {V : Type*} [AddCommGroup V] [Module ℂ V]

/-- A moving-frame derivative cannot add to the auxiliary row when PA=0. -/
theorem moving_frame_auxiliary_row_zero
    (P A Sdot : V →ₗ[ℂ] V) (h : P.comp A = 0) (v : V) :
    P (A (Sdot v)) = 0 := by
  have hx := LinearMap.congr_fun h (Sdot v)
  simpa using hx

/-- The frequency term does not alter the auxiliary block if its compressed
symbol is zero. This asserts no analytic ODE theorem. -/
theorem auxiliary_frequency_independent
    (P K C : V →ₗ[ℂ] V) (n : V) (k : ℂ) (h : P (K n) = 0) :
    P (k • K n + C n) = P (C n) := by
  simp [h]

/-- A uniform linear error cannot overturn a strictly positive quadratic
leading coefficient at a sufficiently large positive frequency. -/
theorem positive_quadratic_dominates
    (a δ B k err : ℝ) (ha : δ ≤ a) (_hδ : 0 < δ)
    (hB : 0 ≤ B) (hk : 1 ≤ k) (hlarge : 2 * B < δ * k)
    (he : |err| ≤ B * k + B) :
    0 < a * k ^ 2 + err := by
  have hkpos : 0 < k := by linarith
  have hb : B ≤ B * k := by nlinarith
  have hprod : 0 < (δ * k - 2 * B) * k :=
    mul_pos (by linarith) hkpos
  have helo := (abs_le.mp he).1
  have hleading : 0 ≤ (a - δ) * k ^ 2 :=
    mul_nonneg (by linarith) (sq_nonneg k)
  nlinarith

/-- The same statement for a negative quadratic coefficient. -/
theorem negative_quadratic_dominates
    (a δ B k err : ℝ) (ha : a ≤ -δ) (hδ : 0 < δ)
    (hB : 0 ≤ B) (hk : 1 ≤ k) (hlarge : 2 * B < δ * k)
    (he : |err| ≤ B * k + B) :
    a * k ^ 2 + err < 0 := by
  have hp := positive_quadratic_dominates (-a) δ B k (-err)
    (by linarith) hδ hB hk hlarge (by simpa using he)
  linarith

/-- Native inverse-metric arithmetic for du=theta3-u(theta4-3theta7).
The geometric identification of this covector is an external premise. -/
theorem normalized_time_covector_norm (u : ℝ) :
    -1 + u ^ 2 * (-(1 / 16 : ℝ) + 9 / 48) = -1 + u ^ 2 / 8 := by
  ring

/-- A negative complexified energy sum has a negative real component. -/
theorem negative_sum_has_negative_component (x y : ℝ) (h : x + y < 0) :
    x < 0 ∨ y < 0 := by
  by_contra hn
  push Not at hn
  linarith

end GUFormalization.ScalarNormalSchur
