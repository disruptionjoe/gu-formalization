# Staging notes -- Located, Not Forced

**Status:** candidate — **GO-to-post, ratified by Joe 2026-07-22 (direct chat): publish LNF FIRST, standalone.**
The 2026-07-02 deferral is **LIFTED** (both gating cards WC-ENUM-COMPLETENESS and WC-ANTILINEAR-BOUND closed at
computed grade the same day; see the 2026-07-22 section at the bottom). Sequence: LNF first, then the
odd-primary boundary paper as the Part II follow-on. Remaining before public = Joe-side mechanical submission
steps only (arXiv endorsement check, Overleaf compile, shortened metadata abstract) — Joe posts.
`.tex` is the arXiv source; `.md` is the readable copy.
**Honest grade:** the headline result is theorem-grade and GU-independent. Honesty discipline: clean.

## What is staged (the claim)

In an explicit real Clifford Rarita-Schwinger sector (Cl(p,q), p+q=14; the j=1 generation triplet carrying a
purely cross-chirality (+96,-96) Krein form): every obstruction to a net chiral generation count established
in this sector is 2-primary, so by the CRT split pi_3^s = Z/24 = Z/8 (+) Z/3 the no-go is arithmetically
**blind** to the odd-torsion summand where a homotopy count could live; every linear Krein-isometric operator
conserves the net chiral index at zero (finite-dimensional theorem -- no Fredholm theory); the only
symmetry-respecting chiralizer is antilinear and frame-trivial; and the order-3 carrier (e_R = 1/12) **locates
the slot without filling it.** Three generations is explicitly **not** claimed.

## Gate pass

1. Title matches the theorem-grade core ("Two-Primary Obstructions **Cannot Force**..."). PASS.
2. No retracted/downgraded wording: grades stated explicitly; the antilinear leg is marked a finite
   adversarial hunt (not a closed proof); "external on present evidence," not "necessarily external." PASS.
3. Citations: web-verified bibliography inline (Wang 2023, Wan-Wang-Yau, Garcia-Etxebarria-Montero, Sati-Shim,
   McLaughlin, Kirby-Melvin, Adams, Seade, etc.). PASS.
4. Sharpest open issue acknowledged in-text: the torsion-count reading is flagged as an interpretive premise
   (under a literal integer-index reading the same obstructions would forbid an odd count). PASS.
5. No overlap with another staged candidate (the methods paper is a distinct track). PASS.

## Open items (disclosed, not blockers for the title claim)

- **The torsion-count reading is a premise, not a result.** The "located order-3 carrier" presupposes that a
  generation count would live as a 3-primary class in pi_3^s; the paper itself invokes Hom(Z/3,Z)=0, i.e. the
  order-3 class cannot literally *be* an integer count. The front matter must keep this unmissable so no reader
  mistakes the located-carrier narrative for a derivation of three generations.
- **Theorem 1 is proven by enumeration** over the listed obstructions; the universal phrasing ("no obstruction
  established in this sector...") should be read as scoped to the enumerated classes, not an impossibility over
  all conceivable obstructions.
- **The antilinear non-existence leg is closed over a delimited class** (WC-ANTILINEAR-BOUND, 2026-07-02:
  an index-nullity theorem over ALL Krein-compatible antilinear operators, down to symmetry-free;
  `canon/antilinear-bound-RESULTS.md`). Residual: non-Krein antilinear operators fail admissibility (they do
  not act on physical states); the function-space extension remains open (WC-FUNCTION-SPACE-EXT). It was never
  needed for the title claim.

## Before posting (Joe's side)

Compile the `.tex` (Overleaf), run any final deep-research pass, then -- on Joe's explicit go -- submit to
arXiv (primary hep-th; secondary math-ph, math.AT). On confirmation it is live, move this folder up to
`papers/published/` with the arXiv id recorded.

## Readiness pass 2026-07-02 (v2.4) -- verdict: READY pending Joe-side steps

Two independent review agents (content-vs-canon; submission mechanics) checked the paper. Content verdict:
nothing in the 2026-06-30 chase-to-kill sweep or any later file contradicts or weakens any sentence; MOVE-4
strengthens the external-source narrative and is now cited as a scoped consistency remark. All required edits
applied (see the .md changelog v2.4 entry). Static .tex analysis: clean, single-file, embedded bibliography,
all cites/labels resolve, no external dependencies; `\pdfoutput=1` added.

Remaining steps are Joe-side only:

1. **Endorsement check (longest lead time, do first):** verify the arXiv account can submit to hep-th; a
   first-time submitter without institutional email likely needs an endorser. Start this before anything else.
2. **One Overleaf compile** (no TeX toolchain on this machine): confirm zero errors; visually check the
   front-matter fbox, the wide Section 7 display equation, the Section 11 longtable, and the 20 references.
3. **Shortened metadata abstract:** the in-PDF abstract (~2,950 chars) exceeds arXiv's 1,920-char metadata
   limit. A ~1,750-char draft is in the submission runbook (JoeOps card WI-032 source notes).
4. **Submit:** single .tex upload; license = arXiv nonexclusive 1.0 (preserves journal options); primary
   hep-th, cross-list math-ph + math.AT; comments field per runbook. Known risk: possible moderation hold /
   gen-ph reclassification (first-time submitter, GU-adjacent subject); mitigations are already in the text.
5. **Post-live:** move folder to `papers/published/`, record the arXiv id here, and update the path references
   listed in the readiness review (README, RESEARCH-PROGRAM, papers/README, tri-repo division-of-labor doc,
   canon depends_on frontmatter).

## Final publication gate 2026-07-02 (v2.5) -- verdict: reputation-attachable, with Joe-side open items

Independent final gate under the mandate "refine until you would attach your reputation; prefer removing weak
claims to defending them." Canon audit found no claim above its repo grade; all changes are credibility-layer.
Substantive edits (full list + justifications: `CHANGELOG-v2.5-publication-gate.md`): cut "referee-proof" and
the F1-flagged "evidence tilts toward one" (replaced with "no computed quantity in this program equals three");
conceded Theorem 2's classical Krein-space core and the NCG Krein-SM precedent (novelty now: embedding +
assembly only); softened the residual "only object that can bridge" (Sections 5, 7) to "natural bridge"; added
caveat (e) + a Verification-status paragraph implementing the ratified three-tier vocabulary (everything here
is internally established at most -- reproduced, not replicated); added GU's own "Caveat Emptor" disclaimer of
draft eq. 10.10 and the Furey-Hughes algebraic-lane citation; scoped the .md abstract's forcing-slot "hardens"
sentence to toy level. Citations spot-verified by fetch (2605.26202, 2409.17948, 1504.02088, 2010.04960);
Pati-Salam verification rerun fresh, 19/19 PASS. Both copies synced at v2.5. Joe-side steps of the v2.4 list
all still apply, plus: confirm the eq.-10.10 / p. 49 locator against the GU PDF, and recheck the Overleaf
compile (one new bibitem, taller fbox).

## Adversarial peer review 2026-07-02 (reviewed v2.4) -- publication DEFERRED pending two work cards

An adversarial peer review of v2.4 arrived 2026-07-02, after the v2.5 gate pass. Full 8-major + 3-minor
disposition table: `papers/drafts/prepublish-review-tracker.md` (located-not-forced section). Small surgical
edits applied to both copies as **v2.5.1** (`CHANGELOG-v2.5.1-adversarial-review.md`): Theorem 1's
enumeration-conditionality raised into the abstract and theorem statement; the Pati-Salam "1" flagged
chain-relative; every "locates the slot" marked as interpretation with `Hom(Z/3,Z)=0` adjacent; a Theorem 2
finite-dimensional-kinematics scope sentence; "single decider / honest gate" colloquialisms retitled; a
computational pointer for the Spin(9,5) Hom-vanishing remark.

**Joe's instruction (2026-07-02): publication is DEFERRED** until the two journal-gating work cards close
(cards live in `NEXT-STEPS.md`, "2026-07-02 Publication-Gating Work Cards"):

- **WC-ENUM-COMPLETENESS** -- prove a classification theorem showing Theorem 1's 7-item enumeration exhausts a
  precisely delimited covariant-operator/anomaly class, or run an adversarial enumeration-extension engine
  (gauge-coupled + boundary variants included) whose census is exhaustively 2-primary.
- **WC-ANTILINEAR-BOUND** -- convert the antilinear finite adversarial hunt into a delimited non-existence
  proof or an exhaustive certificate over a rigorously bounded class, residual stated.

**WC-FUNCTION-SPACE-EXT** (Theorem 2's sections/differential-operator extension) is post-publication and does
not gate. The Joe-side v2.4/v2.5 submission steps (endorsement check, Overleaf compile -- now with the v2.5.1
deltas: retitled Section 8, slightly taller fbox-adjacent abstract, no new bibitems -- shortened metadata
abstract) remain valid but are on hold behind the two gating cards. On card closure: fold any resulting
class-delimitation statements into the paper (likely a v2.6), rerun the publication gate, then proceed to the
"Before posting" steps above on Joe's explicit go.

## Gating-card status 2026-07-02 (same day, later): both cards now carry STAGED results

- **WC-ENUM-COMPLETENESS: CLOSED at computed grade** (outcome (i)): class-C census complete, extension engine
  finds no sector-interior escape, boundary sharp. `canon/enum-completeness-class-c-RESULTS.md` +
  `tests/enum-completeness/`. Paper text NOT edited by that card (Theorem 1 wording upgrade pauses for Joe).
- **WC-ANTILINEAR-BOUND: CLOSED** (outcome (a)+(b)): the antilinear hunt upgraded to a delimited index-nullity
  theorem over all Krein-compatible antilinear operators (declared symmetry ladder down to symmetry-free), with
  the hunted frame-active CII swap operators exhibited in closed form and shown non-forcing; residual stated.
  `canon/antilinear-bound-RESULTS.md` + `tests/antilinear-bound/`. Minimal paper edits applied as **v2.5.2**
  (`CHANGELOG-v2.5.2-antilinear-bound.md`) per that card's explicit instruction: caveat (d), abstract, intro
  item 3, Section 6, status-table row, conclusion -- both copies in sync.

**Publication remains DEFERRED**: it flips only when Joe reviews both gates (and decides the CANON.md
promotions and the Theorem 1 wording upgrade). The Joe-side submission steps above then apply to v2.5.2+.

## Third adversarial review + v2.6 enum fold-in (2026-07-02, later)

A third adversarial peer review (of v2.5.1+v2.5.2) landed 2026-07-02. Verdict: no errors found; **arXiv-ready in
current form** (hep-th / math-ph / math.AT); journal publication would benefit from external validation of the
antilinear index-nullity theorem and progress on the function-space extension. Its lead criticism (#1) was that
enumeration completeness remained the weakest structural link -- Theorem 1 still read "completeness of the
enumeration is open." Every other criticism was already-fixed (v2.5.1/2.5.2) or already-disclosed scope the
reviewer explicitly accepts (antilinear delimitation, finite-dimensional/function-space, unbuilt source action,
internal-only verification, modest broad payoff).

**Action (Joe-authorized):** fold the closed WC-ENUM-COMPLETENESS result into the paper as **v2.6**
(`CHANGELOG-v2.6-enum-completeness.md`). Theorem 1, the abstract, intro item 1, and the status table now state
the enumeration is complete for the delimited class C (computed grade, engine-swept beyond C with a sharp
boundary; completeness over the unrestricted / function-space theory remains open). Added the reviewer's
requested one-sentence representation-theory method for the Spin(9,5) Hom-vanishing remark. The GEM 3-primary
contrast and the `order-3-class -> integer-3` future-work target the review also asked for were already present
and left as-is. All three enum-completeness certificates were re-run this pass (exit 0) before the completeness
language was written.

**Still pending Joe (unchanged):** CANON.md promotion of both RESULTS files; the publication flip (stays
DEFERRED); git commit/push. Both gates' results are now reflected in the paper text (antilinear v2.5.2, enum
v2.6); only outside replication moves the internal-tier verification status (caveat e).

## Reviewer #2 antilinear strengthening -> v2.7 (2026-07-02, later)

Joe asked to take a stab at review criticism #2 (the delimited antilinear class leaves loopholes) and to update
the paper if it held up. It held up. Result (`canon/antilinear-nonkrein-admissibility-RESULTS.md`, computed +
independently re-verified on own recursive-doubling gammas + `Cl(7,7)`): the antilinear index-nullity theorem's
admissible class is not the Krein-compatible operators but the strictly larger **null-eigenspace class**
(re-gradings whose chirality eigenspaces are K-null), and index nullity holds on all of it; a nonzero count
requires a K-definite re-grading that is not a chirality (it carries the vectorlike +-96) and does not act on the
physical sector.

**Paper updated v2.7** (`CHANGELOG-v2.7-antilinear-nonkrein.md`, both copies): caveat (d), abstract, intro item 3,
Section 6, status table, and conclusion now state the null-eigenspace class and re-scope the residual (the earlier
"outside the Krein class admissibility fails" was too strong). Scripts:
`tests/antilinear-bound/nonkrein_physical_admissibility.py` (61 asserts) +
`tests/antilinear-bound/verify/nonkrein_indep_check.py` (69 asserts). This closes the KINEMATIC half of #2; the
QFT effective / non-perturbative (function-space) half remains the open WC-FUNCTION-SPACE-EXT.

**Still pending Joe (unchanged):** CANON.md promotion of the RESULTS files; the publication flip (stays DEFERRED);
git commit/push. This is a strengthening, not a new gate -- publication readiness is unchanged (the third review
already rated the paper arXiv-ready).

## Latest-findings integration -> v2.9 (2026-07-02, later)

A currency check found the staged paper (last folded at v2.8) was behind four staged results produced later the
same day, none referenced in either copy. Folded in as **v2.9** (`CHANGELOG-v2.9-latest-findings-integration.md`,
both copies in sync), **caveats and grade language only, no headline claim strengthened beyond its RESULTS grade**:

- **caveat (c)** "external on present evidence" -> **external by structure** -- the sector-interior contribution
  is even over the complete delimited class C, so an odd count is necessarily external -- *modulo* the open
  function-space APS/end + family-index residual (`canon/external-by-structure-synthesis-RESULTS.md`);
- **core theorems** (index-nullity / index-conservation, antilinear null-eigenspace bound, 2-primary obstruction
  identities) noted as now proved at the **structure level over symbolic entries** (dimension-independent, 22
  sympy-certified identities), still short of a Lean/Coq formal proof and not touching the analytic residual
  (`canon/core-theorems-symbolic-proof-RESULTS.md`);
- **external mechanism concretized** -- net chiral index = flux number in a 2D Wilson-Dirac model, odd for odd
  flux (Aharonov-Casher / Atiyah-Singer) (`canon/external-topological-index-flux-RESULTS.md`);
- **RS function-space framework** referenced as the object that will close WC-FUNCTION-SPACE-EXT (bulk index
  2-primary by Rokhlin; boundary-eta and K3 family-index steps open) (`canon/rs-function-space-framework-SPEC.md`).

Edits: caveat (c), abstract, Section 6, status table, conclusion, reproducibility canon list, version
bookkeeping (both copies). Also in this pass, the `.md`/`.tex` **conclusion and reproducibility appendices,
which an interrupted earlier edit had left truncated, were restored from the last clean commit** before the v2.9
edits were applied.

**Still pending Joe (unchanged):** CANON.md promotion of the four staged RESULTS files; the publication flip
(stays **DEFERRED**); git commit/push. The analytic residual (APS/end + family-index) is genuinely open; the
"external by structure" upgrade is always stated modulo it. Internal tier unchanged (caveat (e)).

## Big-swing corroboration fold -> v2.10 (2026-07-03)

Folded the 2026-07-03 big swing (R1-R5) and answered the same-day adversarial peer review of the v2.9.1
canon-promotion commit. **Caveat/remark/citation + status-table only; no verdict change; count stays OPEN;
publication remains DEFERRED.** Both copies (`.md`, `.tex`) in sync. See `CHANGELOG-v2.10-big-swing-fold.md`.

- The review's load-bearing cautions (#1/#2: "external by structure" leans on *faithful stand-in models";
  #3: enumeration completeness) are answered by **R1**: residual APS/end-eta + family-index items now
  discharged on the **actual** `Cl(9,5)` RS operator (not stand-ins), narrowing the one open residual to the
  definite `Y14`-fiber pushforward (= the external source action); and a table-free parity theorem backstops
  Theorem 1 completeness. Folded as exploration-grade corroboration, not headline strengthening.
- **R2** (Dai-Freed / spin-bordism): SM boundary data does not pin the count mod-3 (`Omega^Spin_5(B G_SM)
  (x) Z_(3) = 0`, color triality) -- new exploration-grade support in Section 8.
- **R3** (`canon/signed-readout-boundary-theorem-RESULTS.md`) and **R4**
  (`canon/two-arena-rep-theory-core-RESULTS.md`) are now canon and cited; standalone drafts live at
  `papers/drafts/signed-readout-boundary-theorem-2026-07-03.md` and
  `papers/drafts/two-arena-rep-theory-core-2026-07-03.md`.

The peer review recommended "clean to post (hep-th)"; **publication stays Joe-gated** — the review is not
authorization. The one pre-submission mechanical item it named (the `.md`/`.tex` consistency pass) was done
in this fold.

## Publication RATIFIED — GO, LNF first (2026-07-22, Joe direct chat)

**Joe ratified in direct chat (2026-07-22): publish LNF FIRST, standalone — the 2026-07-02 deferral is
LIFTED.** This is the authorizing decision the earlier "stays DEFERRED / Joe-gated" notes were waiting on.
Trail: both cards that caused the deferral closed at computed grade on 2026-07-02 (WC-ENUM-COMPLETENESS,
WC-ANTILINEAR-BOUND), the third adversarial review rated the paper arXiv-ready, and Joe's sequence decision
(`system-runtime/mailboxes/gu-formalization/20260722-lnf-oddprimary-sequence-decision.md`) confirmed LNF is
good/useful standalone and must not be suppressed.

- **Sequence:** LNF first (this paper); the odd-primary boundary paper
  (`papers/candidates/generation-number-boundary-odd-primary/`) is the Part II follow-on and CITES LNF —
  keep the two distinct (LNF = the no-go/census; odd-primary = the localization).
- **Status:** GO-to-post. LNF now joins PP3 on the "ready for Joe to post" list.
- **Remaining (Joe-side mechanical only, unchanged from the v2.4 list):** arXiv endorsement check, one Overleaf
  compile, shortened <1920-char metadata abstract; then submit (primary hep-th; or Zenodo), then move this
  folder to `papers/published/` and record the DOI / arXiv id in `papers/published/INDEX.md`.
- **Separate, still open (NOT part of this GO):** the CANON.md promotions of the RESULTS files previously
  flagged "pending Joe" remain a distinct decision — publishing the paper does not itself promote canon.
