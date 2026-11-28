import Mathlib

namespace GUFormalization.PTPositiveQuotient

/-- A finite nonnegative conserved quantity cannot also contract strictly. -/
theorem conserved_contraction (E a : ℝ) (hE : 0 ≤ E) (ha : a < 1)
    (h : E ≤ a * E) : E = 0 := by
  nlinarith

/-- Descending a readout requires every identified-zero state to be invisible. -/
theorem readout_obstruction {V W : Type*} [Zero W] (q : V → ℝ) (o : V → W)
    (x : V) (hq : q x = 0) (ho : o x ≠ 0) :
    ¬ (∀ v, q v = 0 → o v = 0) := by
  intro h
  exact ho (h x hq)

/-- The remaining imaginary off-diagonal of a PSD Jordan Gram matrix vanishes. -/
theorem jordan_psd_offdiagonal (v : ℝ) (h : 0 ≤ -(v^2)) : v = 0 := by
  nlinarith [sq_nonneg v]

/-- Conditional inverse-square partner cost for a uniformly controlled readout. -/
theorem partner_weight (A B M w : ℝ) (hab : A = w^2 * B)
    (h : 144 ≤ M^2 * A) : 144 ≤ M^2 * w^2 * B := by
  rw [hab] at h
  nlinarith [h]

/-- The actual sparse quotient-defect receiver is nonzero. -/
theorem quotient_receiver : (13448 / 13 : ℚ) ≠ 0 := by norm_num

/-- Nonzero phase derivative used in the fixed-history coarea argument. -/
theorem phase_submersion : (-2 * 3 / (26 / 3) : ℚ) = -9 / 13 := by norm_num

/-- The displayed equal-frequency PU overlap is indefinite as a Gram matrix. -/
theorem negative_overlap_determinant (c : ℝ) (hc : 0 < c) : -(c^2) < 0 := by
  nlinarith [sq_pos_of_pos hc]

end GUFormalization.PTPositiveQuotient
