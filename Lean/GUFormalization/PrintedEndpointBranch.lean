import Mathlib

/-! Finite algebra only: analytic IFT, homogeneous geometry and native operator
coefficients are separate written/reviewed premises. No full PDE formalization. -/
namespace GUFormalization.PrintedEndpointBranch

/-- The two ambient zero defects make the first three field coefficients equal.
The quadratic values are already evaluated at S; no source operator is inferred. -/
theorem first_three_coefficients {V : Type*} [AddCommGroup V] [Module ℚ V]
    (P K : V →ₗ[ℚ] V) (S Qp N : V)
    (h1 : P S = K S) (h2 : P (K S) + Qp = K (K S) + N) :
    (-S = -S) ∧ P S = K S ∧ -(P (P S) + Qp) = -(K (K S) + N) := by
  refine ⟨rfl, h1, ?_⟩
  rw [h1, h2]

/-- Multiplication by kappa=1/h shifts a field coefficient down one order. -/
theorem fourth_difference {V : Type*} [AddCommGroup V]
    (p q k n : V) : -(p+q) - (-(k+n)) = -((p-k)+(q-n)) := by abel

/-- On the printed zero locus, the actual Euler row is the negative defect. -/
theorem reverse_elimination {V : Type*} [AddCommGroup V]
    (m s p q k n : V) (hr : m+s+p+q=0) :
    m+s+k+n = -((p-k)+(q-n)) := by
  have hm : m+s = -(p+q) := by
    apply eq_neg_of_add_eq_zero_left
    simpa only [add_assoc] using hr
  rw [hm]
  abel

/-- Readouts may depend on fixed field/background jets; fix these at a witness.
Spacetime jets vanish only because the printed residual vanishes on a neighborhood. -/
theorem no_zero_preserving_recovery {A B : Type*} [Zero A] [Zero B]
    (R : A) (E : B) (hr : R=0) (he : E≠0) :
    ¬ ∃ F : A → B, F 0=0 ∧ E=F R := by
  rintro ⟨F,hF,hE⟩
  apply he
  rw [hE,hr,hF]

/-- Native full-form computation supplies the three rational entries. -/
theorem reverse_receiver :
    -(2*(3/8 : ℚ)*((21/4)*(4/3)+(21/4)*(2/3)+(15/4)*(16/3))) = -183/8 := by
  norm_num

/-- Analyticity supplies a bounded normalized remainder; this is its finite sign core. -/
theorem separated_leading_coefficient (a r h : ℝ) (ha : a≠0)
    (hh : h≠0) (hr : |r| < |a|) (n : ℕ) : h^n*(a+r) ≠ 0 := by
  apply mul_ne_zero (pow_ne_zero n hh)
  intro hz
  have hre : r = -a := by linarith
  rw [hre,abs_neg] at hr
  exact (lt_irrefl |a|) hr

end GUFormalization.PrintedEndpointBranch
