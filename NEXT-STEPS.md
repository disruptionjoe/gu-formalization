---
title: "Next Steps For Contributors"
status: active_research
doc_type: roadmap
updated_at: "2026-06-22"
---

# Next Steps For Contributors

This repo should not ask contributors to solve Geometric Unity. The useful unit is a bounded test with a clear failure condition.

## Best First Tasks

| order | task | output | best for |
|---:|---|---|---|
| 1 | Build or improve the no-go assumption/evasion matrix. | A precise assumption/exits table. | mathematicians, physicists, careful generalists |
| 2 | Fill one six-axis candidate specification. | One complete substrate/observer/pairing/causal/emergence/loop spec. | anyone proposing a path |
| 3 | Strengthen the finite Connes control checklist. | A clearer Type II1 extension requirement. | NCG/operator-algebra contributors |
| 4 | Work on the signed-readout theorem core. | Definitions, theorem statement, proof, or counterexample. | TCS, math, lattice-QFT readers |
| 5 | Run the observer-finality record-graph test. | A diagram and definitions separating evidence, causality, finality, and readout. | distributed systems, foundations, TCS contributors |
| 6 | Claim-mine a transcript-rich GU media source. | Timestamped rows in the source ledger. | source researchers, science communicators |

## Highest-Upside Paths

| path | status | publish potential | next action |
|---|---|---:|---|
| Class-relative no-go map | canon | 5 | sharpen assumptions and known exits |
| Six-axis specification protocol | canon | 5 | add more filled examples |
| Type II1 spectral SM checklist | canon / active research | 5 | specialist review of KO-dim and principal-graph issues |
| Signed-readout boundary theorem | active research | 5 | prove monotonicity criterion and PN/Jordan factorization |
| Observer-finality record-graph test | exploration | 4 | test whether finality semantics clarify signed-readout without smuggling global time |
| Observer-pairing anomaly enrichment | exploration | 3 | build a toy enriched-bordism example |
| C_MPR / 9-tuple / BvN wall | exploration | 3 | state object, morphism, and proof obligations before claiming theorem status |

## Nguyen Critique: Priority Research Items

These three tasks are the direct operational outputs of the full assessment in
`explorations/nguyen-gu-critique/`. They are ranked by how much they constrain
everything downstream.

| order | task | output | blocker if skipped |
|---:|---|---|---|
| ~~N1~~ **RESOLVED 2026-06-22** | **Signature audit** — redo §3.1's complexification argument in split-signature (7,7) with Majorana–Weyl spinors. **Verdict: RESOLVED.** Correct signature is (9,5), not (7,7). Derivation: fiber Frobenius (7,3) → trace-reversal → (6,4) fiber + (3,1) base = (9,5) total. Correct algebra is Cl(9,5) ≅ M(64,H), spinor module S = H^{64}. Unannotated-⊗ℂ gap does NOT arise in (9,5)/quaternionic setting; shiab exists as H-linear hence R-linear Spin(9,5)-equivariant map. | — | — |
| ~~N2~~ **SUBSTANTIALLY ADVANCED 2026-06-22** | **Shiab from Spin(7,7)-invariant data** — shiab existence confirmed under correct (9,5) signature; anomaly structure resolved. **Verdict: RESOLVED for existence; anomaly structure resolved (Sp(64) is anomaly-free); residual open question is IG dimension matching.** The shiab Phi: Omega^2(Y^{14}) ⊗ S → Omega^1(Y^{14}) ⊗ S exists as a Spin(9,5)-equivariant H-linear map (Clifford contraction). The gauge group is Sp(64) = U(64,H), not U(128); Sp(64) has no perturbative or global Z_2 gauge anomaly in 14D. The specific residual form of the anomaly objection is: dim sp(64) = 8256 vs. the 16384 that Nguyen's U(128) dimension-matching required. Whether the tau+ construction selects a larger subgroup within Sp(64) spinor automorphisms that resolves this gap is the outstanding computation. See `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md`. | — | The IG dimension matching question blocks full anomaly resolution. |
| N3 | **Discharge or record H3** — the Čech-H¹ ↔ holonomy dictionary in `time-as-finality` (`tests/T63`) is conditional on H3; run the `cech_sheaf_fixture` in `temporal-issuance` (E015 route). | H3 discharged, or H3 recorded as the named open blocker. | Current holonomy results are conditional; their status is unresolved. |
| ~~N4~~ **RESOLVED 2026-06-22** | **IG dimension matching** — **Verdict: RESOLVED. Nguyen §2 FULLY CLOSED.** The tau+ homomorphism is purely group-theoretic and works for any Lie group G, including G = Sp(64). The 16384 = dim u(128) figure was a coincidence of the (7,7) real-type Clifford algebra (where dim_R Cl(7,7) = 128^2 = dim_R u(128)) with no physical basis in the (9,5) setting. The shiab Phi: Omega^2(Y^{14}) ⊗ S → Omega^1(Y^{14}) ⊗ S depends on Cl(9,5) and S = H^{64}, NOT on the gauge algebra sp(64) — shiab and gauge algebra dimensions are independent (they live in disjoint bundles). The double coset equivariance theta(tau+(g_a) · omega · tau+(g_b)) = Ad(g_b)^{-1} theta(omega) holds for G = Sp(64) by the standard gauge-theoretic proof. dim_R sp(64) = 8256 is the correct figure for the (9,5) IG construction. See `explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`. | — | — |
| ~~N5~~ **CONDITIONALLY RESOLVED 2026-06-22** | **Generation count — two bounded computations** — both completed at exploration/reconstruction grade. **(a) ℍ-line counting:** D_GU commutes with right-ℍ multiplication (proved — Clifford multiplication is ℍ-linear; shiab Φ is ℍ-linear; d_A is ℍ-linear); ker(D_GU) is a right-ℍ-module; the natural index is ind_ℍ(D_GU) ∈ ℤ (KO-theory index, counts ℍ-lines not ℝ-lines); 8 ℍ-lines per SM generation; factor-of-4 gap between "dim_R(S⁺)/32 = 4 generations" and the claimed 2 spin-1/2 sectors is resolved by using the correct counting unit. **(b) RS(3,1) ⊗ S(6,4) SM branching:** S(6,4) = ℂ^16 decomposes under Pati-Salam as (4,2,1) ⊕ (4̄,1,2) [verified, 8+8=16 complex dims ✓]; under SU(3)×SU(2)_L×U(1)_Y gives Q_L(3,2,1/6) + L_L(1,2,-1/2) + ū_R(3̄,1,-2/3) + d̄_R(3̄,1,+1/3) + ē_R(1,1,+1) + ν_R(1,1,0) = 6+2+3+3+1+1 = **16 Weyl fermions = 1 SM generation** [verified]; RS(3,1) ⊗ S(6,4) contributes 1 SM generation (16 Weyl fermions, flipped-chiral = conjugate internal reps, SM charges from S(6,4) unchanged). **Generation count = CONDITIONALLY 3.** Representation-theory conditions: CLOSED. Remaining open: (i) ind_ℍ(D_GU) = 24 from topology (analytic index theorem); (ii) non-compact index theory applicability on Y¹⁴. See `explorations/generation-count-sm-branching-closure-2026-06-22.md`. | Both (a) and (b) pass at reconstruction grade. Remaining open: analytic index computation (topological data on X⁴). | The analytic conditions remain open; the representation-theory conditions are now closed. |
| N6 | **w_2(Y^{14}) via Gysin sequence** — compute the second Stiefel-Whitney class of Y^{14} = Met(X^4) using the Gysin sequence for the fiber bundle pi: Y^{14} → X^4. Determine whether w_2(Y^{14}) = pi*(w_2(X^4)), which would confirm the canonical Dirac operator D_ℊ exists for any spin 4-manifold X^4 without any section choice. | Algebraic topology computation confirming or correcting the spin structure condition for D_ℊ. | Without this, the canonical Dirac operator on Y^{14} is only conditionally defined. |

**Constraint on all three:** No output from N1–N3 should be framed as a Nguyen
refutation in published form. These repos specify escape routes; they do not prove
them. Framing: "these are the constructions GU would need; we are attempting them."

---

## Five-Run Issuance-Rate Findings: Specific Follow-On Tasks (2026-06-22)

These tasks emerged from the five-run observer-contact analysis in
`explorations/time-as-finality-crosswalk/five-run-issuance-rate-observer-contact-2026-06-22.md`.
They are exploration-grade; none are ready for active research or canon without
the derivations specified below.

| order | task | output | blocker if skipped |
|---:|---|---|---|
| FR1 | **Sorkin absorption test** — take example-02 (Sorkin causal-set observer) from six-axis examples and ask: what is the maximum rate at which new causal-set elements can be added to the observer's past cone while preserving the finality relation? Is this determined entirely by L4 + L2, or does it require a new field? | Clear verdict: `lambda_max` absorbed by L4+L2, or new field required in the observer-finality sub-protocol. | Without this, the absorption verdict for the issuance rate concept is conditional rather than confirmed. |
| ~~FR1~~ **RESOLVED 2026-06-22** | Worked check at `explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`. **Verdict: ABSORBED (confirmed, not conditional).** Derived `lambda_max = B / poly(max-past-size(prec, W))` — numerator L2 (compute/memory budget), denominator L4 (order-determined per-record cost), no third input. Sharp sub-result: the Sorkin order `prec` is **rate-blind** (completeness is a predicate on the order, not a rate cap); a patient completeness-gated observer is correct at any rate below its L2 capacity ceiling. Corrects Run 1's guessed bound ("causal horizon width") to the L2-budget-over-L4-cost ratio. Only route to a non-absorbed `lambda_max`: change L6 from "No loop" to a deadline/cadence loop → handed to FR4. | — | — |
| FR2 | **BvN rate-of-classicality formalization** — if the BvN lane is developed to include a formal lattice-functor obstruction (per rigor-redirect Layer 5 requirements), ask whether the obstruction has a rate-parameterized form. If yes: test whether it coincides with `lambda_max` from the TaF observer model. | Either: confirmed convergence `lambda_max = Gamma_min` (a non-trivial linking of L1 and L2); or: confirmed independence (two distinct concepts). | The BvN / Gamma_min convergence hypothesis remains unconfirmed until the BvN wall is formally constructed. Do not assume convergence. |
| ~~FR2~~ **RESOLVED 2026-06-22** | Steps A–C derivation at `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`. **Verdict: CONVERGENCE RESOLVED AS NON-TRIVIAL PROPORTIONALITY.** (A) Supplied the BvN lane's missing rate-of-classicality concept via a Lindblad/pointer-basis model: `Gamma_min(epsilon) = ln(1/epsilon)/t_obs`. (B) `lambda_max = 1/t_obs` (service-rate, from FR1). (C) Both share the observer finalization latency `t_obs`, giving **`Gamma_min = ln(1/epsilon) · lambda_max`** — coupled, not independent. Clean equality `lambda_max = Gamma_min` holds **iff `epsilon = 1/e`**; otherwise proportional. The coupling is non-trivial: "cannot finalize a record of a state before it decoheres" bounds L2 capacity by L1 coherence dynamics, `lambda_max <= Gamma/ln(1/epsilon)`. Produces a **candidate L1–L2 coupling rule** for the six-axis protocol (classicality certification couples observer rate to substrate decoherence rate). Does NOT prove the BvN wall (Layer 5 obligations stand) and does NOT change any GU theorem (respects rate-independence; `Gamma_min` is a pre-classicality precondition, signed-readout is post-classicality). Highest-yield FR output. | — | — |
| FR3 | **Filtered-sheaf toy worked example** — construct a minimal toy example where a sheaf `F` over a simple record space is assembled in filtration steps `F_tau`, and ask whether any transient apparent obstruction during assembly is structurally distinct from the final obstruction `H^1(X, F)`. | A concrete worked example showing collapse (absorbed) or non-collapse (genuine new object) of the temporal obstruction concept. | Current analysis concludes collapse in all toy cases attempted; a non-collapse example would overturn this and re-open the filtered-sheaf concept as a genuine GU exploration target. |
| ~~FR3~~ **RESOLVED 2026-06-22** | Explicit example at `explorations/time-as-finality-crosswalk/fr3-filtered-sheaf-non-collapse-example-2026-06-22.md`. **Verdict: NON-COLLAPSE CONFIRMED; PRIOR VERDICT OVERTURNED; OBJECT REASSIGNED.** The prior collapse argument had a gap: it tested *spatial* assembly (growing subspaces `A(tau) ⊂ X`), but the candidate definition is a *subsheaf* `F_tau ⊂ F` over a **fixed** `X`. Subsheaf inclusions induce non-injective maps on cohomology. Explicit toy: `X = S^1`, `F_1 = C_{S^1}` (constant sheaf, `H^1(S^1,C) = C ≠ 0`), `F = F_2` flasque (`H^1 = 0`). So `O(1) = C ≠ 0`, `O(2) = 0` — a genuine **transient obstruction present at an intermediate stage, resolved at the final stage**, surviving the physically-correct information-accumulating (increasing-subsheaf) direction. **Sharpening:** the obstruction is **structural** (cohomology of honest subsheaves, NOT determined by `H^1(X,F)` — this corrects the prior document) but it is indexed by a **filtration** (structural), NOT a **rate** (dynamical). So the **rate-independence finding is untouched**, and the object belongs to a filtered refinement of L1/L2, NOT to the L6 rate concept (FR4). Exploration-grade; needs a GU result sensitive to `O(tau)` before active-research status. | — | — |
| FR4 | **L6 issuance-rate parameterization** — if a six-axis candidate specification uses an observer-finality sub-protocol, test whether adding `cadence` as a new field (rate of record finalization) produces a different failure mode than L4 already captures. | A filled six-axis spec row with `cadence` field populated, and a verdict on whether it changes the failure mode. | Without this, the issuance rate's claimed L6 home (coordination loop dynamics) remains unverified. |
| ~~FR4~~ **RESOLVED 2026-06-22** | Filled spec + verdict at `explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`. **Verdict: NEW FIELD CONFIRMED AT L6.** Built example-02-D (example-02 with L6 changed from "No loop" to a deadline-cadence loop, `cadence` field `Delta`). A **deadline-gated** finality relation produces a structurally new failure mode — *premature commitment* (a record finalized on an incomplete past, later contradicted by a late-past event) — that is provably **unreachable under L4's completeness-gating** and occurs at **any** rate when `Delta` < past-completion latency. This confirms Run 5's placement of the issuance-rate family at L6. Does NOT overturn FR1: FR1's absorbed object is `lambda_max` (L2 capacity ceiling), FR4's new object is `Delta` (L6 deadline policy) — different quantities. Respects rate-independence: no GU structural theorem depends on `Delta`. Status: exploration-grade L6 field (1 of 2 worked examples needed for sub-protocol promotion). | — | — |

**Status of the registered negative finding:** The signed-readout monotonicity criterion is confirmed rate-independent (see `explorations/time-as-finality-crosswalk/rate-independence-negative-finding-2026-06-22.md` and the worked check `rate-independence-worked-check-2026-06-22.md`). This is a closed finding; do not re-run the rate-independence test for the signed-readout criterion without first identifying a new contact point not covered by the worked check.

---

## FR-Series Resolution Summary (2026-06-22) — Read This Before Re-Opening FR1–FR4

All four FR tasks are resolved. Synthesis: `explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md`. **Central finding: "the issuance rate" was four formally distinct objects, one per chain layer.** Do not re-investigate the resolved objects; the *residual open targets* are the two structural objects the rate language had entangled, with explicit promotion gates below.

| residual open target | what would earn active-research status (promotion gate) |
|---|---|
| **`Gamma_min` / L1–L2 coupling** (FR2, highest-yield) | (i) Prove the BvN wall to Layer-5 rigor (define the denied functor/adjunction; prove the obstruction without smuggling). (ii) Exhibit a GU result (anomaly input or signed-readout scope) that changes when `Gamma < Gamma_min`. A **candidate L1–L2 coupling rule** is offered for review for `canon/six-axis-specification-protocol.md`'s "Current Coupling Rules" section — review against no-go discipline before any inclusion. |
| **Filtered-sheaf obstruction `O(tau)`** (FR3) | A GU chirality/anomaly readout demonstrably sensitive to the observer's record *filtration* `{F_tau}`, not only to the final record `F`. |
| **Cadence field `Delta`** (FR4) | A *second* worked six-axis example (non-Sorkin L4 or Type II_1 L1) where `Delta` catches a real protocol error, per the sub-protocol promotion condition in `observer-finality-layer.md`. |
| ~~`lambda_max`~~ (FR1) | **Closed — absorbed by L2+L4.** No promotion target; it is a derived quantity. Do not re-investigate. |

**Do NOT** re-run the issuance-rate absorption analysis (FR1), the BvN convergence as a clean identity (FR2 — it is a tolerance-specific proportionality, not an identity), the filtered-sheaf collapse question (FR3 — non-collapse is established), or the L6 cadence placement (FR4 — confirmed) without first identifying a contact point not covered by these four worked checks.

---

## Positive GU Constructions Lane (2026-06-22)

A new exploration lane was opened by `explorations/positive-gu-constructions-lane-proposal-2026-06-22.md`. This lane targets positive derivations and theorem-grade reconstructions of specific GU constructions, complementing the existing diagnostic / no-go-evasion program. All targets are exploration-grade; none are active_research or canon without meeting the promotion criteria.

**Background.** The repo previously had no positive derivation content: no theorem statements, derivation stubs, or consistency lemmas for what GU claims would look like if formalized. This lane opens that work. The Nguyen critique (§3.4) correctly faults GU for missing derivations; this lane begins to supply the specifications GU would need.

**Five targets, ordered by tractability:**

| rank | target | key blocker | first action |
|---:|---|---|---|
| **PC1** | **Spinor group / shiab from Spin(7,7)-invariant data** | Representation theory computation: does a natural Spin(7,7)-equivariant map S → Λ•(R¹⁴) exist over R without complexification? | Decompose S and Λ•(R¹⁴) as Spin(7,7) representations; check for shared real irreducibles. This is the N2 computation in positive form. |
| **PC2** | **Y¹⁴ / Met(X⁴) metric bundle and observation/pullback maps** — derivation stub filed at `explorations/pc2-met-x4-bundle-formalization-stub-2026-06-22.md`. Circularity question resolved: the Frobenius construction is a benign tautology, not a vicious circle. D_ℊ can be defined without section choice, subject to a spin structure condition on Y¹⁴. **First open computation:** compute w_2(Y¹⁴) via Gysin sequence to confirm D_ℊ exists for any spin 4-manifold X⁴. Second: branching rules s*(S) for SM fermion content. Third: second fundamental form F_s. | Canonical Dirac operator on Met(X) independent of a prior metric choice — the falsification test for spinor-metric circularity resolution | w_2(Y¹⁴) computation (algebraic topology, routine for a specialist) |
| **PC3** | **Riemannian-Ehresmannian fusion framing** | SM gauge group emergence from structure group of Met(X) → X has no known mechanism | Annotate no-go map Witten entry with Riemannian/Ehresmannian framing as a sharpening; no new derivation required now |
| **PC4** | **Torsion term replacing cosmological constant Λ** | Blocked by PC2: requires 14D connection to be specified first | Write derivation template (torsion setup, candidate torsion-for-Λ invariants, consistency requirements) as exploration stub |
| **PC5** | **Higgs emergence mechanism** | Most downstream: requires PC2 + PC1 substantially advanced | Note Connes-Chamseddine inner-fluctuation comparison as future spec anchor |

**PC1 is the priority task.** It is the positive-construction analog of the existing N2 Nguyen critique task. They should be worked together. PC1 provides the specification that N2's algebra computation would confirm or falsify.

**Constraint on all PC tasks.** No output from the positive constructions lane should be framed as a Nguyen refutation or as a proof of GU. Framing: "these are the constructions GU would need; we are attempting to specify and test them."

**Cross-impacts identified (see proposal document §5 for detail):**

- The Riemannian-Ehresmannian framing (PC3) sharpens the no-go map's Witten entry: the smoothing functor ϕ_smooth can be more precisely described as the "Riemannian-reduction functor" that projects out all Ehresmannian structure and retains only Levi-Civita data. This is a clarification annotation for `canon/no-go-class-relative-map.md`, not a revision.
- The Met(X) = Y¹⁴ construction (PC2) adds a new entry to the Witten "candidate richer substrate datum" column: non-compact fiber breaks Witten assumption (1) directly. Annotation needed.
- The PC1 spinor computation, if a natural equivariant map exists, would be the first example of a richer-datum-inside-class adjacent to the Distler-Garibaldi stress case. If no natural map exists, this confirms the Distler-Garibaldi pattern. Either outcome sharpens the no-go map.
- Torsion (PC4) has no current interaction with the signed-readout boundary theorem (classical vs. quantum quantity).

---

## UCSD Transcript Analysis — New Tasks (2026-06-22)

These tasks emerged from the formal analysis of the Weinstein UCSD April 2025 talk
(`explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md`). Primary source saved
as `literature/weinstein-ucsd-2025-04-transcript.md`. All tasks are exploration-grade.

| order | task | output | blocker if skipped |
|---:|---|---|---|
| VZ1 | **Velo-Zwanziger no-go map entry** — add Velo-Zwanziger (1969) as a fifth no-go family to `canon/no-go-class-relative-map.md`. GU predicts one family of 16 flipped-chiral spin-3/2 particles; Velo-Zwanziger is the primary constraint on any spin-3/2 matter prediction. Entry template: assumptions (minimal coupling + nontrivial gauge group + flat background), known evasions (supergravity Rarita-Schwinger), GU evasion candidate (trivial internal gauge coupling), status (unconfirmed). | New section in no-go map, Distler-Garibaldi format. | No-go map is incomplete with respect to GU's own spin-3/2 predictions. |
| SC1 | **Shiab domain/codomain specification update for N2** — the UCSD transcript makes explicit that the ship-in-a-bottle (shiab) operator maps Ω²(Y¹⁴) ⊗ S → Ω¹(Y¹⁴) ⊗ S. Update the N2 task description with this domain/codomain, and check Clifford algebra literature (Harvey; Lawson-Michelsohn) for any existing map between these spaces in split-signature (7,7). | Updated N2 description + literature check for that specific map. | N2 is currently underspecified at the domain/codomain level; the transcript is the most precise primary-source statement available. |
| ~~DD1~~ **RESOLVED 2026-06-22** | **Distortion tensor literature check** — `explorations/dd1-distortion-tensor-literature-check-2026-06-22.md`. **Verdict: PARTIALLY_NAMED.** The name "distortion" (Hehl et al. 1995) applies in name and schematic type, and "contorsion" (Agricola-Friedrich 2003) captures the identity-gauge limit on X⁴. GU's θ is NOT the same as either: the defining novelty is gauge-equivariance under the full inhomogeneous gauge group IG = G ⋉ Ω¹(ad P) via the τ⁺ homomorphism — which no prior framework provides. PC4 (generic torsion-for-Λ) and GU's θ-mechanism are formally distinct; they may coincide after the section pullback s*(θ) is computed (the open step). | — |
| HC1 | **Three hidden curvature components: representation theory check** — the transcript claims the Lorentz curvature tensor breaks into 6 pieces (not the standard 3) when "the Lorentz group gets large enough," with 3 visible and 3 hidden by the torsion-free Bianchi identity. Identify the relevant group (conformal SO(2,4)? or the structure group of Y¹⁴?) and the specific irreducible representations of the 3 hidden pieces. | Representation theory statement: which group, which irreducibles, verified or corrected "3 hidden" count. | Without this, the claim "three hidden curvature components" is unverifiable; the correct group needs to be identified before the representation theory can be run. |

**New formal objects identified from the transcript not in PC1–PC5:**

| object | description | six-axis home | first action |
|---|---|---|---|
| Distortion tensor | D(∇, g) = ∇ − g·∇_LC; gauge-equivariant replacement for torsion; "superior equivariance" | L1 substrate | ~~DD1 literature check~~ **RESOLVED** — PARTIALLY_NAMED; see `explorations/dd1-distortion-tensor-literature-check-2026-06-22.md` |
| Three hidden curvature components | 6-piece decomposition of Lorentz curvature; 3 killed by G_μν, 3 hidden by torsion-free Bianchi identity | L1 substrate | HC1 rep-theory check |
| Velo-Zwanziger constraint | Fifth no-go family for spin-3/2 matter; must be added to no-go map | L1 substrate + L3 pairing | VZ1 no-go map entry |
| Dirac-DeRham-Einstein complex | DeRham complex ⊗ spinors rolled into self-coupled operator via shiab (Ω² ⊗ S → Ω¹ ⊗ S); produces 3 generations | L1 substrate, L5 emergence | SC1 (shiab domain/codomain update); then N2 computation |
| Tau+ homomorphism / double coset | IG = G ⋉ Ω¹(ad P); diagonal embedding τ⁺; double coset produces equivariant dark energy tensor | L1 substrate, L3 pairing | Claim 2 derivation (requires gauge theory specialist) |
| SUSY on connections (super-IG) | Super-extension of IG over space of connections, not Poincare over Minkowski; predicts no spacetime SUSY at colliders | L1 substrate | Separate task; no immediate action; requires super-IG algebra construction |
| Einstein anticipates Chern-Simons | Einstein's Ricci contraction is 4D analog of 3D Hodge-star in Chern-Simons; sharpens Riemannian-Ehresmannian framing | L1 substrate | Annotation to no-go map Witten entry (clarification-grade, not revision) |

**Constraint on all UCSD transcript tasks.** No output should be framed as a Nguyen refutation or as a proof of GU. Framing: "these are the constructions GU would need; we are specifying and testing them." Do not use transcript claims as technical evidence without independent formalization.

---

## What To Avoid

- Do not claim this repo proves GU.
- Do not claim computation or observer language evades Witten without a construction.
- Do not treat C_MPR, the 9-tuple, PCP-blindness, or the BvN-style wall as settled.
- Do not use media claims as technical evidence without independent formalization.
- Do not make broad synthesis essays when a small falsifiable test is possible.
- Do not use observer-finality language as a no-go theorem escape hatch; state the record protocol and failure mode.
- Do not frame any positive-constructions-lane output as a Nguyen refutation; these are construction attempts, not counter-proofs.
