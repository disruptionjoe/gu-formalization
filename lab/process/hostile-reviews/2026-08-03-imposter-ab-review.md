---
title: "J5 hostile field-specialist review: the imposter A/B fork resolution"
status: process
doc_type: hostile-review
created: 2026-08-03
object_under_review: "explorations/imposter-ab-resolution-proposal-2026-08-03.md (Reading A at 0.80) + explorations/draft-fqz-map-decider-2026-08-03.md (HOLDS, proposed 0.90) + lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
reviewer_charge: "Two-sided (binding): OVERCLAIM — attack the ω-half typing, the p.53 counter-signal, the sign-correlation handling, the W221 re-scope, and the verbatim quotes; OVER-FENCING — test whether the resolution is stronger than 0.90 and whether the label-attachment fence is tighter than needed."
specialisms: "representation theory of Clifford/Spin modules; textual source criticism"
verdict_summary: "PASS-WITH-CORRECTIONS — RESOLVED(A) at final confidence 0.90; five binding corrections (C1–C5), none direction-changing; the reviewer independently re-verified every load-bearing quote against the primary PDF, including pixel-level renders of pp.51 and 62, and found two NEW arguments that strengthen the resolution beyond its filed form"
---

# J5 hostile review: imposter A/B resolution

## 0. Independence of this review's evidence base

Nothing below relies on the extraction file's say-so. The reviewer:

1. **Re-hashed the primary source.** The local PDF
   (`/private/tmp/Geometric_Unity-Draft-April-1st-2021.pdf`, 2,087,649 bytes)
   has SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`
   — an exact match to the repo receipt in
   `lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md` row
   `WG-2021-DRAFT`. Bit-identical to the file the decider ingested.
2. **Independently re-extracted the text layer** of pp.3, 49, 50, 51, 52, 53,
   61, 62, 63, 65 (pypdf 6.14.2, no OCR) and re-ran the negative searches over
   all 69 pages.
3. **Independently rendered pp.51 and 62 as page images** (300 dpi) and read
   them visually — including the eq (12.22) underbrace and the p.51 diagram.
4. **Independently re-derived every load-bearing dimension** from Clifford/Spin
   module theory (no repo number taken on trust): dim S(14) = 128, Weyl halves
   64; Ω¹⊗S = 1792, ker Γ = 1664, graded 832+832; S(4) = 4 (Weyl 2s),
   S(10) = 32 (Weyl 16s), RS(4) = 12 (Weyl 6s), RS(10) = 288 (Weyl 144s);
   F = 2⊗16-type = 128 ungraded/64 graded; Q = 6⊗16-type = 384/192;
   Z = 2⊗144-type = 1152/576; 384+1152+128 = 1664 = 13·128. All exact.

## 1. Charge A — OVERCLAIM: findings

### A-1. The ω-half typing is NOT a dimension coincidence (attack failed)

The map F ↦ 128, Q ↦ 384, Z ↦ 1152 does not run on bare numbers. It runs on
the draft's **printed tensor-factor shapes** — 2⊗16, 6⊗16, 2⊗144 at eq (11.6),
and R̸⊗S̸ / S̸⊗R̸ / S̸⊗S̸ at eqs (11.3)/(12.22) in the same term order — which
have UNIQUE banked counterparts (S(V)⊗S(W), RS(V)⊗S(W), S(V)⊗RS(W)). The
dimension arithmetic (verified independently, §0.4) is corroboration, not the
argument. No alternative assignment of {F,Q,Z} to {128,384,1152} is consistent
with the printed factors. The three-way-"128" fence's warning (numerical
equality ≠ structural identity) is therefore satisfied, not violated: the
identity here is structural first, numerical second.

On the grading convention: the identification "draft ± = ambient chirality
halves = the repo's ω-eigenspace grading" rests on **two hard anchors**, both
re-verified on the page:

- **Eq (12.20) (p.61):** the author dimension-superscripts one chirality half
  of the plain spinor bundle as `S̸⁶⁴_L(TY)` / `S̸⁶⁴_R(TY)` — 64 = 2^(14/2−1),
  the ambient Weyl half — and decomposes each half into exactly two
  2⊗16-shaped products. This types the factor-2 as the two ambient chirality
  halves by the author's own hand.
- **The printed graded dimensions 64± and 832±** on the p.51 diagram
  (64 = graded F; 832 = graded Z⊕Q⊕F; visually confirmed in this review's
  render), which force graded Q = 192 and Z = 576 from the printed factors and
  double to the banked 128/384/1152/1664.

Representation-theoretically the identification is then airtight: for p+q
even, the Weyl decomposition of the complexified Cl(p,q) module IS the
eigendecomposition of the (normalized) volume word, and the repo's grading
operator (`I₁₄⊗ω` restricted; Q2 preregistration §1.1) is exactly the
spinor-factor ambient chirality the draft's halves refer to. Q2's computed
64+64 / 192+192 / 576+576 with sums (832, 832) matches the printed graded
dimensions term by term. **Prong 1 survives hostile scrutiny.** See C2 for the
one soft leg in how the decider PRESENTED this.

### A-2. The sign-correlation "discrepancy" (11.6 vs 12.20) was misdiagnosed — in the resolution's favor

The decider (§1 final paragraph) and the extraction (§4 note) state that
eq (11.6) pairs anti-correlated (2∓⊗16₊) where eq (12.20) pairs correlated
(L⊗L), on different carriers, and absorb this into the allocation-dependent
ω₄ω₁₀ = ±ω caveat. That framing compares OPPOSITE halves and manufactures a
tension that does not exist:

- (11.6): F₊ = 2₋⊗16₊ ⊕ 2₊⊗16₋ (anti-correlated); **F₋ = 2₊⊗16₊ ⊕ 2₋⊗16₋
  (correlated)**.
- (12.20): S̸⁶⁴_L = L⊗L ⊕ R⊗R (correlated); S̸⁶⁴_R = L⊗R ⊕ R⊗L
  (anti-correlated).

The two displays are **mutually consistent under the forced dictionary
F₋ ↔ S̸⁶⁴_L, F₊ ↔ S̸⁶⁴_R** — and the dictionary is convention-independent:
whichever small-factor half is called "+", the correlated class matches the
correlated class. The branching of a fixed ambient Weyl half under
Spin(1,3)×Spin(6,4) is the same rep-theory fact on every carrier (the form
degree never touches the spinor-factor branching), so "different carriers" is
not needed as an excuse. There is NO intra-source correlation discrepancy on
the two load-bearing displays. The ω₄ω₁₀ = ±ω caveat remains true and needed,
but only as repo-side allocation bookkeeping (which correlated class gets
called "+" under a given sign allocation), not as the discharge of a source
tension. **The discrepancy was not papered over — it was over-conceded.
Binding correction C1 restates it; prong 1 comes out stronger.**

### A-3. The p.53 table: genuine second usage, and it cannot host the observed family

Independently verified (§0.2–0.4): Table 3's printed dimensions, multiplicity
column at face value, sum to exactly 144 — the internal factor eq (11.6)
places only inside Z — and the five imposter-NAMED rows carry exactly Table
1's true-generation quantum numbers (one copy each = 16, leaving 128 of
exotics). The star notation is unexplained; the host representation is
unstated. This is a real, non-eliminable second usage of "imposter" and the
extraction was right to flag it rather than harmonize it.

But the hostile question is whether it degrades the LABEL ATTACHMENT, and
here the draft itself closes the door with a passage the decider never
deployed: **p.52 (verbatim, verified): "the one above the dashed line
corresponds to matter in our world with the other sectors not labeled by F to
the left and above the line are currently dark to us"** — and eq (12.20)'s
overbrace labels the F-shaped content "Luminous Light Standard Model Family
Matter" while the complementary half is "Dark Decoupled Looking Glass
Matter." On the draft's own assignment, **non-F content is dark**. The
observed third generation (t, b, τ, ν_τ) is not dark. So whatever the p.53
imposter-named rows are (dark 144-content wearing generation-shaped quantum
numbers — a reading licensed by §11.2's PLURAL heading "Imposter
Generations"), they cannot be the observed third family, and the singular,
definite "Imposter Third Generation" of eq (12.22)/§12.10/p.65 ix remains the
only candidate for that role. Under no reading does any imposter label touch
the Q-shaped RS slot — which on p.52 carries its own different label ("a new
cousin spin-3/2 'generation'", verbatim, verified). No flip condition is met
or approached. Disposition ruling in §5.

### A-4. The W221 re-scope: honest, with one phrasing that must be repaired

W221's pre-declared condition and verdict logic were re-read at source
(`tests/W221_falsify_generation_count_structure.py:35-42, 255-264`). The
proposal's row 1 ("SURVIVES is RE-SCOPED, not fired") is the correct form: the
computed branchings (S⁺(10) → (4,2,1)⊕(4̄,1,2); RS internal Weyl content 16;
H-line arithmetic) are exact facts that survive any labeling, and the verdict
machinery keeps regression value. The re-scope does NOT smuggle a weakening
provided two things are said plainly, which the banner in §6(iii) says:

1. SURVIVES now certifies only that the B-shaped assembly (2 in the spinor
   legs + 1 RS) is not structurally forbidden — an assembly the source
   correction shows is NOT the author's. W221 therefore no longer certifies
   anything about the program's actual generation story, and no falsification
   of the A-assembly has been run.
2. **Binding correction C4:** the proposal's suggested re-derived survival
   statement — "the 128's S(W) content is 16⊕16̄, one 16 per ambient ω-half" —
   is the one place a weakening could smuggle in. Per ambient ω-half the 128
   contains 2∓⊗16₊ ⊕ 2±⊗16₋: each internal Weyl 16 appears with base-Weyl
   multiplicity 2 and PAIRED with its conjugate — vectorlike content (exactly
   P-Q2-3's 32/32/32/32). Any banner or successor statement must say
   "vectorlike 16⊕16̄ content per half," and must never be citable as "one
   generation from the imposter slot."

### A-5. Verbatim-quote audit: all load-bearing quotes verified; two extraction inaccuracies found (non-load-bearing)

Verified verbatim against the reviewer's own extraction and renders: eqs
(11.1)–(11.6) with term order; the §11.2 plural heading; the p.51 2+1 claim;
the p.52 "cousin" sentence and dark-sectors sentence; Table 1 and Table 3
complete; eqs (12.18)–(12.20) with both brace labels; the §12.10 title; eq
(12.22) with the bold third term and the "Imposter Third Generation"
underbrace attached to it and nothing else (pixel-level); the pp.62–63
continuation and footnote 13; p.65 viii–ix; the p.49 caveat-emptor note
(attaching to (10.10), i.e. NOT to the §11–§12 displays, as the extraction
says). Negative findings re-run over all 69 pages: "identical in form"
occurs nowhere; "true generation" only at p.63; the word "imposter" occurs
only on pp.3 (ToC), 50, 53, 62, 65 — eq (11.6)'s page has none. The decider's
two filed corrections to the proposal (§3.1, §3.2) are themselves correct.

Two inaccuracies in the extraction's p.51 diagram description (both outside
the decider's load-bearing legs after C2, but they must be fixed because the
extraction is a SOURCE-grade file):

- **C3a:** "(the other three corners permute the ± signs)" is wrong for the
  bottom row: the bottom-corner 832 brackets also INVERT the stacking order
  (F on top, Z on the bottom; visually confirmed).
- **C3b:** the intra-bracket dashed line `−−⊕−−` appears ONLY in the top-row
  832 brackets; the bottom-row brackets join all three terms with plain ⊕
  (visually confirmed). Extraction item 4 states the dashed-line position
  categorically and must be scoped to the top row.

One further convention wrinkle, found in this review and to be recorded
(part of C2): the diagram's Spin(7,7)± SUPERSCRIPTS track the row (both 832₋
and 832₊ appear under Spin(7,7)⁺ superscripts in the top row; the ν₊ slot
hosts (F⁻)₆₄₋ content under a Spin(7,7)⁺ superscript). The superscript
therefore indexes the two emergent "separate chiral theories" of the p.52
prose, NOT the content's ambient Weyl half. The decider's parenthetical
citing the superscripts as evidence that "the grading index ± is ambient
chirality" is its one soft leg; the two hard anchors of §A-1 carry the typing
without it.

## 2. Charge B — OVER-FENCING: findings

### B-1. The resolution is STRONGER than filed, on two counts

1. **The darkness argument (new, this review; §A-3):** p.52's dark-sectors
   sentence plus (12.20)'s Luminous/Dark braces independently force the
   OBSERVED third family into F-shaped content. This is a fourth textual leg,
   structural rather than label-based, and it simultaneously neutralizes the
   p.53 residual's worst reading. The decider argued the label; the source
   also argues the physics-facing bookkeeping.
2. **The non-discrepancy (C1; §A-2):** the one alleged intra-source wrinkle on
   the load-bearing displays dissolves under the forced dictionary. The
   primary-source case has no internal tension left on eqs (11.6)/(12.20)/
   (12.22); what remains against it is only the p.53 loose usage and the
   diagram's ± bookkeeping wrinkles.

### B-2. Is >0.90 warranted? Ruling: no — 0.90 confirmed as final

The convergent evidence (eq 12.22 underbrace + §12.10 title and prose + p.65
ix + the otherwise-labeled Q slot + the shape-forced map + the darkness
argument) would support ≈0.93 for the draft-internal label attachment taken
alone. The resolved question is slightly larger — "the program's third-family
label attaches to Reading A" — and three residuals cap it: (i) the p.53
second usage shows the author's imposter vocabulary is not perfectly
disciplined; (ii) the document is a self-declared working draft v1.0 (its own
p.49 carries a caveat-emptor about diagram stability), so a future revision
could restructure the story; (iii) the p.51 diagram's ± bookkeeping wrinkles
(§A-5) show the grading notation is not uniformly reliable outside the two
hard anchors. **Final confidence: 0.90.** Better-founded than the decider's
0.90 (two new supports, one dissolved tension), but the same number.

### B-3. Is the label-attachment fence tighter than needed? Ruling: no

The "label only" fence is not over-caution — it is the draft's own content:
the imposter is "merely effective," "NOT a true generation," and the block is
computed vectorlike (PH-K1-KINEMATIC). Loosening the fence would contradict
the very source being adopted. The fences that stay (P3, Rung 1, Π_RS^phys,
PH-K1-PHYSICAL, Witten-1983 on any chiral use of the 384) are each
independently motivated and none is made redundant by RESOLVED(A). One
non-binding note: the draft's Luminous/Dark typing of the F vs Z/Q sectors is
now a verified SOURCE FACT available for future work, but this review
licenses no repo claim built on it beyond its use in §A-3.

## 3. VERDICT

**PASS-WITH-CORRECTIONS.** The imposter A/B fork is **RESOLVED(A)** — the
imposter/third-generation label attaches to Reading A, the 128-dim
S(V)⊗S(W) spin-1/2 slot — at **final confidence 0.90**, label attachment
only. The corrections C1–C5 below are binding on the named artifacts and on
every surface edit in §6; none changes the direction or the number. The
proposal does not return to open; the §6 edits are licensed once the
corrections are carried.

**The licensed sentence (exact, for surface edits):**

> The imposter/third-generation label attaches to Reading A — the 128-dim
> S(V)⊗S(W) spin-1/2 slot — RESOLVED at confidence 0.90 (J5 2026-08-03): the
> 2021 draft's eq (12.22) underbrace, §12.10, and p.65 concur on the F-shaped
> term, the graded factor-2 is typed by the source as the two ambient
> chirality halves (printed 64±/832±; F↦128, Q↦384, Z↦1152), and the RS slot
> carries the draft's separate "new cousin spin-3/2 'generation'" label; this
> is label attachment only — the block remains kinematically vectorlike and
> no physical chiral third generation is asserted.

## 4. Binding corrections (enumerated)

- **C1 (decider §1 + extraction §4 note).** Restate the (11.6)/(12.20)
  relation as CONSISTENCY under the forced dictionary F₋ ↔ S̸⁶⁴_L
  (correlated), F₊ ↔ S̸⁶⁴_R (anti-correlated), convention-independent; delete
  the "anti-correlated vs correlated on different carriers" framing; keep the
  ω₄ω₁₀ = ±ω caveat solely as repo-side allocation bookkeeping. Do not cite
  the pair as an intra-source discrepancy anywhere.
- **C2 (decider §1 legs).** The grading-convention identification rests on
  eq (12.20)'s S̸⁶⁴_{L/R} and the printed 64±/832± graded dimensions; the p.51
  Spin(7,7)± superscripts index the two emergent chiral theories, not the
  content's Weyl half, and may not be cited as convention evidence. Record
  the ν₊-hosts-64₋ wrinkle.
- **C3 (extraction §2.1).** Fix the corner parenthetical (bottom row inverts
  stacking order) and scope the dashed-line claim to the top-row brackets;
  both facts visually confirmed in this review.
- **C4 (W221 re-scope language, proposal §9 row 1 and all successors).** The
  128's per-ω-half internal content is vectorlike 16⊕16̄ with base-Weyl
  multiplicity 2 (P-Q2-3); the phrase "one 16 per ambient ω-half" is
  forbidden as a standalone claim, and the re-scoped W221 may never be cited
  as "one generation from the imposter slot."
- **C5 (residual registration).** The p.53 residual must be carried as a
  typed caveat line wherever RESOLVED(A) is recorded (pack, fork table,
  paper §11), in the form given in §5 — it may not be silently dropped, and
  it may not be inflated into a fork.

## 5. Ruling on the p.53 residual's disposition

**RECORDED, NON-BLOCKING, NO NEW FORK.** Typed disposition: the p.53 table is
a second, looser use of "imposter" (licensed by §11.2's plural heading) —
imposter-named particle rows with exactly true-generation quantum numbers
inside content summing to 144, i.e. Z-internal by the only available
identification; host representation and star notation undecodable from the
document. It cannot host the OBSERVED third family under the draft's own
darkness assignment (p.52 + eq 12.20 braces: only F-labeled content is
luminous SM matter), and under no reading does it attach any imposter label
to the Q-shaped RS slot — so it neither meets a flip condition nor supports
Reading B. It is to be carried as a standing caveat line (C5) and named as a
first-check target against any future revision of the draft. It does NOT
spawn a "Reading C" adjudication row: no repo claim rides on it.

## 6. PROPOSED EDITS (drafted by this review; the orchestrator applies them — this file edits nothing)

### (i) `lab/process/agent-context-pack.md` — replace the "IMPOSTER" fork bullet (Live forks section) with:

> - "IMPOSTER" A-vs-B: **RESOLVED(A) 2026-08-03, confidence 0.90** (J5-passed:
>   lab/process/hostile-reviews/2026-08-03-imposter-ab-review.md). The
>   imposter/third-generation LABEL attaches to the 128 S(V)⊗S(W) spin-1/2
>   slot: the 2021 draft's eq (12.22) underbrace, §12.10, and p.65 ix concur
>   on the F-shaped term; the graded factor-2 is typed BY THE SOURCE as the
>   two ambient chirality halves (printed 64±/832±; F↦128, Q↦384, Z↦1152);
>   the RS 384 carries the draft's separate "new cousin spin-3/2
>   'generation'" label. LABEL ONLY: the block is kinematically VECTORLIKE
>   (PH-K1-KINEMATIC CONFIRMED, 64+64, joint 32/32/32/32); PH-K1-PHYSICAL
>   stays OPEN/BLOCKED; P3, Rung 1, and the Π_RS^phys fence stand; any chiral
>   use of the 384 still owes the Witten-1983 exit. W221's SURVIVES is
>   RE-SCOPED to the B-shaped assembly (a non-generation RS sector — see the
>   W221 banner); under (A) the "2" of 2+1 are ν and the γ-trace part of ζ
>   upstairs, not product-rule occupants. Recorded residual (non-blocking):
>   the draft p.53 table applies imposter particle names to 144-internal
>   (Z-side) content — a second, looser usage; it cannot host the observed
>   family (draft p.52: non-F sectors are dark).

### (ii) `GEOMETER-VS-PHYSICS-OBJECTS.md` — append this row to the fork table:

> | **"Imposter" / the third generation (label attachment)** | the observed third family (t, b, τ, ν_τ) as a third repeated spin-1/2 generation; long-standing in-repo reading: the RS spin-3/2 term is the third family (the W221 assembly) | an EFFECTIVE imposter: the S̸(TX)⊗S̸(Nג) spin-1/2 defect term (the 128) revealed on pull-back of the RS remainder from Y¹⁴; the RS-shaped 384 is the draft's separately-labeled "new cousin spin-3/2 'generation'"; the two true families are ν and the γ-trace part of ζ upstairs | **Settled at LABEL level, native side (J5 2026-08-03, 0.90; lab/process/hostile-reviews/2026-08-03-imposter-ab-review.md):** the 2021 draft attaches "Imposter Third Generation" to eq (12.22)'s third term (underbrace + §12.10 + p.65 ix), and the graded factor-2 is the two ambient chirality halves (printed 64±/832±). Label only — the 128 is kinematically vectorlike (PH-K1-KINEMATIC); no physical chiral third generation is asserted; recorded residual: the draft p.53 table's looser imposter usage on Z-internal content (non-blocking, cannot host the observed family). |

### (iii) `tests/W221_falsify_generation_count_structure.py` — insert at the top of the module docstring:

> ```
> RE-SCOPE BANNER (2026-08-03; J5-passed:
> lab/process/hostile-reviews/2026-08-03-imposter-ab-review.md).
> The imposter A/B fork is RESOLVED(A) at 0.90: the source's "Imposter Third
> Generation" (2021 draft eq 12.22 underbrace, sec 12.10, p.65 ix) is the
> S(V)(x)S(W) spin-1/2 slot (dim 128), NOT the RS(3,1)(x)S(6,4) term this
> test treats as the third family. Consequences:
>   * The computed rep theory below is UNCHANGED and remains green: the
>     branching S+(10) -> (4,2,1)(+)(4bar,1,2), the RS internal Weyl content
>     16, and the H-line arithmetic are exact facts about the subspaces.
>   * The verdict "SURVIVES" is RE-SCOPED, not fired: it certifies only that
>     the 2+1 assembly THIS test modeled (2 generations in the spinor legs
>     + 1 RS generation -- Reading B) is not structurally forbidden. Under
>     the source-corrected reading that assembly is not the author's: the RS
>     term is a NON-generation sector (the draft's "new cousin spin-3/2
>     'generation'", p.52), and the two true families are nu and the
>     gamma-trace part of zeta upstairs on Y14 (draft p.62, p.65 viii-ix).
>   * This test therefore no longer certifies anything about the program's
>     actual (source-corrected) generation story, and no falsification of
>     the A-assembly has been run here. The 128's internal content is
>     VECTORLIKE -- 16(+)16bar per ambient omega-half, base-Weyl
>     multiplicity 2 (P-Q2-3: 32/32/32/32). Do NOT cite this file as "one
>     generation from the imposter slot" or as a survival of the
>     generation-count leg under Reading A.
> Verdict logic and exit coupling below are untouched (regression value).
> ```

### (iv) `papers/drafts/one-generation-not-three/draft.md` — §11 update (replace §11.3's body) plus the mandatory §10.3 companion fix:

**§11.3, replace body with:**

> ### 11.3 Resolution (2026-08-03): the label attaches to Reading A
>
> The named decider ran. The April 2021 draft was ingested directly
> (SHA-256-matched to the program's prior receipt) and both preregistered
> prongs held. Under the draft's own grading convention the eq (11.6)
> letters map F ↦ 128 = S(V)⊗S(W), Q ↦ 384 = RS(V)⊗S(W),
> Z ↦ 1152 = S(V)⊗RS(W), with the factor of two typed by the source itself
> as the two ambient chirality halves: the draft prints 64± and 832± as
> graded dimensions, and eq (12.20) dimension-superscripts one chirality
> half of the plain spinor bundle as S̸⁶⁴_{L/R}. The "Imposter Third
> Generation" underbrace at eq (12.22) sits on the third, S̸(TX)⊗S̸(Nג)
> term — set in bold — and on nothing else; §12.10's prose ("its Spin−1/2
> appearance on X is the result of branching rules under pull back") and
> the p.65 synopsis item ix concur; and the Q-shaped RS slot carries the
> draft's own different label ("a new cousin spin-3/2 'generation'",
> p.52). Two further source facts close the loop: the p.52 darkness
> assignment (sectors not labeled F "are currently dark to us") and
> eq (12.20)'s "Luminous Light Standard Model Family Matter" overbrace
> place the observed, luminous third family in F-shaped content — the RS
> and Z sectors could not host (t, b, τ, ν_τ) on the draft's own terms.
> **Status: RESOLVED(A), confidence 0.90** (hostile field-specialist
> review passed 2026-08-03; label attachment only). This paper's
> Reading-A voice in §§4–7 and 9 is now source-licensed rather than
> conditional. Unchanged: the 128 is kinematically vectorlike (§9), the
> count kills stand, and nothing here asserts a physical chiral third
> generation. One residual is carried honestly: the draft's p.53 table
> applies imposter particle names to content summing to the Z-internal
> 144 — a second, looser usage of "imposter" (§11.2's heading is plural),
> recorded as a source caveat; under no reading does it attach the label
> to the RS slot. The older Reading-B artifacts (the generation-count
> falsification test, the 2026-06-22 branching closure, PC2 item B2) are
> re-scoped per the resolution's dependency table, and §12's Witten-1983
> gate remains binding on any future chiral use of the RS 384.

**§10.3, two mandatory repairs (C5-adjacent; the paper currently quotes a
nonexistent sentence):** (a) delete the quoted gloss `"the imposter —
identical in form to a true generation"` — the phrase occurs nowhere in the
draft (verified by exact-string search, twice independently); replace with
the draft's real sentences: "merely effectively identical to the other two
and, presumably, only at low energy" (p.51) and "not a true generation as it
has a different representation structure than the other two" (p.63), plus
the p.62 "Spin−1/2 appearance on X" sentence for the form-match point.
(b) Replace the "Open typing gate, carried honestly" sentence with: the
factor-2 is now typed by the source as the two ambient chirality halves
(64±/832± printed; S̸⁶⁴_{L/R} at eq 12.20), closing decision criterion #1.

### Companion re-scopes (proposal §9 rows 2, 3, 5, 12 — text as filed there, licensed with C4's phrasing constraint; row 6's legb2 header is CONFIRMED, no banner; rows 4, 10 unchanged either way).

## 7. What this review does NOT license

No physical chiral third generation; no V−A or anomaly claim; no movement of
PH-K1-PHYSICAL, P3, Rung 1, OQ-RK1, bar(b), H59, the count, or any signature/
carrier fork; no transport of the draft's Luminous/Dark typing into a repo
claim; no citation of the re-scoped W221 for the A-assembly; no revival of
the strong hinge reading (the "2" stay upstairs). Q2-B-JOINT stays open as a
named cheap follow-up; its result cannot move the label but could hand B a
physics candidate and should still be run. The two in-repo "2+1"s fork and
the SIGNATURE fork remain open and untouched.
