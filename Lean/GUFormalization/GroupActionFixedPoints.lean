import Mathlib.Algebra.Group.Action.Defs
import Mathlib.Data.Set.Lattice

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
