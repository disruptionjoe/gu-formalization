import Mathlib

/-! Finite logical/arithmetic cores only. The report owns the analytic bridges. -/
namespace GUFormalization.ObserverHorizon

theorem pointed_opposite {V : Type*} [AddGroup V] (C : Set V)
    (hp : ∀ v, v ∈ C → -v ∈ C → v = 0) (v : V)
    (hv : v ∈ C) (hn : -v ∈ C) (hne : v ≠ 0) : False :=
  hne (hp v hv hn)

theorem quotient_obstruction {X A B : Type*} (q : X → A) (r : X → B)
    (x y : X) (hq : q x = q y) (hr : r x ≠ r y) :
    ¬ ∃ f : A → B, ∀ z, f (q z) = r z := by
  rintro ⟨f, hf⟩
  apply hr
  rw [← hf x, ← hf y, hq]

theorem hook_receiver_nonzero : (2 : ℝ) ≠ 0 := by norm_num

theorem arbitrary_jet_receiver_nonzero (n : ℕ) :
    (2 : ℝ) * (Nat.factorial (n + 1) : ℝ) ≠ 0 := by
  positivity

theorem weight_gap (x : ℝ) (hx : 1 < x) : x < x ^ 2 := by nlinarith

theorem trace_mean_square : (-4 : ℝ) * (1 / 2) ^ 2 = -1 := by norm_num

theorem profile_second_variation_selectable (a : ℝ) :
    2 * (a / 2) = a := by ring

end GUFormalization.ObserverHorizon
