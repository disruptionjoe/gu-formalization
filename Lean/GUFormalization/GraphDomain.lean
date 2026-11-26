import Mathlib

/-! Finite cores for the existing constraint-graph and charge-source test.
The native symbols, local domains, physical pairing and selected matter graph
are proved/checked separately. No full PDE or physical quotient is formalized. -/
namespace GUFormalization.GraphDomain

/-- Constraint differentiation kills the quadratic graph term. -/
theorem graph_kills_quadratic {R : Type*} [Ring R]
    (d u m : R) (h : d * u = 0) : d * (u * m * d) = 0 := by
  calc
    _ = (d * u) * m * d := by noncomm_ring
    _ = 0 := by rw [h]; simp

/-- The first derivative graph's factorization requirement is stronger than
merely having a square-zero top-degree symbol. -/
theorem factored_map_preserves_kernel {V W : Type*}
    [AddCommGroup V] [Module ℝ V] [AddCommGroup W] [Module ℝ W]
    (d : V →ₗ[ℝ] W) (c : V →ₗ[ℝ] V) (f : W →ₗ[ℝ] W)
    (h : d.comp c = f.comp d) (v : V) (hv : d v = 0) : d (c v) = 0 := by
  have he := LinearMap.congr_fun h v
  simpa [hv] using he

/-- A negative continuous-energy value cannot be approximated arbitrarily
closely by nonnegative values. Continuity/density transfer is external. -/
theorem negative_not_approximable_by_nonnegative (value : ℝ) (hn : value < 0)
    (h : ∀ ε : ℝ, 0 < ε → ∃ y : ℝ, 0 ≤ y ∧ |value - y| < ε) : False := by
  obtain ⟨y, hy, he⟩ := h (-value / 2) (by linarith)
  have hl := neg_le_abs (value - y)
  linarith

/-- The imaginary central vertex has the opposite sign to the phase current. -/
theorem central_vertex_phase_sign (z : ℂ) :
    (Complex.I * z).re = -((-Complex.I * z).re) := by
  simp

/-- A nonzero selected positive phase charge cannot have zero central source. -/
theorem positive_charge_nonzero_source (charge source : ℝ)
    (hq : 0 < charge) (hsource : source = -charge) : source ≠ 0 := by
  linarith

/-- A bosonic restriction with zero current in that sector cannot cancel it. -/
theorem real_sector_cannot_cancel_positive_charge (boson source charge : ℝ)
    (hb : boson = 0) (hq : 0 < charge) (hs : source = -charge)
    (heq : boson + source = 0) : False := by
  linarith

/-- The graph-packet limit has an affine tail that cannot obey a uniform bound. -/
theorem graph_tail_not_uniformly_bounded (z b bound : ℝ) (hb : 0 < b) :
    ∃ s : ℝ, 0 ≤ s ∧ bound < |z - s * b| := by
  refine ⟨(|z| + |bound| + 1) / b,
    le_of_lt (div_pos (by positivity) hb), ?_⟩
  rw [div_mul_cancel₀ _ (ne_of_gt hb)]
  have hz := le_abs_self z
  have hbound := le_abs_self bound
  have htail := neg_le_abs (z - (|z| + |bound| + 1))
  linarith

end GUFormalization.GraphDomain
