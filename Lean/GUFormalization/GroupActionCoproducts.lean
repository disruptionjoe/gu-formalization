import GUFormalization.GroupActionFixedPoints
import Mathlib.Algebra.Group.Action.Sigma

/-!
# Equivariant maps from indexed coproducts

This file proves the set-level coproduct law for equivariant maps. The action
on a dependent sum preserves its index and acts only within each fiber, so an
equivariant map out of the sum is exactly a family of equivariant maps out of
its components.

The result is pure mathematics. It introduces no physical interpretation and
does not identify or mix distinct indices.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionFixedPoints

variable {G B : Type*} [Group G] [MulAction G B]

/-- Equivariant maps from an indexed dependent sum are exactly indexed
families of equivariant maps from its heterogeneous fibers. The Sigma action
preserves the index, so no action or mixing on the index type is assumed. -/
def equivariantMapEquivSigma {I : Type*} {A : I → Type*}
    [∀ i, MulAction G (A i)] :
    EquivariantMap (G := G) (A := Σ i, A i) (B := B) ≃
      (∀ i, EquivariantMap (G := G) (A := A i) (B := B)) where
  toFun f := fun i =>
    ⟨fun a => f.1 ⟨i, a⟩, by
      intro g a
      simpa only [Sigma.smul_mk] using f.2 g ⟨i, a⟩⟩
  invFun fs :=
    ⟨fun x => (fs x.1).1 x.2, by
      intro g x
      rcases x with ⟨i, a⟩
      simpa only [Sigma.smul_mk] using (fs i).2 g a⟩
  left_inv f := by
    apply Subtype.ext
    funext x
    rfl
  right_inv fs := by
    funext i
    apply Subtype.ext
    funext a
    rfl

/-- For a finite index, finite heterogeneous fibers, and a finite codomain,
the equivariant-map count from the indexed dependent sum is the product of
the component equivariant-map counts. The empty product is `1`, matching the
unique map from the empty dependent sum. -/
theorem natCard_equivariantMap_sigma {I : Type*} {A : I → Type*}
    [∀ i, MulAction G (A i)] [Fintype I] [∀ i, Finite (A i)] [Finite B] :
    Nat.card (EquivariantMap (G := G) (A := Σ i, A i) (B := B)) =
      ∏ i, Nat.card (EquivariantMap (G := G) (A := A i) (B := B)) := by
  rw [Nat.card_congr (equivariantMapEquivSigma (G := G) (B := B) (A := A)),
    Nat.card_pi]

/-- An equivariant map from an indexed dependent sum exists exactly when
every component admits an equivariant map. The reverse direction uses choice
for the possibly infinite index family; for an empty index both sides are
nonempty. -/
theorem nonempty_equivariantMap_sigma_iff {I : Type*} {A : I → Type*}
    [∀ i, MulAction G (A i)] :
    Nonempty (EquivariantMap (G := G) (A := Σ i, A i) (B := B)) ↔
      ∀ i, Nonempty (EquivariantMap (G := G) (A := A i) (B := B)) :=
  (equivariantMapEquivSigma (G := G) (B := B) (A := A)).nonempty_congr.trans
    Classical.nonempty_pi

end GroupActionFixedPoints
end GUFormalization
