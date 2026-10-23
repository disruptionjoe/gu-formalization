---
title: "K1979: Full symmetric first jets and the multicoordinate integrability boundary"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1979_multicoordinate_symmetric_pairing.py
  - tests/channel-swings/k1979_multicoordinate_symmetric_pairing_probe.py
---

# K1979: Full symmetric first jets and the multicoordinate integrability boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: full symmetric first-jet rank, identity-value witness, and complete small-algebra integrability obstruction
carrier: fixed real raw1920 section with 128 core coordinates LAYER=toy CHIRALITY=N/A
pairing: arbitrary real symmetric spinor matrix Q and eta_k Q ON=raw_spinor_and_vector_spinor
real_structure: real Cl(7,7); no source bar or star identification
grading: actual Clifford volume eigenspaces, not observed chirality
action_owner: repository-construction -- specified raw lower-return equation
target: multidirectional pairing compatibility on the unchanged raw core MAP-TYPE=intertwiner
```

## 1. The full first-jet test differs from the one-variable ODE

Keep the exact raw injection J, coefficients Omega and mass target T of
[K1976](k1976-general-pairing-transport-2026-10-23.md), including eta_k=+1
for k<7 and -1 otherwise. Only dependence on coordinates changes. The equation is

    sum_(k=0)^13 eta_k (partial_k Q) J_k = R_epsilon(Q),
    R_epsilon(Q)=sum eta_k Omega_k^T Q J_k - epsilon Q T.       (1)

Here Q is a symmetric128x128 real matrix field. J has15 components in the
stored section: only its FIRST14 are derivative directions. Its last scalar
component is not a fifteenth coordinate. We explicitly corrected that indexing
mistake in an initial check before accepting the result.

At one point, the symmetric gradients H_k are independent unknowns. The map

    B:(Sym_128)^14 -> Mat_128, B(H)=sum eta_k H_k J_k           (2)

has EXACT rank 16382, nullity 99202 and a two-dimensional cokernel. The report
stores a basis Z_1,Z_2 of that cokernel. Both have64 nonzero rational entries
and disjoint support. The full compatibility condition is therefore exactly

    <Z_1,R_epsilon(Q)>=<Z_2,R_epsilon(Q)>=0.                   (3)

Both conditions hold at Q=I for both epsilon signs. The report supplies actual
symmetric H_0,...,H_13 with B(H)=R_epsilon(I), checked entry by entry against
an independently rebuilt raw section and Clifford coefficients. Thus the
one-variable positive-definiteness exclusion DOES NOT extend to a full
multicoordinate FIRST-JET exclusion.

This does not produce a positive pairing field satisfying(1) on an open set.
The first jet is necessary data, not a PDE existence theorem.

## 2. Exact rank and witness construction without a dense matrix

Each J_k is a monomial matrix. For the diagonal symmetric basis E_ii,
H J_k contributes one coordinate; for E_ij+E_ji it contributes two. Regard
output coordinates as graph vertices and these sparse columns as weighted
edges (single-coordinate columns are anchors). A spanning tree determines
all potential dual weights from one root weight. An anchor or inconsistent
cycle eliminates that remaining weight. Exactly two unanchored consistent
components survive. This proves the entire cokernel count, not a sampled rank.

For a given right side, its dual sum must vanish on those two components.
On every other component, one anchor/cycle column pays the total dual sum.
Subtract it, then solve each tree from leaves to root. This gives the stored
right inverse on the compatible image and the explicit symmetric jets.
The independent probe uses weighted union-find relations for the DUAL equations,
not the producer's spanning-tree solve. It separately checks

    Sym(Z J_k^T)=0 for EVERY k<14.

Together with two independent Z and the complete component census this certifies
rank 16382. The signed eta factors do not change the cokernel but are retained
in the actual right-side and jet identity.

## 3. Executed integrability test: the small symmetric algebra still fails

Let V and S be K1976's actual symmetric involutions, with VS=-SV. Restrict
Q=aI+bV+cS; this is the symmetric part of its four-dimensional invariant algebra.
Allow a,b,c to depend on ALL 14 coordinates, rather than assuming x0-only.
The42 derivative columns are independent. Appending the three value columns
R(I),R(V),R(S) increases rank by exactly one. Exact elimination gives

    a=r_epsilon b,
    r_-=-14253/22127, r_+=-3123/6833.                         (4)

All transverse derivatives of a,b,c vanish. The only possible derivative data
are, at x0,

| epsilon | c' per unit b | a' per unit c | b' per unit c |
| --- | --- | --- | --- |
| -1 | -13335209/32039896 | -9777/5792 | 14843/5792 |
| +1 | 13335209/9894184 | -1089/5792 | 363/5792 |

Differentiate(4). In either row, a'-r b' is a NONZERO multiple of c,
so c=0. Then c'=0 and the nonzero first column forces b=0, hence a=0.
Therefore every C1 symmetric solution of(1) in this small algebra is ZERO,
even with unrestricted coordinate dependence. The proof requires only C1,
not an assumption about commuting second derivatives.

Already at value level |r|<1 excludes definiteness: the eigenvalues of
Q are a+-sqrt(b^2+c^2), since (bV+cS)^2=(b^2+c^2)I. The stronger derivative
argument excludes nonzero indefinite solutions in the same algebra as well.
The full identity-value jet in section1 necessarily uses additional matrix
directions; it is not a counterexample to this small-algebra theorem.

## 4. A positive affine jet is still not an integrated solution

The stored H_k define Q_aff(x)=I+sum x_k H_k. Put
B_H=sum ||H_k||_infinity. For max|x_k|<=1/(2B_H), symmetry and the
operator-norm bound give Q_aff>=I/2. The report records that exact rational
cube radius for each sign. This is a genuine locally positive extension of
the pointwise jet, with no claim that it solves the PDE.

In fact its equation residual is EXACTLY

    B(partial Q_aff)-R(Q_aff)=-sum x_k R(H_k).                (5)

At least one coefficient is nonzero in each sign. Thus the first explicit
affine extension fails, and a constant-gradient extrapolation must be rejected.
A nonlinear correction, full formal prolongation, or a compatible analytic
Cauchy system remains necessary. Neither the failure of this affine extension
nor the small-algebra theorem excludes all symmetric fields.

## 5. Validation and source ceiling

The producer computes the complete sparse symbol and witnesses; a separate
raw signed-bit reconstruction checks102 raw/dual/prolongation obligations,
including the exact reduced ranks and differential consequence. Four genuine
coefficient/core/derivative/mass perturbations are rejected after the baseline.
No numerical rank or finite-difference sign establishes a claim here. These
are separate implementations by the same author, not external verification.

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 is UNCERTAIN about
its unselected rival versions. SC-MAS-01/02 ASSERT their scoped stylized mass
claims, neither selecting this Q. SC-META-53 remains UNCERTAIN and
SC-META-56 DISAVOWS an odd-action prerequisite. The source register, physics
ledger (LT-SM8/LT-GR6b/AC-F1/RA-F1), and canon remain unchanged.

Strongest overclaim: a compatible positive first jet called an integrated
positive metric. Equation(5) explicitly rejects that inference. Strongest
contrary route: matrix directions outside span{I,V,S}; the full-symbol witness
shows that route remains live. Next compare a full constrained prolongation
with genuinely source-owned pairing data; do not rerun the closed small-algebra
multicoordinate question or call this an all-GU obstruction.
