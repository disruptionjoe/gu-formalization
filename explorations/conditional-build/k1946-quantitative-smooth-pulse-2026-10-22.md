---
title: "K1946: An explicit smooth pulse with certified resource margins"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional exact mathematics; no native GU identification, source selection, novelty or formal proof
scripts:
  - tests/channel-swings/k1946_quantitative_smooth_pulse.py
  - tests/channel-swings/k1946_quantitative_smooth_pulse_probe.py
---

# K1946: An explicit smooth pulse with certified resource margins

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
result: explicit integral-defined smooth pulse, exact plateaux and quantitative amplitude-energy-derivative bounds
carrier: fixed one-dimensional scalar characteristic tube at c1 T9/2 L3 LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginals and Dirichlet phase energy ON=conditional_scalar_control
real_structure: real compactly supported smooth functions and exact rational affine seed
grading: two propagation directions; no physical chirality
action_owner: repository-construction -- supplied scalar pulse and positive target interpretation
target: constructive regularization with exact zero opposite phase MAP-TYPE=intertwiner
```

## Result and fixed object

[K1944](k1944-optimized-scalar-pulse-certificate-2026-10-22.md) established
smooth feasibility existentially. Here the ACTUAL inherited rational pulse is
converted into one explicit C-infinity compact pulse, defined by finite data
and normalized one-dimensional integrals. It has exact phase+1 on[-2,-1],
phase-1 on[1,2], and identically zero opposite phase, with

    amplitude <0.229975419 <0.23,
    phase Dirichlet energy <4.005271623 <4.01.            (1)

The reported decimals are outward-readable upper bounds; the certificate uses
exact rational bounds. No transport LP is rerun, no improved global energy
optimum is claimed, and the nonsmooth old phase is not preserved outside its
plateaux. A finite derivative bound is supplied. It is large, not a claim of
low bandwidth or a spectral bandlimit.

Use c=1,T=9/2,L=3, u=x-t,z=x+t and E={-3<=u<=3,0<=z-u<=9}.
The inherited w has marginals(phi,0), physical pulse2w, amplitude
M0=22451259/97656250 and phase energy
U=78227902689379/19531250000000. Its h=1/32 affine phase has

    ||phi||inf=1, Lip(phi)=ell=3344727/3125000.           (2)

All193 nodes and110208 rational flow values are losslessly referenced by a
SHA256 pin. Replaying that certificate is inherited verification, not new
scientific discovery.

## 1. An explicit smooth phase retaining the CLOSED plateaux

Fix e=1/2000000. On each free interval[a,b] in
[-3,-2],[-1,1],[2,3], compress the original phase graph into
[a+e,b-e]: map every old node u to

    u_new=a+e+(b-a-2e)(u-a)/(b-a),

keeping its value. Fill the two short endpoint intervals with the corresponding
constant value. Retain the plateaux and zero outside[-3,3]. Call the resulting
continuous piecewise-affine function f_e. Its exact knots are in the artifact.
It is odd, hence has zero area; it vanishes for |u|>=3-e and equals the plateau
values on e-enlargements of both closed intervals. Direct change of variables
on each free interval gives

    ||f_e-phi||inf<=ell e,
    integral |f_e'|^2=sum_free (b-a)/(b-a-2e) integral_a^b |phi'|^2
                       <=U/(1-2e),
    Lip(f_e)<=ell/(1-2e).                               (3)

Define the even probability bump

    eta(s)=exp(-1/(1-s^2))/I for |s|<1, else0,
    I=integral_-1^1 exp(-1/(1-r^2))dr,
    eta_h(s)=eta(s/h)/h.

The EXACT smooth phase is psi=eta_(e/4)*f_e. It is odd, smooth, zero near
|u|=3, and retains the exact closed plateau values. Jensen/Fubini gives
integral |psi'|^2<=integral |f_e'|^2. Convolution and (2)-(3) give

    ||psi-phi||inf<=5ell e/4.                           (4)

The certificate integrates the flattened energy exactly, rather than relying
only on the coarser final inequality in (3). A smooth kernel is defined by its
formula, not by a finite table of samples.

## 2. Smooth the ACTUAL pulse and restore both marginals

Let a=1-e. Transport the old pulse by

    u_new=a u, z_new=a z+9(1-a)/2,
    w_a(u_new,z_new)=w(u,z),

and extend it by zero. Its amplitude is unchanged; its marginals are
(a phi(. /a),0). Its u-support has margin3e, and its two slanted boundaries
have margin9e/2. Now set

    w_p=(eta_e tensor eta_e)*w_a,
    phi_p=eta_e*(a phi(. /a)).

The smoothed pulse is compact in the OPEN E, with u margin2e and slanted
margin5e/2. Product convolution preserves the zero column marginal and never
increases the amplitude. Its row marginal is exactly phi_p. The contraction
and Lipschitz estimate, including the zero extension, give

    ||phi_p-phi||inf<=e(1+4ell).

Thus r=psi-phi_p is smooth, compact, odd and has zero area, with

    ||r||inf<=rho=e(1+21ell/4).                         (5)

This is an actual residual, not an existence statement from cuts. Put

    f(u)=-1/2 integral_-infinity^u r(v)dv,
    g(t)=(4/T) eta(4(t-T/2)/T),
    V_r(t,x)=g'(t)f(x-t)+g(t)r(x-t).                    (6)

The primitive is compact because integral r=0. g is supported in[T/4,3T/4]
and has integral1. Along a right characteristic the integral of V_r is r.
Along a left characteristic it is the integral of
(partial_t-partial_x)[g(t)f(x-t)], hence zero; the sign and factor1/2 in(6)
are essential. Finally the explicit pulse is

    V(t,x)=2 w_p(x-t,x+t)+V_r(t,x).                     (7)

It is C-infinity compact in the open moving tube and has EXACT marginals
(psi,0). Equations(2)-(7), the exact seed and knots completely specify the
function. They are not a floating approximation to unspecified smooth data.
Numerical evaluation of these integrals would need its own quadrature error
certificate if values, rather than the analytic resource bounds, are used.

## 3. Quantitative acceptance, including finite derivative bounds

Elementary bounds for this normalized bump are

    ||eta||inf<=4, ||eta'||inf<=8, ||eta''||inf<=160.

For completeness I>1/4 follows by restricting to[-1/2,1/2] and
exp(4/3)<4. Write y=1/(1-s^2)>=1. Before normalization, the first derivative
is bounded by2 y^2 exp(-y), and the second by
(4y^4+8y^3+2y^2)exp(-y). Maximize y^k exp(-y) at y=k;
e>27/10 bounds these maxima by5,2,1 for k=4,3,2. Multiplication by4 gives
at most152 for the second derivative, so160 is conservative. These bounds
are analytic, not sampled extrema.

Consequently

    G=16/T, G1=128/T^2, G2=10240/T^3,
    ||g||inf<=G, ||g'||inf<=G1, ||g''||inf<=G2,
    ||V||inf<=M0+(3G1+G)rho, 3G1+G=608/27.             (8)

Here ||f||inf<=3rho; zero area could improve that constant, but is not needed.
The rational right side of(8) is below0.229975419. The exact flattened energy
is below4.005271623. These prove(1) without asking for an unquantified small
enough parameter. The artifact also checks e=1/10000000 and1/4000000: smaller
radii spend less amplitude slack and have larger derivative bounds.

Since ||eta'||1<=16, the smoothed seed contributes at most32M0/e to EACH
physical first derivative. Set R1=ell/(1-2e)+ell. Differentiating(6) and using
f'=-r/2 gives

    ||V_x||inf <=32M0/e+G1 rho/2+G R1,
    ||V_t||inf <=32M0/e+(3G2+3G1/2)rho+G R1.             (9)

Both are below14713665 in these coordinate units. They are guaranteed upper
bounds, not estimates of actual peaks, hardware slew requirements, a spectral
cutoff, or minimal derivative cost. This explicit tradeoff is the new consumer:
choose a supplied radius and check amplitude, energy and derivative allowances
against its rational certificate. A stricter derivative cap is unresolved.

## 4. Independent checks, limitations and source boundary

The producer replays111081 inherited pulse checks, constructs the new exact
knots and verifies three quantitative resource choices. The separate probe
reconstructs the node map, integrates energy and area independently, checks
support/plateau margins and derivative chain rules, and symbolically integrates
both characteristic marginals for a nontrivial polynomial correction control.
Actual phase, radius and correction-sign faults must fail after a green baseline.
Report and pin faults are counted separately. Continuum smoothness, contraction,
Fubini and resource guarantees rest on the analytic proof; finite controls alone
cannot establish them. No certified pointwise numerical evaluator is claimed.

Strongest overclaim: exact smooth global optimum or smooth preservation of the
entire old piecewise phase. Neither follows. Contrary construction: a sign
error in f leaves the right marginal intact but destroys the opposite one;
the independent control rejects it. The weakest seam is compact support under
affine contraction and convolution, including the2c Jacobian; the margins and
physical transform are explicit. No outside expert or formal verification is
claimed. The established capacity-transport context remains
[Korman, McCann and Seis](https://arxiv.org/abs/1307.7774); this note uses an
explicit correction, not a new transport-duality claim.

SC-OP-04 ASSERTS candidate grammar and SC-MAS-01/SC-CHI-02 ASSERT a stylized
curvature-mass toy; SC-META-53 remains UNCERTAIN. None identifies this scalar
drive, physical pairing or resource units. LT-SM8, LT-GR6b, AC-F1, source,
physics ledger and canon are unchanged. The native full20/K-C/domain/accessibility
adapter remains separate. Next substantive scalar work is a matching global
pulse/cut certificate or a specified tighter derivative-resource frontier;
replaying smooth0.23/4.01 feasibility is not new work.
