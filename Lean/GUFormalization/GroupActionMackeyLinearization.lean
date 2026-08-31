import GUFormalization.GroupActionMackey
import Mathlib.LinearAlgebra.Finsupp.LSum

/-!
# Free-module linearization of the canonical Mackey carrier

The set-level canonical Mackey equivalence can be lifted without adding any
representation-theoretic choices: apply the free finitely supported `R`-module
functor to both carriers.  The resulting linear equivalence preserves basis
vectors, intertwines the linearizations of equivariant seed maps, and commutes
with the explicitly supplied `K`-actions.

This is an algebraic free-module statement.  It does not construct an additive
Mackey functor on physical representations, a source-native action, a coupling,
or a selector.
-/

namespace GUFormalization
namespace GroupActionMackeyLinearization

open GroupActionFixedPoints GroupActionInduction GroupActionMackey

universe u v w

variable {G : Type u} [Group G]
variable (R : Type w) [Semiring R]

/-- The free `R`-module on a type, represented by finitely supported
coefficient functions. -/
abbrev FreeModule (X : Type v) := X →₀ R

/-- Functorial linearization of a map of basis types. -/
noncomputable def linearizeMap {X Y : Type v} (f : X → Y) :
    FreeModule R X →ₗ[R] FreeModule R Y :=
  Finsupp.lmapDomain R R f

@[simp]
theorem linearizeMap_single {X Y : Type v} (f : X → Y) (x : X) (r : R) :
    linearizeMap R f (Finsupp.single x r) = Finsupp.single (f x) r := by
  simp [linearizeMap]

theorem linearizeMap_comp {X Y Z : Type v} (f : X → Y) (g : Y → Z) :
    linearizeMap R (g ∘ f) =
      (linearizeMap R g).comp (linearizeMap R f) := by
  exact Finsupp.lmapDomain_comp R R f g

/-- The canonical representative-free Mackey carrier equivalence lifted to
free modules. -/
noncomputable def canonicalMackeyFreeLinearEquiv (K H : Subgroup G)
    {B : Type v} [MulAction H B] :
    FreeModule R (CanonicalMackeyCoproductCarrier K H B) ≃ₗ[R]
      FreeModule R (SubgroupInducedCarrier H B) :=
  Finsupp.mapDomain.linearEquiv R R
    (canonicalMackeyCoproductEquivRestrictedInduced K H)

/-- The lift sends every canonical Mackey basis vector to the basis vector of
its assembled restricted-induced class. -/
@[simp]
theorem canonicalMackeyFreeLinearEquiv_single (K H : Subgroup G)
    {B : Type v} [MulAction H B]
    (x : CanonicalMackeyCoproductCarrier K H B) (r : R) :
    canonicalMackeyFreeLinearEquiv R K H (Finsupp.single x r) =
      Finsupp.single (canonicalMackeyCoproductEquivRestrictedInduced K H x) r := by
  simp [canonicalMackeyFreeLinearEquiv]

/-- Linearization preserves the set-level naturality square for every
equivariant seed map. -/
theorem canonicalMackeyFreeLinearEquiv_naturality (K H : Subgroup G)
    {B C : Type v} [MulAction H B] [MulAction H C]
    (f : @EquivariantMap H B C _ inferInstance inferInstance) :
    (canonicalMackeyFreeLinearEquiv R K H).toLinearMap.comp
        (linearizeMap R (canonicalMackeyCoproductMap K H f)) =
      (linearizeMap R (inducedMap H.subtype f)).comp
        (canonicalMackeyFreeLinearEquiv R K H).toLinearMap := by
  change
    (linearizeMap R (canonicalMackeyCoproductEquivRestrictedInduced K H)).comp
        (linearizeMap R (canonicalMackeyCoproductMap K H f)) =
      (linearizeMap R (inducedMap H.subtype f)).comp
        (linearizeMap R (canonicalMackeyCoproductEquivRestrictedInduced K H))
  rw [← linearizeMap_comp, ← linearizeMap_comp]
  apply congrArg (linearizeMap R)
  funext x
  exact canonicalMackeyCoproduct_naturality K H f x

/-- The free-module lift also intertwines the supplied left `K`-actions after
those action maps are linearized. -/
theorem canonicalMackeyFreeLinearEquiv_equivariant (K H : Subgroup G)
    {B : Type v} [MulAction H B] (k : K) :
    (canonicalMackeyFreeLinearEquiv R K H).toLinearMap.comp
        (linearizeMap R fun x : CanonicalMackeyCoproductCarrier K H B =>
          @SMul.smul K (CanonicalMackeyCoproductCarrier K H B)
            (canonicalMackeyCoproductMulAction K H B).toSMul k x) =
      (linearizeMap R fun x : SubgroupInducedCarrier H B =>
          @SMul.smul K (SubgroupInducedCarrier H B)
            (restrictedSubgroupInducedMulAction K H B).toSMul k x).comp
        (canonicalMackeyFreeLinearEquiv R K H).toLinearMap := by
  change
    (linearizeMap R (canonicalMackeyCoproductEquivRestrictedInduced K H)).comp
        (linearizeMap R fun x : CanonicalMackeyCoproductCarrier K H B =>
          @SMul.smul K (CanonicalMackeyCoproductCarrier K H B)
            (canonicalMackeyCoproductMulAction K H B).toSMul k x) =
      (linearizeMap R fun x : SubgroupInducedCarrier H B =>
          @SMul.smul K (SubgroupInducedCarrier H B)
            (restrictedSubgroupInducedMulAction K H B).toSMul k x).comp
        (linearizeMap R (canonicalMackeyCoproductEquivRestrictedInduced K H))
  rw [← linearizeMap_comp, ← linearizeMap_comp]
  apply congrArg (linearizeMap R)
  funext x
  exact canonicalMackeyCoproductEquivRestrictedInduced_equivariant K H k x

/-- Reindexing by the canonical Mackey equivalence preserves the exact number
of nonzero basis coefficients. -/
theorem canonicalMackeyFreeLinearEquiv_support_card (K H : Subgroup G)
    {B : Type v} [MulAction H B]
    (x : FreeModule R (CanonicalMackeyCoproductCarrier K H B)) :
    (canonicalMackeyFreeLinearEquiv R K H x).support.card = x.support.card := by
  classical
  change
    (Finsupp.mapDomain (canonicalMackeyCoproductEquivRestrictedInduced K H) x).support.card =
      x.support.card
  rw [Finsupp.mapDomain_support_of_injective
    (canonicalMackeyCoproductEquivRestrictedInduced K H).injective]
  exact Finset.card_image_of_injective x.support
    (canonicalMackeyCoproductEquivRestrictedInduced K H).injective

end GroupActionMackeyLinearization
end GUFormalization
