---
title: "Lean Verification Run"
status: canon
doc_type: runbook
scope: repo-local
created: 2026-07-07
updated: 2026-07-15
ledger: lab/process/lean-verification-lane-LEDGER.md
---

# Lean Verification Run

The reserve convergent-hardening run type. Its job is to turn already-stable finite theorems into
machine-checked Lean, advancing `lab/process/lean-verification-lane-LEDGER.md` when the daily portfolio
selects this lane.

The hourly default is `meaningful-hourly-progress-swing.md`. Lean is a method inside the reserve lane,
not an automatic priority. Its finishability must not displace a harder North-Star lane that has not
been falsified or genuinely blocked.

## The run loop

1. **Confirm portfolio selection.** The run receipt states why the protected primary lane is blocked,
   complete for its current swing, or explicitly yielding to this reserve lane. Then follow the
   LEDGER Part C integrity-first order: fresh default-target baseline, existing R4 integration and
   stale-duplicate retirement, then a new theorem kernel.
2. **Read the source certificate.** Match the Lean statement to the computed result exactly. Carry
   computed matrix facts as explicit hypotheses. Lean proves the deduction, not that the matrices are
   GU's physical carrier.
3. **Write the Lean file.** Use `Lean/GUFormalization/` or extend an existing file. Keep it finite and
   elementary. Prefer named mathlib lemmas and small tactics over opaque tactic blocks.
4. **Typecheck through the serialized guard:** `./lab/automation/check-lean.ps1`. The helper acquires
   the GU build lock and runs `lake build -j1`. The build must exit 0 with no `sorry` and no `axiom`.
   If it does not, fix it within the run or leave it LEAN-PARTIAL with the exact blocker. Do not commit
   a red or `sorry`-carrying file as verified.
5. **Update the ledger and Lean map.** Flip the selected item's local Lean status and add a precise owner
   entry to `Lean/README.md` when a certificate becomes green.
6. **Commit by explicit path.** Stage only the Lean file, ledger, and owner map that belong to the swing.
   A scientific-status flip still pauses for Joe under repository governance. Lean verification of a
   deduction alone does not authorize that flip.

## Progress metric and halt

Progress is at least one of:

- a newly LEAN-VERIFIED stable kernel;
- a LEAN-PARTIAL item repaired;
- a baseline build reconfirmed after real toolchain drift;
- a proposed formalization rejected with an exact faithfulness, scope, or mathlib obstruction that
  prevents an invalid theorem from entering Lean.

If every eligible item is genuinely blocked, report the exact obstruction and halt. Do not manufacture
a trivial theorem to appear busy.

## Scope guards

- Lean checks finite mathematical kernels. Markdown owns interpretation, provenance, construction fork,
  and physics scope.
- Carrier faithfulness, actual matrix identities, full-arena transfer, Proposition 1, the W235 record bit,
  and interacting physical realization remain explicit premises or external scope conditions.
- Never formalize W241's false frame-specific implication that every compact-image isotropy commutes with
  one fixed `P`. W244 showed the narrower order-parameter no-go survives by a different mechanism.
- The Windows wrapper serializes only this host. It does not coordinate another computer or cloud runner,
  and policy cannot prevent a direct `lake` command. Every run must use the applicable host lock plus `-j1`.
- Do not let "Lean-verified deduction" become "physics proved."
- Never use `git add -A`.
