import GUFormalization.GroupActionMackeyRepresentations
import Mathlib.RepresentationTheory.Rep.Basic

/-!
# Categorical naturality of the canonical Mackey decomposition

The representative-free Mackey carrier construction and restricted induction
are functors from supplied `H`-actions to supplied `K`-actions.  Canonical
assembly is a natural isomorphism between those functors.  Applying Mathlib's
standard linearization functor gives the corresponding natural isomorphism of
free permutation representations.

This is categorical algebra on supplied set actions.  It does not construct a
physical action, an additive Mackey functor with transfer data, a coupling, or
an observable.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionMackeyCategory

open GroupActionFixedPoints GroupActionInduction GroupActionMackey
open CategoryTheory

universe u v w

variable {G : Type u} [Group G]

/-- Regard a morphism of bundled supplied actions as the repository's explicit
equivariant-map type. -/
def actionHomEquivariantMap {H : Type u} [Group H]
    {B C : Action (Type v) H} (f : B ⟶ C) :
    @EquivariantMap H B.V C.V _ (Action.instMulAction C)
      (Action.instMulAction B) :=
  ⟨f.hom, by
    intro h b
    exact ConcreteCategory.congr_hom (f.comm h) b⟩

/-- Composition in the action category agrees with ordinary composition of
the underlying equivariant maps. -/
theorem actionHomEquivariantMap_comp {H : Type u} [Group H]
    {B C D : Action (Type v) H} (f : B ⟶ C) (g : C ⟶ D) :
    actionHomEquivariantMap (f ≫ g) =
      (⟨(actionHomEquivariantMap g).1 ∘ (actionHomEquivariantMap f).1, by
        letI : MulAction H B.V := Action.instMulAction B
        letI : MulAction H C.V := Action.instMulAction C
        letI : MulAction H D.V := Action.instMulAction D
        intro h b
        change (actionHomEquivariantMap g).1
            ((actionHomEquivariantMap f).1 (h • b)) =
          h • (actionHomEquivariantMap g).1
            ((actionHomEquivariantMap f).1 b)
        rw [(actionHomEquivariantMap f).2, (actionHomEquivariantMap g).2]⟩ :
        @EquivariantMap H B.V D.V _ (Action.instMulAction D)
          (Action.instMulAction B)) := by
  rfl

/-- The representative-free dependent coproduct of intrinsic Mackey fibers,
bundled as a supplied `K`-action. -/
noncomputable abbrev canonicalMackeyAction (K H : Subgroup G)
    (B : Action (Type v) H) : Action (Type max u v) K := by
  letI : MulAction H B.V := Action.instMulAction B
  letI : MulAction K (CanonicalMackeyCoproductCarrier K H B.V) :=
    canonicalMackeyCoproductMulAction K H B.V
  exact Action.ofMulAction K (CanonicalMackeyCoproductCarrier K H B.V)

/-- Restricted induction, bundled as a supplied `K`-action. -/
noncomputable abbrev restrictedInducedAction (K H : Subgroup G)
    (B : Action (Type v) H) : Action (Type max u v) K := by
  letI : MulAction H B.V := Action.instMulAction B
  letI : MulAction K (SubgroupInducedCarrier H B.V) :=
    restrictedSubgroupInducedMulAction K H B.V
  exact Action.ofMulAction K (SubgroupInducedCarrier H B.V)

/-- The action morphism induced fiberwise by a supplied equivariant seed map. -/
noncomputable def canonicalMackeyActionMap (K H : Subgroup G)
    {B C : Action (Type v) H} (f : B ⟶ C) :
    canonicalMackeyAction K H B ⟶ canonicalMackeyAction K H C := by
  letI : MulAction H B.V := Action.instMulAction B
  letI : MulAction H C.V := Action.instMulAction C
  let ef := actionHomEquivariantMap f
  exact
    { hom := by
        dsimp [canonicalMackeyAction]
        exact ↾canonicalMackeyCoproductMap K H ef
      comm := fun k => by
        ext x
        exact canonicalMackeyCoproductMap_equivariant K H ef k x }

/-- The action morphism on restricted induction induced by a supplied
equivariant seed map. -/
noncomputable def restrictedInducedActionMap (K H : Subgroup G)
    {B C : Action (Type v) H} (f : B ⟶ C) :
    restrictedInducedAction K H B ⟶ restrictedInducedAction K H C := by
  letI : MulAction H B.V := Action.instMulAction B
  letI : MulAction H C.V := Action.instMulAction C
  let ef := actionHomEquivariantMap f
  exact
    { hom := by
        dsimp [restrictedInducedAction]
        exact ↾inducedMap H.subtype ef
      comm := fun k => by
        ext x
        exact inducedMap_equivariant H.subtype ef (k : G) x }

/-- The representative-free Mackey coproduct is functorial in supplied
`H`-equivariant seed maps. -/
noncomputable abbrev canonicalMackeyActionFunctor (K H : Subgroup G) :
    Action (Type v) H ⥤ Action (Type max u v) K where
  obj B := canonicalMackeyAction K H B
  map f := canonicalMackeyActionMap K H f
  map_id B := by
    letI : MulAction H B.V := Action.instMulAction B
    apply Action.hom_ext
    ext x
    change canonicalMackeyCoproductMap K H (actionHomEquivariantMap (𝟙 B)) x = x
    exact canonicalMackeyCoproductMap_id K H x
  map_comp {B C D} f g := by
    letI : MulAction H B.V := Action.instMulAction B
    letI : MulAction H C.V := Action.instMulAction C
    letI : MulAction H D.V := Action.instMulAction D
    apply Action.hom_ext
    ext x
    change canonicalMackeyCoproductMap K H
        (actionHomEquivariantMap (f ≫ g)) x =
      canonicalMackeyCoproductMap K H (actionHomEquivariantMap g)
        (canonicalMackeyCoproductMap K H (actionHomEquivariantMap f) x)
    apply (canonicalMackeyCoproductEquivRestrictedInduced K H).injective
    rw [canonicalMackeyCoproduct_naturality,
      canonicalMackeyCoproduct_naturality,
      canonicalMackeyCoproduct_naturality,
      actionHomEquivariantMap_comp]
    exact (inducedMap_comp H.subtype (actionHomEquivariantMap f)
      (actionHomEquivariantMap g)
      (canonicalMackeyCoproductEquivRestrictedInduced K H x)).symm

/-- Restricted induction is functorial in supplied `H`-equivariant seed maps. -/
noncomputable abbrev restrictedInducedActionFunctor (K H : Subgroup G) :
    Action (Type v) H ⥤ Action (Type max u v) K where
  obj B := restrictedInducedAction K H B
  map f := restrictedInducedActionMap K H f
  map_id B := by
    letI : MulAction H B.V := Action.instMulAction B
    apply Action.hom_ext
    ext x
    change inducedMap H.subtype (actionHomEquivariantMap (𝟙 B)) x = x
    exact inducedMap_id H.subtype x
  map_comp {B C D} f g := by
    letI : MulAction H B.V := Action.instMulAction B
    letI : MulAction H C.V := Action.instMulAction C
    letI : MulAction H D.V := Action.instMulAction D
    apply Action.hom_ext
    ext x
    change inducedMap H.subtype (actionHomEquivariantMap (f ≫ g)) x =
      inducedMap H.subtype (actionHomEquivariantMap g)
        (inducedMap H.subtype (actionHomEquivariantMap f) x)
    rw [actionHomEquivariantMap_comp]
    exact (inducedMap_comp H.subtype (actionHomEquivariantMap f)
      (actionHomEquivariantMap g) x).symm

/-- Canonical assembly is an isomorphism of the supplied `K`-actions. -/
noncomputable abbrev canonicalMackeyActionIso (K H : Subgroup G)
    (B : Action (Type v) H) :
    canonicalMackeyAction K H B ≅ restrictedInducedAction K H B := by
  letI : MulAction H B.V := Action.instMulAction B
  exact Action.mkIso
    (canonicalMackeyCoproductEquivRestrictedInduced K H).toIso
    (fun k => by
      ext x
      exact canonicalMackeyCoproductEquivRestrictedInduced_equivariant K H k x)

/-- The representative-free Mackey decomposition is natural in every supplied
equivariant seed map. -/
noncomputable def canonicalMackeyActionNatIso (K H : Subgroup G) :
    canonicalMackeyActionFunctor K H ≅ restrictedInducedActionFunctor K H :=
  NatIso.ofComponents (canonicalMackeyActionIso K H) (fun {B C} f => by
    letI : MulAction H B.V := Action.instMulAction B
    letI : MulAction H C.V := Action.instMulAction C
    apply Action.hom_ext
    ext x
    change canonicalMackeyCoproductEquivRestrictedInduced K H
        (canonicalMackeyCoproductMap K H (actionHomEquivariantMap f) x) =
      inducedMap H.subtype (actionHomEquivariantMap f)
        (canonicalMackeyCoproductEquivRestrictedInduced K H x)
    exact canonicalMackeyCoproduct_naturality K H
      (actionHomEquivariantMap f) x)

/-- Applying the standard free-linearization functor transports the complete
set-action natural isomorphism to a natural isomorphism of `K`-representations. -/
noncomputable def canonicalMackeyRepresentationNatIso
    (R : Type w) [CommRing R] (K H : Subgroup G) :
    canonicalMackeyActionFunctor K H ⋙ Rep.linearization R K ≅
      restrictedInducedActionFunctor K H ⋙ Rep.linearization R K :=
  Functor.isoWhiskerRight (canonicalMackeyActionNatIso K H)
    (Rep.linearization R K)

end GroupActionMackeyCategory
end GUFormalization
