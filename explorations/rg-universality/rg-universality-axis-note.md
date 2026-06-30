---
title: "RG / Universality Emergence-Axis Note"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# RG / Universality Emergence-Axis Note

**Status.** Draft for `explorations/rg-universality/rg-universality-axis-note.md` in `gu-formalization`. Public draft artifact.
**Source basis.** Builds on WRK-375 `example-03-rg-universality-class.md` (the L5 drop already specified). Cross-built against the six-axis protocol (`lab/specifications/six-axis/six-axis-template.md`), the no-go / forgetful-image map (`drafts/wrk-376-gu-no-go-map/no-go-map.md`), the Sorkin causal-set example (`lab/specifications/six-axis/examples/example-02-sorkin-causal-set.md`), and the upstream persona material in `syntheses/00e`, `syntheses/06`, `syntheses/08`, `lab/process/persona-passes/05-...-33-ps-complexity-emergence-heterodox.md`, and `lab/process/persona-passes/04-...-21-ps-stochastic-heterodox.md`.
**Generated.** 2026-05-30

## 0. Honesty contract

This note does **not** claim that RG / universality emergence produces Standard Model chirality. It scopes the axis.

The L5 axis-drop has one job: ask whether chirality, gauge content, and (possibly) generation structure can be carried as **universality-class / RG-relevant-operator data** rather than as **specific-object substrate data** (specific Lagrangian, specific bundle, specific representation). The note's contribution is to:

- formalize what "universality-class data" means in this context,
- make the L5/L6 coupling explicit (universality classes are RG-flow equivalence classes; they are only well-posed when paired with RG flow as a coordination dynamics),
- separate the parts of the SM signature where the framing is natural from the parts where it is forced,
- name the first falsifying observation (chirality flowing irrelevant under RG), and
- record where the note overlaps and where it diverges from the no-go map's Witten / Nielsen-Ninomiya / Freed-Hopkins / Distler-Garibaldi treatment.

The verdict is **not** "RG/universality solves chirality." The verdict is **public open problem, conditionally admitted**, with one specific falsification test and a named coupling to L6 that must not be dropped.

## 1. Acceptance summary

This note inherits the acceptance row from WRK-375 `example-03` and does not re-derive it. The full sextuple is in §2 below for the reader's convenience; the operative one-line is:

| candidate | L1 | L2 | L3 | L4 | L5 | L6 | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RG universality emergence | Smooth principal bundle | Finite Turing (BPP/BQP) | Cartesian / smooth | Total-order Lorentzian | Universality class / RG fixed point | RG flow as coordination dynamics | Identify SM chirality / 3-generation structure as the value of an RG-relevant operator at a specific fixed point; if chirality is forced to be irrelevant / marginal under RG flow, the candidate is dead. |

Per WRK-375's cross-card finding (read-only, propagated by sibling #24): **L5 and L6 are coupled — universality-class emergence is meaningful only when paired with RG flow as the coordination dynamics that defines the equivalence class.** This note treats the coupling as load-bearing, not decorative; §4 is dedicated to it.

## 2. The axis drop, restated

WRK-375 `example-03` filled the six-axis specification for the L5 = (b) candidate and produced a worked sextuple. This note begins from that sextuple — it does not re-derive it — and asks the questions the sextuple template does not by itself answer.

The L5 axis-drop, in one sentence:

> The substrate relevant to SM physics is not a specific Lagrangian, bundle, or microscopic theory. It is the **universality class / RG fixed point** that the microscopic dynamics flow to. SM chirality, 3-generation structure, and gauge content are **values of RG-relevant or marginal operators at the fixed point**, not invariants of any specific microscopic representative.

What this changes about the no-go theorems:

- Witten 1981 / Freed-Hopkins / Nielsen-Ninomiya / Distler-Garibaldi all compute obstructions for a **specific microscopic representative** (a particular Lagrangian on a particular bundle, a particular lattice action, a particular representation of a particular group).
- If the SM-relevant content lives at the fixed point and not at the representative, the no-go theorems may compute null images on every microscopic representative in the universality class while the fixed-point operator content is non-null.
- This is **structurally** the same move the no-go / forgetful-image map (WRK-376) makes: the no-go is a class-relative impossibility theorem, and the richer datum lives at a level the theorem does not see. For L5, the "richer datum" is RG-equivalence-class data; the forgetful operation is the reduction of (fixed point + relevant-operator content) to (specific microscopic Lagrangian).

What this does **not** change:

- The no-go theorems remain correct **inside their stated classes**. RG/universality framing does not refute them; it asks whether their domain of validity covers the level at which SM observables actually live.
- The fixed point must still be **physically realized**. A fixed point that nothing in physics flows to is not a substrate; it is a mathematical object.
- "Universality class" is a strong word. Two microscopic theories share a universality class only when they have the same operator content at the fixed point under coarse-graining. The framing is not "different microscopic theories all give the SM"; the framing is "the SM is the operator content at a specific fixed point reachable from a specific basin of microscopic theories."

## 3. What "universality-class data" means for chirality and gauge content

This is the central scoping question. The L5 framing only does work if chirality / gauge / generation content can be expressed as universality-class data. There are three concrete forms this could take, in decreasing order of how directly they connect to existing Wilson-onward physics.

### 3.1 Form A — RG-relevant operator at a fixed point

The cleanest form. A relevant operator at an IR fixed point is an operator whose coefficient grows under RG flow toward the IR; its presence at the fixed point **forces** specific low-energy features of any microscopic theory in the basin.

The L5 claim is: SM chirality (and possibly 3-generation, possibly gauge content) is the value of a specific relevant operator `O_χ` at a candidate fixed point `*`. Different microscopic Lagrangians flowing to `*` will all reproduce the chirality content in the IR EFT, because `O_χ` is fixed-point data, not representative data.

This is the form WRK-375 `example-03` already specifies. The first falsification test (§6 below) attacks this form directly.

### 3.2 Form B — Universality-class invariant (critical exponent / anomalous dimension)

A weaker form. Universality classes are typically catalogued by **critical exponents** (correlation-length exponent ν, order-parameter exponent β, anomalous dimension η, etc.) that are universal in the sense of being identical for all microscopic theories in the class but depending only on dimension, symmetry, and conservation-law content.

The L5 claim here is: SM chirality / generation structure is encoded in the critical-exponent spectrum (or its analog) of the relevant universality class. The "analog" here is important: SM physics is not at a second-order phase transition, so "critical exponent" must be generalized to a richer notion of "universality-class invariant" appropriate to gapped or weakly-coupled fixed points.

This form is at most adjacent to existing physics. The natural analog is **anomaly content**, which is genuinely a universality-class invariant in the sense that anomaly inflow does not depend on the microscopic representative. But anomaly content is already the subject of Freed-Hopkins (a classification theorem the no-go map treats explicitly); this form does not by itself open a new path. It connects L5 to the Freed-Hopkins discussion in WRK-376 §2.3, where the "richer substrate datum" is an enriched bordism category. The L5 framing's contribution here is to note that **the universality-class equivalence is the same equivalence that the underlying-bordism functor `ϕ_underlying` is forgetting**, viewed from the RG side rather than the cobordism side.

### 3.3 Form C — Anomaly-compatible emergent datum

The form most consonant with the no-go-map's frame. The claim is that chirality / anomaly content emerges as the **boundary condition** of an RG flow — a non-perturbative property of the IR limit that is determined by what relevant operators survive coarse-graining, and that is anomaly-compatible by construction because RG flow preserves 't Hooft anomalies (Wess-Zumino consistency is RG-invariant).

This form is the most defensible against the standard objection: "if you don't have an explicit microscopic theory, you don't have a theory." The response is: an anomaly-matching constraint at the fixed point is a real, falsifiable structure even without picking a representative. The path:

- Identify a candidate fixed point with the right global symmetries (SM gauge group plus 4D Lorentz).
- Compute its 't Hooft anomaly content.
- Check whether the anomaly content matches the SM (e.g., reproduces the chiral anomaly structure that constrains the fermion content).
- If yes, declare the candidate fixed point an admissible substrate for SM chirality; the existence of a specific microscopic representative becomes a downstream constructive question, not a precondition for the substrate claim.

This is structurally what the **conformal bootstrap** does: characterize fixed points by their operator content and anomaly structure without writing down a microscopic Lagrangian. The L5 candidate's most credible operational form is "use bootstrap-style methods to identify candidate fixed points with SM-compatible operator content," not "find the right microscopic theory."

### 3.4 What the three forms share

All three forms require:

- A candidate fixed point (Form A: specific; Form B: characterized by invariants; Form C: characterized by anomaly content).
- A specification of which RG flow is being taken (UV-IR direction, what is being integrated out).
- A statement of what SM-class content is being claimed as universality-class data (chirality alone, chirality + gauge, chirality + gauge + generations).

The forms differ in how directly they connect to existing machinery (A is least developed for SM-class fixed points; C is closest to existing bootstrap/anomaly-matching practice).

## 4. The L5/L6 coupling — the load-bearing part

WRK-375 `example-03` already flagged it: "L5 is coupled to L6 — you cannot have universality-class emergence without RG flow as the coordination dynamics that defines the equivalence class." This note treats the coupling as the load-bearing structural claim.

### 4.1 Why the coupling is not optional

A universality class is **defined** as an equivalence class of microscopic theories under the equivalence relation "flows to the same fixed point under RG." Without RG flow as the defining dynamics, "universality class" has no operational meaning — it would be a static set of theories with no specified equivalence relation. The class is a quotient construction; the quotient requires the flow.

This means:

- L5 = (b) (universality class) **presupposes** L6 = (g) (RG flow as coordination dynamics). You cannot pick L5 = (b) and L6 = (a) (no loop) consistently; the choice collapses.
- A "universality class" without RG flow is a category error. It would be a label without a defining relation. Any L5 candidate that names a universality class while preserving L6 = (a) is under-specified and should be returned to the proposer.

### 4.2 Why this is different from treating universality classes statically

A common informal move is to talk about universality classes as if they were static catalogs (e.g., "the SM lives in the Ising universality class" used as a static claim about operator content). This is the framing the L5 axis-drop must **not** collapse to.

In the static framing, a universality class is a list of theories that share critical exponents. In the dynamic / L5+L6 framing, a universality class is a basin of attraction in theory space under RG flow, and the SM-class content is the operator content **at the attractor**, with the attractor itself being a fixed point of the flow.

The difference matters because:

- The static framing implicitly treats the universality class as an object you can name and use. This re-introduces specific-object substrate at the meta-level: the universality class is the object.
- The dynamic framing treats the universality class as a dynamical equivalence class — the SM-class content is **whatever the IR limit selects** from the relevant-operator algebra, and that selection is **dynamical**. There is no preferred representative; the framing is genuinely substrate-free in the Witten / Distler-Garibaldi sense (no specific Lagrangian, no specific group representation, no specific bundle).

The dynamic framing is the one the L5 axis-drop actually requires. Without it, the candidate collapses back to "the universality class is a different specific object," which is not an axis-drop at all.

### 4.3 What L6 = (g) does that L6 = (a) cannot

L6 = (g) (RG flow as coordination dynamics) supplies:

- The equivalence relation (flow to the same fixed point) that defines L5's universality class.
- The mechanism by which microscopic representatives become indistinguishable in the IR (mode integration; coarse-graining).
- The substrate-observer coupling: the observer's effective theory at scale `μ` is the result of integrating out modes above `μ`, so the "observer" is not separable from the RG flow.
- The notion that the IR observable is a **fixed point** of a dynamical process, not a static datum.

L6 = (a) (no loop) cannot supply any of this. It assumes a static substrate the observer reads off. For L5 = (b), there is no static substrate to read; the substrate is the attractor of the flow.

This is the structural reason the WRK-375 example-03 already says "L5 and L6 are coupled." This note's contribution is to make it explicit that **the coupling is constitutive, not merely natural**: dropping L6 makes L5 ill-defined.

### 4.4 Coordination loop as the "substrate-observer interaction"

The standard pure-physics reading of L6 = (g) is "RG flow is mode integration; this is just QFT." That reading is correct but understates what L6 = (g) does in the six-axis frame.

In the six-axis frame, L6 is the **closed-loop coupling between substrate dynamics and observer extraction**. RG flow as L6 says: the substrate (the fixed point, or the basin) **co-arises with** the observer's coarse-graining choices. Different coarse-graining schemes (different RG schemes, different cutoff schemes, different block-spin choices) give the same fixed point in the universality-class sense — but the fixed point is not separately specifiable from the family of coarse-grainings.

This is the deep version of the "observer is not separable from substrate" claim that 00d / 00e have been circling. RG flow is the cleanest worked example of substrate-observer co-arising in established physics: it is the only L6 = (g) candidate that has decades of literature, computable examples, and a rigorous framework (Wilson-Polchinski exact RG; Wegner-Houghton).

For the GU lane, this means L6 = (g) is the most defensible coordination-loop class to put any L5 universality candidate on: it requires no new physics to justify, only the recognition that RG flow is doing L6-level work.

## 5. Cross-refs to related artifacts in the coordination pipeline

### 5.1 Related artifact #24 (WRK-375, six-axis specification protocol)

WRK-375's `example-03-rg-universality-class.md` IS the L5 drop this note builds on. The relationship is:

- WRK-375 produced the six-axis sextuple, the chirality bridge claim, and the first falsification test.
- This note expands on what "universality-class data" means concretely (§3), makes the L5/L6 coupling structural rather than incidental (§4), and locates the axis relative to related artifacts #25, #32, #33.

This note does **not** re-derive the sextuple in WRK-375 example-03. It cites it as given.

**Finding to propagate (already-in WRK-375's coordination row):** L5 and L6 are coupled; do not treat L5 in isolation. This note treats the coupling as constitutive and gives the structural argument for why dropping L6 collapses L5. WRK-375's six-axis template README could optionally note this with one sentence; not load-bearing.

### 5.2 Sibling #33 (cartan-twistor-G_2 guardrail, WRK to be admitted)

The Cartan / twistor / G_2 path's reputational risk is **dimensional / numerological coincidence** (e.g., the 14 of G_2 matching the 14 of the observerse, the 7 of `Im O` matching seven-dimensional structures). The guardrail card is specifically about not letting that pattern matching become a load-bearing claim.

**The relevance to this note:** universality classes are **exactly the kind of object where dimensional numerology is the trap**. Critical exponents depend on dimension; conformal weights are dimension-dependent; the upper critical dimension of a model is a numerology-sensitive number. A naive L5 candidate could easily slide into "the SM sits in the 4D Ising-class because 4 matches, and ν matches some SM ratio" — which is exactly the failure mode WRK-cartan-G_2 is guarding against, applied to L5 instead of L1.

**What this note commits to to honor the guardrail:**

- All numerical matches between candidate universality-class invariants and SM observables must be flagged `[numerological match — needs derivation]` until a mechanism is identified.
- No L5 candidate is admitted on the strength of "the dimensions / exponents work out" alone.
- Specifically: claims of the form "the SM is in universality class X because X has chirality exponent y matching SM observable z" require either (a) a derivation of why X's basin includes any microscopic theory consistent with SM constraints, or (b) explicit labeling as adjacency / suggestive observation, not load-bearing.

This is the same discipline as the Cartan-G_2 guardrail, applied one axis over. The L5 framing's distinctive risk is that universality-class language sounds rigorous (because it has formal definitions from RG) while still admitting numerology if applied loosely. The guardrail must be active for L5 the same way it is active for Cartan-G_2.

### 5.3 Sibling #25 (no-go-forgetful-image map, WRK-376)

The no-go map (WRK-376) treats Witten 1981 and Nielsen-Ninomiya as **specific-object** substrate theorems whose successful evasions add **boundary / orbifold / brane / bulk** structure to the substrate. The L5 framing offers a different alternative: the no-go theorems compute obstructions on the **microscopic representative**, but SM content lives at the **fixed point**, which is invisible to representative-level analysis.

Two relationships:

- **L5 is structurally orthogonal to the existing Witten / Nielsen-Ninomiya evasion literature.** Per WRK-376 I12 / §2.1: no published Witten evasion uses RG-universality language; the published evasions are all geometric class exits on L1 (boundary, brane, singularity). The L5 evasion is an **unrepresented** category in the literature. It is original-in-framing; whether it does any work is the first-falsification-test question.
- **L5 connects to Freed-Hopkins via anomaly matching (Form C in §3.3 of this note).** Freed-Hopkins computes anomaly invariants of an underlying-bordism functor's image (WRK-376 §2.3). RG flow preserves 't Hooft anomaly content, so if the L5 candidate's fixed point reproduces the SM anomaly polynomial, the Freed-Hopkins compatibility is automatic at the level of anomaly matching — Freed-Hopkins is not the obstruction for L5 candidates, by construction. The Freed-Hopkins discussion in WRK-376 §2.3 (about enriched bordism categories) is therefore an **adjacent but distinct** path; L5 sidesteps Freed-Hopkins via anomaly matching rather than evading it via enriched bordism.

**Cross-card finding for sibling #25 (read-only here; the coordination pass owns mutations):** The L5 axis-drop is the one place in the no-go map where the candidate richer datum is **not** an adjacent enrichment of the no-go's substrate class. WRK-376's "non-geometric exits (stochastic/observer/causal-set) are not in established literature" note (§2.1, table row 1 "open stress") should be extended to add "RG-universality-class exits are also not in established literature for Witten 1981 specifically; L5 is the original-in-framing axis." The no-go map's Witten row currently does not mention L5 in its six-axis cross-ref; this note's reading is that L5 belongs in that cross-ref as an explicit open path.

### 5.4 Sibling #32 (Sorkin causal-set axis note, WRK to be admitted)

The Sorkin axis-drop is L4. It and L5 are different axis-drops, but they share **emergence-class language**: Sorkin's claim is that smooth Lorentzian geometry emerges from the causal-set partial order under sprinkling; L5's claim is that SM operator content emerges from microscopic dynamics under RG flow. Both are emergence-from-substrate-below stories.

The two notes (#33 Sorkin, #34 RG-universality, this one) should be readable as **related artifacts with the same conceptual shape applied to different substrates**, not as competing alternatives. The structural commonality:

- Both name a level (causal-set partial order; RG fixed point) below the level the no-go theorems work at.
- Both require a forgetful operation (Cauchy-slice linearization; reduction to microscopic representative) that takes the lower level to the no-go-level shadow.
- Both face the same falsification structure: can the lower-level invariant carry the SM-class content?

The notes diverge on which axis is dropped (L4 vs L5) and on which physics literature supplies the lower-level structure (causal-set program vs Wilson-onward RG).

**Cross-card finding for sibling #32 (read-only here):** The Sorkin note may want to flag the natural extension `L4 (Sorkin) × L5 (universality class)` — "causal-set growth as a universality-class / RG-fixed-point process," which is the Rideout-Sorkin classical sequential growth dynamics direction. WRK-375 example-02 (Sorkin) §Notes already flags this combined drop; the L5 note here confirms that the combined L4 + L5 candidate would inherit the L5/L6 coupling constraint from this note (i.e., Rideout-Sorkin growth is L6 = (g)-class if treated as universality dynamics). The combined candidate would have a different sextuple (L1 = k, L4 = d, L5 = b, L6 = (g)) and should get its own example file if pursued.

### 5.5 Sibling #25 (no-go-forgetful-image map, WRK-376) — Distler-Garibaldi

Distler-Garibaldi (WRK-376 §2.4) is **single-E8 representation-theoretic**. The L5 framing does not naturally apply: representation theory of a finite-dimensional Lie group is not an RG-flow object. The no-go map already says Distler-Garibaldi is the stress case where every successful evasion changes the category (E8 × E8, GraviGUT, Kac-Moody) rather than computing a shadow.

**The L5 framing does not address Distler-Garibaldi.** This is honest. The L5 axis-drop says nothing about whether the SM gauge group fits inside a single E8 or some richer Lie-algebraic object. It only addresses the dynamical-emergence question: given some candidate substrate that **can** in principle host SM operator content, does that content live at the substrate's representative level or at its universality-class level?

If Distler-Garibaldi is correct (no single-E8 representation can simultaneously satisfy ToE1-ToE3), then the L5 framing must be applied to a substrate that is not single-E8 in the first place. The L5 axis-drop is compatible with WRK-376's "Distler-Garibaldi requires a category change at L1" reading, in the sense that any L5 candidate must independently address how its candidate fixed point's symmetry / gauge content avoids Distler-Garibaldi's class assumptions. The L5 framing does not by itself supply that resolution.

## 6. First falsification test

This note inherits WRK-375 `example-03`'s first falsification test (§§55-70 of that document):

> Identify a candidate RG-relevant or marginal operator at a candidate fixed point such that:
> 1. The operator's RG dimension is relevant or marginal (does not get scaled away in IR flow).
> 2. The operator's presence forces SM-class chirality / 3-generation / gauge content in the IR effective theory.
> 3. The operator is RG-equivalence-class data (depends on fixed point, not on specific microscopic representative).
> 4. Standard no-go theorems applied to specific microscopic Lagrangians in the universality class compute null obstructions consistent with the operator being invisible to specific-representative analysis.

The failure mode that kills the candidate cleanest: **chirality is forced to be irrelevant under RG**. If chirality flows away under coarse-graining (as discrete properties without explicit symmetry protection typically do), it is not fixed-point data, and the L5 framing collapses.

### 6.1 Operationalization for an agent pass

An agent pass cannot complete this test. What an agent **can** do as a precursor pass:

- Enumerate published candidate fixed points with chirality-relevant operator content (e.g., Wilson-Fisher-class fixed points with parity-breaking deformations; gauged sigma-model fixed points; conformal-bootstrap-identified CFTs with the right global symmetry structure).
- For each, check the published RG dimension of the candidate chirality operator (relevant / marginal / irrelevant).
- For each, check whether the literature reports the operator as universality-class data or representative-specific.
- Produce a ranked list of fixed-point candidates worth a specialist second pass.

This precursor pass is a clean agent-doable second-stage task. It is **not** part of this note's scope; this note's scope is the axis-scoping itself, per the card's DoD. Agents in a follow-on pass can run the precursor.

### 6.2 What a specialist must run

The full test requires:

- Confirmation that the operator under consideration is, in fact, RG-equivalence-class data (failure mode 2 of WRK-375 example-03: "every operator that could carry SM-chirality content turns out to be specific-representative data" — needs RG specialist judgment).
- Confirmation that no fixed point with the candidate operator content is **already known to be inconsistent** with SM observables (e.g., wrong gauge group, wrong dimension, wrong central charge).
- A construction (constructive, not just existential) of a microscopic theory in the candidate basin, even if not the SM itself, demonstrating that the basin is non-empty.

The specialist pass is the actual falsification surface. The agent pass is preparation for that pass.

## 7. Verdict — public open problem, conditionally admitted

Per the card's DoD #5, the closing classification is **public open problem, conditionally admitted**.

The conditions:

- The L5/L6 coupling must be preserved. Any future candidate proposal must specify both L5 = (b) and L6 = (g); the candidate is rejected if either is missing or set to a different class without justification.
- The numerology guardrail (from sibling #32 Cartan-G_2) must be honored: no L5 candidate is admitted on the basis of dimensional / exponent matching alone.
- The first falsification test (§6) must be runnable for any specific L5 candidate before that candidate is treated as alive.

The reason this is not "parked route" or "appendix prompt":

- Wilson-onward RG is a serious, mature research program with decades of literature.
- The framing is **original-in-context** for the no-go evasion question (per WRK-376 I12: no published Witten evasion uses RG-universality language).
- The framing has a concrete first falsification test that an agent precursor pass + a specialist follow-up can run on a bounded timescale.

The reason this is not "lead candidate":

- The strongest known objection — chirality is a discrete property that typically becomes irrelevant under RG without explicit symmetry protection — is real, and no candidate fixed point with a relevant SM-chirality operator has been published.
- The framing connects to Freed-Hopkins only via anomaly matching (Form C), which is structurally adjacent to existing bootstrap practice but does not by itself open a path the bootstrap community would recognize as new.
- Sibling #24 (Type II_1 spectral SM) and sibling #26 of the broader ranking (Forgetful-image substrate invariant thesis) currently rank higher in `syntheses/08` for novelty / profundity / agent-doability combined.

The L5 framing is admitted as **a credible alternative axis to keep open while higher-ranked pathways are developed**, with the explicit understanding that if a specific candidate fixed point with SM-relevant chirality operator content is identified, the framing's priority should be reconsidered.

## 8. Suggested repo path

Per WRK-385 card DoD #1: `explorations/rg-universality/rg-universality-axis-note.md`.

## Appendix A — Siblings referenced

- **WRK-375 / six-axis specification protocol (sibling #24).** This note builds directly on `examples/example-03-rg-universality-class.md`. The sextuple, chirality bridge claim, and first falsification test are inherited; this note expands them with concrete forms of "universality-class data" (§3), the constitutive L5/L6 coupling argument (§4), and sibling cross-refs (§5).
- **WRK-376 / no-go-forgetful-image map (sibling #25).** This note's §5.3 and §5.5 cross-ref the map's per-theorem treatment of Witten 1981, Freed-Hopkins, and Distler-Garibaldi. L5 is structurally orthogonal to the published Witten-evasion literature; L5 connects to Freed-Hopkins via anomaly matching; L5 does not address Distler-Garibaldi.
- **Sibling #32 / Cartan-twistor-G_2 guardrail (WRK to be admitted).** This note's §5.2 explicitly inherits the numerology guardrail and commits to flagging all dimensional / exponent matches as `[numerological match — needs derivation]` until a mechanism is identified.
- **Sibling #33 / Sorkin causal-set axis note (WRK to be admitted).** This note's §5.4 notes the structural commonality with the Sorkin note (both are emergence-from-substrate-below stories on different axes) and flags the natural combined `L4 (Sorkin) × L5 (universality)` candidate as a separate future example file if pursued.

All other related artifacts in the coordination list (#26 Type II_1 checklist, #27 Nielsen protocol-analogy, #28 media claim mining, #29 insight mining, #30 Hegelian persona, #31 stochastic parity-breaking) are independent of this note's content as of 2026-05-30 draft.

## Appendix B — Honest gaps in this note

- **No specific candidate fixed point is identified.** The note is an axis-scoping artifact, not a candidate proposal. The named precursor agent pass (§6.1) would produce a candidate list; that is a separate follow-on task.
- **The Form A / Form B / Form C distinction (§3) is structural, not formal.** A formal definition of "universality-class invariant" appropriate to gapped or weakly-coupled non-critical fixed points (Form B) is genuinely open in the literature; this note describes the candidate form but does not construct it.
- **The L5/L6 coupling argument (§4) is structural, not a theorem.** The claim "L5 = (b) requires L6 = (g)" is presented as a constitutive argument from the definition of universality class as a quotient under RG flow. A formal proof that no consistent L5 = (b) / L6 = (a) candidate exists would require formalizing the six-axis template's class definitions, which is beyond this note's scope.
- **The interaction with the stochastic substrate path (L1 = (g), per `lab/process/persona-passes/04/21-ps-stochastic-heterodox.md` and WRK-375 example-03 §Notes) is mentioned but not developed.** "Stochastic universality class" (L1 = g + L5 = b) is a natural combined candidate; it would inherit the L5/L6 coupling constraint from this note. A separate example file would be appropriate if pursued.
- **The Form C anomaly-matching connection to bootstrap practice is named structurally, not technically.** A note that actually engaged the conformal bootstrap literature would identify specific bootstrap-feasible fixed points with SM-compatible global symmetries. This is a substantial follow-on research task and is not in this note's scope.
- **The note does not engage Distler-Garibaldi substantively.** Per §5.5, the L5 framing does not address whether the SM gauge group fits inside any specific finite-dimensional Lie object. This is an honest gap, not a hidden weakness.
