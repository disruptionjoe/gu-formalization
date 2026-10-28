---
title: "K2171 Euler filter and scalar-square mixed-port exclusions"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2171_mixed_port_euler_filter_probe.py
---

# K2171 Euler filter and scalar-square mixed-port exclusions

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
result: K2171 noncommutative Euler filter and commuting or anticommuting scalar-square mixed-port exclusions
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

An exact Euler contraction of K2169's ten full lower equations gives a cheaper
necessary matrix equation. Its useful consequence excludes EVERY genuine mixed port
whose normal seven- and three-form components have scalar squares and either commute
or anticommute. This includes nondecomposable components and scalar squares of either
sign or zero; no definiteness or scalar inverse of either component is assumed.
All nonzero coordinate two-blade ports, at every overlap and nonzero combined amplitude, are included (pure cases reuse K2167).

This is an exclusion within the fixed normalized zero-order adapter family for the
supplied coupled operator on Cl77 with W(3,1)+N(4,6). SC-OP-04 ASSERTS candidate
four-field grammar, not this common reverse/contraction; SC-GEO-55 describes a
rotated-Levi-Civita displacement. No source16cell/full20/K-C, native2+1/chirality,
physical quotient, GU verdict, source polarity, ledger0.263 or canon moves. LT-SM8,
LT-GR6b and AC-F1 retain their debts. Layer0 preserves the conditional full real Dirac
carrier. K2167's Z2/pure-port and K2169's singular-pencil exclusions are reused.

The remaining even-port problem requires at least one component with a nonscalar square,
or a pair that neither commutes nor anticommutes. The Euler equation is NECESSARY ONLY:
passing it is not passing all ten full rows. Mixed odd/even ports, moving geometry,
changed reverse/operator and native integrability remain separate alternatives.

## 1. The noncommutative contraction

Use K2169 notation, with omega represented by i in D=Cl(N)_C, and real-Clifford
conjugation denoted by a bar. Define

    R=v+3iu, b=bar(R), P=R+6b=7v-15iu,
    S=5R+2b=7v+9iu, W=P^-1 S,
    K(x)=sum_j eta_j gamma_j x gamma_j,
    Q=sum_j q_j gamma_j.                         (1)

There is NO extra eta_j in Q: q_j already contains the contraction convention.
For nonzero candidate ports P is invertible by K2169. Directly from all ten full
lower residuals, without commuting any coefficient,

    6 bar(P) Q = A W - B,                        (2)
    A=3K(b²)+34b²+36Rb+8bR-24R²,
    B=184R²+140Rb+184bR+194b²+24K(bR)+15K(b²).

Thus AW=B is a small exact rejection filter before evaluating every q_j. It costs
one pencil inverse and several Clifford products, and retains product order.
It can reject a candidate; it cannot certify descent.

For reproducibility, let C_j=-eta_j P^-1 d_jR, J=sum C_j gamma_j=-W,
z=v+iu, T=7v+3iu, M=3v+iu. The identities K(R)=4b, K(z)=4bar(z),
K(M)=4bar(M) and d_jx={gamma_j,x}/2 for these odd forms give

    H=sum bar(C_i)d_i b
      =-1/4 bar(P)^-1 [K(b²)+10b²+4(Rb+bR)],
    L=sum bar(C_j) z gamma_j
      =-1/2 bar(P)^-1 [K(bz)+4b bar(z)],
    G=sum bar(C_i)d_i M
      =-1/4 bar(P)^-1 [4RM+K(bM)+10bM+4b bar(M)],
    Q=(4iu+2H)J-T+7L+4G.

Substitute z=(2R+b)/3, T=4R+3b, M=(5R+4b)/3 and iu=(R-b)/6 to obtain(2).
The scalar projection tau is cyclic and tau(Kx)=10tau(x), so a further necessary
scalar filter is

    tau(AW)=184tau(R²)+564tau(Rb)+344tau(b²).      (3)

This trace is indefinite; no positivity inference follows from it. Its practical
use is early rejection and checking ordered algebra, not an all-port no-go.

## 2. Entire commuting scalar-square class

Set t=iu and suppose [v,t]=0, v²=aI,t²=cI, with v,t both nonzero. Set h=vt.
Seven- and three-forms both reverse with a minus sign, so commuting h is reversion
even. The possible product degrees are4,6,8,10; therefore h has only grades4,8.
K has eigenvalues2,-6 on those grades, and h has zero scalar part. The normal
Clifford formulas give

    A=(84a-36c)I-348h-18K(h),
    B=(1092a-324c)I-60h-90K(h).

P,S commute, so multiplying AW=B on the right by P gives AS=BP. Expanding yields

    K(h)(7v-21t)=(98a+28c)v+(-210a+72c)t.         (4)

Right multiplication by v+3t now gives

    7(a-9c)K(h)=f I+(84a+156c)h,
    f=98a²-602ac+216c².                          (5)

Scalar projection forces f=0. If a=9c, f=2736c² implies a=c=0, and the commuting
square-zero pair gives P^4=0, contrary to invertibility. If h=0, h²=ac=0 together
with f=0 again gives a=c=0. Otherwise(5) makes h a K eigenvector, of eigenvalue
kappa=2 or -6. Since v and t have distinct grades and are nonzero, (4) implies

    98a+(28+21kappa)c=0,
    (210+7kappa)a-72c=0.

The two determinants are respectively -22736 and9408, both nonzero. Thus a=c=0,
again impossible for invertible P. No step inferred v=t=0 from vanishing squares;
nilpotent nonzero forms were explicitly retained and excluded through P.

## 3. Entire anticommuting scalar-square class

Now assume vt=-tv, v²=aI,t²=cI, h=vt. Reversion is odd, so h has grades6,10,
with K eigenvalues -2,-10. The invertible pencil satisfies

    P²=dI, d=49a+225c != 0,
    W=(49a-135c+168h)/d,
    A=(84a-36c)I-168h,
    B=(1092a-324c)I+264h+144K(h).

Using h²=-acI, equation(2) is equivalent to

    f I+(49a+297c)h+d K(h)=0,
    f=343a²+1491ac-540c².                        (6)

Specifically AW-B=-144/d times the left side. Scalar projection forces f=0.
If h=0, ac=0 and f=0 force a=c=0, contradicting d!=0. Otherwise(6) makes h a
K eigenvector. For eigenvalue -2 the coefficient equation is49a+153c=0 and
f=-(12960/7)c². For eigenvalue -10 it is49a+217c=0 and f=-416c². Both give
a=c=0 and the same contradiction.

Every pair of coordinate seven/three blades in ten dimensions overlaps in0,1,2
or3 indices. Odd overlaps commute, even overlaps anticommute, and their squares
are scalar. Thus these two class proofs remove every amplitude of every such
coordinate pair without a case-by-case search. The prior complementary family
was only the overlap-zero subclass. Nondecomposable pairs satisfying the same
algebraic hypotheses are covered too.

## Reproducibility and continuation

Run `python tests/channel-swings/k2171_mixed_port_euler_filter_probe.py` in the
repository SymPy environment; `--write` regenerates the exact JSON evidence.
The probe checks(2) against the ORIGINAL ten full rows on a noncommuting,
nondecomposable fixture, the four coordinate-overlap types, both class polynomial
reductions, spectral coefficients and degeneracies. Genuine product-order,
contraction-sign, K-coefficient and scalar-equation faults fail after a green
baseline. Written universal arguments receive independent mathematical review;
finite controls do not enumerate or exclude all240-coordinate mixed ports.

Use(2) to reject new candidates cheaply, then all ten K2169 equations to test every
survivor. Further scalar-square work must use pairs that neither commute nor
anticommute; nonscalar-square ports also remain open. A moving gamma/splitting or
changed reverse is a new operator construction, not repair by fixed-geometry
adapter derivatives. No novelty, external-expert or proof-assistant claim is made.
