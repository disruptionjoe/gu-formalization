import GUFormalization.GroupActionMackeyAdditivityBoundary
import Mathlib.Algebra.Category.ModuleCat.Adjunctions

/-!
# Free preadditive envelope of the supplied-action Mackey construction

Mathlib's `CategoryTheory.Free R C` keeps the objects of `C` and replaces each
hom-set by finitely supported `R`-linear combinations of the original
morphisms. It supplies the category, preadditive and linear structures, the
embedding of `C`, and the universal linear lift.

This file proves that functors and natural isomorphisms lift functorially
between free integer-linear envelopes and applies the result to the canonical
supplied-action Mackey natural isomorphism. It also identifies the exact fate
of the raw point-to-empty obstruction: the formerly empty hom-set becomes the
singleton zero group, but no original point-to-empty action map appears.

This is not a span or Burnside category. It adds formal sums of existing
morphisms but no span morphisms, restriction/transfer data, coproduct-as-sum
relations, double-coset transfer law, physical representation, source-native
action, or GU claim.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionAdditiveEnvelope

open CategoryTheory
open GroupActionMackeyCategory GroupActionMackeyAdditivityBoundary

noncomputable section

universe v₁ u₁

variable {C D : Type u₁} [Category.{v₁} C] [Category.{v₁} D]

/-- Lift a functor to the free integer-linear envelopes of its source and
target categories. -/
def freeFunctor (F : C ⥤ D) : Free ℤ C ⥤ Free ℤ D :=
  Free.lift ℤ (F ⋙ Free.embedding ℤ D)

instance freeFunctor_additive (F : C ⥤ D) : (freeFunctor F).Additive := by
  dsimp [freeFunctor]
  infer_instance

instance freeFunctor_linear (F : C ⥤ D) : (freeFunctor F).Linear ℤ := by
  dsimp [freeFunctor]
  infer_instance

set_option backward.isDefEq.respectTransparency false in
@[simp]
theorem freeFunctor_map_single (F : C ⥤ D) {X Y : C} (f : X ⟶ Y) (n : ℤ) :
    (freeFunctor F).map (Finsupp.single f n) =
      Finsupp.single (F.map f) n := by
  change
    (Free.lift ℤ (F ⋙ Free.embedding ℤ D)).map (Finsupp.single f n) =
      Finsupp.single (F.map f) n
  rw [Free.lift_map_single]
  change n • Finsupp.single (F.map f) 1 = Finsupp.single (F.map f) n
  rw [Finsupp.smul_single]
  simp

/-- The lifted functor agrees with `F` on objects. -/
@[simp]
theorem freeFunctor_obj (F : C ⥤ D) (X : C) :
    (freeFunctor F).obj (Free.of ℤ X) = Free.of ℤ (F.obj X) :=
  rfl

/-- A natural isomorphism lifts to the free integer-linear envelopes. -/
def freeNatIso {F G : C ⥤ D} (α : F ≅ G) : freeFunctor F ≅ freeFunctor G := by
  apply Free.ext ℤ
  exact
    (Free.embeddingLiftIso ℤ (F ⋙ Free.embedding ℤ D)).trans
      ((Functor.isoWhiskerRight α (Free.embedding ℤ D)).trans
        (Free.embeddingLiftIso ℤ (G ⋙ Free.embedding ℤ D)).symm)

universe u v

variable {G : Type u} [Group G]

/-- The canonical representative-free supplied-action Mackey decomposition,
lifted to a natural isomorphism between free preadditive envelopes. -/
def canonicalMackeyAdditiveEnvelopeNatIso (K H : Subgroup G) :
    freeFunctor (canonicalMackeyActionFunctor K H) ≅
      freeFunctor (restrictedInducedActionFunctor K H) :=
  freeNatIso (canonicalMackeyActionNatIso K H)

/-- The raw point-to-empty action hom-set is empty, so its free preadditive
envelope has exactly one morphism: the formal zero. Additivization removes the
hom-set obstruction without manufacturing an original action map. -/
theorem point_to_empty_envelope_subsingleton
    (H : Type u) [Group H] :
    Subsingleton
      (Free.of ℤ (pointAction H) ⟶ Free.of ℤ (emptyAction H)) := by
  change Subsingleton ((pointAction H ⟶ emptyAction H) →₀ ℤ)
  constructor
  intro f g
  apply Finsupp.ext
  intro a
  exact False.elim (no_point_to_empty H a)

/-- Every point-to-empty envelope morphism is therefore the zero morphism. -/
theorem point_to_empty_envelope_eq_zero
    (H : Type u) [Group H]
    (f : Free.of ℤ (pointAction H) ⟶ Free.of ℤ (emptyAction H)) :
    f = 0 :=
  (point_to_empty_envelope_subsingleton H).elim _ _

end

end GroupActionAdditiveEnvelope
end GUFormalization
