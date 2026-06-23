---
title: "Split-Rank Reconciliation Audit"
status: exploration
doc_type: audit
updated_at: "2026-06-23"
problem_label: "split-rank-reconciliation-audit"
verdict: "scalar BC1/FJ rank-one chain superseded; tau-twisted route remains conditional"
---

# Split-Rank Reconciliation Audit

## Verdict

The corrected `sigma_B` analysis is now the governing scalar statement:

> For the actual metric symmetric pair `(SL(4,R), SO_0(3,1))` with
> `dsigma_B(X) = -J X^T J^{-1}`, `J=diag(1,1,1,-1)`, the scalar split-rank is
> `3`. The scalar restricted-root system is rank-3 `A3` with multiplicity-one roots,
> not rank-one `BC1` with `(m_1,m_2)=(7,1)`.

Consequently, the scalar Flensted-Jensen equal-rank test fails: `split-rank(G/H)=3`
while `rank(K/(K cap H))=1`. The scalar rank-one `BC1` pole ladder
`nu_n=(2n+1)/2`, scalar `rho=9/2`, scalar `(m_1,m_2)=(7,1)`, and scalar
`Lambda_RS^{FJ}=3/2` do not currently prove `ind_H(S_R^{eff})=8` or
`ind_H(D_GU)=24`.

The tau-twisted route is distinct. It may still survive, but only as the conditional
route proposed in `explorations/oq3b-rs-index-8-2026-06-23.md`: for
`L^2(G x_H tau_RS)`, an effective rank reduction `3 -> 1` is asserted via
`rank_correction(tau_RS)=2`. That is reconstruction-grade until the relevant
Oshima-Matsuki/Kobayashi-Oda hypotheses and the twisted multiplicity-one statement are
checked for this specific `tau_RS`.

## Replacement Language

Use these exact replacements when refreshing stale claims.

**S1 - scalar metric pair.**

> For the actual metric symmetric pair `(SL(4,R), SO_0(3,1))` with
> `dsigma_B(X) = -J X^T J^{-1}`, `J=diag(1,1,1,-1)`, the scalar split-rank is `3`.
> The scalar restricted-root system is rank-3 `A3` with multiplicity-one roots. The
> scalar rank-one `BC1` model with `(m_1,m_2)=(7,1)` is superseded and must not be
> cited as data for scalar `L^2(G/H)`.

**S2 - scalar Flensted-Jensen consequence.**

> The Flensted-Jensen equal-rank criterion for scalar
> `L^2(SL(4,R)/SO_0(3,1))` fails: `split-rank(G/H)=3` while
> `rank(K/(K cap H))=1`. Scalar FJ multiplicity-one, the `BC1` pole ladder
> `nu_n=(2n+1)/2`, `rho=9/2`, and `Lambda_RS^{FJ}=3/2` do not currently prove
> the generation count.

**S3 - wrong-rank source.**

> The earlier `split-rank=1` bracket computation belongs to the block-conjugation
> `sigma_A` model, or to an artificial one-dimensional line inside the actual pair. It
> is not the scalar metric pair with fixed algebra `so(3,1)`.

**T1 - tau-twisted route.**

> The remaining analytic route is tau-twisted: for `L^2(G x_H tau_RS)`, OQ3b
> proposes an effective rank reduction `3 -> 1` via `rank_correction(tau_RS)=2`.
> This is reconstruction-grade and conditional until the Oshima-Matsuki/Kobayashi-Oda
> hypotheses and the twisted multiplicity-one statement are verified for this specific
> coefficient representation.

**P1 - rank-independent physical count.**

> The rank-independent physical count may still be cited separately: the RS sector has
> `C^32` physical modes after gamma-trace and gauge fixing; the chiral half is `C^16`,
> hence `dim_H=8` H-lines. This does not verify scalar FJ/BC1 Plancherel claims.

**R1 - RC3 spectral data.**

> Demote the RC3 rank-one spectrum `{8,14,18,20}/R_s^2`, `M_KK^2=8/R_s^2`,
> `rho=9/2`, and `(m_1,m_2)=(7,1)` to an obsolete scalar-BC1 calculation unless the
> same values are explicitly rederived in the tau-twisted coefficient problem. Do not
> present them as verified scalar data for `(SL(4,R), SO_0(3,1))`.

## File/Line Remediation List

### Shared Status And Canonical Docs

- `canon/no-go-class-relative-map.md:32` - already aligned. It correctly says the
  rank-one `BC1` chain is superseded and no replacement is needed.

- `RESEARCH-STATUS.md:105` - already aligned. It correctly demotes `(m1,m2)=(7,1)`,
  scalar FJ poles, and `Lambda_RS^{FJ}=3/2`. No replacement is needed.

- `RESEARCH-STATUS.md:80` - acceptable if kept generic. "Complements F4 Flensted-Jensen
  approach" should not be expanded into scalar `BC1`; if refreshed, append T1.

- `NEXT-STEPS.md:35,37` - already aligned. Keep these as the status-row correction.

- `NEXT-STEPS.md:51` - stale by implication: the OC1 row cites an Atiyah-Schmid/FJ
  spectral gap from RC3 as if the scalar RC3 gap survives. Replace the parenthetical
  `(gap = 8/R_s^2 from RC3; ...)` with: "conditional on the tau-twisted discrete sector;
  the scalar RC3 rank-one gap is superseded by the sigma_B correction."

- `NEXT-STEPS.md:53` - internally contradictory. The first half correctly says
  `FAILS_AS_STATED`; the later `RC1-OQ2 ROOT MULTIPLICITY GATE` block re-promotes FJ
  split-rank `1`, `BC1`, and `(7,1)`. Replace that root-multiplicity block with S1, S2,
  and T1. Also replace "root multiplicity CONDITIONALLY_RESOLVED" with:
  "root multiplicity superseded for scalar `L^2(G/H)`; tau-rank correction remains the
  primary open analytic gate."

- `NEXT-STEPS.md:73` - stale embedded VZ/RC1/RC3 summary. Replace the RC1 sentence
  beginning "RS L^2 modes exist..." with T1 plus P1. Replace the RC3 sentence beginning
  "BC_1 structure verified..." and the `rc3-harish-chandra` sentence with R1.

- `NEXT-STEPS.md:76` - stale N5 summary. Replace "`Flensted-Jensen equal-rank condition
  is satisfied (split-rank min(p,q)=1)`" and "`OQ1 CAS verification of split-rank=1`"
  with S1, S2, and T1.

### Progress Ledger

- `DERIVATION-PROGRESS.md:364,385` - stale N5 summaries. Replace the statements that
  the equal-rank condition is satisfied and split-rank is `1` with S1 and S2.

- `DERIVATION-PROGRESS.md:548,562,590,639` - stale "split-rank-1 verified" and
  Flensted-Jensen multiplicity-one summaries for N5/plancherel/weyl notes. Replace
  with T1 for the analytic route and P1 for the physical-count route.

- `DERIVATION-PROGRESS.md:681,737` - stale RC3 summaries that confirm `BC1`,
  `(m_1,m_2)=(7,1)`, and `rho=9/2`. Replace with R1.

- `DERIVATION-PROGRESS.md:751,772,814,980` - stale downstream claims that use the
  FJ/RC3 discrete sector as established. Replace with: "conditional on the tau-twisted
  route T1; scalar FJ/BC1 no longer supplies the proof."

- `DERIVATION-PROGRESS.md:905,940` - already aligned and should be treated as the
  superseding ledger entries.

- `DERIVATION-PROGRESS.md:926` - mostly aligned. Keep the distinction between
  `sigma_A` and `sigma_B`, but ensure the tau route is labelled conditional as in T1.

- `DERIVATION-PROGRESS.md:933` - stale after the corrected OQ1 computation. Replace the
  entire "two distinct rank notions" paragraph with S1, S2, and T1.

### OQ1 And RC1 Sources

- `explorations/oq1-split-rank-verification-2026-06-23.md:2,6,21-46` - stale
  title/frontmatter/opening claims still say `dim(a_q)=1` and the FJ criterion passes.
  Replace with S1 and S2. Suggested title:
  `"OQ1: Split-Rank Verification for SL(4,R)/SO_0(3,1) - dim(a_q)=3 under sigma_B"`.

- `explorations/oq1-split-rank-verification-2026-06-23.md:448-460,540-596` - stale
  internal reconciliation that tries to save `BC1`/rank `1`. Replace with S3. Keep
  `603-789` as the authoritative corrected conclusion.

- `explorations/rc1-discrete-series-verification-pack-2026-06-23.md:36-58,125-230` -
  already aligned. This is a primary negative source and should be cited for the scalar
  demotion.

- `explorations/rc1-root-multiplicity-check-2026-06-23.md:2,14-15,25,64,108-118,
  281-288,369-377,550,667-678,685-693,731-777` - stale. The note re-establishes
  `BC1`, `(7,1)`, and FJ split-rank `1` for scalar `L^2(G/H)`. Replace the verdict with
  S1 and S2; if any residue is retained, label it "obsolete scalar-BC1 line model" and
  not a verified gate.

- `explorations/rc1-rs-kk-zero-mode-2026-06-23.md:64-78,102-120,133-150,326-327,
  381-390,462-497,533-541,592-606,636-657,692-705` - stale unless rewritten as the
  tau-twisted route. Replace scalar `BC1` and `Lambda_RS^{FJ}=3/2` language with T1;
  replace scalar RC3 spectrum references with R1; retain P1 as an independent count.

### N5 Notes

- `explorations/n5-discrete-series-gl4r-2026-06-23.md:55-175,802-823,852-865,
  2667,2932,2960-2965,3246-3247,3371-3374,3400-3411,3466-3476,3494,3512,
  3533-3749` - stale. These sections say scalar split-rank `1` is verified and FJ
  equal-rank passes. Replace with S1, S2, T1, and P1.

- `explorations/n5-plancherel-multiplicity-2026-06-23.md:25-26,43-45,201-211,
  306-316,381,459,582-583,606-610` - stale. Replace "FJ multiplicity-one for
  split-rank-1 pairs" with T1, and mark the `8` count as conditional on the twisted
  multiplicity-one theorem or as P1 if using the physical count.

- `explorations/n5-parthasarathy-casimir-sl4r-2026-06-23.md:457` - acceptable. It is
  generic and does not assert scalar `BC1`; if refreshed, add "after the scalar
  `sigma_B` correction, this is an alternative/twisted representation-theory route."

- `explorations/weyl-group-s4-orbit-2026-06-23.md:20-21,34,56,207-210,250-253,
  322-323,347-358,426,448-449,486-489,542-543` - stale where it says FJ
  split-rank `1` is verified. Replace with T1 for the analytic route and P1 for the
  rank-independent count. Keep the exact `S_4` orbit enumeration.

### RC3 Notes

- `explorations/rc3-delta-n-spectrum-gl4r-2026-06-23.md:257-258,305-307,611-613,
  694-701,724` - stale scalar rank-one spectrum. Replace with R1 and reopen the
  normal-spectrum computation for the corrected A3/tau-twisted setting.

- `explorations/rc3-root-multiplicity-bc1-2026-06-23.md:2,9,15-24,34-36,44-50,
  475-500,811,825-878,912-914,931-945,957-995,1007-1008` - stale. Replace the
  verdict with: "SUPERSEDED for scalar `SL(4,R)/SO_0(3,1)` by sigma_B split-rank `3`;
  retain only as an obsolete rank-one line/block model unless rederived in the tau-twisted
  problem." Use R1 for spectral conclusions.

- `explorations/rc3-harish-chandra-c-function-2026-06-23.md:17,31,35,45,54-57,
  111-112,170,462-463,679-712,720-805,863-1158,1255,1313-1335,1347-1361` -
  stale scalar `BC1` c-function. Replace with R1; if a c-function is needed, recompute it
  for A3 or for the explicitly justified tau-twisted coefficient problem.

- `explorations/rc3-oq3-lorentzian-casimir-2026-06-23.md:869,1064` - stale only in
  the normalization assumption. Replace "rank-1 symmetric space ... rho=9/2" with
  "old rank-one normalization; superseded for scalar sigma_B, pending A3/tau recomputation."
  The Lorentzian Casimir sign arguments can remain if decoupled from `rho=9/2`.

### Downstream Notes

- `explorations/oc1-noncompact-atiyah-jannich-2026-06-23.md:43-44,239,252-268` -
  stale or mixed. Replace verified scalar split-rank `1` with S1/S2. Keep
  `315-317,358` as the correct remaining gate language, but make it the leading statement.

- `explorations/signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md:88-91,329`
  - stale. Replace verified split-rank `1` and CAS target `Lambda_RS^{FJ}=3/2` with T1.

- `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md:72-73` - stale.
  Replace "OQ1 split-rank=1 (VERIFIED)" with S1/S2.

- `explorations/signed-readout-oq2d-gu-contact-2026-06-23.md:52-55,76,94,107-110,
  355-356,419-421,500-502,568-570,614` - stale or overconfident. Replace scalar
  FJ multiplicity-one with T1; record the GU graph count as conditional on the
  tau-twisted route or as a separate P1-based reconstruction.

- `explorations/oq-weyl3-limit-discrete-series-2026-06-23.md:57,138-139,332-335,
  496-507,515-547,615,621,632,663-699,764,809,935-988` - stale scalar `BC1`
  framework. Replace with S1/S2 and, where discussing coefficient bundles, T1.

- `explorations/oq3c-index-additivity-2026-06-23.md:48,207-212,466,479,597,617-619,
  673` - stale dependencies. Replace the FJ/BC1 path with T1 and keep the algebraic
  Atkinson-Schur additivity result separate from analytic existence of the RS discrete sector.

- `explorations/taf-h3-contact-2026-06-23.md:75-76` - stale cross-reference. Replace
  "Flensted-Jensen split-rank=1 verified" with "scalar FJ rank-one route superseded;
  generation-count contact, if used, is conditional on the tau-twisted route."

- `papers/what-geometric-unity-needs-to-do-next-v6.md:126-136,228,260` - stale public
  surface. Replace the scalar equal-rank claim with S1/S2 and describe the analytic pillar
  as the conditional tau-twisted Oshima-Matsuki/Kobayashi route T1.

## Safe Phrasing Going Forward

Short status phrasing:

> Scalar FJ/BC1 is superseded by the corrected `sigma_B` computation: split-rank is `3`
> and scalar equal-rank fails. The generation-count analytic route is no longer a scalar
> `BC1/(7,1)` claim; it is conditional on the tau-twisted effective rank-correction
> argument, plus independent physical degree-of-freedom counting.

Longer technical phrasing:

> The corrected metric-pair involution is `dsigma_B(X)=-JX^TJ^{-1}`. With this involution,
> `p_G cap q_B` has maximal abelian subspace `span{H_1,H_2,H_3}`, so the scalar split-rank
> is `3`; the scalar restricted-root system is `A3`, not `BC1`. The rank-one computation
> belongs to `sigma_A` or a non-maximal line and must not be used for scalar
> `L^2(SL(4,R)/SO_0(3,1))`. The only FJ-style survival route is the tau-twisted
> coefficient problem, where `rank_correction(tau_RS)=2` is a named unverified gate.

## Audit Scope

Explicitly inspected the requested shared docs:
`NEXT-STEPS.md`, `DERIVATION-PROGRESS.md`, `RESEARCH-STATUS.md`,
`canon/no-go-class-relative-map.md`,
`explorations/oq1-split-rank-verification-2026-06-23.md`, and
`explorations/rc1-discrete-series-verification-pack-2026-06-23.md`.

Also inspected related N5/RC1/RC3/OQ downstream notes found by stale-pattern search,
including `n5-discrete-series-gl4r`, `n5-plancherel-multiplicity`,
`n5-parthasarathy-casimir`, `rc1-root-multiplicity-check`, `rc1-rs-kk-zero-mode`,
`oq3b-rs-index-8`, `oq-weyl3-limit-discrete-series`, `oc1-noncompact-atiyah-jannich`,
`rc3-delta-n-spectrum`, `rc3-root-multiplicity-bc1`,
`rc3-harish-chandra-c-function`, `rc3-oq3-lorentzian-casimir`, and downstream
signed-readout/OQ3c/Weyl notes.
