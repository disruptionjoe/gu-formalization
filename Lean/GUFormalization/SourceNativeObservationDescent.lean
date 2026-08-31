import GUFormalization.SourceNativeSpin64Observation

/-!
# Exact criterion for Clifford-kernel descent through observation

Suppose ambient Clifford contraction has a supplied right inverse.  Then an
observation map preserves the ambient Clifford kernel exactly when the
observed contraction factors through the ambient contraction.  The factor is
explicit and unique.

This is an algebraic acceptance criterion for a proposed observation bridge.
It does not construct the source-owned observation map, a physical quotient,
cohomology, dynamics, or an observed generation sector.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeObservationDescent

universe u v w x y

variable {R : Type u} [Ring R]
variable {A : Type v} {B : Type w} {S : Type x} {T : Type y}
variable [AddCommGroup A] [AddCommGroup B] [AddCommGroup S] [AddCommGroup T]
variable [Module R A] [Module R B] [Module R S] [Module R T]

/-- The only possible factor through a split-surjective ambient contraction. -/
def descentFactor (_gammaA : A →ₗ[R] S) (gammaB : B →ₗ[R] T)
    (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] A) : S →ₗ[R] T :=
  gammaB.comp (observe.comp rightInv)

/-- If observation kills the observed trace of every ambient gamma-traceless
vector, its observed trace factors through ambient Clifford contraction. -/
theorem factorization_of_kernel_preservation
    (gammaA : A →ₗ[R] S) (gammaB : B →ₗ[R] T)
    (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] A)
    (rightInverse : gammaA.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (preservesKernel : ∀ a : A, gammaA a = 0 → gammaB (observe a) = 0) :
    gammaB.comp observe = (descentFactor gammaA gammaB observe rightInv).comp gammaA := by
  ext a
  let k : A := a - rightInv (gammaA a)
  have hk : gammaA k = 0 := by
    dsimp [k]
    rw [map_sub]
    have hpoint := LinearMap.congr_fun rightInverse (gammaA a)
    simpa using sub_eq_zero.mpr hpoint.symm
  have hzero := preservesKernel k hk
  dsimp [k] at hzero
  rw [map_sub, map_sub] at hzero
  change gammaB (observe a) = gammaB (observe (rightInv (gammaA a)))
  exact sub_eq_zero.mp hzero

/-- A commuting-square factorization automatically sends the ambient kernel
into the observed kernel. -/
theorem kernel_preservation_of_factorization
    (gammaA : A →ₗ[R] S) (gammaB : B →ₗ[R] T)
    (observe : A →ₗ[R] B) (factor : S →ₗ[R] T)
    (factorization : gammaB.comp observe = factor.comp gammaA) :
    ∀ a : A, gammaA a = 0 → gammaB (observe a) = 0 := by
  intro a ha
  have hpoint := LinearMap.congr_fun factorization a
  simpa [ha] using hpoint

/-- With a supplied right inverse, preservation of the ambient Clifford
kernel is equivalent to the exact commuting-square law. -/
theorem kernel_preservation_iff_factorization
    (gammaA : A →ₗ[R] S) (gammaB : B →ₗ[R] T)
    (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] A)
    (rightInverse : gammaA.comp rightInv = (LinearMap.id : S →ₗ[R] S)) :
    (∀ a : A, gammaA a = 0 → gammaB (observe a) = 0) ↔
      gammaB.comp observe =
        (descentFactor gammaA gammaB observe rightInv).comp gammaA := by
  constructor
  · exact factorization_of_kernel_preservation gammaA gammaB observe rightInv rightInverse
  · intro h
    exact kernel_preservation_of_factorization gammaA gammaB observe
      (descentFactor gammaA gammaB observe rightInv) h

/-- The factor through a split-surjective ambient contraction is unique. -/
theorem descentFactor_unique
    (gammaA : A →ₗ[R] S) (gammaB : B →ₗ[R] T)
    (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] A)
    (rightInverse : gammaA.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (factor : S →ₗ[R] T)
    (factorization : gammaB.comp observe = factor.comp gammaA) :
    factor = descentFactor gammaA gammaB observe rightInv := by
  ext s
  have hpoint := LinearMap.congr_fun factorization (rightInv s)
  have hright := LinearMap.congr_fun rightInverse s
  change gammaB (observe (rightInv s)) = factor (gammaA (rightInv s)) at hpoint
  change gammaA (rightInv s) = s at hright
  simpa [descentFactor, hright] using hpoint.symm

end SourceNativeObservationDescent
end GUFormalization
