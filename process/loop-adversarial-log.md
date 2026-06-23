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
