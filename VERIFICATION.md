# VERIFICATION -- what is proved, what is computed, what is conjectural

Outsider entry point. This program uses internal labels ("theorem-grade", "closed", "confirmed"); this file
exists so you do NOT have to trust them. It classifies the flagship results into three honesty levels, gives each
a compact verification package, and states plainly what would falsify the leading interpretations. Companion to
`REPRODUCE.md` (how to run the tests) and the long-form audit in
`explorations/obj6-verification-package-2026-07-11.md`.

## The three levels

- **L1 PROVEN MATHEMATICS** -- established exactly from stated assumptions; the proof does not depend on any
  numerical run.
- **L2 COMPUTED MODEL RESULT** -- demonstrated in a specific finite model / numerical calculation / RG
  truncation; regulator/scheme/truncation caveats apply.
- **L3 PHYSICAL INTERPRETATION** -- connects an L1/L2 result to Geometric Unity or to nature; the most
  conjectural level.

## Flagship results

| # | Claim | Level | Confidence | Reproduce | Strongest objection (conceded) |
|---|---|---|---|---|---|
| a | **Diagonal self-valuation theorem:** if a set `B` admits a fixed-point-free endomap, no map `T : A × A -> B` is weakly point-surjective; for inhabited `A`, no valuation `p : A -> B` is invariant under that endomap. More generally, invariance under a group action is equivalent to the image of `p` lying in the common fixed-point set. | **L1** (math) / L3 (optional observer reading) | math HIGH; observer reading LOW | `Lean/GUFormalization/ResidualSelection.lean` (proof); `tests/W99_theorem_finite_instances.py` (confirmation only); paper `papers/candidates/observer-value-selection-theorem/` | "This is Cantor-Lawvere plus an elementary fixed-point observation." CONCEDED -- self-graded NOVEL-PACKAGING (b); novelty is the explicit synthesis and controls, not a new fixed-point theorem. |
| b | **UV structure:** GU/4th-order+ker-Gamma-RS is renormalizable + asymptotically free/safe; unitary at tree/algebraic grade (+ a machine-checked no-local-positive-metric theorem); loop positivity OPEN; the ghost is genuinely kept (HORN K). | **L2** (truncation-conditional) | MEDIUM-HIGH (model); UV completion OPEN | `tests/W44,W45-47,W48-54,W81,W83,W87,W88,W95-97` | "No complete two-loop RGE fixes sign(eta_C)." CONCEDED -- the horn is scheme-conditional (CONTROLLED-EXCEPT-ETAC); loop unitarity is an open positivity-vs-causality trade. |
| c | **Generation count:** located-not-forced -- multiplicity is natively 3 (a representation dimension); the net chiral count is interior-even / net-0 (2-primary, a class-wide no-go) and external-by-structure (the external count is any integer -- flux number / Aharonov-Casher); the only unconditionally computable integer is 1; "3" over "1" is NOT derived (requires an observer/symmetry-breaking selection). | **L1** cores (one Lean-verified); "3" is L3 OPEN | cores HIGH; "3" OPEN | `tests/W55-W60` | "Hom(Z/3,Z)=0 means you surrender the count; only the honest integer is 1." CONCEDED -- it is a no-go that LOCATES, not a derivation of 3. |
| d | **Sectorial-closure BREAK (retraction):** the "physical modular realization closes sectorially" claim was FALSE -- a genuine finite spacetime region is type III_1 / infinite-rank, so under a physical interaction no coherent net of bounded modular conjugations exists (an IFF-no-go with an explicit falsification boundary, condition X = UV-soft coupling). | L2 (reconstruction) | MEDIUM-HIGH | `tests/W98,W100_obj2` | "A region is not a cutoff." This IS the program's own break -- included as the credibility anchor: the program retracts honestly. |
| e | **Observer Structure Theorem (model grade):** under one unified assumption set, on the W98 Krein tower class: (1) an observer's complete one-sided physics (incl. the value-selection cocycle) is finite per-state on a sharp state class, needing NO modular conjugation; (2) the interface obstruction is a grading-relative invariant whose classes form a presheaf WITH a global section (cocycle holds on triple overlaps) -- a global CLASS exists while no global OPERATOR does; (3) no bounded conjugation exists at any level, located ([C]=2[P]) and typed, and the absence is FACTORIZATION-INVARIANT (square-root rigidity). The mixing-direction assumption is DERIVED-conditional (interaction-universality). All mathematical clauses are horn-independent class-statements. | **L2** (model-grade theorem; NOT continuum) | MEDIUM-HIGH; lifts named (Weinberg transfer, skeleton-grade vertex uniqueness, HORN K for membership) | `tests/W109` (composed) + `W105-W108, W110-W112` | "A conjunction of separately-tuned toys" -- answered by the single-instance joint verification + 18/18 sweep; "second reframe of a retracted claim" -- conceded and distinguished: every clause survived pre-registered kill-modes, and the theorem asserts the ABSENCE of the conjugation (W94 negated, not repaired). Prior-art framing per W112: the new content is the exact identification of the wall-carrying grading-sensitive object, inside an existing graded-invariants field. |

## What is proved / computed / imported / conjectural

- **PROVED (L1):** flagship (a) as pure set-level math; several (c) cores (incl. a Lean-checked CRT
  split); the no-local-positive-metric theorem (free case).
- **COMPUTED (L2):** all FRG/UV results (one-loop + ker-Gamma projector + partly ported agravity betas); the
  sectorial IFF-no-go; the source-action skeleton (O5).
- **IMPORTED (cited, not re-derived):** standard higher-derivative-gravity betas (Fradkin-Tseytlin/
  Avramidi-Barvinsky/agravity); the Reuter fixed point + matter bounds (Reuter-Saueressig/Dona-Eichhorn-Percacci);
  Tomita-Takesaki / Bisognano-Wichmann / Shulman / Gottschalk; Lawvere/Yanofsky; DESI DR2 numbers.
- **CONJECTURAL (L3):** "the source action IS the observer" as a physical statement (the modular-conjugation
  realization is WALLED, see (d)); GU housing the Standard Model beyond gauge-group grade; the value of the
  generation count; that GU is on HORN K unconditionally (truncation-conditional).

## What would falsify the leading interpretations

- Flagship (a) physical reading: already broken at the modular-realization level (d). The ABSTRACT theorem is not
  falsifiable by physics (it is math); its physical relevance is.
- Flagship (b) HORN K: a complete two-loop-with-graviton EH x Weyl RGE giving eta_C > 0 in the physical
  (Weyl-adapted) scheme would flip to HORN Q (removable ghost) -- see `explorations/obj4-uv-scheme-stability`.
  Under HORN Q, flagship (e)'s mathematics survives unchanged (class-statements); only GU's MEMBERSHIP in the
  wall class narrows.
- Dark energy (in the one-residual flagship): the current honest register after the W113 joint-profile
  correction -- the shape AND the canonical f_0 = 0.125 are both viable on the DESI DR2 BAO likelihood (the old
  "f_0 tension" was a fixed-amplitude-slice artifact); the sector's ONE residual exclusion is an
  amplitude-calibration direction (+1.81% vs Planck). A future BAO amplitude calibration confirming the Planck
  value at sub-percent precision would exclude it; the CPL-level falsification (H43/H44) stands regardless.
- The observer conjecture's "wall becomes prediction" move: the pre-registered fork
  (`explorations/obj3-adversarial-fork-preregistered`) landed on Outcome B (wall remains); the exact evidence that
  would reverse it to A/C/D is listed there.

## Honesty boundary
The program's leading PHYSICAL story (source action = observer) is NOT established: its rigorous modular
realization broke (d), and its status is mechanism-genuine + abstract-theorem-proven + value-selection-realized-
algebraically, with the full firewall-as-modular-conjugation WALLED. The durable, externally-attackable results
are (a) the abstract theorem, (b) the UV structural map (truncation-conditional), (c) the interior-even /
external-by-structure count no-go, and (d) the honest break. Trust the levels, not the adjectives.
