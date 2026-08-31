import Mathlib

/-!
# A supplied linear involution exchanges anticommuting chirality sectors

This module isolates the algebraic real-sector statement used by the
source-native `Spin(6,4)` analysis.  If a supplied `R`-linear involution
modeling conjugation anticommutes with a supplied chirality involution, it
exchanges the positive and negative chirality kernels and does so bijectively.

The premises do not construct a scalar-antilinear real structure or Clifford
representation, or identify either eigenspace with a physical family or
observed chirality sector.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeRealSector

universe u v

variable {R : Type u} [Ring R]
variable {S : Type v} [AddCommGroup S] [Module R S]

/-- Positive chirality as the kernel of `chi - 1`. -/
def plusSector (chi : S →ₗ[R] S) : Submodule R S :=
  LinearMap.ker (chi - LinearMap.id)

/-- Negative chirality as the kernel of `chi + 1`. -/
def minusSector (chi : S →ₗ[R] S) : Submodule R S :=
  LinearMap.ker (chi + LinearMap.id)

theorem mem_plusSector_iff (chi : S →ₗ[R] S) (s : S) :
    s ∈ plusSector chi ↔ chi s = s := by
  simp [plusSector, sub_eq_zero]

theorem mem_minusSector_iff (chi : S →ₗ[R] S) (s : S) :
    s ∈ minusSector chi ↔ chi s = -s := by
  simp [minusSector, add_eq_zero_iff_eq_neg]

/-- Anticommutation sends every positive-chirality vector to negative
chirality under conjugation. -/
theorem conjugation_maps_plus_to_minus
    (chi conj : S →ₗ[R] S)
    (anticommutes : chi.comp conj = -(conj.comp chi))
    {s : S} (hs : s ∈ plusSector chi) : conj s ∈ minusSector chi := by
  rw [mem_minusSector_iff]
  have hanti := LinearMap.congr_fun anticommutes s
  have hplus := (mem_plusSector_iff chi s).mp hs
  simpa [hplus] using hanti

/-- Anticommutation sends every negative-chirality vector to positive
chirality under conjugation. -/
theorem conjugation_maps_minus_to_plus
    (chi conj : S →ₗ[R] S)
    (anticommutes : chi.comp conj = -(conj.comp chi))
    {s : S} (hs : s ∈ minusSector chi) : conj s ∈ plusSector chi := by
  rw [mem_plusSector_iff]
  have hanti := LinearMap.congr_fun anticommutes s
  have hminus := (mem_minusSector_iff chi s).mp hs
  simpa [hminus] using hanti

/-- Conjugation restricted from the positive to the negative sector. -/
def conjugationPlusToMinus (chi conj : S →ₗ[R] S)
    (anticommutes : chi.comp conj = -(conj.comp chi)) :
    plusSector chi →ₗ[R] minusSector chi :=
  (conj.domRestrict (plusSector chi)).codRestrict (minusSector chi)
    (fun s => conjugation_maps_plus_to_minus chi conj anticommutes s.property)

/-- Conjugation restricted from the negative to the positive sector. -/
def conjugationMinusToPlus (chi conj : S →ₗ[R] S)
    (anticommutes : chi.comp conj = -(conj.comp chi)) :
    minusSector chi →ₗ[R] plusSector chi :=
  (conj.domRestrict (minusSector chi)).codRestrict (plusSector chi)
    (fun s => conjugation_maps_minus_to_plus chi conj anticommutes s.property)

/-- A supplied involutive linear model of conjugation makes the two chirality
sectors linearly equivalent; neither is thereby a physical real sector. -/
def conjugationSectorEquiv (chi conj : S →ₗ[R] S)
    (anticommutes : chi.comp conj = -(conj.comp chi))
    (involutive : conj.comp conj = (LinearMap.id : S →ₗ[R] S)) :
    plusSector chi ≃ₗ[R] minusSector chi where
  toLinearMap := conjugationPlusToMinus chi conj anticommutes
  invFun := conjugationMinusToPlus chi conj anticommutes
  left_inv s := by
    apply Subtype.ext
    exact LinearMap.congr_fun involutive s
  right_inv s := by
    apply Subtype.ext
    exact LinearMap.congr_fun involutive s

end SourceNativeRealSector
end GUFormalization
