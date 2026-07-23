import GUFormalization.LocatedNotForcedLegs

set_option autoImplicit false

/-!
# H2 — located-not-forced finite enumeration core

This module formalizes the bounded finite part of the class-C completeness claim.
The explicit `192`-dimensional carrier census is not reconstructed here.  Its computed,
independently rechecked two-block output is encoded in a finite Schur-matching model below:

* two linear-commutant generators;
* two invariant bilinear generators;
* two invariant sesquilinear generators;
* two equivariant antilinear generators;
* no cross-chirality linear generator; and
* the seven finite characteristic/arithmetic obstruction rows used by the paper.

Lean proves that this encoded list is exhaustive as a finite type, every attached modulus
is a power of two, and arbitrary finite compositions by product, gcd, and lcm remain
2-primary.  This upgrades the extension engine's arithmetic closure from an exhaustive
script sweep to a theorem.  It does **not** upgrade the carrier Hom-space computation to an
end-to-end symbolic classification, and it says nothing about non-equivariant,
function-space/Fredholm, or true-`Y14` source-action data.

The `crossChiralityKrein` row names the program-native indefinite/Krein construction; it is
not a positive-Hilbert-space premise.  The final theorem also keeps the program-native
torsion carrier `ZMod 3` distinct from a `Z`-valued generation index.
-/

namespace GUFormalization
namespace LocatedNotForcedFiniteCore

/-! ## The seven finite obstruction rows -/

/-- The seven obstruction rows in the paper's bounded class-C arithmetic census. -/
inductive CoreItem where
  | kramers
  | realPseudoreal
  | crossChiralityKrein
  | adjointComposition
  | rokhlin
  | spinorParity
  | ghostParity
  deriving DecidableEq, Fintype, Repr

/-- Exponent of the power-of-two modulus used by the finite composition engine.

The adjoint row uses the doubled `4k` proxy `8`, exactly as the extension engine's
`[2, 2, 4, 8, 16, 2, 2]` closure census.  The underlying paper identity
`4 ∣ 4k` remains separately proved by `TwoPrimary.adjoint_index_div_four`.
-/
def CoreItem.twoExponent : CoreItem → ℕ
  | .kramers => 1
  | .realPseudoreal => 1
  | .crossChiralityKrein => 2
  | .adjointComposition => 3
  | .rokhlin => 4
  | .spinorParity => 1
  | .ghostParity => 1

/-- The finite obstruction modulus attached to a core row. -/
def CoreItem.modulus (item : CoreItem) : ℕ :=
  2 ^ item.twoExponent

/-- A positive congruence modulus is 2-primary exactly when it is a power of two. -/
def IsTwoPrimaryModulus (n : ℕ) : Prop :=
  ∃ k : ℕ, n = 2 ^ k

/-- Every core obstruction row has a power-of-two modulus by construction. -/
theorem coreItem_two_primary (item : CoreItem) :
    IsTwoPrimaryModulus item.modulus :=
  ⟨item.twoExponent, rfl⟩

/-- The seven encoded moduli exactly reproduce the extension engine's finite input. -/
theorem core_moduli_exact :
    [CoreItem.kramers.modulus,
      CoreItem.realPseudoreal.modulus,
      CoreItem.crossChiralityKrein.modulus,
      CoreItem.adjointComposition.modulus,
      CoreItem.rokhlin.modulus,
      CoreItem.spinorParity.modulus,
      CoreItem.ghostParity.modulus] =
      [2, 2, 4, 8, 16, 2, 2] := by
  decide

/-- The seven-row list is exhaustive for the finite `CoreItem` type. -/
theorem coreItem_enumeration_complete (item : CoreItem) :
    item ∈ (Finset.univ : Finset CoreItem) := by
  simp

/-! ## Exact two-block matching inside the encoded carrier census -/

/-- The two inequivalent chiral irreducible blocks supplied by the carrier census:
`(3,2,16)` and `(3,2,16bar)`.  Their realization on the actual `192`-dimensional
Clifford-RS carrier remains outside this finite model. -/
inductive ChiralBlock where
  | plus
  | minus
  deriving DecidableEq, Fintype, Repr

/-- Complex duality exchanges the two chiral blocks. -/
def ChiralBlock.dual : ChiralBlock → ChiralBlock
  | .plus => .minus
  | .minus => .plus

abbrev BlockPair := ChiralBlock × ChiralBlock

def allBlockPairs : Finset BlockPair :=
  Finset.univ

/-- Schur matches for linear equivariant endomorphisms: source and target blocks agree. -/
def linearBlockMatches : Finset BlockPair :=
  allBlockPairs.filter fun pair => pair.2 = pair.1

/-- Invariant bilinear pairings match each block with its dual. -/
def bilinearBlockMatches : Finset BlockPair :=
  allBlockPairs.filter fun pair => pair.2 = pair.1.dual

/-- In the physical split/Krein signature, invariant sesquilinear forms are
cross-chirality and use the same finite partner matching.  This is not asserted for a
positive-Hilbert compact real form. -/
def sesquilinearBlockMatches : Finset BlockPair :=
  allBlockPairs.filter fun pair => pair.2 = pair.1.dual

/-- The computed split-signature antilinear generators are T-type:
they preserve the two chiral blocks. -/
def antilinearBlockMatches : Finset BlockPair :=
  allBlockPairs.filter fun pair => pair.2 = pair.1

/-- A cross-chirality linear map would need both an equivariant same-block Schur match
and distinct source/target chirality.  No pair satisfies both conditions. -/
def crossLinearBlockMatches : Finset BlockPair :=
  allBlockPairs.filter fun pair => pair.2 = pair.1 ∧ pair.2 ≠ pair.1

/-- Exact finite Schur-block counts.  These derive `2/2/2/2/0` from the encoded
two-block matching rules rather than storing those five outputs as independent numerals. -/
theorem block_match_dimensions :
    linearBlockMatches.card = 2 ∧
    bilinearBlockMatches.card = 2 ∧
    sesquilinearBlockMatches.card = 2 ∧
    antilinearBlockMatches.card = 2 ∧
    crossLinearBlockMatches.card = 0 := by
  decide

/-- Every invariant bilinear match is cross-chirality. -/
theorem bilinear_matches_cross_chirality :
    ∀ pair ∈ bilinearBlockMatches, pair.2 = pair.1.dual := by
  simp [bilinearBlockMatches, allBlockPairs]

/-- Every physical split-signature sesquilinear match is cross-chirality. -/
theorem sesquilinear_matches_cross_chirality :
    ∀ pair ∈ sesquilinearBlockMatches, pair.2 = pair.1.dual := by
  simp [sesquilinearBlockMatches, allBlockPairs]

/-- Every encoded T-type antilinear match preserves chirality. -/
theorem antilinear_matches_preserve_chirality :
    ∀ pair ∈ antilinearBlockMatches, pair.2 = pair.1 := by
  simp [antilinearBlockMatches, allBlockPairs]

/-- There is no equivariant cross-chirality linear block match in the finite model. -/
theorem no_cross_linear_block_match :
    crossLinearBlockMatches = ∅ := by
  decide

/-! ## The encoded finite class-C generator census -/

/-- The six class-C generator families.  The cross-chirality linear family is retained
as a family label even though the computed census gives it dimension zero. -/
inductive GeneratorFamily where
  | linearCommutant
  | bilinearForm
  | sesquilinearForm
  | antilinearIntertwiner
  | crossChiralityLinear
  | characteristicInput
  deriving DecidableEq, Fintype, Repr

/-- Computed basis dimensions supplied by the explicit-carrier census.

These values are data imported from the exact/computed carrier checks; this definition does
not claim to derive them from Clifford matrices inside Lean.
-/
def GeneratorFamily.basisDimension : GeneratorFamily → ℕ
  | .linearCommutant => linearBlockMatches.card
  | .bilinearForm => bilinearBlockMatches.card
  | .sesquilinearForm => sesquilinearBlockMatches.card
  | .antilinearIntertwiner => antilinearBlockMatches.card
  | .crossChiralityLinear => crossLinearBlockMatches.card
  | .characteristicInput => Fintype.card CoreItem

/-- The finite dimension packet `2/2/2/2/0`, plus seven arithmetic rows, is exact. -/
theorem encoded_family_dimensions :
    GeneratorFamily.linearCommutant.basisDimension = 2 ∧
    GeneratorFamily.bilinearForm.basisDimension = 2 ∧
    GeneratorFamily.sesquilinearForm.basisDimension = 2 ∧
    GeneratorFamily.antilinearIntertwiner.basisDimension = 2 ∧
    GeneratorFamily.crossChiralityLinear.basisDimension = 0 ∧
    GeneratorFamily.characteristicInput.basisDimension = 7 := by
  decide

/-- Actual finite generators in the encoded census.  There is deliberately no constructor
for the zero-dimensional cross-chirality linear family. -/
inductive ClassCGenerator where
  | linearCommutant (basis : {pair // pair ∈ linearBlockMatches})
  | bilinearForm (basis : {pair // pair ∈ bilinearBlockMatches})
  | sesquilinearForm (basis : {pair // pair ∈ sesquilinearBlockMatches})
  | antilinearIntertwiner (basis : {pair // pair ∈ antilinearBlockMatches})
  | characteristicInput (item : CoreItem)
  deriving DecidableEq, Fintype, Repr

/-- Family of an encoded class-C generator. -/
def ClassCGenerator.family : ClassCGenerator → GeneratorFamily
  | .linearCommutant _ => .linearCommutant
  | .bilinearForm _ => .bilinearForm
  | .sesquilinearForm _ => .sesquilinearForm
  | .antilinearIntertwiner _ => .antilinearIntertwiner
  | .characteristicInput _ => .characteristicInput

/-- Map every encoded generator to one of the seven paper obstruction rows. -/
def ClassCGenerator.obstructionItem : ClassCGenerator → CoreItem
  | .linearCommutant _ => .crossChiralityKrein
  | .bilinearForm _ => .realPseudoreal
  | .sesquilinearForm _ => .crossChiralityKrein
  | .antilinearIntertwiner _ => .kramers
  | .characteristicInput item => item

/-- Modulus carried by an encoded generator. -/
def ClassCGenerator.modulus (generator : ClassCGenerator) : ℕ :=
  generator.obstructionItem.modulus

/-- The complete finite generator set for the encoded census. -/
def finiteGeneratorSet : Finset ClassCGenerator :=
  Finset.univ

/-- The encoded class-C census has exactly fifteen generators:
`2 + 2 + 2 + 2 + 7`, with no cross-chirality linear basis element. -/
theorem finite_generator_count :
    Fintype.card ClassCGenerator = 15 := by
  decide

/-- Every encoded class-C generator occurs in the finite generator set. -/
theorem finite_generator_enumeration_complete (generator : ClassCGenerator) :
    generator ∈ finiteGeneratorSet := by
  simp [finiteGeneratorSet]

/-- Every encoded class-C generator maps to one of the seven core rows. -/
theorem generator_maps_to_core_item (generator : ClassCGenerator) :
    generator.obstructionItem ∈ (Finset.univ : Finset CoreItem) := by
  simp

/-- Every encoded class-C generator carries a power-of-two modulus. -/
theorem generator_two_primary (generator : ClassCGenerator) :
    IsTwoPrimaryModulus generator.modulus :=
  coreItem_two_primary generator.obstructionItem

/-! ## Arithmetic closure: product, gcd, and lcm -/

/-- Product of two powers of two is a power of two. -/
theorem pow_two_mul (a b : ℕ) :
    2 ^ a * 2 ^ b = 2 ^ (a + b) := by
  rw [pow_add]

/-- Gcd of two powers of two is the power at the smaller exponent. -/
theorem gcd_pow_two (a b : ℕ) :
    Nat.gcd (2 ^ a) (2 ^ b) = 2 ^ min a b := by
  apply Nat.dvd_antisymm
  · rcases le_total a b with hab | hba
    · rw [min_eq_left hab]
      exact Nat.gcd_dvd_left _ _
    · rw [min_eq_right hba]
      exact Nat.gcd_dvd_right _ _
  · exact Nat.dvd_gcd (pow_dvd_pow 2 (min_le_left a b))
      (pow_dvd_pow 2 (min_le_right a b))

/-- Lcm of two powers of two is the power at the larger exponent. -/
theorem lcm_pow_two (a b : ℕ) :
    Nat.lcm (2 ^ a) (2 ^ b) = 2 ^ max a b := by
  apply Nat.dvd_antisymm
  · exact Nat.lcm_dvd (pow_dvd_pow 2 (le_max_left a b))
      (pow_dvd_pow 2 (le_max_right a b))
  · rcases le_total a b with hab | hba
    · rw [max_eq_right hab]
      exact Nat.dvd_lcm_right _ _
    · rw [max_eq_left hba]
      exact Nat.dvd_lcm_left _ _

/-- 2-primary moduli are closed under product. -/
theorem IsTwoPrimaryModulus.mul {m n : ℕ}
    (hm : IsTwoPrimaryModulus m) (hn : IsTwoPrimaryModulus n) :
    IsTwoPrimaryModulus (m * n) := by
  rcases hm with ⟨a, rfl⟩
  rcases hn with ⟨b, rfl⟩
  exact ⟨a + b, pow_two_mul a b⟩

/-- 2-primary moduli are closed under gcd. -/
theorem IsTwoPrimaryModulus.gcd {m n : ℕ}
    (hm : IsTwoPrimaryModulus m) (hn : IsTwoPrimaryModulus n) :
    IsTwoPrimaryModulus (Nat.gcd m n) := by
  rcases hm with ⟨a, rfl⟩
  rcases hn with ⟨b, rfl⟩
  exact ⟨min a b, gcd_pow_two a b⟩

/-- 2-primary moduli are closed under lcm. -/
theorem IsTwoPrimaryModulus.lcm {m n : ℕ}
    (hm : IsTwoPrimaryModulus m) (hn : IsTwoPrimaryModulus n) :
    IsTwoPrimaryModulus (Nat.lcm m n) := by
  rcases hm with ⟨a, rfl⟩
  rcases hn with ⟨b, rfl⟩
  exact ⟨max a b, lcm_pow_two a b⟩

/-- Finite expressions generated from the class-C atoms by exactly the three composition
operations checked by the extension engine. -/
inductive CompositeModulus where
  | atom (generator : ClassCGenerator)
  | product (left right : CompositeModulus)
  | gcd (left right : CompositeModulus)
  | lcm (left right : CompositeModulus)

/-- Evaluate a finite composite obstruction modulus. -/
def CompositeModulus.value : CompositeModulus → ℕ
  | .atom generator => generator.modulus
  | .product left right => left.value * right.value
  | .gcd left right => Nat.gcd left.value right.value
  | .lcm left right => Nat.lcm left.value right.value

/-- **Bounded class-C closure theorem.**  Every finite expression generated from the
encoded class-C census by product, gcd, and lcm has a power-of-two modulus. -/
theorem composite_modulus_two_primary :
    ∀ expression : CompositeModulus, IsTwoPrimaryModulus expression.value
  | .atom generator => generator_two_primary generator
  | .product left right =>
      (composite_modulus_two_primary left).mul (composite_modulus_two_primary right)
  | .gcd left right =>
      (composite_modulus_two_primary left).gcd (composite_modulus_two_primary right)
  | .lcm left right =>
      (composite_modulus_two_primary left).lcm (composite_modulus_two_primary right)

/-! ## The native torsion carrier is not an integer-valued generation index -/

/-- Program-native order-three torsion carrier. -/
abbrev NativeTorsionCarrier := ZMod 3

/-- A literal integer-valued generation index.  This is a distinct target type. -/
abbrev IntegerGenerationIndex := ℤ

/-- Any additive map from the program-native `Z/3` torsion carrier to a literal
`Z`-valued generation index is zero.  The torsion carrier therefore cannot silently be
identified with an integer count. -/
theorem native_torsion_carrier_to_integer_index_zero
    (f : NativeTorsionCarrier →+ IntegerGenerationIndex) :
    f = 0 := by
  ext x
  have hx : (3 : ℕ) • x = 0 := by
    rw [nsmul_eq_mul]
    have hcast : ((3 : ℕ) : ZMod 3) = 0 := ZMod.natCast_self 3
    rw [hcast, zero_mul]
  have hfx : (3 : ℕ) • f x = 0 := by
    rw [← map_nsmul, hx, map_zero]
  simp only [AddMonoidHom.zero_apply]
  simp at hfx
  omega

end LocatedNotForcedFiniteCore
end GUFormalization
