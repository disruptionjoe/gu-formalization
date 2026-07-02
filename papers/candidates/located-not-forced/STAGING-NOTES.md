# Staging notes -- Located, Not Forced

**Status:** candidate (staged; not submitted). `.tex` is the arXiv source; `.md` is the readable copy.
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
