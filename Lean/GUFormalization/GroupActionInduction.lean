import GUFormalization.GroupActionChangeOfGroups
import Mathlib.GroupTheory.GroupAction.Quotient

/-!
# Induction for set-level group actions

For a homomorphism `phi : H →* G` and an `H`-set `B`, this file constructs
the induced `G`-set as the orbit quotient of `G × B` by the action

`h • (g, b) = (g * (phi h)⁻¹, h • b)`.

Left multiplication on the `G` coordinate commutes with that action and
therefore descends to the quotient. The resulting carrier satisfies the
induction-restriction adjunction

`Hom_G (Ind_phi B, C) ≃ Hom_H (B, Res_phi C)`.

All actions introduced here are explicit named values rather than global
instances. The results are pure set-level mathematics: they construct no
physical group action, observer, selector, dynamics, or Geometric Unity
verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionInduction

open GroupActionFixedPoints GroupActionChangeOfGroups

variable {H G B C : Type*} [Group H] [Group G]

/-- The `H`-action whose orbit quotient is the induced carrier. The inverse
on `phi h` is load-bearing: it makes this a left action while encoding the
balanced-product relation `(g * phi h, b) ~ (g, h • b)`. -/
@[implicit_reducible]
def inductionPairMulAction [MulAction H B] (phi : H →* G) :
    MulAction H (G × B) where
  smul h p := (p.1 * (phi h)⁻¹, h • p.2)
  one_smul p := by
    change (p.1 * (phi 1)⁻¹, (1 : H) • p.2) = p
    ext <;> simp
  mul_smul h k p := by
    change
      (p.1 * (phi (h * k))⁻¹, (h * k) • p.2) =
        ((p.1 * (phi k)⁻¹) * (phi h)⁻¹, h • k • p.2)
    rw [map_mul, mul_inv_rev, mul_assoc, mul_smul]

/-- The induced carrier `G ×_H B`, realized as the orbit quotient of the
explicit action on `G × B`. -/
abbrev InducedCarrier [MulAction H B] (phi : H →* G) :=
  @MulAction.orbitRel.Quotient H (G × B) _ (inductionPairMulAction phi)

/-- The class of `(g,b)` in the induced carrier. -/
def inducedMk [MulAction H B] (phi : H →* G) (g : G) (b : B) :
    InducedCarrier (B := B) phi :=
  @Quotient.mk'' (G × B)
    (@MulAction.orbitRel H (G × B) _ (inductionPairMulAction phi)) (g, b)

/-- The balanced-product relation in its useful forward orientation. -/
theorem inducedMk_mul_phi [MulAction H B] (phi : H →* G)
    (g : G) (h : H) (b : B) :
    inducedMk phi (g * phi h) b = inducedMk phi g (h • b) := by
  letI := inductionPairMulAction (B := B) phi
  apply Quotient.sound
  exact ⟨h⁻¹, by
    change (g * (phi (h⁻¹))⁻¹, h⁻¹ • h • b) = (g * phi h, b)
    ext <;> simp [map_inv]⟩

/-- Left multiplication on `G × B` descends to the induced carrier because
it commutes with the quotienting `H`-action. -/
@[implicit_reducible]
def inducedMulAction [MulAction H B] (phi : H →* G) :
    MulAction G (InducedCarrier (B := B) phi) := by
  letI := inductionPairMulAction (B := B) phi
  exact {
    smul x q :=
      Quotient.map' (fun p : G × B => (x * p.1, p.2)) (by
        intro a b hab
        rw [MulAction.orbitRel_apply] at hab ⊢
        rcases hab with ⟨h, hab⟩
        refine ⟨h, ?_⟩
        rw [← hab]
        change ((x * b.1) * (phi h)⁻¹, h • b.2) =
          (x * (b.1 * (phi h)⁻¹), h • b.2)
        ext <;> simp [mul_assoc]) q
    one_smul q := by
      induction q using Quotient.inductionOn'
      case _ p =>
        apply congrArg Quotient.mk''
        ext <;> simp
    mul_smul x y q := by
      induction q using Quotient.inductionOn'
      case _ p =>
        apply congrArg Quotient.mk''
        ext
        · simp [mul_assoc]
        · rfl }

@[simp]
theorem induced_smul_mk [MulAction H B] (phi : H →* G)
    (x g : G) (b : B) :
    @SMul.smul G (InducedCarrier (B := B) phi) (inducedMulAction phi).toSMul
      x (inducedMk phi g b) = inducedMk phi (x * g) b := by
  letI := inductionPairMulAction (B := B) phi
  change
    Quotient.map' (fun p : G × B => (x * p.1, p.2)) _
      (Quotient.mk'' (g, b)) = Quotient.mk'' (x * g, b)
  exact Quotient.map'_mk'' _ _ _

/-- `G`-equivariant maps out of the induced carrier. -/
abbrev InducedEquivariantMap [MulAction H B] [MulAction G C]
    (phi : H →* G) :=
  @EquivariantMap G (InducedCarrier (B := B) phi) C _ inferInstance
    (inducedMulAction (B := B) phi)

/-- Induction is left adjoint to restriction for set actions. Evaluation on
`[1,b]` is inverse to the quotient-defined map `[g,b] ↦ g • u(b)`. -/
def inductionRestrictionEquiv [MulAction H B] [MulAction G C]
    (phi : H →* G) :
    InducedEquivariantMap (B := B) (C := C) phi ≃
      @EquivariantMap H B C _
        (restrictedMulAction (A := C) phi) inferInstance := by
  letI := inductionPairMulAction (B := B) phi
  exact {
    toFun f :=
      ⟨fun b => f.1 (inducedMk phi 1 b), by
        intro h b
        change f.1 (inducedMk phi 1 (h • b)) =
          phi h • f.1 (inducedMk phi 1 b)
        rw [← inducedMk_mul_phi phi 1 h b]
        have hf := f.2 (phi h) (inducedMk phi 1 b)
        change f.1 (@SMul.smul G (InducedCarrier (B := B) phi)
          (inducedMulAction phi).toSMul (phi h) (inducedMk phi 1 b)) =
            phi h • f.1 (inducedMk phi 1 b) at hf
        rw [induced_smul_mk, mul_one] at hf
        rw [one_mul]
        exact hf⟩
    invFun u :=
      ⟨fun q => Quotient.liftOn' q (fun p : G × B => p.1 • u.1 p.2) (by
          intro a b hab
          rw [MulAction.orbitRel_apply] at hab
          rcases hab with ⟨h, hab⟩
          rw [← hab]
          change (b.1 * (phi h)⁻¹) • u.1 (h • b.2) = b.1 • u.1 b.2
          have hu := u.2 h b.2
          change u.1 (h • b.2) = phi h • u.1 b.2 at hu
          rw [hu, ← mul_smul]
          simp), by
        intro x q
        induction q using Quotient.inductionOn'
        case _ p =>
          change (x * p.1) • u.1 p.2 = x • p.1 • u.1 p.2
          rw [mul_smul]⟩
    left_inv f := by
      apply Subtype.ext
      funext q
      induction q using Quotient.inductionOn'
      case _ p =>
        change p.1 • f.1 (inducedMk phi 1 p.2) =
          f.1 (inducedMk phi p.1 p.2)
        have hf := (f.2 p.1 (inducedMk phi 1 p.2)).symm
        change p.1 • f.1 (inducedMk phi 1 p.2) =
          f.1 (@SMul.smul G (InducedCarrier (B := B) phi)
            (inducedMulAction phi).toSMul p.1 (inducedMk phi 1 p.2)) at hf
        rw [induced_smul_mk, mul_one] at hf
        exact hf
    right_inv u := by
      apply Subtype.ext
      funext b
      simp [inducedMk] }

/-- For finite carriers, induction-restriction gives equal exact
equivariant-map counts. -/
theorem natCard_induction_eq_restriction [MulAction H B] [MulAction G C]
    [Finite G] [Finite B] [Finite C] (phi : H →* G) :
    Nat.card (InducedEquivariantMap (B := B) (C := C) phi) =
      Nat.card (@EquivariantMap H B C _
        (restrictedMulAction (A := C) phi) inferInstance) :=
  Nat.card_congr (inductionRestrictionEquiv (B := B) (C := C) phi)

/-- An equivariant map from the induced action exists exactly when the seed
map into the restricted action exists. -/
theorem nonempty_induction_iff_restriction [MulAction H B] [MulAction G C]
    (phi : H →* G) :
    Nonempty (InducedEquivariantMap (B := B) (C := C) phi) ↔
      Nonempty (@EquivariantMap H B C _
        (restrictedMulAction (A := C) phi) inferInstance) :=
  (inductionRestrictionEquiv (B := B) (C := C) phi).nonempty_congr

end GroupActionInduction
end GUFormalization
