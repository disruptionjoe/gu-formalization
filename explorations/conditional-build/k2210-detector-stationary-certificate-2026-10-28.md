---
title: "K2210 An actual stationary full-tail detector with strict infinite stability"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: existence of a jointly stationary infinite detector and strict nonlinear local minimum in the supplied model; no global optimum or uniqueness claim
scripts:
  - tests/channel-swings/k2210_detector_stationary_certificate_probe.py
---

# K2210 Actual stationary detector certificate

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
result: an actual fully stationary infinite detector with strict Schur and nonlinear cap-local stability
carrier: supplied positive scalar Fock vacuum and photon-added signal with binary diagonal occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form; constrained Q-completion and relative-cap perturbations ON=declared_carrier
real_structure: real effects, positive square-root Kraus and one real positive squeeze per outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction -- supplied free Hamiltonian and output-field energy
target: existence and stability of an infinite stationary detector MAP-TYPE=intertwiner
```

## Result

For exact contrast d=1/2, there EXISTS a strictly interior infinite profile
x* and positive squeezes s* satisfying every effect stationarity equation
with a single multiplier, both squeeze stationarity equations, and the strict
infinite Schur inequality

    S > (1/3) I_2,    S >= (1/100) D.                    (1)

This supplies the actual stationary instance missing in K2207. It is not the
nonstationary rational profile used by K2204 and K2207. The instance is a
minimizer over all cap-feasible infinite profiles and a specified compact
squeeze rectangle; a boundary gap proves its squeezes lie in that rectangle's
interior. No finite shooting trajectory is treated as an infinite solution.

The exact rational squeeze rectangle is |s_j-c_j|<=10^-14, with

    c1 = 1.05488613429285478754105931186146158654745017929929,
    c0 = 0.863900508430229204825776091549763638620341250644714.

The displayed terminating decimals are exact rectangle centers, not claimed
exact optimizing values. Any compact-box minimizer has the stationarity and
strict stability certified here. Existence and the enclosures do not assert
that all such minimizers coincide.

In K2207's notation, for exact-contrast v,

    ||v||cap <= 1/18000
      => H(x*+v)-H(x*) >= Q(v)/800.                     (2)

Thus x* is a strict nonlinear local minimum in the relative-cap topology.
The joint statement has coefficient1/800 multiplying
Q(v)+d1 t1²+d0 t0² when ||v||cap and max_j |t_j|/s_j are at most1/6000.
This is not a claim of uniqueness, global optimality over all squeezes, a
uniformly feasible energy-norm ball, an improved global energy bracket,
apparatus/reset/preparation cost, physical apparatus or GU source recovery.
SC-META-53, ledger0.263, canon and the physical quotient are unchanged.

## 1. The unchanged infinite model

Keep K2198/K2201's

    p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n-x_n, q_n=3n-1,
    R(z)=sum(n+1/2)z_n, T(z)=sum(n+1)sqrt(z_n z_(n+1)),
    A(s)=41s²/6+3/(2s²), C=40/3,
    E(x,s)=A(s1)R(x)+A(s0)R(y)-C[s1T(x)+s0T(y)]+35/18.

The feasible set is 0<=x_n<=p_n and sum q_n x_n=1/2. There is no
extra probability constraint. Every quantity in the proof includes the entire
occupation tail. The model is a supplied positive Hilbert-space detector;
none of the scalar quantities is silently identified with a source-native GU
operator, action, pairing or physical observable.

## 2. Existence from a finite boundary certificate

Let B be the rectangle above. The feasible effect set is compact in the
product topology: it is a closed subset of the product of the compact
intervals[0,p_n]. The contrast series converges uniformly because
sum |q_n|p_n is finite. The moment and coherence series also converge
uniformly, using z_n<=p_n and sqrt(z_n z_(n+1))<=p_n/2. Therefore E is
continuous on feasible effects times B and attains its minimum there.

The exact probe constructs a feasible constant-effect-tail witness at the
rectangle center. Its tail starts at n=60, and its n=0 complement is repaired
by the exact contrast equation. Let U be its rigorously enclosed energy upper
bound. This witness proves the compact-box minimum is at most U; it is not
itself called stationary.

The following boundary lemma proves the compact-box minimizer's squeeze pair
is interior. On each of the four faces split the varying coordinate into eight
equal closed intervals. At each tile center supply ANY valid fixed-squeeze
all-tail dual lower bound D_c. Check the four corners separately. With

    M=(2843/48)(5/6), w=2*10^-14/8,

it suffices that every D_c-M w²/8>U and every corner dual bound exceeds U.

Proof: suppose a boundary pair participates in a compact-box minimizer. A
corner is excluded by its dual. Otherwise the pair lies in the interior of
one face. Holding its minimizing profile x* fixed, the derivative of E in
the tangential squeeze coordinate is zero, since motion in either direction
along that face is allowed. On the whole rectangle,

    d²E/ds_j²=R(z_j)A''(s_j) <= (5/6)(2843/48)=M,

because B lies strictly in[2/3,113/100]² and
A''(s)=41/3+9/s^4. Pick a tile containing the minimizing pair. Its center
is at distance at most w/2, so the exact Taylor bound gives

    D_c <= E(x*, center) <= E(x*, minimizing pair)+M w²/8.

This contradicts D_c-M w²/8>U. The argument uses stationarity at the
hypothetical boundary minimizer, not at an arbitrary point or at a tile
center. It makes no differentiability assumption about the reduced value
function min_x E(x,s). Closed tiles cover their shared endpoints.

The probe verifies exact coverage and derives every center/corner directly
from rational rectangle geometry. Numerical discovery decimals are never
used as purported exact face positions. The certificate gives

    min_face_tiles(D_c-M w²/8-U) and min_corners(D_c-U)
       > 4*10^-28.                                    (3)

Hence no compact-box minimizer lies on the boundary. K2188/K2194 now apply at
its own fixed squeezes: its effect profile is strictly interior, is the unique
fixed-squeeze minimizer, satisfies h_n=lambda q_n at every coordinate, and is
strictly increasing toward1. Interior squeeze variation gives
A'(s_j)R(z_j)=CT(z_j) for BOTH branches. This is full joint stationarity.
It is an existence theorem for an actual infinite profile, with computable
coordinate and tail enclosures, not a numerical residual tolerance.

## 3. Finite proof inputs and all-tail coordinate enclosures

The probe embeds61 rows of six rational polynomial coefficients. They supply
positive complementary values f_n(a,b) at normalized rectangle positions;
the positive AM-GM slopes are downward dyadic approximations to
sqrt(e_(n+1)/e_n)/2 and sqrt(f_(n+1)/f_n)/2. The coefficients were found by
numerical search and quadratic interpolation. They are merely compact inputs
for free dual parameters. Their closeness to an optimizer, interpolation error
and floating-point residuals play no role in validity. Every actual bound is
recomputed using rational/outward arithmetic and the exact infinite affine
tail of K2196's dual. No numerical-discovery package is required to reproduce
the certificate.

Apply the same free slopes from the central polynomial profile over the
ENTIRE squeeze rectangle using outward intervals. This gives a uniform lower
bound D_B(s)<=min_x E(x,s), with

    U-D_B < 1.253*10^-12.                               (4)

K2198's AM-GM square bounds therefore enclose coordinates of the actual
compact-box minimizer. The uniform use is valid because the witness-energy
upper bound U applies to that minimizer and its energy at its own squeezes.
The square-gap coefficient uses each squeeze's lower endpoint. It is NOT
claimed that U bounds the fixed-squeeze optimum at every other point of B.
Representative conservative coordinate enclosures are

| n | certified e_n interval |
|---|---|
|0|[0.15517219,0.15517420]|
|1|[0.68761502,0.68762084]|
|2|[0.93464833,0.93465949]|
|3|[0.98832683,0.98834665]|
|4|[0.99798763,0.99802313]|
|5|[0.99963199,0.99969670]|

The probe retains narrower rational intervals internally. The true multiplier
is enclosed from n=0 stationarity, independently of the freely chosen dual
multiplier. K2198's backwards recurrence barrier certifies, for every n>=2,

    1/3 <= sqrt((1-e_(n+1))/(1-e_n)) <= 1/2.

The n=0,1 coordinate intervals extend this to global constants
L=3/20, sigma=1/3,rho=2/3. In particular the actual joint stationary profile
has the two-sided tail enclosure

    (6534/100000)9^-m <= 1-e_(2+m)
                       <= (6536/100000)4^-m, m>=0.     (5)

These are bounds on the actual infinite profile, not on the free polynomial
values beyond their role as dual inputs.

## 4. Infinite Schur certification at the actual profile

Apply K2204 with the enclosures above. Approximate constrained Riesz solutions
have support0..3. They are found from a single midpoint profile, rounded to
rational dyadics, and repaired to exact contrast zero. Midpoints are used only
to choose trial vectors; every coefficient of their actual error is enclosed
over the full true-profile and squeeze intervals.

Retain the residual at n=4 where the trial meets the fixed tail. Bound the
remaining residual from n=5 using the complementary geometric tail. The
stronger coercivity constant uses

    kappa=C min(s1_lower L,s0_lower sigma)(1-rho²)²/32,
    f0_lower=1-e0_upper,
    kappa_y=(1-rho²)/[1/(kappa f0_lower)+8rho/(C s0_lower)].

The LOWER bound on f0 is necessary. Replacing it by1-L would use an upper
bound and could overstate coercivity; that fault is explicitly tested. The
head residual and tail errors, rounded upward for display, satisfy

    eps1² < 0.812767, eps0² < 7.597256.

For the actual susceptibility K and trial Gram lower matrix T, K2204 gives
0<=K-T<=delta I with delta=eps1²+eps0². Rational interval arithmetic proves
the following conservative bounds for D-T-delta I:

    diagonal1 > 0.3752159,
    diagonal0 > 2.8368417,
    absolute off-diagonal < 0.0341998.

Exact diagonal dominance, not the decimal displays, proves the first
inequality in(1). The branch moment intervals give D<30I, so
S>(1/3)I>(1/100)D. This proves the second inequality. K2207's theorem now
applies with its formerly missing full-stationarity hypothesis established,
yielding(2) and the stated joint bound.

This covers the entire constrained energy completion, with a stronger cap
topology used only for nonlinear feasibility and the remainder theorem. The
point is not that a finite projected Hessian is positive: the nonzero
junction residual and every later occupation are included in the proof.

## Reproduction, controls and claim limits

Run `python tests/channel-swings/k2210_detector_stationary_certificate_probe.py`;
`--write` regenerates its report. No SciPy or numerical optimizer is needed;
embedded free inputs, rational arithmetic and inherited exact helpers suffice.
The probe checks complete boundary coverage, constant-profile dual equality,
exact full-tail contrast repair, the tangential Taylor radius, complementary
coercivity direction and retained junction. Five planted faults respectively
remove a face tile, corrupt the Taylor radius, change the contrast-tail
coefficient, use the wrong complementary bound, and remove the junction.
Failures are actual false predicates; crashes do not count as detections.

Written compactness/boundary-minimum arguments, inherited universal variational
and residual theorems, actual interval certificates, and finite control
identities are distinct evidence kinds. Internal independent review does not
claim external-expert, proof-assistant, novelty or experimental certification.
The next unresolved mathematical questions include global comparison and
joint uniqueness; the present existence result is not used to settle them.
