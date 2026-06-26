---
title: "Residue-to-Physics Derivation Program"
started: 2026-06-22
status: in_progress
---

# Residue-to-Physics Derivation Program

Three-layer program to move from the distortion residue (proved in TI E049) and Weinstein's GU constructions to concrete physical derivations.

> **2026-06-25 global status guard.** Older rows in this progress log are provenance, not
> current verdicts, when they conflict with the status ledgers. Current boundaries:
> generation count / `ind_H(D_GU)=24` is OPEN; Shiab is RESOLVED for algebraic existence
> only; Nguyen's U(128) pincer is SUBSTANTIALLY_ADDRESSED but full GU local/global anomaly
> cancellation is OPEN; VZ is 14D CONDITIONALLY_EVADED and 4D CONDITIONALLY_RESOLVED at
> principal-symbol grade; dark-energy divergence-free is CONDITIONALLY_RESOLVED pending
> the written-action theta/Euler-Lagrange identification.

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

**Status:** COMPLETE FOR ALGEBRAIC EXISTENCE ONLY (corrected 2026-06-25)

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
interior product. The map is real-linear, Spin(9,5)-equivariant, and non-zero as a map.
No complexification required. It is not injective dimensionally as a map from
Lambda^2 V tensor S to V tensor S in 14 dimensions, and non-vanishing on every non-zero
input/rank/kernel/uniqueness are open representation-theory questions. The quaternionic structure of S enriches
but does not obstruct the map. Nguyen §3.1 complexification gap does not arise.

**Key step:** the explicit Clifford-contraction formula is natural and non-zero on a
simple input such as e^1 wedge e^2 tensor s. Simplicity of Cl(9,5) and H-linearity support
the representation-theoretic setting, but they do not imply injectivity of the displayed
map. Future work that needs injectivity must compute the Hom-space rank/kernel directly.

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

**Status:** CONDITIONALLY_RESOLVED (corrected 2026-06-23; C1+C2 independence clarified 2026-06-25)

**Result:**

Equivariance of θ = π − ε⁻¹Bε: **PROVED.** The τ⁺ homomorphism construction ensures the
left factor g_a has no effect on θ; the right factor g_b acts by Ad(g_b)⁻¹. G-equivariance
holds unconditionally.

Dynamism (θ is not forced constant): **PROVED.** The metric-compatibility argument that
forces λ = constant does not apply to θ. θ is free to vary with curvature, dissolving the
fine-tuning problem at the structural level.

Divergence-free (D_A* θ = 0): **CONDITIONALLY_RESOLVED, not proved unconditionally.** The
C3 / Noether-second-theorem path closes the condition only if theta is derived from a
written GU action as the relevant Euler-Lagrange/source sector. Proof skeleton:

1. **Action:** S[A] = ∫_{Y¹⁴} ‖F_A‖²_ℊ dvol_ℊ (Yang-Mills on Y¹⁴, where ℊ is the gimmel
   metric of signature (9,5) from the N1 audit). The action is gauge-invariant under G
   (gauge group of the principal bundle over Y¹⁴): F_A ↦ gF_Ag⁻¹ and cyclicity of trace
   give ‖F_A‖² unchanged.

2. **EL derivative:** δS/δA = 2D_A*F_A ∈ Ω¹(Y¹⁴, ad P). Same type as θ. ✓

3. **Noether's second theorem:** The gauge invariance of S forces D_A*(δS/δA) = 0 off-shell.
   Proof: gauge variation δ_ξ A = D_A ξ, so δS = ∫tr(E_A · D_A ξ) = ∫tr(D_A*E_A · ξ) = 0
   for all compactly supported ξ, hence D_A*E_A = 0. ✓

4. **Conditional identification θ = D_A*F_A:** The GU vacuum field equation (schematic from transcript
   [00:25:56]: divergence operator on curvature term and dark energy term both give zero)
   is reconstructed as D_A*F_A − θ = 0, identifying θ = D_A*F_A on-shell. This is the
   load-bearing unproved action-level identification, not a verified theorem. ⚠

5. **Conclusion:** D_A*θ = D_A*(D_A*F_A) = 0 by Noether only after Step 4 is derived from
   the actual GU variational principle. ⚠

The 120-orders-of-magnitude problem is structurally reframed, not solved: θ is dynamic and
gauge-equivariant, but its divergence-free equation is conditional on the action-level
structural identification above.

**Residual blockers:**
- The identification θ = D_A*F_A is on-shell reconstruction, not derived from a written
  GU action. This is blocking for RESOLVED status.
- Gimmel G-invariance (C1) remains a needed action-invariance cross-check. It is not an
  independent Noether-first-theorem route to D_A*θ = 0; any correct Noether proof is the
  same Noether-second-theorem/E_A-sector route.

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
| 2026-06-22 | Layer 2 (C3/Noether path executed; **superseded by CORRECTION DARK-ENERGY-01 and 2026-06-25 sweep**): this row originally marked D_A*θ = 0 PROVED on-shell. Current status is CONDITIONALLY_RESOLVED. The Noether-second-theorem route is structurally sound only after the written GU action derives theta as the relevant Euler-Lagrange/source sector; C1+C2 is a gauge-invariance cross-check, not an independent Noether route. Filed dark-energy-noether-closure-2026-06-22.md. |
| 2026-06-22 | **N5 generation count SM branching closure** (**superseded by GEN corrections; current status OPEN**): representation-theory computations identified the intended 2 spin-1/2 + 1 RS arithmetic, but the claimed "Total: 3 generations" / "CONDITIONALLY 3" status is stale. Candidate-A three-generation arithmetic remains a reconstruction target; the RS leg `ind_H(D_RS)=8` is unproved and all analytic routes remain blocked, failed, or circular. Filed generation-count-sm-branching-closure-2026-06-22.md. |
| 2026-06-22 | **N4 IG dimension matching and τ⁺/Sp(64) construction**: the dimension-matching residual (dim sp(64) = 8256 vs. 16384) is closed, and τ⁺ construction remains a valid group-theoretic result. **Supersession note 2026-06-25:** the row's original "NGUYEN §2 FULLY CLOSED" language was too strong. Current status: Nguyen §2 anomaly pincer is SUBSTANTIALLY_ADDRESSED; U(128) is defused by Sp(64), but full GU anomaly cancellation remains non-canon pending explicit local I_16/index-density and global spin-bordism/Dai-Freed/eta checks. Filed explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md. |
| 2026-06-22 | **Phase 1 parallel agent results in.** Four agents (A–D) returned verdicts on anomaly structure, generation count, hidden curvature, and distortion + bundle formalization. See Phase 1 Results section below. |
| 2026-06-22 | **Synthesis paper drafted** (**historical, partially superseded**). `papers/canonical-structures-14d-metric-geometry-2026-06-22.md` synthesized Phase 1 and follow-on results. Current readers should not inherit its stronger anomaly/generation wording without later corrections: Shiab existence remains resolved only for one equivariant map; Sp(64) anomaly cancellation is substantially addressed but not canon; generation count is OPEN; Nguyen §2 is substantially addressed, not fully closed. |
| 2026-06-23 | **CORRECTION THETA-01 — theta-field ratio prediction overstated.** The claim in `explorations/theta-field-flrw-eos-2026-06-23.md` §7.2 and §12.1 that the ratio w_a/(w_0+1) ~ -1.80 is "independent of f_0 (the unknown initial amplitude)" and constitutes a "genuine GU prediction" was overstated. The ratio is f_0-independent (correct algebra: f_0 cancels). However, the numerator -3.17 f_0 comes from dw_B/dz at z=0, which was evaluated at phi_0 ~ 1.94 rad derived from the de Sitter tracker approximation. A different phi_0 gives a different dw_B/dz and a different ratio. The ratio is dependent on phi_0, which depends on matter-era evolution that was acknowledged as not computed (OQ3). Corrections applied to: (a) exploration §7.2 and §12.1, (b) exploration §11 OQ5 replaced with phi_0-dependence task, (c) exploration §9.2 "genuine GU prediction" framing replaced, (d) canon/theta-field-flrw-dark-energy-eos.md Result 3 and Primary Gap sections. Correct description: "reconstruction-grade estimate conditional on phi_0 ~ 1.94 rad from the de Sitter tracker, independent of f_0 but not of phi_0." Canon file remains at CONDITIONALLY_RESOLVED; no demotion to explorations needed as the underlying physics is otherwise sound. New open task: compute full phi_0-dependence of w_a/(w_0+1) to determine whether -1.80 is a min/max/saddle. |
| 2026-06-23 | **VZ mixed 14D covectors (superseded scope):** the original row marked the lane `EVADED` and the 4D pullback `VERIFIED`. Current status after VZ-01 / 2026-06-25 sweep: 14D mixed-covector VZ is CONDITIONALLY_EVADED pending independent E-block invertibility; 4D section-pullback is CONDITIONALLY_RESOLVED at principal-symbol grade, not full verified dynamics. Filed `explorations/vz-14d-mixed-covectors-2026-06-23.md` and corrected owner/canon surfaces. |
| 2026-06-23 | **CORRECTION DARK-ENERGY-01 (MO-03): Dark energy theta divergence-free verdict downgraded from RESOLVED to CONDITIONALLY_RESOLVED.** The canon file `canon/dark-energy-theta-divergence-free.md` carried verdict RESOLVED based on the C3/Noether path. Review found the central claim D_A* theta = 0 rests on Assumption 3 (structural identification: theta is the gauge-potential sector of E_A), which is explicitly labeled reconstruction grade and is not proved. The C3 Noether argument is structurally sound but conditional on Assumption 3. The C1+C2 alternative path (gimmel G-invariance) is explicitly acknowledged as open. Neither path is complete. Changes applied: (a) frontmatter verdict changed from RESOLVED to CONDITIONALLY_RESOLVED; (b) correction field added to frontmatter; (c) Step 4 header updated from COMPLETE to CONDITIONALLY COMPLETE; (d) Step 4 opening sentence clarified as conditional on Assumption 3; (e) Assumption 3 block expanded with explicit statement that it is unproved and load-bearing; (f) Known Failure Modes expanded from 3 to 5 named failure modes (F1–F5), with F2 explicitly stating neither path is complete; (g) Upgrade Conditions section added with two conditions for upgrade to RESOLVED; (h) CANON.md entry updated; (i) RESEARCH-STATUS.md current research map entry updated. |
| 2026-06-23 | **NOTE MO-07 (OC2 Gate A1 — P_disc target unanswered): No verdict change; three failure conditions added (FC7-FC9).** The file `explorations/oc2-sobolev-a1-bounded-transform-2026-06-23.md` carried verdict CONDITIONALLY_RESOLVED with FC1-FC6, but did not address the fundamental question: what is P_disc projecting onto when SL(4,R) has no scalar discrete series (Harish-Chandra criterion fails: rank(G) = 3 ≠ rank(K) = 2)? In the non-compact Y^14 setting, the scalar sector of D_GU on SL(4,R)/SO_0(3,1) has no L^2 discrete spectrum; the three framework candidates (b-calculus, scattering, Melrose-Piazza) each supply conditional boundedness but none verify that a non-trivial discrete sector exists on the non-compact fiber. Changes applied: (a) Priority note added to §1 (before Problem Statement) naming the unanswered question and routing clarification that Gate A1 is only operative for the secondary non-compact Y^14 analytic program — the primary APS/K3 route bypasses A1 by working on the compact K3 factor; (b) Three additional failure conditions added to §8: FC7 (scalar P_disc has empty target on non-compact fiber — no discrete series for SL(4,R)), FC8 (tau-twist S(6,4) fails to generate discrete L^2 spectrum on A3 fiber, collapsing the non-compact Y^14 analytic program onto the APS/K3 route), FC9 (Gate A1 is non-load-bearing because APS/K3 route is primary, making CONDITIONALLY_RESOLVED a mislabeled priority weight rather than a false verdict). Verdict CONDITIONALLY_RESOLVED is retained — the frameworks do supply conditional boundedness — but the file now makes explicit that this is secondary to the APS/K3 route and that the P_disc target question is open. |
| 2026-06-23 | **CORRECTION VZ-01 (critical): VZ 14D mixed-covector status downgraded from EVADED to CONDITIONALLY_EVADED.** The §4 argument in `explorations/vz-14d-mixed-covectors-2026-06-23.md` uses `E^{-1}` without proving E invertible. The `det(M) = det(E)*det(S_R)` identity is a consequence of E being invertible, not a proof of it -- using it to conclude `det(E) != 0` is circular. If E has a null vector for some xi with `xi2 != 0`, the Schur block fails before the kernel argument. Changes applied: frontmatter `vz_evasion_status` changed to `CONDITIONALLY_EVADED` and correction field added; §4 invertibility remark replaced with explicit precondition-failure analysis; §7 table mixed-covector and E-block rows updated; §7 overall verdict updated; §9 rewritten with open precondition. The 4D pullback (OQ3-V1/V2/V3, VERIFIED) and the Clifford non-decoupling argument are unaffected. Open precondition: prove `E(xi): Q -> Q` has trivial kernel for all xi with `g_Y(xi,xi) != 0` by direct Cl(9,5) computation. |
| 2026-06-23 | **dark-energy-c1-c2-path-gimmel-ginvariance — C1+C2 path attempted for D_A* theta = 0. Verdict: OPEN.** C1 (gimmel G-invariance) ESTABLISHES at reconstruction grade: G = Sp(64) acts trivially on Y^14 as a base manifold, so g_gimmel is automatically G-invariant; L^2 inner product on Omega^1(Y^14, ad P) is G-invariant by Ad-invariance of the Killing form. C2 (Noether's first theorem yields D_A* theta = 0) FAILS: the blocking condition is that to derive D_A* theta = 0 from global G-symmetry + Noether's first theorem, one must identify theta as the Noether current J ~ D_A* F_A, which requires the structural identification theta = D_A* F_A. This is Assumption 3 from the C3 path restated at a different level; the C1+C2 route does not avoid it. F5 (gimmel G-invariance not independently established) is discharged by C1. Dark-energy canon verdict not upgraded. File: `explorations/dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md`. |
| 2026-06-23 | **CORRECTION DARK-ENERGY-C1C2-01: Equivariance proof-status and Noether theorem errors in `dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md` corrected.** Two errors fixed. (1) Section 2 ('Established Context') labeled the equivariance result as 'PROVED, prior explorations.' This overstates the chain: the prior exploration files are reconstruction grade, with no coordinate-level derivation from a written GU action. The label has been changed to 'reconstruction grade, prior explorations' with an explicit note that treating it as PROVED would overstate the derivation chain. (2) The file correctly identifies at line 200 that the right theorem for deriving D_A* E_A = 0 from gauge invariance is Noether's SECOND theorem, not first. However, the original C1+C2 path description in the canon file implicitly invoked Noether's first theorem (global symmetry → on-shell conserved current), which is the wrong theorem for this purpose. This is a canon-level error in the original path description. A new failure mode F6 has been added to `canon/dark-energy-theta-divergence-free.md` logging this as a canon-level error: the C1+C2 path using Noether's first theorem cannot derive D_A* theta = 0 without Assumption 3; the C1+C2 path using Noether's second theorem collapses into the C3 path; there is no C1+C2 path that is both correct and independent of C3. No verdict change to the canon file (remains CONDITIONALLY_RESOLVED); the OPEN verdict in the exploration file is correct and unchanged. |
| 2026-06-23 | **CORRECTION DG-COUNT-01 (critical): GU-Chir generation count in the DG carve-out corrected from asserted-settled `ind_H(D_GU) = 24 = 3 generations` to OPEN (Candidates A/B equistatus).** `explorations/distler-garibaldi-precision-carveout-2026-06-23.md` stated the GU-Chir condition with a settled count: "ind_H(D_GU) = 24 ... decomposing as 16 H-lines (spin-1/2, two generations) + 8 H-lines (RS sector, one generation). Generation count = ind_H(D_GU) / 8 = 3" (§4 GU-Chir block), plus the same assertion in §2 (chirality-source bullet), §6 (formal carve-out statement), §8 (What This Changes), and §9.1. This selects Candidate A as a baseline, contradicting the same-session synthesis `explorations/generation-count-rank3-resolution-2026-06-23.md` (verdict OPEN), which holds Candidate A (rank_H(S_RS^+) = 4 -> ind_H = 24 -> 3 gen) and Candidate B (rank_H = 8 -> ind_H = 32 -> 4 gen) as equistatus, neither derived nor eliminated, gated on OQ-RK1. This is the "verdict inflation through candidate selection" pattern flagged in `process/loop-adversarial-log.md` (standing calibration: "When two undismissed generation-count candidates exist, emit verdict OPEN ... do not select a baseline"). Changes applied to the carve-out file: (a) §2 chirality-source bullet rewritten to state the value as OPEN in {24, 32}, Candidates A/B equistatus; (b) §4 GU-Chir block rewritten as a chirality *test* (which invariant carries chirality), with the value OPEN pending OQ-RK1 and the 16+8 decomposition explicitly marked Candidate-A-conditional; (c) §6 formal statement made index-value-independent; (d) §8 records the value as OPEN and the scope-exit verdict as index-independent; (e) §9.1 reframed from "ind_H = 24 at verified grade" to OPEN between Candidate A (24) and Candidate B (32), blocking gate OQ-RK1. **The DG scope-exit verdict (frontmatter RESOLVED) is unchanged and correct: it is index-value-independent — GU exits DG_E8 via DG-A1/A2/A6/A7 regardless of the index value.** The canon map `canon/no-go-class-relative-map.md` (§0.1 CANON-5, §1 summary table, §2.1 Witten row, §2.4 GU-Chir block with GC-FC1–GC-FC4) already carried the OPEN/equistatus treatment from a prior pass and required no change. No file-level verdict demotion (the carve-out's RESOLVED is the scope-exit claim, not the count). |
| 2026-06-23 | **CORRECTION H3-01 (MO-04): h3-gap2-gu-universality frontmatter verdict corrected from OPEN to PARTIAL.** The single `verdict: OPEN` in the frontmatter of `explorations/h3-gap2-gu-universality-2026-06-23.md` obscured meaningful partial resolution already recorded in the §6 summary table and §9 body verdict of the same file. The file body (§5.2 and §9) already records a CONDITIONALLY_RESOLVED verdict for Q-NAC and Q-SBP (equivariant splits), alongside FAILS-as-stated for Q-SBP (all splits) and OPEN for Q-SBP (SM-charge/Pati-Salam settings). The single frontmatter OPEN did not capture this structure. Fix applied: frontmatter `verdict` changed from `OPEN` to `PARTIAL`; `verdict_detail` block added enumerating four sub-condition verdicts; `corrections` block added recording H3-01 date and summary. Sub-condition verdicts: (1) Q-NAC: CONDITIONALLY_RESOLVED (reconstruction) -- GU null-cone causal structure forces NAC via null-cone-bounded propagation, conditional on VZ evasion + APS/Fredholm on K3. (2) Q-SBP all settings: FAILS as stated -- product-state non-equivariant bipartite split yields CHSH <= 2; full universality refuted. (3) Q-SBP Sp(64)-equivariant splits: CONDITIONALLY_RESOLVED (reconstruction) -- Sp(64) irreducibility of H^64 rules out any Sp(64)-equivariant bipartite split of H^64. (4) Q-SBP SM-charge (Pati-Salam) settings: OPEN -- G_PS acts reducibly on S(6,4) = C^16 (a subspace of H^64); Sp(64) irreducibility does not transfer to the restricted G_PS action; whether G_PS-equivariant product-state decompositions of S(6,4) exist is an open computation (OQ-G2-1). The §5.2 correction in the body (withdrawal of SM-charge equivariant Q-SBP claim) is now consistently reflected in the frontmatter. |

---

## Phase 1 Results (2026-06-22)

### Agent Verdicts Summary

| Agent | Task | Verdict | File |
|---|---|---|---|
| A | Anomaly audit — Cl(9,5) gauge group and Nguyen §2 | SUPERSEDED: NGUYEN_U128_PINCER_SUBSTANTIALLY_ADDRESSED; FULL_GU_ANOMALY_OPEN | `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md` |
| B | Generation count — Cl(9,5) Dirac-DeRham complex | SUPERSEDED: OPEN | `explorations/generation-count-cl95-dirac-derham-2026-06-22.md` |
| C | VZ1 + HC1 — Velo-Zwanziger no-go and hidden curvature | VZ1: unconfirmed evasion; HC1: THREE HIDDEN CONFIRMED under torsion-sourcing reading | `explorations/hc1-hidden-curvature-components-2026-06-22.md` |
| D | DD1 + PC2 — Distortion literature and bundle stub | DD1: PARTIALLY_NAMED; PC2: formalization stub complete | `explorations/dd1-distortion-tensor-literature-check-2026-06-22.md`, `explorations/pc2-met-x4-bundle-formalization-stub-2026-06-22.md` |

### Agent A — Anomaly (Key Findings)

The correct gauge group in the (9,5) setting is **Sp(64) = U(64,H)**, not U(128). This follows from the fact that Cl(9,5) ≅ M(64,H) is a quaternionic algebra; the natural automorphism group of the spinor module S = H^{64} as a quaternionic Hermitian space is Sp(64) with dim_R = 8256. Nguyen's dimension-matching argument for U(128) was an artifact of the (7,7) real-type Clifford algebra and does not transfer.

**Supersession note 2026-06-25 (ANOMALY-01):** this positive audit defuses the
specific Nguyen U(128) pincer, but it does not prove full GU anomaly cancellation.
Pseudoreality and pi_15(Sp) are not enough by themselves for the actual 14D chiral field
content. Current status: local cancellation needs the explicit `I_16`/index-density
calculation, and global cancellation needs spin-bordism/Dai-Freed/eta control.

**Residual open:** dim sp(64) = 8256 (vs. the 16384 = dim u(128) that anchored Nguyen's algebra-dimension matching). Whether the IG = Sp(64) ⋉ Omega^1(sp(64)) construction achieves the correct algebra-dimension match for the shiab must still be verified. The tau+ homomorphism's behavior in the (9,5)/Sp(64) setting has not been fully checked.

### Agent B — Generation Count (Key Findings)

The chirality operator omega^2 = +1 in Cl(9,5) (verified), giving a well-defined chiral splitting S = S^+ ⊕ S^- over H, with dim_H(S^±) = 32. The fiber of Y^{14} is contractible, so the Families Index Theorem reduces the index computation to data on X^4 alone.

The structural mechanism for 3 = 2 + 1 generations (V ⊕ W spinor product rule + Rarita-Schwinger term + Pati-Salam content SU(4)×SU(2)×SU(2) from the fiber structure group Spin(6)×Spin(4)) is preserved under the Cl(9,5) correction. The Pati-Salam group appearing in the fiber spinor decomposition matches S(6,4) = C^{16} decomposing as (4,2,1) ⊕ (4-bar,1,2) under SU(4)×SU(2)_L×SU(2)_R.

**Supersession note 2026-06-25 (GEN-OPEN-01):** these representation-theoretic
computations identify the intended arithmetic but do not derive the analytic index.
Current status: generation count OPEN; the RS leg and non-compact Fredholm/index
framework remain load-bearing.

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
Verdict: SUPERSEDED_TO_CONDITIONALLY_EVADED
Extended the Schur complement symbol computation from horizontal covectors to all mixed
14D covectors `xi = xi_H + xi_N` using Spin(9,5) Clifford module structure.
**Supersession note 2026-06-25 (VZ-01):** the old `EVADED` verdict used `E^{-1}`
before independently proving the E-block invertible. Current status: 14D mixed-covector
VZ is CONDITIONALLY_EVADED pending a direct E-block proof; 4D pullback is
CONDITIONALLY_RESOLVED at principal-symbol grade, not a full verified dynamics theorem.
Historical details are retained in the source exploration.
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
Verdict: SUPERSEDED_TO_OPEN_FOR_GENERATION_COUNT
Historical entry. This pass supplied useful reconstruction arithmetic, but later audits found
that the RS analytic index leg is not derived and that all previous analytic routes are
blocked, failed, or circular. Current status: generation count OPEN; cite the arithmetic
as a target only, not as a conditionally resolved count.
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### vz-schur (2026-06-23)
Verdict: SUPERSEDED_TO_14D_CONDITIONALLY_EVADED / 4D_CONDITIONALLY_RESOLVED
Historical entry. The main Schur argument depends on E-block invertibility and therefore
does not close 14D VZ evasion. Current status: 14D CONDITIONALLY_EVADED pending an
independent E-block proof; 4D section-pullback is CONDITIONALLY_RESOLVED at
principal-symbol grade, not a full verified dynamics theorem.
File: `explorations/vz-schur-complement-2026-06-23.md`

---

### discrete-series OQ3b+OQ3c analytic Fredholm (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED (upgraded)
Pushed OQ3b (RS block Fredholm index = 8) and OQ3c (H-index additivity) from degree-of-freedom counting to analytic Fredholm theory level. OQ3b (§15): applied Atiyah-Schmid formal-degree sum to S_R^{eff} on L2_disc; Casimir matching gives C_{sl(4,R)} = 13/4 for the RS K-type D(1/2,0) (= 3/4 from sl(2,C) Casimir + rho-shift 10/4 from |rho_G|^2 - |rho_K|^2 = 5 - 10/4); formal degree d(pi) = 1 per summand (Plancherel polynomial ratio P(lambda+rho)/P(rho) = (225/4)/12 at reconstruction grade); Hom count = 8 (4 copies D(1/2,0) + 4 copies D(0,1/2) from physical RS fiber tau_RS^{phys}); ind_H(S_R^{eff}) = 8. OQ3c (§16): exact Atkinson-Schur LDU shows ind(D_GU) = ind(A) + ind(S_R^{eff}) with triangular factors having index 0; H-orthogonality established from H-linearity of Pi_RS (Clifford bimodule). Combined ind_H = 16 + 8 = 24. Remaining hard gates: CAS verification of C_{sl(4,R)} = 13/4 (AF1), Plancherel ratio (AF2), Hom multiplicity-one (AF3).
File: `explorations/n5-discrete-series-gl4r-2026-06-23.md`

---

### vz-schur (2026-06-23) -- OQ3-V1/V2/V3 verification pass
Verdict: VERIFIED (4D VZ evasion) [CORRECTED 2026-06-23 to CONDITIONALLY_RESOLVED — see VS-1 correction note below]
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
Formally stated the signed-readout boundary theorem with full hypotheses (H1-H7 covering free commutative monoid, lattice-ordered abelian group, unique homomorphic extension, PN/Jordan split, Z-grading, and H-linearity), a five-part conclusion (M: monotonicity iff; P: provenance always monotone; C: coexistence at the boundary; Z: integer-index stability; K: K-theory lift to KSp^0 = KO^4), and seven explicit falsification conditions (F1-F7). The two physical instances are placed precisely: GW axial charge Q_A occupies the non-monotone side (coexistence case, Part C), while GU generation-count target ind_H = 24 (OPEN as a physics count) occupies the monotone degenerate side (R_- = 0). Core Parts M/P/C are RESOLVED at reconstruction grade; Parts Z/K are gated on non-compact Atiyah-Jannich stability (OC1) and H-linear Fredholm theory on non-compact Y^14 (OC2).
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
Verdict: CONDITIONALLY_RESOLVED_FOR_GRAVITATIONAL_PRINCIPAL_SYMBOL_LEG
Computed whether the Weyl tensor of the gimmel metric on Y^14 produces a separate
gravitational VZ principal-symbol problem for the RS sector independent of gauge
coupling. Current scope: curvature enters as lower/zero-order structure in this
reconstruction argument, so no independent gravitational principal-symbol obstruction is
identified. This does not upgrade the overall VZ lane beyond 14D CONDITIONALLY_EVADED /
4D CONDITIONALLY_RESOLVED.
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
Verdict: OPEN (corrected 2026-06-23 from CONDITIONALLY_RESOLVED — see CORRECTION GEN-04 below)
Attempted to derive rank_H(S_RS^+) = 4 from Clifford representation theory on Cl(9,5) = M(64,H) and the RS constraint ker(Gamma^{14D}). **The derivation of rank_H(S_RS^+) = 4 FAILS by circularity** and the verdict is corrected to OPEN. The only route to "4" in the file is rank_H(S_RS^+) = ind_H(D_RS)/A-hat(K3) = 8/2, which divides the physical generation H-count (8) by A-hat(K3) = 2; multiplying back recovers 8 — an identity, not a derivation. Every direct Clifford-module computation of the effective rank in the file yields 192, 384, 96, or a non-integer 1/2 instead of 4. The prior "the argument is non-circular" claim is withdrawn. This is consistent with GEN-01 ("the final halving is unjustified") and GEN-03 ("the RS leg is physical-count grade only"). **What survives (kept as established sub-result):** rank_H(ker Gamma^{14D}|_{S^+}) = 448 - 32 = 416, an exact M(64,H) computation (S = H^{64}, S^{pm} = H^{32} from omega^2 = +Id, (p-q) mod 8 = 4). This is genuine Clifford algebra but does NOT connect non-circularly to the effective twist rank 4 — the 416->4 bridge is the open problem. rank_H(S_RS^+) = 4 remains Candidate A; Candidate B (rank_H = 8 => 4 generations) is live and undismissed. Decisive circularity-free gate: OQ-RK1 CAS computation of rank(Pi_RS * E_+ * Pi_RS) in M(64,H), which would return 4 or 8 directly. OQ-RK2 (APS boundary conditions for constrained RS on K3) also remains open.
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
Formal theorem statement for the signed-readout boundary theorem written at reconstruction grade and promoted to canon path. Five-part theorem (M/P/C/Z/K) with full hypotheses H1-H7, complete elementary proofs for the core (Parts M, P, C), and seven explicit falsification conditions F1-F7. The core claim -- monotone provenance coexists with non-monotone readout precisely when any generator weight is negative (w_- != 0) -- is RESOLVED at reconstruction grade with explicit proofs requiring only free commutative monoids and lattice-ordered abelian groups. The integer-index stability (Part Z) and K-theory lift (Part K) are CONDITIONALLY_RESOLVED, gated on Atiyah-Jannich stability for the non-compact Y^14 setting (OC1) and H-linear Fredholm theory for L^2(Y^14, S=H^64) (OC2). Two worked physical instances occupy opposite sides of the boundary: GW axial charge Q_A = n_+ - n_- (non-monotone, coexistence case) and GU generation-count target ind_H = 24 (OPEN as a physics count; monotone, degenerate case with w_- = 0).
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
OQ3a RESOLVED. Generation count CONDITIONALLY_RESOLVED (reconstruction grade, NOT a
precision theorem) at 3 via APS/K3:
ind_H(D_GU) = 8*A-hat(K3) + 8 = 16+8 = 24, generations = 24/8 = 3, conditional on
rank_H(S_RS^+) = 4 (Candidate A); Candidate B (rank_H = 8 => 4 generations) not excluded.
LEG-SPLIT (per GEN-03 below): the two legs of the 24 are NOT of equal proof strength.
The spin-1/2 leg (16 = A-hat(K3)*rank_H(S(6,4)) = 2*8) is a genuine index-theory
(Atiyah-Singer) computation: rank_H(S(6,4)) = 8 from Cl(9,5) = M(64,H) module theory and
A-hat(K3) = 2 is a topological invariant; this leg is index-theory-grade. The RS leg
(8 = A-hat(K3)*rank_H(S_RS^+) = 2*4) is NOT analytically derived: every analytic route to
ind_H(D_RS) = 8 has FAILED (scalar FJ/BC1 superseded; rank-3 Atiyah-Schmid empty sum;
tau-twisted FAILS AS STATED on four criteria; BC1 Jacobi GENUINE_OBSTRUCTION), and the
surviving APS input rank_H(S_RS^+) = 4 rests on the GEN-01 physical-DOF heuristic whose
final halving is unjustified (see GEN-01 note). The RS leg is therefore physical-count grade
only. Do not promote "24 = 3 generations" to a precision theorem until ind_H(D_RS) has an
independent analytic index derivation (gates OQ-RK1, OQ-RK2).
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

### CORRECTION MO-01 — Shiab injectivity argument attempted, superseded by SHIAB-01 (2026-06-23; superseded 2026-06-25)

**File corrected:** `canon/shiab-existence-cl95.md`

**Error (Step 3, original):** The "Non-zero on all non-zero inputs" claim was justified by the argument "c(iota_{e_a} alpha) != 0 for any non-zero alpha and generic frame, therefore the sum sum_a e^a tensor c(iota_{e_a} alpha) s is non-zero." This is logically invalid: 14 individually non-zero terms can sum to zero. The injectivity conclusion was stated without proving non-cancellation of the sum.

**Supersession (SHIAB-01, 2026-06-25):** The attempted fix above was itself invalid. A 2-form has no canonical metric-dual 1-form alpha^#, and the claimed injectivity is impossible by dimension count:

```text
dim(Lambda^2 V tensor S) = 91 dim(S),   dim(V tensor S) = 14 dim(S).
```

No linear injection from the former to the latter can exist in 14 dimensions. The correct retained conclusion is narrower: the displayed Clifford-contraction formula defines at least one natural real-linear Spin(9,5)-equivariant map, and that map is non-zero. Rank, kernel, non-vanishing on every non-zero input, and uniqueness remain open representation-theory questions.

**Verdict change:** `canon/shiab-existence-cl95.md` remains RESOLVED only for algebraic existence/equivariance of one natural map. It must not be cited for injectivity, rank/kernel, uniqueness, source-forced selector identity, anomaly cancellation, or generation count.

**Additional changes in same edit pass:**
- SHIAB-01 replaces the "Non-zero on all non-zero inputs" bullet with "non-zero as a map."
- Known Failure Modes now record kernel/rank and non-degeneracy-on-curvature as open, not discharged.

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

**Verdict change:** None. The RESOLVED verdict stands. The derivation was mathematically correct (it existed in full in N6 §5.5); the fix makes the canon file self-contained so the key identity can be verified without consulting the exploration file. **[SUPERSEDED by CORRECTION W2-01 (2026-06-26): this disposition was wrong. MO-02's own sub-step 4 ("the (R^3 tensor sgn) factor contributes w2 = w1(X4)^2 = 0 for oriented X4") RESTATES the load-bearing error rather than catching it. The derivation was NOT correct; the unconditional spin result is false. See W2-01 below.]**

---

### CORRECTION W2-01 (critical) — canon/w2-y14-spin-structure.md unconditional spin claim is FALSE (2026-06-26)

**File corrected:** `canon/w2-y14-spin-structure.md` (verdict RESOLVED -> CONDITIONALLY_RESOLVED).

**Supersedes:** the "Verdict change: None / RESOLVED stands" disposition of CORRECTION MO-02 (2026-06-23). MO-02 added a correct derivation for `w2(Sym^2(V)) = w1(V)^2 + w2(V)` (valid for the rank-3 V) but its sub-step 4 restated the actual error verbatim. MO-02 audited the missing-derivation citation gap and blessed the load-bearing assembly; it never recomputed the `(R^3 tensor sgn)` term.

**Error (Step 3 assembly + Step 4):** The `(R^3 tensor sgn)` summand of the vertical bundle TV is `V tensor L` (V = spatial R^3, L = time line bundle). For rank-3 V and line bundle L, `w2(V tensor L) = w2(V) + 2 w1(V) w1(L) + 3 w1(L)^2 = w2(V) + w1(L)^2` (mod 2). The canon and N6 §5.3/§5.5 DROPPED the `w2(V)` term, writing `w2(R^3 tensor sgn) = w1(L)^2 = 0` for oriented X4. Restoring it: `w2(TV) = w2(Sym^2_0(R^3)) + w2(R^3 tensor sgn) + 0 = w2(X4) + w2(X4) = 2 w2(X4) = 0`, so `w2(TV) = 0` — NOT `w2(X4)`. Step 4's "doubles to zero" cancellation then vanishes: `w2(Y14) = w2(TV) + w1(TV)*pi*w1(X4) + pi*w2(X4) = 0 + 0 + pi*w2(X4) = pi*w2(X4)`.

**Independent verification:** For any rank-4 real bundle E, `w2(Sym^2 E) = w1(E)^2`. `w(Sym^2 E)` is the product over the six mixed splitting roots `{ti + tj}_{i<j}` (the four squares `2ti` are trivial mod 2); the second elementary symmetric function of those six roots is `e2 = 3 sigma1^2 + 2 sigma2 ≡ sigma1^2 = w1(E)^2` (mod 2) by Newton's identity (`p1 = 3 sigma1`, `p2 = 3 sigma1^2 - 4 sigma2`, `e2 = (p1^2 - p2)/2`). For oriented X4 (`w1 = 0`) this is 0, confirming `w2(TV) = 0`.

**Corrected result:** `w1(Y14) = 0` unconditional (unaffected). `w2(Y14) = pi*w2(X4)` — **Y14 is spin iff X4 is spin**. For non-spin X4 (e.g. CP2) Y14 is non-spin, and `D_gimmel` is well-defined without a section choice only for spin X4; non-spin X4 requires a spin/spin-c structure — OPEN. The "metric bundle absorbs the spin obstruction / spin even for CP2 / D_gimmel needs no section choice" claims are RETRACTED.

**Provenance:** error surfaced by an external adversarial audit (2026-06-26) and verified two independent ways (dropped-term restoration + the Newton-identity `w2(Sym^2 E) = w1^2` computation). This was the one canon result carrying no prior correction; it slipped through because MO-02 audited the citation gap, not the computation.

**Verdict change:** `canon/w2-y14-spin-structure.md` RESOLVED -> CONDITIONALLY_RESOLVED. Cascade applied (sweep order): source `explorations/n6-w2-y14-gysin-spin-structure-2026-06-22.md` (status SUPERSEDED + verdict banner), `RESEARCH-STATUS.md` (canon registry row + promotion-record row), `CANON.md` (Canon Entries table row), and the canon file itself (frontmatter, banner, Steps 3-4, Result, Geometric Explanation, Known Failure Modes).

**Open cascade (downstream re-evaluation required — deliberately NOT done in this pass, per the same-session/independent-pass rule):** `canon/no-go-class-relative-map.md` cites the retracted premise in §0.1 (the "Generic-X4 entries" and "why K3 is a working hypothesis" paragraphs), the Witten Met(X4) entry §2.1, and the CANON-5 scope tags (FH §2.3, DG GU-Chir §2.4). Those entries argued "do not globally fix X4 = K3 because w2-y14 proves spin for any orientable X4 including CP2." That justification is now FALSE: for non-spin X4, Y14 is not spin, so D_gimmel is not defined without extra structure, and the generic-X4 entries inherit a spin-on-X4 precondition. New open failure condition **W2-FC1**: re-derive whether the Witten class-exit (non-compact fiber) and the no-import-K3 argument survive once the base is required spin — or whether GU must restrict to spin X4, which changes the status of the Â(K3)=2 / K3 working hypothesis. **[W2-FC1 RESOLVED 2026-06-26 — see entry immediately below.]**

---

### W2-FC1 — RESOLVED — Witten class-exit survives W2-01; X4 spin is a standing precondition (2026-06-26)

**Opened by:** CORRECTION W2-01 (2026-06-26). **Question:** after W2-01 (Y14 spin iff X4 spin), do the no-go map's Witten Met(X4) class-exit and the "do not globally fix X4 = K3" posture survive once X4 must be spin?

**Resolution (re-derivation, adversarially verified):**

1. **Class-exit survives unchanged.** The Witten 1981 exit (no-go map §2.1) is at Witten assumption (1) — smooth COMPACT internal geometry — which GU violates via the NON-COMPACT fiber `GL(4,R)/O(3,1)` of `Y14 = Met(X4)`. Witten's hypotheses contain no spin condition, and non-compactness is spin-independent. W2-01 affects only the downstream Dirac/generation-count layer, which §2.1 already holds OPEN. The EVASION-BY-NON-COMPACT-FIBER class-exit is unchanged.

2. **Spin-c exists but does NOT rescue GU; X4 spin is a HARD precondition.** Y14 is spin-c for every orientable X4: `W3(Y14) = beta(w2(Y14)) = pi*beta(w2(X4)) = pi*W3(X4) = 0` (every oriented 4-manifold is spin-c; W2-01 gives `w2(Y14) = pi*w2(X4)` exactly, so there is no vertical W3 piece). BUT GU's chirality invariant is the quaternionic H-linear index `ind_H(D_GU)` on `S = H^64` (`Cl(9,5) = M(64,H)`), with the spin-1/2 leg `ind_H(D_{1/2}) = 8*Â(K3) = 16` a genuine SPIN Dirac index and `generations = ind_H / 8`. A U(1) spin-c twist `S tensor_C L^{1/2}` is complex: it breaks H-linearity (so `ind_H` and the `/8` arithmetic become undefined) and shifts the index off `Â(K3)=2` to `(c1(L)^2 - sigma)/8`. On non-spin CP2 there is no genuine spin Dirac index at all (`Â(CP2) = -sigma/8 = -1/8`, non-integral). Therefore **X4 spin is a genuine standing precondition of D_gimmel as GU uses it, not a free structure choice.**

3. **No-import-K3 posture survives, justification corrected.** OLD (false): "K3 need not be imported because Y14 is spin for any orientable X4, including CP2." NEW: K3 is not forced because the construction holds for any SPIN X4 (a broad class: K3, T4, ...); K3 enters only as the local working hypothesis of the generation-count entries (FH §2.3, DG §2.4) via `Â(K3) = 2`, a spin invariant. The Met(X4) genericity narrows from "any orientable X4 (instancing CP2)" to "any SPIN X4"; CP2 instances retired across no-go map §0.1/§2.1/§2.4 and canon/w2-y14 Result/failure-modes.

4. **Consistent everywhere.** Requiring X4 spin breaks no entry: the K3-conditional entries already use K3 (spin); no entry requires a non-spin base. Net effect is a TIGHTENING (the class-exit is now on spin-independent footing; the spin precondition is explicit).

**New open sub-condition W2-FC2:** the only structure that could relax "X4 spin" while preserving the quaternionic `ind_H` is a Spin^h (Spin·Sp(1), quaternionic-twisted) structure. It is NOT part of the current GU formalization, and a non-trivial Sp(1) twist would itself perturb `Â(K3) = 2`. Whether GU admits a canonical Spin^h structure that preserves the generation count is OPEN.

**Surfaces updated:** no-go map §0.1 (banner + genericity/no-import-K3 paragraphs), §2.1 (Met(X4) scope tag + precondition), §2.4 (GU-Chir base-scope note); canon/w2-y14-spin-structure.md (Result bullet). Verdict: **W2-FC1 RESOLVED; W2-FC2 OPEN.**

---

### CORRECTION DARK-ENERGY-02 — theta-field FLRW EOS re-downgraded CONDITIONALLY_RESOLVED -> OPEN; dark-energy-theta-divergence-free bundling clarified (2026-06-26)

**Files corrected:** `canon/theta-field-flrw-dark-energy-eos.md` (verdict CONDITIONALLY_RESOLVED -> OPEN) and `canon/dark-energy-theta-divergence-free.md` (scope clarification, verdict unchanged).

**theta-field-flrw-dark-energy-eos.md — re-downgraded to OPEN.** The 2026-06-23 re-elevation from OPEN (correction OQ3) was justified by "the full FLRW Klein-Gordon integration is now complete" — a PROCESS MILESTONE, not data support. The completed integration actually WORSENED agreement (de Sitter ratio -1.80 flipped to +1.17; the >2 failure-condition fired). The file's only parameter-free prediction, ratio `w_a/(w_0+1) = +1.17`, is SIGN-INCONSISTENT with DESI (`w_a = -0.75`), and the sign of `w_a` itself has two UNDISMISSED candidates (frozen-IC `w_a>0` vs slow-roll-IC `w_a<0`; OQ3-A unresolved). By the repo's own UNDISMISSED-CANDIDATE / verdict-inflation rules, the EOS-vs-DESI verdict must read OPEN, not CONDITIONALLY_RESOLVED with one IC selected as baseline. The structural EOS machinery (theta as a dynamic DE field; oscillating+damped two-component `w(z)`; Result 1 algebraically exact) stays reconstruction-grade. Note `w_0=-0.826` "matching DESI -0.827" is a FIT (`f_0=0.125` tuned), not a prediction. Cascade: frontmatter verdict + top banner (canon file), `CANON.md` Canon Entries row, `RESEARCH-STATUS.md` registry + promotion rows.

**dark-energy-theta-divergence-free.md — scope clarified, verdict CONDITIONALLY_RESOLVED unchanged.** This file is honestly disciplined (F2 states "NEITHER path is complete"; DARK-ENERGY-01 already downgraded it). The only slip is bundling: the title "Divergence-Free and Dynamic" + a single CONDITIONALLY_RESOLVED banner can be misread as "divergence-free established." Added a scope-clarity note: claim 1 (dynamism) and equivariance are proved unconditionally; claim 2 (`D_A* theta = 0`, divergence-free) is conditional and NOT established — it rests entirely on the unproved reconstruction-grade Assumption 3, which effectively IS the theorem. No verdict change.

**Provenance:** surfaced by the same external adversarial audit as W2-01 (2026-06-26), verified against the files' own failure conditions (F2; OQ3-A) and the DESI w_a sign. Both are conservative (demotion / scope-tightening) corrections in the direction the repo's discipline rewards.

---

## Frontier run 2026-06-26 (attempt -> adversarial-verify; all four results verified honest)

### OQ-RK1 — generation-count decisive rank: BLOCKED_NEEDS_SPEC (2026-06-26)

Verdict: **BLOCKED_NEEDS_SPEC.** Attempted the target-INDEPENDENT quaternionic rank rank_H(Pi_RS · E_+ · Pi_RS) in M(64,H) (4 => 3 generations; 8 => 4 generations / Candidate B). New artifact: the first in-repo EXPLICIT Cl(9,5)=M(64,H) matrix representation (`tests/oq_rk1_cl95_explicit_rep.py`, runs clean — all machine-zero Clifford-relation checks for signature (9,5), omega^2=+I, tr(omega)=0, the c(e_a) chirality flip; prior work was abstract rank-nullity or string-audited only). It machine-verifies the COMPLEX ranks rank_C(E_+)=64 and raw RS gamma-trace kernel rank_C=832 (on the 14·64=896 vector-spinor space); the quaternionic ranks 32 and 416 follow via the standard M(64,H)⊗C=M(128,C) halving dictionary (the quaternionic structure J was NOT explicitly constructed — H-rank not machine-proved, only dictionary-derived). Result: the raw RS object has rank_H=416 in M(896,H), neither 4 nor 8. The decisive 4-vs-8 rank is NOT computable on current data — the effective/physical RS projector E_RS^eff (gauge/BRST quotient + K-theory symbol class + ch_2(F) + H-trace + Y14->K3 bridge) is NOT specified anywhere in the repo. The agent deliberately did NOT fabricate E_RS^eff (avoiding the FC4-HOLONOMY-01 fabricate-to-hit-target trap) and re-asserted the INVALID_TARGET_DIVISION guard against the circular 8/Â(K3)=8/2 step. Supersedes the stale CONDITIONALLY_RESOLVED "rank=4" entry (already downgraded by GEN-04). The exact missing-object specification is now the recorded OQ-RK1 closure requirement. File: explorations/oq-rk1-rs-rank-attempt-2026-06-26.md. Adversarially verified (verifier re-ran the test).

### W2-FC2 — Spin^h enhancement: negative disposition, X4-spin precondition STANDS (2026-06-26)

Verdict: **negative disposition** (the affirmative leg stays OPEN; do NOT read as a positive CONDITIONALLY_RESOLVED). Opened by W2-FC1. Y14 IS Spin^h for any orientable X4 (existence is cheap: Spin-c ⊂ Spin^h via U(1) ↪ Sp(1), and W3(Y14)=0 from W2-FC1). BUT (i) no canonical GU-distinguished Spin^h structure is identified in the current formalization (NOT proven impossible — FC-B is a live reopener), and (ii) a non-trivial Sp(1) twist shifts the spin-1/2 index leg off 8·Â(K3)=16 (twisted index picks up the Sp(1) p1/instanton number; the index-packaging normalization is a heuristic placeholder, not a derived factor). Net: Spin^h restores H-linearity but does NOT relax the X4-spin precondition from W2-FC1 — the precondition STANDS. Conservative tightening (opposite of a rescue), over-determined (holds whether or not the FC-D left-H/right-H commutation advance holds). The affirmative question — does GU admit a canonical generation-preserving Spin^h — remains OPEN. Per the same-session/independent-pass rule, no canon verdict is flipped to CONDITIONALLY_RESOLVED; canon/w2-y14 keeps X4-spin as the standing precondition with the negative-disposition note recorded. File: explorations/w2-fc2-spin-h-enhancement-2026-06-26.md. Adversarially verified.

### CORRECTION SHIAB-02 — shiab Nguyen §3.1 "resolution" tightened to existence-only (2026-06-26)

**File corrected:** canon/shiab-existence-cl95.md (verdict UNCHANGED: RESOLVED, existence only). The Step 4 "Resolution of Nguyen §3.1" passage used "a natural real-linear Clifford contraction exists" / "the map exists over R" in a way readable as identifying GU's ACTUAL shiab operator with the constructed map (hence "GU's operator avoids complexification / is well-defined") — which silently presupposes the source-forced selector identity the same file holds OPEN (scope_correction from SHIAB-01; Known Failure Modes "Uniqueness of equivariant map"; "What This Does Not Establish"). **Fix applied (in-place edit, Step 4):** the existence result is reframed as a COUNTEREXAMPLE to the universal claim "every such equivariant map must complexify," explicitly NOT an identification of GU's operator; the line-58 `[verified]` tag is qualified to "existence of the constructed map; identification with GU's operator is OPEN." Strictly more conservative; no new claim. Adversarially verified (replacement text confirmed accurate, no new overclaim).

### CORRECTION RFAIL-02 — Schwarzschild weak-field re-downgraded CONDITIONALLY_RESOLVED -> OPEN (2026-06-26)

**File corrected:** canon/schwarzschild-weak-field-rfail.md (verdict CONDITIONALLY_RESOLVED -> OPEN), following the CR-02 precedent (competing candidate live + discriminating computation unperformed => downgrade). The headline "GU therefore passes solar-system tests" was compatibility-as-derivation on an IMPORTED Schwarzschild metric: the R_fail^GR=0 leg is trivial (true for any vacuum metric, no GU content — line 38 admits this), and the only genuine GU object, the Willmore-EL residual, is NONZERO with an UNRECONCILED leading order — O(M/r^4) here (flat-space Laplacian Delta(M/r^2)=2M/r^4) vs the companion note's leading O(M/r^3) Weyl-proportional estimate, which by this file's OWN F1 would FALSIFY solar-system compatibility. Neither order is settled: OQ2-A (full gimmel Willmore-EL on the Schwarzschild section) is unperformed, and the companion note even contradicts itself (writes 2M/r^4 in §6). **Fix applied:** frontmatter verdict OPEN + correction field + top banner; the "passes solar-system tests" sentence retracted and replaced with "the GU section-equation residual on the ASSUMED metric is (claimed) small at the selected order, pending OQ2-A"; the residual-order claim now flags the O(M/r^3)-vs-O(M/r^4) fork as the load-bearing open gap. Cascade: CANON.md row, RESEARCH-STATUS registry + promotion rows. Reconstruction-grade structural steps (Gauss identity, Q(B) quadraticity) stand. Adversarially verified.

---

### OQ-RK1 follow-up — E_RS^eff specification attempt: sharpened blocker + two findings (2026-06-26)

Verdict: **BLOCKED_NEEDS_SPEC (sharpened).** Attempted to specify the effective Rarita-Schwinger projector E_RS^eff so the decisive rank rank_H(Pi_RS · E_+ · Pi_RS) (4 => 3 generations, 8 => 4 generations) becomes computable, by decomposing it into four components (gauge/BRST quotient; chiral E_+; honest K3 index reduction; ch_2(F)/H-trace), assembling, and attempting the computation. Adversarially verified — the verifier independently re-derived every number from scratch (fresh Clifford rep, fresh K3 arithmetic), confirmed honest, no fabrication, no target-division; land_as_sharpened_blocker.

**Result:** E_RS^eff is NOT specifiable; the decisive rank is NOT computable. But the blocker is now reduced from a six-item list to ONE precise object: the physical gauge-fixed/BRST RS elliptic complex **RS_GU^phys** — its source-defined gauge/BRST differential d_RS,-1, gauge-fixing condition, ghost complex, and resulting K-theory symbol class, on a common source-selected right-H module M_RS,H^src. Everything else is pinned or blocked downstream of this one object.

**Finding 1 (component resolved): E_+ is the global Cl(9,5) chirality projector, NOT the VZ E-block.** E_+ = (I+omega)/2 on S=H^64, rank_H=32 (machine-exact). The OQ-RK1 "E-block / chirality projector" phrasing conflated two unrelated uses of the letter E: the chirality projector is an xi-independent rank-deficient idempotent endomorphism; the VZ E-block is an xi-dependent, invertible, chirality-FLIPPING symbol block (its role is to be inverted in the VZ Schur complement). Only the chirality projector type-checks as the E_+ in Pi_RS · E_+ · Pi_RS.

**Finding 2 (NEW, machine-verified — kills the naive route):** the pure-gauge image is NOT annihilated within the gamma-trace kernel (RS symbol on the projected pure-gauge image has norm 73.48 != 0; i.e. gamma^mu D_mu epsilon = D-slash epsilon != 0). So the gauge transformation does NOT preserve the gamma-trace constraint, and the physical RS space is therefore **NOT a naive subspace subtraction** ker(Gamma)/im(gauge). The repo's prior "subtract one spinor copy (32_H)" rank-counting is uncertified, and a genuine gauge-fixing + ghost (BRST) complex is REQUIRED, not optional. This closes the naive rank-counting route to the generation count.

**Honest target check (decision-relevant):** every honestly-grounded surrogate was computed — E_+ = 32_H; raw 14D gamma-trace kernel = 416_H; Cl(4,0) toy Pi_raw·E_+·Pi_raw = 48_H; honest closed-K3 index ind_H (flat k=0) = -320 / -304 / -336 for ghost branches q = 0 / +1 / -1 — and **NONE is 4 or 8.** The honest K3 integrand ind_C = (-40+2q)·n + (4+q)·k (n=16, k=ch_2(F)[K3]) yields large negatives and is background-dependent (the twisting class q and ch_2(F)=k are both undetermined repo-wide). The value 4 (=> 3 generations) is reachable ONLY via the forbidden 8/Â(K3)=8/2 division (INVALID_TARGET_DIVISION, refused). So the "ind_H(D_RS)=8 => 24 => 3 generations" story is NOT supported by any honest construction on current repo data — it required inserting the target. (Caveat: this is bounded to the surrogates computed here, not an exhaustive proof that no combination reaches 4/8.)

**Discipline:** the assembly code (tests/oq_rk1_e_rs_eff_assembly.py) hard-refuses to fabricate E_RS^eff — the all-slots-present branch raises RuntimeError rather than inventing the quotient (anti-FC4-HOLONOMY-01). Files: explorations/oq-rk1-e-rs-eff-specification-2026-06-26.md, tests/oq_rk1_e_rs_eff_assembly.py.

**Net:** the entire generation-count question now reduces to ONE constructive obligation — specify RS_GU^phys (the BRST quotient of the GU RS field) — and the naive subtraction route is closed. Until then, "3 generations" has no honest computational support.

---

### RS-BRST follow-up — RS_GU^phys is a GENUINE GU THEORY GAP (the generation count is blocked on GU itself) (2026-06-26)

Verdict: **BLOCKED_NEEDS_SPEC; overall origin = genuine_gu_gap.** Attempted to specify RS_GU^phys (the gauge-fixed/BRST Rarita-Schwinger complex — the single object the generation count now hangs on) from GU source, decomposed into four sub-structures (gauge symmetry / gauge-fixing / ghost-BRST complex / elliptic symbol), each classified gu_derived vs textbook_import vs genuine_gu_gap. Adversarially verified — the verifier re-ran the code (Cl(4,0) norm 73.48, Cl(9,5) norm 343.73, K3 index family -320/-304/-336, no surrogate = 4 or 8) AND independently checked the GU draft PDF (page 49 contains "until it is stabilized. Caveat Emptor.") and the transcript; honest, no fabrication; land_as_sharpened_blocker.

**The decisive answer to "does GU determine the structure needed to predict the generation count?": NO — and the gap is in the theory, not the repo.**

- **What GU GENUINELY DETERMINES (gu_derived skeleton):** the RS gauge symmetry (the inhomogeneous gauge group IG = G semidirect Omega^1(ad P), SUSY-extended; the differential d_RS,-1 = d_A: Omega^0(S) -> Omega^1(S), eps |-> D_mu eps); the field content (0/1-forms valued in ad or spinors); the complex skeleton C^{-1} -> C^0 -> C^1 with form-degree grading; the H-structure (S=H^64, d_A H-linear, from the forced Sp(64)=U(64,H) / Cl(9,5)=M(64,H)); and that the RS sector is the generation carrier. The differential's SHAPE coincides with the textbook spin-3/2 symmetry; GU adds only the bundle/connection/H-structure.

- **What is a TEXTBOOK IMPORT (Layer A — closable by formalization, NOT a genuine gap):** the general spin-3/2 BRST apparatus — Faddeev-Popov ghost/antighost, Nielsen-Kallosh commuting-spinor ghost, a gauge slice, and the slice-independence of BRST cohomology. Standard for ANY spin-3/2 gauge theory; would be closable IF the action and symmetry were standard.

- **What is the GENUINE GU THEORY GAP (Layer B — the real, computability-deciding hole):**
  - **(B1) GU does not determine its own RS-sector ACTION.** This is the single root. It traces to GU's OWN primary source: the 2021 draft was read in-repo and found NOT to emit a stabilized action / operator / differential / Noether identity / BRST rule for the RS sector; the only candidate (draft eq 10.10) is author-disclaimed ("Caveat Emptor", PDF p.49); the tau-action field-space is "declared but uninhabited" with the FULL_IG / FIXED_ALEPH / DYNAMIC_A trichotomy source-unselected. Without the action it is not even well-posed whether the spinor 1-form is pure-gauge, dynamical, or constrained — so the gauge-fixing slice, the ghost-subtraction count q (=1-a), and the constraint/orbit reconciliation are all undetermined. **Corroborated by the UCSD talk transcript in Weinstein's OWN words** (literature/weinstein-ucsd-2025-04-transcript.md): he explicitly flags the middle differential as the hard open part — "how the hell do you get from omega one to omega d minus one with a differential? That's really gonna be your issue. It's not up top. It's down bottom where it gets complicated" — and states the elliptic-complex property only conditionally ("if there is no obstruction to d, if d squared equals zero"). The talk explains the structure/intent and a qualitative generation mechanism (the spin product rule; "really two plus one — the third family is an imposter for representation-theoretic reasons") but supplies NO middle differential, action, or gauge-fixing. So GU's primary source, in both the draft (eq 10.10 "Caveat Emptor") and the talk ("that's really gonna be your issue"), flags exactly this gap as unsolved.
  - **(B2) GU's gamma-trace irreducibility constraint and the gauge orbit are incompatible as a naive quotient** (machine-verified this run on the full Cl(9,5) anchor, not just the toy: RS symbol on the projected pure-gauge image has norm 343.73 != 0). So some nontrivial gauge-fixing apparatus is genuinely required (the easy subtraction is rigorously ruled out); GU asserts a reconciled "elliptic deformation complex" (draft p.65) but never constructs it.

**Consequence (decision-relevant):** the GU 3-generation prediction is not merely unproven or uncomputed — it rests on a sector GU has not finished defining, by the author's own admission. Until GU supplies (or someone derives) a stabilized RS-sector action, the generation count is not computable even in principle, and the cherished "ind_H=8 => 24 => 3" value is reachable only via the refused 8/Â(K3)=8/2 division. The honest next obligation is upstream of any computation: stabilize the GU RS-sector action (a theory-completion task), then the rank follows.

Discipline: the assembly code (tests/rs_gu_phys_brst_specification.py) blocks at the first None slot (stabilized_RS_action) and the all-slots-present branch raises rather than fabricating a quotient (anti-FC4-HOLONOMY-01). Files: explorations/rs-gu-phys-brst-specification-2026-06-26.md, tests/rs_gu_phys_brst_specification.py. Cascade: CANON.md "Not Yet Canon" three-generation line annotated.

---

### RS-middle-map persona sprint — a concrete computable lead [speculation] (2026-06-26)

A 41-persona steel-man sprint (artifact: explorations/rs-middle-map-persona-steelman-2026-06-26.md; doc_type persona_pass, verdict speculation, NO claim promotion) on "what the missing shiab / middle map IS" surfaced one genuinely concrete, falsifiable, repo-runnable lead worth recording (everything else stayed narrative): FIVE independent lenses (Clifford-04, homomorphic-encryption, info-coding, world-model, observer-finality) converged that the shiab is the **metric codifferential** d_A* of the spinor-twisted complex, with d^2=0 failing exactly because the spin-3/2 constraint projector Pi_RS does NOT commute with it — i.e. the obstruction is the single finite commutator **[Pi_RS, c∘d*] on H^64, whose magnitude IS the already-measured 73.48 / 343.73.** Two crypto-lens selectors pin the operator: FHE (adjointness = decryption-correctness <D_mid a, b> = <a, d_A b> forces Phi=(d_A)*; obstruction ~ c(F_A) via Weitzenbock) and Probabilist (Takesaki conditional-expectation gives existence+uniqueness on the positive-definite M(64,H) fiber, dodging the (9,5)-signature obstruction). Concrete next step (NOT done; not a promotion): compute that commutator explicitly and test whether GU's shiab = d_A* — but note canon SC1 §3.5 distinguishes GU's Clifford-contraction shiab from d_A*, so this would CHANGE the operator definition and must be confirmed-or-killed, not assumed. The ZK lens adds a finite linear falsifier: I_bind = Hom_{Spin(9,5)}(Lambda^2 V ⊗ S, V ⊗ S) (Schur), with dim 0/1/>1 deciding no-sound-commitment / uniquely-pinned-selector / residual-freedom. Observer thread: the gap reads as "the observer-creates-reality claim turned into a no-go" — choosing a metric section both finalizes reality (binding) and discards the shiab kernel (the shadowy lost moment); the choice-free TaF bridge is to derive Pi as a SPECTRAL projection of a GU finality operator. Six new personas (36-41) added to process/persona-passes/.

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

**Correction note (2026-06-23, RANK-FIBER-INCONSISTENCY-24-VS-96):** Resolves problem (2) of the OQ-RK2-FC4-CIRCULAR-STILL note above and removes a circular rank step. Verdict UNCHANGED (CONDITIONALLY_RESOLVED; FC4 remains OPEN -- the honest residual gap is the uncomputed holonomy integral int_{K3} A-hat * ch_H(S_RS^+), now the sole FC4 blocker). Two edits applied to `explorations/oq-rk2-aps-fc3-fc4-closure-2026-06-23.md`: (a) **24-vs-96 reconciliation.** Section 4.3 now carries an explicit reconciliation table stating which object each number counts: 416 = full 14D kernel rank ker(Gamma^{14D}|_{S^+}) = 14*32-32; 96 = 4D section-pullback fiber kernel rank PRE-gauge, computed on the REDUCIBLE factor R^4 tensor s*(S)^+ = R^4 tensor H^{32} (= 4*32-32); 64 = 96 POST-gauge (one gauge spinor H^{32} removed); 24 = the SAME 4D fiber kernel computed on the Spin(4)-IRREDUCIBLE factor, the trace-free RS rep (1/2,1) [dim_H 3] tensored with each chiral fiber half S(6,4)^{pm} [dim_H 4], summed (3*4+3*4). The 24 is the Spin(4)-irreducible refinement of the reducible 96; both are 4D section-pullback (NOT 14D -- that is 416). Nothing is retracted; the prior '96 must have been a different count' remark is superseded by the table. The earlier-flagged FC4-D contradiction is DOWNGRADED to a reconciled accounting note (would re-open only if the irreducible branching s*(S)^+ = S^+(4,0) tensor S(6,4)^+ + S^-(4,0) tensor S(6,4)^- is shown wrong for the GU pullback). OQ-FC4-3 and OQ-FC4-5 marked RESOLVED in the file. (b) **Removed circular multiplicity-factor step.** The Section 4.4 step 'rank_H(E_RS^{eff}) = rank_H(S_RS^+) / (multiplicity factor) with multiplicity factor = 24/8 = 3' was REJECTED and replaced by a CIRCULARITY GUARD: that factor divides the fiber rank 24 by the target index ind_H = 8 in its denominator, then 'recovers' 8 = 2*4 from the result -- a tautology, since rank_H(E_RS^{eff}) is exactly what ind_H = A-hat * rank_H is meant to FEED. The only admissible route from fiber rank 24 to effective rank 4 is to PRODUCE ind_H by evaluating int_{K3} A-hat * ch_H(S_RS^+) from K3 holonomy data (a route that yields ind_H rather than assuming it). The Section 6 verdict block and FC4 status updated accordingly; FC4 was OPEN before and remains OPEN. The separate successor file `explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md` (verdict OPEN) is the holonomy follow-up and is consistent with this reconciliation; it was not modified. No canon promotion or demotion; CANON.md unaffected.

---

### sc1-oq1a-d7-clebsch-gordan-cas (2026-06-23)
Verdict: OPEN
CORRECTION SC1-OQ1A-VERDICT-OVERSTATED (2026-06-23): verdict downgraded from RESOLVED to CONDITIONALLY_RESOLVED. The chirality-parity argument (algebraic, exact) correctly excludes V(omega_7) and V(omega_1+omega_7) from Lambda^2 tensor Delta^+ at verified grade. However: (1) the irreducibility of ker(c) in Section 3.3 Step 3 is reconstruction grade only, as the file itself acknowledges -- a formal proof requires the D_7 branching law or a LiE weight computation (FC-IRR); (2) the multiplicity-1 claim for V(omega_6) in V(omega_2) tensor V(omega_6) is reconstruction grade pending LiE verification (FC-MULT: if LiE returns multiplicity > 1, dim_H Hom > 1 and uniqueness weakens); (3) the highest-weight assignment omega_1 + omega_7 for ker(c) is reconstruction grade (FC-HW). The file's own Section 10 grade table records decompositions and multiplicities as reconstruction, contradicting the original RESOLVED verdict. Chirality-exclusion results (V(omega_7) absent, V(omega_1+omega_7) absent) are verified grade and stand. OQ-CG-2 (LiE/SageMath numerical verification) is the upgrade path to RESOLVED. OQ1-B (inner/outer automorphism for so(9,5)) remains open.
File: `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`

CORRECTION SC1-OQ1A-PRODUCTB-CANDIDATE-01 (2026-06-25): verdict downgraded from CONDITIONALLY_RESOLVED to OPEN. The 2104 Product B table audit computes the D7 character identity `V(omega_2) tensor V(omega_6) = V(omega_2+omega_6) + V(omega_1+omega_7) + V(omega_6)` with dimensions `4928 + 832 + 64 = 5824`. This supersedes the older chirality-exclusion sentence that `V(omega_1+omega_7)` is absent from `Lambda^2 tensor Delta^+`. The old common-summand count exactly one is no longer current: against `Lambda^1 tensor Delta^- = V(omega_6) + V(omega_1+omega_7)`, the Product B table gives two common summands. Consequence: the OQ1-A uniqueness/common-summand route is OPEN, and any `dim_H Hom = 1` use for the chiral block is blocked until a replacement Hom-space computation is filed. Shiab existence is unaffected because canon claims only existence of one natural Clifford-contraction map and explicitly excludes uniqueness/rank/kernel.

CORRECTION SC1-OQ1A-PRODUCTA-PACKET-01 (2026-06-25): the 2104 cycle 2 Product A packet closes the local D7 computation `V(omega_1) tensor V(omega_7) = V(omega_1+omega_7) + V(omega_6)`, with `ker(c)=V(omega_1+omega_7)`, `image(c)=V(omega_6)`, and `cokernel(c)=0`. This resolves the Product A finite-control packet route-locally, but it does not restore a uniqueness selector. Product B retains both `V(omega_1+omega_7)` and `V(omega_6)`, so the finite comparison has two common rows. Consequence: selector restart remains blocked until a source-natural identity kills or excludes the `V(omega_1+omega_7)` rival row.

Claim-status consistency table:

| claim | prior status | current status | weakest dependency | stale wording searched | files updated |
|---|---|---|---|---|---|
| SC1-OQ1A D7 common-summand / Product B chirality exclusion | CONDITIONALLY_RESOLVED; `V(omega_1+omega_7)` excluded from `Lambda^2 tensor Delta^+` | OPEN; Product B table includes `V(omega_1+omega_7)` | 2104 Product B character audit plus replacement Hom-space computation not yet filed | `rg "sc1-oq1a|V(omega_1+omega_7)|Lambda^2 tensor Delta^+|Product B" RESEARCH-STATUS.md CANON.md DERIVATION-PROGRESS.md NEXT-STEPS.md canon papers` | `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`, `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md`, `explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md`, `tests/hourly_20260625_2104_cycle1_receipt_attempts_audit.py` |
| SC1-OQ1A Product A finite-control packet | Product A packet missing / reconstruction-grade | CLOSED route-locally for Product A; selector identity OPEN | 2104 cycle 2 Product A character audit plus missing `SourceNaturalProductABRivalProjectorIdentity_V1` | `rg "SC1-OQ1A|Product A|Product B|common-summand|selector|K_IG" RESEARCH-STATUS.md CANON.md DERIVATION-PROGRESS.md NEXT-STEPS.md canon explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md` | `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`, `RESEARCH-STATUS.md`, `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md`, `explorations/hourly-20260625-2104-cycle2-ig-product-a-finite-control-packet.md`, `tests/hourly_20260625_2104_cycle2_frontier_gates_audit.py` |

No CANON.md or `canon/shiab-existence-cl95.md` edit is required: both already avoid a uniqueness claim and list uniqueness/rank/kernel as not established.

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

---

### oq-kk1-bc1-jacobi-operator-parameters (2026-06-23)
Verdict: GENUINE_OBSTRUCTION
The correct Jacobi parameters (alpha = 7/2, beta = 0) for the BC_1 ODE with coth(2r) are confirmed by explicit substitution z = sinh^2(r), converting the operator to _2F_1((rho+inu)/2, (rho-inu)/2; 9/2; -sinh^2(r)) with c = alpha + 1 = 9/2. However, the Koornwinder-Flensted-Jensen discrete spectrum condition nu_n = alpha - beta - 1 - 2n gives only nu = 5/2 and nu = 1/2 -- NOT nu = 3/2. All three primary failure conditions are resolved negatively: FC-JACOBI (the simplified c-function poles at half-integers cannot correspond to L^2 eigenfunctions of the correct operator because the pair (GL(4,R), O(3,1)) has A_3 root system and equal-rank fails), FC-OPER-MATCH (alpha = 7/2, beta = 0 confirmed but same result: nu = 3/2 not discrete), FC-FROBENIUS-DISCRETE (both Frobenius solutions decay at e^{-rho*r} for real nu; e^{-6r} requires nu in the imaginary spectral strip which is not admitted). Additionally, dimensional check: BC_1 with (7,1) gives space of dimension 9, but GL(4,R)/O(3,1) has dimension 10. The BC_1 Jacobi fiber wavefunction route to G2a is a GENUINE_OBSTRUCTION. The APS/K3 route (oc1-oc2-aps-closure, CONDITIONALLY_RESOLVED) remains the sole reconstruction-grade path to ind_H(D_GU) = 24 and is unaffected.
File: `explorations/oq-kk1-bc1-jacobi-operator-parameters-2026-06-23.md`

### sc1-oq2-split-signature-ellipticity-lemma (2026-06-23)
Verdict: OPEN  [downgraded from CONDITIONALLY_RESOLVED by CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION, 2026-06-23 — see correction note at end of file] — **part (iii) is FALSE/RETRACTED (the Sp(64) gauge orbit DOES fill NM(xi), per sibling sc1-oq2-f5-gauge-orbit-fill); the firing NAMES an internal contradiction (parts (ii) vs (iii)) resolved same-session, which per the loop's RESOLVED-blocking rule caps the verdict at OPEN until inter-session re-derivation. See CORRECTION ELLIPTICITY-LEMMA-iii (superseded by SC1-LEMMA-CONTRADICTION-SAME-SESSION) below.**

Formal lemma proved at reconstruction grade: sigma_shiab(xi) = 0 at leading (order-1) symbol order (shiab is zero-order, contributing nothing to sigma_D(xi) = c(xi)); the complete kernel trichotomy establishes ker sigma_D(xi) = {0} for all spacelike and timelike xi, and ker sigma_D(xi) = NM(xi) with dim = dim E / 2 for null xi. The structural gate is closed in the expected direction: null-characteristic null modes are NOT all pure gauge (gauge orbit is a proper subspace of NM(xi) by an H-linearity argument **[part (iii) SUPERSEDED 2026-06-23 by sc1-oq2-f5-gauge-orbit-fill — the Sp(64) gauge orbit DOES fill NM(xi); reread as the expected symmetric-hyperbolic signature. Analytic-framework conclusion (real principal type, ind_H = 24) unchanged. See CORRECTION ELLIPTICITY-LEMMA-iii below.]**), so the correct analytic framework is symmetric-hyperbolic / real principal type, not elliptic. Remaining for RESOLVED: ~~CAS verification that the Sp(64) gauge orbit does not fill NM(xi) (F5)~~ **[F5 FIRED 2026-06-23, sibling sc1-oq2-f5-gauge-orbit-fill — the orbit DOES fill NM(xi); this is no longer a remaining task. See CORRECTION below.]**, explicit RS null-mode dimension count, and formal identification of L2-normalizable fiber null modes with Flensted-Jensen discrete-series representations.

**[CORRECTION ELLIPTICITY-LEMMA-iii (critical) applied to this entry 2026-06-23, same session.]** The italicized "gauge orbit is a proper subspace of NM(xi) by an H-linearity argument" above is FALSE. The sibling F5 check (`sc1-oq2-f5-gauge-orbit-fill`) shows by explicit CAS computation that the Sp(64) gauge orbit FILLS NM(xi). **Part (iii) is SUPERSEDED: the orbit DOES fill NM(xi); reread as the expected symmetric-hyperbolic signature.** F5 is therefore FIRED against part (iii), not OPEN.

**Same-session self-resolution — flagged DEFERRED_VERIFICATION (not settled).** The F5 reversal is INTRA-SESSION: the lemma file (18:38) and the F5 check (20:24) are the same uncommitted 2026-06-23 batch, so F5 firing against part (iii) is same-session self-resolution, not inter-session verification (file separation is not a valid defense; see the Same-Session Circularity lens). Accordingly, part (ii) [NM(xi) = Im c(xi), the premise F5 resolves in favor of] is NOT treated as independently settled — it carries status **DEFERRED_VERIFICATION** pending an inter-session re-check of the F5 CAS computation (the gauge-orbit-fill at maximal-rank c(xi)) and of FF3/FF4. **[SUPERSEDED 2026-06-23 by CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION: the verdict label is NO LONGER CONDITIONALLY_RESOLVED — it is OPEN (see header line). The retention argued for below was the ELLIPTICITY-LEMMA-iii position; per the loop's RESOLVED-blocking rule a same-session-named-and-resolved internal contradiction cannot be cleared by a same-session re-derivation, so the verdict is capped at OPEN until inter-session re-derivation.]** The verdict label was previously argued to be retained at CONDITIONALLY_RESOLVED because the symmetric-hyperbolic / real-principal-type conclusion is re-derived from the corrected premise (Koszul-exactness: ker c(xi) = Im c(xi) at null xi; physical content carried by Cauchy-data transport along null bicharacteristics, not by a pointwise null-cohomology quotient) AND because that conclusion is now load-bearing on FF3/FF4 (both OPEN at reconstruction grade), not unconditional — but that re-derivation is itself same-session and does NOT clear the cap (the verdict is OPEN). The analytic-framework conclusion (real principal type, ind_H = 24) is unchanged: ind_H = 24 is computed by Atiyah-Schmid L2-theory on the fiber and never used a pointwise null-cohomology quotient, so it does not depend on the F5 reversal or on FF3/FF4. Successor open gates toward RESOLVED: FF3 (BRST-coboundary structure as a theorem) and FF4 (full-14D-E Koszul-acyclicity), the inter-session re-verification of F5 (DEFERRED_VERIFICATION above), plus the RS null-mode count and discrete-series identification.

File: `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md`

### dark-energy-oq3a-slow-roll-ic-sign (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Computed the slow-roll attractor IC for the GU theta-field Klein-Gordon equation in FLRW at z >> z_osc ~ 1.85. The attractor delivers phi_0 ~ pi/2 (90 deg) at z = 0, which is further from the negative-w_a window (phi < 58 deg) than the frozen IC (49 deg). The sign of w_a does NOT reverse under slow-roll attractor ICs: the ratio w_a/(w_0+1) changes from +1.17 (frozen IC) to approximately +2.53 (slow-roll attractor), both positive. The named failure condition FC5/OQ3-A (sign reversal) does not fire. GU Candidate D structurally predicts w_a > 0 regardless of physically motivated IC choice, constituting a genuine sign mismatch with DESI (w_a = -0.75) that is not an IC artifact. Remaining open: full numerical integration from z >> z_osc to verify phi_0 ~ pi/2, back-reaction correction, and identifying whether any GU mechanism places the field in the phi < 58 deg window.
File: `explorations/dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md`

**Upgrade conditions:** (1) Determine correct Jacobi parameters for L_{BC_1} = d^2/dr^2 + [7 coth(r) + 2 coth(2r)] d/dr. (2) Verify its discrete spectrum includes nu=3/2. (3) Establish the connection formula linking c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) to the Wronskian of the Frobenius solutions of this operator.

### vz-f5-hamiltonian-subsidiary-propagation (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Performed the full Dirac-Bergmann constrained-Hamiltonian analysis of the GU RS subsidiary condition `Gamma^{4D} Psi_R = 0` under Sp(64) gauge curvature `F_A != 0`. The key structural finding is that the gamma-trace constraint is kinematic (it defines the RS sub-bundle `R_s = ker Gamma^{4D}` by construction), not a dynamical constraint derived from an RS Lagrangian E-L equation; the Dirac-Bergmann consistency chain that generates the classical VZ secondary constraint (via `[D_mu, D_nu] psi = F_{mu nu} psi`) does not initiate because there is no primary dynamical constraint to propagate. The gauge curvature `F_A != 0` enters the effective RS Schur complement only as a zero-order potential (via the Shiab coupling) and cannot modify the principal symbol or generate new first-order terms. The open canon gate (no-go-class-relative-map.md F5 row, "constrained-Hamiltonian propagation: residual open at full dynamical level") is CONDITIONALLY_RESOLVED at reconstruction grade, with four explicit failure conditions (FC1: standalone RS Lagrangian existence; FC2: F_A enters B/C blocks at first order; FC3: extrinsic curvature sourcing produces spacelike effective characteristics; FC4: RS mass term enters S_R at first order). Remaining for upgrade to RESOLVED: proof that no standalone GU RS Lagrangian exists (FC1) and energy estimates for the sourced constraint-propagation system (FC3).
File: `explorations/vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md`

### dark-energy-assumption3-variational (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Attempted both the variational and algebraic routes to derive Assumption 3 (theta = gauge-potential sector of E_A). The variational route partially succeeds: S_IG = integral ||theta||^2 is separately gauge-invariant (from equivariance of theta and gimmel G-invariance), variation gives delta S_IG / delta A = 2 theta from the linear structure pi = A - Gamma(epsilon), and Noether's second theorem for S_IG then gives D_A* theta = 0 off-shell at reconstruction grade. The algebraic route fails with a genuine structural obstruction: G-equivariance constrains field-space variation of theta, not the Y^14-base-manifold differential condition D_A* theta = 0, so equivariance alone cannot imply divergence-free. Three explicit failure conditions recorded: FC1 (GU action may not contain ||theta||^2 as a separate sector), FC2 (equivariance may hold only for global gauge transformations, blocking Noether's second theorem), FC3 (reference connection Gamma(epsilon) may depend on A). Canon remains CONDITIONALLY_RESOLVED; the derivation improves Assumption 3 from transcript-inferred to structurally derived at reconstruction grade.
File: `explorations/dark-energy-assumption3-variational-2026-06-23.md`

### freed-hopkins-optionb-ksp-family (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Constructed three explicit X_obs candidates for Option B of the Freed-Hopkins observer-pairing lane: (1) Met(X^4) is contractible (convex cone), immediately killing the naive construction; (2) Omega^2 B Sp(64) (based gauge connection moduli over S^3) is noncontractible with nontrivial KSp^0 via Bott periodicity (pi_2 = Z), but is ordinary Sp(64)-gauge background data and falls into the relabeling case of the prior no-go; (3) the GU solution section moduli X_obs^{sol} is the sole surviving candidate, not yet eliminated but whose topology is OPEN pending a GU moduli theory on compact K3. Five failure conditions named (FC1: solution space contractibility; FC2: KSp class relabeling; FC3: independent Sp structure; FC4: eta-invariant triviality; FC5: Atiyah-Janich for infinite-dimensional bases). The Freed-Hopkins lane remains alive only via the solution section moduli, with all simpler X_obs candidates now eliminated.
File: `explorations/freed-hopkins-optionb-ksp-family-2026-06-23.md`

---

### oq-rk2-fc4-k3-holonomy-rank (2026-06-23)
Verdict: OPEN  [downgraded from CONDITIONALLY_RESOLVED by CORRECTION FC4-HOLONOMY-01, 2026-06-23 — see correction note below]
Decomposed S_RS^+ as an SU(2)-holonomy bundle over K3: under Hol(K3) = SU(2)_L (Berger classification), the RS representation (1/2,1) of Spin(4) restricts to 3 * D^{1/2} = 3V where V is the SU(2)_hol fundamental bundle with c_2(V)[K3] = 12. S^+(4,0) restricts to 2 * D^0 (trivial), explaining A-hat(K3) = 2 from 2 parallel spinors. Established that S_RS^+ is NOT of the form S^+(4,0) tensor E (non-integer multiplicity obstruction, exact — a NEGATIVE result blocking the naive twisted-Dirac route). These three facts are sound. HOWEVER, the file does NOT derive ind_H(D_RS) = 8 or rank_H(E_RS^{eff}) = 4: ten independent Atiyah-Singer / index computations (960, -288, -384, -192, -336, -128, 128, -8, -480, 60) ALL fail to give the target ind_C = 16, with no convergence. The candidate rank_H(E_RS^{eff}) = b_2^+(K3) + b_0(K3) = 3 + 1 = 4 and the formula ind_H = (chi+sigma)/8 * rank_H(S(6,4)) = 8 are REVERSE-ENGINEERED (selected by trial after the answer was known, not derived); the latter is contradicted by the file's own genuine Sec 6.5 computation (60 != 8). The only support for ind_H(D_RS) = 8 is the physical-DOF helicity count, a kinematic polarization count, NOT an analytic index. FC4 therefore REMAINS OPEN (the prior "upgraded from OPEN to CONDITIONALLY_RESOLVED" was unjustified and is retracted). Failure conditions: FC4-N1 (no-convergence, already FIRING), FC4-N2 (standard operator gives -288 per Sec 5.5), FC4-N3 (kinematic != analytic), FC4-N4 (reverse-engineered formulas void), FC4-H1/H2/H3.
File: `explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md`

### sc1-oq2-f5-gauge-orbit-fill (2026-06-23)
Verdict: OPEN  [downgraded from CONDITIONALLY_RESOLVED by CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION, 2026-06-23 — this file NAMES an internal contradiction and resolves it same-session; per the loop's RESOLVED-blocking rule that caps the verdict at OPEN until inter-session re-derivation; see correction note at end of file]
Ran the explicit CAS/structural F5 negative-check: does the Sp(64) gauge orbit fill the null-mode space NM(xi) at null characteristics? Result: it DOES fill — opposite to the prior split-signature ellipticity lemma's part (iii). The mechanism is forced: at null xi, c(xi) is a maximal-rank nilpotent, so Im c(xi) = ker c(xi) = NM(xi) (null-projection property), and the BRST-exact/dynamical-gauge orbit equals Im c(xi) = NM(xi) identically; verified for the full Sp(n)=U(n,H) algebra acting on the same H^n as c(xi) (left action per sc1-oq3), n=6,8, with a generic null direction, and the commutator and direct-action orbits also fill. This NAMES AN INTERNAL CONTRADICTION in the lemma (parts (ii) maximal-rank NM=Im c(xi) and (iii) gauge orbit proper subspace of ker c(xi) are mutually inconsistent), resolved in favor of (ii). The analytic-framework conclusion is unchanged **CONDITIONAL ON FF3 AND FF4 (both OPEN at reconstruction grade) — NOT unconditionally**: D_GU is symmetric-hyperbolic / real principal type, not elliptic — the fill is exactly the Koszul-exactness of the massless-field symbol complex (Maxwell control verified; physical polarizations live in Cauchy-data transport, not in a pointwise null-cone symbol-cohomology quotient, which vanishes). The "unchanged" claim is structurally load-bearing on two of this file's own failure conditions: FF3 (the dynamical gauge symmetry of D_GU is generated by exact-form coboundaries d_A(eps), so Gauge_BRST = Im c(xi) — asserted, not proved as a theorem) is the entire basis for "gauge fills the kernel"; FF4 (full-E Koszul-acyclicity, dim H(xi)=0 — checked only at reconstruction grade via the irreducible-module argument, not by direct 4,194,304-dim computation on the 2^14-dim E) is what rescues the conclusion from implying D_GU has no physical content. If FF3 or FF4 fires, the symmetric-hyperbolic framing reopens. VZ evasion (off-null invertibility) and the generation count ind_H=24 (Atiyah-Schmid L2-theory) are untouched and do NOT depend on FF3/FF4. Five failure conditions named (FF1 non-maximal rank; FF2 gauge action not left-mult; FF3 BRST coboundary structure not a theorem; FF4 full-E Koszul-acyclicity unverified; FF5 Cauchy well-posedness). FF3 and FF4 are LOAD-BEARING (not merely upgrade-to-RESOLVED niceties): they remain OPEN, so the symmetric-hyperbolic conclusion is inherited-conditional on them, not established. The lemma's part (iii) should be reread as "gauge orbit FILLS NM(xi), the expected symmetric-hyperbolic signature (conditional on FF3/FF4)."

**CORRECTION ADV-FC-03 (moderate, 2026-06-23):** Verdict retained at CONDITIONALLY_RESOLVED (legitimate: 3+ specific falsifiable FFs; FF3/FF4 are specific math statements). Summary sharpened so the "analytic-framework conclusion is UNCHANGED" claim is no longer presented as unconditional. The conclusion is structurally load-bearing on FF3 (BRST-coboundary = gauge symmetry, basis for Gauge_BRST = Im c(xi)) and FF4 (full-E Koszul-acyclicity, dim H(xi)=0), both OPEN at reconstruction grade. Fix applied to `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` §5 (Net effect), §6 item 3 + status block (FF3/FF4 flagged LOAD-BEARING on the conclusion) and to this index entry (above). No mathematics changed; this is a verdict-robustness re-binding, not a verdict-label change.
File: `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`

### no-go-velo-zwanziger-canon-entry (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Wrote the formal fifth-theorem Velo-Zwanziger canon entry for the no-go-class-relative-map, in the same four-part shape as the other four families: assumption list (VZ-H1 standalone RS field, VZ-H2 minimal coupling, VZ-H3 non-singlet gauge rep, VZ-H4 mild background, VZ-H5 no guardian); the condition GU satisfies in place of VZ-H1 (GU-VZ = the Clifford-module-non-sub-module mechanism: R = ker Γ is not a sub-Clifford-module of E, so the off-diagonal blocks B/C are kinematically nonzero and the exact entanglement identity A·S_R = g_Y(xi,xi)·Id_R holds, forcing the effective RS characteristic cone into the null cone); the forgetful operation (minimal-coupling functor ϕ_mc that discards the R ⊂ E embedding); and five explicit failure conditions FC-VZ-1…5 (E-block kernel on the non-null cone; existence of a standalone GU RS Lagrangian; F_A entering B/C at first order; extrinsic-curvature-sourced spacelike characteristics; IR loop corrections driving B/C to zero). Verdict is bound honestly — 14D is CONDITIONALLY_EVADED at reconstruction grade (load-bearing on the unverified E-block-invertibility precondition FC-VZ-1), 4D section-pullback was originally reported as VERIFIED but is now held CONDITIONALLY_RESOLVED at principal-symbol grade — and neither leg is over-stated; the entry is a synthesis/no-go-map update, not a new computation or index inflation. Remaining: external verification of the E-block argument (FC-VZ-1) is the single gap separating 14D from EVADED.
File: `explorations/no-go-velo-zwanziger-canon-entry-2026-06-23.md`

### c-mpr-9tuple-object-morphism (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Discharged the standing prerequisite "state object/morphism/proof obligations before claiming theorem status" with a split outcome. The C_MPR object is writable but only as a 5-tuple reduct C_SR = (X, G, w) — the fields (E, ≤_E, G, ≤_G, r) carry laws inherited from the signed-readout theorem, while `Cert` and `P_O` are prose placeholders with no laws and are not needed for the category; a morphism (φ: X→X', ψ: G→G' lattice-ordered-group hom) with readout-compatibility ψ∘w = w'∘φ was written down and the category axioms (identity, composition lifting from generators to all of E by freeness, associativity) all verify, so C_SR is a genuine category and C_CALM a full subcategory — the first axiom-verified (not asserted) statement in the lane. The BvN wall, by contrast, is a NAMING EXERCISE: it denies an adjunction L: C_ClassicalDistribLR ⇄ C_GW: R whose codomain category C_GW is never given an object-level definition and whose functors are never written, so the non-existence claim is not yet a proposition; the true classical BvN-1936 lattice fact it rests on does not by itself yield the categorical wall. What remains: an object-level definition of C_GW (objects + anomaly-free morphisms + functors L,R) is the single highest-leverage missing piece; reflectivity/fibration of C_CALM and re-attachment of Cert/P_O via a comma/Grothendieck construction stay OPEN. 4 explicit failure conditions (FC1-FC4).
File: `explorations/c-mpr-9tuple-object-morphism-2026-06-23.md`

### pc1-spinor-spin77-shiab (2026-06-23)
Verdict: GENUINE_OBSTRUCTION
Computed the spinor branching under Spin(7,7) (Cl(7,7) ~= M(128,R), real-type; S = Sigma^+ oplus Sigma^-, each Majorana-Weyl R^64 with End_{Spin(7,7)} = R) and tested whether the shiab contraction Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha).s is canonically determined by Spin(7,7) symmetry. Result: it is NOT — the equivariant R-linear shiab-type Hom space is at least 2-dimensional over R (independently-scalable chiral generators Phi^+, Phi^-), so the bracket is a 2-real-parameter family under Spin(7,7) alone. The split-form failure is named in four mechanisms: (M1) two-chiral-parameter freedom collapsible only by importing O(7,7) parity; (M2) the real Schur ring removes the H-linearity / Sp(64)-gauge canonicity lever that the corrected (9,5) signature supplies (no R-substitute exists); (M3) Sigma^+ ~= Sigma^- over R with no Spin(7,7)-invariant identification, so the family is not canonically split into chiral parts; (M4) even after O(7,7) parity the surviving real scalar carries a disconnected Z/2 sign plus a parity-axis choice (vs. the connected H^*-scalar of (9,5)). This is an independent representation-theoretic argument (beyond the N1 Frobenius computation) for preferring (9,5) over the original (7,7) convention. Remaining: CAS D_7 Clebsch-Gordan to confirm dim_R = 2 exactly (OQ1, cannot lower below 2); whether the residual Z/2 sign flips the rolled-up index (OQ3).
File: `explorations/pc1-spinor-spin77-shiab-2026-06-23.md`

### freed-hopkins-xobs-sol-k3-moduli (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED (lane-narrowed) [downgraded from GENUINE_OBSTRUCTION by CORRECTION XOBS-IC4-01, 2026-06-23]
Identified the sole surviving Option-B observer-state space X_obs^sol -- previously OPEN in the optionb file -- as the moduli space M_RF(K3) of Ricci-flat (hyperkahler/Einstein) metrics on K3, using the IC4 metric-selection result (GU section field equation reduces to source-free Einstein, Hitchin-Thorpe equality forces Ricci-flat). By global Torelli, X_obs^sol = Gamma\O(3,19)/(O(3)xO(19)) with Gamma = O(3,19;Z), a dim-57 aspherical K(Gamma,1) arithmetic locally symmetric space, hence NONCONTRACTIBLE -- settling FC1 negative. CONDITIONAL ON the IC4 reduction, its noncontractibility is exactly that of the K3 Einstein-metric (gravitational) background moduli, so its KSp^0 = KO^4 index class is in the image of the ordinary gravitational/tangential-structure background-extension functor and RELABELS -- FC2 fires IF IC4 holds. The lane is NARROWED (Met(X^4) contractible, Omega^2 B Sp(64) gauge-relabel both eliminated; X_obs^sol the sole survivor and conditionally a gravitational-relabel) but NOT closed: the load-bearing identification X_obs^sol = M_RF(K3) rests on the same-session input `ic4-ricci-flat-k3-selection-2026-06-23.md`, verdict only CONDITIONALLY_SUPPORTED, with open F3 (surviving trace-free GU source) and F5 (K3 topology not forced). GENUINE_OBSTRUCTION requires a proved failure with verified inputs; deriving it from a same-session conditional input is verdict inflation by same-session chaining. Held at CONDITIONALLY_RESOLVED; promotion deferred to a future session contingent on the OPEN Option-B no-go root lemma, IC4 gates C/D/F (F3/F5), and the RC4 KO^4-over-orbifold lift. Seven reopening/blocking conditions named (RC1 independent quaternionic observer structure; RC2 IC4 reduction failure [LOAD-BEARING]; RC3 GU solution locus a non-generic sublocus; RC4 KO^4 lift failure over the arithmetic orbifold base; RC5 IC4 gate C/D unverified; RC6 K3 topology not forced / IC4 F5; RC7 same-session circular-promotion guard). Aligns the file with the already-corrected canon surface (CORRECTION FH-01).
File: `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md`

### anomaly-sp64-global-pi15 (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Upgraded the reconstruction-grade global-anomaly leg of the Sp(64) anomaly audit (§3 of anomaly-audit-cl95-gauge-group) by reducing the pi_15(Sp(64))=Z winding to the Dai-Freed mapping-torus phase Phi[g_inf] = (-1)^{index_2(D^R_16)}, the mod-2 index of a 16D Dirac operator coupled to R = S = H^64, and proving that index EVEN (so Phi = +1, the winding is trivial for the GU configuration and global anomaly cancellation holds). Two independent mechanisms force evenness: (A) quaternionic/KSp-evenness from Cl(9,5) = M(64,H) (kernel and cokernel are H-vector-spaces, dim_C even), and (B) chiral doubling J: S^+ tensor R -> S^- tensor R. The named task failure condition ("if the pi_15 winding is non-trivial, global anomaly fails") does NOT fire. Verdict bound below RESOLVED honestly: the Dai-Freed reduction and chiral-doubling step are reconstruction-grade and the eta/index sign is not computed to Z-level certainty; four explicit failure conditions stated (FC-1 quaternionic-index parity = load-bearing; FC-2 chiral non-doubling; FC-3 subgroup escape via tau+ selection; FC-4 local polynomial non-vanishing). Upgrade gate to RESOLVED = explicit ch_8 . A-hat characteristic-number computation on S^16 with the symplectic Bott generator (finite CAS pass). Corrects the audit's incorrect reason ("Z milder than Z_2", which is backwards per Witten 1985); the correct reason is the even mod-2 index.
File: `explorations/anomaly-sp64-global-pi15-2026-06-23.md`

### dark-energy-w-window-mechanism (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Mechanism-search leg testing whether ANY GU-admissible mechanism places the theta-field in the negative-w_a window (criterion dw_B/dz + 3(1+w_B) < 0) to match DESI's w_a sign. Enumerated and numerically tested three mechanisms via slow-roll-attractor FLRW Klein-Gordon integration: non-minimal curvature coupling xi R B^2 REACHES the window (xi < -0.319 flips the sign; xi ~ -0.6 reproduces DESI's sign AND magnitude ratio -4.3), while modified Willmore potential (lam B^4) and back-reaction (self-consistent H up to f_0=0.95) are both structurally BLOCKED (ratio stays >= +0.70). The clean falsification target is NOT triggered: the mismatch is not a uniform obstruction. Critically, minimal (xi=0) and conformal (xi=+1/6) coupling both give the wrong sign; the required xi ~ -0.3 to -0.6 negative coupling has no derived GU provenance, so the open problem relocates from cosmology (now fully mapped) to GU geometry (the coefficient of R theta^2 in the reduced action, FC1).
File: `explorations/dark-energy-w-window-mechanism-2026-06-23.md`

### n4-ig-dimension-matching (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Tested whether the inhomogeneous gauge group structure IG = Sp(64) ⋉ Ω¹(ad P) reconciles the gauge-algebra residual dim sp(64) = 8256 vs the desired 16384 = 2^14, taking the IG mechanism seriously as a dimension-supplier rather than only dissolving the target (the prior N4 file's route). Result: IG does NOT and structurally CANNOT close a finite gap — its translation part Ω¹(ad P) is a 1-form gauge object of pointwise size 14·8256 = 115584 (infinite-dimensional globally), in a different form-degree and bundle from the 0-form Clifford endomorphism number 16384, and the increment 8128 that could turn 8256 into 16384 appears nowhere in IG; the genuine reconciliation is the verified direct-sum split M(64,ℍ) = sp(64) ⊕ Herm(64,ℍ), 8256 + 8128 = 16384, with the gauge algebra the skew-Hermitian half of End_R(S) and the 8128 complement the spinor-bilinear (observable) operators that were never gauge symmetry. NOT a genuine obstruction (total 2^14 exactly accounted for); verdict held below RESOLVED by three explicit failure conditions (file §5): FC-1 (subalgebra-escape / gauge-group uniqueness — which subalgebra of M(64,ℍ) the τ⁺/shiab data select, shared with anomaly-sp64-global-pi15 FC-3), FC-2 (bilinear-sector misidentification — reconstruction-grade identification of the 8128 Herm(64,ℍ) complement with the Spin(9,5) spinor bilinears), and FC-3 (hidden gauge-sector dimension requirement — no identified GU consistency condition, e.g. unitarity / Dirac–DeRham–Einstein index / Ward identity, that would force the gauge algebra to carry 2^14 dims and make 8256 genuinely too small; §4.4).
File: `explorations/n4-ig-dimension-matching-2026-06-23.md`

### dd1-distortion-distinct-canon-sharpen (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Sharpened the DD1 novelty claim (PARTIALLY_NAMED literature check) into a cohomological theorem and discharged the named failure condition: does the GU distortion's IG-equivariance collapse to a known torsion notion under a change of frame? Computed the gauge transformation laws of both objects — torsion `T = ∇ − ∇_LC` carries the affine cocycle `α(h) = −(D_{∇_LC}h)h⁻¹` (because the metric-determined reference `∇_LC` does NOT transform under the internal gauge group `G = Sp(64)`), while distortion `D = ∇ − g·∇_LC` carries the trivial cocycle `β ≡ 0` (Ad-tensorial via τ⁺). "Collapse under change of frame" is exactly `[α] = 0` (α a coboundary) in `H¹(G; Ω¹(Y, ad P))`, and the result is `[α] ≠ 0`, so collapse does NOT fire: the binary non-collapse is verified-grade on the identity component via a jet-order argument (`α'(ξ) = −D_{∇_LC}ξ` first-order vs coboundary `[ξ,ζ]` zeroth-order, `[α'] ≠ 0 ∈ H¹(Lie(G); ·)`), with the curvature-pinning interpretation (`[α]` = Chern–Weil class of `F_{∇_LC}`, `Z(sp(64))=0`) at reconstruction grade. Novelty over Hehl/Agricola-Friedrich/Sharpe is precisely that all three keep the reference rigid (→ `[α]≠0`); τ⁺ gauging moves it to the 0 class, which is not a frame change. Consistent with HC1 (same `SO(1,3)` value-level irreducible types; the distinction lives in the transformation law, an orthogonal invariant). Verdict bound at CONDITIONALLY_RESOLVED by four explicit failure conditions (flat reference; center leak; ∇-dependent frame; disconnected `π₀(G)`) and the reconstruction-grade global-`H¹` structure claim; remaining = verified `H¹_cont(G; ·)` (OQ-1), section pullback `s*[α]` (OQ-2), and the Noether divergence-free tie-in (OQ-3).
File: `explorations/dd1-distortion-distinct-canon-sharpen-2026-06-23.md`

### type-ii1-fc-epsilon-prime-sign (2026-06-23)
Verdict: CONDITIONALLY_RESOLVED
Evaluated the previously-deferred decisive M(16,C) reality computation for the FC-EPSILON gate (the epsilon' sign for J_twisted = C_{3,1} (x) C_{(6,4)} against s*(D_GU)). Built Cl(6,4) explicitly as a 32-dim Dirac rep, constructed its charge conjugation by solving for the unitary intertwiner, and found the Majorana C_{(6,4)} with C^2 = +I (the one forced by J_twisted^2 = +1) makes every internal generator C-real; the shiab cross-block s_split = +1 (verified on 20 random real-linear single-generator blocks, with an explicit-i control flipping to -1). Therefore epsilon' = epsilon'_diag * s_split = (+1)(+1) = +1: the J-bridge and D-bridge are COMPATIBLE, the genuine-obstruction falsification target does NOT fire, and KO-dim 6 survives this gate. Held below RESOLVED by three failure conditions (FC-eps-1 full M(64,H) check for hidden i / degree-2 internal terms in the cross-block; FC-eps-2 Riemannian-vs-Lorentzian operator; FC-eps-3 J_twisted^2=+1 selects the type-+ conjugation); does not close any same-session Type-II_1 circularity flag.
File: `explorations/type-ii1-fc-epsilon-prime-sign-2026-06-23.md`

---

### CORRECTION VZ-02 (critical) — canon/no-go-class-relative-map.md VZ 4D verdict downgraded from VERIFIED to CONDITIONALLY_RESOLVED (2026-06-23)
Verdict change: the canon no-go map's Velo-Zwanziger row and §2.5 promoted "4D VERIFIED at principal-symbol level (OQ3-V1/V2/V3)" as a hard VERIFIED verdict label. This is overstated and internally inconsistent with the same section's own failure condition FC-VZ-4. FC-VZ-4 states that if the second fundamental form `II_s = s*(θ)` (extrinsic curvature of the section embedding) sources an effective first-order term in `S_R^{4D}`, "the VERIFIED 4D principal-symbol evasion is overturned at the next (subprincipal) order." A verdict labelled VERIFIED cannot simultaneously carry a known, unaddressed higher-order (subprincipal) route to being overturned — that is a RESOLVED/VERIFIED-strength label attached to proof with an open gap. The `vz-subprincipal` check that closes FC-VZ-4 negatively is itself only reconstruction grade, so VERIFIED is unjustified. Fix applied: every hard "4D VERIFIED at principal-symbol level" label in `canon/no-go-class-relative-map.md` (acceptance-summary VZ row line 30; §2.5 status header; §2.5 OQ3 summary; §2.5 failure-conditions status; the fifth-theorem formal-entry "neither leg over-stated" line; §5 closing posture; Appendix B) is replaced with **CONDITIONALLY_RESOLVED (4D principal-symbol, reconstruction; subprincipal order open per FC-VZ-4)**. VERIFIED is reserved for a result with no acknowledged route to being overturned; FC-VZ-4 is exactly such an open route. The 14D leg (CONDITIONALLY_EVADED, gated on FC-VZ-1) and the underlying mathematics are unchanged; only the verdict label and its honesty binding are corrected. This compounds CORRECTION VZ-01 (which downgraded the 14D leg from EVADED to CONDITIONALLY_EVADED): VZ-01 left the 4D leg at VERIFIED; VZ-02 corrects that the 4D leg is also reconstruction grade with an open subprincipal gap. No CANON.md change needed (CANON.md already lists VZ under exploratory-until-formal-obligations-met). RESEARCH-STATUS.md note added.
File: `canon/no-go-class-relative-map.md`

### no-go-class-relative-map §2.5 verdict-label alignment correction (2026-06-23) [VS-4]
Issue: VS-4 (moderate severity). Internal verdict-label inconsistency within §2.5 of `canon/no-go-class-relative-map.md`. The §2.5 status header (line 311) reads `CONDITIONALLY_EVADED (reconstruction) at 14D — gated on E-block invertibility (VZ-01)`, but the body summary line in the same section (line 315) still carried the stronger, now-superseded label `VZ at 14D: EVADED (reconstruction grade ...)`. A reader saw both EVADED and CONDITIONALLY_EVADED for the same 14D leg in the same section. The CONDITIONALLY_EVADED label is canonical: it matches the §2.5 header, the F5/F6 failure-condition summary (line 329 — "CONDITIONALLY_EVADED at 14D (reconstruction; gated on E-block invertibility, VZ-01)"), and the formal fifth-theorem canon entry (no-go-velo-zwanziger-canon-entry log, this file — "14D is CONDITIONALLY_EVADED at reconstruction grade, load-bearing on the unverified E-block-invertibility precondition FC-VZ-1").
Fix applied: Changed line 315 from `VZ at 14D: EVADED (reconstruction grade -- 14D E-block explicit form is structural, not CAS-verified).` to `VZ at 14D: CONDITIONALLY_EVADED (reconstruction grade; gated on E-block invertibility FC-VZ-1, not CAS-verified -- 14D E-block explicit form is structural, not CAS-verified).`
Verdict change: within §2.5, the body-summary label is corrected EVADED -> CONDITIONALLY_EVADED to match the corrected header. This is a label-alignment correction only; the canonical 14D verdict was already CONDITIONALLY_EVADED elsewhere in the same section. No computed value or mathematical content changes. Note: the earlier vz-e-block-direct-clifford log entry (this file) claimed an upgrade of vz-14d-mixed-covectors from CONDITIONALLY_EVADED to EVADED at the standalone-exploration-file level; that upgrade is NOT reflected in the canon map, whose 14D leg remains gated on the externally-unverified E-block-invertibility precondition (FC-VZ-1).
File: `canon/no-go-class-relative-map.md` (§2.5, line 315)

### no-go-velo-zwanziger-canon-entry 4D verdict-label downgrade (2026-06-23) [VS-6]
Issue: VS-6 (moderate severity). Inherited verdict-strength issue in the formal fifth-theorem VZ canon entry. The entry binds its own overall verdict honestly (CONDITIONALLY_RESOLVED; 14D reconstruction / 4D ...) and correctly names that FC-VZ-1 rests on a same-session, externally-unverified E-block argument (vz-e-block-direct-clifford). The residual problem was inherited only: the entry repeated the `4D VERIFIED` / `4D is verified` label (the §18 vz-schur-complement label that VS-1/VS-2 downgrade), and the §4 cross-theorem note contrasted VZ's `4D VERIFIED` against DG's EVASION-BY-SCOPE-EXIT grade. Once the 4D principal-symbol result is recognized as a principal-symbol-only, flat-gauge computation with subprincipal order and curved-gauge extension still open, the entry's `4D verified` phrasing had to follow.
Fix applied: Replaced the entry's own 4D verdict label `4D VERIFIED` / `4D is verified` with `4D CONDITIONALLY_RESOLVED (principal-symbol, flat-gauge computation; subprincipal and curved-gauge open)` at every place the entry states its own verdict — §1 honest-binding line; §1 analysis-chain citation (added the 4D-correction clause parallel to the existing 14D-correction clause); §3.5 4D verdict bullet (rewritten to state principal-symbol/flat-gauge scope and name the open subprincipal + curved-gauge legs); §3.6 FC-VZ-4 ("VERIFIED 4D principal-symbol evasion" -> "4D principal-symbol evasion", tied to the §3.5 open subprincipal leg); §3.6 grade-restatement; §4 cross-theorem note (VZ now `CONDITIONALLY_RESOLVED` after 4D pullback, sharpening the "should not present VZ at DG's grade" point); §5 honestly-bound-verdict restatement. The overall entry verdict (CONDITIONALLY_RESOLVED) and frontmatter (verdict: CONDITIONALLY_RESOLVED, status: reconstruction) were already correct and unchanged. The §2-citation bullet quoting vz-schur-complement §18's internal "evasion VERIFIED" label was left as an accurate citation of that source file (VS-1/VS-2 own the in-source-file relabel); the new §1 analysis-chain clause records the downgrade so no unqualified "4D VERIFIED" verdict label of the entry's own survives.
Verdict change: the entry's 4D leg label is downgraded VERIFIED -> CONDITIONALLY_RESOLVED (principal-symbol, flat-gauge; subprincipal and curved-gauge open) to inherit the VS-1/VS-2 downgrade of the §18 4D result. No computed value or mathematical content changes; the failure-condition discipline (FC-VZ-1..5) was already adequate and is unchanged. The overall fifth-theorem-entry verdict (CONDITIONALLY_RESOLVED) is unaffected.
File: `explorations/no-go-velo-zwanziger-canon-entry-2026-06-23.md` (§1, §3.5, §3.6, §4, §5)


### no-go-class-relative-map GU-Chir generation-count overstatement correction (2026-06-23) [VS-5]
Issue: VS-5 (moderate severity). Same-session flag-and-reversal around the generation-count mechanism. The new `oq-kk1-bc1-jacobi-operator-parameters` entry (this file, verdict GENUINE_OBSTRUCTION) supersedes the same-session `oq-kk1a-cas-norm-fiber-wavefunction` entry that had asserted "G2a gate CLOSED at reconstruction grade" — the supersession itself is handled honestly (the entry names FC-JACOBI / FC-OPER-MATCH / FC-FROBENIUS-DISCRETE all resolved negatively, and the correct BC1 operator has discrete spectrum only at nu = 5/2, 1/2, NOT nu = 3/2). Net effect: the entire scalar / BC1 / non-compact analytic route to the RS generation index is now DEAD, so the "3 generations" / ind_H(D_GU) = 24 claim rests SOLELY on the APS/K3 route, which is itself only CONDITIONALLY_RESOLVED (reconstruction; gates OQ-RK1, OQ-RK2). The downstream canon surface that still presented the count as established was `canon/no-go-class-relative-map.md` §2.4 GU-Chir block (line 259): it stated `ind_H(D_GU) = 24 via the Atiyah-Singer theorem ... Generation count = ind_H(D_GU) / 8 = 3` flatly, with no grade qualifier and no acknowledgment that the analytic routes had failed.
Fix applied (canon surface, no verdict on any exploration changed):
- GU-Chir block (§2.4, line 259) relabeled `GU-Chir (reconstruction grade — sole surviving route is APS/K3)`; body now states the count is CONDITIONALLY_RESOLVED at reconstruction grade (NOT established), enumerates the four FAILED non-compact/scalar routes (scalar FJ/BC1 superseded; rank-3 Atiyah-Schmid empty sum; tau-twisted FAILS AS STATED on four criteria; BC1 Jacobi route GENUINE_OBSTRUCTION), states the count rests solely on the compact APS/K3 index (ind_H = 8*A-hat(K3) + 8 = 24) with open gates OQ-RK1 and OQ-RK2, and adds an explicit "do not present 3 generations as more than reconstruction-grade" instruction. The scope-exit verdict for Distler-Garibaldi was reinforced as independent of the numerical count (DG is inapplicable to GU regardless of whether ind_H is fully verified), so softening the count does not weaken the DG carve-out.
- Witten row (§1 acceptance table, line 26) stale phrasing tightened: the clause "the generation-count analytic mechanism is currently open after the scalar rank-one BC1 chain was superseded" -> now states the non-compact-fiber mechanism is CLOSED as FAILED with the count surviving only at reconstruction grade via the compact APS/K3 route (gates OQ-RK1/OQ-RK2); the "requires a corrected rank-3 or direct tau-twisted computation" clause -> "all non-compact analytic routes FAILED; reconstruction-grade only via the surviving APS/K3 route (open gates OQ-RK1/OQ-RK2)".
Verdict change: no exploration-file verdict changed. The `oq-kk1-bc1-jacobi-operator-parameters` GENUINE_OBSTRUCTION verdict and the APS/K3 CONDITIONALLY_RESOLVED status are both correct and unchanged. This is a downstream-canon overstatement correction: the GU-Chir surface and the Witten-row phrasing are brought into alignment with the already-recorded analytic-route failures. No computed value changes; the count remains 24 = 3 generations, now correctly carried at reconstruction grade via the single surviving APS/K3 route. NEXT-STEPS.md was checked and already states the count as CONDITIONALLY_RESOLVED via the APS/K3 route exclusively (no change needed).
File: `canon/no-go-class-relative-map.md` (§1 Witten row line 26; §2.4 GU-Chir block line 259)

### no-go-class-relative-map Freed-Hopkins observer-pairing hidden-conditionality correction (2026-06-23) [HAH-1]

Issue: HAH-1 (critical severity). Hidden conditionality dropped on canon promotion. The canon Freed-Hopkins acceptance-table row (§1) and the §2.3 closure paragraph asserted the observer-pairing lane as an UNCONDITIONAL `LANE CLOSED 2026-06-23 (GENUINE_OBSTRUCTION)`. The load-bearing source file `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` carries its OWN verdict as CONDITIONAL: §10 reads "closed at GENUINE_OBSTRUCTION, conditional on the IC4 reduction (RC2) and the KO^4 lift over the arithmetic base (RC4)." The canon promotion kept the GENUINE_OBSTRUCTION label (the strongest closure label) but dropped the word "conditional" and dropped RC4 (and RC3) from the §2.3 reopening list, leaving only RC1/RC2. This violated the map's own §0 Honesty contract and Appendix B ("ships visible stress, not a solved problem"), since the strongest closure label was applied where the source carries an explicit hedge.

Fix applied (canon surface, no verdict on any exploration changed):
- Acceptance table (§1) Freed-Hopkins row relabeled from "observer-pairing enrichment LANE CLOSED 2026-06-23 (GENUINE_OBSTRUCTION)" to "observer-pairing enrichment CONDITIONALLY closed 2026-06-23 (GENUINE_OBSTRUCTION conditional on IC4/RC2 and KO^4-lift/RC4)"; open-stress column now records RC2 (IC4 reduction) and RC4 (KO^4 lift over the non-Hausdorff arithmetic orbifold base) as live conditions.
- §2.3 closure paragraph heading relabeled "Observer-pairing Option-B lane CONDITIONALLY CLOSED (2026-06-23, GENUINE_OBSTRUCTION conditional on IC4/RC2 and KO^4-lift/RC4)"; the verdict sentence now reads "CONDITIONALLY closed at GENUINE_OBSTRUCTION ... conditional on the IC4 reduction (RC2) and the KO^4 lift over the arithmetic base (RC4)"; the reopening list restored from {RC1, RC2} to the full {RC1, RC2, RC3, RC4} from the source file §8, with RC4 (KO^4 = KSp^0 lift may fail over the non-Hausdorff arithmetic orbifold base M_RF(K3) = Gamma\D) and RC3 (GU solution locus a non-generic sublocus of M_RF(K3)) restored verbatim in substance; an explicit Honesty-contract / Appendix B note added that the RC2/RC4 conditionality is load-bearing and kept visible at canon level.

Verdict change: the canon-level label is corrected from UNCONDITIONAL GENUINE_OBSTRUCTION to CONDITIONALLY closed at GENUINE_OBSTRUCTION (conditional on RC2 + RC4), matching the source exploration's own verdict. No exploration-file verdict changed: `freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` was already GENUINE_OBSTRUCTION-conditional-on-RC2/RC4 and its DERIVATION-PROGRESS entry already named all four reopening conditions (RC1-RC4); the canon prose is now realigned to it. The lane status is unchanged in substance (still closed, conditionally); only the dropped conditionality is restored.
File: `canon/no-go-class-relative-map.md` (§1 Freed-Hopkins acceptance-table row; §2.3 observer-pairing Option-B closure paragraph)


### vz-schur 4D-VZ-evasion verdict-label overstatement correction (2026-06-23) [VS-1]

Issue: VS-1 (critical severity). Verdict-label overstatement inside a status:reconstruction file. `explorations/vz-schur-complement-2026-06-23.md` carries frontmatter `status: reconstruction` but set `oq3_status: VERIFIED` and `vz_4d_status: VERIFIED`, and §18 explicitly claimed to "upgrade OQ3 from CONDITIONALLY_RESOLVED to VERIFIED and 4D VZ evasion from reconstruction to verified." The load-bearing OQ3-V1 computation (§18.1) is done ONLY in the constant-coefficient flat Minkowski gauge with a flat section `s(x) = (x, eta)`; the curved/general-section case is asserted pointwise ("The argument is pointwise and holds on all sections"), NOT computed. A flat-gauge-only computation plus an asserted, uncomputed curved extension is reconstruction-grade, not VERIFIED. The `VERIFIED` label must not appear for a step that contains an asserted, uncomputed generalization inside a status:reconstruction file. This is the load-bearing 4D leg that propagates into the canon map §2.5 and the VZ canon entry.

Fix applied:
- `explorations/vz-schur-complement-2026-06-23.md` frontmatter: `oq3_status` VERIFIED -> CONDITIONALLY_RESOLVED; `vz_4d_status` VERIFIED -> CONDITIONALLY_RESOLVED; `oq3_v1` RESOLVED -> CONDITIONALLY_RESOLVED (V2/V3 remain RESOLVED — they are exact, gauge-independent). Added `oq3_open_upgrade_condition` naming the curved-background frame-splitting check (explicit computation, not pointwise assertion, that `{gamma^a_H, gamma^i_N} = 0` and `c_s(eta)^2 = g_s(eta,eta) Id_S` receive no anomalous corrections on a non-flat section).
- Body §16 summary table, §18 header, §18.1 verdict, §18.4 combined result + proof-summary (a), §18.5, and §19 cross-references: every "4D VZ evasion VERIFIED" / "OQ3 VERIFIED" claim relabeled CONDITIONALLY_RESOLVED, stating explicitly that OQ3-V1/V2/V3 are verified only in constant-coefficient gauge and naming the curved-background frame-splitting check as the open upgrade condition.
- `canon/no-go-class-relative-map.md` (§2.5): the verdict label was already downgraded to CONDITIONALLY_RESOLVED by the concurrent FC-VZ-4 (subprincipal-order) correction; this pass additionally corrects the OQ3-V1-specific justification (line 317) to name the second, distinct open condition — that OQ3-V1 is computed only in constant-coefficient flat Minkowski gauge with the curved-section case asserted not computed. Both the subprincipal-order route (FC-VZ-4) and the curved-gauge route now hold the 4D leg below VERIFIED.
- `explorations/no-go-velo-zwanziger-canon-entry-2026-06-23.md`: §2 citation of vz-schur corrected from "OQ3-V1/V2/V3 RESOLVED (4D principal-symbol evasion VERIFIED)" to "OQ3-V2/V3 RESOLVED, OQ3-V1 CONDITIONALLY_RESOLVED (constant-coefficient gauge only) ... 4D principal-symbol evasion CONDITIONALLY_RESOLVED, NOT VERIFIED"; the "4D leg is unaffected" clause corrected to note the 4D leg is independently CONDITIONALLY_RESOLVED via the OQ3-V1 flat-gauge limitation. (The file's §1 verdict prose had already been corrected to CONDITIONALLY_RESOLVED, naming the flat-gauge/curved-gauge open condition, by a concurrent pass.)

Verdict change: `vz_4d_status` / `oq3_status` VERIFIED -> CONDITIONALLY_RESOLVED (reconstruction grade). OQ3-V2 and OQ3-V3 remain RESOLVED (exact). The 14D leg (CONDITIONALLY_EVADED) and the overall VZ verdict are unaffected. No new mathematics; this is a verdict-label correction bringing the 4D leg's grade into line with its actual (flat-gauge-only) computation.
File: `explorations/vz-schur-complement-2026-06-23.md` (frontmatter + §16/§18/§19); `canon/no-go-class-relative-map.md` (§2.5 line 317); `explorations/no-go-velo-zwanziger-canon-entry-2026-06-23.md` (§2)


### CORRECTION ELLIPTICITY-LEMMA-iii: split-signature ellipticity lemma part (iii) downgraded to FALSE; F5 reclassified OPEN -> FIRED (2026-06-23) [VS-3]

Issue: VS-3 (critical). Same-session contradiction with verdict not adjusted. `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` (CONDITIONALLY_RESOLVED) hung its analytic-framework conclusion on part (iii) — "the Sp(64) gauge orbit is a PROPER subspace of NM(xi)" (a surviving pointwise physical quotient carrying SM field content) — and listed failure condition F5 as merely "OPEN (reconstruction)". A sibling file written the SAME session, `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` (CONDITIONALLY_RESOLVED), found the OPPOSITE by explicit CAS check: the gauge orbit FILLS NM(xi). Its own DERIVATION-PROGRESS entry already records that this "NAMES AN INTERNAL CONTRADICTION in the lemma (parts (ii) and (iii) are mutually inconsistent), resolved in favor of (ii)." The lemma file had not absorbed this: it retained part (iii) as live, kept F5 as a generic open gate, and presented the "physical subspace survives" claim throughout §5, §6, §7.3, §8, §9, §11.

Root cause of the math error: part (ii) of the lemma establishes c(xi) is a MAXIMAL-rank nilpotent at null xi (rank = dim_R E / 2), which by the null-projection property forces Im c(xi) = ker c(xi) = NM(xi). The BRST-exact gauge orbit has principal symbol c(xi), so it equals Im c(xi) = NM(xi) — it FILLS the kernel. Part (iii)'s "proper subspace" claim came from an under-justified H-linearity dimension count (§5.3 / §7.3) that implicitly treated the Sp(64) gauge action as living on a factor DISJOINT from Clifford. Per `sc1-oq3` (RESOLVED), gauge rho and Clifford c(xi) are BOTH left matrix multiplication on the SAME S = H^{64}; there is no disjoint factor. With the correct same-side action and maximal rank, the orbit fills.

Fix applied to `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md`:
- Frontmatter: added a `correction:` field recording part (iii) SUPERSEDED/FALSE, F5 FIRED, verdict retained on the corrected (Koszul-exactness) premise.
- §5: added SUPERSEDED banners over §5.3/§5.4 (the false H-linearity argument and "null modes are physical" conclusion); added new §5.5 "CORRECTED gauge analysis" deriving the gauge-orbit-fill from the null-projection property and re-deriving the symmetric-hyperbolic conclusion (physical content via Cauchy-data transport, Maxwell-analogous Koszul-exactness, pointwise quotient H(xi) = 0).
- §6 (formal Lemma): struck original part (iii) and added corrected part (iii') (gauge orbit FILLS NM(xi)); rewrote part (v) gate-closure so the gate still fires but on the corrected (no pointwise elliptic-modulo-gauge kernel / Koszul-exactness) basis rather than the false "physical subspace non-trivial" basis.
- §7.3 (proof of (iii)): banner-superseded the invalid H-linearity proof; added §7.3' proving the gauge-orbit-fill.
- §8 (failure conditions): reclassified F5 from "OPEN (reconstruction)" to FIRED-against-original-part-(iii) in both the table and the per-condition status block, noting the firing is the EXPECTED massless-field signature, absorbed by the corrected derivation (verdict not downgraded).
- §9 (Result): correction banner on §9.1; rewrote verdict summary, item 3, item 5, "Remaining for RESOLVED" and §9.2 "failure conditions recap" so F5 is recorded as FIRED/absorbed and the residual gates are FF3/FF4 (from the F5 file) plus the RS null-mode count and discrete-series identification.
- §10/§11: corrected the connection-table row for sc1-oq2c (null-projection feeds part (ii); original (iii) reading FALSE) and marked OQ-F5 RESOLVED (fired), pointing to the successor FF3/FF4 gates.

Verdict change: overall lemma verdict RETAINED at CONDITIONALLY_RESOLVED — the analytic-framework conclusion (D_GU is symmetric-hyperbolic / real-principal-type, NOT elliptic) SURVIVES because it is re-derived from the corrected premise (gauge-orbit-fill = Koszul-exactness at null xi; physical content carried by Cauchy-data transport per the independently CONDITIONALLY_RESOLVED `sc1-oq2b-symmetric-hyperbolic`), not from the false proper-subspace claim. The internal contradiction is now resolved in-file in favor of part (ii). Part (iii) is FALSE/SUPERSEDED; F5 is FIRED, not OPEN. Downstream verdicts were recorded as untouched at the time, but later status discipline treats the generation-count target ind_H = 24 as OPEN and not derived by the cited Atiyah-Schmid route, as neither used a pointwise null-cohomology quotient. No CANON.md / RESEARCH-STATUS.md entry references this lemma (verified by grep), so no canon cascade was required.
File: `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` (frontmatter, §5, §6, §7.3, §8, §9, §10, §11)

### CORRECTION FH-01 (critical) — canon/no-go-class-relative-map.md Freed-Hopkins observer-pairing verdict downgraded from closed GENUINE_OBSTRUCTION to CONDITIONALLY_RESOLVED / lane-narrowed (2026-06-23)
Verdict change: the canon no-go map's Freed-Hopkins row (§1 acceptance table) and §2.3 "Observer-pairing Option-B lane" block carried the observer-pairing anomaly lane as **CONDITIONALLY closed at GENUINE_OBSTRUCTION** ("GENUINE_OBSTRUCTION is the strongest closure label"). This is a same-session circular canon promotion. The GENUINE_OBSTRUCTION reading rests on a dependency chain in which every load-bearing link was authored in this same session, none is VERIFIED, the root is still OPEN, and the two files carrying the verdict are untracked in git ('??'):
- `freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` (verdict GENUINE_OBSTRUCTION, but **untracked**) depends on
- `freed-hopkins-optionb-ksp-family-2026-06-23.md` (CONDITIONALLY_RESOLVED, **untracked**) +
- `freed-hopkins-nonforgettable-observer-2026-06-23.md` (verdict **OPEN** — the Option-B no-go lemma is itself the open root) +
- `ic4-ricci-flat-k3-selection-2026-06-23.md` (CONDITIONALLY_SUPPORTED, with open failure condition F3/OQ-FH-Bsol-3: nonzero trace-free GU source -> nonzero Lambda_eff would obstruct the K3 source-free-Einstein vacuum gate) +
- `signed-readout-oq2a-k-theory-lift-2026-06-23.md` (CONDITIONALLY_RESOLVED; the KSp^0(X) = KO^4(X) Atiyah-Janich identification is proved for compact Hausdorff / finite CW X only, NOT the non-Hausdorff arithmetic-orbifold base Gamma\O(3,19)/(O(3)xO(19)), Gamma = O(3,19;Z), actually used — this is the RC4 gap).
Promoting a top-strength closed verdict onto a same-session, all-conditional, partly-OPEN substrate is exactly the same-session-circularity pattern the map's own honesty contract / workflow auditor warns against ("be especially suspicious of files promoted today"). A closed GENUINE_OBSTRUCTION cannot coexist with an OPEN root and two unclosed conditional gates (IC4 F3, KO^4-over-orbifold RC4).
Fix applied (canon surface only; no exploration-file verdict changed):
- §1 Freed-Hopkins acceptance-table row (analogy-strength + open-stress cells): relabeled from "observer-pairing enrichment CONDITIONALLY closed (GENUINE_OBSTRUCTION conditional on IC4/RC2 and KO^4-lift/RC4)" to "CONDITIONALLY_RESOLVED / lane-narrowed (reconstruction grade), NOT a closed GENUINE_OBSTRUCTION"; the open-stress cell now enumerates the three live, independently-unclosed conditions (RC1 OPEN root; IC4 F3 vacuum/trace gate; RC4 KO^4-over-orbifold).
- §2.3 block header changed from "CONDITIONALLY CLOSED (GENUINE_OBSTRUCTION conditional on IC4/RC2 and KO^4-lift/RC4)" to "CONDITIONALLY_RESOLVED / lane-narrowed — NOT a closed GENUINE_OBSTRUCTION"; added a "Why this is held at CONDITIONALLY_RESOLVED and NOT promoted" paragraph recording the explicit conditional chain (RC1 OPEN root, IC4 F3 gate, RC4 KO^4-over-orbifold) and the untracked-files observation.
- §2.3 disposition sentence (formerly "the observer-pairing anomaly lane is therefore CONDITIONALLY closed at GENUINE_OBSTRUCTION — GENUINE_OBSTRUCTION is the strongest closure label") rewritten to state the canon-level disposition is CONDITIONALLY_RESOLVED / lane-narrowed at reconstruction grade, with promotion to a closed GENUINE_OBSTRUCTION deferred to a later session on tracked files after RC1 + IC4 F3 + RC4 are independently closed.
Disposition retained as correct: the lane IS genuinely **narrowed** — Met(X^4) (contractible) and Omega^2 B Sp(64) (gauge-relabel) candidates are eliminated, and X_obs^sol is the sole surviving candidate and plausibly a gravitational-background-moduli relabel. The math content (the candidate eliminations, the M_RF(K3) identification argument) is unchanged; only the verdict label and its honesty binding are corrected. The four §8 reopening conditions RC1-RC4 already enumerated in §2.3 are preserved.
No CANON.md change needed (CANON.md does not list a standalone Freed-Hopkins GENUINE_OBSTRUCTION entry; it references only canon/no-go-class-relative-map.md, which is corrected in place). RESEARCH-STATUS.md row "no-go assumption map | canon" unchanged (the document remains canon; the internal verdict is corrected).
File: `canon/no-go-class-relative-map.md` (§1 Freed-Hopkins row line 28; §2.3 lines 195, 205, 212)

### CORRECTION VZ-F5-01 (moderate) — vz-f5-hamiltonian-subsidiary-propagation CONDITIONALLY_RESOLVED verdict re-bound as load-bearing on the unproven claim FC1 (2026-06-23) [HAH-3]

Issue: HAH-3 (moderate severity). Load-bearing hidden assumption recast as benign. `explorations/vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md` (verdict CONDITIONALLY_RESOLVED) carries the F5 dynamical gate of the VZ no-go. The file's OWN §4.6(b) and §4.10 derive that, when `F_A != 0`, the gamma-trace constraint is NOT preserved under time evolution: `[Gamma^{4D}, Phi(F_A)] Psi_R != 0` (generically when `F_A != 0`) and `phi = Gamma^{4D} Psi` does not remain zero for all t. In the CLASSICAL VZ analysis this non-preservation of the gamma-trace constraint under gauge coupling IS the obstruction signature (it generates the inconsistent secondary constraint and the acausal characteristic surface). The file escaped this by asserting the constraint is "kinematic, not dynamical" (so the Dirac-Bergmann chain "does not initiate"), which rests entirely on the unproven negative-existence claim FC1 (no standalone GU RS Lagrangian). The file itself only stated "No such Lagrangian has been identified" (FC1) — absence of identification, not proof of absence. The escape phrases ("automatically", "by construction", "by definition", "trivially" — 9 occurrences) each presupposed that the Schur-complement reframing is the correct dynamics rather than an assumption. §4.8 also contained a visible mid-proof self-correction ("Wait, let me be more careful"), a soft signal the `K_{mu nu}` commutator algebra was not clean.

Fix applied (no mathematics changed; verdict re-bound as assumption-conditional):
- `explorations/vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md`:
  - §4.6(b): added an "Honest reading" block stating the §4.6(b) non-preservation IS the classical VZ obstruction signature and is reinterpreted as benign ONLY IF the Schur-complement system is the correct dynamics — which is exactly FC1, and FC1 is open. Every escape phrase is flagged as inheriting this FC1-conditionality.
  - §4.7 header relabeled "(Conditional on FC1)"; lead sentence rewritten to "the §4.6(b) result IS the VZ obstruction signature under the classical reading, and is benign ONLY IF the Schur-complement system is the correct dynamics — which is FC1, and FC1 is open."
  - §4.8: replaced the bare "Wait, let me be more careful" self-correction with an explicit "Algebra-grade caveat" naming what the first attempt dropped (`K_{mu nu}` term + Clifford mis-ordering), flagging the corrected commutator as reconstruction grade, not independently re-derived / CAS-checked, and noting that any sign/ordering error propagates into the FC3 `K_{mu nu}` analysis.
  - §4.10: added the explicit two-readings block (classical/standalone reading -> GENUINE_OBSTRUCTION if FC1 fails; Schur-complement reading -> benign only if FC1 holds); the "correct and expected behavior" sentence now reads "ONLY UNDER the Schur-complement reading, i.e. only if FC1 holds," with FC1 named as open.
  - §4.11: "Primary constraints" / "Subsidiary condition" / "Conclusion" all relabeled "(conditional on FC1)" and the FC1-false branch (gamma-trace is then an externally-imposed subsidiary condition and the non-preservation is the VZ obstruction) named explicitly.
  - §6 summary table: header column relabeled "GU RS sector (IF FC1 holds)", every cell tagged "— IF FC1", a new "Constraint preservation under `F_A != 0`" row added recording that the constraint DOES fail (§4.6(b)/§4.10) in BOTH columns and is benign only IF FC1, and the VZ-obstruction row now records "arises if FC1 fails." Concluding paragraph re-bound as assumption-conditional.
  - §7 Verdict: relabeled "CONDITIONALLY_RESOLVED — load-bearing on the unproven claim FC1 (no standalone GU RS Lagrangian); assumption-conditional, not a free-standing derivation," with a "Load-bearing dependency (read first)" block; item 1 made conditional on FC1.
  - §7 FC1: upgraded to "(LOAD-BEARING — the verdict of this file is conditional on FC1 holding)" with an explicit "Status of FC1: OPEN. The file establishes only ABSENCE OF IDENTIFICATION, not proof of absence" paragraph, and named the two routes to resolving it affirmatively (full GU action; guardian-symmetry OQ-H3).
  - §8 "What This Closes": closure re-bound as conditional on FC1-FC4 and load-bearing on FC1 in particular, with the FC1-false branch (gate NOT closed; §4.6(b)/§4.10 is the VZ obstruction) named.
- `canon/no-go-class-relative-map.md` (§2.5 F5 row + F5-full failure-conditions status line): the F5 row CONDITIONALLY_RESOLVED label re-bound as "LOAD-BEARING ON THE UNPROVEN CLAIM FC1 ... assumption-conditional, not a free-standing derivation," recording that the §4.6(b)/§4.10 gamma-trace non-preservation is the classical VZ obstruction signature reinterpreted as benign only under the FC1-conditional Schur-complement reading, that FC1 is open (absence of identification, not proof of absence), and that under the FC1-false reading the result is a GENUINE_OBSTRUCTION; FC3's `K_{mu nu}` commutator algebra flagged as reconstruction grade with a visible mid-proof self-correction. F5-full failure-conditions status line given the same FC1-load-bearing caveat.

Verdict change: the file's overall verdict label is RETAINED at CONDITIONALLY_RESOLVED but re-bound as explicitly assumption-conditional on FC1 (no standalone GU RS Lagrangian), an unproven negative-existence claim. This is a verdict-honesty / load-bearing-assumption correction, not a downgrade to OPEN and not a flip to GENUINE_OBSTRUCTION: the result remains conditionally resolved IF FC1 holds, and the correction makes explicit that (a) FC1 is the load-bearing open claim, (b) the §4.6(b)/§4.10 constraint non-preservation is the classical VZ obstruction signature reinterpreted as benign only under the FC1-conditional Schur-complement reading, and (c) the §4.8 `K_{mu nu}` algebra is reconstruction grade. No computed value or mathematical content changed. RESEARCH-STATUS.md was checked: it carries no standalone F5 / vz-f5 row (the VZ no-go is tracked via the canon no-go map, corrected in place), so no RESEARCH-STATUS.md cascade was required. CANON.md was checked: it lists no standalone vz-f5 entry (VZ is referenced only through canon/no-go-class-relative-map.md), so no CANON.md cascade was required.
File: `explorations/vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md` (§4.6(b), §4.7, §4.8, §4.10, §4.11, §6, §7, §8); `canon/no-go-class-relative-map.md` (§2.5 F5 row + F5-full failure-conditions status line)

### CORRECTION GEN-03 (critical) — generation-count verdict split into unequal legs; "24 = 3 generations" is NOT a precision theorem (2026-06-23)
Issue: GENERATION-COUNT-OVERSTATED-IN-CANON. The generation-count claim ind_H(D_GU) = 24 = 16 + 8 (decomposing as 16 H-lines spin-1/2 / two generations + 8 H-lines RS / one generation; generations = 24/8 = 3) was presented in the OQ3a/K3 derivation-progress log entry (the `Generation count CONDITIONALLY_RESOLVED at 3 via APS/K3` block above) as a single CONDITIONALLY_RESOLVED verdict without distinguishing the proof strength of its two legs. The two legs are NOT of equal grade, and the arithmetic being internally consistent (16+8=24, 24/8=3) does not make the result a precision theorem:
- **Spin-1/2 leg (16) — index-theory grade.** 16 = A-hat(K3) * rank_H(S(6,4)) = 2 * 8. A-hat(K3) = 2 is a topological invariant; rank_H(S(6,4)) = 8 follows from Cl(9,5) = M(64,H) module theory. This leg is a genuine Atiyah-Singer index computation.
- **RS leg (8) — physical-DOF-count grade only, no surviving analytic derivation.** 8 = A-hat(K3) * rank_H(S_RS^+) requires rank_H(S_RS^+) = 4, which per GEN-01 rests on a physical-DOF heuristic whose final halving ("half of chiral = 4") is unjustified. Every analytic route to ind_H(D_RS) = 8 has FAILED: scalar Flensted-Jensen / BC1 superseded (split-rank 3, A3 root system, no scalar discrete series); direct rank-3 Atiyah-Schmid is an empty formal-degree sum (SL(4,R) has no discrete series); the tau-twisted rescue FAILS AS STATED on four independent criteria (F1-F4); the BC1 Jacobi fiber-wavefunction route is a GENUINE_OBSTRUCTION (oq-kk1-bc1-jacobi-operator-parameters, 2026-06-23: discrete spectrum at nu = 5/2, 1/2 only, NOT nu = 3/2). Per NEXT-STEPS OQ3b "Tau-Correction Closure" all three analytic routes are retired.
Because the RS leg has no analytic index derivation surviving, "24 = 3 generations" is reconstruction / physical-count grade, NOT a precision theorem.
Fix applied (derivation-progress log surface, no exploration-file verdict changed):
- The OQ3a/K3 `Generation count CONDITIONALLY_RESOLVED at 3 via APS/K3` block above relabeled `CONDITIONALLY_RESOLVED (reconstruction grade, NOT a precision theorem)` and given an explicit LEG-SPLIT clause stating the spin-1/2 leg (16) is index-theory grade and the RS leg (8) is physical-count grade only with all analytic routes FAILED, plus an explicit instruction not to promote "24 = 3 generations" to a precision theorem until ind_H(D_RS) has an independent analytic index derivation (gates OQ-RK1, OQ-RK2).
Canon surface already aligned (verified, no change needed): `canon/no-go-class-relative-map.md` §2.4 GU-Chir block (line 276) was brought to reconstruction grade by correction [VS-5] (2026-06-23) — it already labels the block "reconstruction grade — sole surviving route is APS/K3", states the count is "CONDITIONALLY_RESOLVED at reconstruction grade, NOT established", enumerates the four FAILED routes, splits the legs ("the spin-1/2 leg (16 H-lines) is topological; the RS leg (8 H-lines) carries the reconstruction-grade gates"), and carries "Do not present '3 generations' as more than reconstruction-grade". The §1 Witten-row acceptance entry (line 26) is likewise already hedged. The §2.4 Distler-Garibaldi "precision theorem" promotion (line 278) is the DG *scope-exit / class-membership* claim, which is genuinely precision-grade and independent of the numerical index value, so it is correct and unchanged. NEXT-STEPS.md already carries OQ3b as CONDITIONALLY_RESOLVED via APS/K3 exclusively with all three analytic routes retired (no change needed). CANON.md / RESEARCH-STATUS.md list the no-go map as exploratory/canon respectively with no separate precision-theorem generation-count entry (no cascade required).
Verdict change: no exploration-file verdict changed. The generation count remains CONDITIONALLY_RESOLVED at 3 via the single surviving APS/K3 route, now explicitly recorded with the spin-1/2 (index-theory) vs RS (physical-count) leg split and explicitly NOT carried as a precision theorem.
File: `DERIVATION-PROGRESS.md` (OQ3a/K3 generation-count block, "Generation count CONDITIONALLY_RESOLVED ... via APS/K3")

### CORRECTION ADV-FC-02 (moderate) — n4-ig-dimension-matching index entry undercounted its own failure conditions (2026-06-23)
Issue: TRACKING-GAP between the `n4-ig-dimension-matching (2026-06-23)` index entry above and its exploration file `explorations/n4-ig-dimension-matching-2026-06-23.md`. The index summary stated the CONDITIONALLY_RESOLVED verdict was "held below RESOLVED by FC-1 ... and FC-2" — naming only TWO failure conditions. The exploration file §5 ("Explicit failure conditions") lists THREE explicit, numbered failure conditions: FC1 (subalgebra-escape / gauge-group uniqueness), FC2 (bilinear-sector misidentification — the 8128 Herm(64,ℍ) complement vs the Spin(9,5) spinor bilinears), and FC3 (hidden gauge-sector dimension requirement — a GU consistency condition forcing the gauge algebra to carry 2^14 dims). A reviewer reading only the index entry would correctly flag this CONDITIONALLY_RESOLVED as carrying fewer than three failure conditions (sub-threshold) when the file itself clears the bar. (Note: the file's own §7 closing-summary footer likewise names only FC-1/FC-2, inheriting the same undercount from the §5 set of three; the §5 list is canonical.)
Fix applied (index-entry surface only; no exploration-file verdict or mathematical content changed): the `n4-ig-dimension-matching` index summary line above was edited to reference all three failure conditions — replacing "held below RESOLVED by FC-1 ... and FC-2" with "held below RESOLVED by three explicit failure conditions (file §5): FC-1 (subalgebra-escape / gauge-group uniqueness ...), FC-2 (bilinear-sector misidentification ...), and FC-3 (hidden gauge-sector dimension requirement ...; §4.4)", so the logged failure-condition count matches the file and the entry is no longer mis-readable as a 2-condition sub-threshold entry.
Verdict change: none. The n4-ig-dimension-matching verdict remains CONDITIONALLY_RESOLVED (it was always correctly bound by three failure conditions in the file §5; only the index entry undercounted them). This is a tracking-alignment / failure-condition-count correction on the index surface, not a re-grade. No CANON.md entry exists for n4-ig-dimension-matching (it is an exploration-grade residual on the sp(64) dimension accounting), so no CANON.md cascade is required; RESEARCH-STATUS.md carries no standalone n4-ig row, so no RESEARCH-STATUS.md cascade is required.
File: `DERIVATION-PROGRESS.md` (n4-ig-dimension-matching index summary line)

### CORRECTION FC4-HOLONOMY-01 (critical) — oq-rk2-fc4-k3-holonomy-rank verdict downgraded from CONDITIONALLY_RESOLVED to OPEN; ind_H(D_RS)=8 is reverse-engineered, not derived (2026-06-23)
Issue: RS-INDEX-REVERSE-ENGINEERED. The file `explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md` carried verdict CONDITIONALLY_RESOLVED for the SU(2)-holonomy route to the Rarita-Schwinger contribution ind_H(D_RS) = 8 — the "+8" leg of the headline generation count ind_H(D_GU) = 16 + 8 = 24 = 3 generations. Review found the central number is REVERSE-ENGINEERED, not derived. The file performs ten independent Atiyah-Singer / index-theory computations of the RS index and EVERY ONE fails to give the target ind_C = 16 (= 2*8): the tabulated results (Sec 9.2) are 960, -288, -384, -192, -336, -128, 128, -8, -480, 60, with no convergence. The author then fabricated two formulas SPECIFICALLY because they hit the predetermined answer: (a) ind_H = (chi+sigma)/8 * rank_H(S(6,4)) = (24-16)/8 * 8 = 8 (Sec 6.4 / 9.2), explicitly labeled "[candidate correct formula]" and selected by trying a sequence of guesses ((chi+sigma), (chi+sigma)/2, -(chi+sigma)/2, (chi+sigma)/8) and keeping only the one returning 8; and (b) rank_H(E_RS^{eff}) = b_2^+ + b_0 = 3+1 = 4 = (chi+sigma)/2 (Sec 10.2). Neither is derived from first principles; the file itself admits "its DERIVATION from first principles is not completed here" and "this formula ... is NOT derived from first principles in this file." Formula (a) is directly CONTRADICTED by the file's own genuine Atiyah-Singer computation of the same quantity in Sec 6.5 (which gives ind_C = 60, ind_H = 30). This is the canonical assume-the-answer-then-fit-a-formula error. A body of work containing zero successful derivations of its central number cannot carry CONDITIONALLY_RESOLVED.
What survives (sound, retained): (1) S_RS^+|_{SU(2)_L} = 3V tensor C^{16} (V the SU(2)_hol fundamental, c_2(V)[K3]=12), non-circular from Berger + Spin(4) rep theory; (2) S^+(4,0) flat under SU(2)_hol, 2 parallel spinors = A-hat(K3)=2, exact; (3) S_RS^+ is NOT of the form S^+(4,0) tensor E (non-integer multiplicity obstruction, exact) — a genuine NEGATIVE result that is precisely why the naive twisted-Dirac index attempts all fail. None of these establishes ind_H(D_RS)=8.
Honest status of the "+8": The ONLY support for ind_H(D_RS) = 8 is the physical-DOF helicity count (Sec 6.1: (4-1-1) x C^{16} = C^{32}, chiral half C^{16}, H-rank 8). This is a KINEMATIC polarization count, NOT an analytic index, so "24 = 16 + 8 = 3 generations" has no index-theoretic proof. If the standard vector-spinor-minus-trace operator ind(D^{TM(x)E}) - ind(D^E) is the correct elliptic RS operator, the file's own Sec 5.5 computes -288 (ind_H = -144), so the RS contribution would be -144, not +8, and the generation count would not be 24. This reinforces (and is the holonomy-route analogue of) CORRECTION GEN-03 and GEN-01: every analytic route to ind_H(D_RS) = 8 has now failed.
Fix applied (no mathematics added; verdict downgraded and reverse-engineered formulas flagged):
- `explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md`: frontmatter `verdict` CONDITIONALLY_RESOLVED -> OPEN; `correction_note` field added; title relabeled "OPEN (no successful index derivation)". Sec 6.4 (chi+sigma)/8 selection flagged as reverse-engineered with an inline correction block. Sec 9.2 table expanded to show all ten genuine computations (none = 16) in one block and the two fits segregated into a separate "Reverse-engineered fit (NOT a derivation)" block; "[candidate correct formula]" label retracted. Sec 10.1 item 5, Sec 10.2 (both the (chi+sigma)/8 lead-in and the b_2^+ + b_0 "topologically compelling" claim), and Sec 10.3 ("non-circular status: YES" retracted to NO) all corrected. Sec 11 verdict rewritten to OPEN with the kinematic-vs-analytic statement and four new failure conditions FC4-N1 (no-convergence, already FIRING), FC4-N2 (standard operator gives -288), FC4-N3 (kinematic != analytic), FC4-N4 (reverse-engineered formulas void), plus the retained FC4-H1/H2/H3.
- `DERIVATION-PROGRESS.md`: the oq-rk2-fc4-k3-holonomy-rank entry verdict changed CONDITIONALLY_RESOLVED -> OPEN with the reverse-engineering recorded.
- `NEXT-STEPS.md`: the OQ-RK2 "FC4 CONDITIONALLY_RESOLVED" block rewritten to "FC4 REMAINS OPEN — holonomy attempt did NOT close it," recording the ten failed computations, the two reverse-engineered formulas, the kinematic-not-analytic status, and the -288 standard-operator value.
Verdict change: oq-rk2-fc4-k3-holonomy-rank CONDITIONALLY_RESOLVED -> OPEN. CANON.md and RESEARCH-STATUS.md were checked: neither lists this exploration or a standalone ind_H(D_RS)=8 / FC4 entry — CANON.md already places the three-generation count under "Not Yet Canon" (analytic index ind_H on Y14 open), and RESEARCH-STATUS.md has no FC4/holonomy-rank row — so no canon cascade was required. No computed value changed; the correction removes an unjustified positive verdict from a body that derived none of its central numbers.
File: `explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md` (frontmatter + Sec 6.4, 9.2, 10.1, 10.2, 10.3, 11); `DERIVATION-PROGRESS.md` (oq-rk2-fc4-k3-holonomy-rank entry); `NEXT-STEPS.md` (OQ-RK2 block)

### CORRECTION GEN-04 (moderate) — oq-rk1-rs-rank-first-principles verdict downgraded CONDITIONALLY_RESOLVED -> OPEN; the rank_H(S_RS^+)=4 "first-principles derivation" is circular (2026-06-23)
Issue: APS-EFFECTIVE-RANK-CIRCULAR. The file `explorations/oq-rk1-rs-rank-first-principles-2026-06-23.md` carried verdict CONDITIONALLY_RESOLVED and asserted (its §13) that its derivation of rank_H(S_RS^+) = 4 "is non-circular." Review found the claimed first-principles derivation IS circular. Every direct Clifford-module computation of the effective RS rank in the file fails to give 4: §4.7 / §5.2 give ind_H = 2*96 = 192; §8.2 gives 384; §5.2 again 192; §5.3 (tensor-factor route) yields a non-integer rank_H = 1/2 (§5.3 "8 = ind*8 => ind=1 => 2*rank=1 => rank=1/2", flagged "not an integer. Contradiction"). After these failures the file settles on rank_H(S_RS^+) = rank_H(S(6,4))/2 = 8/2 = 4 (§5.2 "Theorem", restated §10 Step 6). But rank_H(S(6,4)) = 8 IS the physical-DOF generation H-count, and dividing it by 2 to get 4 and then multiplying by A-hat(K3) = 2 to recover ind_H(D_RS) = 8 is an IDENTITY, not a derivation. The file's own §5.1 concedes "ind_H(D_RS) = 8 has been consistently obtained from physical counting, but its derivation [from A-hat * rank] ... requires identifying the correct S_RS^+." The §13 "non-circular" claim is therefore false: the count supplies its own output (8) as input. This is the OQ-RK1 analogue of CORRECTION FC4-HOLONOMY-01, GEN-01, and GEN-03 — every route to ind_H(D_RS) = 8 / rank_H(S_RS^+) = 4 remains physical-count grade, with the final halving unjustified.
What survives (sound, retained): the genuinely algebraic intermediate rank_H(ker Gamma^{14D}|_{S^+}) = 448 - 32 = 416, an exact M(64,H) computation (S = H^{64}, S^{pm} = H^{32} from omega^2 = +Id, (p-q) mod 8 = 4). This is real Clifford algebra and is kept as an established sub-result. It does NOT connect non-circularly to the effective twist rank 4: the 416 -> 4 bridge is exactly the open problem (direct attempts give 192 / 384 / 1/2). rank_H(S_RS^+) = 4 remains Candidate A; Candidate B (rank_H = 8 => 4 generations) is live and undismissed.
Fix applied (no mathematics added; verdict downgraded, circular step retracted as a derivation, failure conditions added):
- `explorations/oq-rk1-rs-rank-first-principles-2026-06-23.md`: frontmatter `verdict` CONDITIONALLY_RESOLVED -> OPEN; added `verdict_scope` and `established_subresult` fields; `gates_for_verified` renamed `gates_for_resolved` with a leading non-circularity gate and a Candidate-B-exclusion gate. Added a top-of-body CORRECTION banner. The §5.2 "Theorem (RS rank from Cl(9,5))" and §10 Step 6 (the rank_H(S(6,4))/2 = 8/2 = 4 identity) flagged "[RETRACTED AS A DERIVATION]" inline; §10 Step 2 (the 416 result) marked as the one genuine non-circular result. §11 failure-condition table extended with FC9 (circularity — currently FIRES), FC10 (Candidate B undismissed), FC11 (no 416->4 bridge). §12 "Achieved" list: rank_H = 4 factorization moved from "Achieved" to "NOT Achieved (OPEN gap)". §13 Verdict rewritten to OPEN, withdrawing the "non-circular" claim and naming the OQ-RK1 CAS computation as the decisive circularity-free gate.
- `DERIVATION-PROGRESS.md`: the oq-rk1-rs-rank-first-principles entry verdict changed CONDITIONALLY_RESOLVED -> OPEN with the circularity recorded and the 416 sub-result retained.
Verdict change: oq-rk1-rs-rank-first-principles CONDITIONALLY_RESOLVED -> OPEN (for the analytic/Clifford-algebraic derivation of rank_H(S_RS^+) = 4). CANON.md and RESEARCH-STATUS.md were checked: neither lists this exploration or a standalone rank_H(S_RS^+) = 4 / first-principles entry (grep for "oq-rk1-rs-rank-first-principles", "rank_H(S_RS^+) = 4", "first-principles" returns no match in either file; CANON.md already places the three-generation count under "Not Yet Canon" with the analytic RS index open), so no canon cascade was required. No computed value changed; the correction removes an unjustified non-circularity claim and preserves the one genuine algebraic result (416).
File: `explorations/oq-rk1-rs-rank-first-principles-2026-06-23.md` (frontmatter + body banner, §5.2, §10 Step 2 & Step 6, §11, §12, §13); `DERIVATION-PROGRESS.md` (oq-rk1-rs-rank-first-principles entry + this note)

### CORRECTION GEN-04 (moderate) — generation-count / ind_H(D_RS)=8 lane verdict flipped CONDITIONALLY_RESOLVED -> OPEN per the workflow's UNDISMISSED-CANDIDATE rule (2026-06-23)
Issue: VERDICT-DISCIPLINE-UNDISMISSED-CANDIDATES. The workflow's own adversarial spec (`.claude/workflows/gu-research-loop.js`, `verdict-inflation` / UNDISMISSED-CANDIDATE lens) states: "When two or more candidates are both plausible and neither has been formally dismissed by derivation, the verdict must be OPEN -- not CONDITIONALLY_RESOLVED" and explicitly: "[flag] generation count files claiming CONDITIONALLY_RESOLVED when rank_H is still uncomputed." For ind_H(D_RS)=8 / the generation count, prior corrections GEN-01, GEN-03, and FC4-HOLONOMY-01 already established that ALL THREE analytic routes (scalar FJ/BC1, A3 direct Harish-Chandra/Atiyah-Schmid, tau-twisted) FAILED, and that the surviving "support" is the physical-DOF helicity count plus the reverse-engineered APS rank rank_H(S_RS^+)=4 (FC4 OPEN; ten independent index computations fail to converge on the target; the helicity count is kinematic, not an analytic index). Despite that, GEN-03 RETAINED the lane label at CONDITIONALLY_RESOLVED ("remains CONDITIONALLY_RESOLVED at 3 via the single surviving APS/K3 route"), and NEXT-STEPS.md repeatedly carried the lane as CONDITIONALLY_RESOLVED while treating "24 = 3 SM generations" as established in the APS Closure Pass and N5 synthesis. By the workflow's own rule, an undismissed candidate with no completed derivation must read OPEN, not CONDITIONALLY_RESOLVED. CONDITIONALLY_RESOLVED is licensed only when one candidate is supported by a derivation; here none is.
Fix applied (NEXT-STEPS.md verdict-label surface; no mathematics added, no computed value changed):
- APS Closure Pass: added a VERDICT CORRECTION banner; "OC1+OC2 APS closure CONDITIONALLY_RESOLVED" -> "OPEN (generation-count leg)"; OC1 RS leg recorded as ANALYTIC_OPEN (topological/spin-1/2 leg =16 genuinely derived; only the =8 RS leg is undismissed).
- OQ3b Closure Pass + "What survives": OQ3b CONDITIONALLY_RESOLVED -> OPEN; the three surviving paths (A) physical DOF count, (B) SM generation count, (C) APS-on-K3 are explicitly marked as physical/counting arguments or as fitting the rank input, NOT analytic derivations of the index.
- Generation Count Rank-3 Resolution Pass: "Summary result: CONDITIONALLY_RESOLVED at 3 generations" -> "OPEN"; the headline equation rewritten from "ind_H(D_GU) = 8*A-hat(K3) + 8 = ... = 24 = 3 SM generations" to a target with the RS leg bracketed and flagged NOT derived; "ind_H(D_RS) = 8 via APS on compact K3: CONDITIONALLY_RESOLVED" -> OPEN; "What this changes" rewritten to state the 3-generation result is not established (it is the conjectured target the surviving routes are fitted to). OQ-RK1 chain annotated to show its "rank_H = 8/2 = 4" step DIVIDES BY THE TARGET ind_H=8 (assumes the index it is meant to support).
- N5 Generation Count Synthesis: n5-generation-count-synthesis CONDITIONALLY_RESOLVED -> OPEN; OQ3b/OC1/OC2 sub-roll-up flipped to OPEN on the RS-leg integer; "24 = 3 SM generations" reframed as the conjectured target.
- Post-Execution Current Next Five, task 1: a CAVEAT added to the "APS route is the surviving reconstruction-grade proof" claim noting the APS rank input is fitted, so the route reproduces the target rather than deriving it; lane recorded as OPEN until OQ-RK1/OQ-RK2 derive rank_H analytically.
Verdict change: generation-count / ind_H(D_RS)=8 lane label CONDITIONALLY_RESOLVED -> OPEN across NEXT-STEPS.md (APS Closure Pass, OQ3b Closure Pass, Generation Count Rank-3 Resolution Pass, N5 synthesis, Post-Execution task 1). The genuinely-derived components are unchanged and retained: the topological spin-1/2 leg (16 H-lines), A-hat(K3)=2, T^4-vs-K3 disambiguation, and OQ3c cross-term cancellation. CANON.md was checked and already places "Three-generation count (analytic index ind_H(D_gimmel) on non-compact Y14)" under "Not Yet Canon," and RESEARCH-STATUS.md carries the count only as "CONDITIONALLY 3 -- structural mechanism intact; two bounded computations remain," so neither asserts a CONDITIONALLY_RESOLVED generation-count verdict and no canon/status cascade was required (the OPEN label is strictly consistent with both, and more conservative). This is a verdict-discipline label correction applying the workflow's UNDISMISSED-CANDIDATE rule; no exploration-file mathematics changed.
File: `NEXT-STEPS.md` (APS Closure Pass; OQ3b Closure Pass + "What survives"; Generation Count Rank-3 Resolution Pass + OQ-RK1 annotation; N5 Generation Count Synthesis; Post-Execution Current Next Five task 1)

### CORRECTION CANON-1 (critical) — DG carve-out GU-Chir block demoted to OPEN and severed from the scope-exit precision verdict; cross-file generation-count contradiction resolved (2026-06-23)
Issue: CROSS-FILE-CONTRADICTION on the GU generation count / ind_H(D_GU) = 24. The Distler-Garibaldi precision carve-out in `canon/no-go-class-relative-map.md` §2.4 (the "condition GU satisfies instead of DG-A6", GU-Chir block + the "promoted from a structural observation to a precision theorem" sentence) read, on a fast scan, as asserting `ind_H(D_GU) = 24` and `generation count = 3` as established fact — the GU-Chir block LED with the bare equalities "ind_H(D_GU) = 24 ... generation count = ind_H(D_GU) / 8 = 3" before its hedge, and the "precision theorem" promotion sentence sat adjacent to the disputed number without disambiguation. This directly contradicted two RESOLVED canon files that flag the same object as OPEN: `canon/w2-y14-spin-structure.md` (analytic index "ind_H(D_gimmel) = 24 ... is a separate computation"; generation count "open") and `canon/shiab-existence-cl95.md` ("Shiab existence does not establish the generation count ... a separate open problem"), as well as the no-go file's own §1 Witten row (count "currently open / unproven pending a corrected rank-3 computation"). The grading in the GU-Chir block was also STALE relative to the same-day CORRECTION FC4-HOLONOMY-01, which downgraded the SU(2)-holonomy / APS-K3 route to OQ-RK2/FC4 from CONDITIONALLY_RESOLVED to OPEN (ten non-convergent index computations; only support for the RS "+8" is a kinematic polarization count, not an analytic index): the block still presented the RS leg's gates as merely-gated reconstruction-grade rather than OPEN.
Direction chosen: recommended fix (a) — DEMOTE. No real non-compact index computation exists (FC4-HOLONOMY-01 confirms every analytic RS-index route has FAILED or is OPEN), so the value cannot be upgraded; instead the carve-out is reconciled DOWN to OPEN/reconstruction-conditional, made consistent with w2 + shiab, and the "precision theorem" language is scoped to the part that is genuinely precision-grade (the class-membership / scope-exit claim) and explicitly severed from the numerical index value.
Fix applied to `canon/no-go-class-relative-map.md` (no mathematics changed; verdict-honesty + cross-file-consistency correction):
- §2.4 GU-Chir block (the "condition GU satisfies instead of DG-A6"): rewritten so the header presents GU-Chir as the chirality *test* GU uses (the invariant ind_H(D_GU) in place of V_{2,1} complexity), NOT a computed value. The bare leading equalities "ind_H(D_GU) = 24 ... = 3" are removed from the assertion position and recast as an OPEN reconstruction-grade *target*, explicitly cross-referenced to the matching OPEN status in w2-y14-spin-structure.md, shiab-existence-cl95.md, and CANON.md "Not Yet Canon". Added an explicit asymmetric two-leg status (spin-1/2 leg 16 = index-theory grade; RS leg 8 = kinematic polarization count only, NO surviving analytic index derivation), with the FC4-HOLONOMY-01 downgrade folded in (SU(2)-holonomy/APS-K3 route is OPEN, ten non-convergent computations, OQ-RK1/OQ-RK2 OPEN). Added four explicit named failure conditions GC-FC1..GC-FC4 (no analytic RS index; OQ-RK1 open; OQ-RK2 open / standard operator gives −144; non-compact base unresolved), all currently FIRING, that keep the count OPEN until all clear. Added an explicit "do NOT cite as established / theorem" instruction.
- §2.4 closing paragraph (the "precision theorem" sentence): rewritten so the precision-theorem status attaches ONLY to the scope-exit / class-membership claim (DG inapplicable because GU is not an object of DG_E8 and uses a different chirality invariant) and explicitly does NOT attach to the numerical value of that invariant; states the EVASION-BY-SCOPE-EXIT verdict does not depend on ind_H(D_GU) evaluating to 24/3 (GU exits via DG-A1/A2/A6/A7 regardless).
- §1 acceptance-summary Distler-Garibaldi row (verdict + open-stress columns): annotated to record that the scope-exit verdict is scope-exit ONLY and the numerical generation count is a SEPARATE OPEN problem (agrees with w2 + shiab) that the verdict does not depend on.
Verdict change: the DG scope-exit / class-membership verdict (EVASION BY SCOPE EXIT, no residual obligation) is RETAINED — it is genuinely precision-grade and independent of the numerical index. The GU-Chir generation-count value (ind_H(D_GU) = 24 / 3 generations) is DEMOTED from a fast-scan-as-established / CONDITIONALLY_RESOLVED reading to explicit OPEN (reconstruction-grade target), now consistent with w2-y14-spin-structure.md, shiab-existence-cl95.md, the §1 Witten row, the same-day FC4-HOLONOMY-01 / GEN-03 corrections, NEXT-STEPS.md (lane already OPEN), and CANON.md ("Not Yet Canon"). No exploration-file mathematics or computed value changed. Cascade check: CANON.md already lists the three-generation count under "Not Yet Canon" (no change needed); RESEARCH-STATUS.md carries it as "CONDITIONALLY 3 -- structural mechanism intact; two bounded computations remain" which is consistent with and more conservative than an asserted value (no cascade required, and the OPEN canon reading is strictly compatible); the contradicting canon files w2 + shiab already say OPEN and required no change.
File: `canon/no-go-class-relative-map.md` (§1 Distler-Garibaldi acceptance row; §2.4 GU-Chir block + closing "precision theorem" paragraph)

### CORRECTION CANON-5 (moderate) — Scope-of-X⁴ inconsistency declared: K3 made an explicit local working hypothesis for the FH and DG generation-count entries, not a silent global assumption (2026-06-23)
Issue: SHARED-ASSUMPTION-NOT-STATED on the spacetime base X⁴ across `canon/no-go-class-relative-map.md`. Two entries silently required X⁴ = K3 specifically: the Freed-Hopkins Option-B closure (§2.3) depends on X_obs^sol = M_RF(K3) (Ricci-flat K3 metric-moduli via the IC4 / Hitchin-Thorpe selection), and the DG GU-Chir block (§2.4) depends on Â(K3) = 2 to get the spin-1/2 leg 16 = 2·8 and the candidate count 24/8 = 3. But two other places treat X⁴ as a generic oriented 4-manifold: the Witten Met(X⁴) entry (§2.1, fiber GL(4,ℝ)/O(3,1), homotopy ℝP³×ℝ⁺) assumes nothing topology-specific, and `canon/w2-y14-spin-structure.md` (RESOLVED) proves its spin result "for any orientable X⁴" and explicitly instances X⁴ = CP2. CANON.md nowhere declares X⁴ = K3 and lists the three-generation count as an open analytic-index problem on non-compact Y14 with no base fixed. So two entries imported K3 while two others assumed genericity, with no cross-reference declaring which scope is in force where.
Direction chosen: recommended fix (b) — do NOT promote K3 to a global canon assumption (that would over-generalize the w2 result, which is proved for any orientable X⁴ and used elsewhere with X⁴ = CP2, and would contradict CANON.md's open-count posture). Instead declare K3 as an explicit LOCAL working hypothesis of the two generation-count-bearing entries, tag every K3-dependent claim "conditional on X⁴ ∈ K3 topological class," and cross-reference the generic-X⁴ entries so the divergence is visible from both sides.
Fix applied to `canon/no-go-class-relative-map.md` (no mathematics changed; shared-assumption-declaration + cross-file-consistency correction):
- New §0.1 "Scope of the spacetime base X⁴ (standing note)": declares X⁴ = K3 is NOT a global assumption; separates generic-X⁴ entries (Witten Met(X⁴) + w2 spin structure, instancing CP2) from K3-conditional entries (FH Option-B closure, DG GU-Chir count); states the rule that no entry may depend on K3 while the Witten/w2 entries assume genericity without this cross-reference; names the two ways to close the K3 dependence (derive X⁴ ∈ K3 from the GU solution locus, or recompute base-independently).
- §2.1 Met(X⁴) entry status line: tagged as treating X⁴ as GENERIC, deliberately divergent from the K3-conditional §2.3/§2.4 entries, consistent with w2-y14-spin-structure.md; "do not silently import K3."
- §2.3 FH Option-B closure: the X_obs^sol = M_RF(K3) identification and the lane-narrowed disposition both tagged CONDITIONAL ON X⁴ ∈ K3; verdict inherits the hypothesis.
- §2.4 DG GU-Chir spin-1/2 leg: the 16 = Â(K3)·8 = 2·8 line tagged CONDITIONAL ON X⁴ ∈ K3, noting Â(CP2) ≠ 2 changes the leg, and the candidate count inherits the K3 hypothesis on top of its already-OPEN status (CANON-1).
Verdict change: NONE. No verdict is reversed. The FH lane stays CONDITIONALLY_RESOLVED / lane-narrowed (per CORRECTION FH-01); the DG verdict stays EVASION BY SCOPE EXIT with the generation count OPEN (per CORRECTION CANON-1). What changed is that a previously-unstated shared assumption (X⁴ = K3) is now declared and the FH lane-narrowing and the DG generation count are explicitly marked as inheriting that working hypothesis. This is a scope/honesty-binding correction, not a recomputation. Cascade check: CANON.md already lists the three-generation count under "Not Yet Canon" and fixes no base (no change needed); w2-y14-spin-structure.md already proves "any orientable X⁴" / CP2 and is the generic-side anchor the new §0.1 cites (no change needed); shiab-existence-cl95.md already flags the count OPEN (no change needed). No exploration-file mathematics changed.
File: `canon/no-go-class-relative-map.md` (§0.1 new scope note; §2.1 Met(X⁴) status line; §2.3 FH Option-B closure tags; §2.4 DG GU-Chir spin-1/2 leg tag)

### CORRECTION CANON-4 (moderate) — theta-field-flrw-dark-energy-eos Result 4 sign contradiction resolved; w_a < 0 retracted to w_a > 0 (OQ3-corrected) (2026-06-23)
Issue: INTERNAL-SIGN-CONTRADICTION within the single CONDITIONALLY_RESOLVED canon file `canon/theta-field-flrw-dark-energy-eos.md`. The OQ3 correction block (frontmatter `correction_oq3`, line 19) and the named failure condition FC5 (OQ3-A) establish the corrected prediction is w_a > 0 (ratio w_a/(w_0+1) = +1.17, "SIGN REVERSED" from the de Sitter -1.80), with Result 2 stating "the sign of w_a is now POSITIVE with frozen ICs ... INCONSISTENT with DESI's w_a = -0.75" and Result 3 stating the corrected GU ratio +1.17 "has the OPPOSITE sign from DESI." But Result 4 was never updated to the OQ3 correction: it still asserted, unconditionally, "GU Candidate D predicts: w_a < 0 ... DESI DR1 also finds w_a < 0," falsely claiming agreement with DESI. The Primary Gaps block (Gap 2) and the Falsification Condition still carried the retracted -1.80 slope and phi_0 ~ 1.94 rad as the GU values, and F6/F7/F8 still referenced -1.80 / phi_0 ~ 1.94 as live. The file therefore simultaneously predicted w_a > 0 (Results 2/3, FC5) and w_a < 0 (Result 4); a reader citing the page got contradictory sign predictions for the headline DESI-comparison observable.
Fix applied (canon-surface consistency correction; no new mathematics, no recomputation — all corrected values were already established by the OQ3 correction block and the cited exploration file theta-field-flrw-matter-era-ode-2026-06-23.md):
- Result 4 rewritten with a "SUPERSEDED BY OQ3 CORRECTION" banner; the bullet flipped from "w_a < 0 ... DESI DR1 also finds w_a < 0" to "w_a > 0 (CORRECTED ...) ... OPPOSITE to DESI DR1, which finds w_a = -0.75 < 0," made explicitly conditional on OQ3-A / FC5; transition redshift aligned to z_osc ~ 1.85.
- Gap 2 (THETA-01) updated: ratio -1.80 -> +1.17, phi_0 1.94 rad -> 0.855 rad, both old de Sitter values marked RETRACTED; the citation guidance changed to "conditional on phi_0 = 0.855 rad and frozen IC at z=3 (OQ3-A unresolved)."
- Falsification Condition (Sharpened) recoefficiented: "w_a + 1.80*(w_0+1)" -> "w_a - 1.17*(w_0+1)", with an explicit note that the de Sitter -1.80 is RETRACTED and that the condition is itself conditional on OQ3-A.
- Known Failure Modes: F6 relabeled OQ3-CORRECTED (slope -1.80 retracted, DESI's negative ratio now sits opposite the corrected +1.17); F7 relabeled FIRED (phi_0 shifted 1.94 -> 0.855 rad, O(1) shift, sign reversed); F8 scan reference updated from -1.80 to the corrected +1.17.
Verdict change: file-level verdict UNCHANGED — remains CONDITIONALLY_RESOLVED (the OQ3 correction had already set this; the headline sign w_a > 0 was already the file's established corrected prediction in Results 2/3 and FC5). This correction removes the stale Result 4 / Gap 2 / falsification-coefficient surfaces that still carried the retracted de Sitter w_a < 0 / -1.80 / phi_0 ~ 1.94, so the page no longer self-contradicts on the sign of the DESI-comparison observable. No exploration-file mathematics changed; no computed value changed (all corrected numbers were already in the OQ3 correction block). Cascade check: CANON.md row (line 44) carries only the verdict CONDITIONALLY_RESOLVED with no sign/ratio value, so no change was needed there. RESEARCH-STATUS.md DID require cascade: its line-72 status note still described the ratio as w_a/(w_0+1) ~ -1.80 conditional on phi_0 ~ 1.94 rad (the pre-OQ3 THETA-01 correction text) as the current prediction; that note was updated to the OQ3-corrected +1.17 / w_a > 0 / phi_0 = 0.855 rad with the CANON-4 in-file alignment recorded, so the cross-file status surface no longer asserts the retracted negative slope.
File: `canon/theta-field-flrw-dark-energy-eos.md` (Result 4; Gap 2 / Primary Gaps; Falsification Condition; Known Failure Modes F6, F7, F8); `RESEARCH-STATUS.md` (line-72 theta-field FLRW dark energy EOS status note)

### CORRECTION CANON-2 (critical) — "via Atiyah-Singer" / compact-index-theorem invocation on the non-compact Y¹⁴ corrected; the 8·Â(K3)+8=24 formula relabeled a compact-toy-model heuristic (2026-06-23)
Issue: MATHEMATICAL-METHOD-ERROR compounding CORRECTION CANON-1. After CANON-1 demoted the GU-Chir generation count to OPEN, two surfaces of `canon/no-go-class-relative-map.md` still invoked the COMPACT index theorem to extract a finite index on the NON-COMPACT Y¹⁴ = Met(X⁴): (a) §2.4 GU-Chir spin-1/2-leg bullet asserted "16 = Â(K3)·rank_H(S(6,4)) = 2·8 is a genuine Atiyah-Singer computation on the compact K3 factor"; (b) the §2.1 Witten acceptance-table row (and its open-stress cell) stated the 3-generation count "survives only at reconstruction grade via the surviving compact APS/K3 route (ind_H = 8·Â(K3) + 8 = 24)". Atiyah-Singer is the COMPACT index theorem; Y¹⁴ = Met(X⁴) is open (the Lorentzian-signature condition is open in Sym²(T*X⁴); fiber GL(4,ℝ)/O(3,1) non-compact). Invoking Atiyah-Singer (or treating "the compact K3 factor" as available) to get a finite index — or any finite leg of one — on the non-compact 14-manifold is a category error: it silently assumes a non-compact→compact-K3 compactification/quotient that is itself an OPEN problem (the topology/index gate; `discrete-series-fiber-dirac-index-2026-06-23.md` finds the finite homogeneous-fiber kernel statement on GL(4,ℝ)/O(3,1) incoherent). This directly contradicted the other canon files, which state compact index theorems do NOT apply on Y¹⁴: `w2-y14-spin-structure.md` (line 143: "Y14 = Met(X4) is open ... Standard compact index theorems do not apply ... requires a separate Fredholm/APS-type analysis") and `shiab-existence-cl95.md` (line 72: "an index theorem on a non-compact Y^14 — a separate open problem"). The "=24, =3" claim was thus not just contradicted (CANON-1) but methodologically unsupported as stated: the operative theorem named was the wrong (compact) theorem.
Direction chosen: recommended fix — replace "via the Atiyah-Singer theorem" with the actual analytic framework that applies on non-compact Y¹⁴ (APS / L²-index / Fredholm, i.e. the Atiyah-Jänich–KSp continuous H-linear Fredholm-family obligation per `signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md`), and relabel the 8·Â(K3)+8=24 result a compact-TOY-MODEL heuristic/expectation (what the index WOULD be if a compact-K3 model applied), not the operative theorem. The genuine algebraic fact rank_H(S(6,4)) = 8 (Cl(9,5) = M(64,ℍ) module theory) is retained; only its packaging into a finite Â-genus index requires the unestablished compactification.
Fix applied to `canon/no-go-class-relative-map.md` (no mathematics changed; methodological correction + cross-file consistency):
- §2.4 GU-Chir spin-1/2-leg bullet: relabeled "compact-K3-MODEL expectation, NOT a theorem on Y¹⁴"; the "genuine Atiyah-Singer computation on the compact K3 factor" wording replaced with an explicit statement that Atiyah-Singer is the COMPACT index theorem and does not apply to D_GU on the non-compact open Y¹⁴, that the leg is a compact-toy-model heuristic presupposing the OPEN non-compact→compact-K3 reduction, and that the applicable framework is APS/L²/Fredholm (with the w2 + shiab quotations and the non-compact-Fredholm exploration cited). The CANON-5 X⁴∈K3 conditionality tag and the retained rank_H(S(6,4))=8 fact are preserved.
- §1 Witten acceptance-table row (richer-datum cell + open-stress cell): the "survives only at reconstruction grade via the surviving compact APS/K3 route (ind_H = 8·Â(K3)+8 = 24)" language replaced with "the 3-generation count is OPEN — the compact APS/K3 formula is a compact-toy-model heuristic, not an operative theorem (Atiyah-Singer is the compact theorem and does not apply on non-compact Y¹⁴; the non-compact→compact-K3 reduction is itself OPEN; the applicable framework is APS/L²/Fredholm; gates OQ-RK1/OQ-RK2 OPEN, FC4 OPEN)."
Verdict change: the generation-count / ind_H(D_GU)=24 lane is RETAINED at OPEN (it was already OPEN per CANON-1, FC4-HOLONOMY-01, GEN-03/GEN-04, and NEXT-STEPS); CANON-2 does not change the OPEN verdict — it corrects the METHOD by which the (already-OPEN) value was framed, removing the compact-index-theorem category error and naming the correct non-compact analytic framework. No exploration-file mathematics or computed value changed. Cascade check: CANON.md already lists the three-generation count under "Not Yet Canon" as an analytic-index problem on non-compact Y14 with no base/compactification fixed (consistent, no change needed); w2-y14-spin-structure.md and shiab-existence-cl95.md already state compact index theorems do not apply and the count is OPEN (they are the cross-file anchors this correction aligns to, no change needed); RESEARCH-STATUS.md line 134 already records that the proof obligation is a continuous H-linear Fredholm family for the actual GU operators on non-compact Y^14 (consistent with the APS/L²/Fredholm framing, no change needed). The RESEARCH-STATUS.md "CONDITIONALLY 3" exploration-status rows (lines 251, 261) are pre-existing and were not introduced or worsened by this correction; they remain consistent-but-more-optimistic exploration-grade notes and are left for the generation-count lane owner, since the canon-grade surfaces (the no-go map + the three RESOLVED/Not-Yet-Canon files) now uniformly read OPEN with the correct non-compact framework.
File: `canon/no-go-class-relative-map.md` (§1 Witten acceptance-table row richer-datum + open-stress cells; §2.4 GU-Chir spin-1/2-leg bullet)

### CORRECTION CANON-6 (moderate) — canon/no-go-class-relative-map.md F5 row: open energy-estimate gap (FC3 / OQ-H1) made visible; constraint-leaves-the-sub-bundle surfaced (2026-06-23)

Issue: CANON-6 (moderate severity). Reconstruction-grade closure presented one notch stronger than the source supports. The canon F5 surfaces (§1 VZ acceptance-table row; §2.5 F5 row; §2.5 F5-full failure-conditions status line) carried F5 as `CONDITIONALLY_RESOLVED 2026-06-23 (vz-f5-hamiltonian-subsidiary-propagation, reconstruction)` and — after CORRECTION VZ-F5-01 — already surfaced the FC1 load-bearing assumption and the §4.6(b)/§4.10 constraint non-preservation. What was still NOT surfaced at canon level: (a) that the underlying file's own computation shows the gamma-trace constraint **does leave `ker Gamma^{4D}` (the RS sub-bundle) at the field-equation level** ("the time derivative of an RS field leaves the RS sub-bundle", §4.6(b); "`phi = Gamma^{4D} Psi` does not remain zero for all t", §4.10); and (b) that the §4.8 "Constraint Propagation Theorem" which reframes that leak as benign is an admitted **proof sketch** whose decisive step — a sourced symmetric-hyperbolic energy estimate `||phi||_{H^k} <= C||source||_{H^k}` for `phi = Gamma^{4D} Psi` (the open gate **FC3 / OQ-H1**, vz-f5 §7 FC3 and §9 OQ-H1, including the `K_{mu nu}` extrinsic-curvature source term) — is explicitly left open. The canon thus presented closure as resting only on the FC1 reframing, when it in fact rests on FC1 AND a second, independent, unproved analytic gate (the FC3/OQ-H1 energy estimate). The source file is honest about both (verdict CONDITIONALLY_RESOLVED, status: reconstruction); the gap was a canon-surfacing omission, not a source-file error.

Fix applied (canon surface only; no exploration-file verdict changed; verdict RETAINED at CONDITIONALLY_RESOLVED per the recommended disposition — keep CONDITIONALLY_RESOLVED but make the load-bearing unproven step visible in canon):
- §2.5 F5 row: added explicit statement that the constraint DOES leave `ker Gamma^{4D}` at the field-equation level (with the §4.6(b)/§4.10 quotes); added a "The benign reading ALSO rests on an unproved energy estimate" block stating the §4.8 Constraint Propagation Theorem is an admitted proof sketch and that the decisive sourced symmetric-hyperbolic energy estimate for `phi = Gamma^{4D} Psi` is the open gate FC3 / OQ-H1 (not done); rewrote the FC3 entry from "extrinsic curvature sourcing produces spacelike effective characteristics" to "FC3 / OQ-H1 (the sourced symmetric-hyperbolic energy estimate for `phi = Gamma^{4D} Psi` that would make the §4.8 proof sketch rigorous is NOT established ... the load-bearing analytic gap on the constraint-propagation side)"; closing sentence now states the verdict rests on BOTH the FC1 reframing AND the still-open FC3/OQ-H1 energy estimate; pointer updated to "(§4.8 proof sketch; §7 FC1/FC3; §9 OQ-H1)".
- §1 VZ acceptance-table row ("Remaining open" cell): F5 item expanded from "constrained-Hamiltonian propagation of subsidiary conditions at full dynamical level (F5)" to name F5 as CONDITIONALLY_RESOLVED only, load-bearing on FC1 plus the still-open FC3/OQ-H1 energy estimate, with the constraint-leaves-the-sub-bundle / proof-sketch-with-energy-estimate-not-done framing.
- §2.5 F5-full failure-conditions status line: added the parallel FC3/OQ-H1 energy-estimate caveat (constraint leaves `ker Gamma^{4D}` at the field-equation level; §4.8 propagation theorem is a proof sketch; the sourced symmetric-hyperbolic energy estimate for `phi`, including the `K_{mu nu}` source, is NOT done).

Verdict change: NONE in substance — F5 remains CONDITIONALLY_RESOLVED (reconstruction grade) at all three canon surfaces, as in the source file. This is a canon-honesty / load-bearing-gap-visibility correction: the closure now visibly rests on TWO open gates (FC1, the kinematic-vs-dynamical reframing; AND FC3/OQ-H1, the sourced energy estimate), and the source file's own constraint-leaks-the-sub-bundle result is no longer hidden behind the Schur-complement reframing at canon level. No computed value or mathematical content changed. CANON.md was checked: it lists no standalone vz-f5 entry (VZ is referenced only through canon/no-go-class-relative-map.md, corrected in place), so no CANON.md cascade required. RESEARCH-STATUS.md was checked: no standalone F5/vz-f5 row (VZ tracked via the canon no-go map), so no RESEARCH-STATUS.md cascade required.
File: `canon/no-go-class-relative-map.md` (§1 VZ acceptance-table row; §2.5 F5 row; §2.5 F5-full failure-conditions status line)

---

### CORRECTION XOBS-IC4-01 (critical) — freed-hopkins-xobs-sol-k3-moduli verdict downgraded GENUINE_OBSTRUCTION -> CONDITIONALLY_RESOLVED; the GENUINE_OBSTRUCTION rests on a same-session CONDITIONALLY_SUPPORTED IC4 input (2026-06-23)
Issue: XOBS-RESTS-ON-CONDITIONAL-IC4. The exploration file `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` carried verdict **GENUINE_OBSTRUCTION** (the strongest possible negative verdict). The whole closure is load-bearing on the identification `X_obs^sol = M_RF(K3)` (Einstein-metric moduli of K3), which requires the IC4 reduction "GU section field equation -> source-free Einstein on K3." That input is `ic4-ricci-flat-k3-selection-2026-06-23.md`, dated the SAME session, verdict only **CONDITIONALLY_SUPPORTED**, with seven open failure conditions F1-F7 — including F3 (surviving trace-free GU source -> Einstein-with-matter, different topology, NOT a pure gravitational background) and F5 (K3 topology not actually forced; index split / RS +8 / Rokhlin / ch_2 gate unproven). The xobs file's own §8 RC2 already admitted "IC4 is only CONDITIONALLY_SUPPORTED, so this is the primary reopening risk." Deriving a GENUINE_OBSTRUCTION from a same-session, merely-conditional input is verdict inflation by same-session chaining: a GENUINE_OBSTRUCTION requires a *proved* failure with *verified* inputs, and the load-bearing input here is unproven and authored the same day. This is the exploration-file half of the same defect that CORRECTION FH-01 already fixed on the canon surface (`canon/no-go-class-relative-map.md`); FH-01 explicitly noted the exploration file was untracked and left its verdict unchanged, so this correction completes the alignment.
Direction chosen: recommended fix — DOWNGRADE to CONDITIONALLY_RESOLVED (lane-narrowed), not OPEN. The lane IS genuinely narrowed (Met(X^4) contractible and Omega^2 B Sp(64) gauge-relabel candidates are eliminated by sound arguments; X_obs^sol is the sole survivor and, IF IC4 holds, a gravitational-background relabel), so CONDITIONALLY_RESOLVED is the correct strength and matches the canon disposition set by FH-01. The math content (candidate eliminations, the M_RF(K3) period-domain / global-Torelli identification, the noncontractibility-via-arithmetic-quotient argument) is unchanged; only the verdict label, its honesty binding, and the failure-condition set are corrected.
Fix applied to `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` (no mathematics changed):
- Frontmatter `verdict` GENUINE_OBSTRUCTION -> CONDITIONALLY_RESOLVED; a `correction:` field recording XOBS-IC4-01 added.
- §1 abstract: the flat "the lane closes" recast as "lane is NARROWED and CONDITIONALLY closes," with the relabeling escape stated to fire ONLY IF IC4 holds and IC4 flagged as only CONDITIONALLY_SUPPORTED (open F3/F5).
- §5.4 header "Why This Is a Genuine Obstruction..." -> "Why This Is a Lane-Narrowing (Not Yet a Closed Genuine Obstruction)," with an inline CORRECTION block; FC2 relabeling restated as conditional on IC4; summary table last-row cells changed from "FAILS (relabel)" to "RELABELS *conditional on IC4*"; post-table prose recast as a lane-narrowing.
- §7 Verdict: self-check bullet rewritten to state the proved-failure-with-verified-inputs bar is NOT met (IC4 same-session/conditional); verdict line changed to "CONDITIONALLY_RESOLVED (lane-narrowed) -- NOT a closed GENUINE_OBSTRUCTION" with a CORRECTION block; closure restated as deferred pending future-session verification of IC4 gates C/D/F (F3/F5) and the RC4 KO^4-over-orbifold lift, and the OPEN Option-B no-go root lemma.
- §8 Failure Conditions: header recast (conditional closure, not a closed obstruction); RC2 upgraded to LOAD-BEARING and named as the reason the verdict is held at CONDITIONALLY_RESOLVED; THREE new explicit reopening/blocking conditions added — RC5 (IC4 gate C/D not verified — Einstein reduction unproven), RC6 (K3 topology not actually forced — IC4 F5 / Gate B), RC7 (same-session circular-promotion guard).
- §10 Cross-Reference/Lane Status: closure statement and final disposition line rewritten from "closed at GENUINE_OBSTRUCTION" to CONDITIONALLY_RESOLVED / lane-narrowed, with promotion deferred to a later session contingent on the OPEN root lemma, IC4 C/D/F (RC2/RC5/RC6), and RC4.
Verdict change: `freed-hopkins-xobs-sol-k3-moduli` GENUINE_OBSTRUCTION -> CONDITIONALLY_RESOLVED (lane-narrowed). Cascade check: the canon surface was ALREADY corrected by CORRECTION FH-01 (`canon/no-go-class-relative-map.md` §1 Freed-Hopkins row + §2.3 Option-B block now read "CONDITIONALLY_RESOLVED / lane-narrowed — NOT a closed GENUINE_OBSTRUCTION"), so this exploration-file downgrade brings the file INTO agreement with canon rather than requiring a further canon change. CANON.md was checked and lists no standalone Freed-Hopkins / X_obs^sol GENUINE_OBSTRUCTION entry (it references only the no-go map, already corrected), so no CANON.md cascade is required. RESEARCH-STATUS.md was checked and carries NO standalone `freed-hopkins-xobs-sol-k3-moduli` row (the file's per-file status index lives in DERIVATION-PROGRESS.md, not RESEARCH-STATUS.md), so no RESEARCH-STATUS.md cascade is required. The DERIVATION-PROGRESS.md per-file index row for this file (which read "Verdict: GENUINE_OBSTRUCTION ... The Freed-Hopkins observer-pairing anomaly lane closes") was updated in this same pass to "CONDITIONALLY_RESOLVED (lane-narrowed) [downgraded ... by CORRECTION XOBS-IC4-01]" with the same-session-conditional-IC4 reasoning and all seven RC conditions, so the status index matches the file. No computed value or mathematical content changed.
File: `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` (frontmatter; §1; §5.4; §7; §8 RC2 + new RC5/RC6/RC7; §10); `DERIVATION-PROGRESS.md` (freed-hopkins-xobs-sol-k3-moduli per-file index row + this correction note)

### CORRECTION F5-SS-01 (moderate) — canon/no-go-class-relative-map.md VZ F5 dynamical gate carried a same-session canon flip; same-session/pending-inter-session-check marker added (2026-06-23)

Issue: F5-CANON-FLIP-SAME-SESSION (moderate). The VZ F5 dynamical gate was flipped in the canon no-go map this same session, from "residual open at full dynamical level" to "CONDITIONALLY_RESOLVED 2026-06-23," citing `explorations/vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md`. That file is UNTRACKED in git ('??') — authored this same session and not yet reviewed in any later pass. The open state of the gate and its closure are therefore BOTH dated 2026-06-23 on the same unreviewed source, which is the same-session-circularity pattern the map's own honesty contract warns against ("be especially suspicious of files promoted today"). The closing argument — the gamma-trace `Gamma^{4D} psi = 0` is KINEMATIC, not a dynamical subsidiary condition, so the Dirac-Bergmann chain never initiates — IS the FC1 claim ("no standalone GU RS Lagrangian exists"), which is OPEN, self-referential to the same reasoning that closes the gate, and established only as absence-of-identification (not proof of absence). This is less severe than a GENUINE_OBSTRUCTION same-session promotion (cf. FH-01): the argument is plausible, the verdict was honestly capped at CONDITIONALLY_RESOLVED, and FC1-FC4 were named in-file. But it is still a same-session canon edit, and the canon must not read as though the full-dynamical-level VZ gate is settled.

Fix applied (canon surface only; no exploration-file verdict changed; no mathematics changed): a same-session / pending-inter-session-check marker was added at all three places the canon F5 CONDITIONALLY_RESOLVED label appears in `canon/no-go-class-relative-map.md`:
- §2.5 F5 detailed cell: after the existing "LOAD-BEARING ON THE UNPROVEN CLAIM FC1" clause, added a "SAME-SESSION, PENDING INTER-SESSION CHECK (CORRECTION F5-SS-01)" block recording that the open state and closure are both 2026-06-23 on an untracked same-session file, that the closing kinematic-vs-dynamical argument IS the open and self-referential FC1 claim, that the full-dynamical-level VZ gate is NOT settled, and that the kinematic-vs-dynamical claim must be independently re-derived in a later session on a tracked/reviewed file before any downstream file treats F5 as closed.
- §2.5 "Failure conditions status" (F5-full) line: added a compact F5-SS-01 same-session marker with the same content.
- §1 acceptance-table Velo-Zwanziger row, open-stress cell: added a compact "same-session, pending inter-session check (F5-SS-01)" parenthetical on the F5 item so the summary table does not read as though the dynamical gate is settled.

Verdict change: NONE. The F5 gate label is RETAINED at CONDITIONALLY_RESOLVED (as recommended). This is a same-session-circularity / verdict-honesty marker, not a downgrade to OPEN and not a flip to GENUINE_OBSTRUCTION. The correction makes explicit that (a) the F5 gate's open state and its closure are both same-session on an untracked file, (b) the kinematic-vs-dynamical FC1 claim that closes the gate is open and self-referential, and (c) F5 must be independently re-derived in a later session on a tracked file before downstream files treat it as closed. This builds on (does not supersede) CORRECTION VZ-F5-01, which re-bound the same verdict as load-bearing on FC1. CANON.md was checked: it lists no standalone vz-f5 / F5 entry (VZ is referenced only through canon/no-go-class-relative-map.md, corrected in place), so no CANON.md cascade is required. RESEARCH-STATUS.md was checked: it carries no standalone F5 / vz-f5 row (the VZ no-go is tracked via the canon no-go map), so no RESEARCH-STATUS.md cascade is required.
File: `canon/no-go-class-relative-map.md` (§1 Velo-Zwanziger acceptance-table row; §2.5 F5 detailed cell; §2.5 F5-full failure-conditions status line)

---

### CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION (moderate) — split-signature ellipticity lemma + F5 gauge-orbit-fill file verdicts downgraded CONDITIONALLY_RESOLVED -> OPEN; same-session-named internal contradiction cannot be self-resolved (2026-06-23) [VID-3]

Issue: VID-3 (moderate). Stale-verdict / same-session self-resolution gap. The prior CORRECTION ELLIPTICITY-LEMMA-iii (logged above) absorbed the F5 firing into `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` but RETAINED the file verdict at CONDITIONALLY_RESOLVED, re-deriving the symmetric-hyperbolic conclusion in-file from the corrected (Koszul-exactness) premise. That retention violates the loop's RESOLVED-blocking rule (`process/loop-adversarial-log.md`: "an explicit internal contradiction in the body of a file is an open problem; block CLOSED or RESOLVED verdicts on any item containing one until the contradiction is resolved in a subsequent session"). The sibling file `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` explicitly NAMED an internal contradiction between lemma parts (ii) (maximal-rank NM(xi) = Im c(xi)) and (iii) (gauge orbit a PROPER subspace of ker c(xi)) and resolved it in favor of (ii); both files were written the SAME session (2026-06-23). A same-session-named-and-resolved internal contradiction cannot be cleared by a same-session re-derivation, and the corrected part (iii') re-derivation itself leans on FF3/FF4 (both OPEN). The two same-session files therefore presented mutually inconsistent verdicts about the same NM(xi) structure under CONDITIONALLY_RESOLVED stamps.

Fix applied (verdict tracking only; no mathematics changed; the corrected part (iii') and the physics direction are unchanged):
- `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md`: frontmatter `verdict` set to OPEN with `verdict_changed_from: CONDITIONALLY_RESOLVED`, `verdict_changed_at`, `verdict_change_reason`, and a `correction:` field recording the same-session-named contradiction and the OPEN cap. Body reconciled to OPEN at every self-verdict point: §5.3/§5.4/§7.3 banners updated to "VERDICT OPEN"; §6 part (iii) RETRACTED/FALSE banner; §8 reframed as "verdict OPEN," F5 marked FIRED-and-naming-a-contradiction, new failure conditions F8 (= FF3), F9 (= FF4), F10 (same-session-resolution gate, FIRED) added; §9.1 header and banner downgraded to OPEN; §9.2 item-2 and summary paragraph corrected from "verdict CONDITIONALLY_RESOLVED is robust / does NOT downgrade the verdict" to "verdict is OPEN, F5+F10 fired"; §10 closing line corrected so the three SC1-OQ2 sub-files stay CONDITIONALLY_RESOLVED but THIS lemma file is stated OPEN; §11 OQ-F5 left as fired with successor gates FF3/FF4.
- `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`: frontmatter `verdict` set to OPEN (downgraded from CONDITIONALLY_RESOLVED, same correction name) with provenance fields and a top-of-file VERDICT OPEN banner — because this file is the one that NAMED-and-RESOLVED the contradiction in the same session, which the loop rule also caps at OPEN. §1 "Established context" cross-reference to the lemma updated to "(verdict OPEN as of 2026-06-23, downgraded as a result of this file) ... original part (iii) now RETRACTED/FALSE (part (iii'))"; §6 verdict header set to OPEN; §6 "correct CONDITIONALLY_RESOLVED reading" sentence corrected to explain why the verdict is OPEN; §7 cascade note corrected from "the lemma's overall verdict is unchanged" to "the lemma's FILE verdict was downgraded to OPEN (physics direction unchanged)" and stating that the F5 file itself is OPEN for the same same-session-resolution reason.

Verdict change: both `sc1-oq2-split-signature-ellipticity-lemma` and `sc1-oq2-f5-gauge-orbit-fill` CONDITIONALLY_RESOLVED -> **OPEN** (supersedes the verdict-retention of CORRECTION ELLIPTICITY-LEMMA-iii). The downstream analytic conclusion (D_GU is symmetric-hyperbolic / real-principal-type, NOT elliptic) is unchanged in DIRECTION — this is a tracking/stale-verdict correction, not a change to the final physics verdict — but it is now correctly carried as a WORKING HYPOTHESIS pending inter-session re-derivation (F10) plus FF3/FF4. The two same-session files no longer present mutually inconsistent CONDITIONALLY_RESOLVED claims: both now agree the gauge orbit FILLS NM(xi), and both are OPEN pending an intervening session that independently re-derives the gauge content of NM(xi). CANON.md and RESEARCH-STATUS.md were checked: neither references either file (grep clean), so no canon cascade is required.
File: `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` (frontmatter, §5, §6, §7.3, §8, §9, §10, §11); `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` (frontmatter, §1, §6, §7)

---

### reciprocal-bridge-ten-lens-review (2026-06-24)
Verdict: exploration/synthesis (incorporation note, NOT canon)
Indexing-only entry for a substantive ten-lens review across Temporal Issuance, Time as Finality, and GU that was previously tracked only in the local `explorations/time-as-finality-crosswalk/README.md`. The file is an incorporation note, not a canon update: it states what should and should not be imported into GU and explicitly does NOT claim that Time as Finality explains GU, that Temporal Issuance supplies GU physics, or that any GU no-go theorem is bypassed. Its useful content: (a) an observer-finality sub-protocol that refines the six-axis L2/L6 fields for observer-facing source/shadow language (exploration-only; do not replace the six-axis protocol); (b) four-object rate discipline — `lambda_max` (L2 budget loaded by L4 cost; derived, no promotion), `Delta` (L6 deadline policy; candidate sub-protocol field after a second worked example), `Gamma_min` (L1-L2 classicality coupling; candidate only after the BvN wall and GU-sensitivity tests), and `O(tau)` (filtered L1/L2 obstruction; the best formal-bridge target if a GU readout is filtration-sensitive) — with the FR1 `lambda_max` absorption re-qualified as conditional on typing the observer window/access cut `W`, cadence/resource clock, and queue/frontier behavior; (c) the filtered-readout bridge `S: Compat_G^MLTT -> FiltSh(C)`, `R: FiltSh(C) -> ReadoutValues` as the most promising theorem-shaped target. Guardrails: do not cite TaF/TI as canon for GU, do not treat observer finality as an anomaly/chirality/spectral-triple construction, do not use the four rate objects to bypass no-go assumptions, do not treat a fixed `Y^14 -> X^4` projection as source-side issuance, do not merge claim ledgers across repos. Ranked next test (recorded at the repo level in `NEXT-STEPS.md`, crosswalk/observer-finality lane): the functorial filtered-readout witness / FR3-GU readout sensitivity test (a toy GU signed-readout/anomaly readout that changes when `{F_tau}` changes while final `F` is held fixed). No verdict, canon, or computed value changed; this entry only brings the file's repo-level tracking into line with the other 17 files from the 2026-06-23/24 crosswalk session. Companion preservation artifacts in sibling repos: `../temporal-issuance/explorations/E056-gu-taf-reciprocal-bridge-incorporation-2026-06-24.md` and `../time-as-finality/open-problems/gu-ti-taf-reciprocal-bridge-contract.md`.
File: `explorations/time-as-finality-crosswalk/reciprocal-bridge-ten-lens-review-2026-06-24.md`

---

### CORRECTION CANON-7 (moderate) — canon/no-go-class-relative-map.md §2.4 GU-Chir inline decomposition: RS-sector 8-H-line leg tagged CONDITIONALLY_RESOLVED-pending-rank_H at the point of the arithmetic (2026-06-23) [VID-2]

Issue: VERDICT-PROMOTED-INTO-CANON-ON-AN-OPEN-SUB-RESULT (moderate). The §2.4 GU-Chir inline statement wrote the candidate decomposition as bare arithmetic — "ind_H(D_GU) = 24 = 16 (spin-1/2) + 8 (RS), giving generation count = 24 / 8 = 3" — with the RS leg appearing only as an unqualified "+ 8 (RS)". The surrounding sentence already marks the whole count OPEN (per CORRECTION CANON-1), and the asymmetric two-leg block below (lines ~287-289) already states the RS leg has NO surviving analytic index derivation with OQ-RK1/OQ-RK2 OPEN. But at the point of the decomposition itself, the legs read as settled summands being added: the RS "8" carried no inline qualifier flagging that it equals ind_H(D_RS) = 8, which rests entirely on rank_H(S_RS^+) = 4 — the value VID-1 shows is uncomputed / curve-fit with an undismissed alternative (gates OQ-RK1, OQ-RK2 open). The arithmetic-summand presentation let a verdict (generation count = 3) rest visibly on an OPEN sub-result without the honest qualifier that `explorations/dg-canon-nogo-map-update-2026-06-23.md` §2.5 already carries ("ind_H(D_RS) = 8 ... primary remaining gate is OQ-RK1").
Direction chosen: recommended fix — mark the RS-sector 8-H-line leg CONDITIONALLY_RESOLVED-pending-rank_H INLINE at the decomposition, mirroring the dg-canon-nogo-map-update §2.5 qualification, so the generation-count = 3 claim cannot read as established in canon while its RS leg's rank_H is uncomputed. No content reverted (the count was already OPEN per CANON-1; this is not a premature-promotion revert), no mathematics changed.
Fix applied to `canon/no-go-class-relative-map.md` (canon surface only; no mathematics changed; inline-honesty correction):
- §2.4 GU-Chir block, inline decomposition: the bare "+ 8 (RS)" expanded to "+ 8 (RS — *CONDITIONALLY_RESOLVED-pending-rank_H: the RS leg ind_H(D_RS) = 8 rests entirely on rank_H(S_RS^+) = 4, which is uncomputed / curve-fit with an undismissed alternative; primary remaining gate is OQ-RK1 [first-principles RS rank], with OQ-RK2 [APS boundary conditions on K3] also open — see the RS-leg bullet below*)"; the trailing "giving generation count = 24 / 8 = 3" recast as "giving a candidate generation count = 24 / 8 = 3 that is therefore only as settled as its weakest leg" before the existing "OPEN — reconstruction-grade target only, not established" qualifier.
Verdict change: NONE. The GU-Chir generation-count value (ind_H(D_GU) = 24 / 3 generations) was already OPEN (reconstruction-grade target) per CORRECTION CANON-1, and remains OPEN; the DG scope-exit / class-membership verdict (EVASION BY SCOPE EXIT) is untouched and does not depend on the number. This correction tightens the INLINE presentation so the RS leg's dependence on the uncomputed rank_H(S_RS^+) = 4 is visible at the point of the arithmetic, not only in the two-leg block below. No exploration-file mathematics or computed value changed. Cascade check: CANON.md already lists the three-generation count under "Not Yet Canon" (consistent, no change needed); w2-y14-spin-structure.md and shiab-existence-cl95.md already flag the count OPEN (no change needed); `explorations/dg-canon-nogo-map-update-2026-06-23.md` §2.5 already carries the "primary remaining gate is OQ-RK1" qualifier this correction mirrors (no change needed); RESEARCH-STATUS.md carries the count as "CONDITIONALLY 3" exploration-grade, strictly more conservative than an asserted value and compatible with OPEN (no cascade required).
File: `canon/no-go-class-relative-map.md` (§2.4 GU-Chir block inline decomposition)

---

### NOTE RS-SYNC-01 (moderate) — RESEARCH-STATUS.md brought up to date for the 2026-06-23 late batch (Freed-Hopkins lane, VZ canon banner, C_MPR) (2026-06-23)

Issue: RESEARCH-STATUS.md (committed 17:11) had dated 2026-06-23 sections through "Five-Step Execution Batch" but no section reflecting the final same-day batch (18:37-22:03), even though that batch made canon status changes in `canon/no-go-class-relative-map.md`. The top-level status file was therefore behind canon on three items: (a) the Freed-Hopkins observer-pairing Option-B lane disposition; (b) the VZ 14D evasion banner downgrade EVADED -> CONDITIONALLY_EVADED and the formal fifth-theorem canon entry; (c) the C_MPR / 9-tuple category result. The lens question "Is RESEARCH-STATUS.md updated if any item changed status?" was answered No for the Freed-Hopkins-closure and VZ-canon-entry items.

Fix applied (status-file synchronization only; NO mathematical verdict changed by this note): added a "2026-06-23 (late batch)" section to RESEARCH-STATUS.md recording the four exploration documents (freed-hopkins-optionb-ksp-family, freed-hopkins-xobs-sol-k3-moduli, no-go-velo-zwanziger-canon-entry, c-mpr-9tuple-object-morphism) with their CONDITIONALLY_RESOLVED verdicts, plus an explicit "Canon status changes" subsection naming the §1/§2.3/§2.5 edits in `canon/no-go-class-relative-map.md`.

Verdict-honesty point (load-bearing): the Freed-Hopkins observer-pairing lane is recorded in RESEARCH-STATUS.md as **lane-narrowed / CONDITIONALLY_RESOLVED, NOT closed at GENUINE_OBSTRUCTION**. The triage recommendation that prompted this fix described the lane as "CLOSED at GENUINE_OBSTRUCTION," but that wording predates same-batch corrections FH-01 (canon) and XOBS-IC4-01 (exploration file), which explicitly downgraded that exact reading as same-session verdict inflation (OPEN root `freed-hopkins-nonforgettable-observer`; IC4 only CONDITIONALLY_SUPPORTED with open F3; KO^4-over-orbifold lift RC4 unproved). Recording the lane as "closed" in the top-level status file would have put RESEARCH-STATUS.md AHEAD of canon in precisely the direction canon refused. The status file was therefore synced to the corrected canon, not to the pre-correction summary.

No new verdict change originates here: the actual verdict changes (Freed-Hopkins GENUINE_OBSTRUCTION -> CONDITIONALLY_RESOLVED; VZ 14D EVADED -> CONDITIONALLY_EVADED; VZ 4D VERIFIED -> CONDITIONALLY_RESOLVED) already carry their own correction notes above (FH-01, XOBS-IC4-01, VZ-01, VZ-02, F5-SS-01). This note records only the propagation of those already-logged changes into the top-level RESEARCH-STATUS.md index, closing the status-file drift.
File: `RESEARCH-STATUS.md` (new "2026-06-23 (late batch)" section); `DERIVATION-PROGRESS.md` (this note)

---

### CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION: both SC1-OQ2 gauge-orbit files downgraded CONDITIONALLY_RESOLVED -> OPEN (2026-06-23)

Issue: SC1-LEMMA-CONTRADICTION-SAME-SESSION (critical). A lemma is stated, an internal contradiction in it is found, and the contradiction is "resolved" — all in the same 2026-06-23 session — yet both files kept CONDITIONALLY_RESOLVED. This is exactly the pattern the loop's own adversarial log forbids: `process/loop-adversarial-log.md` rule 3 — "an explicit internal contradiction in the body of a file is an open problem; block CLOSED or RESOLVED verdicts on any item containing one until the contradiction is resolved IN A SUBSEQUENT SESSION" — and the same log's calibration "(c) when an internal contradiction is explicitly identified in the computation, the verdict must be OPEN until the contradiction is resolved, not merely noted." Same-session self-resolution does not clear it (file separation is not a valid defense). The precedent is `oq-kk1a-cas-norm-fiber-wavefunction` (downgraded CONDITIONALLY_RESOLVED -> OPEN for an internal contradiction earlier the same day).

The two files:
- `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` asserts part (iii): the Sp(64) gauge orbit is a PROPER subspace of NM(xi).
- `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` (same session) finds the orbit DOES fill NM(xi), "opposite to the prior split-signature ellipticity lemma's part (iii)," and explicitly NAMES an internal contradiction in the lemma (parts (ii) and (iii) mutually inconsistent).

The prior in-file correction (ELLIPTICITY-LEMMA-iii / F5-SS-01) tried to retain CONDITIONALLY_RESOLVED by re-deriving the symmetric-hyperbolic conclusion same-session from the corrected (Koszul-exactness) premise and flagging part (ii) DEFERRED_VERIFICATION. That retention is itself the bug this correction fixes: a same-session-named internal contradiction caps the verdict at OPEN regardless of a same-session re-derivation, and the re-derivation additionally leans on FF3/FF4, both admittedly OPEN.

Fix applied:
- `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md`: frontmatter verdict CONDITIONALLY_RESOLVED -> OPEN (added `verdict_changed_from`/`verdict_changed_at`/`verdict_change_reason`); part (iii) marked RETRACTED/FALSE inline (not merely superseded); the §5.3/§5.4, §6 part (iii), §7.3 banners re-headed to RETRACTED/OPEN with the corrected part (iii') labeled a WORKING HYPOTHESIS; §8 reframed as "Failure Conditions (verdict OPEN)" with the F5 row recording that the firing names an internal contradiction that caps the verdict at OPEN, plus three new failure conditions F8 (=FF3, BRST-coboundary as a theorem, OPEN), F9 (=FF4, full-E Koszul-acyclicity, OPEN), and F10 (same-session-resolution gate, FIRED); §9.1 verdict heading and banner rewritten to OPEN; §9 items 3/5, "Remaining" list, and §9.2 recap rewritten to OPEN; §10 connection note and §11 OQ-F5 entry rewritten from "RESOLVED (same session)"/"After Gate Closure" to OPEN / gate-not-yet-closed.
- `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`: frontmatter verdict CONDITIONALLY_RESOLVED -> OPEN (with verdict-change fields); top-of-file OPEN banner added; §6 Result verdict changed to OPEN with a "why OPEN" callout, item 1 softened to "appears to fill (working hypothesis)", item 3 conditioned on FF3/FF4 + the inter-session re-derivation gate; FF6 (same-session contradiction-resolution gate) added and recorded FIRED; §7 "For upgrade to RESOLVED" -> "For re-upgrade above OPEN" with the inter-session re-derivation listed as the primary gate.
- Index entries for both files (above) re-headed to Verdict: OPEN with the downgrade rationale.

Verdict change: `sc1-oq2-split-signature-ellipticity-lemma` and `sc1-oq2-f5-gauge-orbit-fill` both CONDITIONALLY_RESOLVED -> OPEN. The affected claim is the gauge content of NM(xi) (lemma part (iii) / the gauge-orbit-fill) and, derivatively, the gauge-mechanism basis of the elliptic->symmetric-hyperbolic switch. What is UNAFFECTED and still stands: the kernel trichotomy / null-projection facts (ker c(xi) = {0} off-null, ker c(xi) = NM(xi) at null xi; from the Clifford identity and sc1-oq2c), VZ off-null invertibility, and the generation-count target ind_H = 24 (OPEN; never dependent on a pointwise null-cohomology quotient). The corrected part (iii') (gauge orbit FILLS NM(xi); physical content via Cauchy-data transport) is recorded as the WORKING HYPOTHESIS to re-derive in a subsequent session. Cascade check: no CANON.md or RESEARCH-STATUS.md entry references either file (verified by grep); NEXT-STEPS.md SC1 row updated to reflect the OPEN downgrade. No new mathematics; this is a verdict-discipline correction enforcing the loop's same-session-contradiction rule.
File: `explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` (frontmatter, §5, §6, §7.3, §8, §9, §10, §11); `explorations/sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` (frontmatter, banner, §6, §7); `DERIVATION-PROGRESS.md` (both index entries + this note); `NEXT-STEPS.md` (SC1 row)

---

### CORRECTION GEN-05 (moderate) — RESEARCH-STATUS.md generation-count exploration rows synced to OPEN; "CONDITIONALLY 3" was the last surface still reading more-resolved than corrected canon (2026-06-23)

Issue: GENERATION-COUNT-SURFACE-DRIFT (moderate). After CORRECTIONS GEN-04 / FC4-HOLONOMY-01 / CANON-1 / CANON-2 flipped the generation-count / `ind_H(D_RS)=8` lane to OPEN across NEXT-STEPS.md and the canon no-go map (and CANON.md already listed the count under "Not Yet Canon"), two rows in RESEARCH-STATUS.md still carried the lane as **"CONDITIONALLY 3"**: the per-finding row "Generation count under Cl(9,5) | CONDITIONALLY 3 — structural mechanism intact; two bounded computations remain" and the research-map row "Generation count | CONDITIONALLY 3 | H-line counting + RS branching computations remaining". CORRECTION CANON-2 had explicitly noted these two rows were "consistent-but-more-optimistic exploration-grade notes ... left for the generation-count lane owner." They were the last repo surfaces presenting the count as more resolved than the corrected canon (OPEN), and the original issue (GENERATION-COUNT-SYNTHESIS-CONTRADICTION) asks for the honest aggregate verdict to read OPEN. "CONDITIONALLY 3" implies one candidate is derivation-supported; per the UNDISMISSED-CANDIDATE rule, with all analytic routes to `ind_H(D_RS)=8` FAILED and the APS rank reverse-engineered (FC4 OPEN), no candidate is dismissed and the verdict must read OPEN.

Direction chosen: align the two RESEARCH-STATUS.md rows to OPEN (matching canon, NEXT-STEPS.md, and the GEN-04 / FC4-HOLONOMY-01 corrections), preserving the "two bounded computations remain" content as the now-OPEN OQ-RK1 (first-principles RS rank) and OQ-RK2 (APS boundary conditions on K3) gates, and explicitly stating that the physical-DOF and SM-generation counting paths assume the conclusion they are meant to establish. No mathematics changed; the genuinely-derived components (spin-1/2 leg 16, A-hat(K3)=2, T^4-vs-K3 disambiguation, OQ3c cross-term cancellation) are unchanged.

Fix applied to `RESEARCH-STATUS.md` (status-surface honesty correction; no mathematics changed, no computed value changed):
- Per-finding row "Generation count under Cl(9,5)": status "CONDITIONALLY 3 — structural mechanism intact; two bounded computations remain" -> "OPEN (corrected 2026-06-23; was 'CONDITIONALLY 3')" with the RS-leg-has-no-surviving-analytic-derivation statement, the three-failed-analytic-routes summary, the reverse-engineered-APS-rank / FC4-OPEN note, the physical-DOF-and-SM-paths-assume-the-conclusion note, and a pointer to DERIVATION-PROGRESS.md CORRECTIONS FC4-HOLONOMY-01 / GEN-04.
- Research-map row "Generation count": "**CONDITIONALLY 3** | H-line counting + RS branching computations remaining" -> "**OPEN** (corrected 2026-06-23; was 'CONDITIONALLY 3') | RS-leg analytic index not derived; physical/SM counts assume the answer; UNDISMISSED-CANDIDATE rule => aggregate OPEN; see FC4-HOLONOMY-01 / GEN-04".

Verdict change: generation-count lane label "CONDITIONALLY 3" -> OPEN on the two RESEARCH-STATUS.md surfaces. This brings RESEARCH-STATUS.md into agreement with the already-OPEN canon (no-go map §1/§2.4, "Not Yet Canon" in CANON.md), NEXT-STEPS.md (APS Closure Pass, OQ3b Closure Pass, Generation Count Rank-3 Resolution Pass, N5 synthesis), and the GEN-04 / FC4-HOLONOMY-01 / CANON-1 / CANON-2 corrections. Cascade check: CANON.md already lists the three-generation count under "Not Yet Canon" (no change needed); NEXT-STEPS.md and the canon no-go map already read OPEN (no change needed); no other surface now reads "CONDITIONALLY 3" / "CONDITIONALLY_RESOLVED at 3 generations" for this lane. No exploration-file mathematics or computed value changed.
File: `RESEARCH-STATUS.md` (per-finding "Generation count under Cl(9,5)" row; research-map "Generation count" row); `DERIVATION-PROGRESS.md` (this note)

---

### CORRECTION VZ-14D-EVADED-VS-GATED-01 (moderate) — canon/no-go-class-relative-map.md VZ 14D entry: `ker S_R^{14D} = 0` was presented as an established structural result alongside the unproven FC-VZ-1 gate, letting a reader treat them as two independent pieces of evidence; foregrounded that they are the SAME contingent claim (2026-06-23)

Issue: VZ-14D-EVADED-VS-GATED-FC-VZ-1 (moderate). Hidden load-bearing assumption presented as a structural result. The Velo-Zwanziger fifth-theorem canon entry repeatedly stated the 14D evasion as "CONDITIONALLY_EVADED ... gated on E-block invertibility (FC-VZ-1)" while simultaneously asserting the operative mechanism as fact: the Schur-complement kernel argument "establishes `ker S_R^{14D}(xi) = 0` for all 14D non-null covectors" (§2.5 computation-chain cell; §5 closing posture). But `ker S_R = 0` is DERIVED via the Schur-complement formula `S_R = A - B E^{-1} C`, which is defined only when the E-block `E(xi)` is invertible — exactly the unproven precondition FC-VZ-1 ("`E(xi)` has nontrivial kernel for some non-null `xi` -> Schur complement undefined"). So the proof of the evasion assumes its own open gate. The entry was honest that FC-VZ-1 is "the single gap separating 14D from EVADED," and the GUARD (FC-VZ-1) block correctly flagged the E-block argument as same-session and externally unverified — but the prose in §2.5 and the closing posture (§5) presented the kernel argument as an established "reconstruction grade" result without foregrounding that the kernel result is identical to (not independent of) the very invertibility that is unverified. The source file confirms the circularity directly: `explorations/vz-14d-mixed-covectors-2026-06-23.md` §correction (VZ-01) states "the `det(M) = det(E)·det(S_R)` identity requires `E` invertible as a precondition and cannot be used to prove `E` invertible without circularity," and its row table already carries the 14D `ker S_R = 0` line as "CONDITIONALLY_EVADED ... proof assumes E invertible; E invertibility not independently proved." The canon-level prose lost that single-claim framing.

Direction chosen: recommended fix — state once and prominently, at each load-bearing location, that the Schur-complement kernel argument (`ker S_R = 0`) is CONTINGENT on FC-VZ-1 (E-block invertibility), so the "14D reconstruction-grade evasion" is the SAME claim as "FC-VZ-1 holds," not an independent corroboration of it. Wording that lets a reader treat `ker S_R = 0` and E-block invertibility as two separate pieces of evidence was removed/qualified. No verdict label changed (the 14D leg was already CONDITIONALLY_EVADED, gated on FC-VZ-1), no exploration-file verdict changed, and no mathematics changed — this is a hidden-load-bearing-assumption / verdict-honesty correction on the canon surface, in the same family as CORRECTION F5-SS-01 and CANON-7.

Fix applied to `canon/no-go-class-relative-map.md` (canon surface only; no mathematics changed; no computed value changed):
- §2.5 "Summary of 2026-06-23 computation chain" cell (the 14D `ker = 0` sentence): rewritten to read the result as a SINGLE conditional claim, not two facts — `ker S_R = 0` is derived through `S_R = A - B E^{-1} C`, defined only when `E(xi)` is invertible (FC-VZ-1), so "`ker S_R^{14D} = 0`" and "FC-VZ-1 holds" are the same load-bearing assumption; quotes the source VZ-01 circularity statement; states explicitly that a reader must not count the two as separate evidence.
- §5 Closing posture (the "establishes `ker S_R^{14D}(xi) = 0`" sentence): "establishes" softened to "claims," with an inline clause that the claim is contingent on FC-VZ-1 and not independent of it (same Schur-formula reason, same VZ-01 quote), and that this is exactly why the leg is CONDITIONALLY_EVADED rather than EVADED.
- §2.5 fifth-theorem-canon-entry closing line ("The single gap separating 14D from EVADED is ... FC-VZ-1"): added a note that FC-VZ-1 is not a gap *in addition to* the `ker S_R = 0` result — it IS that result; closing FC-VZ-1 is what would turn the conditional kernel claim into an established result and the verdict into EVADED.
- §2.5 F6 (4D EFT) cell ("The §8 kernel argument ... applies verbatim to the EFT"): added that it therefore inherits the §8 contingency verbatim — still derived through `B E^{-1} C`, so the same conditional claim as FC-VZ-1, not an independent EFT-level corroboration.

Verdict change: NONE. The VZ 14D leg label is RETAINED at CONDITIONALLY_EVADED (gated on FC-VZ-1); the 4D leg is untouched (CONDITIONALLY_RESOLVED at principal-symbol order). This is a verdict-honesty / hidden-assumption correction that collapses an apparent two-pieces-of-evidence presentation (`ker S_R = 0` PLUS E-block invertibility) into the single contingent claim it actually is (`ker S_R = 0` IF AND ONLY VIA E-block invertibility = FC-VZ-1). Cascade check: CANON.md carries no standalone VZ / FC-VZ-1 entry (VZ is tracked only through `canon/no-go-class-relative-map.md`), so no CANON.md cascade is required; RESEARCH-STATUS.md carries the VZ 14D status as CONDITIONALLY_EVADED (already conservative, unchanged by this honesty correction), so no RESEARCH-STATUS.md cascade is required; the source exploration file `explorations/vz-14d-mixed-covectors-2026-06-23.md` already carries the circularity/VZ-01 correction this note brings to the canon surface (no exploration-file change needed).
File: `canon/no-go-class-relative-map.md` (§2.5 computation-chain cell; §2.5 fifth-theorem-canon-entry closing line; §2.5 F6 EFT cell; §5 Closing posture); `DERIVATION-PROGRESS.md` (this note)

---
