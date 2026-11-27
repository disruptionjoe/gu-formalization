import Mathlib

/-! Abstract linear cores only. Clifford identities, adjoint conditions,
connection/jet identification, shape geometry, rank512 and source applicability
are written premises, not proved by this file. -/
namespace GUFormalization.UnitaryDualClosure

variable {𝕜 O S E : Type*} [Field 𝕜]
variable [AddCommGroup O] [Module 𝕜 O]
variable [AddCommGroup S] [Module 𝕜 S]
variable [AddCommGroup E] [Module 𝕜 E]

/-- Once a block factors through an insertion killed by the projection,
its projected block vanishes. The factorization is an explicit premise. -/
theorem projection_insertion_zero (P : E →ₗ[𝕜] E)
    (J : S →ₗ[𝕜] E) (C : O →ₗ[𝕜] S) (hPJ : P.comp J = 0) :
    P.comp (J.comp C) = 0 := by
  ext x
  have h := LinearMap.congr_fun hPJ (C x)
  simpa using h

/-- Zero-map part of invertible rank transport. No numerical rank or
geometric identification is supplied by this lemma. -/
theorem invertible_postcompose_zero_iff (U : E ≃ₗ[𝕜] E)
    (B : O →ₗ[𝕜] E) : U.toLinearMap.comp B = 0 ↔ B = 0 := by
  constructor
  · intro h
    ext x
    apply U.injective
    have hx := LinearMap.congr_fun h x
    simpa using hx
  · intro h
    rw [h]
    simp

end GUFormalization.UnitaryDualClosure
