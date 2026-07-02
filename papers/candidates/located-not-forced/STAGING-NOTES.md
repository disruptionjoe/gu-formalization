# Staging notes -- Located, Not Forced

**Status:** candidate (staged; not submitted). **Publication DEFERRED 2026-07-02 (Joe)** pending
WC-ENUM-COMPLETENESS and WC-ANTILINEAR-BOUND (see the adversarial-review section at the bottom).
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
- **The antilinear non-existence leg is open** (a finite adversarial hunt over an infinite-dimensional space,
  no counterexample found). It is not needed for the title claim.

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
