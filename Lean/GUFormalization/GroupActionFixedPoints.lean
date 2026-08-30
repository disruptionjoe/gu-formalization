import Mathlib.Algebra.Group.Action.Defs
import Mathlib.Algebra.Group.Action.Pretransitive
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Set.Lattice
import Mathlib.GroupTheory.GroupAction.Defs
import Mathlib.SetTheory.Cardinal.Finite

/-!
# Group-action fixed-point classification

This file formalizes the elementary set-level classification used by the
observer-value-selection theorem: a valuation is pointwise invariant under a
group action exactly when its range lies in the common fixed-point set.

The result is pure mathematics. It constructs no physical group action,
observer, dynamics, selection mechanism, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionFixedPoints

variable {G A B : Type*} [Group G] [MulAction G B]

/-- Points of `B` fixed by every element of the acting group. -/
def commonFixedPoints : Set B := {b | ∀ g : G, g • b = b}

/-- A valuation fixed pointwise by every element of the acting group. -/
def PointwiseInvariant (p : A → B) : Prop := ∀ g : G, ∀ a : A, g • p a = p a

/-- The subtype of values fixed by every element of the acting group. -/
abbrev FixedPointValue := {b : B // b ∈ commonFixedPoints (G := G) (B := B)}

/-- The subtype of valuations fixed pointwise by the acting group. -/
abbrev InvariantValuation := {p : A → B // PointwiseInvariant (G := G) p}

/-- Maps from the regular left `G`-torsor that intertwine left multiplication
with the given action on `B`. -/
def RegularEquivariant (f : G → B) : Prop :=
  ∀ g x : G, f (g * x) = g • f x

/-- The subtype of equivariant maps from the regular left `G`-torsor. -/
abbrev RegularEquivariantMap := {f : G → B // RegularEquivariant (G := G) f}

/-- A map intertwining the supplied actions on its domain and codomain. -/
def Equivariant [MulAction G A] (f : A → B) : Prop :=
  ∀ g : G, ∀ a : A, f (g • a) = g • f a

/-- The subtype of maps intertwining the supplied actions. -/
abbrev EquivariantMap [MulAction G A] := {f : A → B // Equivariant (G := G) f}

/-- Values fixed by every group element stabilizing `a₀`. -/
def stabilizerFixedValues [MulAction G A] (a₀ : A) : Set B :=
  {b | ∀ g : G, g • a₀ = a₀ → g • b = b}

/-- The subtype of values fixed by the stabilizer of `a₀`. -/
abbrev StabilizerFixedValue [MulAction G A] (a₀ : A) :=
  {b : B // b ∈ stabilizerFixedValues (G := G) a₀}

theorem mem_commonFixedPoints_iff (b : B) :
    b ∈ commonFixedPoints (G := G) (B := B) ↔ ∀ g : G, g • b = b := by
  rfl

/-- Pointwise invariance is exactly range containment in the common fixed set. -/
theorem pointwiseInvariant_iff_range_subset (p : A → B) :
    PointwiseInvariant (G := G) p ↔
      Set.range p ⊆ commonFixedPoints (G := G) (B := B) := by
  constructor
  · intro h _ hb
    obtain ⟨a, rfl⟩ := hb
    exact fun g => h g a
  · intro h g a
    exact h (Set.mem_range_self a) g

/-- Equivalent elementwise form of the range-containment classification. -/
theorem pointwiseInvariant_iff_values_mem (p : A → B) :
    PointwiseInvariant (G := G) p ↔
      ∀ a : A, p a ∈ commonFixedPoints (G := G) (B := B) := by
  constructor
  · intro h a g
    exact h g a
  · intro h g a
    exact h a g

/-- Invariant valuations are exactly functions valued in the common fixed-point subtype. -/
def invariantValuationEquivFixedPointValuation :
    InvariantValuation (G := G) (A := A) (B := B) ≃
      (A → FixedPointValue (G := G) (B := B)) where
  toFun p := fun a =>
    ⟨p.1 a, (pointwiseInvariant_iff_values_mem (G := G) p.1).mp p.2 a⟩
  invFun q :=
    ⟨fun a => (q a).1,
      (pointwiseInvariant_iff_values_mem (G := G) (fun a => (q a).1)).mpr
        (fun a => (q a).2)⟩
  left_inv p := by
    apply Subtype.ext
    rfl
  right_inv q := by
    funext a
    apply Subtype.ext
    rfl

/-- For a finite domain and codomain, invariant valuations are counted exactly
by the number of common fixed values raised to the size of the domain. -/
theorem natCard_invariantValuation
    [Finite A] [Finite B] :
    Nat.card (InvariantValuation (G := G) (A := A) (B := B)) =
      Nat.card (FixedPointValue (G := G) (B := B)) ^ Nat.card A := by
  rw [Nat.card_congr
    (invariantValuationEquivFixedPointValuation (G := G) (A := A) (B := B))]
  exact Nat.card_fun

/-- On a finite inhabited domain, the invariant-valuation space has cardinality
zero exactly when the common fixed-point subtype has cardinality zero. -/
theorem natCard_invariantValuation_eq_zero_iff
    [Finite A] [Finite B] [Nonempty A] :
    Nat.card (InvariantValuation (G := G) (A := A) (B := B)) = 0 ↔
      Nat.card (FixedPointValue (G := G) (B := B)) = 0 := by
  rw [natCard_invariantValuation (G := G) (A := A) (B := B), Nat.pow_eq_zero]
  exact and_iff_left (Nat.ne_of_gt Nat.card_pos)

/-- An empty finite domain has exactly one invariant valuation, independently
of the common fixed-point set. -/
theorem natCard_invariantValuation_eq_one_of_isEmpty
    [Finite A] [Finite B] [IsEmpty A] :
    Nat.card (InvariantValuation (G := G) (A := A) (B := B)) = 1 := by
  rw [natCard_invariantValuation (G := G) (A := A) (B := B)]
  have hcard : Nat.card A = 0 := Nat.card_eq_zero.mpr (Or.inl inferInstance)
  rw [hcard, pow_zero]

/-- Evaluation at the identity classifies regular-domain equivariant maps. -/
def regularEquivariantMapEquivValue :
    RegularEquivariantMap (G := G) (B := B) ≃ B where
  toFun f := f.1 1
  invFun b :=
    ⟨fun g => g • b, by
      intro g x
      exact mul_smul g x b⟩
  left_inv f := by
    apply Subtype.ext
    funext g
    simpa using (f.2 g 1).symm
  right_inv b := one_smul G b

/-- Every codomain value seeds a unique equivariant map from the regular left
`G`-torsor. In particular, no global fixed-point condition is required. -/
theorem existsUnique_regularEquivariantMap_eval (b : B) :
    ∃! f : RegularEquivariantMap (G := G) (B := B), f.1 1 = b := by
  refine ⟨(regularEquivariantMapEquivValue (G := G) (B := B)).symm b, ?_, ?_⟩
  · exact (regularEquivariantMapEquivValue (G := G) (B := B)).apply_symm_apply b
  · intro f hf
    apply (regularEquivariantMapEquivValue (G := G) (B := B)).injective
    change f.1 1 =
      ((regularEquivariantMapEquivValue (G := G) (B := B)).symm b).1 1
    rw [hf]
    exact ((regularEquivariantMapEquivValue (G := G) (B := B)).apply_symm_apply b).symm

/-- For a finite codomain, regular-domain equivariant maps are counted by all
codomain values, not merely the common fixed values. -/
theorem natCard_regularEquivariantMap [Finite B] :
    Nat.card (RegularEquivariantMap (G := G) (B := B)) = Nat.card B := by
  exact Nat.card_congr (regularEquivariantMapEquivValue (G := G) (B := B))

private noncomputable def transporter [MulAction G A]
    [MulAction.IsPretransitive G A] (a₀ a : A) : G :=
  Classical.choose (MulAction.exists_smul_eq G a₀ a)

private theorem transporter_spec [MulAction G A]
    [MulAction.IsPretransitive G A] (a₀ a : A) :
    transporter (G := G) a₀ a • a₀ = a :=
  Classical.choose_spec (MulAction.exists_smul_eq G a₀ a)

/-- A stabilizer-fixed value has representative-independent transport along
its orbit. -/
private theorem stabilizerFixed_transport [MulAction G A]
    (a₀ : A) {b : B}
    (hb : b ∈ stabilizerFixedValues (G := G) a₀)
    {x y : G} (hxy : x • a₀ = y • a₀) :
    x • b = y • b := by
  have hstab : (y⁻¹ * x) • a₀ = a₀ := by
    rw [mul_smul, hxy]
    simp
  have hfix := hb (y⁻¹ * x) hstab
  calc
    x • b = y • ((y⁻¹ * x) • b) := by simp [mul_smul]
    _ = y • b := congrArg (fun z : B => y • z) hfix

/-- On a transitive domain, evaluation at `a₀` classifies equivariant maps
by the values fixed by the stabilizer of `a₀`. The inverse uses a classical
choice of transporter; representative independence is proved above. -/
noncomputable def equivariantMapEquivStabilizerFixedValue [MulAction G A]
    [MulAction.IsPretransitive G A] (a₀ : A) :
    EquivariantMap (G := G) (A := A) (B := B) ≃
      StabilizerFixedValue (G := G) (B := B) a₀ where
  toFun f :=
    ⟨f.1 a₀, by
      intro g hg
      rw [← f.2 g a₀, hg]⟩
  invFun b :=
    ⟨(fun a : A => transporter (G := G) a₀ a • (b.1 : B)), by
      intro g a
      rw [← mul_smul]
      apply stabilizerFixed_transport (G := G) a₀ b.2
      rw [transporter_spec (G := G) a₀ (g • a),
        mul_smul, transporter_spec (G := G) a₀ a]⟩
  left_inv f := by
    apply Subtype.ext
    funext a
    change transporter (G := G) a₀ a • f.1 a₀ = f.1 a
    rw [← f.2 (transporter (G := G) a₀ a) a₀,
      transporter_spec (G := G) a₀ a]
  right_inv b := by
    apply Subtype.ext
    change transporter (G := G) a₀ a₀ • b.1 = b.1
    exact b.2 _ (transporter_spec (G := G) a₀ a₀)

/-- Finite equivariant maps from a transitive domain are counted by the values
fixed by one point stabilizer. -/
theorem natCard_equivariantMap [MulAction G A]
    [MulAction.IsPretransitive G A] [Finite A] [Finite B] (a₀ : A) :
    Nat.card (EquivariantMap (G := G) (A := A) (B := B)) =
      Nat.card (StabilizerFixedValue (G := G) (B := B) a₀) := by
  exact Nat.card_congr
    (equivariantMapEquivStabilizerFixedValue (G := G) (B := B) a₀)

/-- A transitive-domain equivariant map exists exactly when the codomain has a
value fixed by the stabilizer of the chosen basepoint. -/
theorem nonempty_equivariantMap_iff_stabilizerFixedValue [MulAction G A]
    [MulAction.IsPretransitive G A] (a₀ : A) :
    Nonempty (EquivariantMap (G := G) (A := A) (B := B)) ↔
      Nonempty (StabilizerFixedValue (G := G) (B := B) a₀) :=
  (equivariantMapEquivStabilizerFixedValue (G := G) (B := B) a₀).nonempty_congr

/-- The orbit index of the supplied action on `A`. -/
abbrev OrbitIndex [MulAction G A] := MulAction.orbitRel.Quotient G A

noncomputable instance orbitIndexFintype [MulAction G A] [Fintype A] :
    Fintype (OrbitIndex (G := G) (A := A)) :=
  Fintype.ofFinite (OrbitIndex (G := G) (A := A))

/-- A classical representative of one orbit. Its use is exposed by the axiom
receipt, and the classification below proves that transported values do not
depend on this choice. -/
noncomputable def orbitRepresentative [MulAction G A]
    (ω : OrbitIndex (G := G) (A := A)) : A :=
  Quotient.out ω

/-- One stabilizer-fixed seed value for each orbit of the domain action. The
factor is dependent because the chosen representative, and hence its
stabilizer, may vary with the orbit. -/
abbrev OrbitStabilizerFixedSection [MulAction G A] :=
  ∀ ω : OrbitIndex (G := G) (A := A),
    StabilizerFixedValue (G := G) (B := B)
      (orbitRepresentative (G := G) (A := A) ω)

private noncomputable def orbitTransporter [MulAction G A] (a : A) : G :=
  Classical.choose (show
    a ∈ MulAction.orbit G
      (orbitRepresentative (G := G) (A := A)
        (Quotient.mk'' a : OrbitIndex (G := G) (A := A))) by
    exact Quotient.eq''.mp
      (Quotient.out_eq'
        (Quotient.mk'' a : OrbitIndex (G := G) (A := A))).symm)

private theorem orbitTransporter_spec [MulAction G A] (a : A) :
    orbitTransporter (G := G) a •
        orbitRepresentative (G := G) (A := A)
          (Quotient.mk'' a : OrbitIndex (G := G) (A := A)) = a :=
  Classical.choose_spec (show
    a ∈ MulAction.orbit G
      (orbitRepresentative (G := G) (A := A)
        (Quotient.mk'' a : OrbitIndex (G := G) (A := A))) by
    exact Quotient.eq''.mp
      (Quotient.out_eq'
        (Quotient.mk'' a : OrbitIndex (G := G) (A := A))).symm)

private theorem orbitIndex_smul [MulAction G A] (g : G) (a : A) :
    (Quotient.mk'' (g • a) : OrbitIndex (G := G) (A := A)) =
      Quotient.mk'' a :=
  Quotient.sound (MulAction.mem_orbit a g)

/-- For an arbitrary acted-on domain, equivariant maps are exactly independent
stabilizer-fixed seed choices over all domain orbits. The inverse transports
each seed within its orbit; representative independence is inherited from
`stabilizerFixed_transport`. -/
noncomputable def equivariantMapEquivOrbitStabilizerFixedSection [MulAction G A] :
    EquivariantMap (G := G) (A := A) (B := B) ≃
      OrbitStabilizerFixedSection (G := G) (A := A) (B := B) where
  toFun f := fun ω =>
    ⟨f.1 (orbitRepresentative (G := G) (A := A) ω), by
      intro g hg
      rw [← f.2 g (orbitRepresentative (G := G) (A := A) ω), hg]⟩
  invFun q :=
    ⟨(fun a => orbitTransporter (G := G) a •
        (q (Quotient.mk'' a : OrbitIndex (G := G) (A := A))).1), by
      intro g a
      have hq := orbitIndex_smul (G := G) g a
      change orbitTransporter (G := G) (g • a) •
          (q (Quotient.mk'' (g • a) : OrbitIndex (G := G) (A := A))).1 =
        g • (orbitTransporter (G := G) a •
          (q (Quotient.mk'' a : OrbitIndex (G := G) (A := A))).1)
      rw [hq, ← mul_smul]
      apply stabilizerFixed_transport (G := G)
        (orbitRepresentative (G := G) (A := A)
          (Quotient.mk'' a : OrbitIndex (G := G) (A := A)))
        (q (Quotient.mk'' a : OrbitIndex (G := G) (A := A))).2
      calc
        orbitTransporter (G := G) (g • a) •
            orbitRepresentative (G := G) (A := A)
              (Quotient.mk'' a : OrbitIndex (G := G) (A := A)) = g • a := by
          rw [← hq]
          exact orbitTransporter_spec (G := G) (g • a)
        _ = (g * orbitTransporter (G := G) a) •
            orbitRepresentative (G := G) (A := A)
              (Quotient.mk'' a : OrbitIndex (G := G) (A := A)) := by
          rw [mul_smul, orbitTransporter_spec (G := G) a]⟩
  left_inv f := by
    apply Subtype.ext
    funext a
    change orbitTransporter (G := G) a •
        f.1 (orbitRepresentative (G := G) (A := A)
          (Quotient.mk'' a : OrbitIndex (G := G) (A := A))) = f.1 a
    rw [← f.2 (orbitTransporter (G := G) a)
      (orbitRepresentative (G := G) (A := A)
        (Quotient.mk'' a : OrbitIndex (G := G) (A := A))),
      orbitTransporter_spec (G := G) a]
  right_inv q := by
    funext ω
    apply Subtype.ext
    have hq :
        (Quotient.mk'' (orbitRepresentative (G := G) (A := A) ω) :
          OrbitIndex (G := G) (A := A)) = ω :=
      Quotient.out_eq' ω
    change orbitTransporter (G := G)
          (orbitRepresentative (G := G) (A := A) ω) •
        (q (Quotient.mk''
          (orbitRepresentative (G := G) (A := A) ω) :
          OrbitIndex (G := G) (A := A))).1 = (q ω).1
    rw [hq]
    apply (q ω).2
    have htransport := orbitTransporter_spec (G := G)
      (orbitRepresentative (G := G) (A := A) ω)
    rw [hq] at htransport
    exact htransport

/-- Finite equivariant maps from an arbitrary acted-on domain are counted by
the product of the stabilizer-fixed seed counts over all domain orbits. -/
theorem natCard_equivariantMap_orbitProduct [MulAction G A]
    [Fintype A] [Finite B] :
    Nat.card (EquivariantMap (G := G) (A := A) (B := B)) =
      ∏ ω : OrbitIndex (G := G) (A := A),
        Nat.card (StabilizerFixedValue (G := G) (B := B)
          (orbitRepresentative (G := G) (A := A) ω)) := by
  rw [Nat.card_congr
    (equivariantMapEquivOrbitStabilizerFixedSection
      (G := G) (A := A) (B := B)), Nat.card_pi]

/-- An equivariant map on an arbitrary domain exists exactly when every orbit
has a seed value fixed by the stabilizer of its chosen representative. -/
theorem nonempty_equivariantMap_iff_forall_orbit_stabilizerFixedValue
    [MulAction G A] :
    Nonempty (EquivariantMap (G := G) (A := A) (B := B)) ↔
      ∀ ω : OrbitIndex (G := G) (A := A),
        Nonempty (StabilizerFixedValue (G := G) (B := B)
          (orbitRepresentative (G := G) (A := A) ω)) := by
  constructor
  · intro h ω
    exact ⟨(equivariantMapEquivOrbitStabilizerFixedSection
      (G := G) (A := A) (B := B)) h.some ω⟩
  · intro h
    exact ⟨(equivariantMapEquivOrbitStabilizerFixedSection
      (G := G) (A := A) (B := B)).symm
        (fun ω => Classical.choice (h ω))⟩

/-- The stabilizer of the identity for the regular left action is trivial, so
every codomain value satisfies its fixed-value condition. -/
theorem stabilizerFixedValues_regular_one :
    stabilizerFixedValues (G := G) (A := G) (B := B) 1 = Set.univ := by
  ext b
  simp [stabilizerFixedValues]

/-- On an inhabited domain, an invariant valuation exists exactly when the common
fixed-point set is nonempty. -/
theorem exists_pointwiseInvariant_iff_commonFixedPoints_nonempty
    [Nonempty A] :
    (∃ p : A → B, PointwiseInvariant (G := G) p) ↔
      (commonFixedPoints (G := G) (B := B)).Nonempty := by
  constructor
  · rintro ⟨p, hp⟩
    obtain ⟨a⟩ := ‹Nonempty A›
    exact ⟨p a, (pointwiseInvariant_iff_values_mem (G := G) p).mp hp a⟩
  · rintro ⟨b, hb⟩
    refine ⟨fun _ => b, ?_⟩
    exact (pointwiseInvariant_iff_values_mem (G := G) (fun _ : A => b)).mpr
      (fun _ => hb)

/-- One fixed-point-free group element empties the common fixed-point set. -/
theorem commonFixedPoints_eq_empty_of_fixpointFreeElement
    (g : G) (hg : ∀ b : B, g • b ≠ b) :
    commonFixedPoints (G := G) (B := B) = ∅ := by
  ext b
  simp only [commonFixedPoints, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
  intro hb
  exact hg b (hb g)

/-- If the common fixed-point set is empty, no inhabited-domain valuation is invariant. -/
theorem no_pointwiseInvariant_of_commonFixedPoints_eq_empty
    [Nonempty A]
    (hfixed : commonFixedPoints (G := G) (B := B) = ∅)
    (p : A → B) :
    ¬ PointwiseInvariant (G := G) p := by
  intro h
  obtain ⟨a⟩ := ‹Nonempty A›
  have hmem : p a ∈ commonFixedPoints (G := G) (B := B) :=
    (pointwiseInvariant_iff_values_mem (G := G) p).mp h a
  rw [hfixed] at hmem
  exact hmem.elim

/-- On an inhabited domain, no invariant valuation exists exactly when the
common fixed-point set is empty. -/
theorem no_pointwiseInvariant_iff_commonFixedPoints_eq_empty
    [Nonempty A] :
    (∀ p : A → B, ¬ PointwiseInvariant (G := G) p) ↔
      commonFixedPoints (G := G) (B := B) = ∅ := by
  constructor
  · intro h
    ext b
    constructor
    · intro hb
      have hinvariant : PointwiseInvariant (G := G) (fun _ : A => b) :=
        (pointwiseInvariant_iff_values_mem (G := G) (fun _ : A => b)).mpr
          (fun _ => hb)
      exact (h (fun _ : A => b) hinvariant).elim
    · intro hb
      exact hb.elim
  · intro hfixed p
    exact no_pointwiseInvariant_of_commonFixedPoints_eq_empty
      (G := G) (A := A) (B := B) hfixed p

/-- Direct no-invariant corollary from a fixed-point-free acting element. -/
theorem no_pointwiseInvariant_of_fixpointFreeElement
    [Nonempty A]
    (g : G) (hg : ∀ b : B, g • b ≠ b)
    (p : A → B) :
    ¬ PointwiseInvariant (G := G) p := by
  intro h
  obtain ⟨a⟩ := ‹Nonempty A›
  exact hg (p a) (h g a)

end GroupActionFixedPoints
end GUFormalization
