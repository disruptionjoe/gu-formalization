import GUFormalization.CandidateCohomologyPairing

/-!
# Transport of candidate-cohomology pairings

This file proves that the left and right nondegeneracy criteria for a supplied
gauge-basic pairing do not depend on a chosen presentation of the candidate
cycle/gauge quotient, provided an explicit quotient equivalence preserves the
descended pairing and its zero class.

The equivalence and pairing preservation are supplied algebraic data.  They
are not a source-selected physical identification, analytic isometry, positive
completion, conservation law, or observable equivalence.
-/

set_option autoImplicit false

namespace GUFormalization
namespace CandidateCohomologyPairingTransport

open SourceNativeActionObservationComplex
open CandidateCohomologyPairing

universe u v0 v1 v2 w0 w1 w2

variable {R : Type u} [CommRing R]
variable {C0 : Type v0} {C1 : Type v1} {C2 : Type v2}
variable {D0 : Type w0} {D1 : Type w1} {D2 : Type w2}
variable [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup C2]
variable [AddCommGroup D0] [AddCommGroup D1] [AddCommGroup D2]
variable [Module R C0] [Module R C1] [Module R C2]
variable [Module R D0] [Module R D1] [Module R D2]

/-- An explicit equivalence between two candidate quotient presentations that
preserves the zero class and the supplied descended pairings. -/
structure PairingEquivalence
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    (P : GaugeBasicPairing C) (Q : GaugeBasicPairing D) where
  equiv : CandidateCohomology C ≃ CandidateCohomology D
  map_zero : equiv (zeroClass C) = zeroClass D
  preserves : ∀ x y : CandidateCohomology C,
    Q.descended (equiv x) (equiv y) = P.descended x y

/-- Pairing-preserving quotient equivalence is symmetric. -/
def PairingEquivalence.symm
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    {P : GaugeBasicPairing C} {Q : GaugeBasicPairing D}
    (E : PairingEquivalence P Q) : PairingEquivalence Q P where
  equiv := E.equiv.symm
  map_zero := by
    apply E.equiv.injective
    simp [E.map_zero]
  preserves := by
    intro x y
    rw [← E.preserves (E.equiv.symm x) (E.equiv.symm y)]
    simp

/-- Left nondegeneracy transports forward across a pairing-preserving
equivalence. -/
theorem PairingEquivalence.leftNondegenerate_forward
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    {P : GaugeBasicPairing C} {Q : GaugeBasicPairing D}
    (E : PairingEquivalence P Q)
    (hP : LeftNondegenerateOnCohomology P) :
    LeftNondegenerateOnCohomology Q := by
  intro q hq
  let x := E.equiv.symm q
  have hx : x = zeroClass C := by
    apply hP
    intro r
    rw [← E.preserves x r]
    simpa [x] using hq (E.equiv r)
  calc
    q = E.equiv x := by simp [x]
    _ = E.equiv (zeroClass C) := by rw [hx]
    _ = zeroClass D := E.map_zero

/-- Right nondegeneracy transports forward across a pairing-preserving
equivalence. -/
theorem PairingEquivalence.rightNondegenerate_forward
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    {P : GaugeBasicPairing C} {Q : GaugeBasicPairing D}
    (E : PairingEquivalence P Q)
    (hP : RightNondegenerateOnCohomology P) :
    RightNondegenerateOnCohomology Q := by
  intro q hq
  let x := E.equiv.symm q
  have hx : x = zeroClass C := by
    apply hP
    intro r
    rw [← E.preserves r x]
    simpa [x] using hq (E.equiv r)
  calc
    q = E.equiv x := by simp [x]
    _ = E.equiv (zeroClass C) := by rw [hx]
    _ = zeroClass D := E.map_zero

/-- Left nondegeneracy is invariant under pairing-preserving quotient
equivalence. -/
theorem PairingEquivalence.leftNondegenerate_iff
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    {P : GaugeBasicPairing C} {Q : GaugeBasicPairing D}
    (E : PairingEquivalence P Q) :
    LeftNondegenerateOnCohomology P ↔ LeftNondegenerateOnCohomology Q := by
  constructor
  · exact E.leftNondegenerate_forward
  · exact E.symm.leftNondegenerate_forward

/-- Right nondegeneracy is invariant under pairing-preserving quotient
equivalence. -/
theorem PairingEquivalence.rightNondegenerate_iff
    {C : ThreeStageComplex R C0 C1 C2}
    {D : ThreeStageComplex R D0 D1 D2}
    {P : GaugeBasicPairing C} {Q : GaugeBasicPairing D}
    (E : PairingEquivalence P Q) :
    RightNondegenerateOnCohomology P ↔ RightNondegenerateOnCohomology Q := by
  constructor
  · exact E.rightNondegenerate_forward
  · exact E.symm.rightNondegenerate_forward

end CandidateCohomologyPairingTransport
end GUFormalization
