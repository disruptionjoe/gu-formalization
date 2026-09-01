import Mathlib

/-!
# Packet-local positive-cone selection boundary

A real linear carrier and the range of a linear packet are closed under sign.
If that raw carrier or range is declared to be a pointed positive cone, every
member is therefore zero.  On a nontrivial carrier it cannot also generate the
ambient additive group.  A phase action whose square is negation gives the same
obstruction whenever the proposed cone is phase-invariant.

This theorem does not rule out positive cones on quadratic, ray, dual, or
otherwise extended carriers.  It isolates the extra selection data needed to
pass from sign-symmetric amplitude-like data to ordered physical states.
-/

set_option autoImplicit false

namespace GUFormalization
namespace PacketLocalPositiveCone

variable {V : Type*} [AddCommGroup V]

/-- Membership of a subset is preserved by additive negation. -/
def NegInvariant (C : Set V) : Prop :=
  ∀ ⦃x : V⦄, x ∈ C → -x ∈ C

/-- A pointed subset contains no nonzero element together with its negative. -/
def Pointed (C : Set V) : Prop :=
  ∀ ⦃x : V⦄, x ∈ C → -x ∈ C → x = 0

/-- The additive generating condition used by an ordered-vector-space cone. -/
def Generating (C : Set V) : Prop :=
  ∀ x : V, ∃ a ∈ C, ∃ b ∈ C, x = a - b

/-- A sign-invariant pointed subset contains only zero. -/
theorem mem_eq_zero_of_negInvariant_pointed
    {C : Set V} (hneg : NegInvariant C) (hpoint : Pointed C)
    {x : V} (hx : x ∈ C) : x = 0 :=
  hpoint hx (hneg hx)

/-- On a nontrivial carrier, sign invariance and pointedness exclude generation. -/
theorem not_generating_of_negInvariant_pointed
    [Nontrivial V] {C : Set V} (hneg : NegInvariant C) (hpoint : Pointed C) :
    ¬ Generating C := by
  intro hgen
  obtain ⟨x, hx⟩ := exists_ne (0 : V)
  obtain ⟨a, ha, b, hb, hab⟩ := hgen x
  have ha0 : a = 0 := mem_eq_zero_of_negInvariant_pointed hneg hpoint ha
  have hb0 : b = 0 := mem_eq_zero_of_negInvariant_pointed hneg hpoint hb
  apply hx
  rw [hab, ha0, hb0]
  simp

/-- The range of any linear map is sign-invariant. -/
theorem linearMap_range_negInvariant
    {R : Type*} [Ring R] [Module R V] (P : V →ₗ[R] V) :
    NegInvariant (Set.range P) := by
  intro x hx
  obtain ⟨v, rfl⟩ := hx
  exact ⟨-v, by simp⟩

/-- A raw linear-map range cannot itself be both pointed and generating. -/
theorem linearMap_range_not_pointed_and_generating
    {R : Type*} [Ring R] [Module R V] [Nontrivial V] (P : V →ₗ[R] V) :
    ¬ (Pointed (Set.range P) ∧ Generating (Set.range P)) := by
  rintro ⟨hpoint, hgen⟩
  exact not_generating_of_negInvariant_pointed
    (linearMap_range_negInvariant P) hpoint hgen

/-- A transformation preserves a proposed state subset. -/
def Preserves (T : V → V) (C : Set V) : Prop :=
  ∀ ⦃x : V⦄, x ∈ C → T x ∈ C

/-- A preserved phase action squaring to negation makes the subset sign-invariant. -/
theorem negInvariant_of_phase_square
    {C : Set V} {T : V → V} (hpres : Preserves T C)
    (hsquare : ∀ x : V, T (T x) = -x) : NegInvariant C := by
  intro x hx
  have htwice : T (T x) ∈ C := hpres (hpres hx)
  rw [hsquare x] at htwice
  exact htwice

/-- A nontrivial pointed generating cone cannot be invariant under such a phase action. -/
theorem phase_square_not_preserves_pointed_generating
    [Nontrivial V] {C : Set V} {T : V → V}
    (hsquare : ∀ x : V, T (T x) = -x)
    (hpoint : Pointed C) (hgen : Generating C) : ¬ Preserves T C := by
  intro hpres
  exact not_generating_of_negInvariant_pointed
    (negInvariant_of_phase_square hpres hsquare) hpoint hgen

end PacketLocalPositiveCone
end GUFormalization
