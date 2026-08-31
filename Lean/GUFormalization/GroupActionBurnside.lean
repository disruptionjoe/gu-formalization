import GUFormalization.GroupActionAdditiveEnvelope
import Mathlib.GroupTheory.MonoidLocalization.GrothendieckGroup

/-!
# Burnside groups of finite supplied actions

This file constructs the additive Burnside group of finite supplied actions.
Finite actions are first identified up to equivariant equivalence.  Disjoint
coproduct is then made into commutative addition, and the Grothendieck group
formally supplies additive inverses.

The construction is pure group-action algebra.  It is not a physical
representation category, source-native action, observed sector, family
selector, mass model, or Geometric Unity claim.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionBurnside

noncomputable section

universe u v

variable (H : Type u) [Group H]

/-- A finite type equipped with a supplied left `H`-action. -/
structure FiniteAction where
  carrier : Type v
  fintype : Fintype carrier
  action : MulAction H carrier

namespace FiniteAction

instance (A : FiniteAction H) : Fintype A.carrier := A.fintype
instance (A : FiniteAction H) : MulAction H A.carrier := A.action

/-- An equivariant equivalence of finite supplied actions. -/
structure Equiv (A B : FiniteAction H) where
  toEquiv : A.carrier ≃ B.carrier
  map_smul' : ∀ (h : H) (a : A.carrier), toEquiv (h • a) = h • toEquiv a

@[refl]
def Equiv.refl (A : FiniteAction H) : Equiv H A A where
  toEquiv := _root_.Equiv.refl _
  map_smul' _ _ := rfl

@[symm]
def Equiv.symm {A B : FiniteAction H} (e : Equiv H A B) : Equiv H B A where
  toEquiv := e.toEquiv.symm
  map_smul' h b := by
    apply e.toEquiv.injective
    rw [e.toEquiv.apply_symm_apply, e.map_smul', e.toEquiv.apply_symm_apply]

@[trans]
def Equiv.trans {A B C : FiniteAction H} (e : Equiv H A B)
    (f : Equiv H B C) : Equiv H A C where
  toEquiv := e.toEquiv.trans f.toEquiv
  map_smul' h a := by
    change f.toEquiv (e.toEquiv (h • a)) = h • f.toEquiv (e.toEquiv a)
    rw [e.map_smul', f.map_smul']

/-- Forget an equivariant equivalence to an equivariant map. -/
def Equiv.toEquivariantMap {A B : FiniteAction H} (e : Equiv H A B) :
    @GroupActionFixedPoints.EquivariantMap H A.carrier B.carrier _
      inferInstance inferInstance :=
  ⟨e.toEquiv, e.map_smul'⟩

/-- The empty finite action. -/
def empty : FiniteAction H where
  carrier := PEmpty
  fintype := inferInstance
  action := {
    smul := fun _ x => PEmpty.elim x
    one_smul := fun x => PEmpty.elim x
    mul_smul := fun _ _ x => PEmpty.elim x
  }

/-- Disjoint coproduct of finite supplied actions. -/
abbrev sum (A B : FiniteAction H) : FiniteAction H where
  carrier := A.carrier ⊕ B.carrier
  fintype := inferInstance
  action := {
    smul h x := x.elim (fun a => Sum.inl (h • a)) (fun b => Sum.inr (h • b))
    one_smul x := by
      cases x with
      | inl a => exact congrArg Sum.inl (A.action.one_smul a)
      | inr b => exact congrArg Sum.inr (B.action.one_smul b)
    mul_smul h k x := by
      cases x with
      | inl a => exact congrArg Sum.inl (A.action.mul_smul h k a)
      | inr b => exact congrArg Sum.inr (B.action.mul_smul h k b)
  }

/-- Equivariant equivalences are preserved by disjoint coproduct. -/
def Equiv.sumCongr {A A' B B' : FiniteAction H}
    (e : Equiv H A A') (f : Equiv H B B') :
    Equiv H (sum H A B) (sum H A' B') where
  toEquiv := _root_.Equiv.sumCongr e.toEquiv f.toEquiv
  map_smul' h x := by
    cases x with
    | inl a => exact congrArg Sum.inl (e.map_smul' h a)
    | inr b => exact congrArg Sum.inr (f.map_smul' h b)

/-- The empty action is a left unit for disjoint coproduct. -/
def emptySumEquiv (A : FiniteAction H) : Equiv H (sum H (empty H) A) A where
  toEquiv := {
    toFun := Sum.elim PEmpty.elim id
    invFun := Sum.inr
    left_inv := by
      intro x
      cases x with
      | inl e => exact PEmpty.elim e
      | inr a => rfl
    right_inv := fun _ => rfl
  }
  map_smul' _ x := by
    cases x with
    | inl e => exact PEmpty.elim e
    | inr a => rfl

/-- The empty action is a right unit for disjoint coproduct. -/
def sumEmptyEquiv (A : FiniteAction H) : Equiv H (sum H A (empty H)) A where
  toEquiv := {
    toFun := Sum.elim id PEmpty.elim
    invFun := Sum.inl
    left_inv := by
      intro x
      cases x with
      | inl a => rfl
      | inr e => exact PEmpty.elim e
    right_inv := fun _ => rfl
  }
  map_smul' _ x := by
    cases x with
    | inl a => rfl
    | inr e => exact PEmpty.elim e

/-- Disjoint coproduct is associative up to equivariant equivalence. -/
def sumAssocEquiv (A B C : FiniteAction H) :
    Equiv H (sum H (sum H A B) C) (sum H A (sum H B C)) where
  toEquiv := _root_.Equiv.sumAssoc A.carrier B.carrier C.carrier
  map_smul' _ x := by cases x with
    | inl ab => cases ab <;> rfl
    | inr c => rfl

/-- Disjoint coproduct is commutative up to equivariant equivalence. -/
def sumCommEquiv (A B : FiniteAction H) :
    Equiv H (sum H A B) (sum H B A) where
  toEquiv := _root_.Equiv.sumComm A.carrier B.carrier
  map_smul' _ x := by cases x <;> rfl

end FiniteAction

/-- Equivariant equivalence is the isomorphism relation used to form finite
action classes. -/
def finiteActionSetoid : Setoid (FiniteAction H) where
  r A B := Nonempty (FiniteAction.Equiv H A B)
  iseqv := {
    refl := fun A => ⟨FiniteAction.Equiv.refl H A⟩
    symm := fun ⟨e⟩ => ⟨e.symm⟩
    trans := fun ⟨e⟩ ⟨f⟩ => ⟨FiniteAction.Equiv.trans H e f⟩
  }

instance finiteActionSetoidInst : Setoid (FiniteAction H) :=
  finiteActionSetoid H

/-- Isomorphism classes of finite supplied `H`-actions. -/
def BurnsideMonoid := Quotient (finiteActionSetoid H)

namespace BurnsideMonoid

/-- The class of a finite supplied action. -/
def of (A : FiniteAction H) : BurnsideMonoid H := Quotient.mk' A

instance : Zero (BurnsideMonoid H) := ⟨of H (FiniteAction.empty H)⟩

instance : Add (BurnsideMonoid H) where
  add := Quotient.map₂ (FiniteAction.sum H) (by
    rintro A A' ⟨e⟩ B B' ⟨f⟩
    exact ⟨FiniteAction.Equiv.sumCongr H e f⟩)

set_option linter.checkUnivs false in
theorem of_sum (A B : FiniteAction H) :
    of H (FiniteAction.sum H A B) = of H A + of H B := rfl

instance : AddCommMonoid (BurnsideMonoid H) where
  zero := 0
  add := (· + ·)
  zero_add x := by
    induction x using Quotient.inductionOn
    exact Quotient.sound ⟨FiniteAction.emptySumEquiv H _⟩
  add_zero x := by
    induction x using Quotient.inductionOn
    exact Quotient.sound ⟨FiniteAction.sumEmptyEquiv H _⟩
  add_assoc x y z := by
    induction x using Quotient.inductionOn
    induction y using Quotient.inductionOn
    induction z using Quotient.inductionOn
    exact Quotient.sound ⟨FiniteAction.sumAssocEquiv H _ _ _⟩
  add_comm x y := by
    induction x using Quotient.inductionOn
    induction y using Quotient.inductionOn
    exact Quotient.sound ⟨FiniteAction.sumCommEquiv H _ _⟩
  nsmul := nsmulRec
  nsmul_zero _ := rfl
  nsmul_succ _ _ := rfl

end BurnsideMonoid

/-- The additive Burnside group: group completion of finite action classes
under disjoint coproduct. -/
abbrev BurnsideGroup := Algebra.GrothendieckAddGroup (BurnsideMonoid H)

/-- Include a finite supplied action in its Burnside group. -/
def burnsideOf (A : FiniteAction.{u, v} H) : BurnsideGroup H :=
  Algebra.GrothendieckAddGroup.of (BurnsideMonoid.of H A)

/-! ## Restriction -/

open GroupActionChangeOfGroups GroupActionFixedPoints

universe w

variable {K : Type w} [Group K]

/-- Restrict a finite supplied action along a group homomorphism. -/
def FiniteAction.restrict (phi : H →* K) (A : FiniteAction K) :
    FiniteAction H where
  carrier := A.carrier
  fintype := A.fintype
  action := restrictedMulAction (A := A.carrier) phi

/-- Restriction preserves equivariant equivalence. -/
def FiniteAction.Equiv.restrict (phi : H →* K)
    {A B : FiniteAction K} (e : FiniteAction.Equiv K A B) :
    FiniteAction.Equiv H (A.restrict H phi) (B.restrict H phi) where
  toEquiv := e.toEquiv
  map_smul' h a := e.map_smul' (phi h) a

/-- Restriction on finite action classes. -/
def restrictionMonoidMap (phi : H →* K) : BurnsideMonoid K → BurnsideMonoid H :=
  Quotient.map (FiniteAction.restrict H phi) (by
    rintro A B ⟨e⟩
    exact ⟨e.restrict H phi⟩)

@[simp]
theorem restrictionMonoidMap_of (phi : H →* K) (A : FiniteAction K) :
    restrictionMonoidMap H phi (BurnsideMonoid.of K A) =
      BurnsideMonoid.of H (A.restrict H phi) := rfl

/-- Restriction preserves the empty action and disjoint coproduct. -/
def restrictionMonoidHom (phi : H →* K) :
    BurnsideMonoid K →+ BurnsideMonoid H where
  toFun := restrictionMonoidMap H phi
  map_zero' := rfl
  map_add' x y := by
    induction x using Quotient.inductionOn
    induction y using Quotient.inductionOn
    rfl

/-- Restriction on generators, now valued in the target Burnside group. -/
def restrictionGeneratorHom (phi : H →* K) :
    BurnsideMonoid K →+ BurnsideGroup H where
  toFun x := Algebra.GrothendieckAddGroup.of (restrictionMonoidHom H phi x)
  map_zero' := by simp
  map_add' x y := by simp

/-- Restriction on additive Burnside groups. -/
def restriction (phi : H →* K) : BurnsideGroup K →+ BurnsideGroup H :=
  Algebra.GrothendieckAddGroup.lift (restrictionGeneratorHom H phi)

@[simp]
theorem restriction_of (phi : H →* K) (A : FiniteAction K) :
    restriction H phi (burnsideOf K A) = burnsideOf H (A.restrict H phi) := by
  have h := (Algebra.GrothendieckAddGroup.lift.symm_apply_apply
    (restrictionGeneratorHom H phi))
  exact DFunLike.congr_fun h (BurnsideMonoid.of K A)

/-! ## Subgroup induction -/

open GroupActionInduction GroupActionMackey

variable {G : Type u} [Group G] [Finite G]

/-- Induce a finite supplied subgroup action to the ambient finite group. -/
def FiniteAction.induce (L : Subgroup G) (A : FiniteAction.{u, u} L) :
    FiniteAction.{u, u} G where
  carrier := SubgroupInducedCarrier L A.carrier
  fintype := Fintype.ofFinite _
  action := inducedMulAction L.subtype

/-- Induction preserves equivariant equivalence. -/
def FiniteAction.Equiv.induce (L : Subgroup G)
    {A B : FiniteAction.{u, u} L} (e : FiniteAction.Equiv L A B) :
    FiniteAction.Equiv G (A.induce L) (B.induce L) where
  toEquiv := {
    toFun := inducedMap L.subtype e.toEquivariantMap
    invFun := inducedMap L.subtype e.symm.toEquivariantMap
    left_inv := by
      intro x
      induction x using Quotient.inductionOn'
      case _ p =>
        change inducedMk L.subtype p.1
            (e.toEquiv.symm (e.toEquiv p.2)) = inducedMk L.subtype p.1 p.2
        rw [e.toEquiv.symm_apply_apply]
    right_inv := by
      intro x
      induction x using Quotient.inductionOn'
      case _ p =>
        change inducedMk L.subtype p.1
            (e.toEquiv (e.toEquiv.symm p.2)) = inducedMk L.subtype p.1 p.2
        rw [e.toEquiv.apply_symm_apply]
  }
  map_smul' g x := inducedMap_equivariant L.subtype e.toEquivariantMap g x

/-- The induced action of a disjoint coproduct is equivariantly equivalent to
the disjoint coproduct of the induced actions. -/
def FiniteAction.induceSumEquiv (L : Subgroup G)
    (A B : FiniteAction.{u, u} L) :
    FiniteAction.Equiv G ((FiniteAction.sum L A B).induce L)
      (FiniteAction.sum G (A.induce L) (B.induce L)) := by
  letI sumAction : MulAction L (A.carrier ⊕ B.carrier) :=
    (FiniteAction.sum L A B).action
  letI sourcePairAction := inductionPairMulAction
    (B := (FiniteAction.sum L A B).carrier) L.subtype
  letI leftPairAction := inductionPairMulAction (B := A.carrier) L.subtype
  letI rightPairAction := inductionPairMulAction (B := B.carrier) L.subtype
  let toFun : SubgroupInducedCarrier L (FiniteAction.sum L A B).carrier →
      SubgroupInducedCarrier L A.carrier ⊕ SubgroupInducedCarrier L B.carrier :=
    fun q => Quotient.liftOn' q (fun p => p.2.elim
      (fun a => Sum.inl (inducedMk L.subtype p.1 a))
      (fun b => Sum.inr (inducedMk L.subtype p.1 b))) (by
        intro p q hpq
        change ∃ h : L, sourcePairAction.smul h q = p at hpq
        rcases hpq with ⟨h, hpq⟩
        subst p
        rcases q with ⟨g, x⟩
        cases x with
        | inl a =>
            change Sum.inl
                (inducedMk L.subtype (g * (L.subtype h)⁻¹) (h • a)) =
              Sum.inl (inducedMk L.subtype g a)
            apply congrArg Sum.inl
            apply Quotient.sound
            exact ⟨h, rfl⟩
        | inr b =>
            change Sum.inr
                (inducedMk L.subtype (g * (L.subtype h)⁻¹) (h • b)) =
              Sum.inr (inducedMk L.subtype g b)
            apply congrArg Sum.inr
            apply Quotient.sound
            exact ⟨h, rfl⟩)
  let invFun : SubgroupInducedCarrier L A.carrier ⊕
      SubgroupInducedCarrier L B.carrier →
      SubgroupInducedCarrier L (FiniteAction.sum L A B).carrier :=
    Sum.elim
      (fun q => Quotient.liftOn' q
        (fun p => inducedMk L.subtype p.1 (Sum.inl p.2)) (by
          intro p q hpq
          change ∃ h : L, leftPairAction.smul h q = p at hpq
          rcases hpq with ⟨h, rfl⟩
          apply Quotient.sound
          exact ⟨h, rfl⟩))
      (fun q => Quotient.liftOn' q
        (fun p => inducedMk L.subtype p.1 (Sum.inr p.2)) (by
          intro p q hpq
          change ∃ h : L, rightPairAction.smul h q = p at hpq
          rcases hpq with ⟨h, rfl⟩
          apply Quotient.sound
          exact ⟨h, rfl⟩))
  exact {
    toEquiv := {
      toFun := toFun
      invFun := invFun
      left_inv := by
        intro q
        induction q using Quotient.inductionOn'
        case _ p =>
          rcases p with ⟨g, x⟩
          cases x <;> rfl
      right_inv := by
        intro q
        cases q with
        | inl q => induction q using Quotient.inductionOn' with
          | _ p => rfl
        | inr q => induction q using Quotient.inductionOn' with
          | _ p => rfl
    }
    map_smul' := by
      intro g q
      induction q using Quotient.inductionOn'
      case _ p =>
        rcases p with ⟨x, s⟩
        cases s with
        | inl a =>
            change Sum.inl (inducedMk L.subtype (g * x) a) =
              Sum.inl (@SMul.smul G (SubgroupInducedCarrier L A.carrier)
                (inducedMulAction L.subtype).toSMul g
                (inducedMk L.subtype x a))
            exact congrArg Sum.inl (induced_smul_mk L.subtype g x a).symm
        | inr b =>
            change Sum.inr (inducedMk L.subtype (g * x) b) =
              Sum.inr (@SMul.smul G (SubgroupInducedCarrier L B.carrier)
                (inducedMulAction L.subtype).toSMul g
                (inducedMk L.subtype x b))
            exact congrArg Sum.inr (induced_smul_mk L.subtype g x b).symm
  }

/-- Subgroup induction on finite action classes. -/
def inductionMonoidMap (L : Subgroup G) :
    BurnsideMonoid L → BurnsideMonoid G :=
  Quotient.map (FiniteAction.induce L) (by
    rintro A B ⟨e⟩
    exact ⟨e.induce L⟩)

/-- Subgroup induction preserves empty actions and disjoint coproduct. -/
def inductionMonoidHom (L : Subgroup G) :
    BurnsideMonoid L →+ BurnsideMonoid G where
  toFun := inductionMonoidMap L
  map_zero' := by
    letI emptyAction : MulAction L PEmpty.{u + 1} :=
      (FiniteAction.empty.{u, u} L).action
    letI emptyPairAction := inductionPairMulAction (B := PEmpty.{u + 1}) L.subtype
    apply Quotient.sound
    refine ⟨{
      toEquiv := {
        toFun := fun q : SubgroupInducedCarrier L PEmpty.{u + 1} =>
          Quotient.liftOn' q (fun p : G × PEmpty.{u + 1} => PEmpty.elim p.2)
            (by intro p; exact PEmpty.elim p.2)
        invFun := fun e : PEmpty.{u + 1} => PEmpty.elim e
        left_inv := by intro q; induction q using Quotient.inductionOn' with
          | _ p => exact PEmpty.elim p.2
        right_inv := by intro e; exact PEmpty.elim e
      }
      map_smul' := by intro _ q; induction q using Quotient.inductionOn' with
        | _ p => exact PEmpty.elim p.2
    }⟩
  map_add' x y := by
    induction x using Quotient.inductionOn
    induction y using Quotient.inductionOn
    exact Quotient.sound ⟨FiniteAction.induceSumEquiv _ _ _⟩

/-- Subgroup induction on additive Burnside groups. -/
def inductionGeneratorHom (L : Subgroup G) :
    BurnsideMonoid L →+ BurnsideGroup G where
  toFun x := Algebra.GrothendieckAddGroup.of (inductionMonoidHom L x)
  map_zero' := by simp
  map_add' x y := by simp

/-- Subgroup induction on additive Burnside groups. -/
def induction (L : Subgroup G) : BurnsideGroup L →+ BurnsideGroup G :=
  Algebra.GrothendieckAddGroup.lift (inductionGeneratorHom L)

@[simp]
theorem induction_of (L : Subgroup G) (A : FiniteAction.{u, u} L) :
    induction L (burnsideOf L A) = burnsideOf G (A.induce L) := by
  have h := (Algebra.GrothendieckAddGroup.lift.symm_apply_apply
    (inductionGeneratorHom L))
  exact DFunLike.congr_fun h (BurnsideMonoid.of L A)

/-- Equivariantly equivalent finite actions define the same Burnside-group
class. -/
theorem burnsideOf_eq_of_equiv {A B : FiniteAction.{u, u} G}
    (e : FiniteAction.Equiv G A B) : burnsideOf G A = burnsideOf G B := by
  apply congrArg Algebra.GrothendieckAddGroup.of
  exact Quotient.sound ⟨e⟩

/-! ## The additive double-coset identity -/

/-- Restrict an induced finite `G`-action to a subgroup `K`. -/
def restrictedInducedFiniteAction (K L : Subgroup G)
    (A : FiniteAction.{u, u} L) : FiniteAction.{u, u} K :=
  (A.induce L).restrict K K.subtype

/-- The finite dependent coproduct of the transported-intersection induction
summands in the subgroup Mackey formula.  Its outer sigma coordinate is the
finite double-coset space `K \\ G / L`; each fiber is the corresponding
induced conjugate seed action. -/
def mackeyCoproductFiniteAction (K L : Subgroup G)
    (A : FiniteAction.{u, u} L) : FiniteAction.{u, u} K where
  carrier := MackeyCoproductCarrier K L A.carrier
  fintype := Fintype.ofFinite _
  action := mackeyCoproductMulAction K L A.carrier

/-- The set-level Mackey assembly is an equivariant equivalence from the
finite double-coset coproduct to restricted induction. -/
def mackeyCoproductFiniteActionEquiv (K L : Subgroup G)
    (A : FiniteAction.{u, u} L) :
    FiniteAction.Equiv K (mackeyCoproductFiniteAction K L A)
      (restrictedInducedFiniteAction K L A) where
  toEquiv := mackeyCoproductEquivRestrictedInduced K L
  map_smul' k x :=
    mackeyCoproductEquivRestrictedInduced_equivariant K L k x

/-- Additive Mackey double-coset identity on every finite supplied action.

The left side is restriction after transfer/induction.  The right side is the
Burnside-group class of the finite dependent coproduct over `K \\ G / L`, whose
fiber at a representative `g` is induction to `K` from
`K ∩ g L g⁻¹` of the conjugated seed action.  Because Burnside addition is
disjoint coproduct followed by Grothendieck completion, this is exactly the
coproduct-as-sum form of the Mackey law. -/
theorem restriction_induction_of_eq_mackeyCoproduct
    (K L : Subgroup G) (A : FiniteAction.{u, u} L) :
    restriction K K.subtype (induction L (burnsideOf L A)) =
      burnsideOf K (mackeyCoproductFiniteAction K L A) := by
  rw [induction_of, restriction_of]
  exact (burnsideOf_eq_of_equiv
    (mackeyCoproductFiniteActionEquiv K L A)).symm

end

end GroupActionBurnside
end GUFormalization
