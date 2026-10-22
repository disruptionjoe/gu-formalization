---
title: "K1919: An exact finite-energy scalar obstacle branch"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1919_scalar_finite_budget_contact_solution.py
  - tests/channel-swings/k1919_scalar_finite_budget_contact_solution_probe.py
---

# K1919: An exact finite-energy scalar obstacle branch

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
result: global single-contact obstacle minimizer and exact low-energy primitive frontier
carrier: real phase H1_0 on symmetric interval with fixed contrast plateaux LAYER=toy CHIRALITY=N/A
pairing: derivative L2 energy and primitive sup norm ON=one_dimensional_interval
real_structure: real phases and even primitive after odd reflection
grading: scalar propagation directions only
action_owner: repository-construction -- prescribed phase-gradient cost
target: exact finite-budget optimum and short-time pulse limit MAP-TYPE=intertwiner
```

## 1. Result and scope

[K1917](k1917-scalar-energy-primitive-frontier-2026-10-22.md) reduces arbitrary
common plateau phase to the odd phase without raising energy or primitive norm.
Use its 0<a<b<L, h=theta/2>0, ell=b-a, g=L-b. Put

    D=g^3+a^3, E0=2h^2(1/g+1/a),
    Ac=h(ell+(g+a)/2),
    Delta_max=h D/(6 max(g^2,a^2)), A1=Ac-Delta_max,
    E1=E0+24 Delta_max^2/D.

For A in[A1,Ac], the GLOBAL relaxed minimum energy subject to ||F||<=A is

    E_min(A)=E0+24(Ac-A)^2/D.                         (1)

For A>=Ac it is E0. These formulas hold for unequal inner and outer gaps.
They solve a finite interval of the previously open contact problem, not
its entire small-A branch. For smooth compact phases, the infimum has the
same value. For every energy budget E in(E0,E1], the exact primitive infimum is

    A_E=Ac-sqrt[D(E-E0)/24].                         (2)

The smooth class is EMPTY at E<=E0: the relaxed minimum E0 is unattainable
there. This endpoint restriction matters when using a fixed-energy pulse law.

## 2. Explicit candidate, with all joins and obstacle signs

Write Delta=Ac-A and set

    p=hg/2-g^3 Delta/D, v=ha/2-a^3 Delta/D,
    q=p+h ell, p+v=A-h ell,
    H_l(t;z)= (3z/l^2-h/l)t^2+(h/l^2-2z/l^3)t^3.

Build F on the left half and reflect evenly:

* On[-L,-b], t=u+L in[0,g], F=H_g(t;p).
* On[-b,-a], F=p+h(u+b).
* On[-a,0], t=u+a in[0,a],
  F=q+h t+(3v/a^2-2h/a)t^2+(h/a^2-2v/a^3)t^3.

It has F=F'=0 at-L, F'=h on the left plateau, F'(0)=0 and F(0)=A.
Even reflection gives the correct-h right plateau and clamped right endpoint.
F and F' join continuously, so F is H2 and phi=F' is H1_0.

The interval Delta<=Delta_max is exactly a convenient simultaneous sign
certificate p in[hg/3,hg/2] and v in[ha/3,ha/2]. For the outer piece,

    H_g'(t;p)=t[(6p/g^2-2h/g)+(3h/g^2-6p/g^3)t]>=0.

Both bracket coefficients are nonnegative. For the inner piece, with x=t/a,

    F'= (1-x)[h+(6v/a-3h)x]>=0,

since the second factor is at least min(h,6v/a-2h)>=0.
Thus 0<=F<=A globally: no hidden lower-obstacle crossing. In the interior
of the parameter interval the only upper contact is u=0. At Delta_max a
curvature can vanish at an endpoint; all displayed inequalities remain valid.
The artificial interface into the prescribed plateau may jump F'', which is
allowed in H2; F' itself never jumps.

## 3. Global optimality, not merely stationary interpolation

For a segment of length l with clamped initial value and slope0, final value
z and slope h, the cubic has energy

    J_l(z)=12z^2/l^3-12hz/l^2+4h^2/l.

The inner segment is the reversed counterpart with increment v. Hence
E=2[J_g(p)+J_a(v)]. Minimizing this quadratic with p+v=A-h ell gives the
p,v above and(1). Finite-dimensional minimization alone would not prove
optimality among all admissible functions; the following certificate does.
Both free cubics have the SAME third derivative

    j=6h/g^2-12p/g^3=6h/a^2-12v/a^3=12Delta/D>=0.

For any even admissible competitor G, set eta=G-F. Its slope vanishes on
the prescribed plateaux; therefore eta is constant there and
eta(-b)=eta(-a). Integration by parts on the free intervals gives exactly

    integral F'' eta''=-2j eta(0)>=0,                 (3)

because eta(0)<=0. Endpoint terms vanish by clamping, plateau shear terms
cancel by their identical j, and eta'(0)=0 by evenness. There is no missing
point reaction at a plateau. Any noneven competitor can first be averaged
with its reflection, preserving its constraints and decreasing its energy.
Expanding ||G''||^2 proves E(G)>=E(F), with equality only for F by strict
convexity. Equation(3) is the global variational-inequality certificate.

At Delta=0 the same proof has j=0; phi is linear on each free gap and
E0 is its unconstrained minimum. Alternatively Cauchy-Schwarz on the two
outer ramps and the central ramp gives E>=2h^2/g+2h^2/a. Its unique equality
profile has derivative corners against constant plateaux, so cannot be smooth
compact for h>0. Every smooth member has E>E0.

## 4. Smooth recovery with exact plateaux and energy budgets

For each A>A0=h ell/2, K1917 supplies a smooth odd phase with primitive
norm strictly less than A. Mix a relaxed minimizer with this strict feasible
profile with weight epsilon. It remains H1_0, has exactly the prescribed
plateaux, and gains a positive primitive margin while its energy tends to the
relaxed minimum. Approximate it in H1 by smooth compact odd phases which
retain the plateau values exactly. One explicit density construction flattens
and rounds each join in a shrinking interval on its FREE side, rounds the
outer endpoint to zero inside the support, and leaves the closed prescribed
plateaux untouched. Values already match, and the finite piecewise bounded
slopes make the H1 error tend to zero; reflect the corrections oddly.
The smooth strict profile needs no changes on its own smooth pieces.
Uniform primitive error is at most sqrt(2L)||phi_n-phi||_2, so it fits in
the margin. Oddness enforces total integral0. This proves equality of smooth
and relaxed energy INFIMA throughout(1), not smooth attainment.

To invert under an EXACT energy cap E>E0, first use a relaxed profile with
energy E'<E approaching E from below, then the preceding recovery, choosing
mixing/rounding errors smaller than E-E'. Its primitive tends to(2).
For the opposite inequality, if A<A_E were feasible then monotonicity and
strict decrease of(1) between A_E and Ac would force energy>E, even when A
lies below A1: compare it with an intermediate cap in[A1,A_E).
At E=E1 use the same argument approaching from within the certified branch.
No claim about the all-budget contact set follows from this inversion.

## 5. Released successor: a growing central contact interval

The first branch reaching its sign threshold releases another exact regime.
For equal gaps a=g=s, set r in(0,1], tau=sr, and define

    A(r)=h[ell+s(1/2+r/3-1/(6r^2))],
    p(r)=hs(1/2-1/(6r^2)),
    E(r)=(h^2/s)[2+2/(3r^4)+8/(3r)].                 (4)

Keep the outer cubic H_s(t;p), the slope-h plateau, and use on the inner gap

    phi(t)=h(1-t/tau)^2 for0<=t<=tau,
    phi(t)=0 for tau<=t<=s.

Its primitive reaches A at t=tau and is flat thereafter. Reflect evenly.
The inner rise is h tau/3 and its energy is4h^2/(3tau). The outer shear and
inner free shear agree exactly at j=2h/tau^2. At the contact junction F''=0,
so integration by parts now gives

    integral F''(G''-F'')=-2j [G(-s+tau)-A]>=0.       (5)

The plateau terms cancel as before. This proves global optimality whenever
the candidate obeys BOTH obstacles. In particular it does not assume that an
unconstrained negative outer dip is harmless.

With x=t/s the outer cubic is

    F=hs[3(r^2-1)x^2+2x^3]/(6r^2).

Its unique interior minimum lies at x=1-r^2 and equals
-hs(1-r^2)^3/(6r^2). Thus exact feasibility is

    f(r)=r^6-3r^4+2r^3+6(1+ell/s)r^2-2>=0.          (6)

f(0)=-2, f(1)=4+6ell/s>0, and
f'(r)=12r(1+ell/s-r^2)+6r^2+6r^5>0 on(0,1].
There is a unique r0 in(0,1) with f(r0)=0. The ENTIRE interval[r0,1]
is certified, with E decreasing and A increasing in r. At r=1 it joins
A1=h(ell+2s/3), E1=16h^2/(3s) of the first branch. At r=r0 the lower
obstacle first touches; (5) still holds, so this endpoint is included.
Beyond it the candidate violates the lower obstacle and is rejected.

For E in[E1,E(r0)], the exact smooth primitive infimum is A(r), where r is
the unique solution E(r)=E in[r0,1]. The same strict-feasible mixing and
smooth recovery prove this; it is an implicit exact formula with a unique
root, not a grid-derived fit. For h=s=ell=1, r=1/2 gives A=1 and E=18,
with lower minimum-9/32. Hence A_18=1 exactly and the fixed-energy short-time
coefficient is2/c. This is a new global certificate for an actual higher
budget, not merely a feasible upper bound. The more strongly constrained
lower-contact branch and unequal-gap continuation remain unclassified.

## 6. Released duration and concrete finite-energy consequences

Combine(2) with K1917's fixed-energy short-time law:

    lim_(T->0) T^2 M_E(T)=2[Ac-sqrt(D(E-E0)/24)]/c,
    2A_E/(cT^2)<=M_E(T)<=2A_E/(cT^2)+2sqrt(2LE)/T.

This is an exact finite-budget coefficient, not a large-energy approximation.
The square-root improvement near E0 has an infinite right derivative; a
linear-in-extra-energy approximation at the feasibility threshold is wrong.
A peak cap M requires T>=sqrt(2A_E/(cM)).

For a=g=h=ell=1 (L=3,b=2), E0=4, Ac=2, A1=5/3, E1=16/3.
At E=5, A_E=2-1/sqrt(12), and the short-time coefficient is
(4-1/sqrt(3))/c. At A=7/4, the exact relaxed energy is19/4 and
p=v=3/8. This rational profile supplies an independently reproducible
full-piece control. An unequal-gap control a=1,g=2,h=ell=1 has
Ac=5/2, Delta_max=3/8, A1=17/8, E0=3, E1=27/8.

## 7. Verification and remaining frontier

The producer symbolically checks cubic endpoint data, energy, p/v minimization,
shear equality and all endpoint constants. A separate Fraction polynomial
probe integrates complete equal/unequal profiles and checks the distributional
boundary certificate without importing the producer. Corrupting a cubic
coefficient or an allocation fraction must fail after a green baseline.
Analytic sign factorizations, reflection and(3) carry global optimality;
finite evaluations alone would not. Strongest contrary extension is A<A1:
one of the convenient curvature signs fails there, so this branch cannot be
extended by extrapolating its energy polynomial. The equal-gap central-contact continuation is settled in section5; the subsequent
lower-obstacle branch and finite-duration optimization remain open. No claim
is made that this elementary spline calculation is novel.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
its nonzero southeast rival. SC-MAS-01/SC-CHI-02 ASSERT a stylized curvature
mass toy; SC-META-53 remains UNCERTAIN about indefinite spectra. None selects
the positive Hilbert bath, scalar control or physical units used here.
LT-SM8, LT-GR6b and AC-F1, source-register and canon verdicts remain unchanged.
The full20 raw/barred map, separate K/C, accessible algebra and physical domain
remain distinct constructions. These are independent mathematical results.
Analytic arguments carry universal claims; exact finite probes test identities
and examples, not expert acceptance, empirical prediction or formal proof.
