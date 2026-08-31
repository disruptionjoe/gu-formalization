import GUFormalization.GroupActionBurnside
import GUFormalization.GroupActionBurnsideSpanCategory

/-!
# The Burnside Mackey law in additive span-category point endomorphisms

The additive Burnside group of finite supplied `G`-actions is canonically the
additive endomorphism group of the trivial one-point action in the completed
finite-action span category.  Under this equivalence, the already-constructed
restriction and induction homomorphisms become subgroup-change homomorphisms
between point-endomorphism groups, and the additive double-coset identity
holds there.

This is pure finite supplied-action algebra.  It is a Mackey law on the point
endomorphism groups, not a category-valued Mackey functor on every span object,
and it supplies no physical representation, source-native action, observed
sector, selector, dynamics, prediction, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideSpanMackey

noncomputable section

open GroupActionBurnside
open GroupActionSpanCategory
open GroupActionBurnsideSpanCategory

universe u

variable (G : Type u) [Group G]

/-- The trivial one-point supplied `G`-action. -/
def point : FiniteAction.{u, u} G where
  carrier := PUnit
  fintype := inferInstance
  action := inferInstance

namespace RawSpan

variable {G}

/-- A finite action is the apex of a unique span from the point to itself. -/
def pointSpan (A : FiniteAction.{u, u} G) :
    GroupActionSpanCategory.RawSpan G (point G) (point G) where
  apex := A
  left := ⟨fun _ => PUnit.unit, by intro _ _; rfl⟩
  right := ⟨fun _ => PUnit.unit, by intro _ _; rfl⟩

/-- Equivariantly equivalent actions give equivalent point spans. -/
def pointSpanEquiv {A B : FiniteAction.{u, u} G}
    (e : FiniteAction.Equiv G A B) :
    GroupActionSpanCategory.RawSpan.Equiv (pointSpan A) (pointSpan B) where
  apexEquiv := e
  left_comm _ := rfl
  right_comm _ := rfl

/-- Every point span is equivalent to the point span of its apex. -/
def equivPointSpanApex
    (S : GroupActionSpanCategory.RawSpan G (point G) (point G)) :
    GroupActionSpanCategory.RawSpan.Equiv S (pointSpan S.apex) where
  apexEquiv := FiniteAction.Equiv.refl G S.apex
  left_comm x := by cases S.left.1 x; rfl
  right_comm x := by cases S.right.1 x; rfl

end RawSpan

namespace PointSpanClass

variable {G}

/-- Send a finite-action isomorphism class to its point-span class. -/
def ofAction : BurnsideMonoid.{u, u} G →
    GroupActionSpanCategory.SpanClass G (point G) (point G) :=
  Quotient.lift
    (fun A => GroupActionSpanCategory.SpanClass.of (RawSpan.pointSpan A))
    (by
      intro A B h
      rcases h with ⟨e⟩
      exact Quotient.sound ⟨RawSpan.pointSpanEquiv e⟩)

/-- Remember only the apex action of a point-span class. -/
def toAction : GroupActionSpanCategory.SpanClass G (point G) (point G) →
    BurnsideMonoid.{u, u} G :=
  Quotient.lift
    (fun S => BurnsideMonoid.of G S.apex)
    (by
      intro S T h
      rcases h with ⟨e⟩
      exact Quotient.sound ⟨e.apexEquiv⟩)

@[simp]
theorem ofAction_of (A : FiniteAction.{u, u} G) :
    ofAction (BurnsideMonoid.of G A) =
      GroupActionSpanCategory.SpanClass.of (RawSpan.pointSpan A) := rfl

@[simp]
theorem toAction_of (S : GroupActionSpanCategory.RawSpan G (point G) (point G)) :
    toAction (GroupActionSpanCategory.SpanClass.of S) =
      BurnsideMonoid.of G S.apex := rfl

@[simp]
theorem toAction_ofAction (x : BurnsideMonoid.{u, u} G) :
    toAction (ofAction x) = x := by
  induction x using Quotient.inductionOn
  rfl

@[simp]
theorem ofAction_toAction
    (S : GroupActionSpanCategory.SpanClass G (point G) (point G)) :
    ofAction (toAction S) = S := by
  induction S using Quotient.inductionOn
  exact Quotient.sound ⟨(RawSpan.equivPointSpanApex _).symm⟩

/-- The action-to-point-span map preserves disjoint coproduct addition. -/
def ofActionHom : BurnsideMonoid.{u, u} G →+
    GroupActionSpanCategory.SpanClass G (point G) (point G) where
  toFun := ofAction
  map_zero' := rfl
  map_add' x y := by
    induction x using Quotient.inductionOn
    induction y using Quotient.inductionOn
    rfl

/-- Taking a point span's apex preserves disjoint coproduct addition. -/
def toActionHom : GroupActionSpanCategory.SpanClass G (point G) (point G) →+
    BurnsideMonoid.{u, u} G where
  toFun := toAction
  map_zero' := rfl
  map_add' S T := by
    induction S using Quotient.inductionOn
    induction T using Quotient.inductionOn
    rfl

/-- Isomorphism classes of finite actions are additively equivalent to
isomorphism classes of point-to-point spans. -/
def monoidEquiv : BurnsideMonoid.{u, u} G ≃+
    GroupActionSpanCategory.SpanClass G (point G) (point G) where
  toFun := ofActionHom (G := G)
  invFun := toActionHom (G := G)
  left_inv := toAction_ofAction
  right_inv := ofAction_toAction
  map_add' := (ofActionHom (G := G)).map_add

end PointSpanClass

/-- The additive map from the Burnside group into completed point
endomorphisms induced by the point-span construction. -/
def pointEndomorphismForward : BurnsideGroup.{u, u} G →+
    GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G) :=
  Algebra.GrothendieckAddGroup.lift
    ((Algebra.GrothendieckAddGroup.of :
      GroupActionSpanCategory.SpanClass G (point G) (point G) →+
        GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G)).comp
      (PointSpanClass.ofActionHom (G := G)))

/-- The inverse additive map remembers the apex of every point-span
generator. -/
def pointEndomorphismBackward :
    GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G) →+
      BurnsideGroup G :=
  Algebra.GrothendieckAddGroup.lift
    ((Algebra.GrothendieckAddGroup.of :
      BurnsideMonoid.{u, u} G →+ BurnsideGroup.{u, u} G).comp
      (PointSpanClass.toActionHom (G := G)))

@[simp]
theorem pointEndomorphismForward_of (A : FiniteAction.{u, u} G) :
    pointEndomorphismForward G (burnsideOf G A) =
      GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
        (GroupActionSpanCategory.SpanClass.of (RawSpan.pointSpan A)) := by
  unfold pointEndomorphismForward burnsideOf
  rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
  rfl

@[simp]
theorem pointEndomorphismBackward_of
    (S : GroupActionSpanCategory.RawSpan G (point G) (point G)) :
    pointEndomorphismBackward G
        (GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
          (GroupActionSpanCategory.SpanClass.of S)) =
      burnsideOf G S.apex := by
  unfold pointEndomorphismBackward GroupActionBurnsideSpanCategory.BurnsideSpanHom.of
  rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
  rfl

/-- The additive Burnside group is canonically the additive endomorphism group
of the trivial point in the completed Burnside span category. -/
def pointEndomorphismEquiv : BurnsideGroup.{u, u} G ≃+
    GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G) where
  toFun := pointEndomorphismForward G
  invFun := pointEndomorphismBackward G
  left_inv x := by
    have h : (pointEndomorphismBackward G).comp (pointEndomorphismForward G) =
        AddMonoidHom.id (BurnsideGroup.{u, u} G) := by
      apply GroupActionBurnsideSpanCategory.grothendieckHom_ext
      intro a
      change pointEndomorphismBackward G
          (pointEndomorphismForward G (Algebra.GrothendieckAddGroup.of a)) =
        Algebra.GrothendieckAddGroup.of a
      unfold pointEndomorphismForward pointEndomorphismBackward
      rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
      change Algebra.GrothendieckAddGroup.lift _
          (Algebra.GrothendieckAddGroup.of (PointSpanClass.ofAction a)) =
        Algebra.GrothendieckAddGroup.of a
      rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
      change Algebra.GrothendieckAddGroup.of
          (PointSpanClass.toAction (PointSpanClass.ofAction a)) =
        Algebra.GrothendieckAddGroup.of a
      rw [PointSpanClass.toAction_ofAction]
    exact DFunLike.congr_fun h x
  right_inv x := by
    have h : (pointEndomorphismForward G).comp (pointEndomorphismBackward G) =
        AddMonoidHom.id
          (GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G)) := by
      apply GroupActionBurnsideSpanCategory.grothendieckHom_ext
      intro S
      change pointEndomorphismForward G
          (pointEndomorphismBackward G (Algebra.GrothendieckAddGroup.of S)) =
        Algebra.GrothendieckAddGroup.of S
      unfold pointEndomorphismForward pointEndomorphismBackward
      rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
      change Algebra.GrothendieckAddGroup.lift _
          (Algebra.GrothendieckAddGroup.of (PointSpanClass.toAction S)) =
        Algebra.GrothendieckAddGroup.of S
      rw [GroupActionBurnsideSpanCategory.grothendieckLift_of]
      change Algebra.GrothendieckAddGroup.of
          (PointSpanClass.ofAction (PointSpanClass.toAction S)) =
        Algebra.GrothendieckAddGroup.of S
      rw [PointSpanClass.ofAction_toAction]
    exact DFunLike.congr_fun h x
  map_add' := (pointEndomorphismForward G).map_add

@[simp]
theorem pointEndomorphismEquiv_burnsideOf (A : FiniteAction.{u, u} G) :
    pointEndomorphismEquiv G (burnsideOf G A) =
      GroupActionBurnsideSpanCategory.AdditiveBurnsideSpanObject.spanHom (G := G)
        (GroupActionSpanCategory.SpanClass.of (RawSpan.pointSpan A)) := by
  exact pointEndomorphismForward_of G A

@[simp]
theorem pointEndomorphismBackward_forward (x : BurnsideGroup.{u, u} G) :
    pointEndomorphismBackward G (pointEndomorphismForward G x) = x :=
  (pointEndomorphismEquiv G).left_inv x

@[simp]
theorem pointEndomorphismForward_backward
    (x : GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G)) :
    pointEndomorphismForward G (pointEndomorphismBackward G x) = x :=
  (pointEndomorphismEquiv G).right_inv x

/-- Restriction across a supplied homomorphism, transported to additive point
endomorphism groups. -/
def pointRestriction {H K : Type u} [Group H] [Group K] (phi : H →* K) :
    GroupActionBurnsideSpanCategory.BurnsideSpanHom K (point K) (point K) →+
      GroupActionBurnsideSpanCategory.BurnsideSpanHom H (point H) (point H) :=
  (pointEndomorphismForward H).comp
    ((GroupActionBurnside.restriction H phi).comp (pointEndomorphismBackward K))

/-- Induction from a subgroup, transported to additive point-endomorphism
groups. -/
def pointInduction {G : Type u} [Group G] [Finite G] (L : Subgroup G) :
    GroupActionBurnsideSpanCategory.BurnsideSpanHom L (point L) (point L) →+
      GroupActionBurnsideSpanCategory.BurnsideSpanHom G (point G) (point G) :=
  (pointEndomorphismForward G).comp
    ((GroupActionBurnside.induction L).comp (pointEndomorphismBackward L))

@[simp]
theorem pointRestriction_of {H K : Type u} [Group H] [Group K]
    (phi : H →* K) (A : FiniteAction.{u, u} K) :
    pointRestriction phi
        (pointEndomorphismEquiv K (burnsideOf K A)) =
      pointEndomorphismEquiv H
        (burnsideOf H (FiniteAction.restrict H phi A)) := by
  change pointEndomorphismForward H
      (GroupActionBurnside.restriction H phi
        (pointEndomorphismBackward K
          (pointEndomorphismForward K (burnsideOf K A)))) =
    pointEndomorphismForward H
      (burnsideOf H (FiniteAction.restrict H phi A))
  rw [pointEndomorphismBackward_forward,
    GroupActionBurnside.restriction_of]

@[simp]
theorem pointInduction_of {G : Type u} [Group G] [Finite G] (L : Subgroup G)
    (A : FiniteAction.{u, u} L) :
    pointInduction L (pointEndomorphismEquiv L (burnsideOf L A)) =
      pointEndomorphismEquiv G (burnsideOf G (FiniteAction.induce L A)) := by
  change pointEndomorphismForward G
      (GroupActionBurnside.induction L
        (pointEndomorphismBackward L
          (pointEndomorphismForward L (burnsideOf L A)))) =
    pointEndomorphismForward G
      (burnsideOf G (FiniteAction.induce L A))
  rw [pointEndomorphismBackward_forward,
    GroupActionBurnside.induction_of]

/-- The additive subgroup Mackey double-coset identity in the point-
endomorphism groups of the completed Burnside span categories. -/
theorem pointRestriction_pointInduction_eq_mackeyCoproduct
    {G : Type u} [Group G] [Finite G] (K L : Subgroup G)
    (A : FiniteAction.{u, u} L) :
    pointRestriction K.subtype
        (pointInduction L (pointEndomorphismEquiv L (burnsideOf L A))) =
      pointEndomorphismEquiv K
        (burnsideOf K (mackeyCoproductFiniteAction K L A)) := by
  unfold pointRestriction pointInduction pointEndomorphismEquiv
  change pointEndomorphismForward K
      (GroupActionBurnside.restriction K K.subtype
        (pointEndomorphismBackward G
          (pointEndomorphismForward G
            (GroupActionBurnside.induction L
              (pointEndomorphismBackward L
                (pointEndomorphismForward L (burnsideOf L A))))))) =
    pointEndomorphismForward K
      (burnsideOf K (mackeyCoproductFiniteAction K L A))
  rw [pointEndomorphismBackward_forward,
    pointEndomorphismBackward_forward,
    GroupActionBurnside.restriction_induction_of_eq_mackeyCoproduct]

end

end GroupActionBurnsideSpanMackey
end GUFormalization
