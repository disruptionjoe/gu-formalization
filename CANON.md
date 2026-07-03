---
title: "Project Canon"
status: canon
doc_type: canon
updated_at: "2026-06-30"
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
- `canon/no-go-class-relative-map.md`
- `canon/six-axis-specification-protocol.md`
- `canon/type-ii1-spectral-sm-checklist.md`
- `canon/shiab-existence-cl95.md`
- `canon/dark-energy-theta-divergence-free.md`
- `canon/w2-y14-spin-structure.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `canon/theta-field-flrw-dark-energy-eos.md`
- `lab/specifications/six-axis/`
- `lab/specifications/type-ii1-spectral-sm/`

## Canon Entries Added 2026-06-23

| entry | verdict | source explorations |
|---|---|---|
| `shiab-existence-cl95.md` | RESOLVED (existence only) | n1-signature-audit + n2-shiab-computation (2026-06-22); CORRECTION SHIAB-01 (2026-06-25): proves existence of one natural real-linear Spin(9,5)-equivariant Clifford-contraction map only; injectivity, rank/kernel, uniqueness, source-forced selector identity, anomaly cancellation, and generation count are not included; CORRECTION SHIAB-05 (2026-06-30, MOVE-4 chase): the SHIAB-04 heavy-Majorana side-claim upgraded ASSERTED->COMPUTED — dim Hom_{Spin(9,5)}(S^+ tensor S^+, Lambda^0)=0 (exact rep theory over Cl(9,5)=M(64,H); checksum 16384=128^2, errors 0.00e+00), so a same-chirality Majorana scalar-mass channel is provably ABSENT from the equivariant family and must be supplied by an external source-action spurion; EXACT unconditional rep theory, not a physics derivation; selector remains OPEN; tests/chase/MOVE-4/move4_spinor_square_forms.py |
| `dark-energy-theta-divergence-free.md` | CONDITIONALLY_RESOLVED | dark-energy-divergence-free-proof + dark-energy-noether-closure (2026-06-22); CORRECTION DARK-ENERGY-01 plus 2026-06-25 consistency sweep: downgraded from RESOLVED — Assumption 3 (structural identification) is reconstruction grade and unproved; C1+C2 is a cross-check, not an independent Noether route |
| `w2-y14-spin-structure.md` | CONDITIONALLY_RESOLVED | n6-w2-y14-gysin-spin-structure (2026-06-22); CORRECTION W2-01 (2026-06-26): unconditional spin claim RETRACTED — Step 3 dropped a w2(V) term, so w2(Y14)=pi*w2(X4), i.e. Y14 spin iff X4 spin (non-spin for CP2); orientability w1(Y14)=0 unaffected |
| `schwarzschild-weak-field-rfail.md` | OPEN | rfail-schwarzschild-oq2-weak-field (2026-06-23); CORRECTION RFAIL-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN — "passes solar-system tests" was compatibility-as-derivation on an imported metric; the genuine Willmore-EL residual is nonzero with unreconciled O(M/r^3) vs O(M/r^4) order (OQ2-A unperformed); CORRECTION RFAIL-03 (2026-06-30, MOVE-3 chase): the RFAIL-02 order dispute is RESOLVED by direct computation — BOTH linear-in-M estimates RETRACTED (the true linearized mean curvature H^(1)=(M/r)eta is HARMONIC, so the linear Willmore-EL residual is IDENTICALLY ZERO; the O(M/r^3) falsifying and "safe" O(M/r^4) orders are both artifacts), leaving leading order O(M^2/r^4)=Q(B), quadratic in M hence safe; F1 does NOT fire; verdict KEPT OPEN — OQ2-A (full gimmel Willmore-EL from GU's own action) still the open object; computation on an IMPORTED metric, not a GU derivation; tests/chase/MOVE-3/willmore_el_order.py |
| `theta-field-flrw-dark-energy-eos.md` | OPEN | theta-field-flrw-eos (2026-06-23); CORRECTION DARK-ENERGY-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN — only parameter-free prediction (ratio +1.17) is sign-inconsistent with DESI (w_a=-0.75); w_a sign has two undismissed IC candidates; re-elevation was a process milestone. Structural EOS machinery stays reconstruction-grade; CORRECTION DARK-ENERGY-03 (2026-06-30, MOVE-2 chase): the "w_a>0, sign-inconsistent-with-DESI, clean falsification" red-flag is RETRACTED as a local-derivative artifact — the global CPL fit over the DESI window (z<=2) gives w_0=-0.777, w_a=-0.248 (w_a NEGATIVE, same sign as DESI, ~3x smaller); the fitted w_a sign flips with fit window because w_DE(z) is non-monotone; the "+1.17 f_0-independent ratio" was a hardcoded d ln rho/dz=3 bug (only the local ratio ~+2.4 as f_0->0 is f_0-independent). Verdict KEPT OPEN — LCDM-amplitude-DEGENERATE (neither confirmation nor falsification); NOT "GU matches DESI"; source-action bottleneck untouched; tests/chase/MOVE-2/verify/indep_check.py |

## Canon Entries Added 2026-07-02 (located-not-forced structural spine; GU-independent, internal tier)

These are the **GU-independent** structural results of the located-not-forced program (canonical claim 6:
GU-independent results are co-equal products). **Internal tier only** (single-process; the paper's caveat (e) /
"internally established" on the verification-tier ladder): reproduced and adversarially re-verified within this
process, **NOT externally replicated** -- the V3->V4 crossing (independent replication / a Lean port) is still
outstanding. The full owner-surface consistency sweep
(`lab/process/runbooks/claim-status-consistency-quality-workflow.md`) is Joe's to confirm. The generation-count
VERDICT itself stays OPEN (see Not Yet Canon); nothing here derives three.

| entry | verdict | note |
|---|---|---|
| Two-primary meta-theorem + enumeration completeness (`canon/enum-completeness-class-c-RESULTS.md`) | RESOLVED for the delimited class C (computed grade, engine-swept) | No sector-interior covariant structure imposes an odd-prime (mod-3) congruence; the 7-item obstruction list is complete for class C with a sharp boundary. Each obstruction is a symbolic power-of-two identity (`canon/core-theorems-symbolic-proof-RESULTS.md`). |
| Index conservation (Theorem 2) + antilinear null-eigenspace bound (`canon/antilinear-bound-RESULTS.md`, `canon/antilinear-nonkrein-admissibility-RESULTS.md`) | RESOLVED at proof grade (symbolic, from the cross-chirality Krein axioms; independently re-verified) | Every linear Krein-isometric operator, and every antilinear operator whose re-graded chirality eigenspaces are K-null (the null-eigenspace class, strictly larger than Krein-compatible), keeps the net chiral index 0. Residual: the function-space RS-operator setting. |
| External mechanism: an odd chiral count is a topological index = flux/instanton number (`canon/external-topological-index-flux-RESULTS.md`) | RESOLVED (standard index theory, computed + independently re-verified) | An external chiral background carries net chiral index = flux number (any integer, odd for odd flux); realizes the paper's "external" mechanism and does **not** derive three. |
| Function-space extension (`canon/function-space-index-conservation-RESULTS.md`) | CONDITIONALLY_RESOLVED (interior/closed, spectral-gapped) | Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families. Residual OPEN: APS/noncompact-end eta + family-index + the actual Rarita-Schwinger operator. |
| "External by structure" synthesis (`canon/external-by-structure-synthesis-RESULTS.md`) | CONDITIONAL (modulo the RS function-space residual); internal tier | `chi = interior-even + external-topological-index`, so any odd count is necessarily external. Upgrades the paper verdict's modality from "external on present evidence" to "external by structure" MODULO the RS residual. Does **not** derive three. |

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
- Three-generation count (analytic index ind_H(D_gimmel) on non-compact Y14) — **BLOCKED ON A GENUINE GU THEORY GAP (2026-06-26, RS-BRST run):** the count requires the physical gauge-fixed Rarita-Schwinger complex RS_GU^phys, whose computability-deciding data (a stabilized RS-sector action => the ghost-subtraction count q => the gauge-fixing slice) GU does NOT determine. GU fixes the gauge symmetry, field content, and H-structure (gu_derived skeleton) but never stabilizes the RS-sector action — the only candidate, draft eq 10.10, is author-disclaimed ("until it is stabilized. Caveat Emptor.", PDF p.49). Machine-verified obstruction: GU's gamma-trace irreducibility constraint and the gauge orbit are incompatible as a naive quotient (RS symbol on the pure-gauge image: norm 73.48 Cl(4,0) / 343.73 Cl(9,5), neither annihilated). So "3 generations" is not computable even in principle on current GU source — the gap is in the theory, not the formalization. See DERIVATION-PROGRESS RS-BRST entry. **STRUCTURAL UPDATE (2026-07-02):** the interior is now proved EVEN over the complete delimited class (symbolic index conservation + antilinear null-eigenspace bound + enum-completeness), and the external mechanism is computed (an odd count is a topological index = flux/instanton number, any integer). So the count is now characterized as "external by structure" MODULO the function-space Rarita-Schwinger APS/family-index residual (`canon/external-by-structure-synthesis-RESULTS.md`, promoted above as CONDITIONAL). The count itself stays **OPEN / blocked on the source action**; three is NOT derived (the external index is any integer, nothing privileges 3). Closing the RS function-space residual would make the "external by structure" verdict unconditional but would still not derive three.
- Velo-Zwanziger constraint for GU spin-3/2 sector
