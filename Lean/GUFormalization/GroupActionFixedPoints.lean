import Mathlib.Algebra.Group.Action.Defs
import Mathlib.Data.Set.Lattice
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
