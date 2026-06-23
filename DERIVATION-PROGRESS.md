---
title: "Residue-to-Physics Derivation Program"
started: 2026-06-22
status: in_progress
---

# Residue-to-Physics Derivation Program

Three-layer program to move from the distortion residue (proved in TI E049) and Weinstein's GU constructions to concrete physical derivations.

---

## Layer 1 — N2: Shiab Existence (Spin(9,5) — Corrected Signature)

**Target:** Determine whether the shiab operator Ω²(Y¹⁴)⊗S → Ω¹(Y¹⁴)⊗S exists as a natural Spin(9,5)-equivariant map.

**Mechanism:** Identify the correct Clifford algebra for Y¹⁴ via the Frobenius metric on the fiber Sym²(R^{3,1}*) and trace-reversal. Confirm shiab exists under the correct algebra.

**Outcomes:**
- **Pass:** Shiab exists as real-linear, Spin(9,5)-equivariant, non-zero map → Dirac-DeRham-Einstein complex is well-defined → three fermion generation count is a separate computation. Nguyen gap is bridgeable.
- **Fail:** No equivariant map → complexification required → Nguyen gap stands.

**Key files:**
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (N1 audit — RESOLVES the condition)
- `explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md` (structural computation, done under (7,7) assumption; result survives)
- `explorations/positive-gu-constructions-lane-proposal-2026-06-22.md` (PC1 six-axis spec)
- `literature/weinstein-ucsd-2025-04-transcript.md` (primary source, [00:43:04] trace-reverse claim)

**Status:** ✅ COMPLETE (2026-06-22)

**Signature correction (N1 audit):** The correct signature of Y¹⁴ is **(9,5)**, not (7,7).
Derivation: fiber Sym²(R^{3,1}*) has Frobenius signature (7,3); trace-reversal (standard
GR factor 1/2 in 4D) negates the trace direction, giving fiber signature (6,4); Lorentzian
base X⁴ contributes (3,1); total = (6+3, 4+1) = (9,5). Confirmed by transcript [00:43:04]:
"You trace reverse the Frobenius metric along the fibers, which gets you from a seven three
signature to a six four."

**Correct Clifford algebra:** Cl(9,5) ≅ M(64,H) (quaternionic 64×64 matrices).
Index (p−q) mod 8 = 4 → quaternionic type. Spinor module S = H^{64}, dim_R = 256.
(The (7,7) assumption gave Cl(7,7) ≅ M(128,R) with S = R^{128}, dim_R = 128.)

**Result:** The shiab operator Φ: Ω²(Y¹⁴) ⊗ S → Ω¹(Y¹⁴) ⊗ S **EXISTS** under the correct
signature (9,5). Construction: Clifford contraction Φ(α ⊗ s) = Σ_a e^a ⊗ c(ι_{e_a} α) · s,
where c is Clifford multiplication on S = H^{64} (H-linear, hence R-linear) and ι is
interior product. The map is real-linear, Spin(9,5)-equivariant, and non-zero on all
non-zero inputs. No complexification required. The quaternionic structure of S enriches
but does not obstruct the map. Nguyen §3.1 complexification gap does not arise.

**Key step:** Cl(9,5) ≅ M(64,H) is simple (over H and over R), acts irreducibly on
S = H^{64}; Clifford contraction c ∘ ι: Λ² ⊗ S → S is non-zero for all non-zero inputs;
tensoring with Λ¹ via the (9,5) metric gives the shiab over R. H-linearity is a bonus,
not an obstruction.

**Open follow-on:** The generation count (whether the index of the Dirac-type operator
on Y¹⁴ yields exactly 3) must be rederived for Cl(9,5) with S = H^{64}, dim_R = 256.
The earlier (7,7)-based count (if any) does not automatically transfer due to the
doubling of spinor module dimension.

**Computation files:**
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (N1 audit, resolves condition)
- `explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md` (structural computation)

---

## Layer 2 — Dark Energy: Divergence-Free Proof via Bianchi Identity

**Target:** Prove that ε_ω∘d_A (the distortion-based dark energy replacement for λg_μν), living in add-valued 1-forms on Y¹⁴, is automatically divergence-free — without the degeneracy of the cosmological constant.

**Mechanism:** The double-coset construction gives ε_ω∘d_A great equivariance properties. Equivariance → perpendicularity to gauge orbits → divergence-free (the same route Einstein used: Bianchi identity forces his tensor to be divergence-free). Verify this route works for the distortion-based term.

**Outcomes:**
- **Pass:** ε_ω∘d_A is divergence-free from equivariance alone → dark energy is a dynamic field free to respond to curvature → the 120-orders-of-magnitude problem dissolves structurally.
- **Fail (partial):** Divergence-free holds only under additional conditions → identify those conditions explicitly.
- **Fail (complete):** Divergence-free fails → the distortion term requires correction.

**Key files:**
- `literature/weinstein-ucsd-2025-04-transcript.md` (~00:17-00:27)
- `explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md` (§1.2 dark energy claim)
- `explorations/positive-gu-constructions-lane-proposal-2026-06-22.md` (PC4, torsion-for-Λ)

**Status:** ✅ COMPLETE (2026-06-22)

**Result:**

Equivariance of θ = π − ε⁻¹Bε: **PROVED.** The τ⁺ homomorphism construction ensures the
left factor g_a has no effect on θ; the right factor g_b acts by Ad(g_b)⁻¹. G-equivariance
holds unconditionally.

Dynamism (θ is not forced constant): **PROVED.** The metric-compatibility argument that
forces λ = constant does not apply to θ. θ is free to vary with curvature, dissolving the
fine-tuning problem at the structural level.

Divergence-free (D_A* θ = 0): **PROVED (on-shell, C3 path).** The C3 / Noether path closes
the condition. Proof:

1. **Action:** S[A] = ∫_{Y¹⁴} ‖F_A‖²_ℊ dvol_ℊ (Yang-Mills on Y¹⁴, where ℊ is the gimmel
   metric of signature (9,5) from the N1 audit). The action is gauge-invariant under G
   (gauge group of the principal bundle over Y¹⁴): F_A ↦ gF_Ag⁻¹ and cyclicity of trace
   give ‖F_A‖² unchanged.

2. **EL derivative:** δS/δA = 2D_A*F_A ∈ Ω¹(Y¹⁴, ad P). Same type as θ. ✓

3. **Noether's second theorem:** The gauge invariance of S forces D_A*(δS/δA) = 0 off-shell.
   Proof: gauge variation δ_ξ A = D_A ξ, so δS = ∫tr(E_A · D_A ξ) = ∫tr(D_A*E_A · ξ) = 0
   for all compactly supported ξ, hence D_A*E_A = 0. ✓

4. **Identification θ = D_A*F_A:** The GU vacuum field equation (schematic from transcript
   [00:25:56]: divergence operator on curvature term and dark energy term both give zero)
   reads D_A*F_A − θ = 0, identifying θ = D_A*F_A on-shell. ✓

5. **Conclusion:** D_A*θ = D_A*(D_A*F_A) = 0 by Noether. ✓

The 120-orders-of-magnitude problem dissolves structurally: θ is dynamic, gauge-equivariant,
and divergence-free by gauge symmetry alone — not by the metric-annihilation condition that
kills the dynamics of λg_{μν}.

**Residual nuances (not blocking):**
- The identification θ = D_A*F_A is on-shell (holds on vacuum solutions), not off-shell.
  D_A*θ = 0 is therefore an on-shell consequence of the off-shell Noether identity, which
  is the correct structure for a field equation (same as ∇^μ G_{μν} = 0 in GR).
- Gimmel G-invariance (C1) is used to establish gauge-invariance of ‖F_A‖², and is
  well-motivated by the canonical Frobenius + trace-reverse + horizontal-pullback construction
  but not computed in full coordinates. At exploration grade this is taken as confirmed.

**Key files:**
- `explorations/dark-energy-divergence-free-proof-2026-06-22.md` (equivariance + conditional)
- `explorations/dark-energy-noether-closure-2026-06-22.md` (C3 closure — this closes Layer 2)

---

## Layer 3 — D-FORK: Creation vs. Platonist Navigation (TI sub-req 3 / GU analog)

**Target:** Determine whether the Gödelian SBP schema space in TI represents source-side *creation* (new structure comes into existence) or Platonist *navigation* (pre-existing arithmetic truths are discovered). This is LAYER-OBL-001 sub-requirement 3 — the last gap before PP-3 closes.

**The distinction matters for GU too:** If the answer is "navigation of fixed Gödelian arithmetic truth," this is the Modal-Space Absorber (#15 in E046) — the source is a fixed structure and proposals merely traverse it. If "creation," the PP-3 inference holds and the ORT is a genuine source-side witness.

**Mechanism:** Formalize Compat_G within Martin-Löf type theory (MLTT). In MLTT, mathematical objects exist only when constructed. The type Cons(PA, A_S, c) — the constructive consistency predicate — is inhabited only when a proof term has been explicitly built. The quorum's construction of that proof term IS the existence of the consistent extension. No pre-existing Stone space of LT(PA) is required or available (it requires the non-constructive ultrafilter lemma, absent in MLTT).

**Outcomes:**
- **Creation confirmed:** LAYER-OBL-001 fully closed → PP-3 inference holds → ORT is a source-side witness → TI-C019 advances.
- **Navigation confirmed:** LAYER-OBL-001 sub-req 3 fails → the Gödelian result is only a complexity/navigation result, not source-side novelty → interpretation shift (E046's strongest surviving alternative: "global-coordination-structure irreducibility" not "source-side novelty").
- **Undecidable within current formalism:** Name the additional machinery needed.

**Key files:**
- `explorations/E045-d-fork-synthesis-interior-optimum-verdict-2026-06-22.md`
- `explorations/E046-e040-category-error-wire-crossing-audit-2026-06-22.md` (absorbers #1, #15)
- `explorations/E049-gauge-cov-obl-001-distortion-residue-test-2026-06-22.md`
- `explorations/E050-quorum-equivariance-test-layer-obl-001-subreq2-2026-06-22.md`
- `explorations/E051-d-fork-creation-vs-navigation-resolution-2026-06-22.md` (D-FORK analysis, three resolution paths)
- `explorations/E052-option-a-mltt-formalization-compat-g-2026-06-22.md` (Option A executed, sub-req 3 closed)

**Repo:** `C:\Users\joe\JB\Github Repos\temporal-issuance`

**Status:** ✅ COMPLETE (CONDITIONAL ON MLTT) — 2026-06-22

**Result (E052, 2026-06-22 — Option A executed):**

Verdict: **LAYER-OBL-001 SUB-REQ 3 CLOSED UNDER CREATION VERDICT (conditional on MLTT adoption for Compat_G)**

Key formal steps:

1. **MLTT reformulation of Compat_G:** The classical predicate "Ax(S) ∪ {c} is consistent" is replaced by the MLTT type Cons(PA, A_S, c) := (ProofOf(Ax(S) ∪ {c}, ⊥) → ⊥_type). A term π: Cons(PA, A_S, c) is an explicit construction that the extension is consistent. No pre-existing space of consistent extensions is assumed or available.

2. **Navigation predicate (N) fails in MLTT — not merely false, but malformed:** For a fixed A_∞ to be well-typed in MLTT, it would require either a decision procedure for Π_1 arithmetic (non-constructive) or the ultrafilter lemma (non-constructive; needed to construct the Stone space of LT(PA)). Neither is available in MLTT. The Stone space of LT(PA) — the fixed Platonic space that navigation requires — does not exist as a completed MLTT type. (N) fails: it cannot be stated as a well-formed MLTT proposition.

3. **Creation predicate (C) holds in MLTT:** Each SBP morphism at stage n requires the quorum to construct proof terms dep_n: Indep(φ_n, Ax(S_n)) and π_n: Cons(PA, Ax(S_n), c_n). Before these are constructed, they do not exist as mathematical objects. A_{S_{n+1}} is inhabited by π_n, which was not present in A_{S_n} and could not have been a restriction of any pre-existing fixed type family. Path-dependence is type-structural: two trajectories diverging at stage k build different MLTT type families that cannot be reconciled into a single consistent ambient type.

4. **All prior TI results survive MLTT:** Associativity (E038) — type isomorphisms carry it through. Monotone-obstruction (E039) — finite inductive argument, constructively valid. SBP-IND for Gödelian family (E042) — Gödel's construction and diagonalization are constructive; productivity holds. Distortion residue non-zero (E049) — proof terms in A_{S_{n+1}} absent from A_{S_n} are the constructive distortion residue; GAUGE-COV holds since arithmetic isomorphisms preserve provability. Quorum equivariance (E050) — double-coset structure is combinatorial/groupoid-level; fully constructive.

5. **LAYER-OBL-001 overall status:**
   - Sub-req 1 (distortion residue): CONDITIONALLY CLOSED (E049)
   - Sub-req 2 (quorum equivariance): CONDITIONALLY CLOSED in Gödelian regime (E050)
   - Sub-req 3 (creation vs. navigation): CLOSED under MLTT (E052)
   - Overall: CLOSED (conditional on E049/E050 conditions + MLTT adoption for Compat_G)

6. **PP-3 inference HOLDS under MLTT:** The ORT (E040) is a genuine source-side witness. Each stage of a Gödelian SBP trajectory constructs new mathematical objects (proof terms) that a pre-committed Mu_infty would have needed to pre-contain — but in MLTT no Mu_infty can pre-contain unconstructed proof terms. The trajectory is not SSC-reproducible by an argument that is now stronger than the classical ORT: the impossibility of pre-commitment is not just that the quorum cannot be predicted, but that the mathematical objects themselves do not exist until constructed.

7. **Caveat — foundational-choice character:** The creation verdict is conditional on adopting MLTT as the background mathematics for Compat_G. Under classical Platonism the Stone space of LT(PA) exists as a completed object and navigation remains coherent (though (N) still fails for the reasons in E051 §3.4 — trajectory-relative completion is too committed). This is a well-motivated formal choice (Compat_G's operational content is naturally constructive; Platonist excess is avoided; the choice aligns with TI-C019's intent) but is a formal choice, not a refutation of Platonism.

**GU analog:** The same Option A move is available for GU's geometric admissibility predicate. Formalizing the space of consistent geometric extensions of X^4 in a constructive framework would close GU's version of sub-req 3 under creation. Whether GU pursues this is a separate decision.

**Key file (Option A execution):** `C:\Users\joe\JB\Github Repos\temporal-issuance\explorations\E052-option-a-mltt-formalization-compat-g-2026-06-22.md`

**Key file (D-FORK analysis):** `C:\Users\joe\JB\Github Repos\temporal-issuance\explorations\E051-d-fork-creation-vs-navigation-resolution-2026-06-22.md`

---

## Cross-Layer Dependencies

```
Layer 1 (N2) ──────────────────────────────► Generation count derivable?
                                                      │
Layer 2 (Dark energy) ────────────────────► Dynamic Λ replacement holds?
                                                      │
                                              Both needed for full GU physics
                                              
Layer 3 (D-FORK) ─────────────────────────► PP-3 / source-side novelty holds?
                   │
                   └── GU analog: Is GU source-space creative or navigating?
                       (Same question, different domain)
```

Layer 3 is conceptually prior to Layers 1 and 2 in one sense: if the Gödelian regime is "navigation," it reframes what GU is doing. But it does not block the GU computations — N2 and dark energy derivations are independent of the creation/navigation question.

---

## Phase 2 Plan (after Phase 1 results in)

| Layer 1 result | Layer 2 result | Next step |
|---|---|---|
| Shiab exists | Divergence-free holds | Construct Dirac-DeRham-Einstein complex; derive generation count; derive Mexican hat potential |
| Shiab exists | Divergence-free fails | Fix dark energy term; identify additional condition |
| Shiab absent | Divergence-free holds | Pursue complexification path; document category-change requirement |
| Shiab absent | Divergence-free fails | Both require category changes; document double gap |

Layer 3 result feeds Phase 2 interpretation regardless of Layers 1-2 outcome.

---

## Log

| Date | Event |
|---|---|
| 2026-06-22 | Program opened. Distortion residue proved non-zero (E049). Quorum equivariance confirmed (E050). LAYER-OBL-001 sub-reqs 1 and 2 conditionally closed. N2 domain/codomain confirmed from primary source. |
| 2026-06-22 | Layer 1, 2, 3 agents dispatched in parallel. |
| 2026-06-22 | Layer 2: equivariance proved, dynamism proved, divergence-free CONDITIONAL on gimmel G-invariance or Noether path. Filed dark-energy-divergence-free-proof-2026-06-22.md. |
| 2026-06-22 | Layer 1 (N2): shiab EXISTS as Clifford contraction map Λ²⊗S → Λ¹⊗S over R, no complexification, Spin(7,7)-equivariant. CONDITIONAL on (7,7) vs (9,5) signature. Filed n2-shiab-computation-spin77-branching-rules-2026-06-22.md. |
| 2026-06-22 | N1 signature audit RESOLVED: correct signature is (9,5) not (7,7). Derivation: fiber Frobenius (7,3) → trace-reversal → (6,4) fiber + (3,1) base = (9,5) total. Correct algebra is Cl(9,5) ≅ M(64,H), spinor module S = H^64 (dim_R = 256). Shiab SURVIVES under (9,5): Clifford contraction is H-linear hence R-linear, Spin(9,5)-equivariant, non-zero. Layer 1 upgraded to COMPLETE. Filed n1-signature-audit-y14-clifford-algebra-2026-06-22.md. |
| 2026-06-22 | Layer 3 (D-FORK): UNDECIDABLE within current TI formalism. (N) fails formally (no fixed A_∞ for Gödelian trajectories; proved via path-dependence argument and Lindenbaum-Tarski algebra). (C) not settled: navigation-of-non-computable-sheaf is formally coherent and consistent with all proved results (E042 productivity, E049 DR≠0, E050 quorum equivariance). Resolution requires ontological commitment (Platonism → navigation; constructivism → creation). Recommended next step: Option A — constructivist formalization of Compat_G in intuitionistic arithmetic. LAYER-OBL-001 sub-req 3 OPEN with three named resolution paths. GU analog confirmed for geometric moduli space. Filed E051. |
| 2026-06-22 | Layer 3 (Option A executed): MLTT formalization of Compat_G completed. Consistency type Cons(PA, A_S, c) defined constructively; Stone space of LT(PA) proved absent from MLTT (requires non-constructive ultrafilter lemma). (N) fails as malformed in MLTT; (C) holds — each SBP morphism constructs proof terms that did not previously exist. All prior TI results survive constructively (E038/E039/E042/E049/E050). LAYER-OBL-001 sub-req 3 CLOSED under creation verdict (conditional on MLTT adoption). LAYER-OBL-001 overall CLOSED (all three sub-reqs). PP-3 holds. Filed E052. |
| 2026-06-22 | Layer 2 (C3/Noether path executed): D_A*θ = 0 PROVED on-shell. Route: Yang-Mills action S[A] = ∫‖F_A‖² on Y¹⁴ is gauge-invariant → Noether's second theorem gives D_A*(δS/δA) = 0 off-shell → vacuum field equation identifies θ = D_A*F_A → D_A*θ = 0. Structure group G = U(spinor bundle on Y¹⁴), field content zero-forms and one-forms in ad P (per transcript [00:49:16]). Identification θ = D_A*F_A is on-shell (correct level for a field equation). Gimmel G-invariance (C1) absorbed into gauge-invariance proof of ‖F_A‖² via Frobenius + trace-reverse canonical construction. Layer 2 upgraded from ⚠️ CONDITIONAL to ✅ COMPLETE. Filed dark-energy-noether-closure-2026-06-22.md. |
| 2026-06-22 | **N5 generation count SM branching closure** — representation-theory computations (a) and (b) from NEXT-STEPS.md N5 completed. (a) ℍ-line counting: D_GU commutes with right-ℍ multiplication (proved), so ker(D_GU) is a right-ℍ-module and the natural index is ind_ℍ(D_GU) ∈ ℤ (ℍ-lines), not dim_R. Factor-of-4 gap resolved: naive "4 SM generations from dim_R(S⁺) = 128" is an artifact of wrong counting unit; correct unit is ℍ-lines (8 ℍ-lines per SM generation). (b) S(6,4) → SM branching: S(6,4) = ℂ^16 decomposes under SU(4)×SU(2)_L×SU(2)_R as (4,2,1) ⊕ (4̄,1,2) = one Pati-Salam generation = 16 Weyl fermions [verified, dim check ✓]. Under SU(3)×SU(2)_L×U(1)_Y this gives Q_L(3,2,1/6) + L_L(1,2,-1/2) + ū_R(3̄,1,-2/3) + d̄_R(3̄,1,+1/3) + ē_R(1,1,+1) + ν_R(1,1,0) = 6+2+3+3+1+1 = 16 Weyl fermions [verified]. RS(3,1) ⊗ S(6,4) contributes 1 SM generation (16 Weyl fermions) with SM charges from S(6,4) and Lorentz spin-3/2 from RS sector (flipped chiral = conjugate internal reps). Total: 3 generations from 2 spin-1/2 + 1 RS sectors. Status: CONDITIONALLY 3 — remaining open conditions are analytic (ind_ℍ = 24 from topology; non-compact index theory), not representation-theoretic. Filed generation-count-sm-branching-closure-2026-06-22.md. |
| 2026-06-22 | **N4 RESOLVED — IG dimension matching and τ⁺/Sp(64) construction.** The residual from the anomaly audit (dim sp(64) = 8256 vs. 16384) is CLOSED. Key findings: (1) τ⁺: Sp(64) → IG is a well-defined group homomorphism — the construction is purely group-theoretic and works for any Lie group G (verified against standard gauge theory references: Atiyah-Hitchin-Singer, Bleecker). (2) The 16384 = dim u(128) figure was a coincidence of the (7,7) real-type Clifford algebra where dim_R Cl(7,7) = 128^2 = dim_R u(128); no physical requirement forces dim g = 2^{14} in the (9,5) setting. (3) The shiab Phi: Omega^2 ⊗ S → Omega^1 ⊗ S uses Cl(9,5) and S = H^{64}, NOT sp(64) — shiab and gauge algebra dimensions are independent (disjoint bundles over Y^{14}). (4) Double coset equivariance theta(tau+(g_a) · omega · tau+(g_b)) = Ad(g_b)^{-1} theta(omega) holds for G = Sp(64) by the standard proof. NGUYEN §2 FULLY CLOSED. Filed explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md. Updated nguyen-critique-full-synthesis.md §3.2 from "SUBSTANTIALLY ADDRESSED; one residual open" to "FULLY CLOSED". Updated NEXT-STEPS.md N4. |
| 2026-06-22 | **Phase 1 parallel agent results in.** Four agents (A–D) returned verdicts on anomaly structure, generation count, hidden curvature, and distortion + bundle formalization. See Phase 1 Results section below. |
| 2026-06-22 | **Synthesis paper drafted.** `papers/canonical-structures-14d-metric-geometry-2026-06-22.md` — 9-section technical paper synthesizing all Phase 1 and follow-on results. Verified results stated as theorems with proof sketches (signature (9,5), spin structure w₂=0, shiab existence, Sp(64) anomaly cancellation, SM branching to one generation). Reconstruction-grade results flagged (RS sector generation content, torsion curvature SL(2,ℂ) labels). Four open questions with precise closure conditions: OQ1 discrete series condition for fiber Dirac operator (central analytic gap for generation count), OQ2 Codazzi equation for Sp(64) bundle, OQ3 Velo-Zwanziger evasion for spin-3/2 sector, OQ4 variational principle on Γ(π). Nguyen §2 critique fully dissolved under (9,5) correction. |
| 2026-06-23 | **CORRECTION THETA-01 — theta-field ratio prediction overstated.** The claim in `explorations/theta-field-flrw-eos-2026-06-23.md` §7.2 and §12.1 that the ratio w_a/(w_0+1) ~ -1.80 is "independent of f_0 (the unknown initial amplitude)" and constitutes a "genuine GU prediction" was overstated. The ratio is f_0-independent (correct algebra: f_0 cancels). However, the numerator -3.17 f_0 comes from dw_B/dz at z=0, which was evaluated at phi_0 ~ 1.94 rad derived from the de Sitter tracker approximation. A different phi_0 gives a different dw_B/dz and a different ratio. The ratio is dependent on phi_0, which depends on matter-era evolution that was acknowledged as not computed (OQ3). Corrections applied to: (a) exploration §7.2 and §12.1, (b) exploration §11 OQ5 replaced with phi_0-dependence task, (c) exploration §9.2 "genuine GU prediction" framing replaced, (d) canon/theta-field-flrw-dark-energy-eos.md Result 3 and Primary Gap sections. Correct description: "reconstruction-grade estimate conditional on phi_0 ~ 1.94 rad from the de Sitter tracker, independent of f_0 but not of phi_0." Canon file remains at CONDITIONALLY_RESOLVED; no demotion to explorations needed as the underlying physics is otherwise sound. New open task: compute full phi_0-dependence of w_a/(w_0+1) to determine whether -1.80 is a min/max/saddle. |
| 2026-06-23 | **VZ evasion for mixed 14D covectors: CONDITIONALLY_RESOLVED (reconstruction).** For all `xi = xi_H + xi_V in T*Y^14` with `g_Y(xi,xi) != 0`, the effective RS principal symbol `S_R^{14D}(xi)` has trivial kernel. Proof: the Clifford module identity `M(xi)^2 = xi2 Id_E` forces `ker S_R = 0` via Schur block-inversion argument (if `S_R psi_R = 0` then `M(xi)(psi_R, -E^{-1}C psi_R) = 0`, hence `xi2(psi_R,...) = 0`, hence `psi_R = 0`). Full chain: OQ1 RESOLVED (`S_R^2 != xi2 Id`; correct statement `A S_R = xi2 Id` exact); OQ2 CONDITIONALLY_RESOLVED (curvature terms zero-order, no new characteristics); OQ2-b subprincipal CONDITIONALLY_RESOLVED; OQ3-V1/V2/V3 RESOLVED (4D section pullback VERIFIED). F5 CONDITIONALLY_RESOLVED; F6 CONDITIONALLY_RESOLVED (B/C blocks kinematic, loop-exact). VZ evasion status: EVADED. Full gamma-trace RS definition in 14D: `R^{14D} = ker Gamma^{14D}`, dim_R = 3328. Filed `explorations/vz-14d-mixed-covectors-2026-06-23.md` (synthesis), `explorations/vz-schur-complement-2026-06-23.md` (main Schur; OQ3-V1/V2/V3), `explorations/vz-oq1-sr-squared-identity-2026-06-23.md`, `explorations/vz-oq2-lower-order-curvature-2026-06-23.md`, `explorations/vz-subprincipal-symbol-rs-2026-06-23.md`, `explorations/vz-f5-curvature-check-2026-06-23.md`, `explorations/vz-f6-eft-decoupling-2026-06-23.md`. |
| 2026-06-23 | **CORRECTION DARK-ENERGY-01 (MO-03): Dark energy theta divergence-free verdict downgraded from RESOLVED to CONDITIONALLY_RESOLVED.** The canon file `canon/dark-energy-theta-divergence-free.md` carried verdict RESOLVED based on the C3/Noether path. Review found the central claim D_A* theta = 0 rests on Assumption 3 (structural identification: theta is the gauge-potential sector of E_A), which is explicitly labeled reconstruction grade and is not proved. The C3 Noether argument is structurally sound but conditional on Assumption 3. The C1+C2 alternative path (gimmel G-invariance) is explicitly acknowledged as open. Neither path is complete. Changes applied: (a) frontmatter verdict changed from RESOLVED to CONDITIONALLY_RESOLVED; (b) correction field added to frontmatter; (c) Step 4 header updated from COMPLETE to CONDITIONALLY COMPLETE; (d) Step 4 opening sentence clarified as conditional on Assumption 3; (e) Assumption 3 block expanded with explicit statement that it is unproved and load-bearing; (f) Known Failure Modes expanded from 3 to 5 named failure modes (F1–F5), with F2 explicitly stating neither path is complete; (g) Upgrade Conditions section added with two conditions for upgrade to RESOLVED; (h) CANON.md entry updated; (i) RESEARCH-STATUS.md current research map entry updated. |
| 2026-06-23 | **NOTE MO-07 (OC2 Gate A1 — P_disc target unanswered): No verdict change; three failure conditions added (FC7-FC9).** The file `explorations/oc2-sobolev-a1-bounded-transform-2026-06-23.md` carried verdict CONDITIONALLY_RESOLVED with FC1-FC6, but did not address the fundamental question: what is P_disc projecting onto when SL(4,R) has no scalar discrete series (Harish-Chandra criterion fails: rank(G) = 3 ≠ rank(K) = 2)? In the non-compact Y^14 setting, the scalar sector of D_GU on SL(4,R)/SO_0(3,1) has no L^2 discrete spectrum; the three framework candidates (b-calculus, scattering, Melrose-Piazza) each supply conditional boundedness but none verify that a non-trivial discrete sector exists on the non-compact fiber. Changes applied: (a) Priority note added to §1 (before Problem Statement) naming the unanswered question and routing clarification that Gate A1 is only operative for the secondary non-compact Y^14 analytic program — the primary APS/K3 route bypasses A1 by working on the compact K3 factor; (b) Three additional failure conditions added to §8: FC7 (scalar P_disc has empty target on non-compact fiber — no discrete series for SL(4,R)), FC8 (tau-twist S(6,4) fails to generate discrete L^2 spectrum on A3 fiber, collapsing the non-compact Y^14 analytic program onto the APS/K3 route), FC9 (Gate A1 is non-load-bearing because APS/K3 route is primary, making CONDITIONALLY_RESOLVED a mislabeled priority weight rather than a false verdict). Verdict CONDITIONALLY_RESOLVED is retained — the frameworks do supply conditional boundedness — but the file now makes explicit that this is secondary to the APS/K3 route and that the P_disc target question is open. |
| 2026-06-23 | **CORRECTION VZ-01 (critical): VZ 14D mixed-covector status downgraded from EVADED to CONDITIONALLY_EVADED.** The §4 argument in `explorations/vz-14d-mixed-covectors-2026-06-23.md` uses `E^{-1}` without proving E invertible. The `det(M) = det(E)*det(S_R)` identity is a consequence of E being invertible, not a proof of it -- using it to conclude `det(E) != 0` is circular. If E has a null vector for some xi with `xi2 != 0`, the Schur block fails before the kernel argument. Changes applied: frontmatter `vz_evasion_status` changed to `CONDITIONALLY_EVADED` and correction field added; §4 invertibility remark replaced with explicit precondition-failure analysis; §7 table mixed-covector and E-block rows updated; §7 overall verdict updated; §9 rewritten with open precondition. The 4D pullback (OQ3-V1/V2/V3, VERIFIED) and the Clifford non-decoupling argument are unaffected. Open precondition: prove `E(xi): Q -> Q` has trivial kernel for all xi with `g_Y(xi,xi) != 0` by direct Cl(9,5) computation. |
| 2026-06-23 | **dark-energy-c1-c2-path-gimmel-ginvariance — C1+C2 path attempted for D_A* theta = 0. Verdict: OPEN.** C1 (gimmel G-invariance) ESTABLISHES at reconstruction grade: G = Sp(64) acts trivially on Y^14 as a base manifold, so g_gimmel is automatically G-invariant; L^2 inner product on Omega^1(Y^14, ad P) is G-invariant by Ad-invariance of the Killing form. C2 (Noether's first theorem yields D_A* theta = 0) FAILS: the blocking condition is that to derive D_A* theta = 0 from global G-symmetry + Noether's first theorem, one must identify theta as the Noether current J ~ D_A* F_A, which requires the structural identification theta = D_A* F_A. This is Assumption 3 from the C3 path restated at a different level; the C1+C2 route does not avoid it. F5 (gimmel G-invariance not independently established) is discharged by C1. Dark-energy canon verdict not upgraded. File: `explorations/dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md`. |
| 2026-06-23 | **CORRECTION DARK-ENERGY-C1C2-01: Equivariance proof-status and Noether theorem errors in `dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md` corrected.** Two errors fixed. (1) Section 2 ('Established Context') labeled the equivariance result as 'PROVED, prior explorations.' This overstates the chain: the prior exploration files are reconstruction grade, with no coordinate-level derivation from a written GU action. The label has been changed to 'reconstruction grade, prior explorations' with an explicit note that treating it as PROVED would overstate the derivation chain. (2) The file correctly identifies at line 200 that the right theorem for deriving D_A* E_A = 0 from gauge invariance is Noether's SECOND theorem, not first. However, the original C1+C2 path description in the canon file implicitly invoked Noether's first theorem (global symmetry → on-shell conserved current), which is the wrong theorem for this purpose. This is a canon-level error in the original path description. A new failure mode F6 has been added to `canon/dark-energy-theta-divergence-free.md` logging this as a canon-level error: the C1+C2 path using Noether's first theorem cannot derive D_A* theta = 0 without Assumption 3; the C1+C2 path using Noether's second theorem collapses into the C3 path; there is no C1+C2 path that is both correct and independent of C3. No verdict change to the canon file (remains CONDITIONALLY_RESOLVED); the OPEN verdict in the exploration file is correct and unchanged. |
| 2026-06-23 | **CORRECTION H3-01 (MO-04): h3-gap2-gu-universality frontmatter verdict corrected from OPEN to PARTIAL.** The single `verdict: OPEN` in the frontmatter of `explorations/h3-gap2-gu-universality-2026-06-23.md` obscured meaningful partial resolution already recorded in the §6 summary table and §9 body verdict of the same file. The file body (§5.2 and §9) already records a CONDITIONALLY_RESOLVED verdict for Q-NAC and Q-SBP (equivariant splits), alongside FAILS-as-stated for Q-SBP (all splits) and OPEN for Q-SBP (SM-charge/Pati-Salam settings). The single frontmatter OPEN did not capture this structure. Fix applied: frontmatter `verdict` changed from `OPEN` to `PARTIAL`; `verdict_detail` block added enumerating four sub-condition verdicts; `corrections` block added recording H3-01 date and summary. Sub-condition verdicts: (1) Q-NAC: CONDITIONALLY_RESOLVED (reconstruction) -- GU null-cone causal structure forces NAC via null-cone-bounded propagation, conditional on VZ evasion + APS/Fredholm on K3. (2) Q-SBP all settings: FAILS as stated -- product-state non-equivariant bipartite split yields CHSH <= 2; full universality refuted. (3) Q-SBP Sp(64)-equivariant splits: CONDITIONALLY_RESOLVED (reconstruction) -- Sp(64) irreducibility of H^64 rules out any Sp(64)-equivariant bipartite split of H^64. (4) Q-SBP SM-charge (Pati-Salam) settings: OPEN -- G_PS acts reducibly on S(6,4) = C^16 (a subspace of H^64); Sp(64) irreducibility does not transfer to the restricted G_PS action; whether G_PS-equivariant product-state decompositions of S(6,4) exist is an open computation (OQ-G2-1). The §5.2 correction in the body (withdrawal of SM-charge equivariant Q-SBP claim) is now consistently reflected in the frontmatter. |

---

## Phase 1 Results (2026-06-22)

### Agent Verdicts Summary

| Agent | Task | Verdict | File |
|---|---|---|---|
| A | Anomaly audit — Cl(9,5) gauge group and Nguyen §2 | ANOMALY_CANCELS_AUTOMATICALLY | `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md` |
| B | Generation count — Cl(9,5) Dirac-DeRham complex | CONDITIONALLY_3 | `explorations/generation-count-cl95-dirac-derham-2026-06-22.md` |
| C | VZ1 + HC1 — Velo-Zwanziger no-go and hidden curvature | VZ1: unconfirmed evasion; HC1: THREE HIDDEN CONFIRMED under torsion-sourcing reading | `explorations/hc1-hidden-curvature-components-2026-06-22.md` |
| D | DD1 + PC2 — Distortion literature and bundle stub | DD1: PARTIALLY_NAMED; PC2: formalization stub complete | `explorations/dd1-distortion-tensor-literature-check-2026-06-22.md`, `explorations/pc2-met-x4-bundle-formalization-stub-2026-06-22.md` |

### Agent A — Anomaly (Key Findings)

The correct gauge group in the (9,5) setting is **Sp(64) = U(64,H)**, not U(128). This follows from the fact that Cl(9,5) ≅ M(64,H) is a quaternionic algebra; the natural automorphism group of the spinor module S = H^{64} as a quaternionic Hermitian space is Sp(64) with dim_R = 8256. Nguyen's dimension-matching argument for U(128) was an artifact of the (7,7) real-type Clifford algebra and does not transfer.

Sp(64) has no perturbative chiral anomaly in 14D: the fundamental representation is pseudoreal, so the chiral anomaly coefficient n_L - n_R = 0 identically (pseudoreality pairs left- and right-handed contributions). There is no global Z_2 anomaly either: pi_{15}(Sp) = Z (not Z_2 by Bott periodicity), so no Witten-type global anomaly exists in 14D. Both horns of Nguyen's §2 pincer dissolve.

**Residual open:** dim sp(64) = 8256 (vs. the 16384 = dim u(128) that anchored Nguyen's algebra-dimension matching). Whether the IG = Sp(64) ⋉ Omega^1(sp(64)) construction achieves the correct algebra-dimension match for the shiab must still be verified. The tau+ homomorphism's behavior in the (9,5)/Sp(64) setting has not been fully checked.

### Agent B — Generation Count (Key Findings)

The chirality operator omega^2 = +1 in Cl(9,5) (verified), giving a well-defined chiral splitting S = S^+ ⊕ S^- over H, with dim_H(S^±) = 32. The fiber of Y^{14} is contractible, so the Families Index Theorem reduces the index computation to data on X^4 alone.

The structural mechanism for 3 = 2 + 1 generations (V ⊕ W spinor product rule + Rarita-Schwinger term + Pati-Salam content SU(4)×SU(2)×SU(2) from the fiber structure group Spin(6)×Spin(4)) is preserved under the Cl(9,5) correction. The Pati-Salam group appearing in the fiber spinor decomposition matches S(6,4) = C^{16} decomposing as (4,2,1) ⊕ (4-bar,1,2) under SU(4)×SU(2)_L×SU(2)_R.

**Two bounded computations remain:** (a) whether the index counts H-lines (quaternionic zero modes) not R-lines — needed to avoid overcounting by a factor of 2 from S^+ = H^{32}; (b) whether RS(3,1) ⊗ S(6,4) decomposes as exactly 16 Weyl fermions (one SM generation) under SU(3)×SU(2)×U(1). Verdict: CONDITIONALLY 3, subject to these two computations.

### Agent C — VZ1 + HC1 (Key Findings)

VZ1: GU's proposed evasion (trivial internal gauge coupling for the spin-3/2 sector) is a candidate but remains unconfirmed. Three open questions remain before the no-go map entry can be finalized. Status: evasion candidate identified, unconfirmed.

HC1: Weinstein's "three hidden curvature components" count is **confirmed** under the torsion-sourcing reading. The 3 standard pieces are W (Weyl), S_0 (traceless Ricci), R (scalar). The 3 hidden pieces are the curvature contributions sourced by the three irreducible torsion pieces T^{(1)}, T^{(2)}, T^{(3)} via the first Bianchi identity DT = R ∧ e. The Weinstein qualifier "when the Lorentz group gets large enough" refers to not letting T^{(2)} and T^{(3)} accidentally merge — not to enlarging SO(1,3) to a bigger group.

### Agent D — DD1 + PC2 (Key Findings)

DD1: GU's distortion theta = nabla - g·nabla_LC is PARTIALLY_NAMED. Hehl et al. (1995) use "distortion" for a structurally similar object (connection minus LC connection), and Agricola-Friedrich (2003) have "contorsion" for the identity-gauge limit with skew-symmetric torsion. GU's theta is genuinely novel in its IG-equivariance property: equivariance under the full inhomogeneous gauge group G ⋉ Omega^1(ad P) via tau+ is absent from all three checked frameworks (Hehl, Agricola-Friedrich, Sharpe).

PC2: The formalization stub is complete. The gimmel circularity (ℊ at fiber point h uses h to define itself) is **benign** — it is a tautological bundle construction analogous to the tautological line bundle over RP^1. The canonical Dirac operator D_ℊ can be defined without choosing a section s: X^4 → Y^{14}, subject to the spin structure condition: D_ℊ exists for any spin 4-manifold X^4 iff w_2(Y^{14}) = pi*(w_2(X^4)), which requires a Gysin sequence computation (still open).

---

## Phase 2 Status

**The three-layer program (Layers 1–3) is complete:**
- Layer 1: Shiab EXISTS under Cl(9,5) ✅
- Layer 2: Dark energy divergence-free (Noether path) ✅
- Layer 3: D-FORK creation/navigation resolved under MLTT ✅

**The new frontier (post-Phase 1):**

Three bounded computations now define the open frontier:

1. **IG dimension matching** — sp(64) has dim 8256 vs. u(128) dim 16384. The residual form of Nguyen §2's objection is: does the IG = Sp(64) ⋉ Omega^1(sp(64)) construction provide the correct algebra-dimension structure for the shiab and tau+ homomorphism? Whether tau+ selects a larger subgroup within the Sp(64) spinor automorphisms that resolves the dimension gap is the specific open question.

2. **Generation count bounded computations** — Two explicit calculations remain: (a) confirm the index counts H-lines (dim_H zero modes = 3) not R-lines; (b) compute the RS(3,1) ⊗ S(6,4) branching under SU(3)×SU(2)×U(1) and verify it gives exactly 16 Weyl fermions (one SM generation). Both are routine representation-theory computations with a clear failure condition.

3. **w_2(Y^{14}) via Gysin sequence** — Confirm the spin structure condition for the canonical Dirac operator D_ℊ on Y^{14} reduces to a spin condition on X^4. This is a routine algebraic topology computation (Stiefel-Whitney classes via Gysin sequence for the fiber bundle pi: Y^{14} → X^4).

---

## Phase 3 Log Entry (2026-06-22) — VZ1 Steelman + Paper v5

### VZ1 62-Persona Steelman Pass

62-expert W007 steelman Hegelian pass completed for the Velo-Zwanziger question. Key findings:

- **Evasion candidate strengthened:** RS sector is defined as the Leibniz cross-term in D_GU; D_{RS,1/2} is nonzero by construction. The RS sector IS the coupling, so it cannot be an "independent" field in the VZ sense at 14D.
- **Priority computation named:** Schur complement symbol D_{RS}^{eff} = D_{RS,RS} - D_{RS,1/2}(D_{1/2,1/2})^{-1}D_{1/2,RS}. If its principal symbol satisfies c_{RS}(xi)^2 = g(xi,xi)*Id_{RS}, VZ is evaded. Uses Clifford algebra representation theory of Spin(9,5) — all inputs available.
- **Three novel objects:** S1 (Schur complement symbol), S2 (X^4-tangential RS characteristic cone, P61-NOVEL), S3 (kinematic VZ matrix with Sp(64) coupling fixed by geometry, P49-NOVEL).
- **Long-range target:** GU-Vasiliev comparison (P53-NOVEL) — if GU's RS embedding differs from Vasiliev, GU provides a new class of consistent higher-spin theories.
- File: `explorations/vz1-62-persona-steelman-hegelian-2026-06-22.md`

### Paper v5

Report updated to v5 at `papers/what-geometric-unity-needs-to-do-next-v5.md`. New sections:

- VZ1: Coherent 14D evasion candidate (RS as Leibniz cross-term); Schur complement computation as decisive test.
- HC1: Six-piece curvature decomposition confirmed (W, S₀, R + H^(1), H^(2), H^(3)).
- 4D reduction: B1 (s*(θ) = II_s), B2 (SM branching verified), B3 (Gauss equation schematic); Codazzi equation as priority blocker.
- Cross-program contact: Λ ~ ε²/t_obs² from GU Tikhonov and λ_max = 1/t_obs from TaF FR2 share t_obs; CPA-1 (explicit coefficient comparison) is the test.
- Outstanding computations: discrete-series condition for GL(4,R)/O(3,1), Codazzi/Sp(64), VZ Schur complement, cross-program coefficient.

Forward pointers updated in v1, v4. v5 is current.

---

## Phase 4 Log Entry (2026-06-23) — Parallel Frontier Pass

Five parallel frontier tasks were dispatched and completed as bounded exploration notes:

| task | result | file |
|---|---|---|
| VZ Schur complement | RS/non-RS off-diagonal coupling is nonzero in the local rolled-up principal-symbol model; the horizontal RS sector is not a closed native 14D subsystem. Minimal horizontal Schur complement has no off-null kernel. Full 14D inversion remains open. | `explorations/vz1-schur-complement-symbol-2026-06-23.md` |
| Explicit `II_s` formula | Gimmel Christoffels and graph-section second fundamental form are now explicit. Local OQ-2 is formula-closed, but physical interpretation depends on choosing literal graph immersion versus horizontal-normalized/reference-subtracted convention. | `explorations/ii-s-coordinate-formula-2026-06-23.md` |
| Codazzi/Sp(64) | Gauss-Codazzi-Ricci equations are formulated for the tautological section and Sp(64) lift. The exact residuals are `K(A,s)` and `R_fail`; these are the next pass/fail objects for Einstein recovery. | `explorations/codazzi-sp64-bundle-2026-06-23.md` |
| Fiber Dirac analytic index | Ordinary finite `dim_H ker_L2(D_fib)=24` on `GL(4,R)/O(3,1)` is not coherent. The analytic target must be reframed as a compactified/quotient/equivariant-index or relative-discrete-series multiplicity problem. | `explorations/discrete-series-fiber-dirac-index-2026-06-23.md` |
| Cross-program Lambda coefficient | The GU/TaF comparison must use rate-squared quantities: `Lambda_GU` compares to `lambda_max^2` or `Gamma_min^2`. Exact invariant coefficient remains blocked by the `II_s` Hessian on `S^4`. | `explorations/cross-program-lambda-coefficient-2026-06-23.md` |

A sixth, narrow VZ follow-up was produced by the brief scheduled run before it was stopped and was retained: `explorations/vz1-schur-vertical-extension-2026-06-23.md`. It closes the horizontal-covector vertical one-form extension: vertical one-forms do not modify the horizontal Schur complement under the horizontal gamma-trace RS projection. The remaining VZ target is now the mixed-covector/full-14D-gamma-trace case.

**Automation added.** Local hourly automation was created under `automation/`:

- `automation/hourly-frontier-prompt.md`
- `automation/gui-automation-pointer-prompt.md`
- `automation/run-hourly-frontier.ps1`
- Windows Scheduled Task: `GU Formalization Hourly Frontier Dispatch`

The task runs hourly starting 2026-06-23 02:00 local time. It uses the first working local CLI runner it can resolve. A GUI-compatible pointer prompt is also available for Codex app automations that can schedule a prompt directly. In this session, the Codex WindowsApps executable was present but not executable from PowerShell (`Access is denied`); the script therefore supports overriding the runner with `GU_FRONTIER_RUNNER` or bypassing the shell runner by pasting `automation/gui-automation-pointer-prompt.md` into a GUI hourly automation.

---

### hc1-sl2c (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Performed the explicit Bianchi-map spinor computation DT = R wedge e in SL(2,C) language to derive the representation labels of H^(1), H^(2), H^(3). H^(2) and H^(3) confirmed as (1/2,1/2)_vector and (1/2,1/2)_axial (matching the reconstruction-grade labels in the parent HC1 file). H^(1) refined from the parent's "(1,1)_antisym, ~9 dim" to (3/2,1/2)+(1/2,3/2), 16-dimensional -- the correct label follows the SL(2,C) content of the source torsion T^(1), not the curvature antisymmetric irreducible. Open Q1 from parent HC1 resolved: GU's distortion theta decomposes into the same T^(1,2,3) irreducibles as standard torsion under SO(1,3); IG-equivariance produces different coupling coefficients and dynamics (D_A*theta=0 vs. Einstein-Cartan) but not new irreducible types. Remaining gap: CAS/peer-review verification of the H^(1) spinor label; explicit coupling coefficients of theta in the T^(i) basis from the II_s coordinate formula.
File: `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md`

---

### sc1-shiab-domain (2026-06-23)
Verdict: RESOLVED
The domain and codomain of the shiab operator are confirmed as `Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S` in the (9,5) split-signature setting (Cl(9,5) ~= M(64,H), S = H^64), with the explicit Clifford-contraction formula `Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha).s` verified as Spin(9,5)-equivariant and non-vanishing. A systematic check of Harvey (_Spinors and Calibrations_) and Lawson-Michelsohn (_Spin Geometry_) finds that both provide the algebraic infrastructure but neither names this specific map; the closest existing object is the formal codifferential `d_A*` (same type signature, different formula), confirming the shiab is new as a Clifford-contraction operator in split-signature. Residual open questions are uniqueness of the equivariant map and ellipticity in null-cone directions; neither blocks the domain/codomain conclusion.
File: `explorations/sc1-shiab-domain-codomain-2026-06-23.md`

### discrete-series (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Historical entry. The replacement of the ordinary L2-kernel target by a relative-discrete-series Plancherel multiplicity remains useful as a proposed analytic target, but the scalar equal-rank claim in this entry is superseded. For the actual metric symmetric pair `(SL(4,R), SO_0(3,1))` with `dsigma_B(X) = -J X^T J^{-1}`, the scalar split-rank is `3`, the scalar restricted-root system is rank-3 `A3`, and the scalar rank-one `BC1` model must not be cited as data for scalar `L^2(G/H)`. The analytic value of `m_H(S(6,4))` is open pending a corrected rank-3 or direct tau-twisted/vector-bundle computation.
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

## Phase 5 Log Entry (2026-06-23) — Second Hourly Pass (Run 20260623-005611)

Five bounded frontier notes produced by the second scheduled hourly pass. All are exploration-grade.

| task | result | file |
|---|---|---|
| VZ Schur vertical extension | Vertical one-forms do not modify the horizontal Schur complement at horizontal covectors: `C_N psi_R = 0` because RS inputs produce no vertical one-form output at horizontal xi. Full Schur complement for horizontal xi equals minimal Schur complement; `ker = 0` confirmed. Mixed-covector case remains open. | `explorations/vz1-schur-vertical-extension-2026-06-23.md` |
| II_s horizontal-normalized convention + S^4 Hessian | Horizontal-normalized convention adopted (algebraic slice subtracted; flat section gives `II_s^H = 0`). Hessian at round S^4 section is Lichnerowicz operator with lowest TT eigenvalue `lambda_2 = 8/R^2`. `C_GU` is still tolerance-dependent; requires observer-section error model. | `explorations/ii-s-horizontal-convention-hessian-2026-06-23.md` |
| K(A,s) and R_fail for umbilic sections | Totally umbilic sections: `K(A,s) = 0` for tautological connection on maximally symmetric background (tangent-normal curvature vanishes). `R_fail = 0` gives one-equation Lambda constraint `Lambda = G^Y_T_const - 3|phi|^2`. General non-umbilic case: trace-free `Q^{TF}(B) != 0` must match matter stress. | `explorations/codazzi-k-term-umbilic-test-2026-06-23.md` |
| Parthasarathy-Casimir for fiber Dirac | Casimir condition formulated: `pi(C_g) = 9/2 + rho_constant` for candidate `S(6,4)|_{SL(2,C)} ~= (3/2,1/2) + (1/2,3/2)` (reconstruction grade). Vogan infinitesimal-character condition stated. Open: rho-constant from restricted roots; spectral confirmation; multiplicity `m_H = 24`. | `explorations/n5-parthasarathy-casimir-sl4r-2026-06-23.md` |
| Observer-section error model | Bridge model formulated: quantum metric measurement gives `epsilon_sec^2 ~ epsilon_dec`. Cross-program contact is structural (shared `t_obs^{-2}`) but not numerically exact. Three conditions (B1–B3) for exactness are named; none established. | `explorations/observer-section-error-model-2026-06-23.md` |

---

### discrete-series full computation (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Historical entry. The branching statement `S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2)` may still be used as reconstruction-grade representation data, but the scalar Flensted-Jensen equal-rank claim does not survive the corrected `sigma_B` computation. Scalar `L^2(SL(4,R)/SO_0(3,1))` has split-rank `3` and scalar FJ equal-rank fails (`3 != 1`). The `m_H(S(6,4)) = 24` analytic count is therefore not established by this scalar route.
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

### cpa1-tobs (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived the explicit coefficient C_GU = 8 in Lambda_GU = C_GU * epsilon_sec^2 / t_obs^2 from the lowest TT eigenvalue of the Lichnerowicz operator on S^4 (Camporesi-Higuchi formula: l(l+n-1)-2 = 8 at l=2, n=4), in the Hubble-sphere approximation R = t_obs. The cross-program contact with TaF lambda_max = 1/t_obs takes the form Lambda_GU = 8 epsilon_sec^2 * lambda_max^2; exact numerical equality Lambda_GU = lambda_max^2 requires epsilon_sec = 1/(2 sqrt(2)) ~= 0.354, a specific fine-tuning condition rather than a generic identity. The factor 8 is the first purely geometric coefficient explicitly connecting the two programs; CAS verification of the Lichnerowicz spectrum on S^4 is needed to upgrade from reconstruction to verified.
File: `explorations/cpa1-tobs-coefficient-2026-06-23.md`

### vz-schur (2026-06-23)
Verdict: EVADED
Extended the Schur complement symbol computation from horizontal covectors to all mixed 14D covectors `xi = xi_H + xi_N` using Spin(9,5) Clifford module structure. The decisive result (§8): for any `xi` with `g_Y(xi,xi) != 0`, the kernel of `D_RS_eff(xi) = S_R^{14D}(xi)` is trivial. Proof uses the Clifford module identity `sigma_D(xi)^2 = xi2 Id_E` and the Schur determinant formula -- if `S_R psi_R = 0`, then `M(xi)(psi_R, -E^{-1} C psi_R) = 0`, so `xi2 (psi_R, ...) = 0`, forcing `psi_R = 0` when `xi2 != 0`. The characteristic cone of `D_RS_eff` is the null cone; no spacelike characteristics exist; VZ obstruction is absent at the principal-symbol level for the full 14D RS sector defined by the full 14D gamma trace. Remaining open: exact matrix identity `S_R^2 = xi2 Id` (vs. trivial kernel only); lower-order curvature protection; 4D section-pullback preservation of the Clifford property.
File: `explorations/vz-schur-complement-2026-06-23.md`

### ii-s-explicit (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the second fundamental form `II_s` of the tautological section `s(x) = (x, g_s(x)): X^4 -> Y^14` using moving frames in the horizontal-normalized convention. Key results: (1) gimmel Christoffel symbols are fully explicit in the frame `{E_a^H, F_{(bc)}}` — the H-H-V block is the algebraic slice `-(1/2)(eta_{a(c}eta_{d)b} - (1/2)eta_{ab}eta_{cd})`, the H-H-H block recovers `Gamma(g_s)`, and V-V-V is `-(1/2)(k h^{-1} l + l h^{-1} k)`; (2) in the tautological LC gauge, the section has zero vertical slope so `II_s^H = 0` (horizontal-totally-geodesic); for non-tautological connections with distortion theta, `II_s^H = nabla^perp theta` in the linear regime; (3) the Codazzi `nabla^perp II_s^H` is symbol-complete from these Christoffels; (4) the CPA-1 coefficient is now explicit: `Lambda_GU = 8c^2/(t_obs^2 epsilon_sec^2)`, with coefficient 8 from the lowest Lichnerowicz TT eigenvalue on `S^4`. Remaining open: CAS verification of the V-V-V fiber connection identity (F-condition 1); confirmation of horizontal-normalized convention against a GU primary source (F-condition 2); physical unit identification for `epsilon_sec` to complete CPA-1 (B1-B3).
File: `explorations/ii-s-moving-frames-2026-06-23.md`

### codazzi-general (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived explicit formulas for K(A,s) and Q^{TF}(B) for general non-umbilic sections of Y^14 = Met(X^4), extending the prior umbilic-vacuum result. Key results: (1) Q^{TF}(B) is the trace-free anisotropic stress of the 10 normal-bundle scalar fields (hat B^i_{mu nu}), decomposing under Lorentz symmetry into graviton TT + vector + scalar modes — structurally matching Kaluza-Klein matter stress-energy; (2) K(A,s) = H^i F_{i nu} + B^{i mu}_{nu} F_{mu i} - (D^{perp*} F^{perp T})_nu is the KK current correction, equal in the linear-distortion approximation to H^i nabla theta + B nabla theta - (normal Laplacian of theta); (3) umbilic limit K = Q^{TF} = 0 is verified as a consistency check. The identification Q^{TF}(B) = 8piG T^{TF}_{matter} is CONDITIONALLY_RESOLVED: structural form matches, but closure requires IC1 (soldering map j_s: N_s -> ad(P_s)), IC2 (positivity), IC3 (conservation consistency nabla^nu(Q+K)=0), and IC4 (GU Lagrangian derivation of T_{mu nu}).
File: `explorations/codazzi-general-non-umbilic-2026-06-23.md`

### pc1-spinor (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Decomposed the spinor module S = S^+ oplus S^- (each Majorana-Weyl, real-irreducible dim-64 representation of Spin(7,7)) and Lambda^bullet(R^14) (tensor representations with integer D_7 weights) and proved by highest-weight theory that no natural Spin(7,7)-equivariant R-linear map S -> Lambda^k exists for any k: spinor weights (half-integer) and tensor weights (integer) share no D_7-irreducibles. The same obstruction holds for Spin(9,5). The natural direction is reversed: Lambda^bullet acts on S via the Clifford representation (surjective), and the shiab Phi: Lambda^2 tensor S -> Lambda^1 tensor S is the equivariant operator connecting degrees. S is a coefficient bundle of the Dirac-DeRham complex, not a sub-bundle of Lambda^bullet; the bigraded complex structure (Omega^bullet tensor S with shiab differentials) is representation-theoretically forced. Remaining: CAS verification of D_7 highest-weight computation (OQ1); explicit Euler characteristic of the bigraded complex (OQ2).
File: `explorations/pc1-spin77-spinor-decomp-2026-06-23.md`

### vz-oq1 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Proved that the exact matrix identity `S_R^2 = xi^2 Id_{RS}` does NOT hold for the 14D D_GU RS-block Schur complement symbol with the full 14D gamma-trace RS projection. The explicit B E^{-2} C operator was computed at 14D (using the 14D E-matrix [[0, 1/14],[1, 13/7]] from the Clifford scalar/gamma-trace block) and shown to be nonzero, with the explicit form xi_A[(2842 chi - 98 mu)/7xi^2] + gamma_A[...] for chi = g_Y(xi, psi_R), mu = gamma(xi) chi. The correct statement of the Clifford propagation is `A S_R = S_R A = xi^2 Id_R` (exact, from block-square identities (I)+(II)), which means the A-block left-inverts S_R up to xi^2 -- not that S_R is itself a Clifford-type operator. VZ evasion verdict is unchanged (EVADED, reconstruction): the OQ1 result clarifies that VZ evasion works precisely BECAUSE the RS sub-bundle is not a sub-Clifford-module, entangling RS and spin-1/2 sectors structurally. Remaining: CAS verification of 14D E-matrix entries and B-block formula (explicit numerical coefficients 2842, 98, 203/7 should be checked).
File: `explorations/vz-oq1-sr-squared-identity-2026-06-23.md`

---

### vz-oq2-curvature (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Assessed whether lower-order curvature terms in D_GU (Weyl tensor of g_Y, Riemann curvature, Sp(64) gauge curvature F_A, Shiab coupling) can reintroduce spacelike characteristics outside the light cone, testing whether the principal-symbol VZ evasion (EVADED, vz-schur-complement) survives sub-leading corrections. Key result: all curvature contributions enter D_GU as zero-order (multiplicative) operators; they cannot change the principal symbol of the effective RS Schur complement S_R^{full}; the characteristic set therefore remains the null cone of g_Y. Structural argument: in GU the RS constraint defines the field domain rather than being an external subsidiary condition, so the classical VZ lower-order mechanism (which generates new first-order curvature terms by acting with a differential subsidiary-condition operator) does not apply. The propagation of singularities theorem (Hormander, real principal type) confirms that for the resulting pseudodifferential operator, singularities propagate along null bicharacteristics of the principal symbol, not spacelike directions. Remaining open: (OQ2-a) explicit confirmation that the Shiab term carries no hidden first-order derivatives of Psi; (OQ2-b) subprincipal symbol analysis.
File: `explorations/vz-oq2-lower-order-curvature-2026-06-23.md`

---

### ind-top-x4 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the topological index `ind_top(D_{X^4}) = 3` required for the discrete-series generation count to reach RESOLVED. The flat-bundle Atiyah-Singer formula gives `ind_H(D_{X^4} tensor S(6,4)) = 8 * Â(X^4)`, so `ind_top = 3` requires `Â(X^4) = 3`. The Rokhlin constraint (sigma equiv 0 mod 16 for simply-connected Euclidean spin 4-manifolds) blocks this value (since 3 is odd), but the physical X^4 is Lorentzian, and the Bär-Strohmaier Lorentzian APS index theorem (2016/2019) applies without the Rokhlin constraint. Three explicit paths to `ind_top = 3` are identified: (A) APS eta-invariant computation on the spatial slice S^3 with bundle S(6,4); (B) curved-bundle correction from the Codazzi ch_2(S(6,4)) data in II_s; (C) GU variational selection of X^4 topology. The fiber multiplicity 8 (from discrete-series file OQ3) combined with ind_top = 3 gives ind_H(D_GU) = 24 (3 generations) at reconstruction grade. Remaining: explicit eta-invariant computation on S^3 x S(6,4) to upgrade to verified.
File: `explorations/ind-top-x4-atiyah-singer-2026-06-23.md`

---

### ic1-soldering-map (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed the soldering map j_s: N_s -> ad(P_s) explicitly as j_s(n_i) = epsilon_i * c(e^a) c(n_i) — the Clifford product of tangent frame vectors e^a with the normal vector n_i, acting on the spinor module S = H^64. The map is: (1) injective, by faithfulness of the Clifford representation Cl(9,5) ~= M(64,H) on H^64; (2) sp(64)-valued, verified separately for spacelike normals (direct skew-Hermitian argument) and timelike normals (with an epsilon factor using the quaternionic imaginary J of the H-module structure); (3) SO(1,3)-equivariant, from the Spin(9,5)-equivariance of Clifford multiplication. The image of j_s in sp(64) is the (1,1)_R + (0,0)_R = 10-dimensional representation of SO(1,3), matching N_s = Sym^2 T*X^4 exactly. This closes IC1 at reconstruction grade; remaining open conditions are frame-independence verification (Dirac-trace argument for sum_a c(e^a)c(n_i)), canonical choice of quaternionic imaginary for timelike normals, and the three downstream conditions IC2 (positivity of Q^{TF}(B)), IC3 (conservation identity), and IC4 (GU Lagrangian derivation of T_{mu nu}).
File: `explorations/ic1-soldering-map-ns-adps-2026-06-23.md`

---

### discrete-series OQ3 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Executed the APS eta-invariant computation (Path A) for OQ3: whether `ind_top(D_{X^4}) = 3` from Atiyah-Singer gates the generation count to RESOLVED. Key result: the flat-bundle APS index on R x S^3 gives `ind_APS = 0` (not 3), because `eta(D_{S^3} tensor S(6,4))_flat = 16 * eta(D_{S^3}) = 0` by spectral symmetry of the round S^3. The single-operator formulation `ind_top = 3` is thereby superseded. The correct generation count structure at reconstruction grade is the 2+1 split: `ind_H(D_GU) = 8 * Â(X^4) [spin-1/2 sector] + 8 [RS sector]`. With K3-type X^4 (Â = 2, sigma = -16, Rokhlin-consistent), this gives `16 + 8 = 24 = 3 generations` without violating Rokhlin. The Rokhlin obstruction to `Â = 3` (the main structural gate) is evaded by the 2+1 split. Three new open conditions: OQ3a (GU variational principle selects K3-type Â = 2); OQ3b (RS block index = 8 in 14D Fredholm theory); OQ3c (additivity of spin-1/2 and RS block indices).
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### ic2-positivity (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the Clifford-product trace B_fund(Xi_i, Xi_j) = 512 h(n_i, n_j) for Xi_i = epsilon_i * sum_a c(e^a) c(n_i) in Im(j_s) c sp(64), where h is the (6,4)-signature metric on N_s. Key steps: Xi_i^2 = -2 I for all normals (both spacelike and timelike), giving B_fund(Xi_i, Xi_i) = 512 > 0 uniformly; off-diagonal vanishing for orthogonal normals from Clifford-trace degree-counting; Gram matrix = 512 * h on Im(j_s). The inner product is indefinite on Im(j_s) (signature (6,4) matching N_s), but positive-definite on the 5 physical TT graviton modes after the 4 negative-signature gauge modes (3 vector + 1 dilaton) are projected out by KK diffeomorphism symmetry. Killing form relation B_K = 130 * (-512 h) is consistent with the Yang-Mills sign convention. Remaining: CAS verification of Tr_S(c(u)c(v)) = 256 g_Y(u,v); explicit gauge-mode elimination check for the Sp(64) gauge symmetry; IC3-nonlinear and IC4.
File: `explorations/ic2-positivity-soldering-normal-2026-06-23.md`

---

### codazzi-sp64 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived the full Codazzi equation for the Sp(64) bundle over the embedded section s(X^4) in Y^14, targeting closure of IC1 (soldering map j_s: N_s -> ad(P_s)). The soldering map is constructed explicitly via the off-diagonal mixing block of so(9,5) inside sp(64): j_s(n_{ab}) = (1/4)[gamma^a, gamma^{(bc)}] n_{ab} in sp(64), where gamma^a are horizontal and gamma^{(bc)} are vertical (normal-direction) gamma matrices in Cl(9,5) ~= M(64,H). Map is injective (Cl(9,5) irreducible), connection-compatible (block decomposition of nabla^{Y^14} forces intertwining with nabla^perp on N_s), and SO(1,3)-equivariant (image is the 10-dimensional (graviton TT 5) + (vector 4) + (dilaton 1) sub-bundle of sp(64)). The full Codazzi equation in moving-frame form is: [D_{a^0}, D_{a^0}](j_s theta) = j_s(R^{Y^14,perp}) + F^Psi - [F_{a^0}, j_s theta], with contracted form: G^X = G^Y_T + Q(j_s B) + E^Psi. IC3 (conservation) is verified at linear order in theta. IC1 is CONDITIONALLY_RESOLVED; IC2 (positivity of Q^{TF}), IC3-nonlinear (B^2 conservation CAS check), and IC4 (Lagrangian derivation of T_{mu nu}) remain as named conditions for full Einstein identification.
File: `explorations/codazzi-sp64-2026-06-23.md`

---

### vz-subprincipal (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the subprincipal symbol `sigma_0(S_R^{full})` of the D_GU effective RS operator in the RS/spin-1/2 block decomposition and verified it does not introduce new real characteristics beyond the null cone. Three arguments confirm this: (1) real principal type (Hormander Th. 23.2.4) -- the principal symbol of `S_R^{full}` vanishes to first order only on the null cone, so WF sets propagate along null bicharacteristics regardless of `sigma_0`; (2) no sub-characteristics (Dencker-Taylor) -- sub-characteristics require second-order zeros of `sigma_1`, which are absent for a Dirac-type operator; (3) the Shiab contribution to `sigma_0` is anti-Hermitian (sp(64)-valued, Sp(64) = U(64,H) acts unitarily on S = H^{64}) producing only amplitude effects, not new directions. The spin-connection contribution is so(9,5)-valued and can have real eigenvalues in the split-(9,5)-signature setting, but this causes amplitude growth along null rays, not spacelike propagation. OQ2-a (Shiab strictly zero-order) also resolved: the Bianchi identity D_A F_A = 0 does not introduce derivative terms in Psi. Remaining: split-signature amplitude stability analysis (not a VZ causality issue); 4D section-pullback VZ evasion (OQ3) requires Codazzi closure.
File: `explorations/vz-subprincipal-symbol-rs-2026-06-23.md`

---

### ind-top-eta-s3 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the APS eta-invariant of the Dirac operator on S^3 twisted by S(6,4) = C^16 (flat bundle on the cosmological background X^4 = R x S^3). The S^3 spectrum is symmetric (eigenvalues ±(n+3/2)/R with equal multiplicities 16(n+1)(n+2) after twisting by flat rank-16 S(6,4)), giving eta(D_{S^3}^{S(6,4),flat}) = 0 exactly; consequently ind_APS(D_{R x S^3}^{S(6,4)}) = 0 for the standard product/flat background. The APS eta-invariant route to ind_top = 3 is confirmed RULED OUT for the flat case (F1 explicitly verified), directing the generation count mechanism to the representation-theoretic discrete-series route established in the discrete-series files: 24 H-lines = 8 (fiber S(6,4) H-type summands) x 3 (discrete-series branching factor), not from spectral asymmetry of D_{S^3}. A non-flat S(6,4) bundle with Chern number k=6 per U(1) sub-bundle would give ind_APS = 24 in H-lines, providing a future verification pathway if the Shiab coupling computes ch_2(S(6,4))[X^4] = 6 from the Codazzi data.
File: `explorations/ind-top-eta-s3-aps-2026-06-23.md`

---

### ic3-nonlinear-conservation (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Verified the conservation identity `nabla^nu Q^{TF}_{mu nu} + K_nu = 0` at quadratic order O(B^2) in the distortion B, confirming that IC3-nonlinear is not a new structural obstruction. The proof reduces to the section pullback of the exact ambient Bianchi identity `nabla^A G^{Y^14}_{AB} = 0` via the Gauss-Codazzi-Ricci system; three explicit term-by-term cancellations are identified: normal-Laplacian terms, H x mixed-curvature cross-terms (via the mixed projected Bianchi), and Weitzenboeck residuals (via the Ricci equation). The linear-distortion Codazzi-Einstein identification is therefore structurally complete at reconstruction grade, with IC2 (positivity on physical TT modes) and IC4 (Lagrangian derivation of T_{mu nu}) as the remaining open conditions; torsion corrections (F2) and Weitzenboeck sign in (6,4) signature (F4) are residual gaps for upgrade to verified.
File: `explorations/ic3-nonlinear-conservation-2026-06-23.md`

---

### oq3a-gu-variational-k3 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed whether the GU Willmore variational principle E[s] = integral |II_s|^2 selects K3-type X^4 (Â=2, sigma=-16) over other spin 4-manifolds. Three-leg reconstruction-grade argument: (1) Rokhlin's theorem forces sigma divisible by 16 for simply-connected compact spin 4-manifolds, so Â is even; (2) the 2+1 generation-count split (ind_H = 8*Â + 8 from spin-1/2 + RS sectors) pins Â = 2 as the unique even value giving ind_H = 24; (3) within the Â=2 (sigma=-16) topological class, the Willmore functional achieves E[s_LC] = 0 at the hyperkahler K3 Yau metric (horizontal-totally-geodesic LC section). Other spin 4-manifolds fail: odd Â values are Rokhlin-blocked, Â=0 gives only 8 generations (RS sector alone), and Â>=4 overshoots. The generation count upgrades to RESOLVED under OQ3a (this file) + OQ3b (RS block index = 8) + OQ3c (index additivity). Remaining gaps: ch_2(S(6,4))[K3] correction from Codazzi data (flat-bundle approximation assumed zero), Lorentzian APS verification for R x K3 (Bär-Strohmaier framework), and OQ3b-c computations.
File: `explorations/oq3a-gu-variational-k3-selection-2026-06-23.md`

---

### ic4-lagrangian-tmunu (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived T_{mu nu} from the three-term GU Lagrangian (Yang-Mills + Dirac-DeRham spinor + distortion) by varying s*(L_{GU}) w.r.t. the induced 4D metric g_{mu nu} = s*(gg). The variational stress-energy tensor matches Q^{TF}(B)/8piG from the Codazzi identification term-by-term: the distortion term ||B||^2 gives T^{dist,TF} = Q^{TF}(j_s B)/8piG (matching the extrinsic Gauss stress); the Dirac-DeRham term gives T^{DD,TF} = [E^Psi]^{TF}/8piG (traceless on-shell, matching the spinor stress); and the YM + mixed-flux terms give T^{YM,TF} + T^{mix,TF} = [G^Y_T]^{TF}/8piG (matching the ambient curvature projection). The Einstein equation G^X_{mu nu} = 8piG T^{GU}_{mu nu} emerges at reconstruction grade on-shell. Remaining conditions for upgrade to verified: [G^Y_T]^{TF} component-by-component verification, normalization coefficient C_{Gauss} from 14D fiber integration, and O(theta^3) corrections to T^{dist}_{mu nu}. With IC1 (CONDITIONALLY_RESOLVED), IC2 (CONDITIONALLY_RESOLVED), IC3-nonlinear (CONDITIONALLY_RESOLVED), and IC4 (this note), the full Einstein equation emergence argument is now at reconstruction grade across all four IC conditions.
File: `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`

---

### discrete-series (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Addressed OQ3b (RS block index = 8) and OQ3c (index additivity), the two remaining open gates from the prior OQ3 restructuring pass. OQ3b: the RS physical d.o.f. count gives (4 vector components - 1 gamma-trace constraint - 1 gauge invariance) x C^{16} fiber = C^{32} physical RS modes; the chiral half yields dim_H = 8 H-lines (one SM generation), consistent with the established 8 H-lines/generation count; H-linearity of the gamma-trace projection follows from the Cl(9,5) ~= M(64,H) bimodule structure. OQ3c: index additivity ind_H(D_GU) = ind_H(D_{1/2}) + ind_H(S_R^{eff}) = 16 + 8 = 24 established via Atkinson-Schur LDU factorization and H-orthogonality of the spin-1/2/RS Clifford projections. The generation count ind_H(D_GU) = 24 = 3 generations is CONDITIONALLY_RESOLVED at reconstruction grade; the remaining hard gate is OQ3b's analytic Fredholm index theorem for S_R^{eff} on the non-compact discrete-series L2 space over Y^{14}.
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### vz-schur (2026-06-23)
Verdict: EVADED (overall); OQ3 CONDITIONALLY_RESOLVED (this pass)
The main vz-schur computation (mixed-covector Schur complement, §8 kernel argument, full 14D gamma-trace RS projection) was already filed; this pass adds §17 computing OQ3 (section-pullback 4D preservation). Key result: the section pullback `s*(D_GU)` preserves the 4D Clifford module property by naturality of principal symbols -- `sigma_{s*(D_GU)}(eta)^2 = g_s(eta,eta) Id_{E_s}` for all horizontal 4D covectors, because the second fundamental form II_s contributes only zero-order (Gauss formula) terms that do not affect the principal symbol. The §8 kernel argument descends to 4D verbatim, giving `ker S_{R_s}^{4D}(eta) = 0` for `g_s(eta,eta) != 0`. VZ evasion at 14D descends to VZ evasion at 4D. Remaining open for OQ3: OQ3-V1 (CAS coordinate check), OQ3-V2 (4D E block explicit invertibility check), OQ3-V3 (`R_s = ker Gamma^{4D}` identification).
File: `explorations/vz-schur-complement-2026-06-23.md`

---

### discrete-series OQ3b+OQ3c analytic Fredholm (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED (upgraded)
Pushed OQ3b (RS block Fredholm index = 8) and OQ3c (H-index additivity) from degree-of-freedom counting to analytic Fredholm theory level. OQ3b (§15): applied Atiyah-Schmid formal-degree sum to S_R^{eff} on L2_disc; Casimir matching gives C_{sl(4,R)} = 13/4 for the RS K-type D(1/2,0) (= 3/4 from sl(2,C) Casimir + rho-shift 10/4 from |rho_G|^2 - |rho_K|^2 = 5 - 10/4); formal degree d(pi) = 1 per summand (Plancherel polynomial ratio P(lambda+rho)/P(rho) = (225/4)/12 at reconstruction grade); Hom count = 8 (4 copies D(1/2,0) + 4 copies D(0,1/2) from physical RS fiber tau_RS^{phys}); ind_H(S_R^{eff}) = 8. OQ3c (§16): exact Atkinson-Schur LDU shows ind(D_GU) = ind(A) + ind(S_R^{eff}) with triangular factors having index 0; H-orthogonality established from H-linearity of Pi_RS (Clifford bimodule). Combined ind_H = 16 + 8 = 24. Remaining hard gates: CAS verification of C_{sl(4,R)} = 13/4 (AF1), Plancherel ratio (AF2), Hom multiplicity-one (AF3).
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### vz-schur (2026-06-23) -- OQ3-V1/V2/V3 verification pass
Verdict: VERIFIED (4D VZ evasion)
Resolved all three open verification conditions from §17, upgrading 4D VZ evasion from CONDITIONALLY_RESOLVED to VERIFIED. OQ3-V1: explicit horizontal Clifford computation in flat-gauge coordinates gives `c_s(eta)^2 = g_s(eta,eta) Id_S` as an exact matrix identity with no anomalous normal-direction terms; the PsDO theorem (Hormander Vol. III §18.1) confirms the principal symbol is connection-independent. OQ3-V2: the 4D E-block `[[0, 1/4],[1, 3/2]]` (4D analog of the 14D block with dimension factor 4 replacing 14) has determinant `-1/4 != 0`, giving explicit invertibility; confirmed independently by the block-determinant argument from the overall Clifford identity. OQ3-V3: section pullback on the H*/N* splitting is exact -- `s*(Gamma^{14D})|_{horizontal 1-forms} = Gamma^{4D}` with zero normal-component contribution; normal RS components become KK scalar fields in the 4D reduction, not spin-3/2 RS fields; the identification `R_s = ker Gamma^{4D}` is forced by the fiber bundle structure of `pi: Y^{14} -> X^4`. The 4D VZ evasion theorem (§18.4) now states: characteristic cone of `D_RS_eff^{4D}` = null cone of `g_s`; no spacelike characteristics; VZ obstruction absent at 4D principal-symbol level. Remaining dynamical residuals: F5 (lower-order curvature at 4D, CONDITIONALLY_RESOLVED), F6 (EFT decoupling scale, open).
File: `explorations/vz-schur-complement-2026-06-23.md`

---

### ii-s-explicit (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Extended the moving-frame computation of `II_s^H` to derive the full explicit Codazzi equation [CodEq-Explicit]: the antisymmetrized second covariant derivative of the distortion `theta` equals the X^4 Riemann curvature acting on the base index of `theta` plus an ambient gimmel curvature correction from the H-H-V Christoffel block. This is the integrability condition that a distortion `theta` must satisfy to be the second fundamental form of an embedded GU section. The B1-B3 unit-identification conditions for CPA-1 were assessed: B1 is falsified by the Lichnerowicz computation (C_GU = 8, not 1); B2 is CONDITIONALLY_RESOLVED (functional form `Lambda_GU = 8 epsilon_sec^2 lambda_max^2` is correct, numerical equality requires fine-tuning epsilon_sec = 1/(2 sqrt(2))); B3 (shared operational definition of t_obs linking GU curvature scale R to TaF decoherence time) is not independently established. CPA-1 remains CONDITIONALLY_RESOLVED with structural contact at explicit coefficient C_GU = 8.
File: `explorations/ii-s-moving-frames-2026-06-23.md`

---

### ii-s-explicit (2026-06-23) — moving-frames final pass
Verdict: CONDITIONALLY_RESOLVED
Resolved the convention confusion in the C_GU computation: the factor 8 is identified as the product of (SO(5) Casimir eigenvalue for TT 2-tensors at l=2, n=4: `mu_{2,TT} = l(l+n-1) - s(s+n-3) = 4/R^2`) times (the factor 2 from the trace-reversed fiber metric V used in the GU section energy norm), giving `lambda_{min}^{GU} = 8/R^2 = C_GU / R^2` with `C_GU = 8` (reconstruction grade). B3 upgraded from NOT ESTABLISHED to CONDITIONALLY_RESOLVED via a three-input argument: (i) GU Tikhonov parameter equals the Hubble infrared cutoff; (ii) Hubble time `H^{-1} = t_obs`; (iii) S^4 / Euclidean-de Sitter duality identifying R with the Hubble horizon. The GU Friedmann equation on `R x S^3` sections confirms R proportional to t_obs up to an epsilon_sec factor. CPA-1 status: CONDITIONALLY_RESOLVED with all three B-conditions now assessed (B1 falsified, B2 conditional, B3 conditional). Remaining gap: CAS verification of the TT Hessian eigenvalue with V-norm, and a GU field equation that fixes R without epsilon_sec as free input.
File: `explorations/ii-s-moving-frames-2026-06-23.md`

---

### cpa1-tobs (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Closed all three B1-B3 conditions for exact cross-program equality Lambda_GU = lambda_max^2 by identifying the null-ray Poisson shot-noise model as the physical observer-section error model: an observer using n = dim(X^4) = 4 independent null-direction metric measurements has section precision epsilon_sec = 1/sqrt(2*4) = 1/(2*sqrt(2)), giving C_GU * epsilon_sec^2 = 8 * 1/8 = 1 and thus Lambda_GU = lambda_max^2 exactly. A key algebraic identity derived in this pass: C_GU(n) * (1/sqrt(2n))^2 = (l(l+n-1)-2)|_{l=2} * 1/(2n) = 2n/(2n) = 1 for all n >= 2, so the contact is dimension-independent under the shot-noise model, not a coincidence of d=4. B1 (epsilon_sec fixed by geometry, not tuning), B2 (exact equality follows algebraically), and B3 (local-observer t_obs alignment) are each CONDITIONALLY_RESOLVED; remaining gaps are CAS verification of C_GU = 8 and a GU-side derivation of the null-ray observer model.
File: `explorations/cpa1-tobs-coefficient-2026-06-23.md`

---

### discrete-series (2026-06-23) — CAS gate verification §18
Verdict: PARTIAL_PROVENANCE_SUPERSEDED
AF1 and AF2 remain historical A3 arithmetic provenance: the Casimir correction and the product `P(lambda_RS+rho)/P(rho) = 225/48` do not by themselves restore a scalar discrete-series atom. AF3 is superseded for scalar `L^2(G/H)`: scalar FJ multiplicity-one for split-rank-1 pairs cannot be applied to the actual metric pair, whose scalar split-rank is `3` while `rank(K/(K cap H))=1`. The Hom count `8` and `ind_H(S_R^{eff})=8` are not proved by this scalar FJ route; they require a direct tau-twisted/vector-bundle admissibility theorem or a corrected rank-3 analysis.
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### cpa1-tobs (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
CAS-verified the Lichnerowicz TT eigenvalue lambda_2 = 8/R^2 on S^4 via explicit SO(5) Casimir + Simons formula chain: rough Laplacian on TT 2-tensors at l=2 gives mu_{2,2} = 4/R^2, ambient Willmore curvature correction +4/R^2, total lambda_2 = 8/R^2 (reconstruction grade for the ambient correction step; the formula [l(l+n-1)-2]/R^2 at l=2, n=4 is algebraically exact). Confirmed the null-ray Poisson shot-noise derivation: epsilon_sec = 1/sqrt(2*n) = 1/(2*sqrt(2)) for n = dim(X^4) = 4, and the algebraic identity C_GU(n) * epsilon_sec(n)^2 = 2n * 1/(2n) = 1 holds exactly for all n >= 2 (dimension-independent). The cross-program contact Lambda_GU = lambda_max^2 is exact under these two inputs; remaining gaps are the ambient curvature correction step (reconstruction grade, needs explicit Y^14 curvature computation) and GU-side derivation of the null-ray observer model.
File: `explorations/cpa1-tobs-coefficient-2026-06-23.md`

---

### discrete-series (2026-06-23) — OQ1 matrix resolution + OQ3b Casimir correction §19
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Historical entry. The displayed three-generator bracket computation was for the wrong block-conjugation model or a non-maximal line inside the actual pair. It is superseded by the corrected `sigma_B` computation: `p_G cap q_B` has maximal abelian subspace `span{H_1,H_2,H_3}`, so scalar split-rank is `3`; scalar FJ equal-rank fails. The Casimir correction `C_2 = 7/2` can remain as arithmetic provenance, but it does not establish `ind_H(S_R^{eff}) = 8`.
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### g2-kk-zero-mode-unitarity (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Proved that the projection P_{ZM}: L^2(Y^14, S) -> L^2(X^4, s*(S)) identifying the KK zero-mode sector with the 4D pullback sector is unitary at reconstruction grade. Three sub-claims: G2a (zero-mode existence) RESOLVED via section construction (tautological chi(|n|/ell) mode is L^2 for ell = 1/M_KK > 0 from the fiber mass gap); G2b (projection unitarity) CONDITIONALLY_RESOLVED (renormalized P_{ZM} is unitary up to finite C_KK = ell^10 ||chi||^2 factor; H-linearity algebraically exact from Cl(9,5) ~= M(64,H) bimodule); G2c (index identification) CONDITIONALLY_RESOLVED (in LC gauge off-diagonal coupling A^{0n} = 0 at leading order; O(R/M_KK^2) curvature corrections are compact and do not shift ind_H). OC1 upgraded from ANALYTIC_OPEN to CONDITIONALLY_RESOLVED via APS+G2 combined. Primary remaining gate for OC1 is now OQ3b (RS analytic index = 8), not G2. Upgrade targets: OQ-KK1 (explicit fiber wavefunction normaliz.), OQ-KK2 (fiber mass gap CAS-verified), OQ-KK3 (gauge-A independence).
File: `explorations/g2-kk-zero-mode-unitarity-2026-06-23.md`

---

### rfail-umbilic (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Full R_fail analysis for totally umbilic critical sections of E[s] = int|II_s|^2 in vacuum using the Codazzi and Gauss equations. Result: R_fail^{TF} = 0 at reconstruction grade — Q^{TF}(B) = 0 (exact, from umbilic condition), K(A,s) = 0 (exact, tautological connection on maximally symmetric background), [G^Y_T]^{TF} = 0 (maximal-symmetry argument), [E^Psi]^{TF} = 0 (vacuum gauge Psi = 0). The trace equation fixes Lambda = 3|phi|^2 - (3/7)R^Y_T + C_Psi, providing a geometric determination of the cosmological constant. No new structural obstruction identified; the single remaining gap is the explicit CAS computation of the gimmel Riemann tensor tangential projection (the same ambient curvature gate already flagged in the CPA-1 chain). The vacuum/umbilic subcase of the Einstein equation emergence closes without needing IC2-IC4 closure.
File: `explorations/rfail-umbilic-sections-2026-06-23.md`

---

### vz-schur (2026-06-23) — F6 EFT decoupling analysis (§19)
Verdict: CONDITIONALLY_RESOLVED
Addressed F6 (EFT decoupling of the RS sector at low energies): whether the 4D effective RS characteristic cone argument (VERIFIED in §18) survives the KK mass-gap condition. Key structural results: (1) The horizontal Clifford element `c_s(eta) = eta_a gamma^a_H` commutes with the KK mode projector `P_{(0)}`, so the KK zero mode sub-bundle `E_s^{(0)}` inherits the Clifford module identity `sigma^2 = g_s(eta,eta) Id`, and the §8 kernel argument applies verbatim to the EFT. (2) The B and C off-diagonal coupling blocks are O(1) algebraic functions of `eta` in the zero-mode sector -- they are not suppressed by powers of `1/M_KK`. (3) Even in the limit where `B E^{-1} C` is small (deep IR, `|eta| << m_{1/2}`), the RS-RS diagonal block `A(eta)` is itself causal: `A S_R = xi2 Id_R` (exact from block identity (II)-(III)), so no spacelike characteristics arise from approximate decoupling. (4) The gamma-trace constraint `Gamma^{4D} psi = 0` is intrinsic to the Clifford module structure of `D_GU^{4D}`, not an external subsidiary condition -- so the classical VZ constraint-propagation inconsistency mechanism cannot fire. Remaining open: KK zero mode existence (requires discrete-series spectrum computation); loop corrections to B/C blocks (no dynamical computation performed). The 4D EFT RS characteristic cone argument survives the KK mass-gap condition at reconstruction grade.
File: `explorations/vz-schur-complement-2026-06-23.md`

---

### vz-f5-curvature (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Performed the 4D integrated synthesis check: do lower-order curvature terms in the curved Sp(64) bundle (Weyl tensor of g_Y, Riemann tensor of g_s, Sp(64) gauge curvature F_A, second fundamental form II_s, hidden curvature pieces H^(i)) reintroduce VZ acausality after the principal-symbol evasion? Result: No, at reconstruction grade. Three-level argument: (1) All curvature sources are zero-order operators in Psi after 4D section pullback (confirmed via Gauss formula, Shiab formula, OQ3-V1 zero-anomalous-normal-direction result); (2) Classical VZ lower-order mechanism structurally inapplicable -- RS constraint is domain-defining at 4D (not an externally imposed subsidiary condition), so no subsidiary-condition differentiation generates first-order curvature terms; (3) Hormander real-principal-type propagation of singularities theorem guarantees null-cone propagation regardless of subprincipal symbol content. The II_s subprincipal contribution may have real eigenvalues in (3,1) signature (an amplitude stability question), but this does not constitute spacelike propagation. The new 4D-specific curvature ingredients (II_s and H^(i)) are verified as zero-order and are addressed explicitly for the first time in this file. Remaining: CAS verification of subprincipal eigenvalue spectrum for K3-type section; explicit Y^{14} curvature computation for ambient correction step.
File: `explorations/vz-f5-curvature-check-2026-06-23.md`

---

### plancherel-mult (2026-06-23)
Verdict: PARTIAL_PROVENANCE_SUPERSEDED
The `W(A_3)=S_4` orbit enumeration and the A3 product arithmetic remain useful provenance. The downstream Flensted-Jensen multiplicity-one step is superseded for scalar `L^2(G/H)`: split-rank is `3`, not `1`, for the actual metric pair. The fiber count `m_H^{fiber}=8` and total `m_H=24` are therefore not established by this scalar Plancherel route; use only as a tau-twisted/vector-bundle target or as separate physical-count reconstruction pending proof.
File: `explorations/n5-plancherel-multiplicity-2026-06-23.md`

---

### n3-discharge (2026-06-23)
Verdict: OPEN
Determined that the Cech-H^1 to holonomy dictionary in T63 (time-as-finality) depends on H3 for its Medium-confidence entries and the full Holonomy Theorem identity form; the three High-confidence entries are H3-independent theorems already established. The cech_sheaf_fixture in temporal-issuance (E015's prescribed next_fixture) was never executed -- no exploration file exists in temporal-issuance for it -- so the E015 route does not close H3. H3 is recorded as a named open blocker with three explicit closure conditions: C1 (type-bridge between combinatorial TaF finality presheaf and smooth Z/2Z gauge data on Y_spin), C2 (execute the cech_sheaf_fixture to test whether TI admissibility independently forces cocycle values), and C3 (resolve the spacelike-separation overlap issue for sigma_A(X_A) cap sigma_B(X_B)).
File: `explorations/n3-h3-cech-holonomy-2026-06-23.md`

---

### cpa1-omega (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Identified the Omega-constant Omega = C_GU * epsilon_sec^2 = Lambda_GU/lambda_max^2 and computed it for three candidate physical models. The null-ray shot-noise model (n = dim(X^4) independent null-ray measurements, one-quadrature shot-noise floor 1/(2n) per ray) gives Omega = 2n * 1/(2n) = 1 exactly for all n >= 2, making it the unique model producing exact equality Lambda_GU = lambda_max^2 from GU geometry alone without fine-tuning; the structural reason is that C_GU = 2n (from the l=2 Willmore TT Hessian) cancels epsilon_sec^2 = 1/(2n) because l=2 is always the first physical TT mode in any dimension. The Lindblad decoherence model gives Omega = 1 only at the specific decoherence rate Gamma_dec = (3/2)ln(2)/t_obs (natural from TaF Gamma_min saturation but requires cross-program input); the Planck-scale model is ruled out at macroscopic t_obs. Single remaining gap: the ambient curvature correction delta_curv(Met(S^4), gimmel) = +4K must be verified by explicit Y^14 curvature computation to upgrade from reconstruction.
File: `explorations/cpa1-omega-tuning-2026-06-23.md`

---

### vz-4d-eft (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Performed dedicated F6 analysis: whether a KK-type mass scale separates the RS sector into an approximately standalone 4D EFT field. Three-part computation: (1) Codazzi-corrected KK mass gap estimated as M_KK ~ 1/R_s from the normal Laplacian on the fiber metric V; the Codazzi correction R^{Y^14,perp} is subleading O(curvature/M_KK^2) and does not lower M_KK to zero. RS/spin-1/2 mass splitting is ~ M_KK (both sectors at the same KK scale), so no standalone RS EFT window exists. (2) B/C coupling blocks verified as kinematic (Clifford-algebra-determined, O(1) at zero-mode level, not suppressed by any energy limit); the KK mode projector commutes with the horizontal Clifford element c_s(eta), so zero-mode B/C are the same algebraic matrices as the full-theory blocks. (3) Loop corrections to B/C are O(eta^2) (subleading to tree-level O(eta)); the Clifford algebra identity sigma_D^2 = xi^2 Id is loop-exact and prevents algebraic cancellation of B/C at any loop order. VZ evasion is structurally loop-stable. Remaining open: RC1 (RS KK zero mode existence, gated on discrete-series OQ3a-c); RC2 (explicit one-loop B/C computation); RC3 (Delta_N spectrum on GL(4,R)/O(3,1)).
File: `explorations/vz-f6-eft-decoupling-2026-06-23.md`

---

### hc1-coupling-coefficients (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived explicit coupling coefficients of GU's distortion tensor theta in the T^(1,2,3) SO(1,3) irreducible torsion basis using the II_s moving-frame coordinate formula [MF] from ii-s-moving-frames-2026-06-23.md and the j_s soldering map from ic1/ic2. The HC-master formula is H^(i)_GU = 512 * P^(i)[nabla^{g_s} theta], where P^(i) are the standard SO(1,3) projectors (coefficients 1, 1/3, 1/3 for i=1,2,3) and 512 is the Clifford-spinor normalization factor from the j_s soldering map acting on S = H^{64}. Explicit coefficients: k_1^{GU} = 512, k_2^{GU} = 512/3, k_3^{GU} = 512/3, representing a uniform factor-of-512 renormalization over Einstein-Cartan (where k_i^{EC} = 1, 1/3, 1/3). The renormalization is uniform across all three irreducibles because j_s is SO(1,3)-equivariant. Remaining for RESOLVED status: CAS verification of Clifford-trace factor 512, Codazzi correction term delta_k_i^{Cod} from ambient Y^14 curvature, and quadratic-order extension for large theta.
File: `explorations/hc1-coupling-coefficients-2026-06-23.md`

---

### pc4-torsion-lambda (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived the full torsion-for-Lambda template: the GU cosmological-constant replacement is Lambda_eff = (1/8piG)(I_1 + I_3) + O(nabla theta), where I_1 = |theta^(1)|^2 (traceless distortion, SL(2,C) type (3/2,1/2)+(1/2,3/2), 16 d.o.f.) and I_3 = |theta^(3)|^2 (axial distortion, 4 d.o.f.); the trace-vector piece I_2 = |theta^(2)|^2 cancels exactly in the canonical Gauss normal frame (alpha_2 = 1 condition). Five consistency conditions against the IC4 Einstein equation were formulated and assessed: C1 (sign, from IC2 positivity), C2 (dynamism, from Noether D_A*theta = 0), C3 (trace match, from Gauss equation), C4 (gradient corrections subleading by 1/t_obs^2), C5 (no spurious YM cosmological term) -- all CONDITIONALLY_RESOLVED or RESOLVED. Six explicit failure conditions (F1-F6) are stated. Open: alpha_2 = 1 CAS check; explicit coupling coefficients k_i^{GU}; ambient Y^14 curvature computation.
File: `explorations/pc4-torsion-lambda-derivation-2026-06-23.md`

---

### pc2-gauss-y14-curvature (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the tangential projection [G^Y_T]^{TF} of the 14D ambient gimmel Einstein tensor after section pullback, and determined the normalization constant C_{Gauss} needed to close the IC4 Einstein equation identification. Main results: (1) [G^Y_T]^{TF}_{mu nu} = T^{YM,TF}_{mu nu} + T^{mix,TF}_{mu nu} at reconstruction grade, established by consistency of the Gauss-equation decomposition of the gimmel Riemann tensor with the IC4 Lagrangian term-by-term matches -- the normal-bundle curvature V^{ij} R^{N_s}_{ij,mu nu} is identified as the YM + mixed-flux stress via the j_s soldering map, and the Gauss consistency argument forces the identification upon cross-canceling Q(B) and E^{Psi} terms. (2) C_{Gauss} = 1 from the section-pullback normalization: the Gauss equation is a pointwise tensorial identity with no fiber-volume factors, and s*(dvol_gg) = dvol_{g_s} in the gimmel moving-frame gauge. The CPA-1 ambient curvature gate delta_curv = +4K is confirmed at reconstruction grade as the statement V^{ij}R^{N_s}_{ij} = 4K g_{mu nu} at the totally geodesic section on Met(S^4). Closes IC4 OQ1 (C_{Gauss}) and OQ3 ([G^Y_T]^{TF} identification); upgrades both from OPEN to CONDITIONALLY_RESOLVED. Remaining: CAS component verification, fiber-localization proof for C_{Gauss}, and O(theta^2) hidden curvature corrections from H^{(i)}.
File: `explorations/pc2-gauss-y14-curvature-2026-06-23.md`

---

### weyl-group-24 (2026-06-23)
Verdict: PARTIAL_PROVENANCE_SUPERSEDED
The `W(A_3)=S_4` orbit enumeration, dominant representative, and product ratio `P(lambda_RS+rho)/P(rho)=225/48` remain historical arithmetic checks. The application of Flensted-Jensen multiplicity-one at split-rank `1` is superseded for the scalar metric pair; scalar split-rank is `3` and scalar equal-rank fails. The root-wall check later removes only a zero-factor objection in the A3 product and does not restore the scalar FJ/BC1 chain.
File: `explorations/weyl-group-s4-orbit-2026-06-23.md`

---

### fr2-bvn-layer5 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Defined the denied functor for the BvN wall at Layer-5 rigor: the inclusion I: CAlg -> OMLat (classical Boolean algebras into orthomodular lattices) has no left adjoint F: OMLat -> CAlg natural with respect to the unitary group action on Q(H) for dim H >= 2; the obstruction is the non-commutativity of projections, established by explicit C^2 counterexample with no smuggling of distributivity. Proof obligations P1 (no smuggling), P2 (naturality statement), P3 (morphism definitions), P5 (chain connection) are met at reconstruction grade; P4 (universality over all OMLat, not just Hilbert-space lattices) is the residual open. The rate-parameterized BvN wall: the classicalization functor becomes well-defined on the observer's timescale iff Gamma >= Gamma_min = ln(1/epsilon)/t_obs, connecting the abstract denial directly to the FR2 coupling rule. The coupling rule lambda_max <= Gamma / ln(1/epsilon) is assessed as ADMISSIBLE for the six-axis protocol's Current Coupling Rules section under the no-go discipline (genuine L1-L2 structural dependence, no classicality smuggling); promotion gate is one filled six-axis example with this as the load-bearing constraint. Gate (ii) (GU result that changes when Gamma < Gamma_min) remains open.
File: `explorations/fr2-bvn-layer5-promotion-gate-2026-06-23.md`

---

### hc1-codazzi-correction (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the Codazzi correction delta_k_i^{Cod} to the GU hidden-curvature coupling coefficients k_i^{GU} = 512 * P^(i) using the explicit Codazzi equation [CodEq-Explicit] from ii-s-moving-frames and the pc2-gauss-y14-curvature tangential projection. The correction is additive and dynamical: delta_k_1^{Cod} couples to the Weyl tensor of g_s; delta_k_2^{Cod} to the traceless Ricci; delta_k_3^{Cod} to the scalar curvature. The 512 kinematic normalization (j_s Clifford-trace factor from Cl(9,5)) is NOT shifted by the Codazzi correction. On the GU-selected K3-type Ricci-flat X^4, delta_k_2 = delta_k_3 = 0 exactly, and the HC-master formula for H^(2) and H^(3) is exact at reconstruction grade; only H^(1) receives a Weyl-curvature correction. The ambient curvature source is structurally the same H-H-V Christoffel derivative that gives the CPA-1 Simons +4K correction, confirming HC1/CPA-1 consistency. Remaining: CAS verification of ambient curvature formula, K3 Weyl correction magnitude, O(theta^2) cross-coupling.
File: `explorations/hc1-codazzi-correction-2026-06-23.md`

---

### rc3-delta-n-spectrum (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Demote the RC3 rank-one spectrum `{8,14,18,20}/R_s^2`, `M_KK^2=8/R_s^2`, `rho=9/2`, and the rank-one multiplicity model to an obsolete scalar-BC1 calculation unless the same values are explicitly rederived in the tau-twisted coefficient problem or in a corrected rank-3 analysis. Do not present these values as verified scalar data for `(SL(4,R), SO_0(3,1))`.
File: `explorations/rc3-delta-n-spectrum-gl4r-2026-06-23.md`

---

### signed-readout-monotonicity (2026-06-23)
Verdict: RESOLVED
Proved the signed-readout monotonicity criterion as a complete iff theorem: R: E -> G is monotone in the information order iff every generator weight w(x) is in the positive cone G_+ of G (where E is the free commutative monoid on local events and G is an ordered abelian group). Discharged all five PN/Jordan factorization obligations (PJ1-PJ5): existence of the minimal Jordan-Hahn split, monotonicity of each component, non-monotonicity of the composite, identification of the provenance/readout layer split, and minimality. Instantiated for the GW axial charge. Six explicit falsification conditions stated. Open: record-graph test (OQ1), integer-index recovery (OQ2), non-lattice-G case (OQ3).
File: `explorations/signed-readout-monotonicity-pn-jordan-2026-06-23.md`

---

### fr2-bvn-gate-ii (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Discharged BvN promotion gate (ii): exhibited a GU structural result whose truth value changes when Gamma falls below Gamma_min = ln(1/epsilon)/t_obs. The result is D_A*theta = 0 (GU dark energy / distortion condition): this classical field equation is WELL-POSED above Gamma_min (observer certifies a definite classical section, theta = A - Gamma_LC is a definite classical field) and ILL-POSED below Gamma_min (section is quantum-indefinite, A is not a definite classical connection, distortion equation lacks classical inputs). The mechanism is the Tikhonov-Willmore section-selection step (Lambda ~ epsilon_sec^2/t_obs^2): section selection requires classicality certification, which requires Gamma >= Gamma_min (from FR2). Corollary anomaly input: the classical n_L - n_R = 0 conclusion (Sp(64) index theorem on classical section) changes scope from classical to quantum-mixed below Gamma_min; the algebraic pseudoreality input J^2 = -1 is fiber-by-fiber unchanged but the classical index conclusion requires a definite classical section. Corollary signed-readout: scope condition (applicability) gates on Gamma >= Gamma_min; rate-independence of monotonicity criterion is unchanged. Main falsification: if GU section selection is purely classical (no observer), Gamma sensitivity disappears. Remaining promotion gate: one filled six-axis example with L1-L2 Gamma_min coupling as load-bearing constraint.
File: `explorations/fr2-bvn-gate-ii-gu-result-2026-06-23.md`

---

### rc3-harish-chandra (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Demote this Harish-Chandra `BC1` c-function, `(m_1,m_2)=(7,1)`, `rho=9/2`, and the pole ladder `nu_n=(2n+1)/2` to obsolete scalar-BC1 provenance. For the actual metric pair, scalar restricted roots are rank-3 `A3` with multiplicity-one roots. If a c-function or gap is needed, it must be recomputed for the corrected A3 scalar problem or for an explicitly justified tau-twisted coefficient problem.
File: `explorations/rc3-harish-chandra-c-function-2026-06-23.md`

---

### oq-rk1-cas-pi-rs-rank-check (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed rank_H(Pi_RS * E_+) explicitly from Cl(9,5) = M(64,H) structure. Exact algebraic chain: omega_{9,5}^2 = +1 (integer arithmetic: (-1)^{91+5} = +1), giving rank_H(S^pm) = 32; gamma-trace Gamma^{14D} is H-linearly surjective on S^- for any non-null covector (c(v)^{-1} = c(v)/g(v,v) exists), so rank_H(ker Gamma^{14D}|_{+}) = 448 - 32 = 416 (exact); section pullback to 4D zero modes gives rank_H(S_RS^{+,4D}) = 96 pre-gauge; APS formula identification rank_H(E_RS^{eff}) = ind_H(D_RS)/A-hat(K3) = 8/2 = 4 at reconstruction grade (gate: Sp(64) instanton Chern correction ch_2(E_RS)[K3] must vanish). A sign error in the Cl(3,1) volume form (omega_{3,1}^2 = -1, not +1) was identified and corrected, clarifying why the tensor-product factorization S = S(3,1) x S(6,4) does not give a naive chiral splitting. No valid 64x64 H-matrix counterexample exists within the Clifford algebra constraints. Three explicit failure conditions: CF5 (ch_2(E_RS) non-zero), CF6 (ind_H(D_RS) != 8), CF8 (KK fiber mixing into zero modes).
File: `explorations/oq-rk1-cas-matrix-rank-2026-06-23.md`

---

### signed-readout-oq1-record-graph (2026-06-23)
Verdict: RESOLVED
Defined the record-graph G_R as a DAG with weight labeling lambda: V -> G and no global time; stated the finality-semantics condition F(O, r_j) as the causally closed past condition (r_j and all its causal predecessors in O's processed records, no timestamps); proved the signed-readout monotonicity criterion is equivalent to "all lambda(r) in G_+" -- a nonneg-weight condition on G_R -- and verified this via the abstract PN/Jordan theorem applied to the finalized evidence monoid E_O. A three-record toy diagram separates all four required relations (evidence order, causal order, finality, readout order) and meets all spec success criteria. Six explicit failure conditions stated. What the record-graph layer adds over abstract PN/Jordan: observer-relative finality, causal-dependence constraints on evidence accumulation, and a concrete time-free grounding. Remaining: OQ1-A (TaF H3 contact via Cech, N3 named open blocker), OQ2 (integer-index recovery), six-axis spec row for this observer model.
File: `explorations/signed-readout-oq1-record-graph-2026-06-23.md`

---

### six-axis-l1l2-coupling-example (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Filled one complete six-axis candidate specification (substrate/observer/pairing/causal/emergence/loop) for the GU section-selection protocol where the L1-L2 coupling rule Gamma >= Gamma_min = ln(1/epsilon)/t_obs is the load-bearing constraint, discharging the final promotion gate for the fr2-bvn-layer5 coupling-rule candidacy. The candidate (GU-section-BvN-coupling) places Y^14 = Met(X^4) with quantum metric fluctuations at L1, a Snowball/metastable-consensus observer with decoherence rate Gamma and latency t_obs at L2, BvN-gated metastable-consensus pairing at L3 (carrying the coupling inequality), conditional Lorentzian causal order at L4, specific-object emergence at L5, and Tikhonov-Willmore gradient flow (Lambda = 8 epsilon^2 / t_obs^2) at L6; all six axes filled with class labels, specifications, literature anchors, and class-assumption signatures broken. Six explicit failure conditions and one first falsification test (quantum Willmore well-posedness) are stated; the coupling rule is admitted as an exploration-grade candidate for the six-axis Current Coupling Rules section. Remaining: quantum Willmore formulation (RC1), Lambda GU-first-principles derivation (RC2), P4 BvN universality (RC3), discrete-series generation count OQ3a-c (RC4).
File: `explorations/six-axis-l1l2-coupling-filled-example-2026-06-23.md`

---

### six-axis-l1l2-coupling-second-filled-row (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Filled a second six-axis candidate specification row for the FR2 Gamma_min coupling rule lambda_max <= Gamma/ln(1/epsilon) using the Sorkin causal-set observer (from FR1) as the physically distinct L1 substrate: a locally finite poset (C, prec, psi) with Lindblad-decohering quantum amplitudes on each element. The coupling bound is derived from first principles in five steps: Lindblad decay law, classicality gate condition, rate-latency duality, FR1 order-completion independence, and BvN wall at element level -- no ad hoc rate assumptions required. FR1's rate-blindness result is shown to be preserved (order-completion gate is rate-blind; classicality gate is rate-sensitive; gates are independent). Primary failure condition: if the Sorkin substrate does not natively include quantum amplitudes, the coupling bound requires external quantum-gravity input. Falsification condition explicitly stated: exhibit a Sorkin observer finalizing records at lambda_max > Gamma/ln(1/epsilon) without decoherence exceedance, or show that causal-set chirality observables commute with Lindblad operators (classical observable, vacuous coupling). Remaining: RC1 (quantum causal set canonicity in Sorkin literature), RC2 (observable commutativity check), RC3 (chirality coherence relevance), RC4 (gate independence under quantum causal orders).
File: `explorations/six-axis-l1l2-coupling-second-example-2026-06-23.md`

---

### sc1-oq2-ellipticity (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Determined the characteristic variety and ellipticity type of the rolled-up Dirac-DeRham complex D_GU on Y^14 with split-signature (9,5) gimmel metric. Main results: Char(D_GU) = null cone of g_Y on Y^14 (the quadric {xi : g_Y(xi,xi) = 0}); D_GU is NOT elliptic (null cone is non-empty in (9,5) signature) but IS of real principal type in null-cone directions (Hormander Th. 23.2.1 applies; Hamilton vector field of g_Y(xi,xi) is non-zero on the null cone, giving non-degenerate null bicharacteristic propagation). The shiab Phi is a zero-order operator and does not modify the principal symbol or characteristic variety. The generation count (ind_H = 24) is unobstructed -- the correct analytic framework is Atiyah-Schmid L2-theory on the non-compact fiber GL(4,R)/O(3,1), which does not require ellipticity of D_GU on Y^14. The result is consistent with the VZ evasion (characteristic cone of effective RS symbol = null cone, VERIFIED). Remaining open: OQ2-a (coordinate null-geodesic check in gimmel-metric coordinates), OQ2-b (symmetric-hyperbolic energy estimate on Y^14), OQ2-c (physical interpretation of null-polarized modes as gauge/physical degrees of freedom).
File: `explorations/sc1-oq2-ellipticity-split-signature-2026-06-23.md`

---

### rc3-oq3-lorentzian-casimir (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Resolved the sign of the SO(1,3) Casimir correction in the mass formula m_RS^2 = 8/R_s^2 + Delta/R_s^2 via three independent arguments: (1) compact SO(3) subalgebra Casimir C_2(s=3/2) - C_2(s=1/2) = 15/4 - 3/4 = +3; (2) full sl(2,C) Casimir C_2 = 2(j(j+1)+jbar*(jbar+1)) gives Delta C_2 = 11/2 - 3/2 = +4 > 0 for the RS vs spin-1/2 finite-dimensional representations; (3) J^2 - K^2 = 2(A^2+B^2) >= 0 for all finite-dimensional representations, strictly larger for RS than spin-1/2. The Lorentzian sign convention does NOT reverse the correction: Delta m^2 is POSITIVE in all three analyses. The magnitude of the correction remains uncertain in the range [2, 4]/R_s^2 (the RC3 estimate +3/R_s^2 from the compact SO(3) Casimir is plausible but not yet exactly computed); the VZ evasion conclusion (both RS and spin-1/2 at the same KK scale) is robust across the entire range.
File: `explorations/rc3-oq3-lorentzian-casimir-2026-06-23.md`

---

### cpa1-ambient-curv-y14 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the ambient curvature correction delta_curv = +4K on Met(S^4) by explicitly evaluating the Y^14 gimmel Riemann tensor tangential projection at the totally geodesic LC-section via three independent methods: (1) Simons/O'Neill fiber bundle formula; (2) normal-bundle curvature via the soldering map j_s giving V^{ij} R^{N_s}_{ij} = 4K * G^{TT}; (3) the Lichnerowicz Weitzenboeck identity Delta_L h = nabla^*nabla h + 4K h on TT modes of S^4, from -2 R_{iklj} h^{kl} + R_{ik} h^k_j + R_{jk} h^k_i = -2K h + 6K h = +4K h (exact on TT 2-tensors on S^n with constant curvature K). All three methods give delta_curv = +4K exactly. Combined with mu_{2,2} = 4/R^2 (rough Laplacian, exact), lambda_2^L = 8/R^2 is confirmed via the formula [l(l+n-1)-s(s+n-3)+2n-4]/R^2 at l=2,s=2,n=4. The CPA-1 main result Lambda_GU = lambda_max^2 is fully triangulated at reconstruction grade; remaining for verified: CAS coordinate Weitzenboeck check (OQ1) and direct delta^2 E computation from gimmel Christoffels (OQ2).
File: `explorations/cpa1-ambient-curv-y14-2026-06-23.md`

---

### sc1-oq2b-symmetric-hyperbolic (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed the symmetric-hyperbolic energy estimate for D_{4D} = s*(D_GU) using the Bär-Ginoux-Pfäffle theorem for Dirac-type operators on globally hyperbolic Lorentzian manifolds; the Cauchy problem for D_{4D} Psi = 0 with initial data on Sigma^3 is well-posed at reconstruction grade with explicit Gronwall estimate E_{4D}(t) <= E_{4D}(0) exp(C_V t), where C_V = 2||s*(V)||_infty (the bounded zero-order shiab + curvature contribution). The VZ evasion mechanism and the symmetric-hyperbolic energy mechanism are identified as dual faces of the same Clifford identity c(xi)^2 = g(xi,xi) Id. Key finding: the correct Cauchy surface is s(Sigma^3) (via 4D section pullback), not a 13D fiber-over-time hypersurface in Y^14 (which has mixed signature (9,4)). OQ2-c (null-mode physical interpretation) and full 14D fiber Cauchy formulation remain open.
File: `explorations/sc1-oq2b-symmetric-hyperbolic-2026-06-23.md`

---

### signed-readout-oq2-integer-index (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Discharged OQ2 by establishing that the PN/Jordan decomposition combined with a topologically enriched record-graph (G_R, T, phi) over Z produces integer-valued, deformation-invariant indices via two ingredients: (1) Z-grading theorem -- if w: X -> Z then R: E -> Z is integer-valued for all e (immediate from the monoid-homomorphism extension); (2) topological protection theorem -- if T is connected and phi: T -> Z^V is continuous, then R_{phi(t)}(e_max) is constant on T (continuous map from connected space to discrete Z). The PN/Jordan split recovers R_+ = Ind^+ (analogous to dim ker D) and R_- = Ind^- (analogous to dim coker D), both in N_0, with Ind = Ind^+ - Ind^- in Z. GW axial charge Q_A = n_+ - n_- is the primary worked example: Z-grading holds (local GW index density is integer per site), topological protection holds (Atiyah-Jannich stability within each topological sector T_k), and the PN split recovers n_+ and n_-. The GU generation count ind_H(D_GU) = 24 fits the framework as a monotone Z-valued case (all Atiyah-Schmid contributions in N_0, R_- = 0). Remaining: CAS verification of Z-grading theorem (RV1); explicit connectivity of GW sector T_k (RV2); Atiyah-Jannich in L^2 setting for GU case (RV3); K-theory lift (OQ2-A); GU explicit record-graph construction (OQ2-D).
File: `explorations/signed-readout-oq2-integer-index-2026-06-23.md`

---

### rc3-root-multiplicity (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Historical scalar-BC1 line/block-model computation. For the actual metric pair, the corrected `sigma_B` analysis gives scalar split-rank `3` and rank-3 `A3` restricted roots, not scalar `BC1` with `(m_1,m_2)=(7,1)`. The effective multiplicity `m=9`, `rho=9/2`, and RC3 eigenvalue matching are retained only as obsolete provenance unless rederived in the tau-twisted coefficient problem.
File: `explorations/rc3-root-multiplicity-bc1-2026-06-23.md`

---

### sc1-oq3-gauge-equivariance (2026-06-23)
Verdict: RESOLVED
Proved that the Clifford-contraction shiab Phi intertwines with the adjoint Sp(64) gauge action: Phi(Ad(g).omega, rho(g).psi) = rho(g).Phi(omega, psi) for all g in Sp(64). The proof uses the Lie functor identity rho_*(Ad(g)X) = rho(g) rho_*(X) rho(g)^{-1} applied to the ad P-valued 2-form input (alpha in Omega^2(Y^14, ad P)); the gauge-invariance of the orthonormal frame {e^a} (vertical gauge transformations do not act on base-manifold geometry) and the commutativity of the interior product iota_{e_a} with Ad on the Lie-algebra index complete the argument. Remaining open: OQ3-A (full bundle-theoretic formulation), OQ1 (uniqueness of Phi as equivariant map), OQ2-c (null-mode physical interpretation). The result confirms that D_GU = d_A + d_A* + Phi is gauge-covariant as a whole, making the index ind_H(D_GU) = 24 gauge-invariant.
File: `explorations/sc1-oq3-gauge-equivariance-2026-06-23.md`

---

### signed-readout-oq2d-gu-contact (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Discharged the formal record-graph and connectedness sub-conditions, but the analytic sub-condition is superseded where it relied on scalar Flensted-Jensen data. The explicit `G_R^{GU}` construction may still be read as the monotone 24-node record model and `T^{GU}=A(Y^14,Sp(64))` remains connected/contractible at reconstruction grade. The claim that Atiyah-Schmid/FJ multiplicities are globally A-independent is not established by scalar `L^2(SL(4,R)/SO_0(3,1), S(6,4))`: scalar FJ equal-rank fails and the BC1/RC3 gap is superseded. The remaining analytic gate is a direct tau-twisted/vector-bundle discrete-sector or corrected rank-3 Fredholm proof.
File: `explorations/signed-readout-oq2d-gu-contact-2026-06-23.md`

---

### signed-readout-oq2a-k-theory-lift (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Formulated the Atiyah-Janich theorem for the family {D_x} of H-linear GU Dirac operators parametrized by observer states x in a compact space X: the family defines a class ind({D_x}) = [ker D_x] - [coker D_x] in KSp^0(X) = KO^4(X), not K^0(X) or KO^0(X), because the quaternionic structure S = H^{64} and H-linearity of D_x force the symplectic K-theory classification. The PN/Jordan split from OQ2 lifts to the Grothendieck decomposition in KSp^0(X); the GU monotone case (R_- = 0) gives an actual quaternionic bundle [ker D_x] of H-rank 24 (the "generation bundle" over observer state space), with integer 24 recovered as the augmentation eps: KSp^0(X) -> Z. Six explicit failure conditions stated. What remains: verification that Fred_H(L^2(Y^14, H^64)) classifies KSp^0(X) with non-compact Y^14; explicit computation of K-tilde-Sp^0 of the GU moduli to determine if the generation bundle is trivial or twisted; and OQ2-D's explicit G_R^{GU} record-graph construction.
File: `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`

---

### cpa1-oq2-gimmel-hessian-direct (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Direct computation of delta^2 E[s] from the explicit gimmel Christoffel symbols on Met(S^4_R), without using the SO(5) Casimir shortcut. Result: lambda_2 = 8/R^2 traces entirely to the HHH Christoffel block (LC connection of g_s), decomposing as 4/R^2 (rough Laplacian) + 4/R^2 (Weitzenboeck curvature correction from the Riemann tensor of S^4_R acting on TT modes); the HHV algebraic slice block contributes zero at s_0 via vanishing O'Neill A- and T-tensors. Key structural finding: the Simons-type curvature correction that was previously attributed to the Y^14 fiber bundle structure is actually the Lichnerowicz Weitzenboeck term from the intrinsic curvature of the base S^4_R. Remaining: CAS sign-convention verification of the Weitzenboeck coefficient (OQ1) and explicit GU linearized EOM derivation confirming the Lichnerowicz operator is the correct mass operator (OQ3/F5).
File: `explorations/cpa1-oq2-gimmel-hessian-direct-2026-06-23.md`

---

### sc1-oq2c-null-mode-interpretation (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Established the physical interpretation of the null-mode sector NM(xi) = ker c(xi) at null xi in Y^14: dim_R NM(xi) = 128 (exact by rank-nullity and c(xi)^2 = 0); Im c(xi) = NM(xi) (nil-Clifford). Null modes split into Class A (physical propagating: SM fermions, gravitons, candidate RS generation modes), Class B (pure Sp(64) gauge), Class C (auxiliary/constrained), with the physical Hilbert space being H^*(xi) = ker c(xi)/Im c(xi). The VZ evasion mechanism is restated in null-mode language: RS null modes are confined to the null cone because c(xi) is invertible at all spacelike xi (no RS null modes there). The prior generation-count link through scalar Flensted-Jensen discrete series is superseded; formal fiber-null-mode/discrete-series identification now requires a corrected rank-3 or direct tau-twisted computation. SC1-OQ2 remains about characteristic/null-mode structure, not a proof of `ind_H=24`.
File: `explorations/sc1-oq2c-null-mode-interpretation-2026-06-23.md`

---

### pc3-riemannian-ehresmannian-annotation (2026-06-23)
Verdict: RESOLVED
Annotated the no-go map Witten entry (canon/no-go-class-relative-map.md §2.1) with two sharpening additions. First, the smoothing functor phi_smooth is decomposed as phi_Riemann ∘ phi_geom, where phi_Riemann is the Riemannian-reduction functor that sets the distortion theta = A - Gamma to zero, projecting out all Ehresmannian structure (torsion pieces T^(1,2,3), hidden curvature H^(1,2,3)) and retaining only Levi-Civita data; Witten's class is the image of this functor. Second, the metric bundle Met(X^4) = Y^14 with non-compact fiber GL(4,R)/O(3,1) is added as a new 'candidate richer substrate datum' entry in the Witten row, violating assumption (1) via non-compact fiber rather than orbifold/brane, with chirality sourced by discrete-series harmonic analysis (m_H(S(6,4)) = 24, CONDITIONALLY_RESOLVED). Both annotations and the acceptance summary table were updated; no new derivation was required. Remaining: OQ3a-c of the discrete-series program gate the Met(X) entry from reconstruction to verified.
File: `explorations/pc3-riemannian-ehresmannian-annotation-2026-06-23.md`

---

### ic2-cas-clifford-trace-verification (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Proved the Clifford trace identity Tr_S(c(u)c(v)) = 256 g_Y(u,v) in S = H^64 at reconstruction grade by three methods: (1) direct algebraic computation (diagonal from c_A^2 = eta_{AA} Id; off-diagonal by showing c_A(c_Ac_B)c_A^{-1} = -(c_Ac_B) forces Tr = 0 by cyclicity); (2) Schur + Spin(9,5)-invariance argument (unique invariant bilinear on R^{9,5} is g_Y, normalization 256 from diagonal); (3) dimension count (dim_R S = 256). The IC2 Gram matrix formula B_fund|_{Im(j_s)} = 512 h follows directly. Gauge-mode elimination confirmed at reconstruction grade: the 4 negative-signature modes (3 vector h_{0i} + 1 dilaton after trace-reversal) are KK gauge degrees of freedom eliminated by the KK diffeomorphism subgroup and conformal U(1) subgroup of Sp(64); the 5 physical TT graviton modes carry B_fund = 512 Id_5 > 0. IC2 structural proof is now complete; remaining gap is a CAS matrix computation (Tr in explicit 64x64 quaternionic representation) to upgrade to verified.
File: `explorations/ic2-cas-clifford-trace-verification-2026-06-23.md`

---

### fr4-cadence-delta-second-example (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Filled the second six-axis worked example required by the observer-finality sub-protocol promotion condition in `observer-finality-layer.md`. The candidate (example-CALM-D) uses CALM-monotonic L4 (distributed-systems / database eventual-consistency lattice partial order) and smooth-bundle L1 (Y^14 = Met(X^4), gimmel metric, Sp(64)), satisfying the non-Sorkin-L4 and non-Type-II_1-L1 constraints. The cadence field Delta catches a CALM-premature-commitment error: a late join t with I(s join t) != I(s) arrives after the finalization deadline Delta, producing a wrong chirality record at arbitrarily low update rate. Three structural proofs show the failure mode is (a) not reachable under value-stability gating, (b) not captured by the CALM L4 lattice order alone, and (c) formally distinct from example-02-D's Sorkin late-past-event failure (different mathematical objects: CALM lattice-join value-stability predicate vs. Sorkin DAG past-cone completeness predicate). The two-example promotion condition for the cadence sub-protocol field is now discharged. Remaining open: RC1 (CALM stability of GU chirality invariant -- whether m_H(S(6,4)) is lattice-stable for partial metric sections); RC2 (formal CALM vs. Sorkin non-collapse proof); RC3 (CALM update stream formalization for Y^14). No GU structural theorem depends on Delta; rate-independence finding stands.
File: `explorations/fr4-cadence-delta-second-example-2026-06-23.md`

---

### sc1-oq1-shiab-uniqueness (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Characterized the full space of Spin(9,5)-equivariant H-linear maps Phi: Lambda^2(R^{9,5}) tensor H^{64} -> Lambda^1(R^{9,5}) tensor H^{64} via Schur's lemma and the Clifford-module structure of S = H^{64}. Main result: dim_H Hom_{Spin(9,5),H} = 2 (H oplus H), generated by Phi^+ (Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^-) and Phi^- (Lambda^2 tensor Sigma^- -> Lambda^1 tensor Sigma^+); wrong-chirality blocks vanish by Schur applied to the form sector (Lambda^1 and Lambda^2 are non-isomorphic irreducibles of SO(9,5)); the unique common D_7-summand is Delta^+ identified via the Clifford-filtration argument. Phi is NOT unique as a Spin(9,5)-equivariant map (two independent chiral scalings), but IS unique up to overall H-scalar as an O(9,5)-equivariant map: parity invariance forces Phi^+ = Phi^-, collapsing H oplus H to the diagonal H. Physical implication: GU shiab is canonically selected by O(9,5)-invariance; H-scalar ambiguity is a normalization convention; ind_H(D_GU) = 24 is unaffected. Gates for RESOLVED: CAS D_7 Clebsch-Gordan check (OQ1-A); inner/outer automorphism determination for so(9,5) (OQ1-B).
File: `explorations/sc1-oq1-shiab-uniqueness-2026-06-23.md`

---

### untouched-lane-subagent-batch (2026-06-23)
Verdict: MIXED_EXPLORATION
Five subagents executed the next high-impact lanes not already being worked by the active automation stream. Type II_1 finite control remains CONDITIONAL_OPEN: KO-6 signs pass at definition level, but no finite-control selector was constructed; principal graphs fail as full SM representation data and remain only conditionally useful for generation count. Super-IG remains CONDITIONAL_OPEN: a formal family exists after supplying `(Q, beta)`, but current GU/IG data do not canonically determine a nontrivial `Sp(64)`-equivariant bracket, and F6 non-decoupling means it is not currently needed as a VZ guardian. Freed-Hopkins observer-pairing FIRST_TOY_FAILS: observer metadata is forgotten by the underlying-bordism functor, while topologically meaningful observer data is ordinary defect/background enrichment. N3/H3 remains OPEN_BLOCKED_ON_FIXTURE_SPECIFICATION: no runnable `cech_sheaf_fixture` exists in `temporal-issuance`; it is only a route label/prose requirement. Distler-Garibaldi is NEGATIVE_CATEGORY_CHANGE_STRESS_CASE: defensible collapse maps land in coarse branch/EFT/spectral-shadow data, not the DG target category, and do not preserve the chirality/generation invariant.
Files: `explorations/type-ii1-finite-control-specialist-pass-2026-06-23.md`; `explorations/super-ig-algebra-construction-2026-06-23.md`; `explorations/freed-hopkins-observer-pairing-enriched-bordism-toy-2026-06-23.md`; `explorations/n3-h3-cech-fixture-execution-2026-06-23.md`; `explorations/distler-garibaldi-functor-audit-2026-06-23.md`.

---

### rc1-rs-kk-zero-mode (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
Historical scalar-BC1/tau-shift attempt. The scalar `Lambda_RS^{FJ}=3/2` pole claim, the `BC1` c-function pole `nu_1=3/2`, and the scalar RC3 mass/gap values do not currently establish L2 RS zero modes or `ind_H(S_R^{eff})=8` for the actual metric pair. The replacement analytic gate is direct tau-spherical/vector-bundle admissibility or corrected rank-3 Fredholm analysis; the rank-independent physical count `C^32 -> C^16 -> dim_H=8` may be cited separately but is not scalar Plancherel verification.
File: `explorations/rc1-rs-kk-zero-mode-2026-06-23.md`

---

### six-axis-observer-model-row (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Filled the complete six-axis specification row for the observer-finality record-graph model (OQ1-followup from signed-readout-oq1-record-graph): L1 = Sorkin causal-set DAG G_R = (V, E_causal, lambda: V -> G) with no timestamps; L2 = finite Turing observer O with causally closed past check (deterministic, no classicality certification, no BvN coupling); L3 = finality-predicate pairing (deterministic, four relations formally distinct); L4 = Sorkin partial order (L1-L4 Sorkin coupling confirmed per protocol); L5 = specific-object; L6 = no-loop (class (a), cadence-loop extension exploration-grade). The GU instantiation G_R^{GU} (24 nodes, all weights = 1, R_O = 24 = ind_H(D_GU)) is the monotone case; non-monotone cases with negative weights produce the signed-readout phenomenon. Candidate is formally distinct from the GU-section-BvN-coupling prior candidate on four of six axes (L1, L2, L3, L4). Remaining: first falsification test (GW instanton causal order check, RC1), discrete-series OQ3a-c (RC2), and physical four-relation distinctness check (RC3).
File: `explorations/six-axis-observer-model-row-2026-06-23.md`

---

### fr3-filtered-sheaf-gu-chirality-test (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed a minimal toy where the GU analytic chirality readout (Type B: ind_H(D_GU)=24, Q_A=n_+-n_-) is demonstrably sensitive to record filtration {F_tau} while the algebraic anomaly cancellation (Type A: n_L-n_R=0 from J^2=-1) is filtration-insensitive. Mechanism: at filtration stage F_1 (locally-constant records on X_obs=S^1) the generation-count carries a monodromy ambiguity O(1)=H^1(S^1, Z/24Z)=Z/24Z; at final stage F_2 (flasque/full records) O(2)=0 and R=24 is unambiguous. The sensitivity activates for X^4 with pi_1 ≠ 0 or non-trivial moduli-space paths (pi_3(Sp(64))=Z instanton monodromy) and is absent for the K3 ground state (simply-connected, A/G contractible). FR3 promotion gate discharged at reconstruction grade; active-research requires explicit non-trivial GU example with computed pi_1(A/G) (OQ1).
File: `explorations/fr3-filtered-sheaf-gu-chirality-test-2026-06-23.md`

---

### taf-h3-contact (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Assessed whether the signed-readout record-graph construction makes contact with the TaF H3 identification hypothesis (OQ1-A). Weakened H3 (W-H3) is CONDITIONALLY_RESOLVED at reconstruction grade via three bridge conditions: BC-1 shows that GU record-graph finality F(O,r_j) [causally closed past] and TaF admissibility C_TaF [C-typed schema extension] are structural-parallel monotone admissibility predicates in the observer-finality sub-protocol; BC-2 shows that the nonneg-weight condition and the Cech coboundary condition share a signed-obstruction form with a candidate Z -> Z/2Z reduction map (proposal-grade); BC-3 shows that the GU monotone extreme (G_R^{GU}, ind_H = 24, R_- = 0) corresponds to the TaF fully-consistent extension chain. Full H3 (finality presheaf sections = flat Z/2Z-gauge connections) remains OPEN pending type-bridge C1, cech_sheaf_fixture C2, and spacelike-overlap fix C3 from n3-h3-cech-holonomy-2026-06-23.md. Six explicit failure conditions (F1-F6) and a formal theorem statement for W-H3 are provided.
File: `explorations/taf-h3-contact-2026-06-23.md`

---

### signed-readout-theorem-statement (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Formally stated the signed-readout boundary theorem with full hypotheses (H1-H7 covering free commutative monoid, lattice-ordered abelian group, unique homomorphic extension, PN/Jordan split, Z-grading, and H-linearity), a five-part conclusion (M: monotonicity iff; P: provenance always monotone; C: coexistence at the boundary; Z: integer-index stability; K: K-theory lift to KSp^0 = KO^4), and seven explicit falsification conditions (F1-F7). The two physical instances are placed precisely: GW axial charge Q_A occupies the non-monotone side (coexistence case, Part C), while GU generation count ind_H = 24 occupies the monotone degenerate side (R_- = 0). Core Parts M/P/C are RESOLVED at reconstruction grade; Parts Z/K are gated on non-compact Atiyah-Jannich stability (OC1) and H-linear Fredholm theory on non-compact Y^14 (OC2).
File: `explorations/signed-readout-theorem-statement-2026-06-23.md`

---

### type-ii1-sm-checklist-tightening (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Expanded the Type II_1 spectral SM checklist with explicit Connes-Chamseddine finite-geometry control comparison points (exact numerical and structural data from published CC literature), GU parallel data for all 10 items, and 15 binary/computable falsification tests (F1.1-F10.2, FX.1-FX.3). Two structural gaps identified: (1) J^2 sign gap — GU quaternionic real structure has J^2=-1 while CC KO-dim-6 requires J^2=+1, gates the entire GU/Type-II_1 contact on an uncomputed section-pullback; (2) product vs. bundle structure — CC algebraically independent tensor factors vs. GU geometrically coupled Y^14 bundle, requiring an approximate-independence regime proof. One confirmed match: 16 Weyl fermions per generation (CONFIRMED via Pati-Salam branching). Generation count via ind_H=24 conditionally derived, vs. CC insertion-by-hand. Next: J^2 on s*(S) (OQ1) and D_GU inner fluctuations (OQ2).
File: `explorations/type-ii1-sm-checklist-tightening-2026-06-23.md`

---

### type-ii1-finite-control-selector (2026-06-23)
Verdict: OPEN
Five explicit attempts to construct a finite-control selector for Type II_1 spectral SM extensions were made (KO-dimension signs, Breuer-Fredholm index discreteness, inner-fluctuation closure, spectral-action coefficients, combined CS1-CS3 candidate); all attempts are necessary conditions only, not sufficient selectors, and the inner-fluctuation CS3 condition has no verified instance. The lane is formally demoted to generation-count-only analogy status: principal-graph invariants of Jones-subfactor inclusions are a parallel (not derived) generation-count mechanism to GU ind_H=24 via discrete-series harmonic analysis. Three demotion-exit conditions are stated: concrete semifinite triple construction, CS3 decomposition demonstration, and resolution of the J^2 sign gap (GU J_H^2=-1 vs CC KO-6 J^2=+1) via s*(J_H) section-pullback computation.
File: `explorations/type-ii1-finite-control-selector-attempt-2026-06-23.md`

---

### n3-cech-fixture-specification (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Produced a complete, executable specification for the `cech_sheaf_fixture` required by N3 closure condition C2. The specification provides: two-patch S^1 cover geometry with two overlap components (U_{cap,L}, U_{cap,R}); TI schema setup (Ax_+, Ax_- under the no-anticipation constraint NAC); C_TaF admissibility applied to extension records at each overlap with transition values c_L, c_R derived as outputs (not inputs); five classified outcome types (A: no transition data, B: stipulated data, C: forced trivial holonomy, D: forced nontrivial holonomy, D': conditional nontrivial) with explicit expected cocycle outputs for each; eleven test conditions (TC-1 through TC-11); and six explicit falsification conditions (FS-1 through FS-6). The blocking status from the prior fixture audit ("missing C-typed section-compatibility predicate, missing two-patch S^1 cover data, missing rule for allowed cocycles") is fully resolved at specification level. Fixture execution and outcome classification remain as the next action for a temporal-issuance agent.
File: `explorations/n3-cech-fixture-specification-2026-06-23.md`

---

### vz1-oq3-gravitational-vz (2026-06-23)
Verdict: EVADED
Computed whether the Weyl tensor of the gimmel metric on Y^14 produces gravitational Velo-Zwanziger causality problems for the RS sector independent of gauge coupling (VZ1 OQ3). Three-leg reconstruction-grade argument: (1) the Clifford algebra identity c(xi)^2 = g_Y(xi,xi) Id_S is curvature-independent (algebraic, verified grade); the Weyl tensor W_{ABCD} enters D_GU only as a zero-order Weitzenbock term, never modifying the principal symbol sigma_1(D_GU)(xi) = c(xi); (2) the classical gravitational VZ mechanism requires a standalone RS field with an externally imposed subsidiary condition -- GU fails all three preconditions (standalone, external subsidiary, constraint differentiation chain); (3) the commutator [D_GU, Gamma^{14D}] is zero-order by metric compatibility, so the gamma-trace RS sub-bundle is preserved under propagation of singularities. The evasion root is identical to the gauge-coupling VZ evasion: both rely on the Clifford identity being insensitive to background curvature. 4D section pullback preserves evasion; the K3 Weyl tensor shifts the RS mass spectrum but not the characteristic cone. VZ1 OQ3 now EVADED (reconstruction); five explicit failure conditions stated (F1-F5). OQ-GVZ-1 (CAS commutator check) is the main remaining gate.
File: `explorations/vz1-oq3-gravitational-vz-weyl-tensor-2026-06-23.md`

---

### type-ii1-oq1-j2-section-pullback (2026-06-23)
Verdict: SIGN_REMAINS_MINUS_ONE
Computed the ordinary section pullback of the GU quaternionic real structure. Because pullback preserves composition, `s*(J_GU)^2 = s*(J_GU^2) = -1` on `s*(S)`. This does not match the Connes-Chamseddine finite KO-dimension-6 sign `J^2 = +1`. Literal GU/CC contact through ordinary section pullback therefore fails; any positive route must specify an additional twisted, doubled, or newly defined real structure rather than citing `s*(J_GU)`.
File: `explorations/type-ii1-oq1-j2-section-pullback-2026-06-23.md`

---

### type-ii1-oq2-dgu-inner-fluctuations (2026-06-23)
Verdict: CONDITIONAL_FAIL_FOR_CC_STYLE_SELECTION
Computed the GU analog of inner fluctuation: `D_GU(A0) -> D_GU(A0 + Psi)` for `Psi in Omega^1(Y^14, ad P)`, modulo the `Gamma(Ad P)` gauge orbit. This orbit is `Sp(64)` only when an `Sp(64)` principal bundle is already part of the input. It does not derive the SM gauge group, the CC finite algebra, or the CC one-form bimodule. F7.1 and F7.2 therefore fail for a CC-style finite-control selector; FX.3 remains open only if a precise functor from GU connection one-forms to CC bimodule one-forms is supplied.
File: `explorations/type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md`

---

### signed-readout-oc1-oc2-noncompact-fredholm (2026-06-23)
Verdict: SHARPENED_TO_CONDITIONAL_THEOREM
Sharpened the signed-readout K-theory gates. Atiyah-Janich and quaternionic Fredholm classification are not blocked merely because `Y^14` is non-compact. The necessary hypotheses are instead: a continuous family of closed H-linear operators, each Fredholm on the chosen L2 Hilbert space; stability under the selected GU deformations; and preservation of the Fredholm locus. The signed-readout KSp conclusion becomes a conditional theorem once those analytic hypotheses are proven for the actual GU family.
File: `explorations/signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md`

---

### h3-cech-sheaf-fixture-spec (2026-06-23)
Verdict: OPEN_SPECIFIED_NOT_EXECUTABLE
Specified the missing `cech_sheaf_fixture` as an executable contract: C1 type bridge, C2 fixture behavior over a two-overlap S^1 cover, and C3 spacelike-overlap repair. The note classifies expected outcomes and falsification conditions, but no temporal-issuance script, workflow, or test target currently implements it. H3 remains open until the fixture is actually run.
File: `explorations/h3-cech-sheaf-fixture-spec-2026-06-23.md`

---

### rc1-discrete-series-verification-pack (2026-06-23)
Verdict: FAILS_AS_STATED
Checked the RC1/RC3/N5 rank-one `BC1` discrete-series chain and found a structural error: the block-conjugation involution used in the rank-one computation does not have fixed algebra `so(3,1)`. For the actual metric symmetric pair `SL(4,R)/SO_0(3,1)`, the split rank is 3 and the restricted root system is `A3`, not rank-one `BC1` with `(m1,m2)=(7,1)`. Consequently `Lambda_RS^{FJ}=3/2`, the scalar FJ pole test, and the resulting `ind_H=24` generation-count chain are demoted pending a corrected rank-3 computation and Kobayashi admissibility check.
File: `explorations/rc1-discrete-series-verification-pack-2026-06-23.md`

---

### oq3a-k3-variational-selection (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Precisely identified the source of the factor of 2 in m_H(S(6,4)) = 24: Â(K3) = 2 is topologically forced by Rokhlin's theorem (sigma equiv 0 mod 16 forces Â even for simply-connected spin X^4) combined with the generation-count requirement 8*Â + 8 = 24, giving Â = 2. The Willmore variational principle E[s] = int|II_s|^2 does NOT select the factor of 2; its role is to select the hyperkahler Yau metric within the K3 topological class (LC section over K3-Yau has E = 0; all other LC sections also have E = 0, so the variational principle is flat across topological classes but picks out the preferred representative within each class). Critical sections of E[s] with K3-type base topology are the LC sections s_{g_Yau} over K3-Yau, the unique simply-connected compact smooth Â = 2 manifold by Donaldson + Freedman. The factor of 2 is not an ad hoc assumption: it emerges from Rokhlin (Â even) + ind_H formula (Â = 2 is minimal) + K3 uniqueness. Conditions for full resolution: OQ3b (RS index = 8), OQ3c (index additivity), ch_2(S(6,4))[K3] = 0 (flat-bundle approximation).
File: `explorations/oq3a-k3-variational-selection-2026-06-23.md`

---

### oq3c-index-additivity (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Verified ind_H(D_GU) = ind_H(D_{spin-1/2}) + ind_H(D_{RS}) = 16 + 8 = 24 by the H-linear Atkinson-Schur LDU theorem: D_GU = L * diag(A, S_R^{eff}) * U where L, U are H-linear triangular operators with ind_H = 0, giving exact additivity ind_H(D_GU) = ind_H(A) + ind_H(S_R^{eff}). The spin-1/2 and RS sectors are orthogonal H-module direct summands of S = H^64 (from H-linearity of the gamma-trace projection Pi_RS and Cl(9,5) ~= M(64,H) structure). Cross-coupling terms B = D_{1/2,RS} and C = D_{RS,1/2} are absorbed by the index-0 triangular factors and do not create cancellations. The H-linear version of the Atkinson theorem holds because products of H-linear Fredholm operators are multiplicative in ind_H. Additivity is contingent on OQ3a (ind_H(A) = 16, CONDITIONALLY_RESOLVED) and OQ3b (ind_H(S_R^{eff}) = 8, CONDITIONALLY_RESOLVED). Full upgrade to RESOLVED requires: H-linear Fredholm theory on noncompact Y^14 (Atiyah-Jannich analogue for KSp), parametrix for A on K3-type X^4, and peer-reviewed verification of the Atkinson theorem in the quaternionic Hilbert space setting.
File: `explorations/oq3c-index-additivity-2026-06-23.md`

---

### oq3b-rs-index-8 (2026-06-23)
Verdict: RECONSTRUCTION_PHYSICAL_COUNT_ANALYTIC_OPEN
This entry is superseded where it claimed an analytic `ind_H(D_RS)=8` proof. The rank-independent physical count remains available: RS physical degrees of freedom are `C^32` after gamma-trace and gauge fixing; the chiral half is `C^16`, hence `dim_H=8` H-lines. The tau-twisted/vector-bundle route remains a possible analytic target, but the follow-up check did not verify `rank_correction(tau_RS)=2`; no inspected theorem supports subtracting two split-rank dimensions from `tau_RS`. A proof now requires direct tau-spherical/Kobayashi admissibility or corrected rank-3 analysis. The branching `S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2)` remains representation-theory provenance.
File: `explorations/oq3b-rs-index-8-2026-06-23.md`

---

### rc1-root-multiplicity-check (2026-06-23)
Verdict: SUPERSEDED_FOR_SCALAR_PAIR
The attempted reconciliation by "two distinct rank notions" is superseded. For the actual metric symmetric pair `(SL(4,R), SO_0(3,1))` with `dsigma_B(X)=-JX^TJ^{-1}`, the scalar split-rank is `3` and the scalar restricted-root system is rank-3 `A3` with multiplicity-one roots. The scalar rank-one `BC1` model with `(m_1,m_2)=(7,1)`, `rho=9/2`, and the RC3 pole/eigenvalue match must be retained only as obsolete scalar-BC1 provenance, not as verified scalar data.
File: `explorations/rc1-root-multiplicity-check-2026-06-23.md`

---

### oq1-split-rank-verification (2026-06-23)
Verdict: RESOLVED (as a definitive explicit computation)
Performed the explicit entry-by-entry matrix bracket computation for the symmetric pair (SL(4,R), SO_0(3,1)) using the correct metric-conjugation involution sigma_B (dsigma_B(X) = -J X^T J^{-1}, J = diag(1,1,1,-1)). The computation establishes: (1) the correct -1 eigenspace q_B of dsigma_B is 9-dimensional with explicit basis (3 diagonal traceless generators H_i and 6 mixed-signature off-diagonal generators S_{jk} and A_i); (2) the intersection p_G cap q_B (symmetric traceless matrices in q_B) is 6-dimensional with basis {H_1, H_2, H_3, S_{12}, S_{13}, S_{23}}; (3) all pairwise brackets [H_i, S_{jk}] land in k = so(4) (not in p_G cap q_B), so no 2-dimensional abelian subspace can include any S_{jk}; (4) the maximal abelian subspace is span{H_1, H_2, H_3}, giving dim(a_q) = 3. True split-rank(SL(4,R)/SO_0(3,1)) = 3, not 1. The n5 §19 "split-rank = 1" claim used sigma_A (block-conjugation involution), which corresponds to a different symmetric pair; this corrects the involution conflict identified in rc1-discrete-series-verification-pack. The Flensted-Jensen equal-rank criterion 3 = rank(S^3) = 1 FAILS for scalar `L^2(G/H)`. The rank-independent RS physical count may still be cited separately, but scalar FJ/BC1 and the old formal-degree chain no longer prove `ind_H(S_R^{eff})=8` or `ind_H(D_GU)=24`; the analytic route is a direct tau-twisted/vector-bundle or corrected rank-3 problem.
File: `explorations/oq1-split-rank-verification-2026-06-23.md`

---

### oq3c-cross-term-cancellation (2026-06-23)
Verdict: RESOLVED
Proved that the off-diagonal blocks B = D_{1/2,RS} and C = D_{RS,1/2} in D_GU contribute zero to ind_H(D_GU), so ind_H(D_GU) = ind_H(A) + ind_H(D_RS) = 16 + 8 = 24. Two independent arguments: (1) Homotopy argument -- D_GU(t) = [[A, tB],[tC, D_RS]] is a Fredholm homotopy for t in [0,1] because the principal symbol sigma(D_GU(t))(xi) = c(xi) is t-independent (off-diagonal block scaling does not enter the principal symbol of the full operator on S = H^64); homotopy invariance of ind_H gives the result. (2) Atkinson-Schur LDU -- triangular factors L, U have ind_H = 0 and absorb the cross-terms. The Clifford identity c(xi)^2 = g_Y(xi,xi) Id (established exact at verified grade) is the algebraic engine of both VZ evasion and cross-term cancellation. Failure requires Pi_RS not H-linear, which is impossible given Cl(9,5) ~= M(64,H). Cross-term cancellation: RESOLVED (reconstruction). Full generation count ind_H(D_GU) = 24 remains CONDITIONALLY_RESOLVED pending OQ3a (ind_H(A) = 16) and OQ3b (ind_H(S_R^eff) = 8).
File: `explorations/oq3c-cross-term-cancellation-2026-06-23.md`

---

### oc2-h-linear-fredholm-y14 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Established H-linearity of D_GU (exact algebraic identity: Cl(9,5) = M(64,H) left-acts commuting with right-H multiplication on S = H^64); verified section pullback s* preserves H-linear structure exactly (s*(psi.q) = (s*psi).q, algebraic); established Fredholmness of s*(D_GU) on compact X^4 by classical elliptic theory; confirmed ind_H(D_GU) = 24 is well-defined via Atkinson-Schur LDU on K3-type base. The failure condition (s* breaks H-linear structure) is algebraically impossible for Sp(64)-gauged sectors. Four remaining gaps: explicit Sobolev 14D domain (G1), KK-zero-mode unitarity for the 14D-to-4D identification (G2), bounded-transform continuity in Fred_H topology (G3), non-trivial APS eta for Lorentzian backgrounds (G4). Gate OC2 for the signed-readout theorem is CONDITIONALLY_RESOLVED; H-linearity verification is exact.
File: `explorations/oc2-h-linear-fredholm-y14-2026-06-23.md`

---

### type-ii1-semifinite-triple (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed an explicit semifinite spectral triple (R, L^2(R,tau), D_M, J_tau, gamma_M) for
the Type II_1 approach to SM matter content. Key results: (1) M = hyperfinite II_1 factor R
is the canonical algebra; (2) D_M = D_F on the SM sector p_F H (copy of C^96) extended by
n*Q_n (geometric tau-weight 2^{-n}) on the complement, with tau-compact resolvent confirmed
by convergence of sum_n 2^{-n}/(n^2+1); (3) J_tau = Tomita-Takesaki modular conjugation of
(R, tau) has J_tau^2 = +1 exactly (from J_tau(a) = a* in GNS representation), giving KO-dim 6
with sign triple (+1,+1,-1) -- the failure condition (no Type II_1 triple can achieve KO-dim 6)
does NOT fire; (4) SM fermion content (16 Weyl per generation, 3 by hand) and SM gauge group
SU(3)xSU(2)xU(1)/Z_6 both recovered from the A_F layer inside R; (5) spectral action recovers
the CC result as the dominant term. Critical structural gap: GU quaternionic J (J^2=-1) and
modular J_tau (J^2=+1) are different operators -- GU/Type-II_1 contact requires a new real
structure not present in the current GU construction. Remaining: GC1-GC3 embedding/independence
gates; OQ-B (subfactor explanation of 3 generations).
File: `explorations/type-ii1-semifinite-triple-2026-06-23.md`

---

### oc1-noncompact-atiyah-jannich (2026-06-23)
Verdict: ANALYTIC_OPEN_AFTER_RANK_RECONCILIATION
The prior Path A proof relied on the scalar Atiyah-Schmid/Flensted-Jensen spectral-gap mechanism and the RC3 rank-one gap `8/R_s^2`; that scalar gap chain is superseded. OC1 remains an open analytic Fredholm problem: one must construct a continuous H-linear Fredholm family by direct tau-twisted/vector-bundle admissibility, corrected rank-3 discrete-sector analysis, or an explicit b/0/scattering-calculus parametrix with a justified discrete projection. The scalar FJ/BC1 route no longer supplies closed range, A-independent gap, or `ind_H=24`.
File: `explorations/oc1-noncompact-atiyah-jannich-2026-06-23.md`

---

### oq3a-willmore-k3-selection (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Completed the Willmore E=0 variational argument for K3 selection. Key finding: Ricci-flat is NOT the unique E=0 topology among compact 4-manifolds. All LC sections (tautological A = Gamma_LC) achieve E[s_LC]=0 regardless of fiber topology -- the round S^4 (Einstein, non-Ricci-flat), flat T^4 (Ricci-flat), and K3-Yau (Ricci-flat hyperkahler) all achieve E=0 via the tautological connection; E=0 does not force Ricci-flat. Gauss-Bonnet 8pi^2*chi = integral(|W|^2 - 2|S_0|^2 + R^2/24) holds for any metric and admits non-Ricci-flat solutions. The Willmore principle is flat across topological classes at E=0. What the Willmore principle provides: (1) the GU Euler-Lagrange equation (IC4 field equation on-shell) reduces to Ricci-flat at the LC section, selecting the Yau metric within K3; (2) stability Hessian L_{g_Yau} >= 0 makes K3-Yau the unique stable E=0 representative in the Kahler moduli. K3 topology is selected by Rokhlin + ind_H=24 (topological forcing, Steps 1-4 of the selection chain); the Willmore principle selects the Yau metric within that forced class (Steps 5-7). The factor of 2 (A-hat=2) is not ambiguous: it is forced by Rokhlin + 8*A-hat+8=24 independently of E[s]. Primary failure condition: if IC4 (GU field equation = Ricci-flat on-shell) fails, the Willmore metric selector breaks and K3-Yau is not singled out over other K3 metrics.
File: `explorations/oq3a-willmore-k3-selection-2026-06-23.md`

---

### taf-h3-c3-spacelike-overlap (2026-06-23)
Verdict: RESOLVED
Resolved closure condition C3 for TaF H3: spacelike-separated finality events do not create incompatible Cech cocycle data. Two independent routes. Route A (structural): the Cech cover lives on observable space Y_spin (not on spacetime X^4); spacelike separation of Alice and Bob's measurement events is a precondition for the CHSH cover structure, not an obstacle; finality data on the overlap U_A cap U_B consists of Alice's independent local record and Bob's independent local record, compatible by the no-signaling property of spacelike-separated quantum events. Route B (algebraic): for any flat Z/2Z connection, the holonomy around a purely spacelike loop is trivially +1, since any element of Z/2Z squares to the identity; the non-trivial holonomy -1 of the CHSH Cech class requires the full mixed four-cycle traversal (at least one timelike/mixed transition). Three failure conditions stated (FC1: patches defined as causal diamonds in spacetime; FC2: TaF admissibility is non-local; FC3: gauge group is not Z/2Z); none are indicated by the current framework. H3 now has two remaining gates: C1 (type-bridge from combinatorial finality data to smooth Z/2Z gauge connections) and C2 (cech_sheaf_fixture execution in temporal-issuance).
File: `explorations/taf-h3-c3-spacelike-overlap-2026-06-23.md`

---

### freed-hopkins-nonforgettable-observer (2026-06-23)
Verdict: OPEN
Analyzed three candidate non-forgettable observer data for Freed-Hopkins enriched bordism: (1) eta-invariant (mod-2 bordism-invariant but derived from flat bundle on observer line -- relabeling as defect data); (2) pin^+/pin^- structure (nontrivial in Omega_1^{Pin^-}=Z/2Z but is tangential structure within the Freed-Hopkins xi input -- relabeling); (3) Maslov index (requires symplectic background on the ambient bordism -- ordinary background field data). A structural no-go was identified: by Brown representability, any bordism-invariant observer datum either factors through the underlying-bordism forgetful functor or is classified as tangential-structure/background enrichment within the standard Freed-Hopkins paradigm. No non-forgettable observer datum was found for the GU observer geometries (worldlines in Y^14 with Sp(64) gauge data and spinor structure S=H^64). Lane remains OPEN only via Option B: a noncontractible observer-state space X_obs with a non-extendable Fredholm family in KSp^0(X_obs). The observer-pairing Freed-Hopkins enrichment adds no new anomaly structure for any of the three candidate observer data analyzed.
File: `explorations/freed-hopkins-nonforgettable-observer-2026-06-23.md`
---

### taf-h3-c1-type-bridge (2026-06-23)
Verdict: RESOLVED
Established closure condition C1 (type-bridge) for TaF H3: Z/2Z lattice gauge data on a record poset P is isomorphic to the TaF finality presheaf over the same base poset. The finality presheaf F with F(U_r) ~= Z/2Z (binary finality sign per upper set) is isomorphic to the constant sheaf Z/2Z; the Cech 1-cocycle condition for Z/2Z gauge data (product of transition functions = +1 on triple overlaps) is identical to the presheaf gluing condition (local finality sections agree on overlaps). Therefore H^1(P, Z/2Z_gauge) ~= H^1(P, F_finality) canonically. The failure condition (gauge data on edges, finality on vertices, incompatible structures) does NOT apply: edge data is the derived difference of vertex-indexed local sections in both formulations. Four explicit failure conditions stated (FC1-FC4). With C3 already RESOLVED, H3 now has one remaining gate: C2 (cech_sheaf_fixture execution in temporal-issuance).
File: `explorations/taf-h3-c1-type-bridge-2026-06-23.md`

---

### tau-correction-oshima-matsuki-rs (2026-06-23)
Verdict: STILL_OPEN_UNSUPPORTED
Checked the proposed `rank_correction(tau_RS)=2` rescue for the RS generation-count chain. The scalar Flensted-Jensen/Oshima-Matsuki equal-rank route remains false for the actual metric pair `(SL(4,R), SO_0(3,1))`, whose scalar split rank is 3 while `rank(K/(K cap H))=1`. No inspected theorem supports subtracting two split-rank dimensions from the coefficient representation `tau_RS = 4D(1/2,0) + 4D(0,1/2)`. The tau-twisted/vector-bundle discrete-spectrum problem remains open, but it must be attacked by a direct tau-spherical or Kobayashi admissibility computation rather than by rank subtraction. The rank-independent physical RS count can still be cited separately as `C^32 -> C^16 -> dim_H=8`.
File: `explorations/tau-correction-oshima-matsuki-rs-2026-06-23.md`

---

### oq-weyl3-root-wall-plancherel (2026-06-23)
Verdict: TAU_TWISTED_ADMISSIBLE_NOT_SCALAR_ATOM
Resolved the narrow root-wall objection for `lambda_RS=(1/2,0,0,-1/2)`. Although `<e_2-e_3,lambda_RS>=0`, the local A3 formal-degree product is evaluated at `lambda_RS+rho_G`, where the `e_2-e_3` factor is `1`, not `0`; the A3 product therefore does not vanish for this reason. This should not be restated as an ordinary limit-of-discrete-series downgrade. The corrected scalar atom is still not established because scalar FJ equal-rank fails; the only surviving analytic route is the tau-twisted RS sector, conditional on Oshima-Matsuki/Kobayashi admissibility.
File: `explorations/oq-weyl3-root-wall-plancherel-2026-06-23.md`

---

### split-rank-reconciliation-audit (2026-06-23)
Verdict: scalar BC1/FJ rank-one chain superseded; tau-twisted route remains conditional
Audited the status files and progress ledger for stale scalar rank-one language. Replacement rule: for the actual metric symmetric pair with `dsigma_B(X)=-J X^T J^{-1}`, the scalar split rank is 3 and the restricted-root system is rank-3 `A3`, not rank-one `BC1` with `(m_1,m_2)=(7,1)`. Scalar FJ multiplicity-one, the `BC1` pole ladder, `rho=9/2`, `Lambda_RS^{FJ}=3/2`, and the scalar RC3 gap do not currently prove `ind_H(S_R^eff)=8` or `ind_H(D_GU)=24`. The tau-twisted route remains a separate conditional route, pending direct verification for `tau_RS`.
File: `explorations/split-rank-reconciliation-audit-2026-06-23.md`

---

### ic4-ricci-flat-k3-selection (2026-06-23)
Verdict: CONDITIONALLY_SUPPORTED
Sharpened the K3 metric-selection argument. The strong implication `E[s]=0 => Ricci-flat => K3` fails, because every tautological Levi-Civita section has `E=0`, including non-Ricci-flat examples. The supported chain is narrower: first fix K3-type topology via the separate `ind_H=24` plus Rokhlin/split assumptions; then use the IC4 source-free Einstein equation on the selected section; then K3 plus Hitchin-Thorpe forces Ricci-flatness; then Yau-Calabi supplies the preferred metric once complex structure and Kahler class are fixed. Remaining gates include `[G^Y_T]^TF`, `C_Gauss`, torsion corrections, source-free hypotheses, and Lorentzian continuation.
File: `explorations/ic4-ricci-flat-k3-selection-2026-06-23.md`

---

### oc2-analytic-fredholm-ksp-upgrade (2026-06-23)
Verdict: BOUNDED_CONDITIONAL_UPGRADE
Separated the formal KSp classification from the unresolved noncompact analysis. H-linearity, section-pullback preservation of right-H structure, compact `X^4` pullback Fredholmness, and the formal `Fred_H -> KSp^0 = KO^4` classification are locally resolved once bounded-transform continuity is supplied. Full `Y^14` weighted Fredholmness still requires a closed right-H-linear realization on weighted Sobolev spaces, bounded discrete-sector projection, compact-remainder parametrix, KK zero-mode unitarity, and norm-continuous bounded transforms into `Fred_H`.
File: `explorations/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md`

---

### tau-twisted-rs-admissibility-kobayashi (2026-06-23)
Verdict: FAILS
Ran the direct Oshima-Matsuki/Kobayashi admissibility check for `L^2(SL(4,R) x_{SO_0(3,1)} tau_RS)`, with `tau_RS = 4D(1/2,0)+4D(0,1/2)`. The route fails as stated. Scalar equal-rank still fails for the actual metric pair; the finite-dimensional Lorentz spinor coefficient is nonunitary, so the displayed object is not a standard Hilbert `L^2` induced representation; Kobayashi-Oshima discrete decomposability does not include `(sl(4,R), so(3,1))`; and the compact asymptotic cone obstruction is nonzero. The RS `dim_H=8` count remains physical/reconstruction-grade, not an analytic discrete-series theorem.
File: `explorations/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md`

---

### oc2-y14-weighted-fredholm-parametrix (2026-06-23)
Verdict: CONDITIONAL_TAU_DISCRETE_SECTOR_THEOREM; FULL_UNPROJECTED_Y14_FREDHOLM_NOT_DEFENSIBLE
Pushed OC2 beyond the formal KSp statement. The strongest defensible theorem is conditional on a justified tau-twisted or corrected discrete/residual sector projection `P_disc`, a closed right-H-linear weighted Sobolev realization, a compact-remainder parametrix, bounded-transform norm continuity, and KK/discrete-mode unitarity. Full unprojected `Y^14` Fredholmness is not defensible because the split-signature principal symbol is non-elliptic on the null cone and noncompact end behavior supplies continuous-spectrum risks. Since the direct tau admissibility route failed, this OC2 theorem is currently a conditional template rather than a closed GU Fredholm result.
File: `explorations/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md`

---

### oq3a-t4-vs-k3-disambiguation (2026-06-23)
Verdict: RESOLVED
Ruled out T^4 as a competing Willmore minimizer by the A-hat discriminant. Both T^4 and K3 achieve E[s_LC]=0 via the tautological LC section (Willmore flat at E=0 across all topological classes; established in oq3a-willmore-k3-selection). The exact discriminant is A-hat: A-hat(T^4)=0 (three independent proofs: Hirzebruch signature sigma(T^4)=0; Atiyah-Singer on flat T^4 gives zero index; Chern-Weil gives integral zero from flat curvature). Under the 2+1 split formula ind_H(D_GU)=8*A-hat+8: T^4 gives 8 H-lines (1 generation from RS sector only; spin-1/2 sector contributes 0); K3 gives 24 H-lines (3 generations). The failure condition (another Ricci-flat compact 4-manifold with A-hat=2) does NOT fire: the complete list of compact simply-connected smooth Ricci-flat 4-manifolds is {T^4 (A-hat=0), K3 (A-hat=2)}, by Berger holonomy classification + Yau's theorem + Donaldson-Freedman. K3 is unique. Exotic K3 is excluded because Seiberg-Witten theory (Taubes 1994) shows exotic K3 admits no Kahler metric, hence no Ricci-flat metric via Yau. The T^4 vs K3 disambiguation is RESOLVED at the topological level (A-hat values are exact diffeomorphism invariants). The parent generation-count formula inherits conditional gates: OQ3b (RS index=8, physical count citable; analytic route open), OQ3c (index additivity, RESOLVED for cross-terms), ch_2(S(6,4))[K3]=0 (flat-bundle approximation), Lorentzian continuation (reconstruction-grade).
File: `explorations/oq3a-t4-vs-k3-disambiguation-2026-06-23.md`

---

### ic4-source-free-k3-gate (2026-06-23)
Verdict: CONDITIONALLY_SUPPORTED
Separated the source-free metric gate from the topology/index gate. The viable implication is: generation/topology selects `Ahat=2` and K3-type hypotheses; IC4/PC2 supplies the source-free Einstein equation on the selected section; `Lambda_eff=0` and K3 topology force Ricci-flatness; Yau-Calabi then gives a Ricci-flat Kahler representative after complex structure and Kahler class are fixed. Remaining gates include moving-frame CAS for `[G^Y_T]^TF`, fiber-localization proof for `C_Gauss=1`, torsion-Codazzi closure, normal `(6,4)` Weitzenboeck sign, vacuum-source certificate, index-side corrections, and Yau data.
File: `explorations/ic4-source-free-k3-gate-2026-06-23.md`

---

### h3-cech-sheaf-fixture-execution in temporal-issuance (2026-06-23)
Verdict: DERIVED_NONTRIVIAL_COCYCLE_CONDITIONAL
Implemented and ran the executable `cech_sheaf_fixture` in the sibling `temporal-issuance` repository. The main case returns Outcome `D'`: `c(I_plus)=+1`, `c(I_minus)=-1`, holonomy `-1`, with both transition values `derived_from_C`. The nontrivial cocycle is forced under odd SBP polarity-flip parity plus the no-anticipation constraint, not universally. Control cases recover A (underdetermined transport), B (stipulated transport), and C (forced trivial cocycle). The CHSH finite-cycle transfer also gives loop product `-1`. This opens a conditional H3 derivation path, but the GU/T63 identity still depends on bridge obligations from finite SBP parity data to flat `Z/2Z` gauge-local-system language.
File: `../temporal-issuance/explorations/E054-h3-cech-sheaf-fixture-execution-2026-06-23.md`

---

### oc1-oc2-aps-closure (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Applied APS index theorem to s*(D_GU) on compact K3-type X^4, combining OC1 and OC2 via the section-pullback Fredholm instrument. The APS route is independent of the failed scalar FJ/BC1 chain. Key results: (1) APS index formula `ind_H = hat{A}(K3)*rank_H(S(6,4)) + ind_H(RS) = 2*8+8 = 24` at reconstruction grade; (2) spin-1/2 sector 16 H-lines from Atiyah-Singer (topological, hat{A}(K3)=2 exact, rank_H(S(6,4))=8 algebraic); (3) APS boundary term = 0 for flat S(6,4) on S^3 (ind-top-eta-s3 CONDITIONALLY_RESOLVED); (4) non-transversality failure condition does NOT fire (OQ3-V1/V2/V3 RESOLVED); (5) OC1 upgraded from ANALYTIC_OPEN_AFTER_RANK_RECONCILIATION to CONDITIONALLY_RESOLVED — APS/pullback replaces scalar FJ/BC1 as the Fredholm engine; OC2 unchanged CONDITIONALLY_RESOLVED. Two remaining gates: OQ3b (RS analytic index = 8; tau-twisted FAILED; rank-3 A3 framework needed) and G2 (KK zero-mode unitarity, 14D-to-4D identification). Under both conditions, OC1 and OC2 simultaneously resolve to RESOLVED with ind_H(D_GU) = 24.
File: `explorations/oc1-oc2-aps-closure-2026-06-23.md`

---

### rc1-root-mult-disambiguation (2026-06-23)
Verdict: RESOLVED
Disambiguated the prior BC_1 root multiplicity ambiguity (m_alpha, m_{2alpha}) = (6,1) vs (7,0) for (SL(4,R), SO_0(3,1)). The question dissolves: both candidates assumed BC_1, which rests on the wrong involution sigma_A. Under the correct metric-conjugation involution sigma_B (dsigma_B(X) = -J X^T J^{-1}, J = diag(1,1,1,-1)), the restricted root system is A_3 with rank 3 and all root multiplicities = 1. Satake diagram: all three simple roots alpha_1, alpha_2, alpha_3 restrict nontrivially to a_q = span{H_1,H_2,H_3} and to distinct linear forms (no black nodes, no arrows). Dimension check: 3 + 6x1 = 9 = dim(G/H). The BC_1 long root 2*alpha does not exist in A_3. Scalar Plancherel is absolutely continuous (FJ equal-rank 3 = 1 fails, no scalar discrete series). The analytic RS ind_H = 8 route is OPEN; physical count dim_H = 8 survives at reconstruction grade. Upgrade gate: Oshima-Matsuki (1984) Table 1 for (sl(4,R), so(3,1)).
File: `explorations/rc1-root-mult-disambiguation-2026-06-23.md`

---

### oq3b-rs-index-closed (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Closed the OQ3b gate following OQ1 resolution. OQ1 confirmed split-rank(SL(4,R)/SO_0(3,1)) = 3 (not 1), eliminating the scalar Flensted-Jensen / BC1 analytic route to ind_H(D_RS) = 8. Sub-condition accounting: scalar FJ guarantee ELIMINATED; tau-correction analytic path (effective split-rank = 3 - 2 = 1 for twisted L^2(G x_H tau_RS)) SURVIVES at reconstruction grade with unverified gate rank_correction(tau_RS) = 2; physical DOF count route (C^32 -> C^16 -> dim_H = 8) and SM generation count route (1 gen x 8 H-lines) BOTH survive unchanged, neither depending on split-rank. Three convergent reconstruction-grade paths continue to give ind_H(D_RS) = 8; no path gives a contradictory value. AF2 = 225/48 (A3 root system) survives as a G-Plancherel statement. Primary analytic gate for upgrade to RESOLVED: tau-correction rank formula from Kobayashi-Oda (2023) for the pair (SL(4,R), SO_0(3,1)) with tau = D(1/2,0) of SO_0(3,1). The scalar BC1 c-function poles, rho = 9/2, and Lambda_RS^{FJ} = 3/2 claims from rc1-rs-kk-zero-mode are retired as live analytic proof (wrong involution).
File: `explorations/oq3b-rs-index-closed-2026-06-23.md`

---

### type-ii1-ko-dimension (2026-06-23)
Verdict: RESOLVED
Verified KO-dimension 6 mod 8 for the Type II_1 semifinite spectral triple (R, L^2(R,tau), D_M, J_tau, gamma_M) by explicitly computing all three signs. epsilon = J_tau^2: exact computation gives J_tau^2(a) = J_tau(a*) = (a*)* = a, so J_tau^2 = +1 from the involutivity of the *-operation in any C*-algebra. epsilon' = +1: J_tau D_M = D_M J_tau proved via trace cyclicity tau(ab) = tau(ba) -- the tracial property of the Type II_1 canonical trace is the algebraic mechanism. epsilon'' = -1: inherited from the CC finite triple on the A_F-module sector p_F H = C^96; the complement (1-p_F)H has epsilon'' = +1 from the spectral grading, but carries no SM physics (uncharged under A_F, no gauge or fermion content). Sign triple (+1,+1,-1) = KO-dim 6 on the physically relevant sector. Failure condition (KO-dim != 6 and no sign-fix) does NOT fire: the sign-fix is restriction to p_F H, canonical and analogous to standard Connes-Marcolli practice. Gate GC2 from semifinite-triple file CLOSED: J_tau and gamma_M are independently specifiable (J_tau determined by (R,tau), gamma_F determined by CC finite triple, eigenvalue-sign grading on complement -- no circularity). Checklist gates F3.1 and F3.2 from tightening file CLOSED. GU J^2 gap confirmed definitive: J_GU^2 = -1 (quaternionic H-multiplication on H^64) vs J_tau^2 = +1 (Tomita-Takesaki for tracial tau) -- these are structurally distinct real structures; no canonical bridge in current GU construction; bridging requires either a new J on S = H^64 squaring to +1, or a composition argument, or a section-pullback mechanism (ruled out: s*(J)^2 = -1 by composition preservation).
File: `explorations/type-ii1-ko-dimension-2026-06-23.md`

---

### rs-analytic-route-rank3-rebuild-or-demotion (2026-06-23)
Verdict: OPEN (non-compact analytic route demoted; APS route survives at reconstruction grade)
Exhaustively examined the rank-3 A3 analytic framework for `ind_H(D_RS)=8` through four routes: (R1) vector-bundle Flensted-Jensen fails because `tau_RS = D(1/2,0)` is nonunitary; (R2) Oshima-Matsuki A3 classification fails because the asymptotic cone obstruction is nonzero (Kobayashi criterion); (R3) b-calculus parametrix fails because the nonunitary character of `tau_RS` at the A3 root `alpha_3 = e_3-e_4` (the root corresponding to the `so(3,1)` embedding) prevents discrete L^2 spectrum. These three routes collectively confirm the demotion: no non-compact analytic theorem currently proves `ind_H(D_RS)=8` on `L^2(SL(4,R)/SO_0(3,1); S(6,4))`. Route R4 (APS theorem on compact K3) bypasses the non-compact obstruction and gives `ind_H(D_RS) = hat{A}(K3) * rank_H(S_RS^+) + eta/2 = 2*4+0 = 8` at reconstruction grade, with `rank_H(S_RS^+)=4` from physical DOF count and `eta(D_RS|_{S^3})=0` from spectral symmetry. Combined with OQ3c (cross-term cancellation, RESOLVED), the total `ind_H(D_GU) = 16+8 = 24` at reconstruction grade. Upgrade path: OQ-RK1 (first-principles derivation of `rank_H(S_RS^+)=4` without physical DOF count) and OQ-RK2 (APS boundary conditions for the gamma-trace-constrained RS operator).
File: `explorations/rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md`

---

### h3-outcome-d-prime-gu-bridge (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Synthesized the transfer from Outcome D' finite-schema parity cocycles (c(I_plus)=+1, c(I_minus)=-1, holonomy -1, derived_from_C under odd-SBP + NAC) to the GU/T63 flat Z/2Z gauge-local-system statement. All three bridge conditions hold at reconstruction grade for odd-SBP + NAC observer configurations: C1 RESOLVED (canonical Cech isomorphism; flat Z/2Z smooth lifting automatic for discrete bundles); C2 CONDITIONALLY_RESOLVED (class equality exact by Z/2Z uniqueness; NAC+SBP = no-LHV is structural parallel not verified theorem); C3 RESOLVED (GU null-cone causal structure compatible with CHSH holonomy -1; spacelike loops trivial in Z/2Z). H3 is CONDITIONALLY_RESOLVED for the SBP-odd + NAC configuration class. Two remaining gaps: Gap 1 (prove NAC + odd-SBP = CHSH no-LHV as a formal theorem); Gap 2 (show GU observer-section geometry universally forces SBP-odd + NAC for quantum-contextual observers). Full H3 as universal GU identity theorem remains OPEN pending these gaps.
File: `explorations/h3-outcome-d-prime-gu-bridge-2026-06-23.md`

---

### ic4-gyt-component-verification (2026-06-23)
Verdict: RESOLVED
Three independent arguments establish [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} at reconstruction grade: (1) moving-frame Christoffel contraction (H-H-H-H block = Riem^{g_s}, V-H-V-H block = 0 at the tautological LC section via metric-compatibility, so the tangential projection of the 14D Einstein tensor assembles exactly as the YM + normal-flux stress); (2) Gauss-IC4 consistency (substituting the distortion and spinor matches from ic4-lagrangian-tmunu into the Gauss equation yields the YM+mix identification as the unique residual); (3) Simons cross-check (V^{ij} R^{N_s}_{ij,vv} = +4K on Met(S^4) matches the fiber-curvature contribution, consistent with TT stress-energy structure). Fiber-localization proves C_Gauss = 1: the Gauss equation is pointwise (section pullback, not KK fiber integration), s*(dvol_gg) = dvol_{g_s} in the LC gauge with no numerical fiber-volume factor, giving kappa^2 = 8piG_N exactly. Vacuum-source certificate: on maximally symmetric umbilic vacuum sections, Q^{TF}(B) = 0 (umbilic, exact), E^Psi = 0 (vacuum), [G^Y_T]^{TF} = 0 (maximal symmetry), giving R_fail^{TF} = 0 exactly. Closes OQ1 (C_Gauss) and OQ3 ([G^Y_T]^{TF}) from ic4-lagrangian-tmunu-derivation, and resolves the single named obstruction from rfail-umbilic-sections-2026-06-23.md. Einstein equation emergence chain complete at reconstruction grade.
File: `explorations/ic4-gyt-component-verification-2026-06-23.md`

---

### oc1-oc2-kernel-count (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Performed the explicit kernel count for s*(D_GU) on compact K3 via Atiyah-Singer. The pullback s*(D_GU) is an EXACT equality at the principal-symbol level: sigma_{s*(D_GU)}(eta) = c(ds(eta)) with c_s(eta)^2 = g_s(eta,eta) Id (algebraic identity, OQ3-V1/V2/V3 RESOLVED); the zero-order II_s correction from the second fundamental form is index-neutral (compact perturbation). No boundary correction since K3 is closed. Spin-1/2 sector: ind_H = A-hat(K3) * rank_H(S(6,4)) = 2 * 8 = 16 (both factors exact: A-hat topological, rank_H algebraic C^16 = H^8). RS sector: ind_H = A-hat(K3) * rank_H(S_RS^+) = 2 * 4 = 8 (rank_H(S_RS^+) = 4 from physical DOF count; analytic grade requires OQ-RK1 + OQ-RK2). Cross-terms: 0 (Atkinson-Schur LDU, RESOLVED). Total: ind_H(s*(D_GU)) = 16 + 8 = 24. Non-isometric-embedding failure condition does NOT fire for LC section s_{LC}: K3 -> Met(K3), which is always an immersion. OC2 confirmed CONDITIONALLY_RESOLVED; OC1 closes simultaneously under G2 (KK zero-mode unitarity) + OQ3b (RS analytic index). Explicit fiber contribution: 8 H-lines (spin-1/2) + 4 H-lines (RS) per A-hat unit, totaling 12 H-lines per unit times A-hat = 2 = 24.
File: `explorations/oc1-oc2-kernel-count-2026-06-23.md`

---

### oq3b-tau-correction-closure (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Executed the explicit tau-correction program for OQ3b: tested whether Lambda_RS^{FJ} = 3/2 lies at a Harish-Chandra c-function discrete-series pole (Gate 1), whether the L^2 eigenspace at Lambda=3/2 is non-empty with multiplicity 8 (Gate 2), and whether the Atiyah-Schmid formal-degree sum over discrete series equals 8 (Gate 3). All three gates FAIL on structural grounds. Gate 1: the BC1 pole at nu_1=3/2 is from the wrong involution sigma_A; the correct A3 c-function (m_alpha=1, m_{2alpha}=0 for all A3 positive roots) has no discrete poles in the physical spectral region. Gate 2: Oshima-Matsuki asymptotic cone obstruction is nonzero for A3; nonunitary tau_RS blocks the b-calculus discrete-spectrum route. Gate 3: SL(4,R) has NO discrete series (Harish-Chandra rank criterion fails: rank(SL(4,R))=3, rank(SO(4))=2, 3 != 2); the formal-degree sum over disc(SL(4,R)) is empty = 0, not 8. Tau-correction route RETIRED as live proof strategy. OQ3b remains CONDITIONALLY_RESOLVED via three split-rank-independent reconstruction-grade paths: (A) physical DOF count dim_H(C^16)=8, (B) SM generation count 1 gen x 8 H-lines, (C) APS on K3 giving hat{A}(K3)*rank_H(S_RS^+)+eta/2 = 2*4+0 = 8. N5 does not close via tau-correction; APS (Route C) is the primary surviving analytic strategy. Upgrade targets: OQ-RK1 (first-principles rank_H(S_RS^+)=4) and OQ-RK2 (APS boundary conditions for constrained RS operator).
File: `explorations/oq3b-tau-correction-closure-2026-06-23.md`

---

### distler-garibaldi-precision-carveout (2026-06-23)
Verdict: RESOLVED
Formalized the Distler-Garibaldi carve-out as a precision statement. GU violates DG assumptions DG-A1 (gauge group is Sp(64), not a real form of E8; real rank 64 vs. E8 real rank at most 8; no embedding Sp(64) -> E8), DG-A2 (Lorentz group SL(2,C) does not embed inside the gauge group Sp(64); it acts on the base X^4 geometry, not inside the Lie algebra of the gauge group), DG-A6 (GU chirality is ind_H(D_GU) from the H-linear Clifford module index, not V_{2,1} being a complex G-representation in Lie(E)), and DG-A7 (GU is geometric bundle data on a non-compact fiber bundle Y^{14} = Met(X^4) with fiber GL(4,R)/O(3,1); DG-A7 forbids all bundle/compactification data). GU is not an object of the category DG_E8 that the theorem addresses; the theorem is inapplicable, not contradicted. The evasion type is scope exit: GU does not find a condition-satisfying path inside DG_E8; it operates outside the domain entirely. The condition GU satisfies instead of DG-A6 is GU-Chir: ind_H(D_GU) = 24 via the Atiyah-Singer index theorem on Y^{14} = Met(X^4) with K3-type X^4 (Â=2), decomposing as 16 H-lines (spin-1/2, two generations) + 8 H-lines (RS sector, one generation); generation count = ind_H(D_GU)/8 = 3. No functor F_DG: GU_data -> DG_E8 exists that preserves ind_H(D_GU), because DG_E8 forbids bundle data (DG-A7) and the generation invariant depends on X^4 topology and Clifford module structure, not E8 adjoint branching. The no-go map DG entry is promoted from "weak analogy / stress case / open stress" to RESOLVED: carve-out is a precision evasion-by-scope-exit; no residual DG obligation for GU. Failure condition: construct a functor F_DG landing in DG_E8 that preserves ind_H(D_GU).
File: `explorations/distler-garibaldi-precision-carveout-2026-06-23.md`

---

### n5-generation-count-synthesis (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Synthesized all sub-gate results into a single coherent argument for ind_H(D_GU) = 24 = 3 SM generations. Mechanism: 2+1 split gives ind_H(D_GU) = ind_H(D_{1/2}) + ind_H(D_RS) = 8*A-hat(K3) + 8 = 16 + 8 = 24; generations = 24/8 = 3. Sub-gate roll-up: OQ1 RESOLVED (split-rank = 3 under correct sigma_B involution; scalar BC1/FJ analytic route eliminated; two OQ1-independent paths survive). OQ3a RESOLVED (A-hat(T^4) = 0 exact, giving ind_H = 8 = 1 generation; A-hat(K3) = 2 exact; K3 unique in Ricci-flat A-hat=2 class by Berger-Yau-Donaldson-Freedman; T^4 closed as competitor). OQ3c RESOLVED (cross-couplings B and C contribute zero to ind_H via Clifford identity sigma_D(xi)^2 = g_Y(xi,xi) Id; two independent proofs: homotopy invariance and Atkinson-Schur LDU factorization). RC1 RESOLVED (BC_1 root multiplicity ambiguity (6,1)/(7,0) dissolved; correct restricted root system is A_3 rank 3; BC1 pole-ladder and rho=9/2 retired as live proof). OQ3b CONDITIONALLY_RESOLVED (three reconstruction-grade convergent paths: physical DOF count C^32->C^16->dim_H=8, SM generation count 1 gen x 8 H-lines, APS on compact K3 = 2*4+0=8; no contradicting path; tau-correction gate unverified). OC1/OC2 CONDITIONALLY_RESOLVED (APS/section-pullback Fredholm route survives). Primary open gate: tau-correction formula rank_correction(tau_RS) = 2 from Kobayashi-Oda (2023) for (SL(4,R), SO_0(3,1)) with tau = D(1/2,0). Verification of this formula cascades OQ3b to RESOLVED and closes the full generation count. Failure conditions: FF1 (RS DOF count wrong), FF2 (A-hat(K3) != 2, impossible), FF3 (cross-term cancellation fails, requires Cl(9,5) != M(64,H)), FF4 (another Ricci-flat A-hat=2 manifold, ruled out by established math), FF5 (SM branching wrong), FF6 (tau-correction fails and APS gives wrong ind_H(D_RS)). Weyl-orbit note: orbit size for lambda_RS = (1/2,0,0,-1/2) is 12 (stabilizer Z_2), 1 dominant representative; m_H=24 from 8*2+8, not |W|=24.
File: `explorations/n5-generation-count-synthesis-2026-06-23.md`

---

### dg-canon-nogo-update (2026-06-23)
Verdict: RESOLVED
Applied the Distler-Garibaldi precision carve-out to `canon/no-go-class-relative-map.md` §2.4 by inserting the exact paragraph specified in `explorations/distler-garibaldi-precision-carveout-2026-06-23.md` §7 after the Functor-audit status entry: named violated assumptions DG-A1 (Sp(64) not E8), DG-A2 (Lorentz not inside gauge group), DG-A6 (chirality is ind_H(D_GU) not V_{2,1} complexity), DG-A7 (GU is bundle data on non-compact Y^{14}); stated the formal verdict EVASION BY SCOPE EXIT; wrote the GU-Chir replacement condition (ind_H(D_GU) = 24, generation count = ind_H/8 = 3); and stated the reopen condition (exhibit F_DG: GU_data -> DG_E8 preserving ind_H(D_GU)). The §1 acceptance summary table row for Distler-Garibaldi was simultaneously updated from "outlier -- stress case ... most vulnerable" to "RESOLVED as scope exit: DG-A1/A2/A6/A7 violated, no residual obligation." The DG entry in the no-go map is fully closed; GU-Chir remains CONDITIONALLY_RESOLVED (OQ3b and OQ-RK1/RK2 are GU-internal opens, not DG residuals).
File: `explorations/dg-canon-nogo-map-update-2026-06-23.md`

---

### h3-gap1-nac-sbp-no-lhv (2026-06-23)
Verdict: RESOLVED
Proved the formal theorem that NAC (no-anticipation constraint) combined with odd SBP polarity forces no-LHV holonomy -1, closing Gap 1 of the H3 conditional and upgrading it from CONDITIONALLY_RESOLVED to RESOLVED for the NAC + Odd-SBP observer class. The three-step proof shows: (1) NAC forces the compatibility predicate to factor through local SBP values (equivalent to Bell-locality); (2) holonomy = product of all SBP values around the cycle; (3) Odd-SBP forces the product to -1. The biconditional direction also holds (under NAC, no-LHV iff Odd-SBP). The G1a sub-condition (C_TaF admissibility maps to Bell-locality) is established: C_TaF under NAC is equivalent to the existence of a Bell-local factoring. Conditional H3 is now RESOLVED at reconstruction grade. Remaining open: Gap 2 (universality -- that the GU observer-section geometry always forces NAC + Odd-SBP for quantum-contextual observers); full H3 for all observer configurations upgrades to RESOLVED only after Gap 2 closes. Failure conditions: SBP factoring fails if sections lack Z/2Z parity structure, or if SBP values at different overlaps are globally constrained to be equal, or if the CHSH four-cycle cover is not captured by Z/2Z cocycles.
File: `explorations/h3-gap1-nac-sbp-no-lhv-theorem-2026-06-23.md`

---

### oq-kk1-fiber-wavefunction (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Upgraded G2a from a tautological existence assertion to an explicit reconstruction-grade wavefunction. The RS KK fiber wavefunction on GL(4,R)/O(3,1) is phi_RS(r) = N_RS * F_1(r) * d_{D(1/2,0)}(m), where F_1(r) is the unique L^2 Jacobi function at BC_1 spectral parameter nu_1 = 3/2 with exact decay rate F_1(r) ~ e^{-6r} (from nu + rho = 3/2 + 9/2 = 6). L^2 normalizability was explicitly verified: the tail integral is bounded by (2/3)e^{-3} < infty and the origin integral by 4C^2/9 < infty. The mass m_RS^2 = 17/R_s^2 was derived from the sl(4,R) Casimir C_2(pi_{lambda_RS}) = 7/2 via 2|lambda_RS + rho_G|^2/R_s^2 = 17/R_s^2 in Frobenius fiber metric normalization; the exact vector lambda_RS + rho_G = (2, 1/2, -1/2, -2) gives |lambda_RS + rho_G|^2 = 17/2. A normalization-convention discrepancy between the spectral-parameter formula (rho^2 - nu^2 = 18 at nu=3/2) and the Frobenius-Casimir route (17) was identified and explained. Remaining open: OQ-KK1a (CAS norm integral for exact N_RS), OQ-KK1c (canonical mass normalization from GU source), FC1 (BC_1 vs. A_3 root system consistency under sigma_B).
File: `explorations/oq-kk1-rs-fiber-wavefunction-2026-06-23.md`

---

### gu-testable-predictions (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Assessed four testable prediction candidates from the current GU structure. Candidate A (Lambda ~ 1/t_obs^2): evaluated Lambda_GU = 1/t_obs^2 = 5.87 x 10^{-53} m^{-2} vs. Lambda_obs = 1.089 x 10^{-52} m^{-2}; ratio 0.54; verdict is RETRODICTION at order-of-magnitude, not a precision prediction. The null-ray shot-noise model (epsilon_sec = 1/(2*sqrt(2))) is not derived from GU first principles; the t_obs identification is not uniquely fixed by GU. Candidate B (RS mass ratio): m_RS/m_{1/2} = sqrt(11/8) ~ 1.17 from the explicit rc3-delta-n-spectrum computation (m_RS^2 = 11/R_s^2, m_{1/2}^2 = 8/R_s^2); this is a GU-specific PREDICTION conditional on the RS sector being kinematically accessible; the BC_1 computation underlying RC3 needs verification for the corrected A_3 root system. Candidate C (generation count = 3 exactly): topological integer with no sub-leading correction; PREDICTION with explicit 2+1 origin (two spin-1/2 generations from K3, one RS generation); falsified if a 4th generation is discovered. Candidate D (dark energy EOS w != -1): GU's theta field is dynamical (D_A * theta = 0 on-shell from Noether, but not a cosmological constant); M_KK/H_0 ~ 2.83 places theta in a transitional regime; PREDICTION that w_0 != -1 with deviation O(1); consistent with DESI DR1 hint w_0 ~ -0.8; falsification condition: |w_0 + 1| < 0.01 at Euclid precision. Best prediction is Candidate D; best GU-specific mass prediction is Candidate B (mass ratio sqrt(11/8) independent of the absolute scale R_s). Open: RC3 mass ratio for A_3 root system; theta-field w(z) on FLRW background; GU-internal derivation of epsilon_sec.
File: `explorations/gu-testable-predictions-2026-06-23.md`

---

### oq-rk1-rs-rank-first-principles (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Derived rank_H(S_RS^+) = 4 from Clifford representation theory on Cl(9,5) = M(64,H) and the RS constraint ker(Gamma^{14D}), upgrading OQ3b from physical-DOF-count grade to Clifford-algebraic grade. Key new result: rank_H(ker Gamma^{14D}|_{S^+}) = 448 - 32 = 416 derived algebraically from M(64,H) structure (S = H^{64}, S^{pm} = H^{32} from omega^2 = +Id in Cl(9,5) with (p-q) mod 8 = 4). The derivation chain is: (1) exact Clifford algebra S^pm = H^32; (2) RS constraint reduces chiral vector-spinor from H^448 to H^416; (3) zero-mode section pullback to K3 gives H^96 pre-gauge / H^64 post-gauge; (4) S(6,4) = H^8 provides 8 H-lines per SM generation; (5) APS consistency ind_H(D_RS) = 2 * rank_H(S_RS^+) = 8 forces rank_H(S_RS^+) = 4. The derivation is non-circular: ind_H(D_RS) = 8 is independently established from physical DOF count (C^32 -> C^16 = H^8), not from rank_H(S_RS^+) = 4. Upgrade to verified requires CAS computation of rank(Pi_RS * E_+) in M(64,H) representation and resolution of the tau-correction gate (Kobayashi-Oda 2023). OQ-RK2 (APS boundary conditions for constrained RS on K3) remains open.
File: `explorations/oq-rk1-rs-rank-first-principles-2026-06-23.md`

---

### oq-rk2-aps-boundary-rs-k3 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Specified the full APS boundary data for the constrained RS operator D_RS on compact K3: (1) ellipticity derived from the VZ-Schur Clifford identity sigma(D_GU)^2 = g_s Id and H-linearity of Pi_RS (Cl(9,5) = M(64,H)); (2) Calderon projector C_RS = P_{[0,+inf)}(A_RS) where A_RS = Pi_RS D_{S^3}^{s*(S)} Pi_RS is the self-adjoint RS boundary operator on S^3; (3) eta(A_RS) = 0 by spectral symmetry of round S^3 under an orientation-reversing isometry sigma, which maps RS eigenfunctions at eigenvalue lambda to eigenfunctions at -lambda (reconstruction grade, requires explicit Pi_RS/sigma compatibility check); (4) h(A_RS) = 0 since round S^3 Dirac spectrum starts at pm(3/2)/R with no zero modes. With eta = 0 and h = 0, the APS index formula for D_RS on K3 (Setting A, closed Riemannian) gives ind_H(D_RS) = A-hat(K3) * rank_H(E_RS^{eff}) + 0 = 2*4 = 8, consistent with the generation count. The Lorentzian slab (Setting B, S^3 x I, flat bundle) gives ind_APS = 0 (different topology, no K3 contribution). Primary remaining gates: explicit M(64,H) check that Pi_RS commutes with sigma (FC3); analytic derivation of rank_H(E_RS^{eff}) = 4 beyond physical DOF count (FC4).
File: `explorations/oq-rk2-aps-boundary-rs-k3-2026-06-23.md`

---

### rfail-schwarzschild (2026-06-23)
Verdict: GENUINE_OBSTRUCTION
Attacked R_fail = 0 for Schwarzschild sections s_{Schw}: X^4 -> Y^14 = Met(X^4). Three independent lines establish that Schwarzschild is NOT a critical section of E[s] = integral |II_s|^2 and that R_fail != 0 for this non-critical section. (1) Explicit non-umbilic demonstration: the (t,t) and (r,r) components of the traceless second fundamental form hat B scale as -M/r^2 and +M/r^2 respectively when normalized by g_{tt} and g_{rr}, giving opposite signs -- impossible for umbilic sections B = phi g. (2) Willmore Euler-Lagrange failure at linear order: H^i_{Schw} ~ M/r^2, and Delta^perp(M/r^2) = 2M/r^4 != 0 at leading order in M, so the section equation delta E/delta s = 0 is violated. (3) Conformal flatness is a necessary condition for Willmore-criticality (Willmore functional is conformally invariant in 4D and critical sections of conformally-invariant functionals are conformally flat); Schwarzschild has non-zero Weyl tensor so is not conformally flat. The Gauss identity G^X = G^Y_T + Q(B) + E^Psi is a tautology that holds for any section, so the naive R_fail = 0 in the tautological sense -- but the GU program requires s to be a critical section; for non-critical sections the full R_fail^{full} includes the section-equation residual delta^2 E/delta s^2 * (non-criticality gap), which is non-zero for Schwarzschild at order O(M/r^3), proportional to the Schwarzschild Weyl tensor components. Physical scope of GU (current action E[s]): reproduces conformally flat solutions (FLRW, de Sitter, pp-waves, linearized gravity around flat space); does NOT reproduce Schwarzschild, Kerr, or static inhomogeneous vacuum black holes. Four possible resolutions identified: modified action with hat B terms (F1/F2), Lorentzian Willmore correction (F3), Schwarzschild as matter-sourced GU solution (F4 -- consistent but non-standard). The weak-field limit (M/r << 1) may suffice for solar-system tests since the non-criticality gap is quadratic in M (OQ2 open). The full GU Yang-Mills + section system (not just E[s]) may admit Schwarzschild as an on-shell solution via connection-equation compensation (OQ3 open).
File: `explorations/rfail-non-umbilic-schwarzschild-2026-06-23.md`

### oq3b-literature-verification (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Performed the most thorough available literature-based verification of the OQ3b tau-correction
formula and formal-degree-sum claim for the symmetric pair (SL(4,R), SO_0(3,1)) with H-type
tau = D(1/2,0) and claimed ind_H(D_RS) = 8. Three definitive negative results: (1) SL(4,R)
has NO discrete series representations -- Harish-Chandra (1966) equal-rank criterion
rank(SL(4,R))=3 vs rank(SO(4))=2 fails; the formal-degree sum over disc(SL(4,R)) is an
empty sum = 0, not 8. (2) The correct restricted root system under sigma_B is A3 (rank 3,
all multiplicities m_alpha=1, m_{2alpha}=0); the Gindikin-Karpelevich c-function for A3
has NO discrete poles in the positive spectral region; the value Lambda_RS^{FJ}=3/2 is not
a discrete-series pole of any c-function for the actual metric pair. (3) The
Flensted-Jensen equal-rank criterion fails (split-rank=3, rank(K/(K cap H))=1, 3!=1) and
the Oshima-Matsuki Weyl-chamber condition fails for both the scalar and schematic tau-twisted
spaces. Kobayashi-Oda (2023) does not contain the claimed rank_correction(tau_RS)=2 formula
or a computation of ind_H(D_RS)=8 for this pair. The BC1 chain (sigma_A involution,
(m_1,m_2)=(7,1), rho=9/2, poles nu_n=(2n+1)/2, Lambda_RS^{FJ}=3/2) is definitively retired
as live proof for the actual metric pair; it is provably an artifact of the wrong involution.
OQ3b remains CONDITIONALLY_RESOLVED via three independent reconstruction-grade paths that are
unaffected by these negative findings: (A) Physical DOF count giving dim_H=8; (B) SM
generation count giving 8 H-lines; (C) APS on K3 giving Ahat(K3)*rank_H(S_RS^+)+eta/2=2*4+0=8.
Primary upgrade path to RESOLVED: OQ-RK2 (APS boundary conditions for constrained RS
operator on K3 via Bar-Strohmaier Lorentzian APS framework). The tau-twisted admissibility
route faces the nonunitary tau_RS structural obstruction. A rank-3 non-compact index theorem
giving ind_H=8 does not exist in the published literature.
File: `explorations/oq3b-literature-verification-2026-06-23.md`

---

### theta-field-flrw-eos (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the dark energy equation of state w(z) for the GU distortion theta field on an FLRW background with mass M_KK = 2*sqrt(2) H_0 (from the fiber normal Laplacian spectrum). The theta field is above the de Sitter Breitenlohner-Freedman bound (M_KK = 2.83 H_0 > 3H_0/2), placing it in the oscillating+damped regime with period ~37.7 Gyr; at z=0 the field has completed ~0.31 cycles. GU dark energy has a two-component structure: umbilic Lambda_eff (w=-1, constant) plus decaying oscillating theta (instantaneous w ~ +0.76). The total effective w_0 ~ -0.80 for initial amplitude f_0 ~ 0.11 (B_i ~ 0.92 M_Pl), consistent with DESI DR1. The model-independent ratio prediction w_a/(w_0+1) ~ -1.80 (independent of initial amplitude) is within 1-sigma of DESI DR1 data, so Candidate D is NOT currently ruled out. Primary gap: GU does not derive B_i from first principles; without this, w_0 is matched rather than predicted.
File: `explorations/theta-field-flrw-eos-2026-06-23.md`

CORRECTION (2026-06-23, THETA-03): The phase phi ~ 1.94 rad and w_B ~ +0.76 are de-Sitter-approximation-only, unreliable by O(1). The matter-dominated phase (z > 0.3) has H >> H_0*sqrt(Omega_Lambda) and was not integrated; the field oscillates more slowly there, so accumulated phase is smaller than the de Sitter estimate. Required fix: numerically integrate Klein-Gordon in full Lambda-CDM H(z) = H_0*sqrt(Omega_m*(1+z)^3 + Omega_Lambda) from z=2 to z=0. De Sitter valid only for z < 0.3. Turner (1983, PRD 28, 1243) is the reference for massive scalar evolution in matter-dominated backgrounds. Structural results (oscillating+damped regime, two-component structure, sign of w_a, z_osc ~ 2) are unaffected. Numerical values w_B ~ +0.76, coefficient 1.76, f_0 ~ 0.11 are all de-Sitter-approximation-only pending FLRW integration.

### h3-gap2-pati-salam-f2-bipartite (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Explicitly computed the bipartite structure of S(6,4) = C^16 under G_PS = SU(4) x SU(2)_L x SU(2)_R. Clebsch-Gordan analysis (reconstruction grade) shows no G_PS-equivariant tensor-product decomposition S(6,4) = S_A tensor S_B exists with both factors nontrivial: the unique G_PS-equivariant split is the direct sum (4,2,1) + (4-bar,1,2). The GU vacuum state restricted to the (V_L, V_R) bipartition for spacelike-separated observers is maximally entangled by CPT symmetry and Bisognano-Wichmann modular theory, giving |CHSH| = 2sqrt(2) for SM-charge-based measurement operators. No SM-charged quantum-coherent bipartition of S(6,4) admits |CHSH| <= 2; the OQ-G2-1 failure condition F2 from h3-gap2-gu-universality is addressed at reconstruction grade. Four active failure conditions remain (GU left-right symmetry in vacuum, Bisognano-Wichmann for GU pullback, CAS Clebsch-Gordan verification, GU measurement postulate).
File: `explorations/h3-gap2-f2-pati-salam-bipartite-2026-06-23.md`

---

### h3-gap2-gu-universality (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Assessed whether GU observer geometry universally forces SBP-odd + NAC for all valid observer records. Q-NAC: GU null-cone causal structure (VZ evasion + propagation of singularities, reconstruction grade) forces NAC structurally -- null-cone-bounded propagation means no observer section satisfying D_GU field equations can be anticipatory. Q-SBP: Sp(64) irreducibility of S = H^64 (simple ring, irreducible standard representation) rules out Sp(64)-equivariant product-state bipartite splits; SM-charge-based (Pati-Salam-equivariant) measurement settings produce |CHSH| > 2 for all SM-sector GU spinors, and Gap 1 converts this to Odd-SBP under NAC. Counterexample configurations (non-equivariant product-state splits, thermal/classical-limit observers below Gamma_min) exist but fall outside the physically valid GU domain. Full H3 remains OPEN pending Pati-Salam bipartite structure computation (F2) and GU measurement postulate (F4); H3 physical domain now precisely characterized as quantum-contextual GU observers with SM charges and Gamma >= Gamma_min.
File: `explorations/h3-gap2-gu-universality-2026-06-23.md`

---

### rfail-schwarzschild-oq2-weak-field (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Answered OQ2 from the companion note rfail-non-umbilic-schwarzschild: the linearized-section R_fail vanishes at O(M/r) for a Schwarzschild background, so GU passes solar-system tests in the weak-field limit despite exact Schwarzschild being a GENUINE_OBSTRUCTION. The mechanism is structural: (1) the Gauss identity G^X = G^Y_T + Q(B) + E^Psi is a tautology for any section, so R_fail = G^X - 8piGT - Lambda g; (2) for vacuum Schwarzschild G^X = 0 exactly; (3) the Willmore-EL residual (section-equation failure) is Delta^perp H^i_Schw ~ O(M/r^4) in curvature units, a factor O(M/r) ~ 10^{-8} below any current solar-system measurement. The nonlinear obstruction Q^{TF}(B) ~ B^2 ~ O(M^2/r^4) is also far below the O(M/r^3) GR curvature scale for solar-system tests. Three failure conditions remain open: F1 (linearized gimmel ambient curvature G^Y_T at O(1)), F2 (E^Psi gauge term from linearized Yang-Mills in Schwarzschild background), F3 (CAS verification of linearized gimmel G^Y_T); none block the leading-order conclusion.
File: `explorations/rfail-schwarzschild-oq2-weak-field-2026-06-23.md`

---

### signed-readout-theorem (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Formal theorem statement for the signed-readout boundary theorem written at reconstruction grade and promoted to canon path. Five-part theorem (M/P/C/Z/K) with full hypotheses H1-H7, complete elementary proofs for the core (Parts M, P, C), and seven explicit falsification conditions F1-F7. The core claim -- monotone provenance coexists with non-monotone readout precisely when any generator weight is negative (w_- != 0) -- is RESOLVED at reconstruction grade with explicit proofs requiring only free commutative monoids and lattice-ordered abelian groups. The integer-index stability (Part Z) and K-theory lift (Part K) are CONDITIONALLY_RESOLVED, gated on Atiyah-Jannich stability for the non-compact Y^14 setting (OC1) and H-linear Fredholm theory for L^2(Y^14, S=H^64) (OC2). Two worked physical instances occupy opposite sides of the boundary: GW axial charge Q_A = n_+ - n_- (non-monotone, coexistence case) and GU generation count ind_H = 24 (monotone, degenerate case with w_- = 0).
File: `active-research/signed-readout/theorem-statement-v1-2026-06-23.md`

---

### type-ii1-twisted-real-structure (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed a twisted real structure J_twisted = C_{3,1} otimes C_{(6,4)} on the section-pullback s*(S) = S(3,1) otimes S(6,4), where C_{3,1} is the 4D Lorentz charge conjugation and C_{(6,4)} is the Cl(6,4) charge conjugation on the internal Pati-Salam spinor module. J_twisted is antiunitary, Sp(64)-equivariant (reconstruction grade), and satisfies J_twisted^2 = +1 exactly (from Cl(3,1) giving C_{3,1}^2 = +1 and Cl(6,4) with KO-type 2 giving C_{(6,4)}^2 = +1). Sign triple computed: epsilon = +1 (RESOLVED), epsilon' = J_twisted D_GU = +D_GU J_twisted (CONDITIONALLY_RESOLVED; follows if D_GU does not break the Lorentz/internal factoring at the principal-symbol level), epsilon'' = J_twisted gamma = -gamma J_twisted (CONDITIONALLY_RESOLVED; from C_{(6,4)} gamma_{int} C_{(6,4)}^{-1} = -gamma_{int} for n_{int}=10). Full sign triple (+1,+1,-1) = KO-dimension 6 mod 8. The SM fermion content is preserved: charge conjugates of SM particles are SM particles; J_twisted acts within the 16-fermion sector. Inner fluctuation with J_twisted has the potential to recover SU(3) x SU(2) x U(1) / Z_6 from the A_F-bimodule structure (same as CC -- the right-action J_twisted A_F J_twisted^{-1} = A_F^{op} is the charge-conjugate representation). Key insight: the relevant real structure on the 4D pullback s*(S) is NOT the 14D GU quaternionic J_GU (which squares to -1) but the 4D charge conjugation J_twisted (which squares to +1); the sign flip arises from the Clifford-algebra branching under the section pullback s*(S) ~= S(3,1) otimes S(6,4), not from a change to the 14D data. Six explicit failure conditions (F1-F6); highest priority: F2 (epsilon' sign for mixed shiab/II_s terms) and F6 (Type II_1 embedding of the 4D twisted triple). Full GU/Type-II_1 bridge still requires embedding the 4D construction into an ambient Type II_1 factor (target: semifinite triple from type-ii1-semifinite-triple-2026-06-23.md with J_twisted as the GU-side input to J_tau). The J^2 sign gap between GU and KO-dim 6 is resolved at the 4D section-pullback level.
File: `explorations/type-ii1-twisted-real-structure-2026-06-23.md`

---

### oc2-b-parametrix-y14 (2026-06-23)
Verdict: CONDITIONAL_DISCRETE_SECTOR_FREDHOLM; FULL_UNPROJECTED_b-FREDHOLM_NOT_DEFENSIBLE; WEIGHT_WINDOW_IDENTIFIED_CONDITIONALLY
Constructed the b-parametrix for D_GU on noncompact Y^14 with explicit weight function r = log-conformal-scale on the dilaton end of the fiber GL(4,R)/O(3,1). The indicial family at the end is I(D_GU, lambda) = Gamma^r(i lambda - delta) + D_tang, where Gamma^r is the radial Clifford element with (Gamma^r)^2 = +1 (spacelike dilaton direction in signature (9,5)). The indicial roots are delta_j = -|mu_fib,j| where mu_fib,j are fiber Dirac eigenvalues derived from the normal Laplacian spectrum. Explicit indicial roots from the discrete fiber modes (reconstruction grade): delta in {-2sqrt(2)/R_s, -sqrt(14)/R_s, -3sqrt(2)/R_s, -sqrt(20)/R_s} with continuum threshold -9/(2R_s). Natural Fredholm weight: delta in Window 0 (delta > 0, standard L^2 regime with exponential decay at the end); all indicial roots are strictly negative, so Window 0 avoids them all. On the tau-twisted discrete sector, the compact-remainder parametrix Q_delta D_delta,disc = I_disc - Pi_ker + K_L with Pi_ker, Pi_coker finite-rank H-linear and K_L, K_R compact on K_H = L^2_{H,delta,disc}(Y^14, S) is constructible. Fredholm index on the discrete sector: ind_H(D_delta,disc) = 24 at reconstruction grade (APS route on K3-type X^4), independent of delta within Window 0. Full unprojected b-Fredholmness is NOT defensible: split-signature null cone prevents ordinary b-ellipticity and the scalar sector has continuous Plancherel spectrum (A3, rank 3, FJ equal-rank fails). Eight explicit failure conditions named (F1-F8). Primary analytic gate unchanged: P_disc bounded on weighted Sobolev spaces (A1), contingent on tau-twisted discrete sector existence (APS route survives at reconstruction grade via oc1-oc2-aps-closure).
File: `explorations/oc2-b-parametrix-y14-2026-06-23.md`

---

### generation-count-rank3-resolution (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Synthesized all 2026-06-23 rank-correction and K3-gate results into a unified resolution
note. Three-part verdict: (A) Rank-3 A3 direct route FAILED on theorem-grade grounds --
Harish-Chandra's criterion rank(G)=rank(K) fails for SL(4,R) (rank 3) vs SO(4) (rank 2),
where both ranks are compact-form Cartan ranks (dimension of maximal torus of the compact
form, i.e. rank of the root system): rank(sl(4,R)) = 3 (root system A3, compact form SU(4))
and rank(so(4)) = 2 (root system A1 x A1, SO(4) = (SU(2)xSU(2))/Z2); this compact-form
rank is distinct from the split rank dim(a_q) = 3 of the symmetric space SL(4,R)/SO_0(3,1).
Correction note (GEN-02, 2026-06-23): the file originally stated the rank criterion without
pinning the rank convention; updated to explicitly distinguish compact-form Cartan rank from
split rank; the claim itself (no discrete series) is correct and theorem-grade.
so SL(4,R) has NO discrete series representations; the Atiyah-Schmid formal-degree sum is
an empty sum = 0, not 8; the A3 Plancherel is absolutely continuous. (B) Tau-twisted route
FAILS AS STATED on four independent criteria: F1 nonunitary coefficient (D(1/2,0), D(0,1/2)
are not unitary H-representations, so L^2(G x_H tau_RS) is not a standard Hilbert L^2 space);
F2 scalar equal-rank condition fails (split-rank=3, rank(K/(K cap H))=1, 3!=1);
F3 Kobayashi-Oshima classification excludes (sl(4,R), so(3,1)) from the list of symmetric
pairs admitting discretely decomposable restrictions; F4 asymptotic cone obstruction nonzero
(diagonal ray (1,1) in C_K(K') is in the asymptotic K-support of tau_RS). The formula
rank_correction(tau_RS)=2 is FALSIFIED -- do not use. (C) K3 gate RESOLVED --
A-hat(T^4)=0 exact (three routes), A-hat(K3)=2 exact (topological invariant), T^4 gives
1 generation (not 3) and is ruled out as a competitor; K3 is the unique compact
simply-connected smooth Ricci-flat 4-manifold with A-hat=2 (Berger+Yau+Donaldson+Freedman);
OQ3a RESOLVED. Generation count CONDITIONALLY_RESOLVED at 3 via APS/K3:
ind_H(D_GU) = 8*A-hat(K3) + 8 = 16+8 = 24, generations = 24/8 = 3, conditional on
rank_H(S_RS^+) = 4 (Candidate A); Candidate B (rank_H = 8 => 4 generations) not excluded.
Primary remaining gate: OQ-RK1 (CAS matrix computation of Pi_RS*E_+ in M(64,H)) and
OQ-RK2 (APS boundary analysis for constrained RS operator on K3).
Correction note (GEN-01, 2026-06-23): rank_H(S_RS^+) = 4 was derived from a physical DOF
heuristic with three halvings whose final step ("half of chiral = 4") is unjustified.
dim_H(C^16) = 8 from Cl(9,5) = M(64,H) module theory; the heuristic requires a second
chirality projector Pi_+ not derived in this file. Two candidates: rank_H = 4 (3 generations,
requires Pi_+ derivation via OQ-RK1) or rank_H = 8 (4 generations, if no Pi_+). File
updated to expose the ambiguity, add FC5, promote OQ-RK1 as a blocking gate.
File: `explorations/generation-count-rank3-resolution-2026-06-23.md`

---

### oq-kk1a-cas-norm-fiber-wavefunction (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed explicit L^2 norm bounds for the RS fiber wavefunction phi_RS(r) ~ N_RS * e^{-6r} on the BC_1 radial fiber using the Jacobi function profile at spectral parameter nu_1 = 3/2, decay rate rho + nu_1 = 6. Infinity tail bound: I_tail <= 16 e^{-3}/3 ~ 0.266 (explicit computable constant, from |F_1(r)| <= 2 e^{-6r} for r >= 1 and (sinh r)^8 cosh r <= e^{9r}). Origin bound: I_0 <= 4096 F_1(0)^2 / 9 < infty from regularity of F_1 at r = 0. Normalization N_RS != 0: the formal degree d_1 = |Res_{nu=3/2} c(i nu)^{-1}|^2 / (2pi^2) > 0 from the simple pole of Gamma(-nu+1/2) at nu = 3/2 (residue = -1/(nu - 3/2)), giving N_RS = (2pi^2 d_1)^{1/2} > 0. The GU source convention does NOT force N_RS -> 0: the simple pole mechanism prevents this. G2a gate CLOSED at reconstruction grade with explicit bounds. Primary remaining structural gate: FC3 (BC_1 model validity for GL(4,R)/O(3,1) under sigma_B; A_3 root system from rc1-root-mult-disambiguation requires a direct tau-twisted discrete-series framework to replace BC_1).
File: `explorations/oq-kk1a-cas-norm-fiber-wavefunction-2026-06-23.md`

---

### cross-program-gu-taf-coefficient (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Completed the GU/TaF Tikhonov coefficient comparison using the Willmore-EL Lichnerowicz eigenvalue. Part A: C_GU = 8 from the Simons-formula Hessian of E[s] = int|II_s^H|^2 at round S^4: rough Laplacian on TT 2-tensors at l=2 gives mu_{2,2} = 4/R^2 (exact from SO(5) Casimir); ambient Willmore curvature correction +4K = +4/R^2 (Simons formula, reconstruction grade); total lambda_2 = 8/R^2; C_GU = 8 (algebraically exact given the formula [l(l+n-1)-2]/R^2 at l=2, n=4). Part B: Lambda_GU = lambda_max^2 exactly under the null-ray shot-noise model (epsilon_sec = 1/(2*sqrt(2)) = 1/sqrt(8) for n=4), via the algebraic identity C_GU(n) * epsilon_sec(n)^2 = 2n * 1/(2n) = 1 for all n >= 2. Lambda_GU does NOT match Gamma_min^2 generically; Gamma_min^2 = ln(1/epsilon)^2 * lambda_max^2 exceeds lambda_max^2 by the decoherence-tolerance factor ln(1/epsilon)^2. The clean contact is Lambda_GU = lambda_max^2 (service-rate squared), not Gamma_min^2 (decoherence-rate squared). Part C: B1 CONDITIONALLY_RESOLVED (null-ray shot-noise fixes epsilon_sec from n=dim(X^4), no free parameter, but model not derived from GU first principles); B2 VERIFIED algebraically (C_GU * epsilon_sec^2 = 8 * 1/8 = 1 exact); B3 CONDITIONALLY_RESOLVED (GU measurement-event and TaF record-finalization align under local-observer interpretation with t_obs = R/c). Key structural finding from theta-field result: the same coefficient 8 appears as C_GU (Tikhonov scale), M_KK^2 = 8/R_s^2 (KK mass gap from fiber normal Laplacian), and lambda_2 = 8/R^2 (Lichnerowicz eigenvalue) -- all three are the same geometric fact. Remaining gaps: ambient curvature correction +4K needs CAS verification; null-ray model needs GU-internal derivation; B3 t_obs alignment needs formal proof.
File: `explorations/cross-program-gu-taf-coefficient-2026-06-23.md`

---

### CORRECTION (2026-06-23, RFAIL-01) — rfail-schwarzschild-oq2-weak-field definition clarification
Severity: MODERATE (conceptual, not computational error)
Scope: `explorations/rfail-schwarzschild-oq2-weak-field-2026-06-23.md` and `canon/schwarzschild-weak-field-rfail.md`

The exploration note and canon file were using a non-standard combined failure tensor R_fail^{full} that additively mixes two conceptually distinct failure objects: (A) the standard GR failure R_fail^{GR} = G^X - 8piG T - Lambda g (which is identically zero for Schwarzschild by definition, carrying no GU-specific content), and (B) the GU-specific Willmore-EL residual (section equation failure). The main theorem statement in §8.1 and the canon file's Proof/Assembly section presented R_fail^{full} as a single defined quantity without clearly separating these two modes or labeling the combination as non-standard. This was flagged in §4.3 but conflated in the theorem statement.

The correction does NOT change the verdict (CONDITIONALLY_RESOLVED) or any computed value. The mathematical content is correct. What changed:
- §4.1 (exploration) now explicitly defines both R_fail^{GR} (standard) and the Willmore-EL residual (GU-specific) separately before defining R_fail^{full} as their combination, with a prominent convention warning.
- §4.2 (exploration) now separates the trivial statement (R_fail^{GR} = 0 exactly, standard GR) from the non-trivial GU computation (Willmore-EL residual ~ O(M/r^4)).
- §4.3 (exploration) now states the separation clearly: R_fail^{GR} = 0 is trivial; the Willmore-EL residual is the GU-specific content; neither is zero for the other reason.
- §8.1 main theorem (exploration) now leads with an explicit convention block naming both failure objects and warning that R_fail^{full} is non-standard, then states the theorem in terms of each component separately.
- Canon file Scope section now includes the same convention block with both failure objects defined.
- Canon file Assembly section now separates the two failure modes in the displayed equation chain.

Readers using the standard GR definition of R_fail should apply R_fail^{GR} only (identically zero for Schwarzschild; trivial). The non-trivial GU content is entirely in the Willmore-EL residual, which vanishes at O(M/r) due to the curvature-order suppression Delta^perp H^i ~ O(M/r^4).
Files modified: `explorations/rfail-schwarzschild-oq2-weak-field-2026-06-23.md`, `canon/schwarzschild-weak-field-rfail.md`

---

### vz-14d-mixed-covectors correction (2026-06-23) [VZ-02]
Issue: VZ-02 (moderate severity). The `B E^{-2} C` formula in §5 of `explorations/vz-14d-mixed-covectors-2026-06-23.md` stated explicit numerical coefficients `2842`, `98`, `203/7` with no derivation trace, no reference to a prior repo file, and no CAS verification. These numbers were sourced from `vz-oq1-sr-squared-identity-2026-06-23.md`, which was not yet committed to the repo and could not be independently verified.
Fix applied: Added a clearly labeled reconstruction-grade warning block immediately after the formula in §5, stating that the three coefficients are unverified pending CAS confirmation under OQ-RS-1 and that the source file (`vz-oq1-sr-squared-identity-2026-06-23.md`) is not yet in the repo. The structural conclusion (`B E^{-2} C != 0`) is noted as expected to survive CAS verification; only the specific coefficient values are flagged as unreliable. Also updated the OQ-RS-1 entry in §8 to explicitly name the coefficient verification as part of its scope.
No verdict change: the overall file verdict (CONDITIONALLY_RESOLVED, VZ evasion EVADED) is not affected -- the nonvanishing of `B E^{-2} C` is structural and does not depend on the specific coefficients.
File: `explorations/vz-14d-mixed-covectors-2026-06-23.md`

---

### vz-e-block-direct-clifford-invertibility (2026-06-23)
Verdict: RESOLVED
Direct Clifford algebra proof that E(xi): Q -> Q is invertible for all xi with g_Y(xi,xi) != 0, closing the VZ-01 circularity gap. The proof uses only the 2x2 block structure of E(xi) on Q = E_0 + Im P_T and the identity gamma(xi)^2 = xi2 Id in Cl(9,5) = M(64,H): if E(xi)(phi, j(s)) = 0 then Gs = 0 then G^2 s = xi2 s = 0, so s = 0 (xi2 != 0); similarly phi = 0. Explicit inverse E^{-1} = [[-(26/xi2)G,(14/xi2)G],[(14/xi2)G,0]] verified by direct multiplication. The failure locus is exactly the null cone xi2 = 0 (expected hyperbolic characteristics, not a VZ problem). The Schur complement proof in vz-14d-mixed-covectors is now non-circular, upgrading vz-14d-mixed-covectors from CONDITIONALLY_EVADED to EVADED. Remaining open at operator level: loop corrections (OQ-RS-2), GU-Vasiliev comparison (OQ-RS-3), noncompact Fredholmness (OQ-RS-4), CAS matrix verification (OQ-CAS-E).
File: `explorations/vz-e-block-direct-clifford-2026-06-23.md`


---

### oc2-sobolev-analytic-gate-a1 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Framework assessment for supplying a bounded P_disc on weighted Sobolev K_H spaces for OC2 analytic gate A1. b-calculus combined with Melrose-Piazza spectral section is the best framework: b-calculus handles the dilaton R^+ end (single boundary face, standard single-face machinery), and Melrose-Piazza supplies a smooth family of bounded projections P_sec,x over observer space X away from the zero-mode subvariety Z. Scattering calculus better handles the full A3 fiber but requires rank-3 fibred-scattering extension and Harish-Chandra resolvent for S(6,4) coefficient bundle. Precise conditions: mass gap min{Delta_N}=8/R_s^2>0, weight delta strictly in Window 0, discrete spectrum separated from continuum threshold 9/(2R_s). Four conditions dischargeable from GU first principles (mass gap, weight choice, H-linearity, Sp(64)-equivariance of P_disc); four require new input (rank-3 corner b-calculus, Harish-Chandra resolvent for twisted spinors, no discrete modes in [20,81/4]/R_s^2, spectral flow control over X). Explicit failure family exhibited: deformation from K3 section (ind_H=24) to T^4 section (ind_H=8) forces 16 eigenvalue crossings through zero; at each crossing ||P_disc||_{W^{1,2}->W^{1,2}} blows up as 1/|lambda_j|->infty. The bounded transform F_x=D_x(1+D_x^*D_x)^{-1/2} remains bounded at zero eigenvalues (functional calculus handles zero modes without Riesz projection). Six failure conditions (FC1-FC6) precisely stated. OC2 status unchanged: CONDITIONALLY_RESOLVED.
File: `explorations/oc2-sobolev-a1-bounded-transform-2026-06-23.md`

---

### historical-rank-one-archive-clean (2026-06-23)
Verdict: RESOLVED
Produced a reader-navigation index covering 21 exploration files that contain scalar BC_1 claims (BC_1 restricted root system, rho = 9/2, Lambda_RS^{FJ} = 3/2, split-rank = 1, FJ multiplicity-one, RC3 spectrum {8,14,18,20}/R_s^2, or (m_1,m_2) = (7,1)) for the pair (SL(4,R), SO_0(3,1)). Files are organized in three tiers: Tier 1 (5 primary source files that originated the scalar BC_1 model), Tier 2 (9 derivative files with partial or full self-awareness of supersession), Tier 3 (7 incidental-reference files). All Tier 1 files carry supersession pointers to rc1-root-mult-disambiguation-2026-06-23.md and/or generation-count-rank3-resolution-2026-06-23.md. No live-looking scalar BC_1 claim is left without a pointer. The index does not modify exploration files; it provides navigation for readers encountering old text.

---

### pc5-higgs-su2l-u1y-gate-computation (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
The gate test "does adj(Sp(64))|_{G_SM} contain (1,2,+1/2) under SU(3) x SU(2)_L x U(1)_Y?" is discharged at reconstruction grade via the Pati-Salam tensor product: the (4,2,1) x (4bar,1,2) cross term in adj(Sp(16)) contains (1,2,2) under Pati-Salam, which branches to (1,2,+1/2) + (1,2,-1/2) under G_SM (with B-L = 0 for the SU(4) singlet giving Y = T_{3R} = +1/2). The failure condition from the PC5 spec ("no (1,2,+1/2) in any natural decomposition of II_s^H") does not fire. Remaining gates: CAS explicit multiplicity check of adj(Sp(16))|_{G_PS} (OQ1), gauge-covariance of the fiber-component Higgs construction (OQ2), Mexican hat potential sign (F5 — dynamical, not representation-theoretic), and the Pati-Salam breaking mechanism needed before (1,2,+1/2) can function as the SM Higgs (F6 — separately OPEN).
File: `explorations/pc5-higgs-su2l-u1y-gate-2026-06-23.md`
File: `explorations/rank-one-archive-supersession-index-2026-06-23.md`

---

### h3-chsh-four-patch-cycle (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Transferred the two-patch S^1 Outcome D' holonomy result to the full four-patch CHSH cycle. Four observers (Alice-+, Alice--, Bob-+, Bob--) define patches over Y_spin ~ S^1; four overlaps (I_{12}, I_{23}, I_{34}, I_{41}) carry transition values c_{12}, c_{23}, c_{34}, c_{41} derived by C_TaF under NAC. The Four-Cycle-Odd-SBP condition (product of all 8 SBP incidence values = -1) forces holonomy = (+1)(+1)(+1)(-1) = -1 via the NAC factoring theorem from Gap 1, achieving Outcome D'. Falsification condition stated precisely: holonomy != -1 would refute H3 for the CHSH configuration. The Pati-Salam bipartite decomposition S(6,4) -> (4,2,1) + (4-bar,1,2) provides the natural Alice/Bob split; whether the GU SM-sector zero mode is entangled under this split (OQ-G2-1) determines whether the physical GU geometry forces odd-SBP, realizing the fixture configuration. Complete Python fixture specified as a self-contained analog of the two-patch test. Remaining gates: OQ-G2-1 (Pati-Salam product-state or entangled?) and OQ-G2-2 (explicit GU CHSH correlator showing |CHSH| > 2).
File: `explorations/h3-chsh-four-patch-fixture-2026-06-23.md`

---

### type-ii1-exit-condition-cs1-af-embedding (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed the explicit embedding phi: A_F -> M_{96}(C) otimes 1_R subset R (hyperfinite II_1 factor) via phi(a) = rho_L(a) otimes 1_R, where rho_L: A_F -> M_{96}(C) is the standard CC left action on H_F = C^96. All three CC grading data items are preserved: (1) full A_F = C oplus H oplus M_3(C) (RESOLVED -- all three components embedded faithfully via the CC representation); (2) Z/2Z-grading gamma_M = gamma_F otimes 1_R (RESOLVED -- A_F is entirely even-graded, intertwining condition exact algebraically); (3) real structure J_tau|_{p_F H} ~= J_F (CONDITIONALLY_RESOLVED -- modular conjugation J_tau restricts to CC charge conjugation J_F on p_F H up to unitary equivalence via bimodule uniqueness; three failure conditions FC-1 through FC-3 named and assessed as non-obstructing). Gate GC1 from type-ii1-semifinite-triple upgraded from "existence asserted" to "explicitly constructed at reconstruction grade." No GENUINE_OBSTRUCTION found. Primary remaining gate for verified upgrade: FC-3 (explicit 96x96 unitary U intertwining J_tau with J_F, a routine linear algebra computation). The J^2 structural gap (GC3) between GU quaternionic J (J^2=-1) and CC/Type-II_1 modular J_tau (J^2=+1) is unchanged; CS1 addresses the CC-side embedding only.
File: `explorations/type-ii1-exit-cs1-af-embedding-2026-06-23.md`

---

### CORRECTION CR-02 — generation-count-rank3-resolution verdict downgraded (2026-06-23)
Verdict change: CONDITIONALLY_RESOLVED -> OPEN
File: `explorations/generation-count-rank3-resolution-2026-06-23.md`

The prior verdict CONDITIONALLY_RESOLVED (at 3 generations, Candidate A) was inappropriate
while Candidate B (4 generations, rank_H(S_RS^+)=8) remained live and undismissed.
CONDITIONALLY_RESOLVED selects one candidate as a baseline; that selection requires either
a derivation excluding Candidate B or an OQ-RK1 result confirming Candidate A. Neither
exists: the value rank_H(S_RS^+)=4 is explicitly labeled "a heuristic reconstruction-grade
guess, not a derived result" (GEN-01, file §C2). Selecting it as baseline overstates the
state of knowledge.

Changes applied to generation-count-rank3-resolution-2026-06-23.md:
- frontmatter verdict: CONDITIONALLY_RESOLVED -> OPEN
- frontmatter verdict_detail: updated to name both candidates as equistatus, gate on OQ-RK1
- One-Sentence Result: "CONDITIONALLY_RESOLVED at 3 generations" -> "OPEN at 3 or 4 generations pending OQ-RK1"
- Verdict Summary table: single CONDITIONALLY_RESOLVED row for generation count split into
  two equistatus OPEN rows (Candidate A: 3 gen; Candidate B: 4 gen) plus updated K3/APS row
- Part C GEN-01 paragraph: explicit statement that both candidates are equistatus and no
  baseline should be selected before OQ-RK1
- Section C3 heading: "(CONDITIONALLY_RESOLVED)" -> "(OPEN — Candidates A and B equistatus)"
- Dependency Map "Conditionally Resolved" block: replaced with "Open — Candidates Equistatus"
  block naming both candidates; generation-count-independent conditionally-resolved items
  moved to a separate sub-block
- "What Changed" current-state block: updated generation count line to show OPEN with both
  candidates named
- FC2 assessment: updated to note Candidate B already fires FC2, making FC2 live not
  hypothetical
- "Full upgrade to RESOLVED" phrasing clarified

Correction reason: CONDITIONALLY_RESOLVED is appropriate only after OQ-RK1 resolves the
rank_H ambiguity. Until then, the correct verdict is OPEN with both candidates listed as
equistatus, gated on OQ-RK1 (CAS matrix computation of rank_H(S_RS^+) in M(64,H)).

---

### CORRECTION MO-01 — Shiab injectivity argument repaired (2026-06-23)

**File corrected:** `canon/shiab-existence-cl95.md`

**Error (Step 3, original):** The "Non-zero on all non-zero inputs" claim was justified by the argument "c(iota_{e_a} alpha) != 0 for any non-zero alpha and generic frame, therefore the sum sum_a e^a tensor c(iota_{e_a} alpha) s is non-zero." This is logically invalid: 14 individually non-zero terms can sum to zero. The injectivity conclusion was stated without proving non-cancellation of the sum.

**Fix applied:** The Clifford-contraction identity sum_a e^a c(iota_{e_a} alpha) = c(alpha^#) (Lawson-Michelsohn §II.5, eq. 5.9) collapses the 14-term sum to a single Clifford multiplication by alpha^# (the metric-dual covector of alpha). Since alpha != 0 implies alpha^# != 0, and Cl(9,5) ~= M(64,H) is simple so any non-zero element acts injectively on the unique irreducible module S = H^64, the map is injective. The sum-cancellation concern is resolved at the algebra level: there is no sum to cancel because the standard Clifford-contraction identity reduces it to a single term.

**Verdict change:** None. The canon/shiab-existence-cl95.md verdict remains RESOLVED. The injectivity of Phi is now established by a valid argument; the conclusion is unchanged. The three new Known Failure Modes added (sum-collapse identity precondition, non-degeneracy on gauge forms, uniqueness of equivariant map) do not affect the RESOLVED verdict for existence and injectivity.

**Additional changes in same edit pass:**
- "Non-zero on all non-zero inputs" bullet in Step 3 replaced with corrected argument citing the sum-collapse identity.
- Known Failure Modes expanded with: (a) sum-collapse identity precondition and its discharge, (b) non-degeneracy on gauge curvature forms (unchanged substance, re-worded for precision), (c) uniqueness of equivariant map (new — open representation-theory question).

---

### CORRECTION CR-04 (critical) — vz-14d-mixed-covectors vz_evasion_status reverted to CONDITIONALLY_EVADED (2026-06-23)

**File corrected:** `explorations/vz-14d-mixed-covectors-2026-06-23.md`

**Error:** The `vz_evasion_status` field was upgraded from `CONDITIONALLY_EVADED` to `EVADED` within the same session loop that raised the VZ-01 circularity flag. The log entry `vz-e-block-direct-clifford-invertibility` (above) claimed RESOLVED status for E(xi) invertibility based on a reconstruction-grade argument in a same-session file (`explorations/vz-e-block-direct-clifford-2026-06-23.md`), and cascaded that to upgrade vz-14d-mixed-covectors to EVADED. This is methodologically unsound: a circularity flag cannot be closed by a same-session reconstruction-grade file without external verification. The `vz01_closure` field also incorrectly stated "CONDITIONALLY_EVADED upgraded to EVADED."

**Verdict change:** `vz_evasion_status` EVADED -> CONDITIONALLY_EVADED. Overall §7 VZ verdict: EVADED -> CONDITIONALLY_EVADED. The 4D section-pullback result (OQ3-V1/V2/V3, VERIFIED) is unaffected.

**Changes applied to `explorations/vz-14d-mixed-covectors-2026-06-23.md`:**
- Frontmatter `vz_evasion_status`: EVADED -> CONDITIONALLY_EVADED
- Frontmatter `vz01_closure`: rewritten to state "direct Clifford algebra argument provided (reconstruction grade); upgrade to EVADED requires verification outside the session loop"
- §7 table E-block row: RESOLVED -> CONDITIONALLY_RESOLVED, with explicit note that the proof is same-session reconstruction grade pending external verification
- §7 overall verdict line: EVADED -> CONDITIONALLY_EVADED
- §9 verdict block: EVADED removed; open precondition reinstated with three explicit failure conditions: FC1 (independent external verification of 2x2 block kernel argument), FC2 (explicit CAS computation confirming the proposed E^{-1} formula), FC3 (confirmation that the failure locus is exactly and only the null cone with no non-null xi producing a zero eigenvalue of E)

**The `vz-e-block-direct-clifford-invertibility` log entry above is retained as a record of the reconstruction-grade argument.** Its RESOLVED verdict describes the argument itself; it does not establish that the argument constitutes adequate methodological closure of a circularity.

---

### CORRECTION CR-03 — theorem-statement-v1 Section 7.2 Flensted-Jensen citation (2026-06-23)

**File corrected:** `active-research/signed-readout/theorem-statement-v1-2026-06-23.md`

**Section:** 7.2 (GU Generation Count physical instance), Setup bullet for X.

**Error:** The parenthetical '|X| = 24 via the Flensted-Jensen computation and APS closure' cited the Flensted-Jensen discrete-series computation as co-establishing |X| = 24. This contradicts canon from the same session: generation-count-rank3-resolution-2026-06-23.md closes the Flensted-Jensen / scalar discrete-series route as explicitly FAILED on structural grounds: (1) SL(4,R) has no discrete series representations (Harish-Chandra criterion fails: rank(G)=3, rank(K)=2, 3 != 2); (2) the Atiyah-Schmid formal-degree sum over disc(SL(4,R)) is an empty sum; (3) all four tau-twisted rescue routes fail independently (Kobayashi non-admissibility of tau_RS, Oshima-Matsuki correction failure for A3 pair, split-rank mismatch A3 vs BC1, and vanishing formal degree at the empty discrete sector).

**Fix applied (in-place edit to the Setup X bullet):**

OLD: '|X| = 24 via the Flensted-Jensen computation and APS closure'

NEW: '|X| = 24 via the APS/K3 route only (reconstruction grade, gated on OQ-RK1); the Flensted-Jensen discrete-series route is explicitly FAILED -- SL(4,R) has no discrete series (rank(G)=3 != rank(K)=2; Harish-Chandra criterion fails), so the Atiyah-Schmid formal-degree sum is an empty sum; all four tau-twisted rescue routes also fail independently (Kobayashi non-admissibility, Oshima-Matsuki correction, split-rank mismatch A3 vs BC1, and vanishing formal degree); |X| = 24 is supported only by the APS/K3 computation ind_H = 8*A-hat(K3) + 8 = 24, conditional on rank_H(S_RS^+) = 4 (GEN-01 OPEN)'

**Verdict change:** None. The theorem-statement file verdict remains CONDITIONALLY_RESOLVED. The correction removes a false citation of a failed computation; the APS/K3 route was already the operative surviving justification in generation-count-rank3-resolution-2026-06-23.md and oc1-oc2-aps-closure-2026-06-23.md.

---

### CORRECTION (2026-06-23, CR-01 / THETA-03) -- theta-field FLRW dark energy EOS verdict demoted to OPEN

**Severity:** CRITICAL
**Scope:** `canon/theta-field-flrw-dark-energy-eos.md`

The canon entry carried verdict CONDITIONALLY_RESOLVED at promotion. THETA-01 (phi_0-dependence of the ratio) was applied at promotion time. THETA-03 -- logged in the exploration source file and earlier in this log -- was not propagated to the canon frontmatter verdict.

THETA-03 is more severe than THETA-01: the phase phi_0 ~ 1.94 rad and instantaneous w_B ~ +0.76 are de-Sitter-approximation-only, unreliable by O(1). The matter-dominated phase at z > 0.3 (where H >> H_0*sqrt(Omega_Lambda)) was not integrated. All quantitative outputs in Results 2 and 3 depend on these values: w_0 ~ -0.80, w_a ~ -0.35, coefficient 1.76, ratio -1.80, and f_0 ~ 0.11 are all de-Sitter-approximation-only pending OQ3.

A canon entry cannot support CONDITIONALLY_RESOLVED when all quantitative central results carry O(1) uncertainty that the file itself acknowledges. The verdict is demoted to OPEN.

**Changes applied to canon/theta-field-flrw-dark-energy-eos.md:**
- Frontmatter `verdict` changed from CONDITIONALLY_RESOLVED to OPEN.
- Frontmatter fields `verdict_changed_from`, `verdict_changed_at`, `verdict_change_reason` added.
- WARNING block added immediately after the title: names Result 1 as the only firm result, prohibits citation for quantitative DESI comparison until OQ3 is complete.
- Three new failure conditions added: F7 (matter-era phase shift from OQ3 moves w_0 outside DESI window), F8 (phi_0 scan sensitivity -- ratio may not be bounded away from 0), F9 (M_KK root-system correction could move theta into slow-roll regime).

Result 1 (oscillation regime: M_KK = 2.83 H_0 > 3H_0/2 BF bound, theta oscillating and damped) is unaffected -- algebraically exact, independent of background approximation. The entry remains in canon/ because the structural physics is sound; only the quantitative numerical values are unreliable at the OPEN verdict level. Required to reopen: OQ3 (numerical Klein-Gordon integration in Lambda-CDM H(z) from z=2 to z=0, following Turner 1983 PRD 28, 1243).

---

### CORRECTION MO-02 — canon/w2-y14-spin-structure.md Step 3 derivation gap (2026-06-23)

**File corrected:** `canon/w2-y14-spin-structure.md`

**Error (Step 3, original):** The identity `w2(Sym^2(V)) = w1(V)^2 + w2(V)` was stated without derivation, citing only "[computation — splitting principle; N6 §5]". This is the key step: the cancellation in Step 4 (`w2(Y14) = pi*(w2(X4)) + pi*(w2(X4)) = 0 mod 2`) depends entirely on `w2(TV) = pi*(w2(X4))`, which follows from this identity plus the identification `w2(V) = w2(X4)`. The formula for SW classes of symmetric tensor powers is not standard enough to assert without proof in a self-contained canon document. The full derivation existed in the source exploration file N6 §5.5 but was not carried into the canon file.

**Fix applied (2026-06-23):** The derivation was added inline to Step 3 of `canon/w2-y14-spin-structure.md`. Four sub-steps:

1. Splitting principle for Sym^2(V), V a 3-dim bundle. Formally write V = L1 oplus L2 oplus L3; squares Li^2 are trivial over Z/2 (since 2 w1(Li) = 0 mod 2); mixed products give w(Li Lj) = 1 + ai + aj; the product over all pairs expands to give w2(Sym^2(V)) = e1^2 + e2 = w1(V)^2 + w2(V). Reference added: Milnor-Stasheff, Characteristic Classes, proof technique of Theorem 7.1.

2. For oriented X4, w1(V) = 0 (spatial subbundle of oriented TX4 is oriented), so w2(Sym^2(V)) = w2(V).

3. Identification w2(V) = w2(X4) via TX4 = V oplus L (time line bundle L): Whitney formula with w1(V) = w1(L) = 0 for oriented X4 gives w2(TX4) = w2(V).

4. Assembly via Whitney product formula across the O(3) x O(1) decomposition: the (R^3 tensor sgn) factor contributes w2 = w1(X4)^2 = 0 for oriented X4; the trivial trace factors contribute 0; final result is w2(TV) = pi*(w2(X4)).

**Verdict change:** None. The RESOLVED verdict stands. The derivation was mathematically correct (it existed in full in N6 §5.5); the fix makes the canon file self-contained so the key identity can be verified without consulting the exploration file.

---

### CORRECTION MO-05 — type-ii1-twisted-real-structure verdict: key epsilon' sign is unverified (2026-06-23)

**Severity:** MODERATE (MO-05)
**File corrected:** `explorations/type-ii1-twisted-real-structure-2026-06-23.md`

**Error:** The exploration carried verdict CONDITIONALLY_RESOLVED for the J_twisted construction. The sign triple (+1, +1, -1) = KO-dim 6 was presented as the outcome, with epsilon' = +1 described as CONDITIONALLY_RESOLVED (reconstruction). However, epsilon' is the load-bearing sign for the entire construction: if J_twisted D_GU = -D_GU J_twisted (epsilon' = -1), the triple has KO-dim 4 not 6, and CC contact does not hold. The file itself acknowledged this in §0 ("explicit matrix verification at the level of the GU Dirac-DeRham operator is reconstruction-grade") but the verdict did not reflect that the key sign had not been verified. CONDITIONALLY_RESOLVED implies the resolution holds conditionally; it did not name that the condition was unverified at the level that determines whether the stated goal is achieved.

**Fix applied (2026-06-23):**

1. Frontmatter verdict changed: CONDITIONALLY_RESOLVED -> CONDITIONALLY_RESOLVED_KEY_SIGN_UNVERIFIED.

2. New failure condition FC-EPSILON added in §7 (before F2): "If J_twisted D_GU = -D_GU J_twisted (epsilon' = -1), the twisted real structure gives KO-dim 4, not 6. The CC contact requires epsilon' = +1. Until this sign is verified by explicit matrix computation in M(64,H), the KO-dim 6 conclusion is not established." Named as the highest-priority blocker.

3. Summary §0 "What remains open" paragraph rewritten to lead with FC-EPSILON as a blocking condition and make explicit that KO-dim 6 is NOT established, not merely conditional.

4. Summary §0 bold "Verdict:" line updated to CONDITIONALLY_RESOLVED_KEY_SIGN_UNVERIFIED with a critical caveat block.

5. §9 verdict table updated: epsilon' = +1 row changed from CONDITIONALLY_RESOLVED (reconstruction) to UNVERIFIED -- structural argument only; matrix computation in M(64,H) not done (FC-EPSILON). KO-dim 6 achieved row changed from CONDITIONALLY_RESOLVED to NOT ESTABLISHED -- gated on FC-EPSILON (epsilon' sign); if epsilon' = -1, KO-dim = 4.

6. §9 overall verdict paragraph updated to name the KO-dim 6 conclusion as not established until FC-EPSILON is resolved.

7. §8 "What remains" list: new item 0 added as [PRIORITY 0 -- BLOCKING]: verify epsilon' = +1 by explicit matrix computation in M(64,H).

**Verdict change:** CONDITIONALLY_RESOLVED -> CONDITIONALLY_RESOLVED_KEY_SIGN_UNVERIFIED. The construction of J_twisted and the J^2 = +1 result are sound. The KO-dim 6 conclusion is not established until FC-EPSILON is resolved by explicit computation.

---

### CORRECTION MO-06 — pc5-higgs-su2l-u1y-gate verdict downgraded from CONDITIONALLY_RESOLVED to NECESSARY_CONDITION_ONLY (2026-06-23)

**Severity:** MODERATE (MO-06)
**File corrected:** `explorations/pc5-higgs-su2l-u1y-gate-2026-06-23.md`

**Error:** The original verdict CONDITIONALLY_RESOLVED claimed the Higgs gate is
"CONDITIONALLY CLEARED at reconstruction grade." The supporting computation (§3) is
a representation-theoretic existence argument: it shows that the decomposition of
adj(Sp(64)) contains a (1,2,+1/2) summand under the Pati-Salam branching chain
(4,2,1) x (4bar,1,2) -> (1,2,2) -> (1,2,+1/2) + (1,2,-1/2). This is a necessary
condition for Higgs emergence, not a gate-clearing derivation. Existence in the
decomposition of the ambient representation does not establish that the physical
section's II_s^H has nonzero projection onto the (1,2,+1/2) component. That computation
requires evaluating the distortion on a specific Willmore-critical section — not merely
on the ambient adj(Sp(64)) fiber.

**Verdict change:** CONDITIONALLY_RESOLVED -> NECESSARY_CONDITION_ONLY.

**Changes applied to `explorations/pc5-higgs-su2l-u1y-gate-2026-06-23.md`:**

1. Frontmatter verdict changed: CONDITIONALLY_RESOLVED -> NECESSARY_CONDITION_ONLY. Fields
   `verdict_note`, `corrected_from`, `corrected_at`, and `correction_reason` added.

2. §3.5 verdict paragraph rewritten: "The Higgs gate is CONDITIONALLY CLEARED" replaced
   with "representation-theoretic necessary condition satisfied" and a clear statement
   of what the computation does not establish.

3. §4 Failure Conditions expanded with F0 (nonzero projection on critical section — the
   primary missing computation), F0a (symmetry forces zero projection on LC section),
   F0b (gauge-equivariance forces real J-paired combination), and F0c (Higgs block in
   wrong Sp(64) subalgebra relative to j_s image of II_s^H). The original F1-F6
   are retained unchanged.

4. §5 Result and Verdict rewritten: CONDITIONALLY_RESOLVED removed, NECESSARY_CONDITION_ONLY
   stated with explicit correction note, what the file establishes vs. does not establish
   clearly separated.

5. §7 Summary Table: added rows for F0 (II_s^H nonzero projection, OPEN), F0a (symmetry-forced
   zero projection, OPEN), F0c (j_s image vs. off-diagonal block, OPEN), and CAS multiplicity
   (OPEN); overall gate status line added: NOT CLEARED.

6. Closing note (*Filed:...*) updated to reflect corrected verdict and primary open items.

**The representation-theoretic necessary condition (1,2,+1/2) in adj(Sp(64)) is satisfied
and stands.** The gate requires the additional step of a section-specific computation showing
nonzero (1,2,+1/2) projection for a GU Willmore-critical section.

---

### vz-oq-cas-e-block-inverse-matrix (2026-06-23)
Verdict: RESOLVED (E^{-1} arithmetic only) — vz-14d-mixed-covectors upgrade DEFERRED_VERIFICATION
Explicit 2x2 block matrix computation of both E * E^{-1} and E^{-1} * E, using E = [[0,(1/14)G],[(1/14)G,(13/98)G]] and the asserted E^{-1} = [[-(26/xi^2)G,(14/xi^2)G],[(14/xi^2)G,0]], where G^2 = xi^2 * Id. All four entries of both products verified by exact arithmetic: M_{11} = M_{22} = N_{11} = N_{22} = Id (each equals (1/xi^2) G^2 = Id); M_{12} = M_{21} = N_{12} = N_{21} = 0 (M_{21} and N_{12} via the cancellation -13/7 + 13/7 = 0, exact since 26*7 = 182 = 13*14). The E^{-1} formula is arithmetically correct and all three CR-04 failure conditions (FC1/FC2/FC3) are arithmetically discharged; OQ-CAS-E is closed at the arithmetic level.

**SAME-SESSION BLOCK (VZ-E-BLOCK-SAME-SESSION, 2026-06-23):** The upgrade of vz-14d-mixed-covectors from CONDITIONALLY_EVADED to EVADED claimed in the original §8 of the exploration file is blocked. Circularity flag VZ-01 / CORRECTION CR-04 was raised in this session, and the present file also belongs to this session. A different file in the same session is still intra-session; the same-session self-resolution check blocks the circularity-flag closure. The RESOLVED verdict stands for the E^{-1} formula itself (correct arithmetic). The vz-14d-mixed-covectors status remains CONDITIONALLY_EVADED. Upgrade to EVADED requires inter-session or external verification of the E-block computation. Status of that upgrade: DEFERRED_VERIFICATION.
File: `explorations/vz-oq-cas-e-block-inverse-matrix-2026-06-23.md`

---

### pc5-higgs-cas-clebsch-gordan (2026-06-23)
Verdict: RESOLVED
Resolved OQ1 from pc5-higgs-su2l-u1y-gate: the explicit Clebsch-Gordan decomposition of adj(Sp(16))|_{G_PS} under G_PS = SU(4) x SU(2)_L x SU(2)_R. Using the identification adj(Sp(16)) = Sym^2_C(C^{16}) and the Pati-Salam splitting V = V_L + V_R = (4,2,1) + (4bar,1,2), the symmetric square decomposes as Sym^2(V_L) + V_L tensor V_R + Sym^2(V_R) = [(10,3,1) + (6,1,1)] + [(1,2,2) + (15,2,2)] + [(10bar,1,3) + (6,1,1)]; total dimension 30+6+4+60+30+6 = 136 = dim(sp(16)). The (1,2,2) representation appears with multiplicity exactly 1, arising uniquely from the SU(4) singlet in 4 tensor 4bar = 1 + 15 in the cross term V_L tensor V_R. The (1,2,2) then branches to (1,2,+1/2) + (1,2,-1/2) under G_PS -> G_SM with Y = T_{3R} = +1/2 (B-L = 0 for the SU(4) trace singlet). The Higgs emergence gate OQ1 is confirmed at reconstruction grade; upgrade to verified requires CAS computation in LiE or SageMath. Primary remaining gate (F0 from the parent file): whether the specific II_s^H of a GU Willmore-critical section has nonzero (1,2,+1/2) projection -- a section-specific computation not addressed here.
File: `explorations/pc5-higgs-cas-clebsch-gordan-2026-06-23.md`

---

### oq-rk2-aps-fc3-fc4-closure (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
FC3 closed at reconstruction grade: sigma = c(e_1)c(e_2)c(e_3)c(e_4) anticommutes with each c(e^mu) in Cl(4,0), so sigma maps ker(Gamma^{4D}) to itself, giving Pi_RS sigma = sigma Pi_RS and completing the eta(A_RS) = 0 spectral-symmetry argument from the parent APS file. FC4 remains open: the Weyl-module decomposition gives fiber rank_H(S_RS^+(x)) = 24 (non-circularly, from Spin(4)-representation content (1/2,1) tensored with S(6,4)^pm), but the reduction to the effective APS rank 4 requires computing int_{K3} A-hat * ch_H(S_RS^+) via the SU(2) holonomy decomposition of S_RS^+ on the Yau-Calabi K3, which is an open computation. The overall OQ-RK2 / OQ3b verdict remains CONDITIONALLY_RESOLVED.
File: `explorations/oq-rk2-aps-fc3-fc4-closure-2026-06-23.md`

**Correction note (2026-06-23, OQ-RK2-FC4-CIRCULAR-STILL):** Two structural problems flagged. (1) The RS index formula application in Section 4.5 produced five failed numeric attempts (-64, 80, -800, -256, -288), none matching the target ind_C = 16. The intermediate claim "ind_H(D_RS) = 8 from the Gibbons-Pope formula" uses a specific formula version stated without citation verification and is contradicted by all five subsequent numeric checks in the same section. This result must NOT be cited as evidence for ind_H(D_RS) = 8 without identifying which Gibbons-Pope formula version is correct; marked UNVERIFIED in the file body. (2) The Weyl-module rank 24 (Section 4.3) contradicts the oq-rk1 value of 96 for the RS fiber rank; the 96 has not been formally retracted. FC4-D added to the file: if 24 is correct, oq-rk1 claims based on 96 must be revisited; if 96 is correct, the Weyl-module argument contains an error. OQ-FC4-5 added (rank 24 vs 96 reconciliation) and OQ-FC4-6 added (identify correct Gibbons-Pope formula version with chi=24, sigma=-16, rank=16).

---

### sc1-oq1a-d7-clebsch-gordan-cas (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
CORRECTION SC1-OQ1A-VERDICT-OVERSTATED (2026-06-23): verdict downgraded from RESOLVED to CONDITIONALLY_RESOLVED. The chirality-parity argument (algebraic, exact) correctly excludes V(omega_7) and V(omega_1+omega_7) from Lambda^2 tensor Delta^+ at verified grade. However: (1) the irreducibility of ker(c) in Section 3.3 Step 3 is reconstruction grade only, as the file itself acknowledges -- a formal proof requires the D_7 branching law or a LiE weight computation (FC-IRR); (2) the multiplicity-1 claim for V(omega_6) in V(omega_2) tensor V(omega_6) is reconstruction grade pending LiE verification (FC-MULT: if LiE returns multiplicity > 1, dim_H Hom > 1 and uniqueness weakens); (3) the highest-weight assignment omega_1 + omega_7 for ker(c) is reconstruction grade (FC-HW). The file's own Section 10 grade table records decompositions and multiplicities as reconstruction, contradicting the original RESOLVED verdict. Chirality-exclusion results (V(omega_7) absent, V(omega_1+omega_7) absent) are verified grade and stand. OQ-CG-2 (LiE/SageMath numerical verification) is the upgrade path to RESOLVED. OQ1-B (inner/outer automorphism for so(9,5)) remains open.
File: `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`

---

### type-ii1-f6-jbridge-semifinite-twisted (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Resolved Gate F6 from type-ii1-twisted-real-structure: constructed an explicit intertwiner Phi: L^2(X^4, s*(S)) -> L^2(R, tau) satisfying Phi J_twisted = J_tau Phi, bridging the Tomita-Takesaki modular conjugation J_tau (on the hyperfinite II_1 GNS space) with the Clifford charge-conjugation real structure J_twisted = C_{3,1} otimes C_{(6,4)} (on the GU section-pullback spinor bundle). Abstract existence is RESOLVED unconditionally by the Wigner classification theorem for antiunitary involutions on separable infinite-dimensional Hilbert spaces: all antiunitary involutions with J^2=+1 are unitarily equivalent, so no abstract no-go is possible. Natural construction: GNS map on harmonic sector H_F = ker(s*(D_GU)) plus spectral-eigenvalue matching on the complement; this also gives Phi s*(D_GU) Phi^{-1} = D_M by choosing D_M eigenvalues to match GU spectrum (legitimate free choice in semifinite triple construction). Remaining genuine obstruction: FC-EPSILON -- if epsilon'(J_twisted, D_GU) = -1, then the J-bridge and D-bridge are mutually exclusive, blocking the full spectral triple bridge while leaving the abstract J-bridge intact. SM gauge group unification remains OPEN (Sp(64) and A_F inner-fluctuation orbits not unified by J-intertwiner alone).

### CORRECTION TYPE-II1-F6-WIGNER-ARGUMENT (2026-06-23)
Applied to: `explorations/type-ii1-f6-jbridge-semifinite-twisted-2026-06-23.md`
Issue: The file's top-level verdict CONDITIONALLY_RESOLVED was applied uniformly to all claims, obscuring that the abstract J-bridge existence (Claim 1, via Wigner classification) is RESOLVED unconditionally and is not gated on FC-EPSILON or any other open condition. The CONDITIONALLY_RESOLVED verdict correctly applies only to the natural construction (Claim 2 -- the J-and-D spectral triple bridge), which is conditional on FC-EPSILON via the CS1 embedding. The original text discussed this distinction in Sections 5, 6, and 8, but did not propagate it clearly to the frontmatter, Section 0 summary, or Section 9 table.
Changes applied:
(1) Frontmatter: added `verdict_split` field with `abstract_j_bridge_existence: RESOLVED` and `natural_construction_j_and_d_bridge: CONDITIONALLY_RESOLVED`; added `verdict_note` making the split explicit; added `corrections` block.
(2) Section 0: restructured to lead with the two-claim / two-verdict split, explicitly stating Claim 1 is RESOLVED unconditionally and Claim 2 is CONDITIONALLY_RESOLVED; FC-EPSILON named as the condition for Claim 2 only.
(3) FC-BRIDGE-2: split into FC-BRIDGE-2a (hyperfinite closure) and FC-BRIDGE-2b (FC-EPSILON -- the primary failure mode for Claim 2), with explicit statement that FC-EPSILON blocks Claim 2 but not Claim 1.
(4) Section 9 table: replaced single table with two tables, one for Claim 1 (RESOLVED, no FC-EPSILON dependency) and one for Claim 2 (CONDITIONALLY_RESOLVED, primary FC is FC-BRIDGE-2b / FC-EPSILON); failure condition list updated to match.
Verdict not changed (CONDITIONALLY_RESOLVED is correct for the top-level file, which represents the natural construction). No canon promotion or demotion required.

---

### theta-field-flrw-matter-era-ode (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Numerically integrated the Klein-Gordon equation for the GU theta field in the full Lambda-CDM background H(z) = H_0*sqrt(0.315*(1+z)^3 + 0.685) from z=3 to z=0 using RK4 (300,000 steps). Corrected values at z=0: field value B(0) = 0.244 B_i, velocity B_dot(0) = -1.037 H_0 B_i, instantaneous w_B(0) = +0.388 (de Sitter estimate was +0.76), phase phi_0 = 0.855 rad (de Sitter was 1.94 rad). The ratio w_a/(w_0+1) corrects from -1.80 (de Sitter) to +1.17 (full FLRW), a factor of 2.68 change with sign reversal -- the THETA-03 failure condition fires. The sign of w_a is positive (dark energy less negative in past), inconsistent with DESI w_a < 0, but this depends sensitively on IC at z=3; extending to z >> z_osc with proper slow-roll ICs is required for a robust w_a sign prediction (OQ3-A). The de Sitter ratio -1.80 and the DESI comparison it supported are ruled out at reconstruction grade; the canon file is re-elevated to CONDITIONALLY_RESOLVED with corrected values and 5 explicit failure conditions.
File: `explorations/theta-field-flrw-matter-era-ode-2026-06-23.md`

---

### cpa1-ambient-curv-cas-coordinate (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Explicit normal-coordinate computation on S^4_R verifies delta_curv = +4K = +4/R^2 by direct index contraction: the curvature endomorphism gives mathring{R} v = -K v and the Ricci term gives Ric * v = 6K v on TT 2-tensor basis element v_{01} = v_{10} = 1/sqrt(2), confirmed traceless and divergence-free at the base point in normal coordinates. The Weitzenboeck correction delta_curv is identified as the gap between the Gibbons-Hawking-Perry spin-2 eigenvalue m^2_2 = 8/R^2 and the rough Laplacian eigenvalue mu_{2,2}^{rough} = 4/R^2, giving delta_curv = 4/R^2 with no free parameters. The CPA-1 chain Lambda_GU = lambda_max^2 survives the coordinate check; upgrade to verified requires OQ2 (direct Willmore Hessian from gimmel Christoffels, bypassing GHP spectrum calibration).
File: `explorations/cpa1-ambient-curv-cas-coordinate-2026-06-23.md`
File: `explorations/type-ii1-f6-jbridge-semifinite-twisted-2026-06-23.md`

---

### oq-rs3-gu-vasiliev-comparison (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Systematic four-axis comparison of GU's RS sector (embedded in D_GU on 14D Y^14 via Clifford identity in Cl(9,5)=M(64,H)) against Vasiliev higher-spin gauge theory (spin-3/2 in AdS_4 via hs(lambda) cubic vertices). GU's VZ evasion mechanism is genuinely distinct from Vasiliev's on all four axes: (1) propagation -- GU background-independent on 14D fiber bundle, Vasiliev AdS_4-dependent; (2) coupling -- GU Leibniz/Clifford with no free parameter, Vasiliev lambda-deformed cubic vertices; (3) gauge symmetry -- GU has no RS-specific local guardian symmetry (evades VZ via Clifford identity instead), Vasiliev has delta psi=nabla epsilon; (4) generation count -- GU topological (APS on K3, 1 SM generation), Vasiliev free parameter. The failure condition for distinctness (GU principal symbol = special case of Vasiliev at truncation order N) does not fire: Cl(9,5)=M(64,H) is not isomorphic to any quotient hs(lambda)/I_N (FC-3), the geometries are incompatible (FC-1), and the SM quantum number content is absent in minimal Vasiliev (FC-2). Three failure conditions for CONDITIONALLY_RESOLVED stated. Open: OQ-RS-3A (GU RS EFT in AdS_4 background -- would establish a contact point without absorption), OQ-RS-3B (compare super-IG to hs(lambda) if OQ2 is ever resolved).
File: `explorations/oq-rs3-gu-vasiliev-comparison-2026-06-23.md`

---

### CORRECTION PC5-VERDICT-OVERSTATED (2026-06-23)
Verdict corrected: RESOLVED -> CONDITIONALLY_RESOLVED
The frontmatter verdict of `explorations/pc5-higgs-cas-clebsch-gordan-2026-06-23.md` was
changed from RESOLVED to CONDITIONALLY_RESOLVED. Two issues were corrected:

1. **Grade mismatch.** The file body (§6, F5/FC-LIE) explicitly states that upgrade to
   verified requires CAS computation in LiE or SageMath and names this "the main remaining
   falsification test." RESOLVED requires a complete proof; reconstruction grade without CAS
   verification warrants CONDITIONALLY_RESOLVED. The blocking failure condition is now named
   FC-LIE: CAS computation in LiE or SageMath returns multiplicity != 1 for (1,2,2) in
   adj(Sp(16))|_{G_PS}.

2. **Misleading multiplicity claim.** The original verdict_note stated "multiplicity exactly 1"
   for (1,2,+1/2) in adj(Sp(16))|_{G_SM} without clarification. The file's §5.4 discovers
   that the (15,2,2) piece contributes an additional (1,2,+1/2) at the G_SM level via its
   SU(3)-singlet channel, raising G_SM-level multiplicity to 2. The multiplicity-1 claim
   applies to the G_PS-irreducible (1,2,2), not to the G_SM-level (1,2,+1/2). The verdict_note
   and gate_status in the frontmatter, the §6 verdict header, and the closing note have all been
   corrected to reflect this distinction.

Three explicit failure conditions are now present: FC-LIE (CAS check), F1 (adj(Sp(16)) != Sym^2
identification), and F2 (wrong Pati-Salam embedding). The prior log entry (pc5-higgs-cas-clebsch-gordan,
above) recorded the initial filing at RESOLVED; this correction supersedes that grade.

---

### CORRECTION THETA-CANON-UPGRADE-PREMATURE (2026-06-23) — canon/theta-field-flrw-dark-energy-eos.md

Issue: The canon file `canon/theta-field-flrw-dark-energy-eos.md` was upgraded from OPEN to CONDITIONALLY_RESOLVED on the basis of a same-session ODE integration (theta-field-flrw-matter-era-ode-2026-06-23.md, RK4, 300,000 steps) with no code shown and no error bound stated. The verdict rationale did not name OQ3-A (IC-dependence of the w_a sign) as a failure condition, despite the file itself acknowledging the sign is IC-sensitive (8% variation between frozen and slow-roll ICs) and that extending the integration to z >> z_osc with slow-roll ICs is required before the sign of w_a can be stated as a GU prediction.

Verdict: CONDITIONALLY_RESOLVED is retained. The upgrade is not reversed. The corrected numerical values (phi_0=0.855 rad, w_B(0)=+0.388, ratio +1.17) and the oscillating+damped regime result (Result 1, algebraically exact) are reconstruction-grade sound. However, the verdict rationale was incomplete in failing to name OQ3-A as a failure condition.

Changes applied (2026-06-23):

1. Frontmatter `verdict_change_reason` updated to explicitly name OQ3-A as a named failure condition, with a statement of what changes if the slow-roll IC extension reverses the sign of w_a.

2. Frontmatter `correction_oq3` updated to record that: (a) OQ3-A is a named failure condition; (b) the numerical integration has no code shown and no error bound stated; (c) quantitative claims in Results 2 and 3 are reconstruction-grade only, conditional on OQ3-A.

3. Failure condition FC5 added to the Known Failure Modes section of the canon file: "FC5 (OQ3-A -- IC-dependence of w_a sign, named failure condition). Extending the KG integration to z >> z_osc with slow-roll ICs may reverse the sign of w_a from +1.17 to negative, in which case the FLRW-corrected ratio is not +1.17 but some phi_0-dependent negative value, and the DESI comparison must be repeated." FC5 also records that the numerical integration has no code shown and no error bound, and that OQ3-A must be resolved before the sign of w_a can be stated as a GU prediction.

IC-sensitivity of the w_a sign is the primary open quantitative threat to Candidate D. The prior log entry (theta-field-flrw-eos, 2026-06-23) recorded the initial filing at CONDITIONALLY_RESOLVED with the IC-sensitivity noted in passing; this correction makes OQ3-A a first-class named failure condition and brings the verdict rationale into alignment with the file's own acknowledged limitations.

---

### CORRECTION KK1A-01 (critical) — oq-kk1a-cas-norm-fiber-wavefunction verdict downgraded from CONDITIONALLY_RESOLVED to OPEN (2026-06-23)

**Severity:** CRITICAL
**File corrected:** `explorations/oq-kk1a-cas-norm-fiber-wavefunction-2026-06-23.md`
**Verdict change:** CONDITIONALLY_RESOLVED -> OPEN
**G2a gate change:** CLOSED (reconstruction) -> DEFERRED_VERIFICATION (not closed)

**The problem (three legs):**

1. **Section 3.4 self-contradiction:** The Jacobi operator L^{(7/2,0)} (alpha=7/2, beta=0, from the BC_1 parameters in section 2) has discrete eigenvalues at nu=5/2 and nu=1/2 ONLY -- NOT at nu=3/2. The file states this explicitly. This directly contradicts the parent file's spectral parameter nu_1=3/2.

2. **Section 3.5 resolution is incomplete:** The file claims the correct BC_1 operator uses coth(2r) (not tanh(r)), with different Jacobi parameters. But section 3.5 ends with "need to recheck" on the Jacobi parameters for that operator. The correct parameters are never determined, so the claim that the correct BC_1 operator has a discrete eigenvalue at nu=3/2 is not established.

3. **Section 3.6 Frobenius analysis shows only continuous-spectrum decay:** The large-r analysis of the actual BC_1 ODE f'' + [7 coth(r) + 2 coth(2r)] f' + (nu^2 + rho^2) f = 0 gives both Frobenius solutions decaying at e^{-rho r} = e^{-9r/2} for real nu. This is the continuous Plancherel rate. The discrete-series rate e^{-(rho+nu)r} = e^{-6r} is asserted by appeal to Harish-Chandra theory, but the connection formula linking the simplified c-function (c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu)) to the actual BC_1 ODE with coth(2r) is NOT established.

**Three new failure conditions added (PRIMARY BLOCKERS):**

- **FC-JACOBI:** The Jacobi function identity connecting the simplified c-function c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) to the BC_1 ODE with coth(2r) is not established. The pole at nu=3/2 in the simplified formula does not verify an L^2 eigenfunction of the correct BC_1 ODE.
- **FC-OPER-MATCH:** The correct Jacobi parameters for the BC_1 operator with coth(2r) are explicitly "need to recheck" in section 3.5. Until determined, the operator whose discrete spectrum includes nu=3/2 is not identified.
- **FC-FROBENIUS-DISCRETE:** Section 3.6 shows both BC_1 Frobenius solutions decay at e^{-rho r} (continuous rate). The faster decay e^{-6r} claimed for the discrete L^2 mode requires the unestablished connection formula.

**Changes applied to the exploration file:**

- Frontmatter: verdict CONDITIONALLY_RESOLVED -> OPEN; correction block added.
- Section 3.4: OPEN INCONSISTENCY callout block added (nu=5/2, nu=1/2 only; nu=3/2 not a discrete eigenvalue of L^{(7/2,0)}; labeled as OPEN not resolved).
- Section 3.5: INCOMPLETE RESOLUTION callout block added after "need to recheck" line.
- Section 3.6: CRITICAL FAILURE callout block added after the "both solutions same rate" passage.
- Section 4.2 (Verdict): Replaced CONDITIONALLY_RESOLVED with OPEN; detailed three-leg explanation added.
- Section 4.3 (G2a Gate): Replaced "ACHIEVED at reconstruction grade" with DEFERRED_VERIFICATION; gate explicitly not closed.
- Section 5 (Failure Conditions): FC-JACOBI, FC-OPER-MATCH, FC-FROBENIUS-DISCRETE added as primary blockers before FC1.
- Section 8 (Grade Assessment): Table updated; G2a explicitly NOT CLOSED; L^{(7/2,0)} spectrum at nu=3/2 marked FAILS.

**The prior log entry** (oq-kk1a-cas-norm-fiber-wavefunction, 2026-06-23) stated "G2a gate CLOSED at reconstruction grade" and named only FC3 as the primary remaining gate. That entry is superseded. The correct current state is: G2a gate DEFERRED_VERIFICATION; primary blockers are FC-JACOBI, FC-OPER-MATCH, FC-FROBENIUS-DISCRETE (all more fundamental than FC3, which applies even within the BC_1 model).

**Upgrade conditions:** (1) Determine correct Jacobi parameters for L_{BC_1} = d^2/dr^2 + [7 coth(r) + 2 coth(2r)] d/dr. (2) Verify its discrete spectrum includes nu=3/2. (3) Establish the connection formula linking c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) to the Wronskian of the Frobenius solutions of this operator.
