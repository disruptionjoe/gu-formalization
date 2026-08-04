---
artifact_type: source-extraction
status: source
doc_type: primary-source-extraction
created: 2026-08-03
work_item: "DRAFT-FQZ-MAP (the named decider computation of explorations/imposter-ab-resolution-proposal-2026-08-03.md §10; standing register item promoted by that proposal). This file is the PRIMARY-SOURCE INGESTION half of the deliverable; the check's verdict lives in explorations/draft-fqz-map-decider-2026-08-03.md."
title: "Primary-source extraction: Weinstein 2021 GU draft, §11 (Observed Field Content) and §12.8–§12.11 — eq (11.1)–(11.6), the p.51 rolled-up complex, the three §11.3 quantum-number tables, eq (12.18)–(12.22), and every passage attaching 'imposter'/'third generation' language to a specific summand. All load-bearing content read visually from rendered pages, not just the text layer."
grade: "VERBATIM EXTRACTION with provenance. Quotes are exact against the rendered PDF pages (born-digital TeX, no OCR involved; transliteration conventions declared below). No mathematical claim is certified here; no repo number is re-derived here; dimension arithmetic shown is labeled as extractor's arithmetic, not the draft's, wherever the draft does not print the number. PRE-DEPOSIT: no claim-status, canon, verdict, bar(b), H59, count, LANE-STATE, or public-posture movement."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
verdict_gate: "Source extraction only. Consequences for the imposter A/B fork are stated ONLY in explorations/draft-fqz-map-decider-2026-08-03.md and remain J5-gated there."
hostile_review_status: "NOT YET REVIEWED — input to the J5 review of the A/B resolution proposal"
depends_on:
  - lab/process/agent-context-pack.md
  - explorations/imposter-ab-resolution-proposal-2026-08-03.md
  - explorations/imposter-reading-adjudication-2026-08-03.md
  - lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md
---

# GU 2021 draft §11–§12.10: primary-source extraction

## 0. Provenance of the PDF obtained (2026-08-03)

- Source URL (the official mirror named by the repo's source pack,
  `lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md` row
  `WG-2021-DRAFT`):
  `https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf`
- Downloaded 2026-08-03. 69 pages, 2,087,649 bytes.
- SHA-256: `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`
  — **exact match to the prior repo receipt** recorded in the source pack
  (same row). This is therefore bit-identical to the file the repo has
  previously cited, not merely the same edition.
- Title page (p.1, verbatim): "Geometric Unity: Author's Working Draft, v 1.0
  / Eric Weinstein / technicalfeedback@geometricunity.org /
  generalfeedback@geometricunity.org / Thursday, April 1st, 2021".
  PDF metadata CreationDate/ModDate: `2021-04-01T16:26:28Z`, Producer
  pdfTeX-1.40.21 (TeX Live 2020).
- Version/date obtained: **the April 1, 2021 "Author's Working Draft v 1.0"**
  — the only public draft edition; no later revision was found at
  geometricunity.org during this run, and the hash match makes edition drift
  moot for repo purposes.
- Reading method: born-digital TeX PDF (NO OCR). Text layer extracted with
  pypdf for search; every load-bearing equation, table, brace label, and
  sentence below was verified by visually reading the rendered page images
  (150 dpi) — pages 49, 50, 51, 52, 53, 61, 62, 63, 65. Page numbers below
  are the draft's printed page numbers, which coincide with PDF page numbers.

**Transliteration conventions (applies to every quote below):** the draft's
slashed bundle glyphs are written `S̸` (slashed S, spinor bundle) and `R̸`
(slashed R, gamma-traceless Rarita-Schwinger bundle); the Hebrew gimel map is
written `ג`; subscripts/superscripts are rendered inline (e.g. `F±_{1/2}`,
`16₊`, `832₋`, `S̸²_L(TX)`). Bold in quotes reproduces bold in the draft.

## 1. §11.1 (pp.49–50): the product rules and the "odd re-appearance" term

§11 "Observed Field Content" opens on p.49; §11.1 "Fermionic Quantum Numbers
as Reply to Rabi's question." is pp.50.

Eq (11.1), p.50:

> W ⊗ S̸_W = S̸_W ⊕ R̸_W    (11.1)

followed verbatim by:

> "breaks into a piece representing the action of gamma matrices as spinor
> endomorphisms and a second piece giving the pure Rarita-Schwinger spin 3/2
> representation corresponding to the sum of the highest weights of the
> factors."

Eq (11.2), p.50:

> W = U ⊕ V  ⇝  S̸(W) = S̸(U ⊕ V) = S̸(U) ⊗ S̸(V)    (11.2)

Eq (11.3), p.50 — a three-row column vector, term order top to bottom exactly
as printed:

> R̸(W) = R̸(U ⊕ V) = ( R̸(U) ⊗ S̸(V)  ⊕  S̸(U) ⊗ R̸(V)  ⊕  S̸(U) ⊗ S̸(V) )    (11.3)

followed verbatim (grammar as printed):

> "with an odd re-appearance of a final term which has purely spinorial with
> no 3/2 spin Rarita-Schwinger component."

Application sentence, p.50 (verbatim):

> "To apply the above to our situation we recognize that ζ represents a
> spinor valued 1-form and ν a spinor on Y with U representing the Horizontal
> and V the Vertical normal bundle Nג to the metric as an embedding
> ג : X → Y.  (11.4)"

## 2. §11.2 (pp.50–52): the 2+1 claim, the rolled-up complex, eq (11.6)

Section heading, p.50 (verbatim): "11.2 The Three Family Problem in GU and
Imposter Generations." (note: "Generations" PLURAL). Epigraph: "'Who ordered
that?' -Isidore Rabi on the Muon".

The 2+1 claim, p.51 (verbatim):

> "The first is that we do not believe that nature has simply repeated
> herself three times albeit at different mass scales. While we do believe
> that a second copy of Fermionic matter matches this description, we believe
> that a third family is merely effectively identical to the other two and,
> presumably, only at low energy."

Eq (11.5), p.51: `ג∗(T∗Y) = T∗X ⊕ Nג  (11.5)`.

### 2.1 The p.51 rolled-up Fermionic complex (structure, visually verified)

The unnumbered display on p.51 ("our rolled up Fermionic complex") is a
diagram whose four corner objects carry, verbatim, the following bracket
structure (upper-left corner shown; the other three corners permute the ±
signs):

> ( ( Z⁻_{1/2} ⊕ Q⁺_{3/2} −−⊕−− F⁻_{1/2} )^{Spin(7,7)⁺}_{832₋}
>   ⊕ ( F⁻_{1/2} )^{Spin(7,7)⁺}_{64₋} )^{Ω¹(S̸₋, Y¹⁴)}_{ζ₋}

Load-bearing structural facts read off the diagram:

1. Each ζ± slot (Ω¹ and its dual Ω¹³ slot) contains a bracket of
   **Z ⊕ Q ⊕ F subscripted 832₊ or 832₋**, PLUS a standalone
   **F bracket subscripted 64₊ or 64₋**. The draft itself prints the numbers
   832 and 64 as dimension subscripts on graded (single-chirality) objects.
2. The ν± slots (Ω⁰ and Ω¹⁴) each contain ONLY a standalone F bracket
   subscripted 64.
3. The superscript on every bracket is Spin(7,7)⁺ or Spin(7,7)⁻ — the
   grading index is ambient Spin(7,7) chirality.
4. The dashed line `−−⊕−−` inside the 832 bracket sits between Q and F
   (Z and Q above the dashes, F below).

### 2.2 Eq (11.6), p.52 — the F/Q/Z definitions (verbatim)

> F±_{1/2} = ( 2∓ ⊗ 16₊ ⊕ 2± ⊗ 16₋ )   Q±_{3/2} = ( 6∓ ⊗ 16₊ ⊕ 6± ⊗ 16₋ )   Z±_{1/2} = ( 2∓ ⊗ 144₊ ⊕ 2± ⊗ 144₋ )    (11.6)

followed immediately, verbatim:

> "for Spin(1,3)×Spin(6,4). The idea being explored here is that the full
> operator depicted decouples effectively into two separate Dirac like
> operators, when there is no vacuum expectation value pulling the various
> sub-fields of ϖ to values significantly above zero. Thus we assert that a
> non-chiral total theory splits at the emergent level into two separate
> chiral theories and that the one above the dashed line corresponds to
> matter in our world with the other sectors not labeled by F to the left
> and above the line are currently dark to us."

Extractor's arithmetic (NOT printed in the draft, flagged as such): each
graded label's dimension follows from its printed factors —
F± = 2·16 + 2·16 = **64** (matching the diagram's printed 64± subscripts);
Q± = 6·16 + 6·16 = **192**; Z± = 2·144 + 2·144 = **576**;
64 + 192 + 576 = **832** (matching the diagram's printed 832± subscripts).
Ungraded (both chirality halves): F = 128, Q = 384, Z = 1152, total 1664.

**Negative finding (full-text search receipt):** the phrase "identical in
form to a true generation" — quoted in-repo as an eq (11.6) gloss via the L1
lens — occurs NOWHERE in the draft (exact-string search over all 69 pages'
text layer, patterns "identical in form" and "true generation"; the only
"true generation" hit is the p.63 sentence quoted in §5 below, which asserts
the OPPOSITE emphasis: the imposter is NOT a true generation because its
representation structure differs). Eq (11.6) and its surrounding p.52 text
also do NOT contain the word "imposter" anywhere.

## 3. §11.3 (pp.52–53): the three quantum-number tables and the imposter-named rows

§11.3 "Explict Values: Predicting the Rest of Rabi's Order." [sic "Explict"]

**Table 1, p.52** (introduced by: "we can now predict what the internal
quantum numbers will likely be if GU is correct as per the following:").
Columns: Names / Multiplicity / Dimension / Structure / Notation / Name(s).
Rows verbatim:

| Names | Mult | Dim | Structure |
|---|---|---|---|
| Left Quarks | 1 | 6 | [3 × 2]^{n=1}_L |
| Left Anti-Quarks | 1 | 3 | [3̄ × 1]^{n=2}_L |
| Left Anti-Quarks | 1 | 3 | [3̄ × 1]^{n=−4}_L |
| Left Leptons | 1 | 2 | [1 × 2]^{n=−3}_L |
| Left Anti-Lepton | 1 | 1 | [1 × 1]^{n=6}_L |
| Left Anti-Lepton | 1 | 1 | [1 × 1]^{n=0}_L |

(Extractor: dimensions sum to 16 — one internal Weyl 16; the true-generation
quantum-number shape.)

**Between the tables, p.52, verbatim:**

> "Another surprise would be a new cousin spin-3/2 'generation' Q⁺_{3/2}, in
> which the logic of the known matters is reversed in the sense that it is
> right handed matter and left handed anti-matter that feel the effects of
> Weak-Isospin."

**Table 2, p.52** (the Q table; no Names filled in): six rows, dims
6,3,3,2,1,1 (sum 16), structures [3̄×2]^{n=−1}_L, [3×1]^{n=−2}_L,
[3×1]^{n=+4}_L, [1×2]^{n=+3}_L, [1×1]^{n=−6}_L, [1×1]^{n=0}_L — the n-values
of Table 1 negated. NOTE: the draft attaches the word "generation" (in scare
quotes) to Q⁺_{3/2} here as a "new cousin", explicitly DISTINCT from both the
known matter and (see §4–§5 below) from the imposter language.

**Table 3, p.53** (no introductory sentence — it follows Table 2 directly
across the page break). Columns: Number / Multiplicity / Dimension /
Structure / Electric Charge / Name(s). Complete verbatim rows:

| Number | Mult | Dim | Structure | Electric Charge | Name(s) |
|---|---|---|---|---|---|
| 1 | 1 | 16 | [8 × 2]^{n=−3}_L | −1, 0 | |
| 2 | 1 | 8 | [8 × 1]^{n=0}_L | 0 | |
| 3 | 1 | 8 | [8 × 1]^{n=6}_L | 1 | |
| 6 | 1 | 12 | [6̄ × 2]^{n=1}_L | +2/3, −1/3 | |
| 5 | 1 | 6 | [6 × 1]^{n=2}_L | +1/3 | |
| 4 | 1 | 6 | [6 × 1]^{n=−4}_L | −2/3 | |
| 12 | 1 | 9 | [3̄ × 3]^{n=2}_L | +4/3, +1/3, −2/3 | |
| 11 | 1 | 9 | [3̄ × 3]^{n=−4}_L | +1/3, −2/3, −5/3 | |
| 8 | 1 | 6 | [3 × 2]^{n=7}_L | +5/3, +2/3 | |
| 7 | 1 | 6 | [3 × 2]^{n=−5}_L | −1/3, −4/3 | |
| 20 | *1 | 6 | [3 × 2]^{n=1}_L | +2/3, −1/3 | |
| 13 | 1 | 6 | [3̄ × 2]^{n=5}_L | +4/3, +1/3 | |
| 10 | 1 | 3 | [3 × 1]^{n=−2}_L | −1/3 | |
| 9 | 1 | 3 | [3 × 1]^{n=−8}_L | −4/3 | |
| 20 | *2 | 6 | [3 × 2]^{n=1}_L | +2/3, −1/3 | **Imposter Quarks** |
| 18 | 2 | 3 | [3̄ × 1]^{n=2}_L | +1/3 | **Imposter Anti-Quarks** |
| 19 | 2 | 3 | [3̄ × 1]^{n=−4}_L | −2/3 | **Imposter Anti-Quarks** |
| 15 | 1 | 3 | [1 × 3]^{n=6}_L | +2, +1, 0 | |
| 16 | 1 | 2 | [1 × 2]^{n=−9}_L | −2, −1 | |
| 23 | 1 | 1 | [1 × 1]^{n=0}_L | 0 | **Imposter Anti-Neutrino** |
| 14 | 1 | 3 | [1 × 3]^{n=0}_L | +1, 0, −1 | |
| 21 | *1 | 2 | [1 × 2]^{n=−3}_L | −1, 0 | **Imposter Leptons** |
| 22 | 1 | 1 | [1 × 1]^{n=6}_L | +1 | **Imposter Anti-Electron** |
| 17 | 1 | 2 | [1 × 2]^{n=3}_L | +1, 0 | |
| 21 | *1 | 2 | [1 × 2]^{n=−3}_L | −1, 0 | |

Extractor's arithmetic and caveats on Table 3 (NOT the draft's statements):

- Taking the printed multiplicity column at face value (*1 → 1, *2 → 2), the
  dimensions sum to exactly **144** — the internal 144 that eq (11.6) places
  inside Z (and only inside Z). The imposter-NAMED rows' quantum numbers
  ([3×2]^{n=1}, [3̄×1]^{n=2}, [3̄×1]^{n=−4}, [1×2]^{n=−3}, [1×1]^{n=6},
  [1×1]^{n=0}) are EXACTLY Table 1's true-generation set; counting one copy
  of each named slot gives 6+3+3+2+1+1 = 16, i.e. one generation-shaped 16
  inside the 144 with 128 of exotics remaining.
- The star notation (rows 20 *1 / 20 *2, and 21 *1 appearing twice, once
  named and once unnamed) is never explained in the draft; whether the
  imposter tag covers one copy or all copies of the starred/multiplicity-2
  slots is NOT decodable from the document alone.
- The draft never states which representation Table 3 decomposes; the
  144-sum is the extractor's identification. FLAGGED as the one genuinely
  ambiguous imposter-labeled surface (see the decider file §3 for what this
  does and does not touch).

## 4. §12.9 (pp.60–61): the effective-chirality mechanism and eq (12.20)

Eqs (12.18)–(12.19), p.61 (verbatim): `ג : X^{1,3} → Y^{7,7}  (12.18)` and
`ג∗(TY^{7,7}) = TX^{1,3} ⊕ N^{6,4}_ג  (12.19)`.

Eq (12.20), p.61, verbatim including the draft's own brace labels (overbrace
on the first line, underbrace on the second):

> ג∗(S̸⁶⁴_L(TY)) = (S̸²_L(TX) ⊗ S̸¹⁶_L(Nג)) ⊕ (S̸²_R(TX) ⊗ S̸¹⁶_R(Nג))   ← overbraced "Luminous Light Standard Model Family Matter"
> ג∗(S̸⁶⁴_R(TY)) = (S̸²_L(TX) ⊗ S̸¹⁶_R(Nג)) ⊕ (S̸²_R(TX) ⊗ S̸¹⁶_L(Nג))   ← underbraced "Dark Decoupled Looking Glass Matter"    (12.20)

followed verbatim:

> "requiring a different view of chirality as both Left and Right handed
> spinors emerge from the branching rules of both Weyl halves confusing the
> picture. Left handed spinors on Y do not remain exclusively Left handed
> on X."

Extractor's note: (12.20) is the draft's own explicit statement of the
grading convention — one ambient chirality half of the plain spinor bundle
is dimension-superscripted **64** by the author (`S̸⁶⁴_L`), and each half is a
two-term chirality-correlated sum of 2⊗16 products. The ungraded 2⊗16-type
object is 64+64 = 128. Note also that (12.20)'s L-half pairs L⊗L ⊕ R⊗R while
(11.6)'s F⁺ pairs 2₋⊗16₊ ⊕ 2₊⊗16₋ (anti-correlated); the two displays sit on
different carriers (plain spinors on Y vs the 1-form-valued complex), and the
relative sign of the correlation is exactly the allocation-dependent
ω₄ω₁₀ = ±ω bookkeeping caveat already filed by Q2 (new-fact 2). Recorded,
not adjudicated.

## 5. §12.10 (pp.62–63): the imposter label and eq (12.22)

Section title, p.62 (verbatim): "12.10 Three Generations Should be Replaced
by 2+1 model of two True Generations and one Effective Imposter Generation".

Opening text, p.62 (verbatim):

> "At the time of this writing, the author is not convinced that we have
> three true generations of matter which differ only by mass. We instead
> posited here that the so-called third generation of matter is instead part
> of pure Rarita-Schwinger Spin−3/2 matter on Y and its Spin−1/2 appearance
> on X is the result of branching rules under pull back from Y where it is
> native:"

Eq (12.22), p.62 — term order top to bottom exactly as printed; the third
term is set in BOLD in the draft and carries an underbrace whose label is
reproduced here in its exact position:

> ג∗(R̸(TY)) = R̸(ג∗(TY)) = R̸(TX ⊕ Nג) = ( R̸(TX) ⊗ S̸(Nג)  ⊕  S̸(TX) ⊗ R̸(Nג)  ⊕  **S̸(TX) ⊗ S̸(Nג)** )    (12.22)
>                                                                                    ⎣___________________⎦
>                                                                                  "Imposter Third Generation"

**The underbrace "Imposter Third Generation" is attached to the THIRD term,
S̸(TX) ⊗ S̸(Nג), and to nothing else.** The first term (R̸(TX) ⊗ S̸(Nג) — the
Rarita-Schwinger-on-X-shaped slot) and the second term (S̸(TX) ⊗ R̸(Nג))
carry no label of any kind in this equation.

Continuation, pp.62–63, verbatim across the page break (footnote marker as
printed):

> "Thus, part of the field ζ ∈ Ω¹(Y, S̸_R) is an ordinary second generation
> spinor in Ω⁰(Y, S̸_L) via the Dirac gamma matrix contraction while the
> complement R̸_R(TY) corresponding to the sum of the highest weights
> contains the imposter third generation which is only revealed under
> decomposition as in the above. Thus, it is not a true generation as it has
> a different representation structure than the other two beyond its obvious
> mass difference.¹³"

Footnote 13, p.63 (verbatim): "Note: we are speaking loosely here as if mass
eigenstates and flavor eigenstates were one and the same."

## 6. §12.11 (p.65): the Witten-synopsis restatement

From the enumerated GU synopsis list, items viii)–ix), p.65 (verbatim):

> "viii) The branching rules of ν leads to the appearance of one family of
> Fermions. ix) ζ branches as a second family due to gamma matrix
> multiplication on Y as TY ⊗ S̸_Y = S̸_Y ⊕ R̸_Y with a Rarita-Schwinger
> remainder. The Spin 3/2 portion of ζ breaks down under pull back to reveal
> a third 'imposter generation' that is merely effective, as it has
> different representation behavior in the full theory."

Extractor's note: viii)–ix) are the draft's own location of the "2" of 2+1 —
ν is family one; ζ's gamma-trace part is family two; the imposter is what
the Spin-3/2 remainder REVEALS under pull-back, i.e. via (12.22)'s labeled
third term. This is the primary-source form of the L1 correction already
carried by the hinge panel (the two true families do not live in the
product-rule decomposition).

## 7. Reading caveats (complete list)

1. Born-digital PDF; no OCR anywhere in the chain. Text-layer extraction was
   used only for SEARCH; every quoted equation, brace, table row, and
   sentence above was verified by eye against the rendered page image.
2. Draft typos preserved: "Explict" (§11.3 heading), "has purely spinorial
   with no 3/2 spin" (p.50), "The branching rules of ν leads" (p.65).
3. The p.51 diagram is dense; the structural facts extracted from it (§2.1
   items 1–4) are limited to bracket membership, printed subscripts
   (832±, 64±), printed superscripts (Spin(7,7)±), form degrees, and the
   dashed line's position. No claim is made here about the diagram's arrows.
4. Table 3's host representation and star semantics are ambiguous in the
   source (§3 caveats); everything else quoted is unambiguous on the page.
5. p.49 carries the draft's own §10 warning "[Note: This diagram is carried
   over from an older version and may contain some inconsistancies until it
   is stabilized. Caveat Emptor.]" — that warning attaches to the §10
   deformation-complex diagram (10.10), NOT to the §11–§12 displays quoted
   here, but it is recorded as evidence of the draft's working-draft state.
