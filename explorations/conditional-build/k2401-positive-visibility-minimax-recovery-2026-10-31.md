---
title: "K2401 Exact positive-visibility minimax mirror recovery"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional all-CPTP finite-instrument theorem; no hardware or native GU verdict
scripts:
  - tests/channel-swings/k2401_positive_visibility_minimax_recovery_probe.py
---

# K2401 Exact positive-visibility minimax mirror recovery

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2401
carrier: K2398 normalized two-loss survivor-sign and planar clock-qubit instrument with untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing and worst-law half-diamond norm ON=declared_carrier
real_structure: complex CPTP qubit channels and real mirror-axis moments
grading: classical sign, two mirror laws and optional good/bad flags
action_owner: repository-construction -- stipulated QND instrument and supplied clock visibility
target: one fixed decoder attaining the all-CPTP minimax value MAP-TYPE=evaluation
```

## Result and the remaining question

[K2398](k2398-uncertain-clock-law-recovery-2026-10-31.md) solved zero visibility and visibility at least1/2, and reduced the missing interval to a convex program. Here **every0<nu<1/2** has an explicit rank-two optimal decoder determined by one uniquely isolated algebraic root. A supporting-hyperplane lower bound and a matching physical channel prove global optimality. No numerical optimizer status or Bell-overlap replacement is used.

The two laws put probability a=1/4 at+X and b=3/4 at either+Z or−Z; their convex mixtures are included. A single decoder must serve the unknown law. The common symmetries from K2398 reduce all CPTP decoders to translation cX and diagonal Bloch matrix diag(x,y,z), with nonnegative c,x,z. The recovered planar trace and skew are

    f=ac+nu(ax+bz),    |k|=bc,
    E=(1+sqrt((2-f)^2+b^2c^2))/4.                         (1)

This applies to the normalized two-loss branch; complete flagged error is wE under K2398's mirror-family good-flag lower bound, even if good recovery is freely chosen. It is not a claim about arbitrary uncertainty sets. Imported quantum mechanics and the QND/sign instrument are assumptions. SC-META-53 remains UNCERTAIN and LT-GR6b remains open; no source/ledger/canon status changes.

## 1. Support function from the full CP constraints

For L>=0,d,e>0, maximize Lc+dx+ez. The two Choi blocks require

    c²+(y+z)² <= (1+x)²,
    c²+(y-z)² <= (1-x)²,    c<=1-x.                      (2)

For fixed c,x, e>0 makes maximal z optimal. Write U=sqrt((1+x)²-c²), V=sqrt((1-x)²-c²); (2) implies2z=(y+z)-(y-z)<=U+V. Equality is achieved by the following y,z, saturating both inequalities:

    z=(sqrt((1+x)²-c²)+sqrt((1-x)²-c²))/2,
    y=(sqrt((1+x)²-c²)-sqrt((1-x)²-c²))/2.

These imply x=yz and c²=(1-y²)(1-z²), with0<=y,z<=1. Conversely every such y,z yields a valid CP-boundary channel, so this is a consequence of the complete constraints, not an assumed rank restriction.

At fixed z, Cauchy-Schwarz on the vector(sqrt(1-y²),y) gives

    max_y L sqrt(1-z²)sqrt(1-y²)+dzy
      =sqrt(L²-(L²-d²)z²).

Maximize this plus ez over0<=z<=1. If L²<=d(d+e), its maximum is d+e at z=y=1. Otherwise its unique interior maximizing z gives

    H(L;d,e)=L sqrt((L²-d²+e²)/(L²-d²)).                 (3)

For L<=d, the function is increasing and the same endpoint branch applies. For L>d it is concave; its derivative at z=1 is nonnegative exactly at the stated threshold. This covers the entire domain without assuming the interior formula has a positive denominator where it does not.

## 2. Unique root and actual decoder

Write v=nu∈(0,1/2). For ell∈(2v,1) define

    h(ell)=ell/4 sqrt((ell²+8v²)/(ell²-v²)),
    c(ell)=(ell²-4v²)(ell²+2v²)
            /[(ell²-v²)^(3/2)sqrt(ell²+8v²)].             (4)

There is exactly one ell_* in this interval solving

    c(ell)[9+(1-ell)²]=4(1-ell)[2-h(ell)].                (5)

The optimal channel is

    y=3v²/(ell_*²-v²),
    z=3v ell_*/sqrt((ell_*²-v²)(ell_*²+8v²)),
    x=yz,   t=c(ell_*)X.                                 (6)

Because ell>2v, 0<y<1 and 1-z²=(ell²-4v²)(ell²+2v²)/[(ell²-v²)(ell²+8v²)]>0. Thus0<z<1, x<1 and c>0. Both Choi determinants vanish and both blocks have positive trace in the open interval, giving rank two. Equations(2) specify a physical CPTP map; a Choi factorization supplies Kraus operators if an implementation needs them. The exact optimal normalized error is

    E_*(v)=[1+(2-h(ell_*))/sqrt(1+(1-ell_*)²/9)]/4.        (7)

At v=0 the established endpoint is mixed preparation c=4/5; do not insert zero into the singular interior expressions. For v>=1/2 the midpoint-law lower bound from K2398 makes identity optimal, E_*=(3-v)/4.

## 3. Direct global certificate and uniqueness

Put s=(1-ell)/3, L=a-bs,d=va,e=vb. Every feasible decoder satisfies

    sqrt((2-f)²+b²c²)
      >= [(2-f)+sbc]/sqrt(1+s²)
      >= [2-H(a-bs;va,vb)]/sqrt(1+s²).                   (8)

The first is a scalar-product bound; the second is precisely the support function. It does not interchange a minimization and a maximum.

Let F(s)=2-H(a-bs;va,vb) on0<=s<=(1-2v)/3. Its derivative is F'=bc and F''<=0 because H is a convex support function. The derivative sign of F/sqrt(1+s²) is N=(1+s²)F'−sF. Therefore

    N'=sF'+(1+s²)F''−F <= H+sbc−2=f−2<=−1.

The last inequality follows from the nuclear norm<=1 of the physical recovered planar block, established on the original instrument in K2398. At s=0, c>0 so N>0. At the upper endpoint c=0 and F=2-v>0, so N<0. There is one zero, equivalent to(5). At that zero, the support-maximizing channel obeys bc=s(2-f), so it attains both inequalities in(8). This proves existence, uniqueness of the scalar root and the global all-CPTP value. It does not assert uniqueness of every nonsymmetric physical realization related by the averaging symmetries.

For any ell in the interval, (8) gives a rigorous lower bound and channel(6) gives a rigorous upper bound. Thus root isolation can be converted into a practical exact optimality bracket without evaluating an algebraic matrix numerically. The gap is the norm-versus-support mismatch and vanishes at alignment. This supplies a certified stopping criterion for approximation of the decoder.

## 4. Rational visibility certificate and independent control

For v=1/4, define

    p(ell)=-32ell^5+302ell^4+22ell^3-40ell²+ell-10.

The unique root is isolated in(1/2,3/4) by

    p(ell)²−8(1-ell)²(16ell²-1)^3(2ell²+1)=0.            (9)

Before squaring, the positive numerator is

    P=[9+(1-ell)²](ell²-4v²)(ell²+2v²)
      +(1-ell)ell(ell²+8v²)(ell²-v²),

and the positive right side is8(1-ell)(ell²-v²)^(3/2)sqrt(ell²+8v²). Both are positive for2v<ell<1. Hence squaring preserves the branch there. The stationarity residual is negative at1/2 and positive at3/4; equation(8) proves uniqueness. The probe uses rational polynomial bisection and rational square-root enclosures to produce an actual rigorous value bracket. Approximate decimal display is informational only.

An independent simple feasible channel has

    c=x=12/25,  y=3/5, z=4/5.

At v=1/4 it gives f=3/10, |k|=9/25 and error(1+sqrt(7549)/50)/4, strictly below identity11/16. The exact squared radial gap is429/10000. The probe checks its actual Choi matrix, trace preservation, original sign-block composition and Bell-output trace norm. This is an upper-bound control, not the optimal channel.

## 5. Unknown visibility without a nonphysical relaxation

K2398's finite-axis confidence interface assumed known visibility. For unknown common visibility v∈[v_min,v_max]⊆[0,1], take masses p_j>=0,sum p_j=1 and auxiliary weights

    v_min p_j <= r_j <= v_max p_j,
    m=sum p_j n_j,  Q=sum r_j n_j n_j^T.                 (10)

Every point corresponds to an actual axis-dependent visibility law v_j=r_j/p_j; p_j=0 forces r_j=0. The family includes every common visibility law through r_j=vp_j. It generally enlarges that family: it is exact for axis-dependent visibility and conservative for the common-visibility question.

The measurable sign and pointer correlations are E[sign]=m_j and E[sign·pointer_i]=Q_ij. Confidence slabs are affine in(p,r), so a finite physical polytope results. Recovery uses B=t m^T+A_plane Q. Its normalized error is [1+sqrt((2-tr B)²+(B12-B21)²)]/4, using the general K2398 formula rather than the mirror-specific bc. This remains valid because this is still the same measure-and-prepare sign instrument, common symmetries and a physical channel. Maximizing over vertices is exact for this enlarged polytope. This avoids pretending a bilinear product vM is an affine common-visibility parameterization.

A simultaneously covered set permits a data-selected decoder frozen before deployment; calibration/deployment drift, loss weight and implementation error still require separate budgets. A tested fixed decoder's complete error is bounded by w times its certified worst-law error plus a justified complete-channel implementation allowance epsilon. Improvement over identity is useful only if that allowance is smaller than the certified ideal margin. Costs include obtaining rare flags, preparation, sign control, damping, rotation and reset. No physical cost/rate/sample is fabricated.

## Review and provenance

Preflight lenses compare a direct CP support proof with numerical minimization and law-dependent polar optimization. The support route removes the uncertified optimizer and preserves the actual diamond objective. Postflight targets wrong square-root branch, lost sign normalization, a hidden law-dependent decoder and nonphysical confidence sets. The specialized formulas are repository-derived, with no novelty claim. General norm/certificate background: [Watrous, Semidefinite programs for completely bounded norms](https://cs.uwaterloo.ca/~watrous/Papers/SDPforCBnorms.pdf).

The narrow exact probe and independent internal review support these conditional claims. They are not external-expert, hardware or proof-assistant certification. General non-mirror uncertainty and complete measured resource optimization remain separate successors.
