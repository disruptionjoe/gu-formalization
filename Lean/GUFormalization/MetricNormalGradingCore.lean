import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
Conditional finite core for the metric-normal grading theorem.

The written geometric proof supplies the nondegenerate horizontal pairing,
selfadjoint shape, skew metric connection block, injectivity of the mixed
Clifford coefficient map, and the equation relating the observed defect to
that map. This file does not construct Clifford modules, connections,
observation quotients, global domains, or source physical grades.
-/
set_option autoImplicit false

namespace GUFormalization.MetricNormalGradingCore

variable {V Z N : Type*}
variable [AddCommGroup V] [Module ℝ V]
variable [AddCommGroup Z] [Module ℝ Z]

/-- A selfadjoint operator equal to a skew operator vanishes for a
nondegenerate real pairing. The pairing laws needed by this implication
are stated explicitly; positivity is neither used nor asserted. -/
theorem symmetric_skew_zero
    (pair : V → V → ℝ)
    (nondegenerate : ∀ x, (∀ y, pair x y = 0) → x = 0)
    (S A : V →ₗ[ℝ] V)
    (symmetric : ∀ x y, pair (S x) y = pair x (S y))
    (skew : ∀ x y, pair (A x) y = -pair x (A y))
    (equal : S = A) : S = 0 := by
  subst A
  ext x
  apply nondegenerate (S x)
  intro y
  have hs := symmetric x y
  have ha := skew x y
  linarith

/-- Faithfulness of the mixed Clifford coefficients turns an observed
zero residual into equality of the shape and skew connection families.
The faithful coefficient map is supplied by the analytic Clifford proof. -/
theorem mixed_residual_nonzero
    (pair : V → V → ℝ)
    (nondegenerate : ∀ x, (∀ y, pair x y = 0) → x = 0)
    (S A : N → (V →ₗ[ℝ] V))
    (symmetric : ∀ n x y, pair (S n x) y = pair x (S n y))
    (skew : ∀ n x y, pair (A n x) y = -pair x (A n y))
    (nonzeroShape : ∃ n, S n ≠ 0)
    (F : (N → (V →ₗ[ℝ] V)) →ₗ[ℝ] Z)
    (faithful : Function.Injective F) : F (S - A) ≠ 0 := by
  intro hz
  have hdiff : S - A = 0 := faithful (by simpa using hz)
  have hequal : S = A := sub_eq_zero.mp hdiff
  obtain ⟨n, hn⟩ := nonzeroShape
  apply hn
  exact symmetric_skew_zero pair nondegenerate (S n) (A n)
    (symmetric n) (skew n) (congrFun hequal n)

/-- The nonzero stable scalar coefficient and invertible horizontal grade
cannot erase a nonzero mixed residual. -/
theorem graded_defect_nonzero
    (Fvalue : Z) (hF : Fvalue ≠ 0)
    (chi : Z →ₗ[ℝ] Z) (injectiveChi : Function.Injective chi)
    (coefficient : ℝ) (nonzeroCoefficient : coefficient ≠ 0) :
    coefficient • chi Fvalue ≠ 0 := by
  intro hz
  have hchi : chi Fvalue = 0 :=
    (smul_eq_zero.mp hz).resolve_left nonzeroCoefficient
  apply hF
  apply injectiveChi
  simpa using hchi

/-- The stable zero-SE coefficient in the sigma receiver is a/6. -/
theorem stable_sigma_coefficient (a : ℝ) : a + 10 * (-a / 12) = a / 6 := by
  ring

end GUFormalization.MetricNormalGradingCore
