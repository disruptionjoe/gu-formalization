import Mathlib

/-!
# Finite certificate for the source-native adjoint/144 degree ladder

The representation decompositions and Pati--Salam singlet multiplicities are
explicit supplied premises of the banked result.  This module checks their
intersection: the cubic adjoint channel exists, the adjoint itself has no
Pati--Salam singlet, and the first quadratic Pati--Salam-preserving owners are
exactly the symmetric `54` and `210` channels.  The alternating `45` and `945`
channels supply none.

This does not derive the decomposition tables, a Clebsch normalization, a
source action term, a family covector, a mass, or an observed-sector map.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeAdjointCoupling

/-- The finite irreducible labels needed by the exact degree-ladder check. -/
inductive Label where
  | trivial | d45 | d54 | d210 | d770 | d945 | d1050
  deriving DecidableEq, Repr

open Label

/-- Supplied irreducible support of one same-half `16 ⊗ 144` product. -/
def familyPartnerSupport : Finset Label := {d45, d54, d210, d945, d1050}

/-- Supplied support of `Sym²(45)`. -/
def symmetricAdjointSupport : Finset Label := {trivial, d54, d210, d770}

/-- Supplied support of `Λ²(45)`. -/
def alternatingAdjointSupport : Finset Label := {d45, d945}

/-- Held Pati--Salam singlet multiplicity on the relevant labels. -/
def patiSalamSinglets : Label → Nat
  | d54 | d210 => 1
  | _ => 0

/-- Candidate quadratic coupling owners are the common irreducibles. -/
def symmetricOwners : Finset Label :=
  familyPartnerSupport ∩ symmetricAdjointSupport

/-- Candidate alternating coupling owners are the common irreducibles. -/
def alternatingOwners : Finset Label :=
  familyPartnerSupport ∩ alternatingAdjointSupport

theorem cubic_adjoint_available : d45 ∈ familyPartnerSupport := by decide

theorem linear_adjoint_ps_obstructed : patiSalamSinglets d45 = 0 := by rfl

theorem symmetric_owners_exact : symmetricOwners = {d54, d210} := by decide

theorem alternating_owners_exact : alternatingOwners = {d45, d945} := by decide

theorem symmetric_owner_ps_multiplicities :
    (symmetricOwners.attach.image fun x => patiSalamSinglets x.1) = {1} := by
  decide

theorem alternating_owner_ps_multiplicities :
    (alternatingOwners.attach.image fun x => patiSalamSinglets x.1) = {0} := by
  decide

/-- Exactly two quadratic Pati--Salam-preserving representation owners occur,
both in the symmetric adjoint square. -/
theorem quadratic_ps_owner_split :
    symmetricOwners.filter (fun x => patiSalamSinglets x > 0) = {d54, d210} ∧
    alternatingOwners.filter (fun x => patiSalamSinglets x > 0) = ∅ := by
  decide

/-- Duplicating an equivalent family copy duplicates the same allowed owner
set; representation support alone supplies no family selector. -/
theorem equivalent_family_copies_same_owners (copy₁ copy₂ : Nat) :
    (copy₁, symmetricOwners) = (copy₁, {d54, d210}) ∧
    (copy₂, symmetricOwners) = (copy₂, {d54, d210}) := by
  simp [symmetric_owners_exact]

end SourceNativeAdjointCoupling
end GUFormalization
