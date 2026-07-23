import GUFormalization.LocatedNotForcedFiniteCore

set_option autoImplicit false

namespace GUFormalization.LocatedNotForcedFiniteCore

example : Fintype.card CoreItem = 7 :=
  core_item_count

example : Fintype.card ClassCGenerator = 15 :=
  finite_generator_count

example : BoundedClassCConclusion :=
  bounded_class_c_codomain_separated

example (row : FiniteTorsionRow) :
    IsTwoPrimaryModulus row.modulus :=
  bounded_class_c_codomain_separated.finiteTorsionTwoPrimary row

example (row : FiniteTorsionRow) (p : ℕ)
    (hp : Nat.Prime p) (hp_ne_two : p ≠ 2) :
    ¬ p ∣ row.modulus :=
  bounded_class_c_codomain_separated.finiteTorsionHasNoOddPrimeModulus
    row p hp hp_ne_two

example (row : IntegerEqualityRow) :
    row.lhs = row.rhs :=
  bounded_class_c_codomain_separated.integerEqualitiesRemainZ row

example (row : IntegerDivisibilityRow) (k : ℤ) :
    (4 : ℤ) ∣ row.indexFour k ∧
    (12 : ℤ) ∣ row.indexTwelve k ∧
    (24 : ℤ) ∣ row.indexTwentyFour k :=
  bounded_class_c_codomain_separated.integerDivisibilityRemainsZ row k

example (row : RepresentationDimensionRow) (exponent : ℕ) :
    row.dimension exponent = 2 ^ exponent :=
  bounded_class_c_codomain_separated.representationDimensionsRemainDimensions
    row exponent

example (row : DiagnosticRow) :
    row.positiveRank = 96 ∧
    row.negativeRank = 96 ∧
    row.positiveRank = row.negativeRank :=
  bounded_class_c_codomain_separated.diagnosticsRemainDiagnostics row

example (integerRow : IntegerEqualityRow) (torsionRow : FiniteTorsionRow) :
    CoreItem.integerEquality integerRow ≠ CoreItem.finiteTorsion torsionRow :=
  integer_equality_ne_finite_torsion integerRow torsionRow

example (integerRow : IntegerDivisibilityRow) (torsionRow : FiniteTorsionRow) :
    CoreItem.integerDivisibility integerRow ≠ CoreItem.finiteTorsion torsionRow :=
  integer_divisibility_ne_finite_torsion integerRow torsionRow

def zeroKramersFramedInput : MappedTorsionInput where
  source := .kramers
  sourceValue := 0
  toFramedClass := 0

example : crtTwoPrimaryProjection zeroKramersFramedInput = 0 := by
  rfl

example : crtThreePrimaryProjection zeroKramersFramedInput = 0 := by
  rfl

/--
error: Type mismatch
  IntegerEqualityRow.crossChiralityKrein
has type
  IntegerEqualityRow
but is expected to have type
  MappedTorsionInput
-/
#guard_msgs (error) in
example : MappedTorsionInput :=
  IntegerEqualityRow.crossChiralityKrein

/--
error: Type mismatch
  IntegerDivisibilityRow.adjointComposition
has type
  IntegerDivisibilityRow
but is expected to have type
  MappedTorsionInput
-/
#guard_msgs (error) in
example : MappedTorsionInput :=
  IntegerDivisibilityRow.adjointComposition

end GUFormalization.LocatedNotForcedFiniteCore
