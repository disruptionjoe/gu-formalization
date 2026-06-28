---
title: "From Speculation to Falsification"
subtitle: "A Six-Axis Specification Protocol for Testable Frontier Physics"
author: "Disruption Joe"
status: draft
doc_type: white_paper
version: "0.1"
updated_at: "2026-06-11"
---

# From Speculation to Falsification

## A Six-Axis Specification Protocol for Testable Frontier Physics

**Disruption Joe**

**White paper draft v0.1, June 11, 2026**

> This paper proposes and preregisters a research-method protocol. It does not
> establish a new physical theory, validate Geometric Unity, or weaken any
> no-go theorem outside that theorem's stated assumptions.

## Abstract

Frontier theories often remain difficult to evaluate because their central
claims mix several independent choices: the mathematical substrate, the
observer allowed to extract predictions, the coupling between observer and
substrate, the causal-order model, the level at which regularities emerge, and
the dynamics coordinating those levels. A proposal may appear to evade a
no-go theorem or generate a novel prediction while changing one of these
choices without stating the change.

This paper introduces a six-axis specification protocol that turns such a
proposal into a typed research object:

```text
C = (L1 substrate, L2 observer, L3 pairing,
     L4 causal order, L5 emergence, L6 coordination loop)
```

The sextuple is accompanied by a source-to-observation map, an assumption
signature against relevant theorems, and one preregistered falsification test.
The protocol does not judge a theory true. It asks whether specialists can
identify what the theory is, compare it with alternatives, determine which
theorems apply, and state what result would kill its first load-bearing claim.

We present six testable hypotheses about the protocol itself and a prospective
benchmark comparing six-axis specifications with free-form proposals and a
length-matched generic checklist. Primary outcomes are specification
completeness, reviewer agreement, theorem-assumption localization,
falsification-test yield, time to identify fatal ambiguity, and resistance to
post hoc axis changes. Three worked examples show distinct uses: a
single-axis substrate modification, a coupled substrate/causal-order change,
and an emergence/coordination coupling. A fourth preliminary toy example
shows how changing only observer-substrate pairing can produce different,
noncontradictory reconstructed orders from one causal record graph.

The contribution is therefore methodological and falsifiable: if the protocol
does not outperform simpler documentation controls, fails to produce reliable
reviewer agreement, or merely relocates ambiguity into axis labels, it should
be revised or rejected.

## 1. The Problem

Theories at the edge of established physics face a recurring evaluation
problem. A proposal may name an exotic algebra, discrete causal structure,
emergent fixed point, computational observer, or feedback process without
specifying how these pieces jointly produce an observable result. Review then
oscillates between two weak forms:

1. dismissal by applying a theorem whose assumptions may not match the
   proposal; or
2. defense by claiming the proposal lives at a deeper level that the theorem
   cannot see.

Neither move is enough. A theorem is not defeated by changing vocabulary.
Likewise, a proposal is not evaluated fairly when its actual mathematical
class is left unspecified.

The central methodological claim of this paper is:

> Before asking whether a frontier theory is true, require it to declare the
> six structural choices that determine what its claims and tests mean.

This is specification before advocacy. It makes the proposal easier to
criticize because hidden assumptions become named commitments.

### 1.1 Why no-go theorems motivate the protocol

No-go theorems are exact results inside stated classes. Witten's
Kaluza-Klein analysis, the Nielsen-Ninomiya lattice obstruction,
Freed-Hopkins classification of invertible phases, and the
Distler-Garibaldi analysis of `E8` embeddings are not interchangeable
slogans. Each operates on particular mathematical objects with particular
symmetry, locality, regularity, or representation assumptions [1-4].

A serious alternative must therefore say:

- which assumptions it preserves;
- which assumptions it breaks;
- which new structure replaces a broken assumption;
- how the new structure maps to an observable or established control case;
- what failure would show that the replacement did not help.

The six-axis protocol is a compact way to force those statements.

### 1.2 Related specification practices

Other fields have improved review by standardizing what must accompany an
artifact. Model cards report intended use and evaluation conditions for
machine-learning models, while datasheets document the provenance,
composition, and limitations of datasets [5,6]. Registered Reports move
method review before results are known, reducing the freedom to redesign a
study after seeing its outcome [7].

The present proposal shares that discipline but targets a different object:
an under-specified theoretical research program. Its distinctive task is to
make theorem applicability, cross-level mappings, and first falsification
tests inspectable before a candidate receives substantial advocacy or
engineering effort.

## 2. The Six-Axis Research Object

Let a candidate theory or mechanism be represented by:

```text
C = (S, O, P, K, E, L; phi, Sigma, B, T)
```

where:

- `S` is the substrate class;
- `O` is the observer class;
- `P` is the observer-substrate pairing;
- `K` is the causal-order class;
- `E` is the emergence class;
- `L` is the coordination-loop class;
- `phi` is the source-to-observation map;
- `Sigma` is the theorem-assumption signature;
- `B` is the bridge claim connecting substrate structure to an observable;
- `T` is the first falsification test.

The first six entries define the candidate's structural type. The remaining
four make it evaluable.

### 2.1 L1: Substrate class

**Question:** What kind of mathematical object carries the proposed
invariant or dynamics?

Examples include a smooth bundle, spectral triple, operator algebra, tensor
network, causal set, rewriting system, stochastic field, cellular automaton,
or higher-categorical object.

This axis prevents an ordinary smooth object and a noncommutative or discrete
object from being discussed as though they were the same candidate.

### 2.2 L2: Observer class

**Question:** What kind of system is allowed to extract, calculate, or
physically register the claimed result?

An observer might be an ideal mathematical evaluator, finite classical
algorithm, bounded quantum algorithm, local measurement apparatus,
record-bearing physical system, or distributed reconciliation process.

This axis does not make observation create reality. It states the resources
and access conditions under which a prediction is defined.

### 2.3 L3: Pairing

**Question:** Through what channel does the observer couple to the substrate?

Pairing may be a smooth measurement map, spectral functional, local
interaction, communication protocol, reference-frame relation, sampling
process, or record-access channel. It determines which substrate distinctions
survive into the observer's data.

Pairing is often the hidden axis. Two observers can share a substrate and
causal structure yet receive different records because they couple through
different channels.

### 2.4 L4: Causal-order class

**Question:** What order of influence is assumed?

Candidates may use smooth Lorentzian causality, a partial order, locally
finite causal set, gossip-induced event order, branching history, or another
specified structure. Metric time, partial causal order, and protocol commit
order must not be silently conflated.

### 2.5 L5: Emergence class

**Question:** At what level is the claimed regularity supposed to exist?

The target may be a specific object, equivalence class, phase, universality
class, fixed point, attractor, or coarse-grained effective theory. Wilsonian
renormalization shows why this distinction matters: macroscale behavior may
belong to a universality class rather than one microscopic realization [8].

Recursive organization alone does not imply fractality. A fractal claim
requires evidence of self-similarity or scaling, not merely multiple levels.

### 2.6 L6: Coordination-loop class

**Question:** What dynamics, if any, connect substrate evolution, observer
extraction, and the emergence process?

The answer may be no loop, renormalization flow, self-stabilizing protocol,
consensus dynamics, attractor update, learning rule, or feedback process.
This axis makes history dependence and convergence assumptions explicit.
Distributed-systems results such as CALM and FLP illustrate why timing,
monotonicity, and coordination assumptions must be declared rather than
treated as implementation detail [11,12].

Context inheritance, including an epigenetic-style mechanism in which stable
state can be differentially expressed and locally reprogrammed, belongs here
when it acts as a coordination mechanism. It may also alter L3 when expression
controls which records reach an observer. It is a mechanism filling an axis,
not evidence for a seventh universal layer.

### 2.7 Why these six

The six axes decompose one source-to-observation chain:

```text
substrate
  -- pairing to observer, under a causal order -->
accessible state
  -- emergence and coordination -->
stable observable
```

Each axis answers a different question:

- what exists in the model;
- what can read or register it;
- how the two interact;
- which influences may precede which others;
- what equivalence level carries the claimed regularity;
- what update or feedback process makes that regularity stable.

This decomposition is minimal only as a working hypothesis. The axes are not
assumed to be statistically independent or ontologically fundamental. Some
candidates impose coupling rules, and some future domains may require an
additional field outside the sextuple. The benchmark in Section 6 is designed
to discover both cases.

## 3. The Testability Transform

The protocol transforms an informal proposal `Q` into a reviewable candidate
`C` through four operations.

### 3.1 Type the candidate

Every axis receives:

1. a class label;
2. a concrete specification;
3. a literature anchor or an explicit statement that none is known;
4. the assumptions preserved or broken.

An empty or atmospheric entry such as "emergent somehow" does not count.

### 3.2 Specify the source-to-observation map

The map

```text
phi: substrate state -> observer-accessible result
```

must identify intermediate operations such as projection, coarse-graining,
measurement, record formation, inherited expression, access restriction,
reconciliation, and readout.

These operations need not preserve the same structure. For example, evidence
states may merge monotonically while a later signed decision or threshold
readout is nonmonotonic. A clean specification names the stage at which the
change occurs.

### 3.3 Compute the theorem-assumption signature

For every relevant theorem `N_j`, define:

```text
Sigma_j(C) = (
  preserved assumptions,
  broken assumptions,
  replacement structure,
  unresolved assumptions
)
```

This does not prove that the candidate evades `N_j`. It determines whether the
theorem applies directly, applies to an image of the candidate, or cannot yet
be evaluated.

The crucial distinction is:

```text
assumption broken != theorem defeated
```

A broken assumption creates an obligation to construct and test the
replacement.

### 3.4 Name one load-bearing falsification test

The first test `T` must state:

- the object or computation to construct;
- the observable result;
- the acceptance threshold;
- the failure result that kills or sharply demotes the candidate;
- the person or tool capable of running it;
- the control case that must continue to work.

The test is registered before its result is known. Failure is counted as
research progress because it removes a typed candidate from the active set.

## 4. Candidate Admission Protocol

A candidate passes through eight stages.

### Stage 0: State the target claim

Write one sentence naming the observable, theorem boundary, or construction
the candidate addresses.

### Stage 1: Fill all six axes

No blank axes. New classes are allowed, but they require a definition and a
reason existing classes are insufficient.

### Stage 2: Declare axis couplings

Some choices are not independent. A causal-set substrate may make substrate
and causal order the same structure. A universality-class claim requires a
flow defining the equivalence relation. Couplings are constraints, not
clerical details.

### Stage 3: Draw the source-to-observation chain

Each arrow must name an operation. If a claim jumps directly from substrate
to observed physics, reviewers should treat the missing map as the primary
open problem.

### Stage 4: Map theorem assumptions

Record `preserved`, `broken`, or `unresolved` for each assumption. A reviewer
must be able to identify where disagreement lies without reconstructing the
whole proposal.

### Stage 5: Preserve a control case

A richer candidate should reproduce the established behavior it claims to
extend. A Type II operator-algebra proposal, for example, must preserve the
finite spectral-model controls that motivated it.

### Stage 6: Register the first kill test

The candidate is not admitted without a result that would count against it.

### Stage 7: Assign status

Recommended statuses are:

- `specified`: all fields filled, not yet tested;
- `testable`: test and runner are available;
- `supported`: first test passed;
- `weakened`: only a narrower claim survived;
- `rejected`: load-bearing test failed;
- `blocked`: test requires unavailable mathematics, data, or expertise.

### Stage 8: Record the result without rewriting the candidate

After a result, changes to any axis create a new candidate version. This
prevents a failed proposal from silently moving to a different class while
retaining the rhetorical identity of the original.

## 5. Testable Hypotheses About the Protocol

The framework is useful only if it outperforms simpler ways of documenting
theories.

### H1: Specification completeness

Independent reviewers identify fewer unresolved structural assumptions after
a proposal is converted to the six-axis format.

**Primary measure:** proportion of required fields receiving a concrete,
reviewer-accepted specification.

**Failure:** no improvement over a length-matched generic checklist.

### H2: Reviewer agreement

Reviewers agree more often about what class a candidate occupies and which
theorem assumptions it changes.

**Primary measures:** Krippendorff's alpha or Fleiss' kappa for axis labels and
assumption signatures.

**Failure:** agreement remains at chance or is no better than the controls.

### H3: Falsification yield

More proposals produce a concrete first test with an explicit killing result.

**Primary measure:** fraction of proposals for which blinded reviewers judge
the proposed test operational, load-bearing, and outcome-discriminating.

**Failure:** the protocol produces more tests only by accepting vague or
non-load-bearing checks.

### H4: Assumption localization

Reviewers identify fatal ambiguities and theorem mismatches faster.

**Primary measures:** time to first valid objection and number of document
sections inspected before locating it.

**Failure:** the six-axis format adds reading overhead without reducing search
time.

### H5: Candidate discriminability

Proposals that differ materially are less likely to be treated as one
undifferentiated family, while equivalent proposals are more likely to be
recognized as equivalent.

**Primary measures:** precision and recall on a gold-standard set of matched,
single-axis-ablation, and multi-axis-different candidate pairs.

**Failure:** axis labels create artificial distinctions or fail to separate
known differences.

### H6: Resistance to post hoc drift

After a negative result, candidate revisions are more likely to be recorded as
explicit axis changes rather than presented as though the original candidate
survived unchanged.

**Primary measure:** proportion of revisions with versioned axis deltas and a
new falsification test.

**Failure:** reviewers cannot reliably distinguish principled refinement from
goalpost movement.

## 6. Prospective Evaluation

### 6.1 Study design

Construct a benchmark corpus of 36 to 60 frontier-theory proposals drawn from
public preprints, research notes, and deliberately generated controls. The
corpus should include:

- established theories described incompletely;
- speculative proposals with genuine mathematical content;
- proposals known to violate a theorem assumption;
- proposals that only rename an existing structure;
- matched pairs differing on exactly one axis;
- incoherent proposals with hidden coupled-axis conflicts.

Each proposal is represented in three conditions:

1. original free-form description;
2. length-matched generic research checklist;
3. six-axis specification.

Reviewers are assigned by expertise and blinded to the study hypothesis where
practical. No reviewer scores the same candidate in more than one condition.

### 6.2 Reviewer tasks

For each candidate, reviewers answer:

1. What is the mathematical object being proposed?
2. Which theorem assumptions are preserved, broken, or unresolved?
3. What map produces the claimed observable?
4. What is the first load-bearing test?
5. What result would kill the candidate?
6. Is the candidate coherent enough to justify further work?

Reviewers also classify every proposed axis and identify any coupled-axis
constraint.

### 6.3 Outcomes

| Outcome | Operational definition |
| --- | --- |
| completeness | accepted concrete fields divided by required fields |
| agreement | inter-rater reliability on axes and theorem signatures |
| falsification yield | accepted kill tests divided by candidates |
| localization time | minutes to first expert-validated fatal ambiguity |
| discriminability | accuracy on matched and ablated candidate pairs |
| drift resistance | explicit versioned axis changes after negative results |
| review burden | completion time and reviewer-rated cognitive load |

### 6.4 Analysis plan

The primary comparison is six-axis versus the stronger of the two controls.
Use mixed-effects models with reviewer and candidate as random effects.
Report effect sizes and uncertainty intervals, not only significance tests.

The protocol is supported only if it improves at least four of the first six
outcomes without a large review-burden penalty. Reviewer agreement and
falsification yield are mandatory: a framework that looks complete but cannot
be applied consistently or produce decisive tests has failed.

### 6.5 Preregistered rejection conditions

Reject or substantially redesign the protocol if any of the following holds:

1. median axis-label agreement is below `0.60`;
2. falsification-test yield is not higher than the generic checklist;
3. reviewers place more than `25%` of material assumptions outside all six
   axes with no consistent mapping to `phi`, `Sigma`, `B`, or `T`;
4. review time increases by more than `50%` without gains in localization;
5. candidate authors routinely game the fields by relabeling claims without
   adding mathematical or operational detail;
6. the benchmark shows that fewer than six axes provide equal performance.

The last condition matters. Six is a hypothesis, not a sacred number.

## 7. Worked Examples

These examples demonstrate the protocol's use. They do not establish the
underlying physics.

### 7.1 Single-axis substrate modification

A Type II_1 spectral Standard Model candidate changes L1 while preserving the
finite observer, smooth pairing, Lorentzian order, specific-object emergence,
and no-loop assumptions.

Its value as a specification is immediate: disagreement can focus on whether
the operator-algebra extension preserves the finite Connes control case. The
first kill test checks KO-dimension, order-one structure, gauge extraction,
and anomaly cancellation. Failure on those controls kills the candidate
without requiring a debate about every other axis.

MIP*=RE supplies legitimate motivation for taking non-embeddable operator
algebras seriously, but it does not construct a particle-physics model [9].
The protocol keeps that distinction visible.

### 7.2 Coupled substrate and causal order

A Sorkin causal-set candidate occupies a locally finite partial order at L1
and L4. These entries are coupled because causal order is the substrate, not
an independent overlay [10].

The first kill test is not "does causal-set theory sound plausible?" It is
whether one can define a causal-set-native chirality invariant that is
isomorphism-invariant, behaves coherently under continuum approximation, and
contains information not already exhausted by its smooth shadow.

If the construction requires imported smooth orientation data, the candidate
has smuggled back the structure it claimed to replace.

### 7.3 Coupled emergence and coordination

An RG-universality candidate changes L5 from a specific microscopic object to
a universality class. That choice requires L6 to include RG flow, because the
flow defines the equivalence relation [8].

The first kill test asks whether the proposed chirality-bearing content is
actually fixed-point or relevant-operator data. If it depends on one
microscopic representative, the candidate collapses back to the
specific-object class.

### 7.4 Preliminary pairing-axis toy

A companion record-graph experiment varies only L3. Four observers inspect
the same causal graph at the same event with identical holder access, but
couple to different record channels. Their reconstructed temporal relations
differ because different propositions are visible:

```text
all channels:       A<C, B<C, D<C
gravity + EM:       A<C, B<C
gravity + social:   A<C, D<C
gravity only:       A<C
```

The local orders do not contradict the all-channel order, and observers agree
on shared content. This is not a claim about consciousness or a proof that
pairing generates spacetime. It is a worked demonstration that L3 can be an
independent experimental variable with testable consequences.

The same model distinguishes unconditional coupling from conditional
interpretive binding. That separation is useful because it prevents physical
constraint and semantic acceptance from being treated as one process.

## 8. What the Protocol Can and Cannot Establish

### 8.1 What it can do

- turn an informal proposal into a stable comparison unit;
- expose hidden changes of mathematical class;
- localize which assumptions of a theorem remain relevant;
- reveal coupled choices that make a candidate incoherent;
- require a source-to-observation map;
- produce a first result that can kill or weaken the proposal;
- preserve negative findings as reusable knowledge.

### 8.2 What it cannot do

- prove a candidate true;
- make an unavailable mathematical construction exist;
- convert analogy into mechanism;
- replace specialist review;
- infer physical reality from observer agreement;
- treat a broken theorem assumption as a successful evasion;
- guarantee that six axes are complete or independent.

### 8.3 The deepest failure mode

The protocol fails if it becomes a vocabulary for making speculation look
formal. A filled template is not evidence. Every label must cash out in a
mathematical object, operational map, or explicit unresolved obligation.

## 9. Publication and Replication Package

A publishable release should include:

1. this paper;
2. the blank six-axis candidate template;
3. at least three completed examples;
4. the theorem-assumption signature form;
5. the benchmark corpus and scoring rubric;
6. a preregistered analysis plan;
7. reviewer instructions;
8. all negative and ambiguous classifications.

The first publication should be positioned as a methods paper for
mathematical physics and theory evaluation. Claims about Geometric Unity or
any specific candidate should remain examples, not the evidentiary basis for
the protocol.

## 10. Conclusion

Frontier physics does not suffer from a shortage of imaginative proposals. It
suffers from a shortage of stable units for comparing them.

The six-axis protocol proposes one such unit. A candidate must declare its
substrate, observer, pairing, causal order, emergence class, and coordination
loop. It must then specify the map from source structure to observation, show
how relevant theorem assumptions are preserved or changed, and name one
result that would kill its first load-bearing claim.

The protocol's own claim is deliberately modest and testable:

> Typed six-axis specifications should make frontier theories easier to
> compare, criticize, and falsify than free-form descriptions or generic
> checklists.

That claim now has a prospective experiment and explicit rejection
conditions. The next step is not broader advocacy. It is to run the benchmark.

## Appendix A: One-Page Candidate Card

Every benchmark submission should fit the following form before supporting
material is consulted.

| Field | Required content |
| --- | --- |
| target claim | one observable, construction, or theorem boundary |
| L1 substrate | class, concrete object, literature anchor |
| L2 observer | capabilities, resource bounds, access assumptions |
| L3 pairing | channel or map coupling observer and substrate |
| L4 causal order | order structure and locality assumptions |
| L5 emergence | specific object, phase, class, fixed point, or attractor |
| L6 coordination | update, flow, consensus, feedback, or no loop |
| coupled axes | pairs or groups that cannot vary independently |
| `phi` | named source-to-observation operations |
| `Sigma` | preserved, broken, replacement, and unresolved assumptions |
| bridge claim | structure alleged to carry the target observable |
| control case | established behavior that must remain intact |
| first kill test | construction, measure, threshold, and killing result |
| runner | expertise, code, data, or apparatus needed |
| status | specified, testable, supported, weakened, rejected, or blocked |

## Appendix B: Benchmark Scoring Rubric

Each item receives `0`, `1`, or `2`.

| Score | Meaning |
| --- | --- |
| 0 | missing, circular, or purely rhetorical |
| 1 | named but underspecified, disputed, or not operational |
| 2 | concrete enough for an independent reviewer to check |

Score the following 16 items:

1. target claim;
2. L1 substrate;
3. L2 observer;
4. L3 pairing;
5. L4 causal order;
6. L5 emergence;
7. L6 coordination loop;
8. coupled-axis declarations;
9. source-to-observation map;
10. theorem-assumption signature;
11. bridge claim;
12. control case;
13. falsification-test construction;
14. measurable outcome and threshold;
15. explicit killing result;
16. feasible runner.

The completeness score is the sum divided by `32`. A candidate may not be
classified `testable` unless items 9 through 16 each score `2`. This prevents
strong descriptive detail on the six labels from compensating for a missing
map or non-falsifiable test.

For benchmark adjudication, two domain reviewers score independently. A third
reviewer resolves disagreements only after the original ratings are frozen.
The study reports both pre-adjudication reliability and final scores.

## References

1. E. Witten, "Search for a Realistic Kaluza-Klein Theory," *Nuclear Physics
   B* 186, 412-428 (1981).
   [doi:10.1016/0550-3213(81)90021-3](https://doi.org/10.1016/0550-3213(81)90021-3).
2. H. B. Nielsen and M. Ninomiya, "A No-Go Theorem for Regularizing Chiral
   Fermions," *Physics Letters B* 105, 219-223 (1981).
   [doi:10.1016/0370-2693(81)91026-1](https://doi.org/10.1016/0370-2693(81)91026-1).
3. D. S. Freed and M. J. Hopkins, "Reflection Positivity and Invertible
   Topological Phases," *Geometry & Topology* 25, 1165-1330 (2021).
   [arXiv:1604.06527](https://arxiv.org/abs/1604.06527).
4. J. Distler and S. Garibaldi, "There Is No 'Theory of Everything' Inside
   E8," *Communications in Mathematical Physics* 298, 419-436 (2010).
   [arXiv:0905.2658](https://arxiv.org/abs/0905.2658).
5. M. Mitchell et al., "Model Cards for Model Reporting," *Proceedings of
   FAT* 2019, 220-229.
   [arXiv:1810.03993](https://arxiv.org/abs/1810.03993).
6. T. Gebru et al., "Datasheets for Datasets," *Communications of the ACM*
   64(12), 86-92 (2021).
   [arXiv:1803.09010](https://arxiv.org/abs/1803.09010).
7. Center for Open Science, "Registered Reports."
   [cos.io/initiatives/registered-reports](https://www.cos.io/initiatives/registered-reports).
8. K. G. Wilson, "The Renormalization Group: Critical Phenomena and the Kondo
   Problem," *Reviews of Modern Physics* 47, 773-840 (1975).
   [doi:10.1103/RevModPhys.47.773](https://doi.org/10.1103/RevModPhys.47.773).
9. Z. Ji, A. Natarajan, T. Vidick, J. Wright, and H. Yuen, "MIP*=RE,"
   *Communications of the ACM* 64(11), 131-138 (2021).
   [arXiv:2001.04383](https://arxiv.org/abs/2001.04383).
10. R. D. Sorkin, "Causal Sets: Discrete Gravity," in *Lectures on Quantum
    Gravity* (2005).
    [arXiv:gr-qc/0309009](https://arxiv.org/abs/gr-qc/0309009).
11. J. M. Hellerstein and P. Alvaro, "Keeping CALM: When Distributed
    Consistency Is Easy," *Communications of the ACM* 63(9), 72-81 (2020).
    [arXiv:1901.01930](https://arxiv.org/abs/1901.01930).
12. M. J. Fischer, N. A. Lynch, and M. S. Paterson, "Impossibility of
    Distributed Consensus with One Faulty Process," *Journal of the ACM*
    32(2), 374-382 (1985).
    [doi:10.1145/3149.214121](https://doi.org/10.1145/3149.214121).

## Repository Artifacts

- [`../canon/six-axis-specification-protocol.md`](../canon/six-axis-specification-protocol.md)
- [`../specifications/six-axis/six-axis-template.md`](../specifications/six-axis/six-axis-template.md)
- [`../specifications/six-axis/examples/example-01-type-ii1-spectral-sm.md`](../specifications/six-axis/examples/example-01-type-ii1-spectral-sm.md)
- [`../specifications/six-axis/examples/example-02-sorkin-causal-set.md`](../specifications/six-axis/examples/example-02-sorkin-causal-set.md)
- [`../specifications/six-axis/examples/example-03-rg-universality-class.md`](../specifications/six-axis/examples/example-03-rg-universality-class.md)
