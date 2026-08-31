import GUFormalization.SourceNativeCorrectedObservation

/-!
# Split dependence and naturality of corrected observation

The corrected observation projector `P = 1 - j gamma` is canonical only after
a right inverse `j` has been supplied. This file makes that dependence exact:
two splittings give the same projector exactly when the splittings agree.

It also proves the correct naturality statement. A carrier map intertwines
the corrected projectors when it intertwines both the Clifford contractions
and the selected right inverses. These are conditional linear-algebra laws;
they do not construct or source-own a preferred splitting or physical
quotient.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeCorrectedObservationNaturality

open SourceNativeCorrectedObservation

universe u v w x y z

variable {R : Type u} [Ring R]
variable {A : Type v} {B : Type w} {S : Type x}
variable {B' : Type y} {S' : Type z}
variable [AddCommGroup A] [AddCommGroup B] [AddCommGroup S]
variable [AddCommGroup B'] [AddCommGroup S']
variable [Module R A] [Module R B] [Module R S]
variable [Module R B'] [Module R S']

/-- The change in the projector is exactly the change in the selected trace
insertion, evaluated on the Clifford trace. -/
theorem kernelProjector_sub_kernelProjector
    (gamma : B →ₗ[R] S) (rightInv₁ rightInv₂ : S →ₗ[R] B) :
    kernelProjector gamma rightInv₁ - kernelProjector gamma rightInv₂ =
      (rightInv₂ - rightInv₁).comp gamma := by
  ext b
  simp [kernelProjector_apply]

/-- For a split-surjective contraction, the projector remembers the whole
selected right inverse: equal projectors are equivalent to equal splittings. -/
theorem kernelProjector_eq_iff_rightInverse_eq
    (gamma : B →ₗ[R] S) (rightInv₁ rightInv₂ : S →ₗ[R] B)
    (rightInverse₁ : gamma.comp rightInv₁ =
      (LinearMap.id : S →ₗ[R] S)) :
    kernelProjector gamma rightInv₁ = kernelProjector gamma rightInv₂ ↔
      rightInv₁ = rightInv₂ := by
  constructor
  · intro hprojector
    ext s
    have hright := LinearMap.congr_fun rightInverse₁ s
    change gamma (rightInv₁ s) = s at hright
    have hpoint := LinearMap.congr_fun hprojector (rightInv₁ s)
    change rightInv₁ s - rightInv₁ (gamma (rightInv₁ s)) =
      rightInv₁ s - rightInv₂ (gamma (rightInv₁ s)) at hpoint
    rw [hright] at hpoint
    have hzero : rightInv₁ s - rightInv₂ s = 0 := by
      simpa using hpoint.symm
    exact sub_eq_zero.mp hzero
  · intro h
    rw [h]

/-- Distinct supplied splittings necessarily give distinct corrected
projectors. -/
theorem kernelProjector_ne_of_rightInverse_ne
    (gamma : B →ₗ[R] S) (rightInv₁ rightInv₂ : S →ₗ[R] B)
    (rightInverse₁ : gamma.comp rightInv₁ =
      (LinearMap.id : S →ₗ[R] S))
    (hne : rightInv₁ ≠ rightInv₂) :
    kernelProjector gamma rightInv₁ ≠ kernelProjector gamma rightInv₂ := by
  exact fun h => hne ((kernelProjector_eq_iff_rightInverse_eq
    gamma rightInv₁ rightInv₂ rightInverse₁).1 h)

/-- A map between observed carriers intertwines the split corrections when it
intertwines both contractions and their selected trace insertions. -/
theorem kernelProjector_natural
    (gamma : B →ₗ[R] S) (gamma' : B' →ₗ[R] S')
    (rightInv : S →ₗ[R] B) (rightInv' : S' →ₗ[R] B')
    (carrierMap : B →ₗ[R] B') (traceMap : S →ₗ[R] S')
    (contractionSquare : gamma'.comp carrierMap = traceMap.comp gamma)
    (splitSquare : carrierMap.comp rightInv = rightInv'.comp traceMap) :
    (kernelProjector gamma' rightInv').comp carrierMap =
      carrierMap.comp (kernelProjector gamma rightInv) := by
  ext b
  have hgamma := LinearMap.congr_fun contractionSquare b
  change gamma' (carrierMap b) = traceMap (gamma b) at hgamma
  have hsplit := LinearMap.congr_fun splitSquare (gamma b)
  change carrierMap (rightInv (gamma b)) =
    rightInv' (traceMap (gamma b)) at hsplit
  change carrierMap b - rightInv' (gamma' (carrierMap b)) =
    carrierMap (b - rightInv (gamma b))
  rw [hgamma, ← hsplit, map_sub]

/-- Corrected observation is natural across a commuting observation square
once the contraction and split squares are also supplied. -/
theorem correctedObservation_natural
    (gamma : B →ₗ[R] S) (gamma' : B' →ₗ[R] S')
    (rightInv : S →ₗ[R] B) (rightInv' : S' →ₗ[R] B')
    (observe : A →ₗ[R] B) (observe' : A →ₗ[R] B')
    (carrierMap : B →ₗ[R] B') (traceMap : S →ₗ[R] S')
    (observationSquare : carrierMap.comp observe = observe')
    (contractionSquare : gamma'.comp carrierMap = traceMap.comp gamma)
    (splitSquare : carrierMap.comp rightInv = rightInv'.comp traceMap) :
    carrierMap.comp (correctedObservation gamma observe rightInv) =
      correctedObservation gamma' observe' rightInv' := by
  rw [correctedObservation, correctedObservation]
  rw [← LinearMap.comp_assoc, ← kernelProjector_natural gamma gamma'
    rightInv rightInv' carrierMap traceMap contractionSquare splitSquare]
  rw [LinearMap.comp_assoc, observationSquare]

end SourceNativeCorrectedObservationNaturality
end GUFormalization
