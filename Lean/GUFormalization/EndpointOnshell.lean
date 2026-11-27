import Mathlib

/-! Finite cores only. The native endpoint, full coupled stationarity,
observation map and root/branch certificates are established separately. -/
namespace GUFormalization.EndpointOnshell

/-- Eliminate the common mass and curvature source using the actual Euler
zero, without assuming that the printed endpoint is the variational derivative. -/
theorem on_shell_defect {V : Type*} [AddCommGroup V]
    (m s k n p w : V) (he : m + s + k + n = 0) :
    m + s + p + w = (p - k) + (w - n) := by
  have hs : m + s = -(k + n) := by
    apply eq_neg_of_add_eq_zero_left
    simpa only [add_assoc] using he
  rw [hs]
  abel

/-- A nonzero output at an exact equation-zero cannot be any zero-preserving
postprocessing of those equations. Differential-operator applicability needs
an actual solution on a neighborhood, not merely a zero at one point. -/
theorem no_zero_preserving_transfer {State Eqn Out : Type*} [Zero Eqn] [Zero Out]
    (E : State → Eqn) (R : State → Out) (x : State)
    (he : E x = 0) (hr : R x ≠ 0) :
    ¬ ∃ L : Eqn → Out, L 0 = 0 ∧ R x = L (E x) := by
  rintro ⟨L, hL, hR⟩
  apply hr
  rw [hR, he, hL]

/-- Exact scalar quadratic receiver expansion, the algebra behind center,
linear-radius and quadratic-radius error terms. -/
theorem quadratic_receiver_shift (c q x d : ℝ) :
    (c * (x+d) + q * (x+d)^2) - (c*x + q*x^2) =
    (c + 2*q*x)*d + q*d^2 := by ring

/-- A scalar witness remains nonzero after an injective (e.g. nondegenerate
metric raising) map. This does not justify pulling back a degree13 form. -/
theorem injective_raise_preserves_nonzero {V W : Type*} [Zero V] [Zero W]
    (f : V → W) (hf : Function.Injective f) (h0 : f 0 = 0)
    (v : V) (hv : v ≠ 0) : f v ≠ 0 := by
  intro h
  apply hv
  apply hf
  exact h.trans h0.symm

/-- A first-order output recovered from a third-order residual needs an
inverse-square coefficient cost. Native finite-jet bounds supply the premise. -/
theorem order_gap_cost (a C M h : ℝ) (hh : 0 < h) (hC : 0 < C)
    (bound : a*h ≤ M*C*h^3) : a/(C*h^2) ≤ M := by
  apply (div_le_iff₀ (mul_pos hC (pow_pos hh 2))).2
  have factor : (M*(C*h^2))*h = M*C*h^3 := by ring
  have ht : a*h ≤ (M*(C*h^2))*h := by
    rw [factor]
    exact bound
  exact (mul_le_mul_iff_left₀ hh).mp ht

end GUFormalization.EndpointOnshell
