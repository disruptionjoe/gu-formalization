import Mathlib

namespace GUFormalization.EvolutionComplement

/-- Differentiating a fixed algebraic graph constraint gives this necessary equation.
The derivative premise and matrix construction are established in the written proof. -/
theorem first_prolongation {R : Type*} [Ring R] (T V B X : R)
    (h : (T * V - B) * X = 0) : T * (V * X) = B * X := by
  rw [sub_mul, mul_assoc] at h
  exact sub_eq_zero.mp h

/-- A factorization must annihilate every vector annihilated by its input map. -/
theorem factorization_kernel {K E F G : Type*} [Field K]
    [AddCommGroup E] [Module K E] [AddCommGroup F] [Module K F]
    [AddCommGroup G] [Module K G]
    (X : E →ₗ[K] F) (Y : E →ₗ[K] G) (T : F →ₗ[K] G)
    (h : T.comp X = Y) (v : E) (hx : X v = 0) : Y v = 0 := by
  rw [← h]
  simp [hx]

/-- The native minor contradicts the dimension bound if both rank facts hold.
Lean does not compute that minor or formalize the geometric transfer. -/
theorem minor_exceeds_factorization (r : ℕ) (upper : r ≤ 192)
    (lower : 193 ≤ r) : False := by omega

theorem principal_hom_dimension : 9 * (2 + 3 + 1) * 2048 = (110592 : ℕ) := by
  norm_num

end GUFormalization.EvolutionComplement
