import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic

/-!
Finite exact-sequence additivity only. For a compatible Fredholm observation
complex, the six vector spaces below are its kernels and cokernels. Constructing
that analytic exact sequence, proving Fredholmness and physical grading, and
identifying a source index remain supplied obligations. No such realization is
asserted here. Exactness is supplied as range=kernel, not dimension arithmetic.
-/
namespace GUFormalization.ObservedHiddenSplit
open Module

variable {k E₀ E₁ E₂ F₀ F₁ F₂ : Type*} [Field k]
  [AddCommGroup E₀] [Module k E₀] [FiniteDimensional k E₀]
  [AddCommGroup E₁] [Module k E₁] [FiniteDimensional k E₁]
  [AddCommGroup E₂] [Module k E₂] [FiniteDimensional k E₂]
  [AddCommGroup F₀] [Module k F₀] [FiniteDimensional k F₀]
  [AddCommGroup F₁] [Module k F₁] [FiniteDimensional k F₁]
  [AddCommGroup F₂] [Module k F₂] [FiniteDimensional k F₂]

/-- The exact sequence 0→E₀→E₁→E₂→F₀→F₁→F₂→0 implies index additivity.
In the Fredholm application the subscripts are hidden,total,observed. -/
theorem six_exact_index_additivity
    (a : E₀ →ₗ[k] E₁) (b : E₁ →ₗ[k] E₂) (c : E₂ →ₗ[k] F₀)
    (d : F₀ →ₗ[k] F₁) (e : F₁ →ₗ[k] F₂)
    (ha : Function.Injective a) (he : Function.Surjective e)
    (hab : a.range = b.ker) (hbc : b.range = c.ker)
    (hcd : c.range = d.ker) (hde : d.range = e.ker) :
    (finrank k E₁ : Int) - finrank k F₁ =
      ((finrank k E₀ : Int) - finrank k F₀) +
      ((finrank k E₂ : Int) - finrank k F₂) := by
  have ra := LinearMap.finrank_range_of_inj ha
  have rb := b.finrank_range_add_finrank_ker
  have rc := c.finrank_range_add_finrank_ker
  have rd := d.finrank_range_add_finrank_ker
  have re := e.finrank_range_add_finrank_ker
  rw [← hab, ra] at rb
  rw [← hbc] at rc
  rw [← hcd] at rd
  rw [← hde, LinearMap.range_eq_top.mpr he, finrank_top] at re
  omega

/-- Balanced total in the same exact sequence implies observed=−hidden. -/
theorem balanced_total_observed_eq_neg_hidden
    (a : E₀ →ₗ[k] E₁) (b : E₁ →ₗ[k] E₂) (c : E₂ →ₗ[k] F₀)
    (d : F₀ →ₗ[k] F₁) (e : F₁ →ₗ[k] F₂)
    (ha : Function.Injective a) (he : Function.Surjective e)
    (hab : a.range = b.ker) (hbc : b.range = c.ker)
    (hcd : c.range = d.ker) (hde : d.range = e.ker)
    (total_zero : (finrank k E₁ : Int) - finrank k F₁ = 0) :
    (finrank k E₂ : Int) - finrank k F₂ =
      -((finrank k E₀ : Int) - finrank k F₀) := by
  have h := six_exact_index_additivity a b c d e ha he hab hbc hcd hde
  omega

end GUFormalization.ObservedHiddenSplit
