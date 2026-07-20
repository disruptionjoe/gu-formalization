---
title: "Hardening H2 (gap G-A4): Lean formalization of the co-flip core — sorry-free, axiom-free, in the default target"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (hardening swing H2, gap G-A4)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/blockbuster-p3-one-bit-dossier-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - tests/channel-swings/ch_rec_coflip_probe.py
  - explorations/blockbuster-p3-one-bit-dossier-2026-07-19.md
  - explorations/hardening-h1-exhaustiveness-2026-07-19.md
runnable:
  - Lean/GUFormalization/CoflipCore.lean (via lab/automation/check-lean.ps1)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Hardening H2: the co-flip core in Lean 4 (gap G-A4)

The dossier's G-A4 called the finite co-flip and split-costs-one propositions
"Lean-amenable" and priced them as the credibility doubler. This swing delivers
`Lean/GUFormalization/CoflipCore.lean`: a **sorry-free, new-axiom-free** Lean 4 +
mathlib module, wired into the repo's default `lake build` target, machine-checking
the minimal finite core of P1 (co-flip / zero-import diagonal) and P2
(split-costs-one), plus the (1,1) instances of H1's rigidity lemmas L1/L2, the
split-parity identity `sigma·d = mu`, and the charge action of H1's benign miss F.

Everything is conditional work under the standing axiom at R0_COND working grade.
No claim-status, canon-verdict, or public-posture moves; no external actions; files
written: the Lean module, one import line in `Lean/GUFormalization.lean`, one row in
`Lean/README.md`, and this document.

---

## 0. Five-lens council (inline, before execution)

**Lens 1 — Lean/mathlib expert.** *Approach:* mirror the repo's existing Lean
conventions (`import Mathlib`, `set_option autoImplicit false`, namespace
`GUFormalization`); mathlib is already provisioned and built in `.lake/packages`, so
a full-Mathlib import costs one elaboration pass and buys `ring`, `linarith`,
`positivity`-class tactics and the `Int.units_*` API. *Trap:* `decide` over
`ZMod 2`/`ℤˣ` quantifications is brittle across mathlib versions; prefer explicit
case-bashing via `Int.units_eq_one_or`. (Fired in practice: `Xor'` is deprecated in
the pinned mathlib — caught by grepping the package before building.)

**Lens 2 — Finite-group formalizer.** *Approach:* present the operation set
multiplicatively as `ℤˣ⁴` — each coordinate an involution, so this IS `(ℤ/2)⁴` —
acting componentwise on configurations, and make "finite group action" a proven
`MulAction` instance, not a label. *Trap:* stipulating the generators' actions on
the observables directly would make P1 vacuous; the diagonal action must be derived
from a concrete Krein structure where sector sign and register direction are
computed.

**Lens 3 — Proof engineer (minimal-dependency bias).** *Approach:* signature (1,1)
over ℚ suffices for the co-flip core — pairs of rationals, no `Matrix`, no `Fintype`
gymnastics; the probe's (2,2) block structure exists only to make dynamics
nontrivial, and dynamics can be abstracted by quantifying over arbitrary
nonnegative-charge trajectories, which subsumes both time directions and any
Krein-unitary at once (T-inertness becomes a corollary, strictly stronger than the
probe's check — this is exactly H1's Corollary C1 shape). *Trap:* porting the
probe's `Fraction`-matrix arithmetic verbatim (determinants, leading minors) is a
time sink with zero extra content.

**Lens 4 — Skeptical auditor (no axioms, no sorry).** *Approach:* every load-bearing
definitional identification needs a justifying theorem: `dir c := mu·eps` gets a
uniqueness lemma (the only sign u with `u·(register final) > 0`), `sector c := eps`
gets G-definiteness of the selected subspace in every gauge, relabel-triviality is
an invariance proof, and the probe's [F] controls (partial-relabel rejection,
mu-import detection) are formalized too. *Trap:* silent overclaim — the file must
not claim inventory exhaustiveness for the full construction (that is H1's theorem
at class grade, and G-A2's open question at cohomological grade); mathlib's standard
axioms (propext, Classical.choice, Quot.sound) are fine, `axiom`/`sorry` are not.

**Lens 5 — Expositor.** *Approach:* the file reads top-down as Part A (concrete
Krein toy: form, fundamental-symmetry gate, projector, charge, register) then Part B
(operation group, justified observables, P1/P2/P3 theorems), with docstrings tying
each theorem to the probe check and dossier proposition it formalizes. *Trap:*
docstring overclaim — say "finite (1,1) instance," never "C_0 in general."

**Chair synthesis (executed):** (1) fresh default-target build baseline through the
required host-local wrapper FIRST (standing Lane 3 integrity step); (2) write
`CoflipCore.lean` per the two-part architecture; (3) rebuild through the wrapper;
wire into the default target since the baseline works; (4) align admissibility with
H1's doc — which materialized in parallel during the swing and was read and aligned
to mid-flight; (5) this document.

---

## 1. Build baseline and receipts (Lane 3 integrity step)

All builds ran through the required host-local wrapper
`lab/automation/check-lean.ps1` (exclusive CapacityOS temp lock, then `lake build`).
Toolchain `leanprover/lean4:v4.32.0-rc1`, mathlib prebuilt in `.lake/packages`.

1. **Baseline (pre-change):** exit 0, `Built GUFormalization`, 8641 jobs, default
   target green. Only pre-existing benign linter warnings
   (`LocatedNotForcedLegs.lean` unused-variable/unused-simp-arg). Fresh baseline
   established as PROOF-STABLE-KERNELS' next_swing requires.
2. **Round 1 (module added, pre-fix snapshot):** exit 1 with exactly one error — a
   type mismatch in `witness_restored` (an `at`-rewrite of `c.mu = 1` leaked into
   the register argument). Every other declaration in the module elaborated clean on
   first contact. Fixed by rewriting the goal side first.
3. **Round 2 (final):** **exit 0**, `Built GUFormalization.CoflipCore (410s)`, 8642
   jobs. No errors, no `sorry` diagnostics (`declaration uses 'sorry'` appears
   nowhere in the log). Two benign linter warnings remain (unused simp arguments in
   one branch each of the four-way case split in `splits_iff` — an artifact of
   `<;> simp [...]` sharing one lemma list across branches).

Static hygiene: the only occurrences of the tokens `sorry`/`axiom` in the file are
inside documentation comments; no `axiom` declarations, no `sorry` terms. The
module is imported by `Lean/GUFormalization.lean` and is therefore part of the
default `lake build` target from now on. `Lean/README.md`'s certificate table has a
new row pointing here as owner surface.

---

## 2. What is formalized, sorry-free (the theorem list)

File: `Lean/GUFormalization/CoflipCore.lean`, namespace
`GUFormalization.CoflipCore`. Architecture: **Part A** derives the observables from
a concrete finite Krein structure; **Part B** proves the co-flip package over the
operation group. Nothing observable is stipulated: `sector` and `dir` each carry a
specification/uniqueness theorem grounding them in Part A.

### Part A — the (1,1) Krein toy over ℚ (rigidity, derived)

- `charge_spec` — structure lemma: in every gauge the projector selects one
  coordinate line and the charge is the square of the retained coordinate.
- `charge_nonneg`, `sector_definite` — the (1,1) instance of H1's L1/L2 rigidity:
  charge is nonnegative always, strictly positive on nonzero selected vectors; the
  selected sector is form-definite with sign `eps` in BOTH gauges.
- `relabel_charge_invariant` — the full covariant relabel (form, symmetry, state
  transported together) is invisible to the charge: anchor exchange is gauge.
- `total_flip_charge` — H1's benign miss F at (1,1) scale: flipping (G, J) without
  transporting the state stays admissible and exchanges the charge with the
  mirror-sector charge (`q ∘ F = q(−eps)`); the signed observables are F-inert.
- `fundamental_symmetry_gate`, `partial_relabel_rejected` — the admissibility gate:
  `G·J` positive definite in every matched presentation; the partial-relabel attack
  (flip J, keep G) produces a strictly negative witness and exits the class.
- `register_eq_sum`, `register_direction`, `direction_unique` — the register's
  closed form; on ANY trajectory with positive total charge the final sign is
  `mu·eps`, and that sign is unique. The arbitrary-trajectory quantifier subsumes
  both time directions and any dynamics (H1's C1 shape).
- `vacuum_charge_zero`, `vacuum_unwitnessed`, `unit_state_charge_pos` — the vacuum
  carries zero charge and an orientation-independent identically-zero register
  (dossier P10's "one absence seen twice," finite shadow); the unit state is the
  standing positive witness.

### Part B — the operation group and the co-flip theorems

- `Op := ℤˣ × ℤˣ × ℤˣ × ℤˣ` with generators `E, M, T, Rl`; `op_mul_self` (every
  element an involution); `act` with a proven `MulAction Op Cfg` instance.
- `sector`, `dir`, `importCost`, `zeroImport` — with justification theorems
  `sector_spec`, `dir_spec`, `dir_unique`, `witness_restored`.
- `split_parity` — H1 alignment: `sector c * dir c = c.mu` — the import bit is
  itself an observable, the split parity of the pair.

The main theorems, as written in Lean:

```lean
theorem coflip (c : Cfg) : sector (act E c) = -sector c ∧ dir (act E c) = -dir c

theorem zeroImport_diagonal (g : Op) (hg : zeroImport g) (c : Cfg) :
    (sector (act g c) = sector c ∧ dir (act g c) = dir c) ∨
    (sector (act g c) = -sector c ∧ dir (act g c) = -dir c)

theorem timeReversal_inert (c : Cfg) :
    sector (act T c) = sector c ∧ dir (act T c) = dir c

theorem relabel_inert (c : Cfg) :
    sector (act Rl c) = sector c ∧ dir (act Rl c) = dir c

theorem zeroImport_arrow_flip_forces_sector_flip (g : Op) (hg : zeroImport g)
    (c : Cfg) (h : dir (act g c) = -dir c) : sector (act g c) = -sector c

def splits (g : Op) (c : Cfg) : Prop :=
  Xor (sector (act g c) = -sector c) (dir (act g c) = -dir c)

theorem splits_iff (g : Op) (c : Cfg) : splits g c ↔ g.m = -1

theorem no_zeroImport_split (g : Op) (c : Cfg) (hg : zeroImport g) : ¬ splits g c

theorem split_costs_one (g : Op) (c : Cfg) (hc : importCost c = 0)
    (hs : splits g c) : importCost (act g c) = 1

theorem M_splits (c : Cfg) :
    splits M c ∧ sector (act M c) = sector c ∧ dir (act M c) = -dir c

theorem split_factorization (g : Op) (c : Cfg) (hs : splits g c) :
    ∃ g0 : Op, zeroImport g0 ∧ g = M * g0

theorem one_bit_accounting (g : Op) (c : Cfg) :
    (zeroImport g ↔ ¬ splits g c) ∧
    (splits g c ↔ g.m = -1) ∧
    (splits g c → ∃ g0 : Op, zeroImport g0 ∧ g = M * g0)

theorem split_parity (c : Cfg) : sector c * dir c = c.mu
```

Admissibility, generated-group form (Section 3's alignment anchor):

```lean
theorem zeroImport_iff_mem_ker (g : Op) : zeroImport g ↔ g ∈ recordChar.ker

theorem zeroImport_iff_generated (g : Op) :
    zeroImport g ↔ g ∈ Subgroup.closure ({E, T, Rl} : Set Op)

theorem inventory_generates (g : Op) :
    g ∈ Subgroup.closure ({E, M, T, Rl} : Set Op)
```

End-to-end instances (Part A driving Part B, nothing stipulated):

```lean
theorem concrete_direction (c : Cfg) :
    0 < sv (dir c) * register c.mu c.eps [charge c.gauge c.eps (1, 1)]

theorem concrete_coflip (c : Cfg) :
    dir (act E c) = -dir c ∧ sector (act E c) = -sector c ∧
      0 < sv (dir (act E c)) *
        register (act E c).mu (act E c).eps
          [charge (act E c).gauge (act E c).eps (1, 1)]
```

Reading of the package: `coflip` + `zeroImport_diagonal` is P1 at machine-checked
grade over the whole (ℤ/2)⁴ inventory group (not 16 sampled composites);
`splits_iff` + `split_costs_one` + `split_factorization` + `one_bit_accounting` is
P2 — decoupling requires one additional ℤ/2 datum, that datum is always the same
bit, and the import counter is an observable (`split_parity`); `timeReversal_inert`
+ `zeroImport_arrow_flip_forces_sector_flip` is P3's sharp form.

**Nothing is pending inside the module:** every declaration in the file is
sorry-free and compiled in the green default-target build. What is *not yet
formalized* is scoped in Section 4.

---

## 3. H1 alignment (the admissibility definition)

The swing instruction said to align with H1's exhaustiveness doc if it existed.
It did not exist at swing start and materialized in parallel
(`explorations/hardening-h1-exhaustiveness-2026-07-19.md`); it was read and aligned
to mid-flight:

- **Quantifier relation.** H1's admissibility is strictly weaker — arbitrary
  partial maps between admissible configurations of the general-(p,q) envelope
  class — and its Theorems A/B derive diagonality from rigidity lemmas L1/L2 alone.
  This file's operation notion is the generated group `(ℤ/2)⁴` (proven:
  `inventory_generates`), with zero-import = kernel of the record-law character =
  subgroup generated by `{E, T, Rl}` (`zeroImport_iff_mem_ker`,
  `zeroImport_iff_generated`). Both notions agree on what they share; the Lean
  module machine-checks the group form and the (1,1) instances of L1/L2 that power
  H1's proofs.
- **Split parity.** H1's headline identity `sigma·d = mu` is formalized verbatim as
  `split_parity`.
- **The benign miss F.** H1's standalone total form flip `(G, J) → (−G, −J)` is
  formalized at (1,1) scale as `total_flip_charge`: admissible, charge-exchanging
  (`q ∘ F = mirror charge`), signed-observable-inert.
- **P3 upgrade shape.** `register_direction` quantifies over arbitrary charge
  trajectories — the same move as H1's Corollary C1 (propagator independence),
  of which dynamics-reversal inertness is the special case.

---

## 4. What remains for a full formal note (scoped, honest)

1. **General-(p,q) abstract class (H1 §7 item 4, the named G-A4 remainder).** Lift
   L0 (spectral decomposition of admissibility), L1, L2 and Theorems A/B to the
   abstract envelope class in Lean: finite-dimensional real bilinear forms,
   `J`-eigenspace decomposition, Sylvester — all in mathlib's range
   (`LinearAlgebra.QuadraticForm`, `Module.finrank`), but a genuinely larger lift
   than this swing. The present module is the (1,1) instance plus the full
   observable-shadow theorems; a smaller sorry-free theorem beat a bigger sorried
   one, per the swing's own rule.
2. **H1's all-partial-maps quantifier in Lean.** Once the abstract class exists,
   H1's Theorem A quantifier ("any map between zero-import witnessed instances") is
   a two-line corollary of the lifted L1/L2 — the hard content is item 1.
3. **Connectedness/continuum statement (H1 §4.3).** The contractibility of the
   fundamental-symmetry space (angle-operator convexity) is formalizable but
   analysis-adjacent; lowest priority of the three.
4. **Not a Lean target:** T3/P9 membership of GU's built W229 law (an audit of
   external artifacts, per the dossier: "the audit is a methodology, not a
   formalization target"), and the cohomological grade G-A2 (open mathematics
   first, formalization later).
5. **Housekeeping (cheap, next Lean touch):** silence the two unused-simp-arg
   linter warnings in `splits_iff`; the PROOF-STABLE-KERNELS next_swing items not
   in this swing's scope (folding `tests/big-swing/R4_TwoArena.lean` into the
   default target; retiring the un-typechecked A1 draft duplicate) remain queued.

---

## 5. Boundary

Conditional work under the standing axiom, R0_COND working grade. Lean verifies
deduction from explicit premises: this module machine-checks the finite kernel of
P1/P2/P3 and nothing more. It does not prove that the premises are GU's physical
realization; membership of the built W229 law (T3/P9, D1/D2) carries the external
risk exactly as before. No claim-status, canon-verdict, scorecard, register, or
public-posture moves. Files written this swing:
`Lean/GUFormalization/CoflipCore.lean` (new), `Lean/GUFormalization.lean` (one
import line), `Lean/README.md` (one certificate row), this document. Builds ran
only through the required host-local wrapper; no git operations; no cross-repo
writes; no external actions.
