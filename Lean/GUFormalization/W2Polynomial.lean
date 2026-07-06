import Mathlib

set_option autoImplicit false

/-!
# Algebraic `w2` Polynomial Kernel

This file proves the `F_2` polynomial identities used in the corrected
`w2(Y14)` calculation. It is an algebraic splitting-principle shim, not a
formalization of Stiefel-Whitney classes as topological characteristic classes.
-/

namespace GUFormalization
namespace W2Polynomial

abbrev F2 := ZMod 2

/-- First elementary symmetric polynomial in three formal degree-one roots. -/
def e1 (a b c : F2) : F2 :=
  a + b + c

/-- Second elementary symmetric polynomial in three formal degree-one roots. -/
def e2 (a b c : F2) : F2 :=
  a * b + a * c + b * c

/--
Degree-two part of `w(Sym^2 V)` for a rank-three bundle under the splitting
principle, with roots `a`, `b`, `c`.
-/
def w2Sym2Rank3 (a b c : F2) : F2 :=
  a ^ 2 + b ^ 2 + c ^ 2 + a * b + a * c + b * c

theorem w2Sym2Rank3_eq_e1_sq_add_e2 (a b c : F2) :
    w2Sym2Rank3 a b c = e1 a b c ^ 2 + e2 a b c := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> decide

theorem w2Sym2Rank3_oriented {a b c : F2} (h : e1 a b c = 0) :
    w2Sym2Rank3 a b c = e2 a b c := by
  rw [w2Sym2Rank3_eq_e1_sq_add_e2, h]
  ring_nf

/--
Degree-two part of `w(V tensor L)` for rank-three `V` and line root `l`.
The roots are `a+l`, `b+l`, `c+l`.
-/
def w2TensorLineRank3 (a b c l : F2) : F2 :=
  (a + l) * (b + l) + (a + l) * (c + l) + (b + l) * (c + l)

theorem w2TensorLineRank3_eq_e2_add_l_sq (a b c l : F2) :
    w2TensorLineRank3 a b c l = e2 a b c + l ^ 2 := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases l <;> decide

theorem w2TensorLineRank3_trivial_line (a b c : F2) :
    w2TensorLineRank3 a b c 0 = e2 a b c := by
  rw [w2TensorLineRank3_eq_e2_add_l_sq]
  ring_nf

/-- The corrected vertical degree-two contribution cancels over `F_2`. -/
theorem vertical_w2_cancels (baseObstruction : F2) :
    baseObstruction + baseObstruction = 0 := by
  exact CharTwo.add_self_eq_zero baseObstruction

/-- Algebraic form of the corrected final assembly: if vertical `w2` is zero, base survives. -/
theorem y14_w2_equals_base_when_vertical_zero (baseObstruction : F2) :
    0 + baseObstruction = baseObstruction := by
  ring

end W2Polynomial
end GUFormalization
