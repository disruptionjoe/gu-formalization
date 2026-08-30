import GUFormalization.GroupActionFixedPoints
import Mathlib.Algebra.Group.Action.Basic
import Mathlib.Algebra.Group.Action.Prod

/-!
# Equivariant internal homs

This file gives the function type `A → B` the explicit conjugation action

`(g • f) a = g • f (g⁻¹ • a)`.

Its common fixed points are exactly the equivariant maps `A → B`, and the
usual curry/uncurry equivalence restricts to equivariant maps when products
carry the diagonal action. The action is a named definition rather than a
global instance, avoiding ambiguity with the ordinary pointwise function
action.

These results are pure set-level mathematics. They construct no physical
action, observer, dynamics, selection mechanism, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace EquivariantInternalHom

open GroupActionFixedPoints

variable {G A B C : Type*} [Group G]

/-- The conjugation action on a function space. This is deliberately not a
global instance: clients opt into it locally or pass it explicitly. -/
@[implicit_reducible]
def internalHomMulAction [MulAction G A] [MulAction G B] :
    MulAction G (A → B) where
  smul g f a := g • f (g⁻¹ • a)
  one_smul f := by
    change (fun a => (1 : G) • f ((1 : G)⁻¹ • a)) = f
    simp only [inv_one, one_smul]
  mul_smul g h f := by
    change (fun a => (g * h) • f ((g * h)⁻¹ • a)) =
      (fun a => g • (h • f (h⁻¹ • (g⁻¹ • a))))
    simp only [mul_inv_rev, mul_smul]

@[simp]
theorem internalHom_smul_apply [MulAction G A] [MulAction G B]
    (g : G) (f : A → B) (a : A) :
    (internalHomMulAction (G := G) (A := A) (B := B)).smul g f a =
      g • f (g⁻¹ • a) := by
  rfl

/-- Functions fixed by every group element under the internal-hom action. The
action is supplied explicitly, so this abbreviation installs no instance. -/
abbrev InternalHomFixedPoint [MulAction G A] [MulAction G B] :=
  @FixedPointValue G (A → B) _
    (internalHomMulAction (G := G) (A := A) (B := B))

/-- Common fixed points of the internal-hom action are exactly equivariant
maps. -/
def internalHomFixedPointEquivEquivariantMap [MulAction G A] [MulAction G B] :
    InternalHomFixedPoint (G := G) (A := A) (B := B) ≃
      EquivariantMap (G := G) (A := A) (B := B) where
  toFun f :=
    ⟨f.1, by
      intro g a
      have h := congrFun (f.2 g) (g • a)
      change g • f.1 (g⁻¹ • (g • a)) = f.1 (g • a) at h
      simpa using h.symm⟩
  invFun f :=
    ⟨f.1, by
      intro g
      funext a
      change g • f.1 (g⁻¹ • a) = f.1 a
      simpa using (f.2 g (g⁻¹ • a)).symm⟩
  left_inv f := by
    apply Subtype.ext
    rfl
  right_inv f := by
    apply Subtype.ext
    rfl

/-- Equivariant maps from `A` into the internal hom `C → B`. The codomain
action is passed explicitly, so no competing function-space instance is
installed. -/
abbrev CurriedEquivariantMap [MulAction G A] [MulAction G C]
    [MulAction G B] :=
  @EquivariantMap G A (C → B) _
    (internalHomMulAction (G := G) (A := C) (B := B)) _

/-- Equivariant currying and uncurrying for the diagonal action on `A × C`
and the internal-hom action on `C → B`. -/
def equivariantMapCurry [MulAction G A] [MulAction G C] [MulAction G B] :
    EquivariantMap (G := G) (A := A × C) (B := B) ≃
      CurriedEquivariantMap (G := G) (A := A) (C := C) (B := B) where
  toFun f :=
    ⟨fun a c => f.1 (a, c), by
      intro g a
      funext c
      change f.1 (g • a, c) = g • f.1 (a, g⁻¹ • c)
      simpa using f.2 g (a, g⁻¹ • c)⟩
  invFun f :=
    ⟨fun ac => f.1 ac.1 ac.2, by
      intro g ac
      rcases ac with ⟨a, c⟩
      have h := congrFun (f.2 g a) (g • c)
      change f.1 (g • a) (g • c) =
        g • f.1 a (g⁻¹ • (g • c)) at h
      change f.1 (g • a) (g • c) = g • f.1 a c
      simpa using h⟩
  left_inv f := by
    apply Subtype.ext
    funext ac
    cases ac
    rfl
  right_inv f := by
    apply Subtype.ext
    rfl

end EquivariantInternalHom
end GUFormalization
