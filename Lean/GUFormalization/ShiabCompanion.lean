import Mathlib

/-! Two finite cores only. Exterior-symbol classification, Clifford/Riemann
identities, real forms and actual connection jets are written arguments. -/
namespace GUFormalization.ShiabCompanion

/-- A zero input with nonzero output excludes every zero-preserving
factorization, including nonlinear ones. -/
theorem no_zero_preserving_factorization {X Y Z : Type*} [Zero Y] [Zero Z]
    (incoming : X → Y) (outgoing : X → Z) (v : X)
    (hin : incoming v = 0) (hout : outgoing v ≠ 0) :
    ¬ ∃ companion : Y → Z,
      companion 0 = 0 ∧ ∀ x, outgoing x = companion (incoming x) := by
  rintro ⟨companion, hzero, hfactor⟩
  apply hout
  rw [hfactor v, hin, hzero]

/-- Polarizing a diagonal-zero bilinear form gives the skewness used in the
three-index tensor argument. Full alternation is not formalized here. -/
theorem diagonal_zero_implies_skew {V W : Type*}
    [AddCommGroup V] [Module ℂ V] [AddCommGroup W] [Module ℂ W]
    (B : V →ₗ[ℂ] V →ₗ[ℂ] W) (h : ∀ v, B v v = 0) (x y : V) :
    B x y = -(B y x) := by
  have hx := h x
  have hy := h y
  have hsum := h (x + y)
  simp only [map_add, LinearMap.add_apply] at hsum
  have hxy : B x y + B y x = 0 := by
    simpa only [hx, hy, zero_add, add_zero, add_comm] using hsum
  exact eq_neg_of_add_eq_zero_left hxy

end GUFormalization.ShiabCompanion
