---
title: "Lean Verification Lane: Ledger and Queue"
status: canon
doc_type: lane-ledger
scope: repo-local
created: 2026-07-07
updated: 2026-07-15
owner_surface: lab/process/runbooks/lean-verification-run.md
---

# Lean verification lane: ledger and queue

## Purpose and boundary

This is the standing queue for the Lean reserve lane. Hourly Progress uses it only when
`lab/process/research-portfolio.json` selects the reserve. A finishable formalization must not displace
the protected North-Star lane merely because Lean has a monotone success condition.

Lean hardens the deduction from explicit premises. It does not establish carrier faithfulness, physical
realization, full-arena transfer, Proposition 1, the W235 record bit, interacting QFT, or external
replication. Those stay in owner prose and machine certificates. Status vocabulary:

- `LEAN-VERIFIED`: default or named target typechecks, with no `sorry` or unreported axioms, and the owner cites it.
- `SOURCE-READY`: complete proof source exists, but the current checkout lacks a green build receipt.
- `LEAN-PARTIAL`: source needs a bounded repair.
- `NUMPY-CERT`: checked in Python only.
- `SYMPY-DERIVED`: symbolic result outside Lean.
- `PROSE`: written argument only.

## Part A: current certificate surface

The toolchain and manifest are pinned. A fresh checkout currently has no compiled-artifact receipt, so
the default target must be rebuilt before this lane claims a current green baseline.

| Lean file | Scope | Current source status |
|---|---|---|
| `Lean/GUFormalization/Status.lean` | Claim-status order and dependency monotonicity | Previously `LEAN-VERIFIED`; baseline refresh due |
| `Lean/GUFormalization/K3IndexArithmetic.lean` | Symbolic K3 and RS index arithmetic | Previously `LEAN-VERIFIED`; baseline refresh due |
| `Lean/GUFormalization/W2Polynomial.lean` | `F_2` polynomial identities behind corrected `w2(Y14)` | Previously `LEAN-VERIFIED`; baseline refresh due |
| `Lean/GUFormalization/LocatedNotForcedLegs.lean` | Krein index-nullity, antilinear bound, and 2-primary identities | Previously `LEAN-VERIFIED`; authoritative A1 certificate |
| `Lean/GUFormalization/ResidualSelection.lean` | Residual-selection finite logic kernels | Previously `LEAN-VERIFIED`; baseline refresh due |
| `tests/big-swing/R4_TwoArena.lean` | R4 weight parity, CRT, and 2-primary blindness | `SOURCE-READY`; sorry-free and axiom-free standalone source, not yet in the default target |

The un-typechecked draft duplicate
`papers/drafts/hardening-pass-2026-07-03/A1-located-not-forced-legs.lean` remains outside the certificate
surface and is scheduled for retirement at L2. It must not be cited as a certificate.

## Part B: stable theorem-grade queue

| Id | Theorem-grade claim | Source | Current | Feasibility | Load-bearing for |
|---|---|---|---|---|---|
| T1 | No-go is 2-primary; no obstruction is 3-divisible | located-not-forced paper section 4 | `LEAN-VERIFIED` at last receipt | complete | located-not-forced |
| T2 | Linear Krein-isometry conserves net chiral index zero | located-not-forced paper section 6 | `LEAN-VERIFIED` at last receipt | complete | located-not-forced |
| T3 | Antilinear null-eigenspace bound | located-not-forced paper section 6 | `LEAN-VERIFIED` at last receipt | complete | located-not-forced |
| A | Achirality: `{K,chi}=0` implies `Re tr(chi Pi_+) = 0` | R3 | `NUMPY-CERT` | high | fences the chiral-generation reading |
| B | V7 mod-3 index arithmetic | V7 | `SYMPY-DERIVED` | high | count-import boundary |
| C | Exact A1 phase boundary `lq = -l4/192` | A1b | `SYMPY-DERIVED` | high | mirror alignment phase |
| D | Power-mean reduction | A1b | `NUMPY-CERT` | medium | supports C |
| E | Chi-parity no-go for orientation selection | A2 | `NUMPY-CERT` | medium | sign-selection boundary |
| F | Abstract Cartan-involution structural core | V2 | `NUMPY-CERT` | medium | quantization seat |
| G | Involution projector algebra for the mirror map | V8 | `NUMPY-CERT` | medium | mirror kinematics |
| H | Extremal-weight stabilizer contains an explicit nonzero nilpotent | W243, GU-002, W244 | structural plus `NUMPY-CERT` | medium | compactification no-go |

## Part C: integrity-first execution order

The first three items are mandatory integrity work, not a retreat from the North Star.

1. `L0 BASELINE`: run `lab/automation/check-lean.ps1` so the default `GUFormalization` target builds at
   `-j1`; record exit status, toolchain, manifest revision, and placeholder scan.
2. `L1 R4 INTEGRATION`: move or fold `tests/big-swing/R4_TwoArena.lean` into the default
   `GUFormalization` target; fix only real API drift; require exit 0 with no `sorry` or unreported axioms.
3. `L2 STALE DUPLICATE`: remove the un-typechecked A1 draft duplicate and make historical notes point to
   `Lean/GUFormalization/LocatedNotForcedLegs.lean` as the sole authoritative certificate.
4. `L3 THEOREM H`: formalize the extremal-weight stabilizer deduction over an explicitly graded finite
   representation. Carrier realization, Proposition 1, W235, and compactness remain explicit premises or
   outside the Lean conclusion. Do not formalize W241's false fixed-`P` implication.
5. `L4 THEOREM A`: formalize the achirality trace core with matrix anticommutation supplied as a premise.
6. `L5 THEOREM B`: formalize the pure mod-3 arithmetic using `Nat`, `Int`, `omega`, or `decide`.
7. `L6 THEOREM C`: formalize the exact rational phase boundary with `field_simp` and `ring`.
8. `L7 THEOREM D`: formalize the power-mean reduction.
9. `L8 THEOREM E`: formalize trace parity under chi conjugation.
10. `L9 THEOREMS F AND G`: formalize only the abstract involution and projector cores.
11. `L10 OLD FILE TRIAGE`: repair or retire older broken library files only when they create certificate
    confusion or every higher-value stable kernel is blocked.

## Part D: lock and progress contract

On Windows, every invocation uses `lab/automation/check-lean.ps1`. Its exclusive file handle is host-local.
It does not serialize another computer or cloud runner, and it cannot technically stop a direct command from
bypassing policy. Other hosts require a runner-native single-build lock and `-j1`. No two hosts may write the
same checkout.

A run makes progress only by producing a current green baseline, integrating an existing certificate,
retiring a misleading certificate lookalike, adding a newly `LEAN-VERIFIED` kernel, repairing a
`LEAN-PARTIAL` kernel, or recording an exact faithfulness/mathlib obstruction that prevents a false theorem
from entering Lean. Do not manufacture a trivial theorem to appear busy.
