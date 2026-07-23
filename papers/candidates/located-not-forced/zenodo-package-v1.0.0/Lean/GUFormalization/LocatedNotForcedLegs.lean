import Mathlib

set_option autoImplicit false

/-!
# Located-not-forced theorem-grade finite legs

The transversality leg is stated over a finite-dimensional complex vector space
with a nondegenerate Hermitian sesquilinear form. This is the program-native
indefinite/Krein construction, not a positive inner-product replacement.

The exact `192/96/96/96` dimensions are explicit in the carrier corollary and
remain hypotheses. The proof uses only positivity on one subspace and total
isotropy of the other two. The integer below is solely a difference of
intersection dimensions; projection ranks and operator constructions are not
part of this declaration.
-/

namespace GUFormalization

/- ===================================================================== -/
/-  Finite complex Krein transversality                                 -/
/- ===================================================================== -/

namespace KreinTransversality

variable {V : Type*} [AddCommGroup V] [Module ℂ V]

/-- A finite-dimensional Krein carrier uses a complex sesquilinear form,
conjugate-linear in the first argument and linear in the second, together with
Hermitian symmetry and nondegeneracy. Indefiniteness is witnessed in the
application by the supplied positive and totally isotropic subspaces. -/
structure FiniteKreinForm (V : Type*) [AddCommGroup V] [Module ℂ V] where
  form : V →ₗ⋆[ℂ] V →ₗ[ℂ] ℂ
  hermitian : form.IsSymm
  nondegenerate : form.Nondegenerate

/-- Strict positivity of the Hermitian quadratic value on a complex subspace. -/
def PositiveOn (K : FiniteKreinForm V) (P : Submodule ℂ V) : Prop :=
  ∀ v ∈ P, v ≠ 0 → 0 < (K.form v v).re

/-- The Hermitian form vanishes on every pair of vectors in the subspace. -/
def TotallyIsotropic (K : FiniteKreinForm V) (W : Submodule ℂ V) : Prop :=
  ∀ x ∈ W, ∀ y ∈ W, K.form x y = 0

/-- A complex-linear equivalence preserves the supplied Hermitian form. -/
def Isometry (K : FiniteKreinForm V) (U : V ≃ₗ[ℂ] V) : Prop :=
  ∀ x y, K.form (U x) (U y) = K.form x y

/-- Difference of the two complex intersection dimensions. This invariant is
independent of projection ranks and of any operator-theoretic construction. -/
noncomputable def intersectionDifference
    (P Wp Wm : Submodule ℂ V) : ℤ :=
  (Module.finrank ℂ (P ⊓ Wp : Submodule ℂ V) : ℤ)
    - (Module.finrank ℂ (P ⊓ Wm : Submodule ℂ V) : ℤ)

/-- A subspace on which the form is strictly positive is transverse to every
totally isotropic subspace. -/
theorem positive_inf_totallyIsotropic_eq_bot
    (K : FiniteKreinForm V) (P W : Submodule ℂ V)
    (hP : PositiveOn K P) (hW : TotallyIsotropic K W) :
    P ⊓ W = ⊥ := by
  rw [eq_bot_iff]
  intro v hv
  by_contra hv0
  have hpos : 0 < (K.form v v).re := hP v hv.1 hv0
  have hnull : K.form v v = 0 := hW v hv.2 v hv.2
  rw [hnull] at hpos
  exact lt_irrefl 0 hpos

/-- The finite transversality statement: both intersection dimensions vanish,
so their difference is zero. -/
theorem intersectionDifference_eq_zero
    [FiniteDimensional ℂ V]
    (K : FiniteKreinForm V) (P Wp Wm : Submodule ℂ V)
    (hP : PositiveOn K P)
    (hWp : TotallyIsotropic K Wp) (hWm : TotallyIsotropic K Wm) :
    intersectionDifference P Wp Wm = 0 := by
  unfold intersectionDifference
  rw [positive_inf_totallyIsotropic_eq_bot K P Wp hP hWp,
    positive_inf_totallyIsotropic_eq_bot K P Wm hP hWm]
  simp

/-- The manuscript carrier dimensions are recorded explicitly. The numerical
equalities do not strengthen the transversality proof, which is dimension
independent once finite dimensionality, positivity, and isotropy are supplied. -/
theorem carrier_intersectionDifference_eq_zero
    [FiniteDimensional ℂ V]
    (K : FiniteKreinForm V) (P Wp Wm : Submodule ℂ V)
    (_hVdim : Module.finrank ℂ V = 192)
    (_hPdim : Module.finrank ℂ P = 96)
    (_hWpdim : Module.finrank ℂ Wp = 96)
    (_hWmdim : Module.finrank ℂ Wm = 96)
    (hP : PositiveOn K P)
    (hWp : TotallyIsotropic K Wp) (hWm : TotallyIsotropic K Wm) :
    intersectionDifference P Wp Wm = 0 :=
  intersectionDifference_eq_zero K P Wp Wm hP hWp hWm

/-- A form isometry carries strict positivity to the mapped subspace. -/
theorem positiveOn_map
    (K : FiniteKreinForm V) (U : V ≃ₗ[ℂ] V) (P : Submodule ℂ V)
    (hU : Isometry K U) (hP : PositiveOn K P) :
    PositiveOn K (P.map U.toLinearMap) := by
  intro v hv hv0
  rcases hv with ⟨p, hp, rfl⟩
  have hp0 : p ≠ 0 := fun hp0 => hv0 (by simp [hp0])
  exact (congrArg Complex.re (hU p p)).symm ▸ hP p hp hp0

/-- A form isometry carries total isotropy to the mapped subspace. -/
theorem totallyIsotropic_map
    (K : FiniteKreinForm V) (U : V ≃ₗ[ℂ] V) (W : Submodule ℂ V)
    (hU : Isometry K U) (hW : TotallyIsotropic K W) :
    TotallyIsotropic K (W.map U.toLinearMap) := by
  intro x hx y hy
  rcases hx with ⟨x, hx, rfl⟩
  rcases hy with ⟨y, hy, rfl⟩
  exact (hU x y).trans (hW x hx y hy)

/-- A form isometry preserves the zero intersection difference after all three
subspaces are transported by the same complex-linear equivalence. -/
theorem intersectionDifference_map_eq_zero
    [FiniteDimensional ℂ V]
    (K : FiniteKreinForm V) (U : V ≃ₗ[ℂ] V) (P Wp Wm : Submodule ℂ V)
    (hU : Isometry K U) (hP : PositiveOn K P)
    (hWp : TotallyIsotropic K Wp) (hWm : TotallyIsotropic K Wm) :
    intersectionDifference
        (P.map U.toLinearMap) (Wp.map U.toLinearMap) (Wm.map U.toLinearMap) = 0 :=
  intersectionDifference_eq_zero K _ _ _
    (positiveOn_map K U P hU hP)
    (totallyIsotropic_map K U Wp hU hWp)
    (totallyIsotropic_map K U Wm hU hWm)

/-- A subspace containing a vector of strictly negative quadratic value is not
totally isotropic. -/
theorem negative_value_not_totallyIsotropic
    (K : FiniteKreinForm V) (W : Submodule ℂ V)
    (w : V) (hwW : w ∈ W) (hneg : (K.form w w).re < 0) :
    ¬ TotallyIsotropic K W := by
  intro hW
  have hnull : K.form w w = 0 := hW w hwW w hwW
  rw [hnull] at hneg
  exact lt_irrefl 0 hneg

end KreinTransversality

/- ===================================================================== -/
/-  Leg 3 — 2-primary obstructions as power-of-two / mod-2^k identities   -/
/- ===================================================================== -/

namespace TwoPrimary

/-- 3a. Cross-chirality Krein signature: `96` is `2^5 · 3` (its *even* part is `2^5`). -/
theorem cross_chirality_ninety_six : (96 : ℤ) = 2 ^ 5 * 3 := by norm_num

/-- 3a. The signed-dimension sum for the `(+96, −96)` split is zero. -/
theorem cross_chirality_net_zero : (96 : ℤ) + (-96) = 0 := by norm_num

/-- 3b. Spinor 2-smoothness: a spinor dimension `2^k` is never divisible by the odd prime
    `3`. (The rep-theory fact `dim = 2^k` is a hypothesis; this is its arithmetic core.) -/
theorem spinor_dim_not_div_three (k : ℕ) : ¬ (3 ∣ 2 ^ k) := by
  intro h
  have hp : Nat.Prime 3 := by norm_num
  have h2 : (3 : ℕ) ∣ 2 := hp.dvd_of_dvd_pow h
  norm_num at h2

/-- 3c. On a Rokhlin signature `σ = 16 k`, the RS bulk index `I_{3/2} = 21 σ / 8` equals
    `42 k` (exact integer division by `8`). -/
theorem rs_bulk_index_on_rokhlin (k : ℤ) : 21 * (16 * k) / 8 = 42 * k := by
  omega

/-- 3c. Hence the RS bulk index is even (2-primary) on every Rokhlin signature. -/
theorem rs_bulk_even (k : ℤ) : Even (21 * (16 * k) / 8) := by
  rw [rs_bulk_index_on_rokhlin]
  exact ⟨21 * k, by ring⟩

/-- 3d. Adjoint Dirac index `2 · T(adj) · k = 4k` is divisible by `4`. -/
theorem adjoint_index_div_four (k : ℤ) : (4 : ℤ) ∣ 4 * k :=
  ⟨k, rfl⟩

/-- 3e. Boundary-η lens numerator `2q² − 4q + 1` is odd for every integer charge `q`. -/
theorem lens_eta_numerator_odd (q : ℤ) : Odd (2 * q ^ 2 - 4 * q + 1) :=
  ⟨q ^ 2 - 2 * q, by ring⟩

/-- 3e. The lens-η denominator is `2^3` — 2-primary, so the residue stays in `(1/8)ℤ`. -/
theorem lens_eta_denominator_two_primary : (8 : ℤ) = 2 ^ 3 := by norm_num

/-- 3f. Kramers / mod-2 Witten index: a doubled count is `0 mod 2`. -/
theorem kramers_mod_two (n : ℤ) : (2 * n) % 2 = 0 := by omega

/-- 3f. Ghost-parity `50/50`: equal integer ranks have difference zero. -/
theorem ghost_parity_net_zero (n : ℤ) : n - n = 0 := by ring

end TwoPrimary

end GUFormalization
