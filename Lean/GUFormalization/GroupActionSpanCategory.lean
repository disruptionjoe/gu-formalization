import GUFormalization.GroupActionBurnside
import Mathlib.CategoryTheory.Category.Basic

/-!
# The category of finite supplied-action spans

This file constructs a category whose objects are finite supplied `G`-actions
and whose morphisms are arbitrary equivariant spans, identified up
to equivariant isomorphism of their apex. Composition is the finite equivariant
pullback. Explicit unitors and an associator prove the category laws after
passing to span-isomorphism classes.

No separate categorical universal property is asserted. The construction is
pure finite group-action algebra. It supplies no physical
representation, source-native action, observed sector, selector, dynamics,
prediction, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionSpanCategory

noncomputable section

open CategoryTheory
open GroupActionBurnside
open GroupActionFixedPoints

universe u

variable (G : Type u) [Group G]

/-- Equivariant maps between two finite supplied actions. -/
abbrev ActionMap (A B : FiniteAction.{u, u} G) :=
  @EquivariantMap G A.carrier B.carrier _ inferInstance inferInstance

/-- An arbitrary equivariant span between finite supplied actions. -/
structure RawSpan (A B : FiniteAction.{u, u} G) where
  apex : FiniteAction.{u, u} G
  left : ActionMap G apex A
  right : ActionMap G apex B

namespace RawSpan

variable {G} {A B C D : FiniteAction.{u, u} G}

/-- Equivariant isomorphism of span apices, commuting with both legs. -/
structure Equiv (S T : RawSpan G A B) where
  apexEquiv : FiniteAction.Equiv G S.apex T.apex
  left_comm : ∀ x, T.left.1 (apexEquiv.toEquiv x) = S.left.1 x
  right_comm : ∀ x, T.right.1 (apexEquiv.toEquiv x) = S.right.1 x

namespace Equiv

@[refl]
def refl (S : RawSpan G A B) : RawSpan.Equiv S S where
  apexEquiv := FiniteAction.Equiv.refl G S.apex
  left_comm _ := rfl
  right_comm _ := rfl

@[symm]
def symm {S T : RawSpan G A B} (e : RawSpan.Equiv S T) : RawSpan.Equiv T S where
  apexEquiv := e.apexEquiv.symm
  left_comm y := by
    change S.left.1 (e.apexEquiv.toEquiv.symm y) = T.left.1 y
    have h := e.left_comm (e.apexEquiv.toEquiv.symm y)
    simpa using h.symm
  right_comm y := by
    change S.right.1 (e.apexEquiv.toEquiv.symm y) = T.right.1 y
    have h := e.right_comm (e.apexEquiv.toEquiv.symm y)
    simpa using h.symm

@[trans]
def trans {S T U : RawSpan G A B} (e : RawSpan.Equiv S T)
    (f : RawSpan.Equiv T U) : RawSpan.Equiv S U where
  apexEquiv := FiniteAction.Equiv.trans G e.apexEquiv f.apexEquiv
  left_comm x := by
    change U.left.1 (f.apexEquiv.toEquiv (e.apexEquiv.toEquiv x)) = S.left.1 x
    rw [f.left_comm, e.left_comm]
  right_comm x := by
    change U.right.1 (f.apexEquiv.toEquiv (e.apexEquiv.toEquiv x)) = S.right.1 x
    rw [f.right_comm, e.right_comm]

end Equiv

/-- The identity span. -/
def identity (A : FiniteAction.{u, u} G) : RawSpan G A A where
  apex := A
  left := ⟨id, by intro _ _; rfl⟩
  right := ⟨id, by intro _ _; rfl⟩

/-- Composition of supplied equivariant maps. -/
def composeMap (f : ActionMap G A B) (g : ActionMap G B C) : ActionMap G A C :=
  ⟨fun x => g.1 (f.1 x), by
    intro h x
    change g.1 (f.1 (h • x)) = h • g.1 (f.1 x)
    rw [f.2, g.2]⟩

/-- The graph span of an equivariant map. -/
def graph (f : ActionMap G A B) : RawSpan G A B where
  apex := A
  left := ⟨id, by intro _ _; rfl⟩
  right := f

/-- The converse graph supplies the transfer-direction span of an equivariant
map without claiming that the map itself has an inverse. -/
def converseGraph (f : ActionMap G A B) : RawSpan G B A where
  apex := A
  left := f
  right := ⟨id, by intro _ _; rfl⟩

/-- The diagonal action on the pullback apex used to compose two spans. -/
def pullbackAction (S : RawSpan G A B) (T : RawSpan G B C) :
    FiniteAction.{u, u} G where
  carrier := {p : S.apex.carrier × T.apex.carrier //
    S.right.1 p.1 = T.left.1 p.2}
  fintype := Fintype.ofFinite _
  action := {
    smul := fun g p => ⟨(g • p.1.1, g • p.1.2), by
      change S.right.1 (g • p.1.1) = T.left.1 (g • p.1.2)
      rw [S.right.2, T.left.2, p.2]⟩
    one_smul := by
      intro p
      apply Subtype.ext
      exact Prod.ext (one_smul _ _) (one_smul _ _)
    mul_smul := by
      intro g h p
      apply Subtype.ext
      exact Prod.ext (mul_smul g h p.1.1) (mul_smul g h p.1.2)
  }

/-- Pullback composition of equivariant spans. -/
def comp (S : RawSpan G A B) (T : RawSpan G B C) : RawSpan G A C where
  apex := pullbackAction S T
  left := ⟨fun p => S.left.1 p.1.1, by intro g p; exact S.left.2 g p.1.1⟩
  right := ⟨fun p => T.right.1 p.1.2, by intro g p; exact T.right.2 g p.1.2⟩

/-- Pullback composition respects equivariant isomorphism of both input spans. -/
def compEquiv {S S' : RawSpan G A B} {T T' : RawSpan G B C}
    (e : RawSpan.Equiv S S') (f : RawSpan.Equiv T T') :
    RawSpan.Equiv (comp S T) (comp S' T') where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => ⟨(e.apexEquiv.toEquiv p.1.1,
          f.apexEquiv.toEquiv p.1.2), by
        calc
          S'.right.1 (e.apexEquiv.toEquiv p.1.1) = S.right.1 p.1.1 := e.right_comm _
          _ = T.left.1 p.1.2 := p.2
          _ = T'.left.1 (f.apexEquiv.toEquiv p.1.2) := (f.left_comm _).symm⟩
      invFun := fun p => ⟨(e.apexEquiv.toEquiv.symm p.1.1,
          f.apexEquiv.toEquiv.symm p.1.2), by
        have he := e.right_comm (e.apexEquiv.toEquiv.symm p.1.1)
        have hf := f.left_comm (f.apexEquiv.toEquiv.symm p.1.2)
        rw [e.apexEquiv.toEquiv.apply_symm_apply] at he
        rw [f.apexEquiv.toEquiv.apply_symm_apply] at hf
        exact he.symm.trans (p.2.trans hf)⟩
      left_inv := by
        intro p
        apply Subtype.ext
        exact Prod.ext (e.apexEquiv.toEquiv.symm_apply_apply p.1.1)
          (f.apexEquiv.toEquiv.symm_apply_apply p.1.2)
      right_inv := by
        intro p
        apply Subtype.ext
        exact Prod.ext (e.apexEquiv.toEquiv.apply_symm_apply p.1.1)
          (f.apexEquiv.toEquiv.apply_symm_apply p.1.2)
    }
    map_smul' := by
      intro g p
      apply Subtype.ext
      exact Prod.ext (e.apexEquiv.map_smul' g p.1.1)
        (f.apexEquiv.map_smul' g p.1.2)
  }
  left_comm p := e.left_comm p.1.1
  right_comm p := f.right_comm p.1.2

/-- Pullback composition of graph spans is the graph of map composition. -/
def graphCompEquiv (f : ActionMap G A B) (g : ActionMap G B C) :
    RawSpan.Equiv (comp (graph f) (graph g)) (graph (composeMap f g)) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => p.1.1
      invFun := fun x => ⟨(x, f.1 x), rfl⟩
      left_inv := by intro p; apply Subtype.ext; exact Prod.ext rfl p.2
      right_inv := fun _ => rfl
    }
    map_smul' := fun _ _ => rfl
  }
  left_comm _ := rfl
  right_comm p := congrArg g.1 p.2

/-- Left identity up to equivariant apex isomorphism. -/
def identityCompEquiv (S : RawSpan G A B) :
    RawSpan.Equiv (comp (identity A) S) S where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => p.1.2
      invFun := fun x => ⟨(S.left.1 x, x), rfl⟩
      left_inv := by intro p; apply Subtype.ext; exact Prod.ext p.2.symm rfl
      right_inv := fun _ => rfl
    }
    map_smul' := fun _ _ => rfl
  }
  left_comm p := p.2.symm
  right_comm _ := rfl

/-- Right identity up to equivariant apex isomorphism. -/
def compIdentityEquiv (S : RawSpan G A B) :
    RawSpan.Equiv (comp S (identity B)) S where
  apexEquiv := {
    toEquiv := {
      toFun := fun p => p.1.1
      invFun := fun x => ⟨(x, S.right.1 x), rfl⟩
      left_inv := by intro p; apply Subtype.ext; exact Prod.ext rfl p.2
      right_inv := fun _ => rfl
    }
    map_smul' := fun _ _ => rfl
  }
  left_comm _ := rfl
  right_comm p := p.2

/-- Pullback composition is associative up to the canonical reassociation of
the two nested pullback apices. -/
def assocEquiv (S : RawSpan G A B) (T : RawSpan G B C)
    (U : RawSpan G C D) :
    RawSpan.Equiv (comp (comp S T) U) (comp S (comp T U)) where
  apexEquiv := {
    toEquiv := {
      toFun := fun p =>
        ⟨(p.1.1.1.1, ⟨(p.1.1.1.2, p.1.2), p.2⟩), p.1.1.2⟩
      invFun := fun p =>
        ⟨(⟨(p.1.1, p.1.2.1.1), p.2⟩, p.1.2.1.2), p.1.2.2⟩
      left_inv := by intro p; rfl
      right_inv := by intro p; rfl
    }
    map_smul' := fun _ _ => rfl
  }
  left_comm _ := rfl
  right_comm _ := rfl

end RawSpan

/-- Setoid of arbitrary spans under equivariant isomorphism of their apices. -/
def spanSetoid (A B : FiniteAction.{u, u} G) : Setoid (RawSpan G A B) where
  r S T := Nonempty (RawSpan.Equiv S T)
  iseqv := {
    refl := fun S => ⟨RawSpan.Equiv.refl S⟩
    symm := fun ⟨e⟩ => ⟨e.symm⟩
    trans := fun ⟨e⟩ ⟨f⟩ => ⟨e.trans f⟩
  }

instance spanSetoidInst (A B : FiniteAction.{u, u} G) : Setoid (RawSpan G A B) :=
  spanSetoid G A B

/-- Isomorphism classes of arbitrary finite equivariant spans. -/
def SpanClass (A B : FiniteAction.{u, u} G) := Quotient (spanSetoid G A B)

namespace SpanClass

variable {G} {A B C D : FiniteAction.{u, u} G}

/-- Include a raw span in its isomorphism class. -/
def of (S : RawSpan G A B) : SpanClass G A B := Quotient.mk' S

/-- Compose span classes by equivariant pullback. -/
def comp : SpanClass G A B → SpanClass G B C → SpanClass G A C :=
  Quotient.map₂ RawSpan.comp (by
    rintro S S' ⟨e⟩ T T' ⟨f⟩
    exact ⟨RawSpan.compEquiv e f⟩)

theorem id_comp (S : SpanClass G A B) :
    comp (of (RawSpan.identity A)) S = S := by
  induction S using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.identityCompEquiv _⟩

theorem comp_id (S : SpanClass G A B) :
    comp S (of (RawSpan.identity B)) = S := by
  induction S using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.compIdentityEquiv _⟩

theorem assoc (S : SpanClass G A B) (T : SpanClass G B C)
    (U : SpanClass G C D) :
    comp (comp S T) U = comp S (comp T U) := by
  induction S using Quotient.inductionOn
  induction T using Quotient.inductionOn
  induction U using Quotient.inductionOn
  exact Quotient.sound ⟨RawSpan.assocEquiv _ _ _⟩

theorem graph_comp (f : ActionMap G A B) (g : ActionMap G B C) :
    comp (of (RawSpan.graph f)) (of (RawSpan.graph g)) =
      of (RawSpan.graph (RawSpan.composeMap f g)) :=
  Quotient.sound ⟨RawSpan.graphCompEquiv f g⟩

end SpanClass

/-- Objects of the finite supplied-action span category. -/
def BurnsideSpanObject := FiniteAction.{u, u} G

namespace BurnsideSpanObject

instance : Category (BurnsideSpanObject G) where
  Hom := SpanClass G
  id A := SpanClass.of (RawSpan.identity A)
  comp S T := SpanClass.comp S T
  id_comp := SpanClass.id_comp
  comp_id := SpanClass.comp_id
  assoc := SpanClass.assoc

/-- The quotient really supplies a category: identity and composition are the
identity span and finite equivariant pullback, respectively. -/
theorem category_laws (A B C D : BurnsideSpanObject G)
    (S : A ⟶ B) (T : B ⟶ C) (U : C ⟶ D) :
    (𝟙 A ≫ S = S) ∧ (S ≫ 𝟙 B = S) ∧ ((S ≫ T) ≫ U = S ≫ T ≫ U) := by
  exact ⟨Category.id_comp S, Category.comp_id S, Category.assoc S T U⟩

/-- Include an equivariant map as its graph morphism. -/
def graphHom {A B : BurnsideSpanObject G} (f : ActionMap G A B) : A ⟶ B :=
  SpanClass.of (RawSpan.graph f)

/-- Equivariant maps embed by graph spans and compose as ordinary maps. -/
theorem graph_composition {A B C : BurnsideSpanObject G}
    (f : ActionMap G A B) (g : ActionMap G B C) :
    graphHom (G := G) f ≫ graphHom (G := G) g =
      graphHom (G := G) (RawSpan.composeMap f g) :=
  SpanClass.graph_comp f g

end BurnsideSpanObject

end

end GroupActionSpanCategory
end GUFormalization
