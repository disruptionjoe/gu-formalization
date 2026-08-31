import GUFormalization.SourceCoefficientRank
import GUFormalization.SourceNativeCorrectedObservationNaturality

/-!
# A minimal action--observation complex

This file formalizes the smallest linear complex that can carry a gauge
quotient at a field stage, and the exact conditions under which a supplied
split-corrected observation descends through it.  The three stages are

`gauge --d0--> field --d1--> equation`, with `d1 ∘ d0 = 0`.

This is a conditional mathematical interface.  It does not construct the
source action, select the two owner coefficients, choose a Clifford splitting,
provide analytic domains or a positive pairing, or identify the resulting
cycle quotient as a physical state space.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeActionObservationComplex

open SourceCoefficientRank
open SourceNativeCorrectedObservation

universe u v0 v1 v2 w0 w1 w2 x

variable {R : Type u} [Ring R]
variable {C0 : Type v0} {C1 : Type v1} {C2 : Type v2}
variable {D0 : Type w0} {D1 : Type w1} {D2 : Type w2}
variable {S : Type x}
variable [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup C2]
variable [AddCommGroup D0] [AddCommGroup D1] [AddCommGroup D2]
variable [AddCommGroup S]
variable [Module R C0] [Module R C1] [Module R C2]
variable [Module R D0] [Module R D1] [Module R D2]
variable [Module R S]

/-- The smallest linear action complex with a gauge stage, a field stage and
an equation stage. -/
structure ThreeStageComplex
    (R : Type u) [Ring R]
    (C0 : Type v0) (C1 : Type v1) (C2 : Type v2)
    [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup C2]
    [Module R C0] [Module R C1] [Module R C2] where
  d0 : C0 →ₗ[R] C1
  d1 : C1 →ₗ[R] C2
  zero : d1.comp d0 = 0

/-- A middle-stage cycle is a field killed by the equation map. -/
def IsCycle (C : ThreeStageComplex R C0 C1 C2) (x : C1) : Prop :=
  C.d1 x = 0

/-- Two fields are gauge-equivalent when their difference is a gauge image.
This relation is the representative-level interface for middle cohomology. -/
def Cohomologous (C : ThreeStageComplex R C0 C1 C2) (x y : C1) : Prop :=
  ∃ g : C0, y = x + C.d0 g

theorem cohomologous_refl
    (C : ThreeStageComplex R C0 C1 C2) (x : C1) :
    Cohomologous C x x := by
  exact ⟨0, by simp⟩

theorem cohomologous_symm
    (C : ThreeStageComplex R C0 C1 C2) {x y : C1}
    (hxy : Cohomologous C x y) : Cohomologous C y x := by
  rcases hxy with ⟨g, rfl⟩
  refine ⟨-g, ?_⟩
  simp

theorem cohomologous_trans
    (C : ThreeStageComplex R C0 C1 C2) {x y z : C1}
    (hxy : Cohomologous C x y) (hyz : Cohomologous C y z) :
    Cohomologous C x z := by
  rcases hxy with ⟨g, rfl⟩
  rcases hyz with ⟨h, rfl⟩
  refine ⟨g + h, ?_⟩
  simp [add_assoc]

/-- Gauge equivalence as an actual equivalence relation on the field stage. -/
def cohomologySetoid (C : ThreeStageComplex R C0 C1 C2) : Setoid C1 where
  r := Cohomologous C
  iseqv := ⟨cohomologous_refl C, cohomologous_symm C,
    cohomologous_trans C⟩

/-- The algebraic middle quotient.  Its physical interpretation remains an
extra ownership/domain/pairing obligation. -/
abbrev CandidateCohomology (C : ThreeStageComplex R C0 C1 C2) :=
  Quotient (cohomologySetoid C)

/-- Every gauge image is a cycle. -/
theorem gaugeImage_isCycle
    (C : ThreeStageComplex R C0 C1 C2) (g : C0) :
    IsCycle C (C.d0 g) := by
  have h := LinearMap.congr_fun C.zero g
  simpa [IsCycle] using h

/-- A map of three-stage complexes consists exactly of the two chain squares. -/
structure ChainMap
    (C : ThreeStageComplex R C0 C1 C2)
    (D : ThreeStageComplex R D0 D1 D2) where
  f0 : C0 →ₗ[R] D0
  f1 : C1 →ₗ[R] D1
  f2 : C2 →ₗ[R] D2
  left : f1.comp C.d0 = D.d0.comp f0
  right : D.d1.comp f1 = f2.comp C.d1

/-- A chain map sends cycles to cycles. -/
theorem ChainMap.mapsCycle
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) {x : C1} (hx : IsCycle C x) :
    IsCycle D (f.f1 x) := by
  have h := LinearMap.congr_fun f.right x
  change D.d1 (f.f1 x) = f.f2 (C.d1 x) at h
  change C.d1 x = 0 at hx
  change D.d1 (f.f1 x) = 0
  calc
    D.d1 (f.f1 x) = f.f2 (C.d1 x) := h
    _ = 0 := by rw [hx, map_zero]

/-- A chain map respects gauge equivalence, so its middle map is well-defined
on cycle classes whenever the representative quotient is formed. -/
theorem ChainMap.mapsCohomologous
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) {x y : C1} (hxy : Cohomologous C x y) :
    Cohomologous D (f.f1 x) (f.f1 y) := by
  rcases hxy with ⟨g, rfl⟩
  refine ⟨f.f0 g, ?_⟩
  rw [map_add]
  have h := LinearMap.congr_fun f.left g
  change f.f1 (C.d0 g) = D.d0 (f.f0 g) at h
  rw [h]

/-- A chain map induces a map of the candidate middle quotients. -/
def ChainMap.cohomologyMap
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) : CandidateCohomology C → CandidateCohomology D :=
  Quotient.map f.f1 (fun _ _ hxy => f.mapsCohomologous hxy)

/-- Correct only the field-stage component of a supplied observation chain
map by the selected Clifford-kernel projector. -/
def correctedMiddle
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (gamma : D1 →ₗ[R] S) (rightInv : S →ₗ[R] D1) :
    C1 →ₗ[R] D1 :=
  correctedObservation gamma f.f1 rightInv

/-- The corrected middle observation is a chain map exactly after supplying
the two action--projector compatibility laws: the projector fixes observed
gauge images, and the observed equation map is insensitive to the removed
trace direction. -/
def correctedChainMap
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (gamma : D1 →ₗ[R] S) (rightInv : S →ₗ[R] D1)
    (fixesGaugeImage :
      (kernelProjector gamma rightInv).comp D.d0 = D.d0)
    (equationIgnoresTrace :
      D.d1.comp (kernelProjector gamma rightInv) = D.d1) :
    ChainMap C D where
  f0 := f.f0
  f1 := correctedMiddle f gamma rightInv
  f2 := f.f2
  left := by
    rw [correctedMiddle, correctedObservation, LinearMap.comp_assoc,
      f.left, ← LinearMap.comp_assoc, fixesGaugeImage]
  right := by
    rw [correctedMiddle, correctedObservation, ← LinearMap.comp_assoc,
      equationIgnoresTrace, f.right]

/-- With a genuine right inverse, every corrected observed field is in the
observed Clifford kernel. -/
theorem gamma_correctedMiddle
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (gamma : D1 →ₗ[R] S) (rightInv : S →ₗ[R] D1)
    (rightInverse : gamma.comp rightInv = (LinearMap.id : S →ₗ[R] S))
    (x : C1) :
    gamma (correctedMiddle f gamma rightInv x) = 0 := by
  exact gamma_correctedObservation gamma f.f1 rightInv rightInverse x

/-- Under the compatibility laws, corrected observation sends action cycles
to observed cycles. -/
theorem corrected_mapsCycle
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (gamma : D1 →ₗ[R] S) (rightInv : S →ₗ[R] D1)
    (fixesGaugeImage :
      (kernelProjector gamma rightInv).comp D.d0 = D.d0)
    (equationIgnoresTrace :
      D.d1.comp (kernelProjector gamma rightInv) = D.d1)
    {x : C1} (hx : IsCycle C x) :
    IsCycle D (correctedMiddle f gamma rightInv x) := by
  exact (correctedChainMap f gamma rightInv fixesGaugeImage
    equationIgnoresTrace).mapsCycle hx

/-- Under the same laws, corrected observation respects gauge equivalence and
therefore descends to the candidate middle cohomology quotient. -/
theorem corrected_mapsCohomologous
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (gamma : D1 →ₗ[R] S) (rightInv : S →ₗ[R] D1)
    (fixesGaugeImage :
      (kernelProjector gamma rightInv).comp D.d0 = D.d0)
    (equationIgnoresTrace :
      D.d1.comp (kernelProjector gamma rightInv) = D.d1)
    {x y : C1} (hxy : Cohomologous C x y) :
    Cohomologous D (correctedMiddle f gamma rightInv x)
      (correctedMiddle f gamma rightInv y) := by
  exact (correctedChainMap f gamma rightInv fixesGaugeImage
    equationIgnoresTrace).mapsCohomologous hxy

/-- The action--observation weld therefore supplies an actual map on the
candidate middle quotient. -/
def correctedCohomologyMap
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (gamma : D1 →ₗ[R] S) (rightInv : S →ₗ[R] D1)
    (fixesGaugeImage :
      (kernelProjector gamma rightInv).comp D.d0 = D.d0)
    (equationIgnoresTrace :
      D.d1.comp (kernelProjector gamma rightInv) = D.d1) :
    CandidateCohomology C → CandidateCohomology D :=
  (correctedChainMap f gamma rightInv fixesGaugeImage
    equationIgnoresTrace).cohomologyMap

/-- Packet-relative uniqueness of an action family would mean that every two
strict-source coefficient solutions instantiate the same action object. -/
def StrictSourceSelectsUniqueAction
    {K A : Type*} [Field K]
    (actionFamily : OwnerSpace K → A) : Prop :=
  ∀ x y, strictSourceConstraint K x = 0 →
    strictSourceConstraint K y = 0 → actionFamily x = actionFamily y

/-- If distinct owner coefficients give distinct action objects, the frozen
strict source packet cannot select a unique member of that action family. -/
theorem strictSource_does_not_select_injective_actionFamily
    {K A : Type*} [Field K]
    (actionFamily : OwnerSpace K → A)
    (injective : Function.Injective actionFamily) :
    ¬ StrictSourceSelectsUniqueAction actionFamily := by
  intro hselects
  apply owner_axes_distinct K
  apply injective
  exact hselects (owner54Axis K) (owner210Axis K)
    (strictSource_owner54_solution K) (strictSource_owner210_solution K)

end SourceNativeActionObservationComplex
end GUFormalization
