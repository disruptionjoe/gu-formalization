---
title: "Lean Verification Run"
status: canon
doc_type: runbook
scope: repo-local
created: 2026-07-07
ledger: lab/process/lean-verification-lane-LEDGER.md
---

# Lean Verification Run

The default run type for **hourly / automated progress runs**. Its job is convergent hardening:
turn already-proven finite theorems into machine-checked Lean, advancing the queue in
`lab/process/lean-verification-lane-LEDGER.md`. Discovery — breaking no-gos, escaping obstructions,
new mechanisms — is reserved for maintainer-directed sessions (see the rationale in
`../../repos/public/ai-epistemology` on the automation-vs-directed division of labor, and
`five-lane-frontier-run.md` for the discovery run type, now session-only by default).

Why this is the automation default: the five-lane discovery run keeps hitting its no-progress HALT
(claim promotions read zero), because divergent discovery is not reliably automatable. Lean
verification is the opposite — every item either typechecks (exit 0, no `sorry`/`axiom`) or it does
not, so a run always has a well-defined, monotone success condition.

## The run loop

1. **Pick the top unblocked item** from the LEDGER Part C queue (L0 first on a cold start or after
   any mathlib bump; then L1, L2, ... in order). One item per run is fine; the point is a
   green typecheck, not volume.
2. **Read the source certificate** the item names (the numpy/sympy script + its route doc) so the
   Lean statement matches the computed result exactly, and so the computed matrix facts are carried
   as explicit HYPOTHESES (the faithfulness boundary — Lean proves the deduction, not that the
   matrices are GU's).
3. **Write the Lean file** under `Lean/GUFormalization/` (or extend an existing one). Keep it
   finite and elementary; prefer `omega`/`decide`/`ring`/`field_simp`/`norm_num` and named mathlib
   lemmas over long tactic blocks.
4. **Typecheck: `lake build GUFormalization`** (or the targeted file). It must exit 0 with no
   `sorry` and no `axiom`. If it does not, either fix it within the run or leave it LEAN-PARTIAL
   with a one-line note on the exact blocker — do not commit a red or `sorry`-carrying file as
   verified.
5. **Update the LEDGER**: flip the item's status (NUMPY-CERT/SYMPY-DERIVED -> LEAN-VERIFIED, or ->
   LEAN-PARTIAL with the blocker), add the file to `Lean/README.md`'s certificate table with its
   owner surface.
6. **Commit** the Lean file + LEDGER + README by explicit path. A canon claim's status flip to
   `verified` (in `RESEARCH-STATUS.md` / the paper's status table) still PAUSES for the maintainer —
   append a one-line note to `../mailboxes/joeops/` proposing it; do not flip canon yourself.

## Progress metric and HALT

Progress = at least one of: a queue item newly LEAN-VERIFIED; a LEAN-PARTIAL repaired; the baseline
build re-confirmed green after a real drift. If **every** queue item is genuinely blocked (a true
mathlib gap, not a solvable API-name drift), append a dated `## BLOCKED` note to the LEDGER with the
exact obstruction and the human action needed, and HALT — do not manufacture a trivial file to
appear busy. A run that only re-states "still blocked" is not progress.

## Scope guards

- Lean checks finite kernels only; markdown owns interpretation, provenance, physics scope (per
  `Lean/README.md`). Do not let a Lean file assert a physics claim.
- The computed premises (carrier faithfulness, the actual matrix (anti)commutations) are inputs, not
  Lean outputs. Never upgrade "the deduction is Lean-checked" to "the physics is Lean-proved."
- No `git add -A`; stage the Lean file, the LEDGER, and the README by explicit path.
