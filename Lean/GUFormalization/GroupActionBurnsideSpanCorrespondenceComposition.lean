import GUFormalization.GroupActionBurnsideSpanCorrespondence

/-!
# Composition of additive restriction correspondences

For homomorphisms `H -> K -> L`, an element of `Hom_H(A, Res B)` composes
with an element of `Hom_K(B, Res C)` by restricting the second span to `H`
and using composition in the completed Burnside span category.

This gives the first typed composition law for the restriction companions. It
is additive in both inputs and is compatible with the existing outer actions
and graph generators. It is not an induction functor, a coend classification,
or a full Mackey 2-functor.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideSpanCorrespondenceComposition

noncomputable section

open CategoryTheory
open GroupActionBurnside
open GroupActionSpanCategory
open GroupActionBurnsideSpanCategory
open GroupActionBurnsideSpanRestriction
open GroupActionBurnsideSpanCorrespondence

universe u

variable {H K L : Type u} [Group H] [Group K] [Group L]

/-- The target of composing restriction companions along `H -> K -> L`. -/
abbrev IteratedRestrictionCorrespondence (phi : H →* K) (psi : K →* L)
    (A : AdditiveBurnsideSpanObject H)
    (C : AdditiveBurnsideSpanObject L) :=
  A ⟶ (restrictionFunctor phi).obj ((restrictionFunctor psi).obj C)

/-- Compose two restriction-correspondence elements by restricting the second
completed span and composing in the `H`-Burnside category. -/
def compose (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (x : RestrictionCorrespondence phi A B)
    (y : RestrictionCorrespondence psi B C) :
    IteratedRestrictionCorrespondence phi psi A C :=
  x ≫ (restrictionFunctor phi).map y

theorem compose_add_left (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (x₁ x₂ : RestrictionCorrespondence phi A B)
    (y : RestrictionCorrespondence psi B C) :
    compose phi psi (x₁ + x₂) y =
      compose phi psi x₁ y + compose phi psi x₂ y := by
  simp [compose, Preadditive.add_comp]

theorem compose_add_right (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (x : RestrictionCorrespondence phi A B)
    (y₁ y₂ : RestrictionCorrespondence psi B C) :
    compose phi psi x (y₁ + y₂) =
      compose phi psi x y₁ + compose phi psi x y₂ := by
  simp [compose, Preadditive.comp_add]

@[simp]
theorem compose_zero_left (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (y : RestrictionCorrespondence psi B C) :
    compose phi psi (0 : RestrictionCorrespondence phi A B) y = 0 := by
  simp [compose]

@[simp]
theorem compose_zero_right (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (x : RestrictionCorrespondence phi A B) :
    compose phi psi x (0 : RestrictionCorrespondence psi B C) = 0 := by
  simp [compose]

/-- An outer `H`-span may act before or after companion composition. -/
theorem leftAction_compose (phi : H →* K) (psi : K →* L)
    {A A' : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (f : A' ⟶ A) (x : RestrictionCorrespondence phi A B)
    (y : RestrictionCorrespondence psi B C) :
    compose phi psi (leftAction phi f x) y =
      f ≫ compose phi psi x y := by
  exact Category.assoc f x ((restrictionFunctor phi).map y)

/-- The right `L`-action distributes through companion composition. -/
theorem compose_rightAction (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C C' : AdditiveBurnsideSpanObject L}
    (x : RestrictionCorrespondence phi A B)
    (y : RestrictionCorrespondence psi B C) (g : C ⟶ C') :
    compose phi psi x (rightAction psi g y) =
      compose phi psi x y ≫
        (restrictionFunctor phi).map ((restrictionFunctor psi).map g) := by
  calc
    x ≫ (restrictionFunctor phi).map
        (y ≫ (restrictionFunctor psi).map g) =
      x ≫ ((restrictionFunctor phi).map y ≫
        (restrictionFunctor phi).map ((restrictionFunctor psi).map g)) := by
          rw [(restrictionFunctor phi).map_comp]
    _ = (x ≫ (restrictionFunctor phi).map y) ≫
        (restrictionFunctor phi).map ((restrictionFunctor psi).map g) :=
      (Category.assoc _ _ _).symm

/-- Composition of graph generators is the graph of the restricted second map
after the first. -/
theorem compose_graphElements (phi : H →* K) (psi : K →* L)
    {A : AdditiveBurnsideSpanObject H}
    {B : AdditiveBurnsideSpanObject K}
    {C : AdditiveBurnsideSpanObject L}
    (f : ActionMap H A (B.restrict H phi))
    (g : ActionMap K B (C.restrict K psi)) :
    compose phi psi (graphElement phi f) (graphElement psi g) =
      AdditiveBurnsideSpanObject.graphHom (G := H)
        (RawSpan.composeMap f (ActionMap.restrict phi g)) := by
  unfold compose graphElement
  rw [restrictionFunctor_graph]
  exact AdditiveBurnsideSpanObject.graph_composition H f
    (ActionMap.restrict phi g)

end

end GroupActionBurnsideSpanCorrespondenceComposition
end GUFormalization
