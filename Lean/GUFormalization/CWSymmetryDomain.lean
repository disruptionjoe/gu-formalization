import Mathlib

namespace GUFormalization.CWSymmetryDomain

/-- Domain closure under reversal turns a future property into a past property.
The analytic meaning of P and reversal is a premise, not encoded here. -/
theorem reversal_closure {α : Type*} (D P : α → Prop) (R : α → α)
    (closed : ∀ x, D x → D (R x)) (future : ∀ x, D x → P x) :
    ∀ x, D x → P x ∧ P (R x) := by
  intro x hx
  exact ⟨future x hx, future (R x) (closed x hx)⟩

/-- The smallest shell shift bounds all declared mass squares. -/
theorem mass_positive (N c shift : ℝ) (hN : c < N) (hs : -c ≤ shift) :
    0 < N + shift := by linarith

/-- A normal margin is a new domain premise, not a derived physical gap. -/
theorem mass_margin (N c shift eps : ℝ)
    (hN : c + eps ≤ N) (hs : -c ≤ shift) : eps ≤ N + shift := by linarith

/-- Bounded remainder cannot cancel the prescribed inverse-root leading term. -/
theorem residue_lower_bound (z J lam C : ℝ)
    (h : J / (2 * lam) - C ≤ z) (hc : C ≤ J / (4 * lam)) :
    J / (4 * lam) ≤ z := by
  have heq : J / (2 * lam) = 2 * (J / (4 * lam)) := by ring
  linarith

/-- Exact inputs in the Lorentz core and the two nonzero actual receiver values. -/
theorem core_witness_arithmetic :
    ((28 : ℚ) / 3)^2 - 3^2 = 703 / 9 ∧
    (703 : ℚ) / 9 > 36 ∧
    ((86 : ℚ) / 13)^2 > 36 ∧
    -(83 / 13 : ℚ)^2 + (86 / 13 : ℚ)^2 = 3 ∧
    (104448 : ℚ) ≠ 0 ∧ (69696 : ℚ) / 12 = 5808 := by norm_num

end GUFormalization.CWSymmetryDomain
