import Mathlib

/-! Finite inference boundaries for X-P1-P2. No class-C action or geometry is formalized. -/
namespace GUFormalization.WeldCoefficientScope

theorem phase_eq_of_reachable {V M : Type*} (R : V → V → Prop) (p : V → M)
    (hedge : ∀ a b, R a b → p a = p b) {a b : V}
    (hab : Relation.ReflTransGen R a b) : p a = p b := by
  induction hab with
  | refl => rfl
  | tail hab hbc ih => exact ih.trans (hedge _ _ hbc)

theorem phase_constant_if_connected {V M : Type*} (R : V → V → Prop) (p : V → M)
    (hedge : ∀ a b, R a b → p a = p b)
    (hconn : ∀ a b, Relation.ReflTransGen R a b) : ∀ a b, p a = p b := by
  intro a b
  exact phase_eq_of_reachable R p hedge (hconn a b)

theorem incompatible_two_cycle {a b : ℂ} (h1 : 2*b = a) (h2 : 2*a = b) :
    a = 0 ∧ b = 0 := by
  have ha : 3*a = 0 := by linear_combination h1 + 2*h2
  have hzero : a = 0 := (mul_eq_zero.mp ha).resolve_left (by norm_num)
  constructor
  · exact hzero
  · rw [hzero] at h2
    simpa using h2.symm

theorem no_nonzero_phase_on_two_cycle {a b : ℂ} (ha : a ≠ 0) :
    ¬ (2*b = a ∧ 2*a = b) := by
  rintro ⟨h1,h2⟩
  exact ha (incompatible_two_cycle h1 h2).1

end GUFormalization.WeldCoefficientScope
