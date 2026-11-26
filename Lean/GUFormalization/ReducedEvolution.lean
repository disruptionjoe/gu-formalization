import Mathlib

/-! Finite algebraic core of the reduced-evolution domain test.
The native symbol, exact endpoint coefficients, functional domain and localized
wavepacket estimates are supplied by the separately reviewed written argument.
No physical quotient or nonlinear evolution theorem is formalized here. -/
namespace GUFormalization.ReducedEvolution

/-- The differentiated constant-rank symbol identity forces the quadratic
Schur symbol to square to zero, independently of the inverse constraint factor. -/
theorem sandwich_square_zero {R : Type*} [Ring R]
    (g k p m : R) (h : p * k * g * k * p = 0) :
    (g * k * p * m * p * k) * (g * k * p * m * p * k) = 0 := by
  calc
    _ = (g * k * p * m) * (p * k * g * k * p) * (m * p * k) := by
      noncomm_ring
    _ = 0 := by rw [h]; simp

/-- A nonzero scalar slope gives an unbounded affine ray. -/
theorem positive_slope_unbounded (a b bound : ℝ) (hb : 0 < b) :
    ∃ t : ℝ, 0 ≤ t ∧ bound < a + t * b := by
  refine ⟨(|bound - a| + 1) / b, le_of_lt (div_pos (by positivity) hb), ?_⟩
  rw [div_mul_cancel₀ _ (ne_of_gt hb)]
  have h := le_abs_self (bound - a)
  linarith

/-- Uniformly bounded affine-ray coordinates must have zero slope.
This checks the contradiction used after the rescaled-time packet limit. -/
theorem bounded_affine_ray_forces_zero (a b bound : ℝ)
    (h : ∀ t : ℝ, 0 ≤ t → |a + t * b| ≤ bound) : b = 0 := by
  by_contra hb
  rcases lt_or_gt_of_ne hb with hn | hp
  · obtain ⟨t, ht, hg⟩ := positive_slope_unbounded (-a) (-b) bound (neg_pos.mpr hn)
    have hu := h t ht
    have hl := neg_le_abs (a + t * b)
    nlinarith
  · obtain ⟨t, ht, hg⟩ := positive_slope_unbounded a b bound hp
    have hu := h t ht
    have hl := le_abs_self (a + t * b)
    linarith

/-- Universal independent value/derivative jets cannot hide a nonzero
first-derivative readout coefficient. The smooth-jet realization is external. -/
theorem universal_zero_jets_force_symbol_zero (lower symbol : ℝ)
    (h : ∀ value derivative : ℝ, value * lower + derivative * symbol = 0) :
    symbol = 0 := by
  simpa using h 0 1

end GUFormalization.ReducedEvolution
