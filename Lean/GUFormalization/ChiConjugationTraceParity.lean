import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# Finite trace parity under involutory conjugation

This module formalizes the finite algebraic core used by the repository's A2
native-ring symmetry result.  It proves only that ordinary power traces are
even and traces weighted by an anticommuting matrix are odd under conjugation
by an involution.

The hypotheses do not construct the repository's condensate carrier, identify
the matrices with GU-native operators, prove gauge invariance, or select a
physical orientation.  Those realization and interpretation premises remain
in the owning prose and executable artifacts.
-/

namespace GUFormalization.ChiConjugationTraceParity

open Matrix

variable {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]

/-- Conjugation by an involution commutes with taking a natural-number power. -/
theorem conjugation_pow (chi phi : Matrix n n R) (hchi : chi * chi = 1) (k : ℕ) :
    (chi * phi * chi) ^ k = chi * phi ^ k * chi := by
  induction k with
  | zero => simp [hchi]
  | succ k ih =>
      rw [pow_succ, ih]
      calc
        (chi * phi ^ k * chi) * (chi * phi * chi) =
            chi * phi ^ k * (chi * chi) * phi * chi := by
              simp only [Matrix.mul_assoc]
        _ = chi * phi ^ (k + 1) * chi := by
              rw [hchi]
              simp [pow_succ, Matrix.mul_assoc]

/-- The finite trace is unchanged by conjugation with an involution. -/
theorem trace_conjugation_even (chi x : Matrix n n R) (hchi : chi * chi = 1) :
    (chi * x * chi).trace = x.trace := by
  rw [trace_mul_comm (chi * x) chi]
  rw [← Matrix.mul_assoc, hchi, one_mul]

/-- Every ordinary power trace is even under involutory conjugation. -/
theorem trace_pow_conjugation_even
    (chi phi : Matrix n n R) (hchi : chi * chi = 1) (k : ℕ) :
    ((chi * phi * chi) ^ k).trace = (phi ^ k).trace := by
  rw [conjugation_pow chi phi hchi k]
  exact trace_conjugation_even chi (phi ^ k) hchi

omit [DecidableEq n] in
/-- A trace weighted by a matrix that is odd under the involution changes sign. -/
theorem weighted_trace_conjugation_odd
    (chi weight x : Matrix n n R)
    (hweight : chi * weight * chi = -weight) :
    (weight * (chi * x * chi)).trace = -(weight * x).trace := by
  calc
    (weight * (chi * x * chi)).trace = ((weight * chi * x) * chi).trace := by
      simp [Matrix.mul_assoc]
    _ = (chi * (weight * chi * x)).trace := by
      rw [trace_mul_comm (weight * chi * x) chi]
    _ = ((chi * weight * chi) * x).trace := by
      simp [Matrix.mul_assoc]
    _ = ((-weight) * x).trace := by rw [hweight]
    _ = -(weight * x).trace := by simp

/-- Every weighted power trace is odd under involutory conjugation when the
weight itself is odd. -/
theorem weighted_trace_pow_conjugation_odd
    (chi weight phi : Matrix n n R)
    (hchi : chi * chi = 1)
    (hweight : chi * weight * chi = -weight)
    (k : ℕ) :
    (weight * ((chi * phi * chi) ^ k)).trace =
      -(weight * (phi ^ k)).trace := by
  rw [conjugation_pow chi phi hchi k]
  exact weighted_trace_conjugation_odd chi weight (phi ^ k) hweight

end GUFormalization.ChiConjugationTraceParity
