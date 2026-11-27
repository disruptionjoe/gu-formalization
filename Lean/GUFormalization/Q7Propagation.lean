import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
Algebraic core only. Native Clifford parity, actual equation projection,
source identification and the root-box energy intervals are independently
validated by the linked native probe and written proof. These are not encoded
as an assertion that the complete PDE or a GU prediction has been formalized.
-/
namespace GUFormalization.Q7Propagation

/-- Opposite diagonal signs force a Hermitian determinant to be negative,
regardless of the real and imaginary parts of its off-diagonal entry. -/
theorem hermitian_det_neg (a d u v : ℝ) (h : a * d < 0) :
    a * d - (u ^ 2 + v ^ 2) < 0 := by
  nlinarith [sq_nonneg u, sq_nonneg v]

/-- The two tested linear rows, not a single quadratic value, force zero. -/
theorem two_rows_injective {K : Type*} [Field K]
    (a b c d x y : K) (hdet : a * d - b * c ≠ 0)
    (h₁ : a * x + b * y = 0) (h₂ : c * x + d * y = 0) :
    x = 0 ∧ y = 0 := by
  have hx : (a * d - b * c) * x = 0 := by
    linear_combination d * h₁ - b * h₂
  have hy : (a * d - b * c) * y = 0 := by
    linear_combination a * h₂ - c * h₁
  exact ⟨(mul_eq_zero.mp hx).resolve_left hdet,
    (mul_eq_zero.mp hy).resolve_left hdet⟩

/-- Native reciprocity makes an auxiliary-kernel change invisible to a
source row already supplied with a preimage. No full inverse is assumed. -/
theorem source_row_kernel_independent {V K : Type*} [Zero V] [Zero K]
    (M : V → V) (pair : V → V → K)
    (reciprocal : ∀ u v, pair (M u) v = pair u (M v))
    (right_zero : ∀ u, pair u 0 = 0)
    (source preimage correction : V)
    (owned : M preimage = source) (kernel : M correction = 0) :
    pair source correction = 0 := by
  rw [← owned, reciprocal, kernel, right_zero]

/-- The relevant Hermitian complex determinant cannot vanish. -/
theorem complex_hermitian_det_ne_zero (a d : ℝ) (z : ℂ)
    (h : a * d < 0) :
    (a : ℂ) * (d : ℂ) - z * star z ≠ 0 := by
  intro hz
  have hr := congrArg Complex.re hz
  simp [Complex.mul_re] at hr
  have hn := hermitian_det_neg a d z.re z.im h
  nlinarith

/-- If actual tangency forces both tested Hermitian rows to vanish, the
highest-weight multiplicity vector must be zero. -/
theorem hermitian_rows_force_zero (a d : ℝ) (z x y : ℂ)
    (h : a * d < 0)
    (row₁ : (a : ℂ) * x + z * y = 0)
    (row₂ : star z * x + (d : ℂ) * y = 0) :
    x = 0 ∧ y = 0 :=
  two_rows_injective (a : ℂ) z (star z) (d : ℂ) x y
    (complex_hermitian_det_ne_zero a d z h) row₁ row₂

/-- A nonzero null quadratic value is compatible with an indefinite form;
this is why the proof uses both rows above. -/
theorem indefinite_has_null_vector :
    (1 : ℝ) ^ 2 - (1 : ℝ) ^ 2 = 0 ∧ (1 : ℝ) ≠ 0 := by
  norm_num

end GUFormalization.Q7Propagation
