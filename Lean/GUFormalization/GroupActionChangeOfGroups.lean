import GUFormalization.GroupActionFixedPoints
import Mathlib.Algebra.Group.Action.Basic

/-!
# Change of acting groups for equivariant maps

This file constructs restriction of a set action along a group homomorphism.
For a surjective homomorphism, restricted equivariance and fixedness are
equivalent to their original forms. For an arbitrary homomorphism
`phi : H →* G`, coinduction is realized by the functions `f : G → B`
satisfying

`f (phi h * g) = h • f g`,

with `G` acting by right translation. Evaluation at the identity then gives
the restriction-coinduction adjunction

`Hom_H (Res_phi A, B) ≃ Hom_G (A, Coind_phi B)`.

All actions introduced here are explicit named values rather than global
instances. The results are pure set-level mathematics: they construct no
physical group action, observer, selector, dynamics, or Geometric Unity
verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionChangeOfGroups

open GroupActionFixedPoints

variable {H G A B : Type*} [Group H] [Group G]

/-- Restrict a `G`-action to an `H`-action along `phi : H →* G`. The action
is explicit and does not install a second global instance on the carrier. -/
@[implicit_reducible]
def restrictedMulAction [MulAction G A] (phi : H →* G) : MulAction H A where
  smul h a := phi h • a
  one_smul a := by
    change phi 1 • a = a
    rw [map_one]
    exact one_smul G a
  mul_smul h k a := by
    change phi (h * k) • a = phi h • phi k • a
    rw [map_mul, mul_smul]

/-- Equivariant maps after restricting both supplied `G`-actions along
`phi`. -/
abbrev RestrictedEquivariantMap [MulAction G A] [MulAction G B]
    (phi : H →* G) :=
  @EquivariantMap H A B _ (restrictedMulAction (A := B) phi)
    (restrictedMulAction (A := A) phi)

/-- Every `G`-equivariant map remains equivariant after restriction along an
arbitrary group homomorphism. -/
def restrictEquivariantMap [MulAction G A] [MulAction G B]
    (phi : H →* G) :
    EquivariantMap (G := G) (A := A) (B := B) →
      RestrictedEquivariantMap (A := A) (B := B) phi :=
  fun f => ⟨f.1, fun h a => f.2 (phi h) a⟩

/-- If the group homomorphism is surjective, restricted equivariance is
exactly full equivariance. Surjectivity is load-bearing: without it the
restricted action may test fewer group elements. -/
def equivariantMapEquivRestricted_of_surjective [MulAction G A]
    [MulAction G B] (phi : H →* G) (hphi : Function.Surjective phi) :
    EquivariantMap (G := G) (A := A) (B := B) ≃
      RestrictedEquivariantMap (A := A) (B := B) phi where
  toFun := restrictEquivariantMap phi
  invFun f :=
    ⟨f.1, by
      intro g a
      obtain ⟨h, rfl⟩ := hphi g
      exact f.2 h a⟩
  left_inv f := by
    apply Subtype.ext
    rfl
  right_inv f := by
    apply Subtype.ext
    rfl

/-- Values fixed by the action after restriction along `phi`. -/
abbrev RestrictedFixedPointValue [MulAction G B] (phi : H →* G) :=
  @FixedPointValue H B _ (restrictedMulAction (A := B) phi)

/-- A surjective change of acting group preserves the complete fixed-point
subtype. -/
def fixedPointValueEquivRestricted_of_surjective [MulAction G B]
    (phi : H →* G) (hphi : Function.Surjective phi) :
    FixedPointValue (G := G) (B := B) ≃
      RestrictedFixedPointValue (B := B) phi where
  toFun b := ⟨b.1, fun h => b.2 (phi h)⟩
  invFun b :=
    ⟨b.1, by
      intro g
      obtain ⟨h, rfl⟩ := hphi g
      exact b.2 h⟩
  left_inv b := by
    apply Subtype.ext
    rfl
  right_inv b := by
    apply Subtype.ext
    rfl

/-- Finite equivariant-map counts are unchanged by a surjective change of
acting group. -/
theorem natCard_equivariantMap_eq_restricted_of_surjective
    [MulAction G A] [MulAction G B] [Finite A] [Finite B]
    (phi : H →* G) (hphi : Function.Surjective phi) :
    Nat.card (EquivariantMap (G := G) (A := A) (B := B)) =
      Nat.card (RestrictedEquivariantMap (A := A) (B := B) phi) :=
  Nat.card_congr (equivariantMapEquivRestricted_of_surjective phi hphi)

/-- Existence of an equivariant map is unchanged by a surjective change of
acting group. -/
theorem nonempty_equivariantMap_iff_restricted_of_surjective
    [MulAction G A] [MulAction G B]
    (phi : H →* G) (hphi : Function.Surjective phi) :
    Nonempty (EquivariantMap (G := G) (A := A) (B := B)) ↔
      Nonempty (RestrictedEquivariantMap (A := A) (B := B) phi) :=
  (equivariantMapEquivRestricted_of_surjective phi hphi).nonempty_congr

/-- The coinduced carrier along `phi : H →* G`: functions on `G` whose
left `phi(H)`-translation is controlled by the supplied `H`-action on `B`. -/
def CoinducedCarrier [MulAction H B] (phi : H →* G) :=
  {f : G → B // ∀ h : H, ∀ g : G, f (phi h * g) = h • f g}

/-- The `G`-action on a coinduced carrier is right translation of the function
argument. The multiplication order is what makes the adjunction map below
equivariant. -/
@[implicit_reducible]
def coinducedMulAction [MulAction H B] (phi : H →* G) :
    MulAction G (CoinducedCarrier (B := B) phi) where
  smul x f :=
    ⟨fun g => f.1 (g * x), by
      intro h g
      change f.1 ((phi h * g) * x) = h • f.1 (g * x)
      rw [mul_assoc, f.2]⟩
  one_smul f := by
    apply Subtype.ext
    funext g
    change f.1 (g * 1) = f.1 g
    rw [mul_one]
  mul_smul x y f := by
    apply Subtype.ext
    funext g
    change f.1 (g * (x * y)) = f.1 ((g * x) * y)
    rw [mul_assoc]

/-- `G`-equivariant maps into the coinduced carrier. -/
abbrev CoinducedEquivariantMap [MulAction G A] [MulAction H B]
    (phi : H →* G) :=
  @EquivariantMap G A (CoinducedCarrier (B := B) phi) _
    (coinducedMulAction (B := B) phi) inferInstance

/-- Restriction is left adjoint to coinduction for set actions. The forward
map sends `f : Res_phi A → B` to `a ↦ (g ↦ f (g • a))`; the inverse is
evaluation at the identity of `G`. Both inverse laws are explicit. -/
def restrictionCoinductionEquiv [MulAction G A] [MulAction H B]
    (phi : H →* G) :
    @EquivariantMap H A B _ inferInstance
        (restrictedMulAction (A := A) phi) ≃
      CoinducedEquivariantMap (A := A) (B := B) phi where
  toFun f :=
    ⟨fun a =>
      ⟨fun x => f.1 (x • a), by
        intro h x
        change f.1 ((phi h * x) • a) = h • f.1 (x • a)
        rw [mul_smul]
        exact f.2 h (x • a)⟩,
      by
        intro g a
        apply Subtype.ext
        funext x
        change f.1 (x • (g • a)) = f.1 ((x * g) • a)
        rw [mul_smul]⟩
  invFun F :=
    ⟨fun a => (F.1 a).1 1, by
      intro h a
      have heq := congrArg (fun q : CoinducedCarrier (B := B) phi => q.1 1)
        (F.2 (phi h) a)
      change (F.1 ((phi h) • a)).1 1 = (F.1 a).1 (1 * phi h) at heq
      change (F.1 ((phi h) • a)).1 1 = h • (F.1 a).1 1
      calc
        (F.1 ((phi h) • a)).1 1 = (F.1 a).1 (1 * phi h) := heq
        _ = h • (F.1 a).1 1 := by simpa using (F.1 a).2 h 1⟩
  left_inv f := by
    apply Subtype.ext
    funext a
    simp
  right_inv F := by
    apply Subtype.ext
    funext a
    apply Subtype.ext
    funext x
    have heq := congrArg (fun q : CoinducedCarrier (B := B) phi => q.1 1)
      (F.2 x a)
    change (F.1 (x • a)).1 1 = (F.1 a).1 (1 * x) at heq
    simpa using heq

/-- For finite carriers, restriction and coinduction have equal exact
equivariant-map counts. -/
theorem natCard_restriction_eq_coinduction [MulAction G A] [MulAction H B]
    [Finite A] [Finite G] [Finite B] (phi : H →* G) :
    Nat.card (@EquivariantMap H A B _ inferInstance
      (restrictedMulAction (A := A) phi)) =
      Nat.card (CoinducedEquivariantMap (A := A) (B := B) phi) :=
  Nat.card_congr (restrictionCoinductionEquiv (A := A) (B := B) phi)

/-- An equivariant map out of the restricted action exists exactly when the
corresponding map into the coinduced action exists. -/
theorem nonempty_restriction_iff_coinduction [MulAction G A] [MulAction H B]
    (phi : H →* G) :
    Nonempty (@EquivariantMap H A B _ inferInstance
      (restrictedMulAction (A := A) phi)) ↔
      Nonempty (CoinducedEquivariantMap (A := A) (B := B) phi) :=
  (restrictionCoinductionEquiv (A := A) (B := B) phi).nonempty_congr

end GroupActionChangeOfGroups
end GUFormalization
