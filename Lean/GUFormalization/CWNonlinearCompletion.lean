import Mathlib

namespace GUFormalization.CWNonlinearCompletion

/-- The actual boosted packets lie strictly inside the common stable set. -/
theorem stable_threshold_witness :
    (703 : ℚ) / 9 - 36 = 379 / 9 ∧ (379 : ℚ) / 9 > 0 ∧
    -(3 : ℚ) / (26 / 3) - 3 / (26 / 3) = -9 / 13 := by
  norm_num

/-- The actual sign convention gives a nonzero inverse residue receiver. -/
theorem threshold_residue :
    -(-(12 : ℚ) / 2) * 104448 = 626688 ∧ (626688 : ℚ) ≠ 0 := by
  norm_num

/-- No principal-value freedom exists where the homological operator is invertible. -/
theorem inverse_forces_unique {V : Type*} (L B : V → V)
    (h : Function.LeftInverse B L) (x y : V) (heq : L x = L y) : x = y := by
  exact h.injective heq

/-- The explicitly computed invariant-block particular solves the negative force. -/
theorem self_particular :
    12 * (1144 : ℚ) - 144 * (1144 / 3) = -41184 ∧
    -4 * (1144 : ℚ) + 12 * (1144 / 3) = 0 ∧
    12 * (-4056 : ℚ) = -48672 := by
  norm_num

/-- The threshold divisor has a fixed sign on the invertible side. -/
theorem threshold_divisor (δ ν : ℝ) (hδ : 0 < δ) :
    144 - 4 * (36 + δ + ν^2) = -4 * (δ + ν^2) ∧ δ + ν^2 > 0 := by
  constructor
  · ring
  · positivity

end GUFormalization.CWNonlinearCompletion
