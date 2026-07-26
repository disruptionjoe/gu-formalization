---
title: "Graded Exterior-Bundle 14D Comparator"
artifact_type: exploration
status: exploration
updated_at: "2026-07-26"
depends_on:
  - "explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md"
  - "GEOMETER-VS-PHYSICS-OBJECTS.md"
---

# Graded Exterior-Bundle 14D Comparator

## Status and verdict boundary

This file turns the proposed \(4+6+4\) exterior-algebra reading into a
conditional GU comparator and work program. It does **not** identify the
proposal with GU's \(Y^{14}\), make its four trivector components physical
access dimensions, replace \(\operatorname{Met}(X^4)\), or move a claim,
canon, source-action, priority, or research verdict.

The immediate result is a type correction:

> A rank-14 fibre and a 14-dimensional total space are different objects.

That correction creates two exterior candidates, only one of which is even
dimensionally comparable to GU's total-space construction.

## 1. Three objects that the number 14 can name

Let \(V\) be a four-dimensional real vector space.

| object | definition | fibre rank | base dimension | total dimension |
|---|---|---:|---:|---:|
| Graded rank-14 object | \(G(V)=\Lambda^1V^*\oplus\Lambda^2V^*\oplus\Lambda^3V^*\) | \(4+6+4=14\) | none, or 4 after bundling | 14 as a vector space; 18 as a bundle over \(X^4\) |
| Exterior total-14 comparator | \(Y_{\mathrm{gr}}=\Lambda^2T^*X\oplus\Lambda^3T^*X\) | \(6+4=10\) | 4 | 14 |
| GU-native metric bundle | \(Y_{\mathrm{GU}}=\operatorname{Met}_{1,3}(X)\subset S^2T^*X\) | 10 | 4 | 14 |

Consequently, the expression

\[
\Lambda^1T^*X\oplus\Lambda^2T^*X\oplus\Lambda^3T^*X
\]

is a rank-14 bundle over \(X^4\) whose total space has dimension \(18\).
It is not an alternative 14-dimensional total space.

If the intended count is instead

\[
4+6+4=14
\]

with the first four dimensions supplied by the base \(X^4\), the correctly
typed exterior comparator is

\[
Y_{\mathrm{gr}}
  =\Lambda^2T^*X\oplus\Lambda^3T^*X,
\]

not a second copy of \(\Lambda^1T^*X\) in the fibre.

GU's native object remains different. Its rank-10 fibre is the open
homogeneous space of Lorentzian symmetric bilinear forms inside
\(S^2T^*X\), not a vector-bundle identification with exterior forms.

## 2. Exact naturality obstruction

Equal rank does not produce a natural bridge:

\[
S^2V^*\not\cong
\Lambda^2V^*\oplus\Lambda^3V^*
\quad\text{as natural \(GL(V)\)-representations.}
\]

There are two quick exact checks.

### 2.1 Central-weight check

For a central scaling \(aI\in GL(V)\), the contragredient action has weights

\[
\begin{aligned}
S^2V^* &: a^{-2},\\
\Lambda^2V^* &: a^{-2},\\
\Lambda^3V^* &: a^{-3}.
\end{aligned}
\]

Any \(GL(V)\)-equivariant map from the \(\Lambda^3V^*\) summand to
\(S^2V^*\) must intertwine incompatible central weights and is therefore
zero. An isomorphism cannot discard the four-dimensional summand.

### 2.2 Young-symmetry check

After complexification, \(S^2V^*\) and \(\Lambda^2V^*\) are distinct
irreducible polynomial representations, with symmetric and antisymmetric
Young types. Their equivariant Hom space is zero. Thus the remaining
six-dimensional summand cannot supply the bridge either.

**Exact result:** no canonical, target-independent \(GL(4)\)-equivariant
isomorphism turns the exterior rank-10 fibre into the GU metric fibre.
Any bridge must reduce the structure group or add further fields.

## 3. What the second four can mean without ontology

There is a canonical determinant-twisted duality

\[
\Lambda^3V^*\cong V\otimes\Lambda^4V^*,
\]

given by contraction into a top form. It supports a conservative
interpretation: trivectors naturally encode oriented hyperplane or
codimension-one data, subject to the determinant twist.

Stronger identifications cost structure:

- a chosen volume form trivializes \(\Lambda^4V^*\);
- a metric identifies \(V\) with \(V^*\);
- a metric plus orientation defines the Hodge map
  \(*:\Lambda^3V^*\to\Lambda^1V^*\);
- a time orientation, spin structure, connection, or observer field adds
  still more.

Therefore the four trivector coordinates are not presently derived physical
access dimensions. If Hodge duality is used to assign that meaning, the
metric and orientation have already been supplied. That is circular when the
purpose is to derive those structures.

## 4. Closure obstruction

The truncated graded space

\[
\Lambda^1V^*\oplus\Lambda^2V^*\oplus\Lambda^3V^*
\]

is not a subalgebra of \(\Lambda^\bullet V^*\):

\[
\Lambda^1\wedge\Lambda^3\subseteq\Lambda^4,
\qquad
\Lambda^2\wedge\Lambda^2\subseteq\Lambda^4.
\]

The full exterior algebra in four dimensions has dimension

\[
1+4+6+4+1=16.
\]

The proposed 14-dimensional truncation deletes precisely the scalar and top
form. Under a Clifford product, grades 0 and 4 are also regenerated, and the
Clifford product itself already requires a metric.

Any dynamical proposal must therefore state one of:

1. the missing grades are retained as a boundary, source, or coefficient
   sector;
2. the product is followed by a declared projection;
3. a quotient makes the truncation closed; or
4. the object is only a graded vector space and no algebra closure is claimed.

The reason for excluding grades 0 and 4 must be derived rather than inferred
from the desired count 14.

## 5. Structure-cost ledger

| desired move | minimum extra datum | risk introduced |
|---|---|---|
| \(\Lambda^3\leftrightarrow V\) | volume/top-form trivialization | orientation or density is supplied |
| \(\Lambda^3\leftrightarrow\Lambda^1\) | metric and orientation | target geometry may be smuggled in |
| exterior fibre \(\to S^2V^*\) | noncanonical field or structure-group reduction | bridge becomes model data |
| Clifford dynamics | nondegenerate metric | metric is antecedent |
| covariant comparison across points | connection | transport law is antecedent |
| observer/access semantics | observer, instrument, boundary, decoder | semantics are not geometric consequences |

## 6. GU work program

The exterior candidate remains worth keeping because it creates sharp,
inexpensive gates.

### Gate G1 — type

Declare whether the candidate is:

- a 14-dimensional graded vector space;
- a rank-14 bundle with 18-dimensional total space; or
- the rank-10 exterior fibre of a different total-14 bundle.

Failure to declare this stops the attempt.

### Gate G2 — naturality

Supply an explicit bundle map

\[
\Phi:\Lambda^2T^*X\oplus\Lambda^3T^*X
\longrightarrow S^2T^*X
\]

and state its equivariance group. The exact \(GL(4)\) obstruction above means
that any nonzero candidate must expose the extra structure that makes it
possible.

### Gate G3 — closure

Specify the product or differential, show where grades 0 and 4 go, and prove
closure or name the controlled failure. Do not use a Clifford product while
claiming that the metric was derived by the same construction.

### Gate G4 — source/action

Construct a program-native action on the correctly typed object that selects
sections or configurations without importing the target metric, observer, or
held-out result.

### Gate G5 — physical bridge

Produce at least one invariant or held-out physical consequence not already a
relabeling of metric, volume, orientation, differential-form, or standard
gauge data.

## 7. Kill, survival, and reopening conditions

The proposal is killed as a replacement ontology if:

- it relies only on the matching number 14;
- its bridge is non-natural and no physical selector chooses it;
- its access semantics are assigned rather than derived;
- its grade-3 sector is fully Hodge-absorbed after matching admitted metric
  and orientation data; or
- it generates no invariant or held-out consequence.

It survives as useful mathematical infrastructure if it supplies a
target-independent structure-group reduction, a closed graded dynamics, or a
source-selected bridge. It becomes physically interesting only if that
structure changes a held-out observable or reconstruction result.

No local computation is warranted yet: the first decision-changing results
are exact representation and algebra facts already given above.

## 8. Ownership

GU owns:

- the dimensional and bundle-type comparison;
- the naturality and structure-group-reduction problem;
- the product/action closure problem; and
- any bridge to \(Y_{\mathrm{GU}}=\operatorname{Met}(X)\).

Dynamic Unity owns whether the grades independently reconstruct
observer-accessible time, geometry, fields, or capability. The DU work
contract is
`../../../dynamic-unity/explorations/graded-observer-geometry-4-6-4-work-program-2026-07-26.md`.
