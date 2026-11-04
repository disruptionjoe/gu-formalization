---
title: "K2540 Same-family initialization repair and uniform C3 closure"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional source-data repair and compact-interval C3 closure; no empirical or native GU claim
scripts:
  - tests/channel-swings/k2540_prepared_cosmology_source_data_probe.py
---

# K2540 The derivative test needs an independently fixed initialization

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
result: K2540
carrier: sourced quadratic flat FLRW action family with explicitly shifted rho and initial/source data LAYER=toy CHIRALITY=N/A
pairing: real scalar energy and finite difference observation ON=declared_carrier
real_structure: real positive a, H0 and fixed Omega in (0,1)
grading: frozen seed, repaired seed, dimensional dust and action-normalized Omega remain distinct
action_owner: repository-construction -- K2534 sourced quadratic metric comparator
target: initialization robustness and uniform derivative closure MAP-TYPE=evaluation
```

## Result and source boundary

The observer snap difference in [K2538](k2538-derivative-limit-and-snap-2026-11-04.md) is not robust across its broader sourced action family. An explicitly admissible O(1/a) shift of initial velocity, with the original00 source normalization recomputed once, matches observer snap exactly. A separate branch matches the third redshift derivative exactly. Both families converge in C3 on every fixed observer-inclusive redshift interval; both retain a nonzero limiting fourth-derivative discrepancy. This sharpens the actual missing assumption for a derivative test: the initial/source data must be constrained independently.

The quadratic action form, fixed H0, U0 and action-normalized Omega are unchanged. The coefficient-complete action changes: its constant coefficient rho shifts, as do initial velocity and the source normalization q0. No independently measured density is held fixed. Neither branch is the frozen seed of K2538, whose C2/not-C3 result remains true. SC-COS-50 ASSERTS its conditional variable-dark-energy demand, SC-COS-51 ASSERTS its connection-displacement/VEV claim and SC-COS-54 ASSERTS its two-movable-fields claim. They do not select this quadratic metric action or these data. LT-GR2e and ledger0.263 remain unchanged; there is no empirical or native GU credit.

## 1. Preserve the original equation and its source

Use the same normalized variables as [K2536](k2536-einstein-limit-closure-2026-11-04.md): s=3log(1+z), t=exp(s), x=U/U0, a=alpha/U0^(4/3), b=rho/U0^(8/3), fixed 0<Omega<1. Write

    v=3Omega/4, y0=v+delta,
    b_ref=6a(1-Omega)-(81/2)Omega²-72(1-v)Omega,
    b=b_ref+72(Omega-3)delta,
    F0/U0^(4/3)=a+12(1-y0),
    q0=3F0 U0^(4/3)Omega.

Here q0 is the dust normalization in the inherited K2534 units, not an independently measured density. The ORIGINAL reduced equation becomes

    x''=x'-a/(36x^(1/3))
        +[b+6(a+12(1-y0))Omega exp(s)]/(216x^(5/3)),
    x(0)=1, x'(0)=y0.

The dust coefficient is recomputed from the new F0, then held fixed in the evolution. It is not independently fitted at each redshift. Direct substitution gives x''(0)=3Omega(4-Omega)/16, exactly the reference r=(1-Omega+Omega exp(s))^(3/4) second derivative. Holding b fixed instead would lose that property; holding dimensional dust fixed would be a different problem.

Let d0=Omega/3+Omega²/8. Total differentiation of this original equation gives

    x'''(0)-r'''(0)=d0-A delta+(5/3)delta²,
    A=a/27-11Omega/12-5Omega²/16.

For A>0 and A²>(20/3)d0 the small root

    delta_3=2d0/[A+sqrt(A²-(20/3)d0)]

matches the third redshift derivative exactly. These conditions hold for sufficiently large positive a.

## 2. Match proper-time snap, rather than confuse the two derivatives

At common H0, H/H0=x^(2/3) and d/dt_proper=-3H d/ds. Direct repeated differentiation of the scale factor gives

    snap=1-12x'/x+24x''/x+20(x'/x)²
           -30x'x''/x²-18x'''/x.

Because y0 changes, matching x''' alone does not match snap exactly. Its actual observer difference is

    snap_a(0)-snap_ref(0)=-18d0+B delta-10delta²,
    B=2a/3-9Omega-12.

For B>0 and B²>720d0, choose instead

    delta_snap=36d0/[B+sqrt(B²-720d0)].

Then observer snap agrees EXACTLY at finite a. Both choices satisfy delta=d1/a+O(a^-2), d1=27d0. The first-jet error tends to zero, the second jet agrees exactly, and the third-jet error on the snap branch is O(a^-1). The two roots are different; no simultaneous exact matching claim is made. Positive rho and F hold on each fixed interval for sufficiently large a, as proved next.

## 3. A uniform C3 theorem for actual solutions

Reuse K2536's functions f,h,c=f_u(s,0)=1/(27L), h0=h(s,0), p=h0/c and u=x-r. The exact modified equation is

    u''-u'+a f(s,u)=h(s,u)+delta k(s,u),
    k(s,u)=[-1+Omega(1-exp(s))/3](r+u)^(-5/3),
    u(0)=0, u'(0)=delta.

On a fixed compact interval, the original coercive bootstrap applies with this uniformly bounded forcing and delta=O(a^-1). Its initial energy is still O(a^-1). Hence actual solutions exist throughout the interval, x stays bounded away from zero, and u=O(a^-1),u'=O(a^-1/2). This supplies the common tube before the sharper estimate; it assumes no formal series solution.

Define a second slow correction (call it p2, not the time variable):

    p2=[h_u(s,0)p+d1 k(s,0)-p''+p'
        -(1/2)f_uu(s,0)p²]/c,
    q=p/a+p2/a².

The coefficient of a^-1 in the exact residual

    R=q''-q'+a f(s,q)-h(s,q)-delta k(s,q)

vanishes. Taylor expansion with bounded derivatives on the common tube gives R=O(a^-2) and R'=O(a^-2), uniformly. Derivatives of delta with respect to s are zero. This residual estimate, not convergence of an asymptotic series, is all that is used.

Set w=u-q, F=f(s,q+w)-f(s,q) and H=h(s,q+w)-h(s,q)+delta[k(s,q+w)-k(s,q)]. The exact equation is w''-w'+aF=H-R. For sufficiently large a, F_w>=m>0, |H|<=C|w| and |F_s|<=C|w| uniformly, including the q' term. The same energy

    E=w'²/2+a integral_0^w F(s,z)dz

obeys E'<=C E+C_R/a^4. Here p(0)=0 and p'(0)=d1, so w(0)=O(a^-2),w'(0)=O(a^-2), giving E(0)=O(a^-3). Gronwall proves

    w=O(a^-2), w'=O(a^-3/2),
    u=O(a^-1), u'=O(a^-1).

The exact w equation then gives w''=O(a^-1). Differentiating it once gives w'''=O(a^-1/2): the largest term is a F_w w'=O(a^-1/2); a F_s=O(a^-1), and the remaining total derivatives are bounded by the preceding estimates and R'. Therefore u''=O(a^-1),u'''=O(a^-1/2). Both repaired families converge in C3. The proof actually applies to any delta=d1/a+O(a^-2) with the displayed b/source relation.

Finally b=6a(1-Omega)+O(1)>0, and F/U0^(4/3)=a+12x^(1/3)(x-x')>0 for large a because x,x' stay bounded. This verifies that the construction remains in the positive branch. No infinite-redshift, arbitrary-data attraction or physically selected preparation is asserted.

## 4. Execute the next derivative and finite-data consequence

Differentiating the original equation twice, inserting delta=d1/a+O(a^-2), and taking the limit yields

    lim [x''''(0)-r''''(0)]
      =Omega(16+16Omega-3Omega²)/48 >0.

At Omega=3/10 this is 2053/16000. Thus these explicit repaired families do not converge in C4 on intervals containing the observer. This is a contrary control on the stronger preparation claim, not a new universal family-level discriminator. It follows independently from p''(0)/27 and the exact original fourth jet.

For a positive spacing h with 4h<=S, the fourth forward difference of u obeys

    |D4_h u| <= sup|p''''|/a+sup|p2''''|/a²+16Cw/(a²h⁴).

The smooth terms use the exact fourfold integral formula; the last uses the proven uniform remainder. A persistent positive difference requires h=O(a^-1/2). The exact worst-case five-sample error is 16epsilon/h⁴, attained by alternating signed errors. At that spacing, bounded error requires epsilon=O(a^-2). These are necessary scaling statements, not sufficient sensitivity or a forecast. The source/initial-data freedom must be fixed before escalating measurement precision.

## Evidence and remaining question

The probe differentiates the original force, reconstructs proper-time snap, checks both exact roots, the normalization change, slow residual coefficients, fourth-jet limit and sharp finite-difference weights. Independent review addresses the continuum energy/continuation argument; exact algebra checks do not replace that argument. No novelty, proof-assistant or external-expert certification is claimed.

The immediate snap exclusion is repaired inside the same conditional action family. A useful physical successor is an independently justified source/initial-state restriction or full perturbation observable, with a shared physical observation model. Merely selecting the next derivative or repeating a fixed-width forecast cannot supply that restriction. The earlier frozen-seed result and all its uncertainty limits remain evidence.
