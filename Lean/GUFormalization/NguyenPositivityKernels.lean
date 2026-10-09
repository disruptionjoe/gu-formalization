import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.BilinearForm.Basic
import Mathlib.Tactic.Linarith

/-!
# Mathematical kernels used in the Nguyen--Polya section 3.1 assessment

This module separates the conditional counterexample logic from actual
mathematical deductions about positive forms, observation and a supplied
polynomial system. It does not formalize Witten's Chern--Simons construction,
identify that construction with GU, or prove that GU is unitary or inconsistent.

In particular, the counterexample theorem takes its witness as an explicit
argument. No physics existence statement is introduced as a postulate. The
canonical polynomial coefficients come from the separately checked Clifford
calculation; their geometric derivation is outside this Lean module.
-/

set_option autoImplicit false

namespace GUFormalization.NguyenPositivityKernels

/-- A supplied unitary, semibounded witness refutes the universal failure
implication. This checks logic only; it does not construct a gauge theory. -/
theorem witness_refutes_universal_failure
    {Theory : Type*} (complexified unitary boundedBelow : Theory → Prop)
    (w : Theory) (hc : complexified w) (hu : unitary w) (hb : boundedBelow w) :
    ¬ (∀ t, complexified t → ¬ unitary t ∨ ¬ boundedBelow t) := by
  intro claim
  rcases claim w hc with failure | failure
  · exact failure hu
  · exact failure hb

/-- A real growing eigenvector cannot belong to a strictly positive bilinear
carrier on which the generator conserves that form. All domain membership
and conservation data are explicit premises; no GU physical domain is chosen. -/
theorem positive_conserved_form_excludes_growing_eigenvector
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (A : V →ₗ[ℝ] V)
    (positive : ∀ v, v ≠ 0 → 0 < B v v)
    (conserved : ∀ x y, B (A x) y + B x (A y) = 0)
    (v : V) (hv : v ≠ 0) (rate : ℝ) (hRate : 0 < rate)
    (eigenvector : A v = rate • v) : False := by
  have identity := conserved v v
  rw [eigenvector] at identity
  rw [LinearMap.BilinForm.smul_left, LinearMap.BilinForm.smul_right] at identity
  have strictly_positive := mul_pos hRate (positive v hv)
  linarith

/-- A nonzero symmetric action difference within one observation fibre
prevents the action from factoring through observation. Smooth bump support,
Clifford parity and the action coefficients must be supplied separately. -/
theorem nonzero_even_difference_prevents_action_descent
    {Carrier Observed : Type*} (observe : Carrier → Observed)
    (action : Carrier → ℝ) (zero plus minus : Carrier)
    (hPlus : observe plus = observe zero)
    (hMinus : observe minus = observe zero)
    (hDifference : action plus + action minus - 2 * action zero ≠ 0) :
    ¬ (∃ reduced : Observed → ℝ, ∀ x, action x = reduced (observe x)) := by
  rintro ⟨reduced, factorization⟩
  apply hDifference
  rw [factorization plus, factorization minus, factorization zero, hPlus, hMinus]
  linarith

/-- Normal grade-one rows on the three constant invariant blocks. The five
conditions are necessary rows, not a claim that these fields truncate the
full action consistently. The action-to-polynomial bridge is external. -/
def CanonicalThreeBlockNecessary (a b c kappa : ℝ) : Prop :=
  (b - a) / 2 = 0 ∧
  (a - c) / 2 = 0 ∧
  12*a^2 + 108*a*b + 12*a*c + 144*b^2 + 36*b*c + kappa*a - 21/4 = 0 ∧
  24*a^2 + 128*a*b + 16*a*c + 112*b^2 + 32*b*c + kappa*b - 15/4 = 0 ∧
  24*a^2 + 144*a*b + 144*b^2 + kappa*c - 21/4 = 0

/-- The supplied canonical necessary system has no real solution for any
coupling. This is universal real algebra, not a finite numerical search. -/
theorem canonical_three_block_no_solution (a b c kappa : ℝ) :
    ¬ CanonicalThreeBlockNecessary a b c kappa := by
  rintro ⟨hAB, hAC, hH, hV, _hTrace⟩
  have hba : b = a := by linarith
  have hca : c = a := by linarith
  subst b
  subst c
  nlinarith [hH, hV]

/-- The obstruction persists even at zero coupling. -/
theorem canonical_three_block_no_solution_zero_coupling (a b c : ℝ) :
    ¬ CanonicalThreeBlockNecessary a b c 0 :=
  canonical_three_block_no_solution a b c 0

end GUFormalization.NguyenPositivityKernels

#print axioms GUFormalization.NguyenPositivityKernels.witness_refutes_universal_failure
#print axioms GUFormalization.NguyenPositivityKernels.positive_conserved_form_excludes_growing_eigenvector
#print axioms GUFormalization.NguyenPositivityKernels.nonzero_even_difference_prevents_action_descent
#print axioms GUFormalization.NguyenPositivityKernels.canonical_three_block_no_solution
#print axioms GUFormalization.NguyenPositivityKernels.canonical_three_block_no_solution_zero_coupling
