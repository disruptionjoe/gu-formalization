import Mathlib

/-!
# Observation pullback need not preserve a Clifford kernel

This module isolates the algebraic core of the source-native observation
obstruction.  An ambient one-form spinor is split into horizontal and normal
parts.  If normal Clifford multiplication has a right inverse, every nonzero
horizontal trace has an ambient gamma-traceless lift whose literal pullback
retains that nonzero trace.

The theorem is representation-grade linear algebra.  It does not construct a
physical observation map, quotient, generation sector, mass, or action.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeSpin64Observation

universe u v w x

variable {R : Type u} [Ring R]
variable {H : Type v} {N : Type w} {S : Type x}
variable [AddCommGroup H] [AddCommGroup N] [AddCommGroup S]
variable [Module R H] [Module R N] [Module R S]

/-- Ambient Clifford contraction on a horizontal/normal splitting. -/
def ambientGamma (gammaH : H →ₗ[R] S) (gammaN : N →ₗ[R] S) :
    H × N →ₗ[R] S :=
  gammaH.comp (LinearMap.fst R H N) + gammaN.comp (LinearMap.snd R H N)

/-- Literal observation pullback discards the normal covector component. -/
def observationPullback : H × N →ₗ[R] H := LinearMap.fst R H N

@[simp]
theorem ambientGamma_apply (gammaH : H →ₗ[R] S) (gammaN : N →ₗ[R] S)
    (h : H) (n : N) :
    ambientGamma gammaH gammaN (h, n) = gammaH h + gammaN n := by
  rfl

/-- A right inverse for normal Clifford multiplication produces an ambient
gamma-traceless lift of every horizontal one-form spinor. -/
theorem ambient_kernel_lift (gammaH : H →ₗ[R] S) (gammaN : N →ₗ[R] S)
    (invN : S →ₗ[R] N)
    (rightInverse : gammaN.comp invN = (LinearMap.id : S →ₗ[R] S)) (h : H) :
    ambientGamma gammaH gammaN (h, -invN (gammaH h)) = 0 := by
  rw [ambientGamma_apply, map_neg]
  have pointwise := LinearMap.congr_fun rightInverse (gammaH h)
  have pointwise' : gammaN (invN (gammaH h)) = gammaH h := by
    simpa using pointwise
  rw [pointwise', add_neg_cancel]

/-- The literal pullback of the same lift retains its horizontal component. -/
@[simp]
theorem observationPullback_kernel_lift (gammaH : H →ₗ[R] S)
    (invN : S →ₗ[R] N) (h : H) :
    observationPullback (R := R) (h, -invN (gammaH h)) = h := by
  rfl

/-- If some horizontal Clifford trace is nonzero, literal observation
pullback does not map the ambient gamma kernel into the observed gamma kernel.

This is the general algebraic witness used by the source-native `Spin(6,4)`
analysis.  No dimension count or physical-sector interpretation enters. -/
theorem exists_ambient_kernel_observed_trace_ne_zero
    (gammaH : H →ₗ[R] S) (gammaN : N →ₗ[R] S)
    (invN : S →ₗ[R] N)
    (rightInverse : gammaN.comp invN = (LinearMap.id : S →ₗ[R] S))
    (h : H) (horizontalTrace : gammaH h ≠ 0) :
    ∃ t : H × N,
      ambientGamma gammaH gammaN t = 0 ∧
      gammaH (observationPullback (R := R) t) ≠ 0 := by
  refine ⟨(h, -invN (gammaH h)), ambient_kernel_lift gammaH gammaN invN rightInverse h, ?_⟩
  simpa using horizontalTrace

end SourceNativeSpin64Observation
end GUFormalization
