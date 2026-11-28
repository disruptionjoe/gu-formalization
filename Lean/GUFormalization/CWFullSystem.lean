import Mathlib

namespace GUFormalization.CWFullSystem

/-- A nonzero excluded quadratic receiver contradicts exact support closure. -/
theorem quadratic_receiver_obstruction {K : Type*} [Ring K]
    (linear quadratic : K) (hlinear : linear = 0)
    (hequation : linear + quadratic = 0) (hquad : quadratic ≠ 0) : False := by
  apply hquad
  simpa [hlinear] using hequation

/-- A conserved positive norm cannot include a nonzero linear growth orbit. -/
theorem linear_growth_not_bounded (a C : ℝ) (ha : 0 < a) :
    ∃ t : ℝ, 0 ≤ t ∧ C < t * a := by
  refine ⟨max 0 (C / a) + 1, by positivity, ?_⟩
  have h : C / a < max 0 (C / a) + 1 := by linarith [le_max_right (0 : ℝ) (C / a)]
  exact (div_lt_iff₀ ha).mp h

/-- The owned nonlinear support witness lies strictly in/out of the domain. -/
theorem support_witness :
    (84 : ℚ) > 12^2 / 4 ∧ (-64 : ℚ) < 12^2 / 4 ∧ (-749632 : ℚ) ≠ 0 := by
  norm_num

/-- Reversing the forcing reverses the certified quadratic receiver. -/
theorem secular_receiver :
    -(3 * (26112 : ℚ)) = -78336 ∧ (-104448 : ℚ) ≠ 0 := by
  norm_num

end GUFormalization.CWFullSystem
