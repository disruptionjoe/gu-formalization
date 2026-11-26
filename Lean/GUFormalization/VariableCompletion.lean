import Mathlib

/-!
Finite algebra for the actual stationary variable-coefficient completion.
This file does not formalize parameter-dependent CK, Parseval, actual native
coefficient analyticity, global boundary conditions or source selection.
The matrix lemma checks LEFT normalization of a possibly non-Hermitian Gram.
The scalar lemmas fix the +i row-contour and -i U(1) generator convention.
-/

namespace GUFormalization.VariableCompletion

open ComplexConjugate

section Gram
variable {m n : Type*} [Fintype m] [Fintype n] [DecidableEq n]

/-- Normalizing the rows on the left recovers the identity pairing without
assuming that the original Gram matrix is Hermitian. -/
theorem left_gram_normalization
    (V : Matrix n m ℂ) (A : Matrix m m ℂ) (U : Matrix m n ℂ)
    (G R : Matrix n n ℂ)
    (hG : V * A * U = G) (hR : R * G = 1) :
    (R * V) * A * U = 1 := by
  calc
    (R * V) * A * U = R * (V * A * U) := by
      simp only [Matrix.mul_assoc]
    _ = R * G := by rw [hG]
    _ = 1 := hR

end Gram

/-- With row phase +i and U(1) generator -i, the actual action current
has positive amplitude charge. -/
theorem phase_charge (r : ℝ) :
    ((-Complex.I) * (Complex.I * (r : ℂ))).re = r := by
  simp [Complex.mul_re, Complex.mul_im]

/-- With time dependence exp(-i w t), the +i contour gives +w times
the amplitude norm in the canonical on-shell time-translation charge. -/
theorem phase_energy (w r : ℝ) :
    ((Complex.I * (-Complex.I * (w : ℂ))) * (r : ℂ)).re = w * r := by
  simp [Complex.mul_re, Complex.mul_im]

/-- The opposite contour phase flips canonical energy; charge positivity
under an oppositely oriented phase generator would not remove this sign. -/
theorem opposite_phase_energy (w r : ℝ) :
    (((-Complex.I) * (-Complex.I * (w : ℂ))) * (r : ℂ)).re = -(w * r) := by
  simp [Complex.mul_re, Complex.mul_im]

/-- The real action presymplectic form restricted to the +i graph is
minus twice the imaginary Hermitian pairing. -/
theorem restricted_symplectic (z : ℂ) :
    (Complex.I * z - Complex.I * conj z).re = -2 * z.im := by
  simp [Complex.mul_re, Complex.mul_im]
  <;> ring

/-- In the dTheta convention the compatible complex structure is -i. -/
theorem compatible_complex_structure (r : ℝ) :
    (-2 : ℝ) * ((-Complex.I) * (r : ℂ)).im = 2 * r := by
  simp [Complex.mul_re, Complex.mul_im]
  <;> ring

/-- In the dTheta convention, contraction with X_t=-i omega a gives
minus dE. Here z denotes the weighted Hermitian pairing with a variation. -/
theorem time_symplectic_sign (z : ℂ) :
    (-2 : ℝ) * (Complex.I * z).im = -(2 * z.re) := by
  simp [Complex.mul_re, Complex.mul_im]
  <;> ring

theorem energy_nonnegative (w r : ℝ) (hw : 0 ≤ w) (hr : 0 ≤ r) :
    0 ≤ ((Complex.I * (-Complex.I * (w : ℂ))) * (r : ℂ)).re := by
  rw [phase_energy]
  exact mul_nonneg hw hr

end GUFormalization.VariableCompletion
