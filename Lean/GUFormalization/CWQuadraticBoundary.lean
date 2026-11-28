import Mathlib

namespace GUFormalization.CWQuadraticBoundary

/-- High-frequency input/output invariants; actual symbol binding is separate. -/
theorem shell_arithmetic (R : ℝ) :
    (2*R)^2 - R^2 = 3*R^2 ∧ -(2*R)^2 = -4*R^2 := by
  constructor <;> ring

/-- Normalized native receiver identity after clearing the positive denominator. -/
theorem receiver_identity (R : ℝ) (h : R^2 + 9 ≠ 0) :
    (36-R^2)/(4*(R^2+9)) + 1/4 = 45/(4*(R^2+9)) := by
  field_simp
  <;> ring

/-- The actual receiver is nonzero at the exact high-frequency control R=12. -/
theorem receiver_control :
    (36-(12:ℚ)^2)/(4*((12:ℚ)^2+9)) = -3/17 := by norm_num

/-- Intrinsic projected forced equation; matrix identities remain explicit premises. -/
theorem intrinsic_equation (l p n x u v f : ℝ) :
    l^2*p*x + l*n*x - u*f - l*v*f =
      l*(n+l*p)*x - (u+l*v)*f := by ring

/-- Ball-growth and derivative-accounting finite core. -/
theorem exponents :
    (39:ℚ)+11/2+1/2=45 ∧ (13:ℚ)/2=2*(13/4) ∧ (13:ℚ)/2>0 := by norm_num

/-- The sum of input regularities, not each individually, pays bilinear scaling. -/
theorem regularity_budget (d1 d2 p : ℝ) (hp : 0 ≤ p)
    (h : (13:ℝ)/2+p ≤ d1+d2) : (13:ℝ)/2 ≤ d1+d2 := by linarith

end GUFormalization.CWQuadraticBoundary
