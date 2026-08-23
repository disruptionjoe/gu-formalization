import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Module

/-!
# Abstract involution and complementary-projector kernels

This module formalizes only the algebraic cores used by the repository's F/G
owner artifacts.  The first part treats conjugation by an involution inside an
associative ring and records the induced commutator parity.  The second part
constructs the two complementary projectors of a linear involution when `2`
is invertible.

The hypotheses do not identify a GU carrier, prove representation faithfulness,
establish Cartan positivity or a maximal-compact subgroup, select a physical
sector, construct dynamics, or prove a spectral/mass interpretation.
-/

namespace GUFormalization.InvolutionProjectorKernels

section InnerInvolution

variable {A : Type*} [Ring A]

/-- Conjugation by a chosen ring element. -/
def involutionConjugate (theta x : A) : A := theta * x * theta

/-- Conjugation by an involution is itself involutive. -/
theorem involutionConjugate_involutive
    (theta x : A) (htheta : theta * theta = 1) :
    involutionConjugate theta (involutionConjugate theta x) = x := by
  calc
    involutionConjugate theta (involutionConjugate theta x) =
        (theta * theta) * x * (theta * theta) := by
          simp only [involutionConjugate, mul_assoc]
    _ = x := by rw [htheta]; simp

/-- Conjugation by an involution preserves multiplication. -/
theorem involutionConjugate_mul
    (theta x y : A) (htheta : theta * theta = 1) :
    involutionConjugate theta (x * y) =
      involutionConjugate theta x * involutionConjugate theta y := by
  calc
    involutionConjugate theta (x * y) = theta * x * 1 * y * theta := by
      simp [involutionConjugate, mul_assoc]
    _ = theta * x * (theta * theta) * y * theta := by rw [htheta]
    _ = involutionConjugate theta x * involutionConjugate theta y := by
      simp only [involutionConjugate, mul_assoc]

/-- The associative-ring commutator. -/
def ringCommutator (x y : A) : A := x * y - y * x

/-- Conjugation by an involution preserves the associative commutator. -/
theorem involutionConjugate_commutator
    (theta x y : A) (htheta : theta * theta = 1) :
    involutionConjugate theta (ringCommutator x y) =
      ringCommutator (involutionConjugate theta x) (involutionConjugate theta y) := by
  rw [ringCommutator, ringCommutator]
  change theta * (x * y - y * x) * theta = _
  rw [mul_sub, sub_mul]
  change involutionConjugate theta (x * y) - involutionConjugate theta (y * x) = _
  rw [involutionConjugate_mul theta x y htheta]
  rw [involutionConjugate_mul theta y x htheta]

/-- The commutator of two even elements is even. -/
theorem commutator_even_even
    (theta x y : A) (htheta : theta * theta = 1)
    (hx : involutionConjugate theta x = x)
    (hy : involutionConjugate theta y = y) :
    involutionConjugate theta (ringCommutator x y) = ringCommutator x y := by
  rw [involutionConjugate_commutator theta x y htheta, hx, hy]

/-- The commutator of an even and an odd element is odd. -/
theorem commutator_even_odd
    (theta x y : A) (htheta : theta * theta = 1)
    (hx : involutionConjugate theta x = x)
    (hy : involutionConjugate theta y = -y) :
    involutionConjugate theta (ringCommutator x y) = -ringCommutator x y := by
  rw [involutionConjugate_commutator theta x y htheta, hx, hy]
  simp [ringCommutator, sub_eq_add_neg]
  apply add_comm

/-- The commutator of two odd elements is even. -/
theorem commutator_odd_odd
    (theta x y : A) (htheta : theta * theta = 1)
    (hx : involutionConjugate theta x = -x)
    (hy : involutionConjugate theta y = -y) :
    involutionConjugate theta (ringCommutator x y) = ringCommutator x y := by
  rw [involutionConjugate_commutator theta x y htheta, hx, hy]
  simp [ringCommutator]

end InnerInvolution

section ComplementaryProjectors

variable {R M : Type*} [Field R] [CharZero R] [AddCommGroup M] [Module R M]

/-- The `+1` projector associated with a linear involution. -/
def evenProjector (p : M →ₗ[R] M) : M →ₗ[R] M :=
  (2 : R)⁻¹ • (LinearMap.id + p)

/-- The `-1` projector associated with a linear involution. -/
def oddProjector (p : M →ₗ[R] M) : M →ₗ[R] M :=
  (2 : R)⁻¹ • (LinearMap.id - p)

/-- The two involution projectors sum to the identity. -/
theorem evenProjector_add_oddProjector (p : M →ₗ[R] M) :
    evenProjector p + oddProjector p = LinearMap.id := by
  ext x
  simp [evenProjector, oddProjector]
  module

/-- The even projector is fixed by the involution. -/
theorem involution_comp_evenProjector
    (p : M →ₗ[R] M) (hp : p.comp p = LinearMap.id) :
    p.comp (evenProjector p) = evenProjector p := by
  ext x
  have hpx : p (p x) = x := by
    simpa using LinearMap.congr_fun hp x
  simp [evenProjector, hpx]
  module

/-- The odd projector changes sign under the involution. -/
theorem involution_comp_oddProjector
    (p : M →ₗ[R] M) (hp : p.comp p = LinearMap.id) :
    p.comp (oddProjector p) = -oddProjector p := by
  ext x
  have hpx : p (p x) = x := by
    simpa using LinearMap.congr_fun hp x
  simp [oddProjector, hpx]
  module

/-- The even involution projector is idempotent. -/
theorem evenProjector_idempotent
    (p : M →ₗ[R] M) (hp : p.comp p = LinearMap.id) :
    (evenProjector p).comp (evenProjector p) = evenProjector p := by
  ext x
  have hpx : p (p x) = x := by
    simpa using LinearMap.congr_fun hp x
  simp [evenProjector, hpx]
  module

/-- The odd involution projector is idempotent. -/
theorem oddProjector_idempotent
    (p : M →ₗ[R] M) (hp : p.comp p = LinearMap.id) :
    (oddProjector p).comp (oddProjector p) = oddProjector p := by
  ext x
  have hpx : p (p x) = x := by
    simpa using LinearMap.congr_fun hp x
  simp [oddProjector, hpx]
  module

/-- The complementary involution projectors annihilate one another. -/
theorem evenProjector_comp_oddProjector
    (p : M →ₗ[R] M) (hp : p.comp p = LinearMap.id) :
    (evenProjector p).comp (oddProjector p) = 0 := by
  ext x
  have hpx : p (p x) = x := by
    simpa using LinearMap.congr_fun hp x
  simp [evenProjector, oddProjector, hpx]
  module

/-- The complementary involution projectors also annihilate in reverse order. -/
theorem oddProjector_comp_evenProjector
    (p : M →ₗ[R] M) (hp : p.comp p = LinearMap.id) :
    (oddProjector p).comp (evenProjector p) = 0 := by
  ext x
  have hpx : p (p x) = x := by
    simpa using LinearMap.congr_fun hp x
  simp [evenProjector, oddProjector, hpx]
  module

end ComplementaryProjectors

end GUFormalization.InvolutionProjectorKernels
