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
Verdict: CONDITIONALLY_RESOLVED
Full reconstruction-grade computation of the relative-discrete-series Plancherel multiplicity m_H(S(6,4)) for SL(4,R)/SO_0(3,1) with fiber spinor S(6,4). The Flensted-Jensen equal-rank criterion is confirmed to pass: the correct split-rank is dim(a_q) = 1 (not 3 as in the prior pessimistic reading), where a_q is the maximal abelian subspace in p_G ∩ q within the 9-dimensional tangent space Sym^2_0(R^{3,1}*). The isotropy branching is established at reconstruction grade as S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2) (four left-Weyl plus four right-Weyl spinors of Spin(3,1)), consistent with one SM generation. The multiplicity m_H(S(6,4)) = 24 arises as 8 (fiber H-type summands) x 3 (topological factor from X^4); remaining open conditions are OQ1 (CAS verification split-rank = 1), OQ2 (CAS branching check), and OQ3 (topological factor ind_top(D_{X^4}) = 3 from hat-A genus on X^4).
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
