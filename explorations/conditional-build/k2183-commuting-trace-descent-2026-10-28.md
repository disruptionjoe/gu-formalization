---
title: "K2183 Trace descent and finite affine spectral candidates"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2183_commuting_trace_descent_probe.py
---

# K2183 Trace descent and finite affine spectral candidates

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
result: K2183 commuting trace filter, affine Jordan exclusion and finite spectral remainder
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

A new grade-trace identity excludes the remaining affine nilpotent-square-defect
case and reduces every surviving affine-square pair to a finite algebraic set
of normalized spectral parameters: at most60 complex slopes and120 pairs
(z,c/a). A released real four-coefficient central construction is excluded in full.
General real Clifford reconstruction and all ten original equations remain necessary. This is a finite necessary classification, not an existence
result or exclusion of all affine pairs.

The same trace filter applies to nonaffine commuting squares. Noncommuting
ports require a separate ordered argument. The fixed full real Cl77 S128,
W(3,1)+N(4,6), common reverse, simple contraction and normalized adapters are
unchanged. SC-OP-04 ASSERTS candidate four-field grammar, not these supplied
adapters. SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, not
ordinary torsion. Ledger0.263, LT-SM8/LT-GR6b/AC-F1, source/full16cell/full20/K-C,
native2+1/chirality, physical quotient and canon remain unchanged.
This is conditional internal mathematics, not GU falsification or novelty.

## Universal commuting trace filter

Use [K2181](k2181-mixed-square-pencil-descent-2026-10-28.md) and
[K2179](k2179-commuting-nonscalar-descent-2026-10-28.md). Put

    V=v², T=t², a=<V>0, c=<T>0, h=vt=h4+h8, U=2h4-6h8,
    F=10V+16T+4a-12c, G=142V+36T+68a-108c.

The necessary equations include invertible P=7v-15t, [U,v]=[U,t]=0,
FG=21U², FV+3Uh=0, h²=VT, and

    Q=35V²-157VT-54T²+(14a-42c)V+(-102a+162c)T=0.

Let tau be normalized full32 trace after the real tangent split. It equals
the scalar part on the even normal expressions used here. Grade orthogonality
implies tau(h4 h8)=0, hence

    tau(U²)+4tau(Uh)-12tau(h²)=0.                     (1)

The coefficients on h4² and h8² vanish separately; cross products have zero
trace. Substituting the necessary equations gives tau(FG-28FV-252VT)=0.
Expanding and dividing by4 proves

    285tau(V²)+483tau(VT)+144tau(T²)
       +352a²-616ac-216c²=0.                         (2)

No positive form, real spectrum, individual-port inverse or diagonalizability
is assumed. In particular tau(X²) can be negative. Equation(2) remains a useful
necessary filter for general nonaffine commuting candidates.

## Affine trace descent

Write V=a+X, T=c+zX, tau(X)=0, M=tau(X²). K2181 gives

    AX²+DX+C0=0,
    A=35-157z-54z²,
    D=84a-199c+z(-259a+54c), C0=49a²-301ac+108c²,
    AM+C0=0.

K2181 already excludes A=0. Equation(2) supplies LM+C1=0, where

    L=285+483z+144z², C1=637a²-133ac-72c².

Thus E=AC1-LC0=0, with

    E=-2[(20727z²+61838z-4165)a²
       -(25263z²+83132z+40565)ac
       +(5832z²+20430z+16650)c²].                    (3)

### The repeated-root case is excluded

K2181's repeated-root case has D=C0=0 and X²=0, hence M=C1=0. If a=0,
C0=108c² forces c=0, which is the excluded proportional-square case.
Otherwise r=c/a would satisfy two quadratics whose exact resultant is

    Res_r(49-301r+108r²,637-133r-72r²)=-1443826944.

It cannot vanish. Every affine survivor therefore has two distinct roots and
is diagonalizable over C. This closes the genuine Jordan loophole retained
by K2181; it does not replace X²=0 with X=0 without proof.

### Zero scalar part a is also excluded

If a=0 and c is nonzero, E=0 requires 324z²+1135z+925=0.
For multiplicity m, put k=m(32-m). K2181's trace-multiplicity condition becomes

    (32-2m)² 108 A+k(-199+54z)²=0.

Its resultant with the preceding quadratic is

    2916[15239903841k²+33615525529600k+7671026339020800]>0.

All allowed k are positive. If also c=0, T=zV is already excluded.
Thus a is nonzero for every remaining affine candidate.

### Even multiplicities

Split the real tangent algebra before working in the faithful complex normal32
representation, where t=+i u or -i u on the tangent-volume eigenspaces; both
normal-volume sectors must remain present. The normal
volume has square -1 and eigenspaces +i,-i. The pencil P is odd in normal degree,
anticommutes with this volume, is invertible, and commutes with X because the
ports commute. It therefore bijects the two volume sectors inside each
X-eigenspace. Each multiplicity m is even. Selecting one16-dimensional sector
before applying P would invalidate the proof.

## Finite normalized spectral candidates

Normalize a=1 algebraically in (3), i.e. r=c/a and X/a; this is a ratio reduction,
not an assertion that a real port rescaling changes the sign of a. Define

    C0=49-301r+108r², D=84-199r+z(-259+54r),
    C1=637-133r-72r², E=AC1-LC0,
    R_m(z)=Res_r(E,(32-2m)² A C0+m(32-m)D²).

Evenness and interchange of the two roots leave only
m=2,4,6,8,10,12,14,16. The first seven resultants have degree8. For m=16
the resultant is a nonzero constant times the square of a quartic. None of
the degree8 leading coefficients vanishes: for integer k=m(32-m) it is

    2268426384[21990393k²+20902856704k-5674993975296].

The discriminant936110809545523068928 lies strictly between
30595927989² and30595927990², so this quadratic has no rational, hence no
integer, root. Also E(z,r) never vanishes identically in r: C0 and C1 are
linearly independent quadratics and Res_z(A,L)=203212800 is nonzero.
For each possible slope, E consequently permits at most two r values.
There are at most7*8+4=60 distinct complex slopes and120 normalized pairs.

These are upper bounds; resultants may introduce extraneous roots. Each pair
still requires real z,r, A nonzero, r distinct from z (otherwise proportional),
a nonzero traceless grade4 X, the two-root multiplicity condition, centrality,
actual real grade7/grade3 port squares, invertible P and all original equations.
No finite parameter count is a scientific existence proof.

## A real spectral relaxation survives

For m=16, D=0 implies r=(84-259z)/(199-54z). The denominator cannot vanish
with its numerator. The remaining quartic is

    2006694z^4+22562181z^3+69814211z²+58023859z-14806945=0.

It has exactly four simple real roots, isolated respectively in
(-3150/467,-20647/3061), (-2499/925,-7832/2899),
(-2487/1244,-2485/1243), and (319/1575,303/1496).
The positive root has r approximately0.167721 and M/a² approximately-1.576059.
A real matrix can have conjugate imaginary square-defect eigenvalues, so this
negative trace square is not a positivity contradiction. This is a necessary
spectral relaxation, not an actual Clifford solution.

The K2181 proportional and nonproportional affine fixtures satisfy (1), while
the residual of (2) is respectively -10704 and -35268. Reconstructing their
original ten rows again finds nine nonzero rows each. The trace filter rejects
these actual candidates but does not exhaust the finite spectral remainder.

## Released real Clifford reconstruction test

The finite spectral filter can immediately reject an entire actual Clifford
ansatz, not just the two earlier numerical fixtures. In the fixed normal basis
with signs ++++------, let b,c,d,e be real and set

    v=I_N n1(b n2n3+c n4n5),
    u=n6(d n2n3+e n4n5), t=Omega_W u.

The ports commute. Put B=n2n3n4n5, with B²=-1. Their squares are

    V=a+2bc B, a=c²-b²,
    T=c0+2de B, c0=e²-d².

Here c0 is the scalar square part; c is an ansatz coefficient. This class
contains both K2181 fixtures and admits nonproportional affine squares.
The original necessary equation Fv+3Ut=0 has two independent coefficients,
on blades n45678910 and n23678910 are respectively -2f1 and +2f2, giving

    f1=7b³-17bc²-7bd²-5be²-10cde=0,
    f2=17b²c+10bde-7c³+5cd²+7ce²=0.

Their exact combination is

    c f1+b f2=2bc(c0-12a)-10a de.                    (4)

If bc is nonzero, put z=de/(bc). For a=0, (4) forces c0=0 and T=zV,
already excluded. For a nonzero, r=c0/a=12+5z. Also X=2bc B has scalar
square, so the grade4 part of AX²+DX+C0=0 forces D=0. Substitution gives

    D/a=6(45z²-101z-384)=6H.

The new trace equation additionally requires

    J=E(z,12+5z)
     =-2(145800z^4+1084275z³+3009569z²+3801349z+1906655)=0.

But Res_z(H,J)=199816992133516800 is nonzero. No such pair exists.
This proof uses only necessary equations, so failing them suffices.

The boundary cases are also covered. If bc=0 but v is nonzero, f1 or f2
forces de=0; both squares are scalar and K2177 excludes them. If v=0,
the invertible pencil forces t invertible; Gt=0 then gives T=3c0 I.
Taking normalized trace gives c0=3c0, hence T=0, contradicting invertibility.
Thus the entire real four-coefficient ansatz is excluded, including zero
coefficients, without imposing individual-port invertibility generally.

This closes the natural central mixed affine construction behind the prior
fixtures. General affine ports can use more bivectors or a different Clifford
subalgebra and remain open; the finite spectral list is not exhausted by this
ansatz. Its explicit rejection makes that change of construction necessary.

## Verification and useful continuation

The exact probe derives(2),(3), the resultant identities and every allowed
multiplicity polynomial; isolates the quartic roots; checks grade orthogonality
on actual Clifford fixtures; and reconstructs the original ten-row consumer.
Genuine grade-weight, coefficient, dimension and contraction faults follow a
green baseline. Universal proofs, finite algebraic controls and sampled actual
fixtures remain distinct evidence kinds. Independent internal review checks
real tangent splitting, trace normalization, parity and resultant projection.

The next affine problem is now finite spectral reconstruction: realize or
exclude those normalized pairs by actual grade-supported real v,t, retaining
the sign/scale of a and testing all ten rows. Nonaffine candidates can first
face (2); noncommuting candidates need an ordered reduction. This eliminates
unbounded searches over affine slopes and Jordan blocks, without importing a
positive trace or attributing supplied adapters to the source.
