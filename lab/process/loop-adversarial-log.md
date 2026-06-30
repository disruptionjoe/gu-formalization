## Run 2026-06-23 — 10/10 completed, 8 fixed

**Items:** oq-kk1a-cas-norm-fiber-wavefunction, vz-oq-cas-e-block-inverse-matrix, pc5-higgs-cas-clebsch-gordan, oq-rk2-aps-fc3-fc4-closure, dark-energy-c1-c2-path-gimmel-ginvariance, type-ii1-f6-jbridge-semifinite-twisted, sc1-oq1a-d7-clebsch-gordan-cas, theta-field-flrw-matter-era-ode, cpa1-ambient-curv-cas-coordinate, oq-rs3-gu-vasiliev-comparison

**Session patterns (from adversarial review):**
Three recurring failure modes across this session: (1) VERDICT GRADE MISMATCH — multiple files (pc5-higgs-cas-clebsch-gordan, sc1-oq1a-d7-clebsch-gordan-cas) labeled RESOLVED when the body text explicitly states reconstruction grade and lists open CAS verification steps; RESOLVED requires a complete proof, not a reconstruction-grade argument with a pending LiE check. (2) SAME-SESSION SELF-RESOLUTION — the E-block circularity flag (CR-04) was raised and resolved within the same session; the vz-oq-cas-e-block-inverse-matrix file explicitly argues that being 'a separate file' is sufficient to close the same-session gate, which is incorrect; separation by file does not constitute external or inter-session verification. (3) INTERNAL CONTRADICTION LABELED RESOLVED — oq-kk1a-cas-norm-fiber-wavefunction explicitly raises a contradiction (Jacobi discrete spectrum gives nu=5/2 and 1/2, not 3/2) and its resolution section contains 'need to recheck' language, yet the file claims G2a is CLOSED and posts a CONDITIONALLY_RESOLVED verdict; an acknowledged 'need to recheck' is an open problem, not a resolved one. For the next run: (a) require that RESOLVED verdicts pass a gate-check — 'would this computation be accepted at a referee-level review without further computation?'; (b) enforce that same-session files cannot close same-session circularity flags regardless of which file they appear in; (c) when an internal contradiction is explicitly identified in the computation, the verdict must be OPEN until the contradiction is resolved, not merely noted.

**Calibration for next run:**
1. Gate-check every RESOLVED verdict against the referee standard: if any named step requires further computation or a pending external check, the verdict is CONDITIONALLY_RESOLVED at best.
2. Same-session circularity gate is file-boundary-blind — a flag raised in session N cannot be closed by any file also produced in session N, regardless of how the files are separated.
3. An explicit internal contradiction in the body of a file (including 'need to recheck' language) is an open problem; block CLOSED or RESOLVED verdicts on any item containing one until the contradiction is resolved in a subsequent session.

**Issue summary:** 10 total (8 critical/moderate, 2 minor)

---

## Run 2026-06-23 — 9/9 completed, 11 fixed

**Items:** vz-e-block-direct-clifford-invertibility, historical-rank-one-archive-clean, oc2-sobolev-analytic-gate-a1, oq-rk1-cas-pi-rs-rank-check, six-axis-l1l2-coupling-second-filled-row, pc5-higgs-su2l-u1y-gate-computation, h3-gap2-pati-salam-f2-bipartite, h3-chsh-four-patch-cycle, type-ii1-exit-condition-cs1-af-embedding

**Session patterns (from adversarial review):**
Three recurring failure modes dominated this session:

1. Same-session self-resolution of flags. Multiple critical problems were identified and then 'resolved' within the same session by reconstruction-grade arguments from sister files (VZ-01 circularity resolved by vz-e-block-direct-clifford; H3-01 correction entered then partially re-resolved). This pattern produces a false sense of closure. The rule should be: any flag raised against a proof cannot be closed by a reconstruction-grade file produced in the same session loop — it requires either a verified external computation or a formal demotion of the verdict.

2. Verdict inflation through candidate selection. When two equally-supported candidates exist (generation count 3 vs 4 via rank_H = 4 or 8), the session defaulted to selecting Candidate A as the baseline and labeling the result CONDITIONALLY_RESOLVED rather than OPEN. A CONDITIONALLY_RESOLVED verdict is appropriate only when one candidate is supported by a derivation and the other is named as a failure condition; when both candidates are undismissed guesses, the correct verdict is OPEN.

3. Reconstruction-grade structural identifications in RESOLVED canon entries. The dark-energy-theta-divergence-free.md carries RESOLVED verdict while the central claim rests on Assumption 3 ('theta is the gauge potential sector of E_A'), which is explicitly labeled reconstruction grade. The shiab-existence canon carries RESOLVED while a subtle non-cancellation gap exists in the injectivity argument. For the next run: every RESOLVED verdict in a canon entry should require a full proof of each named assumption — reconstruction grade is not a valid basis for RESOLVED at canon level.

What the next run should do differently: (a) Never upgrade a verdict within the same session that raised the flag — require at least one intervening verified computation. (b) When OQ-RK1 (rank_H CAS computation) is the blocking gate, hold the generation count at OPEN and do not present either candidate as the baseline. (c) Audit all RESOLVED canon entries for assumptions labeled reconstruction grade — any such assumption automatically drops the parent verdict to CONDITIONALLY_RESOLVED.

**Calibration for next run:**
1. Before any verdict upgrade: check whether the flag and the resolution both originate in the current session loop — if so, block the upgrade and mark the item DEFERRED_VERIFICATION instead.
2. When two undismissed generation-count candidates exist, emit verdict OPEN and list both candidates as hypotheses; do not select a baseline or label either as primary.
3. Open the RESOLVED canon entries audit pass as the first Orient task: list every assumption labeled reconstruction-grade inside a RESOLVED file and immediately downgrade those entries to CONDITIONALLY_RESOLVED pending external verification.

**Issue summary:** 14 total (11 critical/moderate, 3 minor)

---
