---
title: "K1976: Local general bilinear transport and its symmetry boundary"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1976_general_pairing_transport.py
  - tests/channel-swings/k1976_general_pairing_transport_probe.py
---

# K1976: Local general bilinear transport and its symmetry boundary

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
result: local lower-return transport, invariant matrix algebra, symmetric-trajectory exclusion and one global singularity
carrier: fixed real raw1920 section with128 core coordinates LAYER=toy CHIRALITY=N/A
pairing: general real nondegenerate bilinear Q and eta_k Q ON=raw_spinor_and_vector_spinor
real_structure: real Cl(7,7), no source star identification
grading: actual Clifford volume eigenspaces, not observed chirality
action_owner: repository-construction -- specified lower-return equation only
target: variable bilinear repair on a fixed common raw core MAP-TYPE=intertwiner
```

## 1. The specified lower-return equation has a local repair

Keep [K1967](k1967-paired-raw-coefficient-observation-2026-10-22.md)'s
actual raw injection J, real scalar grade1/13 coefficients Omega_k and target
T=-J_0 M. The mass normalization is the stored nonzero representative.
[K1973](k1973-differential-adjoint-density-2026-10-23.md) excluded every
smooth chiral-diagonal density/pairing in its class. Change that hypothesis:
let Q(x) be an arbitrary invertible real bilinear spinor matrix, with the
vector-spinor form eta_k Q, constant density and dependence only on x=x^0.
Here eta_k=+1 for k<7 and -1 otherwise.

The right formal bilinear adjoint of D_k=partial_k+Omega_k is

    D^dagger zeta = sum_k eta_k[-partial_k zeta_k
      -Q^-1(partial_k Q)zeta_k+Q^-1 Omega_k^T Q zeta_k].

On the fixed section, the specified zeroth-order lower-return condition,
with its two sign conventions epsilon in{-1,+1}, becomes exactly

    Q' J_0 = sum_k eta_k Omega_k^T Q J_k - epsilon Q T.       (1)

The producer reconstructs J_0 and proves it is an invertible monomial matrix.
Thus (1) is the constant linear ODE

    Q'=L_epsilon(Q)
      =[sum eta_k Omega_k^T Q J_k-epsilon Q T] J_0^-1.        (2)

For Q(0)=I, its convergent exponential series is an entire REAL matrix
solution. In the maximum-row-sum norm, the exact bound for BOTH signs is

    ||L|| <= B=6331/1448,
    ||Q(x)-I|| <= exp(B|x|)-1.

Therefore Q is invertible on |x|<=724/6331: B|x|<=1/2 and exp(1/2)<2.
This is a rigorous local repair of (1), not a truncated-jet existence claim.
The four stored derivatives are reproduction controls on that exact ODE.
The usual [matrix-exponential construction](https://hankyang.seas.harvard.edu/OptimalControlEstimation/linear-algebra-and-differential-equations.html)
is standard; the work here is the actual raw equation and its constraints.

This does NOT select the source bar/star, make a positive symmetric metric,
construct a global operator domain, or verify every other adjoint block of
the four-field source operator. Only the specified lower return and unchanged
raw coefficients/core are repaired. Nonsymmetric bilinear adjoints need not
be involutive, so this cannot be substituted for a Hilbert-space adjoint.

## 2. The transport closes in an explicit four-dimensional algebra

Let V be the actual Clifford volume matrix and S the all-positive monomial
permutation on the support of L(I). Exact entry reconstruction proves

    V^2=S^2=I, VS=-SV, V^T=V, S^T=S.

The space span{I,V,S,VS} is invariant under L for both signs. The report
stores its full rational4x4 coefficient matrix A, by columns, and verifies
EVERY raw128x128 entry of this invariance, not selected compressed entries.
Writing Q=aI+bV+cS+dVS gives q'=Aq, q(0)=(1,0,0,0).
The multiplication identities yield

    Q(aI-bV-cS-dVS)=(a^2-b^2-c^2+d^2)I,
    det Q=(a^2-b^2-c^2+d^2)^64.                           (3)

The multiplicity64 follows by pairing each +1 volume basis vector with its
S-image in the -1 eigenspace. This reduces the actual invertibility question
from128x128 determinants to one scalar analytic function; no quotient or
unproved raw intertwining is involved.

## 3. Released symmetry and global-extension tests

Because VS is antisymmetric, a trajectory in this algebra is symmetric iff
d(x)=0 throughout its interval. The observability matrix formed by row4 of
I,A,A^2,A^3 has determinant

    9076276625625/2250837843771392       (epsilon=-1),
    15814504392489/2250837843771392      (epsilon=+1).

Both are nonzero. If d and its first three derivatives vanish at any point,
q at that point is zero; uniqueness then makes Q identically zero. Hence
NO nonzero trajectory in this four-dimensional family can stay symmetric
on an open interval, including any different initial matrix in this algebra.
This is stronger than merely checking Q'(0) is nonsymmetric. It does not
exclude arbitrary initial matrices in the full16384-dimensional space or
pairings depending on additional coordinates.

### Full-matrix positive-definiteness consumer

The reduced obstruction is not automatically a full-space obstruction. We
therefore checked the independent missing transfer. With the Frobenius inner
product, the adjoint of L is exactly

    L*(Q)=sum eta_k Omega_k Q (J_k J_0^-1)^T
          -epsilon Q (T J_0^-1)^T.

It ALSO preserves span{I,V,S,VS}. Every raw entry is checked; its coefficient
matrix is A^T because the four basis matrices are orthogonal and have equal
squared norm128. Thus this subspace is reducing, and its orthogonal projection
E commutes with L on the FULL16384-dimensional real matrix space.

If an arbitrary full-matrix Q(x) is symmetric and satisfies(2), E(Q(x)) is
symmetric: its VS coefficient is zero because VS is antisymmetric. It is a
reduced symmetric trajectory, hence section3 forces E(Q(x))=0. In particular
its I coefficient tr(Q(x))/128 vanishes. Therefore EVERY symmetric full-space
trajectory of(2) has trace zero. No positive-definite or negative-definite
symmetric solution can exist on any open interval, for either sign and ANY
initial matrix, under the one-coordinate-dependence ansatz.

This uses a separately verified transfer, not invariance of L alone. It does
not exclude invertible indefinite trace-zero pairings, nonsymmetric pairings,
or Q fields depending on several coordinates. It also makes no source-star
identification. The positive-definite one-variable question is now closed;
a full-space repeat of that same question has no remaining decision value.

For the identity-initialized epsilon=+1 trajectory, an exact Taylor enclosure
at x=1 gives

    -3/2 < a(1)^2-b(1)^2-c(1)^2+d(1)^2 < -7/5.

It is1 at x=0. Continuity proves a singular Q at SOME x in(0,1), so this
solution cannot supply a globally nondegenerate pairing on the whole line.
The epsilon=-1 determinant factor lies in(4,5) at x=1; this is NOT a proof
of global invertibility for that sign. Both analytic determinants have
isolated zeros unless identically zero, excluded by their value at0.

For reproducibility the producer sums40 terms and bounds the coordinate
remainder by3^ceil(B4) B4^41/41!, where B4 is the row-sum norm of A.
The separate probe sums48 terms and uses its own49th-order bound. Squaring
intervals propagates a rigorous determinant enclosure. No floating sign test
establishes the singularity. The conservative local radius is unchanged.

## 4. Verification, source fidelity and next calculation

The producer checks raw jet equations, norm bounds, invariant-algebra closure,
symmetry observability and a certified determinant sign. The separate probe
rebuilds gamma/J from the prior signed-bit implementation, checks34 combined
raw/reduced/determinant obligations and rejects four mathematical faults:
changed coefficient, signature, transpose and mass sign. These are internal
implementations by the same author, not external independent certification.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
rival southeast versions. SC-MAS-01/02 ASSERT their scoped stylized mass
claims, neither selecting this Q. SC-META-53 remains UNCERTAIN and
SC-META-56 DISAVOWS an odd-action prerequisite. LT-SM8/LT-GR6b/AC-F1/RA-F1,
source register, physics ledger and canon verdicts remain unchanged.

The changed nonsymmetric class survives locally, so the earlier diagonal
exclusion must not be expanded into all-pairing impossibility. The actually
executed consumers delimit symmetry and global extension. Stronger next
questions are multi-coordinate symmetric transport/integrability or a genuinely
source-selected reality/pairing; one-variable full-space positive metrics are
excluded, while indefinite symmetric solutions require a separate test. Epsilon=-1 global determinant positivity remains open.
