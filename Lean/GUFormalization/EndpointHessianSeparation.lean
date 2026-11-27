import Mathlib

/-! The new finite inference only. Differentiability, compact tests, the
universal Shiab theorem and source attribution remain written premises. -/
namespace GUFormalization.EndpointHessianSeparation

/-- Comparing Hessians at two backgrounds removes the fixed differential
and mass terms. No assumption that the base background is zero is needed. -/
theorem affine_pairing_separation {K : Type*} [Field K]
    (A B C D r : K) (hr : r ≠ 0) (hbase : A = B)
    (hshift : A + r * C = B + r * D) : C = D := by
  rw [hbase] at hshift
  exact mul_left_cancel₀ hr (add_left_cancel hshift)

/-- The arithmetic end of the irreducible-domain rank argument. The
rank dichotomy and output bound must be supplied by the written proof. -/
theorem rank_gap_zero (r : ℕ) (bound : r ≤ 14)
    (irreducible_rank : r = 0 ∨ r = 91) : r = 0 := by
  omega

end GUFormalization.EndpointHessianSeparation
