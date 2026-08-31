import GUFormalization.GroupActionBurnsideSpanRestriction

/-!
# The additive restriction correspondence for Burnside spans

For a supplied group homomorphism `H -> K`, categorical restriction gives an
additive functor from completed `K`-Burnside spans to completed `H`-Burnside
spans.  Its companion correspondence is

`P(A,B) = Hom_H(A, Res(B))`.

Precomposition by an `H`-span and postcomposition by a restricted `K`-span
give commuting additive actions.  For subgroup inclusion, the ordinary
set-action induction/restriction adjunction sends induced equivariant maps to
graph generators in this correspondence.

This is the correctly typed induction direction at the present categorical
ceiling.  It is not an induction functor on span categories: ordinary
induction need not preserve the pullbacks used for span composition.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideSpanCorrespondence

noncomputable section

open CategoryTheory
open GroupActionBurnside
open GroupActionInduction
open GroupActionSpanCategory
open GroupActionBurnsideSpanCategory
open GroupActionBurnsideSpanRestriction

universe u

variable {H K G : Type u} [Group H] [Group K] [Group G]

/-- The additive restriction companion from the `H`-Burnside span category to
the `K`-Burnside span category. -/
abbrev RestrictionCorrespondence (phi : H →* K)
    (A : AdditiveBurnsideSpanObject H)
    (B : AdditiveBurnsideSpanObject K) :=
  A ⟶ (restrictionFunctor phi).obj B

/-- Contravariant action of an `H`-span by precomposition. -/
def leftAction (phi : H →* K)
    {A A' : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K} (f : A' ⟶ A) :
    RestrictionCorrespondence phi A B →+
      RestrictionCorrespondence phi A' B where
  toFun x := f ≫ x
  map_zero' :=
    (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compRightHom f).map_zero
  map_add' x y :=
    (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compRightHom f).map_add x y

/-- Covariant action of a `K`-span after applying categorical restriction. -/
def rightAction (phi : H →* K)
    {A : AdditiveBurnsideSpanObject H}
    {B B' : AdditiveBurnsideSpanObject K} (g : B ⟶ B') :
    RestrictionCorrespondence phi A B →+
      RestrictionCorrespondence phi A B' where
  toFun x := x ≫ (restrictionFunctor phi).map g
  map_zero' :=
    (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compLeftHom
      ((restrictionFunctor phi).map g)).map_zero
  map_add' x y :=
    (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compLeftHom
      ((restrictionFunctor phi).map g)).map_add x y

@[simp]
theorem leftAction_identity (phi : H →* K)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    (x : RestrictionCorrespondence phi A B) :
    leftAction phi (𝟙 A) x = x := by
  exact Category.id_comp x

@[simp]
theorem rightAction_identity (phi : H →* K)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    (x : RestrictionCorrespondence phi A B) :
    rightAction phi (𝟙 B) x = x := by
  calc
    x ≫ (restrictionFunctor phi).map (𝟙 B) =
        x ≫ 𝟙 ((restrictionFunctor phi).obj B) := by
          exact congrArg (fun h => x ≫ h) ((restrictionFunctor phi).map_id B)
    _ = x := Category.comp_id x

/-- Successive left actions compose in contravariant order. -/
theorem leftAction_composition (phi : H →* K)
    {A₀ A₁ A₂ : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    (f : A₀ ⟶ A₁) (g : A₁ ⟶ A₂)
    (x : RestrictionCorrespondence phi A₂ B) :
    leftAction phi f (leftAction phi g x) = leftAction phi (f ≫ g) x := by
  exact (Category.assoc f g x).symm

/-- Successive right actions compose covariantly. -/
theorem rightAction_composition (phi : H →* K)
    {A : AdditiveBurnsideSpanObject H}
    {B₀ B₁ B₂ : AdditiveBurnsideSpanObject K}
    (x : RestrictionCorrespondence phi A B₀)
    (f : B₀ ⟶ B₁) (g : B₁ ⟶ B₂) :
    rightAction phi g (rightAction phi f x) =
      rightAction phi (f ≫ g) x := by
  calc
    (x ≫ (restrictionFunctor phi).map f) ≫
        (restrictionFunctor phi).map g =
      x ≫ ((restrictionFunctor phi).map f ≫
        (restrictionFunctor phi).map g) := Category.assoc x _ _
    _ = x ≫ (restrictionFunctor phi).map (f ≫ g) := by
      exact congrArg (fun h => x ≫ h)
        ((restrictionFunctor phi).map_comp f g).symm

/-- The left and right categorical actions commute. -/
theorem left_right_actions_commute (phi : H →* K)
    {A A' : AdditiveBurnsideSpanObject H}
    {B B' : AdditiveBurnsideSpanObject K}
    (f : A' ⟶ A) (x : RestrictionCorrespondence phi A B)
    (g : B ⟶ B') :
    rightAction phi g (leftAction phi f x) =
      leftAction phi f (rightAction phi g x) := by
  exact Category.assoc f x ((restrictionFunctor phi).map g)

/-- An equivariant seed map into a restricted target determines the graph
generator in the restriction correspondence. -/
def graphElement (phi : H →* K)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    (f : ActionMap H A (B.restrict H phi)) :
    RestrictionCorrespondence phi A B :=
  AdditiveBurnsideSpanObject.graphHom (G := H) f

variable [Finite G]

/-- Finite-action version of the set-action induction/restriction adjunction. -/
def inducedActionMapEquivRestrictedActionMap (L : Subgroup G)
    (A : FiniteAction.{u, u} L) (B : FiniteAction.{u, u} G) :
    ActionMap G (A.induce L) B ≃ ActionMap L A (B.restrict L L.subtype) :=
  inductionRestrictionEquiv (B := A.carrier) (C := B.carrier) L.subtype

/-- An equivariant map out of subgroup induction produces the corresponding
graph generator in the additive restriction correspondence. -/
def inducedMapGraphElement (L : Subgroup G)
    {A : FiniteAction.{u, u} L} {B : FiniteAction.{u, u} G}
    (f : ActionMap G (A.induce L) B) :
    RestrictionCorrespondence L.subtype A B :=
  graphElement L.subtype
    (inducedActionMapEquivRestrictedActionMap L A B f)

/-- The correspondence generator retains the exact set-action adjunction map;
passing to it and back changes no equivariant map. -/
theorem induced_restricted_action_map_roundtrip (L : Subgroup G)
    {A : FiniteAction.{u, u} L} {B : FiniteAction.{u, u} G}
    (f : ActionMap G (A.induce L) B) :
    (inducedActionMapEquivRestrictedActionMap L A B).symm
        (inducedActionMapEquivRestrictedActionMap L A B f) = f := by
  exact Equiv.symm_apply_apply _ f

/-- Conversely, every equivariant seed map into the restricted target is the
adjoint of a unique equivariant map out of subgroup induction. -/
theorem restricted_induced_action_map_roundtrip (L : Subgroup G)
    {A : FiniteAction.{u, u} L} {B : FiniteAction.{u, u} G}
    (f : ActionMap L A (B.restrict L L.subtype)) :
    inducedActionMapEquivRestrictedActionMap L A B
        ((inducedActionMapEquivRestrictedActionMap L A B).symm f) = f := by
  exact Equiv.apply_symm_apply _ f

end

end GroupActionBurnsideSpanCorrespondence
end GUFormalization
