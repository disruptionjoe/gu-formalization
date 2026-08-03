---
title: "Hardening ledger: Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32)"
status: "v1.0.0 adversarially saturated; post-ready"
updated: "2026-08-03"
---

# Hardening ledger

This ledger records the revision from the GU-facing v0.4 draft through the
standalone mathematical v0.5 candidate, the hostile-specialist-hardened v0.6
candidate, and the final v1.0.0 post-ready gate. It distinguishes actual
repairs from scope boundaries.

## Final v1.0.0 saturation gate

The final ten-lens pass produced four small, fixable items. Version 1.0.0 now:

- states that `Sp(n,n)` is connected real reductive and that its defining
  real action is faithful;
- quantifies the finite vector-family and smooth-representation clauses in
  Corollary 7;
- states that the quaternionic block derivation works for every `n >= 1`,
  while retaining `n = 32` as the titled numerical specialization; and
- separates maximal/positive and minimal/negative extremal rows in the result
  table; and
- carries an explicit generative-AI-use and author-responsibility disclosure
  consistent with the repository's prior public-paper standard.

Two fresh hostile gates then attacked the exact theorem and the
publication/reproducibility surface. Both returned
`fatal=0`, `major=0`, `minor_actionable=0`, and
`actionable_hardening_remaining=0`. The exact disposition is bound to the
v1.0.0 manuscript SHA-256 in
`review/adversarial-saturation-receipt-v1.0.0.md`.

## Second hostile-specialist intake

The 2026-08-03 specialist report returned `fatal=0`, `major=2`, `minor=8`,
`actionable_hardening_remaining=11`, and a saturation verdict of `fail`. Its
SHA-256 is
`f6ef374c8ad43ca3d3de4f1185be58292aeb0315aa2ff0e46a25793dbc4da08e`.
The complete item-level disposition is recorded in
`review/hostile-specialist-disposition-2026-08-03.md`.

The core theorem and every independent quaternionic block, sign, product, and
dimension calculation survived. The two major findings were:

1. summaries of the extremal leg omitted the real-diagonalizable `dR(Z)` and
   sign-specific represented-nilpotent-witness hypotheses; and
2. the one-file review upload did not include the repository supplements named
   by the manuscript.

Version 0.6 repairs the first defect on every public theorem surface. The
second is resolved at repository grade because every named artifact exists,
is versioned, and is checksum-locked; the manuscript now also says explicitly
that a manuscript-only circulation gives those artifacts no evidentiary
weight, and that an archival package must contain the complete evidence tree.

Additional v0.6 hardening includes sign-specific theorem clauses, smoothness
and topology conventions, a hypothesis-minimal neutrality definition, a
topology-precise finite-dimensional majorant statement, a complete
fundamental-symmetry calculation, right-quaternionic/left-matrix conventions,
the real dimension of the tested module, an exact isotropic-basis derivation of
the `|1|` parabolic grading, more direct prior art, and consolidated scope
language.

## Hostile-report intake

The attached hostile-but-fair deep-research report returned:

| classification | count |
|---|---:|
| fatal | 0 |
| major actionable | 4 |
| minor actionable | 12 |
| already addressed | 6 |
| deliberate scope/trade-off | 4 |
| invalid criticism | 4 |

The central compact-image theorem survived. All sixteen actionable items are
now disposed below.

## Major repairs

| report finding | v0.5 disposition |
|---|---|
| One nonzero real eigenvalue was incorrectly promoted to full hyperbolicity. | The theorem now separates unbounded represented flow, sufficient for parts 1–2, from real diagonalizability of `ad(Z)`, required for part 3. A mixed split/elliptic counterexample explains why. |
| Continuous vector neutrality was conflated with a discrete operator grading. | `A_Z = exp(RZ)` invariance is defined for vectors. Discrete parity is defined separately on `End(E)` only when `z²=1`. No arbitrary vector representation is called chirality-safe. |
| The Sp(32,32) nilpotent-radical assertion was not demonstrated. | Section 6 now derives the full `-2,0,+2` decomposition, the exact block forms, dimensions `2080+4096+2080=8256`, mutual zero products, square-zero nilpotence, and unbounded linear exponentials. |
| The GU application was not self-contained. | The W235/channel-D/channel-S census and the Clifford reconstruction dictionary were removed entirely. The paper is now a standalone matrix/Lie-theoretic result; model-specific application requires a separate future dictionary. |

## Minor repairs

| report finding | v0.5 disposition |
|---|---|
| Fundamental-symmetry converse omitted conditions. | Equivariance, involutivity, eta-self-adjointness, and strict positivity are all explicit. |
| “Majorant” could imply infinite-dimensional topology. | Defined as finite-dimensional shorthand; Bognár added. |
| Common vector representations were inconsistently typed. | `R_i`, `V_i`, and `w_i` are defined and exponentiation is shown in the proof. |
| Vector and line stabilizers could be confused. | A dedicated remark explains why the nilpotent subgroup fixes the vector pointwise. |
| A generic involution was casually called a Cartan implementer. | Normalization and implementation are now named as additional hypotheses; the compactness corollary does not require them. |
| Eigenspaces were called restricted-root spaces. | They are called `ad(Z)` eigenspaces and, when applicable, sums of restricted-root spaces. |
| Clifford sign convention/application dictionary was undefined. | The Clifford dictionary was removed with the GU application and is no longer a paper premise. |
| Knapp citation mixed editions. | The second edition is cited by its correct 2002 ISBN; the first-edition DOI was removed. |
| Sedano-Mendoza was cited only as an arXiv preprint. | Updated to *Journal of Lie Theory* 29 (2019), 755–786, DOI 10.5802/jolt.1077. |
| Citation support was too broad. | Krein, Cartan/restricted-root, highest-weight, orbit, and quaternionic-group claims now have direct references; the decisive concrete calculation is written out. |
| Regression pass counts were unavailable to a manuscript-only reviewer. | The six old development regressions are no longer evidence in the paper. A paper-specific, locked, exact reproduction capsule is included. |
| Title and abstract outran the predicate; “Two distinctions” introduced three. | Replaced by the mathematical compact-image title, rebuilt abstract, and four explicit distinctions. |

## Additional mechanized hardening

### Exact SageMath certificate

- Rational quaternion arithmetic only.
- 2,721 exact checks.
- Checks Lie-algebra membership, `±2` commutators, nonzero square-zero blocks,
  mutual zero products, linear truncation, the isotropic basis change and
  upper/diagonal/lower block forms, and all dimensions.

### Independent property certificate

- Separate integer-quaternion implementation; no Sage or NumPy code sharing.
- 400 deterministic Hypothesis-generated examples plus dimension controls.
- Planted wrong-sign and “noncommuting implies purely odd” mutants are rejected.

### Lean kernel

Seven paper-facing declarations compile under the pinned Lean/mathlib toolchain.
The receipt exposes only Lean's standard `propext` and `Quot.sound` dependencies;
there are no project-specific axioms or admitted declarations. The formal scope
is narrow and is stated identically in the manuscript and verification receipt.

## Remaining honest boundaries

- The theorem does not cover non-extremal or mixed-weight vectors.
- It does not build a physical Hilbert space, vacuum, source action, or
  interacting dynamics.
- It does not identify continuous vector neutrality with physical chirality.
- Infinite-dimensional domains and metric operators remain outside scope.
- Proposition 1 and the full real-reductive theorem are written proofs, not
  Lean-formalized results.
- External replication is not required, but none is claimed.

## Publication gate result

The v1.0.0 gate is complete. The remaining objections ask for successor work:
a non-extremal classification, an infinite-dimensional theorem, or a physical
application dictionary. They do not expose an omitted proof, citation,
qualification, test, or wording repair in the present paper. Joe authorized
release-package engineering after this result; public posting remains separate.
