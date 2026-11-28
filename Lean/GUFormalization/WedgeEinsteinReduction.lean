import Mathlib.Tactic

/-!
Finite cores for the declared leading four-dimensional wedge reduction.
The moments, their positivity and moment-cone inequality are hypotheses.
This file does not prove measure support, geometric reduction, PDE existence,
physical state admission, or any statement about full fourteen-dimensional GU.
-/
namespace GUFormalization.WedgeEinsteinReduction

/-- The four-dimensional Weyl/Euler algebra; geometric identities are inputs. -/
theorem curvature_decomposition (riem ric scalarSq : ℝ) :
    (riem - 2 * ric + scalarSq / 3) / 2 -
      (riem - 4 * ric + scalarSq) / 2 + (17 / 6 : ℝ) * scalarSq =
      ric + (5 / 2 : ℝ) * scalarSq := by ring

/-- The exact conformal-ray scalar identity at nonzero scale. -/
theorem conformal_scalar (a r q : ℝ) (ha : a ≠ 0) :
    (115 / 8 : ℝ) + r / (2 * a) + q / a ^ 2 +
      (5 / 2 : ℝ) * (-10 + r / a) ^ 2 =
      (q + (5 / 2 : ℝ) * r ^ 2) / a ^ 2 -
      (99 / 2 : ℝ) * r / a + (2115 / 8 : ℝ) := by
  field_simp
  ring

/-- Positivity of the moment-cone margin excludes the degenerate scalar row. -/
theorem scalar_margin (m₀ m₁ m₂ : ℝ) (h₁ : 0 < m₁)
    (hcone : m₁ ^ 2 ≤ m₀ * m₂) :
    0 < 3995 * m₀ * m₂ - 3267 * m₁ ^ 2 := by
  have hsq : 0 < m₁ ^ 2 := sq_pos_of_pos h₁
  nlinarith

/-- The scalar mass has negative sign for every positive moment pair. -/
theorem scalar_mass_negative (m₀ m₁ : ℝ) (h₀ : 0 < m₀) (h₁ : 0 < m₁) :
    -(99 * m₁) / (34 * m₀) < 0 := by
  exact div_neg_of_neg_of_pos (by nlinarith) (by positivity)

/-- Coefficient-cone bound, expressed without divisions or sign ambiguity in h. -/
theorem coefficient_bound (h m₀ m₁ m₂ : ℝ)
    (hcone : m₁ ^ 2 ≤ m₀ * m₂) :
    (-99 * h * m₁ / 4) ^ 2 ≤
      (2178 / 235 : ℝ) * ((h * m₀ / 2) * (2115 * h * m₂ / 16)) := by
  have hp := mul_le_mul_of_nonneg_left hcone (sq_nonneg h)
  nlinarith

/-- The full conformal metric row factors through this scalar operator. -/
theorem full_row_factor (a b lam box : ℝ) :
    (a + 8 * b * lam) - 2 * b * (3 * box + 4 * lam) = a - 6 * b * box := by ring

/-- Positive-moment de Sitter scalar growth has a strictly positive root.
This is the algebraic instability criterion, not a PDE existence theorem. -/
theorem growing_root_positive (H μ : ℝ) (hH : 0 < H) (hμ : 0 < μ) :
    0 < (-3 * H + Real.sqrt (9 * H ^ 2 + 4 * μ)) / 2 := by
  have hs := Real.sq_sqrt (show 0 ≤ 9 * H ^ 2 + 4 * μ by positivity)
  have hn := Real.sqrt_nonneg (9 * H ^ 2 + 4 * μ)
  have hg : 3 * H < Real.sqrt (9 * H ^ 2 + 4 * μ) := by nlinarith
  linarith

end GUFormalization.WedgeEinsteinReduction
