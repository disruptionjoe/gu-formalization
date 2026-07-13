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
| a | **Observer/value-selection theorem:** a self-referential arena with a fixpoint-free two-valued admissibility grading admits no symmetric total valuation; any committed valuation breaks the symmetry, and (non-circular partition) the forced residual is a value. | **L1** (math) / L3 (physical reading) | math HIGH; physical reading LOW | `tests/W70,W73,W99` (confirmation, not proof); paper `papers/candidates/observer-value-selection-theorem/` | "Just Cantor-Lawvere + Curie in costume." CONCEDED -- self-graded NOVEL-PACKAGING (b); novelty is the synthesis, not a new fixed-point theorem. |
| b | **UV structure:** GU/4th-order+ker-Gamma-RS is renormalizable + asymptotically free/safe; unitary at tree/algebraic grade (+ a machine-checked no-local-positive-metric theorem); loop positivity OPEN; the ghost is genuinely kept (HORN K). | **L2** (truncation-conditional) | MEDIUM-HIGH (model); UV completion OPEN | `tests/W44,W45-47,W48-54,W81,W83,W87,W88,W95-97` | "No complete two-loop RGE fixes sign(eta_C)." CONCEDED -- the horn is scheme-conditional (CONTROLLED-EXCEPT-ETAC); loop unitarity is an open positivity-vs-causality trade. |
| c | **Generation count:** located-not-forced -- the count is forced to {1,3} and 3-primary (a class-wide no-go theorem); "3" over "1" is NOT derived (requires an observer/symmetry-breaking selection). | **L1** cores (one Lean-verified); "3" is L3 OPEN | cores HIGH; "3" OPEN | `tests/W55-W60` | "Hom(Z/3,Z)=0 means you surrender the count; only the honest integer is 1." CONCEDED -- it is a no-go that LOCATES, not a derivation of 3. |
| d | **Sectorial-closure BREAK (retraction):** the "physical modular realization closes sectorially" claim was FALSE -- a genuine finite spacetime region is type III_1 / infinite-rank, so under a physical interaction no coherent net of bounded modular conjugations exists (an IFF-no-go with an explicit falsification boundary, condition X = UV-soft coupling). | L2 (reconstruction) | MEDIUM-HIGH | `tests/W98,W100_obj2` | "A region is not a cutoff." This IS the program's own break -- included as the credibility anchor: the program retracts honestly. |

## What is proved / computed / imported / conjectural

- **PROVED (L1):** flagship (a) as pure set/category-theoretic math; several (c) cores (incl. a Lean-checked CRT
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
- The observer conjecture's "wall becomes prediction" move: the pre-registered fork
  (`explorations/obj3-adversarial-fork-preregistered`) landed on Outcome B (wall remains); the exact evidence that
  would reverse it to A/C/D is listed there.

## Honesty boundary
The program's leading PHYSICAL story (source action = observer) is NOT established: its rigorous modular
realization broke (d), and its status is mechanism-genuine + abstract-theorem-proven + value-selection-realized-
algebraically, with the full firewall-as-modular-conjugation WALLED. The durable, externally-attackable results
are (a) the abstract theorem, (b) the UV structural map (truncation-conditional), (c) the {1,3} no-go, and (d)
the honest break. Trust the levels, not the adjectives.
