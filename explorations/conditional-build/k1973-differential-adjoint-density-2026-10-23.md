---
title: "K1973: Smooth density jets cannot repair the fixed raw mass"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1973_differential_adjoint_density.py
  - tests/channel-swings/k1973_differential_adjoint_density_probe.py
---

# K1973: Smooth density jets cannot repair the fixed raw mass

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
result: all smooth chiral-diagonal density/adjoint first jets excluded on the fixed core
carrier: real raw1920 operator with positive128 injection J and fixed flat principal coefficients LAYER=toy CHIRALITY=N/A
pairing: fixed core energy H=8I; pointwise bilinear Q0 P with density rho ON=raw_spinor_and_vector_spinor
real_structure: real Cl(7,7); nonzero real or complex bilinear weights, positive scalar density
grading: Clifford volume eigenspaces, not physical chirality
action_owner: repository-construction -- fixed conditional model
target: fixed-core differential lower return MAP-TYPE=intertwiner
```

## 1. Actual differential question and result

[K1970](k1970-weighted-adjoint-mass-completion-2026-10-22.md) leaves
variable density terms open. We now include their actual first jets, rather
than repeat its constant pairing scan. Keep K1967's scalar coefficient line,
raw injection J, fixed flat principal blocks and fixed positive core energy.
On a connected coordinate patch let

    Q(x)=Q0 P(x), Q0=I or B, P=p_plus Pi_plus+p_minus Pi_minus,
    rho(x)>0, p_plus(x)p_minus(x) !=0.

All functions may be smooth; the exclusion even allows complex nonzero
bilinear weights. Both overall signs of the tested barred adjoint remain
included. No such density/pairing repairs a NONZERO member of the raw mass
line on any open patch where that mass is nonzero. This is a conditional
operator-class exclusion, not identification of the source barred-star map.

For the differential column (D u)_k=partial_k u+Omega_k u, equip the
vector-spinor form with eta_k Q and the spinor form with Q, both with rho.
Integration by parts gives the exact local expression

    D^dagger zeta = sum_k eta_k[-partial_k zeta_k
      - H_k zeta_k + Q^-1 Omega_k^T Q zeta_k],
    H_k=Q^-1 partial_k Q+(partial_k log rho)I
       =h_k_plus Pi_plus+h_k_minus Pi_minus.             (1)

The zeroth-order multiplication coefficient has no derivative-of-Omega term.
Derivative-of-coefficient terms would occur for a changed principal symbol;
that is a different class. Formula(1) is a formal expression on compactly
supported tests, not a global adjoint-domain assertion. The lower raw block
is its specified signed negative, consistent with the stored source-shaped
model. Any sign changes only rescale the available correction space.

## 2. Complete first-jet image and a coordinate quotient witness

On the fixed section zeta_k=J_k psi, the new lower correction is in

    span{Pi_plus J_k, Pi_minus J_k : k=0,...,13}.         (2)

The exact rank is28. Its union of nonzero matrix positions has896 entries.
The required mass return T=-J_0 M has128 nonzero entries, and the two supports
are DISJOINT. This is a projection onto actual matrix coordinates of the
same raw equation, not compression to an unrelated energy quotient.

K1970 already gives L0=r_plus Pi_plus T+r_minus Pi_minus T for both base
forms. Projecting the complete differential equation onto the128 positions
of T annihilates EVERY first-jet correction(2). It therefore still requires

    epsilon r_plus/q=1, epsilon r_minus q=1,
    q=p_plus/p_minus, r_plus r_minus=1.                 (3)

The exact products remain3438423/16773632 and4040255/4193408, neither1.
At every point with nonzero mass, (3) is impossible. Allowing arbitrary
independent jets is a superset of smooth integrable fields, so no PDE for
the density can evade this obstruction. It is not legitimate to retain
K1970's residual RANK lower bound after adding arbitrary off-support entries;
we claim the nonzero coordinate projection, not that unproved rank bound.
A varying mass m(x) multiplies T and L0 equally and does not differentiate a
multiplication operator, so the argument is pointwise wherever m(x)!=0.

## 3. Released integrability and global density consumer

The two gradient one-forms in(1) are locally d log(rho p_plus) and
d log(rho p_minus). They are closed and their local connection curvature
vanishes. Arbitrary independently assigned28 jets need not integrate on a
patch; we allowed them only to make the exclusion stronger. Global complex
weights can have logarithmic periods, so local exactness is not asserted as
a single global logarithm or trivial holonomy for unrelated data.

For the separate POSITIVE scalar-density differential model on R^n,
U f=sqrt(rho) f is unitary from L2(rho dx) to L2(dx). The corrected
operator partial_k+(1/2)partial_k log rho equals U^-1 partial_k U on
the matched domain U^-1 H1. For periodic positive smooth rho the same holds
on the torus. Thus a density alone in this explicitly matched model cannot
create a new spectral mass gap. This is a global domain statement for that
scalar-density control, not for the antisymmetric B pairing or the unbuilt
GU physical quotient. Unmatched domains or a changed operator are not covered.

## 4. Verification and remaining source input

The producer reconstructs actual raw entries and computes the28-column rank
by sparse rational elimination. A separate probe reconstructs J and T without
that producer, obtains rank28 with a separate matrix implementation, and
checks a nonconstant pairing/density integration-by-parts identity symbolically.
Four genuine mathematical faults are rejected after a green baseline.
An initial symbolic check needed rational cancellation rather than expansion;
this harness simplification was corrected before the final replay.

The [formal-adjoint definition](https://www.math.ucdavis.edu/~hunter/book/ch10.pdf)
is prior mathematical context; the new work is its fixed-core image and
quotient test. No novelty, external expert acceptance or formal proof claimed.
SC-OP-04 ASSERTS candidate grammar, SC-OP-05 is UNCERTAIN about rival
southeast completion, SC-MAS-01/02 ASSERT their scoped stylized mass claims;
none selects Q, rho, this mixed grade1/13 line or this core. SC-META-53
remains UNCERTAIN. LT-SM8/LT-GR6b/AC-F1/RA-F1 remain NEEDS.
Next source-facing input must change the actual coefficient/core/principal
class or provide a non-chiral pairing/reality map; another scalar density
or smooth chiral reweighting of this class cannot repair it. No source,
physics-ledger, canon or physical-family claim changes.
