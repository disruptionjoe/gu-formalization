# Changelog v2.9 -- latest-findings integration (2026-07-02)

Trigger: a check found the staged v2.8 paper was behind four findings produced later the same day, none of
which were referenced in either copy. This pass folds those four staged results into the paper's **caveats and
grade language only**. Both copies edited in sync. **No headline claim is strengthened beyond its RESULTS
grade; three generations are still not claimed; internal tier (caveat (e)) is unchanged.** The four results are
`status: staged`, not CANON.md-promoted; the function-space analytic residual remains genuinely open.

## The four findings folded in

1. **External by structure** (`canon/external-by-structure-synthesis-RESULTS.md`, synthesis theorem). The
   sector-interior contribution to the net chiral count is even (2-primary) over the *complete delimited class
   C*; therefore any odd count is *necessarily* external. The earlier "external on present evidence" hedge
   tightens to a structural decomposition -- **modulo the open function-space APS/end + family-index residual.**
2. **Core theorems at the structure level** (`canon/core-theorems-symbolic-proof-RESULTS.md`, symbolic grade).
   The index-nullity / index-conservation theorem, the antilinear null-eigenspace bound, and the 2-primary
   obstruction identities are now proved dimension-independently from the axioms of a cross-chirality Krein
   space, with 22 load-bearing identities sympy-certified to vanish for symbolic entries -- not merely computed
   on the explicit 192-dim carrier. **Still short of a full Lean/Coq formal proof, and it does not touch the
   analytic residual.**
3. **External mechanism concretized** (`canon/external-topological-index-flux-RESULTS.md`, computed +
   independently re-verified). A 2D magnetic-flux Wilson-Dirac has net chiral index = flux number
   (Aharonov-Casher / Atiyah-Singer): any integer, and odd for odd flux. This realizes and pins the parity of
   the paper's external mechanism while privileging no particular value (nothing selects 3).
4. **RS function-space framework** (`canon/rs-function-space-framework-SPEC.md`, spec + computed bulk). The
   bulk RS index `I_{3/2} = 21*sigma/8` is 2-primary by Rokhlin; the boundary-eta and K3 family-index steps are
   precisely-scoped open stubs. Named as the object that will close WC-FUNCTION-SPACE-EXT.

## EDITS APPLIED (v2.9, both copies)

1. **Caveat (c)** (header): "external on present evidence, not necessarily external" -> "external by structure
   modulo the function-space analytic residual" (interior even over the complete delimited class C; odd count
   necessarily external), citing the synthesis result and keeping the internal-tier hedge.
2. **Abstract**: "therefore external" -> "external by structure (modulo the open function-space APS/end
   residual)" with the interior-even / necessarily-external clause; added the index = flux 2D Wilson-Dirac
   concretization.
3. **Grade language on the core theorems** (Section 3 contribution / Section 6 Krein-index passage):
   "machine-corroborated" -> "machine-corroborated, and now proved at the structure level over symbolic entries
   (dimension-independent, sympy-certified)", with the not-a-Lean-proof / not-touching-residual hedge.
4. **Section 6**: paragraph title "The count is therefore external on present evidence" -> "external by
   structure" with the modulo-residual + necessarily-external clause; added the index = flux realization
   sentence.
5. **Status table**: linear-index-conservation row gains the structure-level symbolic-proof note; the
   "external on present evidence" row -> "external by structure (modulo the function-space APS/end +
   family-index residual)"; the external-background row gains the index = flux concretization.
6. **Conclusion**: "On present evidence the generation count is external" -> "By structure ... necessarily
   external, modulo the open ... residual"; added the index = flux realization; "now computationally
   established" -> "now established at the structure level over symbolic entries for the core theorems, and
   computed + engine-swept for the class exhaustion."
7. **Reproducibility appendix**: the four new canon files added to the per-result canon list.
8. **Version bookkeeping**: .md version marker 2.8 -> 2.9 and version-history paragraph; .tex header comment
   2.8 -> 2.9 with a one-line v2.9 note.

## NOT CHANGED

- Theorem 1, Theorem 2, the antilinear index-nullity theorem, the CRT structure, and every integer are
  untouched. This pass edits caveats and grade language, not results.
- The analytic residual (APS/end + family-index) is genuinely open; the "external by structure" upgrade is
  always stated *modulo* it.
- Internal tier unchanged (caveat (e)). All four canon files are `status: staged`, not CANON.md-promoted.

## STATUS

Publication remains **DEFERRED** (Joe). This pass brings the staged paper current with the four same-day
findings; it strengthens the caveats' framing without adding any claim above its repository grade. Publication
flips only on Joe's review and the CANON.md-promotion decision.
