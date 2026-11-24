import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic

/-!
Finite-dimensional core only. The written symbol proof supplies kernel
containment and dimensions. This file does not formalize Spin invariant theory,
the source operator, physical modes, or an analytic observation domain.
-/
namespace GUFormalization.SourceClassCore
open Module

variable {k E F : Type*} [Field k]
  [AddCommGroup E] [Module k E] [FiniteDimensional k E]
  [AddCommGroup F] [Module k F]

/-- A map retaining the required information has rank at least its target
codimension, once the symbol argument supplies the kernel containment. -/
theorem rank_bound_from_kernel
    (f : E →ₗ[k] F) (K : Submodule k E) (d : Nat)
    (hker : f.ker ≤ K)
    (hdim : finrank k E = finrank k K + d) :
    d ≤ finrank k f.range := by
  have hle := Submodule.finrank_mono hker
  have hr := f.finrank_range_add_finrank_ker
  omega

/-- With 15 spinor slots and a hidden 9-slot kernel, at least six slots
remain. Dimensions and kernel inclusion are explicit supplied hypotheses. -/
theorem six_spinor_minimum
    (f : E →ₗ[k] F) (K : Submodule k E) (s : Nat)
    (hker : f.ker ≤ K)
    (hE : finrank k E = 15 * s) (hK : finrank k K = 9 * s) :
    6 * s ≤ finrank k f.range := by
  apply rank_bound_from_kernel f K (6 * s) hker
  omega

/-- Nonzero spinor size rules out a five-slot output under the same
explicit containment/dimension premises. -/
theorem not_five_spinor_rank
    (f : E →ₗ[k] F) (K : Submodule k E) (s : Nat) (hs : 0 < s)
    (hker : f.ker ≤ K)
    (hE : finrank k E = 15 * s) (hK : finrank k K = 9 * s) :
    ¬ finrank k f.range ≤ 5 * s := by
  have h := six_spinor_minimum f K s hker hE hK
  omega

theorem full_dirac_minimum : 6 * 128 = (768 : Nat) := by norm_num

end GUFormalization.SourceClassCore
