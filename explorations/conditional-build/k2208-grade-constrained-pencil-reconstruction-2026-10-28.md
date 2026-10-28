---
title: "K2208 Exact real-grade reconstruction of prescribed Clifford pencils"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete prescribed-factor reconstruction for exact supplied matrices; not a solution or classification of all ten adapter rows
scripts:
  - tests/channel-swings/k2208_grade_constrained_pencil_reconstruction_probe.py
---

# K2208 Prescribed real-grade pencil reconstruction

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: exact real-grade prescribed-pencil kernel, invertibility test and central-half classification
carrier: full real Cl77 S128 with auxiliary complex normal S32 and chiral16 halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: normal Chevalley bilinear form inducing alternating chiral matrices ON=declared_carrier
real_structure: real normal Cl46 grade3 coefficients with quaternionic opposite-half transport
grading: normal Clifford grade3/7 and parity, not observed chiral families
action_owner: repository-construction -- fixed normalized K2169 adapter
target: realization of prescribed even norm-one factors by real grade3/7 pencils MAP-TYPE=intertwiner
```

## Scope and new decision problem

[K2205](k2205-ordered-pencil-real-constraints-2026-10-28.md) supplies abstract
norm-one completion of the singular-safe Euler image equations. That completion
does not supply the prescribed real Clifford pencil. This note solves the
latter reconstruction problem for an EXACT SUPPLIED even invertible norm-one
matrix Y. It does not solve the nonlinear selection of Y from the Euler system,
and every reconstructed pencil must still satisfy all ten original adapter rows.
The actual K2205 pencil is a realizable control and remains Euler-rejected.

Use the same real normal Cl(4,6), auxiliary complex spinor32, normal volume I_N
with I_N²=-I, quaternionic bar beta and nondegenerate B. Let real grade3 ports
w,u give v=I_N w and

    P=7v-15iu, bar(P)=7v+15iu, Y=P^-1 bar(P).             (1)

Do not identify this bar with reversion. Require the full Y's norm-one identity
bar(Y)Y=I; the two chiral halves cannot be independently assigned.
SC-OP-04 ASSERTS candidate grammar and SC-GEO-55 ASSERTS rotated-LC displacement;
neither selects these fixed normalized adapters. No physical quotient, source
verdict, ledger, canon, observed-family or external novelty claim follows.

## 1. A real form of alternating16 matrices

Choose a normal chiral half S_epsilon with I_N=epsilon i, epsilon=+1 or-1.
Measure epsilon in the actual representation; Fock parity is not a convention
for its sign. Define Phi(h)=(B h)|S_epsilon for grade3 h. B pairs opposite
halves and h is odd and B-skew, so Phi(h) is alternating.

The complex-linear Phi:Lambda³ C10 -> Alt16(C) is an isomorphism. Its
kernel is zero: Phi(h)=0 means h kills S_epsilon because B is nondegenerate
between opposite halves. Equivalently h Pi_epsilon=0, a linear relation
between Clifford grades3 and7 (h and h I_N); both vanish in the faithful
Clifford representation. The dimensions agree: binom(10,3)=120=16*15/2.
Therefore W=Phi(Lambda³ R^(4,6)) is a real form of Alt16(C), so W intersect
iW=0. W is generally NOT the entrywise-real alternating matrices.

Set a=7w+15epsilon u and b=7w-15epsilon u. On the selected half,

    (BP)|=-epsilon i Phi(a), (Bbar(P))|=-epsilon i Phi(b).

Thus prescribed Y_epsilon reconstruction is exactly

    Phi(a)Y_epsilon=Phi(b),  a,b real grade3, det Phi(a)!=0.     (2)

## 2. Complete reconstruction by a real kernel

Define the real-linear space

    K_Y={a in R120: Phi(a)Y_epsilon belongs to W}.          (3)

Each a in K_Y with Pf(Phi(a))!=0 reconstructs b uniquely through Phi inverse,
then w=(a+b)/14 and u=epsilon(a-b)/30. Conversely every actual real-grade
invertible pencil giving Y supplies one such a. There is no lost singular
chart: singular Phi(a) is excluded precisely because P must be invertible,
not because w,u or the Euler coefficient A must be invertible.

The chosen-half Phi(a) invertibility and Y invertibility imply Phi(b)
invertibility. Reality relates bar(P)'s chosen block to P's opposite block,
so P is invertible on both halves. Apply bar to P Y=bar(P) on the chosen
block and use bar(Y)=Y^-1 to recover the opposite equation. Hence(2) is
sufficient for full32 reconstruction, not only one block, under the stated
full norm-one assumption.

For rational-Gaussian data, take G whose120 columns are the upper triangles
of Phi's real blade basis. Impose both

    [Phi(a)Y]^T=-Phi(a)Y,
    Im[G^-1 upper(Phi(a)Y)]=0.                            (4)

The first contributes at most136 complex symmetric equations, the second120
real equations: at most392 real linear equations in120 variables. Diagonal
entries are included. Exact elimination yields a real kernel basis a1,...,am.
For real algebraic data use an exact algebraic number field and its specified
conjugation. Arbitrary unspecified real inputs do not have a claimed effective
equality oracle; this is not a floating-rank algorithm.

## 3. Deciding invertibility of the entire kernel

The homogeneous polynomial f(c)=Pf(Phi(sum_l c_l a_l)) has degree8. An
invertible member exists iff f is not identically zero. This is not equivalent
to an invertible basis member. A complete finite witness/rejection certificate
for m>=1 evaluates det Phi(sum_l alpha_l a_l) on all nonnegative integer
alpha with sum alpha_l=8. There are binom(m+7,8) nodes. A nonzero determinant
gives a real integer-coordinate witness. If every determinant is zero, then
f vanishes at the degree8 simplex interpolation nodes, hence identically.
For m=0 reject immediately.

For completeness, the simplex nodes are unisolvent for polynomials of degree
at most8 in m-1 variables on sum alpha=8: the barycentric falling-factorial
basis indexed by |beta|=8 is zero at every other degree8 integer node and
nonzero at its own node. Its size is the polynomial-space dimension. A
homogeneous f vanishing on sum c=8 vanishes wherever sum c!=0 by scaling,
then everywhere by polynomial identity. No determinant-degree16 grid is
needed because det of an alternating16 matrix is Pf².

This is a terminating exact algorithm, not an efficient one: m can be120,
there may be binom(127,8) nodes, and exact coefficients may grow. The program
implements the grid for a supplied subspace; large unsupported searches are
not silently run. Universal completeness is the proof, not a finite benchmark.

## 4. Entire central-half family and a strict false-positive control

For Y_epsilon=lambda I16 and the opposite block=(1/conjugate(lambda))I16,
reconstruction is possible exactly when lambda is nonzero REAL. Indeed if
lambda=a+ib with b!=0 and Z in W, lambda Z in W implies b iZ in W, hence Z=0.
For any nonzero real lambda choose invertible real trivector a=n123 and
b=lambda a to obtain a pencil. Thus the full scalar phase Y=lambda I32,
|lambda|=1, has only lambda=+1 and-1 as realizable phases.

In particular Y=iI32 passes norm-one and every paired-Jordan multiplicity test
(all eigenvalues are semisimple with even multiplicity). It is nevertheless
excluded by(3): K_Y=0. This is an actual prescribed-grade obstruction beyond
abstract norm-one completion. The real central-half realizations have
proportional w,u, including pure endpoints; their rejection as adapters uses
inherited commuting/anticommuting/pure-port exclusions, not a new all-row proof.

## 5. Controls that prevent false rejection or false acceptance

In signature(4,6), a1=(n1+n5)n2n3 and a2=(n1-n5)n2n3 are real trivectors.
Each squares to zero and has singular Phi: real quaternionic half exchange gives equal ranks of its two odd blocks, so square-zero forbids either block being invertible. But a1+a2=2n123 is invertible.
The span{a1,a2} therefore has a grid witness at alpha=(4,4), despite both
basis determinants being zero. The span{a1} has identically zero Pfaffian.
These are determinant-subspace controls; no claim identifies them as the
complete K_Y of some particular Y.

The actual K2205 w,u reconstruct their own Y using(2), while their original
Euler residual remains nonzero. A surviving grade reconstruction is not an
adapter solution. Deliberate loss of real-coordinate conditions falsely admits
iI; wrong epsilon or corrupted pencil coefficients fail the original full
P Y=bar(P) identity. Tests check those actual failures.

## Reproduction and useful next work

Run `python tests/channel-swings/k2208_grade_constrained_pencil_reconstruction_probe.py`;
`--write` regenerates the report. Exact finite Fock/blade, real-kernel,
invertibility-span and actual nonsolution controls accompany the universal
reconstruction/interpolation proof. There is no proof-assistant, external-expert,
parameter-search or global adapter certificate. The next useful consumer is
an exact proposed Euler factor Y, followed by this reconstruction and ALL ten
original rows. The prescribed-factor interface itself no longer needs to be
rebuilt, and neither abstract norm-one tests nor more spectra can replace it.
