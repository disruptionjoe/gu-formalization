import GUFormalization.GroupActionBurnsideAdditiveCoend

/-!
# Additive co-Yoneda for Burnside restriction correspondences

The all-middle additive coend is identified with the represented iterated
restriction-correspondence hom group.  Composition is the forward additive
map.  Its explicit inverse inserts a correspondence at the canonical middle
object `Res_psi C` and uses the identity correspondence as the second leg.

This is a hom-group co-Yoneda equivalence for the supplied restriction
functors.  It is not a construction of 2-morphisms, a biset bicategory,
ambidexterity, a Mackey 2-functor, or a physical/source realization.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideCoYoneda

noncomputable section

open CategoryTheory
open GroupActionBurnside
open GroupActionBurnsideSpanCategory
open GroupActionBurnsideSpanRestriction
open GroupActionBurnsideSpanCorrespondence
open GroupActionBurnsideSpanCorrespondenceComposition
open GroupActionBurnsideBisetCoend
open GroupActionBurnsideAdditiveCoend

universe u

variable {H K L : Type u} [Group H] [Group K] [Group L]

/-- The canonical all-middle pair representing an already-composed
correspondence. -/
def canonicalPair (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L}
    (t : IteratedRestrictionCorrespondence phi psi A C) :
    AllMiddlePair phi psi A C :=
  ⟨(restrictionFunctor psi).obj C, t, 𝟙 _⟩

/-- The left-additivity relation is visible as the corresponding equality of
coend generators. -/
theorem coendGenerator_add_left
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L}
    (B : AdditiveBurnsideSpanObject K)
    (x x' : RestrictionCorrespondence phi A B)
    (y : RestrictionCorrespondence psi B C) :
    coendGenerator phi psi (⟨B, x + x', y⟩ : AllMiddlePair phi psi A C) =
      coendGenerator phi psi ⟨B, x, y⟩ +
        coendGenerator phi psi ⟨B, x', y⟩ := by
  change QuotientAddGroup.mk' (additiveCoendRelations phi psi A C)
      (FreeAbelianGroup.of (⟨B, x + x', y⟩ : AllMiddlePair phi psi A C)) =
    QuotientAddGroup.mk' (additiveCoendRelations phi psi A C)
      (FreeAbelianGroup.of (⟨B, x, y⟩ : AllMiddlePair phi psi A C) +
        FreeAbelianGroup.of (⟨B, x', y⟩ : AllMiddlePair phi psi A C))
  apply (QuotientAddGroup.eq_iff_sub_mem).2
  change FreeAbelianGroup.of
      (⟨B, x + x', y⟩ : AllMiddlePair phi psi A C) -
        (FreeAbelianGroup.of (⟨B, x, y⟩ : AllMiddlePair phi psi A C) +
          FreeAbelianGroup.of (⟨B, x', y⟩ : AllMiddlePair phi psi A C)) ∈
    AddSubgroup.closure (AdditiveCoendRelation phi psi A C)
  simpa [sub_eq_add_neg, add_assoc, add_comm,
    add_left_comm] using
    (AddSubgroup.subset_closure
      (AdditiveCoendRelation.left_add B x x' y))

/-- The canonical generator with zero first leg is zero in the additive
coend. -/
theorem coendGenerator_zero_left
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L}
    (B : AdditiveBurnsideSpanObject K)
    (y : RestrictionCorrespondence psi B C) :
    coendGenerator phi psi
      (⟨B, 0, y⟩ : AllMiddlePair phi psi A C) = 0 := by
  change QuotientAddGroup.mk' (additiveCoendRelations phi psi A C)
      (FreeAbelianGroup.of (⟨B, 0, y⟩ : AllMiddlePair phi psi A C)) = 0
  apply (QuotientAddGroup.eq_zero_iff _).2
  have hneg := AddSubgroup.subset_closure
    (AdditiveCoendRelation.left_add B
      (0 : RestrictionCorrespondence phi A B) 0 y)
  simpa [additiveCoendRelations] using
    (AddSubgroup.neg_mem (AddSubgroup.closure
      {z | AdditiveCoendRelation phi psi A C z}) hneg)

/-- Insert an iterated correspondence at the canonical middle object with an
identity second leg. -/
def coYonedaSection
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L} :
    IteratedRestrictionCorrespondence phi psi A C →+
      AdditiveBalancedCoend phi psi A C where
  toFun t := coendGenerator phi psi (canonicalPair phi psi t)
  map_zero' := coendGenerator_zero_left phi psi _ _
  map_add' t t' := coendGenerator_add_left phi psi _ t t' _

/-- Every generator is equal to the canonical identity-leg generator of its
composite.  This is the representative-level co-Yoneda equation. -/
theorem coYonedaSection_compose_generator
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L}
    (p : AllMiddlePair phi psi A C) :
    coYonedaSection phi psi (compose phi psi p.first p.second) =
      coendGenerator phi psi p := by
  rcases p with ⟨B, x, y⟩
  change QuotientAddGroup.mk' (additiveCoendRelations phi psi A C)
      (FreeAbelianGroup.of
        (canonicalPair phi psi (compose phi psi x y))) =
    QuotientAddGroup.mk' (additiveCoendRelations phi psi A C)
      (FreeAbelianGroup.of (⟨B, x, y⟩ : AllMiddlePair phi psi A C))
  apply (QuotientAddGroup.eq_iff_sub_mem).2
  change FreeAbelianGroup.of
      (canonicalPair phi psi (compose phi psi x y)) -
        FreeAbelianGroup.of (⟨B, x, y⟩ : AllMiddlePair phi psi A C) ∈
    AddSubgroup.closure (AdditiveCoendRelation phi psi A C)
  simpa [canonicalPair, compose, rightAction,
    leftAction] using
    (AddSubgroup.subset_closure
      (AdditiveCoendRelation.balance B
        ((restrictionFunctor psi).obj C) x y (𝟙 _)))

/-- Composition after the canonical section is the identity. -/
theorem additiveBalancedCompose_comp_coYonedaSection
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L} :
    (additiveBalancedCompose phi psi).comp (coYonedaSection phi psi) =
      AddMonoidHom.id (IteratedRestrictionCorrespondence phi psi A C) := by
  apply AddMonoidHom.ext
  intro t
  simp [coYonedaSection, canonicalPair, compose]

/-- The canonical section after composition is the identity on the additive
coend. -/
theorem coYonedaSection_comp_additiveBalancedCompose
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L} :
    (coYonedaSection phi psi).comp (additiveBalancedCompose phi psi) =
      AddMonoidHom.id (AdditiveBalancedCoend phi psi A C) := by
  let q := QuotientAddGroup.mk' (additiveCoendRelations phi psi A C)
  have hfree :
      ((coYonedaSection phi psi).comp
          (additiveBalancedCompose phi psi)).comp q =
        (AddMonoidHom.id (AdditiveBalancedCoend phi psi A C)).comp q := by
    apply FreeAbelianGroup.lift_ext
    intro p
    change coYonedaSection phi psi
        (additiveBalancedCompose phi psi (coendGenerator phi psi p)) =
      coendGenerator phi psi p
    rw [additiveBalancedCompose_generator]
    exact coYonedaSection_compose_generator phi psi p
  apply AddMonoidHom.ext
  intro z
  obtain ⟨a, rfl⟩ := QuotientAddGroup.mk'_surjective
    (additiveCoendRelations phi psi A C) z
  exact DFunLike.congr_fun hfree a

/-- Additive co-Yoneda: the all-middle additive coend is additively
equivalent to the actual iterated restriction-correspondence hom group. -/
def additiveCoYonedaEquiv
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L} :
    AdditiveBalancedCoend phi psi A C ≃+
      IteratedRestrictionCorrespondence phi psi A C :=
  AddEquiv.ofBijective (additiveBalancedCompose phi psi) (by
    have hleft : Function.LeftInverse
        (coYonedaSection phi psi (A := A) (C := C))
        (additiveBalancedCompose phi psi) := by
      intro z
      exact DFunLike.congr_fun
        (coYonedaSection_comp_additiveBalancedCompose phi psi
          (A := A) (C := C)) z
    have hright : Function.RightInverse
        (coYonedaSection phi psi (A := A) (C := C))
        (additiveBalancedCompose phi psi) := by
      intro t
      exact DFunLike.congr_fun
        (additiveBalancedCompose_comp_coYonedaSection phi psi
          (A := A) (C := C)) t
    exact ⟨hleft.injective, hright.surjective⟩)

@[simp]
theorem additiveCoYonedaEquiv_generator
    (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {C : AdditiveBurnsideSpanObject L}
    (p : AllMiddlePair phi psi A C) :
    additiveCoYonedaEquiv phi psi (coendGenerator phi psi p) =
      compose phi psi p.first p.second := by
  change additiveBalancedCompose phi psi (coendGenerator phi psi p) = _
  exact additiveBalancedCompose_generator phi psi p

end

end GroupActionBurnsideCoYoneda
end GUFormalization
