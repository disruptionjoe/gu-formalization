import Mathlib

namespace GUFormalization.CosmologyRoll

/-- The actual positive moment cone makes the discriminant strictly positive. -/
theorem discriminant_gap (m0 m1 m2 : ℝ) (hm : 0 < m1)
    (hc : m1^2 ≤ m0*m2) : 0 < 3995*m0*m2-3267*m1^2 := by
  nlinarith [sq_nonneg m1]

/-- Legendre potential in the positive-F chart; no physical scale selected. -/
theorem potential_identity (a b c F : ℝ) (hb : b ≠ 0) (hF : F ≠ 0) :
    (((F+a)^2/(4*b)-c)/(2*F^2)) =
      (1+2*a/F-(4*b*c-a^2)/F^2)/(8*b) := by
  field_simp
  <;> ring

/-- Comparison inequality used on the decreasing-F branch. -/
theorem damping_bound (v H M vd c : ℝ) (hv : 0 ≤ v) (hH : H ≤ M)
    (h : c ≤ vd+3*H*v) : c ≤ vd+3*M*v := by
  nlinarith

/-- Finite crossing constraint, not a curvature singularity assertion. -/
theorem crossing (H v D b : ℝ) (hb : b ≠ 0)
    (h : D/(8*b)-3*H*v=0) : H*v=D/(24*b) := by
  field_simp at h ⊢
  nlinarith [h]

/-- Conversion of the late-time rate to the inherited mass scale. -/
theorem rate_identity (a b : ℝ) : a/(36*b) = (a/(6*b))/6 := by ring

/-- Kinematic w can approach minus one for a growing H. -/
theorem kinematic_identity (C t : ℝ) (hC : C ≠ 0) (ht : t ≠ 0) :
    -2*C/(3*(C*t)^2) = -2/(3*C*t^2) := by
  field_simp
  <;> ring

end GUFormalization.CosmologyRoll
