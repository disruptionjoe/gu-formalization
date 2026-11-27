import Mathlib

/-! Finite algebraic cores. Native codifferential identification, homogeneous
geometry, source dictionary and exact root bounds are separately verified. -/
namespace GUFormalization.ThetaDivergence

/-- Symmetric metric contraction annihilates the self-commutator. No positive
metric or commutativity of the coefficient algebra is assumed. -/
theorem symmetric_commutator_contraction {ι A : Type*} [Fintype ι]
    [Ring A] [Module ℝ A] (g : ι → ι → ℝ) (T : ι → A)
    (hg : ∀ i j, g i j = g j i) :
    (∑ i, ∑ j, g i j • (T i * T j - T j * T i)) = 0 := by
  classical
  simp_rw [smul_sub, Finset.sum_sub_distrib]
  apply sub_eq_zero.mpr
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  rw [hg j i]

/-- Changing the affine connection cannot change its self-codifferential
when the contracted self-commutator vanishes. -/
theorem affine_connection_independence (d q s : ℝ) (hq : q = 0) :
    d - s*q = d := by simp [hq]

/-- A certified component enclosure separated from zero is a nonzero tensor
witness. The native root enclosure is a separate exact computation. -/
theorem separated_component (x c e : ℝ)
    (bound : |x-c| ≤ e) (separated : e < |c|) : x ≠ 0 := by
  intro hx
  subst x
  simp only [zero_sub, abs_neg] at bound
  linarith

/-- If all non-mass homogeneous Euler terms lie in the coderivative kernel,
nonzero mass coefficient forces stationary conservation. -/
theorem stationary_kernel (k d s : ℝ) (hk : k ≠ 0)
    (hs : s = 0) (euler : k*d+s=0) : d=0 := by
  rw [hs, add_zero] at euler
  exact (mul_eq_zero.mp euler).resolve_left hk

/-- A separated leading coefficient remains nonzero when the remainder is
smaller by the same nonzero power. Analyticity supplies this bound separately. -/
theorem leading_power_nonzero (x a h e : ℝ) (n : ℕ)
    (hh : h ≠ 0) (he : e < |a|)
    (bound : |x-a*h^n| ≤ e*|h|^n) : x ≠ 0 := by
  intro hx
  subst x
  have hp : 0 < |h|^n := pow_pos (abs_pos.mpr hh) n
  simp only [zero_sub, abs_neg, abs_mul, abs_pow] at bound
  exact (not_le_of_gt (mul_lt_mul_of_pos_right he hp)) bound

end GUFormalization.ThetaDivergence
