---
title: "Research Status"
status: active_research
doc_type: roadmap
updated_at: "2026-06-25"
canon_sweep_at: "2026-06-23"
---

# Research Status

The internal work-artifact system was the originating workspace for this project. The
public repository is now the durable research authority.

The primary research posture is now GU reconstruction under a bold working hypothesis:
Geometric Unity is substantially correct, and the repository's task is to determine
whether that hypothesis can be rigorously reconstructed, extended, or falsified. See
`RESEARCH-POSTURE.md`.

## Status Labels

Every Markdown research document carries YAML frontmatter with one of these statuses:

- `canon`: stable public spine
- `active_research`: promising frontstage work, not yet canon
- `exploration`: speculative or redirected branch
- `process`: method, dialectic, or synthesis history
- `archive`: historical provenance
- `source`: source or literature material
- `draft`: paper or exposition draft

### Claim-Status Consistency Rule

Any promotion, downgrade, or substantial re-scoping must run
`process/runbooks/claim-status-consistency-quality-workflow.md` before commit. Downstream
claims cannot outrank their weakest load-bearing dependency, and historical stronger
wording must be removed or explicitly marked superseded on owner surfaces.

## Current Research Map

| area | status | where to read |
|---|---|---|
| research posture | canon | `RESEARCH-POSTURE.md` |
| project canon | canon | `CANON.md` |
| no-go assumption map | canon | `canon/no-go-class-relative-map.md` |
| six-axis protocol | canon | `canon/six-axis-specification-protocol.md` |
| Type II1 checklist | canon | `canon/type-ii1-spectral-sm-checklist.md` |
| shiab existence — Cl(9,5) | canon (RESOLVED for existence only; injectivity/rank/kernel not claimed) | `canon/shiab-existence-cl95.md` — CORRECTION SHIAB-01 (2026-06-25); SHIAB-02 (2026-06-26): Nguyen §3.1 "resolution" tightened — existence rebuts "every such map must complexify" but does NOT identify GU's actual operator as the real map (selector identity OPEN) |
| dark energy theta — divergence-free and dynamic | canon (CONDITIONALLY_RESOLVED) | `canon/dark-energy-theta-divergence-free.md` — CORRECTION DARK-ENERGY-01 (2026-06-23): downgraded from RESOLVED |
| w2(Y14) = pi*w2(X4) — Y14 spin iff X4 spin | canon (CONDITIONALLY_RESOLVED; unconditional spin claim RETRACTED) | `canon/w2-y14-spin-structure.md` — CORRECTION W2-01 (2026-06-26) |
| Schwarzschild weak-field R_fail (O(M/r^3) vs O(M/r^4) unreconciled) | canon (verdict OPEN; weak-field compatibility check on an imported metric, not a GR derivation) | `canon/schwarzschild-weak-field-rfail.md` — CORRECTION RFAIL-02 (2026-06-26) |
| theta-field FLRW dark energy EOS | canon (EOS-vs-DESI verdict OPEN; structural machinery reconstruction-grade) | `canon/theta-field-flrw-dark-energy-eos.md` — CORRECTION DARK-ENERGY-02 (2026-06-26) |
| signed-readout boundary theorem | active_research | `active-research/signed-readout/` |
| CALM/Ginsparg-Wilson boundary | active_research | `active-research/calm-gw-boundary/` |
| ranked next steps | active_research | `roadmap/` |
| C_MPR and 9-tuple | exploration | `explorations/c-mpr/` |
| observer-finality crosswalk | exploration | `explorations/time-as-finality-crosswalk/` |
| positive GU constructions lane | exploration | `explorations/positive-gu-constructions-lane-proposal-2026-06-22.md` |
| stochastic, causal-set, RG, CA, higher-categorical branches | exploration | `explorations/` |
| persona process and dialectics | process | `process/` |
| early frontier packets | archive | `archive/` |
| source and media provenance | source | `sources/` |
| literature briefs | source | `literature/` |

## 2026-06-23 Correction VZ-01 (critical)

**VZ evasion status for 14D mixed covectors downgraded from EVADED to CONDITIONALLY_EVADED.**

The `vz-schur` result logged in the second parallel pass (and the synthesis in `explorations/vz-14d-mixed-covectors-2026-06-23.md`) reported `VZ evasion status: EVADED`. This is overstated. The Schur complement proof uses `E^{-1}` without independently establishing that `E(xi)` is invertible on `Q = E_0 + Q^{14D}`. The `det(M) = det(E)*det(S_R)` identity is circular: it holds when E is invertible and cannot be used to prove E invertibility. Until a direct Clifford algebra proof is supplied, the 14D mixed-covector result is CONDITIONALLY_EVADED. The 4D section-pullback result (OQ3-V1/V2/V3) is unaffected at the principal-symbol order but is NOT VERIFIED (see VZ-02 below). The exploration file has been corrected (frontmatter, §4, §7 table, §9). See DERIVATION-PROGRESS.md log entry CORRECTION VZ-01.

## 2026-06-23 Correction VZ-02 (critical)

**VZ 4D principal-symbol verdict in `canon/no-go-class-relative-map.md` downgraded from VERIFIED to CONDITIONALLY_RESOLVED.**

The canon no-go map's VZ row and §2.5 carried a hard `4D VERIFIED at principal-symbol level (OQ3-V1/V2/V3)` label. This was internally inconsistent with the same section's failure condition FC-VZ-4, which states the VERIFIED 4D evasion "is overturned at the next (subprincipal) order" if the extrinsic curvature `II_s = s*(θ)` sources spacelike characteristics. A VERIFIED verdict cannot coexist with a known, unaddressed higher-order route to being overturned; the `vz-subprincipal` check that would close FC-VZ-4 is itself only reconstruction grade. All such labels in the canon map are now **CONDITIONALLY_RESOLVED (4D principal-symbol, reconstruction; subprincipal order open per FC-VZ-4)**. VERIFIED is reserved for a result with no acknowledged route to being overturned. The 14D leg (CONDITIONALLY_EVADED) and the underlying mathematics are unchanged. See DERIVATION-PROGRESS.md log entry CORRECTION VZ-02.

## 2026-06-25 Claim-Status Consistency Sweep

This sweep corrects stale stronger claims that survived earlier downgrade work. It is a status-alignment pass, not a new proof.

| claim | corrected current status | controlling correction |
|---|---|---|
| Shiab existence | RESOLVED for existence of one natural real-linear Spin(9,5)-equivariant Clifford-contraction map only | `canon/shiab-existence-cl95.md` CORRECTION SHIAB-01. The previous injectivity/non-vanishing-on-all-inputs proof is invalid dimensionally; rank/kernel/uniqueness remain open. |
| Dark-energy theta divergence-free | CONDITIONALLY_RESOLVED | Assumption 3 must be derived from a written action. C1+C2 is a gauge-invariance cross-check, not an independent Noether route. |
| Sp(64) anomaly lane | SUBSTANTIALLY_ADDRESSED / OPEN for full anomaly cancellation / NOT PROMOTED | The U(128) horn is defused by Sp(64), but pseudoreality does not automatically kill the even 14D degree-8 local anomaly. Full status requires an explicit I_16/index-density computation and a spin-bordism/Dai-Freed/eta global-anomaly check. |
| Freed-Hopkins Option-B / X_obs^sol | CONDITIONALLY_RESOLVED / lane-narrowed, not closed | Riemannian full-section-space contractibility does not automatically cover Lorentzian metric components; K3 and KSp relabeling remain conditional. |
| Generation count | OPEN | Old compact-toy and physical-count arithmetic is provenance only until the RS leg is derived without target division or reverse-engineered rank input. |
| Velo-Zwanziger | 14D CONDITIONALLY_EVADED; 4D CONDITIONALLY_RESOLVED at principal-symbol grade | Do not cite 4D as VERIFIED; subprincipal/extrinsic-curvature and full dynamical gates remain open. |
| SC1-OQ1A D7 common-summand / Product B chirality exclusion | OPEN | CORRECTION SC1-OQ1A-PRODUCTB-CANDIDATE-01 (2026-06-25): the 2104 Product B audit finds `V(omega_2) tensor V(omega_6) = V(omega_2+omega_6) + V(omega_1+omega_7) + V(omega_6)`, so the older claim excluding `V(omega_1+omega_7)` from `Lambda^2 tensor Delta^+` is superseded. Shiab existence remains RESOLVED for existence only; uniqueness/common-summand is open. |
| SC1-OQ1A Product A finite-control packet | CLOSED route-locally for Product A; selector identity OPEN | The 2104 cycle 2 Product A audit finds `V(omega_1) tensor V(omega_7) = V(omega_1+omega_7) + V(omega_6)`, `ker(c)=V(omega_1+omega_7)`, `image(c)=V(omega_6)`, and `cokernel(c)=0`. Together with Product B, this leaves two common rows, so proof restart is still blocked pending `SourceNaturalProductABRivalProjectorIdentity_V1`. |

## 2026-06-23 Canon Promotion Sweep

Five explorations checked against all five promotion criteria. Five promoted; one checked but not yet eligible.

| candidate | verdict in source | promotion decision | reason |
|---|---|---|---|
| shiab existence (N1+N2) | RESOLVED (existence only; superseded scope) | PROMOTED WITH SCOPING CORRECTION | CORRECTION SHIAB-01: Clifford contraction construction is explicit and non-zero as a map, but injectivity/non-vanishing on all inputs was overclaimed and is impossible dimensionally. Future use may cite only existence/equivariance unless rank/kernel is computed. |
| dark energy divergence-free (Layer 2) | CONDITIONALLY_RESOLVED (supersedes original RESOLVED row) | PROMOTED WITH DOWNGRADE | CORRECTION DARK-ENERGY-01 plus 2026-06-25 sweep: equivariance/dynamism remain unconditional, but D_A*theta=0 depends on unproved Assumption 3. C1+C2 is a cross-check, not an independent route. |
| w2(Y14) (N6) | CONDITIONALLY_RESOLVED (supersedes RESOLVED) | PROMOTED WITH CORRECTION | CORRECTION W2-01 (2026-06-26): the unconditional spin claim was FALSE. The Step 3 assembly dropped a w2(V) term in the (R^3 tensor sgn = V tensor L) factor — w2(V tensor L) = w2(V) + w1(L)^2, not w1(L)^2 — so w2(TV) = 0, not w2(X4) (independently confirmed by w2(Sym^2 E) = w1(E)^2 for rank-4 E). MO-02 restated the error rather than catching it. Corrected: w2(Y14) = pi*w2(X4), so Y14 is spin iff X4 is spin (NON-spin for non-spin bases like CP2). Orientability w1(Y14)=0 stays unconditional. D_gimmel needs no section choice only for spin X4; non-spin X4 OPEN. |
| Schwarzschild weak-field R_fail (today) | OPEN (RFAIL-02 re-downgrade 2026-06-26) | PROMOTED THEN RE-DOWNGRADED | CORRECTION RFAIL-02: the "GU passes solar-system tests" headline was compatibility-as-derivation on an imported Schwarzschild metric (R_fail^GR=0 is trivial vacuum, no GU content); the genuine Willmore-EL residual is nonzero with an unreconciled leading order (O(M/r^4) flat-space vs companion O(M/r^3) Weyl, which F1 says would falsify); discriminating computation OQ2-A unperformed. Gauss-identity / Q(B)-quadraticity steps stay reconstruction-grade. Original: All 5 criteria met at promotion. |
| theta-field FLRW dark energy EOS (today) | OPEN (DARK-ENERGY-02 re-downgrade 2026-06-26) | PROMOTED THEN RE-DOWNGRADED | EOS-vs-DESI verdict is OPEN: the only parameter-free prediction (ratio +1.17) is sign-inconsistent with DESI (w_a=-0.75) and the w_a sign has two undismissed IC candidates (UNDISMISSED-CANDIDATE rule); the 2026-06-23 re-elevation was a process milestone, not data support. Structural EOS machinery stays reconstruction-grade. Original promotion note: All 5 criteria met at promotion. CORRECTION 2026-06-23 OQ3 (supersedes THETA-01): full FLRW Klein-Gordon (RK4) integration corrected the ratio prediction to w_a/(w_0+1) = +1.17 (de Sitter -1.80 RETRACTED, SIGN REVERSED) at phi_0 = 0.855 rad (was 1.94 rad). Corrected sign is w_a > 0 with frozen ICs, OPPOSITE to DESI's w_a = -0.75; the sign is IC-sensitive and conditional on named failure condition FC5/OQ3-A (slow-roll ICs from z >> z_osc). CORRECTION 2026-06-23 CANON-4: in-file Result 4 / Gap 2 / Falsification Condition / F6-F8 still carried the retracted w_a < 0 / -1.80 / phi_0 ~ 1.94; aligned to the OQ3-corrected +1.17 / w_a > 0 / phi_0 = 0.855. The ratio is reconstruction-grade, conditional on phi_0 = 0.855 rad and frozen IC at z=3, not a phi_0-independent free prediction. Failure modes F1-F9 + FC5; open questions include OQ3-A (IC-sensitivity of w_a sign) and OQ5 phi_0-scan. |
| anomaly Sp(64) (substantially addressed) | SUBSTANTIALLY_ADDRESSED / OPEN for full cancellation | NOT PROMOTED | Nguyen's U(128) pincer is defused by the Sp(64) replacement, but perturbative cancellation is not verified by pseudoreality alone in 14D because the relevant trace degree is even. Global anomaly is not settled by pi_15(Sp) alone. Needs explicit I_16/index-density plus spin-bordism/Dai-Freed/eta checks and the existing §5.1 items. |

## Promotion Rule

An exploration can move toward canon only when it has:

1. a clear scope statement,
2. a proof or falsification target,
3. explicit assumptions,
4. known failure modes,
5. no dependency on internal work artifacts for its next action,
6. no stale stronger status remains in `RESEARCH-STATUS.md`, `CANON.md`, affected `canon/*`, `NEXT-STEPS.md`, live paper drafts, or process/DAG/firewall artifacts after a claim-status consistency sweep.

## Current Caution

The observer-finality crosswalk is useful only as a test layer. It should not be cited as GU canon or as a way to evade no-go theorems. Its near-term value is the bounded signed-readout record-graph test in `explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md`.

## 2026-06-23 Parallel Frontier Pass

Five bounded frontier notes were added by the manual parallel pass. One additional VZ follow-up note from the brief scheduled run was retained because it closes a narrow vertical-sector subcase. All are exploration-grade; no canon or active-research promotion is implied.

| document | status | content |
|---|---|---|
| `explorations/vz1-schur-complement-symbol-2026-06-23.md` | exploration | Confirms RS/non-RS off-diagonal coupling in the local rolled-up principal-symbol model. The 14D horizontal spin-3/2 sector is not a closed standalone subsystem under stated assumptions. Full VZ evasion remains open; the first unresolved piece after this note was the vertical-sector extension below. |
| `explorations/vz1-schur-vertical-extension-2026-06-23.md` | exploration | Extends the VZ Schur calculation for horizontal covectors by including vertical one-form inputs. Verdict: vertical one-forms do not change the horizontal Schur complement under the horizontal gamma-trace RS projection. Mixed 14D covectors and the full 14D gamma-trace RS definition remain open. |
| `explorations/ii-s-coordinate-formula-2026-06-23.md` | exploration | Supplies explicit gimmel Christoffels and the graph-section formula for `II_s`. OQ-2 is locally closed at formula level, but the physical convention must be chosen: literal graph immersion versus horizontal-normalized pullback/reference subtraction. |
| `explorations/codazzi-sp64-bundle-2026-06-23.md` | exploration | Formulates Gauss-Codazzi-Ricci for the tautological section and Sp(64) associated bundle. Names the exact residuals: normal-flux correction `K(A,s)` and Einstein failure tensor `R_fail`. |
| `explorations/discrete-series-fiber-dirac-index-2026-06-23.md` | exploration | Finds that `dim_H ker_L2(D_fib)=24` is not coherent as an ordinary finite homogeneous-fiber kernel statement on `GL(4,R)/O(3,1)`. The generation-count analytic target must be replaced by a compactified, quotient, equivariant-index, or relative-discrete-series multiplicity problem. |
| `explorations/cross-program-lambda-coefficient-2026-06-23.md` | exploration | Corrects the cross-program comparison: GU `Lambda` has rate-squared units, so it should be compared with `lambda_max^2` or `Gamma_min^2`, not raw TaF rates. The invariant coefficient remains blocked on the `II_s` Hessian on `S^4`. |

## 2026-06-23 Second Parallel Pass (Run 20260623-005611)

Five bounded frontier notes from the second hourly automation pass. All exploration-grade; no promotion to active_research or canon.

| document | status | content |
|---|---|---|
| `explorations/vz1-schur-vertical-extension-2026-06-23.md` | exploration | Extends the VZ Schur calculation: for horizontal covectors, vertical one-forms do not modify the Schur complement (`C_N psi_R = 0`). Horizontal-covector VZ characteristics are contained in the light cone. Mixed 14D covectors remain open. |
| `explorations/ii-s-horizontal-convention-hessian-2026-06-23.md` | exploration | Adopts horizontal-normalized `II_s^H` convention (flat spacetime gives `II_s^H = 0`). Hessian at round S^4 section is Lichnerowicz operator with lowest TT eigenvalue `8/R^2`. Coefficient `C_GU` still tolerance-dependent. |
| `explorations/codazzi-k-term-umbilic-test-2026-06-23.md` | exploration | K(A,s) = 0 for totally umbilic tautological section on maximally symmetric background. R_fail = 0 gives one-equation Lambda constraint. General (non-umbilic) case: trace-free Q(B) must be identified with matter stress. |
| `explorations/n5-parthasarathy-casimir-sl4r-2026-06-23.md` | exploration | Parthasarathy-Casimir condition for fiber Dirac: `pi(C_g) = 9/2 + rho_constant`. Candidate `S(6,4)|_{SL(2,C)} ~= (3/2,1/2) + (1/2,3/2)` at reconstruction grade. Treat as an alternative/tau-twisted representation-theory route; it does not restore the superseded scalar FJ/BC1 chain. |
| `explorations/observer-section-error-model-2026-06-23.md` | exploration | Bridge model: quantum metric measurement gives `epsilon_sec^2 ~ epsilon_dec`. Cross-program contact confirmed structural (shared `t_obs^{-2}`) but not numerically exact. Conditions B1–B3 for exactness named. |

## 2026-06-23 Untouched-Lane Subagent Batch

Five subagents were dispatched against high-impact lanes that were not already covered by the active hourly automation stream. All are exploration-grade; no promotion to active_research or canon.

| document | status | content |
|---|---|---|
| `explorations/type-ii1-finite-control-specialist-pass-2026-06-23.md` | exploration | Type II_1 lane remains open. KO-6 signs pass at the formal real-even sign-package level but are unproven as a finite-control selector. Principal graphs fail as a full SM representation source and remain only a conditional generation-count selector. |
| `explorations/super-ig-algebra-construction-2026-06-23.md` | exploration | A super-IG family can be defined after supplying `(Q, beta)`, but current GU/IG data do not canonically determine a nontrivial `Sp(64)`-equivariant bracket. Not currently needed as a VZ guardian after F6 non-decoupling. |
| `explorations/freed-hopkins-observer-pairing-enriched-bordism-toy-2026-06-23.md` | exploration | First observer-pairing enriched-bordism toy fails as a new anomaly model: metadata descends away; topological observer data is ordinary defect/background enrichment. |
| `explorations/n3-h3-cech-fixture-execution-2026-06-23.md` | exploration | H3 remains open and is sharpened to fixture-specification blocked. `cech_sheaf_fixture` exists only as route/prose, not as a runnable fixture, script, test target, workflow implementation, or exploration file. |
| `explorations/distler-garibaldi-functor-audit-2026-06-23.md` | exploration | Distler-Garibaldi is confirmed as a category-change stress case, not a genuine forgetful-image case. Coarse shadows do not preserve the chirality/generation invariant. |

## 2026-06-23 Five-Goal Verification Batch

Five follow-up subagents were dispatched after the next-five-item inspection. All are exploration-grade and supersede older optimistic language where noted.

| document | status | content |
|---|---|---|
| `explorations/type-ii1-oq1-j2-section-pullback-2026-06-23.md` | exploration | Section pullback preserves the GU real-structure sign: `s*(J_GU)^2 = -1`, not the CC KO-6 `+1`. Literal GU/Type-II_1 contact through ordinary pullback fails unless a twisted or new real structure is added. |
| `explorations/type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md` | exploration | GU inner fluctuations preserve an already input `Sp(64)` connection orbit. They do not derive a finite Connes one-form bimodule or select the SM gauge group. |
| `explorations/signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md` | exploration | Non-compactness alone does not block Atiyah-Janich/KSp classification. The proof obligation is now a continuous H-linear Fredholm family for the actual GU operators on non-compact `Y^14`. |
| `explorations/h3-cech-sheaf-fixture-spec-2026-06-23.md` | exploration | The missing `cech_sheaf_fixture` is specified as an executable contract, but no runnable fixture has been implemented or executed. H3 remains `OPEN_SPECIFIED_NOT_EXECUTABLE`. |
| `explorations/rc1-discrete-series-verification-pack-2026-06-23.md` | exploration | Major correction: the rank-one `BC1` discrete-series chain fails as stated for actual `SL(4,R)/SO_0(3,1)`. The correct metric symmetric-pair analysis has split rank 3 and restricted root system `A3`; claims depending on `(m1,m2)=(7,1)`, scalar FJ poles, and `Lambda_RS^{FJ}=3/2` are demoted pending direct rank-3 or tau-twisted/Kobayashi admissibility computation. |

## 2026-06-23 Five-Task Follow-Up Batch

Five subagents ran the follow-up tasks opened by the prior verification batch. All outputs are exploration-grade and supersede older optimistic language where they conflict.

| document | status | content |
|---|---|---|
| `explorations/tau-correction-oshima-matsuki-rs-2026-06-23.md` | exploration | The asserted `rank_correction(tau_RS)=2` is not supported as a rank-subtraction theorem. The scalar Flensted-Jensen route remains false for the actual rank-3 pair; the tau-twisted RS discrete-spectrum question remains open and needs a direct tau-spherical/Kobayashi admissibility computation. |
| `explorations/oq-weyl3-root-wall-plancherel-2026-06-23.md` | exploration | The root-wall condition `<e2-e3,lambda_RS>=0` does not make the local A3 formal-degree product vanish, because the product uses `lambda_RS+rho_G`. This avoids a zero-factor objection but does not establish a scalar atom; any surviving RS contribution is tau-twisted and conditional. |
| `explorations/split-rank-reconciliation-audit-2026-06-23.md` | exploration | Consolidates the rank correction: scalar `BC1/(7,1)`, `rho=9/2`, `Lambda_RS^{FJ}=3/2`, and the scalar RC3 gap are superseded for `(SL(4,R), SO_0(3,1))` unless rederived inside the tau-twisted coefficient problem. |
| `explorations/ic4-ricci-flat-k3-selection-2026-06-23.md` | exploration | K3-Yau metric selection is conditionally supported only after K3 topology is fixed separately and IC4 supplies the source-free Einstein equation. Willmore energy alone does not select Ricci-flat metrics, since every Levi-Civita section has `E=0`. |
| `explorations/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md` | exploration | Formal H-linear Fredholm/KSp classification is locally resolved once bounded-transform continuity is supplied. Full noncompact `Y^14` weighted Fredholmness, KK zero-mode unitarity, and a b/0/scattering parametrix remain analytic proof obligations. |

## 2026-06-23 Five-Step Execution Batch

The dependency-aware five-step plan was executed across GU formalization and the sibling `temporal-issuance` repository. Outputs remain exploration-grade.

| document | status | content |
|---|---|---|
| `explorations/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md` | exploration | Direct Oshima-Matsuki/Kobayashi check fails as stated. The tau route does not rescue `ind_H(RS)=8`: scalar equal-rank fails, `tau_RS` is nonunitary as a finite-dimensional Lorentz coefficient, the Kobayashi route fails for this pair, and the compact asymptotic cone obstruction is nonzero. |
| `explorations/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md` | exploration | Strongest defensible OC2 result is a conditional tau/discrete-sector Fredholm/KSp theorem. Full unprojected `Y^14` Fredholmness is not defensible from current data, and the required sector projection is now blocked by the failed tau route. |
| `explorations/ic4-source-free-k3-gate-2026-06-23.md` | exploration | Source-free K3 metric selection is conditionally supported only after the topology/index gate selects K3. `T^4` is source-free, Ricci-flat, and Willmore-minimizing, but has `Ahat=0`, so it gives the wrong generation count. |
| `explorations/oq3a-t4-vs-k3-disambiguation-2026-06-23.md` | exploration | Existing untracked note incorporated into the batch: `T^4` is explicitly ruled out by `Ahat(T^4)=0` and `ind_H=8`, while K3 has `Ahat=2` and the target `ind_H=24`, conditional on the parent generation-count formula. |
| `temporal-issuance: explorations/E054-h3-cech-sheaf-fixture-execution-2026-06-23.md` | exploration | Executable H3 fixture returns Outcome `D'`: `c(I_plus)=+1`, `c(I_minus)=-1`, holonomy `-1`, derived from `C` under odd SBP polarity-flip parity and NAC. This opens a conditional derivation path, not a universal H3 identity theorem. |

## 2026-06-23 (late batch) — Freed-Hopkins lane disposition, VZ fifth-theorem canon entry, C_MPR

This batch made **canon status changes** recorded directly in `canon/no-go-class-relative-map.md` (§1 acceptance summary, §2.3 Freed-Hopkins, §2.5 Velo-Zwanziger). The top-level status file is brought into agreement with those canon edits so it is not behind canon. All exploration documents below are exploration/reconstruction-grade; no promotion to active_research or canon beyond the no-go-map surface edits noted.

| document | status | content / canon effect |
|---|---|---|
| `explorations/freed-hopkins-optionb-ksp-family-2026-06-23.md` | exploration (CONDITIONALLY_RESOLVED, scoped) | Eliminates the Riemannian full-section-space candidate by convexity and the `Ω²B Sp(64)` candidate by Sp(64) gauge-background relabeling. Do not cite the convexity argument as a Lorentzian `Y^14 = Met(X^4)` result without a separate signature-component proof. Sole surviving candidate is `X_obs^sol`. |
| `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` | exploration (CONDITIONALLY_RESOLVED, lane-narrowed) | Analyzes the sole survivor `X_obs^sol`. Via the IC4 metric-selection result it conditionally identifies `X_obs^sol = M_RF(K3)`, noncontractible but plausibly a gravitational-background relabel (KSp⁰=KO⁴ class pulled back from the Einstein-metric moduli). The numerical augmentation `ind_H(D_GU)=24` is not load-bearing and remains part of the OPEN generation-count lane. **Verdict downgraded GENUINE_OBSTRUCTION → CONDITIONALLY_RESOLVED (CORRECTION XOBS-IC4-01):** the closed-obstruction reading was same-session verdict inflation resting on the only-CONDITIONALLY_SUPPORTED IC4 input (open F3 trace-free GU source, F5 K3-topology-not-forced). |
| `explorations/no-go-velo-zwanziger-canon-entry-2026-06-23.md` | reconstruction (CONDITIONALLY_RESOLVED) | Formal four-part fifth-theorem canon entry for Velo-Zwanziger (assumptions VZ-H1…H5; the Clifford-module-non-sub-module evasion GU-VZ; forgetful operation `ϕ_mc`; explicit failure conditions FC-VZ-1…5). Synthesis/formalization of the existing §2.5 vz-* chain, not a new computation. |
| `explorations/c-mpr-9tuple-object-morphism-2026-06-23.md` | exploration (CONDITIONALLY_RESOLVED) | Discharges the prerequisite for the C_MPR / 9-tuple / BvN-wall lane: writes the category object `M = (E, ≤_E, Cert, G, ≤_G, r, P_O)`, the morphism, and checks the category axioms. Object/morphism survive the axiom check; the BvN wall itself stays an open proof obligation, not yet a theorem. |

**Canon status changes in `canon/no-go-class-relative-map.md` (this batch):**

1. **Freed-Hopkins observer-pairing Option-B lane — NARROWED, held at CONDITIONALLY_RESOLVED, NOT closed at GENUINE_OBSTRUCTION.** §1 row and §2.3 record the lane as `CONDITIONALLY_RESOLVED / lane-narrowed (reconstruction grade)`. The Riemannian full-section-space candidate is eliminated by convexity, but the same convexity argument does not automatically apply to Lorentzian signature components. The Ω²B Sp candidate gauge-relabels, and the sole surviving K3-conditional candidate `X_obs^sol = M_RF(K3)` is plausibly a gravitational-background relabel — but per **CORRECTION FH-01** (canon) and **CORRECTION XOBS-IC4-01** (exploration file) it is **explicitly NOT promoted to a closed GENUINE_OBSTRUCTION**: the closure reads on a same-session, all-conditional dependency chain whose root (`freed-hopkins-nonforgettable-observer`) is OPEN, whose IC4 input is only CONDITIONALLY_SUPPORTED (open F3 vacuum/trace gate), whose generation-count augmentation is OPEN, and whose KO⁴-over-orbifold lift (RC4) is unproved on the actual non-Hausdorff arithmetic base. Promotion to a closed obstruction is deferred to a later session on tracked, independently-reviewed files. The lane-narrowing is additionally conditional on `X⁴ ∈ K3` (CANON-5 §0.1).
2. **Velo-Zwanziger 14D evasion banner downgraded EVADED → CONDITIONALLY_EVADED (gated on E-block invertibility FC-VZ-1).** §1, §2.5, and the closing posture now carry the 14D leg as `CONDITIONALLY_EVADED` (reconstruction grade), gated on the still-externally-unverified E-block invertibility precondition (Correction VZ-01; GUARD FC-VZ-1). The 4D leg is held at `CONDITIONALLY_RESOLVED` at the principal-symbol level (subprincipal order open per FC-VZ-4; not VERIFIED). The formal fifth-theorem entry above was written into §2.5.

**Net effect:** the lens question "Is RESEARCH-STATUS.md updated if any item changed status?" is now answered Yes for the Freed-Hopkins-lane disposition, the VZ 14D/4D canon banner + fifth-theorem entry, and the C_MPR category result. Note that the Freed-Hopkins item is recorded as **lane-narrowed / CONDITIONALLY_RESOLVED**, not "closed at GENUINE_OBSTRUCTION": corrections FH-01 and XOBS-IC4-01 (this same batch) explicitly refused that closure as same-session verdict inflation, and the top-level status file follows the corrected canon rather than the pre-correction reading.

## 2026-06-22 Additions (Positive GU Constructions Lane)

One new exploration document was added as a new parallel lane of work:

| document | status | content |
|---|---|---|
| `explorations/positive-gu-constructions-lane-proposal-2026-06-22.md` | exploration | Opens the positive GU constructions lane. Five targets: (1) Y¹⁴ / Met(X⁴) metric bundle and pullback maps, (2) Riemannian-Ehresmannian fusion, (3) torsion-for-Λ, (4) spinor group mechanics / shiab from Spin(7,7), (5) Higgs emergence. Includes full six-axis specifications for Targets 1 and 4. Cross-impact assessment: Riemannian-Ehresmannian framing sharpens Witten no-go map; spinor/Spin(7,7) computation is the positive analog of N2; torsion has no current interaction with signed-readout theorem. Tractability ordering: Target 4 (PC1) is highest, Target 5 (PC5) is lowest. |

NEXT-STEPS.md was updated with the five PC-ranked tasks and cross-impact notes.

---

## 2026-06-22 Additions (Five-Run Issuance-Rate Analysis)

Four new exploration documents were added to `explorations/time-as-finality-crosswalk/` following the five-run issuance-rate / observer-contact analysis:

| document | status | content |
|---|---|---|
| `rate-independence-negative-finding-2026-06-22.md` | exploration | Registers the confirmed null result: signed-readout monotonicity criterion is rate-independent with respect to `lambda*(s)`. Closed finding. |
| `rate-independence-worked-check-2026-06-22.md` | exploration | Worked check showing component-by-component why `lambda*(s)` does not appear in the criterion's definition, weight function, information order, scope, or failure condition. Provides the auditable basis for the negative finding. |
| `filtered-sheaf-temporal-obstruction-2026-06-22.md` | exploration | Formalization attempt for the filtered-sheaf temporal obstruction concept (Run 4). Verdict: process-level, collapses to standard Cech cohomology in toy cases. Conditions for re-opening specified. |
| `bvn-gamma-min-convergence-investigation-2026-06-22.md` | exploration | Investigation of the hypothesis that `lambda_max = Gamma_min` (BvN classicality threshold). Verdict: unconfirmed; BvN lane lacks rate-of-classicality formalism; derivation path specified. Most interesting open contact point. |

NEXT-STEPS.md was updated with four follow-on tasks (FR1–FR4) derived from the five-run findings.

## 2026-06-22 FR-Series Execution (Sequential Research Pass)

A sequential research pass executed the FR1–FR4 follow-on tasks and produced a cross-cutting synthesis. New exploration documents in `explorations/time-as-finality-crosswalk/`:

| document | status | content |
|---|---|---|
| `fr1-sorkin-absorption-worked-check-2026-06-22.md` | exploration | FR1 resolved. **Verdict: ABSORBED.** `lambda_max = B / poly(max-past-size(prec, W))`; L2 budget over L4 order-cost, no third input. Sub-result: Sorkin order is rate-blind; the rate cap is a pure L2 capacity effect. |
| `fr4-l6-cadence-parameterization-2026-06-22.md` | exploration | FR4 resolved. **Verdict: NEW L6 FIELD.** Deadline-gated finality (cadence `Delta`) produces a new failure mode — *premature commitment* — provably unreachable under L4 completeness-gating, occurring at any rate. Confirms the issuance-rate family's L6 home. Distinct from FR1's `lambda_max`; respects rate-independence (no structural theorem depends on `Delta`). Exploration-grade L6 field. |
| `fr2-bvn-rate-of-classicality-derivation-2026-06-22.md` | exploration | FR2 resolved (highest-yield). **Verdict: NON-TRIVIAL PROPORTIONALITY.** Supplied the BvN lane's missing rate-of-classicality concept `Gamma_min(epsilon) = ln(1/epsilon)/t_obs`; derived `Gamma_min = ln(1/epsilon)·lambda_max` (coupled via shared `t_obs`); clean equality iff `epsilon=1/e`. Non-trivial L1↔L2 bound `lambda_max <= Gamma/ln(1/epsilon)`. Produces a candidate six-axis L1–L2 coupling rule. Does NOT prove the BvN wall; does NOT change any GU theorem. |
| `fr3-filtered-sheaf-non-collapse-example-2026-06-22.md` | exploration | FR3 resolved. **Verdict: NON-COLLAPSE CONFIRMED; PRIOR VERDICT OVERTURNED.** Explicit toy (`X=S^1`, `F_1=C_{S^1}` with `H^1=C≠0`, `F` flasque with `H^1=0`) gives a genuine transient obstruction `O(1)≠0`, `O(2)=0`. The prior collapse argument tested spatial assembly (subspaces); the real construction is subsheaves over a fixed space, whose inclusions induce non-injective cohomology maps. Sharpening: the obstruction is **structural** (subsheaf cohomology, not determined by `H^1(X,F)`) but indexed by a **filtration**, not a **rate** — so rate-independence is untouched and the object is decoupled from the issuance rate. Belongs to a filtered L1/L2 refinement, not L6. Exploration-grade. |
| `fr-series-synthesis-2026-06-22.md` | exploration | **FR-series synthesis.** Central finding: "the issuance rate" was a portmanteau for **four formally distinct objects at four chain layers** — `lambda_max` (L2, absorbed), `Delta` (L6, new field), `Gamma_min` (L1↔L2, coupled), `O(tau)` (filtered L1/L2, structural). Resolves all three five-run divergences and closes/advances the three GU-relevance conditions (A closed, B advanced, C closed affirmative). Issuance rate proper stays GU-irrelevant structurally; the two structural objects it entangled (FR2 coupling, FR3 obstruction) are separated as the residual targets. No canon change; no no-go bypass. |

---

## 2026-06-22 Additions (UCSD Transcript + Formal Analysis)

Two new documents were added: a primary source transcript and a formal exploration analysis.

| document | status | content |
|---|---|---|
| `literature/weinstein-ucsd-2025-04-transcript.md` | source (raw_transcript) | Full transcript of Eric Weinstein's UCSD April 2025 talk at the Astroparticle Cosmology Cinema, Mayor Room. Recorded by Brian Keating. First primary-source document in the `literature/` folder for GU content (prior literature files are secondary source briefs). |
| `explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md` | exploration | Formal analysis of 8 technical claims from the UCSD talk, assessed against repo canon. Identifies 7 new formal objects not in the positive-constructions-lane proposal (PC1–PC5). Four new follow-on tasks added to NEXT-STEPS.md (VZ1, SC1, DD1, HC1). |

**Key findings from the analysis:**

1. **Velo-Zwanziger is missing from the no-go map.** The transcript confirms GU predicts one family of 16 spin-3/2 particles. Velo-Zwanziger is the primary constraint on spin-3/2 matter coupled to gauge groups. The no-go map currently covers four families (Witten, Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi); Velo-Zwanziger is a fifth that should be added (task VZ1).

2. **N2 (shiab) now has explicit domain/codomain from the primary source.** The transcript names the ship-in-a-bottle operator as mapping Ω²(Y¹⁴) ⊗ S → Ω¹(Y¹⁴) ⊗ S. This is more specific than the current N2 description and should be incorporated (task SC1).

3. **Distortion tensor is distinct from torsion.** D(∇, g) = ∇ − g·∇_LC (using gauge-transformed Levi-Civita) vs. T(∇) = ∇ − ∇_LC (naked Levi-Civita). The distortion is gauge-equivariant; torsion is not. PC4's "torsion-for-Λ" should be sharpened to distinguish these (task DD1).

4. **Three hidden curvature components claim.** The Lorentz curvature tensor breaks into 6 pieces under a group "larger than just the Lorentz group"; 3 are killed by G_μν and 3 are hidden by the torsion-free Bianchi identity. Representation theory check needed to identify the group and verify the count (task HC1).

5. **PC2 first falsification test has a primary-source candidate answer.** The falsification test for Target 1 (Y¹⁴) was: "does a canonical metric on Y¹⁴ exist without prior metric choice?" The transcript provides a specific candidate: trace-reverse the Frobenius metric along the fibers, changing signature from (7,3) to (6,4), to produce an automatic metric. This is the mechanism the analysis identifies as `[reconstruction]`-grade.

6. **No changes to canon or active research.** All findings are exploration-grade. No no-go theorem is claimed bypassed. No Nguyen refutation is claimed.

NEXT-STEPS.md updated with VZ1, SC1, DD1, HC1 tasks and new formal objects table.

---

## 2026-06-22 Phase 1 Parallel Agent Results (Nguyen Critique + Positive Constructions)

Four parallel agents (A-D) ran following the Layer 1-3 completions and the UCSD transcript analysis. Results below. All are exploration-grade; no result promoted to active_research or canon without meeting promotion criteria.

### Nguyen critique lane — significant advances

| finding | status | file |
|---|---|---|
| N1 (signature audit): (9,5) confirmed, Cl(9,5) ≅ M(64,H) | RESOLVED | `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (prior session) |
| N2 (shiab): algebraic map exists under (9,5); anomaly structure partially defused via Sp(64) | SUBSTANTIALLY ADVANCED | `canon/shiab-existence-cl95.md`; `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md` |
| Nguyen §3.1 (complexification gap) | RESOLVED | See N1/N2 files above |
| Nguyen §2 (anomaly pincer) | SUBSTANTIALLY ADDRESSED — Sp(64) replaces U(128) and defuses the original pincer; full local/global GU anomaly cancellation remains open/non-canon | `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md` |
| Residual: IG dimension matching (sp(64) dim = 8256 vs. desired 16384) | OPEN | `NEXT-STEPS.md` N4 |

The Nguyen synthesis document has been updated with §3.1 RESOLVED, §3.2 reclassified from Column A to Column B (substantially addressed), and a new §3.3 generation count entry. See `explorations/nguyen-gu-critique/nguyen-critique-full-synthesis.md`.

### Positive constructions lane — new completions

| finding | status | file |
|---|---|---|
| HC1: "Three hidden curvature components" count | CONFIRMED under torsion-sourcing reading | `explorations/hc1-hidden-curvature-components-2026-06-22.md` |
| DD1: Distortion tensor literature check | PARTIALLY_NAMED (Hehl/Agricola-Friedrich partial; IG-equivariance is novel) | `explorations/dd1-distortion-tensor-literature-check-2026-06-22.md` |
| PC2: Y^{14} bundle formalization stub | COMPLETE (gimmel circularity benign; D_ℊ without section subject to w_2 condition) | `explorations/pc2-met-x4-bundle-formalization-stub-2026-06-22.md` |
| Generation count under Cl(9,5) | OPEN (corrected 2026-06-23; was "CONDITIONALLY 3") — structural mechanism intact, but the RS leg `ind_H(D_RS)=8` has NO surviving analytic derivation: all three analytic routes (scalar FJ/BC1, A3 Harish-Chandra/Atiyah-Schmid, tau-twisted) FAILED, and the APS/K3 route consumes a reverse-engineered physical-DOF rank (FC4 OPEN). The physical-DOF and SM-generation "paths" assume the conclusion; per the UNDISMISSED-CANDIDATE rule the aggregate verdict is OPEN. See DERIVATION-PROGRESS.md CORRECTIONS FC4-HOLONOMY-01 / GEN-04. | `explorations/generation-count-cl95-dirac-derham-2026-06-22.md` |

### Updated research map (Nguyen critique and positive constructions lanes)

| area | status | note |
|---|---|---|
| Nguyen §3.1 | **RESOLVED** | Complexification not needed in (9,5)/quaternionic setting |
| Nguyen §2 (anomaly) | **SUBSTANTIALLY ADDRESSED / full cancellation OPEN** | Sp(64) replaces U(128) and removes Nguyen's original U(1) pincer; local/global anomaly cancellation still needs explicit I_16 and bordism/eta checks |
| Shiab existence | **RESOLVED (existence only)** | One natural real-linear Spin(9,5)-equivariant Clifford-contraction map exists; injectivity/rank/kernel/uniqueness not claimed |
| Dark energy divergence-free | **CONDITIONALLY_RESOLVED** | Noether route depends on unproved action-level structural identification of theta as the relevant Euler-Lagrange sector |
| Generation count | **OPEN** (corrected 2026-06-23; was "CONDITIONALLY 3") | RS-leg analytic index `ind_H(D_RS)=8` not derived (all analytic routes failed; APS rank reverse-engineered, FC4 OPEN); physical/SM counts assume the answer. Per UNDISMISSED-CANDIDATE rule the aggregate verdict is OPEN. See DERIVATION-PROGRESS.md FC4-HOLONOMY-01 / GEN-04. |
| HC1 hidden curvature count | **CONFIRMED** | 3 torsion-sourced pieces via DT=R∧e |
| DD1 distortion nomenclature | **PARTIALLY_NAMED** | IG-equivariance is genuinely novel vs. Hehl/Agricola-Friedrich/Sharpe |
| PC2 bundle formalization | **STUB COMPLETE** | w_2 Gysin computation and branching rules s*(S) still open |

`DERIVATION-PROGRESS.md` updated with Phase 1 Results and Phase 2 Status sections. `NEXT-STEPS.md` updated with N1/N2 marked resolved, three new tasks N4/N5/N6 added. Paper v3 filed at `papers/what-geometric-unity-needs-to-do-next-v3.md`.
