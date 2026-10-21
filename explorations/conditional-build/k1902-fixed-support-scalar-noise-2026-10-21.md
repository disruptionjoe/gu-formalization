---
title: "K1902: Fixed-support scalar noise budgets"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied noise and finite-mode mathematics; no native GU realization or physical bath selection
scripts:
  - tests/channel-swings/k1902_fixed_support_scalar_noise.py
  - tests/channel-swings/k1902_fixed_support_scalar_noise_probe.py
---

# K1902: Fixed-support scalar noise budgets

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
result: sharp symmetric finite-support energy infimum and explicit amplitude-duration feasibility bracket
carrier: two plateau modes in one direction of a rank-four massless R1 target LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: real phase profiles and complex conjugation
grading: finite mode labels and CAR parity
action_owner: repository-construction -- supplied classical laws or finite quantum dilation
target: bounded neutral coherence and specified control cost MAP-TYPE=intertwiner
```


## 1. Freeze resources before optimizing

Fix 0<a<b<L, support of each final phase in [-L,L], plateaux
[-b,-a] and [a,b], and the other transport direction's final phase identically
zero. The common scalar generator is smooth in spacetime, with duration T>0.
We constrain its support to the moving tube x-ct in [-L,L], 0<t<T.
This is a specified conditional control geometry, not a detector model or
a rectangular lab support. Let the modulus of the plateau coherence be eta.
Set theta=acos(eta) in[0,pi/2] and ell=L-b.

The scalar steering range condition from K1900 is integral Phi_+=0 when
Phi_-=0. Fixed support forbids its old arbitrarily remote cheap correction.
An odd phase profile supplies the range condition intrinsically in this
symmetric geometry. No channel-specific matrix potential is imported.

## 2. Exact spatial variational problem

For any H0^1(-L,L) profile with plateau values A,B and X=B-A, its three
transition intervals imply

    ||phi'||^2 >= A^2/ell + X^2/(2a) + B^2/ell
                 >= X^2 [1/(2a)+1/(2ell)] = kappa X^2.

The last step uses A^2+B^2 = X^2/2+2((A+B)/2)^2. The intermediate plateaux
have zero derivative. The optimal common phase is A=-X/2,B=X/2.
The odd continuous piecewise linear interpolant reaches equality in H0^1
and has zero integral. Its slopes on the two exterior intervals have
magnitude |X|/(2ell), while the central slope has magnitude |X|/(2a).
Thus imposing the scalar range condition costs nothing EXTRA in this
symmetric problem, even though fixed support itself does cost energy.

For smooth compact profiles the same value is an infimum: smooth the corners
and exterior endpoints in shrinking transition neighborhoods, keep exact
plateau values on the stated closed intervals, and impose odd reflection.
Transition derivatives can be chosen smooth and flat at both ends, with fixed
integral and L2 norms approaching the constant-slope norm. This construction
keeps support inside (-L,L), zero integral and the exact coherence.
A nonzero theta gives no smooth minimizer, because constant nonzero slopes
cannot meet flat plateaux smoothly at equality.

K1900's arbitrary-law inequality then gives the SHARP result

    inf Ebar = c/(2pi) kappa theta^2,
    kappa = 1/(2a)+1/[2(L-b)].                         (1)

Use the binary law phi=+/-phi_theta with equal weights. Compared to the
unrestricted-support bound c theta^2/(4pi a), the penalty factor is
1+a/(L-b). This tends to one as L grows and diverges as the return margin
L-b shrinks at nonzero theta. A finite fixed support, not the number of
histories, causes this penalty. It remains valid for arbitrary probability
laws, and the binary law is sufficient here.

## 3. Released finite-duration scalar generator

Take a real nonnegative C-infinity bump h supported in(0,1) with integral1;
let H0=||h||infinity, H1=||h'||infinity and g(t)=h(t/T)/T.
For any smooth odd approximant phi define

    f(x)=-(1/(2c)) integral_(-L)^x phi(y)dy,
    V(t,x)=g'(t)f(x-ct)+g(t)phi(x-ct).

The antiderivative f is smooth and compact in(-L,L) because integral phi=0.
V=(partial_t-c partial_x)[g(t)f(x-ct)] is a COMMON SCALAR potential.
Integrating on opposite characteristic families yields final Phi_+=phi and
Phi_-=0 exactly. The pulse has characteristic speed c throughout; no
instantaneous or infinite-amplitude limit is used for any individual history.
A finite mixture of these histories is a normal causal CAR channel.

For the piecewise linear limiting profile,

    ||phi||infinity=|X|/2,
    ||f||infinity=|X|(L+b-a)/(8c).

The latter follows by integrating the negative half profile: its unsigned
area is |X|(L+b-a)/4. Smooth approximants can preserve the first bound and
approach the second. Consequently every amplitude budget strictly greater than

    M_suff = theta [H0/(2T)+H1(L+b-a)/(8cT^2)]          (2)

admits approximants to the sharp energy(1), with all histories |V|<=M.
Strict slack absorbs smoothing. Equation(2) is a sufficient construction,
not a sharp amplitude optimum. It exposes the T^-2 cost of the steering term
and the tradeoff between long return tails and amplitude at fixed duration.

For an explicit reproducible bump one may choose h(s)=Z^-1 exp[-1/(s(1-s))]
on(0,1), zero outside, Z its integral. H0,H1 are finite defined constants;
no unchecked numerical maximum is needed for(2).

## 4. A necessary amplitude-duration bound and consumer decision

For EVERY scalar pulse with |V|<=M and duration T, regardless of the moving
support shape, each characteristic phase lies in[-MT,MT]. The contrast
therefore obeys |X|<=2MT. If 2MT<=pi/2, then

    |E exp(iX)| >= Re E exp(iX) >= cos(2MT).

For any eta in[0,1], a necessary condition for producing modulus eta is

    M T >= (acos eta)/2.                              (3)

When 2MT>pi/2, (3) is automatic; no periodic continuation of the cosine
inequality is claimed. In particular complete decoherence requires MT>=pi/4.
This necessary bound and(2) give an honest feasibility bracket. A budget
violating(3) excludes the frozen bounded-control model. A budget satisfying
(2) with strict slack admits near-optimal energy. The intermediate region
is unresolved; it is not automatically impossible or feasible.

For a specified energy cap Emax, Emax below(1) is impossible, and Emax
strictly above(1), together with amplitude slack(2), has an explicit smooth
realization. Equality at(1) is generally unattained. These paired tests are
useful consumers of the exact result without a new probability law or fitted
coefficient. A rectangular spacetime support, separable pulses, exact amplitude
optimality and massive 3D transfers remain separate problems. The next
section resolves arbitrary asymmetric plateau positions in the moving tube.

## 5. Released asymmetric fixed-support solution

The symmetric construction suggests the precise missing area cost for arbitrary
ordered plateaux, which can also be solved rather than left to numerical
optimization. Use support[0,S], plateaux[x1,x2] and[x3,x4], all three gaps
l=x1, g=x3-x2, r=S-x4 strictly positive, and widths w0=x2-x1,w1=x4-x3.
Set u=w0+(l+g)/2, v=w1+(g+r)/2 and Q=(l^3+g^3+r^3)/12.
For plateau values A,B the piecewise linear profile has integral I=uA+vB.
On each open transition of length d let b_d(s)=s(d-s)/2. These functions
vanish at transition endpoints, satisfy -b_d''=1, and have both integral
and squared derivative norm d^3/12. The least-cost zero-area correction is
-(I/Q)b_d on EACH gap, with total extra derivative cost I^2/Q.
Indeed its derivative is orthogonal to the piecewise constant derivatives
of the linear profile; Cauchy--Schwarz in the direct sum of the three H0^1
gap spaces proves no cheaper area correction exists. Thus the exact relaxed
cost is

    J(A,B)=A^2/l+(B-A)^2/g+B^2/r+(uA+vB)^2/Q.         (4)

Put A=Y-X/2, B=Y+X/2. Define

    D=1/l+1/r+(u+v)^2/Q,
    E=-1/l+1/r+(v^2-u^2)/Q,
    F=1/g+(1/l+1/r)/4+(v-u)^2/(4Q).

Then J=D Y^2+E X Y+F X^2, and minimizing the common phase gives

    Y=-E X/(2D),  kappa_asym=F-E^2/(4D)>0.           (5)

Positivity also follows directly from J>=X^2/g. Equations(4)--(5) give an
exact rational formula for the spatial coefficient at every positive choice
of the three gaps and plateau widths. The arbitrary-law sharp energy is
c kappa_asym theta^2/(2pi), by the same binary law and scalar steering.
Smooth approximants preserve plateaux; a small compact gap correction restores
exact zero area after smoothing with vanishing additional H1 cost. Unlike the
symmetric case the optimal profiles are generally piecewise QUADRATIC, because
a finite-area constraint has a genuine Lagrange multiplier. Their amplitudes
can exceed the plateau values, so the symmetric amplitude bound(2) must not
be transferred. Direct evaluation of the constructed profile and its compact
antiderivative supplies the corresponding sufficient amplitude bound.

For l=g=r=1,w0=1,w1=2: u=2,v=3,Q=1/4, D=102,E=20,F=5/2,
Y=-5X/51 and kappa_asym=155/102. Omitting the scalar zero-area condition
would instead give3/2, strictly smaller. For the symmetric geometry E=0 and
u=v, recovering(1) with l=r=L-b,g=2a. This supplies both a positive control
where area is free and a counterexample to treating it as free in general.

## Scope and verification

These are supplied positive-Hilbert/CAR controls, not the GU physical quotient.
SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN.
The controls do not identify that source mechanism. LT-SM8, LT-GR6b and AC-F1,
the source register, physics ledger and canon verdicts remain unchanged.
Classical randomness, the observable algebra, sea and/or quantum ancilla are
imported. No microscopic bath, native full20/K-C adapter, GU prediction,
novelty, external specialist acceptance or formal proof is claimed.

The analytic argument carries the general scope. The producer checks exact
matrices/integrals; a separate probe rederives decisive controls and rejects
mathematical input faults after a clean baseline, separately from report and
provenance checks. These finite tests do not certify all continuum hypotheses.
Hostile review targets phase lifts, positivity versus classical realizability,
infima versus minima, source attribution and the exact physical carrier.
