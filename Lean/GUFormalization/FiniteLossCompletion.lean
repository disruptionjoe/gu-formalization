import Mathlib

/-! Arithmetic and limiting core of the finite-loss packet argument. Smooth
classical symbols, the uniform remainder, maximal-spectrum transport and
physical/source identifications are separately reviewed hypotheses. -/
namespace GUFormalization.FiniteLossCompletion

open Filter
open scoped Topology

/-- Matching the transport coefficients through N raises the formal residual
order past N, including for noncommutative matrix coefficient rings. This
does not assert convergence of a formal series or an analytic remainder. -/
theorem transport_residual_order {R : Type*} [Ring R] (N : ℕ)
    (A W Wt : PowerSeries R)
    (h : ∀ j ≤ N, PowerSeries.coeff j Wt = PowerSeries.coeff j (A * W)) :
    (↑(N + 1) : ℕ∞) ≤ (Wt - A * W).order := by
  apply PowerSeries.nat_le_order
  intro j hj
  rw [map_sub, h j (by omega), sub_self]

/-- Any natural upper bound on the proposed loss gives strict negative
initial and residual exponents for the chosen correction schedule. -/
theorem schedule_exponents (ell : ℝ) (q : ℕ) (h : ell ≤ (q : ℝ)) :
    ell - ((q : ℝ) + 1) ≤ -1 ∧
      ell - ((2 * (q : ℝ) + 2) + 1) / 2 ≤ -(3 / 2 : ℝ) := by
  constructor <;> linarith

/-- Polynomial logarithmic factors cannot defeat a strict inverse power.
This is a real limit theorem, not a sampled-frequency check. -/
theorem log_power_over_power_tends_zero (m : ℕ) (delta : ℝ)
    (hd : 0 < delta) :
    Tendsto (fun x : ℝ => (Real.log x) ^ m / x ^ delta) atTop (𝓝 0) := by
  simpa using (isLittleO_log_rpow_rpow_atTop (m : ℝ) hd).tendsto_div_nhds_zero

/-- The logarithmic packet observation time stays local. -/
theorem logarithmic_time_tends_zero (c : ℝ) :
    Tendsto (fun x : ℝ => c * Real.log x / x) atTop (𝓝 0) := by
  have h := (log_power_over_power_tends_zero 1 1 (by norm_num)).const_mul c
  simpa [mul_div_assoc] using h

/-- A fixed estimate cannot bound a normalized unit output by two errors
which both vanish. Native packet estimates must supply these limits. -/
theorem vanishing_rhs_contradiction (a b : ℝ → ℝ) (C : ℝ)
    (ha : Tendsto a atTop (𝓝 0)) (hb : Tendsto b atTop (𝓝 0))
    (he : ∀ k, 1 ≤ C * (a k + b k)) : False := by
  have hl : Tendsto (fun k => C * (a k + b k)) atTop (𝓝 0) := by
    simpa using (ha.add hb).const_mul C
  have h : (1 : ℝ) ≤ 0 := ge_of_tendsto hl (Eventually.of_forall he)
  norm_num at h

/-- Two continuous Sobolev embeddings plus a bounded Y estimate produce
the forbidden finite-loss bound. The actual embeddings are external inputs. -/
theorem sandwich_transfers_bound
    (out yout yin yr hs_initial hs_residual c1 c2 m : ℝ)
    (hc1 : 0 ≤ c1) (_hc2 : 0 ≤ c2) (hm : 0 ≤ m)
    (hlo : out ≤ c1 * yout)
    (he : yout ≤ m * (yin + yr))
    (hi : yin ≤ c2 * hs_initial) (hr : yr ≤ c2 * hs_residual) :
    out ≤ c1 * m * c2 * (hs_initial + hs_residual) := by
  calc
    out ≤ c1 * (m * (yin + yr)) := hlo.trans (mul_le_mul_of_nonneg_left he hc1)
    _ ≤ c1 * (m * (c2 * hs_initial + c2 * hs_residual)) := by
      gcongr
    _ = c1 * m * c2 * (hs_initial + hs_residual) := by ring

end GUFormalization.FiniteLossCompletion
