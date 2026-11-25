import Mathlib

/-!
Conditional arithmetic core for the held-observation lower-term equations.
Clifford identities, unitary-adjoint classification, source membership, and the
faithful evaluation map are supplied, not proved here. This is not a GU theorem.
-/
namespace GUFormalization.ChiralWeightTransport

/-- The scalar/trace/tangent/normal equations force the density residual. -/
theorem density_residual (m w b s wh wn t : ℝ)
    (hS : s = w - b) (hTrace : s - t = w)
    (hH : wh = -w) (hN : wn = -2 * (m - 2) * s)
    (hTotal : t = wh + wn) : (2 * m - 3) * (w - b) = 0 := by
  rw [hS] at hN hTrace
  rw [hH, hN] at hTotal
  nlinarith

/-- At the actual normal dimension10, the required normal jet equals H. -/
theorem dimension_ten_density (w b s wh wn t : ℝ)
    (hS : s = w - b) (hTrace : s - t = w)
    (hH : wh = -w) (hN : wn = -16 * s)
    (hTotal : t = wh + wn) : b = w := by
  linarith

/-- The fixed-density case cannot satisfy these rows at a nonzero witness. -/
theorem fixed_density_obstruction (w s wh wn t : ℝ) (hw : w ≠ 0)
    (hS : s = w) (hTrace : s - t = w)
    (hH : wh = -w) (hN : wn = -16 * s)
    (hTotal : t = wh + wn) : False := by
  apply hw
  linarith

/-- A supplied faithful real-coordinate evaluation turns pointwise row
compatibility into equality of the geometric vectors. Faithfulness is explicit. -/
theorem faithful_density_jet {V I : Type*} (ev : V → I → ℝ)
    (faithful : Function.Injective ev) (H b : V)
    (s wh wn t : I → ℝ)
    (hS : ∀ i, s i = ev H i - ev b i)
    (hTrace : ∀ i, s i - t i = ev H i)
    (hH : ∀ i, wh i = -(ev H i))
    (hN : ∀ i, wn i = -16 * s i)
    (hTotal : ∀ i, t i = wh i + wn i) : b = H := by
  apply faithful
  funext i
  exact dimension_ten_density _ _ _ _ _ _ (hS i) (hTrace i) (hH i) (hN i) (hTotal i)

/-- Density equality supplies consistent abstract rows; it does not construct
an operator or select this density from the source. -/
theorem density_equal_rows (w : ℝ) :
    (0 : ℝ) = w - w ∧ (0 : ℝ) - (-w) = w ∧
    (-w : ℝ) = -w + 0 ∧ (0 : ℝ) = -16 * 0 := by
  constructor
  · ring
  constructor
  · ring
  constructor <;> ring

end GUFormalization.ChiralWeightTransport
