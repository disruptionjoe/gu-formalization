# Changelog v2.5.1 -- adversarial-review response addendum (2026-07-02)

Trigger: an adversarial peer review of the paper arrived 2026-07-02. It reviewed **v2.4**; the v2.5
publication-gate pass (same date, `CHANGELOG-v2.5-publication-gate.md`) had already landed some of its points.
Triage ratified by Joe 2026-07-02: act on what is worth acting on, add the remaining work to the project,
**publication DEFERRED** until the journal-gating work is done. Full 8-major + 3-minor disposition table:
`papers/drafts/prepublish-review-tracker.md` (located-not-forced section). Both copies (.tex canonical,
.md readable) edited in sync. All edits are small and surgical; no theorem, proof, number, or grade changed.

## EDITS APPLIED (v2.5.1, both copies)

1. **Theorem 1 conditionality made unmissable (reviewer point 1, partial).** The abstract now states in bold
   that the no-go is conditional on the enumerated obstruction list and that completeness of the enumeration is
   open; the Theorem 1 statement itself now reads "The no-go is conditional on this enumerated list: completeness
   of the enumeration is an open question ..." (previously "scoped to this enumerated list" -- true but
   skimmable); the .md theorem label became "Theorem 1 (a no-go conditional on the enumerated obstruction
   list)"; intro contribution item 1 carries the same sentence. The substantive residual (prove or exhaust the
   enumeration) is work card **WC-ENUM-COMPLETENESS** (journal-gating).
2. **Pati-Salam "1" flagged chain-relative (reviewer point 7, residual).** Added in Section 8 (decider bullet)
   and the Pati-Salam appendix scope paragraph: "The Spin(7,7) Pati-Salam chain is one reduction among many
   possible symmetry-breaking chains; the integer 1 it yields is chain-relative, not chain-independent." Status
   table row annotated "chain-relative -- one reduction chain among many". (The v2.5 pass had already cut the
   "evidence tilts toward one" phrasing; this closes the residual.)
3. **"Locates the slot" marked as interpretation everywhere (reviewer point 6, residual).** All four sites
   (abstract, intro item 4, Section 7 paragraph -- retitled "It locates but does not fill (properties computed;
   'locates' is interpretation)" -- and the Conclusion) now mark "locates" as an interpretive gloss under the
   torsion-count premise, with the `Hom(Z/3,Z)=0` category-error flag adjacent at each site. The computed
   content (tangentiality p_1=4, vectorlikeness, homotopy-fixedness) is separated from the interpretive gloss.
4. **Theorem 2 scoped to finite-dimensional kinematics (reviewer point 2).** One added scope sentence (a
   "Scope." paragraph in the .md; appended to the "no Fredholm theory is needed" remark in the .tex): Theorem 2
   is finite-dimensional kinematics on the 192-dim carrier; the function-space extension (sections,
   differential operators, Fredholm indices, spectral flow) is a separate named open problem. The extension
   itself is work card **WC-FUNCTION-SPACE-EXT** (post-publication).
5. **Colloquialisms softened (reviewer minor points m1, m2).** Section 8 retitled "The deciding computation, and
   the gate" (was "The single decider, and the honest gate"); intro item 5 retitled to match; "Honestly gated,
   not fabricated" -> "Gated, not fabricated"; "single-decider integers" -> "decider integers" in the
   reproducibility/Data Availability text. Test-directory and canon file names unchanged.
6. **Computational pointer for the Spin(9,5) Hom-vanishing remark (reviewer minor point m3).** The
   `dim Hom_{Spin(9,5)}(S^+ (x) S^+, Lambda^0) = 0` remark (carrier-mass capstone) now cites
   `tests/chase/MOVE-4/move4_spinor_square_forms.py` and the independent re-check
   `tests/chase/MOVE-4/verify/indep_check.py`.
7. Version bookkeeping: .tex header comment -> v2.5.1; .md internal version -> 2.5.1 with this addendum
   summarized in the version-history paragraph.

## NOT EDITED (recorded dispositions)

- **Point 3 (antilinear leg is a hunt, not a proof):** already disclosed in-text (caveat (d)); the substantive
  fix is work card **WC-ANTILINEAR-BOUND** (journal-gating), not prose.
- **Point 4 (no dynamics; S_IG unbuilt):** accepted-scope -- gated on the repo's top-level source-action card;
  the paper states the gate rather than papering over it.
- **Point 5 (GU provenance) and the advocacy/novelty residue of points 5/6:** addressed in v2.5 (cut
  "referee-proof", conceded Theorem 2's classical core and NCG precedent); the remaining provenance concern is
  strategic and accepted-scope (presentation already maximally detached).
- **Point 7 (Pati-Salam "1" presented as decisive):** the decisive-flavored phrasing was already cut in v2.5;
  only the chain-relativity sentence (edit 2 above) was added in v2.5.1.
- **Point 8 (does not resolve the generation problem):** accepted-scope -- the paper explicitly does not claim
  to ("we do not claim three" is title-level).

## STATUS CHANGE

Publication **DEFERRED** (Joe, 2026-07-02) pending closure of **WC-ENUM-COMPLETENESS** and
**WC-ANTILINEAR-BOUND** (work cards in `NEXT-STEPS.md`, 2026-07-02 publication-gating section).
`WC-FUNCTION-SPACE-EXT` is post-publication and does not gate. STAGING-NOTES.md updated accordingly; the v2.4/
v2.5 Joe-side submission steps (endorsement, Overleaf compile, metadata abstract) remain valid but on hold.
