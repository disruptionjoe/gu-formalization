---
title: "Disposition of the hostile specialist referee report"
date: "2026-08-03"
manuscript_version: "0.6.0-hardening"
status: "all current-paper hardening applied; clean hostile rerun required"
---

# Hostile specialist report disposition

The report reviewed the v0.5 Markdown manuscript as a single uploaded file. It
reported no fatal finding, two major findings, eight minor findings, one
editorial finding, and eleven actionable changes. Its independent calculation
reproduced the Lie-algebra block form, all commutator signs, mutual zero
products, dimensions, compact centralizer, and parity distinctions.

Source report SHA-256:
`f6ef374c8ad43ca3d3de4f1185be58292aeb0315aa2ff0e46a25793dbc4da08e`.

## Item-level disposition

| finding | v0.6 disposition |
|---|---|
| Extremal summaries omitted indispensable hypotheses. | Repaired in the abstract, result table, strongest-conclusion block, Corollary 7, and conclusion. Every summary now names real diagonalizability of `ad(Z)` and `dR(Z)`, the corresponding sign, and a witness whose defining image is nonzero nilpotent. The split-torus counterexample now shows why `ad`-hyperbolicity alone is insufficient. |
| Referenced supplements were absent from the one-file review upload. | Resolved as a packaging condition, not a mathematical defect. All named files exist in the repository, are versioned, reproducible, and checksum-locked. The manuscript now says that they receive no evidentiary weight when the Markdown circulates alone and that the full tree is mandatory in an archival submission. |
| Theorem 3(3) required witnesses of both signs. | Split into maximal/positive and minimal/negative clauses. Each clause assumes only the sign it uses. |
| Smoothness and matrix topology were implicit. | All representations are now declared finite-dimensional continuous, hence smooth, real Lie-group representations; Euclidean matrix topology is explicit. |
| Neutrality unnecessarily required diagonalizability. | Neutrality is now defined by `dR(Z)w=0` for any smooth representation. Diagonalizability appears only when the weight decomposition and extremality are introduced. |
| “Majorant” wording was topology-loose. | Replaced by an exact finite-dimensional topology/continuity statement, with rescaling for a conventional domination inequality and a narrow local definition. |
| Fundamental-symmetry bridge skipped algebra. | Added the `T^{-1}AT=A` derivation, functional-calculus equivariance, eta-self-adjointness, positivity, converse symmetry, and converse invariance. |
| Quaternionic side and endomorphism conventions were implicit. | The paper now specifies a right quaternionic module, left matrix action, conjugate transpose, real-linear `End(E)`, and `dim_R E=256` at `n=32`. |
| Restricted-root/parabolic bridge was compressed. | Added the exact `S`-basis calculation, `g_0 ≅ gl(n,H)`, upper/diagonal/lower block grading, isotropic-plane parabolic, abelian nilradical, and the `|1|`-grading normalization. Both executable certificates now check the basis-change identities. |
| Literature descriptions were too broad. | Added Čap–Slovák and Draper–Meulewaeter; added chapter/section pinpoints; narrowed Khare and Richardson–Slodowy to contextual roles. |
| Scope caveats were repetitive. | Consolidated the interpretation and limitation material into one compact boundary section and shortened the conclusion without deleting any load-bearing qualification. |

## Cross-audit additions

The report was reconciled with the preceding six-point specialist audit. That
cross-audit also produced the following repairs:

- the abstract indefinite form is connected explicitly to the concrete
  quaternionic form by
  `eta(x,y)=Re(x* beta y)` and
  `h_P(x,y)=eta(x,Py)=Re(x*y)>0`;
- “frame-independent” is replaced by “reducer-independent relative to fixed
  `z`”;
- nonreal eigenvalues are correctly located in the complexified spectrum, with
  real rotation blocks named;
- the unboundedness literature summary now requires a nonzero real weight in
  the tested representation;
- the title of Knapp’s book is punctuated as *Lie Groups: Beyond an
  Introduction*.

## Residual classification

No known counterexample remains inside the written hypotheses. The remaining
criticisms in the report are disclosed scope choices: finite dimensionality,
the stronger-but-clean global diagonalizability assumption, no classification
of all stabilizers, no non-extremal theorem, and no physical or GU application.
Those would be successor papers or different theorems, not unfinished
hardening of this note.

This disposition does not itself satisfy the repository’s adversarial
saturation rule. A clean hostile rerun against v0.6 and the complete supplement
set remains required before post-ready promotion.
