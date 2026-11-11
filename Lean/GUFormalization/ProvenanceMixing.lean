import Mathlib

/-! Finite six-slot checks only. No Clifford, action, PDE, or physical family claim. -/
namespace GUFormalization.ProvenanceMixing

def evolve (x : Fin 6 → ℚ) (i : Fin 6) : ℚ :=
  let vp := (x 5 + 2*x 4 - x 2 - x 3) / 12
  if i = 0 then x 1 else if i = 1 then x 0+x 2+x 3+9*x 4-x 5+vp
  else if i = 2 then x 2-x 4+vp else if i = 3 then x 3-x 4+vp
  else if i = 4 then vp else x 2+x 3+10*x 4

def gamma (x : Fin 6 → ℚ) : ℚ := x 0 + x 1 + x 2 + x 3 + 10*x 4

def traceSeed (i : Fin 6) : ℚ := if i = 5 then 0 else 1/14
def remainderSeed (i : Fin 6) : ℚ := if i = 0 then 1 else if i = 4 then -1/10 else 0
def scalarSeed (i : Fin 6) : ℚ := if i = 5 then 1 else 0

theorem trace_seed_typed : gamma traceSeed = 1 := by norm_num [Fin.ext_iff, gamma, evolve, traceSeed, remainderSeed, scalarSeed]
theorem trace_to_scalar : evolve traceSeed 5 = 6/7 := by norm_num [Fin.ext_iff, gamma, evolve, traceSeed, remainderSeed, scalarSeed]
theorem trace_not_preserved : ¬ ∃ c : ℚ, evolve traceSeed = fun i => c * traceSeed i := by
  rintro ⟨c, h⟩
  have h5 := congrFun h 5
  have hs : traceSeed 5 = 0 := by norm_num [Fin.ext_iff, gamma, evolve, traceSeed, remainderSeed, scalarSeed]
  rw [trace_to_scalar, hs, mul_zero] at h5
  norm_num at h5

theorem remainder_seed_typed : gamma remainderSeed = 0 := by norm_num [Fin.ext_iff, gamma, evolve, traceSeed, remainderSeed, scalarSeed]
theorem remainder_to_trace : gamma (evolve remainderSeed) = 1/12 := by norm_num [Fin.ext_iff, gamma, evolve, traceSeed, remainderSeed, scalarSeed]
theorem remainder_not_preserved : gamma (evolve remainderSeed) ≠ 0 := by
  rw [remainder_to_trace]
  norm_num

theorem scalar_to_one_form : evolve scalarSeed 4 = 1/12 := by norm_num [Fin.ext_iff, gamma, evolve, traceSeed, remainderSeed, scalarSeed]

end GUFormalization.ProvenanceMixing
