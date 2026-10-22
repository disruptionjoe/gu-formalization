---
title: "K1921: The complete equal-gap scalar energy frontier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1921_scalar_lower_contact_global_solution.py
  - tests/channel-swings/k1921_scalar_lower_contact_global_solution_probe.py
---

# K1921: The complete equal-gap scalar energy frontier

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
result: global lower-contact obstacle solution, complete equal-gap energy frontier and pulse consumer
carrier: real H2 clamped primitive on symmetric interval with fixed slope plateaux LAYER=toy CHIRALITY=N/A
pairing: curvature L2 energy and primitive sup norm ON=one_dimensional_interval
real_structure: real even primitive and odd phase
grading: scalar propagation directions only
action_owner: repository-construction -- prescribed phase-gradient cost
target: global constrained energy and its exact inverse MAP-TYPE=intertwiner
```

## 1. Scope and complete result

Use [K1919](k1919-scalar-finite-budget-contact-solution-2026-10-22.md)'s
symmetric plateaux with equal free gaps a=g=s>0, plateau length ell>0 and
height h>0, so L=2s+ell. Minimize E=integral(F'')^2 over real H2 clamped
primitives with F'=h on the left plateau, F'=-h on the right and |F|<=A.
Reflection reduces to even F, including the arbitrary common plateau-phase
problem by K1917. Write A0=h ell/2, Ac=h(ell+s), E0=4h^2/s.

K1919 gives the single-contact and growing-central-contact branches. This
note supplies the remaining lower-contact branch and therefore the entire
relaxed frontier for equal gaps. It also determines the smooth primitive
infimum for EVERY E>E0 by unique inversion. Smooth feasibility at E<=E0
remains empty. The intermediate unequal-gap contact topology and finite-duration pulse
optimization are not solved here.

Let r0 be K1919's unique root in(0,1) of

    f(x)=x^6-3x^4+2x^3+6(1+ell/s)x^2-2.

For x in[r0,1), let w be the unique positive root

    (1+x^2+2/x)w^2+[4s(1-x^2)+6ell]w-2s^2(1-x^2)=0.   (1)

Set

    d=s-w, tau=w/x, k=h(1-x^2)/w, j=2h/tau^2,
    A=k d^2/6,
    E=2[12A^2/d^3+k^2 w+k j w^2+j^2 w^3/3+4h^2/(3tau)]. (2)

These give the GLOBAL minimum energy at cap A. A decreases continuously from
the first-lower-contact cap to A0 as x increases to1, and E increases
continuously to infinity. Thus no unclassified equal-gap cap remains between
A0 and Ac. At A<=A0 the admissible H1 phase class is empty; continuity at
nonzero plateau endpoints precludes attaining the primitive-width floor.

## 2. Explicit profile and obstacle feasibility

On the left outer gap use t=u+L. Before contact, 0<=t<=d, put

    F=-A[3(t/d)^2-2(t/d)^3].                          (3)

For d<=t<=s, y=t-d, put

    F=-A+k y^2/2+j y^3/6.                            (4)

At t=s write p=F(s). Continue with slope h over the left plateau of length
ell. In the inner gap, with z measured from its left endpoint, set

    F=p+h ell+h[z-z^2/tau+z^3/(3tau^2)]  (0<=z<=tau),
    F=A                                  (tau<=z<=s). (5)

Reflect evenly to the right half. Equations(1)-(2) imply

    k d^2/6=A,  k w+j w^2/2=h,
    p+h ell+h tau/3=A.                               (6)

The value, slope and curvature match at the lower contact t=d; the slope
matches prescribed plateaux and the central contact. The plateau interfaces
may jump curvature because the slope is prescribed there. This is allowed
in H2. Formula(3) decreases from0 to-A, (4) increases from-A to p, and the
plateau and(5) increase to A. Thus both obstacles hold everywhere.

To verify lengths and reaction signs without numerical root assumptions,
call the left side of(1) P(w,x). For fixed x it is strictly increasing for
w>=0, with P(0,x)<0. Direct substitution gives

    P(s x^2,x)=s^2 f(x)>=0.

Hence 0<w<=s x^2<s, tau<=sx<=s, d>0. The lower-contact shear jump is

    mu=j-12A/d^3=2h(s x^2-w)/(w^2 d)>=0.             (7)

At x=r0 this reaction vanishes, w=s r0^2 and tau=s r0. The profile is
exactly K1919's limiting central-contact cubic split at its minimum.
No lower contact INTERVAL is inserted: the left clamped-to-minimum cubic
has positive curvature there, and falsely flattening it would break moment
matching. The contact is a point on each outer gap.

## 3. Global variational certificate

For any even feasible competitor G put eta=G-F. Let u_-=-L+d denote the
left lower-contact point and u_+=-s+tau the start of central upper contact.
Clamping removes outer boundary terms. At the prescribed plateau eta'=0
and eta has the same value at its two endpoints. Their shear terms cancel.
At u_- the curvatures match; at u_+ curvature vanishes. Integration by parts
on each free cubic therefore yields

    integral F'' eta''=2[mu eta(u_-)-j eta(u_+)]>=0.   (8)

Indeed eta(u_-)>=0 and eta(u_+)<=0. No condition eta'(u_-)=0 is imposed on
a competitor: it cancels through moment matching. Expanding the square
proves E(G)>=E(F). Strict convexity on clamped H2 gives uniqueness, and
reflection covers noneven competitors. This is a continuum proof; polynomial
checks below only verify its coefficients and boundary algebra.

## 4. Parameter coverage, smooth inversion and duration

The positive root w(x) is continuous. As x approaches1, equation(1) gives
w/(1-x^2)->s^2/(3ell), hence A->A0. At r0 it matches K1919 exactly.
If two distinct x gave the same A, strict uniqueness in(8) would identify
the profiles. Their lower-contact point fixes w, and their central contact
fixes tau, so x=w/tau would also coincide: contradiction. A is therefore
continuous and injective, hence strictly decreasing by its endpoints. This
avoids an unproved derivative sign of a radical expression.

The energy is strictly decreasing with A below Ac. To see strictness for
A<A'<Ac, mix the cap-A minimizer with the unconstrained minimizer at Ac,
with a sufficiently small positive weight so the cap stays below A'. Strict
convexity and the strictly smaller unconstrained energy lower E. Together
with the preceding branches, this proves unique inversion for every E>E0.
K1919's exact-plateau smoothing with strict cap and energy slack applies to
these finite piecewise cubics. Thus smooth and relaxed INFIMA agree; the
minimizing piecewise phase need not itself be smooth.

The released finite-energy pulse law is consequently specified for every
budget, not only the earlier intervals:

    lim_(T->0) T^2 M_E(T)=2A_E/c,
    2A_E/(cT^2)<=M_E(T)<=2A_E/(cT^2)+2sqrt(2LE)/T.     (9)

For E<=E0 there is no smooth admissible phase. Equation(9) is not a closed
finite-T optimizer. It reuses K1917's pulse theorem with a now fully
specified equal-gap A_E.

## 5. Released high-energy check and an exact nontrivial profile

From(6),

    A-A0=h[tau/6+w/4-w x^2/12].

As x->1, tau/w->1, k->3h ell/s^2, and
E w->16h^2/3. Hence

    lim_(E->infinity) E(A_E-A0)=16h^3/9=2theta^3/9.    (10)

This independently matches K1917's asymptotic coefficient using the exact
optimizer. It does not turn an ordered small-T/high-E limit into a joint
uniform expansion.

A rational control takes s=h=1, x=3/4 and w=1/4. Equation(1) fixes
ell=133/1152>0. Then d=3/4, tau=1/3, k=7/4, j=18,
A=21/128, mu=40/3 and

    E=147/8.

The primitive has lower contact at t=3/4 and central contact after1/3 of
the inner gap. Positive mu certifies that this is beyond first contact.
The exact controls check the actual piecewise profile, joins, energy and
boundary functional, with deliberately corrupted coefficients and shear.

## 6. Released unequal-gap high-budget branch

The same certificate also supplies a nonempty high-budget interval for EVERY
pair a,g>0. Replace s by g in(1)-(4), use inner gap length a in(5), and
require additionally tau=w/x<=a. Keep w<=g x^2, so mu>=0. All endpoint,
plateau and reaction cancellations are unchanged. Since tau tends to zero
as x tends to1, these conditions hold throughout some final interval of x.
The cap tends to h ell/2 and the energy diverges, so this covers all
sufficiently high budgets. Uniqueness again makes A injective on any such
interval. It does not classify the intermediate unequal-gap topology.

For example the exact profile above also works with a=1/2, g=1,
ell=133/1152, h=1: tau=1/3 fits the shorter inner gap. Its cap21/128,
energy147/8 and reaction40/3 are unchanged; only the flat contact interval
shortens. Thus once the central gap can contain the two transition pieces,
extra central contact length costs no energy. The universal high-energy
coefficient16h^3/9 is unchanged. This is an actual unequal-gap certified
profile and high-budget family, not an extrapolation of K1919's low-budget
formula. Full arbitrary-gap energy inversion still needs the intervening
contact regimes.

## 7. Hostile review and known context

No claim of a new general obstacle theory is made. The method is the usual
fourth-order convex variational inequality; for context see
[Azam et al. (2013), fourth-order obstacle BVP](https://doi.org/10.1155/2013/308692).
The present proof is explicit and does not import its numerical conclusions.
Strongest overclaim is full intermediate unequal-gap or finite-duration optimality.
Strongest contrary construction is a feasible nonsymmetric competitor;
reflection and strict convexity cover it. Weakest seam is a missing point
moment term: independent boundary tests allow arbitrary eta' at lower
contact, and verify its cancellation. Smooth attainment is not claimed.

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
