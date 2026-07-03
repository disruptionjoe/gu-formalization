---
title: "Internal path #3 — actually Lean-typecheck the core-theorem spine (honest env probe + real build results)"
status: exploration
doc_type: verification-log
created: 2026-07-03
staging_only: true
promote: false
scope: "Records ACTUAL command outputs from a real Lean/mathlib run on this machine. Corrects the A1 inventory's stale 'mathlib not provisioned' claim. No canon/paper edits."
---

# Lean typecheck of the core-theorem spine — real run, 2026-07-03

**Bottom line.** The environment is BETTER than the A1 inventory reported: a Lean toolchain
AND a fully-built mathlib are now provisioned in the repo. Against them, the **located-not-forced
core spine typechecks CLEAN** (Theorem 2 Krein index-nullity, the antilinear bound, and all
2-primary identities). The mathlib-free arithmetic subset also typechecks clean. The R4 two-arena
big-swing file does **NOT** typecheck — it fails on mathlib-master API drift (bounded, fixable).
Three unrelated older lib files (`Status`, `K3IndexArithmetic`, `W2Polynomial`) also fail and drag
`lake build` (the whole lib) to a nonzero exit.

## 1. Environment probe (HONEST, actual outputs)

`lean`/`lake`/`elan` are NOT on `PATH`, but elan IS installed at `~/.elan/bin`:

```
~/.elan/bin/elan --version   -> elan 4.2.3 (b6cec7e10 2026-06-08)
~/.elan/bin/lean --version   -> Lean (version 4.31.0, x86_64-w64-windows-gnu, Release)   [default]
~/.elan/bin/lake --version   -> Lake version 5.0.0-src+68218e8 (Lean version 4.31.0)
toolchains installed         -> leanprover--lean4---v4.31.0, leanprover--lean4---v4.32.0-rc1
```

Repo Lake state (this is the correction to the A1 inventory):

```
lean-toolchain           -> leanprover/lean4:v4.32.0-rc1
lakefile.lean            -> require "leanprover-community" / "mathlib"; lean_lib GUFormalization (srcDir "Lean")
.lake/packages/          -> aesop batteries importGraph LeanSearchClient mathlib plausible proofwidgets Qq
mathlib oleans built     -> 8255 *.olean under .lake/packages/mathlib/.lake/build   (mathlib IS provisioned + compiled)
our lib build outputs    -> .lake/build/lib/lean/GUFormalization/*.olean present
toolchain in effect      -> `lake env lean --version` -> Lean 4.32.0-rc1
```

The A1 inventory (`papers/drafts/hardening-pass-2026-07-03/A1-lean-formalization-inventory.md`)
and the header of `Lean/GUFormalization/LocatedNotForcedLegs.lean` both state mathlib was NOT
provisioned and the `import Mathlib` files were "NOT typechecked / UNVERIFIED." **That is now stale.**
Mathlib was provisioned and built after those were written (`.lake` timestamped Jul 3 11:14).

No large downloads were triggered by this run — everything needed was already on disk.

## 2. What ACTUALLY typechecked this run

### 2a. Mathlib-free arithmetic core — CLOSED
```
lean papers/drafts/hardening-pass-2026-07-03/A1-arith-core-check.lean   -> EXIT 0
```
No errors, no `sorry`, no `axiom`. Confirms the inventory's claim for the five core-Lean identities
(`rs_bulk_index_on_rokhlin`, `rs_bulk_even`, `adjoint_index_div_four`, `kramers_mod_two`,
`ghost_parity_net_zero`). Genuinely machine-checked, toolchain v4.32.0-rc1.

### 2b. The located-not-forced core spine (import Mathlib) — CLOSED
File: `Lean/GUFormalization/LocatedNotForcedLegs.lean`.

`lake build GUFormalization` **replayed this module clean** (olean current with source hash; the
olean therefore genuinely compiled with no errors), and a fresh full elaboration
(`lake env lean Lean/GUFormalization/LocatedNotForcedLegs.lean`) was run to remove all doubt.
Only two BENIGN LINTER WARNINGS, no errors, no `sorry`, no `axiom`:

- `linter.unusedVariables`: bound `K` at line 52 (cosmetic).
- `linter.unusedSimpArgs`: `Submodule.mem_bot` unused in the `simp` at line 77 (cosmetic).

Machine-verified theorems in this file (this is the theorem-grade spine):
- `KreinIndex.positive_inter_isotropic_trivial`, `inter_isotropic_eq_bot`
- `KreinIndex.chi_eq_zero`  — **Theorem 2 finite-dim core (net chiral index = 0)**
- `KreinIndex.antilinear_bound`  — **Leg 2, antilinear null-eigenspace bound** (corollary)
- `KreinIndex.definite_not_isotropic`  — the "null condition is load-bearing" boundary
- `TwoPrimary.cross_chirality_ninety_six / _net_zero` (3a), `spinor_dim_not_div_three` (3b),
  `rs_bulk_index_on_rokhlin / rs_bulk_even` (3c), `adjoint_index_div_four` (3d),
  `lens_eta_numerator_odd / lens_eta_denominator_two_primary` (3e),
  `kramers_mod_two / ghost_parity_net_zero` (3f).

This closes the exact gap every RESULTS file and `canon/core-theorems-symbolic-proof-RESULTS.md`
flagged: "a Lean/symbolic port would upgrade the grade." The finite-dimensional structural core is
now **Lean-typechecked**, not merely sympy-symbolic. (Scope unchanged: the physical premises —
that the actual 192-dim carrier form is cross-chirality signature (96,96), etc. — remain machine-
checked Python hypotheses fed into the Lean theorems, NOT re-derived in Lean. Nothing here derives
the generation count.)

## 3. What did NOT typecheck (honest failures)

### 3a. R4 two-arena big-swing — BLOCKED (mathlib-master API drift, fixable)
```
lake env lean tests/big-swing/R4_TwoArena.lean   -> R4_EXIT 1
```
Three real errors, all API drift against current mathlib master (not logic errors):
1. `R4_TwoArena.lean:66` — `Finset.card_sdiff` is applied as `Finset.card_sdiff (filter_subset ..)`,
   but in this mathlib `Finset.card_sdiff` resolves to an unconditional equality
   `(s \ t).card = s.card - (t ∩ s).card` (not a function taking the subset proof positionally).
   Cascades to an unsolved goal at line 59 (`minusCount_neg`).
2. `R4_TwoArena.lean:143` — `addOrderOf_eq_one_iff` is an **unknown identifier** (renamed/moved in
   current mathlib). Used in `eq_zero_of_coprime_nsmul`.

Everything else in the file (Leg A parity lemmas, Leg B CRT `twoArena`, `two_primary_blind`,
`arenas_disjoint`, Leg C `TwoPrimaryGenerators`) is structurally sound; the two API breaks are the
only blockers. This matches the risk the A1 inventory itself predicted ("API-name drift, resolvable
at first compile") — now realized and pinpointed.

### 3b. Three older lib modules — FAILED (pre-existing, outside the named spine)
`lake build GUFormalization` builds all four lib modules; the spine one passes, these three fail,
so the **whole-lib build exits 1**:
- `GUFormalization/Status.lean` — uses the reserved keyword `open` as a `ClaimStatus` constructor
  (`| open => 1`, `verified <= open`): syntax errors at lines 32/52/55 plus `simp made no progress`
  at 70/75/80.
- `GUFormalization/W2Polynomial.lean` — `ring_nf [lemmas]` simp-arg syntax is rejected (lines
  35/51 `unexpected token '['`); `ring` cannot prove `baseObstruction * 2 = 0` because `F2` is an
  abstract field, not `ZMod 2` (char-2 fact not available to `ring`); unsolved goals at 34/50/60.
- `GUFormalization/K3IndexArithmetic.lean` — Lean crashed with exit `3221225477` (0xC0000005
  access violation / segfault) on this Windows toolchain; no diagnostic. Needs an isolated re-run.

These three are not part of the "core-theorem spine" this task targets, but they are why a naive
`lake build` reports failure. They pre-date this run.

## 4. Honest outcome grades

| Target | Grade | Evidence |
|---|---|---|
| Arithmetic core (`A1-arith-core-check.lean`, mathlib-free) | **CLOSED** | `lean` EXIT 0, no sorry/axiom |
| Located-not-forced spine (`LocatedNotForcedLegs.lean`: Thm 2 core, antilinear bound, 3a–3f) | **CLOSED** | replayed + fresh-elaborated clean; only linter warnings; no sorry/axiom |
| R4 two-arena (`tests/big-swing/R4_TwoArena.lean`) | **BLOCKED (fixable)** | 2 mathlib-master API-drift errors, pinpointed |
| `Status` / `W2Polynomial` / `K3IndexArithmetic` (older lib) | **FAILED** | syntax / char-2 gap / segfault; pre-existing, out of scope |

## 5. Exact unblock steps for a future run

- **To re-verify the spine (no download needed):**
  `export PATH="$HOME/.elan/bin:$PATH"` then
  `lake env lean Lean/GUFormalization/LocatedNotForcedLegs.lean` (expect exit 0, 2 linter warnings).
- **To fix R4 (bounded, ~2 edits):**
  (i) replace `rw [hcompl, Finset.card_sdiff (Finset.filter_subset _ _)]` with a form that matches
  the unconditional `Finset.card_sdiff` in mathlib v4.32-rc1 (rewrite then discharge the
  `t ∩ s` / `card_univ` bookkeeping with `simp`); (ii) replace `addOrderOf_eq_one_iff.mp this`
  with the current lemma name (grep mathlib for `addOrderOf_eq_one` / use
  `by simpa using this` on `addOrderOf x = 1 → x = 0`). Then
  `lake env lean tests/big-swing/R4_TwoArena.lean`.
- **Toolchain/pin of record:** elan 4.2.3; `leanprover/lean4:v4.32.0-rc1`; mathlib pinned to
  `master` in `lake-manifest.json` (already fetched + built, 8255 oleans).

## 6. Recommended follow-ups (NOT done here — staging only)

- The header of `Lean/GUFormalization/LocatedNotForcedLegs.lean` still says "**UNVERIFIED (this
  file)** ... has not been typechecked." **This is now false** — it typechecks clean against the
  provisioned mathlib. Recommend Joe update that header (and the A1 inventory's toolchain-status
  paragraph) to reflect CLOSED status. Left unedited here to respect the no-promote / no-paper-edit
  rule.
- `canon/core-theorems-symbolic-proof-RESULTS.md` grade line notes "NOT a fully machine-checked
  formal (Lean/Coq) proof -- no Lean ... in this sandbox." For the finite-dimensional core that
  caveat can now be softened to "Lean-typechecked (v4.32.0-rc1 + mathlib)" — Joe's decision, on the
  spine only; the function-space / APS analytic residual remains untouched.
