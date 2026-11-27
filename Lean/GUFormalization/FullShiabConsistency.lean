import Mathlib

/-! Finite algebraic cores. Universal matrix-unit quasicentroid classification,
trace/form/Spin identifications, formal integration by parts, arbitrary jets
and the source dictionary remain separately reviewed written premises. -/
namespace GUFormalization.FullShiabConsistency

/-- Centerlessness supplies right-slot separation for the Lie bracket.
The cyclic relations and skew symmetry then force the three maps equal. -/
theorem three_cyclic_collapse {V : Type*} [AddCommGroup V]
    (br : V → V → V) (skew : ∀ x y, br x y = -br y x)
    (separates : ∀ u v, (∀ x, br x u = br x v) → u = v)
    (D E F : V → V)
    (h₁ : ∀ x y, br (D x) y = br x (E y))
    (h₂ : ∀ x y, br (E x) y = br x (F y))
    (h₃ : ∀ x y, br (F x) y = br x (D y)) :
    D = E ∧ E = F := by
  have swapped : ∀ x y, br (E x) y = br x (D y) := by
    intro x y
    calc
      br (E x) y = -br y (E x) := skew _ _
      _ = -br (D y) x := congrArg Neg.neg (h₁ y x).symm
      _ = br x (D y) := by rw [skew (D y) x]; simp
  have hDF : D = F := by
    funext y
    apply separates
    intro x
    exact (swapped x y).symm.trans (h₂ x y)
  have hED : E = D := by
    funext y
    apply separates
    intro x
    have h := h₃ x y
    rw [← hDF] at h
    exact (h₁ x y).symm.trans h
  exact ⟨hED.symm, hED.trans hDF⟩

theorem odd_scalar_parity_zero (c : ℂ) (h : c = -c) : c = 0 := by
  have hs : c+c = 0 := by
    nth_rewrite 1 [h]
    exact neg_add_cancel c
  have ht : (2:ℂ)*c = 0 := by
    calc
      2*c = c+c := by ring
      _ = 0 := hs
  exact (mul_eq_zero.mp ht).resolve_left (by norm_num)

/-- Matrix-unit trace tests give off-diagonal zero and equal diagonals.
This is the finite conclusion that the output is central. -/
theorem central_matrix_of_tests (n : ℕ) (M : Fin (n+1) → Fin (n+1) → ℂ)
    (hoff : ∀ i j, i ≠ j → M i j = 0)
    (hdiag : ∀ i, M i i = M 0 0) :
    ∀ i j, M i j = if i=j then M 0 0 else 0 := by
  intro i j
  by_cases h : i=j
  · subst j
    simp [hdiag i]
  · simp [h, hoff i j h]

/-- The one-half mixed action derivative cannot equal a unit endpoint
unless the mixed pairing vanishes. Integration supplies this premise. -/
theorem quadratic_mixed_pair_zero (x : ℝ) (h : x/2=x) : x=0 := by
  linarith

/-- Once the central and traceless input parts are both killed, their
linear span exhausts the input. The decomposition is an explicit premise. -/
theorem central_traceless_span_zero {V W : Type*}
    [AddCommGroup V] [Module ℂ V] [AddCommGroup W] [Module ℂ W]
    (S : V →ₗ[ℂ] W) (P Q : V → V)
    (decompose : ∀ x, P x + Q x = x)
    (hP : ∀ x, S (P x) = 0) (hQ : ∀ x, S (Q x) = 0) : S = 0 := by
  ext x
  change S x = 0
  rw [← decompose x, map_add, hP x, hQ x, add_zero]

end GUFormalization.FullShiabConsistency
