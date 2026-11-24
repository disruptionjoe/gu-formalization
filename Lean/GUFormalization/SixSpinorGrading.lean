import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Tactic

/-!
# Six-spinor grading: conditional finite algebra core

This file does not construct the geometric operator, prove the Clifford
identities, identify a source-owned physical grade, or formalize an analytic
domain. The accompanying result supplies: the perpendicular-row identity,
the nonzero coefficients, the unique parallel principal grade, and the exact
torsion witness. The statements below certify the algebraic implications of
those named premises, including passage of oddness to a surjective quotient.
-/

set_option autoImplicit false

namespace GUFormalization.SixSpinorGradingCore

variable {K E O S B : Type*} [Field K]
variable [AddCommGroup E] [Module K E]
variable [AddCommGroup O] [Module K O]
variable [AddCommGroup S] [Module K S]
variable [AddCommGroup B] [Module K B]

/-- The perpendicular horizontal slot kills the whole residual trace row.
The parallel slot then kills the whole residual scalar row. No diagonal
ansatz, involution, adjoint or reality law is imposed on the residual maps. -/
theorem residual_rows_vanish
    (rSigma rNu : E →ₗ[K] S) (P U : S →ₗ[K] S)
    (c e : K) (hc : c ≠ 0) (he : e ≠ 0)
    (hP : Function.Injective P)
    (perpendicular : ∀ x, c • P (rSigma x) = 0)
    (parallel : ∀ x, U (rSigma x) + e • rNu x = 0) :
    rSigma = 0 ∧ rNu = 0 := by
  have hSigma : ∀ x, rSigma x = 0 := by
    intro x
    have hz : P (rSigma x) = 0 :=
      (smul_eq_zero.mp (perpendicular x)).resolve_left hc
    apply hP
    simpa using hz
  constructor
  · ext x
    exact hSigma x
  · ext x
    have hz := parallel x
    rw [hSigma x, map_zero, zero_add] at hz
    exact (smul_eq_zero.mp hz).resolve_left he

/-- Joint coordinates turn the row result into uniqueness of the entire
receiver grade. In the application R=G-G0, b is the fixed first row, and
sigma and nu retain both independent spinor outputs. -/
theorem receiver_residual_zero
    (R : E →ₗ[K] E) (b : E →ₗ[K] B) (sigma nu : E →ₗ[K] S)
    (coordinates : ∀ x, b x = 0 → sigma x = 0 → nu x = 0 → x = 0)
    (hB : ∀ x, b (R x) = 0)
    (P U : S →ₗ[K] S) (c e : K)
    (hc : c ≠ 0) (he : e ≠ 0) (hP : Function.Injective P)
    (perpendicular : ∀ x, c • P (sigma (R x)) = 0)
    (parallel : ∀ x, U (sigma (R x)) + e • nu (R x) = 0) :
    R = 0 := by
  have hrows := residual_rows_vanish
    (sigma.comp R) (nu.comp R) P U c e hc he hP perpendicular parallel
  ext x
  apply coordinates (R x)
  · exact hB x
  · have hz := LinearMap.congr_fun hrows.1 x
    exact hz
  · have hz := LinearMap.congr_fun hrows.2 x
    exact hz

/-- Oddness descends to a surjective operator quotient. Hidden grades and
upper off-block shears never enter this conclusion. -/
theorem oddness_descends
    (q : E →ₗ[K] O) (D G : E →ₗ[K] E) (Do Go : O →ₗ[K] O)
    (hq : Function.Surjective q)
    (operatorDescent : ∀ x, q (D x) = Do (q x))
    (gradeDescent : ∀ x, q (G x) = Go (q x))
    (odd : ∀ x, G (D x) + D (G x) = 0) :
    ∀ y, Go (Do y) + Do (Go y) = 0 := by
  intro y
  obtain ⟨x, rfl⟩ := hq y
  calc
    Go (Do (q x)) + Do (Go (q x)) =
        q (G (D x)) + q (D (G x)) := by
      rw [← operatorDescent x, ← gradeDescent (D x),
          ← gradeDescent x, ← operatorDescent (G x)]
    _ = q (G (D x) + D (G x)) := (map_add q _ _).symm
    _ = 0 := by rw [odd x, map_zero]

/-- The concrete witness coefficient is -a/3, while C is normal Clifford
multiplication by H_mean and chi is horizontal chirality. The square laws
make the projected anticommutator witness injective, hence nonzero. -/
theorem torsion_witness_injective
    (chi C W : S →ₗ[K] S) (d : K) (hd : d ≠ 0)
    (hChi : ∀ x, chi (chi x) = x)
    (hC : ∀ x, C (C x) = -x)
    (witness : ∀ x, W x = d • chi (C x)) :
    Function.Injective W := by
  have chiInjective : Function.Injective chi := by
    intro x y h
    have hh := congrArg chi h
    simpa only [hChi] using hh
  have cInjective : Function.Injective C := by
    intro x y h
    have hh := congrArg C h
    rw [hC x, hC y] at hh
    exact neg_injective hh
  intro x y h
  have hscaled : d • chi (C x) = d • chi (C y) := by
    rw [← witness x, ← witness y]
    exact h
  have hz : d • (chi (C x) - chi (C y)) = 0 := by
    rw [smul_sub, hscaled, sub_self]
  have heq : chi (C x) = chi (C y) :=
    sub_eq_zero.mp ((smul_eq_zero.mp hz).resolve_left hd)
  exact cInjective (chiInjective heq)

/-- A nonzero spinor gives a nonzero torsion anticommutator output. The
geometric proof separately identifies that output with W psi. -/
theorem torsion_witness_nonzero
    (chi C W : S →ₗ[K] S) (d : K) (hd : d ≠ 0)
    (hChi : ∀ x, chi (chi x) = x)
    (hC : ∀ x, C (C x) = -x)
    (witness : ∀ x, W x = d • chi (C x))
    (psi : S) (hpsi : psi ≠ 0) : W psi ≠ 0 := by
  intro hz
  apply hpsi
  apply torsion_witness_injective chi C W d hd hChi hC witness
  simpa using hz

section StableCoefficients
variable [CharZero K]

theorem stable_sigma_coefficient (a : K) :
    a + 10 * (-a / 12) = a / 6 := by ring

theorem stable_tau_coefficient (a : K) :
    2 * a + 14 * (-a / 12) = 5 * a / 6 := by ring

theorem nonzero_witness_coefficient (a : K) (ha : a ≠ 0) :
    -(a / 3) ≠ 0 := by
  exact neg_ne_zero.mpr (div_ne_zero ha (by norm_num))

end StableCoefficients
end GUFormalization.SixSpinorGradingCore
