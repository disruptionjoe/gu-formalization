# CHANGELOG v2.9.1 — function-space residual closure scope note (2026-07-03)

**Type:** additive scope note. No verdict change, no claim promotion, no new theorem stated in the
paper. Internal tier throughout.

## What changed

Two loci in both copies (`.md` and `.tex`) gained a one-sentence scope update recording that the
three residual terms of the v2.8 conditional function-space theorem — (1) gap well-posedness,
(2) the APS/noncompact-end eta correction, (3) the family-index term — are each **discharged on
faithful stand-in models** by the same `sigma_1 (x) B` cross-chirality mechanism:

- the **abstract caveat block** (the function-space clause of caveat (c)/(d)): added that the residual
  terms are discharged on faithful models, with the actual RS boundary eta on `RP^3` 2-primary, leaving
  the true-RS-`Y14`-bundle computation as the one open residual;
- the **Section 6 conditional-theorem remark**: same, with the per-item mechanism (gap set by the end;
  APS/end eta = 0 in the class; `c1(E_-) = c1(upper) + c1(lower)` cancels).

## Sources

- `canon/function-space-index-conservation-residual-closure-RESULTS.md` (items (1)-(3) discharged on
  faithful models; computed + independently re-verified; 8 scripts under `tests/function-space-ext/`
  and `.../verify/`, all exit 0).
- `canon/rs-boundary-eta-2primary-RESULTS.md` (STEP 2: the actual RS boundary operator's reduced
  eta-bar on `RP^3 = L(2;1)` is 2-primary, computed grade).

## What did NOT change

- The **verdict stays OPEN**; nothing derives three (the external index is any integer).
- The paper's many "function-space extension open" / "modulo the function-space residual" statements
  remain literally correct — the true-RS-`Y14`-bundle extension IS still open. The note is additive
  and narrows the open residual to the true-bundle computation; it does not contradict those phrasings.
- No status-table verdict cell was upgraded; no Theorem statement was restated.
- Publication remains **DEFERRED / Joe-gated** (WI-032); this is a repo-local claim-status edit, not a
  submission action.

## Consistency

Part of the 2026-07-03 coherent-cluster canon promotion (Joe-authorized). Owner-surface sweep run
across `CANON.md`, `RESEARCH-STATUS.md`, `canon/` RESULTS, `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md`,
and this paper (`lab/process/runbooks/claim-status-consistency-quality-workflow.md`).
