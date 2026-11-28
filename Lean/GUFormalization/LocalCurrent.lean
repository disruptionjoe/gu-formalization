import Mathlib

/-! Finite cores only. Native symbol, current-jet identity and spectral quotient
arguments are written proofs; no physical-domain statement is formalized. -/
namespace GUFormalization.LocalCurrent

theorem nonnegative_anti_isometry_zero {V : Type*} (q : V → ℝ) (E : V → V)
    (hq : ∀ v, 0 ≤ q v) (hE : ∀ v, q (E v) = -q v) : ∀ v, q v = 0 := by
  intro v
  have h1 := hq v
  have h2 := hq (E v)
  rw [hE] at h2
  linarith

theorem observation_not_retained {V O : Type*} (q : V → ℝ) (E : V → V)
    (obs : V → O) (zero : O) (v : V)
    (hq : ∀ u, 0 ≤ q u) (hE : ∀ u, q (E u) = -q u)
    (hretain : ∀ u, q u = 0 → obs u = zero)
    (hvisible : obs v ≠ zero) : False := by
  exact hvisible (hretain v (nonnegative_anti_isometry_zero q E hq hE v))

theorem normal_aggregate_flip (u0 uk S B : ℚ) :
    (S - uk) - (u0 + S - uk + (1 - 11/12) * B)
      + (u0 - (11/12) * B) = -B := by ring

theorem coefficient_restore (u B : ℚ) :
    (u + B / 12) + (-B) / 12 = u := by ring

theorem restricted_density_positive (k l : ℝ) (hk : 0 < k)
    (hl : |l| < k) : 0 < 1 - |l / k| := by
  rw [abs_div, abs_of_pos hk]
  have h : |l| / k < 1 := (div_lt_one hk).2 hl
  linarith

end GUFormalization.LocalCurrent
