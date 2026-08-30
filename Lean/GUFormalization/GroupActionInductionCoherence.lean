import GUFormalization.GroupActionInduction

/-!
# Coherence laws for set-level induction

This file proves that the balanced-product model of induction has the expected
unit and composition laws.  Induction along the identity is equivariantly
equivalent to the original action, and induction along a composite is
equivariantly equivalent to iterated induction.

All actions remain explicit named values.  These are pure set-level coherence
laws for supplied actions; they construct no physical action, carrier,
observer, selector, dynamics, or Geometric Unity verdict.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionInductionCoherence

open GroupActionInduction

variable {K H G B : Type*} [Group K] [Group H] [Group G]

/-- Induction along the identity homomorphism is the original acted-on type. -/
def inductionIdentityEquiv [MulAction G B] :
    InducedCarrier (B := B) (MonoidHom.id G) ≃ B := by
  letI := inductionPairMulAction (B := B) (MonoidHom.id G)
  exact {
    toFun q := Quotient.liftOn' q (fun p : G × B => p.1 • p.2) (by
      intro a b hab
      rw [MulAction.orbitRel_apply] at hab
      rcases hab with ⟨g, hab⟩
      rw [← hab]
      change (b.1 * g⁻¹) • (g • b.2) = b.1 • b.2
      rw [← mul_smul]
      simp)
    invFun b := inducedMk (MonoidHom.id G) 1 b
    left_inv q := by
      induction q using Quotient.inductionOn'
      case _ p =>
        change inducedMk (MonoidHom.id G) 1 (p.1 • p.2) =
          inducedMk (MonoidHom.id G) p.1 p.2
        simpa using
          (inducedMk_mul_phi (B := B) (MonoidHom.id G) 1 p.1 p.2).symm
    right_inv b := by
      simp [inducedMk] }

/-- The identity-induction equivalence commutes with the supplied `G`-action. -/
theorem inductionIdentityEquiv_equivariant [MulAction G B] (g : G)
    (q : InducedCarrier (B := B) (MonoidHom.id G)) :
    inductionIdentityEquiv (B := B)
        (@SMul.smul G (InducedCarrier (B := B) (MonoidHom.id G))
          (inducedMulAction (B := B) (MonoidHom.id G)).toSMul g q) =
      g • inductionIdentityEquiv (B := B) q := by
  letI := inductionPairMulAction (B := B) (MonoidHom.id G)
  induction q using Quotient.inductionOn'
  case _ p =>
    change (g * p.1) • p.2 = g • p.1 • p.2
    rw [mul_smul]

/-- Induction along a composite is equivalent to iterated induction.  The
forward map is `[g,b] ↦ [g,[1,b]]`; its inverse flattens
`[g,[h,b]] ↦ [g * psi(h),b]`. -/
def inductionCompositionEquiv [MulAction K B] (phi : K →* H) (psi : H →* G) :
    InducedCarrier (B := B) (psi.comp phi) ≃
      @InducedCarrier H G (InducedCarrier (B := B) phi) _ _
        (inducedMulAction (B := B) phi) psi := by
  letI innerAction := inducedMulAction (B := B) phi
  letI innerPairAction := inductionPairMulAction (B := B) phi
  letI compositePairAction :=
    inductionPairMulAction (B := B) (psi.comp phi)
  letI outerPairAction :=
    inductionPairMulAction (B := InducedCarrier (B := B) phi) psi
  exact {
    toFun q := Quotient.liftOn' q
      (fun p : G × B => inducedMk psi p.1 (inducedMk phi 1 p.2)) (by
        intro a b hab
        rw [MulAction.orbitRel_apply] at hab
        rcases hab with ⟨k, hab⟩
        change
          (b.1 * ((psi.comp phi) k)⁻¹, k • b.2) = a at hab
        rw [← hab]
        simp only [MonoidHom.coe_comp, Function.comp_apply]
        change
          inducedMk psi (b.1 * (psi (phi k))⁻¹) (inducedMk phi 1 (k • b.2)) =
            inducedMk psi b.1 (inducedMk phi 1 b.2)
        rw [← inducedMk_mul_phi phi 1 k b.2]
        simp only [one_mul]
        have hi : inducedMk phi (phi k) b.2 =
            @SMul.smul H (InducedCarrier (B := B) phi) innerAction.toSMul
              (phi k) (inducedMk phi 1 b.2) := by
          simpa only [mul_one] using
            (induced_smul_mk phi (phi k) 1 b.2).symm
        rw [hi]
        calc
          inducedMk psi (b.1 * (psi (phi k))⁻¹)
              (@SMul.smul H (InducedCarrier (B := B) phi) innerAction.toSMul
                (phi k) (inducedMk phi 1 b.2)) =
            inducedMk psi ((b.1 * (psi (phi k))⁻¹) * psi (phi k))
              (inducedMk phi 1 b.2) :=
                (inducedMk_mul_phi psi (b.1 * (psi (phi k))⁻¹)
                  (phi k) (inducedMk phi 1 b.2)).symm
          _ = inducedMk psi b.1 (inducedMk phi 1 b.2) := by simp)
    invFun q := Quotient.liftOn' q
      (fun p : G × InducedCarrier (B := B) phi =>
        Quotient.liftOn' p.2
          (fun r : H × B => inducedMk (psi.comp phi) (p.1 * psi r.1) r.2)
          (by
            intro a b hab
            rw [MulAction.orbitRel_apply] at hab
            rcases hab with ⟨k, hab⟩
            change (b.1 * (phi k)⁻¹, k • b.2) = a at hab
            rw [← hab]
            change
              inducedMk (psi.comp phi)
                  (p.1 * psi (b.1 * (phi k)⁻¹)) (k • b.2) =
                inducedMk (psi.comp phi) (p.1 * psi b.1) b.2
            have h := inducedMk_mul_phi (psi.comp phi)
              (p.1 * psi b.1 * ((psi.comp phi) k)⁻¹) k b.2
            simpa [map_mul, mul_assoc] using h.symm)) (by
        intro a b hab
        rw [MulAction.orbitRel_apply] at hab
        rcases hab with ⟨h, hab⟩
        change
          (b.1 * (psi h)⁻¹,
            @SMul.smul H (InducedCarrier (B := B) phi)
              innerAction.toSMul h b.2) = a at hab
        rw [← hab]
        induction b.2 using Quotient.inductionOn'
        case _ r =>
          change
            inducedMk (psi.comp phi)
                ((b.1 * (psi h)⁻¹) * psi (h * r.1)) r.2 =
              inducedMk (psi.comp phi) (b.1 * psi r.1) r.2
          simp [map_mul, mul_assoc])
    left_inv q := by
      induction q using Quotient.inductionOn'
      case _ p =>
        change inducedMk (psi.comp phi) (p.1 * psi 1) p.2 =
          inducedMk (psi.comp phi) p.1 p.2
        simp
    right_inv q := by
      induction q using Quotient.inductionOn'
      case _ p =>
        rcases p with ⟨g, inner⟩
        induction inner using Quotient.inductionOn'
        case _ r =>
          simp only [Quotient.liftOn'_mk'']
          change
            inducedMk psi (g * psi r.1) (inducedMk phi 1 r.2) =
              inducedMk psi g (inducedMk phi r.1 r.2)
          have hi : inducedMk phi r.1 r.2 =
              @SMul.smul H (InducedCarrier (B := B) phi) innerAction.toSMul
                r.1 (inducedMk phi 1 r.2) := by
            simpa only [mul_one] using
              (induced_smul_mk phi r.1 1 r.2).symm
          rw [hi]
          exact inducedMk_mul_phi psi g r.1 (inducedMk phi 1 r.2) }

/-- The composition equivalence is `G`-equivariant. -/
theorem inductionCompositionEquiv_equivariant [MulAction K B]
    (phi : K →* H) (psi : H →* G) (g : G)
    (q : InducedCarrier (B := B) (psi.comp phi)) :
    inductionCompositionEquiv (B := B) phi psi
        (@SMul.smul G (InducedCarrier (B := B) (psi.comp phi))
          (inducedMulAction (B := B) (psi.comp phi)).toSMul g q) =
      @SMul.smul G
        (@InducedCarrier H G (InducedCarrier (B := B) phi) _ _
          (inducedMulAction (B := B) phi) psi)
        (@inducedMulAction H G (InducedCarrier (B := B) phi) _ _
          (inducedMulAction (B := B) phi) psi).toSMul
        g (inductionCompositionEquiv (B := B) phi psi q) := by
  letI := inductionPairMulAction (B := B) (psi.comp phi)
  letI := inducedMulAction (B := B) phi
  letI := inductionPairMulAction (B := InducedCarrier (B := B) phi) psi
  induction q using Quotient.inductionOn'
  case _ p =>
    change inducedMk psi (g * p.1) (inducedMk phi 1 p.2) =
      inducedMk psi (g * p.1) (inducedMk phi 1 p.2)
    rfl

end GroupActionInductionCoherence
end GUFormalization
