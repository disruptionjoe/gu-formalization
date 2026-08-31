import GUFormalization.SourceNativeActionObservationComplex

/-!
# Pairings on the candidate middle cohomology

This file isolates the exact algebraic obligations for a bilinear form on the
middle field carrier to descend through the actual cycle/gauge quotient. It
then proves that left or right nondegeneracy of the descended form is
equivalent to the corresponding radical among cycles containing no classes
beyond gauge images.

The result is deliberately conditional. It does not construct GU's source
action, analytic domain, real/Krein structure, conserved positive majorant,
probability rule, or physical state space.
-/

set_option autoImplicit false

namespace GUFormalization
namespace CandidateCohomologyPairing

open SourceNativeActionObservationComplex

universe u v0 v1 v2

variable {R : Type u} [CommRing R]
variable {C0 : Type v0} {C1 : Type v1} {C2 : Type v2}
variable [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup C2]
variable [Module R C0] [Module R C1] [Module R C2]

/-- Bilinear data on the field carrier that annihilate gauge images in both
arguments. -/
structure GaugeBasicPairing (C : ThreeStageComplex R C0 C1 C2) where
  pair : C1 →ₗ[R] C1 →ₗ[R] R
  leftGauge : ∀ (g : C0) (y : C1), pair (C.d0 g) y = 0
  rightGauge : ∀ (x : C1) (g : C0), pair x (C.d0 g) = 0

theorem GaugeBasicPairing.respectsCohomology
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) {x x' y y' : Cycle C}
    (hx : CohomologousCycles C x x')
    (hy : CohomologousCycles C y y') :
    P.pair x.1 y.1 = P.pair x'.1 y'.1 := by
  rcases hx with ⟨g, hg⟩
  rcases hy with ⟨h, hh⟩
  rw [hg, hh]
  simp [P.leftGauge, P.rightGauge]

/-- The pairing descended through both arguments of the actual middle-cycle
quotient. -/
def GaugeBasicPairing.descended
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) :
    CandidateCohomology C → CandidateCohomology C → R :=
  fun q r => Quotient.liftOn₂ q r
    (fun x y => P.pair x.1 y.1)
    (fun _ _ _ _ hx hy => P.respectsCohomology hx hy)

@[simp]
theorem GaugeBasicPairing.descended_mk
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) (x y : Cycle C) :
    P.descended (Quotient.mk _ x) (Quotient.mk _ y) = P.pair x.1 y.1 := rfl

/-- The zero middle cycle. -/
def zeroCycle (C : ThreeStageComplex R C0 C1 C2) : Cycle C :=
  ⟨0, by simp [IsCycle]⟩

/-- The distinguished zero class of the candidate quotient. -/
def zeroClass (C : ThreeStageComplex R C0 C1 C2) : CandidateCohomology C :=
  Quotient.mk _ (zeroCycle C)

/-- No left-radical cycle survives except a gauge image. -/
def LeftRadicalIsGauge
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) : Prop :=
  ∀ x : Cycle C, (∀ y : Cycle C, P.pair x.1 y.1 = 0) →
    ∃ g : C0, x.1 = C.d0 g

/-- No right-radical cycle survives except a gauge image. -/
def RightRadicalIsGauge
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) : Prop :=
  ∀ y : Cycle C, (∀ x : Cycle C, P.pair x.1 y.1 = 0) →
    ∃ g : C0, y.1 = C.d0 g

/-- Left nondegeneracy on quotient classes. -/
def LeftNondegenerateOnCohomology
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) : Prop :=
  ∀ q : CandidateCohomology C,
    (∀ r : CandidateCohomology C, P.descended q r = 0) →
    q = zeroClass C

/-- Right nondegeneracy on quotient classes. -/
def RightNondegenerateOnCohomology
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) : Prop :=
  ∀ r : CandidateCohomology C,
    (∀ q : CandidateCohomology C, P.descended q r = 0) →
    r = zeroClass C

/-- Left nondegeneracy of the descended form is exactly the statement that
the left radical on cycles is exhausted by gauge images. -/
theorem left_nondegenerate_iff_radical_is_gauge
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) :
    LeftNondegenerateOnCohomology P ↔ LeftRadicalIsGauge P := by
  constructor
  · intro hnondeg x hx
    have hclass : (Quotient.mk _ x : CandidateCohomology C) = zeroClass C := by
      apply hnondeg
      intro r
      induction r using Quotient.inductionOn with
      | _ y => exact hx y
    have hrel : CohomologousCycles C x (zeroCycle C) :=
      Quotient.exact hclass
    rcases hrel with ⟨g, hg⟩
    refine ⟨-g, ?_⟩
    calc
      x.1 = (x.1 + C.d0 g) + -(C.d0 g) := by simp [add_assoc]
      _ = (zeroCycle C).1 + -(C.d0 g) := by rw [← hg]
      _ = C.d0 (-g) := by simp [zeroCycle]
  · intro hrad q hq
    induction q using Quotient.inductionOn with
    | _ x =>
        rcases hrad x (fun y => hq (Quotient.mk _ y)) with ⟨g, hg⟩
        apply Quotient.sound
        refine ⟨-g, ?_⟩
        simp [hg, zeroCycle]

/-- Right nondegeneracy of the descended form is exactly the statement that
the right radical on cycles is exhausted by gauge images. -/
theorem right_nondegenerate_iff_radical_is_gauge
    {C : ThreeStageComplex R C0 C1 C2}
    (P : GaugeBasicPairing C) :
    RightNondegenerateOnCohomology P ↔ RightRadicalIsGauge P := by
  constructor
  · intro hnondeg y hy
    have hclass : (Quotient.mk _ y : CandidateCohomology C) = zeroClass C := by
      apply hnondeg
      intro q
      induction q using Quotient.inductionOn with
      | _ x => exact hy x
    have hrel : CohomologousCycles C y (zeroCycle C) :=
      Quotient.exact hclass
    rcases hrel with ⟨g, hg⟩
    refine ⟨-g, ?_⟩
    calc
      y.1 = (y.1 + C.d0 g) + -(C.d0 g) := by simp [add_assoc]
      _ = (zeroCycle C).1 + -(C.d0 g) := by rw [← hg]
      _ = C.d0 (-g) := by simp [zeroCycle]
  · intro hrad r hr
    induction r using Quotient.inductionOn with
    | _ y =>
        rcases hrad y (fun x => hr (Quotient.mk _ x)) with ⟨g, hg⟩
        apply Quotient.sound
        refine ⟨-g, ?_⟩
        simp [hg, zeroCycle]

end CandidateCohomologyPairing
end GUFormalization
