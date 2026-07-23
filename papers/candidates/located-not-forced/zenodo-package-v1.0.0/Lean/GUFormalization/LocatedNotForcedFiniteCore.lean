import GUFormalization.LocatedNotForcedLegs

set_option autoImplicit false

/-!
# H2 — located-not-forced finite enumeration core

This module formalizes the bounded, codomain-separated part of the class-C completeness
claim.  The explicit `192`-dimensional carrier census is not reconstructed here.  Its
computed, independently rechecked two-block output is encoded in a finite Schur-matching
model below:

* two linear-commutant generators;
* two invariant bilinear generators;
* two invariant sesquilinear generators;
* two equivariant antilinear generators;
* no cross-chirality linear generator; and
* the seven characteristic/arithmetic rows used by the paper, separated by codomain.

Lean proves that this encoded list is exhaustive as a finite type, every finite-torsion
modulus is a power of two, and arbitrary finite compositions of torsion moduli by product,
gcd, and lcm remain 2-primary.  Integer equalities, integer divisibility statements,
representation dimensions, and rank diagnostics have distinct constructors and no
modulus.  CRT projection requires an explicit torsion-valued map into `ZMod 24`.

This upgrades the extension engine's finite deduction from an exhaustive script sweep to
a theorem.  It does **not** upgrade the carrier Hom-space computation to an end-to-end
symbolic classification, and it says nothing about non-equivariant,
function-space/Fredholm, or true-`Y14` source-action data.  The cross-chirality equality
names the program-native indefinite/Krein construction, not a positive-Hilbert-space
premise.  The final theorem also keeps the program-native torsion carrier `ZMod 3`
distinct from a `Z`-valued generation index.
-/

namespace GUFormalization
namespace LocatedNotForcedFiniteCore

/-! ## The seven rows, separated by codomain -/

/-- Codomains that occur in the bounded packet, plus the deliberately absent target
codomain of a selected generation integer. -/
inductive ConstraintCodomain where
  | finiteTorsion
  | integerEquality
  | integerDivisibility
  | representationDimension
  | diagnostic
  | selectedGenerationInteger
  deriving DecidableEq, Fintype, Repr

/-- The three rows whose values genuinely live in finite torsion groups. -/
inductive FiniteTorsionRow where
  | kramers
  | realPseudoreal
  | rokhlin
  deriving DecidableEq, Fintype, Repr

/-- Exponent of the actual power-of-two torsion modulus. -/
def FiniteTorsionRow.twoExponent : FiniteTorsionRow → ℕ
  | .kramers => 1
  | .realPseudoreal => 1
  | .rokhlin => 4

/-- A modulus exists only for a finite-torsion row. -/
def FiniteTorsionRow.modulus (row : FiniteTorsionRow) : ℕ :=
  2 ^ row.twoExponent

/-- The program-native finite value type of a torsion row. -/
abbrev FiniteTorsionRow.Value (row : FiniteTorsionRow) :=
  ZMod row.modulus

/-- The `Z`-valued cross-chirality Krein intersection equality. -/
inductive IntegerEqualityRow where
  | crossChiralityKrein
  deriving DecidableEq, Fintype, Repr

def IntegerEqualityRow.lhs : IntegerEqualityRow → ℤ
  | .crossChiralityKrein => 0

def IntegerEqualityRow.rhs : IntegerEqualityRow → ℤ
  | .crossChiralityKrein => 0

/-- The `Z`-valued adjoint-index divisibility row. -/
inductive IntegerDivisibilityRow where
  | adjointComposition
  deriving DecidableEq, Fintype, Repr

def IntegerDivisibilityRow.indexFour : IntegerDivisibilityRow → ℤ → ℤ
  | .adjointComposition, k => 4 * k

def IntegerDivisibilityRow.indexTwelve : IntegerDivisibilityRow → ℤ → ℤ
  | .adjointComposition, k => 12 * k

def IntegerDivisibilityRow.indexTwentyFour : IntegerDivisibilityRow → ℤ → ℤ
  | .adjointComposition, k => 24 * k

/-- The irreducible-spinor representation-dimension row. -/
inductive RepresentationDimensionRow where
  | irreducibleSpinor
  deriving DecidableEq, Fintype, Repr

def RepresentationDimensionRow.dimension :
    RepresentationDimensionRow → ℕ → ℕ
  | .irreducibleSpinor, exponent => 2 ^ exponent

/-- The balanced-rank diagnostic.  It is not a torsion class or integer index. -/
inductive DiagnosticRow where
  | ghostRankBalance
  deriving DecidableEq, Fintype, Repr

def DiagnosticRow.positiveRank : DiagnosticRow → ℕ
  | .ghostRankBalance => 96

def DiagnosticRow.negativeRank : DiagnosticRow → ℕ
  | .ghostRankBalance => 96

/-- The exact seven-row packet.  Each constructor fixes the row's codomain. -/
inductive CoreItem where
  | finiteTorsion (row : FiniteTorsionRow)
  | integerEquality (row : IntegerEqualityRow)
  | integerDivisibility (row : IntegerDivisibilityRow)
  | representationDimension (row : RepresentationDimensionRow)
  | diagnostic (row : DiagnosticRow)
  deriving DecidableEq, Fintype, Repr

def CoreItem.codomain : CoreItem → ConstraintCodomain
  | .finiteTorsion _ => .finiteTorsion
  | .integerEquality _ => .integerEquality
  | .integerDivisibility _ => .integerDivisibility
  | .representationDimension _ => .representationDimension
  | .diagnostic _ => .diagnostic

/-- A positive congruence modulus is 2-primary exactly when it is a power of two. -/
def IsTwoPrimaryModulus (n : ℕ) : Prop :=
  ∃ k : ℕ, n = 2 ^ k

/-- Every finite-torsion row has a power-of-two modulus by construction. -/
theorem finite_torsion_row_two_primary (row : FiniteTorsionRow) :
    IsTwoPrimaryModulus row.modulus :=
  ⟨row.twoExponent, rfl⟩

/-- The only three torsion moduli in the packet are `2`, `2`, and `16`. -/
theorem finite_torsion_moduli_exact :
    [FiniteTorsionRow.kramers.modulus,
      FiniteTorsionRow.realPseudoreal.modulus,
      FiniteTorsionRow.rokhlin.modulus] = [2, 2, 16] := by
  decide

/-- The packet contains exactly seven codomain-separated rows. -/
theorem core_item_count : Fintype.card CoreItem = 7 := by
  decide

/-- The seven-row packet is exhaustive for the finite `CoreItem` type. -/
theorem coreItem_enumeration_complete (item : CoreItem) :
    item ∈ (Finset.univ : Finset CoreItem) := by
  simp

/-- No encoded row has the codomain of a selected generation integer. -/
theorem no_core_item_selects_generation_integer (item : CoreItem) :
    item.codomain ≠ .selectedGenerationInteger := by
  cases item <;> simp [CoreItem.codomain]

/-- Integer equality rows are disjoint from finite-torsion rows by construction. -/
theorem integer_equality_ne_finite_torsion
    (integerRow : IntegerEqualityRow) (torsionRow : FiniteTorsionRow) :
    CoreItem.integerEquality integerRow ≠ CoreItem.finiteTorsion torsionRow := by
  simp

/-- Integer divisibility rows are disjoint from finite-torsion rows by construction. -/
theorem integer_divisibility_ne_finite_torsion
    (integerRow : IntegerDivisibilityRow) (torsionRow : FiniteTorsionRow) :
    CoreItem.integerDivisibility integerRow ≠ CoreItem.finiteTorsion torsionRow := by
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

/-- Map every encoded generator to one of the seven paper rows without erasing codomain. -/
def ClassCGenerator.constraint : ClassCGenerator → CoreItem
  | .linearCommutant _ => .integerEquality .crossChiralityKrein
  | .bilinearForm _ => .finiteTorsion .realPseudoreal
  | .sesquilinearForm _ => .integerEquality .crossChiralityKrein
  | .antilinearIntertwiner _ => .finiteTorsion .kramers
  | .characteristicInput item => item

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
    generator.constraint ∈ (Finset.univ : Finset CoreItem) := by
  simp

/-- A generator has a modulus only after a proof that its row is finite torsion. -/
theorem torsion_generator_two_primary
    (generator : ClassCGenerator) (row : FiniteTorsionRow)
    (_hrow : generator.constraint = .finiteTorsion row) :
    IsTwoPrimaryModulus row.modulus := by
  exact finite_torsion_row_two_primary row

/-! ## Finite-torsion arithmetic closure: product, gcd, and lcm -/

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

/-- Finite expressions generated only from torsion-valued atoms by exactly the three
composition operations checked by the extension engine. -/
inductive CompositeModulus where
  | atom (row : FiniteTorsionRow)
  | product (left right : CompositeModulus)
  | gcd (left right : CompositeModulus)
  | lcm (left right : CompositeModulus)

/-- Evaluate a finite composite obstruction modulus. -/
def CompositeModulus.value : CompositeModulus → ℕ
  | .atom row => row.modulus
  | .product left right => left.value * right.value
  | .gcd left right => Nat.gcd left.value right.value
  | .lcm left right => Nat.lcm left.value right.value

/-- **Bounded class-C closure theorem.**  Every finite expression generated from the
encoded class-C census by product, gcd, and lcm has a power-of-two modulus. -/
theorem composite_modulus_two_primary :
    ∀ expression : CompositeModulus, IsTwoPrimaryModulus expression.value
  | .atom row => finite_torsion_row_two_primary row
  | .product left right =>
      (composite_modulus_two_primary left).mul (composite_modulus_two_primary right)
  | .gcd left right =>
      (composite_modulus_two_primary left).gcd (composite_modulus_two_primary right)
  | .lcm left right =>
      (composite_modulus_two_primary left).lcm (composite_modulus_two_primary right)

/-! ## Exact content of the non-torsion rows -/

/-- No odd prime divides an encoded finite-torsion modulus. -/
theorem finite_torsion_row_no_odd_prime_modulus
    (row : FiniteTorsionRow) (p : ℕ) (hp : Nat.Prime p) (hp_ne_two : p ≠ 2) :
    ¬ p ∣ row.modulus := by
  intro hdiv
  rcases finite_torsion_row_two_primary row with ⟨exponent, hexponent⟩
  rw [hexponent] at hdiv
  have hp_dvd_two : p ∣ 2 := hp.dvd_of_dvd_pow hdiv
  rcases (Nat.dvd_prime (by norm_num : Nat.Prime 2)).mp hp_dvd_two with hp_one | hp_two
  · exact hp.ne_one hp_one
  · exact hp_ne_two hp_two

/-- The supplied finite intersection difference is the literal `Z`-valued equality
`0 = 0`; it is not the separate `96/96` signature or rank diagnostic. -/
theorem integer_equalities_exact (row : IntegerEqualityRow) :
    row.lhs = row.rhs := by
  cases row
  norm_num [IntegerEqualityRow.lhs, IntegerEqualityRow.rhs]

/-- The three adjoint-index formulas remain literal `Z`-valued divisibility statements. -/
theorem integer_divisibility_exact (row : IntegerDivisibilityRow) (k : ℤ) :
    (4 : ℤ) ∣ row.indexFour k ∧
    (12 : ℤ) ∣ row.indexTwelve k ∧
    (24 : ℤ) ∣ row.indexTwentyFour k := by
  cases row
  exact ⟨⟨k, rfl⟩, ⟨k, rfl⟩, ⟨k, rfl⟩⟩

/-- Every encoded irreducible-spinor dimension is exactly a power of two. -/
theorem representation_dimensions_exact
    (row : RepresentationDimensionRow) (exponent : ℕ) :
    row.dimension exponent = 2 ^ exponent := by
  cases row
  rfl

/-- The ghost-pairing output is a balanced rank diagnostic, not a count. -/
theorem diagnostic_ranks_exact (row : DiagnosticRow) :
    row.positiveRank = 96 ∧
    row.negativeRank = 96 ∧
    row.positiveRank = row.negativeRank := by
  cases row
  decide

/-! ## CRT accepts only explicitly mapped finite torsion -/

/-- A torsion row together with a value and an explicit additive map into the framed
`ZMod 24` class.  Merely having a core row does not construct this packet. -/
structure MappedTorsionInput where
  source : FiniteTorsionRow
  sourceValue : source.Value
  toFramedClass : source.Value →+ ZMod 24

def MappedTorsionInput.framedValue (input : MappedTorsionInput) : ZMod 24 :=
  input.toFramedClass input.sourceValue

/-- CRT projection to the 2-primary summand.  Its input type contains only finite torsion. -/
def crtTwoPrimaryProjection (input : MappedTorsionInput) : ZMod 8 :=
  ZMod.castHom (by norm_num : 8 ∣ 24) (ZMod 8) input.framedValue

/-- CRT projection to the 3-primary summand.  Its input type contains only finite torsion. -/
def crtThreePrimaryProjection (input : MappedTorsionInput) : ZMod 3 :=
  ZMod.castHom (by norm_num : 3 ∣ 24) (ZMod 3) input.framedValue

/-! ## The exact bounded manuscript conclusion -/

/-- The machine-checked conclusion obtained from the encoded finite packet. -/
structure BoundedClassCConclusion : Prop where
  rowCount : Fintype.card CoreItem = 7
  generatorCount : Fintype.card ClassCGenerator = 15
  rowsExhaustive : ∀ item : CoreItem, item ∈ (Finset.univ : Finset CoreItem)
  generatorsExhaustive :
    ∀ generator : ClassCGenerator, generator ∈ finiteGeneratorSet
  noSelectedGenerationInteger :
    ∀ item : CoreItem, item.codomain ≠ .selectedGenerationInteger
  finiteTorsionTwoPrimary :
    ∀ row : FiniteTorsionRow, IsTwoPrimaryModulus row.modulus
  finiteTorsionHasNoOddPrimeModulus :
    ∀ (row : FiniteTorsionRow) (p : ℕ),
      Nat.Prime p → p ≠ 2 → ¬ p ∣ row.modulus
  integerEqualitiesRemainZ :
    ∀ row : IntegerEqualityRow, row.lhs = row.rhs
  integerDivisibilityRemainsZ :
    ∀ (row : IntegerDivisibilityRow) (k : ℤ),
      (4 : ℤ) ∣ row.indexFour k ∧
      (12 : ℤ) ∣ row.indexTwelve k ∧
      (24 : ℤ) ∣ row.indexTwentyFour k
  representationDimensionsRemainDimensions :
    ∀ (row : RepresentationDimensionRow) (exponent : ℕ),
      row.dimension exponent = 2 ^ exponent
  diagnosticsRemainDiagnostics :
    ∀ row : DiagnosticRow,
      row.positiveRank = 96 ∧
      row.negativeRank = 96 ∧
      row.positiveRank = row.negativeRank

/-- **Codomain-separated bounded class-C theorem.**  The encoded packet has exactly the
fifteen supplied generators and seven rows; finite torsion is 2-primary with no odd-prime
modulus; the integer rows remain literal equalities/divisibility statements in `Z`;
representation dimensions and diagnostics remain in their own codomains; and no
constructor supplies a selected generation integer. -/
theorem bounded_class_c_codomain_separated :
    BoundedClassCConclusion where
  rowCount := core_item_count
  generatorCount := finite_generator_count
  rowsExhaustive := coreItem_enumeration_complete
  generatorsExhaustive := finite_generator_enumeration_complete
  noSelectedGenerationInteger := no_core_item_selects_generation_integer
  finiteTorsionTwoPrimary := finite_torsion_row_two_primary
  finiteTorsionHasNoOddPrimeModulus := finite_torsion_row_no_odd_prime_modulus
  integerEqualitiesRemainZ := integer_equalities_exact
  integerDivisibilityRemainsZ := integer_divisibility_exact
  representationDimensionsRemainDimensions := representation_dimensions_exact
  diagnosticsRemainDiagnostics := diagnostic_ranks_exact

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
