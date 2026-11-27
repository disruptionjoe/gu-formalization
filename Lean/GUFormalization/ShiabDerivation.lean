import Mathlib

/-! Two finite algebraic cores only. The full graded derivation classification,
Clifford/Spin decomposition, real-form transfer and Riemann-curvature vanishing
are written premises, not formalized here. -/
namespace GUFormalization.ShiabDerivation

/-- Coefficient commutators obey Leibniz. Exterior-degree signs and the
geometric identification of the coefficient algebra are separate inputs. -/
theorem commutator_leibniz {R : Type*} [Ring R] (t x y : R) :
    t * (x * y) - (x * y) * t =
      (t * x - x * t) * y + x * (t * y - y * t) := by
  noncomm_ring

/-- Pointwise scalar combinations preserve annihilation of a supplied input.
This does not assert that the scalar coefficient functions are parallel. -/
theorem two_channel_annihilation {V W : Type*}
    [AddCommGroup V] [Module ℂ V] [AddCommGroup W] [Module ℂ W]
    (A B : V →ₗ[ℂ] W) (v : V) (a b : ℂ)
    (hA : A v = 0) (hB : B v = 0) :
    (a • A + b • B) v = 0 := by
  simp [hA, hB]

end GUFormalization.ShiabDerivation
