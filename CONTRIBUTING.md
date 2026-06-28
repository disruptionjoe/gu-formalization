---
title: "Contributing"
status: canon
doc_type: overview
updated_at: "2026-06-25"
---

# Contributing

Thank you for considering a contribution to the Geometric Unity Formalization Program. This document covers who the repository is for, what kinds of contribution are welcome, how to propose substrate-class specifications, pull-request norms, and the code of conduct.

---

## Who this is for

The work in this repository sits at the intersection of differential geometry, gauge theory, mathematical physics, operator algebras, complexity science, distributed systems theory, and philosophy of physics. The audience the maintainer is hoping to reach includes:

- Pure mathematicians working in operator algebras (especially Connes spectral triples, subfactor theory, MIP* = RE), higher category theory, motivic cohomology, topological modular forms, prismatic cohomology, or other "substrate-class-rich" areas
- Mathematical physicists working on Standard Model derivations, anomaly classification, cobordism / generalized cohomology, twistor theory, Cartan geometry, generalized geometry, or AdS/CFT
- Physicists working on quantum error correction, holographic codes, lattice gauge theory beyond Nielsen-Ninomiya, the Wolfram Physics Project, causal-set theory, or other substrate-candidate programs
- Complexity scientists and theoretical computer scientists working on consensus impossibility theorems (FLP, CAP, BFT), distributed systems lower bounds, computability and decidability, complexity classes, and self-organized criticality
- Philosophers of physics working on observer-substrate questions, computational ontology, modal realism, structural realism, or related frames
- Writers, teachers, and science communicators interested in making the methodology accessible to non-specialists

If you don't fit those boxes but think the work is interesting, you are still welcome. The repository explicitly invites perspectives the maintainer hasn't considered.

The math content is technical. The methodology — Hegelian dialectical synthesis across heterodox lenses — is not. Contributions at either level are valued.

---

## What kinds of contribution are welcome

### GU reconstruction work

The core open question is: **can Geometric Unity be rigorously reconstructed, extended, or
falsified through systematic mathematics?**

The repository uses GU as a generative test case: a bold, contested conjecture that spawns falsifiable
hypotheses. Contributions should help find the truth by constructing, testing, or killing specific
mathematical pieces and keeping whatever survives (often GU-independent), not by advocating for or against
GU.

High-priority contribution types include:

- source-to-shadow reductions for GR, QFT, matter/gauge, measurement, or dark-energy
  sectors;
- branch-fixed action/operator proposals with explicit variation spaces and rollback
  conditions;
- analytic machinery for the noncompact `Y^14` setting;
- category or functor language that makes a GU class exit precise;
- obstruction theorems that show a required GU reconstruction object cannot exist.

### Substrate-level invariant work

One important adjacent question is: **does there exist a substrate-class candidate hosting
a chirality invariant that reduces, under the lossy projection to the smooth bundle, to
Standard Model chirality content while satisfying Freed-Hopkins compatibility?**

The repository identifies four mathematically-adjacent substrate-class candidates:
1. Connes Type II_1 spectral triples with Jones-subfactor extension (witnessed by MIP* = RE non-embeddability)
2. Holographic quantum error-correcting codes with chiral modular tensor category logical algebra
3. Wolfram multiway hypergraph rewriting in a specified rulial reference frame
4. Higher categorical substrates valued in motivic, topological modular forms, or prismatic cohomology

Concrete construction attempts in any of these directions are welcome when they clarify a live hypothesis.
Results that are valuable independent of GU are co-equal products, not secondary; label them GU-independent
so a reader can take them without buying GU.

### Refutations and counterexamples

If you can show one of the substrate-class candidates does not host the required invariant, or that the dialectical analysis at a specific lens is wrong, that is just as valuable as a positive construction. The program is structured so that a clean negative result is a publishable outcome.

If you find a no-go theorem the analysis missed, or a hypothesis decomposition that closes a loophole the analysis identified, please open an issue. Naming a structural obstruction the program does not currently see is high-value work.

### Specification of new substrate-class candidates

The six-axis specification space (substrate × observer × pairing × causal-order × emergence × coordination-loop) contains roughly 16,000 candidate hextuples, of which roughly 20-50 are mathematically tractable today. If you can specify a hextuple the current materials don't name — with explicit citations to the existing literature for each axis — and propose how to construct the substrate-level invariant for it, that is exactly the kind of expansion the program needs.

To propose a new substrate-class specification:
- Open an issue titled `Specification proposal: <short name>`
- Name the hextuple (L1 substrate, L2 observer, L3 pairing, L4 causal-order, L5 emergence, L6 coordination-loop) with at least one published-literature citation per axis
- Name the lossy reduction map you propose connects this substrate class to the smooth-bundle shadow
- Name the Freed-Hopkins compatibility test you propose for the construction
- Name the time horizon and skill set you think a research effort on this specification would need

### Refinements to existing material

- Persona pass corrections: if a pass cites a result inaccurately, or misses a more recent reference, open a pull request with the fix.
- Synthesis refinements: if the meta-syntheses (00 through 00e and the supplementary 06-07) overstate or understate a convergence claim, open an issue and we can discuss whether the synthesis needs a revision pass.
- Deep-research brief updates: if you know of a paper the briefs missed, open an issue. The four briefs survey existing literature; staying current is community work.
- Accessibility edits to the blog post or README: if a sentence is confusing or jargon-heavy, open a pull request with a cleaner version.

### Methodology contributions

The 15-lens dialectical method itself is a transferable artifact. If you apply it to an adjacent open problem in physics, mathematics, or complexity science and want to share what worked and what didn't, please open an issue or write a guest post for the repository.

### Documentation and infrastructure

The repository is intentionally lightweight. If you think a piece of infrastructure (GitHub Discussions, a Zulip workspace, a static documentation site) would help collaboration, open an issue and propose it.

---

## How to submit a pull request

1. Fork the repository.
2. Create a branch named descriptively (e.g. `pr/freed-hopkins-pairing-counterexample` or `pr/connes-subfactor-construction-attempt`).
3. Make your changes. If you are adding a new persona pass, follow the structural template visible in the existing passes (sections a through e, optional appendix). If you are adding a new deep-research brief, follow the structure of the existing four. If you are adding a new substrate-class specification, follow the hextuple specification template above.
4. If the change involves a math claim, follow the repository's three-tier tagging discipline:
   - `[verified]` — defensible against a knowledgeable reader with named established result references
   - `[reconstruction]` — inferred from existing material with the source named
   - `[speculation]` — extrapolation beyond available sources, with explicit naming of what would need to be true for the speculation to hold
   If the change promotes, downgrades, or re-scopes a claim, also run
   `process/runbooks/claim-status-consistency-quality-workflow.md` before opening the PR.
5. Open a pull request. The maintainer (initial review by the repository maintainer; broader review by contributors as the community grows) will engage with the substantive content. Please respond to review comments; the goal is to develop the strongest version of the contribution.
6. Once accepted, the contribution lands with attribution. If you'd prefer pseudonymous or anonymous contribution, name that preference in the pull request.

### Style notes

- Markdown source. Plain text wins over heavy formatting.
- Math: LaTeX inline (`$E = mc^2$`) or block (`$$ ... $$`) is fine, though many readers will read the rendered Markdown on GitHub which has limited LaTeX support. If a derivation is heavy, include a PDF in the same directory.
- Citations: full reference at the end of the document, inline `[Author Year]` style. arXiv links preferred.
- Length: pieces can be as long as they need to be, but a clear thesis-statement summary in the first 200 words is appreciated.

---

## Issues

Open an issue for any of:
- A question about the methodology or material
- A proposed substrate-class specification (see above)
- A refutation, counterexample, or missed reference
- A request to clarify a section
- A pointer to adjacent published work
- A request to add a new lens family
- An infrastructure proposal

Please tag the issue with one of `question`, `specification-proposal`, `refutation`, `clarification`, `reference-pointer`, `lens-proposal`, `infrastructure` to help maintainers route it.

---

## Code of conduct

This repository follows the spirit of the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). The short version:

- Be respectful of contributors regardless of background, level of expertise, or distance from the mainstream of physics or mathematics. Heterodox contributions are explicitly welcome.
- Disagree with the work, not with the person. The maintainer expects strong technical pushback and welcomes it. The bar is mathematical and structural argument, not credentialism or social pressure.
- No harassment, ad hominem, or bad-faith engagement.
- If you observe behavior that violates these norms, contact the maintainer privately.

The maintainer reserves the right to close issues, lock threads, or block contributors whose engagement is in bad faith or violates these norms. Mathematical or structural disagreement, no matter how forceful, is not bad faith.

---

## Maintainer expectations

The repository is maintained by Joe Hernandez (initial maintainer; the maintainer set is expected to grow as the program develops). Maintainer commitments:

- Issues and pull requests will receive an initial response within two weeks
- Substantive technical engagement on substrate-class specifications and refutations
- No silent merges of substrate-level math work without at least one external reviewer
- Public acknowledgment of contributors in the final paper if the work proceeds to publication
- Honest closure of the program with a structural-diagnosis verdict if the substrate-level invariant question proves intractable across the specification space

If maintainer responsiveness slips, open an issue tagging the maintainer or contact the maintainer directly.

---

## Licensing

This repository is dual-licensed: **CC-BY-4.0** for documentation, papers, syntheses, persona passes, deep-research briefs, and all prose (see `LICENSE-DOCS.md`); **MIT** for any code, scripts, or computational artifacts (see `LICENSE-CODE.md`).

We welcome forks, derivative research programs, formalizations, critiques, educational uses, and commercial applications. If this work contributes meaningfully to your own, please cite the repository, link to relevant artifacts, and consider sharing findings back with the broader research community.

By contributing, you agree your contribution will be released under the corresponding license (CC-BY-4.0 for prose contributions, MIT for code contributions).
