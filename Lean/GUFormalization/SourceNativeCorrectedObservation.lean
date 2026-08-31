import GUFormalization.SourceNativeObservationDescent

/-!
# The canonical split correction into an observed Clifford kernel

For a supplied split-surjective observed Clifford contraction `gamma`, the
map `P = 1 - j gamma` is a projector onto `ker gamma`.  It gives an explicit
linear equivalence between the observed carrier and its gamma kernel paired
with the trace carrier.  Composing `P` with any observation map removes its
observed gamma trace and changes nothing exactly when the original output was
already gamma-traceless.

This is exact linear algebra from a supplied right inverse.  It does not show
that the correction is source-owned, dynamically selected, a physical
quotient, or an observed family sector.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeCorrectedObservation

universe u v w x

variable {R : Type u} [Ring R]
variable {A : Type v} {B : Type w} {S : Type x}
variable [AddCommGroup A] [AddCommGroup B] [AddCommGroup S]
variable [Module R A] [Module R B] [Module R S]

/-- Subtract the supplied trace insertion from an observed carrier. -/
def kernelProjector (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B) : B →ₗ[R] B :=
  LinearMap.id - rightInv.comp gamma

@[simp]
theorem kernelProjector_apply (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    (b : B) :
    kernelProjector gamma rightInv b = b - rightInv (gamma b) := by
  rfl

/-- The split correction is gamma-traceless. -/
theorem gamma_kernelProjector
    (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (b : B) :
    gamma (kernelProjector gamma rightInv b) = 0 := by
  rw [kernelProjector_apply, map_sub]
  have hpoint := LinearMap.congr_fun rightInverse (gamma b)
  simpa using sub_eq_zero.mpr hpoint.symm

/-- The projector viewed as a map into the observed gamma kernel. -/
def kernelComponent
    (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S)) :
    B →ₗ[R] LinearMap.ker gamma :=
  (kernelProjector gamma rightInv).codRestrict (LinearMap.ker gamma)
    (gamma_kernelProjector gamma rightInv rightInverse)

/-- Gamma-traceless vectors are fixed by the split correction. -/
theorem kernelProjector_fixed_of_mem
    (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    {b : B} (hb : b ∈ LinearMap.ker gamma) :
    kernelProjector gamma rightInv b = b := by
  rw [kernelProjector_apply]
  simp only [LinearMap.mem_ker] at hb
  simp [hb]

/-- Being fixed by the split correction is equivalent to gamma-tracelessness. -/
theorem kernelProjector_fixed_iff
    (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (b : B) :
    kernelProjector gamma rightInv b = b ↔ gamma b = 0 := by
  constructor
  · intro h
    have hzero := gamma_kernelProjector gamma rightInv rightInverse b
    rw [h] at hzero
    exact hzero
  · intro h
    exact kernelProjector_fixed_of_mem gamma rightInv h

/-- The split correction is idempotent. -/
theorem kernelProjector_idempotent
    (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S)) :
    (kernelProjector gamma rightInv).comp (kernelProjector gamma rightInv) =
      kernelProjector gamma rightInv := by
  ext b
  exact kernelProjector_fixed_of_mem gamma rightInv
    (gamma_kernelProjector gamma rightInv rightInverse b)

/-- A split-surjective observed contraction canonically decomposes its carrier
as gamma kernel plus trace carrier. -/
def kernelTraceEquiv
    (gamma : B →ₗ[R] S) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S)) :
    B ≃ₗ[R] LinearMap.ker gamma × S where
  toLinearMap := LinearMap.prod (kernelComponent gamma rightInv rightInverse) gamma
  invFun pair := pair.1.1 + rightInv pair.2
  left_inv b := by
    change kernelProjector gamma rightInv b + rightInv (gamma b) = b
    simp [kernelProjector_apply]
  right_inv pair := by
    have hright : gamma (rightInv pair.2) = pair.2 := by
      simpa using LinearMap.congr_fun rightInverse pair.2
    have hker : gamma pair.1.1 = 0 := pair.1.property
    apply Prod.ext
    · apply Subtype.ext
      change kernelProjector gamma rightInv (pair.1.1 + rightInv pair.2) = pair.1.1
      simp [kernelProjector_apply, hker, hright]
    · change gamma (pair.1.1 + rightInv pair.2) = pair.2
      simp [hker, hright]

/-- Correct any observation map by projecting its output into the observed
gamma kernel. -/
def correctedObservation
    (gamma : B →ₗ[R] S) (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] B) :
    A →ₗ[R] B :=
  (kernelProjector gamma rightInv).comp observe

@[simp]
theorem correctedObservation_apply
    (gamma : B →ₗ[R] S) (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] B)
    (a : A) :
    correctedObservation gamma observe rightInv a =
      observe a - rightInv (gamma (observe a)) := by
  rfl

/-- The corrected observation output is always gamma-traceless. -/
theorem gamma_correctedObservation
    (gamma : B →ₗ[R] S) (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (a : A) :
    gamma (correctedObservation gamma observe rightInv a) = 0 := by
  exact gamma_kernelProjector gamma rightInv rightInverse (observe a)

/-- Literal observation splits into its corrected kernel component and its
supplied trace insertion. -/
theorem observe_eq_corrected_add_trace
    (gamma : B →ₗ[R] S) (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] B)
    (a : A) :
    observe a = correctedObservation gamma observe rightInv a +
      rightInv (gamma (observe a)) := by
  simp [correctedObservation_apply]

/-- Correction changes nothing exactly on outputs already in the observed
gamma kernel. -/
theorem correctedObservation_eq_observe_iff
    (gamma : B →ₗ[R] S) (observe : A →ₗ[R] B) (rightInv : S →ₗ[R] B)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (a : A) :
    correctedObservation gamma observe rightInv a = observe a ↔
      gamma (observe a) = 0 := by
  exact kernelProjector_fixed_iff gamma rightInv rightInverse (observe a)

/-- If literal observation already preserves the ambient kernel, correction
agrees with it on that kernel. -/
theorem correctedObservation_eq_of_kernel_preservation
    (gammaA : A →ₗ[R] S) (gammaB : B →ₗ[R] S)
    (observe : A →ₗ[R] B) (rightInvB : S →ₗ[R] B)
    (rightInverseB : gammaB.comp rightInvB = (LinearMap.id : S →ₗ[R] S))
    (preservesKernel : ∀ a : A, gammaA a = 0 → gammaB (observe a) = 0)
    {a : A} (ha : gammaA a = 0) :
    correctedObservation gammaB observe rightInvB a = observe a := by
  exact (correctedObservation_eq_observe_iff gammaB observe rightInvB rightInverseB a).2
    (preservesKernel a ha)

end SourceNativeCorrectedObservation
end GUFormalization
