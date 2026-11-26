import Mathlib

/-! Finite cores only. Native representation, differential-operator identities,
functional domains and boundary geometry are established separately. -/
namespace GUFormalization.SteelmanDatum

/-- Highest-time-order coefficient descent. The external differential-operator
argument supplies the finite recurrence and its terminal zero. -/
theorem finite_coefficient_chain_zero {V : Type*} [Zero V]
    (F : V → V) (hF : F 0 = 0) (q : ℕ → V) :
    ∀ n : ℕ, q n = 0 → (∀ k < n, q k = F (q (k + 1))) →
      ∀ k ≤ n, q k = 0 := by
  intro n
  induction n with
  | zero =>
    intro hn hr k hk
    have h : k = 0 := Nat.eq_zero_of_le_zero hk
    simpa [h] using hn
  | succ n ih =>
    intro hn hr k hk
    have hn0 : q n = 0 := by
      rw [hr n (Nat.lt_succ_self n), hn, hF]
    have hlow : ∀ j ≤ n, q j = 0 :=
      ih hn0 (fun j hj => hr j (Nat.lt_trans hj (Nat.lt_succ_self n)))
    by_cases h : k = n + 1
    · simpa [h] using hn
    · exact hlow k (Nat.le_of_lt_succ (lt_of_le_of_ne hk h))

/-- An exact negative interval certifies nonzero curvature. -/
theorem negative_interval_excludes_flat (x c r : ℝ)
    (he : |x - c| ≤ r) (hn : c + r < 0) : x ≠ 0 := by
  have hu := le_abs_self (x - c)
  have hx : x < 0 := by linarith
  exact ne_of_lt hx

/-- Equivalent positive norms would bound the original squared norm. -/
theorem equivalent_metric_bound (m M x y energy : ℝ) (hm : 0 < m)
    (hlo : m * x ≤ energy) (hhi : energy ≤ M * y) :
    x ≤ (M * y) / m := by
  apply (le_div_iff₀ hm).2
  nlinarith

/-- A boundary term vanishing on an interior test cannot change its sign. -/
theorem vanishing_boundary_term_preserves_negative (energy boundary : ℝ)
    (he : energy < 0) (hb : boundary = 0) : energy + boundary < 0 := by
  simpa [hb] using he

end GUFormalization.SteelmanDatum
