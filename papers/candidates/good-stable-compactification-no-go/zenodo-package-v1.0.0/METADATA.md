# Proposed Zenodo metadata

## Title

```text
Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32): Neutral, Grading-Even, and Extremal Order Parameters
```

## Core fields

- **Upload type:** Publication / Preprint
- **Creator:** Joseph Hernandez
- **Affiliation:** Independent Researcher
- **Email:** joe@disruptionjoe.com
- **ORCID:** Not supplied; omit rather than infer
- **Publication date:** 2026-08-03
- **Version:** 1.0.0
- **Language:** English
- **Primary license:** Creative Commons Attribution 4.0 International
  (`CC-BY-4.0`)
- **Bundled code license:** MIT
- **Funding:** None declared
- **Communities:** None preselected

## Description

```text
Let a connected real reductive group G act faithfully on a finite-dimensional real vector space E, and let A_Z be a one-parameter subgroup with unbounded represented image. This paper isolates three compact-image obstructions for stabilizers of order parameters. A vector fixed by A_Z retains the entire unbounded flow in its stabilizer. An operator commuting with the infinitesimal generator retains the same flow in its centralizer. Under real-diagonalizability and an explicitly detected sign-matched nilpotent witness, a maximal or minimal Z-weight vector retains a corresponding unipotent one-parameter subgroup. In each case the represented stabilizer has noncompact closure and therefore preserves no positive-definite inner product on E.

For Sp(32,32), the hypotheses are verified directly in a quaternionic matrix model. The grading has adjoint eigenvalues -2, 0, and 2; the two nonzero eigenspaces each have real dimension 2080, are abelian, and consist of square-zero matrices. The same block calculation works for Sp(n,n) for every n >= 1. The paper also separates continuous vector neutrality from discrete operator parity and proves that noncommutation of a compact-reducing involution does not by itself imply pure oddness.

The contribution is a scoped synthesis, explicit fixed-grading calculation, and falsifier taxonomy, not a new classification theorem for real Lie groups. It is finite-dimensional and algebraic. It does not establish a physical Hilbert space, vacuum, compactification, interacting unitarity, or dynamical stability. The written proofs are accompanied by exact SageMath and property-based certificates and a narrow Lean 4 kernel, with their scope and dependencies disclosed.
```

## Keywords

- compact-image obstruction
- Sp(32,32)
- quaternionic symplectic group
- hyperbolic grading
- parabolic grading
- extremal weight
- invariant inner product
- Krein space
- stabilizer
- Lean 4

## Related resources

Enter the repository as a related work/resource:

- **Identifier:** `https://github.com/disruptionjoe/gu-formalization`
- **Relation:** Is supplemented by
- **Resource type:** Software

Record the exact reviewed source revision in the description or notes if the
form permits a second resource:

- **Identifier:** `https://github.com/disruptionjoe/gu-formalization/tree/507cd21bb2edf72db96d55ba3cef3f9f7e23ff26/papers/candidates/good-stable-compactification-no-go`
- **Relation:** Is supplemented by
- **Resource type:** Other

## Depositor notes

Use `compact-image-obstructions-sp32-32-v1.0.0.pdf` as the primary article and
default preview. Do not mint or insert a DOI before Zenodo assigns one. The
record-level license should be `CC-BY-4.0`; `LICENSE-CODE.md` preserves MIT
terms for the bundled Lean and Python code.
