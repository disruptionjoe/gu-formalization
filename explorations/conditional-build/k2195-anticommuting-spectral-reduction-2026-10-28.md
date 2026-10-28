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
result: K2195 complete anticommuting fixed-adapter exclusion
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

The fixed normalized adapter family has **no anticommuting solution**, including
nonscalar squares and Jordan blocks. The J=0 case follows from a complete
32-dimensional trace census and Pfaffian/chiral multiplicities. For J nonzero,
a quartic and an eight-value weighted trace reduction leave finitely many
multiplicity partitions; exact rational certificates exclude every one,
including singular branches and coincident missing quartic roots. This closes
the entire anticommuting family left by
[K2193](k2193-noncommuting-clifford-constraints-2026-10-28.md).

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
not eliminated by that equal-weight calculation; sections6--7 address them.

## 6. All unequal four-root multiplicities

Write the monic quartic as x⁴+A x³+B x²+C x+E, where

    A=(-129a+27c)/1080, B=-85/18,
    C=(49a+693c)/1080, E=49/54.

Equations(6) are equivalently

    A=-mu1/7+4mu_(-1)/45,
    C=7mu1-196mu_(-1)/135,
    mu2+A mu1=23/36.                         (7)

The unequal partitions of8 into four positive parts are5111,4211,3311,3221.
The exact probe derives the following exclusions, with rational Bezout
coefficients saved in its report. All computations are over C.

For5111 let t have weight5. Vieta gives mu1=(-A+4t)/8,
mu_(-1)=(-C/E+4/t)/8, mu2=(A²-2B+4t²)/8. The first two traces give
A=-4t/31+16/(279t), C=140t/31-812/(837t). The root equation gives
486z²-83z-35=0, z=t², whereas the last trace gives972z+1273=0.
Their exact substitution is nonzero.

For3311 let p,q be sum/product of the weight3 pair and r,s of the weight1
pair. Vieta gives q+s+pr=B, qs=E. The last trace gives
2pr+3q+s=-23/9, hence q-s=62/9 and q²-62q/9-E=0. The other two traces
are an invertible constant row combination of

    (12985+504s)p+(13475+168q)r=0,
    (12s+217)p+(12q+203)r=0.

Their determinant modulo the product equation is59976q+124656, coprime
to q²-62q/9-E. Thus p=r=0, so B then forces q=13/12, which fails the
product equation.

For3221 let the weight3 and weight1 roots have sum k, difference d and
product h; let the weight2 pair have sum p and product q=E/h. Here h!=0,
d!=0, and the last trace gives dp=R=124/9. Put

    U=(81h+28)/(1350h), W=49(9h+2)/(270h),
    Z=h+RU+E/h-B.

The first traces give A=-dU,C=dW, hence p=R/d,k=dU-R/d. Vieta B gives
d²Z=R², so Z!=0. Vieta C and d²=k²-4h imply

    R²(W+UE/h)-R(E/h-h)Z=0,
    R²(U²-1)+(-UR-3h+E/h-B)Z=0.

Their primitive numerators are

    72900h⁴+404514h³+1661352h²+52185h-60025,
    -218700h⁴-929556h³-12428403h²+624750h+60025.

Their exact rational gcd is1.

For4211 let the weight4 and weight2 roots have sum k,difference d,product h;
the weight1 pair has sum p,product q=E/h. Put f=k+d-p,g=(k-d)/h-p/q.
The trace equations are

    -k-p+3f/50-14g/675=0,
    -hp-kq-49f/30+49g/135=0.

Their k,p coefficient determinant is7Delta/(8100h), with
Delta=1566h²-3732h-707. If Delta=0, d!=0 requires all augmented2-by2
minors to vanish; their polynomial numerators have constant gcd7, impossible.
Otherwise k=alpha*d,p=beta*d, where

    alpha=2(27h²+957h+203)/Delta,
    beta=-7(2430h²+657h+28)/(9h Delta).

The last trace gives dp=R=124/9+2q-2h. Vieta and the difference identity
imply alpha*R=B-h-q and R(alpha²-1)=4h beta. Their primitive numerators
have degrees4 and6 and rational gcd1. These equations were obtained by
multiplication, with NO division by beta or R; their zero cases remain covered.
Thus all four-root weights, including2222 from section5, are excluded.

## 7. All three-root multiplicities, including a repeated missing root

The partitions of8 into three positive parts are611,521,431,422,332.
Append a fourth quartic root of weight0. This missing root may coincide
with a supported root; none of the following arguments assumes squarefree F.
Every quartic root is nonzero since E!=0.

### Equal supported pair:6110,4220,3320

Give the distinguished supported/missing roots weights N,0, with N=6,4,2;
give the other pair equal weights c=(8-N)/2. Let their sums/differences and
products be k,d,h and p,q=E/h. Then

    mu1=(Nk+Nd+2cp)/16,
    mu_(-1)=((Nk-Nd)/h+2cp/q)/16,
    Npd+2(N-4)(h-q)=248/9.                    (8)

The first two traces(7) form M(h)(k,p)^T=d*v(h). The probe derives M,v
from these displayed equations, not a fitted polynomial. For detM!=0 write
k=alpha*d,p=beta*d. The identities d²=k²-4h and kp=B-h-q imply the
necessary pair

    4h alpha beta-(B-h-q)(alpha²-1)=0,
    4h N beta-[248/9-2(N-4)(h-q)](alpha²-1)=0.

Each pair's primitive numerators has constant gcd. No division by alpha²-1,
beta, or d occurs in these final necessities. When detM=0 and d!=0,
all augmented2-by2 minors must vanish; their numerator gcd is constant for
each N. When d=0, k²=4h!=0 and p/k=(B-h-q)/(4h). Substituting this ratio
in both trace rows and the last equation(8) again gives numerator gcd1.
This explicitly covers a missing root coincident with the distinguished root.

### Unequal pairs:5210 and4310

Pair weights(5,0),(2,1) or(4,0),(3,1). Let pair sums/differences be k,d and
p,j, products h and q=E/h. If N1,N2 are pair weight sums and D1,D2 their
differences, the moments are exactly

    mu1=(N1 k+D1 d+N2 p+D2 j)/16,
    mu_(-1)=((N1 k-D1 d)/h+(N2 p-D2 j)/q)/16,
    mu2=[N1(k²+d²)+2D1 kd+N2(p²+j²)+2D2 pj]/32.

Use two charts for the linear trace equations(7): solve for(k,p), or for(k,d).
Their determinant numerator polynomials, with irrelevant nonzero constants
removed, are

| weights | first chart | second chart |
|---|---|---|
|5210|9504h²-13062h-6125|2430h²+639h+28|
|4310|54h²-49|2430h²+621h+28|

The two chart determinants are coprime for each partition. In a valid chart,
substitute its linear solution into the four equations

    kp+h+q=B, d²-k²+4h=0, j²-p²+4q=0,
    mu2+(-k-p)mu1=23/36.

These are linear equations F(h)(u²,uv,v²,1)^T=0 in the three quadratic
monomials of the two remaining free variables u,v. Thus detF=0. Let T be
the first three rows/columns of F and b=-F[first three rows,last column].
The vector y=adj(T)b must obey y1²-y0*y2=0. This remains necessary when
T is singular: Ty_actual=b gives adj(T)b=det(T)y_actual. No division by
detT, u, v, d or j is used.

The probe constructs F from the original moment equations, verifies exact
quadratic reconstruction, and saves rational Bezout certificates. In each
second chart, the two necessary numerators have gcd a nonzero constant
times h², excluding the chart because h!=0. At a second-chart singularity,
the first chart is valid. For4310, its two necessary numerators together
with the second determinant have gcd1. For5210 that gcd is h+1/18:
this is a REAL exceptional branch to check, not a disposable denominator.
At h=-1/18, the first-chart F has coefficient rank2 and augmented rank3,
so its original four linear equations are inconsistent. The exact matrix is
saved in the report and both ranks are checked. This closes5210 as well.

Therefore no three-root spectrum survives. Together with sections2--6,
**every anticommuting fixed normalized zero-order adapter is excluded**.
The exclusion is a necessary-condition contradiction, so no reconstruction
or sufficient spectral test is being claimed. Jordan blocks cannot repair
trace contradictions. It does not exclude general noncommuting ports for
which {v,t}!=0 or change the source-native theory.

## Verification and next question

The probe performs the full rational32-dimensional trace census, exact
factorization/elimination/Bezout/rank checks, Fock bilinear and actual commuting
fixture controls, and genuine sign/coefficient/pairing faults after a green
baseline. The written universal Pfaffian/chiral-transfer argument supplies
the multiplicity restriction; the finite partition certificates then cover
all allowed supports. The original ten rows enter through K2193's pinned
necessary contraction, never a claimed sufficient spectral replacement.

Do not requeue any anticommuting port in this fixed normalized adapter family.
The next operator question is the general noncommuting original ten-row
problem, or a distinct explicit source-native common R0/R1 map on the same
16cells/shared lower return. Mobile geometry remains a separate construction.
