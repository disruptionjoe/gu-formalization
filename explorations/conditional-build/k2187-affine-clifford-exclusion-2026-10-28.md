---
title: "K2187 Exclusion of commuting affine-square Clifford ports"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2187_affine_clifford_exclusion_probe.py
---

# K2187 Exclusion of commuting affine-square Clifford ports

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
result: K2187 complete affine-square exclusion and nonaffine support constraint
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

There are no commuting affine-square ports satisfying the fixed normalized
adapter equations. Here affine-square means

    V=v^2=a+X, T=t^2=c+zX, <X>0=0,

with real scalar a,c,z, together with the vertical case V=a scalar and T
nonscalar. Thus the result covers every affinely dependent pair 1,V,T.
The scalar and proportional cases were already
excluded. The new result closes the remaining rank-four class of K2185,
including metric-degenerate support. It removes the entire affine spectral
reconstruction search, not merely a chosen coefficient ansatz. General
nonaffine commuting ports and noncommuting ports remain open.

The model is the same full real Cl77 S128, W(3,1)+N(4,6), simple contraction,
supplied common reverse and normalized adapters as K2185. Only the pencil
7v-15t is assumed invertible; neither individual port is inverted. SC-OP-04
ASSERTS candidate four-field grammar, not these adapters. SC-GEO-55 ASSERTS
displacement from gauge-rotated Levi-Civita, not ordinary torsion. No GU
falsification, source/full16cell/full20/K-C result, physical quotient, native
2+1/chirality, ledger0.263, LT-SM8/LT-GR6b/AC-F1 or canon verdict follows.

## 1. The inherited algebra and the remaining geometric object

Use [K2185](k2185-clifford-spectral-obstruction-2026-10-28.md) and its exact
scalar-grade-square exclusions. Write v=I_N w, t=Omega_W u for normal
trivectors w,u. Commutativity gives {w,u}=0, hence

    wu=B+C, B=(wu)_2, C=w wedge u,
    J=Omega_W I_N, J^2=1, h8=JB, h4=JC.

J commutes with even normal elements, so h8^2=B^2 and h4^2=C^2. Centrality
from the actual normalized equations gives {B,w}={B,u}=0, in particular
B wedge w=B wedge u=0. K2185 excludes ranks0,2,6,8,10, so rank B=4.
Let E=supp B have dimension4 and D=B wedge B. Then D is nonzero and is a
decomposable top four-blade of E. The bivector identity is

    B^2=b+D, b=<B^2>0.                              (1)

Rank is exterior alternating rank; it does not assume the metric restricted
to E is nondegenerate.

The inherited affine quadratic is A X^2+d X+C0=0, with A nonzero. Both
B^2 and C^2 lie in span{1,X}: K2185 equation(1) expresses 1344 times each
square as a quadratic polynomial in commuting V,T, and reduction by the
quadratic gives this assertion. Since B^2 is not scalar, its X coefficient
beta is nonzero. Taking scalar parts, using <X>0=<D>0=0, gives

    D=beta X, beta !=0.                             (2)

Every decomposable blade has scalar square, including a null blade. Thus
X^2 is scalar. This is the geometric restriction that arbitrary faithful32
spectra alone did not enforce.

## 2. Degenerate support cannot survive

A decomposable four-blade D has D^2 equal to its scale squared times the
Gram determinant of E (the grade-four reversal sign is positive). If the
restricted metric is degenerate, D^2=0 and (2) gives X^2=0.
[K2183](k2183-commuting-trace-descent-2026-10-28.md) excludes this nilpotent
square defect; this is not an inference that a nilpotent matrix is zero.
For completeness its operator quadratic and traced identity give, when X^2=0,

    d X+C0=0, L<X^2>0+C1=0.

Independence of 1,X forces C0=0; X^2=0 then forces C1=0. For a!=0 normalize r=c/a:
C0/a^2=49-301r+108r^2 and C1/a^2=637-133r-72r^2 have nonzero resultant
(the probe recomputes it). The a=0 branch is already excluded by K2183.
Therefore E must be metric-nondegenerate.

## 3. Orthogonal factorization closes the rank-four remainder

Choose K=E-perp, so N=E orthogonal-direct-sum K. The metric may be indefinite
on either factor. The metric-independent wedge-support theorem gives

    w,u in Lambda^3 E plus (Lambda^2_primitive E tensor K).

On wedging w and u, terms with more than four E legs vanish. Therefore

    C=w wedge u in Lambda^4 E tensor Lambda^2 K,
    C=D H for some H in Lambda^2 K.                (3)

D is invertible because D^2!=0. It commutes with H, and the orthogonal
Clifford product equals the exterior product on the disjoint factors. Hence

    C^2=D^2 H^2 in Cl(K).                          (4)

But section1 also gives C^2 in span{1,X}=span{1,D}. The PBW exterior basis
for Cl(E orthogonal-direct-sum K) shows

    Cl(K) intersection span{1,D} = real scalars.   (5)

Indeed D is a nonzero pure E four-blade, absent from every pure K exterior
component. Equations(4),(5) force C^2 scalar, contradicting the K2185
scalar-h4-square theorem. This exhausts rank4, including its degenerate
strata, and therefore the full commuting affine-square class.

No Euclidean positivity, diagonalization of B, individual port inverse,
source-selected real structure or physical quotient was inserted. The only
new inverse implicit in choosing an orthogonal complement is justified by
the already proved nondegeneracy of E.

## 4. The vertical affine line is also excluded

The representation T=c+z(V-a) does not cover scalar V and nonscalar T.
It must not be hidden by swapping asymmetric equations. Instead set V=a,
T=c+Y, tau(Y)=0 in the original commuting square and trace identities:

    -54Y^2+(-259a+54c)Y+C0=0,
    C0=49a^2-301ac+108c^2,
    144tau(Y^2)+637a^2-133ac-72c^2=0.

Taking the trace of the first equation and eliminating tau(Y^2) gives

    2303a^2-2807ac+648c^2=0.                     (10)

If a=0, then c=0 and Y^2=0. The commuting v,t have v^2=0 and t^4=0,
so P=7v-15t satisfies P^5=0 by the binomial expansion, contradicting
its required invertibility. No inference from nilpotent to zero is used.

If a!=0 normalize r=c/a and Y/a. The quadratic coefficient is -54.
A repeated root, with trace zero, would require -259+54r=0. Its resultant
with Evert=2303-2807r+648r^2 is10925334, nonzero. Distinct roots give
multiplicities m,32-m in the faithful normal32 representation; nonscalar
Y requires 1<=m<=31. The trace-zero multiplicity identity gives

    -54(32-2m)^2(49-301r+108r^2)
      +m(32-m)(-259+54r)^2=0.                    (11)

Writing k=m(32-m), the exact resultant of(10),(11) is

    7001316[21990393k^2+20902856704k-5674993975296].

It is nonzero for every integer m=1,...,31; the probe supplies31 exact
Bezout identities. A shorter proof avoids even this enumeration. The
discriminant of Evert is1909873, strictly between1381^2 and1382^2, so r
is irrational. Reduction of(11) modulo Evert gives

    [(41391k-18450432)r-31213k+37029888]/2.

For integer0<=k<=256 the coefficient of r is at most-7854336, hence nonzero.
Vanishing would force r rational, a contradiction. This is a structural
arithmetic obstruction, not a numerical root search, and needs no even
multiplicity restriction. All vertical-line candidates are excluded too. This completes affine dependence, rather than
just graphs over V.

## 5. Released consequence for the nonaffine question

The necessary support statements still give rank B<=6 for all commuting
ports. The graph and vertical exclusions imply 1,V,T are linearly independent
for every remaining commuting candidate. Proportional square defects and
scalar V with nonscalar T are no longer candidate constructions.

For a general nonaffine commuting candidate with rank4 and nondegenerate E,
centrality supplies a further reduction without invoking the affine
quadratic. From {B,w}=0 obtain [B^2,w]=[D,w]=0, and similarly for u.
D anticommutes with Lambda^3 E and commutes with Lambda^2 E tensor K.
Because D is invertible, the Lambda^3 E parts vanish. Thus w and u lie in
Lambda^2 E tensor K. For each K coefficient alpha, both

    B wedge alpha=0 and <B alpha>0=0               (6)

are necessary: {B,alpha} has only scalar and four-form grades, which cannot
cancel. These are two linear functionals on Lambda^2 E.
The wedge functional corresponds to D B; the metric functional corresponds
to B under the nondegenerate induced bilinear form. Dependence would give
D B=lambda B. This can occur for self-dual/anti-self-dual B, so no universal
four-dimensional coefficient-kernel count is claimed. The executable
controls exhibit both a dimension4 generic kernel and a dimension5 special
kernel. In particular a dimension count cannot substitute for actual
B=(wu)_2, centrality, invertible pencil and all ten original equations.

A concrete nonaffine control uses normal signs ++++------, alpha=n13,
beta=n23+n14, w=alpha n5+beta n6 and u=beta n5+2alpha n6.
It has actual B=(wu)2=-n12-n34, C=(wu)6=-2n123456 and satisfies the
centrality conditions. Its squares are

    V=3-2n1234+2B n56, T=-6+2n1234+4B n56.

Thus 1,V,T are independent: centrality alone does not imply affine squares.
The probe verifies its pencil is invertible and all ten original residual
rows are nonzero. This is a concrete rejected structural candidate, not an
existence witness and not a claim that all nonaffine ports are excluded.

The orthogonal reduction does not cover a degenerate E in the general
nonaffine problem: section2 used the affine quadratic essentially. Nor does
it imply V,T lie in one common quadratic algebra. Mixed E/K grade4 terms
can remain in the individual squares. Noncommuting ports require an ordered
analysis; none of these commutative factorizations transfers to them.

## Verification and continuation

The written argument is universal within its hypotheses; finite exact
Clifford controls check its load-bearing identities on definite, indefinite
and null support, the PBW intersection, the nonaffine coefficient kernels
and actual predecessor original-row failures. Exact resultants check the
nilpotent contradiction and all vertical spectral multiplicities. Faults alter product signs, dual factors, wedge
coefficients, Gram data or the nilpotent polynomial, after a green baseline.
These checks supplement independent internal proof review; they are not a
proof-assistant, external-expert, novelty or GU physical certification.

Do not reconstruct any affine spectral candidates after this result. Compare
nonaffine commuting reconstruction with noncommuting ports and an actual
common R0/R1 reality-density map or mobile deficient-stratum source
construction. Preserve all prior scalar/homogeneous exclusions and source
boundaries. This theorem removes a search branch; it does not complete GU.
