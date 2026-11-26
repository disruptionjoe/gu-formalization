import Mathlib

/-!
Finite algebra and norm core for predictive-realization checks.

These statements do not formalize the Clifford commutant classification,
actual contour coefficient assembly, interval arithmetic, pseudodifferential
symbol descent, Sobolev estimates, or source relevance. Those remain separately
proved/reviewed hypotheses. No physical reality or positive energy is inferred.
-/

namespace GUFormalization.PredictiveRealization

section Minor
variable {K : Type*} [Field K]
variable {m n : Type*} [Fintype m] [Fintype n] [DecidableEq n]

/-- An actual finite left inverse makes the selected minor detect every
coefficient vector, over either the real or complex field. -/
theorem minor_kernel_zero
    (M : Matrix m n K) (R : Matrix n m K)
    (hleft : R * M = 1) (x : n → K) (hx : M.mulVec x = 0) : x = 0 := by
  have hrecover : R.mulVec (M.mulVec x) = x := by
    rw [Matrix.mulVec_mulVec, hleft, Matrix.one_mulVec]
  calc
    x = R.mulVec (M.mulVec x) := hrecover.symm
    _ = 0 := by rw [hx, Matrix.mulVec_zero]

end Minor

section NormCertificate
variable {E F : Type*}
variable [NormedAddCommGroup E] [NormedSpace ℝ E]
variable [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- Elementary strict-contraction inequality behind a residual certificate. -/
theorem norm_le_strict_multiple_zero
    (x : E) (c : ℝ) (hc : c < 1) (hx : ‖x‖ ≤ c * ‖x‖) : x = 0 := by
  by_contra hne
  have hpos : 0 < ‖x‖ := norm_pos_iff.mpr hne
  nlinarith

/-- A certified approximate left inverse with residual bound below one
proves injectivity. Finite-dimensionality is not needed for this implication. -/
theorem residual_left_inverse_injective
    (L : E →ₗ[ℝ] F) (R : F →ₗ[ℝ] E) (c : ℝ) (hc : c < 1)
    (hres : ∀ x : E, ‖x - R (L x)‖ ≤ c * ‖x‖) :
    Function.Injective L := by
  intro x y hxy
  have hz : L (x - y) = 0 := by simp only [map_sub, hxy, sub_self]
  have hR : R (L (x - y)) = 0 := by rw [hz, map_zero]
  have hbound := hres (x - y)
  rw [hR, sub_zero] at hbound
  exact sub_eq_zero.mp (norm_le_strict_multiple_zero (x - y) c hc hbound)

end NormCertificate

section Projectors
variable {n : Type*} [Fintype n] [DecidableEq n]

noncomputable def positiveProjector (S : Matrix n n ℂ) : Matrix n n ℂ :=
  (1 / 2 : ℂ) • (1 + S)

noncomputable def negativeProjector (S : Matrix n n ℂ) : Matrix n n ℂ :=
  (1 / 2 : ℂ) • (1 - S)

/-- Involution spectral projectors sum to the identity. -/
theorem projectors_sum (S : Matrix n n ℂ) :
    positiveProjector S + negativeProjector S = 1 := by
  ext i j
  simp only [positiveProjector, negativeProjector, Matrix.add_apply,
    Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- The positive spectral projector is idempotent. -/
theorem positive_idempotent (S : Matrix n n ℂ) (hS : S * S = 1) :
    positiveProjector S * positiveProjector S = positiveProjector S := by
  unfold positiveProjector
  simp only [Matrix.smul_mul, Matrix.mul_smul,
    Matrix.add_mul, Matrix.mul_add, Matrix.one_mul, Matrix.mul_one, hS]
  ext i j
  simp only [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- The negative spectral projector is idempotent. -/
theorem negative_idempotent (S : Matrix n n ℂ) (hS : S * S = 1) :
    negativeProjector S * negativeProjector S = negativeProjector S := by
  unfold negativeProjector
  simp only [Matrix.smul_mul, Matrix.mul_smul,
    Matrix.sub_mul, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one, hS]
  ext i j
  simp only [Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- Opposite involution projectors annihilate each other. -/
theorem projectors_disjoint (S : Matrix n n ℂ) (hS : S * S = 1) :
    positiveProjector S * negativeProjector S = 0 := by
  unfold positiveProjector negativeProjector
  simp only [Matrix.smul_mul, Matrix.mul_smul,
    Matrix.add_mul, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one, hS]
  ext i j
  simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply,
    Matrix.zero_apply, smul_eq_mul]
  ring

/-- The positive spectral subspace has eigenvalue +1. -/
theorem positive_eigen (S : Matrix n n ℂ) (hS : S * S = 1) :
    S * positiveProjector S = positiveProjector S := by
  unfold positiveProjector
  simp only [Matrix.mul_smul, Matrix.mul_add, Matrix.mul_one, hS]
  ext i j
  simp only [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- The negative spectral subspace has eigenvalue -1. -/
theorem negative_eigen (S : Matrix n n ℂ) (hS : S * S = 1) :
    S * negativeProjector S = -negativeProjector S := by
  unfold negativeProjector
  simp only [Matrix.mul_smul, Matrix.mul_sub, Matrix.mul_one, hS]
  ext i j
  simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.neg_apply, smul_eq_mul]
  ring

end Projectors
end GUFormalization.PredictiveRealization
