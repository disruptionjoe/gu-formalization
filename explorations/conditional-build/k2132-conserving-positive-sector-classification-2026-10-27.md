---
title: "K2132: Complete graph chart for maximum-dimension conserving positive sectors"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite native classification; no selected physical quotient or GU recovery
scripts:
  - tests/channel-swings/k2132_conserving_positive_sector_classification_probe.py
---

# K2132: Complete graph chart for maximum-dimension conserving positive sectors

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
result: complete classification of complex32 constant invariant sectors conserving the fixed massive current
carrier: actual K2120 complex128 core with Cl4 multiplicity32 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: inherited S=iF=a t+3a(iV)Z ON=declared_core
real_structure: complex adjoint of actual real Clifford matrices; no real positive sector asserted
grading: joint t and Z signs; not source ambient-half or observed chirality
action_owner: repository-construction -- K1951 principal and nonzero K1967 mass
target: maximum-dimension positive conserving invariant subspaces MAP-TYPE=intertwiner
```

## 1. Question, input and distinction

[K2120](k2120-inherited-core-current-2026-10-27.md) proves the maximum dimension32
and constructs a positive circle. [K2129](k2129-rotated-positive-sector-raw-equations-2026-10-27.md)
closes smooth raw motion of that circle. Neither classifies the larger family.
We classify every **maximum-dimension** constant invariant subspace with a
strictly positive, conserved inherited current. This is not a classification of
all smaller inclusion-maximal subspaces, source-selected observations or quotients.

Use the ACTUAL K2120 matrices C1,C2,C3,M,t=iT,Z and S=iF. Here a=9/280,
S=a t+3a(iV)Z, V=C1 C2 C3. The four Hermitian Clifford generators Cj,iM
act irreducibly on C4 with multiplicity C32. Their invariant subspaces reduce
and have form C4 tensor L. The commuting t,Z act on multiplicity, with four
joint sign spaces E++ E+- E-+ E--, each dimension8. Positivity is exactly

    (t+3Z)|L>0 and (t-3Z)|L>0.                         (1)

Conservation is a further requirement. For nonzero fixed real mass mu,
M*=-M, [t,M]=0 and {iV,M}=0. The compressed current must obey
S_L M+M* S_L=0. Its defect is 6a(iV)M tensor Z_L. Since (iV)M is invertible,

    massive current conservation iff Z_L=0.           (2)

The derivative terms already commute with S_L. Positivity without (2) need
not conserve this current. For example L=(x,r x,0,0), r=6/5, satisfies(1)
but Z_L=(1-r²)I is nonzero. For mu=0 condition(2) is not necessary.
This does not revise K2120's constructed circle, which already has Z_L=0.

## 2. Exhaustive graph chart

For a maximum-dimension sector, dim L=8. Projection to E++ is injective.
Indeed Z_L=0 gives, on a vector with x++=0,
||x-+||²=||x+-||²+||x--||², hence <t>=-2||x--||²<=0,
contradicting strict positivity. The equal dimensions make the projection
bijective, so in the fixed joint-space bases every such L is uniquely

    L={(x, A x, B x, C x): x in C8}.                   (3)

The letters A,B,C here are graph maps, not Clifford generators or connections.
Their compressed forms are

    Z_L=I-A* A+B* B-C* C,
    t_L=I+A* A-B* B-C* C.

Consequently all and only the conserving positive graphs are

    B arbitrary; C* C<I;
    A=U (I+B* B-C* C)^(1/2), U in U(8).              (4)

The square root is strictly positive and unique; polar decomposition makes U
unique. The inherited form in these coordinates is 2a(I-C*C), independent
of B and U. Conversely(4) makes Z_L=0 and t_L=2(I-C*C)>0, proving every
listed graph works. No missing graph patch occurs at finite strict-positive
points. This is an explicit parameter space, not a source selection rule.
Its real dimension is 128+128+64=320 (two complex8x8 matrices, one unitary8).
The contraction ball for C and unrestricted B are contractible; the parameter
space deformation retracts onto U(8). The K2120 circle is only the slice
B=C=0, U=e^(i theta)I up to its chosen sign convention. These parameters are
not booked GU residue or physical observables.

For comparison, without conservation the same graph chart for positive
maximum-dimension L follows from K2120's positivity argument, but its exact
conditions are the TWO inequalities

    4I-2A*A+2B*B-4C*C>0,
    -2I+4A*A-4B*B+2C*C>0.                             (5)

To justify that chart without assuming Z_L=0: (1) implies t_L>0. If x++=0,
then ||x+-||²>||x-+||²+||x--||², and the first form in(1) is negative.
Thus the same injectivity proof applies. Equation(5) is not replaced by(4)
unless current conservation is required.

## 3. Native noncircle survivor and its consequences

In the ORIGINAL128 coordinate order define

    Q_ij = (-1)^popcount(i & 72) when j=i xor4, else0.

The exact native probe verifies Q*=Q, Q²=I; Q commutes with Cj,M,Z,R and
anticommutes with t. It maps E++ to E-+. R maps E++ to E+-.
Thus the following family uses actual core matrices rather than a schematic
multiplicity-space identification:

    E=(I+t)(I+Z)/4,
    Y(u)=(I+cosh(u)R+sinh(u)Q)E, u real.

Direct algebra gives, for all real u,

    Y*Y=2 cosh²(u)E, Y*tY=2E, Y*ZY=0,
    Y*S Y=2aE, Y*S Y'=0.                              (6)

The three target joint spaces are mutually orthogonal, making these identities
immediate from cosh²u-sinh²u=1. Q and R intertwine the four Clifford generators,
so ran Y is invariant and conserving. For u nonzero it has a nonzero t-negative
component, and therefore lies outside the whole K2120 circle. Its orthogonal
projector is P_u=Y Y*/(2 cosh²u); P_u S P_u=a sech²u P_u.
This last expression is relative to Euclidean normalization. The moving frame
Y carries the constant current2a and must not be mistaken for a failing current.

The released [K2134](k2134-noncircle-current-transport-2026-10-27.md) constructs
its exact transport and checks the original raw-coefficient constraint.
A new family survives positivity and conservation; it has not thereby survived
source action, raw upper contraction, or global physical selection.

## 4. Acceptance and ceiling

The probe reconstructs native matrices and verifies all Q/E/frame identities;
small noncommuting graph-map controls exercise adjoint order and strict boundary.
The exhaustive chart, dimension and all-u statements have the written proofs
above, separately reviewed internally. Exact finite checks do not certify
those quantifiers by sampling. No novelty, external-expert or proof-assistant
certification is asserted. Native correction/path-dependency checks preserve
full1920 mass defect, fixed-circle rigidity and source-normalization boundaries.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 remain
UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. LT-SM8/LT-GR6b,
source register, ledger0.263 and canon remain unchanged: a conditional sector
classification is not a source-selected interacting physical quotient.
