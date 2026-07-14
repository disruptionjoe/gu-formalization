---
artifact_type: exploration
status: process
doc_type: landscape_assessment
created: 2026-07-14
title: "Landscape Assessment After the Three Waves: Full Generative Re-Rank of All Standing Research Paths"
council: "five standing archetypes (orthodox, heterodox-rigorous, commercial, philosopher, wild frontier); reflect -> draft -> drop -> Condorcet"
evidence_base: "the 2026-07-13/14 three-wave results as consolidated by W127 (commit 61937e6): W119-W126, H46B/H46C, H52, Track 2, Yukawa scoping, the 27-row requirements spec"
depends_on:
  - papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md
  - explorations/source-action-requirements-spec-2026-07-13.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - explorations/E2-asymptotic-safety-2026-07-11.md
  - explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md
  - attention/gu_priority_condorcet.py
scope_rule: "research advancement of this repo only; no external-review, submission, methodology-paper, or shipping items (standing rule, Joe 2026-07-11)"
---

# Landscape Assessment After the Three Waves (2026-07-14)

First FULL-LANDSCAPE generative re-rank since the 2026-07-13 three-wave results. Prior re-ranks
compared only the recent shortlist; this pass inventories every standing path, runs the
five-archetype reflect-draft-vote protocol over the enlarged set, and updates the Condorcet
ranker (`attention/gu_priority_condorcet.py`, re-run exit 0). The DE exclusion (H46C) and the
AF-branch tachyon (W122/W123/W126) are treated as EVIDENCE throughout, not re-litigated.

## 1. Inventory and new-evidence impact pass

The three-wave evidence, compressed: (a) a native, tree-unliftable, positive-norm tachyonic
scalaron on the AF branch; (b) dark energy excluded as a CMB-consistently-calibrated distance
model (theta_star re-solve, dAIC +35.78 at GU's own calibration); (c) the source action (H41)
compressed onto ONE blocking object, the covariant operator on Y14, with SA-C4 built and
passing at symbol level; (d) two-loop graded cleanliness at fixed order, with the even-cut
inter-family disagreement (+1 vs 0) and the odd-ghost-cut leak as the surviving price;
(e) the Yukawa no-gos (channel table rigid, non-form carriers forbidden, mod-3
Froggatt-Nielsen provably sterile, hierarchy SILENT); (f) the mu_DW floor cited
(H52: [3.4, 4.7] meV envelope, H36 window EXCLUDED-CITED).

| # | Path | Prior status | Impact | Why |
|---|---|---|---|---|
| 1 | H59/W48 loop positivity: the odd-ghost-cut leak | OPEN | RAISED | W124 resolves the two-loop scalar core and leaves the leak at s > (2m+M)^2 as the precise open price; the leak now IS the loop-positivity question, at sharper resolution than ever. |
| 2 | AF-vs-AS fork (W82 E2; the Reuter branch) | OPEN | RAISED (most) | The tachyon made this the theory's last perturbative escape; W119 concretized the Reuter FP inside a minimal FRG truncation. Also the referee's vulnerability: the tachyon chain rests on ported pure-gravity loop blocks with the AS branch UNCOMPUTED. |
| 3 | Y14 covariant operator (the compressed H41 build) | OPEN | RAISED, E1-flagged | W125 names it as the single object blocking the full build, the loop packet, and SA-G9; SA-C4 passed for the first time. E1/Lakatos watch: the one-object pattern just recurred one level down; naming is a map, not progress. |
| 4 | OQ2: the M^2 ansatz gate on all DE statements | OPEN | RAISED | H46C is exploration-grade at M^2 = 8 only, BAO + theta_star only; OQ2 is now the last gate on a headline falsification instead of a technicality. Referee vulnerability: single-pipeline, OQ2-gated. |
| 5 | Even-cut inter-family disagreement (+1 vs 0) | NEW (W124) | RAISED | The two removal-vs-grading families now disagree on a computable even-cut number: a candidate DISCRIMINATOR, the first internal one the loop program has produced. |
| 6 | W124 Stage C: spin-2 tensor numerators | NEW (W124) | RAISED | The leak verdict is scalar-core only; tensor numerators decide whether it survives spin-2 structure. |
| 7 | c_L background-vs-TT normalization (+ W126 16/3 flag) | OPEN (small) | RAISED slightly | W126 flags a second normalization ratio between the flat-slice and horizontal-sectional chains; signs robust, magnitudes not. Feeds any native loop block. |
| 8 | Thread A chain (A3-A14): native constant-background coefficients for the SA-G rows / OQ2-A | OPEN | UNCHANGED-to-RAISED | Untouched directly, but the waves' method lesson (compute the ported/argued number natively and exactly) is exactly this chain's design; A14's shear gate is the standing block. |
| 9 | H28 remnants: Yukawa texture hooks | OPEN | LOWERED | The no-gos closed most hooks: channel table rigid, non-form carriers forbidden exactly, mod-3 FN sterile for all 27 assignments, hierarchy SILENT. What remains is source-action-gated, i.e. collapses into path 3. |
| 10 | H64: mass hierarchy as the observer's selection | OPEN | LOWERED but sharpened | FN-sterility removes the easiest breaking-mechanism class the question could have used; the question stands with a smaller toolset. |
| 11 | H63: abstract Lawvere no-closure payoff theorem (symmetry-breaking language) | OPEN | UNCHANGED | Needs only the fixpoint-free label-involution, not type-III modular theory; the waves touched neither. H62 (arena/value non-circularity) is FIRMED (W73) and folds in as a lemma. |
| 12 | H61: the PHYSICAL Krein-TT campaign | OPEN | MOOTED | Already walled at type III (W84); W122 then showed the spin-0 object is positive-norm, so there is nothing for a modular grading to grade there, and the decisive physical question moved to the branch fork (path 2). The abstract legs survive in H63. |
| 13 | W83 AS-selection close of the observer spin-0 leg | CONDITIONAL | LOWERED-to-hostage | Its two conditions are now exactly path 2's computation; it has no independent life. |
| 14 | H52: digitize the alpha = 1/3 exclusion | OPEN | RESOLVED by the waves | EXCLUDED-CITED with the resolved mu_DW floor; banked, dropped from ballots. |
| 15 | Track-2 conditional ledger (GU-given-S numbers) | DONE at grade | UNCHANGED (banked) | Extensions (PPN/GW channels via SA-G9) are gated on path 3. |
| 16 | H30: referee-grade statement of the gravity conditional theorem | OPEN | ABSORBED | The W127 consolidation carries the theorem at referee grade inside the flagship; a standalone re-statement adds no research content. Dropped. |
| 17 | DE rescue family (freed amplitude, backreaction, two-fluid, distance-model register) | spent/OPEN | MOOTED | H46C removed the register these lived in; survivors exist only as the OQ2 gate (path 4). |
| 18 | H19-adjacent signature items ((9,5) vs (7,7)) | RETIRED as count-decider | MOOTED (stays retired) | No wave gave the signature a new lever; the Kramers-veto lift remains non-deriving. Not resurrected. |
| 19 | Family-puzzle/H6 follow-ons (mod-3 selector-kind theorem) | BANKED | UNCHANGED | The theorem stands, arena-independent; no new front opened. |
| 20 | Causal-set / order-dimension thread | exploration (low) | UNCHANGED | Chirality bridge closed; the GR/QG axis is a public open problem, not a repo-critical path. |
| 21 | TaF / tri-repo boundary-content leg | OPEN | UNCHANGED | GU owns boundary content in exact mathematics; the waves did not touch the interface. |
| 22 | Firewall-boundary hypothesis (posture-level target) | OPEN | UNCHANGED | If anything mildly corroborated: every residual keeps routing to a boundary-like declaration; still to be attacked, not defended. |
| 23 | Anomaly global leg (Dai-Freed / eta / spin-bordism) | OPEN | UNCHANGED | Y14-operator-gated; collapses into path 3 for any near-term movement. |
| 24 | Shiab selector identity (selection among the >= 8 family) | OPEN | UNCHANGED | Source-action-gated; collapses into path 3. |
| 25 | Gauge-vacuum / su(3,2) sub-block selection | OPEN | UNCHANGED | Source-action-gated; collapses into path 3. |

Impact counts: RAISED 7 (rows 1-7, counting row 8 as unchanged), LOWERED 3 (rows 9, 10, 13),
MOOTED 4 (rows 12, 17, 18; row 16 absorbed), RESOLVED-BANKED 2 (rows 14, 15), UNCHANGED 9.
Retired items reaffirmed retired, none resurrected: chromatic torsion, the (9,5)/(7,7) flip as a
count-decider, the guardian/SUSY hope, the clean-forcing coherence route, the H36 DE-scale
identification. The A-E hunt list from the Willmore arc is closed as a list: A (oracle) done,
B (Lambda-in-the-convention) absorbed into the DeWitt-Lambda arc and the rate reading assessed
false, C (DESI discriminator) discharged in the falsifying direction by H43/H46C, D (Bach
identification) absorbed into the Wave 1-8 arc, E carried forward as the standing E1 watch,
which just fired again at the Y14 operator.

## 2. The five reflections (compact)

Shared facts on the table: both blockbuster negatives (DE, tachyon) came from taking a
ported or argued number and computing it natively and exactly; the E1 watch says the
one-object pattern just recurred at the Y14 operator; and the referee's three residual
vulnerabilities (title strain; the tachyon chain resting on ported pure-gravity loop blocks
with the AS/Reuter branch uncomputed; the DE exclusion being single-pipeline and OQ2-gated)
are each path-shaped.

**Orthodox professor.** LEARNED: the program's only reliable epistemic engine is exact native
computation of previously ported or argued numbers; every other move this month produced maps.
MISSING: the DE exclusion is one pipeline at one M^2; a referee will ask for the band sweep
before accepting "excluded", and we should ask first. INTERESTING: the two-loop fixed-order
sector is now clean enough that finishing it (tensor numerators) is a bounded, standard
computation with a real verdict at the end.

**Heterodox-rigorous professor.** LEARNED: the tachyon is a branch property, not a theory
property; the honest statement of GU's UV standing is per-branch, and one branch is
uncomputed. MISSING: we have never run GU's own field content through the Reuter-branch
scalaron question natively; W83's conditional close and W119's catalogued fork both lean on
ported blocks. INTERESTING: computing the AS branch natively either kills the theory's last
perturbative escape (a clean global negative) or opens the only branch on which GU is
UV-viable and non-tachyonic; either answer is a result, and the playbook that produced both
blockbusters points straight at it.

**Commercial scientist.** LEARNED: cheap decisive computations (H46C was one script) moved
the program more than months of synthesis; buy more of those. MISSING: the OQ2 M^2-band sweep
is the cheapest remaining computation that can flip or harden a headline claim; the tensor
numerators are second. INTERESTING: the even-cut disagreement is the first internally
generated discriminator between the two loop families; a discriminator is worth more than
another consistency pass.

**Philosopher of science.** LEARNED: the E1 rule worked as designed; the residual relocated
(source action to Y14 operator) while nothing was built, and the referee's title-strain
complaint is the same observation from outside. MISSING: nobody has asked whether the
residual is still ONE object: the AF-vs-AS branch choice is a new residual-shaped datum that
is not obviously a row of the 27-row spec, and if it is a second independent residual the
paper's central thesis needs restating as a research matter, not a wording matter.
INTERESTING: turning the even-cut disagreement into a principled selection between grading
and removal families would be a genuine Lakatosian progressive step: novel content, not
accommodation.

**Wild frontier scientist.** LEARNED: the geometry keeps corroborating the ported signs when
computed natively (W126's F(R) matched the ported direction); the native machinery is trustworthy
enough to attempt the real objects. MISSING: the covariant operator on Y14 = Met(X4) is a
genuinely interesting infinite-dimensional geometric object (a propagator on the DeWitt-metric
bundle) that nobody has tried to build head-on; and the odd-cut leak has never been tested
against the optical theorem restricted to the PHYSICAL subspace, which is the only unitarity
that matters physically. INTERESTING: a physical-subspace graded optical theorem would be new
mathematics with reach far beyond GU (all PT/Krein QFT).

## 3. Drafted new hypotheses (from the reflections)

- **H65 - Compute the AS/Reuter-branch scalaron NATIVELY.** The tachyon's last perturbative
  escape, the uncomputed half of the referee's strongest vulnerability, and the sole hinge of
  the W83 conditional close, all one computation: GU's ker-Gamma content in an f(R) + Weyl^2
  FRG truncation at the Reuter FP, native heat-kernel blocks, scalaron mass sign out. Either
  the escape closes (global negative at full strength) or GU acquires its viable branch.
- **H66 - GU-native graviton one-loop block.** Replace the last big ported ingredient (the
  agravity/pure-gravity one-loop beta blocks under the tachyon chain) with a native
  computation on GU's own field content and gimmel conventions; also discharges the W126 16/3
  and c_L background-vs-TT normalization flags. The exact move that produced both blockbusters.
- **H67 - OQ2 M^2-band sweep of the H46C exclusion.** Re-run the theta_star calibration
  across the admissible M^2 band and the ansatz variants; closes the DE exclusion's last gate
  in either direction and retires the single-pipeline vulnerability at the same time.
- **H68 - Build the Y14 covariant operator, time-boxed, build-or-prove-unbuildable.** The
  W125 blocking object (covariant propagator and vertex on the Met(X4) bundle). Run under the
  E1 discipline: the deliverable is the operator or an unbuildability obstruction, not a
  further reduction.
- **H69 - Graded optical theorem on the physical subspace.** Formulate the optical theorem
  restricted to the positive (physical) subspace of the graded theory and test whether the
  odd-ghost-cut leak at s > (2m+M)^2 violates it; the precise open price of keep-and-grade,
  and frontier mathematics independent of GU.
- **H70 - W124 Stage C: spin-2 tensor numerators.** Extend the two-loop overlap/kite cut
  computation beyond the scalar core; decides whether the leak and the even-cut disagreement
  survive tensor structure. Bounded and standard.
- **H71 - The even-cut disagreement as a family discriminator.** Turn the +1 vs 0 inter-family
  even-cut disagreement into a principled selection between the grading and removal families
  (which one's answer is compatible with fixed-order causality/unitarity trades); the loop
  program's first internal discriminator candidate.
- **H72 - Residual-arity audit (the title strain as a research question).** Is the residual
  still ONE object? Formalize the residual as (field-space declaration, coefficients, branch
  choice) and determine whether AF-vs-AS is a derivable consequence of the declared action, a
  28th spec row, or an independent second residual. A structural result either way; also the
  honest response to the E1 recurrence.

Survivors carried into the vote: **H63** (abstract Lawvere payoff theorem, H62 folded in as a
firmed lemma), **H64** (mass hierarchy as observer selection, post-Yukawa-no-gos), **A15**
(the thread-A native constant-background coefficient chain through the A14 shear gate, feeding
the SA-G rows and OQ2-A), **TAFB** (the tri-repo boundary-content leg). Low-tier survivors
below the ballot cutoff, carried but not voted (all either dormant or collapsing into H68):
family-puzzle follow-ons (banked), causal-set axis, anomaly global leg, shiab selector,
gauge-vacuum selection, firewall-boundary posture target.

## 4. Dropped / mooted (explicit)

- **H52** dropped: RESOLVED by wave 32 (EXCLUDED-CITED, mu_DW floor [3.4, 4.7] meV). Banked.
- **H61 (physical Krein-TT campaign)** dropped as mooted: the type-III wall (W84) stands, and
  W122's positive-norm verdict moved the decisive physical question to the branch fork (H65).
  The abstract content lives on inside H63.
- **H62** dropped as resolved: FIRMED non-circular (W73); folded into H63 as a lemma.
- **H30** dropped as absorbed: the W127 flagship consolidation carries the conditional theorem
  at referee grade.
- **DE rescue family** mooted by H46C: freed-amplitude, backreaction, two-fluid, and
  distance-model registers are closed as evidence; only the OQ2 gate (H67) remains.
- **Retired list reaffirmed, none resurrected:** chromatic torsion; the (9,5)/(7,7) signature
  flip as a count-decider; the guardian/SUSY hope; the clean-forcing coherence route; the H36
  DE-scale identification.

## 5. Condorcet vote and final ranking

Ballots updated in `attention/gu_priority_condorcet.py` (documented format, edited in place;
re-run `python attention/gu_priority_condorcet.py`, exit 0). Twelve items voted: H63, H64,
A15, TAFB, H65-H72.

Per-archetype ballots (best first):

| archetype | ballot |
|---|---|
| orthodox | H67, H70, H66, H65, H69, A15, H68, H71, H72, H63, H64, TAFB |
| heterodox-rigorous | H65, H66, H68, H67, H69, H70, H71, H72, A15, H63, H64, TAFB |
| commercial | H67, H65, H64, H71, H66, H70, H68, A15, H72, H69, TAFB, H63 |
| philosopher | H72, H71, H65, H67, H63, H69, H66, H68, H64, A15, TAFB, H70 |
| wild frontier | H68, H66, H69, H65, H63, H71, H70, H72, A15, H64, TAFB, H67 |

Script output (re-run 2026-07-14, exit 0): **Condorcet winner H65** (beats every other item
pairwise across the five archetypes); full Copeland order H65 (+11), H67 (+9), H66 (+7),
H68 (+5), H69 (+3), H71 (+1), H70 (-1), H72 (-3), A15 (-5), H63 (-7), H64 (-9), TAFB (-11).

**Final ranked list (top 10, per the script's Copeland order):**

1. **H65 - AS/Reuter-branch scalaron, computed natively.** The tachyon's last perturbative
   escape and the referee's strongest vulnerability, one computation; Condorcet winner.
   (#1 for heterodox-rigorous.)
2. **H67 - OQ2 M^2-band sweep of the DE exclusion.** Cheapest computation that can flip or
   harden a headline claim; retires the single-pipeline gate. (#1 for orthodox AND commercial.)
3. **H66 - GU-native graviton one-loop block.** The compute-the-ported-number-natively
   playbook applied to the last big ported block under the tachyon chain; also discharges the
   normalization flags.
4. **H68 - Build the Y14 covariant operator (build-or-prove-unbuildable, time-boxed).** The
   single blocking object of the source-action program, run under the E1 discipline.
   (#1 for wild frontier.)
5. **H69 - Graded optical theorem on the physical subspace.** The precise form of the open
   loop-positivity price; frontier mathematics with reach beyond GU.
6. **H71 - Even-cut disagreement as family discriminator.** The loop program's first internal
   discriminator candidate; a progressive-step opportunity, not another consistency pass.
7. **H70 - Spin-2 tensor numerators (W124 Stage C).** Bounded, standard, verdict-bearing:
   does the odd-cut leak survive tensor structure?
8. **H72 - Residual-arity audit.** Is the residual still one object, or did the branch fork
   make it two? Structural result either way. (#1 for philosopher.)
9. **A15 - Thread-A native background-coefficient chain (A14 shear gate).** Supplies SA-G
   rows source-first; the native-computation pattern's standing home in the gravity sector.
10. **H63 - Abstract Lawvere no-closure payoff theorem.** The GU-independent credibility
    result that survives the type-III wall; H62 firmed as its lemma.

Below the cut: H64 (11th; sharpened but tool-poor after FN-sterility) and TAFB (12th;
cross-repo-gated). Both stay open.

## 6. What changed about the program's shape

The program has stopped being a narrowing exercise and become a fork-resolution exercise. For
two weeks every pass reduced freedom toward "one unbuilt object"; the three waves instead
produced two hard computed negatives (DE excluded in every tested register; a native tachyon
on the AF branch) plus a sharper map, and in doing so they relocated the live frontier from
the residual itself to three named forks that are each computable: which UV branch (AF with
the tachyon vs the uncomputed Reuter branch), which loop family (grading vs removal, now
separated by a computable even-cut number), and whether the DE exclusion survives its own OQ2
gate. The method lesson is equally structural: every state-changing result of the arc came
from computing a ported or argued number natively and exactly, and the top of this ranking is
simply that playbook pointed at the three ported numbers that remain (the Reuter-branch
scalaron, the graviton loop block, the M^2 band). The E1 watch stands: the Y14 operator is
the residual's new name, and building it (or proving it unbuildable) is the only move at that
address that counts as progress.
