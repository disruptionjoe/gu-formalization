---
artifact_type: exploration
status: exploration
doc_type: decider-computation
created: 2026-08-03
work_item: "DRAFT-FQZ-MAP — the named flip computation of explorations/imposter-ab-resolution-proposal-2026-08-03.md §10 (primary decider for criterion 1 and exit-condition item (i) of the imposter A/B fork). Executes the preregistered check against the ingested primary source (lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md)."
title: "DRAFT-FQZ-MAP verdict: HOLDS on both preregistered prongs — (1) the map F ↦ 128 = S(V)⊗S(W), Q ↦ 384 = RS(V)⊗S(W), Z ↦ 1152 = S(V)⊗RS(W) holds under the draft's OWN grading convention (the ± labels are ambient-chirality halves; the draft itself prints 64± and 832± as graded dimensions, and eq 12.20 prints S̸⁶⁴_{L/R} for one half of the 2⊗16 object), and (2) the draft's 'Imposter Third Generation' underbrace at eq (12.22) sits on the THIRD, S̸(TX)⊗S̸(Nג) (F-shaped, spin-1/2) term — NOT on the Q-shaped RS term. Neither flip condition is met. Criterion 1 of the resolution proposal upgrades from gated-0.75 to primary-source grade, with two filed corrections to the proposal's own citations and one flagged residual (the p.53 table). NOTHING RESOLVES HERE: adoption of Reading A remains J5-gated."
grade: "PREREGISTERED CHECK EXECUTION — reading and comparison only. The only computation is dimension arithmetic on the draft's printed factors (2·16+2·16 = 64 etc.), labeled as such; no script, no new mathematical claim, no FD read (P-H29 engaged nowhere). Every load-bearing quote is verbatim from the visually verified primary source with page/equation numbers (see the extraction file). PRE-DEPOSIT: no claim-status, canon, verdict, bar(b), H59, count, LANE-STATE, or public-posture movement; the fork resolves only via a passed J5 hostile field-specialist review."
canon_verdict_change: none
verdict_gate: "DECIDER INPUT ONLY. Per the adjudication row §4.5 and the resolution proposal §12, the imposter A/B fork resolves only via a typed ruling that has PASSED a J5 hostile field-specialist review. Until then W221's verdict logic, the 2026-06-22 closure, NEXT-STEPS PC2, legb2's header, the context-pack fork row, and every register/canon surface stay exactly as they are. This file changes CONFIDENCE INPUTS to the J5 review, nothing else."
hostile_review_status: "NOT YET REVIEWED — this file is input to the J5 review alongside the resolution proposal"
depends_on:
  - lab/process/CURRENT-RESEARCH-CONTEXT.md
  - explorations/imposter-ab-resolution-proposal-2026-08-03.md
  - explorations/imposter-reading-adjudication-2026-08-03.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md
  - explorations/chirality-grading-and-77-rerun-2026-08-03.md
  - tests/escape-corners/legb2_shadow_restriction.py
---

# DRAFT-FQZ-MAP: the named decider, executed

## 0. What was preregistered, and what was obtained

The resolution proposal §10 named this computation as the single decisive
action for criterion 1: ingest the 2021 draft §11–§12.10 directly; extract
eq (11.6)'s F/Q/Z definitions UNDER THE DRAFT'S OWN GRADING CONVENTION and
eq (12.22)'s term order and labels; check the proposed map F ↦ 128, Q ↦ 384,
Z ↦ 1152 through the ω-half typing of proposal §2.1. Flip condition
(verbatim from §10): "the draft's 'Imposter Third Generation' term is the
RS-shaped slot (Q-shaped, 6⊗16), or F fails to map to S(V)⊗S(W) under the
draft's own convention."

Primary source obtained 2026-08-03: the official April 1, 2021 "Author's
Working Draft v 1.0" PDF (69 pp.), SHA-256
`3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4` — an
exact hash match to the repo's prior receipt, so this is bit-identical to
the file every earlier repo citation pointed at. All load-bearing content
was read visually from rendered pages (born-digital TeX; no OCR). Full
verbatim extraction with page/equation numbers:
`lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` (cited below as
EXT §n). The hearsay-once-removed objection (proposal §8) is hereby
discharged for every quote in this file: nothing below routes through the L1
lens.

## 1. Prong 1 — the map, under the draft's own grading convention: HOLDS

**The draft's grading convention, from the source itself (three independent
printed surfaces):**

1. Eq (11.6), draft p.52 (EXT §2.2):
   `F±_{1/2} = (2∓⊗16₊ ⊕ 2±⊗16₋)`, `Q±_{3/2} = (6∓⊗16₊ ⊕ 6±⊗16₋)`,
   `Z±_{1/2} = (2∓⊗144₊ ⊕ 2±⊗144₋)` "for Spin(1,3)×Spin(6,4)". Each graded
   label is a TWO-TERM chirality-correlated sum; the grading index ± is
   ambient chirality (the p.51 diagram superscripts every bracket
   Spin(7,7)⁺ or Spin(7,7)⁻).
2. The p.51 diagram (EXT §2.1) prints the graded dimensions itself:
   standalone F brackets are subscripted **64₊/64₋**, and the Z⊕Q⊕F brackets
   are subscripted **832₊/832₋**. So graded F = 64 is the author's own
   number, not a reconstruction; and graded F+Q+Z = 832 forces graded
   Q = 192 and Z = 576 from the printed factors (6·16·2, 2·144·2).
3. Eq (12.20), draft p.61 (EXT §4) prints `S̸⁶⁴_L(TY)` and `S̸⁶⁴_R(TY)`:
   the author dimension-superscripts ONE chirality half of the 2⊗16-type
   object as 64, each half being a chirality-correlated two-term sum —
   exactly the structure of eq (11.6)'s F±.

**The map, checked:**

| draft label (graded) | draft's printed/forced graded dim | ungraded (both ± halves) | banked object (legb2:185-190, adjudication row §0) | verdict |
|---|---|---|---|---|
| F±_{1/2} = 2∓⊗16₊ ⊕ 2±⊗16₋ | 64 (printed: diagram 64±) | **128** | S(V₄)⊗S(W₁₀), dim 128, spin-1/2 | **MATCH** |
| Q±_{3/2} = 6∓⊗16₊ ⊕ 6±⊗16₋ | 192 (forced by printed factors) | **384** | RS(V)⊗S(W), dim 384, spin-3/2 | **MATCH** |
| Z±_{1/2} = 2∓⊗144₊ ⊕ 2±⊗144₋ | 576 (forced by printed factors) | **1152** | S(V)⊗RS(W), dim 1152 | **MATCH** |
| (Z⊕Q⊕F)± | 832 (printed: diagram 832±) | 1664 | ker Γ = 1664; certified ω-graded (832, 832) | **MATCH** |

Shape identification is the draft's own: eq (12.22) writes the ungraded
versions of the three slots as R̸(TX)⊗S̸(Nג), S̸(TX)⊗R̸(Nג), S̸(TX)⊗S̸(Nג) —
the same term order as the abstract rule eq (11.3) — and eq (11.6) gives
their graded Spin(1,3)×Spin(6,4) content. F is 2⊗16-shaped = S(V)⊗S(W);
Q is 6⊗16-shaped = RS(V)⊗S(W); Z is 2⊗144-shaped = S(V)⊗RS(W).

**The factor-2 is now TYPED BY THE SOURCE: it is the two ambient chirality
halves.** The proposal §2.1's ω-half typing (author's graded labels
64/192/576 = one ω-half each of the banked 128/384/1152) is confirmed at
primary-source level, including the chirality-correlated internal structure
of each half (proposal §2.1 leg 2) and including its sign caveat: eq (11.6)
pairs anti-correlated (2∓⊗16₊) where eq (12.20) pairs correlated (L⊗L) — on
different carriers — which is precisely the allocation-dependent ω₄ω₁₀ = ±ω
bookkeeping already fenced by Q2's new-fact 2 (EXT §4 note). Prong 1:
**F maps to S(V)⊗S(W); the map HOLDS in full.**

## 2. Prong 2 — where the draft's own imposter label sits: the F-shaped slot

Eq (12.22), draft p.62 (EXT §5): the underbrace **"Imposter Third
Generation" is attached to the THIRD term, S̸(TX)⊗S̸(Nג) — set in bold — and
to nothing else.** The Q-shaped first term R̸(TX)⊗S̸(Nג) carries no label.
Convergent surrounding text, all verbatim in EXT:

- §12.10 title (p.62): "Three Generations Should be Replaced by 2+1 model of
  two True Generations and one Effective Imposter Generation."
- p.62–63: the RS complement "contains the imposter third generation which
  is only revealed under decomposition as in the above. Thus, it is not a
  true generation as it has a different representation structure than the
  other two beyond its obvious mass difference."
- p.62: "its Spin−1/2 appearance on X is the result of branching rules under
  pull back from Y where it is native" — the draft's own resolution of the
  spin-3/2/spin-1/2 tension: NATIVE HOME = R̸(TY) on Y (spin-3/2 there);
  the imposter AS IT APPEARS ON X = the revealed spin-1/2-shaped summand.
- p.65 (item ix): "The Spin 3/2 portion of ζ breaks down under pull back to
  reveal a third 'imposter generation' that is merely effective" — again:
  the imposter is what the breakdown REVEALS, i.e. eq (11.3)/(12.22)'s odd
  purely-spinorial third term, not the RS-shaped first term.
- p.52: the Q slot has its own, different label — "a new cousin spin-3/2
  'generation' Q⁺_{3/2}" with reversed weak-isospin logic — a SEPARATE
  prediction the draft never calls an imposter. Reading B's candidate object
  is therefore not merely unlabeled; it is otherwise-labeled.

Prong 2: **the labeled imposter term is the F-shaped (S(V)⊗S(W), spin-1/2)
slot. It is not Q-shaped.**

## 3. Corrections and residuals (the honest column)

1. **Citation correction to proposal §2.2 bullet 1:** eq (11.6) does NOT
   itself carry the word "imposter" (the word appears nowhere on draft
   pp.51–52 body text; EXT §2.2 negative finding). The F-attachment runs
   through eq (12.22)'s underbrace + §12.10 text + p.65, with eq (11.6)
   supplying the graded typing of the F shape. The proposal's conclusion
   survives; its first bullet's citation was off by one equation.
2. **The "identical in form to a true generation" gloss does not exist in
   the draft** (exact-string search, all 69 pages; EXT §2.2). The draft's
   actual language is "merely effectively identical to the other two ...
   only at low energy" (p.51) and "NOT a true generation as it has a
   different representation structure" (p.63, emphasis added). The L1 lens's
   quoted gloss was a paraphrase and slightly overclaims form-identity.
   Constraint 4 of the proposal's §11 count ("Lorentz type matches ... with
   zero additional mechanism") is UNAFFECTED — it rests on the slot's
   2⊗16 shape and the p.62 "Spin−1/2 appearance on X" sentence, both now
   source-verified — but any future quotation must use the real sentences.
3. **Flagged residual — the p.53 table (EXT §3):** the rows named "Imposter
   Quarks / Imposter Anti-Quarks / Imposter Leptons / Imposter
   Anti-Electron / Imposter Anti-Neutrino" sit in a table whose printed
   dimensions sum to exactly 144, i.e. the internal 144 that eq (11.6)
   places only inside Z; the named rows' quantum numbers are exactly the
   true-generation 16 of Table 1 (one copy each: 6+3+3+2+1+1 = 16, leaving
   128 of exotics). The draft never says what the table decomposes and never
   explains its star notation. Read one way it is a second, looser use of
   "imposter" (§11.2's heading is "Imposter GenerationS", plural): dark
   144-content wearing generation-shaped quantum numbers. Read another way
   it attaches imposter PARTICLE names to Z-internal content, in tension
   with eq (12.22)'s F-attachment. **Under NEITHER reading does any imposter
   label attach to the Q-shaped RS(V)⊗S(W) slot, so no flip condition is
   met; but the J5 review should weigh this surface explicitly.** It is the
   one imposter-labeled passage in §11–§12 that does not point at F.
4. The two true families' location is now source-verified along with the
   imposter's: ν = family one, ζ's gamma-trace part = family two (p.62,
   p.65 viii–ix; EXT §5–§6) — the primary-source form of the L1 correction
   the hinge panel already carries ("the 2 do not live in the product
   rule"), relevant to proposal §9 rows 2 and 11.
5. Signature note, fenced: the §12.9–§12.10 development is written on
   Y^{7,7} (eqs 12.18–12.19; Spin(7,7)± superscripts on p.51). This bears on
   the separate, unadjudicated SIGNATURE fork and transports nothing here
   (the split is 4+10 either way; the map check above is
   signature-independent).

## 4. Verdict and what it does to the proposal's confidence

**VERDICT: HOLDS** — both preregistered prongs, cleanly:

- F ↦ 128 = S(V)⊗S(W), Q ↦ 384 = RS(V)⊗S(W), Z ↦ 1152 = S(V)⊗RS(W) hold
  under the draft's own grading convention, and the factor-2 is typed by the
  source itself as the two ambient chirality halves (64/192/576 graded,
  128/384/1152 ungraded, 832± printed by the author).
- The draft's "Imposter Third Generation" label sits on the F-shaped
  (spin-1/2, S̸(TX)⊗S̸(Nג)) slot — eq (12.22) underbrace, §12.10 title and
  text, and p.65 all concurring — and the Q-shaped slot carries a different
  label of its own ("new cousin spin-3/2 'generation'").

Neither flip condition of proposal §10 is met. Per the proposal's own
decision rule, **criterion 1 upgrades from "0.75, gated" to primary-source
grade**: its three textual legs no longer share the L1-lens gate, and the
§2.3 gate (the sole stated cap on the proposal's 0.80) is discharged. The
honest offsets are §3 above: two citation-level corrections to how the
textual legs were quoted, and one flagged residual (the p.53 table) that
does not meet any flip condition but belongs in front of the J5 reviewer.
Proposed post-decider confidence for the J5 review's consideration: **0.90**
(up from 0.80; capped below higher by the p.53 residual and by the
transcript leg's unchanged ambiguity). The recommendation's direction is
unchanged: Reading A.

Unchanged and untouched by this file: PH-K1-KINEMATIC (the 128 is
kinematically vectorlike), the reinstated P3, Rung 1 (blocks ≠ generations),
the kinematic/physical carrier fence (Π_RS^phys does not exist), Q3's
booked deflation of A's payoff, and every surface listed in proposal §9.
Label attachment is all that this decider informs, and its adoption remains
J5-gated.

## 5. Governance

LANE-STATE, or public-posture movement; no file outside this one and its
companion extraction was created or edited; nothing was committed. The J5
hostile field-specialist review (two-sided charge: overclaim AND
over-fencing) now has, as requested by proposal §12, the primary source in
front of it; the review should attack, in order: the §3.3 p.53 residual,
the §1 grading-convention identification (eq 11.6 vs eq 12.20 sign
correlation), and the §4 confidence proposal.
