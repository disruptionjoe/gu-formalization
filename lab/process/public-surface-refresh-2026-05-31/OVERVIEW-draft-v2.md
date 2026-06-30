---
title: "Start Here: The Five-Minute Research Map"
status: process
doc_type: synthesis
updated_at: "2026-05-31"
---

# Start Here: The Five-Minute Research Map

This repository is a first-principles research map, not a proof of Geometric Unity.

It asks whether Geometric Unity-class higher-dimensional programs fail only inside the usual smooth-bundle reduction class, or whether there is a substrate-level invariant whose smooth shadow is exactly what the no-go theorems see as null.

## 1. What is the central claim?

The working hypothesis is:

> The four no-go theorem families are class-relative impossibility results. They may compute forgetful images of richer substrate-level invariants in the smooth bundle shadow, rather than ruling out every possible substrate-level route to Standard Model chirality.

The strongest version of the claim is not established in the literature. The deep-research briefs found the substrate-replacement reading to be *implicit or adjacent in the published literature* for three of the four canonical no-go theorems (Witten 1981, Nielsen-Ninomiya, Freed-Hopkins), and *original-and-contested* for the fourth (Distler-Garibaldi). Distler-Garibaldi is treated as the hardest line: every published evasion of it changes the category (product group, GraviGUT SO(3,11), K(E10) Kac-Moody quotient, etc.) rather than relaxing assumptions inside the single-real-E_8 frame, and the public framing of this repo names that category-change tax explicitly. Any E_8 invocation here must name the (G, real form, V_{m,n}) triple Distler-Garibaldi rules out, or it does not engage the theorem.

Sector qualification matters. When this repo says "Geometric Unity evades Witten by substrate replacement," it specifically means **GU's Sector I** — Weinstein's own "spacetime is replaced and recovered by the observerse contemplating itself" subdivision (Oxford 2013) — not GU as a whole. Sector I is the part of Geometric Unity the substrate-level invariant reading actually engages; other sectors carry their own structural moves and are not in scope for these evasion claims.

## 2. What would falsify it?

Any of these would be a clean negative result:

- Prove that every mathematically tractable substrate specification reduces to one of the existing no-go theorem classes.
- Show that the Connes Type II_1 / non-embeddable internal algebra bridge cannot satisfy the spectral Standard Model control requirements.
- Show that observer-pairing data cannot change anomaly classification because the relevant enriched bordism categories collapse back to ordinary Freed-Hopkins input data.
- Show that the distributed-systems analogy cannot be formalized even for the most operational pilot case, Nielsen-Ninomiya.

A clean negative result is a success condition for this repo.

## 3. What is the current evidence?

The evidence is currently structural, not constructive:

- `lab/process/persona-passes/` contains 35 persona passes across mathematical physics, computation-substrate, heterodox problem-shape, and distributed-systems lenses.
- `syntheses/` contains five core syntheses, three ranking/priority syntheses, and the first public pathway scoping artifacts. The strongest synthesis is the six-axis specification space: substrate, observer, pairing, causal order, emergence class, and coordination loop.
- `lab/literature/` contains four literature reviews. Their shared result is that the highest-priority bridges are genuinely unexplored in the published/arXiv literature, with adjacent machinery but no positive construction and no known counter-result.
- `lab/sources/` contains the GU media/source provenance index, including lectures, podcasts, official pages, and candidate videos that need transcript/timestamp extraction before they support specific claims.
- `lab/archive/` contains the originating execution log and four frontier packets showing why the work pivoted away from GU-source reconstruction and toward first-principles substrate tests.

### 3a. Two structural findings carried by bridge work (in-progress, incoming syntheses)

Two structural results from the in-progress Nielsen-Ninomiya/CALM bridge work are load-bearing for the repo's public framing and will be added to `syntheses/` as the formal write-ups land:

- **Layered-factorization architecture (C_MPR)** `[speculation, candidate categorical statement]`. The natural categorical bridge from classical local-rule / distributed-coordination systems to the lattice-chiral-anomaly side is not a direct equivalence; it is a layered factorization `C_GW_loc → C_MPR → C_Shadow`, where `C_MPR` is the category of **monotone provenance with possibly-signed readout** (objects `(E, ≤_E, Cert, G, ≤_G, r, P_O)` separating monotone evidence accumulation `E` from non-monotone readout `r : E → G`). CALM appears as the *monotone-readout sub-category* of `C_MPR`; proof-carrying-provenance constructions appear as a fully-certified sub-structure. This is the corrected categorical object the in-progress synthesis carries; the stronger adjunction-style claims (reflectivity, free adjoint, fibration structure) remain open. Earlier "CALM = GW characterizes the same class of observables" framing is superseded by this factorization reading.

- **Classical-value-lattice wall theorem** `[speculation, candidate negative theorem]`. The reason the direct categorical equivalence fails is structural: there is no 1-categorical adjunction `L : C_ClassicalDistribLR ⇄ C_GW : R` that lifts the load-bearing physics content (non-trivial Dirac operator, non-trivial Ginsparg-Wilson relation, non-trivial chiral anomaly index) for *any* classical-distributive value lattice on the source side (CALM, signed Z, generic CRDT lattices, Class-1-4 Wolfram CA, even universal CA like Rule 110). The principal obstruction is the value-lattice-distributivity vs. projection-lattice-orthomodularity split (Birkhoff-von Neumann 1936, generalized to all classical value lattices). CALM is one special case of the wall; the wall is more general. The only escape known is to leave the classical-distributive frame entirely (quantum cellular automata / `C_QLR`-style sources, flagged as a separate follow-on lane).

These two findings sit together: the wall theorem says the direct categorical equivalence is obstructed for a precise structural reason, and the C_MPR factorization is the corrected architecture that survives the obstruction. The synthesis number for the formal write-up will land in `syntheses/` when WRK-386 paper drafting finalizes the public-grade statements.

## 4. What are the highest-leverage open questions?

1. Can the finite Connes-Chamseddine spectral Standard Model be used as a control case for a Type II_1 or non-embeddable internal algebra extension?
2. Can one write a no-go assumption/evasion matrix precise enough to separate real class exits from rhetorical loopholes? (Distler-Garibaldi is the stress case where the unified frame works least well — see §1.)
3. Can Nielsen-Ninomiya be recast as a protocol/model impossibility theorem in a way that makes the distributed-systems analogy testable? (The C_MPR factorization architecture in §3a is the current best categorical statement of this bridge.)
4. Can observer/reference-frame data be added to anomaly classification without overclaiming that Freed-Hopkins is already observer-relative?
5. Which specific six-axis candidate is the first one worth attempting?
6. Does the classical-value-lattice wall (§3a) apply at the adjunction level to Witten and Freed-Hopkins as well, or is it specific to the Nielsen-Ninomiya / Ginsparg-Wilson row?

The current priority ranking is in `lab/roadmap/five-persona-value-ranking-rubric.md` and `lab/roadmap/15-persona-pathway-ranking.md`. The first public pathway artifacts begin at `canon/six-axis-specification-protocol.md`.

## 5. Where can I contribute?

- If you know noncommutative geometry, operator algebras, subfactors, or spectral triples: start with `lab/literature/01-non-embeddable-type-ii-1-spectral-standard-model.md` and the Connes/Type II questions in `lab/roadmap/potential-insights-novelty-and-tests-v1.md`.
- If you know anomalies, cobordism, QFT, or quantum reference frames: start with `lab/literature/02-observer-dependence-freed-hopkins-anomaly-classification.md`.
- If you know lattice fermions, no-go theorem workarounds, or string compactification: start with `lab/literature/03-assumption-decomposition-no-go-evasion-literature.md`.
- If you know distributed systems, consensus, CAP/FLP/BFT, causal DAGs, or complexity science: start with `lab/literature/04-spectral-triples-anomaly-chirality-distributed-systems-analogies.md`. The C_MPR factorization architecture (§3a) is the current categorical statement of what the distributed-systems-to-lattice-anomaly bridge actually delivers; contributions sharpening either the wall theorem or the open C_MPR adjunction-style claims are especially welcome.
- If you know category theory, lattice theory, or quantum logic: the Birkhoff-von Neumann generalization framing of the classical-value-lattice wall (§3a) is a natural entry point — does the wall extend cleanly to the Witten and Freed-Hopkins forgetful operations, or does it stop at Nielsen-Ninomiya?
- If you want an issue-sized task: start with `NEXT-STEPS.md`.
- If you want to propose a new candidate path: start with `lab/specifications/six-axis/six-axis-template.md`.
- If you want the shortest non-specialist read: start with `papers/blog-post-draft-v2.md`, then `papers/formal-paper-draft-v2.md`, then `CONTRIBUTING.md`.
