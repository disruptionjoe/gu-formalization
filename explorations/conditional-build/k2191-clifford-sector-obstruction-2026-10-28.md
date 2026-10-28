---
title: "K2191 Spectral obstruction for all commuting fixed-adapter Clifford ports"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2191_clifford_sector_obstruction_probe.py
---

# K2191 Spectral obstruction for all commuting fixed-adapter Clifford ports

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
result: K2191 all commuting fixed-adapter Clifford spectral exclusion
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

No commuting solution of the fixed normalized adapter equations exists.
K2189's rank exclusions, the six-plane argument below, and the remaining
rank2/degenerate-rank4 argument exhaust the commuting family. The proof
retains repeated eigenvalues, nilpotent parts and Jordan blocks. A necessary
spectral/trace system already contradicts, so original-row reconstruction
cannot rescue a commuting solution. Noncommuting ports remain open.

The object is full real Cl77 S128, W(3,1)+N(4,6), simple contraction,
supplied common reverse and normalized adapters. SC-OP-04 ASSERTS candidate
four-field grammar, not these adapters; SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita, not ordinary torsion. No source, ledger0.263,
canon, physical quotient, native2+1/chirality, source/full16cell/full20/K-C
verdict changes. This is conditional mathematics, not a GU falsification,
novelty, proof-assistant or external-expert claim.

## Six-plane strata proof

On an h4=q sector, q!=0, [K2189](k2189-nonaffine-clifford-reduction-2026-10-28.md) provides normalized trace a,c and tau(h)=q. A joint triangularization of v,t shows both are invertible: if lambda=0, the first Euler row is 24q mu=0, hence mu=0, contradicting P invertible; the converse uses second row 56q lambda=0. Define X=t v^-1, invertible. The pencil is an invertible odd intertwiner for X as well as V,T (all commute), so K2189's faithful-four-dimensional representation and trace reduction apply. Retain both h4 sectors in the underlying real construction; analysis of either necessary sector suffices for contradiction.

The Euler equations reduce to

    10V-2T+4a-12c+24qX=0,
    100V+36T+68a-108c+56qX^-1=0.

Thus

    V=(-35a+81c)/70 -(54q/35)X -(q/5)X^-1,
    T=-a/2-3c/14 +(30q/7)X-qX^-1.

The two coefficient vectors on X,X^-1 have determinant 12q²/5, nonzero. Taking traces gives

    tau(X)=-7(a-c)/(12q), tau(X^-1)=-3(7a-3c)/(7q).

Using T=VX² gives the annihilator

    108q X^4+(35a-81c)X³+314qX²-(35a+15c)X-70q=0.

Normalize all square-valued data by q, so q=1 algebraically (no real physical rescaling is asserted). Write monic polynomial

    P4(x)=x⁴+A x³+B x²+C x+E,
    A=(35a-81c)/108, B=157/54,
    C=-(35a+15c)/108, E=-35/54.

The degree of the minimal polynomial of X is >=3: if at most2, invertibility makes 1,X,X^-1 dependent and hence 1,V,T dependent, contradicting [K2187](k2187-affine-clifford-exclusion-2026-10-28.md). Degree is <=4 by P4.

### Characteristic polynomial equal to P4

Vieta and the two traces give 217a-171c=0 and 161a-75c=0. Their determinant is11256, so a=c=0. Then tau(X²)=-B/2=-157/108, and h=VX=-(54/35)X²-1/5 gives tau(h)=143/70, contradicting tau(h)=1. This covers minimal degree4, including every Jordan pattern; it also excludes any lower minimal-degree representation whose characteristic polynomial happens to be P4.

### Remaining cubic minimal polynomial

Let m be the monic cubic minimal polynomial. Since it divides both characteristic polynomial chi of degree4 and P4, write chi=m(x)(x-r), P4=m(x)(x-s). Necessarily r is a root of m, hence of P4; s is also a root of P4. The previous case excludes r=s. Because X is invertible and E!=0, both r,s are nonzero. This argument does not assume distinct roots of m or diagonalizability and exhausts all remaining Jordan cases.

Put d=r-s!=0, p=rs!=0, D=d², t=d(r+s). Trace changes from P4 to chi are d for X and -d/p for X^-1. The two trace equations give

    217a-171c=-108d, 161a-75c=14d/p,
    a=d(1350p+399)/(1876p),
    c=d(1242p+217)/(804p).

Hence A=d Af, C=d Cf, where

    Af=-(1116p+161)/(1206p),
    Cf=-5(324p+77)/(3618p).

Since r,s are distinct roots of P4, its remainder by x²-(r+s)x+p vanishes. Its constant remainder and the linear remainder multiplied by d are respectively

    f0=p²-p(D+4p)-Af p t-Bp+E=0,
    f1=t(D+2p+B)+Af D(D+3p)+Cf D=0.

Also t²=D(D+4p). Trace h=1, using h=(-35a+81c)X/70-(54/35)X²-1/5 and tau(X²)=(A²-2B+t)/4, gives

    -3348Dp-483D+3618pt-9782p=0.

Together with -3618 f0=0 this is a linear system for D,t, determinant

    9(90p-161)(2322p+161).

The two exceptional p values161/90 and -161/2322 give coefficient rank1 and augmented rank2, checked exactly, hence are impossible. Otherwise put H=3(90p-161)(2322p+161). Then

    D=(-13089924p³-1769202p²-1253168p)/H,
    t=(-12113064p³-1689606p²-4310579p-377545)/H.

Substitution into f1=0 and t²-D(D+4p)=0 respectively requires

    F=654105456p⁴-3130538868p³-644992956p²-832929405p-52073525=0,
    G=586116p⁴-3091284p³-758643p²-736330p-82075=0.

Their resultant is the nonzero integer

    745790970945833428732624324573391936687609669708021760000.

The exact probe also derives an exact rational Bezout identity uF+vG=1. Thus no complex p satisfies the necessary equations. No reality, positivity, diagonalizability, search exhaustion or individual inverse before proof was assumed. This closes all six-plane cases.

## Faithfulness of the six-plane transfer

The faithful-four transfer is load-bearing. V=w² and T=-u² contain no
orthogonal-volume J_R. In a fixed J_R sector the invertible odd pencil P
commutes with V,T and X, hence its two chiral blocks intertwine their
representations. Also X=-(10V-2T+4a-12c)/(24q), so X belongs to the already
faithful square algebra on that sector. A relation among 1,V,T on one chiral4 block holds on the
faithful Cl6 module of dimension8 and therefore in the actual square algebra;
it also holds in the opposite J_R sector. A complex relation among real
1,V,T supplies a nonzero real relation by real or imaginary parts. K2187
therefore excludes minimal degree<=2 here; sector-specific affine relations
are not silently allowed. This reasoning makes no semisimplicity assumption.

## 1. Common geometry of the remaining strata

K2189 leaves rank B=2 nondegenerate, and rank B=4 with E=supp(B) metric-degenerate and b=scalar(B²) !=0. The scalar b need NOT be positive. In rank2 put Bs=B, Bn=0. In rank4 put D=B wedge B, so B²=b+D,D²=0, and define

    Bs=B(1-D/(2b)), Bn=BD/(2b).

B commutes with D. BD is a bivector: its support lies in E4, hence no grade6 term, and reversion negates BD, hence no grade4 term. Both Bs,Bn are therefore bivectors and

    Bs²=b, Bn²=0, BsBn=D/2, Bs+Bn=B.

Bs is simple, nonzero and supported on a nondegenerate two-plane Es. Since {B,w}=0 gives [B²,w]=[D,w]=0, both Bs and Bn anticommute with w, and likewise u. Let K=Es-perp. The wedge equation Bs wedge w=0 restricts w to Es tensor Lambda²K plus Lambda²Es tensor K. The anticommutator with invertible Bs removes the second term. Hence

    w,u in Es tensor Lambda²K, dim K=8.

Write hs=J Bs, hn=J Bn, where J=Omega_W I_N and J²=1. Then hs²=b!=0, hn²=0 and hs,hn commute with v,t and each other. hs is pure grade8. In either hs=q sector, q²=b, h8=q+hn, while the nilpotent hn has zero diagonal in a common triangularization.

The sector traces are tau(V)=a,tau(T)=c,tau(h)=q. Indeed hs is pure grade8, V,T only grades0,4, h4 grade4, and hs hn=BsBn is pure grade4. All cross scalar traces vanish. Projectors (1±hs/q)/2 have ambient rank16, and hn has zero trace on each. This uses no positivity and permits imaginary q.

## 2. Why the trace multiplicities reduce to four, with no Jordan claim

Fix an hs sector. Since Bs is the Es two-volume, hs is a nonzero multiple of the K eight-volume, so fixing hs selects one complex halfspin module of Cl(K), dimension8. The two Es Clifford components give a16-space. In the Es volume basis, w and u are offdiagonal2x2 matrices whose entries are K-bivectors acting on that8-space. The same holds for v,t, up to nonzero complex scalar factors.

There is an explicit symmetric nondegenerate bilinear form on each K halfspin8-space. Realize Cl8 over C on Lambda(C4). Define

    B(alpha,beta)=[reverse(alpha) wedge beta]_top,
    reverse|Lambda^k=(-1)^(k(k-1)/2).

On even degrees0,2,4 and on odd degrees1,3 this form is symmetric and nondegenerate. Exterior multiplication and contraction are self-adjoint for it (move a wedge through reversal; use contraction of a top+1 form for the other identity). Thus Clifford bivectors, commutators of generators, are skew-adjoint for this form. After choosing the form matrix G, multiplying any bivector matrix by G gives an ordinary skew-symmetric matrix.

A simultaneous triangularization on the hs sector proves both v,t invertible: if either eigenvalue is zero, h=0 on that position and U=2h-8h8=-8q; the two Euler equations force the other port eigenvalue zero, contradicting P invertible. Thus all offdiagonal blocks are invertible. The even ratio X=t v^-1 has two8x8 diagonal blocks, each (up to a nonzero scalar) of the form C A^-1 with C,A invertible skew-adjoint matrices for the same G. Therefore

    det(xI-C A^-1)=det(xA-C)/det(A)

is the square of a monic quartic, by the Pfaffian identity for the skew pencil G(xA-C). Each algebraic eigenvalue multiplicity is even. The odd invertible pencil P commutes with X,V,T,h and intertwines the two8-blocks, so their traces coincide. The normalized sector trace is thus an average of FOUR eigenvalues, counted with their divided-by-two integer multiplicities.

No assertion about the size of Jordan blocks, the minimal polynomial, or absence of nilpotent parts is needed. In particular the degenerate case is treated by diagonal trace equations, not by assuming a literal quartic operator identity.

## 3. Spectral equations

On each joint diagonal, hn=0. Normalize q=1 algebraically. Set x=mu/lambda!=0. The Euler rows yield

    V(x)=(-169a+243c)/384 -(9/32)x +(77/192)x^-1,
    T(x)=(7a+99c)/384 +(39/32)x -(35/192)x^-1.

Every one of the four weighted x values solves

    P4(x)=x⁴+A x³+B x²+C x+E=0,
    A=(169a-243c)/108, B=157/54,
    C=(7a+99c)/108, E=-35/54.

The trace equations are

    mean(x)=(7a+5c)/12,
    mean(x^-1)=(28a-9c)/7,
    mean(V(x)x)=1.

The first two guarantee mean(V)=a,mean(T)=c by direct substitution. Jordan parts contribute zero to all these traces. Exhaust the number of distinct eigenvalues,1 through4.

### Four distinct roots

All roots of P4 appear once. Vieta and the first two traces imply

    421a-63c=0,1113a-459c=0,

so a=c=0. Then mean(x²)=-157/108 and mean(Vx)=311/384 !=1, contradiction.

### Three distinct roots

Let m be the product of the three DISTINCT linear factors. The weighted degree4 characteristic polynomial is m(x)(x-r), and P4=m(x)(x-s). If r=s the preceding Vieta contradiction applies even with repeated roots. Otherwise d=r-s!=0,p=rs!=0,D=d²,t=d(r+s). Trace shifts give

    421a-63c=108d,1113a-459c=-70d/p,
    a=d(2754p+245)/(6840p),
    c=d(60102p+14735)/(61560p),
    A=d Af, Af=-(7614p+2345)/(4860p),
    C=d Cf, Cf=35(54p+13)/(2052p).

The two root-remainder equations are the same structural formulas as in the six-plane proof,

    f0=p²-p(D+4p)-Af p t-Bp+E=0,
    f1=t(D+2p+B)+Af D(D+3p)+Cf D=0,
    t²=D(D+4p).

The h trace gives -7614Dp-2345D+4860pt+13140p=0. The f0/htrace determinant is nonzero except p=-2345/2754 or -335/1782; both exceptional values have coefficient rank1 and augmented rank2. Otherwise eliminate D,t. The remaining numerators require

    F=9491536260p⁴+24610284756p³+2902896225p²-5922516250p-2710624875=0,
    G=393660p⁴+1460268p³+364655p²-494550p-55125=0.

The exact rational-polynomial gcd is constant (the native probe constructs a Bezout identity equal to1). This excludes all three-distinct-root spectra, irrespective of underlying Jordan blocks.

### Two distinct roots

Write the roots r=y s and s, with y,s!=0, and weights n,4-n. Swapping roots reduces n to1 or2. Put u=s². Means are

    mx=(ny+4-n)s/4,
    mi=(n/y+4-n)/(4s),
    m2=(ny²+4-n)s²/4.

Solve 7a+5c=12mx and28a-9c=7mi for a,c. Then the h trace is linear in u.

For n=1 it gives

    u=7(1273y²+22030y+1273)/(54y(-75y²+1174y+949)).

Its exceptional denominator polynomial has no common root with its numerator, as certified by gcdex (the raw h-coefficient resultant is75611828220981745287168). Substituting u into P4(s)=P4(ys)=0 requires the quintics

    F1=60750y⁵-364763y⁴+2873112y³-55938354y²-21121534y-1006683,
    G1=315577y⁵+4991594y⁴-7884842y³+24019656y²+4697513y-973674

to vanish together. Their gcd is constant.

For n=2 the h trace gives

    u=7(1273y²+15886y+1273)/(54y(181y²+1174y+181)).

Its exceptional denominator likewise cannot vanish with its numerator (raw coefficient resultant -2427794136515245768704). The two root equations require

    F2=3258y⁵-431197y⁴-4608372y³-8280762y²-824414y-14289,
    G2=14289y⁵+824414y⁴+8280762y³+4608372y²+431197y-3258.

Again gcd is constant. Every gcd statement is certified by a rational Bezout identity in the native probe. No root sampling is used.

### One distinct root

V,T,h have one respective diagonal value a,c,1. Hence h4=h-h8 has zero diagonal, and U=-6h diagonally. The two Euler equations reduce to14a-14c=0 and168a-72c=0, so a=c=0, contradicting h²=ac=1.

## Exhaustion, scope and verification

K2189 excludes rank0/nilpotent B and rank at least8; its remaining
rank6 and nondegenerate rank4 supports are the six-plane cases above.
Rank2 and metric-degenerate rank4 with nonzero scalar B² part are the
remaining cases, now excluded by the trace-only halfspin argument.
Thus all commuting ports in this fixed normalized adapter family are excluded.
This proof does not cover noncommuting ports, a different adapter, mobile
geometry, or a source-native common R0/R1 reality-density construction.
It does not establish a general source-operator or physical obstruction.

The universal evidence is the written geometry, faithful-sector transfer,
Pfaffian multiplicity theorem and exhaustive algebraic case division.
The native exact probe reconstructs the Euler solution, trace identities,
quartics, exceptional systems and rational Bezout identities. It also
checks the Chevalley pairing on both concrete halfspin modules and a
nonzero degenerate rank4 split fixture. Those fixtures verify identities;
they do not replace the universal proof or assert an Euler solution.
Planted faults alter actual coefficients or trace targets. Reproduction:
`tests/channel-swings/k2191_clifford_sector_obstruction_probe.py`, with
`--write` to regenerate its dependency-hashed report. No finite numerical
search is used as an exhaustive proof, and no proof-assistant or external
certification is claimed.
