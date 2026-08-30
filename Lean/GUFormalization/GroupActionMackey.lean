import GUFormalization.GroupActionInductionCoherence

/-!
# The first Mackey interface for set-level subgroup induction

For subgroups `H K ≤ G`, induction of the one-point `H`-set is the right
coset carrier `G / H`.  Restricting its action to `K` and then taking
`K`-orbits gives the double-coset quotient `K \ G / H`.  This file proves
that identification by explicit quotient maps and identifies the stabilizer
of the induced class of `g` with the transported intersection condition

`k * g = g * h` for some `h : H`.

The left-right action is fixed explicitly as `(k,h) • g = k * g * h⁻¹`.
All actions are named non-instances.  These are pure set-level laws for
supplied subgroup actions; they construct no physical action, carrier,
observer, selector, dynamics, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionMackey

open GroupActionChangeOfGroups GroupActionInduction

variable {G : Type*} [Group G]

/-- The one-point action used to identify subgroup induction with a coset
carrier.  It is named explicitly rather than installed globally. -/
@[implicit_reducible]
def pointMulAction (H : Subgroup G) : MulAction H PUnit where
  smul _ _ := PUnit.unit
  one_smul _ := rfl
  mul_smul _ _ _ := rfl

/-- The induced `G`-set `G ×_H PUnit`. -/
abbrev SubgroupInducedPointCarrier (H : Subgroup G) :=
  @InducedCarrier H G PUnit inferInstance inferInstance (pointMulAction H)
    H.subtype

/-- The explicit left `G`-action on `G ×_H PUnit`. -/
@[implicit_reducible]
def subgroupInducedPointMulAction (H : Subgroup G) :
    MulAction G (SubgroupInducedPointCarrier H) :=
  @inducedMulAction H G PUnit inferInstance inferInstance (pointMulAction H)
    H.subtype

/-- Restrict the induced point carrier from `G` to the subgroup `K`. -/
@[implicit_reducible]
def restrictedSubgroupInducedPointMulAction (K H : Subgroup G) :
    MulAction K (SubgroupInducedPointCarrier H) :=
  @restrictedMulAction K G (SubgroupInducedPointCarrier H) inferInstance
    inferInstance (subgroupInducedPointMulAction H) K.subtype

/-- The orbit quotient of the restricted induced point carrier. -/
abbrev RestrictedInducedPointOrbitCarrier (K H : Subgroup G) :=
  @MulAction.orbitRel.Quotient K (SubgroupInducedPointCarrier H)
    inferInstance (restrictedSubgroupInducedPointMulAction K H)

/-- The left-right action whose orbits are double cosets.  The inverse on the
right subgroup is forced by the product multiplication law. -/
@[implicit_reducible]
def doubleCosetMulAction (K H : Subgroup G) : MulAction (K × H) G where
  smul kh g := (kh.1 : G) * g * (kh.2 : G)⁻¹
  one_smul g := by
    change (1 : G) * g * (1 : G)⁻¹ = g
    simp
  mul_smul kh lm g := by
    change
      (((kh.1 * lm.1 : K) : G) * g * (((kh.2 * lm.2 : H) : G))⁻¹) =
        (kh.1 : G) * ((lm.1 : G) * g * (lm.2 : G)⁻¹) * (kh.2 : G)⁻¹
    simp [mul_assoc]

/-- The double-coset carrier `K \ G / H`, represented as one orbit quotient
for the explicit `K × H` action. -/
abbrev DoubleCosetCarrier (K H : Subgroup G) :=
  @MulAction.orbitRel.Quotient (K × H) G inferInstance
    (doubleCosetMulAction K H)

/-- The double coset of `g`. -/
def doubleCosetMk (K H : Subgroup G) (g : G) : DoubleCosetCarrier K H :=
  @Quotient.mk'' G
    (@MulAction.orbitRel (K × H) G inferInstance
      (doubleCosetMulAction K H)) g

/-- The `K`-orbit of the induced point represented by `g`. -/
def restrictedInducedPointOrbitMk (K H : Subgroup G) (g : G) :
    RestrictedInducedPointOrbitCarrier K H :=
  @Quotient.mk'' (SubgroupInducedPointCarrier H)
    (@MulAction.orbitRel K (SubgroupInducedPointCarrier H) inferInstance
      (restrictedSubgroupInducedPointMulAction K H))
    (@inducedMk H G PUnit inferInstance inferInstance (pointMulAction H)
      H.subtype g PUnit.unit)

/-- Passing from the nested right-`H`, then left-`K`, quotient to the single
`K × H` orbit quotient. -/
def restrictedInducedPointOrbitsToDoubleCoset (K H : Subgroup G) :
    RestrictedInducedPointOrbitCarrier K H → DoubleCosetCarrier K H := by
  letI pointAction := pointMulAction H
  letI pairAction := inductionPairMulAction (B := PUnit) H.subtype
  letI inducedAction := subgroupInducedPointMulAction H
  letI restrictedAction := restrictedSubgroupInducedPointMulAction K H
  letI doubleAction := doubleCosetMulAction K H
  intro q
  exact Quotient.liftOn' q
    (fun inner => Quotient.liftOn' inner
      (fun p : G × PUnit => doubleCosetMk K H p.1) (by
        intro a b hab
        rw [MulAction.orbitRel_apply] at hab
        rcases hab with ⟨h, hab⟩
        rw [← hab]
        apply Quotient.sound
        refine ⟨(1, h), ?_⟩
        exact show (1 : G) * b.1 * (h : G)⁻¹ = b.1 * (h : G)⁻¹ by
          simp)) (by
      intro a b hab
      rw [MulAction.orbitRel_apply] at hab
      rcases hab with ⟨k, hab⟩
      rw [← hab]
      induction b using Quotient.inductionOn'
      case _ p =>
        apply Quotient.sound
        refine ⟨(k, 1), ?_⟩
        change (k : G) * p.1 * (1 : G)⁻¹ = (k : G) * p.1
        simp)

/-- Passing from the single double-coset quotient back to the nested orbit
quotient. -/
def doubleCosetToRestrictedInducedPointOrbits (K H : Subgroup G) :
    DoubleCosetCarrier K H → RestrictedInducedPointOrbitCarrier K H := by
  letI pointAction := pointMulAction H
  letI pairAction := inductionPairMulAction (B := PUnit) H.subtype
  letI inducedAction := subgroupInducedPointMulAction H
  letI restrictedAction := restrictedSubgroupInducedPointMulAction K H
  letI doubleAction := doubleCosetMulAction K H
  intro q
  exact Quotient.liftOn' q (restrictedInducedPointOrbitMk K H) (by
    intro a b hab
    rw [MulAction.orbitRel_apply] at hab
    rcases hab with ⟨kh, hab⟩
    rw [← hab]
    apply Quotient.sound
    refine ⟨kh.1, ?_⟩
    change
      @SMul.smul K (SubgroupInducedPointCarrier H) restrictedAction.toSMul
          kh.1
          (@inducedMk H G PUnit inferInstance inferInstance pointAction
            H.subtype b PUnit.unit) =
        @inducedMk H G PUnit inferInstance inferInstance pointAction
          H.subtype ((kh.1 : G) * b * (kh.2 : G)⁻¹) PUnit.unit
    rw [show
      @SMul.smul K (SubgroupInducedPointCarrier H) restrictedAction.toSMul
          kh.1
          (@inducedMk H G PUnit inferInstance inferInstance pointAction
            H.subtype b PUnit.unit) =
        @inducedMk H G PUnit inferInstance inferInstance pointAction
          H.subtype ((kh.1 : G) * b) PUnit.unit by
      exact induced_smul_mk H.subtype (kh.1 : G) b PUnit.unit]
    simpa [mul_assoc] using
      (inducedMk_mul_phi H.subtype
        ((kh.1 : G) * b * (kh.2 : G)⁻¹) kh.2 PUnit.unit))

/-- The `K`-orbits of the restricted point induction are exactly the double
cosets `K \ G / H`.  Both quotient directions and inverse laws are explicit. -/
def restrictedInducedPointOrbitEquivDoubleCoset (K H : Subgroup G) :
    RestrictedInducedPointOrbitCarrier K H ≃ DoubleCosetCarrier K H where
  toFun := restrictedInducedPointOrbitsToDoubleCoset K H
  invFun := doubleCosetToRestrictedInducedPointOrbits K H
  left_inv q := by
    letI := pointMulAction H
    letI := inductionPairMulAction (B := PUnit) H.subtype
    letI := subgroupInducedPointMulAction H
    letI := restrictedSubgroupInducedPointMulAction K H
    letI := doubleCosetMulAction K H
    induction q using Quotient.inductionOn'
    case _ inner =>
      induction inner using Quotient.inductionOn'
      case _ p => rfl
  right_inv q := by
    letI := pointMulAction H
    letI := inductionPairMulAction (B := PUnit) H.subtype
    letI := subgroupInducedPointMulAction H
    letI := restrictedSubgroupInducedPointMulAction K H
    letI := doubleCosetMulAction K H
    induction q using Quotient.inductionOn'
    case _ g => rfl

@[simp]
theorem restrictedInducedPointOrbitEquivDoubleCoset_mk
    (K H : Subgroup G) (g : G) :
    restrictedInducedPointOrbitEquivDoubleCoset K H
        (restrictedInducedPointOrbitMk K H g) =
      doubleCosetMk K H g :=
  rfl

/-- The subgroup of `K` transported from the intersection with `gHg⁻¹`,
written in a division-free form that exposes the exact witness equation. -/
def transportedIntersection (K H : Subgroup G) (g : G) : Subgroup K where
  carrier := {k | ∃ h : H, (k : G) * g = g * (h : G)}
  one_mem' := ⟨1, by simp⟩
  mul_mem' := by
    rintro k l ⟨h, hk⟩ ⟨j, hl⟩
    refine ⟨h * j, ?_⟩
    change ((k * l : K) : G) * g = g * (((h * j : H) : G))
    calc
      ((k * l : K) : G) * g = (k : G) * ((l : G) * g) := by
        simp [mul_assoc]
      _ = (k : G) * (g * (j : G)) := by rw [hl]
      _ = ((k : G) * g) * (j : G) := by rw [mul_assoc]
      _ = (g * (h : G)) * (j : G) := by rw [hk]
      _ = g * (((h * j : H) : G)) := by simp [mul_assoc]
  inv_mem' := by
    rintro k ⟨h, hk⟩
    refine ⟨h⁻¹, ?_⟩
    have moved := congrArg
      (fun x : G => (k : G)⁻¹ * x * (h : G)⁻¹) hk
    change ((k⁻¹ : K) : G) * g = g * (((h⁻¹ : H) : G))
    simpa [mul_assoc] using moved.symm

/-- The stabilizer condition on a representative of the restricted induced
point carrier.  Equality of quotient classes is unpacked to an actual
subgroup witness; no cardinality argument is used. -/
theorem restrictedInducedPoint_stabilizer_iff (K H : Subgroup G)
    (k : K) (g : G) :
    @SMul.smul K (SubgroupInducedPointCarrier H)
        (restrictedSubgroupInducedPointMulAction K H).toSMul k
        (@inducedMk H G PUnit inferInstance inferInstance (pointMulAction H)
          H.subtype g PUnit.unit) =
      @inducedMk H G PUnit inferInstance inferInstance (pointMulAction H)
        H.subtype g PUnit.unit ↔
      ∃ h : H, (k : G) * g = g * (h : G) := by
  letI pointAction := pointMulAction H
  letI pairAction := inductionPairMulAction (B := PUnit) H.subtype
  letI inducedAction := subgroupInducedPointMulAction H
  letI restrictedAction := restrictedSubgroupInducedPointMulAction K H
  constructor
  · intro hfix
    change
      @inducedMk H G PUnit inferInstance inferInstance pointAction H.subtype
          ((k : G) * g) PUnit.unit =
        @inducedMk H G PUnit inferInstance inferInstance pointAction H.subtype
          g PUnit.unit at hfix
    obtain ⟨h, hp⟩ := Quotient.exact hfix
    change (g * (h : G)⁻¹, PUnit.unit) = ((k : G) * g, PUnit.unit) at hp
    refine ⟨h⁻¹, ?_⟩
    simpa using congrArg Prod.fst hp.symm
  · rintro ⟨h, hkg⟩
    change
      @inducedMk H G PUnit inferInstance inferInstance pointAction H.subtype
          ((k : G) * g) PUnit.unit =
        @inducedMk H G PUnit inferInstance inferInstance pointAction H.subtype
          g PUnit.unit
    rw [hkg]
    simpa using inducedMk_mul_phi H.subtype g h PUnit.unit

/-- The abstract action stabilizer is exactly the transported subgroup
intersection used by the Mackey summand indexed by `g`. -/
theorem stabilizer_restrictedInducedPoint_eq_transportedIntersection
    (K H : Subgroup G) (g : G) :
    @MulAction.stabilizer K (SubgroupInducedPointCarrier H) inferInstance
        (restrictedSubgroupInducedPointMulAction K H)
        (@inducedMk H G PUnit inferInstance inferInstance (pointMulAction H)
          H.subtype g PUnit.unit) =
      transportedIntersection K H g := by
  letI := pointMulAction H
  letI := inductionPairMulAction (B := PUnit) H.subtype
  letI := subgroupInducedPointMulAction H
  letI := restrictedSubgroupInducedPointMulAction K H
  ext k
  rw [MulAction.mem_stabilizer_iff]
  exact restrictedInducedPoint_stabilizer_iff K H k g

end GroupActionMackey
end GUFormalization
