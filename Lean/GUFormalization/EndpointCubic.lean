import Mathlib

/-! Finite cores only. Native operators, coordinate custody, convergence,
full coupled stationarity and the observation map are separate dependencies.
No analytic remainder bound or numerical radius is asserted by these cores. -/
namespace GUFormalization.EndpointCubic

theorem exact_receiver_coefficient :
    2 * (3 / 8 : ℚ) * ((21 / 4) * (4 / 3) + (21 / 4) * (2 / 3) +
      (15 / 4) * (16 / 3)) = 183 / 8 := by
  norm_num

/-- Coefficient extraction from a quadratic receiver along a cubic path.
The bilinear path expansion supplies the displayed polynomial; the zero
linear row removes its linear-functional contribution at every order. -/
theorem zero_linear_row_cubic_coefficient (q11 q12 q13 q22 q23 q33 : ℝ) :
    (Polynomial.C q11 * Polynomial.X ^ 2 +
      Polynomial.C (2*q12) * Polynomial.X ^ 3 +
      Polynomial.C (2*q13+q22) * Polynomial.X ^ 4 +
      Polynomial.C (2*q23) * Polynomial.X ^ 5 +
      Polynomial.C q33 * Polynomial.X ^ 6).coeff 3 = 2*q12 := by
  simp only [Polynomial.coeff_add, Polynomial.coeff_C_mul_X_pow]
  norm_num

/-- Scalar version of the symmetric bilinear mixed term. Missing the factor2
would halve the certified endpoint coefficient. -/
theorem symmetric_mixed_expansion (q a b h : ℝ) :
    q * (a*h+b*h^2)^2 = q*a^2*h^2+2*q*a*b*h^3+q*b^2*h^4 := by
  ring

/-- Analyticity supplies such a relative remainder bound on a sufficiently
small interval; this finite inequality turns it into strict positivity. -/
theorem leading_cubic_positive (x h : ℝ) (hh : 0 < h)
    (bound : |x-(183/8:ℝ)*h^3| ≤ (183/16:ℝ)*h^3) : 0 < x := by
  have hp : 0 < h^3 := pow_pos hh 3
  have hl := (abs_le.mp bound).1
  linarith

theorem positive_receiver_nonzero (x h : ℝ) (hh : 0 < h)
    (bound : |x-(183/8:ℝ)*h^3| ≤ (183/16:ℝ)*h^3) : x ≠ 0 := by
  exact ne_of_gt (leading_cubic_positive x h hh bound)

end GUFormalization.EndpointCubic
