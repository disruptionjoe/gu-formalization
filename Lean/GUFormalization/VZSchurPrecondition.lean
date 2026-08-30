import Mathlib

/-!
# Determinant-free Schur kernel precondition

The theorem below isolates the stable linear-algebra deduction used by a Schur
elimination: the eliminated `E` block must have an explicit left inverse, and
the resulting Schur complement must be injective.  It does not identify the
blocks with GU's actual operator, prove the required inverse on a physical
cone, or close any Velo--Zwanziger gate.
-/

namespace GUFormalization.VZSchurPrecondition

section

variable {R X Y : Type*}
variable [Ring R]
variable [AddCommGroup X] [Module R X]
variable [AddCommGroup Y] [Module R Y]

/-- The Schur complement after eliminating the `Y` block with a supplied
candidate inverse. -/
def schurComplement
    (A : X →ₗ[R] X) (B : Y →ₗ[R] X) (C : X →ₗ[R] Y)
    (Einv : Y →ₗ[R] Y) : X →ₗ[R] X :=
  A - B.comp (Einv.comp C)

/-- Determinant-free block-kernel elimination.  A left inverse for `E` turns
the second block equation into `y = -E⁻¹Cx`; substituting that identity into
the first equation gives the Schur-complement kernel equation. -/
theorem blockKernelTrivial_of_leftInverse_and_schurInjective
    (A : X →ₗ[R] X) (B : Y →ₗ[R] X) (C : X →ₗ[R] Y)
    (E Einv : Y →ₗ[R] Y)
    (hleft : Einv.comp E = LinearMap.id)
    (hschur : Function.Injective (schurComplement A B C Einv))
    {x : X} {y : Y}
    (hfirst : A x + B y = 0)
    (hsecond : C x + E y = 0) :
    x = 0 ∧ y = 0 := by
  have hinvSecond := congrArg (fun z : Y => Einv z) hsecond
  have hy : y = -(Einv (C x)) := by
    have hleft_y : Einv (E y) = y := by
      simpa [LinearMap.comp_apply] using LinearMap.congr_fun hleft y
    have : Einv (C x) + y = 0 := by
      simpa [map_add, hleft_y] using hinvSecond
    rw [add_comm] at this
    exact eq_neg_of_add_eq_zero_left this
  have hkernel : schurComplement A B C Einv x = 0 := by
    rw [hy] at hfirst
    simpa [schurComplement, LinearMap.sub_apply,
      LinearMap.comp_apply, sub_eq_add_neg] using hfirst
  have hx : x = 0 := by
    apply hschur
    simpa using hkernel
  refine ⟨hx, ?_⟩
  simpa [hx] using hy

end

end GUFormalization.VZSchurPrecondition
