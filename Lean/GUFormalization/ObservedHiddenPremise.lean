import Std.Tactic

/-!
Conditional arithmetic only. The analytic exact-sequence/additivity premise,
zero total chiral index in a single grading, and observed-weak-grading bridge
are supplied assumptions. This file neither formalizes Fredholm analysis nor
claims that source non-chirality already supplies those assumptions.
The separate packet step 3 remains responsible for finite exact-sequence
index additivity, not just this corollary.
-/
namespace GUFormalization.ObservedHiddenPremise

theorem cancellation_from_same_grading
    (total hidden observed : Int)
    (compatible_additivity : total = hidden + observed)
    (source_nonchiral_index_premise : total = 0) :
    observed = -hidden := by omega

theorem descended_balance_forces_observed_zero
    (total hidden observed : Int)
    (compatible_additivity : total = hidden + observed)
    (total_balanced : total = 0)
    (hidden_balanced : hidden = 0) : observed = 0 := by omega

theorem nonzero_observed_requires_nonzero_hidden
    (total hidden observed : Int)
    (compatible_additivity : total = hidden + observed)
    (total_balanced : total = 0)
    (observed_nonzero : observed ≠ 0) : hidden ≠ 0 := by omega

-- The source-specific closed comparison supplies these coefficients;
-- their index-theoretic derivation is outside this arithmetic kernel.
theorem closed_comparison_balance_excludes_nonzero_observed
    (signature observed total : Int)
    (total_formula : total = -820 * signature)
    (observed_formula : observed = 368 * signature)
    (total_balanced : total = 0) : observed = 0 := by omega

end GUFormalization.ObservedHiddenPremise
