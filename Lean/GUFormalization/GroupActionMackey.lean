import GUFormalization.GroupActionInductionCoherence

/-!
# Mackey interfaces for set-level subgroup induction

For subgroups `H K ≤ G`, induction of the one-point `H`-set is the right
coset carrier `G / H`.  Restricting its action to `K` and then taking
`K`-orbits gives the double-coset quotient `K \ G / H`.  This file proves
that identification by explicit quotient maps and identifies the stabilizer
of the induced class of `g` with the transported intersection condition

`k * g = g * h` for some `h : H`.  For an arbitrary supplied `H`-set `B`, it
then constructs the representative Mackey summand

`K ×_(K ∩ gHg⁻¹) {}^gB`

and proves it `K`-equivariantly equivalent to its image in
`Res_K^G Ind_H^G(B)` under `[k,b] ↦ [kg,b]`.

Finally, it partitions the restricted induced carrier by its intrinsic
double-coset index. The dependent coproduct of these actual fibers is
canonically `K`-equivalent to the carrier without choosing representatives;
the classical representative theorem is retained as a separate comparison.
Equivariant maps of supplied seeds preserve the intrinsic index, act
fiberwise on this canonical coproduct, and commute with its assembly map.

The left-right action is fixed explicitly as `(k,h) • g = k * g * h⁻¹`.
All actions are named non-instances.  These are pure set-level laws for
supplied subgroup actions; they construct no physical action, carrier,
observer, selector, dynamics, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionMackey

open GroupActionFixedPoints GroupActionChangeOfGroups GroupActionInduction

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

/-! ## The nontrivial-seed Mackey summand -/

/-- The induced `G`-set `G ×_H B` for an arbitrary supplied `H`-action. -/
abbrev SubgroupInducedCarrier (H : Subgroup G) (B : Type*)
    [MulAction H B] :=
  @InducedCarrier H G B inferInstance inferInstance inferInstance H.subtype

/-- The explicit left `G`-action on `G ×_H B`. -/
@[implicit_reducible]
def subgroupInducedMulAction (H : Subgroup G) (B : Type*)
    [MulAction H B] : MulAction G (SubgroupInducedCarrier H B) :=
  @inducedMulAction H G B inferInstance inferInstance inferInstance H.subtype

/-- Restriction of the general induced carrier from `G` to `K`. -/
@[implicit_reducible]
def restrictedSubgroupInducedMulAction (K H : Subgroup G) (B : Type*)
    [MulAction H B] : MulAction K (SubgroupInducedCarrier H B) :=
  @restrictedMulAction K G (SubgroupInducedCarrier H B) inferInstance
    inferInstance (subgroupInducedMulAction H B) K.subtype

/-- Conjugation transports the representative stabilizer into `H`.  The
codomain membership proof uses the exact witness stored by
`transportedIntersection`; the value itself is the explicit formula
`g⁻¹kg`. -/
def transportedIntersectionToH (K H : Subgroup G) (g : G) :
    transportedIntersection K H g →* H where
  toFun k :=
    ⟨g⁻¹ * (k : G) * g, by
      rcases k.property with ⟨h, hk⟩
      have moved := congrArg (fun x : G => g⁻¹ * x) hk
      have heq : g⁻¹ * (k : G) * g = (h : G) := by
        simpa [mul_assoc] using moved
      rw [heq]
      exact h.property⟩
  map_one' := by
    apply Subtype.ext
    simp
  map_mul' k l := by
    apply Subtype.ext
    change g⁻¹ * (((k * l : transportedIntersection K H g) : K) : G) * g =
      (g⁻¹ * (k : G) * g) * (g⁻¹ * (l : G) * g)
    simp [mul_assoc]

/-- The action on a Mackey seed is the original `H`-action restricted along
the transported-intersection homomorphism `k ↦ g⁻¹kg`. -/
@[implicit_reducible]
def transportedSeedMulAction (K H : Subgroup G) (g : G)
    {B : Type*} [MulAction H B] :
    MulAction (transportedIntersection K H g) B :=
  @restrictedMulAction (transportedIntersection K H g) H B inferInstance
    inferInstance inferInstance (transportedIntersectionToH K H g)

/-- The representative-`g` Mackey summand
`K ×_(K ∩ gHg⁻¹) {}^gB`. -/
abbrev MackeySummandCarrier (K H : Subgroup G) (g : G) (B : Type*)
    [MulAction H B] :=
  @InducedCarrier (transportedIntersection K H g) K B inferInstance
    inferInstance (transportedSeedMulAction K H g)
    (transportedIntersection K H g).subtype

/-- The explicit left `K`-action on the representative Mackey summand. -/
@[implicit_reducible]
def mackeySummandMulAction (K H : Subgroup G) (g : G) (B : Type*)
    [MulAction H B] : MulAction K (MackeySummandCarrier K H g B) :=
  @inducedMulAction (transportedIntersection K H g) K B inferInstance
    inferInstance (transportedSeedMulAction K H g)
    (transportedIntersection K H g).subtype

/-- The transported subgroup equation in the orientation used by the
balanced-product descent. -/
theorem transportedIntersectionToH_spec (K H : Subgroup G) (g : G)
    (k : transportedIntersection K H g) :
    (k : G) * g = g * (transportedIntersectionToH K H g k : G) := by
  change (k : G) * g = g * (g⁻¹ * (k : G) * g)
  simp [mul_assoc]

/-- Map the representative Mackey summand into the restricted induced
carrier by `[k,b] ↦ [kg,b]`.  The transported action is exactly what makes
this descend through the source balanced product. -/
def mackeySummandToRestrictedInduced (K H : Subgroup G) (g : G)
    {B : Type*} [MulAction H B] :
    MackeySummandCarrier K H g B → SubgroupInducedCarrier H B := by
  letI transportedAction := transportedSeedMulAction (B := B) K H g
  letI summandPairAction := inductionPairMulAction
    (B := B) (transportedIntersection K H g).subtype
  letI targetPairAction := inductionPairMulAction (B := B) H.subtype
  intro q
  exact Quotient.liftOn' q
    (fun p : K × B => inducedMk H.subtype ((p.1 : G) * g) p.2) (by
      intro a b hab
      rw [MulAction.orbitRel_apply] at hab
      rcases hab with ⟨l, hab⟩
      rw [← hab]
      let h : H := transportedIntersectionToH K H g l
      have hlg : ((l⁻¹ : transportedIntersection K H g) : G) * g =
          g * (h : G)⁻¹ := by
        change (l : G)⁻¹ * g = g * (g⁻¹ * (l : G) * g)⁻¹
        simp [mul_assoc]
      change
        inducedMk H.subtype
            (((b.1 * (l : K)⁻¹ : K) : G) * g)
            (@SMul.smul (transportedIntersection K H g) B
              transportedAction.toSMul l b.2) =
          inducedMk H.subtype ((b.1 : G) * g) b.2
      change
        inducedMk H.subtype
            (((b.1 * (l : K)⁻¹ : K) : G) * g) (h • b.2) =
          inducedMk H.subtype ((b.1 : G) * g) b.2
      rw [show (((b.1 * (l : K)⁻¹ : K) : G) * g) =
          ((b.1 : G) * g) * (h : G)⁻¹ by
        calc
          (b.1 : G) * (l : G)⁻¹ * g =
              (b.1 : G) * ((l : G)⁻¹ * g) := by rw [mul_assoc]
          _ = (b.1 : G) * (g * (h : G)⁻¹) :=
            congrArg (fun x : G => (b.1 : G) * x) hlg
          _ = (b.1 : G) * g * (h : G)⁻¹ := by rw [mul_assoc]]
      simpa [mul_assoc] using
        (inducedMk_mul_phi H.subtype
          (((b.1 : G) * g) * (h : G)⁻¹) h b.2).symm)

/-- The summand map commutes with the explicit left `K`-actions. -/
theorem mackeySummandToRestrictedInduced_equivariant
    (K H : Subgroup G) (g : G) {B : Type*} [MulAction H B]
    (k : K) (q : MackeySummandCarrier K H g B) :
    mackeySummandToRestrictedInduced K H g
        (@SMul.smul K (MackeySummandCarrier K H g B)
          (mackeySummandMulAction K H g B).toSMul k q) =
      @SMul.smul K (SubgroupInducedCarrier H B)
        (restrictedSubgroupInducedMulAction K H B).toSMul k
        (mackeySummandToRestrictedInduced K H g q) := by
  letI transportedAction := transportedSeedMulAction (B := B) K H g
  letI summandPairAction := inductionPairMulAction
    (B := B) (transportedIntersection K H g).subtype
  letI summandAction := mackeySummandMulAction K H g B
  letI targetPairAction := inductionPairMulAction (B := B) H.subtype
  letI targetAction := subgroupInducedMulAction H B
  letI restrictedAction := restrictedSubgroupInducedMulAction K H B
  induction q using Quotient.inductionOn'
  case _ p =>
    change inducedMk H.subtype ((((k : K) * p.1 : K) : G) * g) p.2 =
      inducedMk H.subtype ((k : G) * ((p.1 : G) * g)) p.2
    apply congrArg Quotient.mk''
    ext
    · simp [mul_assoc]
    · rfl

/-- Equality after mapping into `Res_K^G Ind_H^G(B)` already holds in the
representative Mackey summand.  The proof extracts the target quotient witness
and turns it into an actual element of `K ∩ gHg⁻¹`. -/
theorem mackeySummandToRestrictedInduced_injective
    (K H : Subgroup G) (g : G) {B : Type*} [MulAction H B] :
    Function.Injective (mackeySummandToRestrictedInduced
      (B := B) K H g) := by
  letI transportedAction := transportedSeedMulAction (B := B) K H g
  letI summandPairAction := inductionPairMulAction
    (B := B) (transportedIntersection K H g).subtype
  letI targetPairAction := inductionPairMulAction (B := B) H.subtype
  intro q r hqr
  induction q using Quotient.inductionOn'
  case _ p =>
    induction r using Quotient.inductionOn'
    case _ s =>
      change inducedMk H.subtype ((p.1 : G) * g) p.2 =
        inducedMk H.subtype ((s.1 : G) * g) s.2 at hqr
      obtain ⟨h, hp⟩ := Quotient.exact hqr
      change
        ((s.1 : G) * g * (h : G)⁻¹, h • s.2) =
          ((p.1 : G) * g, p.2) at hp
      have hfirst := congrArg Prod.fst hp
      have hsecond := congrArg Prod.snd hp
      have hmove : (s.1 : G) * g = ((p.1 : G) * g) * (h : G) := by
        have moved := congrArg (fun x : G => x * (h : G)) hfirst
        simpa [mul_assoc] using moved
      have hlg : (((p.1⁻¹ * s.1 : K) : G) * g) = g * (h : G) := by
        calc
          (((p.1⁻¹ * s.1 : K) : G) * g) =
              (p.1 : G)⁻¹ * ((s.1 : G) * g) := by simp [mul_assoc]
          _ = (p.1 : G)⁻¹ * (((p.1 : G) * g) * (h : G)) := by
            rw [hmove]
          _ = g * (h : G) := by simp [mul_assoc]
      let l : transportedIntersection K H g :=
        ⟨p.1⁻¹ * s.1, ⟨h, hlg⟩⟩
      have hlh : transportedIntersectionToH K H g l = h := by
        apply Subtype.ext
        change g⁻¹ * (((p.1⁻¹ * s.1 : K) : G)) * g = (h : G)
        have moved := congrArg (fun x : G => g⁻¹ * x) hlg
        simpa [mul_assoc] using moved
      have hlb :
          @SMul.smul (transportedIntersection K H g) B
            transportedAction.toSMul l s.2 = p.2 := by
        change (transportedIntersectionToH K H g l) • s.2 = p.2
        rw [hlh]
        exact hsecond
      have balanced := inducedMk_mul_phi
        (transportedIntersection K H g).subtype p.1 l s.2
      change
        inducedMk (transportedIntersection K H g).subtype
            (p.1 * (l : K)) s.2 =
          inducedMk (transportedIntersection K H g).subtype p.1
            (@SMul.smul (transportedIntersection K H g) B
              transportedAction.toSMul l s.2) at balanced
      change
        inducedMk (transportedIntersection K H g).subtype p.1 p.2 =
          inducedMk (transportedIntersection K H g).subtype s.1 s.2
      simpa [l, hlb] using balanced.symm

/-- The actual subset of the restricted induced carrier occupied by the
representative-`g` Mackey summand. -/
abbrev MackeySummandImage (K H : Subgroup G) (g : G)
    {B : Type*} [MulAction H B] :=
  Set.range (mackeySummandToRestrictedInduced (B := B) K H g)

/-- Membership in the representative summand has the concrete form expected
from the double coset of `g`: the class has a representative `[kg,b]` for
some `k : K` and seed `b : B`. -/
theorem mem_mackeySummandImage_iff (K H : Subgroup G) (g : G)
    {B : Type*} [MulAction H B] (q : SubgroupInducedCarrier H B) :
    q ∈ MackeySummandImage (B := B) K H g ↔
      ∃ k : K, ∃ b : B, q = inducedMk H.subtype ((k : G) * g) b := by
  letI transportedAction := transportedSeedMulAction (B := B) K H g
  letI summandPairAction := inductionPairMulAction
    (B := B) (transportedIntersection K H g).subtype
  constructor
  · rintro ⟨s, rfl⟩
    induction s using Quotient.inductionOn'
    case _ p => exact ⟨p.1, p.2, rfl⟩
  · rintro ⟨k, b, rfl⟩
    exact ⟨inducedMk (transportedIntersection K H g).subtype k b, rfl⟩

/-- Equip the image with the restricted left `K`-action.  Stability follows
from equivariance of the summand map. -/
@[implicit_reducible]
def mackeySummandImageMulAction (K H : Subgroup G) (g : G)
    {B : Type*} [MulAction H B] :
    MulAction K (MackeySummandImage (B := B) K H g) := by
  letI summandAction := mackeySummandMulAction K H g B
  letI targetAction := restrictedSubgroupInducedMulAction K H B
  exact {
    smul k q :=
      ⟨k • q.1, by
        rcases q.2 with ⟨s, hs⟩
        refine ⟨k • s, ?_⟩
        change
          mackeySummandToRestrictedInduced K H g
              (@SMul.smul K (MackeySummandCarrier K H g B)
                (mackeySummandMulAction K H g B).toSMul k s) =
            @SMul.smul K (SubgroupInducedCarrier H B)
              (restrictedSubgroupInducedMulAction K H B).toSMul k q.1
        rw [mackeySummandToRestrictedInduced_equivariant K H g k s]
        exact congrArg
          (fun x => @SMul.smul K (SubgroupInducedCarrier H B)
            (restrictedSubgroupInducedMulAction K H B).toSMul k x) hs⟩
    one_smul q := by
      apply Subtype.ext
      exact (restrictedSubgroupInducedMulAction K H B).one_smul q.1
    mul_smul k l q := by
      apply Subtype.ext
      exact (restrictedSubgroupInducedMulAction K H B).mul_smul k l q.1 }

/-- The induced transported-intersection carrier is exactly the
representative Mackey summand inside the restricted induced `G`-set. -/
noncomputable def mackeySummandEquivImage (K H : Subgroup G) (g : G)
    {B : Type*} [MulAction H B] :
    MackeySummandCarrier K H g B ≃ MackeySummandImage (B := B) K H g :=
  Equiv.ofBijective
    (fun s =>
      ⟨mackeySummandToRestrictedInduced K H g s, ⟨s, rfl⟩⟩)
    ⟨by
      intro a b hab
      apply mackeySummandToRestrictedInduced_injective K H g
      exact congrArg Subtype.val hab,
     by
      intro q
      rcases q.2 with ⟨s, hs⟩
      refine ⟨s, ?_⟩
      apply Subtype.ext
      exact hs⟩

/-- The summand equivalence is `K`-equivariant for the explicit actions on
both sides. -/
theorem mackeySummandEquivImage_equivariant
    (K H : Subgroup G) (g : G) {B : Type*} [MulAction H B]
    (k : K) (s : MackeySummandCarrier K H g B) :
    mackeySummandEquivImage K H g
        (@SMul.smul K (MackeySummandCarrier K H g B)
          (mackeySummandMulAction K H g B).toSMul k s) =
      @SMul.smul K (MackeySummandImage (B := B) K H g)
        (mackeySummandImageMulAction (B := B) K H g).toSMul k
        (mackeySummandEquivImage K H g s) := by
  apply Subtype.ext
  exact mackeySummandToRestrictedInduced_equivariant K H g k s

/-! ## The global choice-dependent Mackey coproduct -/

/-- Choose one representative of every explicit double-coset class.  This is
the only representative choice used by the global decomposition. -/
noncomputable def doubleCosetRepresentative (K H : Subgroup G)
    (q : DoubleCosetCarrier K H) : G :=
  Quotient.out q

/-- The chosen representative belongs to the double-coset class it
represents. -/
theorem doubleCosetMk_representative (K H : Subgroup G)
    (q : DoubleCosetCarrier K H) :
    doubleCosetMk K H (doubleCosetRepresentative K H q) = q :=
  Quotient.out_eq' q

/-- Forget the seed while remembering the double coset of an induced class.
The map is well-defined because the balanced right `H`-relation stays within
one double coset. -/
def restrictedInducedDoubleCosetIndex (K H : Subgroup G)
    {B : Type*} [MulAction H B] :
    SubgroupInducedCarrier H B → DoubleCosetCarrier K H := by
  letI pairAction := inductionPairMulAction (B := B) H.subtype
  letI doubleAction := doubleCosetMulAction K H
  intro q
  exact Quotient.liftOn' q
    (fun p : G × B => doubleCosetMk K H p.1) (by
      intro a b hab
      rw [MulAction.orbitRel_apply] at hab
      rcases hab with ⟨h, hab⟩
      rw [← hab]
      apply Quotient.sound
      refine ⟨(1, h), ?_⟩
      exact show (1 : G) * b.1 * (h : G)⁻¹ = b.1 * (h : G)⁻¹ by
        simp)

@[simp]
theorem restrictedInducedDoubleCosetIndex_mk (K H : Subgroup G)
    {B : Type*} [MulAction H B] (g : G) (b : B) :
    restrictedInducedDoubleCosetIndex K H (inducedMk H.subtype g b) =
      doubleCosetMk K H g :=
  rfl

/-- Applying an equivariant map to the supplied seed does not change the
intrinsic double-coset index of an induced class. -/
theorem restrictedInducedDoubleCosetIndex_inducedMap (K H : Subgroup G)
    {B C : Type*} [MulAction H B] [MulAction H C]
    (f : @EquivariantMap H B C _ inferInstance inferInstance)
    (x : SubgroupInducedCarrier H B) :
    restrictedInducedDoubleCosetIndex K H
        (inducedMap H.subtype f x) =
      restrictedInducedDoubleCosetIndex K H x := by
  induction x using Quotient.inductionOn'
  case _ p => rfl

/-! ## The canonical choice-free Mackey fibers -/

/-- Left multiplication by `K` preserves the intrinsic double-coset index of
the restricted induced carrier. -/
theorem restrictedInducedDoubleCosetIndex_smul (K H : Subgroup G)
    {B : Type*} [MulAction H B] (k : K) (x : SubgroupInducedCarrier H B) :
    restrictedInducedDoubleCosetIndex K H
        (@SMul.smul K (SubgroupInducedCarrier H B)
          (restrictedSubgroupInducedMulAction K H B).toSMul k x) =
      restrictedInducedDoubleCosetIndex K H x := by
  letI targetPairAction := inductionPairMulAction (B := B) H.subtype
  letI targetAction := restrictedSubgroupInducedMulAction K H B
  letI doubleAction := doubleCosetMulAction K H
  induction x using Quotient.inductionOn'
  case _ p =>
    change
      doubleCosetMk K H ((k : G) * p.1) = doubleCosetMk K H p.1
    apply Quotient.sound
    refine ⟨(k, 1), ?_⟩
    change (k : G) * p.1 * (1 : G)⁻¹ = (k : G) * p.1
    simp

/-- The canonical fiber over one double coset.  Unlike a representative
Mackey summand, this is a literal subtype of the target and makes no choice. -/
abbrev MackeyFiberCarrier (K H : Subgroup G) (B : Type*) [MulAction H B]
    (q : DoubleCosetCarrier K H) :=
  {x : SubgroupInducedCarrier H B //
    restrictedInducedDoubleCosetIndex K H x = q}

/-- The restricted left `K`-action on one canonical double-coset fiber. -/
@[implicit_reducible]
def mackeyFiberMulAction (K H : Subgroup G) (B : Type*) [MulAction H B]
    (q : DoubleCosetCarrier K H) : MulAction K (MackeyFiberCarrier K H B q) where
  smul k x :=
    ⟨@SMul.smul K (SubgroupInducedCarrier H B)
        (restrictedSubgroupInducedMulAction K H B).toSMul k x.1,
      (restrictedInducedDoubleCosetIndex_smul K H k x.1).trans x.2⟩
  one_smul x := by
    apply Subtype.ext
    exact (restrictedSubgroupInducedMulAction K H B).one_smul x.1
  mul_smul k l x := by
    apply Subtype.ext
    exact (restrictedSubgroupInducedMulAction K H B).mul_smul k l x.1

/-- The dependent coproduct of the actual index fibers.  This is the
representative-free carrier underlying the canonical Mackey partition. -/
abbrev CanonicalMackeyCoproductCarrier (K H : Subgroup G) (B : Type*)
    [MulAction H B] :=
  Σ q : DoubleCosetCarrier K H, MackeyFiberCarrier K H B q

/-- The fiberwise `K`-action on the canonical coproduct. -/
@[implicit_reducible]
def canonicalMackeyCoproductMulAction (K H : Subgroup G) (B : Type*)
    [MulAction H B] : MulAction K (CanonicalMackeyCoproductCarrier K H B) where
  smul k x :=
    ⟨x.1,
      @SMul.smul K (MackeyFiberCarrier K H B x.1)
        (mackeyFiberMulAction K H B x.1).toSMul k x.2⟩
  one_smul x := by
    rcases x with ⟨q, z⟩
    exact Sigma.ext rfl (heq_of_eq ((mackeyFiberMulAction K H B q).one_smul z))
  mul_smul k l x := by
    rcases x with ⟨q, z⟩
    exact Sigma.ext rfl
      (heq_of_eq ((mackeyFiberMulAction K H B q).mul_smul k l z))

/-- Every indexed family is canonically the dependent coproduct of its actual
fibers.  Here this gives a representative-free Mackey decomposition of the
restricted induced carrier. -/
def canonicalMackeyCoproductEquivRestrictedInduced
    (K H : Subgroup G) {B : Type*} [MulAction H B] :
    CanonicalMackeyCoproductCarrier K H B ≃ SubgroupInducedCarrier H B where
  toFun x := x.2.1
  invFun x := ⟨restrictedInducedDoubleCosetIndex K H x, ⟨x, rfl⟩⟩
  left_inv x := by
    rcases x with ⟨q, ⟨z, hz⟩⟩
    cases hz
    rfl
  right_inv _ := rfl

/-- An equivariant seed map acts fiberwise on the canonical Mackey coproduct;
the double-coset coordinate is unchanged. -/
def canonicalMackeyCoproductMap (K H : Subgroup G)
    {B C : Type*} [MulAction H B] [MulAction H C]
    (f : @EquivariantMap H B C _ inferInstance inferInstance) :
    CanonicalMackeyCoproductCarrier K H B →
      CanonicalMackeyCoproductCarrier K H C := fun x =>
  ⟨x.1, ⟨inducedMap H.subtype f x.2.1,
    (restrictedInducedDoubleCosetIndex_inducedMap K H f x.2.1).trans x.2.2⟩⟩

/-- The canonical Mackey decomposition is natural in the supplied seed map:
assembling after the fiberwise map equals inducing the seed map first. -/
theorem canonicalMackeyCoproduct_naturality (K H : Subgroup G)
    {B C : Type*} [MulAction H B] [MulAction H C]
    (f : @EquivariantMap H B C _ inferInstance inferInstance)
    (x : CanonicalMackeyCoproductCarrier K H B) :
    canonicalMackeyCoproductEquivRestrictedInduced K H
        (canonicalMackeyCoproductMap K H f x) =
      inducedMap H.subtype f
        (canonicalMackeyCoproductEquivRestrictedInduced K H x) :=
  rfl

/-- Fiberwise canonical Mackey maps preserve identity seed maps. -/
theorem canonicalMackeyCoproductMap_id (K H : Subgroup G)
    {B : Type*} [MulAction H B]
    (x : CanonicalMackeyCoproductCarrier K H B) :
    canonicalMackeyCoproductMap K H
        (⟨id, by intro h b; rfl⟩ :
          @EquivariantMap H B B _ inferInstance inferInstance) x = x := by
  apply (canonicalMackeyCoproductEquivRestrictedInduced K H).injective
  rw [canonicalMackeyCoproduct_naturality]
  exact inducedMap_id H.subtype
    (canonicalMackeyCoproductEquivRestrictedInduced K H x)

/-- The canonical fiber decomposition commutes with the explicit left
`K`-actions and requires no representative transport. -/
theorem canonicalMackeyCoproductEquivRestrictedInduced_equivariant
    (K H : Subgroup G) {B : Type*} [MulAction H B]
    (k : K) (x : CanonicalMackeyCoproductCarrier K H B) :
    canonicalMackeyCoproductEquivRestrictedInduced K H
        (@SMul.smul K (CanonicalMackeyCoproductCarrier K H B)
          (canonicalMackeyCoproductMulAction K H B).toSMul k x) =
      @SMul.smul K (SubgroupInducedCarrier H B)
        (restrictedSubgroupInducedMulAction K H B).toSMul k
        (canonicalMackeyCoproductEquivRestrictedInduced K H x) :=
  rfl

/-- The fiberwise canonical Mackey map is equivariant for the restricted
left `K`-actions. -/
theorem canonicalMackeyCoproductMap_equivariant (K H : Subgroup G)
    {B C : Type*} [MulAction H B] [MulAction H C]
    (f : @EquivariantMap H B C _ inferInstance inferInstance)
    (k : K) (x : CanonicalMackeyCoproductCarrier K H B) :
    canonicalMackeyCoproductMap K H f
        (@SMul.smul K (CanonicalMackeyCoproductCarrier K H B)
          (canonicalMackeyCoproductMulAction K H B).toSMul k x) =
      @SMul.smul K (CanonicalMackeyCoproductCarrier K H C)
        (canonicalMackeyCoproductMulAction K H C).toSMul k
        (canonicalMackeyCoproductMap K H f x) := by
  apply (canonicalMackeyCoproductEquivRestrictedInduced K H).injective
  rw [canonicalMackeyCoproduct_naturality]
  rw [canonicalMackeyCoproductEquivRestrictedInduced_equivariant]
  rw [canonicalMackeyCoproductEquivRestrictedInduced_equivariant]
  rw [canonicalMackeyCoproduct_naturality]
  exact inducedMap_equivariant H.subtype f (k : G)
    (canonicalMackeyCoproductEquivRestrictedInduced K H x)

/-- The dependent coproduct of transported-intersection inductions, one
summand for the chosen representative of each double coset. -/
abbrev MackeyCoproductCarrier (K H : Subgroup G) (B : Type*)
    [MulAction H B] :=
  Σ q : DoubleCosetCarrier K H,
    MackeySummandCarrier K H (doubleCosetRepresentative K H q) B

/-- The fiberwise left `K`-action on the Mackey coproduct.  The double-coset
index is fixed and `K` acts inside the corresponding induced summand. -/
@[implicit_reducible]
noncomputable def mackeyCoproductMulAction (K H : Subgroup G) (B : Type*)
    [MulAction H B] : MulAction K (MackeyCoproductCarrier K H B) where
  smul k x :=
    ⟨x.1,
      @SMul.smul K
        (MackeySummandCarrier K H (doubleCosetRepresentative K H x.1) B)
        (mackeySummandMulAction K H (doubleCosetRepresentative K H x.1) B).toSMul
        k x.2⟩
  one_smul x := by
    rcases x with ⟨q, s⟩
    change
      (⟨q,
        @SMul.smul K
          (MackeySummandCarrier K H (doubleCosetRepresentative K H q) B)
          (mackeySummandMulAction K H
            (doubleCosetRepresentative K H q) B).toSMul 1 s⟩ :
          MackeyCoproductCarrier K H B) =
        (⟨q, s⟩ : MackeyCoproductCarrier K H B)
    exact Sigma.ext rfl (heq_of_eq
      ((mackeySummandMulAction K H
        (doubleCosetRepresentative K H q) B).one_smul s))
  mul_smul k l x := by
    rcases x with ⟨q, s⟩
    change
      (⟨q,
        @SMul.smul K
          (MackeySummandCarrier K H (doubleCosetRepresentative K H q) B)
          (mackeySummandMulAction K H
            (doubleCosetRepresentative K H q) B).toSMul (k * l) s⟩ :
          MackeyCoproductCarrier K H B) =
        (⟨q,
          @SMul.smul K
            (MackeySummandCarrier K H (doubleCosetRepresentative K H q) B)
            (mackeySummandMulAction K H
              (doubleCosetRepresentative K H q) B).toSMul k
            (@SMul.smul K
              (MackeySummandCarrier K H
                (doubleCosetRepresentative K H q) B)
              (mackeySummandMulAction K H
                (doubleCosetRepresentative K H q) B).toSMul l s)⟩ :
          MackeyCoproductCarrier K H B)
    exact Sigma.ext rfl (heq_of_eq
      ((mackeySummandMulAction K H
        (doubleCosetRepresentative K H q) B).mul_smul k l s))

/-- Assemble the chosen representative summands inside the restricted
induced carrier. -/
noncomputable def mackeyCoproductToRestrictedInduced (K H : Subgroup G)
    {B : Type*} [MulAction H B] :
    MackeyCoproductCarrier K H B → SubgroupInducedCarrier H B :=
  fun x => mackeySummandToRestrictedInduced K H
    (doubleCosetRepresentative K H x.1) x.2

/-- Every assembled element remembers exactly its coproduct index. -/
theorem restrictedInducedDoubleCosetIndex_mackeyCoproduct
    (K H : Subgroup G) {B : Type*} [MulAction H B]
    (x : MackeyCoproductCarrier K H B) :
    restrictedInducedDoubleCosetIndex K H
        (mackeyCoproductToRestrictedInduced K H x) = x.1 := by
  rcases x with ⟨q, s⟩
  letI transportedAction := transportedSeedMulAction
    (B := B) K H (doubleCosetRepresentative K H q)
  letI summandPairAction := inductionPairMulAction
    (B := B) (transportedIntersection K H
      (doubleCosetRepresentative K H q)).subtype
  induction s using Quotient.inductionOn'
  case _ p =>
    calc
      restrictedInducedDoubleCosetIndex K H
          (mackeyCoproductToRestrictedInduced K H
            ⟨q, Quotient.mk'' p⟩) =
          doubleCosetMk K H
            ((p.1 : G) * doubleCosetRepresentative K H q) := rfl
      _ = doubleCosetMk K H (doubleCosetRepresentative K H q) := by
        apply Quotient.sound
        refine ⟨(p.1, 1), ?_⟩
        change
          (p.1 : G) * doubleCosetRepresentative K H q * (1 : G)⁻¹ =
            (p.1 : G) * doubleCosetRepresentative K H q
        simp
      _ = q := doubleCosetMk_representative K H q

/-- Distinct double-coset fibers cannot meet, and each representative-level
summand map is injective. -/
theorem mackeyCoproductToRestrictedInduced_injective
    (K H : Subgroup G) {B : Type*} [MulAction H B] :
    Function.Injective
      (mackeyCoproductToRestrictedInduced (B := B) K H) := by
  intro x y hxy
  have hindex : x.1 = y.1 := by
    calc
      x.1 = restrictedInducedDoubleCosetIndex K H
          (mackeyCoproductToRestrictedInduced K H x) :=
        (restrictedInducedDoubleCosetIndex_mackeyCoproduct K H x).symm
      _ = restrictedInducedDoubleCosetIndex K H
          (mackeyCoproductToRestrictedInduced K H y) := congrArg _ hxy
      _ = y.1 :=
        restrictedInducedDoubleCosetIndex_mackeyCoproduct K H y
  rcases x with ⟨q, x⟩
  rcases y with ⟨r, y⟩
  change q = r at hindex
  subst r
  exact Sigma.ext rfl (heq_of_eq
    (mackeySummandToRestrictedInduced_injective K H
      (doubleCosetRepresentative K H q) hxy))

/-- Every restricted induced class lies in the summand indexed by its double
coset.  Surjectivity uses an actual `K × H` orbit witness relating the chosen
representative to the supplied representative. -/
theorem mackeyCoproductToRestrictedInduced_surjective
    (K H : Subgroup G) {B : Type*} [MulAction H B] :
    Function.Surjective
      (mackeyCoproductToRestrictedInduced (B := B) K H) := by
  letI targetPairAction := inductionPairMulAction (B := B) H.subtype
  letI doubleAction := doubleCosetMulAction K H
  intro z
  induction z using Quotient.inductionOn'
  case _ p =>
    let q : DoubleCosetCarrier K H := doubleCosetMk K H p.1
    have hrep :
        doubleCosetMk K H (doubleCosetRepresentative K H q) =
          doubleCosetMk K H p.1 := by
      exact doubleCosetMk_representative K H q
    obtain ⟨kh, hkh⟩ := Quotient.exact hrep
    letI transportedAction := transportedSeedMulAction
      (B := B) K H (doubleCosetRepresentative K H q)
    letI summandPairAction := inductionPairMulAction
      (B := B) (transportedIntersection K H
        (doubleCosetRepresentative K H q)).subtype
    let s : MackeySummandCarrier K H
        (doubleCosetRepresentative K H q) B :=
      inducedMk
        (transportedIntersection K H
          (doubleCosetRepresentative K H q)).subtype
        kh.1⁻¹ (kh.2 • p.2)
    refine ⟨⟨q, s⟩, ?_⟩
    change
      inducedMk H.subtype
          (((kh.1⁻¹ : K) : G) * doubleCosetRepresentative K H q)
          (kh.2 • p.2) =
        inducedMk H.subtype p.1 p.2
    have hfirst :
        ((kh.1 : G) * p.1 * (kh.2 : G)⁻¹) =
          doubleCosetRepresentative K H q := by
      exact hkh
    have hmove :
        (((kh.1⁻¹ : K) : G) * doubleCosetRepresentative K H q) =
          p.1 * (kh.2 : G)⁻¹ := by
      rw [← hfirst]
      simp [mul_assoc]
    rw [hmove]
    simpa [mul_assoc] using
      (inducedMk_mul_phi H.subtype
        (p.1 * (kh.2 : G)⁻¹) kh.2 p.2).symm

/-- Global set-level Mackey decomposition for a supplied `H`-set.  The
equivalence depends on the explicit classical choice of one representative in
each double coset. -/
noncomputable def mackeyCoproductEquivRestrictedInduced
    (K H : Subgroup G) {B : Type*} [MulAction H B] :
    MackeyCoproductCarrier K H B ≃ SubgroupInducedCarrier H B :=
  Equiv.ofBijective (mackeyCoproductToRestrictedInduced K H)
    ⟨mackeyCoproductToRestrictedInduced_injective K H,
      mackeyCoproductToRestrictedInduced_surjective K H⟩

/-- The global Mackey equivalence commutes with the explicit left `K`-actions
on the coproduct and the restricted induced carrier. -/
theorem mackeyCoproductEquivRestrictedInduced_equivariant
    (K H : Subgroup G) {B : Type*} [MulAction H B]
    (k : K) (x : MackeyCoproductCarrier K H B) :
    mackeyCoproductEquivRestrictedInduced K H
        (@SMul.smul K (MackeyCoproductCarrier K H B)
          (mackeyCoproductMulAction K H B).toSMul k x) =
      @SMul.smul K (SubgroupInducedCarrier H B)
        (restrictedSubgroupInducedMulAction K H B).toSMul k
        (mackeyCoproductEquivRestrictedInduced K H x) := by
  rcases x with ⟨q, s⟩
  exact mackeySummandToRestrictedInduced_equivariant K H
    (doubleCosetRepresentative K H q) k s

/-- The representative-based Mackey coproduct and the canonical fiber
coproduct are equivalent through their common restricted-induced carrier.
Only this comparison inherits the representative choice; the canonical
fiber equivalence above does not. -/
noncomputable def mackeyCoproductEquivCanonicalFibers
    (K H : Subgroup G) {B : Type*} [MulAction H B] :
    MackeyCoproductCarrier K H B ≃ CanonicalMackeyCoproductCarrier K H B :=
  (mackeyCoproductEquivRestrictedInduced K H).trans
    (canonicalMackeyCoproductEquivRestrictedInduced K H).symm

end GroupActionMackey
end GUFormalization
