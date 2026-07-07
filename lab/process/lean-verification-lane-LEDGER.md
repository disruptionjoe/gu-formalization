---
title: "Lean Verification Lane — Ledger and Queue"
status: canon
doc_type: lane-ledger
scope: repo-local
created: 2026-07-07
owner_surface: lab/process/runbooks/lean-verification-run.md
---

# Lean Verification Lane — Ledger and Queue

**Purpose.** This is the standing work-queue for the Lean verification lane. Discovery (big
swings, new mechanisms) happens in interactive maintainer sessions; **hourly / progress runs work
THIS lane** — formalizing already-proven finite theorems in Lean 4 + mathlib so the paper's
deductive spine carries machine-checked proof, not prose. Convergent by design: each item either
typechecks to exit 0 with no `sorry`/`axiom`, or it does not. See the runbook for the run loop.

**The honest boundary (what Lean does and does not harden).** Lean hardens the *deductive* step:
given the premises, the conclusion follows. It does NOT harden (a) *faithfulness* — that the numpy
carrier is GU's actual matter module (that is a modeling audit, a separate lane), or (b) the
*single-process ceiling* — external replication. So every Lean theorem below takes the computed
matrix facts as HYPOTHESES (supplied by the numpy/sympy certificates) and proves the structural
core over them. "Lean-verified" here means the deduction is machine-checked, with the premises
explicitly the computed certificates — exactly the boundary set in
`papers/drafts/hardening-pass-2026-07-03/A1-lean-formalization-inventory.md`.

Status vocabulary: **LEAN-VERIFIED** (typechecks, no sorry/axiom, cited by owner surface) /
**LEAN-PARTIAL** (written, needs a bounded fix) / **NUMPY-CERT** (machine-checked in Python only) /
**SYMPY-DERIVED** (symbolic, not Lean) / **PROSE** (hand-argued only).

---

## Part A — Baseline: what is already Lean-verified (2026-07-07)

Provisioning is done: `lake` on PATH, `.lake` present, mathlib provisioned (per the 2026-07-03
correction). Certified files (`Lean/README.md`):

| Lean file | Scope | Status |
|---|---|---|
| `GUFormalization/Status.lean` | claim-status order + dependency-monotonicity governance kernel | LEAN-VERIFIED |
| `GUFormalization/K3IndexArithmetic.lean` | symbolic K3 / RS index arithmetic | LEAN-VERIFIED |
| `GUFormalization/W2Polynomial.lean` | `F_2` polynomial identities behind the corrected `w2(Y14)` | LEAN-VERIFIED |
| `GUFormalization/LocatedNotForcedLegs.lean` | located-not-forced spine: Krein index-nullity (Th 2), antilinear bound, 2-primary identities (Th 1) | LEAN-VERIFIED (per 2026-07-03 correction; re-confirm build, task L0) |
| `tests/big-swing/R4_TwoArena.lean` | standalone two-arena rep-theory legs (R4) | LEAN-PARTIAL (2 mathlib API-drift fixes) |

So the **located-not-forced paper's deductive spine is already Lean-verified.** The gap this lane
closes is the 2026-07-06/07 swing results, none of which are yet in Lean.

---

## Part B — The theorem-grade ledger (paper + 2026-07-06/07 swings)

| # | Theorem-grade claim | Source | Current | Lean feasibility | Load-bearing for |
|---|---|---|---|---|---|
| T1 | No-go is 2-primary; no obstruction is 3-divisible (Th 1) | paper §4 | LEAN-VERIFIED | — | located-not-forced |
| T2 | Linear Krein-isometry conserves net chiral index = 0 (Th 2) | paper §6 | LEAN-VERIFIED | — | located-not-forced |
| T3 | Antilinear null-eigenspace bound (CII escape) | paper §6 | LEAN-VERIFIED | — | located-not-forced |
| **A** | **Achirality: `{K,chi}=0 => Re tr(chi Pi_+) = 0` for every admissible C** | R3 (`cg_r3_pt_phase_gu_cores.py`) | NUMPY-CERT | **HIGH** (trace + anticommutation, ~10 lines) | fences the "3 chiral generations" canon reading |
| **B** | **V7 mod-3 arithmetic: selected `m^2 = 1 (mod 3)`; `ind = 12k + 16 m^2 d' - 2 sigma`; residue `= m^2 d' + sigma`** | V7 (`vg_v7_cp2_equivariant_payoff.py`) | SYMPY-DERIVED | **HIGH** (pure Nat/Int, `omega`/`decide`, like the 2-primary legs) | closes the count import (CP^2 double import) |
| **C** | **A1 phase boundary `lq = -l4/192`: corner min `-24/(96 l0+l4+96 lq)` vs sym min `-48/(192 l0+l4)`, diff vanishes at `-l4/192`** | A1b (`as_a1b_reduced_phase_confirm.py`) | SYMPY-DERIVED | **HIGH** (rational-function comparison, `field_simp`/`ring`) | mirror mechanism: alignment is a phase |
| **D** | **Power-mean reduction: `tr(A^4) >= tr(A^2)^2 / n`, equality iff uniform** | A1b | NUMPY-CERT | MEDIUM (mathlib `inner_mul_le` / power-mean) | justifies the 2-scalar reduction (C) |
| **E** | **chi-parity split: `chi K chi = -K => t_n` chi-even, `q_n` chi-odd => chi-symmetric potential cannot select orientation** | A2 (`as_a2b_native_ring_symmetry_nogo.py`) | NUMPY-CERT | MEDIUM (trace parity under conjugation) | bounded no-go: import = one sign bit |
| **F** | **Cartan structural core: `theta^2 = id`, `B_theta > 0` on even part, even part = max compact** | V2 (`vg_v2_fourth_seat_gauge_indefiniteness.py`) | NUMPY-CERT | MEDIUM (abstract Cartan involution; the `theta = K` identity stays NUMPY-CERT) | fourth seat = quantization seat |
| **G** | **V8 mirror map core: for an involution `Q5`, `Pi_mirror = (I - Q5)/2` projects, gaps one K-half, `[M,P]=0`** | V8 (`vg_v8_t5_map_attempt.py`) | NUMPY-CERT | MEDIUM (projector algebra of an involution) | mirror mechanism kinematics |

The paper legs T1-T3 are done. Items A-G are the lane's work, roughly in priority order (A, B, C
first: highest feasibility × load-bearing).

---

## Part C — The prioritized queue (what an hourly run picks up)

Work top-down; each item = one Lean theorem file + a ledger status flip to LEAN-VERIFIED.

- **L0 — re-confirm the baseline build is green.** `lake build GUFormalization` exit 0, no
  sorry/axiom in the four verified files. (First run only, and after any mathlib bump. Cheap,
  always-progressable, and it protects everything downstream.)
- **L1 — Theorem A (achirality).** New file `Lean/GUFormalization/AchiralityKrein.lean`: over a
  finite real/complex space with `K` self-adjoint, `chi` with `{K,chi}=0` (hypothesis), and `Pi_+`
  the positive spectral projector, prove `Re tr(chi Pi_+) = 0`. Premise "the actual 192-dim
  matrices anticommute" stays a numpy hypothesis. Feasibility HIGH.
- **L2 — Theorem B (V7 mod-3 arithmetic).** Extend `K3IndexArithmetic.lean` or new
  `Cp2IndexArithmetic.lean`: `m^2 % 3 = 1` for `m in {1,2,4,5} (mod 3, m not div by 3)`;
  `ind = 12*k + 16*m^2*d' - 2*sigma`; the mod-3 residue identity; conclude a factor 3 requires
  `3 | m AND 3 | sigma`. Pure `Nat`/`Int`, `omega`/`decide`. Feasibility HIGH — mirrors the
  existing 2-primary legs exactly.
- **L3 — Theorem C (phase boundary).** New `PhaseBoundary.lean`: the two rational minima and the
  exact root `lq = -l4/192` (as `-l4/(2*96)`); `field_simp`/`ring`. Feasibility HIGH.
- **L4 — Theorem D (power-mean).** The Cauchy-Schwarz eigenvalue inequality from mathlib; supports
  L3's reduction. MEDIUM.
- **L5 — Theorem E (chi-parity no-go).** Trace-parity under `chi`-conjugation; the chi-symmetric
  potential degeneracy. MEDIUM.
- **L6 — Theorem F (Cartan core) & G (mirror projector core).** The abstract involution / Cartan
  structural cores. MEDIUM.
- **L7 — repair `R4_TwoArena.lean`** (2 API-drift fixes) and triage the 3 older broken lib files
  (repair or retire with a note). Cleanup; always available when L1-L6 are blocked.

---

## Part D — Progress metric and the anti-no-op rule

Unlike the discovery runbook (whose progress metric — claim promotions — keeps reading zero and
triggering HALT), this lane's metric is concrete and monotone: **theorem files typechecked to exit
0, no sorry/axiom, ledger status flipped.** A run makes progress iff it advances at least one queue
item (a new LEAN-VERIFIED, a LEAN-PARTIAL repaired, or the baseline build re-confirmed green after a
drift). If every queue item is genuinely blocked (e.g. a real mathlib gap), append a dated note here
and escalate — do not manufacture motion. Canon status flips to `verified` still pause for the
maintainer; formalizing and flipping the LEDGER's own row to LEAN-VERIFIED is agent-owned.
