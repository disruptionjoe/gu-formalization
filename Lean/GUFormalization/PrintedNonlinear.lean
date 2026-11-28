import Mathlib

/-! Algebra cores only. Native Clifford identities, analytic branch closure,
and the frozen PDE/domain conclusions are separately reviewed written proofs. -/
namespace GUFormalization.PrintedNonlinear

theorem hook_mode {V : Type*} [AddCommGroup V] [Module ℝ V]
    (L : V →ₗ[ℝ] V) (b w : V) (k q : ℝ)
    (hb : L b = (-2 : ℝ) • w) (hw : L w = (-2*q) • b)
    (h : 4*q = k*k) :
    L (k • b + (2:ℝ) • w) = (-k) • (k • b + (2:ℝ) • w) := by
  rw [map_add, map_smul, map_smul, hb, hw]
  have hq : -4*q = -k*k := by nlinarith [h]
  calc
    k • ((-2:ℝ) • w) + (2:ℝ) • ((-2*q) • b) = (-4*q) • b + (-2*k) • w := by module
    _ = (-k) • (k • b + (2:ℝ) • w) := by rw [hq]; module

theorem self_interaction_free {V : Type*} [AddCommGroup V] [Module ℝ V]
    (L : V →ₗ[ℝ] V) (B : V → V → V) (v : V) (k : ℝ)
    (hL : L v = (-k) • v) (hB : B v v = 0) :
    k • v + L v + B v v = 0 := by
  rw [hL,hB]
  module

theorem cokernel_obstructs_correction {V : Type*} [AddCommGroup V] [Module ℝ V]
    (P : V →ₗ[ℝ] V) (ell : V →ₗ[ℝ] ℝ) (y : V)
    (hP : ∀ v, ell (P v) = 0) (hy : ell y ≠ 0) :
    ¬ ∃ v, P v + y = 0 := by
  rintro ⟨v,h⟩
  have he := congrArg ell h
  have hz : ell y = 0 := by simpa only [map_add, map_zero, hP, zero_add] using he
  exact hy hz

theorem hook_dispersion (k n lam : ℝ) (h : lam^2 = n^2-k^2/4) :
    4*(-lam^2+n^2)=k^2 := by nlinarith [h]

end GUFormalization.PrintedNonlinear
