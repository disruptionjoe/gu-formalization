---
title: "Next Steps for Contributors"
status: process
doc_type: synthesis
updated_at: "2026-05-31"
---

# Next Steps for Contributors

This repo should not ask first-time contributors to "solve Geometric Unity." The fastest path is to turn the strongest insights into small, falsifiable work units with clear acceptance criteria.

## Quickest Low-Hanging Fruit

| order | task | why it is fast | output | good for |
| ---: | --- | --- | --- | --- |
| 1 | Build the no-go assumption/evasion matrix | The four target theorem families and their known exits are already named in `lab/literature/03-*` and `syntheses/06-*`. | A table mapping hypotheses, known evasions, and what each evasion adds. Distler-Garibaldi rows must name the (G, real form, V_{m,n}) triple each evasion changes. | Mathematicians, physicists, careful generalists |
| 2 | Claim-mine the GU media index | The media list now exists; contributors can add timestamps without taking a position on the math. | Timestamp rows in `lab/sources/claim-ledger.md`. Sector enumeration (I, II, III, ...) is a useful sub-target — the Sector I substrate-replacement framing is sourced (Oxford 2013); later sectors remain to be characterized from the media trail. | New contributors, science communicators |
| 3 | Make the Connes finite spectral triple a control checklist | The Type II_1 path is only meaningful if it preserves what the finite control case does. | A checklist of what a Type II_1 extension must reproduce. | NCG/operator algebra contributors |
| 4 | Fill the six-axis specification template for one candidate | This turns broad speculation into a typed research object. | One complete substrate/observer/pairing/causal/emergence/loop spec. | Anyone proposing a new path |
| 5 | Run the Nielsen-Ninomiya protocol analogy pilot | It is the cleanest distributed-systems bridge because the assumptions are already operational. | A theorem-assumption to protocol-assumption map. The current best categorical statement of this bridge is the C_MPR layered factorization (see Highest-Upside table below); contributions sharpening or stress-testing it are welcome. | Distributed-systems and TCS contributors |

Most of these first artifacts now have draft public surfaces:

- Six-axis protocol: `canon/six-axis-specification-protocol.md` and `lab/specifications/six-axis/`
- No-go matrix: `canon/no-go-class-relative-map.md`
- Type II_1 checklist: `canon/type-ii1-spectral-sm-checklist.md` and `lab/specifications/type-ii1-spectral-sm/`
- Nielsen protocol pilot: `lab/active-research/calm-gw-boundary/nielsen-protocol-analogy-pilot.md`

## Highest-Upside Research Paths

These are the paths most likely to yield novel or profound insight, ranked by the five-persona rubric in `lab/roadmap/five-persona-value-ranking-rubric.md`.

| path | novelty | profundity | first public task | why it matters |
| --- | ---: | ---: | --- | --- |
| No-goes as class-relative theorems | 3 | 4 | Assumption/evasion matrix | It is defensible even if every speculative path fails. The Distler-Garibaldi row is the stress case — every evasion in the published literature changes the category. |
| Type II_1 / non-embeddable spectral Standard Model | 5 | 5 | Finite-control checklist plus Type II_1 requirements | Strongest math-adjacent open direction with real operator-algebra machinery nearby. |
| Six-axis specification protocol | 4 | 5 | Candidate template plus 5 examples | Keeps heterodox work from dissolving into vibes. |
| Nielsen-Ninomiya as distributed-systems impossibility | 5 | 4 | Protocol-analogy pilot plus C_MPR factorization sharpening | Best "out of the gradient" bridge because it is novel but operational. The C_MPR layered-factorization architecture is the current categorical object; CALM appears as the monotone-readout sub-category. |
| Observer-pairing anomaly enrichment | 5 | 5 | Toy enriched-bordism scoping note | Profound if it works, but it needs careful scoping before public claims. |
| Forgetful-image substrate invariant thesis | 4 | 5 | Define data/forgetful map for each no-go | The deepest synthesis; should trail the assumption matrix rather than lead alone. |

## C_MPR / Factorization Architecture — Follow-On Candidates

The in-progress bridge work has surfaced a categorical architecture, the layered factorization `C_GW_loc → C_MPR → C_Shadow` with `C_MPR` the category of monotone provenance with possibly-signed readout (see `docs/OVERVIEW.md` §3a). It carries one negative theorem (the classical-value-lattice wall, generalizing Birkhoff-von Neumann 1936) and a positive corrected architecture. The following follow-on candidates emerge from that work; they are not yet drafted but are tracked as live research lanes `[speculation]`:

- **Quantum-CA escape (C_QLR).** The only known escape from the classical-value-lattice wall is to leave the classical-distributive frame entirely. A quantum-cellular-automata source category `C_QLR` (Heunen-Reyes-style) plausibly admits a non-trivial adjunction with `C_GW`, but this is unverified in detail. Good first task: literature pass on quantum-CA-to-spectral-triples categorification.
- **Reflectivity / free adjoint.** Is `C_CALM` reflective in `C_MPR`? Is there a left adjoint freely approximating non-monotone readouts as monotone provenance? Both are open follow-up theorem lanes.
- **Fibration structure.** Is `C_MPR` best modeled as a fibration over provenance states with readout fibers?
- **Wall theorem extension.** Does the value-lattice-distributivity wall extend at the adjunction level to the Witten and Freed-Hopkins forgetful operations, or is it specific to the Ginsparg-Wilson row? Either result is publishable.
- **Computational-irreducibility meta-obstruction.** Discussion-only at present; flagged here as a thinking lane, not a load-bearing claim.

## Recommended Sprint Sequence

### 0 to 2 hours: public scaffolding

- Keep `NEXT-STEPS.md` as the public routing page.
- Use issue templates for open problems, media claim-mining, and reference pointers.
- Use labels like `good first issue`, `claim-mining`, `open-problem`, `math-check`, `specification`, `distributed-systems`, `operator-algebras`, and `c-mpr-architecture` (for the factorization follow-on lanes above).

### 2 to 8 hours: first agent-doable artifacts

1. No-go assumption/evasion matrix — with Distler-Garibaldi rows carrying the (G, real form, V_{m,n}) triple discipline.
2. `lab/sources/claim-ledger.md` seeded with 5 to 10 timestamped GU claims from transcript-available sources, with explicit sector tagging when the source supports it.
3. Finite Connes control checklist for the Type II_1 path.

The initial media v1 bundle is in `lab/sources/claim-ledger-v1-draft.md`, `lab/sources/media-claim-mining-report-v1.md`, and `lab/sources/media-claim-and-insight-mining-v1.md`. Treat it as provenance scaffolding until the transcript-rich v2 batch lands.

### First week: public collaborator hooks

1. Publish 3 to 5 GitHub issues from the roadmap.
2. Prioritize one issue per audience:
   - operator algebra / NCG
   - anomaly / topology
   - distributed systems / TCS (consider an issue specifically on the C_MPR open lanes above)
   - source/media claim-mining (sector enumeration is a natural sub-task)
   - accessibility / exposition
3. Ask contributors for falsification paths, not agreement.

### First month: serious research fork

Pick one of:

- Type II_1 spectral Standard Model control extension.
- Nielsen-Ninomiya protocol analogy pilot, extended toward the C_MPR factorization architecture.
- Observer-pairing Freed-Hopkins toy category.

The fastest likely path to a profound result is **Type II_1 control checklist -> no-go matrix -> Nielsen protocol pilot (with C_MPR factorization sharpening)**. That order gives the repo a rigorous base, a high-novelty math path, and a heterodox bridge without making the public posture sound like a proof claim.

## What To Avoid

- Do not lead with "GU is true."
- Do not claim Freed-Hopkins is observer-relative; frame it as an extension proposal.
- Do not claim computation evades Witten without a construction.
- Do not write "GU evades Witten" unqualified; the substrate-replacement reading is **Sector I-specific** (Weinstein's own subdivision — "spacetime is replaced and recovered by the observerse contemplating itself," Oxford 2013).
- Do not invoke E_8 evasions of Distler-Garibaldi without naming the (G, real form, V_{m,n}) triple the evasion changes; every published evasion lives in a *different* category (product group, GraviGUT SO(3,11), K(E10) Kac-Moody, twistor, etc.), and conflating them is the most common framing error.
- Do not describe the CALM / Ginsparg-Wilson bridge as a direct equivalence or as "characterizing the same class of observables"; use the C_MPR layered-factorization language (`docs/OVERVIEW.md` §3a). CALM is the monotone-readout sub-category, not an equivalent characterization.
- Do not attempt a full sextuple sweep.
- Do not add more GU-source archaeology unless it changes a specific claim or timestamp.
