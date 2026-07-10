---
title: "Six-Axis Candidate Specification Template"
status: canon
doc_type: specification
updated_at: "2026-05-31"
---

# Six-Axis Candidate Specification Template

**Purpose.** Any proposed substrate-level pathway for evading or reframing the chirality / anomaly / gauge-emergence no-go theorems (Witten 1981, Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi) must fill this template before it is admitted as an open candidate. The protocol's job is not to solve any path. Its job is to make every candidate a typed research object, so that:

- Specialists can evaluate it without translating informal prose.
- Agents can reject under-specified proposals quickly.
- Heterodox proposals become testable rather than atmospheric.
- Two candidates can be compared axis by axis instead of by rhetorical mood.

**Hard rule.** A candidate with any axis left blank, vague ("emergent somehow"), or filled with adjacent terminology that does not name a class is not admitted. It returns to the proposer for sharpening.

---

## How to fill each axis

Each axis has:

1. **A class label** — pick from the menu, or extend the menu with one sentence saying why a new class is needed.
2. **A specification** — the concrete construction at that axis (algebra, category, partial order, protocol, etc.). 1-3 sentences.
3. **A literature anchor** — at least one published paper, preprint, or textbook the class points to. "None known" is acceptable but must be stated.
4. **A class-assumption signature it breaks** — name which assumption of which no-go theorem this axis-choice violates, or "preserves all four."

A candidate is the septuple `(L1, L2, L3, L4, L5, L6, L7)` of these fillings, PLUS a Layer-0
semantic-alignment precondition, plus the chirality bridge claim and one first falsification test.

> **RATIFIED 2026-07-10 (Joe): six axes -> seven axes + a Layer-0 precondition.** (1) **L7
> (positivity / state-space metric signature)** is promoted from the provisional seventh candidate
> (`canon/six-axis-candidate-krein-positivity-dg.md`) to a full axis: it earned its slot because its
> lever is now exercised by two independent candidates (ghost-parity/Krein AND the records-as-rows
> reframe) and, decisively, the anchor-scale result FORCES the Krein form on GU's own graded-IG
> algebra (`canon/anchor-scale-graded-ig-algebra-RESULTS.md`). The conservative reading (L7 = L3 with
> its inner-product signature made explicit) is preserved, not erased. (2) **Layer-0 (semantic
> alignment / homonymy)** is added as a PRECONDITION run before L1-L7: it is a different KIND of check
> (semantic, not structural), so it is a precondition, not an eighth peer axis. Rationale + receipts:
> `explorations/semantic-alignment-precondition-axis-proposal-2026-07-10.md`.

---

## Layer 0 — Semantic alignment (PRECONDITION, run before L1-L7)

> *Do the construction and the no-go MEAN the same object by their shared terms?* A no-go may fail to
> bite not because a structural assumption is dropped, but because its key term denotes a different
> object than the one the construction built — the philosopher's and the geometer's "shape" sharing a
> name for different things. This is a semantic check, not a structural one, so it runs first; if the
> shared terms are homonyms, the entire L1-L7 mapping is comparing different objects.

**The check:** for each key term in the no-go's statement (the object it constrains, the
predicate/test it applies, the invariant it computes), mark the construction's use as:

- **SAME-OBJECT** — the construction and the theorem denote the same mathematical object by this term.
- **HOMONYM** — same name, different object (name which two objects, and via what map they relate).
- **UNCERTAIN** — not yet adjudicated (an open sub-task, not a free pass).

**Two failure directions Layer-0 catches:**

- *False escape (equivocation trap):* the candidate believes it evaded, but quietly weakened the
  term's sense — the theorem still bites the object actually built.
- *Real inapplicability (scope by homonymy):* the theorem genuinely constrains a different object; the
  construction is outside its domain, not in contradiction with it. (This is what produces
  "EVASION BY SCOPE EXIT" verdicts — Layer-0 makes them predictable rather than ad hoc.)

**Worked receipts (do not skip — these are why Layer-0 exists):** Distler-Garibaldi's "chirality"
(`V_{2,1}` complexity, Lie-algebraic) vs GU's `ind_H(D_GU)` (operator-analytic) — HOMONYM, the source
of the DG scope-exit; "the Rarita-Schwinger operator" = the ghost-subtracted gravitino (-42) vs the
geometric gamma-traceless operator (-38) — HOMONYM, the entire carrier bit; and "generation" itself
(GU's rep-theoretic "imposter" third family vs the SM's observed generations) — UNCERTAIN.

**Hard rule:** a candidate that leaves any key term UNCERTAIN may still be admitted, but the
uncertainty is a tracked open sub-task; a candidate that has an unmarked HOMONYM at a load-bearing
term is NOT admitted until the two objects and their relating map are named.

---

## Leg 1 — Substrate class

> *What kind of mathematical object is the substrate?* The substrate is the level at which the chirality-bearing invariant lives, before any reduction to the smooth bundle shadow. The no-go theorems do not see this level; they see its forgetful image.

**Menu (extend with justification if needed):**

- (a) Smooth principal bundle on a smooth manifold (00d default; what Witten 1981 and Distler-Garibaldi assume).
- (b) Connes spectral triple (finite Connes-Chamseddine SM control case).
- (c) Type II_1 spectral triple with Jones-subfactor extension; non-embeddable regime allowed (MIP*=RE adjacent).
- (d) Holographic QEC code with chiral MTC logical algebra.
- (e) Wolfram multiway hypergraph rewriting in a specified rulial frame.
- (f) Higher / motivic / tmf / prismatic substrate (generalized cohomology valued).
- (g) Stochastic / log-correlated GFF noise class.
- (h) Cartan parabolic Klein pair with G_2 hint.
- (i) Asynchronous / Margolus partition cellular automaton.
- (j) IIT-integration-maximal substrate.
- (k) Sorkin causal-set substrate (the substrate IS the causal set; see also Leg 4).

**Fill:**

- **Class label:**
- **Specification (1-3 sentences):**
- **Literature anchor:**
- **Class-assumption signature broken:**

---

## Leg 2 — Observer class

> *What kind of observer extracts the bundle shadow from the substrate?* The observer is the computational/measurement class that performs the forgetful operation. Different observer classes can see different invariants of the same substrate.

**Menu:**

- (a) Finite Turing observer (BPP / BQP) — the implicit baseline.
- (b) Hypercomputing observer (Malament-Hogarth class).
- (c) Ω-oracle observer (halting-class oracle).
- (d) Snowball / metastable consensus observer — finite, subsampling, ε-bounded (k, α, β parameters).
- (e) Quantum reference frame (Bartlett-Rudolph-Spekkens class).
- (f) IIT-maximal-Φ observer.

**Fill:**

- **Class label:**
- **Specification:**
- **Literature anchor:**
- **Class-assumption signature broken:**

---

## Leg 3 — Pairing

> *How does the observer pair with the substrate?* This axis names the channel/coupling/pairing between substrate and observer. It is what determines whether the extracted invariant is well-defined, and whether anomaly content survives the pairing.

**Menu:**

- (a) Cartesian / smooth (implicit baseline; tensor-product channel).
- (b) Superdeterministic (Hossenfelder, 't Hooft).
- (c) IIT-maximal-partition (Tononi).
- (d) Marletto counterfactual / constructor-theoretic.
- (e) Wheeler-Lewis modal-selection.
- (f) Metastable-consensus pairing — parameters (k, α, β, CAP-corner).
- (g) FLP / CAP / BFT protocol-class pairing — timing model, determinism, CAP corner, BFT threshold, consistency model.

**Fill:**

- **Class label:**
- **Specification:**
- **Literature anchor:**
- **Class-assumption signature broken:**

---

## Leg 4 — Causal-order class

> *What is the causal order on the substrate?* This axis names whether causal order is total (smooth Lorentzian), partial (DAG, CALM-monotonic), or substrate-native (Sorkin causal set). Witten, Freed-Hopkins, and Distler-Garibaldi all assume total smooth Lorentzian order.

**Menu:**

- (a) Total-order Lorentzian (smooth manifold, Cauchy slicing).
- (b) CALM-monotonic partial-order (distributed-systems / database eventual-consistency class).
- (c) Gossip-consensus partial-order (Hashgraph / Snowball gossip-induced partial order).
- (d) Sorkin causal-set (substrate IS a locally finite partially ordered set; Lorentzian metric is emergent).
- (e) Branching multiway DAG (Wolfram-style; rulial frame selects a slice).

**Fill:**

- **Class label:**
- **Specification:**
- **Literature anchor:**
- **Class-assumption signature broken:**

---

## Leg 5 — Emergence class

> *Is the substrate a specific object, or a universality class / fixed point / attractor whose macroscale invariants are emergent?* Witten / Freed-Hopkins / Distler-Garibaldi assume specific-object substrate (a particular manifold, bundle, group). Wilson-onward physics says universality-class substrate is often what nature actually supplies.

**Menu:**

- (a) Specific-object substrate (00d default).
- (b) Universality class / RG fixed point (Wilson, Kadanoff).
- (c) Self-organized critical attractor (Bak, Per Tang Wiesenfeld).
- (d) Autopoietic / Maturana-Varela closure.
- (e) Topological phase / SPT class (Wen, Kitaev).

**Fill:**

- **Class label:**
- **Specification:**
- **Literature anchor:**
- **Class-assumption signature broken:**

---

## Leg 6 — Coordination-loop class

> *Is there a closed-loop coupling between substrate dynamics and observer extraction?* The no-go theorems implicitly assume no loop — substrate is fixed, observer reads off invariants. Coordination-loop class names the dynamics that links them and may be where chirality gets selected.

**Menu:**

- (a) No loop (00d implicit baseline).
- (b) Mean-field game (Lasry-Lions).
- (c) Hopfield-style attractor dynamics.
- (d) Physarum / reaction-diffusion stigmergic.
- (e) Ising / spin-glass broken-symmetry dynamics.
- (f) Dijkstra self-stabilizing protocol.
- (g) Stochastic gradient / RG flow as coordination dynamics.

**Fill:**

- **Class label:**
- **Specification:**
- **Literature anchor:**
- **Class-assumption signature broken:**

---

## Leg 7 — Positivity / state-space metric signature

> *What is the SIGNATURE of the inner product on the state space, and is a superselection needed to
> recover probabilities?* Two candidates can share an identical L3 pairing CHANNEL yet differ on
> whether the induced form is positive-definite or indefinite, and on whether a ghost-parity `Z2`
> superselection is required — a difference invisible in the L3 menu and exactly what decides the
> hidden positivity premise many no-goes assume. Ratified as a full axis 2026-07-10; the lever is
> exercised by the ghost-parity/Krein candidate and the records-as-rows reframe, and is FORCED on GU's
> graded-IG algebra at anchor scale.

**Menu:**

- (a) Positive-definite Hilbert (the standard hidden premise; no ghosts).
- (b) Indefinite Krein `(+,-)` with a ghost-parity `Z2` superselection + generalized (projector) Born
  rule (Turok-Bateman, arXiv:2607.00096; the `(+96,-96)` GU triplet).
- (c) Degenerate / null sector present (records or modes with zero norm).

**Fill:**

- **Class label:**
- **Specification:** (state the signature explicitly; if indefinite, name the superselection datum and
  the probability rule that recovers nonnegative probabilities.)
- **Literature anchor:**
- **Class-assumption signature broken:** (which no-go's positivity premise this touches.)

**Conservative-reading note (keep visible):** L7 can be read as "L3 with its inner-product signature
and any superselection structure made explicit." It is ratified as its own axis because the signature
is a degree of freedom NOT determined by the L3 channel (Euclidean -> definite; `q>0` -> indefinite;
the ghost-parity `Z2` is extra data), and isolating it is what keeps the single dropped assumption from
being smeared into a pairing tuple. Do not erase the conservative reading; it is the honest either/or.

---

## Closing the candidate

After clearing the Layer-0 precondition and filling all seven axes, the candidate must also state:

### Chirality bridge claim

One paragraph (3-6 sentences) saying:

- What substrate-level invariant carries chirality / 3-generation / gauge-group content at the substrate level.
- What the forgetful operation looks like that reduces the substrate to the smooth-bundle shadow.
- Why the smooth-bundle shadow yields exactly the null Witten / Nielsen-Ninomiya / Freed-Hopkins / Distler-Garibaldi image that those theorems compute.

### One first falsification test

One concrete check that, if it fails, kills the candidate. The test must be:

- Operationally describable in 1-2 paragraphs.
- Runnable either by an agent pass, a contributor, or a defined specialist; name which.
- Tied to a specific no-go theorem assumption being broken or preserved.

A candidate with no first falsification test is not admitted.

---

## Acceptance summary (one-line table)

When the candidate is filled, summarize at the top of the artifact with this row:

| candidate | L0 semantic-alignment | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | L7 positivity | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (name) | (class) | (class) | (class) | (class) | (class) | (class) | (1-line) |

This row is what the repo navigation lists. It is the contract.

---

## Why every future substrate path must use this

The seven-axis space (a Layer-0 precondition + L1-L7) contains ≈ 16,000 candidate sextuples; the mathematically tractable subset is perhaps 20-50. The template's job is to keep the conversation inside that tractable subset rather than letting candidates accumulate as informal prose.

It also forces honest comparison: two candidates that agree on (L1, L2, L3) but differ on (L4, L5, L6) are doing different work, and the template makes that visible. Without it, both proposals can look like "alternative substrate ideas" and waste reviewer attention.

The protocol does not prefer any class. It prefers any candidate that fills all six axes with specifications a specialist can check.
