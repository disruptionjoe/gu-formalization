---
title: "Five-Minute Research Posture"
status: canon
doc_type: overview
updated_at: "2026-07-07"
---

# Five-Minute Research Posture

This repository is a Geometric Unity reconstruction program, not a proof of Geometric
Unity.

## Central Hypothesis

The working hypothesis is that Geometric Unity is substantially correct, and that the
missing mathematics can either be reconstructed, extended, or precisely shown not to
exist.

The hypothesis is not established. The repo is designed so either outcome is a success:
a rigorous GU reconstruction that derives new physics, or a precise mathematical account
of why such a reconstruction cannot exist.

The current framing separates two questions that are easy to conflate:

- **Force three:** whether bare GU/interior geometry derives the generation count with no
  additional selection datum. Current verdict: OPEN, and many native routes are blocked.
- **Unifying fit:** whether GU gives a better, lower-complexity account of the known
  classical/quantum structures than competing stories, with the generation count entering
  as a constrained source/boundary/selection datum. This remains live and is the larger
  project-level question.

An unforced generation count is not automatically a global negative verdict on GU. It is a
defect only if the imported datum is arbitrary, unconstrained, or more expensive than the
alternatives.

## What Is Canonical Here?

The canon is disciplined, but no longer neutral-map-first:

- The primary mission is GU reconstruction under a bold working hypothesis.
- The repo should optimize for information gain about whether GU is true.
- No-go results must be handled by their exact assumptions and known class exits.
- Candidate constructions must be specified before they are promoted.
- Type II1 spectral Standard Model work must preserve the finite Connes control case.
- Independent mathematical tools remain valuable secondary outputs.

See `RESEARCH-POSTURE.md`, `CANON.md`, and `canon/`.

## What Is Active Research?

Active research should prioritize constructive GU reconstruction: source-to-shadow maps,
exact GR recovery, QFT state extraction, matter/gauge selection, anomaly control,
generation-count machinery, measurement channels, and Lambda/dark-energy provenance.

Important independent theorem lanes still matter. One example is the signed-readout
boundary:

> monotone provenance can coexist with non-monotone, signed, phase-sensitive, or cancellation-bearing readout.

This reframes the CALM/Ginsparg-Wilson bridge as a boundary theorem rather than a direct equivalence. See `lab/active-research/`.

## What Is Exploratory?

Exploratory branches should not merely critique GU. When they hit an obstruction, they
should ask what stronger object, richer category, invariant, or reduction would have to
exist if GU were true. If the obstruction is intrinsic, formalize it and kill the branch.

## How To Help

Use `RESEARCH-POSTURE.md` for the philosophy, `NEXT-STEPS.md` for issue-sized tasks, and
`lab/roadmap/` for ranked research priorities.
