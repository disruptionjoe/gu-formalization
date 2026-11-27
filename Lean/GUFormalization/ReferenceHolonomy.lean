import Mathlib

/-! Finite arithmetic and inner-product cores only. The metric-bundle
connection, curvature formula, holonomy equivalence and spectral continuity
are written geometric arguments, not formalized by this module. -/
namespace GUFormalization.ReferenceHolonomy

/-- A nonzero real curvature eigenvalue forces a parallel bilinear form to
vanish on that eigenvector. Curvature compatibility supplies the equation. -/
theorem real_curvature_eigenvector_is_null (e q : ℝ) (he : e ≠ 0)
    (hskew : e * q + e * q = 0) : q = 0 := by
  have h : e * q = 0 := by linarith
  exact (mul_eq_zero.mp h).resolve_left he

/-- The preceding necessary condition contradicts a positive squared norm. -/
theorem no_positive_parallel_norm (e q : ℝ) (he : e ≠ 0)
    (hq : 0 < q) (hskew : e * q + e * q = 0) : False := by
  have h := real_curvature_eigenvector_is_null e q he hskew
  linarith

/-- A skew operator in a real positive inner-product space has no nonzero
real eigenvalue on a nonzero vector. The operator/domain must be supplied. -/
theorem positive_skew_no_real_eigenvector {V : Type*}
    [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    (v w : V) (e : ℝ) (he : e ≠ 0) (hv : v ≠ 0)
    (hw : w = e • v) (hskew : inner ℝ w v + inner ℝ v w = 0) : False := by
  rw [hw, inner_smul_left, inner_smul_right] at hskew
  have hp : 0 < inner ℝ v v := real_inner_self_pos.mpr hv
  exact no_positive_parallel_norm e (inner ℝ v v) he hp (by simpa using hskew)

/-- A small real-part perturbation cannot cross the imaginary axis. This
is the arithmetic margin, not a spectral-continuity theorem. -/
theorem half_margin_positive (e x : ℝ) (he : 0 < e)
    (hclose : |x - e| < e / 2) : 0 < x := by
  have h := (abs_lt.mp hclose).1
  linarith

end GUFormalization.ReferenceHolonomy
