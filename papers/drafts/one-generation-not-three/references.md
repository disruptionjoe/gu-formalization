---
title: "One Generation, Not Three — in-repo evidence map"
status: draft
doc_type: evidence-map
paper_slug: one-generation-not-three
created: 2026-08-03
updated: 2026-08-03
purpose: "Artifact-by-artifact receipts for every computational and source-critical claim in draft.md. This file is part of the PRE-DEPOSIT package; paths are repo-relative. Nothing here moves any claim status."
---

# In-repo evidence map for `draft.md`

Each row: the paper section, the claim, the owning artifact(s), and the grade at which the claim is
carried. Grades follow program convention (EXACT / GREEN ASSERT / DETERMINISTIC FINITE COMPUTATION /
SOURCE-CRITICAL / TYPING DECISION / REFEREE_CONJECTURE / CANDIDATE). Hostile-review corrections are
binding on the artifacts they correct; where a row cites a corrected artifact, the correction banner
governs.

| Paper § | Claim | Artifact(s) | Grade / note |
|---|---|---|---|
| §2.1 | Cl(9,5) ≅ M(64,ℍ) reconstruction; anchors ‖[Π_RS, M_D]‖ = 58.7215, C2 = 155.3625 | `tests/oq_rk1_cl95_explicit_rep.py`; survey generation-sector interface section | Reconstruction-grade; rep-canonicity is the named referee risk |
| §2.2 | dim ker Γ = 1664 = 13·128, signature-independent | firewall canon (:227 row); `explorations/imposter-reading-adjudication-2026-08-03.md` §2 (reading-independent list) | EXACT |
| §2.3 | Carrier-split fork, three options incl. author-declared TX^{1,3} ⊕ N^{6,4} ⊂ Y^{7,7} | `GEOMETER-VS-PHYSICS-OBJECTS.md:24`; `lab/process/CURRENT-RESEARCH-CONTEXT.md` (live forks) | Fork row; unadjudicated |
| §2.3 | Π_RS^phys does not exist (kinematic ≠ physical carrier) | OQ-RK1 BLOCKED_NEEDS_SPEC (register); `lab/process/CURRENT-RESEARCH-CONTEXT.md` | Standing fence |
| §3.1 | Product rule; 1664 = 384 + 1152 + 128; even/even splits; planted wrong-subtraction kill control | `explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md` (computation section); probe `tests/channel-swings/external_datum_ledger_probe.py`; `tests/escape-corners/legb2_shadow_restriction.py:181-190` (checks 3.1, 3.2) | EXACT dimension count + operator verification; NOT a rep-theoretic proof (grade line of the ledger artifact) |
| §3.2 | Traceful control: two-term Leibniz, no third term | same ledger artifact ("the isolating control") | EXACT |
| §3.3 | Odd/odd scope exception (3+11, 9+5 as splits); split-vs-signature homonym fence | same ledger artifact ("scope condition found by a control"); `lab/process/CURRENT-RESEARCH-CONTEXT.md` (pack fix 68a3013) | EXACT; fence mandatory |
| §3.4 | Arity law b(k−1); blocks 2k−1; 10 = 6+4 gives "3+2"; walls compose not pair (Brauer-Wall) | `lab/process/hinge-panel-synthesis-2026-08-03.md` §2 (L9 master law), §3 (pairwise kill, L7/L8/L9) | Internal analytic (panel L9) |
| §3.5 | Coboundary theorem: defect = δR, exact, class zero | `lab/process/hinge-panel-synthesis-2026-08-03.md` §3 (L9) | Internal analytic; count kill #2 |
| §4.1–4.2 | Γ∘ι_B = 4·I, Γ∘ι_F = 10·I; imposter = ker Γ ∩ span{ι_B, ι_F} = im(10·ι_B − 4·ι_F); allocation-invariant, both signatures, five allocations each | `lab/process/hinge-panel-synthesis-2026-08-03.md` §2; confirmed exactly in `tests/generation-sector/q2_imposter_chirality_grading.py` (result §2.1 item 3 of the Q2 artifact) | EXACT, machine-verified, fork-independent |
| §4.3 | Mutual orthogonality of the three blocks; ι_B = Γ_B†; tight frame X†X = 560·I | `explorations/chirality-grading-and-77-rerun-2026-08-03.md` §2.1 (CHEAP_NEW_COMPUTATION items 1) | EXACT (machine zero, all ten runs) |
| §5.1 | Separator/cut-vertex theorem on the frozen B5 matrix | `lab/process/hinge-panel-synthesis-2026-08-03.md` §2 (L2); B5 matrix: `explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md` | EXACT on the frozen matrix |
| §5.2 | Krein neutrality (192,192)+(576,576)+(64,64) = (832,832); imposter uniquely β-type | `lab/process/hinge-panel-synthesis-2026-08-03.md` §2 (L5) | EXACT; non-transportable (seat4 §3(h) fence) |
| §6 | 10⊗16 = 144 ⊕ 16 (green assert); imposter's 16 = gamma-trace of the 144's module; stranded spin-3/2 16s, two routes; empty (3,2)×144 cells | `lab/process/hinge-panel-synthesis-2026-08-03.md` §2 (L2) | GREEN ASSERT + two independent routes |
| §7.1 | Split canonical to the tautological section; N ≅ Sym²T*X, dim 10; ledger under-claimed | `lab/process/hinge-panel-synthesis-2026-08-03.md` §4 (L3 K6) | Panel-settled; scope stated in the paper |
| §7.2 | (3,9,1) = {3⁰,3¹,3²}; unique even/even split of 14; unique ambient n ∈ {10..20}; HARD FENCE multiplicity ≠ index | `lab/process/hinge-panel-synthesis-2026-08-03.md` §4 (L4 F5 / L6 F3) | EXACT finite check; fence verbatim from panel §10 |
| §8.1 | Cut-invariance (128 = dim S(14) for every even/even 2-split); "meet" everywhere-hence-nowhere; II = 0 on tautological section | `lab/process/hinge-panel-synthesis-2026-08-03.md` §3 (L7/L8, L7 K5, L3) | Kill: locus |
| §8.3 | Callan-Harvey co-variation failure | `lab/process/hinge-panel-synthesis-2026-08-03.md` §3 (L4) | Kill: inflow-interface |
| §8.4 (1) | Rung-1 multiplicity/index fence; the retracted P3-withdrawal and its correction; ledger back to three pieces | `explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md` (CORRECTION and WAVE 1A banners, frontmatter_correction CG-04); `explorations/layer0-pass-on-the-2plus1-count-claim-2026-07-29.md` | Correction banners BINDING on this paper |
| §8.4 (3) | Euler-degree kill (N = 10 > dim X = 4), :24-fork-conditional | `lab/process/hinge-panel-synthesis-2026-08-03.md` §3 (L9) | Fork-conditional flag carried |
| §8.4 (4) | legb2 cross-term index classes (0,0,0) all internal F; 19-day propagation gap | `tests/escape-corners/legb2_shadow_restriction.py`; `lab/process/hinge-panel-synthesis-2026-08-03.md` §2 (L3) | Computed; the propagation failure is documented in the panel |
| §8.4 (5), §9 | PH-K1-KINEMATIC CONFIRMED; 64+64 both signatures all allocations; blocks 192+192/576+576/64+64; joint grading 32/32/32/32; ω₄ does not preserve the block; PH-K1-PHYSICAL OPEN/BLOCKED; no V−A or anomaly claim | `explorations/chirality-grading-and-77-rerun-2026-08-03.md` (preregistered; 318 checks; hostile-review banner controls) | DETERMINISTIC FINITE COMPUTATION; hostile-reviewed; the banner's scoping is reproduced verbatim in the paper |
| §8.5 | Scale bifurcation (~TeV vs 10¹⁴ GeV, 11 decades) | `lab/process/hinge-panel-synthesis-2026-08-03.md` §3 (L6 B3) | Kill: single-scale readings |
| §8.6 | Boyle-Turok count-forcing foil, outside the delimited class; EK1 does not fire | `papers/drafts/no-go-class-relative-survey.md` (Addendum); `explorations/boyle-turok-foil-class-relative-typing-2026-08-03.md`; `lab/sources/claim-mining-boyle-turok-cpt-2026-08-03.md` | Class-relative typing |
| §10.1 | Draft §12.10 / eq (12.22) labels ONLY the third term "Imposter Third Generation"; three blocks = one generation + two non-generation sectors | `lab/process/hinge-panel-synthesis-2026-08-03.md` §1 (L1) | SOURCE-CRITICAL; primary-source ingestion of §11–§12.10 is a queued register item |
| §10.2 | Two-decomposition homonym; strong hinge reading textually falsified; the "2" = ν and gamma-trace part of ζ, by form degree | `lab/process/hinge-panel-synthesis-2026-08-03.md` §1 (L1) | SOURCE-CRITICAL |
| §10.3 | F/Q/Z decode (Q = 6⊗16 (192), Z = 2⊗144 (576), F = 2⊗16 (64)); reunify = Spin(7,7) 832; graded factor-2 untyped (gate) | `lab/process/hinge-panel-synthesis-2026-08-03.md` §1; `explorations/imposter-reading-adjudication-2026-08-03.md` §1 (Reading A, gate note) and §4 criterion 1 | SOURCE-CRITICAL; factor-2 typing OPEN |
| §10.4 | Statement census 2009–2026: "3+1" (2009), "2×32 non-chiral" (2020), super-IG supercharges (ToE :446); Jaimungal inversion + live correction; one-talk duplication; dropped symmetry-breaking-chain sentence; two unrouted transcripts | `lab/process/hinge-panel-synthesis-2026-08-03.md` §1 (L1 census) | SOURCE-CRITICAL; census filed in the L1 report |
| §11 | A/B fork typed; objects provably distinct (128 vs 384, spin-1/2 vs spin-3/2); dependency table (12 rows); decision criteria; J5-gated resolution | `explorations/imposter-reading-adjudication-2026-08-03.md` (entire) | TYPING DECISION; OPEN; the paper is row 11 of its dependency table |
| §12 | Witten 1983 RS/KK-gravitino class burden; two-horn payment; (3,2,16±) = M-H1 identification; symmetric-chirality data (96 each; W221 B9) | `papers/drafts/no-go-class-relative-survey.md` §2.6; register M-H1; `tests/W221_falsify_generation_count_structure.py` (check B9); `tests/oq_rk1_j_restriction_probe.py` | PRIOR-ART GATE (citation-and-burden, not a verdict); gate PAID 2026-08-03 (Wave A-3 item Q7) |
| §13 | Novelty posture; KK-gravitino branching prior-art shadow | seed gate (panel L8-F5/O4) as discharged by survey §2.6; `papers/drafts/prior-art-and-novelty-assessment.md` (program-wide method) | Honesty regrade per the seed's own instruction |
| §14.2 | Not-a-Leibniz-partner ⇒ different high-energy behavior | `explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md` ("that is a discriminator, not a free pass") | CANDIDATE |
| §14.3 | 144 exotic charges ±4/3, ±5/3, ±2; charge-5/3 searches; 16×144 mediator queued; II-mediation conjecture + Q3 first-order leakage kill of the sole-leading route | seed prediction-candidates; `lab/process/hinge-panel-synthesis-2026-08-03.md` §6 (L2-O4, II-mediation); `lab/process/CURRENT-RESEARCH-CONTEXT.md` anchor #2 (Q3 EXECUTED, Resolver Wave B) | CANDIDATE; conjecture carries its kill on record |
| §14.4 | Third-family-philic, no light-family counterpart; R(D)/R(D*) retrodiction posture | `lab/process/hinge-panel-synthesis-2026-08-03.md` §8 (L6) | CANDIDATE / posture |
| §14.5 | JUNO+NOvA+T2K 2026–28 as nearest hard clock (bites banked seesaw K3) | `lab/process/hinge-panel-synthesis-2026-08-03.md` §8 | Adjacent clock, not a test of this mechanism |
| §15.1 (1) | Pati-Salam chain: one 16 = one SM family (normalization, not a count) | `lab/active-research/pati-salam-chain-verification.md`; survey §7 | Verified group theory; normalization only |
| §15.1 (6) | External ledger P1/P2/P3 unreduced; Wave 1A current state | `explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md` (WAVE 1A banner); `explorations/cycle-gates-and-audits/post-batch2-wave1a-supersession-dependency-map-2026-08-03.md` | Banner BINDING |
| §15.3 | Internal verification tier; two filed hostile reviews binding | `lab/process/hostile-reviews/` | Program governance |

## Provenance notes

1. **Seed and gating.** This draft implements the drafting-factory seed "two-plus-one-mechanism"
   (2026-08-03, Joe-approved). The seed's mandatory pre-draft gate — the KK-gravitino prior-art check —
   was paid before drafting via the survey's §2.6 (Wave A-3, item Q7); §13 of the paper carries the
   honesty regrade the seed prescribed for that outcome.
2. **Correction banners honored.** The 2026-07-29 ledger artifact is cited only through its correction
   banners: the P3-withdrawal is treated as retracted, the ledger as three-piece, and the multiplicity/
   index homonym as the governing fence. No sentence of the paper depends on the retracted outcome label.
3. **Do-not-touch hygiene.** `tests/escape-corners/legb2_shadow_restriction.py` and the ledger artifact
   carry deferred-banner status per the adjudication row §5 (campaign do-not-touch list); this paper cites
   them without editing them.
4. **A/B fork.** Per the adjudication row's dependency table (row 11), this paper is a dependent of the
   fork and must be revised when (and only when) a resolution passes J5 hostile review. Until then §11
   states the fork as OPEN and §§4–7/9 are explicitly in Reading A's voice with the §11 disclaimer.
5. **No claim movement.** This package is PRE-DEPOSIT; claim_status_change: none; no canon, verdict, bar,
   count, H59, or LANE-STATE movement is proposed by either file.
