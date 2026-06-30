# Deep-research adversarial prompt -- PASS 2 (for the hardened v2.3 PDF)

Use after the first hostile pass has been absorbed. Paste the text below into a web-enabled deep-research model
with the compiled `located-not-forced-...-2026-06-29.pdf` (version 2.3) attached.

---

You are a hostile, meticulous referee **and** a research-integrity auditor. The attached paper, "Located, Not
Forced" (**version 2.3**), is a *revision* that has already absorbed one hostile deep-research review; your job
is two-fold: **(1) verify that the specific fixes below actually landed and are themselves correct** (a wrong or
incomplete fix is worse than the original), and **(2) find anything new the revision introduced, plus anything
the first pass missed.** Do not praise or soften. Assume the most skeptical expert reader, including a researcher
whose own prior work the paper cites (e.g. Juven Wang). **Use web search to verify every checkable claim and
cite the URL.**

**What you can rely on this time.** The PDF now contains the *full bibliography* inline (audit every entry). All
numeric/representation-theoretic claims are reproducible from the public repository at
`github.com/disruptionjoe/gu-formalization` under `tests/` (so "opaque numerology" is checkable, not a
black box). The paper's value proposition remains **honesty and grading discipline** (theorem-grade vs computed
vs reconstruction-grade vs gated vs open); hold it ruthlessly to that standard.

**Be calibrated on severity.** Mark each finding MUST-FIX (a genuine error, a real overclaim a hostile expert
would exploit, or an integrity issue), SHOULD-FIX (improves rigor/clarity), or NICE-TO-HAVE. Do **not**
recommend downgrading a claim that is actually supported merely because it is ambitious; distinguish "this is
wrong or embarrassing" from "this is a presentation preference." A correct claim should be hardened, not weakened.

**Verify these v2.3 fixes specifically -- did each land, and is it sound?**

1. **Theorem 2, now a finite-dimensional proof.** The previous pass objected that "connectedness of `U(96,96)`
   does not prove an index is conserved; you need a Fredholm/spectral-flow setup." The revision replaces this
   with an elementary finite-dimensional argument and demotes connectedness to a one-line remark. Check, hard:
   (a) Is the *net chiral index* now defined as a genuinely invariant integer (`chi(P)=dim pi_+(P)-dim pi_-(P)`
   on a physical subspace `P`), not a tautology? (b) Is the proof airtight: cross-chirality => the chirality
   eigenspaces `W_+,W_-` are K-Lagrangian => any maximal K-positive `P` meets each trivially => `P` is a graph
   projecting isomorphically onto both => `chi(P)=0`, invariant under any linear K-isometry? (c) Is the claim
   "no Fredholm theory is needed -- the carrier is finite-dimensional and `chi` is exactly an integer" correct,
   so the prior objection is genuinely defused rather than reworded? (d) Is the corrected signature scope right:
   `chi=0` in the physical indefinite signatures `(9,5),(7,7)`, with Euclidean `(14,0)` grading-*aligned*
   (`|chi|=96`) as a control -- and is the prior "verified across (9,5),(7,7),(14,0)" claim now gone?

2. **The `e_R = p_1/48 = (p_1/2)/24 = 1/12` normalization.** The revision adds a "normalization conventions"
   paragraph. Verify each link: (i) `p_1/2` generates `H^4(BSpin;Z)` -- check the cited sources (McLaughlin,
   Pacific J. Math. 155 (1992); Sati-Shim, arXiv:1504.02088); (ii) the stabilization `pi_3(SO(3))->pi_3(SO)` is
   multiplication by 2 (Kirby-Melvin); (iii) the generator of `pi_3^s=Z/24` has Adams `e`-invariant `1/24`
   (Adams). Is the composite stated honestly as the authors' own (not quoted), and is the sign-flip robustness
   argument correct? Can a referee still exploit a generator/sign/normalization ambiguity?

3. **The "order-3" precision.** A footnote now states the framed class is `2 in Z/24` (order 12), whose `Z/3`
   projection is the order-3 element. Verify the arithmetic (CRT image `(2,2)`; `Z/8` component order 4; `Z/3`
   component order 3) and that no remaining occurrence asserts the *element* has order 3.

4. **The torsion-count assumption on page one.** The abstract and introduction now state that "located, not
   forced" is contingent on a torsion-theoretic reading of the obstruction data (under a literal integer-index
   reading the obstructions would forbid an odd count). Is this disclosure adequate and early, or still buried?

5. **The novelty claim, now narrowed.** The revision concedes no novelty for the bare `Z/24=Z/8(+)Z/3`
   factorization or the use of `pi_3^s=Z/24` (both Wang's; Wang's full title, containing `24/8=3`, is restored
   in the bibliography), and claims novelty only for: (a) the *inverse* reading -- a 2-primary no-go is
   arithmetically blind to a 3-primary count (Wang *forces* `N_gen in 3Z`; this paper shows a no-go *cannot*
   force the count), (b) the Clifford Rarita-Schwinger embedding, (c) the Krein/`U(96,96)` index-conservation
   theorem. Is even this narrowed claim defensible? Search for prior work anticipating any of the three. Is
   Wang 2023 (arXiv:2312.14928) and Wan-Wang-Yau (arXiv:2605.26202) now characterized accurately and completely?

6. **CRT relabel and AZ class-CII data.** The CRT split is now labeled standard (the *reading* is the
   contribution); the antilinear escape now states the class-CII symmetry data (chiral grading plus an
   antiunitary `C` with `C^2=-I`). Are both now defensible against a technical correction?

**Then the full hostile sweep -- find NEW problems the revision introduced and anything the first pass missed:**

- **Math.** Re-derive the two-primary meta-theorem, the index-conservation theorem (per item 1), and check
  `Hom(Z/3,Z)=0` and the relative/rank-invariant claim. Did the Theorem 2 rewrite introduce any inconsistency
  with the rest of Section 5 (the structural no-go, the antilinear leg)?
- **Fabrication / citations.** Audit EVERY bibliography entry now that the full list is present: existence,
  correct authors/date/title (including the new McLaughlin and Sati-Shim entries), and accurate
  characterization. Flag any hallucinated ID, misattribution, or truncated/altered title.
- **Internal consistency.** Abstract vs body vs status-of-claims table after the edits; the antilinear-leg
  "finite hunt, not a closed proof" caveat consistent in all five places; no claim stronger in one section than
  its evidence elsewhere.
- **Physics / reconstruction.** Are the GU-specific identifications still clearly reconstruction-grade? Is the
  characterization of GU fair (the "2+1" hedge, effective chirality, unbuilt matter action)?
- **Submission-readiness.** Is the "does NOT claim three generations" disclaimer unmistakable? Any LaTeX issue?
  Anything that draws an arXiv moderation flag or an easy public rebuttal?

**Output.**
1. **Overall verdict**: safe to post publicly now, or after what level of fixes?
2. **Fix-status table** for items 1-6 above: for each, did the v2.3 fix LAND and is it SOUND (yes / partial /
   no), with the specific remaining issue if any.
3. **Prioritized punch-list** of everything else: MUST-FIX / SHOULD-FIX / NICE-TO-HAVE, each with quoted text,
   the problem, the specific fix, and a source URL for any factual claim.
4. **Fabrication-check section**: every reference, verified or flagged, with URL.
5. **The single most damaging objection** a hostile expert could still raise, and whether the paper survives it.

Be specific; quote section/line; cite sources. If a claim cannot be verified, say so and recommend the
conservative fix. The goal: after addressing your report, the paper cannot be embarrassed by any expert reader.

---

**Note for the human (Joe):** if it returns MUST-FIX items, bring them back and we apply the same judicious
loop -- harden where the claim is correct, downgrade only on genuine reputational risk, decline where the
reviewer lacks context. The repo `tests/` are ground truth for any disputed number.
