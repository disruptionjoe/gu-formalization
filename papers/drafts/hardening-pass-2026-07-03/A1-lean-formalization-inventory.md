---
title: "A1 — Lean-formalization inventory for the theorem-grade legs (located-not-forced)"
status: draft
doc_type: hardening-inventory
created: 2026-07-03
staging_only: true
verified_in_lean: yes-core-spine
toolchain_available: yes
correction: "2026-07-22: mathlib is provisioned and Lean/GUFormalization/LocatedNotForcedLegs.lean typechecks in the pinned default target, exit 0 (no sorry/axiom), independently re-verified. The UNVERIFIED / 'mathlib not provisioned' statements below are SUPERSEDED — see explorations/internal-paths-2026-07-03/lean-typecheck-core-theorems.md. The former A1 draft duplicate has been retired. R4 is also integrated at Lean/GUFormalization/R4TwoArena.lean."
---

# A1 — Which theorem-grade legs are Lean-formalizable, and at what obligation cost

**Scope.** This inventory covers exactly the legs the hardening card names as
"theorem-grade": (i) **Theorem 2**, net chiral index conservation, as
finite-dimensional linear algebra over the cross-chirality Krein carrier; (ii) the
**antilinear null-eigenspace bound** (P_iso class); (iii) each **2-primary obstruction**
recast as a power-of-two / mod-2^k arithmetic identity. Sources:
`papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md`
(§4, §5, §6), `canon/antilinear-bound-RESULTS.md`,
`canon/antilinear-nonkrein-admissibility-RESULTS.md`,
`canon/rs-boundary-eta-2primary-RESULTS.md`, `canon/two-primary-lemma.md` (referenced).

**Toolchain status (updated 2026-07-22).** Elan, the pinned Lean
`v4.32.0-rc1` toolchain, and the committed mathlib revision are provisioned.
`Lean/GUFormalization/LocatedNotForcedLegs.lean` is the sole authoritative full
module and builds in the default target, exit 0.  The former unverified draft
duplicate was retired.  The 2026-07-03 lack-of-mathlib condition is historical.

**What WAS compiled (real, no mathlib).** A mathlib-free subset,
`A1-arith-core-check.lean`, reproducing the arithmetic legs that need only Lean core
(`omega`/`rfl`), was compiled with the installed `lean` — **exit 0, no errors, no `sorry`**.
Compiler-verified: `rs_bulk_index_on_rokhlin` (3c: `21*(16k)/8 = 42k`), `rs_bulk_even` (3c),
`adjoint_index_div_four` (3d: `4 ∣ 4k`), `kramers_mod_two` (3f: `(2n)%2=0`),
`ghost_parity_net_zero` (3f: `n−n=0`). These five identities are genuinely Lean-checked.
The Krein linear-algebra core (Legs 1–2) and the
`norm_num`/`Nat.Prime`/`Odd` legs (3a/3b/3e) are now verified in the authoritative
default-target module.  The smaller file remains useful as an independent core check.

An independent **Python arithmetic certificate**
(`A1-arithmetic-certificate.py`, in this same folder) re-checks the numeric content of
every 2-primary identity and the two rank facts behind Theorem 2 / the antilinear bound,
so the *numbers* carry an executable certificate even though the *Lean* does not.

---

## Leg 1 — Theorem 2: linear Krein index conservation

**Informal statement (paper §6).** On the 192-dim generation carrier the invariant Krein
form `K = eta_V (x) beta_S` is purely cross-chirality with signature `(+96, -96)`; the two
chirality eigenspaces `W_+`, `W_-` are K-null (Lagrangian). A *physical* subspace `P` is
maximal K-positive-definite (dim 96). Then `P ∩ W_+ = P ∩ W_- = {0}`, so the net chiral
index `chi(P) = dim(P ∩ W_+) − dim(P ∩ W_-) = 0`; a K-isometry maps physical subspaces to
physical subspaces, so `chi(UP) = 0` as well.

**Formalizable core (what actually needs Lean).** The load-bearing content is a single
finite-dimensional linear-algebra fact, *stripped of the physics*:

> A K-positive-definite subspace and a K-isotropic subspace intersect only at `0`.

Everything else (`chi = 0`) is `finrank ⊥ = 0` bookkeeping. No Hilbert space, no Fredholm
operator, no group connectedness.

**PROOF OBLIGATIONS.**
- *Definitions needed:* a real vector space `V`; a form `K : V → V → ℝ` (modeled as a bare
  pairing — we never need bilinearity for the core lemma); `KPositive K P` :=
  `∀ v ∈ P, v ≠ 0 → 0 < K v v`; `KIsotropic K W` := `∀ w ∈ W, K w w = 0`; `chi K P Wp Wm`
  := `(finrank (P ⊓ Wp) : ℤ) − (finrank (P ⊓ Wm) : ℤ)`.
- *Lemmas:* `positive_inter_isotropic_trivial` (v ∈ P ∩ W ⇒ v = 0, by the
  `0 < K v v` vs `K v v = 0` contradiction); `inter_isotropic_eq_bot` (`P ⊓ W = ⊥`).
- *Exact statement to formalize:* `chi_eq_zero : KPositive K P → KIsotropic K Wp →
  KIsotropic K Wm → chi K P Wp Wm = 0`.
- *Not attempted in Lean (honest scope line):* that `W_+`, `W_-` are *actually* K-null for
  the *actual* `eta_V (x) beta_S` on the 192-dim carrier (that is the machine-checked
  premise in `tests/generation-sector/net_chiral_index_invariant.py`, not a Lean fact);
  that a physical subspace is maximal-positive of dim 96; that a K-isometry preserves
  positivity. These are supplied as *hypotheses* to the Lean theorem, matching how the
  paper cites them (the linear-algebra core is theorem-grade; the premises are computed).

**Feasibility: HIGH.** The core is ~5 lines of elementary Lean; only `Submodule`,
`finrank`, and `Submodule.mem_bot` are needed from mathlib. Risk is purely
API-name drift (e.g. `Module.finrank` vs `FiniteDimensional.finrank`,
`Submodule.mem_bot`), resolvable at first compile.

---

## Leg 2 — Antilinear null-eigenspace bound (P_iso class)

**Informal statement (paper §6 corollary; `antilinear-nonkrein-admissibility-RESULTS.md`).**
The admissible antilinear class is `P_iso` = antilinear `C = M·conj` whose re-graded
chirality eigenspaces `C(W_+)`, `C(W_-)` are K-isotropic. Index nullity holds on **all** of
`P_iso` because the proof uses *only* isotropy of the two images, never the full Krein
condition `M† K M = λ K̄`. The load-bearing boundary is the *definite* re-gradings — which
are not chiralities (they grade physical-vs-ghost, carrying the vectorlike `±96`) and do
not act on the physical sector.

**Formalizable core.** Identical to Leg 1's core lemma, applied to the image submodules.
An antilinear map over ℂ is ℝ-linear, so `C(W_+)`, `C(W_-)` are genuine real submodules;
the bound is `chi_eq_zero` with `Wp := C(W_+)`, `Wm := C(W_-)`.

**PROOF OBLIGATIONS.**
- *Definitions needed:* none beyond Leg 1 (reuse `chi`, `KPositive`, `KIsotropic`). The
  antilinearity of `C` is *not* needed for the bound — only that its images are isotropic
  submodules — so it is captured by taking arbitrary submodules `CWp`, `CWm` with
  `KIsotropic` hypotheses. This is honest: it formalizes exactly the "proof only used
  isotropy" observation.
- *Exact statement to formalize:* `antilinear_bound : KPositive K P → KIsotropic K CWp →
  KIsotropic K CWm → chi K P CWp CWm = 0` (a one-line corollary of `chi_eq_zero`).
- *Companion remark (formalizable, low value):* a K-*negative-definite* subspace is not
  K-isotropic (there is a `w ≠ 0` with `K w w < 0 ≠ 0`), i.e. the definite re-gradings fall
  outside the hypothesis — this is the "null condition is load-bearing" boundary as a Lean
  statement.
- *Not attempted in Lean:* that any *specific* antilinear `C` on the real carrier has
  isotropic images (machine-certified in `tests/antilinear-bound/`), and the K-definite
  non-action on physical states (Gram-range computation). Supplied as hypotheses.

**Feasibility: HIGH.** Corollary of Leg 1; near-zero marginal cost. The genuinely
theorem-grade content and the antilinear-bound content collapse to *the same* Lean lemma,
which is itself the cleanest possible witness to the paper's claim that "the proof used
only isotropy."

---

## Leg 3 — 2-primary obstructions as power-of-two / mod-2^k identities

**Informal statement (paper §4, Theorem 1 enumeration; `rs-boundary-eta-2primary`).** Every
enumerated obstruction is even or a statement mod a power of two; none is an odd-prime
congruence. Each item is an arithmetic identity, individually Lean-formalizable. The *point
of each* is 2-primality — **not** that anything forces the count 3.

| # | Obstruction | Arithmetic content | Lean statement | Feasibility |
|---|---|---|---|---|
| 3a | Cross-chirality Krein signature | `96 = 2^5 · 3`; net `(+96)+(−96)=0` | `cross_chirality_ninety_six`, `cross_chirality_net_zero` | HIGH (`norm_num`) |
| 3b | Spinor 2-smoothness (§3 lemma, item 6) | `dim = 2^k` never divisible by 3: `¬ 3 ∣ 2^k` | `spinor_dim_not_div_three` | HIGH (prime-dvd-pow) |
| 3c | Rokhlin bulk RS index | `16 ∣ σ ⇒ I_{3/2}=21σ/8 = 42(σ/16)` even | `rs_bulk_index_on_rokhlin`, `rs_bulk_even` | MEDIUM (int division; `omega`) |
| 3d | Adjoint Dirac index | `2·T(adj)·k = 4k`, `4 ∣ 4k` | `adjoint_index_div_four` | HIGH (trivial `⟨k,rfl⟩`) |
| 3e | Boundary η lens type | `(2q²−4q+1)/8`: numerator odd, denom `8=2^3` | `lens_eta_numerator_odd`, `lens_eta_denominator_two_primary` | HIGH (`⟨q²−2q, ring⟩`) |
| 3f | Kramers / mod-2 Witten / ghost 50-50 | `Z/2` statements: `(2n) % 2 = 0`, `n − n = 0` | `kramers_mod_two`, `ghost_parity_net_zero` | HIGH (`omega`/`ring`) |

**PROOF OBLIGATIONS (per row).**
- 3a: `Int` literals only. `(96:ℤ) = 2^5*3` by `norm_num`; `96 + (-96) = 0` by `norm_num`.
  *No target import*: `96 = 2^5·3` merely factorizes a computed dimension to exhibit its
  even part; it does not, and must not, be read as forcing a factor-3 count.
- 3b: needs `Nat.Prime 3` (`by norm_num`) and `Nat.Prime.dvd_of_dvd_pow`: `3 ∣ 2^k ⇒ 3 ∣ 2`,
  contradiction by `norm_num`. This is the exact content of the §3 "spinor 2-smoothness"
  lemma restricted to the divisibility conclusion (the rep-theory that `dim = 2^k` is a
  hypothesis, not a Lean fact).
- 3c: `21*(16*k)/8 = 42*k` over `ℤ` by `omega` (exact division by the literal 8), then
  `Even (42*k)` via `⟨21*k, by ring⟩`. The `≡ 0 mod 3` remark in the canon is a *separate*
  divisibility (21 = 3·7); we formalize the load-bearing *evenness*, not the mod-3 factor.
- 3d: `(4:ℤ) ∣ 4*k` := `⟨k, rfl⟩`.
- 3e: `Odd (2*q^2 - 4*q + 1)` := `⟨q^2 - 2*q, by ring⟩`; `(8:ℤ)=2^3` by `norm_num`.
- 3f: `(2*n) % 2 = 0` by `omega`; `n - n = 0` by `ring`.

**Feasibility overall: HIGH** (3c MEDIUM only because integer division sometimes needs
`omega` coaxing). None of these requires mathlib beyond `Int`/`Nat` arithmetic and one
prime-divisibility lemma.

---

## What is NOT formalizable here (honest exclusions)

- **The physical premises** (that the *actual* 192-dim carrier form is purely
  cross-chirality signature `(96,96)`; that `dim ker(Γ) = 1664`; that the `su(2)_+` triplet
  is the `j=1` sector). These are numerical/representation facts, machine-checked in
  `tests/generation-sector/`, and enter the Lean theorems only as hypotheses. Formalizing
  them would require building the Clifford module in Lean — out of scope, and low value
  (the interesting content is the *conditional* theorem, not re-deriving the census).
- **The function-space / spectral-flow extension** (Theorem 2's conditional upgrade;
  `function-space-index-conservation-RESULTS.md`) — needs Fredholm operators, spectral
  flow, APS boundary terms; **not** finite-dimensional and **not** attempted.
- **Enumeration completeness of class C** (Theorem 1's "complete for C" clause) — a
  classification claim over an operator class, not a single identity; out of scope.
- **The order-3 → integer-3 bridge (§9)** — deliberately OPEN in canon; nothing here
  touches it, and nothing here derives three.

## Verdict

The **entire theorem-grade skeleton is Lean-formalizable at HIGH feasibility**, and Legs 1
and 2 collapse to a single 5-line finite-dimensional lemma (`chi_eq_zero`) that is the
cleanest possible witness to the paper's "the proof only used isotropy" claim. The 2-primary
identities are one-liners. **Verification is complete for this finite kernel:** the
authoritative `Lean/GUFormalization/LocatedNotForcedLegs.lean` module is part of the
pinned default target (2026-07-22, exit 0, no `sorry`/unreported axioms), while the
mathlib-free arithmetic subset remains an independent check. All numeric content is
additionally certified by `A1-arithmetic-certificate.py` (exit 0). The generation-count
verdict remains OPEN; nothing in this inventory derives three.
