---
title: "Hardening ledger: Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32)"
status: "maximal revision complete; fresh adversarial saturation rerun pending"
updated: "2026-08-03"
---

# Hardening ledger

This ledger records the revision from the GU-facing v0.4 draft to the
standalone mathematical v0.5 candidate. It distinguishes actual repairs from
scope boundaries and does not promote the paper to post-ready status.

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
- 2,266 exact checks.
- Checks Lie-algebra membership, `±2` commutators, nonzero square-zero blocks,
  mutual zero products, linear truncation, and all dimensions.

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

## Remaining publication gate

The post-hardening ten-specialist internal audit found no new theorem defect. It
did identify and repair one test-quality issue: the mutual-product property
generator now guarantees equal ranks, so all 160 generated pair cases execute
rather than skipping rank-mismatched inputs.

Run a fresh hostile deep-research review against the v0.5 Markdown file as a
complete standalone submission. The post-ready gate passes only when any new
criticism is either fixed, shown already addressed, or identified as an honest
scope/trade-off rather than additional hardening potential. PDF, TeX, and Zenodo
engineering remain prohibited until Joe approves after that rerun.
