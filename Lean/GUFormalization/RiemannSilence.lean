import Mathlib

/-! Finite cores only. Native Clifford witnesses, completeness of the Riemann
restriction and source matching are separate exact/reviewed dependencies. -/
namespace GUFormalization.RiemannSilence

theorem cubic_kernel_pairing (x y : ℝ) (hy : y = 0)
    (hendpoint : x / 3 + y / 3 = x) : x = 0 := by
  rw [hy] at hendpoint
  linarith

theorem four_witness_elimination (a b c d : ℝ)
    (hlout : 264 * b = 0) (hlin : 22 * a + 264 * b = 0)
    (hhout : -312 * d = 0) (hhin : -24 * c - 312 * d = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 := by
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

theorem restriction_vanishes (a b c d r s : ℝ)
    (h : a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0) :
    (a * r + b * s, c * r + d * s) = (0, 0) := by
  rcases h with ⟨ha, hb, hc, hd⟩
  simp [ha, hb, hc, hd]

theorem zero_preserving_postcompose {X Y Z : Type*} [Zero Y] [Zero Z]
    (S : X → Y) (q : Y → Z) (hS : ∀ x, S x = 0) (hq : q 0 = 0) :
    ∀ x, q (S x) = 0 := by
  intro x
  rw [hS x, hq]

end GUFormalization.RiemannSilence
