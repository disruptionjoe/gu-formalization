---
title: "K2195 Anticommuting spectral exclusions and quartic reduction"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2195_anticommuting_spectral_reduction_probe.py
---

# K2195 Anticommuting spectral exclusions and quartic reduction

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
result: K2195 zero-top-grade exclusion and weighted quartic spectrum constraints
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

The fixed normalized adapter family has **no anticommuting solution with
vanishing normal-grade10 product component J**, even when both squares are
nonscalar and have Jordan blocks. This closes the remaining J=0 family left
by [K2193](k2193-noncommuting-clifford-constraints-2026-10-28.md).

If J is nonzero, a surviving anticommuting solution must instead have an
invertible ratio X with a specific quartic polynomial and an eight-value
weighted trace representation. Its spectrum cannot have one or two distinct
roots, or four equally weighted distinct roots. The remaining three-root
and unequal four-root possibilities are necessary spectral candidates, not
Clifford reconstructions or solutions of the original ten rows.

The object remains the full real Cl77 S128, fixed W(3,1)+N(4,6), normalized
zero-order adapters and supplied common reverse of K2169/K2171. SC-OP-04
ASSERTS candidate four-field grammar, not these adapters. SC-GEO-55 ASSERTS
rotated-LC displacement, not ordinary torsion. No source, full16cell/full20,
K-C, physical quotient, native2+1/chirality, ledger0.263, LT-SM8/LT-GR6b/AC-F1
or canon claim changes. No GU falsification, faithful eight-dimensional
representation, novelty or proof-assistant/external-expert claim.

## 1. Necessary equations and the trace carrier

Reuse K2193's independently checked contraction of all ten original rows:

    E=245V²+1275VT+270T²+(98a-294c)V+(510a-810c)T=0,
    LH=8eD,
    L=-21V+99T-28a-252c, D=49V+225T invertible.       (1)

Here v=I_N w, t=Omega u, w,u are real normal trivectors and [w,u]=0;
V=v²=w², T=t²=-u², H=wu, H²=-VT, and

    a=tau(V), c=tau(T), e=tau(H), J=Omega I_N e.

Tau is normalized trace on the faithful complex normal Clifford module of
dimension32. A nonzero real Clifford solution would give a complex one, so
complex spectral exclusions suffice. V,T,H commute. Simultaneous triangular
form is used only for eigenvalues and traces; no diagonalizability is assumed.
D invertible excludes a joint pair (r,s)=(0,0) and every pair49r+225s=0.

## 2. J=0 reduces to four joint spectral types

When e=0, LH=0 and H²=-VT imply LVT=0. On each joint diagonal entry,
rsL(r,s)=0. Equations(1) then give the following exhaustive possibilities:

| type | r | s |
|---|---|---|
| pure V | (-2a+6c)/5 | 0 |
| pure T | 0 | (-17a+27c)/9 |
| mixed1 | (-43a+9c)/90 | (49a+693c)/270 |
| mixed2 | -25(a+9c)/38 | 49(a+9c)/342 |

For the mixed cases substitute r=(99s-28a-252c)/21. Then

    E(r,s)=(8/63)(-49a-693c+270s)(-49a-441c+342s).

Degenerate coincidences do not create a fifth type: assign their algebraic
multiplicity to any matching row. Both pure types can have vanished nominal
values, but an occupied vanished pair violates invertible D.

Let their multiplicities be n,m,k,l, nonnegative integers summing to32.
The two normalized-trace equations are a two-by-two homogeneous system in
(a,c). With l=32-n-m-k, after multiplying both normalized trace equations by32, its determinant is

    (2/285)[1875km+98kn-12320k+1875m²+2125mn
            -70800m+98n²+1568n+53760].          (2)

The exact probe exhausts all6,545 compositions. The only singular systems are

    (n,m,k,l)=(18,8,6,0), a/c=333/631;
    (n,m,k,l)=(20,0,12,0), a/c=27/49.           (3)

Both kernels are one-dimensional with c!=0. Thus c=0 gives only a=0,
which makes every displayed pair zero and contradicts D invertible. This also
covers a=c=0 directly. No root reality or diagonalization assumption enters.

For the first candidate, occupied pairs after dividing by c are

    (624/631,0), (0,1264/631), (-96/631,1680/631).

Only the six-dimensional mixed sector has H²!=0. Its two H eigenvalues are
±sqrt(-rs). Trace H=0 forces multiplicity3 for each. But the invertible odd
pencil P=7v-15t commutes with H and interchanges normal chirality, so every
H eigenvalue has equal algebraic multiplicity on the two chiral halves.
A total multiplicity3 is impossible, including nontrivial Jordan blocks.

For the second candidate,

    pure V: r=48c/49, s=0, multiplicity20;
    mixed: r=-8c/49, s=8c/3, multiplicity12.

V is invertible. Define X=u w^-1=HV^-1. Trace H=0 forces its nonzero
eigenvalues +7/sqrt(3) and -7/sqrt(3) each to have multiplicity6; its zero
eigenvalue has multiplicity20. These violate the stronger invariant below.

## 3. Pfaffian-square multiplicities

On the complex normal Cl10 module Λ* C5 use the Chevalley bilinear pairing

    B(alpha,beta)=[reverse(alpha) wedge beta]_top.

It is symmetric and pairs opposite chirality. Every Clifford vector is
self-adjoint for B; trivectors w,u are skew-adjoint. In chiral bases write
B=[[0,G],[G^T,0]]. The matrices G w_- and G u_- (and the corresponding
opposite blocks) are skew-symmetric16-by16 matrices. If w is invertible,
its two off-diagonal blocks are invertible, so the characteristic polynomial
of each chiral X block is a quotient

    det(u_- - z w_-)/det(w_-)

(up to choosing the equivalent opposite block). Each determinant is the
square of its Pfaffian. Thus each chiral eigenmultiplicity is even.
Because [w,u]=0 and X is even, it commutes with I_N and the odd invertible
P. P identifies the two chiral X blocks, so their characteristic polynomials
are equal. Every full32 algebraic eigenmultiplicity is therefore divisible4.
Multiplicity6 in the second candidate of(3) is impossible. All J=0
anticommuting solutions are excluded.

This is an algebraic-multiplicity statement. It does not bound Jordan block
sizes or exhibit a faithful representation of the generated algebra in a
smaller dimension. The exact Fock-matrix controls verify the pairing and
signs, all10 gamma relations and120 coordinate-trivector adjoints, and a
nontrivial commuting pair with invertible w,P. They are controls of the
universal pairing/Pfaffian argument, not exhaustive numerical Clifford search.

## 4. Released nonzero-J quartic

For e!=0, (1) and invertible D force H,L,V,T invertible. X=uw^-1 is now
invertible and the same Pfaffian result applies. Put

    A=245-1275X²+270X⁴,
    B=(98a-294c)-(510a-810c)X²,
    C0=21X+99X³,
    D0=(28a+252c)X+392e-1800eX².

Equations(1) become AV+B=0 and C0 V+D0=0. The exact elimination is

    C0 B-A D0=2(225X²-49)F(X),
    F(X)=1080eX⁴+(-129a+27c)X³-5100eX²
                         +(49a+693c)X+980e.    (4)

D=V(49-225X²) is invertible, so F(X)=0. Also gcd(A,C0)=1. Direct
polynomial identities then give

    V=(-43a+9c)/90+4eX-14eX^-1/9,
    T=(49a+693c)/270-52eX/3+98eX^-1/27.        (5)

For example substituting the proposed V gives
AV+B=(18X²-7)F/(18X) and C0 V+D0=11F/30. The Bezout identity for
A,C0 makes this V unique. T=-X²V follows from H²=-VT.

Since char32(X) is a fourth power of a degree8 polynomial, traces are averages
over eight values x_i (repetition allowed), each a nonzero root of F. Write
mu_k=(1/8)sum x_i^k. After normalizing a,c by e (algebraically dividing,
not asserting a real square-root rescaling of ports), take e=1. Then

    mu1=(-49a+27c)/120,
    mu_(-1)=(-28a+9c)/14,
    4mu2+((-43a+9c)/90)mu1=23/9.              (6)

The last is tau(H)=1 with H=XV. Jordan blocks contribute no extra trace
terms. This is an eight-value weighted TRACE reduction, not a faithful8
representation or a degree8 minimal-polynomial assertion.

## 5. Released exclusions of small spectral supports

One distinct root would give ac=-1 from H²=-VT and trace H=1. The scalar
L equation gives49a+217c=0; substitution into E gives -416c², impossible.
This argument concerns eigenvalues and still permits Jordan blocks.

For two distinct roots write them ys,s, with multiplicities n,8-n.
Invertibility gives y,s!=0; relabeling restricts n to1,2,3,4. Put z=s².
The first two equations(6) solve

    a=24mu1/7-6mu_(-1)/5,
    c=32mu1/3-98mu_(-1)/45.

The third equation is linear in z. It yields z=P_n(y)/Q_n(y):

| n | P_n | Q_n |
|---|---|---|
|1| -196y²+11480y-196 |45y(55y²-14y+343)|
|2| -28y²+980y-28 |45y(9y²-2y+25)|
|3| -140y²+3976y-140 |45y(53y²-10y+85)|
|4| -28y²+749y-28 |45y(13y²-2y+13)|

For every n, the probe also verifies gcd1 for the RAW linear coefficient and
constant of the h-trace equation before solving or canceling factors. It then
verifies gcd(P_n,Q_n)=1, so a vanished denominator supplies no omitted solution. Substitute z in F(s)=0 and F(ys)=0 and clear denominators.
The probe derives the two primitive degree5 polynomials for each n and
verifies an exact rational Bezout identity1 for each pair. Hence no two-root
spectrum survives, even over C. Clearing denominators only enlarges a zero
set; coprimality is therefore a valid exclusion, not an existence test.

For four equally weighted distinct roots, each is counted twice in the
8-value trace. Vieta and the first two equations(6) give

    631a-333c=0, 371a-153c=0,

hence a=c=0. The quartic's second Newton sum then makes the left side of
the third equation85/9 instead of23/9: contradiction. Unequal weights,
three distinct roots, repeated polynomial roots and Jordan structure are
not eliminated by that equal-weight calculation.

## Verification and next question

The probe performs the full rational32-dimensional trace census, exact
factorization/elimination/Bezout checks, Fock bilinear and actual commuting
fixture controls, and genuine sign/coefficient/pairing faults after a green
baseline. The proof of whole-class J=0 exclusion composes these with the
written universal Pfaffian/chiral-transfer argument. The original ten rows
are used through K2193's pinned necessary contraction, not silently replaced
by a sufficient spectral test.

Do not requeue J=0, one/two-root or equal-four-weight anticommuting spectra.
Remaining nonzero-J spectral candidates have three distinct roots or four
unequally weighted roots and must satisfy(4)--(6), real Clifford grades,
invertible pencil and ALL original rows. General noncommuting ports outside
{v,t}=0, common R0/R1 source maps and mobile geometry remain separate.
