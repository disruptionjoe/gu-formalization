import Mathlib

/-! Finite algebra only; native symbol, curved CK and growth estimates are
separately reviewed written proofs. -/
namespace GUFormalization.PrintedDifferential

theorem trace_mode {V : Type*} [AddCommGroup V] [Module ℝ V]
    (L : V →ₗ[ℝ] V) (O W : V) (k q : ℝ)
    (hO : L O = (-2 : ℝ) • W) (hW : L W = (24*q) • O)
    (h : k^2+48*q=0) : L (k • O + (2:ℝ) • W) = (-k) • (k • O + (2:ℝ) • W) := by
  rw [map_add, map_smul, map_smul, hO, hW]
  have hq : 48*q = -k*k := by nlinarith [h]
  calc
    k • ((-2:ℝ) • W) + (2:ℝ) • ((24*q) • O) = (48*q) • O + (-2*k) • W := by module
    _ = (-k) • (k • O + (2:ℝ) • W) := by rw [hq]; module

theorem quadratic_quotient (k z : ℝ) :
    (k+z)*(k-z)=k^2-z^2 := by ring

theorem massive_trace_determinant (k q : ℝ) :
    k*k-(24*q)*(-2)=k^2+48*q := by ring

theorem perturbative_nonzero (a b : ℝ) (hb : |b| < a) : a+b ≠ 0 := by
  have h := (abs_lt.mp hb).1
  linarith

end GUFormalization.PrintedDifferential
