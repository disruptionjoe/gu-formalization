---
artifact_type: exploration
status: exploration
created: 2026-07-12
wave: 18
title: "H34 -- predictive-content audit of the one-residual flagship: an adversarial skeptic's pass classifying every material claim as PREDICTION / FIT / CONDITIONAL / LOCATED-NOT-FORCED / HOUSING / STANDING FALSIFIER. Honest headline count: ZERO parameter-free predictions; 4 free parameters; the accommodation framing is honest and if anything the one-residual thesis is the only genuinely novel positive."
grade: "AUDIT (no new derivation; a sorting pass over the built Wave 1-17 / one-residual picture). Arithmetic the ledger leans on is reproduced deterministically in tests/wave18/H34_parameter_count.py (exit 0, 13/13). All grades are cited to the wave writeup or test that computed them; none imported."
depends_on:
  - papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md
  - explorations/predictive-boundary-audit-2026-07-12.md
  - explorations/wave1/H3-desi-verified-and-intersection-2026-07-11.md
  - explorations/wave8/H23-source-action-construction-2026-07-11.md
  - explorations/wave16/H39-sourceaction-kclass-2026-07-11.md
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - tests/wave18/H34_parameter_count.py
scripts:
  - tests/wave18/H34_parameter_count.py
---

# H34 -- Predictive-content audit of the one-residual flagship

Purpose: be the hostile-but-fair referee. Of every material claim in the flagship
(`papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md`),
ask one question: is this a genuine parameter-free PREDICTION, or is it tuned, assumed, located,
merely housed, or a live negative? This audit does not advance GU; it measures it. Conservatism rule:
when in doubt a claim is HOUSING or FIT, never PREDICTION. Over-counting predictions is the exact
failure this pass exists to prevent.

Classification scheme (each material claim gets exactly one):
- **PREDICTION** -- falsifiable, parameter-free, emitted source-first; GU would be WRONG if not observed.
- **FIT** -- matched only by tuning a named free parameter.
- **CONDITIONAL** -- true modulo a named postulate (forced / leaning / free).
- **LOCATED-NOT-FORCED** -- structurally present in the built (9,5) but not derived.
- **HOUSING** -- GU can contain the structure but does not predict it (consistent-with).
- **STANDING FALSIFIER** -- a live negative that could kill GU as it stands.

## The ledger

### Sector: Gravity

| Claim | Class | Free params | What would falsify | Verdict |
|---|---|---|---|---|
| Tree-level Stelle-clear: induced EH `R^X` + `Weyl^2` + DeWitt `Lambda` | CONDITIONAL (modulo soldering `A=spin-lift(grad^gimmel)`, a genuine postulate per H27; + `mu_DW`) | `mu_DW` (1, free) | A forced soldering that lands off the spin-lift; or loop ghost non-unitarity | Real conditional theorem, but the condition is an unforced codim-8165 postulate; not a prediction |
| Massive-ghost sign healthy, `C_RY` computed POSITIVE two ways (`m^2_eff=1/2+C_RY>1/2`) | CONDITIONAL (same soldering); the sign itself is a genuine COMPUTED result (H25) | 0 for the sign; `mu_DW` for the absolute mass | `C_RY<-1/2` (it is not) | Strongest internal gravity computation; sign is real and non-tuned, but only meaningful given the soldering |
| Exact Schwarzschild/Kerr Bach-flat at all orders (H1) | HOUSING (a property of GR vacua, not a GU prediction) | 0 | n/a (it is a theorem about the vacua) | True and reproducible, but it is background math GU inherits, not a GU consequence |
| Krein ghost-parity `[P,S]=0` clears the ghost (Bateman-Turok, tree) | CONDITIONAL + explicitly SIGN-BLIND (H23 C) | 0 | Loop-level `[P,S]=0` failure | Buys tree positivity; does NOT select anything; loop level OPEN |
| `mu_DW ~ M_Pl` (Planckian, decoupled ghost) | FIT / smuggled (H24 BAR 2) | `mu_DW` (1) | n/a until derived | The natural value is asserted, not derived |

### Sector: Dark energy / DESI

| Claim | Class | Free params | What would falsify | Verdict |
|---|---|---|---|---|
| GU shares DESI's `w_a<0` SIGN / correct quadrant | FIT (sign of a fitted, window-dependent CPL of a free-`f0` family) | `f0`, `M2`, `B_i` | already near-excluded jointly (below) | Sign-only, LCDM-amplitude-degenerate; not a prediction |
| GU "nails" `w0` (`-0.768` vs `-0.752`, `-0.28 sigma`) | FIT (the same `f0` family; `w0` is where the family happens to sit) | `f0` | a `w0` far from DESI at all `f0` | Good marginal agreement but on a tuned family, not emitted source-first |
| GU under-evolves `|w_a|` (~0.27 vs ~0.86); joint ~3-4 sigma from DESI DR2 | **STANDING FALSIFIER** (H3, primary source arXiv:2503.14738, rho-scanned, closest 3.47 sigma) | -- | this IS the falsifier; a future `f0` forced near the in-tension default hardens it to a kill | The one genuine near-falsifying observational handle; robust (two rescue routes tested, both fail) |
| `f0` pinned by the gravity intersection | RETRACTED (H3 part B: corrected `M^2/r^6` residual breaks the order match) | -- | -- | No gravitational lifeline; `f0` stays free, tension stands alone |

### Sector: Standard Model / forces

| Claim | Class | Free params | What would falsify | Verdict |
|---|---|---|---|---|
| SM algebra `su(3)+su(2)+u(1)` = maximal compact of `su(3,2)`, one U(1), no extra photon | LOCATED-NOT-FORCED (exact group theory, but `su(3,2)` is a non-native sub-block; selecting it is the residual) | 0 (but the sub-block/vacuum choice is source-action-gated) | a source action that selects a different sub-block | Exact and reproducible existence; NOT a derivation -- the native `so(5,5)` max compact is `so(5)+so(5)`, not the SM |
| Pati-Salam rank-1 stabilizer = SM algebra (dim 12, rank 4) | HOUSING / existence (fingerprint match, not explicit iso) | 0 | -- | Consistency check, not a prediction |
| Mirror generation anomaly-free (4 SM traces vanish; so(10) cubic Casimir = 0 on 16) | HOUSING / existence | 0 | -- | Standard SO(10) rep theory; existence of a safe mirror, not a prediction that this is realized |
| Forces: a breaking to exactly the SM exists; no "28-photon" catastrophe | HOUSING | 0 | -- | Existence of an admissible breaking, not a forced one |

### Sector: Quantum / ghost (Krein)

| Claim | Class | Free params | What would falsify | Verdict |
|---|---|---|---|---|
| Unitarity repairable on Krein: positive physical sector + Krein-unitary generator exist | HOUSING / faithful-model consistency | 0 | a loop-level obstruction to `[P,S]=0` | Repairability on a faithful model, not a claim the true dynamics chooses it at loop level |
| `Sp(32,32;H)` non-compact gauge group (sharpens canon "Sp(64)") | CONDITIONAL / structural (H23 B) | 0 | -- | Correct sharpening; the indefinite metric exists only because the group is non-compact (stated, not hidden) |

### Sector: Generation count

| Claim | Class | Free params | What would falsify | Verdict |
|---|---|---|---|---|
| Count is a rigid finite 2-bit residual, located in odd-primary boundary summand | LOCATED-NOT-FORCED (principle grade; Nielsen-Ninomiya / Callan-Harvey / Kaplan; NOT proven for the true `Y14` index) | 0 | a proof it is index-forced (would upgrade) or forbidden | The honest structural status; the 3-primary localization is PRIOR ART (arXiv:1808.00009, 2605.26202) |
| Count is `{1,3}`, NOT pinned to 3, even in the full forced build (H40) | LOCATED-NOT-FORCED; residue trap (net-3 has residue 0 = carrier A's; order-3 datum cannot certify 3) | 0 | a source-action carrier-B declaration that is itself forced | Clean negative result, correctly refusing to manufacture a 3 |
| A derived `Z/3` grading IS present in the built (9,5) matter sector | LOCATED-NOT-FORCED (H38; `3=dim Lambda^2_+`, not imported) | 0 | -- | Genuine structural presence; but ghost parity permits `3+3` and cannot select a chiral 3 |

### Sector: The source action (the terminal object)

| Claim | Class | Free params | What would falsify | Verdict |
|---|---|---|---|---|
| All residual freedom (gauge vacuum, soldering, `mu_DW`, count/`C2`) jointly fixed by ONE object | CONDITIONAL / structural compression (a conjunction, not an identity -- flagship's own E-audit brake) | -- | building the object and finding a residual it does NOT fix | The genuinely novel positive contribution -- but a compression/map, NOT a prediction |
| The built `M_D` leaks (`C2=155.36`), a real VZ acausality demanding a causal cure | MEASURED (H40; a built magnitude, never fit) + CONDITIONAL forcing (collapses 4 corners to `{A,B}`) | 0 | -- | Real structural forcing of the cure requirement; stops one bit short of the carrier |
| Causal-cure term (non-minimal RS coupling) | not yet built -- the one unbuilt input | -- | building it forces or falsifies carrier B | GU has the acausality trigger, not the cure; the terminal construction problem |

## Synthesis

### Honest headline count (be strict)

- **PREDICTIONS (parameter-free, source-first, falsifiable): ZERO.**
  There is no claim in the flagship that emits an observed number before comparison with no free
  parameter, chosen carrier, chosen sub-block, or post-hoc branch doing the load-bearing work. The
  nearest candidates all fail the rule: the SM max-compact result is exact group theory but the
  sub-block is selected not derived (LOCATED-NOT-FORCED); the DESI `w0` "nail" rides the free `f0`
  family (FIT); `C_RY>0` is a genuine non-tuned computation but is conditional on the unforced
  soldering. This is the finding, reported cleanly: **the program currently has zero genuine
  parameter-free predictions.** It has a strong COMPRESSION result, not a prediction result -- which
  matches the standalone `explorations/predictive-boundary-audit-2026-07-12.md` verdict.

- **FITS: the accommodation carries 4 free parameters** (reproduced in the test):
  `f0`, `M2`, `B_i` (dark-energy machinery) and `mu_DW` (gravity scale). The two data-facing knobs
  are `f0` (DESI amplitude) and `mu_DW` (gravity scale/ghost mass). None is derived.

- **CONDITIONALs: the gravity leg (whole)** -- Stelle-clear MODULO the soldering postulate
  (genuine, PROVED-not-forced by H27) plus `mu_DW`; loop unitarity open. Plus the source-action
  compression thesis (conditional on building the object). Postulate status: the soldering is
  **genuine/unforced** (not leaning-forced); `mu_DW ~ M_Pl` is **leaning** (natural but smuggled).

- **LOCATED-NOT-FORCED:** the SM gauge algebra (sub-block-selected), the generation count `{1,3}`,
  and the derived `Z/3` grading. Forcing any of them needs the same unbuilt source-action declaration.

- **HOUSING:** Pati-Salam stabilizer, mirror anomaly-freedom, forces breaking, Krein repairability,
  Bach-flat vacua. All existence/consistency, none predicted.

- **STANDING FALSIFIERS (live negatives that could kill GU as it stands): ONE primary, plus latent.**
  1. **DESI DR2 ~3-4 sigma** (the known one) -- under-evolved `|w_a|`, primary-source-verified
     (arXiv:2503.14738), robust across two failed rescue routes. Currently *soft* only because `f0`
     is free; it hardens to a hard kill the instant the source action forces `f0` near the in-tension
     default. Status: LIVE, the program's one real observational handle.
  2. **Loop-level `[P,S]=0` / Stelle-Mannheim** -- latent: tree-only is shown; a loop non-unitarity
     would kill the gravity clear. Status: OPEN, generic-Stelle-shared, GU resolves it no better.
  3. **The soldering could be falsified** -- if a forced build lands `theta` off the second-fundamental-
     form locus, the whole gravity chain becomes a gauge statement, not a derivation. Status: OPEN.

### The single most exposed claim (what a referee attacks first)

The **dark-energy sector**. It is the only place GU touches data with a number, and that number is
~3-4 sigma wrong on `|w_a|` against primary-source DESI DR2. A referee does not need to accept any GU
internals to attack it: the CPL point sits outside the DESI ellipse, the sign match is degenerate with
LCDM on amplitude, `f0` is a free fit, and the gravity lifeline that would have pinned `f0` was
retracted (H3 part B). This is simultaneously the most exposed claim and the program's most honest
asset -- it is a genuine near-falsifier kept in plain sight.

### The single strongest genuine result

Two candidates, ranked honestly:
- **The one-residual compression itself** -- that gauge vacuum, gravity soldering + `mu_DW`, the
  count/`C2` residual, and the causal-cure term all route to a single named source-action declaration.
  This is the only genuinely novel *positive* contribution and it survives adversarial grading as a
  structural map. It is NOT a prediction.
- **`C_RY` computed positive by two independent methods** (H25) -- the strongest self-contained
  *computation* (it retired the wrong-sign antigravity kill by sign, not magnitude). But it is
  conditional on the soldering, so its physical force is gated.

The compression is the stronger *contribution*; `C_RY` is the stronger *computation*.

### Is "ACCOMMODATES" honest?

**Honest, and if anything slightly UNDER-claimed on the one point that is real, while correctly
refusing to over-claim everywhere else.** "A geometric framework accommodates known physics with all
remaining freedom in a single source-action declaration" is exactly right: accommodation (housing +
existence + conditional), not derivation, is what the ledger shows. The headline does not say predict,
derive, or confirm -- and the ledger confirms zero predictions, so the hedge is earned. The genuinely
novel claim (all freedom localizes to one object) is a compression, and the headline frames it as a
declaration, not a result about nature -- also honest. The only place the flagship risks reading as
stronger than it is: the phrase "no sector falsifies the framework" sits next to a live ~3-4 sigma
DESI tension; that is honest ONLY because `f0` is free (soft, not hard), and the body says so
explicitly. Verdict: the ACCOMMODATES headline is honest; the internal grade discipline is unusually
careful; the one watch-item is that "not falsified" is contingent on `f0` staying free.

## RE-RANK signal

The audit does not change the compression map, but it sharpens the priority order:

1. **Run the cheap falsifiers BEFORE the next synthesis.** The most decisive next moves are
   observational/loop tests that do not need the full source action:
   - **H10 weak-field / PPN** on the gravity branch against solar-system bars -- a failure here is
     more decisive than any further synthesis and is cheap (no source-action build required).
   - **A dark-energy coefficient gate** -- any source-derived `f0`/`xi_eff` recorded *before* DESI
     comparison would convert the sole FIT into a real predictive test (or a clean kill).
   - **H26 loop-level ghost unitarity** -- the latent gravity falsifier.
2. **H41 / the causal-cure term remains the terminal build** -- but the audit demotes it below the
   cheap falsifiers in urgency: it is the object that would turn conditionals into predictions, yet a
   *free* build p-hacks the carrier, so it only pays off if forced. Do the cheap discriminators first;
   they can kill or credit the program without waiting for the terminal object.
3. **Do NOT count another "reduced to one X" pass as progress** (the flagship's own E-audit brake).
   The compression is already at its terminal state; the epistemic state changes only when the source
   action emits a number before comparison, or a cheap falsifier fires.

Net: the program is exactly where its own boundary audit places it -- a strong compression with zero
predictions, four free parameters, one live near-falsifier, and one unbuilt terminal object. The
highest-value next runs are the cheap falsifiers (PPN, DE coefficient gate, loop `[P,S]=0`), not more
synthesis.

---

*Filed 2026-07-12. Wave 18, the predictive-content audit (H34). Arithmetic reproduced:
`python tests/wave18/H34_parameter_count.py` (exit 0, 13/13). Exploration-grade; no canon movement, no
claim-status change -- a sorting pass. Adversarially conservative: the PREDICTION column is empty by
design, and every positive was pushed to HOUSING/FIT/CONDITIONAL/LOCATED unless it cleared the clean
prediction rule, which none did.*
