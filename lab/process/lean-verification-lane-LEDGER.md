---
title: "Lean Verification Lane: Ledger and Queue"
status: canon
doc_type: lane-ledger
scope: repo-local
created: 2026-07-07
updated: 2026-08-03
owner_surface: lab/process/runbooks/lean-verification-run.md
---

# Lean verification lane: ledger and queue

## Purpose and boundary

This is the standing Lean queue inside Lane 3, result hardening and publication readiness. Hourly Progress
uses it only when `lab/process/research-portfolio.json` selects the relevant Lane 3 work item. A finishable
formalization must not displace protected Lane 1 merely because Lean has a monotone success condition.

Lean hardens the deduction from explicit premises. It does not establish carrier faithfulness, physical
realization, full-arena transfer, Proposition 1, the W235 record bit, interacting QFT, or external
replication. Those stay in owner prose and machine certificates. Status vocabulary:

- `LEAN-VERIFIED`: default or named target typechecks, with no `sorry` or unreported axioms, and the owner cites it.
- `SOURCE-READY`: complete proof source exists, but the current checkout lacks a green build receipt.
- `LEAN-PARTIAL`: source needs a bounded repair.
- `NUMPY-CERT`: checked in Python only.
- `SYMPY-DERIVED`: symbolic result outside Lean.
- `ARB-CERT`: rigorous interval/ball enclosure via python-flint (FLINT 3 / Arb), with the working
  precision recorded. Strictly stronger than `NUMPY-CERT` for any claim that compares floats or
  asserts a bound; strictly weaker than an exact symbolic identity. Use it for the RB-campaign
  residual, signal/floor, and stability margins currently graded "controlled local numerics."
- `CAS-VERIFIED`: multiplicity, branching, or rank result independently confirmed in a computer
  algebra system (SageMath / Singular / GAP), with the session transcript or script committed.
  Required by the gates listed in `computational-toolchain.md`. Layer-0 applies: a CAS returns a
  decomposition, never a count.
- `PROSE`: written argument only.

## Part A: current certificate surface

The toolchain and manifest are pinned.  A fresh serialized macOS build at Lean `4.32.0-rc1` and manifest
mathlib revision `96ec947e9b66a5e6059131fc9c6d13a14cef756e` completed successfully on 2026-07-22
(`lake build`, 8,643 jobs, exit 0; pre-existing linter warnings only).  Receipt scope note (2026-08-03):
that 2026-07-22 build predates the 2026-07-23 edits to `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`
and `Lean/GUFormalization/LocatedNotForcedLegs.lean`.  The current receipt for those two files is the
located-not-forced v1.0.0 release verification,
`papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md` (verified 2026-07-23):
targeted `lake -Kjobs=1 build +GUFormalization.LocatedNotForcedFiniteCore` (which builds
`LocatedNotForcedLegs` via its import) plus `lake env lean` single-file checks passed, with only the
standard mathlib axioms `propext`, `Classical.choice`, `Quot.sound` reported.

| Lean file | Scope | Current source status |
|---|---|---|
| `Lean/GUFormalization/Status.lean` | Claim-status order and dependency monotonicity | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/K3IndexArithmetic.lean` | Symbolic K3 and RS index arithmetic | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/W2Polynomial.lean` | `F_2` polynomial identities behind corrected `w2(Y14)` | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/LocatedNotForcedLegs.lean` | Krein transversality (positive-definite subspace meets each totally isotropic subspace trivially; `intersectionDifference = 0`) and 2-primary identities; no antilinear operator content (scope corrected 2026-08-03) | `LEAN-VERIFIED`; authoritative A1 certificate; current receipt is the 2026-07-23 zenodo package `VERIFICATION.md` (see receipt scope note above) |
| `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean` | Finite census encoding for the LNF paper; exhaustiveness/closure by `decide` over the encoded item list; census numerals are imported data, not derivations | `LEAN-VERIFIED`; 2026-07-23 zenodo receipt (`papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md`) |
| `Lean/GUFormalization/ResidualSelection.lean` | Residual-selection finite logic kernels | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/ResidualSelectionAxioms.lean` | Manual `#print axioms` receipt; NOT in the default target; informational, non-enforcing — run via `lake env lean` | `LEAN-VERIFIED`; 2026-07-22 baseline toolchain (via `lake env lean`; outside the default `lake build`) |
| `Lean/GUFormalization/R4TwoArena.lean` | R4 weight parity, CRT, and 2-primary blindness | `LEAN-VERIFIED`; default-target integration 2026-07-22 |
| `Lean/GUFormalization/CoflipCore.lean` | Concrete Q×Q coflip accounting, Part A derived | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/CoflipAbstract.lean` | Abstract (eps,mu) sign accounting; the `FiniteSignature` field and the `witnessed` Prop are currently formally inert — noted | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `tests/big-swing/R4_TwoArena.lean` | Stable R4 compatibility entrypoint | imports the default-target proof-bearing module |

The un-typechecked draft duplicate formerly at
`papers/drafts/hardening-pass-2026-07-03/A1-located-not-forced-legs.lean` was retired on 2026-07-22.
`Lean/GUFormalization/LocatedNotForcedLegs.lean` is the sole authoritative certificate.

## Part B: stable theorem-grade queue

| Id | Theorem-grade claim | Source | Current | Feasibility | Load-bearing for |
|---|---|---|---|---|---|
| T1 | No-go is 2-primary; no obstruction is 3-divisible | located-not-forced paper section 4 | `LEAN-VERIFIED` at last receipt | complete | located-not-forced |
| T2 | Krein transversality: positive-definite subspace meets each totally isotropic subspace trivially (`intersectionDifference = 0`) | located-not-forced paper section 6 | `LEAN-VERIFIED` at last receipt (retitled 2026-08-03: `papers/candidates/located-not-forced/HARDENING-QUEUE.md:118` bans the former "net chiral index" phrasing) | complete | located-not-forced |
| T3 | Antilinear null-eigenspace bound | located-not-forced paper section 6 | `SYMPY-DERIVED` (corrected 2026-08-03: no antilinear operator content exists in `Lean/`; the owning canon file `canon/core-theorems-symbolic-proof-RESULTS.md` itself states "a symbolic proof, not a Lean-checked one"; the Krein-transversality Lean lemma covers T2 only) | high | located-not-forced |
| A | Achirality: `{K,chi}=0` implies `Re tr(chi Pi_+) = 0` | `canon/ghost-parity-krein-synthesis.md:26` (statement); `explorations/big-swing-2026-07-06/R3-pt-phase-classification-gu-cores.md` | `NUMPY-CERT` | high | fences the chiral-generation reading |
| B | V7 mod-3 index arithmetic | `explorations/big-swing-2026-07-06/VG-V7-cp2-equivariant-payoff.md` | `SYMPY-DERIVED` | high | count-import boundary |
| C | Exact A1 phase boundary `lq = -l4/192` | `explorations/big-swing-2026-07-07/A1-native-potential-alignment.md` | `SYMPY-DERIVED` | high | mirror alignment phase |
| D | Power-mean reduction | A1b (source document not located in repo — flagged 2026-08-03) | `NUMPY-CERT` | medium | supports C |
| E | Chi-parity no-go for orientation selection | `explorations/big-swing-2026-07-07/A2-native-ring-symmetry-nogo.md` | `NUMPY-CERT` | medium | sign-selection boundary |
| F | Abstract Cartan-involution structural core | `explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md` | `NUMPY-CERT` | medium | quantization seat |
| G | Involution projector algebra for the mirror map | `explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md` | `NUMPY-CERT` | medium | mirror kinematics |
| H | Extremal-weight stabilizer contains an explicit nonzero nilpotent | W243, GU-002, W244 | structural plus `NUMPY-CERT` | medium | compactification no-go |

## Part C: integrity-first execution order

The first three items are mandatory integrity work, not a retreat from the North Star.

1. `L0 BASELINE` — **DONE 2026-07-22**: exact pinned default target, serialized, exit 0; receipt above.
2. `L1 R4 INTEGRATION` — **DONE 2026-07-22**: proof-bearing source folded into the default target; old path
   retained as a compatibility entrypoint; post-integration build and placeholder audit required by the run receipt.
3. `L2 STALE DUPLICATE` — **DONE 2026-07-22**: the un-typechecked A1 draft duplicate was removed;
   `Lean/GUFormalization/LocatedNotForcedLegs.lean` is the sole authoritative certificate.
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
