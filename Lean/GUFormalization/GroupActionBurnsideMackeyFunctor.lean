import GUFormalization.GroupActionBurnsideSpanMackey
import Mathlib.CategoryTheory.Preadditive.Yoneda.Basic

/-!
# The point-representable Mackey functor on finite supplied actions

The completed Burnside span category gives every finite supplied `G`-action
an additive group of morphisms from the trivial point action.  The additive
covariant Yoneda functor represented by that point is therefore a Mackey
functor on every object of the category.  For an equivariant map, its graph
induces transfer and its converse graph induces restriction.  Their separate
identity and composition laws follow from span composition, and the canonical
equivariant pullback square satisfies the Beck--Chevalley identity.

This is pure finite supplied-action algebra.  It constructs one representable
additive Mackey functor internal to the Burnside span category.  It does not
classify all Mackey functors or supply a physical representation, source-native
action, observed sector, selector, dynamics, prediction, or Geometric Unity
verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideMackeyFunctor

noncomputable section

open CategoryTheory
open CategoryTheory.Preadditive
open Opposite
open GroupActionBurnside
open GroupActionSpanCategory
open GroupActionBurnsideSpanCategory
open GroupActionBurnsideSpanMackey

universe u

variable (G : Type u) [Group G]

/-- The identity equivariant map of a finite supplied action. -/
def identityMap (A : FiniteAction.{u, u} G) : ActionMap G A A :=
  ⟨id, by intro _ _; rfl⟩

namespace RawSpan

variable {G} {A B C : FiniteAction.{u, u} G}

/-- Converse graphs reverse composition, up to the canonical pullback-apex
equivalence. -/
def converseGraphCompEquiv (f : ActionMap G A B) (g : ActionMap G B C) :
    GroupActionSpanCategory.RawSpan.Equiv
      (GroupActionSpanCategory.RawSpan.converseGraph
        (GroupActionSpanCategory.RawSpan.composeMap f g))
      (GroupActionSpanCategory.RawSpan.comp
        (GroupActionSpanCategory.RawSpan.converseGraph g)
        (GroupActionSpanCategory.RawSpan.converseGraph f)) where
  apexEquiv := {
    toEquiv := {
      toFun := fun a => ⟨(f.1 a, a), rfl⟩
      invFun := fun p => p.1.2
      left_inv := by intro a; rfl
      right_inv := by
        intro p
        apply Subtype.ext
        apply Prod.ext
        · exact p.2.symm
        · rfl
    }
    map_smul' := by
      intro h a
      apply Subtype.ext
      apply Prod.ext
      · exact f.2 h a
      · rfl
  }
  left_comm a := rfl
  right_comm a := rfl

/-- The canonical pullback of `f : B -> C` and `g : A -> C`. -/
abbrev pullbackAction (f : ActionMap G B C) (g : ActionMap G A C) :
    FiniteAction.{u, u} G :=
  GroupActionSpanCategory.RawSpan.pullbackAction
    (GroupActionSpanCategory.RawSpan.graph f)
    (GroupActionSpanCategory.RawSpan.converseGraph g)

/-- First projection from the canonical equivariant pullback. -/
def pullbackFst (f : ActionMap G B C) (g : ActionMap G A C) :
    ActionMap G (pullbackAction f g) B :=
  ⟨fun p => p.1.1, by intro h p; rfl⟩

/-- Second projection from the canonical equivariant pullback. -/
def pullbackSnd (f : ActionMap G B C) (g : ActionMap G A C) :
    ActionMap G (pullbackAction f g) A :=
  ⟨fun p => p.1.2, by intro h p; rfl⟩

/-- The graph/converse-graph composite across a pullback agrees with the
converse-first-projection/graph-second-projection composite. -/
def graphConversePullbackEquiv (f : ActionMap G B C) (g : ActionMap G A C) :
    GroupActionSpanCategory.RawSpan.Equiv
      (GroupActionSpanCategory.RawSpan.comp
        (GroupActionSpanCategory.RawSpan.graph f)
        (GroupActionSpanCategory.RawSpan.converseGraph g))
      (GroupActionSpanCategory.RawSpan.comp
        (GroupActionSpanCategory.RawSpan.converseGraph (pullbackFst f g))
        (GroupActionSpanCategory.RawSpan.graph (pullbackSnd f g))) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => ⟨(p, p), rfl⟩
      invFun := fun q => q.1.1
      left_inv := by intro p; rfl
      right_inv := by
        intro q
        apply Subtype.ext
        apply Prod.ext
        · rfl
        · exact q.2
    }
    map_smul' := by
      intro h p
      apply Subtype.ext
      apply Prod.ext <;> rfl
  }
  left_comm p := rfl
  right_comm p := rfl

end RawSpan

variable {G} {A B C : AdditiveBurnsideSpanObject G}

/-- Converse-graph generators reverse ordinary equivariant-map composition. -/
theorem converseGraph_composition (f : ActionMap G A B) (g : ActionMap G B C) :
    AdditiveBurnsideSpanObject.converseGraphHom (G := G)
        (RawSpan.composeMap f g) =
      AdditiveBurnsideSpanObject.converseGraphHom (G := G) g ≫
        AdditiveBurnsideSpanObject.converseGraphHom (G := G) f := by
  unfold AdditiveBurnsideSpanObject.converseGraphHom
    AdditiveBurnsideSpanObject.spanHom
  change BurnsideSpanHom.of _ = BurnsideSpanHom.comp _ _
  rw [BurnsideSpanHom.comp_of_of]
  exact congrArg BurnsideSpanHom.of
    (Quotient.sound ⟨RawSpan.converseGraphCompEquiv f g⟩)

/-- The graph/converse-graph Beck--Chevalley equality for the canonical
equivariant pullback square. -/
theorem graph_converse_pullback (f : ActionMap G B C) (g : ActionMap G A C) :
    AdditiveBurnsideSpanObject.graphHom (G := G) f ≫
        AdditiveBurnsideSpanObject.converseGraphHom (G := G) g =
      AdditiveBurnsideSpanObject.converseGraphHom (G := G)
          (RawSpan.pullbackFst f g) ≫
        AdditiveBurnsideSpanObject.graphHom (G := G)
          (RawSpan.pullbackSnd f g) := by
  unfold AdditiveBurnsideSpanObject.graphHom
    AdditiveBurnsideSpanObject.converseGraphHom
    AdditiveBurnsideSpanObject.spanHom
  change BurnsideSpanHom.comp _ _ = BurnsideSpanHom.comp _ _
  rw [BurnsideSpanHom.comp_of_of, BurnsideSpanHom.comp_of_of]
  exact congrArg BurnsideSpanHom.of
    (Quotient.sound ⟨RawSpan.graphConversePullbackEquiv f g⟩)

/-- The additive Mackey functor represented by the trivial point action.  Its
value on `A` is the additive group of completed spans `point G -> A`. -/
def pointMackeyFunctor (G : Type u) [Group G] :
    AdditiveBurnsideSpanObject G ⥤ AddCommGrpCat :=
  preadditiveCoyoneda.obj (op (point G))

instance pointMackeyFunctor_additive (G : Type u) [Group G] :
    Functor.Additive (pointMackeyFunctor G) :=
  by
    change Functor.Additive (preadditiveCoyoneda.obj (op (point G)))
    infer_instance

/-- Covariant transfer along an equivariant map, induced by its graph span. -/
def transfer {A B : AdditiveBurnsideSpanObject G} (f : ActionMap G A B) :
    (pointMackeyFunctor G).obj A ⟶ (pointMackeyFunctor G).obj B :=
  (pointMackeyFunctor G).map
    (AdditiveBurnsideSpanObject.graphHom (G := G) f)

/-- Contravariant restriction along an equivariant map, induced by its
converse graph span. -/
def restriction {A B : AdditiveBurnsideSpanObject G} (f : ActionMap G A B) :
    (pointMackeyFunctor G).obj B ⟶ (pointMackeyFunctor G).obj A :=
  (pointMackeyFunctor G).map
    (AdditiveBurnsideSpanObject.converseGraphHom (G := G) f)

/-- Transfer along the identity map is the identity homomorphism. -/
theorem transfer_identity (A : AdditiveBurnsideSpanObject G) :
    transfer (G := G) (identityMap G A) = 𝟙 ((pointMackeyFunctor G).obj A) := by
  unfold transfer
  change (pointMackeyFunctor G).map (𝟙 A) = _
  exact (pointMackeyFunctor G).map_id A

/-- Restriction along the identity map is the identity homomorphism. -/
theorem restriction_identity (A : AdditiveBurnsideSpanObject G) :
    restriction (G := G) (identityMap G A) =
      𝟙 ((pointMackeyFunctor G).obj A) := by
  unfold restriction
  change (pointMackeyFunctor G).map (𝟙 A) = _
  exact (pointMackeyFunctor G).map_id A

/-- Transfers preserve ordinary equivariant-map composition. -/
theorem transfer_composition {A B C : AdditiveBurnsideSpanObject G}
    (f : ActionMap G A B) (g : ActionMap G B C) :
    transfer (G := G) (RawSpan.composeMap f g) =
      transfer (G := G) f ≫ transfer (G := G) g := by
  unfold transfer
  rw [← (pointMackeyFunctor G).map_comp,
    AdditiveBurnsideSpanObject.graph_composition]

/-- Restrictions reverse ordinary equivariant-map composition. -/
theorem restriction_composition {A B C : AdditiveBurnsideSpanObject G}
    (f : ActionMap G A B) (g : ActionMap G B C) :
    restriction (G := G) (RawSpan.composeMap f g) =
      restriction (G := G) g ≫ restriction (G := G) f := by
  unfold restriction
  rw [← (pointMackeyFunctor G).map_comp, converseGraph_composition]

/-- Beck--Chevalley coherence for the canonical equivariant pullback square:
restriction after transfer equals transfer after restriction. -/
theorem restriction_transfer_eq_transfer_restriction
    {A B C : AdditiveBurnsideSpanObject G}
    (f : ActionMap G B C) (g : ActionMap G A C) :
    transfer (G := G) f ≫ restriction (G := G) g =
      restriction (G := G) (RawSpan.pullbackFst f g) ≫
        transfer (G := G) (RawSpan.pullbackSnd f g) := by
  unfold transfer restriction
  rw [← (pointMackeyFunctor G).map_comp,
    ← (pointMackeyFunctor G).map_comp,
    graph_converse_pullback]

/-- The all-object Mackey package: additive representability, separate
restriction/transfer functoriality, and pullback base change hold together. -/
theorem pointMackeyFunctor_laws
    {A B C : AdditiveBurnsideSpanObject G}
    (f : ActionMap G A B) (g : ActionMap G B C) (h : ActionMap G A C) :
    (transfer (G := G) (identityMap G A) = 𝟙 ((pointMackeyFunctor G).obj A)) ∧
      (restriction (G := G) (identityMap G A) =
        𝟙 ((pointMackeyFunctor G).obj A)) ∧
      (transfer (G := G) (RawSpan.composeMap f g) =
        transfer (G := G) f ≫ transfer (G := G) g) ∧
      (restriction (G := G) (RawSpan.composeMap f g) =
        restriction (G := G) g ≫ restriction (G := G) f) ∧
      (transfer (G := G) g ≫ restriction (G := G) h =
        restriction (G := G) (RawSpan.pullbackFst g h) ≫
          transfer (G := G) (RawSpan.pullbackSnd g h)) := by
  exact ⟨transfer_identity (G := G) A, restriction_identity (G := G) A,
    transfer_composition (G := G) f g,
    restriction_composition (G := G) f g,
    restriction_transfer_eq_transfer_restriction g h⟩

end

end GroupActionBurnsideMackeyFunctor
end GUFormalization
