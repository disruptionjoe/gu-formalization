import GUFormalization.GroupActionBurnsideMackeyFunctor

/-!
# Restriction between additive Burnside span categories

Restriction of a supplied finite action along a group homomorphism preserves
the underlying finite carrier, equivariant maps, disjoint coproducts, and
finite pullbacks.  It therefore descends from raw spans to span-isomorphism
classes and through homwise Grothendieck completion, giving an additive
functor between the completed Burnside span categories.  The functor preserves
graph and converse-graph generators and is coherent with identity and
composition of acting-group homomorphisms.

This is pure finite supplied-action algebra.  It constructs categorical
restriction, not categorical induction: induction does not in general
preserve the pullbacks used for span composition.  It supplies no physical
representation, source-native action, observed sector, selector, dynamics,
prediction, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideSpanRestriction

noncomputable section

open CategoryTheory
open GroupActionBurnside
open GroupActionSpanCategory
open GroupActionBurnsideSpanCategory

universe u

variable {H K L : Type u} [Group H] [Group K] [Group L]

namespace FiniteAction

/-- Restricting along the identity homomorphism changes no supplied action,
up to the canonical identity equivalence. -/
def restrictIdentityEquiv (A : FiniteAction.{u, u} H) :
    FiniteAction.Equiv H (A.restrict H (MonoidHom.id H)) A where
  toEquiv := _root_.Equiv.refl _
  map_smul' _ _ := rfl

/-- Iterated restriction agrees with restriction along the composite
homomorphism, up to the canonical identity equivalence of carriers. -/
def restrictCompositionEquiv (phi : H →* K) (psi : L →* H)
    (A : FiniteAction.{u, u} K) :
    FiniteAction.Equiv L ((A.restrict H phi).restrict L psi)
      (A.restrict L (phi.comp psi)) where
  toEquiv := _root_.Equiv.refl _
  map_smul' _ _ := rfl

end FiniteAction

namespace ActionMap

/-- Forget part of the acting group on an equivariant map. -/
def restrict (phi : H →* K) {A B : FiniteAction.{u, u} K}
    (f : GroupActionSpanCategory.ActionMap K A B) :
    GroupActionSpanCategory.ActionMap H (A.restrict H phi) (B.restrict H phi) :=
  ⟨f.1, by intro h a; exact f.2 (phi h) a⟩

@[simp]
theorem restrict_apply (phi : H →* K) {A B : FiniteAction.{u, u} K}
    (f : GroupActionSpanCategory.ActionMap K A B) (a : A.carrier) :
    (restrict phi f).1 a = f.1 a := rfl

/-- Restriction along the identity homomorphism is pointwise the original
equivariant map. -/
theorem restrict_identity_apply {A B : FiniteAction.{u, u} H}
    (f : GroupActionSpanCategory.ActionMap H A B) (a : A.carrier) :
    (restrict (MonoidHom.id H) f).1 a = f.1 a := rfl

/-- Iterated restriction is pointwise restriction along the composite
homomorphism. -/
theorem restrict_composition_apply (phi : H →* K) (psi : L →* H)
    {A B : FiniteAction.{u, u} K}
    (f : GroupActionSpanCategory.ActionMap K A B) (a : A.carrier) :
    (restrict psi (restrict phi f)).1 a =
      (restrict (phi.comp psi) f).1 a := rfl

end ActionMap

namespace RawSpan

variable {A B C : FiniteAction.{u, u} K}

/-- Restrict the apex and both legs of a span along a group homomorphism. -/
def restrict (phi : H →* K) (S : GroupActionSpanCategory.RawSpan K A B) :
    GroupActionSpanCategory.RawSpan H (A.restrict H phi) (B.restrict H phi) where
  apex := S.apex.restrict H phi
  left := ActionMap.restrict phi S.left
  right := ActionMap.restrict phi S.right

/-- Restriction preserves equivalences of span apices. -/
def Equiv.restrict (phi : H →* K)
    {S T : GroupActionSpanCategory.RawSpan K A B}
    (e : GroupActionSpanCategory.RawSpan.Equiv S T) :
    GroupActionSpanCategory.RawSpan.Equiv (restrict phi S) (restrict phi T) where
  apexEquiv := e.apexEquiv.restrict H phi
  left_comm := e.left_comm
  right_comm := e.right_comm

/-- Restriction of an identity span is the identity span of the restricted
object, up to the canonical identity apex equivalence. -/
def restrictIdentityEquiv (phi : H →* K) (A : FiniteAction.{u, u} K) :
    GroupActionSpanCategory.RawSpan.Equiv
      (restrict phi (GroupActionSpanCategory.RawSpan.identity A))
      (GroupActionSpanCategory.RawSpan.identity (A.restrict H phi)) where
  apexEquiv := FiniteAction.Equiv.refl H (A.restrict H phi)
  left_comm _ := rfl
  right_comm _ := rfl

/-- Restriction preserves the finite pullback apex used for span
composition. -/
def restrictCompEquiv (phi : H →* K)
    (S : GroupActionSpanCategory.RawSpan K A B)
    (T : GroupActionSpanCategory.RawSpan K B C) :
    GroupActionSpanCategory.RawSpan.Equiv
      (restrict phi (GroupActionSpanCategory.RawSpan.comp S T))
      (GroupActionSpanCategory.RawSpan.comp (restrict phi S) (restrict phi T)) where
  apexEquiv := {
    toEquiv := _root_.Equiv.refl _
    map_smul' := by intro _ _; rfl
  }
  left_comm _ := rfl
  right_comm _ := rfl

/-- Restriction of the empty span is the empty span. -/
def restrictZeroEquiv (phi : H →* K) (A B : FiniteAction.{u, u} K) :
    GroupActionSpanCategory.RawSpan.Equiv
      (restrict phi (GroupActionBurnsideSpanCategory.RawSpan.zero A B))
      (GroupActionBurnsideSpanCategory.RawSpan.zero
        (A.restrict H phi) (B.restrict H phi)) where
  apexEquiv := {
    toEquiv := _root_.Equiv.refl _
    map_smul' := by intro _ x; exact PEmpty.elim x
  }
  left_comm x := PEmpty.elim x
  right_comm x := PEmpty.elim x

/-- Restriction preserves disjoint coproduct of span apices. -/
def restrictSumEquiv (phi : H →* K)
    (S T : GroupActionSpanCategory.RawSpan K A B) :
    GroupActionSpanCategory.RawSpan.Equiv
      (restrict phi (GroupActionBurnsideSpanCategory.RawSpan.sum S T))
      (GroupActionBurnsideSpanCategory.RawSpan.sum (restrict phi S) (restrict phi T)) where
  apexEquiv := {
    toEquiv := _root_.Equiv.refl _
    map_smul' := by intro _ x; cases x <;> rfl
  }
  left_comm x := by cases x <;> rfl
  right_comm x := by cases x <;> rfl

/-- Restriction commutes with graph-span formation. -/
def restrictGraphEquiv (phi : H →* K)
    (f : GroupActionSpanCategory.ActionMap K A B) :
    GroupActionSpanCategory.RawSpan.Equiv
      (restrict phi (GroupActionSpanCategory.RawSpan.graph f))
      (GroupActionSpanCategory.RawSpan.graph (ActionMap.restrict phi f)) where
  apexEquiv := FiniteAction.Equiv.refl H (A.restrict H phi)
  left_comm _ := rfl
  right_comm _ := rfl

/-- Restriction commutes with converse-graph formation. -/
def restrictConverseGraphEquiv (phi : H →* K)
    (f : GroupActionSpanCategory.ActionMap K A B) :
    GroupActionSpanCategory.RawSpan.Equiv
      (restrict phi (GroupActionSpanCategory.RawSpan.converseGraph f))
      (GroupActionSpanCategory.RawSpan.converseGraph (ActionMap.restrict phi f)) where
  apexEquiv := FiniteAction.Equiv.refl H (A.restrict H phi)
  left_comm _ := rfl
  right_comm _ := rfl

end RawSpan

namespace SpanClass

variable {A B C : FiniteAction.{u, u} K}

/-- Restriction descends to isomorphism classes of spans. -/
def restrict (phi : H →* K) :
    GroupActionSpanCategory.SpanClass K A B →
      GroupActionSpanCategory.SpanClass H (A.restrict H phi) (B.restrict H phi) :=
  Quotient.map (RawSpan.restrict phi) (by
    rintro S T ⟨e⟩
    exact ⟨GroupActionBurnsideSpanRestriction.RawSpan.Equiv.restrict phi e⟩)

@[simp]
theorem restrict_of (phi : H →* K)
    (S : GroupActionSpanCategory.RawSpan K A B) :
    restrict phi (GroupActionSpanCategory.SpanClass.of S) =
      GroupActionSpanCategory.SpanClass.of (RawSpan.restrict phi S) := rfl

/-- Restriction preserves identity span classes. -/
theorem restrict_identity (phi : H →* K) (A : FiniteAction.{u, u} K) :
    restrict phi (GroupActionSpanCategory.SpanClass.of
      (GroupActionSpanCategory.RawSpan.identity A)) =
      GroupActionSpanCategory.SpanClass.of
        (GroupActionSpanCategory.RawSpan.identity (A.restrict H phi)) :=
  Quotient.sound ⟨RawSpan.restrictIdentityEquiv phi A⟩

/-- Restriction preserves pullback composition of span classes. -/
theorem restrict_comp (phi : H →* K)
    (S : GroupActionSpanCategory.SpanClass K A B)
    (T : GroupActionSpanCategory.SpanClass K B C) :
    restrict phi (GroupActionSpanCategory.SpanClass.comp S T) =
      GroupActionSpanCategory.SpanClass.comp (restrict phi S) (restrict phi T) := by
  induction S using Quotient.inductionOn
  induction T using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.restrictCompEquiv phi _ _⟩

/-- Restriction of span classes is additive under disjoint coproduct. -/
def restrictionHom (phi : H →* K) :
    GroupActionSpanCategory.SpanClass K A B →+
      GroupActionSpanCategory.SpanClass H (A.restrict H phi) (B.restrict H phi) where
  toFun := restrict phi
  map_zero' := Quotient.sound ⟨RawSpan.restrictZeroEquiv phi A B⟩
  map_add' S T := by
    induction S using Quotient.inductionOn
    induction T using Quotient.inductionOn
    exact Quotient.sound ⟨RawSpan.restrictSumEquiv phi _ _⟩

end SpanClass

namespace BurnsideSpanHom

variable {A B C : FiniteAction.{u, u} K}

/-- Restriction on positive span generators, valued in the completed target
hom-group. -/
def restrictionGeneratorHom (phi : H →* K) :
    GroupActionSpanCategory.SpanClass K A B →+
      GroupActionBurnsideSpanCategory.BurnsideSpanHom H
        (A.restrict H phi) (B.restrict H phi) where
  toFun S := GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
    (SpanClass.restrictionHom phi S)
  map_zero' := by
    change Algebra.GrothendieckAddGroup.of 0 = 0
    exact map_zero _
  map_add' S T := by
    rw [map_add]
    change Algebra.GrothendieckAddGroup.of
      ((SpanClass.restrictionHom phi) S + (SpanClass.restrictionHom phi) T) = _
    exact map_add _ _ _

/-- Restriction on completed Burnside span hom-groups. -/
def restrict (phi : H →* K) :
    GroupActionBurnsideSpanCategory.BurnsideSpanHom K A B →+
      GroupActionBurnsideSpanCategory.BurnsideSpanHom H
        (A.restrict H phi) (B.restrict H phi) :=
  Algebra.GrothendieckAddGroup.lift (restrictionGeneratorHom phi)

@[simp]
theorem restrict_of (phi : H →* K)
    (S : GroupActionSpanCategory.SpanClass K A B) :
    restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of S) =
      GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
        (SpanClass.restrictionHom phi S) := by
  unfold restrict
  unfold GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
  rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
  rfl

/-- Restriction preserves the completed identity morphism. -/
theorem restrict_identity (phi : H →* K) (A : FiniteAction.{u, u} K) :
    restrict phi (𝟙 (A : AdditiveBurnsideSpanObject K)) =
      𝟙 (A.restrict H phi : AdditiveBurnsideSpanObject H) := by
  change restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of _) =
    GroupActionBurnsideSpanCategory.BurnsideSpanHom.of _
  rw [restrict_of]
  exact congrArg GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
    (SpanClass.restrict_identity phi A)

/-- Restriction preserves bilinear completed span composition. -/
theorem restrict_comp (phi : H →* K)
    (S : GroupActionBurnsideSpanCategory.BurnsideSpanHom K A B)
    (T : GroupActionBurnsideSpanCategory.BurnsideSpanHom K B C) :
    restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.comp S T) =
      GroupActionBurnsideSpanCategory.BurnsideSpanHom.comp
        (restrict phi S) (restrict phi T) := by
  have hT :
      (restrict (A := A) (B := C) phi).comp
          (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compRightHom S) =
        (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compRightHom
          (restrict phi S)).comp (restrict (A := B) (B := C) phi) := by
    apply GroupActionBurnsideSpanCategory.grothendieckHom_ext
    intro T₀
    have hS :
        (restrict (A := A) (B := C) phi).comp
            (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compLeftHom
              (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of T₀)) =
          (GroupActionBurnsideSpanCategory.BurnsideSpanHom.compLeftHom
            (restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of T₀))).comp
            (restrict (A := A) (B := B) phi) := by
      apply GroupActionBurnsideSpanCategory.grothendieckHom_ext
      intro S₀
      change restrict phi
          (GroupActionBurnsideSpanCategory.BurnsideSpanHom.comp
            (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of S₀)
            (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of T₀)) =
        GroupActionBurnsideSpanCategory.BurnsideSpanHom.comp
          (restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of S₀))
          (restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of T₀))
      rw [GroupActionBurnsideSpanCategory.BurnsideSpanHom.comp_of_of,
        restrict_of, restrict_of, restrict_of,
        GroupActionBurnsideSpanCategory.BurnsideSpanHom.comp_of_of]
      exact congrArg GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
        (SpanClass.restrict_comp phi S₀ T₀)
    exact DFunLike.congr_fun hS S
  exact DFunLike.congr_fun hT T

end BurnsideSpanHom

/-- Additive restriction between completed Burnside span categories. -/
def restrictionFunctor (phi : H →* K) :
    AdditiveBurnsideSpanObject K ⥤ AdditiveBurnsideSpanObject H where
  obj A := A.restrict H phi
  map f := BurnsideSpanHom.restrict phi f
  map_id A := BurnsideSpanHom.restrict_identity phi A
  map_comp f g := BurnsideSpanHom.restrict_comp phi f g

instance restrictionFunctor_additive (phi : H →* K) :
    Functor.Additive (restrictionFunctor phi) where
  map_add := by
    intro A B f g
    exact map_add (BurnsideSpanHom.restrict (A := A) (B := B) phi) f g

/-- Categorical restriction preserves graph-span generators. -/
theorem restrictionFunctor_graph {A B : AdditiveBurnsideSpanObject K}
    (phi : H →* K) (f : GroupActionSpanCategory.ActionMap K A B) :
    (restrictionFunctor phi).map
        (AdditiveBurnsideSpanObject.graphHom (G := K) f) =
      AdditiveBurnsideSpanObject.graphHom (G := H) (ActionMap.restrict phi f) := by
  change BurnsideSpanHom.restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of _) =
    GroupActionBurnsideSpanCategory.BurnsideSpanHom.of _
  rw [BurnsideSpanHom.restrict_of]
  exact congrArg GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
    (Quotient.sound ⟨RawSpan.restrictGraphEquiv phi f⟩)

/-- Categorical restriction preserves converse-graph generators. -/
theorem restrictionFunctor_converseGraph
    {A B : AdditiveBurnsideSpanObject K}
    (phi : H →* K) (f : GroupActionSpanCategory.ActionMap K A B) :
    (restrictionFunctor phi).map
        (AdditiveBurnsideSpanObject.converseGraphHom (G := K) f) =
      AdditiveBurnsideSpanObject.converseGraphHom (G := H)
        (ActionMap.restrict phi f) := by
  change BurnsideSpanHom.restrict phi (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of _) =
    GroupActionBurnsideSpanCategory.BurnsideSpanHom.of _
  rw [BurnsideSpanHom.restrict_of]
  exact congrArg GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
    (Quotient.sound ⟨RawSpan.restrictConverseGraphEquiv phi f⟩)

end

end GroupActionBurnsideSpanRestriction
end GUFormalization
