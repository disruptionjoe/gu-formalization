---
title: "K1982: Exact trace flux obstructs bounded global positive pairings"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1982_positive_pairing_flux_obstruction.py
  - tests/channel-swings/k1982_positive_pairing_flux_obstruction_probe.py
---

# K1982: Exact trace flux obstructs bounded global positive pairings

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
result: full raw adjoint trace certificate, periodic exclusion and exponential growth of positive-pairing volume
carrier: fixed raw1920 section, real128 core, all14 flat coordinates LAYER=toy CHIRALITY=N/A
pairing: real symmetric positive-semidefinite Q in the fixed frame ON=raw_spinor_and_vector_spinor
real_structure: real Cl(7,7); neither source bar nor physical positivity is identified
grading: Clifford volume, not observed chirality
action_owner: repository-construction -- fixed lower-return PDE
target: global bounded positive completion of the unchanged raw equation MAP-TYPE=intertwiner
```

## 1. Global question and exact certificate

Keep the coefficients, raw section and mass target of
[K1979](k1979-multicoordinate-symmetric-pairing-2026-10-23.md) EXACTLY:

    sum_k eta_k (partial_k Q) J_k = R_epsilon(Q),
    R_epsilon(Q)=sum_k eta_k Omega_k^T Q J_k - epsilon Q T,
    eta_k=+1 (k<7), -1 (k>=7), epsilon in{-1,+1}.           (1)

Q is a real symmetric128x128 C1 field. The base of this theorem is the
flat coordinate space R14, with Euclidean coordinate balls and volume for
the estimates; that is not a claim about a physical positive ambient metric.
K1979's local positive first jets remain valid. The new question is whether
ANY full-matrix positive-semidefinite solution can be periodic or globally
bounded, without restricting Q to a small algebra or one coordinate.

For each sign there is an explicit constant128x128 matrix Y satisfying

    R_epsilon^*(Y)=I,
    R_epsilon^*(Y)=sum eta_k Omega_k Y J_k^T-epsilon Y T^T. (2)

This is a FULL matrix equality, checked exactly, not only a projection onto
an invariant subspace. Put C_k=Sym(eta_k Y J_k^T) and
F_k(x)=tr(C_k Q(x)). Equations(1)-(2) imply the exact identity

    div F = tr Q.                                        (3)

The coefficient matrices and rational norm bounds are in the linked JSON.
The construction reuses K1976's verified invariant algebra. Write its basis
as I,V,S,VS and L(Q)=R(Q)J_0^{-1}. Its Frobenius-adjoint invariance permits
solving L^*X=I in four dimensions, followed by Y=X(J_0^{-1})^T:

| epsilon | coefficient of S in X | coefficient of VS in X |
| --- | --- | --- |
| -1 | 20638344/13335209 | -9894184/13335209 |
| +1 | -4522104/13335209 | 32039896/13335209 |

The I,V coefficients are zero. Independent reconstruction checks(2) on the
actual raw matrices; existence of the reduced solve alone would not prove it.
For symmetric C_k use its exact maximum absolute row sum c_k. Then
||C_k||_op<=c_k and for Q>=0, |F_k|<=c_k tr Q. Consequently

    |F|_Euclidean <= C tr Q,   C=sum c_k,
    C_-=1106515264/120016881, C_+=37242560/2927241.         (4)

These constants are certified upper bounds, not optimized constants.

## 2. Executed global consumers

**Periodic domains.** Integrate(3) on any rectangular flat torus with periodic
Q. The flux cancels, giving integral tr Q=0. A continuous PSD matrix field
has nonnegative trace and vanishes wherever its trace vanishes. Thus every
periodic PSD solution is identically ZERO. Positive-definite solutions are
excluded. The same conclusion holds on a bounded domain with zero outward
flux, under the usual divergence-theorem regularity.

**Whole-space growth.** For a global PSD solution define
V(r)=integral over B_r(x0) of tr Q. Divergence and(4) give

    0 <= V(r) = integral_boundary F.n <= C V'(r).

If Q is nonzero, choose x0 and r0 with V(r0)>0. Integration yields

    V(r) >= V(r0) exp((r-r0)/C), r>=r0.                   (5)

Therefore no nonzero global PSD solution has bounded, polynomial-growth,
or more generally sub-exponential total trace volume. In particular there
is no globally bounded positive pairing on this fixed raw core. No uniform
positive lower bound is needed: nonzero continuity supplies V(r0)>0.
This also excludes finite-total-trace PSD fields. It does NOT exclude an
unbounded, exponentially growing field and does not prove one exists.

**Quantitative finite-domain requirement.** If mI<=Q<=MI throughout a closed
ball of radius r, where 0<m<=M, then volume versus boundary area in14
coordinates gives

    r <= 14 C M/m.                                      (6)

A well-conditioned positive field cannot extend through arbitrarily large
balls with fixed m,M. Boundary injection or growth must pay this exact
necessary cost. This is not an existence criterion, an optimal radius or a
physical prediction. Equation(5) is stronger for global growth; equation(6)
is a convenient finite-domain consumer.

## 3. Follow-through on the surviving local route

For every actual K1979 identity-value gradient H_k, both cokernel tests
<Z_j,R(H_k)>=0 pass exactly, for both signs. These are the necessary
conditions obtained by differentiating the algebraic value constraints
<Z_j,R(Q)>=0. The separate raw implementation checks all56 identities.
Thus this cheap next compatibility test does NOT exclude those first jets.
It also does not produce symmetric mixed second derivatives: the coupled
second-order prolongation remains necessary. This is affirmative limited
follow-through, not another claim that first-jet survival proves a field.

## 4. Controls, contrary routes and claim ceiling

Producer checks the complete adjoint identity and all stored symmetric flux
coefficients. A separate raw signed-bit reconstruction checks94 matrix/PSD/compatibility
obligations and rejects four genuine coefficient, core, dual and mass-sign
faults after its clean baseline. Exact matrix algebra supports(3)-(4);
the divergence argument, not a finite sample, proves the universal claims.
These are separate implementations by one author, not external verification.

Strongest overclaim: using the global obstruction to refute local positive
first jets or every source pairing. Neither follows. Strongest contrary
construction: exponentially growing fields, nonperiodic boundary flux,
changed coefficients/core or indefinite Q; these lie outside the excluded
class, and their existence/physical admissibility is not asserted. Weakest
transfer seam: a curved or source-owned moving equation would have extra
coefficients/density terms and must rederive(2)-(3). No automatic transfer.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
unselected rival versions. SC-MAS-01/02 ASSERT scoped stylized mass statements.
None selects this Q. SC-META-53 remains UNCERTAIN and SC-META-56 DISAVOWS an
odd-action prerequisite. LT-SM8/LT-GR6b/AC-F1/RA-F1 and canon remain unchanged.
The useful next native test is local constrained prolongation or a genuinely
source-owned change of coefficients/pairing, not another bounded-global
completion attempt of(1). No all-GU obstruction or novelty is claimed.
