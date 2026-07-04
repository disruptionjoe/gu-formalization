import Mathlib

set_option autoImplicit false

/-!
# A1 — Located-not-forced theorem-grade legs (Lean skeleton)

**VERIFIED 2026-07-03.** Mathlib IS now provisioned (Lean 4.32.0-rc1 via elan, mathlib built) and
this `import Mathlib` file elaborates **exit 0 with no `sorry` and no `axiom`** (only benign linter
warnings) — confirmed by the internal-paths Lean run and independently re-verified in the main loop
(see `explorations/internal-paths-2026-07-03/lean-typecheck-core-theorems.md`). The theorem-grade legs
(Theorem 2 Krein index-nullity `chi_eq_zero`, the antilinear bound, and the 2-primary identities 3a–3f)
are genuinely machine-checked. The companion mathlib-free `A1-arith-core-check.lean` also compiles clean
(exit 0). (Supersedes the prior "UNVERIFIED — mathlib not provisioned" note.)

Style mirrors `Lean/GUFormalization/*.lean`: `import Mathlib`, `set_option autoImplicit
false`, `namespace GUFormalization`.

Scope boundary (as in the existing Lean layer): Lean checks finite kernels only. The
*physical* premises — that the actual 192-dim generation carrier's invariant Krein form is
purely cross-chirality with signature `(+96,-96)`, that the chirality eigenspaces are K-null,
that a physical subspace is maximal K-positive of dim 96 — are machine-checked in
`tests/generation-sector/` and `tests/antilinear-bound/`, and enter here only as
**hypotheses**. This file does not re-derive them and does not derive the generation count.
-/

namespace GUFormalization

/- ===================================================================== -/
/-  Leg 1 & Leg 2 — Krein index conservation and the antilinear bound     -/
/-  (both collapse to one finite-dimensional lemma: `chi_eq_zero`)        -/
/- ===================================================================== -/

namespace KreinIndex

variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- `P` is K-positive-definite: nonzero vectors have strictly positive K-norm.
    (Models a *physical* subspace; the form `K` is left as a bare pairing since the
    core lemma never needs bilinearity.) -/
def KPositive (K : V → V → ℝ) (P : Submodule ℝ V) : Prop :=
  ∀ v ∈ P, v ≠ 0 → 0 < K v v

/-- `W` is K-isotropic (Lagrangian / null): the K-norm vanishes on it.
    The chirality eigenspaces `W_+`, `W_-` are of this kind, and so — by the
    antilinear-nonkrein result — are the re-graded images `C(W_+)`, `C(W_-)` in `P_iso`. -/
def KIsotropic (K : V → V → ℝ) (W : Submodule ℝ V) : Prop :=
  ∀ w ∈ W, K w w = 0

/-- Net chiral index of a physical subspace relative to two eigenspaces. -/
noncomputable def chi (K : V → V → ℝ) (P Wp Wm : Submodule ℝ V) : ℤ :=
  (Module.finrank ℝ (P ⊓ Wp : Submodule ℝ V) : ℤ)
    - (Module.finrank ℝ (P ⊓ Wm : Submodule ℝ V) : ℤ)

/-- **Core lemma.** A K-positive-definite subspace meets a K-isotropic subspace only at `0`.
    This is the entire load-bearing content of Theorem 2 and the antilinear bound. -/
theorem positive_inter_isotropic_trivial
    (K : V → V → ℝ) (P W : Submodule ℝ V)
    (hP : KPositive K P) (hW : KIsotropic K W) :
    ∀ v, v ∈ P → v ∈ W → v = 0 := by
  intro v hvP hvW
  by_contra hv
  have h1 : 0 < K v v := hP v hvP hv
  have h2 : K v v = 0 := hW v hvW
  rw [h2] at h1
  exact lt_irrefl 0 h1

/-- The intersection of a K-positive and a K-isotropic subspace is trivial. -/
theorem inter_isotropic_eq_bot
    (K : V → V → ℝ) (P W : Submodule ℝ V)
    (hP : KPositive K P) (hW : KIsotropic K W) :
    P ⊓ W = ⊥ := by
  rw [eq_bot_iff]
  intro v hv
  have hz : v = 0 := positive_inter_isotropic_trivial K P W hP hW v hv.1 hv.2
  simp [Submodule.mem_bot, hz]

/-- **Theorem 2 (finite-dimensional core).** Net chiral index of any physical subspace,
    relative to two K-isotropic eigenspaces, is `0`. -/
theorem chi_eq_zero
    (K : V → V → ℝ) (P Wp Wm : Submodule ℝ V)
    (hP : KPositive K P) (hWp : KIsotropic K Wp) (hWm : KIsotropic K Wm) :
    chi K P Wp Wm = 0 := by
  unfold chi
  rw [inter_isotropic_eq_bot K P Wp hP hWp, inter_isotropic_eq_bot K P Wm hP hWm]
  simp

/-- **Leg 2 (antilinear null-eigenspace bound).** Identical corollary: for any physical `P`
    and any two K-isotropic images `CWp`, `CWm` (the re-graded chirality eigenspaces of an
    admissible antilinear `C ∈ P_iso`), the re-graded net chiral index is `0`. The proof
    uses only isotropy — never a full Krein / antiunitary condition — exactly as
    `canon/antilinear-nonkrein-admissibility-RESULTS.md` observes. -/
theorem antilinear_bound
    (K : V → V → ℝ) (P CWp CWm : Submodule ℝ V)
    (hP : KPositive K P) (hCWp : KIsotropic K CWp) (hCWm : KIsotropic K CWm) :
    chi K P CWp CWm = 0 :=
  chi_eq_zero K P CWp CWm hP hCWp hCWm

/-- **Boundary remark (the null condition is load-bearing).** A K-*negative-definite*
    subspace is NOT K-isotropic: it contains some `w ≠ 0` with `K w w < 0`, hence `≠ 0`.
    So the definite re-gradings fall outside the hypothesis of `chi_eq_zero` — matching the
    canon's point that a nonzero count requires abandoning chirality (a non-null re-grading),
    not merely Krein-compatibility. -/
theorem definite_not_isotropic
    (K : V → V → ℝ) (W : Submodule ℝ V)
    (w : V) (hwW : w ∈ W) (hneg : K w w < 0) :
    ¬ KIsotropic K W := by
  intro hIso
  have : K w w = 0 := hIso w hwW
  rw [this] at hneg
  exact lt_irrefl 0 hneg

end KreinIndex

/- ===================================================================== -/
/-  Leg 3 — 2-primary obstructions as power-of-two / mod-2^k identities   -/
/- ===================================================================== -/

namespace TwoPrimary

/-- 3a. Cross-chirality Krein signature: `96` is `2^5 · 3` (its *even* part is `2^5`). -/
theorem cross_chirality_ninety_six : (96 : ℤ) = 2 ^ 5 * 3 := by norm_num

/-- 3a. The `(+96, −96)` split is net zero (vectorlike; net chirality `0`). -/
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

/-- 3f. Ghost-parity `50/50`: a balanced physical sector has net count `0`. -/
theorem ghost_parity_net_zero (n : ℤ) : n - n = 0 := by ring

end TwoPrimary

end GUFormalization
