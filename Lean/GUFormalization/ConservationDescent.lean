import Mathlib

/-! Finite cores only. Gaussian coordinates, local smooth ODE existence,
bundle extension, the source dictionary and free-jet realization are written
premises. No full Euler, global boundary or physical stress theorem is
formalized here. -/
namespace GUFormalization.ConservationDescent

/-- A nonzero normal coefficient can compensate an arbitrary tangential
divergence jet, independently of its sign. -/
theorem free_normal_jet_compensation (a r : ℝ) (ha : a ≠ 0) :
    r + a * (-r/a) = 0 := by
  field_simp <;> ring

/-- Surjective observation on the conservation-only solution class makes
any property of the observed field an off-shell property of every field. -/
theorem surjective_conservation_inference {Ambient Observed : Type*}
    (q : Ambient → Observed) (conserved : Ambient → Prop)
    (property : Observed → Prop)
    (lift : ∀ b, ∃ t, conserved t ∧ q t = b) :
    (∀ t, conserved t → property (q t)) ↔ ∀ b, property b := by
  constructor
  · intro h b
    rcases lift b with ⟨t, ht, hq⟩
    rw [← hq]
    exact h t ht
  · intro h t _
    exact h (q t)

/-- Independent first jets force every coefficient in the divergence
chain-rule row to vanish. Smooth field independence is a separate step. -/
theorem free_jet_coefficient_row (n : ℕ) (c : Fin n → ℝ)
    (h : ∀ p : Fin n → ℝ, ∑ i, c i * p i = 0) : ∀ i, c i = 0 := by
  intro i
  simpa [Pi.single_apply, mul_ite] using h (Pi.single i 1)

/-- Flat superpotential divergence vanishes when the two derivative
operators commute. Curved covariant derivatives are not assumed to commute. -/
theorem flat_superpotential_divergence {V : Type*}
    [AddCommGroup V] [Module ℝ V]
    (Dx Dy : V →ₗ[ℝ] V) (h : Dx.comp Dy = Dy.comp Dx) (f : V) :
    (Dx (Dy (Dy f)) - Dy (Dx (Dy f)),
      -Dx (Dx (Dy f)) + Dy (Dx (Dx f))) = (0, 0) := by
  have commute : ∀ v, Dx (Dy v) = Dy (Dx v) := by
    intro v
    have hv := congrArg (fun L : V →ₗ[ℝ] V => L v) h
    simpa using hv
  have second : Dx (Dx (Dy f)) = Dy (Dx (Dx f)) := by
    rw [commute f, commute (Dx f)]
  rw [commute (Dy f), second]
  simp

end GUFormalization.ConservationDescent
