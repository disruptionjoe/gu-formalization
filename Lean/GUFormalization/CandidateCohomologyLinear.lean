import GUFormalization.CandidateCohomologyPairingTransport
import Mathlib.LinearAlgebra.Quotient.Basic

/-!
# Linear presentation of candidate middle cohomology

The existing candidate cohomology is a representative quotient of middle
cycles by gauge equivalence.  This file constructs the canonical linear
presentation `ker d1 / range d0`, proves that its carrier is equivalent to the
existing quotient, and shows that every chain map induces the expected linear
map compatibly with the representative-level map.

This is algebraic cohomology for a supplied three-stage complex.  It does not
select the complex from a source action or construct an analytic domain,
positive state space, physical pairing, observable, probability rule, or
dynamics.
-/

set_option autoImplicit false

namespace GUFormalization
namespace CandidateCohomologyLinear

open SourceNativeActionObservationComplex

noncomputable section

universe u v0 v1 v2 w0 w1 w2

variable {R : Type u} [Ring R]
variable {C0 : Type v0} {C1 : Type v1} {C2 : Type v2}
variable {D0 : Type w0} {D1 : Type w1} {D2 : Type w2}
variable [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup C2]
variable [AddCommGroup D0] [AddCommGroup D1] [AddCommGroup D2]
variable [Module R C0] [Module R C1] [Module R C2]
variable [Module R D0] [Module R D1] [Module R D2]

/-- The middle-cycle module is the kernel of the equation map. -/
abbrev CycleModule (C : ThreeStageComplex R C0 C1 C2) :=
  LinearMap.ker C.d1

/-- The gauge differential with codomain restricted to middle cycles. -/
def gaugeToCycles (C : ThreeStageComplex R C0 C1 C2) :
    C0 →ₗ[R] CycleModule C :=
  C.d0.codRestrict (LinearMap.ker C.d1) fun g => gaugeImage_isCycle C g

@[simp]
theorem gaugeToCycles_val (C : ThreeStageComplex R C0 C1 C2) (g : C0) :
    (gaugeToCycles C g).1 = C.d0 g := rfl

/-- Gauge images as a submodule of the cycle module. -/
def gaugeSubmodule (C : ThreeStageComplex R C0 C1 C2) :
    Submodule R (CycleModule C) :=
  LinearMap.range (gaugeToCycles C)

/-- The canonical linear middle cohomology `ker d1 / range d0`. -/
abbrev LinearCandidateCohomology
    (C : ThreeStageComplex R C0 C1 C2) :=
  (CycleModule C) ⧸ gaugeSubmodule C

/-- Regard an existing cycle representative as an element of the kernel
submodule. -/
def cycleToModule (C : ThreeStageComplex R C0 C1 C2) :
    Cycle C → CycleModule C :=
  fun x => ⟨x.1, x.2⟩

/-- Regard an element of the kernel submodule as an existing cycle
representative. -/
def moduleToCycle (C : ThreeStageComplex R C0 C1 C2) :
    CycleModule C → Cycle C :=
  fun x => ⟨x.1, x.2⟩

@[simp]
theorem cycleToModule_moduleToCycle
    (C : ThreeStageComplex R C0 C1 C2) (x : CycleModule C) :
    cycleToModule C (moduleToCycle C x) = x := rfl

@[simp]
theorem moduleToCycle_cycleToModule
    (C : ThreeStageComplex R C0 C1 C2) (x : Cycle C) :
    moduleToCycle C (cycleToModule C x) = x := rfl

/-- Send a representative cycle class to the same representative in the
canonical module quotient. -/
def toLinearCandidate
    (C : ThreeStageComplex R C0 C1 C2) :
    CandidateCohomology C → LinearCandidateCohomology C :=
  Quotient.lift
    (fun x => Submodule.Quotient.mk (cycleToModule C x))
    (by
      intro x y hxy
      apply (Submodule.Quotient.eq (gaugeSubmodule C)).2
      rcases hxy with ⟨g, hg⟩
      refine ⟨-g, ?_⟩
      apply Subtype.ext
      change C.d0 (-g) = x.1 - y.1
      rw [hg]
      simp)

@[simp]
theorem toLinearCandidate_mk
    (C : ThreeStageComplex R C0 C1 C2) (x : Cycle C) :
    toLinearCandidate C (Quotient.mk _ x) =
      Submodule.Quotient.mk (cycleToModule C x) := rfl

/-- Equality in the linear quotient implies the original representative-level
gauge equivalence. -/
theorem toLinearCandidate_injective
    (C : ThreeStageComplex R C0 C1 C2) :
    Function.Injective (toLinearCandidate C) := by
  intro q r hqr
  induction q using Quotient.inductionOn with
  | _ x =>
      induction r using Quotient.inductionOn with
      | _ y =>
          apply Quotient.sound
          have hmem := (Submodule.Quotient.eq (gaugeSubmodule C)).1 hqr
          rcases hmem with ⟨g, hg⟩
          have hgval : C.d0 g = x.1 - y.1 :=
            congrArg Subtype.val hg
          refine ⟨-g, ?_⟩
          calc
            y.1 = x.1 - (x.1 - y.1) := by abel
            _ = x.1 - C.d0 g := by rw [← hgval]
            _ = x.1 + C.d0 (-g) := by simp only [map_neg, sub_eq_add_neg]

/-- Every linear quotient class has an existing representative quotient
class. -/
theorem toLinearCandidate_surjective
    (C : ThreeStageComplex R C0 C1 C2) :
    Function.Surjective (toLinearCandidate C) := by
  intro q
  obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective
    (gaugeSubmodule C) q
  exact ⟨Quotient.mk _ (moduleToCycle C x), rfl⟩

/-- The old cycle/gauge quotient and the canonical linear quotient have the
same carrier, with no extra representatives or identifications. -/
def candidateCohomologyEquivLinear
    (C : ThreeStageComplex R C0 C1 C2) :
    CandidateCohomology C ≃ LinearCandidateCohomology C :=
  Equiv.ofBijective (toLinearCandidate C)
    ⟨toLinearCandidate_injective C, toLinearCandidate_surjective C⟩

@[simp]
theorem candidateCohomologyEquivLinear_mk
    (C : ThreeStageComplex R C0 C1 C2) (x : Cycle C) :
    candidateCohomologyEquivLinear C (Quotient.mk _ x) =
      Submodule.Quotient.mk (cycleToModule C x) := rfl

/-- A chain map restricts linearly to the middle-cycle modules. -/
def cycleLinearMap
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) : CycleModule C →ₗ[R] CycleModule D :=
  (f.f1.domRestrict (LinearMap.ker C.d1)).codRestrict
    (LinearMap.ker D.d1) fun x => f.mapsCycle x.2

@[simp]
theorem cycleLinearMap_val
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (x : CycleModule C) :
    (cycleLinearMap f x).1 = f.f1 x.1 := rfl

/-- The cycle map sends each gauge image to the gauge image of the chain
map's degree-zero component. -/
theorem cycleLinearMap_gauge
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (g : C0) :
    cycleLinearMap f (gaugeToCycles C g) =
      gaugeToCycles D (f.f0 g) := by
  apply Subtype.ext
  exact LinearMap.congr_fun f.left g

/-- A chain map carries the gauge submodule into the target gauge
submodule. -/
theorem gaugeSubmodule_le_comap
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) :
    gaugeSubmodule C ≤ Submodule.comap (cycleLinearMap f) (gaugeSubmodule D) := by
  intro x hx
  rcases hx with ⟨g, rfl⟩
  change cycleLinearMap f (gaugeToCycles C g) ∈ gaugeSubmodule D
  exact ⟨f.f0 g, (cycleLinearMap_gauge f g).symm⟩

/-- Every chain map induces a linear map on the canonical cohomology module. -/
def linearCohomologyMap
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) :
    LinearCandidateCohomology C →ₗ[R] LinearCandidateCohomology D :=
  (gaugeSubmodule C).mapQ (gaugeSubmodule D) (cycleLinearMap f)
    (gaugeSubmodule_le_comap f)

@[simp]
theorem linearCohomologyMap_mk
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (x : CycleModule C) :
    linearCohomologyMap f (Submodule.Quotient.mk x) =
      Submodule.Quotient.mk (cycleLinearMap f x) := by
  exact Submodule.mapQ_apply _ _ _ _

/-- The existing representative-level cohomology map is exactly the carrier
map underlying the induced linear quotient map. -/
theorem linearCohomologyMap_compatible
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (f : ChainMap C D) (q : CandidateCohomology C) :
    linearCohomologyMap f (toLinearCandidate C q) =
      toLinearCandidate D (f.cohomologyMap q) := by
  induction q using Quotient.inductionOn with
  | _ x => rfl

end

end CandidateCohomologyLinear
end GUFormalization
