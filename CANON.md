---
title: "Project Canon"
status: canon
doc_type: canon
updated_at: "2026-07-03"
---

# Project Canon

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

## Canonical Posture

This repository optimizes for finding the truth, using Geometric Unity as a generative test case: a bold,
high-information, contested conjecture rich enough to spawn precise falsifiable hypotheses that we drive to
resolution. The objective is the true structure that survives the drive (often GU-independent) and a
reliable method for finding it, not a verdict on GU.

This is not a proof of Geometric Unity, not a claim that Eric Weinstein's presentation is complete, and not
an attempt to prove GU true or false, vindicate or refute Weinstein, or make the program look right. Any
verdict on GU is a byproduct, and every such byproduct is a scientific success.

**Primary research question (2026-06-28): the Firewall-Boundary Hypothesis.** The repository's
primary falsification target is now whether every successful reconstruction converges on a
firewall-like BOUNDARY object rather than a closed internal completion. This supersedes the prior
default that the endpoint must be a closed system. Attack it, do not defend it.
See `canon/firewall-boundary-hypothesis.md`.

See `RESEARCH-POSTURE.md` for the canonical research philosophy.

## Canonical Claims

1. **Truth is the mission; GU is the generative engine.** Take GU as the bold conjecture that
   generates falsifiable hypotheses, drive each to a verdict, and keep what survives. Reconstructing the
   missing mathematics, derivations, reductions, categorical language, and analytic machinery is how the
   engine runs, not the goal.
2. **Constructive obstruction discipline.** When a branch blocks, ask what object,
   stronger structure, richer category, or invariant would remove the obstruction before
   deciding whether the obstruction is intrinsic.
3. **No-go theorem discipline.** The target no-go families must be handled through their
   exact assumptions, known class exits, and failure modes.
4. **Specification before promotion.** Any candidate path must state its substrate,
   observer, pairing, causal order, emergence class, coordination loop, source-to-shadow
   map, or equivalent proof object before making physics claims.
5. **Finite control first.** Type II1 or non-embeddable spectral Standard Model ideas must
   preserve the finite Connes-Chamseddine control case before they can claim relevance.
6. **GU-independent results are co-equal products.** The surviving structure is often GU-independent
   (signed-readout, six-axis specification, no-go class-relativity, the generation-multiplicity rep
   theory, reconstruction methodology). It is elevated, not secondary: the scaffold is allowed to fall
   away once it has pointed at something real.
7. **Falsification remains success.** Clean falsification, narrowing, or demotion of a
   path is a successful contribution.

## Canon Documents

- `RESEARCH-POSTURE.md`
- `canon/firewall-boundary-hypothesis.md` (primary research question / falsification target)
- `canon/no-go-class-relative-map.md`
- `canon/no-go-quaternionic-parity-generation-sector.md`
- `canon/six-axis-specification-protocol.md`
- `canon/type-ii1-spectral-sm-checklist.md`
- `canon/shiab-existence-cl95.md`
- `canon/dark-energy-theta-divergence-free.md`
- `canon/w2-y14-spin-structure.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `canon/theta-field-flrw-dark-energy-eos.md`
- `canon/signed-readout-boundary-theorem-RESULTS.md` (big-swing R3; GU-independent)
- `canon/two-arena-rep-theory-core-RESULTS.md` (big-swing R4; GU-independent)
- `lab/specifications/six-axis/`
- `lab/specifications/type-ii1-spectral-sm/`

The **located-not-forced structural spine** RESULTS files (`canon/enum-completeness-class-c-RESULTS.md`,
`canon/core-theorems-symbolic-proof-RESULTS.md`, `canon/antilinear-bound-RESULTS.md`,
`canon/antilinear-nonkrein-admissibility-RESULTS.md`, `canon/external-topological-index-flux-RESULTS.md`,
`canon/function-space-index-conservation-RESULTS.md`, `canon/rs-boundary-eta-2primary-RESULTS.md`,
`canon/function-space-index-conservation-residual-closure-RESULTS.md`,
`canon/external-by-structure-synthesis-RESULTS.md`) are canon and enumerated in the tables below (internal
tier). Demoted 2026-07-03: `canon/multiplicity-theorem.md` is now `status: superseded` (self-superseded
2026-06-28; retained for the correction record — its live successors are `canon/h2-base-index-chirality.md`,
`canon/leg3-closure-and-spinor-2smoothness.md`, `canon/ghost-parity-krein-synthesis.md`, and
`papers/drafts/generation-multiplicity-vs-chirality-2026-06-28.md`).

## Canon Entries Added 2026-06-23

| entry | verdict | source explorations |
|---|---|---|
| `shiab-existence-cl95.md` | RESOLVED (existence only) | n1-signature-audit + n2-shiab-computation (2026-06-22); CORRECTION SHIAB-01 (2026-06-25): proves existence of one natural real-linear Spin(9,5)-equivariant Clifford-contraction map only; injectivity, rank/kernel, uniqueness, source-forced selector identity, anomaly cancellation, and generation count are not included; CORRECTION SHIAB-05 (2026-06-30, MOVE-4 chase): the SHIAB-04 heavy-Majorana side-claim upgraded ASSERTED->COMPUTED — dim Hom_{Spin(9,5)}(S^+ tensor S^+, Lambda^0)=0 (exact rep theory over Cl(9,5)=M(64,H); checksum 16384=128^2, errors 0.00e+00), so a same-chirality Majorana scalar-mass channel is provably ABSENT from the equivariant family and must be supplied by an external source-action spurion; EXACT unconditional rep theory, not a physics derivation; selector remains OPEN; tests/chase/MOVE-4/move4_spinor_square_forms.py |
| `dark-energy-theta-divergence-free.md` | CONDITIONALLY_RESOLVED | dark-energy-divergence-free-proof + dark-energy-noether-closure (2026-06-22); CORRECTION DARK-ENERGY-01 plus 2026-06-25 consistency sweep: downgraded from RESOLVED — Assumption 3 (structural identification) is reconstruction grade and unproved; C1+C2 is a cross-check, not an independent Noether route |
| `w2-y14-spin-structure.md` | CONDITIONALLY_RESOLVED | n6-w2-y14-gysin-spin-structure (2026-06-22); CORRECTION W2-01 (2026-06-26): unconditional spin claim RETRACTED — Step 3 dropped a w2(V) term, so w2(Y14)=pi*w2(X4), i.e. Y14 spin iff X4 spin (non-spin for CP2); orientability w1(Y14)=0 unaffected |
| `schwarzschild-weak-field-rfail.md` | OPEN | rfail-schwarzschild-oq2-weak-field (2026-06-23); CORRECTION RFAIL-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN — "passes solar-system tests" was compatibility-as-derivation on an imported metric; the genuine Willmore-EL residual is nonzero with unreconciled O(M/r^3) vs O(M/r^4) order (OQ2-A unperformed); CORRECTION RFAIL-03 (2026-06-30, MOVE-3 chase): the RFAIL-02 order dispute is RESOLVED by direct computation — BOTH linear-in-M estimates RETRACTED (the true linearized mean curvature H^(1)=(M/r)eta is HARMONIC, so the linear Willmore-EL residual is IDENTICALLY ZERO; the O(M/r^3) falsifying and "safe" O(M/r^4) orders are both artifacts), leaving leading order O(M^2/r^4)=Q(B), quadratic in M hence safe; F1 does NOT fire; verdict KEPT OPEN — OQ2-A (full gimmel Willmore-EL from GU's own action) still the open object; computation on an IMPORTED metric, not a GU derivation; tests/chase/MOVE-3/willmore_el_order.py |
| `theta-field-flrw-dark-energy-eos.md` | OPEN | theta-field-flrw-eos (2026-06-23); CORRECTION DARK-ENERGY-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN — only parameter-free prediction (ratio +1.17) is sign-inconsistent with DESI (w_a=-0.75); w_a sign has two undismissed IC candidates; re-elevation was a process milestone. Structural EOS machinery stays reconstruction-grade; CORRECTION DARK-ENERGY-03 (2026-06-30, MOVE-2 chase): the "w_a>0, sign-inconsistent-with-DESI, clean falsification" red-flag is RETRACTED as a local-derivative artifact — the global CPL fit over the DESI window (z<=2) gives w_0=-0.777, w_a=-0.248 (w_a NEGATIVE, same sign as DESI, ~3x smaller); the fitted w_a sign flips with fit window because w_DE(z) is non-monotone; the "+1.17 f_0-independent ratio" was a hardcoded d ln rho/dz=3 bug (only the local ratio ~+2.4 as f_0->0 is f_0-independent). Verdict KEPT OPEN — LCDM-amplitude-DEGENERATE (neither confirmation nor falsification); NOT "GU matches DESI"; source-action bottleneck untouched; tests/chase/MOVE-2/verify/indep_check.py; CORRECTION DARK-ENERGY-04 (2026-07-13, Wave 45): the DE-03 "neither confirmation nor falsification" phrase is SCOPED — (a) the (w0,wa)-CPL-projection comparison is FALSIFIED at exploration grade (H43/H44: ~3.2 sigma global miss, robust to M^2 band, ansatz, ICs, backreaction); (b) the raw-distance comparison on the actual DESI DR2 BAO likelihood is MARGINAL (H46: excluded only at canonical f0 + CMB-fixed amplitude; shape-competitive once amplitude marginalized, dAIC=-3.17, not decisive; f0 rescues mutually inconsistent). DESI DR2 + Planck digits verified vs primary sources — tests/wave45/H46B_referee_grade_desi_verification.py. Verdict stays OPEN; CORRECTION DARK-ENERGY-05 (2026-07-13, Wave 46): DE-04 clause (b) SCOPED -- the theta_star re-solve (Wave 45 blocker B1) is executed: GU's own CMB-calibrated amplitude is A_GU=31.97 (H0_GU=63.75), overshooting the BAO-preferred amplitude by +5.7 sigma_A; dAIC=+35.78 at GU's own calibration (+16.03 with omega_m h^2 profiled for both models); the freed-amplitude shape win (dAIC=-3.17) has no CMB-consistent realization; per-f0 CMB calibration prefers the LCDM limit f0->0 (bound f0 < ~0.03). Excluded as a CMB-consistently-calibrated distance model for f0 >= ~0.03 at exploration grade (M^2=8; BAO+theta* only); tests/wave46/H46C_theta_star_cmb_calibration.py. Verdict stays OPEN; CORRECTION DARK-ENERGY-06 (2026-07-14, W129): the OQ2 M^2-band sweep is EXECUTED -- the theta_star-calibrated raw-BAO exclusion HOLDS BAND-WIDE at DESI-signal amplitudes (admissible M^2 = 3/7/8, bracketing scan [1,25], 1-component ansatz, z_start variants; every DESI-CPL-matched amplitude excluded at dchi^2 >= +33.5, softest point M^2=3 still +14.9 with omega_m h^2 profiled); the OQ2 single-band-point gate is RETIRED. Honest softening: the "f0 < ~0.03" bound is M^2=8-specific -- the band bound is f0 < 0.027 (BC_1) / 0.039 (A_1) / 0.208 (S^3, M^2=3, where f0=0.125 is only mildly disfavored, dAIC +5.25) -- but everything allowed anywhere on the band is an LCDM mimic (|w0+1| < 0.1), so the band-safe exclusion is signal-level. SNe + a second BAO dataset remain named residuals; tests/W129_oq2_m2_band_sweep.py (exit 0, 13/13). Verdict stays OPEN |

## Canon Entries Added 2026-07-02 (located-not-forced structural spine; GU-independent, internal tier)

These are the **GU-independent** structural results of the located-not-forced program (canonical claim 6:
GU-independent results are co-equal products). **Internal tier only** (single-process; the paper's caveat (e) /
"internally established" on the verification-tier ladder): reproduced and adversarially re-verified within this
process, **NOT externally replicated** -- the V3->V4 crossing (independent replication / a Lean port) is still
outstanding. The generation-count VERDICT itself stays OPEN (see Not Yet Canon); nothing here derives three.

**Promotion reconciled 2026-07-03 (Joe-authorized, coherent-cluster scope).** The RESULTS files in the
table below carried `status: staged` while this spine already narrated them as canon; their file-level status is
now flipped to `canon` (`canon_promoted_at: 2026-07-03`), and the owner-surface consistency sweep
(`lab/process/runbooks/claim-status-consistency-quality-workflow.md`) was run across `RESEARCH-STATUS.md`,
this file, the `canon/` RESULTS, `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md`, and the paper. Two 2026-07-03
entries are added: STEP-2 RS boundary eta (2-primary on the actual `RP^3` boundary) and the function-space
residual closure (items (1)-(3) discharged on faithful models). Grade discipline is preserved: canon here means
"citable as the current spine," still internal tier; nothing is upgraded to a physics derivation, and the count
stays OPEN. The two RS function-space **SPEC** documents (`rs-function-space-framework-SPEC.md`,
`source-action-family-index-interface-SPEC.md`) remain `staged` as living framework/interface specs.

| entry | verdict | note |
|---|---|---|
| Two-primary meta-theorem + enumeration completeness (`canon/enum-completeness-class-c-RESULTS.md`) | RESOLVED for the delimited class C (computed grade, engine-swept) | No sector-interior covariant structure imposes an odd-prime (mod-3) congruence; the 7-item obstruction list is complete for class C with a sharp boundary. Each obstruction is a symbolic power-of-two identity (`canon/core-theorems-symbolic-proof-RESULTS.md`). |
| Index conservation (Theorem 2) + antilinear null-eigenspace bound (`canon/antilinear-bound-RESULTS.md`, `canon/antilinear-nonkrein-admissibility-RESULTS.md`) | RESOLVED at proof grade (symbolic, from the cross-chirality Krein axioms; independently re-verified) | Every linear Krein-isometric operator, and every antilinear operator whose re-graded chirality eigenspaces are K-null (the null-eigenspace class, strictly larger than Krein-compatible), keeps the net chiral index 0. Residual: the function-space RS-operator setting. |
| External mechanism: an odd chiral count is a topological index = flux/instanton number (`canon/external-topological-index-flux-RESULTS.md`) | RESOLVED (standard index theory, computed + independently re-verified) | An external chiral background carries net chiral index = flux number (any integer, odd for odd flux); realizes the paper's "external" mechanism and does **not** derive three. |
| Function-space extension (`canon/function-space-index-conservation-RESULTS.md`) | CONDITIONALLY_RESOLVED (interior/closed, spectral-gapped) | Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families. The three residual items are now DISCHARGED on faithful models (see the two 2026-07-03 rows below); the true-RS-`Y14`-bundle computation remains the honest residual. |
| RS boundary eta 2-primary — STEP 2 (`canon/rs-boundary-eta-2primary-RESULTS.md`) | RESOLVED at computed grade | The **actual** Rarita-Schwinger boundary operator's reduced eta-bar on the sector's own boundary `RP^3 = L(2;1)` is 2-primary — the real-bundle version of the class-symmetry that forces the boundary/end eta neutral. |
| Function-space residual closure — items (1)-(3) (`canon/function-space-index-conservation-residual-closure-RESULTS.md`) | DISCHARGED on faithful models (computed + independently re-verified); internal tier | Gap well-posedness (gap set by the end; count 0 when well-posed), APS/end eta = 0 for every operator in the class (nonzero eta is external), and the family-index term `c1(E_-)=c1(upper)+c1(lower)=0` are each discharged by the one `sigma_1 (x) B` mechanism. Honest residual: model -> true RS `Y14` bundle (standard APS/family-index machinery, not re-derived on `Y14`). Does **not** derive three. |
| "External by structure" synthesis (`canon/external-by-structure-synthesis-RESULTS.md`) | RESOLVED on faithful models (the RS function-space residual is discharged per the two rows above); internal tier; true-`Y14`-bundle computation is the remaining honest residual | `chi = interior-even + external-topological-index`, so any odd count is necessarily external. Upgrades the paper verdict's modality from "external on present evidence" to "external by structure" — now with the analytic residual discharged on faithful models rather than deferred. Does **not** derive three (the external index is any integer). |

## Canon Entries Added 2026-07-03 (big-swing GU-independent results; internal tier)

Promoted under the 2026-07-03 agent-owned Promotion Rule (`RESEARCH-STATUS.md`); JoeOps awareness notes filed
in `../../../system/mailboxes/joeops/`. Both are GU-independent (canonical claim 6), internal tier, and neither
derives three; the count verdict stays OPEN.

| entry | verdict | note |
|---|---|---|
| Signed-Readout Boundary Theorem (`canon/signed-readout-boundary-theorem-RESULTS.md`) | RESOLVED (abstract core M/P/C + compact Part Z/K, unconditional + machine-certified 22/22); OC1/OC2 remain labeled hypotheses for the non-compact case | GU-independent boundary theorem in ordered-algebra + index theory; no `chi(K3)` / 24 / 8 / 3 imported. Certificate `tests/big-swing/R3_signed_readout_certificate.py` exit 0 (re-run 2026-07-03). |
| Two-Arena Rep-Theory Core (`canon/two-arena-rep-theory-core-RESULTS.md`) | RESOLVED (three exact facts; exact-integer certified; arithmetic cores have written Lean proof terms) | (A) `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0` (corroborated by SHIAB-05); (B) `pi_3^s = Z/8 (+) Z/3` CRT split + 2-primary blindness; (C) class-C generator arithmetic. `R4_crt_two_arena.py` exit 0 (re-run 2026-07-03); Lean recompilation not re-reproduced in this pass. |

## Not Yet Canon

These remain exploratory until formal obligations are met:

Before promoting any item from this list, run
`lab/process/runbooks/claim-status-consistency-quality-workflow.md` and update all owner
surfaces that might still carry a stronger historical verdict.

- Anomaly cancellation for Sp(64) — Nguyen's U(128) anomaly pincer is defused by the Sp(64) replacement, but full GU anomaly cancellation is OPEN / not canon: local 14D anomaly requires an explicit I_16/index-density computation for the actual chiral field content; global anomaly requires a spin-bordism/Dai-Freed/eta check, not only pi_15(Sp). **CORRECTION MOVE1-01 (2026-06-30, MOVE-1 chase):** the "irreducible Sp(64) gauge octic" reading of the local non-factorization is a GAUGE-READING ARTIFACT — under the genuine Clifford commutant Sp(1)=right-H, Str_S F^8 = 128 (y^2)^4 is a pure product of quadratic Casimirs with NO independent order-8 invariant (Green-Schwarz reducible; gauge octic red flag flips True->False). The TOTAL local non-factorizability SURVIVES but is reclassified as pure-gravitational/net-chirality: the reading-independent gravitational tr R^8 (A-hat(TY14) deg-16 coefficient, matches Alvarez-Gaume-Witten; K3^4->16, HP^2^2->0 index checks pass) is nonzero solely because the ASSUMED truncated content has net chirality n_+-n_- = 1-14 = -13. This is EXPLICITLY CONDITIONAL on the assumed truncated fermion content (chirally balanced -> vanishes) and is NO promotion to an anomaly-cancellation claim; the global eta/Dai-Freed/spin-bordism leg stays OPEN. tests/chase/MOVE-1/move1_octic_sp64_vs_sp1.py, tests/chase/MOVE-1/verify/indep_ahat16.py
- C_MPR as a category
- the 9-tuple as a complete invariant
- PCP-blindness
- BvN/Classical-Value-Lattice Wall as universal obstruction
- stochastic, Sorkin, RG, CA, bicategorical, and layer-split applications
- Three-generation count (analytic index ind_H(D_gimmel) on non-compact Y14) — **BLOCKED ON A GENUINE GU THEORY GAP (2026-06-26, RS-BRST run):** the count requires the physical gauge-fixed Rarita-Schwinger complex RS_GU^phys, whose computability-deciding data (a stabilized RS-sector action => the ghost-subtraction count q => the gauge-fixing slice) GU does NOT determine. GU fixes the gauge symmetry, field content, and H-structure (gu_derived skeleton) but never stabilizes the RS-sector action — the only candidate, draft eq 10.10, is author-disclaimed ("until it is stabilized. Caveat Emptor.", PDF p.49). Machine-verified obstruction: GU's gamma-trace irreducibility constraint and the gauge orbit are incompatible as a naive quotient (RS symbol on the pure-gauge image: norm 73.48 Cl(4,0) / 343.73 Cl(9,5), neither annihilated). So "3 generations" is not computable even in principle on current GU source — the gap is in the theory, not the formalization. See DERIVATION-PROGRESS RS-BRST entry. **STRUCTURAL UPDATE (2026-07-02):** the interior is now proved EVEN over the complete delimited class (symbolic index conservation + antilinear null-eigenspace bound + enum-completeness), and the external mechanism is computed (an odd count is a topological index = flux/instanton number, any integer). So the count is now characterized as "external by structure" MODULO the function-space Rarita-Schwinger APS/family-index residual (`canon/external-by-structure-synthesis-RESULTS.md`). **UPDATE (2026-07-03):** that function-space residual is now DISCHARGED on faithful models — gap well-posedness, APS/end eta neutrality in the class (plus STEP-2: the actual RS boundary eta on `RP^3` is 2-primary, `canon/rs-boundary-eta-2primary-RESULTS.md`), and the family-index term all fall to the one `sigma_1 (x) B` mechanism (`canon/function-space-index-conservation-residual-closure-RESULTS.md`). The "external by structure" reading is therefore no longer gated by an open analytic residual on faithful models; the one honest residual that remains is the true-RS-`Y14`-bundle computation (standard APS/family-index machinery, not re-derived on `Y14`). **None of this changes the verdict:** the count itself stays **OPEN / blocked on the source action**; three is NOT derived (the external index is any integer, nothing privileges 3).
- Velo-Zwanziger constraint for GU spin-3/2 sector
