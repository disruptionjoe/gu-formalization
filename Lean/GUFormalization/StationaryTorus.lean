import Mathlib

/-! Finite cores only. The covariant-jet identity, global bundle sections,
stationary PDE, integration by parts, operator domain and inherited flat-PS
classification remain separate written/exact dependencies. These lemmas do
not assert existence or classification of a Yang--Mills connection. -/
namespace GUFormalization.StationaryTorus

/-- Scalar component version of the antisymmetric two-form norm count.
Summing over an orthonormal Lie basis and integrating are external steps. -/
theorem antisymmetric_norm_sum (a b c : ℝ) :
    (0 ^ 2 + a ^ 2 + b ^ 2) + ((-a) ^ 2 + 0 ^ 2 + c ^ 2) +
      ((-b) ^ 2 + (-c) ^ 2 + 0 ^ 2) = 2 * (a ^ 2 + b ^ 2 + c ^ 2) := by
  ring

/-- Two point-component readouts suffice once one curvature component is
nonzero. They imply independence of the corresponding global contractions. -/
theorem two_contraction_independence (x α β : ℝ) (hx : x ≠ 0)
    (hi : -β * x = 0) (hj : α * x = 0) : α = 0 ∧ β = 0 := by
  have ha : α = 0 := (mul_eq_zero.mp hj).resolve_right hx
  have hb' : β * x = 0 := by linarith
  have hb : β = 0 := (mul_eq_zero.mp hb').resolve_right hx
  exact ⟨ha, hb⟩

/-- Positivity excludes a nonzero vector equal to a gauge direction to
which it is orthogonal. Coulomb orthogonality itself is a written
integration-by-parts premise, not formalized here. -/
theorem orthogonal_equal_vector_zero {V : Type*} [NormedAddCommGroup V]
    [InnerProductSpace ℝ V] (v g : V) (heq : v = g)
    (horth : inner ℝ v g = 0) : v = 0 := by
  rw [← heq] at horth
  exact (inner_self_eq_zero).mp horth

/-- A nonpositive quadratic witness of positive norm forbids a strictly
positive lower spectral bound. The theorem applies to a zero Jacobi field
as well as to a negative-energy witness. -/
theorem no_positive_gap (massSq normSq energy : ℝ)
    (hm : 0 < massSq) (hn : 0 < normSq) (he : energy ≤ 0)
    (hgap : massSq * normSq ≤ energy) : False := by
  have hp : 0 < massSq * normSq := mul_pos hm hn
  linarith

end GUFormalization.StationaryTorus
