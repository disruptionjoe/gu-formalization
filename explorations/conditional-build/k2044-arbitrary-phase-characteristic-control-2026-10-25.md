---
title: "K2044: Arbitrary-phase characteristic control and exact scattering"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed classical two-speed sector under stated charge bounds; no physical fermion or unrestricted transverse dynamics
scripts:
  - tests/channel-swings/k2044_arbitrary_phase_characteristic_control.py
  - tests/channel-swings/k2044_arbitrary_phase_characteristic_control_probe.py
---

# K2044: Arbitrary-phase characteristic control and exact scattering

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


```gu-typed-objects
result: arbitrary-phase two-sided smooth continuation and finite-time free scattering
carrier: two complex eigenlines in K2038 real1408 graph, opposite C1 speeds LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Euclidean graph norm and skew T=diag(J,2J) ON=declared_graph
real_structure: real commuting fields; complex coordinates on real planes
grading: even sextic polynomial, not Grassmann statistics
action_owner: repository-construction -- fixed K2038 action and K2040 sextic
target: interacting domain and causal propagation MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The phase restriction in
[K2042](k2042-sextic-transport-instability-2026-10-25.md) is unnecessary for
small-data global evolution on the line. Positive charge flux controls the
nonlinearity along the opposite characteristics. The sufficient condition is
scale invariant and gives uniform amplitude bounds for all positive and negative
times. Compactly supported solutions become exactly free after finite time.
A stronger position-dependent condition also gives one-sided results for data
that fail the uniform condition. None is a source-selected physical domain.

## 1. The fixed system and local construction

On R, take arbitrary smooth complex z0,w0 with bounded derivatives and finite
M=integral_R (|z0|^2+|w0|^2) dx. The same system embeds in R x T2 with no
transverse dependence; M is charge per unit transverse volume. Keep the actual
K2042 opposite-speed invariant eigenlines and potential Re(z^2 conjugate(w)^4):

    (partial_t+partial_x)z = 2i conjugate(z) w^4,
    (partial_t-partial_x)w = 2i z^2 conjugate(w)^3.          (1)

No fixed relative phase is imposed. Local existence and uniqueness follow from
the two characteristic integral equations on a bounded amplitude ball: the
polynomial right sides have a uniform Lipschitz constant, giving a contraction
for sufficiently small time. Differentiation yields a linear integral system
for the highest spatial derivatives; lower derivatives give its forcing.
Consequently a uniform amplitude bound on each finite interval continues a
smooth solution. These elementary facts do not require a global PDE theorem.

Set a=|z|^2, b=|w|^2, rho=a+b and j=a-b. Direct differentiation gives

    D_+ a = S, D_- b = -S, rho_t+j_x=0,
    |S| <= 4 a b^2,                                     (2)
    S^2+16 Re(z^2 conjugate(w)^4)^2 = 16 a^2 b^4.

The exact last identity checks the coefficient in the inequality. Positive
charge conservation gives M at every local time. Integrating the current on a
finite causal diamond and taking the spatial endpoints to infinity proves the
half-line identities below; finite initial charge and finite propagation justify
the limit. This avoids assuming a pointwise boundary limit of the current.

## 2. Flux estimates, not a supremum-only Gronwall argument

For any right-moving characteristic x=x0+t, the charge to its right decreases
at rate 2b(t,x0+t). For a left-moving characteristic x=y0-t, the charge to its
left decreases at rate 2a(t,y0-t). Thus on ANY time interval inside existence,

    integral b(t,x0+t) dt <= M/2,
    integral a(t,y0-t) dt <= M/2.                         (3)

Each integral is oriented from earlier to later time and has nonnegative
integrand. The same estimates bound the absolute integrals from a negative
time to zero. They use the two opposite speeds and the positive current;
pointwise conservation along one characteristic would be false here.

Where b is nonzero, (2) gives |D_-(1/b)|<=4a. A zero initial w stays zero
along its characteristic by local uniqueness. Let B=||w0||_infinity^2 and
A=||z0||_infinity^2. If

    2 M B < 1,                                         (4)

then (3), in either time direction, yields

    b(t,x) <= Bstar := B/(1-2MB).                        (5)

For nonzero a, |D_+ log(a)|<=4b^2<=4 Bstar b. Again zeros remain zero.
Applying (3) once more gives

    a(t,x) <= A exp(2 M Bstar).                         (6)

These bounds are uniform for all times of local existence. The coefficients
in every differentiated system are therefore bounded on every finite time
interval. Iterated integral inequalities bound each derivative (they may grow
with time), so local continuation gives a unique global smooth solution for
all t in R. The result asserts uniform amplitudes, not uniform derivative
bounds, nonlinear stability of nonzero equilibria, or general3D well-posedness.
When B=0, (1) is free and the formulas hold by continuity.

## 3. Released successor: directional, position-dependent charge

Write M_left(y)=integral_{-infinity}^y rho0 and
M_right(y)=integral_y^{infinity} rho0. The same half-line calculation sharpens
(3), along a w-characteristic originating at y:

    integral_0^t a(s,y-s) ds <= M_left(y)/2      (t>=0),
    integral_t^0 a(s,y-s) ds <= M_right(y)/2     (t<=0).

Hence the forward condition

    eta_plus = sup_y 2 |w0(y)|^2 M_left(y) < 1           (7)

alone proves forward global smooth existence, with
b<=B/(1-eta_plus) and a<=A exp(2MB/(1-eta_plus)). Replacing left by right gives
a separate backward theorem with eta_minus. If both are below one, both
directions are global. Conditions (7) and its reverse can be strictly weaker
than (4); they retain the physical position of the charge.

For example, choose a smooth narrow w pulse of squared height B and total
charge m with 2Bm<1, and put an arbitrarily massive smooth z pulse entirely to
its right. Wherever w0 is nonzero, M_left<=m, so (7) holds independently of the
z charge. In forward time the pulses move apart and actually never interact.
The example proves that failure of (4) is not a blowup criterion. Overlapping
profiles satisfying (7) are also allowed; their continuation uses the flux
proof, not separation. No necessity or sharpness claim is made for either
sufficient condition. Large interacting data failing both estimates remain open.

## 4. Exact finite-time scattering for compact data

The z equation is a real-linear homogeneous equation in z along its own
characteristic once w is fixed. The w equation is locally Lipschitz and
vanishes at w=0 along its characteristic. Uniqueness in both time directions
therefore preserves zero sets: each component's support translates exactly
with its own speed. If the initial supports lie in [l,r], then

    supp z(t) subset [l+t,r+t],
    supp w(t) subset [l-t,r-t].                          (8)

For |t|>(r-l)/2 these intervals are disjoint, so both nonlinearities vanish
identically. Under the two-sided hypothesis there are smooth compactly
supported profiles z_plus,w_plus,z_minus,w_minus with

    z(t,x)=z_plus(x-t), w(t,x)=w_plus(x+t)   for t>(r-l)/2,
    z(t,x)=z_minus(x-t),w(t,x)=w_minus(x+t)  for t<-(r-l)/2.

This is exact scattering after finite interaction time, stronger than a
merely asymptotic estimate. A forward-only hypothesis gives the outgoing
statement only. Total L2 charge is the same on both scattering sides; individual
component charges may transfer during overlap. This does not identify the
nonlinear scattering map with the identity or prove a quantum S-matrix.

The rescaling u_lambda(t,x)=lambda^(1/4)u(lambda t,lambda x) preserves (1).
Its squared sup scales as lambda^(1/2), and M scales as lambda^(-1/2), so MB
and both eta conditions are invariant. Small charge alone is insufficient
for this proof: compression can lower M while raising the squared supremum.
This explains why a charge-only appeal would miss a load-bearing factor.

## 5. Checks, contrary cases and scope

The producer derives the actual real gradient, both density sources, their
sharp algebraic magnitude identity, reciprocal coefficient and scaling.
A separate rational-complex implementation differentiates the original degree6
potential by exact centered polynomial interpolation at24 field fixtures
(96 directional derivatives), and separately checks three null-flux and three
reciprocal-bound fixtures. Four actual faults change a force coefficient,
kinetic frequency, null-flux factor and the reciprocal smallness coefficient.
The theorem follows from sections1--4, not from those fixtures. Raw graph,
Clifford eigenline existence and the action lift are unchanged K2038/K2042
premises; their full matrices are not replayed here.

The hostile checks are: (i) integrate the opposite density with the factor2
from rho plus/minus j, (ii) preserve both time orientations and half-lines,
(iii) control reciprocal b before log a, (iv) require finite charge on R rather
than pretending that a periodic background has finite line charge, and (v) use
local uniqueness to prove support transport before claiming scattering.
Nonzero homogeneous periodic backgrounds lie outside this theorem and retain
K2042's instability. The inequality is sufficient, not a predicted singularity
threshold. No contrary example is known here within the stated hypotheses.

SC-OP-04 ASSERTS only a candidate four-field operator; SC-OP-05 remains
UNCERTAIN about its southeast rival. SC-META-53 remains UNCERTAIN about physical
positivity. This deliberately changed real commuting action does not supply
source fermionic parity, an actual independent-dual identification or a physical
observed quotient. LT-SM8/LT-GR6b, the source register and canon are unchanged.
Same-author separate implementations and proof review are internal checking,
not external, proof-assistant or novelty certification. Next compare a
large-data characteristic obstruction/continuation argument with the genuine
transverse system and the missing physical bridge.
