# Changelog v2.5 -- final publication gate (2026-07-02)

Mandate (Joe, verbatim intent): refine until reputation-attachable; optimize for correctness, clarity,
credibility, usefulness to skeptical experts; prefer removing weak claims to defending them. Both copies
(.tex canonical, .md readable) edited in sync. Substantive changes only; wording-neutral edits omitted.

## CUT

1. **"referee-proof" self-description** (Conclusion, both copies). Calling one's own contribution
   referee-proof is advocacy, not adjudication; a hostile referee feasts on it. Now plain "GU-independent
   contribution."
2. **"the evidence tilts toward one"** (Section 9, status table, Conclusion; both copies). The repo's own
   review tracker (F1) warns that one-generation phrasing reads as a prediction, and the paper's own appendix
   scope paragraph says the Pati-Salam "1" is structural and "says nothing about how many generations occur" --
   an internal inconsistency. Replaced with the strictly earned statement: "no computed quantity in this
   program equals three" / "no computation performed in this program yields the integer three."

## WEAKENED

3. **Theorem 2 novelty claim** (Section 10, both copies). "the Krein index-conservation theorem is ...
   without precedent" overclaimed: the theorem's core (a maximal definite subspace of a form pairing two
   complementary Lagrangians is a graph) is elementary and of a classical Krein-space kind; the repo's own
   prior-art assessment grades the vectorlike/real-pseudoreal backbone as standard rep theory and notes
   Krein-space Standard-Model precedent in NCG (Lorentzian spectral SM, arXiv:2010.04960 -- title
   web-verified 2026-07-02). Novelty is now claimed only for the embedding + the specific assembly.
4. **"The only object that can bridge the two arenas is anomaly inflow"** (Section 5) and **"bound only by
   anomaly inflow"** (Section 7, both copies). The post-2.3 pass softened "sole possible bridge" to "natural
   bridge" in the intro but left the same overclaim in Sections 5 and 7. Now "natural bridge" everywhere --
   uniqueness of the bridge was never proven.
5. **Abstract forcing-slot sentence** (.md; the .tex abstract never had it). "hardens the verdict from
   conjecture to computation" now scoped: "hardens the RS-side gate verdict ... at toy level (the actual
   stabilized action remains unbuilt)." Same qualifier added to the Section 8 closing sentence.
6. **"The one place the literature does obtain an odd constraint"** (Section 1, both copies). False as
   stated -- the paper itself cites Wang (N_gen in 3Z) and Wan-Wang-Yau (n=3). Now "Where the literature does
   obtain an odd constraint -- Garcia-Etxebarria-Montero ... is the sharpest example -- ...".
7. **.md abstract "two theory-independent impossibility results"** -> "structural results" (Theorem 1 is
   enumeration-scoped; "impossibility" overstates it, and the .tex abstract never used the word).

## STRENGTHENED-WITH-EVIDENCE

8. **Verification-tier disclosure** (new caveat (e) in the front-matter box + a "Verification status"
   paragraph in Data Availability/.md reproducibility appendix). Implements the three-tier vocabulary Joe
   ratified 2026-07-02 (lab/roadmap/tri-repo-division-of-labor-2026-07-02.md): every result is at most
   *internally established* (reproduced, not replicated); no internal step can promote to externally
   established. This preempts the strongest hostile meta-objection ("machine-verified by the same process
   that wrote it") by stating it first.
9. **GU's own "Caveat Emptor" disclaimer** (Section 10, both copies). "does not build the matter action" is
   now sourced: the draft's candidate source term (eq. 10.10) is author-disclaimed ("until it is stabilized.
   Caveat Emptor.", working draft p. 49; recorded in CANON.md / DERIVATION-PROGRESS RS-BRST entry). The
   central gate is GU's own admission, not our characterization.
10. **Furey-Hughes algebraic-lane citation** (Section 10 + .tex bibliography). The repo's prior-art
    assessment directs situating the paper in the active algebraic-three-generations lane; arXiv:2409.17948
    abstract verified by fetch 2026-07-02 (two generations as spinors, third via Cartan factorization).

## CLARIFIED

11. **Postnikov remark** (Theorem 1 remark, both copies): scare-quoted "lost in the mod-2 Postnikov system"
    (read as an unattributed quotation) -> plain statement "invisible to a mod-2 Postnikov/Adams analysis."
12. **.md Section 7 normalization provenance** synced to the .tex's careful v2.3 statement: the composite
    e_R = (p_1/2)/24 is ours, assembled from three stated conventions (McLaughlin/Sati-Shim; Kirby-Melvin;
    Adams), not a formula quoted verbatim from any one source. (The .md previously said "standard topology
    (Kirby-Melvin; the e = p_1/48 framed-bordism formula)", which the .tex itself disavows.)
13. **Stale .tex header comment** "(v2.3)" -> "(v2.5)"; thebibliography width arg {18} -> {99} (now 21
    entries); .md internal version -> 2.5 with this changelog summarized in the version-history paragraph.

## STRUCTURAL

None. Section order, theorem statements, proofs, all numbers, and the status-table grades are unchanged; the
2026-07-02 canon audit (two-primary-lemma, CRT-RESULTS, single-decider, forcing-slot, carrier-mass,
frame-triviality, boundary-eta, source-action-SW, ghost-parity-krein) found no claim above its repo grade in
the v2.4 text; v2.5's changes are all at the phrasing/credibility layer plus the two evidence additions above.

## Verification performed this pass

- Canon-vs-paper claim audit (all nine load-bearing RESULTS files + DERIVATION-PROGRESS corrections since
  2026-06-29): no numeric mismatch; no grade exceeded.
- Citations: Wan-Wang-Yau arXiv:2605.26202 title verified by fetch; Furey-Hughes 2409.17948 and Sati-Shim
  1504.02088 abstracts verified by fetch; arXiv:2010.04960 title verified by fetch. All other bibliography
  entries were web-verified in the v2.2/v2.3 passes per STAGING-NOTES.
- Reran `lab/active-research/pati_salam_chain_verification.py` in a fresh sandbox: 19/19 PASS, exit 0 (the
  appendix's load-bearing "1"). Heavier scripts (e.g. `net_chiral_index_invariant.py`) exceed this sandbox's
  45 s limit and were not rerun; their files are byte-identical to git HEAD.
- Arithmetic spot-checks (1664 = 2^7*13; 96 = 2^5*3; -5376 = -2^8*3*7; -672; e_R = 2/24 = 1/12; CRT
  components (2,2); Tr Y = Tr Q = 0 over the labeled 16; denom(B_2/4) = 24; |Weyl(D7)| factorization): all pass.

## OPEN ITEMS (need Joe)

1. **Overleaf compile** still pending (no TeX toolchain here); v2.5 added one bibitem, one fbox caveat, and
   three paragraphs -- recheck the fbox height and the references count (now 21).
2. **Shortened metadata abstract** (~1,920-char arXiv limit) still needs the runbook draft; consider whether
   caveat (e) merits a one-line mention there.
3. **"Caveat Emptor" page anchor**: the quote and eq. 10.10 / PDF p. 49 locator come from CANON.md's
   RS-BRST record; eyeball the GU draft PDF once to confirm the page number before submission.
4. **Furey-Hughes bibliography fields**: authors/title taken from the repo's prior-art assessment plus an
   abstract fetch (title page did not render); confirm the exact title capitalization on the arXiv landing page.
5. **Heavy test scripts not rerun this pass** (sandbox timeout); if desired, rerun tests/generation-sector/
   and tests/decider/ locally before submission for a fresh exit-0 log.
6. The antilinear non-existence leg remains an open finite hunt (disclosed in-text; unchanged).
