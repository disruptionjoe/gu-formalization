import Mathlib

/-! Finite algebra and support-set core. Native Clifford/vertex identification,
all-polarization admission, and flat versus curved PDE scope are external
hypotheses checked in the accompanying report. -/
namespace GUFormalization.CoupledSupport

/-- The rational K95 null pair has positive center margin and a strictly
negative normal transfer norm. The geometric identification is external. -/
theorem native_pair_arithmetic :
    (5 : ℚ)^2 - 3^2 - 16^2 / 16 = 0 ∧
    (5 : ℚ)^2 - 16^2 / 16 = 9 ∧
    -(32 : ℚ)^2 / 16 = -64 ∧
    (5 : ℚ)^2 - 3^2 + 16^2 / 16 = 32 := by norm_num

/-- Longitudinal cancellation for a null pair is an algebraic Ward control;
it does not assert a physical gauge quotient. -/
theorem longitudinal_cancellation {V : Type*} [AddCommGroup V] [Module ℝ V]
    (p q : V) (d : ℝ) :
    d • (p - q) - d • p - (-d) • q = 0 := by module

/-- On the common transverse annihilator, the polarized current is a nonzero
scalar multiple of the Clifford image. Nonzero Clifford image is a premise. -/
theorem transverse_current_nonzero {V : Type*} [AddCommGroup V] [Module ℝ V]
    (a : V) (d : ℝ) (ha : a ≠ 0) (hd : d ≠ 0) : d • a ≠ 0 := by
  exact smul_ne_zero hd ha

/-- A source support containing all witnessed pairwise differences must
contain the entire difference set. The vertex witness is a separate input. -/
theorem closure_contains_differences {V : Type*} [AddGroup V]
    (S B : Set V) (h : ∀ x ∈ S, ∀ y ∈ S, x - y ∈ B) :
    {z | ∃ x ∈ S, ∃ y ∈ S, x - y = z} ⊆ B := by
  rintro z ⟨x, hx, y, hy, rfl⟩
  exact h x hx y hy

/-- Every open momentum patch has a neighborhood of zero among its
pairwise differences. It is not necessary to admit all momenta. -/
theorem ball_in_differences {V : Type*} [NormedAddCommGroup V]
    (S : Set V) (v : V) (r : ℝ) (hr : 0 < r)
    (hs : ∀ h : V, ‖h‖ < r → v + h ∈ S) :
    ∀ z : V, ‖z‖ < r → ∃ x ∈ S, ∃ y ∈ S, x - y = z := by
  intro z hz
  refine ⟨v + z, hs z hz, v, ?_, ?_⟩
  · simpa using hs 0 (by simpa using hr)
  · abel

/-- A nonempty open patch plus positive dilation closure has every vector
as a difference. This is a genuine all-frequency support statement; it does
not assert that a particular physical state class has these hypotheses. -/
theorem open_cone_differences_all {V : Type*} [NormedAddCommGroup V]
    [NormedSpace ℝ V] (S : Set V) (v : V) (r : ℝ) (hr : 0 < r)
    (hs : ∀ h : V, ‖h‖ < r → v + h ∈ S)
    (hc : ∀ t : ℝ, 0 < t → ∀ x ∈ S, t • x ∈ S) :
    ∀ z : V, ∃ x ∈ S, ∃ y ∈ S, x - y = z := by
  intro z
  let t : ℝ := ‖z‖ / r + 1
  have ht : 0 < t := by dsimp [t]; positivity
  have hv : v ∈ S := by simpa using hs 0 (by simpa using hr)
  have hsmall : ‖t⁻¹ • z‖ < r := by
    rw [norm_smul, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr ht)]
    rw [← div_eq_inv_mul, div_lt_iff₀ ht]
    dsimp [t]
    have he : r * (‖z‖ / r + 1) = ‖z‖ + r := by field_simp
    rw [he]
    linarith
  refine ⟨t • (v + t⁻¹ • z), hc t ht _ (hs _ hsmall),
    t • v, hc t ht _ hv, ?_⟩
  rw [smul_add, smul_smul, mul_inv_cancel₀ (ne_of_gt ht), one_smul]
  abel

/-- Once all differences occur, a universal same-support current closure
has no nontrivial forbidden transfer set. -/
theorem full_difference_forces_full_source {V : Type*} [AddGroup V]
    (S B : Set V)
    (hd : ∀ z : V, ∃ x ∈ S, ∃ y ∈ S, x - y = z)
    (hc : ∀ x ∈ S, ∀ y ∈ S, x - y ∈ B) : B = Set.univ := by
  apply Set.eq_univ_of_forall
  intro z
  obtain ⟨x, hx, y, hy, rfl⟩ := hd z
  exact hc x hx y hy

end GUFormalization.CoupledSupport
