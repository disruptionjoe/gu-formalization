---
title: "K2192 Paired detector inequality and global threshold saturation"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, vacuum output field energy only
scripts:
  - tests/channel-swings/k2192_detector_smoothing_and_sign_probe.py
---

# K2192 Paired detector inequality and global threshold saturation

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
result: K2192 paired heavy-branch inequality and strictly increasing energy frontier
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

For the supplied binary diagonal detector, the exact minimum vacuum output
field energy F(d) is continuous and strictly increasing on 0<=d<=3/4.
Every threshold optimum saturates its required contrast: V(d)=F(d).
The proof controls the branch carrying at least half the weighted moment;
single-branch counterexamples from K2190 do not satisfy that condition.
The ratio F(d)/d also strictly increases for d>0. These results release a
unique scalar inverse energy frontier and an equality-safe terminating
approximation procedure; they do not imply a unique optimizing detector.

The model is the fixed positive scalar Fock vacuum and photon-added signal,
positive square-root binary diagonal Kraus instrument, one real squeeze per
reported outcome. Costs are output FIELD energy only; apparatus, clock,
preparation, switching, reset and total work are excluded. SC-META-53 remains
UNCERTAIN. LT-SM8/LT-GR6b, source, ledger0.263, canon and physical quotient
are unchanged. No new numerical half-contrast bracket, novelty,
proof-assistant or external-expert certification is claimed.

## 1. Uniform capped-branch bound

Let p_n=(3/4)4^-n, 0<e_n<1, z_n=p_n e_n, b_n=sqrt(e_n), W_n=(n+1)p_n, R=R(z), T=T(z), C=40/3, and J=D(z)-2/3, where D=DT(z)[p]. D may be +infinity for a general profile; at [K2188](k2188-detector-variational-structure-2026-10-28.md) minimizers it is finite.

The full-tail identities are

    J=(1/4) sum W_n (b_(n+1)-b_n)^2/(b_n b_(n+1)),
    Delta:=T-(4/5)R
      =sum W_n (b_(n+1)-b_n)[(2/5)b_n-(1/10)b_(n+1)].

The second follows from d=sum W_n(e_(n+1)-e_n), plus K2188's Dirichlet identity. All its terms converge absolutely because caps give uniform bounds and sum W_n=4/3.

Weighted Cauchy-Schwarz gives

    Delta^2 <= J sum 4 W_n b_n b_(n+1)
                           [(2/5)b_n-(1/10)b_(n+1)]^2
            <= (12/25) J.                                      (A)

The last inequality is the elementary cap bound ab(4a-b)^2<=9 on [0,1]^2. If 4a-b<0, the left side is <=1. If 4a-b>=0, its derivative in a is b(4a-b)(12a-b)>=0, so a can be increased to1; b(4-b)^2 is increasing for b in[0,1] and ends at9. Thus the edge expression is at most9/25, and multiplying by sum W_n=4/3 gives12/25. For J infinite, (A) holds as an extended bound; for finite J use finite sums and pass to the limit.

At the unique optimizing squeeze s, RA'(s)=CT, A(s)=41s^2/6+3/(2s^2). Hence

    Delta=(R/C)(A'(s)-32/3).

If R>=5/12, (A) implies

    CsJ >= (125/4608)s(A'(s)-32/3)^2.                            (B)

## 2. Scalar bound

Let Ep(s)=(5/6)A(s)-(80/9)s+35/18. Exact polynomial division gives

    (125/4608)s(A'(s)-32/3)^2-Ep(s)
        =(s-1)^2 P(s)/(41472 s^5),

    P(s)=210125s^6-143910s^5-1305s^4+60660s^3
          +30375s^2+20250s+10125.

At u=s-2/3, the coefficients of P(u+2/3), from constant to u^6, are

    39611405/729, 13281950/81, 9299005/27, 17894660/27,
    2759485/3, 696590, 210125.

They are all strictly positive. Consequently the scalar difference is nonnegative for all s>=2/3, and strictly positive unless s=1. [K2180](k2180-detector-contrast-frontier-2026-10-28.md)'s branch optimum lies in[2/3,113/100]. Combining with (B),

    Q_z=Ep(s)-CsJ <=0 whenever R(z)>=5/12.

For a nonconstant e this is strict: off s=1 use the strictly positive polynomial gap; at s=1, Q_z=-CJ<0 because some adjacent pair differs. Constant e gives R=(5/6)e, s=1, J=0, Q=0.

## 3. Complementary branches and minimizing multiplier

For x=pe, y=p(1-e), R(x)+R(y)=5/6; at least one R is>=5/12. If e is nonconstant, both effects are nonconstant. Thus

    min(Q_x,Q_y)<0

for every strictly interior nonconstant complementary profile for which the quantities are defined (extended values allowed for a general profile).

At any exact-contrast minimizer with 0<|d|<3/4, K2188 gives strict coordinate interiority, finite derivative sums and Q_x=Q_y=H-eta*d. Therefore

    eta*d > H >=0.

Here H>=0 is inherited from the actual positive free Hamiltonian; K2160 section2 explicitly records branch energy positivity, and K2162 section5 proves zero total energy implies a constant effect and identity squeeze on every nonzero branch, under its no-one-particle-zero-modes assumption (satisfied by the positive-frequency fixture). In particular H=F(d)>0 for d!=0 by attainment, and eta*d>F(d)>0. Strict eta*d>0 and global strict increase themselves need only H>=0; the stronger positive F/d conclusion can also be obtained from the resulting strict increase and F(0)=0.

## 4. Frontier and threshold consequences

K2180 proves local Lipschitz continuity of F on(-3/4,3/4) and endpoint continuity. K2188 proves F'(d)=eta at every differentiability point and every optimizer there. For d>0,

    F'(d)>F(d)/d>0 almost everywhere.

Absolute continuity on each compact interior interval gives strict increase there; continuity plus strict interior increase gives strict increase on all[0,3/4], including0 and the endpoint. F(0)=0 and the K2162 zero-energy characterization exclude equality with0 at positive d. Alternatively, choosing one intermediate interior point handles each endpoint strictly. The stronger ratio conclusion is (F(d)/d)'>0 a.e. and hence F(d)/d strictly increases on(0,3/4].

Since the threshold feasible set is the union of exact-contrast slices, compactness gives

    V(d)=min_(t in[d,3/4]) F(t)=F(d).

Every positive-threshold minimizing detector saturates contrast exactly; outcome exchange gives |d(x)|=d for the absolute-threshold problem. No endpoint slack optimizer survives because F is strictly increasing up to3/4. The already established K2182 endpoint theorem remains valid but is no longer needed to carry the entire saturation argument.

For energy budgets B in[0,Emax], Emax=F(3/4), continuity and strict increase make F a homeomorphism onto[0,Emax]; the maximal achievable absolute contrast is the unique d=F^{-1}(B). For B>=Emax it is3/4. For B=0 only constant effects achieve zero energy, with arbitrary constant probability and identity squeezes on nonzero branches. The inverse is a scalar frontier inverse, not uniqueness of the optimizing effect or squeezes.

For a computable B>=0, an equality-safe algorithm starts with[l,u]=[0,3/4], sets a=l+(u-l)/3 and b=l+2(u-l)/3, and refines certified enclosures of F(a), F(b) and B until either F(a)<B or F(b)>B is certified. At least one is strictly true because F(a)<F(b); convergent enclosures eventually certify it even when B equals one tested frontier value. The first comparison permits l=a; the second permits u=b. Either preserves the clipped maximizing contrast and contracts interval width by2/3. Repetition gives an arbitrary prescribed rational accuracy, including B=0, B=Emax and B>Emax. Inner query points always lie in(0,3/4), so K2180's effective exact-arithmetic interface suffices. This is a terminating oracle/quantifier-elimination algorithm, with no practical complexity guarantee. A naive single-point equality comparison can still fail to terminate; arbitrary noncomputable budgets have no algorithmic promise.

## Verification and remaining work

The universal capped-edge/Cauchy argument, scalar positivity certificate and
absolute-continuity transfer are written proofs. The exact probe checks their
algebra independently, full-tail rational capped profiles, strict Q witnesses,
and an equality-safe inverse consumer on exact monotone controls. Planted
faults alter actual formulas or input geometry. Finite controls are not the
universal proof, and a floating search has no acceptance role.

Reproduction: `tests/channel-swings/k2192_detector_smoothing_and_sign_probe.py`;
`--write` regenerates its dependency-hashed report. The prior K2180 effective
finite optimizer interface is reused, not claimed implemented. Birth-death
energy descent remains unproved and is unnecessary for saturation. K2184
profile nonconvexity and K2186/K2190 fixed-noise counterexamples survive:
nonminimizing profiles can gain energy under contrast contraction even though
the minimizing frontier strictly increases. K2182 endpoint asymptotics,
weak-contrast353/170 and K2176 half-contrast numerical bracket are retained.

Remaining substantial questions are joint optimizer uniqueness, a practical
certified global solver and a shared stable field-apparatus Hamiltonian with
preparation/reset accounting. They require new minimizing structure, actual
solver certification or physical input; saturation alone supplies none.
