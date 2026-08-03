import Mathlib

/-!
# Compact-image obstruction algebraic kernel

This module formalizes only the narrow algebraic claims used by
`Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32)`:

* an involutory conjugation fixes an element exactly when the two commute;
* a commutator relation shifts an eigenvector by the stated weight;
* an explicit no-higher-weight hypothesis forces the raising map to vanish;
* the positive and negative block maps in the concrete specialization have
  mutually zero products, hence square to zero.

It does not formalize Haar averaging, compact closures, real reductive Lie
groups, quaternionic adjoints, or the complete manuscript.
-/

namespace GUFormalization.CompactImageObstructions

section InvolutoryConjugation

variable {R : Type*} [Ring R]

/-- If `z² = 1`, conjugation by `z` fixes `O` exactly when `z` and `O` commute. -/
theorem conjugation_fixed_iff_commutes (z O : R) (hz : z * z = 1) :
    z * O * z = O ↔ z * O = O * z := by
  constructor
  · intro hfixed
    calc
      z * O = (z * O) * 1 := by simp
      _ = (z * O) * (z * z) := by rw [hz]
      _ = (z * O * z) * z := by simp only [mul_assoc]
      _ = O * z := by rw [hfixed]
  · intro hcomm
    calc
      z * O * z = (O * z) * z := by rw [hcomm]
      _ = O * (z * z) := by simp only [mul_assoc]
      _ = O := by rw [hz]; simp

end InvolutoryConjugation

section WeightShift

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- The pointwise commutator relation `[Z,X]=αX` shifts a `λ`-eigenvector to
the `(λ+α)` eigenspace. -/
theorem shifted_eigenvector
    (Z X : V →ₗ[K] V) (w : V) (lam alpha : K)
    (hcomm : ∀ v, Z (X v) - X (Z v) = alpha • X v)
    (hw : Z w = lam • w) :
    Z (X w) = (lam + alpha) • X w := by
  calc
    Z (X w) = (Z (X w) - X (Z w)) + X (Z w) :=
      (sub_add_cancel (Z (X w)) (X (Z w))).symm
    _ = alpha • X w + X (Z w) := by rw [hcomm w]
    _ = alpha • X w + lam • X w := by rw [hw, X.map_smul]
    _ = (lam + alpha) • X w := by
      rw [add_smul]
      exact add_comm _ _

/-- If the shifted eigenspace contains only zero, the raising/lowering map
annihilates the original weight vector. -/
theorem extremal_annihilation
    (Z X : V →ₗ[K] V) (w : V) (lam alpha : K)
    (hcomm : ∀ v, Z (X v) - X (Z v) = alpha • X v)
    (hw : Z w = lam • w)
    (hno : ∀ v, Z v = (lam + alpha) • v → v = 0) :
    X w = 0 := by
  exact hno (X w) (shifted_eigenvector Z X w lam alpha hcomm hw)

end WeightShift

section SquareZeroBlocks

variable {R : Type*} [Ring R]

/-- Action of the positive block `[-B B; -B B]` on a two-block column. -/
def xPlus (B : R) (v : R × R) : R × R :=
  (-B * v.1 + B * v.2, -B * v.1 + B * v.2)

/-- Action of the negative block `[B B; -B -B]` on a two-block column. -/
def xMinus (B : R) (v : R × R) : R × R :=
  (B * v.1 + B * v.2, -B * v.1 - B * v.2)

/-- Any two positive blocks have zero product, over an arbitrary possibly
noncommutative ring. -/
theorem xPlus_comp_zero (B C : R) (v : R × R) :
    xPlus B (xPlus C v) = (0, 0) := by
  rcases v with ⟨u, v⟩
  apply Prod.ext <;> simp [xPlus]

/-- Any two negative blocks have zero product, over an arbitrary possibly
noncommutative ring. -/
theorem xMinus_comp_zero (B C : R) (v : R × R) :
    xMinus B (xMinus C v) = (0, 0) := by
  rcases v with ⟨u, v⟩
  apply Prod.ext <;> simp [xMinus] <;> noncomm_ring

theorem xPlus_square_zero (B : R) (v : R × R) :
    xPlus B (xPlus B v) = (0, 0) :=
  xPlus_comp_zero B B v

theorem xMinus_square_zero (B : R) (v : R × R) :
    xMinus B (xMinus B v) = (0, 0) :=
  xMinus_comp_zero B B v

end SquareZeroBlocks

end GUFormalization.CompactImageObstructions
