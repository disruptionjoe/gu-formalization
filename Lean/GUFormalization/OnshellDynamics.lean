import Mathlib

/-! Finite core of the on-shell dynamics calculation. The native identification
of the microlocal symbol, root certificates, eigenvalue/trace bridge and packet
estimate are separately reviewed mathematics, not formalized here. -/
namespace GUFormalization.OnshellDynamics

open scoped BigOperators

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The correction is LEFT multiplication by a shear, not similarity. -/
theorem left_shear_blocks (X A B C D : Matrix n n ℂ) :
    Matrix.fromBlocks (1 : Matrix n n ℂ) 0 X 1 * Matrix.fromBlocks A B C D =
      Matrix.fromBlocks A B (X * A + C) (X * B + D) := by
  simp [Matrix.fromBlocks_multiply]

omit [DecidableEq n] in
/-- An even left factor preserves an odd operator under reflection. -/
theorem reflection_left_factor
    (R S H : Matrix n n ℂ) (hs : R * S = S * R)
    (hh : R * H = -(H * R)) :
    R * (S * H) = -((S * H) * R) := by
  calc
    R * (S * H) = (R * S) * H := by rw [Matrix.mul_assoc]
    _ = (S * R) * H := by rw [hs]
    _ = S * (R * H) := by rw [Matrix.mul_assoc]
    _ = -((S * H) * R) := by rw [hh]; simp [Matrix.mul_assoc]

omit [DecidableEq n] in
/-- A trace-zero list with positive real square moment has a positive real
entry. Supplying this list as the spectrum is a separate theorem/input. -/
theorem positive_real_entry_of_moment (z : n → ℂ)
    (hz : ∑ i, (z i).re = 0)
    (hm : 0 < ∑ i, ((z i) ^ 2).re) :
    ∃ i, 0 < (z i).re := by
  by_contra hn
  push Not at hn
  have hall : ∀ i, (z i).re = 0 := by
    intro i
    have hsum : ∑ j, -(z j).re = 0 := by simpa using congrArg Neg.neg hz
    have hle : -(z i).re ≤ ∑ j, -(z j).re :=
      Finset.single_le_sum (fun j _ => neg_nonneg.mpr (hn j)) (Finset.mem_univ i)
    rw [hsum] at hle
    linarith [hn i]
  have hnonpos : ∑ i, ((z i) ^ 2).re ≤ 0 := by
    apply Finset.sum_nonpos
    intro i _
    simp only [pow_two, Complex.mul_re, hall, zero_mul, zero_sub]
    exact neg_nonpos.mpr (mul_self_nonneg _)
  linarith

/-- Scalar step in the dimension-20 moment bound. The lower bound follows
from trace zero and the upper bound on the other nineteen entries. -/
theorem scalar_moment_bound (a m : ℝ)
    (hlo : -19 * m ≤ a) (hhi : a ≤ m) :
    a ^ 2 ≤ -18 * m * a + 19 * m ^ 2 := by
  have h := mul_nonneg (sub_nonneg.mpr hhi) (show 0 ≤ a + 19 * m by linarith)
  nlinarith

/-- The certified threshold implies the stated conservative normalized rate,
provided the separately established dimension-20 spectral moment bound. -/
theorem certified_rate (m q : ℝ) (hm : 0 ≤ m)
    (hq : (19 / 80 : ℝ) < q) (hb : q ≤ 380 * m ^ 2) :
    (1 / 40 : ℝ) < m := by
  by_contra h
  have hmhi : m ≤ 1 / 40 := le_of_not_gt h
  have hp := mul_nonneg hm (sub_nonneg.mpr hmhi)
  nlinarith

end GUFormalization.OnshellDynamics
