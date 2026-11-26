import Mathlib

/-! Finite algebraic core only. The written proof supplies the constant-rank
pencil, compatible connection, projector transport, and source interpretation.
No root-matrix inverse, evolution theorem, or physical quotient is formalized. -/
namespace GUFormalization.KappaOneConstraints

/-- A symmetric Hessian contracts an antisymmetric coefficient array to zero. -/
theorem symmetric_skew_contraction {ι : Type*} [Fintype ι]
    (h b : ι → ι → ℝ)
    (hs : ∀ i j, h i j = h j i)
    (hb : ∀ i j, b i j = -b j i) :
    (∑ i, ∑ j, h i j * b i j) = 0 := by
  have he : (∑ i, ∑ j, h i j * b i j) =
      -(∑ i, ∑ j, h i j * b i j) := by
    calc
      (∑ i, ∑ j, h i j * b i j) =
          ∑ j, ∑ i, h i j * b i j := Finset.sum_comm
      _ = ∑ i, ∑ j, -(h i j * b i j) := by
        apply Finset.sum_congr rfl
        intro i _
        apply Finset.sum_congr rfl
        intro j _
        rw [hs j i, hb j i]
        ring
      _ = -(∑ i, ∑ j, h i j * b i j) := by
        simp only [Finset.sum_neg_distrib]
  linarith

/-- Accounting of invariant blocks is not a particle multiplicity. -/
theorem imaginary_constraint_block_count :
    6146 + 7 * 6144 = 49154 := by norm_num

/-- A continuous real scalar constraint eigenvalue cannot change sign
along a regular path. Matrix invariance and endpoint certificates are supplied
by the exact native calculation, not this lemma. -/
theorem sign_change_forces_zero (f : ℝ → ℝ)
    (hf : ContinuousOn f (Set.Icc 0 1))
    (h0 : 0 < f 0) (h1 : f 1 < 0) :
    ∃ t ∈ Set.Icc (0 : ℝ) 1, f t = 0 := by
  have hm : (0 : ℝ) ∈ Set.Icc (f 1) (f 0) := by
    exact ⟨le_of_lt h1, le_of_lt h0⟩
  have hi := intermediate_value_Icc' (by norm_num : (0 : ℝ) ≤ 1) hf hm
  exact hi

end GUFormalization.KappaOneConstraints
