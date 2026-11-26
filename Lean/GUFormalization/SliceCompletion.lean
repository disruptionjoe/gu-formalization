import Mathlib

/-!
Finite algebra core for the moving-cone slice-completion theorem.

These lemmas do not formalize analytic Cauchy existence, free-jet comparison,
continuity across the finite determinant-exceptional set, or source relevance.
The written theorem supplies those hypotheses and arguments. In particular,
`rightFactor_vanish` requires an actual right inverse; it does not assume that
an arbitrary characteristic value is nonexceptional.
-/

namespace GUFormalization.SliceCompletion

variable {K : Type*} [Field K]
variable {n m : Type*} [Fintype n] [Fintype m]
variable [DecidableEq n] [DecidableEq m]

theorem intertwiner_square
    (A : Matrix n n K) (B : Matrix m m K) (E : Matrix n m K)
    (h : A * E = E * B) :
    (A * A) * E = E * (B * B) := by
  calc
    (A * A) * E = A * (A * E) := Matrix.mul_assoc _ _ _
    _ = A * (E * B) := by rw [h]
    _ = (A * E) * B := (Matrix.mul_assoc _ _ _).symm
    _ = (E * B) * B := by rw [h]
    _ = E * (B * B) := Matrix.mul_assoc _ _ _

/-- The same relation after subtracting a common scalar shift. -/
theorem intertwiner_shift
    (A : Matrix n n K) (B : Matrix m m K) (E : Matrix n m K)
    (b : K) (h : A * E = E * B) :
    (A - b • 1) * E = E * (B - b • 1) := by
  simp only [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul,
    Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one]
  rw [h]

/-- Distinct scalar squares forbid a nonzero intertwiner. -/
theorem distinct_scalar_squares
    (A : Matrix n n K) (B : Matrix m m K) (E : Matrix n m K)
    (c d : K) (h : A * E = E * B)
    (hA : A * A = c • 1) (hB : B * B = d • 1)
    (hcd : c ≠ d) : E = 0 := by
  have heq : c • E = d • E := by
    have hs := intertwiner_square A B E h
    rw [hA, hB] at hs
    simpa using hs
  ext i j
  have hij := congrArg (fun M : Matrix n m K => M i j) heq
  change c * E i j = d * E i j at hij
  have hz : (c - d) * E i j = 0 := by
    rw [sub_mul, hij, sub_self]
  exact (mul_eq_zero.mp hz).resolve_left (sub_ne_zero.mpr hcd)

/-- Right multiplication by an invertible spectral factor detects zero. -/
theorem rightFactor_vanish
    (E : Matrix n m K) (Q R : Matrix m m K)
    (hEQ : E * Q = 0) (hQR : Q * R = 1) : E = 0 := by
  calc
    E = E * 1 := (Matrix.mul_one E).symm
    _ = E * (Q * R) := by rw [hQR]
    _ = (E * Q) * R := (Matrix.mul_assoc _ _ _).symm
    _ = 0 := by rw [hEQ, Matrix.zero_mul]

/-- The finite-rank spectral test used away from exceptional cone values. -/
theorem cone_factor_vanish
    (A : Matrix n n K) (B : Matrix m m K) (E : Matrix n m K)
    (c : K) (R : Matrix m m K)
    (h : A * E = E * B) (hA : A * A = c • 1)
    (hInv : (B * B - c • 1) * R = 1) : E = 0 := by
  apply rightFactor_vanish E (B * B - c • 1) R _ hInv
  have hs := intertwiner_square A B E h
  rw [hA] at hs
  have hc : E * (B * B) = c • E := by
    simpa using hs.symm
  simp only [Matrix.mul_sub, Matrix.mul_smul, Matrix.mul_one]
  rw [hc, sub_self]

end GUFormalization.SliceCompletion
