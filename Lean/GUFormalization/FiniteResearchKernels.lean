import Mathlib

/-!
# Finite result-hardening kernels

This module formalizes three narrow deductions already listed in GU's Lean
verification queue:

* the real part of the declared chirality/projector trace vanishes under
  explicit finite complex-matrix Hermiticity, anticommutation, and zero-trace
  premises;
* section-independent vanishing of `m² d + sigma` modulo three is equivalent
  to `m = sigma = 0` in `ZMod 3`; and
* the reduced quartic family's coefficient comparison changes sign exactly at
  `lq = -l4 / 192`.

The module proves deductions from those premises. It does not establish that a
particular GU carrier, source action, physical state space, or vacuum realizes
them; it does not prove a physical chirality or generation-count verdict.
-/

open Matrix Complex

namespace GUFormalization.FiniteResearchKernels

section AchiralityTrace

variable {n : Type*} [Fintype n]

/-- If the supplied inverse Krein matrix `Kinv`, `chi`, and `H` are Hermitian
and `Kinv` anticommutes with `chi`, then the trace of `chi * Kinv * H` is
purely imaginary. In the owning application `C = K⁻¹ H`; identifying these
matrices with that physical carrier remains an external premise. -/
theorem trace_chirality_pure_imaginary
    (Kinv chi H : Matrix n n ℂ)
    (hKinv : Kinvᴴ = Kinv)
    (hchi : chiᴴ = chi)
    (hH : Hᴴ = H)
    (hanti : Kinv * chi = -(chi * Kinv)) :
    star ((chi * (Kinv * H)).trace) = -((chi * (Kinv * H)).trace) := by
  calc
    star ((chi * (Kinv * H)).trace) = (chi * (Kinv * H))ᴴ.trace := by
      rw [trace_conjTranspose]
    _ = (H * (Kinv * chi)).trace := by
      simp only [conjTranspose_mul, hchi, hKinv, hH, Matrix.mul_assoc]
    _ = -(H * (chi * Kinv)).trace := by rw [hanti]; simp
    _ = -(chi * (Kinv * H)).trace := by
      congr 1
      rw [trace_mul_comm H, Matrix.mul_assoc]

/-- Real-part form of `trace_chirality_pure_imaginary`. -/
theorem trace_chirality_real_zero
    (Kinv chi H : Matrix n n ℂ)
    (hKinv : Kinvᴴ = Kinv)
    (hchi : chiᴴ = chi)
    (hH : Hᴴ = H)
    (hanti : Kinv * chi = -(chi * Kinv)) :
    ((chi * (Kinv * H)).trace).re = 0 := by
  have hpure := trace_chirality_pure_imaginary Kinv chi H hKinv hchi hH hanti
  rw [Complex.star_def] at hpure
  have hre := congrArg Complex.re hpure
  simp only [conj_re, neg_re] at hre
  linarith

/-- For the declared `Pi_+ = (1+C)/2` trace readout, `tr chi = 0` and the
Hermitian/anticommutation premises force zero real part. This theorem is about
that matrix trace only; it does not identify every possible physical chirality
observable. -/
theorem projector_trace_real_zero
    (Kinv chi H : Matrix n n ℂ)
    (hKinv : Kinvᴴ = Kinv)
    (hchi : chiᴴ = chi)
    (hH : Hᴴ = H)
    (hanti : Kinv * chi = -(chi * Kinv))
    (htrace_chi : chi.trace = 0) :
    ((chi.trace + (chi * (Kinv * H)).trace) / 2).re = 0 := by
  simp [htrace_chi, trace_chirality_real_zero Kinv chi H hKinv hchi hH hanti]

end AchiralityTrace

namespace ModThree

/-- The residue expression `m² d + sigma` vanishes for every section residue
`d` exactly when both the coupling residue and offset residue vanish. -/
theorem section_independent_vanishes_iff (m sigma : ZMod 3) :
    (∀ d : ZMod 3, m ^ 2 * d + sigma = 0) ↔ m = 0 ∧ sigma = 0 := by
  constructor
  · intro h
    have hsigma : sigma = 0 := by simpa using h 0
    have hm2 : m ^ 2 = 0 := by simpa [hsigma] using h 1
    exact ⟨eq_zero_of_pow_eq_zero hm2, hsigma⟩
  · rintro ⟨rfl, rfl⟩
    simp

/-- A unit coupling residue cannot give section-independent vanishing. This is
the negative control for the `m² = 1 mod 3` case. -/
theorem unit_charge_not_section_independent (sigma : ZMod 3) :
    ¬ (∀ d : ZMod 3, (1 : ZMod 3) ^ 2 * d + sigma = 0) := by
  intro h
  have := (section_independent_vanishes_iff 1 sigma).mp h
  norm_num at this

end ModThree

namespace PhaseBoundary

/-- The aligned-side coefficient comparison is exactly `lq < -l4/192`. -/
theorem aligned_inequality {l0 lq l4 : ℚ} :
    l0 - lq > l0 + lq + l4 / 96 ↔ lq < -l4 / 192 := by
  constructor <;> intro h <;> linarith

/-- The two reduced branches meet exactly at `lq = -l4/192`. -/
theorem boundary_equality {l0 lq l4 : ℚ} :
    l0 - lq = l0 + lq + l4 / 96 ↔ lq = -l4 / 192 := by
  constructor <;> intro h <;> linarith

/-- The mirror-blind-side coefficient comparison is the opposite strict
inequality. -/
theorem mirror_blind_inequality {l0 lq l4 : ℚ} :
    l0 - lq < l0 + lq + l4 / 96 ↔ -l4 / 192 < lq := by
  constructor <;> intro h <;> linarith

end PhaseBoundary

end GUFormalization.FiniteResearchKernels
