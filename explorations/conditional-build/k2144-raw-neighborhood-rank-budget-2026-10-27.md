---
title: "K2144: Raw neighborhood rank budget and integrable no-departure"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source selection, apparatus construction or GU recovery
scripts:
  - tests/channel-swings/k2144_raw_neighborhood_rank_budget_probe.py
---

# K2144: Raw neighborhood rank budget and integrable no-departure

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
result: Raw neighborhood rank budget and integrable no-departure
carrier: K2132 complex32 graph in fixed K77 core128, real1280 joint jets LAYER=toy CHIRALITY=N/A
pairing: inherited S and original common-H raw coefficient class ON=declared_carrier
real_structure: real coefficients and complex adjoint as stated
grading: graph t/Z multiplicity, not observed chirality
action_owner: repository-construction -- explicit conditional object below
target: dimension bound on coupled admissible jets near P0 MAP-TYPE=intertwiner
```

## 1. The new question is a neighborhood, not another curve

[K2141](k2141-full-graph-raw-tangent-2026-10-27.md) certifies zero allowable first
jets at P0. That fact alone does not persist as zero jets nearby: the raw-column
rank may increase. We combine its actual certificate with the universal homogeneous
coefficients of [K2028](k2028-all-grade-raw-common-form-2026-10-24.md).
The result is a genuine open-neighborhood bound, with no claimed radius:

    dimension of the admissible JOINT real1280 first-jet space <= 3.       (1)

At least1277 linear obstructions persist. This is not three moving graph coordinates,
not rank(Dz)<=3, and not an integrable distribution. A one-dimensional linear space
of derivative matrices may contain a rank-four matrix. Neither existence nor
integrability of any surviving nonzero jet is established.

## 2. Native persistent kernel and exact rank budget

Use exactly K2141's smooth finite-dimensional real equations

    F(z)c+T(z)v=0, c in R16620, v in R1280, z=0 at P0.                  (2)

This includes upper closure, normal leakage and the inherited-current equation
replaced by its equivalent expression jointly with leakage. The chart inverse is
on ran E as in K2141; no full D0 inverse or lower-return equation is introduced.
The stored32 systems sum to raw rank16604. The globally COUPLED target obstruction
rank is1280, hence rank[F(0),T(0)]=17884. It is this global certificate, not
independent copies of local target labels, that supplies the augmented rank.

K2028 constructs13 independent real coefficient vectors in the purely imaginary
common-H branch. Nine induce zero on the ENTIRE core; the image of the other four
is i span_R{I,C1,C2,C3}. Upper closure holds on the entire core before restricting
to a graph. Every K2132 graph projector P commutes with each Cj; the native S also
commutes with Cj, verified in [K2120](k2120-inherited-core-current-2026-10-27.md)
and directly by the adjacent probe. Thus A=iCj and iI obey [P,A]=0 and
SA+A*S=0. Zero-image vectors obey both automatically. At v=0 the modified
current row is equivalent to the original row. The SAME13 raw vectors therefore
lie in ker F(z) for every point of this graph chart. Their independence is inherited
from K2028's complete coefficient kernels, not inferred from their four-dimensional
image. This proves rank F(z)<=16620-13=16607.

Choose a nonzero17884 minor at0. Smoothness preserves it on an open neighborhood,
so rank[F(z),T(z)]>=17884 there. The quotient map v -> T(z)v modulo im F(z) has
rank rank[F,T]-rank F. Its kernel, the admissible jet space, has dimension

    1280+rank F-rank[F,T] <=1280+16607-17884=3.                       (3)

There are16 raw homogeneous directions at0. The universal13 account for all but
three possible rank increases. Proving that the remaining three persist, or
computing their actual interaction with the target, is the next sharper question.
We have not supplied a uniform numerical radius or the smallest singular value.

## 3. Quantitative coefficient cost and a stronger regularity hypothesis

Take a norm-one fixed left annihilator L0 with ker L0=im F(0), and let
alpha=sigma_min(L0 T(0))>0. For local Lipschitz constants LF,LT of F,T,
applying L0 to (2) gives

    alpha ||v|| <= LF |z| ||c|| + LT |z| ||v||.

On a small ball with LT |z|<=alpha/2 (no restriction from LT if it is zero),

    ||Dz|| <= C |z| ||c||, C=2LF/alpha.                              (4)

For an absolutely continuous spacetime path gamma parametrized by arc length,
assume the equations and this chain rule hold almost everywhere and
c(gamma(s)) is integrable. Wherever z is nonzero and remains in that small ball,

    |log(|z(gamma(b))|/|z(gamma(a))|)|
       <= C integral_a^b ||c(gamma(s))|| ds.                         (5)

Gronwall gives no departure from zero along each such path. A C1 selector on a
connected open domain is constant P0 if it equals P0 once and every point can be
joined to it by piecewise C1 paths with locally integrable coefficient norm
along their compact subpaths. Local boundedness implies this hypothesis;
ambient L1 integrability alone does NOT imply integrability on every chosen path.
Apply the local estimate until first exit; zero continuation prevents exit.
This extends K2141's bounded-coefficient condition without claiming arbitrary
singular coefficients harmless. The logarithmic cost must diverge to reach or
leave zero through a nonzero branch under the same inequality.

## 4. Genuine countercontrols and transport boundary

The analytic scalar system z c+z'=0 has injective quotient tangent at0, but
z(t)=epsilon exp(t), c=-1 is a nonconstant bounded-coefficient solution in any
small punctured neighborhood. Its raw rank jumps from0 to1. This rejects the
false inference that injective quotient at a point implies an open rigidity theorem.
The separate solution z=t^2, c=-2/t for t!=0 (with any finite c(0)) reaches0
with derivative0 and obeys the equation there, but its coefficient cost is
nonintegrable. It tests the actual hypothesis, not a native raw realization.
Conversely c(t)=1/sqrt(t) on t>0 is unbounded yet integrable; the scalar homogeneous
ODE still has unique zero solution from0. These scalar controls distinguish
boundedness, path integrability and arbitrary singularity.

[K2129](k2129-rotated-positive-sector-raw-equations-2026-10-27.md) already warns
that the native Z rotation is not a symmetry of the full raw upper contraction.
Cl4 commutation and K2138 graph-connection holonomy do not prove raw-class covariance.
A genuine distinct-sector transport needs an invertible coefficient map and
upper-output map intertwining the complete raw residual, preservation of S and
C_mu, and a core map sending P0 to a different projector. None is supplied here.
The rank budget narrows the next calculation without falsely choosing a symmetry.


## 5. Released follow-through: extract the three directions, then test transport

The extra base homogeneous dimensions all lie in XOR coset64={64,65,126,127}.
Every other nonzero-nullity coset is fully accounted for by K2028's universal13.
The adjacent probe now RECOMPUTES just this block:556 raw columns,3234 distinct
primitive rows, exact rational and mod101 rank549, with a seven-dimensional
right kernel. It stores the actual seven vectors in the original coefficient
basis, checks every kernel equation, embeds and checks the four inherited
universal vectors in this coset, then chooses three independent quotient
representatives. The four universal vectors here all have zero core image.
Eight original gamma contractions (four output blocks, real/imaginary input)
cross-check the inherited fast contraction.

For each of the three extras the probe reconstructs ALL14 upper outputs and
the core action in the original native coordinates. All satisfy P0 closure,
leakage and current. Their full-core upper residuals are nonzero. At the
distinct K2132 noncircle sector cosh(u)=5/3, sinh(u)=4/3, each has upper leakage;
the JOINT residual map on their real three-dimensional span has exact rank3.
Thus NO nonzero linear combination of these fixed extra representatives persists
as a homogeneous solution at that sector, even allowing the four universal
zero-image additions. Deleting one actual extra direction drops the residual
rank and is detected; changing a raw kernel coefficient breaks an original row.

Since every other base-kernel direction is already universal, the intersection
of the homogeneous kernels at P0 and this noncircle sector is EXACTLY the universal13.
It follows that the raw coefficient vectors homogeneous for EVERY graph are
exactly those13. Along the native hyperbolic curve P(u), the restricted residual matrix is
real analytic for finite real u. A rank3 minor nonzero at cosh(u)=5/3 cannot
vanish identically. Its zeros cannot accumulate at0, so the fixed-extra residual
rank is3 also for all sufficiently small nonzero u (without a supplied numerical
radius). Hence the common FIXED homogeneous coefficients throughout any open
P0 neighborhood are exactly13 as well. This closes the fixed-universal-kernel
question, not the moving-kernel question. For example F(z)=[-z,1] has constant rank1 and moving
kernel span{(1,z)}, yet its kernels at0 and1 intersect trivially. Therefore an
exact universal13 does not show that the native raw rank actually increases
near P0: extra kernel vectors could rotate with z.

This rules out the cheapest constant-coefficient transport of these extra
directions, not all smooth c(z), not every raw homogeneous vector at the new
sector, and not its full1280 first-jet problem. A new sector may have homogeneous
vectors outside the base kernel. The next calculation must determine the moving
kernel/target intersection or a smooth elimination of all other coefficients;
it must not reuse this restricted rank3 as a full-sector verdict. The <=3
neighborhood budget and path-integrability theorem remain unchanged.

## Acceptance and source boundary

The adjacent probe checks finite exact identities, certificate arithmetic and altered-input
controls. Universal statements use the written arguments and independent internal specialist
review; finite controls do not prove continuum claims. No external-expert certification,
proof-assistant verification, remote CI or novelty claim is made. SC-OP-04 ASSERTS candidate
operator grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action
prerequisite. LT-SM8/LT-GR6b, ledger0.263, source polarity and canon are unchanged.
