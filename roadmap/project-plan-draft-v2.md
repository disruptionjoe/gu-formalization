---
title: "Geometric Unity Formalization Program — Formal Project Plan"
status: active_research
doc_type: roadmap
updated_at: "2026-05-31"
---

# Geometric Unity Formalization Program — Formal Project Plan

**Draft v2 - 2026-05-30**

> Status: working project plan for the initial public repository. Phase 1 deep research is complete; the next substantive work is specification selection and first-test design.

---

## 1. Program objective

Resolve the open question of whether Geometric Unity-class higher-dimensional bundle programs can derive Standard Model chiral fermion content plus gravity. The resolution will take one of three forms: (a) a positive substrate-level invariant construction with confirmed Standard Model chirality reduction and Freed-Hopkins compatibility, (b) a negative result demonstrating the substrate-level invariant approach is exhausted across the identified specification space, or (c) a precise structural-diagnosis closure naming why the program cannot terminate (Rice-undecidability, ZFC-independence, or observer-class-relativity).

## 2. Background

The standard objection to Geometric Unity-class programs invokes Witten 1981 chirality no-go, Nielsen-Ninomiya lattice fermion doubling, Freed-Hopkins anomaly classification, and Distler-Garibaldi E_8 non-embedding. The 15-persona heterodox dialectical synthesis completed 2026-05-28 (documents 00 through 00e in `../process/syntheses/`) identifies these as class-relative impossibility theorems whose joint application closes the smooth Kaluza-Klein reduction path but does not constrain substrate-level invariants. The synthesis identifies a six-axis specification space of alternative reduction classes the no-go theorems do not cover.

## 3. Phase structure

### Phase 1: Deep research synthesis (complete)

Four deep-research prompts drafted 2026-05-28 to survey existing literature on:
- Connes spectral triple extension to non-embeddable Type II_1 internal algebra
- Pairing-relativity of Freed-Hopkins cobordism classification
- Class-assumption decomposition of the four no-go theorems plus published evasions
- Formal FLP / CAP analogy between physics no-go theorems and distributed systems consensus impossibility results

Deliverable: four literature-anchored synthesis briefs filed in `../literature/`. Each brief identifies prior art, names adjacent published work, and assesses genuine novelty of the corresponding finding. **Status (2026-05-30): all four briefs have returned and are in `../literature/`.**

Success criterion: each prompt returns either substantive prior art (which informs the specification choice) or honest "genuinely unexplored" verdict (which confirms novelty of the proposed direction).

Risk: deep-research tools may return incomplete coverage. Mitigation: cross-check with at least two independent deep-research tools (ChatGPT Deep Research, Gemini Deep Research, or Perplexity Pro) where divergence appears.

Time estimate: complete as of 2026-05-29.

### Phase 2: Open-source repository setup

Migrate the work to a public GitHub repository, set up contribution guidelines, and prepare three initial publication artifacts.

Tasks:
- Create public GitHub repository with CC-BY-4.0 for documentation/content and MIT for code
- Migrate 35 persona passes plus 5 syntheses plus 4 deep-research briefs to repo
- Finalize formal paper draft, blog post draft, and this project plan as repo-root documents
- Write `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `README.md`, repo navigation index
- Publish blog post on chosen platform; announce repo to relevant communities

Deliverable: live public repository with full work record, contribution surface, v2 top-line drafts, and a soft-launch posture.

Success criterion: at least one external contributor opens an issue or pull request within 60 days of repo public-launch.

Risk: repo receives no external engagement. Mitigation: targeted outreach to mathematicians and physicists working in the four substrate-class candidate areas (Connes school, Sorkin causal-set community, Wolfram Physics Project contributors, AdS/CFT holography researchers).

Time estimate: initial repository setup complete when this draft is public; follow-on work is issue triage and contributor onboarding.

### Phase 3: Specification selection

Lock the sextuple specification (L1 substrate class, L2 observer class, L3 pairing, L4 causal-order class, L5 emergence class, L6 coordination-loop class) for the first concrete construction attempt.

Recommended starting points based on 00e analysis:

- Path X (hold-fixed-vary-one): L1 = Connes Type II_1 + Jones subfactor, L2-L6 set to standard defaults. Question: which single axis dropping opens a substrate-level invariant?
- Path Y axis 1: Vary L4 to Sorkin causal-set (strongest single-axis dropping from established literature)
- Path Y axis 2: Vary L5 to Wilson RG fixed-point / universality-class substrate
- Path Y combined: Vary L1 + L5 simultaneously
- Full sextuple: name a specific (L1...L6) hextuple at the start

The deep-research and ranking packets refine the first public test order:

1. No-go assumption/evasion matrix across Witten, Nielsen-Ninomiya, Freed-Hopkins, and Distler-Garibaldi.
2. Finite Connes spectral Standard Model control case plus Type II_1 / non-embeddable extension checklist.
3. Six-axis candidate template with 5 concrete examples.
4. Nielsen-Ninomiya protocol-analogy pilot as the most operational distributed-systems bridge.
5. Repo posture/collaboration map so contributors know which claims are established, speculative, or parked.

Deliverable: written specification lock document for the chosen sextuple, with explicit citations to the existing mathematical literature for each axis choice.

Success criterion: specification is concrete enough that a working mathematician can produce or refute the substrate-level invariant within a 3-to-6 month research effort.

Risk: specification space proves intractable for any tested sextuple. Mitigation: pivot to honest closure (option (c) under Section 1) with structural-diagnosis verdict naming why.

Time estimate: 4 to 6 weeks for specification lock.

### Phase 4: Substrate-level invariant development

Develop the substrate-level chirality invariant for the chosen sextuple. This phase is the core mathematical work and depends entirely on collaborator participation.

Tasks (representative; will vary by sextuple choice):
- For Connes Type II_1 + Jones subfactor sextuple: construct a finite-index subfactor inclusion N⊂M whose planar algebra hosts Standard Model gauge group representations. Check non-embeddability via MIP* = RE.
- For Sorkin causal-set L4 dropping: construct a causal-set with directional invariant whose smooth Lorentzian shadow is the null Witten 1981 bundle-chirality content.
- For Wolfram multiway L1 + rulial-frame L2 dropping: identify the specific rulial reference frame implicit in the Geometric Unity construction and compute the branchial-space Z/2-graded invariant.

Deliverable: explicit substrate-level invariant construction with the substrate-level chirality content named and proved.

Success criterion: at least one constructed invariant either matches Standard Model chirality structure (positive result) or proves no construction in the chosen sextuple can match it (negative result).

Risk: extended exploration without termination. Mitigation: time-box to 12 months; if neither positive nor negative result is achieved, pivot to specification re-selection (return to Phase 3) or honest closure.

Time estimate: 6 to 18 months for first concrete result.

### Phase 5: Lossy reduction and Freed-Hopkins test

Verify that the substrate-level invariant, under the lossy reduction to the smooth bundle, reproduces the null Witten 1981 / Freed-Hopkins / Nielsen-Ninomiya / Distler-Garibaldi forgetful image. Confirms that the no-go theorems compute exactly what they should compute, without contradiction.

Tasks:
- Define the lossy reduction map from substrate to smooth bundle.
- Compute the bundle-shadow image of the substrate-level chirality invariant.
- Verify the image equals the null no-go theorem output.
- Verify the substrate-level invariant satisfies Freed-Hopkins compatibility (either pairing-invariant or with explicit pairing-relative justification per Phase 1 deep-research finding).

Deliverable: written verification document with explicit computation and cited theorems.

Success criterion: verification is reproducible by at least one independent reviewer.

Risk: the lossy reduction does not produce the expected null shadow, indicating the substrate-level invariant is not the right object for the no-go theorems' subject. Mitigation: re-examine the substrate specification and consider alternative invariant candidates.

Time estimate: 3 to 6 months for verification.

### Phase 6: Publication or honest closure

Publish results in a peer-reviewed venue or release as a closing document.

Tasks:
- Prepare final formal paper for arxiv submission (preferred categories: math.QA, hep-th, math.OA depending on substrate-class choice)
- Coordinate with collaborators for co-authorship
- Submit to peer-reviewed venue (Communications in Mathematical Physics, Journal of High Energy Physics, or equivalent)
- Update repo with final results and contributor acknowledgments

Deliverable: published or arxiv-posted paper plus updated repo.

Success criterion: paper is accepted by peer-reviewed venue OR honest closure document is released with structural-diagnosis verdict.

Risk: peer review identifies error in substrate-level invariant. Mitigation: revise and resubmit, or update repo with the identified error and honest-closure verdict.

Time estimate: 6 to 12 months for publication cycle.

## 4. Resource requirements

### Joe-time

- Phase 1 deep-research execution: 4 to 8 hours total across 4 prompts
- Phase 2 repo setup desk session: 4 to 8 hours
- Phase 3 specification lock: 2 to 4 hours per axis evaluation
- Phase 4 substrate-level invariant work: depends entirely on collaborator participation; Joe-time minimal if collaborators carry the math
- Phase 5 verification: 2 to 4 hours coordination
- Phase 6 publication: 4 to 8 hours for paper preparation

### Collaborator requirements

- One or more mathematicians with subfactor / spectral triple expertise (for Connes II_1 path)
- One or more physicists with causal-set / Sorkin theory expertise (for Sorkin L4 path)
- One or more Wolfram Physics Project contributors (for Wolfram L1 path)
- One or more topologists with motivic / tmf / prismatic expertise (for higher-categorical L1 path)
- One or more philosophers of physics for cross-checking the dialectical analysis
- One or more writers for ongoing accessibility maintenance

### Infrastructure

- GitHub repository (free tier sufficient for initial public working draft)
- Optional: discussion forum (GitHub Discussions sufficient)
- Optional: Zulip or Slack workspace for active contributors (decision deferred to Phase 2)

## 5. Success measurement

### Phase-level success

Each phase has explicit success criteria named above. Phase success is binary: criterion met or not met within time estimate.

### Program-level success

The program succeeds in any of the following three outcomes:

1. Positive: a substrate-level invariant exists for at least one sextuple, maps to Standard Model chirality content under the lossy reduction, and satisfies Freed-Hopkins compatibility. Geometric Unity-class programs have a real mathematical foundation.
2. Negative: no substrate-level invariant exists for any sextuple tested across at least three mathematically-distinct paths. Geometric Unity-class programs close honestly with a precise reason for failure.
3. Structural closure: the substrate-level invariant question is shown to be Rice-undecidable for non-regular reductions, ZFC-independent, or observer-class-relative in a way that no finite observer can settle. The lane closes with a precise structural-diagnosis verdict and the methodology of substrate-inversion analysis becomes a transferable artifact for adjacent open problems.

Each outcome is publishable. None requires Geometric Unity to be vindicated as a finished theory.

## 6. Risk register

- Risk: deep-research prompts return inadequate coverage. Mitigation: cross-tool verification.
- Risk: no external collaborators engage. Mitigation: targeted outreach to specific research communities.
- Risk: specification space proves intractable. Mitigation: pivot to honest closure with structural-diagnosis verdict.
- Risk: substrate-level invariant construction is too long-running for any single research effort. Mitigation: time-box phases; pivot to honest closure when time bounds exceeded.
- Risk: peer review identifies error. Mitigation: standard revise-and-resubmit cycle plus repo update.
- Risk: program is perceived as fringe or speculative by mainstream physics community. Mitigation: maintain rigorous citation discipline; release work under permissive license; emphasize the established mathematics underlying each substrate-class candidate.

## 7. Boundaries

This program does not:

- Vindicate Eric Weinstein's specific Geometric Unity claims as a particular formulation; the program tests Geometric Unity-CLASS programs from first principles.
- Replace existing Standard Model derivations; the program tests an alternative derivation path.
- Require the substrate-inversion methodology to be universally correct; the methodology is tested specifically on this question.
- Promise a positive result; honest closure is a valid outcome.

## 8. Cadence

- Monthly: project-state update committed to repo
- Quarterly: cross-phase progress review with collaborators
- Annual: structural reassessment of whether to continue, pivot specification, or close

The program continues so long as collaborators engage and phases deliver per their criteria. The program closes (any of the three success outcomes above) when phase deliverables stabilize.
