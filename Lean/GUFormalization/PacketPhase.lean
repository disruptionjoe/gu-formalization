import Mathlib

/-! Finite arithmetic and inverse-cost cores only. The native CK uniformity,
classical graph calculus, compact-support integration by parts and packet
normal-jet identification are separately reviewed written mathematics. -/
namespace GUFormalization.PacketPhase

/-- Leave two powers after the chosen logarithmic growth and normalization
cost. One may absorb any fixed logarithmic power into part of this margin. -/
theorem derivative_budget (q L c rho A d : ℝ)
    (hq : L + 2*c*rho + A + 2 - d/2 ≤ q) :
    L + 2 ≤ (q+2) + d/2 - 2 - 2*c*rho - A := by
  linarith

/-- A polynomial-size source paired with a rapidly small coefficient requires
the corresponding growing charge. N=m+r is an arbitrary stronger bound. -/
theorem charge_cost (F Q C c k : ℝ) (m r : ℕ)
    (hk : 0 ≤ k) (hC : 0 < C)
    (upper : F * k^(m+r) ≤ C*Q)
    (lower : c ≤ F * k^m) :
    (c * k^r) / C ≤ Q := by
  apply (div_le_iff₀ hC).mpr
  have h := mul_le_mul_of_nonneg_right lower (pow_nonneg hk r)
  rw [mul_assoc, ← pow_add] at h
  nlinarith

/-- Even one extra inverse power contradicts a uniform fixed-power lower
bound at all sufficiently large frequencies. This is not exact vanishing. -/
theorem no_uniform_power_lower
    (f : ℝ → ℝ) (C c : ℝ) (m : ℕ) (hc : 0 < c)
    (upper : ∀ k : ℝ, 1 ≤ k → f k * k^(m+1) ≤ C)
    (lower : ∀ k : ℝ, 1 ≤ k → c ≤ f k * k^m) : False := by
  let k : ℝ := max 1 (C/c+1)
  have hk : 1 ≤ k := le_max_left _ _
  have hkc : C/c < k := by
    have h := le_max_right (1 : ℝ) (C/c+1)
    dsimp [k]
    linarith
  have hlarge : C < k*c := (div_lt_iff₀ hc).mp hkc
  have h := mul_le_mul_of_nonneg_right (lower k hk) (show 0 ≤ k by linarith)
  have hp : (f k * k^m) * k = f k * k^(m+1) := by
    rw [pow_succ, mul_assoc]
  rw [hp] at h
  linarith [upper k hk]

/-- A nonzero complex packet output has a nonzero real quadrature. -/
theorem visible_real_quadrature (z : ℂ) (hz : z ≠ 0) :
    z.re ≠ 0 ∨ z.im ≠ 0 := by
  by_contra h
  push Not at h
  apply hz
  apply Complex.ext <;> simp [h.1, h.2]

end GUFormalization.PacketPhase
