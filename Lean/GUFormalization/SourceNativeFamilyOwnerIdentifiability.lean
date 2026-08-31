import GUFormalization.SourceNativeAdjointCoupling

/-!
# Family and owner identifiability at the adjoint/144 interface

The supplied representation packet has two equivalent family copies and two
independent Pati--Salam-preserving quadratic owners, `54` and `210`.  This file
separates the two resulting identifiability questions.

Family-exchange invariance forces equal coefficients on the two copies, so an
invariant coefficient cannot select exactly one family.  The same symmetry
does not relate the `54` and `210` owner coordinates: explicit invariant
packets supported on only one owner remain distinct.

These are coefficient-identifiability boundaries.  They do not supply a
source action, family covector, owner coefficient, mass, observed sector, or
physical selector.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceNativeFamilyOwnerIdentifiability

open SourceNativeAdjointCoupling

/-- The two equivalent family copies in the held paired-family packet. -/
inductive FamilyCopy where
  | first
  | second
  deriving DecidableEq, Repr

open FamilyCopy

/-- Exchange the two equivalent family copies. -/
def familySwap : FamilyCopy → FamilyCopy
  | first => second
  | second => first

@[simp]
theorem familySwap_first : familySwap first = second := rfl

@[simp]
theorem familySwap_second : familySwap second = first := rfl

@[simp]
theorem familySwap_involutive (i : FamilyCopy) :
    familySwap (familySwap i) = i := by
  cases i <;> rfl

/-- Scalar coefficients attached to the two family copies. -/
abbrev FamilyCoefficients (R : Type*) := FamilyCopy → R

/-- Pull a coefficient packet across family exchange. -/
def swapCoefficients {R : Type*} (c : FamilyCoefficients R) :
    FamilyCoefficients R :=
  fun i => c (familySwap i)

/-- The coefficient packet respects equivalence of the two family copies. -/
def FamilySwapInvariant {R : Type*} (c : FamilyCoefficients R) : Prop :=
  swapCoefficients c = c

theorem familySwapInvariant_iff {R : Type*} (c : FamilyCoefficients R) :
    FamilySwapInvariant c ↔ c first = c second := by
  constructor
  · intro h
    have hfirst := congrFun h first
    simpa [swapCoefficients] using hfirst.symm
  · intro h
    funext i
    cases i with
    | first => simpa [swapCoefficients] using h.symm
    | second => simpa [swapCoefficients] using h

/-- Exactly-one-family support, stated without choosing which copy. -/
def SelectsExactlyOneFamily {R : Type*} [Zero R]
    (c : FamilyCoefficients R) : Prop :=
  (c first ≠ 0 ∧ c second = 0) ∨
    (c first = 0 ∧ c second ≠ 0)

/-- Family-exchange invariant coefficients cannot select exactly one of the
two equivalent copies. -/
theorem no_family_selection_from_swap_invariance
    {R : Type*} [Zero R] (c : FamilyCoefficients R)
    (hinvariant : FamilySwapInvariant c) :
    ¬ SelectsExactlyOneFamily c := by
  have heq := (familySwapInvariant_iff c).1 hinvariant
  intro hselect
  rcases hselect with hfirst | hsecond
  · exact hfirst.1 (heq.trans hfirst.2)
  · exact hsecond.2 (heq ▸ hsecond.1)

/-- Separate family-coefficient packets for the two surviving quadratic
owners.  Nothing in the representation support identifies these fields. -/
structure QuadraticOwnerCoefficients (R : Type*) where
  d54 : FamilyCoefficients R
  d210 : FamilyCoefficients R

/-- Family exchange acts independently inside each owner coordinate. -/
def QuadraticOwnerCoefficients.familySwap {R : Type*}
    (c : QuadraticOwnerCoefficients R) : QuadraticOwnerCoefficients R where
  d54 := swapCoefficients c.d54
  d210 := swapCoefficients c.d210

/-- Both owner coordinates respect exchange of the equivalent family copies. -/
def OwnerFamilySwapInvariant {R : Type*}
    (c : QuadraticOwnerCoefficients R) : Prop :=
  FamilySwapInvariant c.d54 ∧ FamilySwapInvariant c.d210

theorem ownerFamilySwapInvariant_iff {R : Type*}
    (c : QuadraticOwnerCoefficients R) :
    OwnerFamilySwapInvariant c ↔
      (c.d54 first = c.d54 second ∧
       c.d210 first = c.d210 second) := by
  simp only [OwnerFamilySwapInvariant, familySwapInvariant_iff]

/-- An invariant packet supported only on the `54` owner. -/
def owner54Only (R : Type*) [Zero R] [One R] :
    QuadraticOwnerCoefficients R where
  d54 := fun _ => 1
  d210 := fun _ => 0

/-- An invariant packet supported only on the `210` owner. -/
def owner210Only (R : Type*) [Zero R] [One R] :
    QuadraticOwnerCoefficients R where
  d54 := fun _ => 0
  d210 := fun _ => 1

theorem owner54Only_family_invariant
    (R : Type*) [Zero R] [One R] :
    OwnerFamilySwapInvariant (owner54Only R) := by
  constructor <;> apply (familySwapInvariant_iff _).2 <;> rfl

theorem owner210Only_family_invariant
    (R : Type*) [Zero R] [One R] :
    OwnerFamilySwapInvariant (owner210Only R) := by
  constructor <;> apply (familySwapInvariant_iff _).2 <;> rfl

/-- Family symmetry leaves the `54` and `210` owner coordinates independent:
two distinct invariant coefficient packets choose opposite owner axes. -/
theorem family_symmetry_does_not_select_quadratic_owner
    (R : Type*) [Zero R] [One R] (hone : (1 : R) ≠ 0) :
    OwnerFamilySwapInvariant (owner54Only R) ∧
      OwnerFamilySwapInvariant (owner210Only R) ∧
      owner54Only R ≠ owner210Only R := by
  refine ⟨owner54Only_family_invariant R, owner210Only_family_invariant R, ?_⟩
  intro h
  have hcoord := congrArg (fun c => c.d54 first) h
  have honezero : (1 : R) = 0 := by
    simpa [owner54Only, owner210Only] using hcoord
  exact hone honezero

/-- The representation theorem supplies exactly the two owner labels, while
the identifiability theorem shows that family symmetry supplies neither a
single-family selector nor a relation between the owner coordinates. -/
theorem representation_support_identifiability_boundary
    {R : Type*} [Zero R] [One R]
    (hone : (1 : R) ≠ 0)
    (c : FamilyCoefficients R) (hinvariant : FamilySwapInvariant c) :
    symmetricOwners = {Label.d54, Label.d210} ∧
      ¬ SelectsExactlyOneFamily c ∧
      owner54Only R ≠ owner210Only R := by
  exact ⟨symmetric_owners_exact,
    no_family_selection_from_swap_invariance c hinvariant,
    (family_symmetry_does_not_select_quadratic_owner R hone).2.2⟩

end SourceNativeFamilyOwnerIdentifiability
end GUFormalization
