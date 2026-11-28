import Mathlib

/-! Finite cokernel and resonance algebra. Native Clifford/projector data,
C² graph differentiability and PDE solutions are separate written proofs. -/
namespace GUFormalization.PrintedStateCompletion

theorem left_kernel_excludes_completion {K V : Type*} [Field K]
    [AddCommGroup V] [Module K V] (L : V →ₗ[K] V)
    (ell : V →ₗ[K] K) (f : V)
    (hL : ∀ v, ell (L v) = 0) (hf : ell f ≠ 0) :
    ¬ ∃ v, L v = -f := by
  rintro ⟨v,h⟩
  have hv := congrArg ell h
  rw [hL, map_neg] at hv
  exact hf (neg_eq_zero.mp hv.symm)

theorem nonlinear_base_cannot_remove_external_receiver {K V : Type*}
    [Field K] [AddCommGroup V] [Module K V]
    (L : V →ₗ[K] V) (ell : V →ₗ[K] K) (f b : V)
    (hL : ∀ v, ell (L v) = 0) (hb : ell b = 0) (hf : ell f ≠ 0) :
    ¬ ∃ v, L v + f + b = 0 := by
  rintro ⟨v,h⟩
  have he := congrArg ell h
  have hz : ell f = 0 := by
    simpa only [map_add,map_zero,hL,hb,zero_add,add_zero] using he
  exact hf hz

theorem scaled_receiver_nonzero (k : ℝ) (hk : k ≠ 0) :
    (2176/3 : ℝ)*k^2 ≠ 0 := by
  exact mul_ne_zero (by norm_num) (pow_ne_zero 2 hk)

theorem rational_receiver_scale : (104448 : ℚ)/12^2 = 2176/3 := by norm_num

end GUFormalization.PrintedStateCompletion
