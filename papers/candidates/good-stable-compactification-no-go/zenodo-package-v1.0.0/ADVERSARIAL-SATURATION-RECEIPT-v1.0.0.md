---
title: "Adversarial saturation receipt: Compact-Image Obstructions v1.0.0"
date: "2026-08-03"
manuscript_version: "1.0.0"
manuscript_sha256: "406bbf731ab1f58c6de097f25b59695ee59c2217b1919745738d52c22a6e39be"
status: "pass; zero actionable hardening remaining"
---

# Adversarial saturation receipt

This receipt records two final hostile passes against the complete manuscript
and paper-specific evidence tree. It is a consolidated, AI-assisted internal
review, not a claim of independent human peer review. It follows the external
hostile-specialist report whose eleven actionable findings were repaired in
v0.6 and the subsequent ten-lens final pass whose four small repairs were
incorporated into v1.0.0.

The exact reviewed manuscript has SHA-256:

```text
406bbf731ab1f58c6de097f25b59695ee59c2217b1919745738d52c22a6e39be
```

## Gate A: hostile theorem and specialist pass

| attack surface | adversarial question | disposition |
|---|---|---|
| theorem quantifiers | Can a summary be read without unbounded represented flow, real diagonalizability where used, the correct extremal sign, or a detected nonzero nilpotent witness? | Pass. The abstract, result table, theorem, Corollary 7, and conclusion carry the required hypotheses. |
| vector versus line stabilization | Does the extremal argument silently prove only line preservation? | Pass. The sign-matched nilpotent algebra annihilates the chosen vector; exponentiation fixes it pointwise. |
| representation smoothness | Is `R(exp tX) = exp(t dR(X))` used without an adequate representation hypothesis? | Pass. All finite-dimensional group representations are declared continuous, hence smooth. |
| compactness predicate | Is abstract source-group noncompactness substituted for noncompact represented closure? | Pass. Every conclusion is stated for the closure of the tested image, and faithfulness is explicitly stronger than necessary. |
| quaternionic conventions | Can right-versus-left action or multiplication order reverse the block identities? | Pass. Module side, left matrix action, conjugate transpose, and real-linear endomorphisms are typed; two independent exact implementations confirm the signs and products. |
| parabolic identification | Is the `|1|` grading merely asserted or assigned the wrong isotropic-plane stabilizer? | Pass. The basis change, upper/diagonal/lower blocks, preserved first isotropic plane, and rescaled degrees are written explicitly. |
| compact reducer | Does noncommutation get overstated as pure oddness or as a universal fixed-frame Cartan result? | Pass. Only a nonzero odd component is inferred in general; pure oddness and Cartan implementation require added hypotheses. |
| invariant majorant | Does finite-dimensional positivity borrow an undeclared infinite-dimensional Krein theorem? | Pass. The local meaning of majorant, topology, functional calculus, equivariance, self-adjointness, positivity, and converse are all explicit. |
| generality versus title | Does extending the block calculation to `Sp(n,n)` make the `Sp(32,32)` title false? | Pass. The title is a truthful specialization; Corollary 7 states the stronger family result without changing the paper's fixed numerical application. |
| falsification pressure | Is a tempting stronger claim left available by rhetoric? | Pass. Split-plus-elliptic, rank-one split-torus, charged-vector, and tilted-compact counterexamples delimit the theorem. |

Gate A result:

```text
fatal=0
major=0
minor_actionable=0
actionable_hardening_remaining=0
```

## Gate B: hostile editor, literature, and reproducibility pass

| attack surface | result |
|---|---|
| title and abstract | The title names compact-image obstructions, not physical compactification or stability; the abstract states both the algebraic result and the excluded physical claims. |
| novelty positioning | Direct literature recheck confirms that parabolic gradings and real-simple inner ideals are prior art. The manuscript claims only a scoped synthesis, explicit fixed-grading calculation, correction of overstatements, and diagnostic taxonomy. |
| bibliography | Author/title/year/venue/DOI records were rechecked. DOI endpoints resolve; automated 403 responses from some publisher pages are access-policy responses, not missing identifiers. |
| supplement visibility | Every artifact named in the paper-specific evidence map exists. The manuscript assigns no weight to unavailable supplements and requires the complete tree in an archive. |
| executable evidence | SageMath passes 2,721 exact checks; the independent Python property suite passes 400 generated examples plus deterministic controls; the seven-declaration Lean kernel compiles with only disclosed standard axioms. |
| frozen source | The Markdown passes a strict Pandoc parse, delimiter and placeholder scans, and `git diff --check`. The evidence manifest is regenerated after the v1.0.0 edits. |
| AI-use transparency | A dedicated disclosure names substantial AI use in drafting, literature discovery, formalization and computational support, and adversarial review while assigning full responsibility to the author. |
| claim boundary | No external replication, full-paper formalization, physical Hilbert space, dynamical vacuum, non-extremal classification, or infinite-dimensional theorem is claimed. |

Gate B result:

```text
fatal=0
major=0
minor_actionable=0
actionable_hardening_remaining=0
```

## Remaining criticisms and decision

The surviving criticisms are known scope choices rather than hardening work:

- classify non-extremal and mixed-weight stabilizers;
- replace finite-dimensional invariant majorants with a rigorously specified
  infinite-dimensional stability framework;
- supply a model-specific physical dictionary and dynamical construction; or
- obtain independent external replication or conventional peer review.

Each would create successor work or a different theorem. None is needed to
make the present finite-dimensional statement accurate, reproducible, and
useful on its stated domain.

## Verdict

```text
adversarial_saturation_verdict=pass
publication_recommendation=build version-bound release package
public_posting_authorized=false
```
