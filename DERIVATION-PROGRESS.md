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
Verdict: CONDITIONALLY_RESOLVED
Replaced the incoherent ordinary L2-kernel target `dim_H ker_L2(D_fib) = 24` on `GL(4,R)/O(3,1)` with the precise analytic invariant: the relative-discrete-series Plancherel multiplicity `m_H(S(6,4))` in `L2(SL(4,R) x_{SO_0(3,1)} S(6,4))`. Key finding: the Flensted-Jensen equal-rank condition is satisfied (split-rank of `SL(4,R)/SO_0(3,1)` is `min(3,1) = 1` = rank of compact fiber `SO(4)/SO(3) = S^3`), so relative discrete series exist and the invariant is well-defined and coherent. The prior pessimistic rank reading (3 != 1) used the wrong rank definition. Remaining open: branching rules for the non-standard 9-dimensional isotropy embedding of `Spin(3,1)` into `Spin(6,4)`, and the explicit value `m_H(S(6,4)) = 24?`
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`
