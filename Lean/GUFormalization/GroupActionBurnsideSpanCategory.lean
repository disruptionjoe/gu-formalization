import GUFormalization.GroupActionSpanCategory
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.GroupTheory.MonoidLocalization.GrothendieckGroup

/-!
# The additive Burnside category of finite supplied-action spans

Disjoint coproduct of span apices makes every hom-set in the finite supplied-
action span category an additive commutative monoid. Finite equivariant
pullback distributes over that coproduct in both variables. Homwise
Grothendieck completion therefore supplies additive inverses and a genuine
preadditive category.

This is pure finite group-action algebra. It supplies no physical
representation, source-native action, observed sector, selector, dynamics,
prediction, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnsideSpanCategory

noncomputable section

open CategoryTheory
open GroupActionBurnside
open GroupActionSpanCategory

universe u

variable (G : Type u) [Group G]

namespace RawSpan

variable {G} {A B C : FiniteAction.{u, u} G}

/-- The zero span has empty apex. -/
def zero (A B : FiniteAction.{u, u} G) : RawSpan G A B where
  apex := FiniteAction.empty G
  left := ⟨PEmpty.elim, by intro _ x; exact PEmpty.elim x⟩
  right := ⟨PEmpty.elim, by intro _ x; exact PEmpty.elim x⟩

/-- Disjoint coproduct of two spans with the same endpoints. -/
def sum (S T : RawSpan G A B) : RawSpan G A B where
  apex := FiniteAction.sum G S.apex T.apex
  left := ⟨Sum.elim S.left.1 T.left.1, by
    intro g x
    cases x with
    | inl s => exact S.left.2 g s
    | inr t => exact T.left.2 g t⟩
  right := ⟨Sum.elim S.right.1 T.right.1, by
    intro g x
    cases x with
    | inl s => exact S.right.2 g s
    | inr t => exact T.right.2 g t⟩

/-- Span equivalences are preserved by disjoint coproduct. -/
def Equiv.sumCongr {S S' T T' : RawSpan G A B}
    (e : RawSpan.Equiv S S') (f : RawSpan.Equiv T T') :
    RawSpan.Equiv (sum S T) (sum S' T') where
  apexEquiv := FiniteAction.Equiv.sumCongr G e.apexEquiv f.apexEquiv
  left_comm x := by cases x with
    | inl s => exact e.left_comm s
    | inr t => exact f.left_comm t
  right_comm x := by cases x with
    | inl s => exact e.right_comm s
    | inr t => exact f.right_comm t

/-- The empty span is a left additive unit. -/
def zeroSumEquiv (S : RawSpan G A B) :
    RawSpan.Equiv (sum (zero A B) S) S where
  apexEquiv := FiniteAction.emptySumEquiv G S.apex
  left_comm x := by cases x with
    | inl e => exact PEmpty.elim e
    | inr s => rfl
  right_comm x := by cases x with
    | inl e => exact PEmpty.elim e
    | inr s => rfl

/-- The empty span is a right additive unit. -/
def sumZeroEquiv (S : RawSpan G A B) :
    RawSpan.Equiv (sum S (zero A B)) S where
  apexEquiv := FiniteAction.sumEmptyEquiv G S.apex
  left_comm x := by cases x with
    | inl s => rfl
    | inr e => exact PEmpty.elim e
  right_comm x := by cases x with
    | inl s => rfl
    | inr e => exact PEmpty.elim e

/-- Disjoint coproduct of spans is associative up to apex equivalence. -/
def sumAssocEquiv (S T U : RawSpan G A B) :
    RawSpan.Equiv (sum (sum S T) U) (sum S (sum T U)) where
  apexEquiv := FiniteAction.sumAssocEquiv G S.apex T.apex U.apex
  left_comm x := by cases x with
    | inl st => cases st <;> rfl
    | inr u => rfl
  right_comm x := by cases x with
    | inl st => cases st <;> rfl
    | inr u => rfl

/-- Disjoint coproduct of spans is commutative up to apex equivalence. -/
def sumCommEquiv (S T : RawSpan G A B) :
    RawSpan.Equiv (sum S T) (sum T S) where
  apexEquiv := FiniteAction.sumCommEquiv G S.apex T.apex
  left_comm x := by cases x <;> rfl
  right_comm x := by cases x <;> rfl

/-- Pullback distributes over a coproduct in its first span variable. -/
def sumCompEquiv (S T : RawSpan G A B) (U : RawSpan G B C) :
    RawSpan.Equiv (RawSpan.comp (sum S T) U)
      (sum (RawSpan.comp S U) (RawSpan.comp T U)) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => match h : p.1.1 with
        | Sum.inl s => Sum.inl ⟨(s, p.1.2), by simpa [sum, h] using p.2⟩
        | Sum.inr t => Sum.inr ⟨(t, p.1.2), by simpa [sum, h] using p.2⟩
      invFun := fun q => match q with
        | Sum.inl p => ⟨(Sum.inl p.1.1, p.1.2), p.2⟩
        | Sum.inr p => ⟨(Sum.inr p.1.1, p.1.2), p.2⟩
      left_inv := by intro p; rcases p with ⟨⟨s | t, u⟩, h⟩ <;> rfl
      right_inv := by intro q; rcases q with p | p <;> rcases p with ⟨⟨x, u⟩, h⟩ <;> rfl
    }
    map_smul' := by intro g p; rcases p with ⟨⟨s | t, u⟩, h⟩ <;> rfl
  }
  left_comm p := by rcases p with ⟨⟨s | t, u⟩, h⟩ <;> rfl
  right_comm p := by rcases p with ⟨⟨s | t, u⟩, h⟩ <;> rfl

/-- Pullback distributes over a coproduct in its second span variable. -/
def compSumEquiv (U : RawSpan G A B) (S T : RawSpan G B C) :
    RawSpan.Equiv (RawSpan.comp U (sum S T))
      (sum (RawSpan.comp U S) (RawSpan.comp U T)) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => match h : p.1.2 with
        | Sum.inl s => Sum.inl ⟨(p.1.1, s), by simpa [sum, h] using p.2⟩
        | Sum.inr t => Sum.inr ⟨(p.1.1, t), by simpa [sum, h] using p.2⟩
      invFun := fun q => match q with
        | Sum.inl p => ⟨(p.1.1, Sum.inl p.1.2), p.2⟩
        | Sum.inr p => ⟨(p.1.1, Sum.inr p.1.2), p.2⟩
      left_inv := by intro p; rcases p with ⟨⟨u, s | t⟩, h⟩ <;> rfl
      right_inv := by intro q; rcases q with p | p <;> rcases p with ⟨⟨u, x⟩, h⟩ <;> rfl
    }
    map_smul' := by intro g p; rcases p with ⟨⟨u, s | t⟩, h⟩ <;> rfl
  }
  left_comm p := by rcases p with ⟨⟨u, s | t⟩, h⟩ <;> rfl
  right_comm p := by rcases p with ⟨⟨u, s | t⟩, h⟩ <;> rfl

/-- Pullback composition with an empty right apex is empty. -/
def compZeroEquiv (S : RawSpan G A B) :
    RawSpan.Equiv (RawSpan.comp S (zero B C)) (zero A C) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => PEmpty.elim p.1.2
      invFun := PEmpty.elim
      left_inv := fun p => PEmpty.elim p.1.2
      right_inv := fun x => PEmpty.elim x
    }
    map_smul' := fun _ p => PEmpty.elim p.1.2
  }
  left_comm p := PEmpty.elim p.1.2
  right_comm p := PEmpty.elim p.1.2

/-- Pullback composition with an empty left apex is empty. -/
def zeroCompEquiv (T : RawSpan G B C) :
    RawSpan.Equiv (RawSpan.comp (zero A B) T) (zero A C) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => PEmpty.elim p.1.1
      invFun := PEmpty.elim
      left_inv := fun p => PEmpty.elim p.1.1
      right_inv := fun x => PEmpty.elim x
    }
    map_smul' := fun _ p => PEmpty.elim p.1.1
  }
  left_comm p := PEmpty.elim p.1.1
  right_comm p := PEmpty.elim p.1.1

end RawSpan

namespace SpanClass

variable {G} {A B C : FiniteAction.{u, u} G}

instance : Zero (SpanClass G A B) :=
  ⟨GroupActionSpanCategory.SpanClass.of (RawSpan.zero A B)⟩

instance : Add (SpanClass G A B) where
  add := Quotient.map₂ RawSpan.sum (by
    rintro S S' ⟨e⟩ T T' ⟨f⟩
    exact ⟨RawSpan.Equiv.sumCongr e f⟩)

instance : AddCommMonoid (SpanClass G A B) where
  zero := 0
  add := (· + ·)
  zero_add S := by
    induction S using Quotient.inductionOn
    exact Quotient.sound ⟨RawSpan.zeroSumEquiv _⟩
  add_zero S := by
    induction S using Quotient.inductionOn
    exact Quotient.sound ⟨RawSpan.sumZeroEquiv _⟩
  add_assoc S T U := by
    induction S using Quotient.inductionOn
    induction T using Quotient.inductionOn
    induction U using Quotient.inductionOn
    exact Quotient.sound ⟨RawSpan.sumAssocEquiv _ _ _⟩
  add_comm S T := by
    induction S using Quotient.inductionOn
    induction T using Quotient.inductionOn
    exact Quotient.sound ⟨RawSpan.sumCommEquiv _ _⟩
  nsmul := nsmulRec
  nsmul_zero _ := rfl
  nsmul_succ _ _ := rfl

@[simp]
theorem comp_zero (S : SpanClass G A B) :
    SpanClass.comp S (0 : SpanClass G B C) = 0 := by
  induction S using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.compZeroEquiv _⟩

@[simp]
theorem zero_comp (T : SpanClass G B C) :
    SpanClass.comp (0 : SpanClass G A B) T = 0 := by
  induction T using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.zeroCompEquiv _⟩

theorem add_comp (S T : SpanClass G A B) (U : SpanClass G B C) :
    SpanClass.comp (S + T) U = SpanClass.comp S U + SpanClass.comp T U := by
  induction S using Quotient.inductionOn
  induction T using Quotient.inductionOn
  induction U using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.sumCompEquiv _ _ _⟩

theorem comp_add (S : SpanClass G A B) (T U : SpanClass G B C) :
    SpanClass.comp S (T + U) = SpanClass.comp S T + SpanClass.comp S U := by
  induction S using Quotient.inductionOn
  induction T using Quotient.inductionOn
  induction U using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.compSumEquiv _ _ _⟩

end SpanClass

/-- An additive hom out of a Grothendieck completion is determined by its
values on the original commutative monoid. -/
theorem grothendieckHom_ext {M N : Type*} [AddCommMonoid M] [AddCommGroup N]
    {f g : Algebra.GrothendieckAddGroup M →+ N}
    (h : ∀ m, f (Algebra.GrothendieckAddGroup.of m) =
      g (Algebra.GrothendieckAddGroup.of m)) : f = g := by
  apply (Algebra.GrothendieckAddGroup.lift (M := M) (G := N)).symm.injective
  ext m
  exact h m

@[simp]
theorem grothendieckLift_of {M N : Type*} [AddCommMonoid M] [AddCommGroup N]
    (f : M →+ N) (m : M) :
    Algebra.GrothendieckAddGroup.lift f
        (Algebra.GrothendieckAddGroup.of m) = f m := by
  have h := (Algebra.GrothendieckAddGroup.lift (M := M) (G := N)).symm_apply_apply f
  exact DFunLike.congr_fun h m

/-- Formal differences of equivariant-span classes. -/
abbrev BurnsideSpanHom (A B : FiniteAction.{u, u} G) :=
  Algebra.GrothendieckAddGroup (GroupActionSpanCategory.SpanClass G A B)

namespace BurnsideSpanHom

variable {G} {A B C D : FiniteAction.{u, u} G}

/-- Include an actual equivariant span class as an additive generator. -/
def of (S : GroupActionSpanCategory.SpanClass G A B) : BurnsideSpanHom G A B :=
  Algebra.GrothendieckAddGroup.of S

/-- For a fixed right span generator, pullback composition is additive in the
left completed hom-group. -/
def compLeftGenerator (T : GroupActionSpanCategory.SpanClass G B C) :
    GroupActionSpanCategory.SpanClass G A B →+ BurnsideSpanHom G A C where
  toFun S := of (GroupActionSpanCategory.SpanClass.comp S T)
  map_zero' := by simp [of, GroupActionBurnsideSpanCategory.SpanClass.zero_comp]
  map_add' S U := by
    change Algebra.GrothendieckAddGroup.of
        (GroupActionSpanCategory.SpanClass.comp (S + U) T) = _
    rw [GroupActionBurnsideSpanCategory.SpanClass.add_comp]
    exact map_add _ _ _

/-- Extend composition by a fixed right span generator across the left
Grothendieck completion. -/
def compLeft (T : GroupActionSpanCategory.SpanClass G B C) :
    BurnsideSpanHom G A B →+ BurnsideSpanHom G A C :=
  Algebra.GrothendieckAddGroup.lift (compLeftGenerator T)

/-- Span-generator composition is itself additive in the right variable. -/
def compositionGenerator :
    GroupActionSpanCategory.SpanClass G B C →+
      (BurnsideSpanHom G A B →+ BurnsideSpanHom G A C) where
  toFun := compLeft
  map_zero' := by
    apply grothendieckHom_ext
    intro S
    unfold compLeft
    rw [grothendieckLift_of]
    change of (GroupActionSpanCategory.SpanClass.comp S 0) = 0
    rw [GroupActionBurnsideSpanCategory.SpanClass.comp_zero]
    exact map_zero _
  map_add' T U := by
    apply grothendieckHom_ext
    intro S
    unfold compLeft
    rw [grothendieckLift_of]
    change (compLeftGenerator (T + U)) S =
      Algebra.GrothendieckAddGroup.lift (compLeftGenerator T)
          (Algebra.GrothendieckAddGroup.of S) +
        Algebra.GrothendieckAddGroup.lift (compLeftGenerator U)
          (Algebra.GrothendieckAddGroup.of S)
    rw [grothendieckLift_of, grothendieckLift_of]
    change of (GroupActionSpanCategory.SpanClass.comp S (T + U)) =
      of (GroupActionSpanCategory.SpanClass.comp S T) +
        of (GroupActionSpanCategory.SpanClass.comp S U)
    rw [GroupActionBurnsideSpanCategory.SpanClass.comp_add]
    exact map_add _ _ _

/-- Extend the right span variable across its Grothendieck completion. The
result assigns to each completed right morphism an additive operator on
completed left morphisms. -/
def compositionOperator : BurnsideSpanHom G B C →+
    (BurnsideSpanHom G A B →+ BurnsideSpanHom G A C) :=
  Algebra.GrothendieckAddGroup.lift compositionGenerator

/-- Bilinear pullback composition of formal differences of span classes. -/
def comp (S : BurnsideSpanHom G A B) (T : BurnsideSpanHom G B C) :
    BurnsideSpanHom G A C := compositionOperator T S

/-- Composition by a fixed right morphism is additive. -/
def compLeftHom (T : BurnsideSpanHom G B C) :
    BurnsideSpanHom G A B →+ BurnsideSpanHom G A C :=
  compositionOperator T

/-- Composition by a fixed left morphism is additive. -/
def compRightHom (S : BurnsideSpanHom G A B) :
    BurnsideSpanHom G B C →+ BurnsideSpanHom G A C where
  toFun T := comp S T
  map_zero' := by simp [comp, compositionOperator]
  map_add' T U := by simp [comp, compositionOperator]

@[simp]
theorem comp_of_of (S : GroupActionSpanCategory.SpanClass G A B)
    (T : GroupActionSpanCategory.SpanClass G B C) :
    comp (of S) (of T) = of (GroupActionSpanCategory.SpanClass.comp S T) := by
  unfold comp compositionOperator
  unfold of
  rw [grothendieckLift_of]
  change compLeft T (Algebra.GrothendieckAddGroup.of S) = _
  unfold compLeft
  rw [grothendieckLift_of]
  rfl

/-- The completed identity span is a left unit. -/
theorem id_comp (T : BurnsideSpanHom G A B) :
    comp (of (GroupActionSpanCategory.SpanClass.of (RawSpan.identity A))) T = T := by
  have h : compRightHom
      (of (GroupActionSpanCategory.SpanClass.of (RawSpan.identity A))) =
      AddMonoidHom.id (BurnsideSpanHom G A B) := by
    apply grothendieckHom_ext
    intro S
    change comp (of (GroupActionSpanCategory.SpanClass.of (RawSpan.identity A)))
      (of S) = of S
    rw [comp_of_of, GroupActionSpanCategory.SpanClass.id_comp]
  exact DFunLike.congr_fun h T

/-- The completed identity span is a right unit. -/
theorem comp_id (S : BurnsideSpanHom G A B) :
    comp S (of (GroupActionSpanCategory.SpanClass.of (RawSpan.identity B))) = S := by
  have h : compLeftHom
      (of (GroupActionSpanCategory.SpanClass.of (RawSpan.identity B))) =
      AddMonoidHom.id (BurnsideSpanHom G A B) := by
    apply grothendieckHom_ext
    intro T
    change comp (of T)
      (of (GroupActionSpanCategory.SpanClass.of (RawSpan.identity B))) = of T
    rw [comp_of_of, GroupActionSpanCategory.SpanClass.comp_id]
  exact DFunLike.congr_fun h S

/-- Bilinear completed pullback composition is associative. -/
theorem assoc (S : BurnsideSpanHom G A B) (T : BurnsideSpanHom G B C)
    (U : BurnsideSpanHom G C D) :
    comp (comp S T) U = comp S (comp T U) := by
  have hU : compRightHom (C := D) (comp S T) =
      (compRightHom (C := D) S).comp (compRightHom (C := D) T) := by
    apply grothendieckHom_ext
    intro U₀
    have hT : (compLeftHom (of U₀)).comp (compRightHom S) =
        (compRightHom S).comp (compLeftHom (of U₀)) := by
      apply grothendieckHom_ext
      intro T₀
      have hS : (compLeftHom (A := A) (of U₀)).comp
          (compLeftHom (A := A) (of T₀)) =
          compLeftHom (A := A) (comp (of T₀) (of U₀)) := by
        apply grothendieckHom_ext
        intro S₀
        change comp (comp (of S₀) (of T₀)) (of U₀) =
          comp (of S₀) (comp (of T₀) (of U₀))
        rw [comp_of_of, comp_of_of, comp_of_of, comp_of_of]
        exact congrArg of (GroupActionSpanCategory.SpanClass.assoc S₀ T₀ U₀)
      exact DFunLike.congr_fun hS S
    exact DFunLike.congr_fun hT T
  exact DFunLike.congr_fun hU U

end BurnsideSpanHom

/-- Objects of the preadditive Burnside span category. -/
abbrev AdditiveBurnsideSpanObject := FiniteAction.{u, u} G

namespace AdditiveBurnsideSpanObject

instance : Category (AdditiveBurnsideSpanObject G) where
  Hom := BurnsideSpanHom G
  id A := BurnsideSpanHom.of
    (GroupActionSpanCategory.SpanClass.of (RawSpan.identity A))
  comp := BurnsideSpanHom.comp
  id_comp := BurnsideSpanHom.id_comp
  comp_id := BurnsideSpanHom.comp_id
  assoc := BurnsideSpanHom.assoc

instance homAddCommGroup (A B : AdditiveBurnsideSpanObject G) :
    AddCommGroup (A ⟶ B) := by
  change AddCommGroup (BurnsideSpanHom G A B)
  infer_instance

instance : Preadditive (AdditiveBurnsideSpanObject G) where
  homGroup := fun _ _ => inferInstance
  add_comp := by
    intro A B C S T U
    exact (BurnsideSpanHom.compLeftHom U).map_add S T
  comp_add := by
    intro A B C S T U
    exact (BurnsideSpanHom.compRightHom S).map_add T U

/-- Include an arbitrary span class as a positive morphism generator. -/
def spanHom {A B : AdditiveBurnsideSpanObject G}
    (S : GroupActionSpanCategory.SpanClass G A B) : A ⟶ B :=
  BurnsideSpanHom.of S

/-- Include an equivariant map by its graph span. -/
def graphHom {A B : AdditiveBurnsideSpanObject G}
    (f : ActionMap G A B) : A ⟶ B :=
  spanHom (G := G) (GroupActionSpanCategory.SpanClass.of (RawSpan.graph f))

/-- Include the transfer direction of an equivariant map by its converse
graph span, without assuming invertibility. -/
def converseGraphHom {A B : AdditiveBurnsideSpanObject G}
    (f : ActionMap G A B) : B ⟶ A :=
  spanHom (G := G)
    (GroupActionSpanCategory.SpanClass.of (RawSpan.converseGraph f))

/-- Graph-span generators preserve ordinary equivariant-map composition. -/
theorem graph_composition {A B C : AdditiveBurnsideSpanObject G}
    (f : ActionMap G A B) (g : ActionMap G B C) :
    graphHom (G := G) f ≫ graphHom (G := G) g =
      graphHom (G := G) (RawSpan.composeMap f g) := by
  unfold graphHom spanHom
  change BurnsideSpanHom.comp _ _ = _
  rw [BurnsideSpanHom.comp_of_of,
    GroupActionSpanCategory.SpanClass.graph_comp]

/-- The completed category laws and both distributivity laws hold together. -/
theorem preadditive_category_laws (A B C D : AdditiveBurnsideSpanObject G)
    (S S' : A ⟶ B) (T T' : B ⟶ C) (U : C ⟶ D) :
    (𝟙 A ≫ S = S) ∧ (S ≫ 𝟙 B = S) ∧
      ((S ≫ T) ≫ U = S ≫ T ≫ U) ∧
      ((S + S') ≫ T = S ≫ T + S' ≫ T) ∧
      (S ≫ (T + T') = S ≫ T + S ≫ T') := by
  exact ⟨Category.id_comp S, Category.comp_id S, Category.assoc S T U,
    Preadditive.add_comp A B C S S' T, Preadditive.comp_add A B C S T T'⟩

end AdditiveBurnsideSpanObject

end

end GroupActionBurnsideSpanCategory
end GUFormalization
