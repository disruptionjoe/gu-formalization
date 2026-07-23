import GUFormalization.LocatedNotForcedFiniteCore

set_option autoImplicit false

/-!
Targeted H2 smoke certificate.

This file checks the public theorem surface without adding physical premises.  The default
library build checks the proof-bearing module; run this entrypoint separately with:

    lake env lean tests/located-not-forced/H2_FiniteCore.lean
-/

namespace GUFormalization.LocatedNotForcedFiniteCore

example :
    linearBlockMatches.card = 2 ∧
    bilinearBlockMatches.card = 2 ∧
    sesquilinearBlockMatches.card = 2 ∧
    antilinearBlockMatches.card = 2 ∧
    crossLinearBlockMatches.card = 0 :=
  block_match_dimensions

example : crossLinearBlockMatches = ∅ :=
  no_cross_linear_block_match

example :
    [FiniteTorsionRow.kramers.modulus,
      FiniteTorsionRow.realPseudoreal.modulus,
      FiniteTorsionRow.rokhlin.modulus] =
      [2, 2, 16] :=
  finite_torsion_moduli_exact

example : Fintype.card CoreItem = 7 :=
  core_item_count

example : Fintype.card ClassCGenerator = 15 :=
  finite_generator_count

example (generator : ClassCGenerator) :
    generator ∈ finiteGeneratorSet :=
  finite_generator_enumeration_complete generator

example (row : FiniteTorsionRow) :
    IsTwoPrimaryModulus row.modulus :=
  finite_torsion_row_two_primary row

example : BoundedClassCConclusion :=
  bounded_class_c_codomain_separated

example (expression : CompositeModulus) :
    IsTwoPrimaryModulus expression.value :=
  composite_modulus_two_primary expression

example (a b : ℕ) :
    Nat.gcd (2 ^ a) (2 ^ b) = 2 ^ min a b :=
  gcd_pow_two a b

example (a b : ℕ) :
    Nat.lcm (2 ^ a) (2 ^ b) = 2 ^ max a b :=
  lcm_pow_two a b

example (f : ZMod 3 →+ ℤ) : f = 0 :=
  native_torsion_carrier_to_integer_index_zero f

example (k : ℤ) : Even (21 * (16 * k) / 8) :=
  TwoPrimary.rs_bulk_even k

example (q : ℤ) : Odd (2 * q ^ 2 - 4 * q + 1) :=
  TwoPrimary.lens_eta_numerator_odd q

example (k : ℕ) : ¬ (3 ∣ 2 ^ k) :=
  TwoPrimary.spinor_dim_not_div_three k

#print axioms finite_generator_count
#print axioms bounded_class_c_codomain_separated
#print axioms composite_modulus_two_primary
#print axioms native_torsion_carrier_to_integer_index_zero

end GUFormalization.LocatedNotForcedFiniteCore
