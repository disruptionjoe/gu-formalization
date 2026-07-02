# Changelog v2.5.2 -- antilinear-bound closure (2026-07-02)

Trigger: work card **WC-ANTILINEAR-BOUND** (journal-gating, priority 2; `NEXT-STEPS.md`, 2026-07-02
publication-gating section) closed. The paper's antilinear non-existence leg -- caveat (d), previously a
*finite adversarial hunt* over an infinite-dimensional space -- is upgraded to a delimited **index-nullity
theorem** over the class `S` of **all Krein-compatible antilinear operators** on the 192-dim carrier
(`M^dag K M = lambda K-bar`, `lambda` real nonzero; every covariance from full `so(4)+so(5,5)` down to
symmetry-free; no square or continuity assumption). Full result, class definition, per-rung ladder census, and
the outside-class residual: `canon/antilinear-bound-RESULTS.md`. Executable certificates:
`tests/antilinear-bound/` (three scripts, 247 hard asserts, all exit 0; independently re-verified on an
own-gamma substrate and on `Cl(7,7)`, with a Euclidean `(14,0)` control that fires `|chi| = 96` to prove the
premise is load-bearing). Both copies (.tex canonical, .md readable) edited in sync. **All edits are small and
surgical; no theorem, proof, number, or grade of the paper's core changed.** The card's failure condition (an
admissible frame-non-trivial antilinear chiralizer that forces a nonzero index) did NOT fire.

## EDITS APPLIED (v2.5.2, both copies)

1. **Caveat (d) upgraded (abstract front matter).** "The antilinear non-existence leg is an open finite
   adversarial hunt, not a closed proof" -> "the antilinear non-existence leg is *closed over a delimited
   class* (every Krein-compatible antilinear operator on the carrier, any covariance down to symmetry-free: an
   index-nullity theorem, `canon/antilinear-bound-RESULTS.md`); outside that class admissibility itself fails,
   and the function-space extension remains open (WC-FUNCTION-SPACE-EXT)."

2. **Abstract body.** The one-line statement of the antilinear result now reads that the antilinear loophole is
   closed by a delimited index-nullity theorem (all Krein-compatible antilinear operators, down to
   symmetry-free, keep every physical subspace's net chiral index at 0), replacing the "finite adversarial
   hunt / none found" phrasing.

3. **Intro contribution item 3.** Retitled to "An index-conservation theorem, a necessary antilinear escape,
   and a class-level structural no-go." The antilinear clause now states the leg is closed over the delimited
   Krein-compatible class (function-space extension open), rather than reporting an unfinished hunt.

4. **Section 6 ("Theorem 2: index conservation and the necessary antilinear escape").** The paragraph that
   previously recorded the frame-non-trivial antilinear (CII) chiralizer as "the one genuine loophole ... was
   [hunted, none found]" now adds that the hunt has since been closed by a delimited theorem
   (`canon/antilinear-bound-RESULTS.md`, `tests/antilinear-bound/`): over the class of all Krein-compatible
   antilinear operators on the carrier, every operator maps the chirality pair to a K-Lagrangian pair, so no
   admissible antilinear re-grading moves the net chiral index off 0 (machine-certified; independently
   re-verified, including on `Cl(7,7)`, with a Euclidean control confirming the premise is load-bearing). The
   sharp, non-suppressed point is added: the hunted frame-active CII swap operators **exist** in the class
   (exhibited in closed form) and still force nothing, because Krein compatibility alone pins the index -- the
   linear leg is theorem-grade (index conservation), the antilinear leg is now closed over the delimited class.

5. **Status-table row.** The "No interior operator forces an odd chiral count; the count is external on present
   evidence" row now annotates: linear leg theorem-grade (index conservation); antilinear leg closed over the
   delimited Krein-compatible class (index-nullity theorem, `canon/antilinear-bound-RESULTS.md`; residual:
   non-Krein operators fail admissibility, function-space extension open).

6. **Conclusion.** The closing summary of why the count is not internal now states that the antilinear side is
   closed over the delimited Krein-compatible operator class (function-space extension remains open), matching
   the abstract and Section 6.

7. **Version bookkeeping.** .tex header comment -> v2.5.2; .md version-history paragraph gains the v2.5.2
   antilinear-bound entry summarizing this addendum and pointing here.

## NOT CHANGED (recorded)

- **No core claim, theorem, proof, integer, or grade moved.** The only target integers anywhere in the
  antilinear artifacts are the carrier's own `(+96, -96)` and `0`. Theorem 2 (finite-dimensional linear index
  conservation) is untouched; the new content is the antilinear companion bound.
- **No CANON.md promotion.** `canon/antilinear-bound-RESULTS.md` is staged, not promoted; the promotion pauses
  for Joe per the card's process gate.
- **Function-space extension** (sections, Fredholm indices, spectral flow) stays the separate post-publication
  card **WC-FUNCTION-SPACE-EXT**; it does not gate publication and is named as the honest residual alongside
  the non-Krein (admissibility-failing) operators.

## STATUS

Publication remains **DEFERRED** (Joe, 2026-07-02). Both journal-gating cards now carry staged, executable
results: **WC-ENUM-COMPLETENESS** (`canon/enum-completeness-class-c-RESULTS.md`) and **WC-ANTILINEAR-BOUND**
(`canon/antilinear-bound-RESULTS.md`). Publication flips only when Joe reviews both gates and decides the
CANON.md promotions and the Theorem 1 wording upgrade. The Joe-side submission steps (endorsement, Overleaf
compile, shortened metadata abstract) in `STAGING-NOTES.md` then apply to v2.5.2+.
