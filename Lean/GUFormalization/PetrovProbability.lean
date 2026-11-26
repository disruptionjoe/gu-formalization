import Mathlib.Tactic
import Mathlib.Analysis.Complex.Basic

/-!
Finite core only for quantitative observer-probability escape.
The weighted overlap inequality and exact quartic substitution identities are
formalized. Proper actions, measure tightness, Petrov classification, limits,
and the existence of the Julia covariant are NOT formalized here.
-/

namespace GUFormalization.PetrovProbability

open scoped BigOperators

/-- Double-counting with weights: q equal row masses and column overlap at
most m give q * mass ≤ m. This is the finite arithmetic of the measure proof. -/
theorem weighted_overlap_budget {q k : ℕ}
    (a : Fin q → Fin k → ℝ) (w : Fin k → ℝ) (mass m : ℝ)
    (hrow : ∀ i, ∑ j, a i j = mass)
    (hcol : ∀ j, ∑ i, a i j ≤ m * w j)
    (hw : ∑ j, w j = 1) : (q : ℝ) * mass ≤ m := by
  calc
    (q : ℝ) * mass = ∑ i : Fin q, ∑ j : Fin k, a i j := by
      simp [hrow]
    _ = ∑ j : Fin k, ∑ i : Fin q, a i j := Finset.sum_comm
    _ ≤ ∑ j : Fin k, m * w j := Finset.sum_le_sum (fun j _ => hcol j)
    _ = m := by rw [← Finset.mul_sum, hw, mul_one]

theorem typeII_budget (mass : ℝ) (h : 4 * mass ≤ 2) : mass ≤ 1 / 2 := by
  linarith

theorem typeIII_budget (mass : ℝ) (h : 4 * mass ≤ 1) : mass ≤ 1 / 4 := by
  linarith

/-- The probability discrepancy forced by two almost disjoint tight masses. -/
theorem variation_lower_bound (p q e : ℝ) (hp : 1 - e ≤ p) (hq : q ≤ e) :
    1 - 2 * e ≤ p - q := by linarith

def quartic (a b c x y : ℂ) : ℂ := a * x^2 * y^2 + b * x * y^3 + c * x^3 * y

/-- Exact II/III escaping involution, for arbitrary nonzero complex t.
For escape in the analytic theorem t tends to +infinity in the reals. -/
theorem escaping_involution (a b t x y : ℂ) (ht : t ≠ 0) :
    quartic a b (b / t^2) (-Complex.I * t * y) (-Complex.I / t * x) =
      quartic a b (b / t^2) x y := by
  unfold quartic
  field_simp
  ring_nf
  simp

/-- Exact nonidentity type-II stabilizer for its normalized alpha=beta=1 form. -/
theorem typeII_stabilizer (x y : ℂ) :
    quartic 1 1 0 (Complex.I * (x+y)) (-Complex.I * y) =
      quartic 1 1 0 x y := by
  unfold quartic
  ring_nf
  simp

/-- One extra III stabilizer before its common 1/sqrt(2) normalization.
A homogeneous quartic acquires factor 4; normalization removes it. -/
theorem typeIII_stabilizer_A (t x y : ℂ) (ht : t ≠ 0) :
    quartic 0 1 (1 / t^2) (-Complex.I*x+t*y) (-x/t+Complex.I*y) =
      4 * quartic 0 1 (1 / t^2) x y := by
  unfold quartic
  field_simp
  ring_nf
  simp
  ring

theorem typeIII_stabilizer_B (t x y : ℂ) (ht : t ≠ 0) :
    quartic 0 1 (1 / t^2) (-Complex.I*x-t*y) (x/t+Complex.I*y) =
      4 * quartic 0 1 (1 / t^2) x y := by
  unfold quartic
  field_simp
  ring_nf
  simp
  ring

/-- The fixed compact involution in the sharp type-II degeneration. -/
theorem even_quartic_stabilizer (a b c x y : ℂ) :
    a * (Complex.I*x)^4 + b * (Complex.I*x)^2 * (-Complex.I*y)^2 +
      c * (-Complex.I*y)^4 = a*x^4 + b*x^2*y^2+c*y^4 := by
  ring_nf
  simp

end GUFormalization.PetrovProbability
