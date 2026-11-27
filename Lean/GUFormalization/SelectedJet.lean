import Mathlib

/-! Finite algebraic cores for the matched selected-current jet.
The native CK formula, Clifford identification, Lorentzian band argument,
root enclosures and normalized physical current are separately reviewed.
Raw current separation does not prove normalized Hermitian visibility. -/
namespace GUFormalization.SelectedJet

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- A non-null Clifford difference cannot right-annihilate a nonzero matrix. -/
theorem clifford_right_cancellation
    (A C : Matrix n n ℂ) (q : ℂ) (hq : q ≠ 0)
    (hsq : C * C = q • (1 : Matrix n n ℂ))
    (hz : A * C = 0) : A = 0 := by
  have h : q • A = 0 := by
    calc
      q • A = A * (q • (1 : Matrix n n ℂ)) := by simp
      _ = A * (C * C) := by rw [hsq]
      _ = (A * C) * C := by rw [Matrix.mul_assoc]
      _ = 0 := by rw [hz, zero_mul]
  exact (smul_eq_zero.mp h).resolve_left hq

/-- Two vanishing affine outputs with a non-null Clifford separation force
their common coefficient to vanish; no freely chosen zero frequency is used. -/
theorem two_frequency_affine_separation
    (A B C D : Matrix n n ℂ) (q : ℂ) (hq : q ≠ 0)
    (hsq : (C - D) * (C - D) = q • (1 : Matrix n n ℂ))
    (hc : B + A * C = 0) (hd : B + A * D = 0) : A = 0 := by
  have heq : A * C = A * D := add_left_cancel (hc.trans hd.symm)
  apply clifford_right_cancellation A (C - D) q hq hsq
  rw [Matrix.mul_sub, heq, sub_self]

omit [DecidableEq n] in
/-- Any proposed lower-order constant changes neither the difference nor its
separation criterion. This includes the required moving-graph correction. -/
theorem affine_difference
    (A B C D : Matrix n n ℂ) :
    (B + A * C) - (B + A * D) = A * (C - D) := by
  rw [Matrix.mul_sub]
  abel

/-- Raw nonvanishing alone does not imply a nonzero Hermitian part.
This scalar control is not a statement about the native candidate. -/
theorem raw_nonzero_can_be_skew :
    (Complex.I ≠ 0) ∧ Complex.I + star Complex.I = 0 := by
  simp

/-- Scalar core of the uniform Gram-perturbation threshold. The operator
and integrated-norm inequalities identifying m and M are separate inputs. -/
theorem gram_perturbation_threshold (m M e : ℝ)
    (hm : 0 < m) (hM : 0 ≤ M) (he : 0 ≤ e)
    (hsmall : e < m / (m + M)) :
    e < 1 ∧ e / (1 - e) * M < m := by
  have hd : 0 < m + M := by linarith
  have hb : e * (m + M) < m := (lt_div_iff₀ hd).mp hsmall
  have heM : 0 ≤ e * M := mul_nonneg he hM
  have he1 : e < 1 := by nlinarith
  refine ⟨he1, ?_⟩
  rw [div_mul_eq_mul_div]
  apply (div_lt_iff₀ (show 0 < 1 - e by linarith)).mpr
  nlinarith

end GUFormalization.SelectedJet
