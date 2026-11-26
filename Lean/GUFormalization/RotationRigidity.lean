import Mathlib

namespace GUFormalization.RotationRigidity

-- Arithmetic beneath subtraction of actual equations at two trace scales.
theorem central_scale_separation (a x c : ℝ) (ha : a ≠ 1)
    (h0 : x + c = 0) (h1 : a*x + c = 0) : x = 0 ∧ c = 0 := by
  have hx : (a-1)*x=0 := by nlinarith
  have hx0 : x=0 := (mul_eq_zero.mp hx).resolve_left (sub_ne_zero.mpr ha)
  exact ⟨hx0, by linarith⟩

-- Once all other coordinate contributions agree, the selected derivative vanishes.
theorem coordinate_scale_separation (a x rest : ℝ) (ha : a ≠ 1)
    (h0 : x + rest = 0) (h1 : a*x + rest = 0) : x = 0 :=
  (central_scale_separation a x rest ha h0 h1).1

theorem injective_symbol_and_seed {V W Z : Type*} [Zero V] [Zero W] [Zero Z]
    (J : V → W) (A : W → Z) (hJ : Function.Injective J)
    (hA : Function.Injective A) (J0 : J 0 = 0) (A0 : A 0 = 0)
    (v : V) (hv : A (J v) = 0) : v = 0 := by
  apply hJ
  rw [J0]
  apply hA
  simpa [A0] using hv

theorem all_base_derivatives_zero (d : Fin 4 → ℝ)
    (a : Fin 4 → ℝ) (rest : Fin 4 → ℝ)
    (ha : ∀ i, a i ≠ 1)
    (h0 : ∀ i, d i + rest i = 0)
    (h1 : ∀ i, a i*d i + rest i = 0) : d = 0 := by
  funext i
  exact coordinate_scale_separation (a i) (d i) (rest i) (ha i) (h0 i) (h1 i)

theorem rotation_transversality (t : ℝ) (ht : t ≠ 0) : 2*t ≠ 0 :=
  mul_ne_zero (by norm_num) ht

theorem raw_trace_dual_norm : (-(16:ℚ)) * (-1/4)^2 = -1 := by norm_num

theorem coordinate_trace_dual_norm : (1:ℚ)/(-16) = -1/16 := by norm_num

theorem boost_equalizes_two_rotation_scalars (a b : ℝ) (h : a-b=0) : a=b := by
  linarith

-- No null-vector shortcut survives anisotropic scaling of a nonzero component.
theorem anisotropic_null_unmasking (b x : ℝ) (hb : b^2 ≠ 1) (hx : x ≠ 0) :
    (b^2-1)*x^2 ≠ 0 := by
  exact mul_ne_zero (sub_ne_zero.mpr hb) (pow_ne_zero 2 hx)

end GUFormalization.RotationRigidity
