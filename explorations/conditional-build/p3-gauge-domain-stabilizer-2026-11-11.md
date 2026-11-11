---
title: "Gauge covariance and fixed spectral domains are different requirements"
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: X-P2-P3
tier: T2
expected_delta: "Constrain the declared structural boundary category without a full-C decision"
actual_delta: "Constrained: all offset spectral-domain multiplier stabilizers are classified; determinant-blind mixed end gauge classes obstruct bulk extension."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Gauge covariance and fixed spectral domains are different requirements

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P2-P3
tier: T2
expected_delta: Constrain the declared structural boundary category without a full-C decision
actual_delta: Constrained: all offset spectral-domain multiplier stabilizers are classified; determinant-blind mixed end gauge classes obstruct bulk extension.

```gu-typed-objects
result: spectral-domain gauge stabilizer and end extension
carrier: L2(S1,C^r) with smooth unitary multiplication, and L2(N,S_N tensor C^r) on the auxiliary positive spin end N=RP3 x S6 LAYER=toy CHIRALITY=N/A
pairing: standard positive L2 Hermitian form ON=declared_carrier
real_structure: complex unitary category; no K77/K95 or physical reality transfer
grading: explicit Fourier cuts and K parity, not physical chirality
action_owner: N/A -- complete structural automorphism classification, no action constructed
target: fixed spectral domain versus bulk gauge extension MAP-TYPE=intertwiner
```

## 1. Native demand and new seam

SC-CHI-01/51 ASSERTS a nonchiral-total/effectively-chiral distinction; SC-GEN-02/03/54
ASSERTS native 2+1 and graded-extension claims. The physical observation bridge
remains open. A locally covariant operator does not by that fact preserve a
chosen fixed boundary domain. The [moving-gauge note](x-p1-p2-moving-gauge-naturality-2026-11-11.md)
separated covariance from fixed finite diagrams, while the
[spectral-family note](p3-equivariant-spectral-sections-2026-11-11.md) examined a
clutched varying-spectrum family. Here we classify the entire multiplication
stabilizer of fixed spectral cut data and test which end transformations are
actual bulk gauge transformations. No scalar-crossing theorem is re-counted.

This is a structural requirement for any putative action demanding this analytic
category. It neither supplies such an action nor identifies an ordinary index
with the native observed count. RA-F1, AC-F1, LT-SM8, class C and canon remain
unchanged. Full smooth U(r) multiplication is an explicitly declared category;
a native gauge group must separately map into it and preserve all demanded data.

## 2. Complete fixed-domain classification

Write z=exp(i theta), B=-i d/dtheta on H1(S1,C^r), and Q the orthogonal projection
onto modes n>=0. For arbitrary integer offsets k_j set

    K=diag(k_j), D(z)=diag(z^k_j), P_k=M_D Q M_D^-1.

Thus the j-th component of ran P_k contains exactly modes n>=k_j. All smooth
unitary matrix-valued multipliers preserving this subspace **onto itself** are
exactly

    g(z)=D(z) U D(z)^-1,   U constant in U(r),
    g_ij(z)=z^(k_i-k_j) U_ij.

Proof: conjugate by D. A unitary multiplier h that preserves ran Q onto itself
commutes with Q, since its orthogonal complement is also invariant. Applying h
to the constant coordinate vectors forbids every negative Fourier coefficient;
applying h to z^-1 times those vectors in the complement forbids every positive
coefficient. Hence h is constant. Conversely constant unitaries commute with Q.
Smoothness makes all Hs trace-domain transports bounded. Mere forward inclusion
is insufficient: multiplication by z preserves the scalar Hardy space but not
onto; it is the simplest contrary control.

For a split zero mode, take W subset C^r, k=0 on W and k=1 on Wperp. Then P_k
contains n>0 in every component and n=0 only in W. Its stabilizer has blocks

    [ A       z^-1 C ]
    [ z E     F     ]

for any constant block-unitary matrix U. In particular W=span(e1) admits
[[0,z^-1],[z,0]], a nonconstant exact domain-preserving multiplier. A blanket
constant-stabilizer statement would be false. Uniform offsets alone recover
the constant group. The formula classifies arbitrary finite offsets, not only
one split kernel.

## 3. Full operator, connection and other fixed data

For the unshifted B, [B,M_g]=-iM_g'. Therefore preserving both B and P_k requires
g constant and commuting with K: the group is product over distinct offsets a
of U(m_a). Domain preservation by itself is larger. Direct conjugation gives

    B_g=M_g B M_g^-1 = B+i g' g^-1 = B-K+gKg^-1.

For a classified stabilizer this typically changes the connection term while
leaving the selected trace domain fixed. If the zero-mode convention W is used,
the transported zero subspace is gW, not necessarily the old constant W; the
whole projection nevertheless equals the original P_k.

A different reference operator B^D=D B D^-1=B-K has P_k as its nonnegative
spectral projection. Its full multiplier commutant is precisely D U D^-1.
These are two different connections, so the statements do not contradict.
The exact probe verifies the derivative term, both commutants, and generalized
cuts with nonadjacent offsets. It also shows that vanishing determinant winding
is insufficient: diag(z,z^-1) has zero winding but fails a uniform cut.

Additional fixed matrix data F_l impose [DUD^-1,F_l]=0 coefficient by
coefficient. For a constant orthogonal grading compatible with K, this reduces
to [U,F_l]=0. For a compact constant symmetry commuting with K, its commutant
similarly intersects the U(r) above. These are exact further conditions, not
permission to discard a real structure or native Gamma/j arrows.

## 4. Genuine end transformations: an extension test

Reuse the owned auxiliary compactification M=RP3 x D7 and N=RP3 x S6 from the
[supported-index note](p3-metric-fibre-supported-index-2026-11-11.md). Choose
product spin orientations. Let x generate K1(RP3), paired to +1 by its spin
Dirac class, and beta6=[p]-4 the reduced Bott class on S6 paired to +1. Then

    K1(N)=Z{x tensor 1} + Z{x tensor beta6},
    restriction K1(M)->K1(N): a -> (a,0).

The restriction calculation was already established by the relative pair;
we use it to classify stable gauge extension. A unitary end map g with class
(a,b) extends over M after finite stabilization iff b=0. For sufficiency,
choose a bulk representative of a; its boundary restriction is stably homotopic
to g. Use a collar to realize that homotopy and obtain an extension with the
specified boundary value. Necessity is restriction functoriality. This is a
stable U category, not an assertion for an arbitrary fixed rank or native group.

For the positive spin Dirac on the closed odd manifold N, work on
L2(N,S_N tensor C^r), with a separate trivial coefficient bundle C^r. Set
P=P_D tensor I_r and let g act as I_S tensor g on that coefficient bundle.
This commutes with the principal Clifford action; [P,g] is compact. The
SU16 construction below is a rank16 COEFFICIENT transformation, not an
arbitrary automorphism of the intrinsic rank16 spinor bundle S_N. The
Toeplitz operator P g P has

    index(P g P)=-< [g],[D_N] >=-b.

Here the product pairing has <1,D_S6>=Ahat(S6)=0 and
<beta6,D_S6>=1; the x pairing is normalized to one. The sign convention matches
P on n>=0 on the circle, where P z P has cokernel dimension1.
The closed-odd-manifold Toeplitz index formula is given in
[Dai–Zhang, Introduction, equation 1.1](https://web.math.ucsb.edu/~dai/paper/dzJFA.pdf).
This is an application of that theorem and the explicit product pairing, not a
finite Fourier truncation claim.

In particular, any genuine extendible bulk gauge transformation has zero such
pairing. Nonzero b changes the extension sector; it is **not** an index change
produced by a gauge redundancy of the same bulk problem. Zero Toeplitz index
does not imply preservation of a fixed spectral projection, as Section 3 shows.

## 5. Executed determinant-blind representative

Integral cohomology H^1(N;Z)=0, since homology H_1(RP3;Z)=Z/2 and
H_1(S6;Z)=0, and the universal coefficient theorem gives H^1=Hom(H_1,Z). Thus every determinant map N->U1 is nullhomotopic. Circle determinant
winding cannot detect the b coefficient on this nine-dimensional end.

Choose a smooth degree-one map u:RP3->SU2=S3 by collapsing the complement of an
oriented coordinate ball and taking a smooth homotopic approximation. Choose
seven Hermitian 8x8 Clifford matrices c_i; on s in S6 set

    p(s)=(I+sum s_i c_i)/2.

This is a rank4 projection; orientation chooses [p]-4=beta6. Its normalization
can be checked on the entire sphere: Tr(p(dp)^6) integrates to
Tr(c1...c7) 6! Vol(S6)/2^7, where Vol(S6)=16 pi^3/15. Division by
3!(2 pi i)^3 gives +1 or -1 according to Clifford orientation. The probe
checks this exact Chern normalization, beyond sampled projector identities.
For its displayed Clifford orientation c1...c7=-iI8, giving
Tr(p(dp)^6)=-45i times the standard sphere volume form and Chern number +1.
Define on a separate trivial rank16 coefficient bundle, in SU16

    G1=u tensor p + I2 tensor (I8-p),
    G2=diag(u^-1 tensor I4, I8),  g=G1 G2.

G1 is unitary by the orthogonal projection splitting and detG1=(detu)^4=1.
G2 also has determinant1. K1 classes multiply additively, even though G1 and
G2 need not commute. Therefore

    [g]=x[p]-4x=x beta6.

This explicit determinant-one stable category has Toeplitz index -1 and no
bulk extension, even after further stabilization. Clifford and rational SU2
controls check projector rank/unitarity/determinant through exact algebra;
the Bott pairing and degree-one-map argument, not sampled matrices, establish
the class. This map is not a selected GU gauge transformation. Its role is to
show exactly which information determinant and pointwise unitary tests miss.

## 6. Released rank consequence and an unstable contrary case

The coefficient rank is not free bookkeeping. In this UNTWiSTED product-spin
problem, the minimum rank permitting b=1 is exactly5. The displayed SU16 map
is explicit, not minimal.

For the lower bound, clutch a rank-r bundle E on the suspension of N using g.
The degree-nine odd Chern character of g is the suspension inverse of ch5(E).
All products of positive-degree cohomology classes on a suspension vanish.
Newton identities therefore reduce ch5(E) to c5(E)/24. If r<5, c5(E)=0,
so ch9(g)=0 in rational cohomology. The end N is stably parallelizable
(RP3 is a Lie group and S6 is stably parallelizable), hence Ahat(N)=1.
There are no lower-character contributions to this untwisted pairing, and
index=-b implies b=0. This does not assert pointwise vanishing of a chosen
Chern differential form or a bound for an independently twisted Dirac system.

For sufficiency, the fibrations U(r)->U(r+1)->S^(2r+1) make U5->U stable
on homotopy through dimension9 and surjective in dimension10. Obstruction
theory on the nine-dimensional finite CW space N then gives
[N,U5]=[N,U]=K1(N). Thus b=1 has a rank5 representative. Multiplying by
an appropriate diagonal determinant inverse makes the representative SU5;
that determinant correction is nullhomotopic because H^1(N;Z)=0.
For rank r>=5 the same classification is injective: any map with b=0 is
homotopic in U(r) to the restriction of an a-class map from RP3. A collar
homotopy produces an actual rank-r extension over M. The elementary unitary
stable-range facts and the unstable group used next are documented in
[Püttmann–Rigas, Introduction and §1.1](https://ems.press/content/serial-article-files/42980).
The suspension and Chern-character tools are reviewed in
[Hatcher, Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf).

Below that range, zero integer or stable class is not sufficient for extension.
On S6={(y,z) in R x C3: y^2+|z|^2=1}, use the explicit characteristic map

    v(y,z)=I3-2 z z*/(1-i y)^2 in U3.

Its denominator never vanishes. It is the identity on z-perp and its remaining
eigenvalue is -(1+i y)^2/(1-i y)^2, of modulus1; at the two poles it is I3.
Püttmann–Rigas §3 identifies this smooth rational map as a generator of
pi6(U3)=Z/6. The cited homotopy theorem, not the matrix checks, supplies its
nontriviality. Define g(x,y,z)=v(y,z) on RP3 x S6. Its stable class vanishes
because K1(S6)=0, so a=b=0 and its Toeplitz index is0. If it extended over
RP3 x D7, restriction to one disk fibre would nullhomotope v, a contradiction.
Thus this actual rank3 map has zero integer obstruction but does not extend.
No native group, coefficient rank or field content is selected here.

## 7. Released real-structure transfer

The mixed integer also tests the coefficient real structure. Complex
conjugation fixes x: its SU2 representative has the quaternionic intertwiner.
It negates beta6, since conjugation negates ch3 and the reduced K0(S6) is
free cyclic. Thus conjugation on K1(N) sends (a,b) to (a,-b), integrally.

On a trivial complex coefficient bundle, suppose a same-base real or
quaternionic structure J=C times complex conjugation commutes with g. Then

    g=C bar(g) C^-1,  [g]=[bar(g)],  b=-b,  hence b=0.

Here C may even vary smoothly; inner conjugation cancels in K1. The argument
requires no positive fibre form, but does require a globally represented
same-base coefficient J and the stated commutation. It supplies a necessary
condition only, not a construction for every b=0 map. In particular the
explicit b=1 SU16 coefficient representative cannot preserve such a J.

A structure covering a base involution tau instead imposes
[g]=tau* conjugate([g]); it need not force b=0. A nontrivial coefficient bundle
also needs its own transfer. These are exact limits: the K77/K95 spinor reality,
native coflip, coefficient symmetry, and induced base map cannot be silently
identified. This is a new conditional real-structure consequence of the end
classification, not a claim about the native gauge group or physical count.

## 8. What the joint constraint now requires

For the declared analytic category, fixed principal symbol/phase, full operator,
fixed spectral domain and bulk gauge extendibility are four distinct tests.
Neither a fixed-symbol phase calculation nor a zero integer Toeplitz pairing
can replace the actual domain-stabilizer equation. Conversely a nonzero
boundary pairing cannot be presented as a legitimate bulk gauge redundancy
violating invariance. The required native group homomorphism, complete
fermion/real-structure diagram and physical-count bridge remain separate.

The all-offset stabilizer and stable extension classifications close these
structural questions; no class-wide existence/emptiness decision follows.
`tests/program-focus/p3_gauge_domain_stabilizer_probe.py` checks exact Fourier
coefficient equations without an artificial upper mode boundary, genuine
nonconstant stabilizers, forbidden modes, connection transport and actual
Clifford/SU16 matrices. Proofs above are separate from these finite controls.
