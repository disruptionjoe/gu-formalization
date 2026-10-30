---
title: "K2305 Regular constrained matter transfer"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction only; no native physical acceptance
scripts:
  - tests/channel-swings/k2305_regular_constrained_matter_transfer_probe.py
---

# K2305 Regular constrained matter transfer

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
result: K2305
carrier: four-dimensional homogeneous Einstein metric, scalar, smooth dust and optional radiation LAYER=toy CHIRALITY=N/A
pairing: real constrained tangent vectors and a declared coordinate infinity norm ON=declared_carrier
real_structure: real coefficients with complex Fourier or Hilbert representation where stated
grading: explicitly stated native Clifford or ordinary scalar/number grades; no transfer between them
action_owner: repository-construction -- fixed healthy designer metric f(R) and matter action from K2302
target: homogeneous source-coupled Jacobi transfer through H_E=0 MAP-TYPE=evaluation
```

## Fixed action and regular equations

Retain [K2302](k2302-designer-frame-turnaround-2026-10-30.md)'s healthy matter action, with no same-background Hessian modification. Let M=Mpl>0, u=dot phi, d=rho_d,E>0, r=rho_r,E>=0, beta=d log B/dphi=-1/(sqrt6 M), and V the SAME Einstein potential. Einstein time is used throughout. In the local smooth-dust regime before caustics,

    dot H=-(u²+d+4r/3)/(2M²), dot phi=u,
    dot u=-3Hu-V'(phi)-beta d,
    dot d=(-3H+beta u)d, dot r=-4Hr.                    (1)

The radiation equation describes homogeneous stress; if r=0 the absent radiation field is not counted as a healthy extra mode. The Friedmann constraint

    C=3M²H²-u²/2-V-d-r=0                               (2)

satisfies dot C=0 identically, even off the constraint surface. The beta sign encodes dust mass mB(phi); changing it in only one equation breaks conservation. These equations have no division by H. They define regular homogeneous perturbations, not a k>0 scalar/vector/tensor perturbation theorem or Jeans stability.

For z=(H,phi,u,d,r), J=D_z f is finite wherever V is C². Its entries are explicit derivatives of (1). If dot T=J(t)T and T(t0)=I, then

    grad C(z(t)) T(t,t0)=grad C(z(t0)).                 (3)

Thus exact constraint tangents propagate across H=0. Since partial C/partial d=-1, solve (2) for dust d; no square root H=±sqrt(rho/3M²) is needed. This chart remains valid near any crossing with d>0.

## Dust constrained flow and a determinant with no turnaround zero

For r=0 use (H,phi,u) and d=3M²H²-u²/2-V. The reduced vector field is

    dot H=-3H²/2-u²/(4M²)+V/(2M²),
    dot phi=u,
    dot u=-3Hu-V'-beta(3M²H²-u²/2-V).                  (4)

Its Jacobian trace is -6H+beta u. Liouville's formula gives the exact determinant of the constrained tangent transfer K:

    det K(t,t0)=(a(t0)/a(t))^6 B(phi(t))/B(phi(t0))>0.  (5)

The determinant is coordinate dependent but proves invertibility of this explicit regular chart. It is not a physical phase-space symplectic volume or an instability exponent. Forward and inverse norms are bounded by exp integral ||J|| in any fixed declared coordinate norm on a compact smooth background interval.

## Explicit crossing fixture and a rigorous finite bound

Normalize the inherited dust fixture C=Fref=alpha=M_J=H*=1, A=2/5, p=(5+sqrt73)/4. Here M_J is K2299's dust background coefficient; Mpl=1. Set

    F=1-A x^-p, a_E=sqrt(F)/x, dt_E/dx=-sqrt(F)x^-5/2,
    H=x^(3/2)[1-A(1+p/2)x^-p]/F^(3/2),
    phi=sqrt(3/2)log F,
    u=-sqrt(3/2) A p x^(3/2-p)/F^(3/2),
    d=3x³/F², V=-3A(1+p)x^(3-p)/F².                  (6)

The relation 2p²-5p-6=0 verifies (1)-(2) exactly along this solution. On x∈[1,11/10], 3<p<7/2, 3/5<=F<73/100, |H|<1, |u|<4, d<12 and |V|<15. The crossing x*=[A(1+p/2)]^(1/p) lies strictly in this interval and dot H*<0. Let nu=1-3/p∈(0,1/7), b=2+nu F/(1-F), c=nu F/(1-F)². Then

    V'= -sqrt(2/3) b V, V''=(2/3)(b²-c)V.              (7)

The bounds b<12/5,c<2 give |V'|<30, |V''|<58. The unreduced dust 4x4 Jacobian in coordinates (H,phi,u,d) has maximum absolute row sum below74. The Einstein time duration is less than1/10, so BOTH ||T||_infinity and ||T^-1||_infinity are bounded by exp(37/5). This deliberately coarse bound establishes finite transfer, not decay, small gain, or a measured physical amplitude.

Along this fixture the constrained determinant is

    det K=(x/x0)^6 (F(x0)/F(x))^(7/2).                 (8)

It remains positive through the crossing; no special cancellation involving 1/H is assumed.

## Actual coupled initial-data followthrough

At the turnaround select the exact constraint family H_epsilon=epsilon, phi_epsilon=phi*, u_epsilon=u*, d_epsilon=d*+3epsilon². Its tangent is (1,0,0,0) in (H,phi,u,d). It is not a time translation of the background, because u* is nonzero. The Jacobi equations give, for tau=t-t*,

    delta H=1+(3u*²/2+3d*/4)tau²+O(tau³),
    delta phi=-(3/2)u* tau²+O(tau³),
    delta u=-3u* tau+O(tau²), delta d=-3d* tau+O(tau²).  (9)

The matter perturbation is generated even when its initial tangent vanishes. Freezing dust thereafter violates the coupled equations. The crossing time also shifts smoothly: by the implicit-function theorem, dt_cross/depsilon=-1/dot H*=2/(u*²+d*)>0. This is an explicit response of a fixed action to specified constrained data, rather than an inference from the algebraic trace mass.

## Verification, scope and next condition

Exact symbolic checks cover off-shell constraint conservation, its differentiated tangent identity, the reduced Jacobian trace, fixture equations, determinant derivative and crossing initial-data jets. Rational interval estimates establish the finite bound; a floating-point crossing value is descriptive only. Real faults alter the dust exchange sign, freeze dust transfer or use the wrong determinant power. Internal review is not proof-assistant or external-expert certification.

SC-COS-50/51/54 remain ASSERTS and the ledger0.263 LT-GR2e missing native/held-out prediction stays unchanged. This supplies homogeneous transfer in a conventional supplied f(R) model. It does not determine inhomogeneous modes, dust caustic avoidance, spatial sound/Jeans evolution or an observed power spectrum. The next substantive construction is the k>0 constrained scalar system in a regular gauge, with fixed spatial matter data and a physical readout; no vacuum formula dividing by H_E may be transplanted through this crossing.
