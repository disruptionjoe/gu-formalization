import Mathlib

/-! Algebraic core for complete auxiliary elimination and formal constraint
consistency. The actual native matrices, their whole-root inverse certificates,
the differential operators/domains, and the analytic obstruction theorems are
separate reviewed inputs. In particular, a formal time jet is not a solution. -/
namespace GUFormalization.CompleteAuxiliaryGraph

variable {V N : Type*} [AddCommGroup V] [Module ℝ V]
  [AddCommGroup N] [Module ℝ N]

/-- The algebraic constraint selects exactly one auxiliary value. -/
theorem auxiliary_constraint_iff (M : N ≃ₗ[ℝ] N) (D : V →ₗ[ℝ] N)
    (v : V) (n : N) :
    D v + M n = 0 ↔ n = -M.symm (D v) := by
  constructor
  · intro h
    apply M.injective
    simpa using (eq_neg_of_add_eq_zero_right h)
  · intro h
    rw [h]
    simp

/-- Exact two-block equations are equivalent to an unrestricted graph and
the Schur reduced equation. This is not a PDE existence assertion. -/
theorem block_equations_iff (A : V ≃ₗ[ℝ] V) (M : N ≃ₗ[ℝ] N)
    (B : V →ₗ[ℝ] V) (E : N →ₗ[ℝ] V) (D : V →ₗ[ℝ] N)
    (v w : V) (n : N) :
    (A w + B v + E n = 0 ∧ D v + M n = 0) ↔
    (w = A.symm (E (M.symm (D v)) - B v) ∧ n = -M.symm (D v)) := by
  constructor
  · rintro ⟨h, hc⟩
    have hn := (auxiliary_constraint_iff M D v n).mp hc
    refine ⟨?_, hn⟩
    apply A.injective
    rw [hn, map_neg] at h
    simp only [LinearEquiv.apply_symm_apply]
    have hw : A w + B v = E (M.symm (D v)) := by
      apply sub_eq_zero.mp
      simpa [sub_eq_add_neg] using h
    exact eq_sub_of_add_eq hw
  · rintro ⟨hw, hn⟩
    refine ⟨?_, (auxiliary_constraint_iff M D v n).mpr hn⟩
    rw [hw, hn]
    simp

omit [AddCommGroup V] [Module ℝ V] in
/-- Every starting value has a unique formal recurrence. Convergence and
admissibility of any associated power series are deliberately not asserted. -/
theorem formal_recursion_unique (L : V → V) (v : ℕ → V)
    (h : ∀ j, v (j + 1) = L (v j)) :
    ∀ j, v j = (L^[j]) (v 0) := by
  intro j
  induction j with
  | zero => rfl
  | succ j ih => simp [h j, ih, Function.iterate_succ_apply']

/-- A commuting endomorphism preserves each supplied scalar eigenspace. -/
theorem commuting_preserves_eigenvector (S F : V →ₗ[ℝ] V) (a : ℝ)
    (h : S.comp F = F.comp S) (v : V) (hv : S v = a • v) :
    S (F v) = a • F v := by
  have he := LinearMap.congr_fun h v
  simpa [hv] using he

/-- Independent even/odd and base-inversion multiplicities cover all the
remaining coefficient directions; these are not particle counts. -/
theorem remaining_native_count :
    (183 + 211) + (196 + 196) +
    3 * ((512 + 480) + (496 + 496)) +
    5 * ((576 + 592) + (584 + 584)) + 7 * (490 + 462) = (25082 : ℕ) := by
  norm_num

/-- Reciprocity makes an auxiliary kernel direction annihilate a compatible
source. No inverse of M is assumed in this theorem. -/
theorem kernel_annihilates_compatible_source (M : N →ₗ[ℝ] N)
    (b : N →ₗ[ℝ] N →ₗ[ℝ] ℝ)
    (hs : ∀ x y, b (M x) y = b x (M y))
    (n k source : N) (hk : M k = 0) (hc : source + M n = 0) :
    b k source = 0 := by
  have hz : b k (M n) = 0 := by
    rw [← hs k n, hk]
    simp
  rw [eq_neg_of_add_eq_zero_left hc, map_neg, hz, neg_zero]

/-- The constrained quadratic energy does not depend on an auxiliary-kernel
addition. The native spatial Lagrangian and physical sign are supplied outside
Lean; no Q-restricted dynamical system is asserted. -/
theorem auxiliary_energy_kernel_independent (M : N →ₗ[ℝ] N)
    (b : N →ₗ[ℝ] N →ₗ[ℝ] ℝ)
    (hs : ∀ x y, b (M x) y = b x (M y))
    (n k : N) (hk : M k = 0) :
    b (n + k) (M (n + k)) = b n (M n) := by
  have hz : b k (M n) = 0 := by
    rw [← hs k n, hk]
    simp
  simp [map_add, hk, hz]

end GUFormalization.CompleteAuxiliaryGraph
