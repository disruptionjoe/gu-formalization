import Mathlib

/-! Finite cores only. Native current, CK-domain, root-ball and energy
identifications are separate written/exact-computation obligations. -/
namespace GUFormalization.CurrentReceiver

/-- Pure antilinear conjugation reverses the real-action phase charge. -/
theorem conjugation_reverses_charge (z : ℂ) :
    (-Complex.I * star z).re = -(-Complex.I * z).re := by
  simp

/-- The additional time-reflection sign restores that charge. -/
theorem reflected_conjugation_preserves_charge (z : ℂ) :
    (-Complex.I * (-star z)).re = (-Complex.I * z).re := by
  simp

/-- A charge-reversing map cannot preserve a strictly positive-charge graph. -/
theorem positive_graph_not_charge_reversing (q q' : ℝ)
    (hq : 0 < q) (hq' : 0 < q') (h : q' = -q) : False := by
  linarith

/-- The exact sparse trace identity leaves a strict margin over the
half-norm Gram-defect threshold. Analytic norm estimates are external. -/
theorem half_trace_margin (b h : ℝ) (hb : 0 < b)
    (hid : h = b / 2) : b / 4 < h := by
  linarith

/-- A positive-semidefinite work source can pair nontrivially with a vector
of negative indefinite energy. Nonzero work is not negative forcing. -/
theorem work_does_not_identify_energy_channel :
    (1 : ℝ)^2 - 2^2 < 0 ∧ (1 : ℝ) * 1 + 0 * 2 ≠ 0 ∧
    (1 : ℝ)^2 - 0^2 > 0 := by
  norm_num

/-- A fixed bounded band cannot supply arbitrarily large difference momenta. -/
theorem bounded_difference_frequency (k l radius : ℝ)
    (hk : |k| ≤ radius) (hl : |l| ≤ radius) :
    |k - l| ≤ 2 * radius := by
  calc
    |k - l| ≤ |k| + |l| := abs_sub k l
    _ ≤ 2 * radius := by linarith

end GUFormalization.CurrentReceiver
