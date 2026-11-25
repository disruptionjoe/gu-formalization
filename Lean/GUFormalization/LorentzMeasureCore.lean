import Mathlib

/-! Exact algebraic core of the invariant-probability support result.
This checks actual rational Lorentz boosts on symmetric 4×4 real matrices.
Compactness of probability-preserving actions, integration, and weak convergence
are written/reviewed inputs, not formalized by this module. -/
noncomputable section
namespace GUFormalization.LorentzMeasureCore

abbrev M4 := Matrix (Fin 4) (Fin 4) ℝ

def lorentz : M4 := !![-1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1]
def boost1 : M4 := !![5/4, 3/4, 0, 0; 3/4, 5/4, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1]
def boost2 : M4 := !![5/4, 0, 3/4, 0; 0, 1, 0, 0; 3/4, 0, 5/4, 0; 0, 0, 0, 1]
def boost3 : M4 := !![5/4, 0, 0, 3/4; 0, 1, 0, 0; 0, 0, 1, 0; 3/4, 0, 0, 5/4]
def symmetric (a b c d e f k h i j : ℝ) : M4 :=
  !![a,b,c,d; b,e,f,k; c,f,h,i; d,k,i,j]

/-- The displayed maps genuinely preserve the Lorentz form. -/
theorem boosts_preserve_lorentz :
    boost1.transpose * lorentz * boost1 = lorentz ∧
    boost2.transpose * lorentz * boost2 = lorentz ∧
    boost3.transpose * lorentz * boost3 = lorentz := by
  refine ⟨?_, ?_, ?_⟩ <;> ext r s <;> fin_cases r <;> fin_cases s <;>
    norm_num [boost1, boost2, boost3, lorentz, Matrix.mul_apply,
      Fin.sum_univ_succ, Matrix.transpose_apply]

/-- Simultaneous fixed symmetric forms are exactly multiples of g.
Using inverse congruence gives the same fixed equations since the boosts are
invertible. No measure-theoretic conclusion is asserted without its premises. -/
theorem three_boost_fixed_is_conformal (a b c d e f k h i j : ℝ)
    (h1 : boost1.transpose * symmetric a b c d e f k h i j * boost1 =
      symmetric a b c d e f k h i j)
    (h2 : boost2.transpose * symmetric a b c d e f k h i j * boost2 =
      symmetric a b c d e f k h i j)
    (h3 : boost3.transpose * symmetric a b c d e f k h i j * boost3 =
      symmetric a b c d e f k h i j) :
    symmetric a b c d e f k h i j = (-a) • lorentz := by
  have h100 := congrArg (fun m : M4 => m 0 0) h1
  have h101 := congrArg (fun m : M4 => m 0 1) h1
  have h102 := congrArg (fun m : M4 => m 0 2) h1
  have h112 := congrArg (fun m : M4 => m 1 2) h1
  have h103 := congrArg (fun m : M4 => m 0 3) h1
  have h113 := congrArg (fun m : M4 => m 1 3) h1
  have h200 := congrArg (fun m : M4 => m 0 0) h2
  have h203 := congrArg (fun m : M4 => m 0 3) h2
  have h300 := congrArg (fun m : M4 => m 0 0) h3
  simp [boost1, boost2, boost3, symmetric, Matrix.mul_apply,
    Fin.sum_univ_succ, Matrix.transpose_apply] at h100 h101 h102 h112 h103 h113 h200 h203 h300
  have hb : b = 0 := by linarith
  have he : e = -a := by linarith
  have hc : c = 0 := by linarith
  have hf : f = 0 := by linarith
  have hd : d = 0 := by linarith
  have hk : k = 0 := by linarith
  have hh : h = -a := by linarith
  have hi : i = 0 := by linarith
  have hj : j = -a := by linarith
  subst b; subst e; subst c; subst f; subst d; subst k; subst h; subst i; subst j
  ext r s
  fin_cases r <;> fin_cases s <;> simp [symmetric, lorentz]

end GUFormalization.LorentzMeasureCore
