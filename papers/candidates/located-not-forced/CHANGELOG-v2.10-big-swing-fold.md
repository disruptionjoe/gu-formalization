# CHANGELOG v2.10 — big-swing corroboration fold (2026-07-03)

**Type:** additive corroboration fold. No verdict change, no headline claim strengthened beyond its
grade, no new theorem stated in the paper. Internal tier throughout; generation count stays **OPEN**.
Publication remains **DEFERRED / Joe-gated**.

## Context

Folds the 2026-07-03 "big swing" (R1–R5, `explorations/big-swing-2026-07-03/`, `tests/big-swing/`, all
certificates exit 0) into the paper, and responds to the 2026-07-03 adversarial peer review of the
v2.9.1 canon-promotion commit. That review's two load-bearing cautions were (#1/#2) that "external by
structure" leaned on residuals discharged only on *faithful stand-in models*, and (#3) that Theorem 1's
completeness was a scoped enumeration. R1 addresses both directly; the fold keeps the review's discipline
(every load-bearing "external by structure" sentence stays caveated; R1/R2 enter as **exploration-grade**
corroboration that *narrows but does not close* the residual, not as headline strengthening).

## What changed (both copies, `.md` and `.tex`)

- **Caveat (d):** added that a 2026-07-03 exploration discharges the APS/end-eta and family-index residual
  terms on the **actual** `Cl(9,5)` RS operator over a source-parameter loop (not only stand-in models),
  narrowing the one open residual to the definite `Y14`-fiber pushforward — which is the external unbuilt
  source action itself. Marked exploration-grade; true-bundle computation still open; verdict unchanged.
- **Section 4 (Theorem 1):** new exploration-grade remark — a table-free parity theorem (centrality +
  Schur + even-dimensionality of the appearing `so(4)+so(10)` irreps) backstops the enumeration's
  2-primary verdict without a census, addressing the "is the enumeration complete?" concern structurally.
- **Section 5 (CRT two-arena):** noted the CRT split + 2-primary blindness is now canon as a standalone
  Lean-backed restatement (`canon/two-arena-rep-theory-core-RESULTS.md`, R4).
- **Section 8:** noted the `Spin(9,5)` Hom-vanishing is now canon fact (A) of the two-arena core (re-run
  exit 0); added a new exploration-grade remark that on the global Dai-Freed / spin-bordism layer, SM
  boundary data does **not** pin the count — `Omega^Spin_5(B G_SM) ⊗ Z_(3) = 0` (color triality), so the
  carrier arena inflow could populate is empty for the SM. Removes a forcing mechanism; does not derive three.
- **Status table:** three new rows recording the R1 parity backstop, the R1 actual-operator residual
  discharge, and the R2 mod-3-arena-empty result, each marked exploration-grade.
- **Version line:** 2.9.1 → 2.10 with the fold summary.

## Grades / sources

- R1 (exploration-grade, not canon): `explorations/big-swing-2026-07-03/R1-rs-operator-residual-and-odd-count-nogo.md`;
  `tests/big-swing/R1_actual_rs_operator_residual.py` (exit 0), `tests/big-swing/R1_kill_odd_index_isotypic.py` (exit 0).
- R2 (exploration-grade): `explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md`,
  `explorations/anomaly-and-bordism/sm-as-boundary-cobordism-frontier-2026-07-03.md`.
- R3 (canon 2026-07-03): `canon/signed-readout-boundary-theorem-RESULTS.md`; standalone draft
  `papers/drafts/signed-readout-boundary-theorem-2026-07-03.md`.
- R4 (canon 2026-07-03): `canon/two-arena-rep-theory-core-RESULTS.md`; standalone draft
  `papers/drafts/two-arena-rep-theory-core-2026-07-03.md`.

## What did NOT change

- Verdict stays **OPEN**; nothing derives three.
- The "external by structure … modulo the function-space residual" phrasing stays literally correct — the
  true-RS-`Y14`-bundle extension is still open. R1 narrows the residual to the definite fiber pushforward
  (which *is* the external datum); it does not close it.
- No status-table verdict cell for the headline claims was upgraded; no theorem statement was restated.
- Publication remains **DEFERRED / Joe-gated**. The peer review's "clean to post" recommendation is noted
  but is not authorization; that is Joe's call.
