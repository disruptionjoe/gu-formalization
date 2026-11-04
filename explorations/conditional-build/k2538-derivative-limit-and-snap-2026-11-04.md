---
title: "K2538 Derivative closure, exact observer snap and finite-window resolution"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional well-prepared C2 convergence and exact endpoint derivative distinction; no empirical or native GU claim
scripts:
  - tests/channel-swings/k2538_derivative_limit_and_snap_probe.py
---

# K2538 Which derivative can distinguish the approaching histories?

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
result: K2538
carrier: positive sourced quadratic flat FLRW initial-value family on a fixed finite redshift interval LAYER=toy CHIRALITY=N/A
pairing: real scalar energy and finite difference observation ON=declared_carrier
real_structure: real positive a, H0 and fixed Omega in (0,1)
grading: history, redshift derivatives, proper-time cosmography and finite-window measurements are distinct
action_owner: repository-construction -- K2534 sourced quadratic metric comparator
target: derivative-sensitive discrimination of the K2536 family MAP-TYPE=evaluation
```

## Result and exact applicability

The EXACT jet-matched family of [K2536](k2536-einstein-limit-closure-2026-11-04.md) converges in C2 on every fixed interval [0,S], but not in C3 on that interval. Deceleration and scalar curvature converge at order a^-1; jerk converges at least at order a^-1/2. Observer snap has a nonzero, a-independent difference. This is a derivative distinction within the selected family, not a measured signal: fixed-width finite-difference observations still converge to the reference. A shrinking-window construction prices the resolution needed to retain the distinction and supplies exact blind spots of the limiting statistic.

SC-COS-50 ASSERTS its conditional variable-dark-energy requirement; SC-COS-51 ASSERTS its displacement/VEV claim; SC-COS-54 ASSERTS the stated two-movable-fields claim. None specifies this metric quadratic action, dust normalization or initial data. LT-GR2e and ledger0.263 remain unchanged; this result does not falsify or verify GU. The family keeps action-normalized Omega fixed, while dimensional dust and rho vary with a. The near-prepared Omega=0 countercontrol in K2536 is a DIFFERENT family and is preserved.

## 1. Reuse the original nonlinear equation

Use exactly K2536's s=3log(1+z), L=1-Omega+Omega exp(s), r=L^(3/4), x=r+u, and

    u''-u'+a f(s,u)=h(s,u), u(0)=u'(0)=0,
    f(s,u)=[(r+u)^(-1/3)-L(r+u)^(-5/3)]/36,
    h(s,u)=r'-r''+g(s)(r+u)^(-5/3),
    h0=h(s,0)=(exp(s)-1)Omega[1/3+Omega(3exp(s)-1)/16]L^(-5/4).

The exact original00 constraint and g are those in K2536; no new freely selectable velocity is introduced. On a fixed [0,S], K2536 already proves existence, x>=1/2 and u=O(a^-1), u'=O(a^-1/2), together with positive F,rho for sufficiently large a. Reuse that theorem; do not count its probe again.

Set

    c(s)=f_u(s,0)=1/(27L), p=h0/c=27L h0,
    q=p/a, w=u-q.

All derivatives of p needed below are bounded on this fixed interval. Since h0(0)=0, w(0)=0 and w'(0)=-p'(0)/a. Define

    R=q''-q'+a f(s,q)-h(s,q),
    F(s,w)=f(s,q+w)-f(s,q),
    H(s,w)=h(s,q+w)-h(s,q).

Then w''-w'+aF=H-R EXACTLY. Taylor's formula gives |R|<=M/a: a c q=h0 cancels, a O(q²)=O(a^-1), h(s,q)-h0=O(a^-1), and q',q''=O(a^-1). This is a uniform estimate on the compact tube, not a formal asymptotic solution.

## 2. The sharper shifted energy

For sufficiently large a, both q and u lie in a common tube where f_u>=m>0. All intermediate points q+theta w lie there. Uniform constants also satisfy |H|<=d|w| and |F_s|<=k|w|. Here the s derivative is at fixed w and INCLUDES the q' f_uu term; q'=O(a^-1) makes its bound uniform. Since F(s,0)=F_s(s,0)=0, the primitive Vw=integral_0^w F(s,v)dv obeys

    Vw>=m w²/2, |(Vw)_s|<=k w²/2.

Put E=w'²/2+a Vw. Differentiation on the exact equation gives

    E'=w'²+H w'-R w'+a(Vw)_s.

Using |w|²<=2E/(am), |w'|²<=2E, a>=1, and Young's inequality yields

    E' <= C E + M²/(2a²),
    C=3+d(1+1/m)+k/m,
    E(0)=p'(0)²/(2a²).

Gronwall therefore gives E<=B/a² with B finite and independent of a. Consequently

    w=O(a^-3/2), w'=O(a^-1),
    u=p/a+O(a^-3/2), u'=O(a^-1).

Finally u''=u'-a f(s,u)+h(s,u). Substitute u=q+w and use the exact leading cancellation: a[f(s,u)-f(s,q)]=O(a^-1/2), while the other residual terms are O(a^-1). Thus u''=O(a^-1/2). No residual derivatives or convergence of a perturbation series are assumed. This proves C2 convergence on [0,S] for the SAME original family.

## 3. The endpoint that does not converge

At s=0 all differences through u'' vanish. Differentiate the original equation once. Because u=u'=u''=0 there and f(s,0)=0 identically, f_s(0,0)=0, so

    u'''(0)=h0'(0)=d0=Omega/3+Omega²/8>0.

This is exact for every finite a, not a numerical asymptotic observation. Therefore C3 convergence on [0,S] is impossible. This statement alone does not prove nonconvergence on every interval separated from zero.

Let A denote the cosmological scale factor (not the large parameter a). Since s=-3log A and d/dt=-3H d/ds, H/H0=x^(2/3), the actual proper-time observables are

    deceleration = -1+2x'/x,
    Ricci scalar = 12H0² x^(1/3)(x-x'),
    jerk = 1-6x'/x+2(x'/x)²+6x''/x.

Their errors have the rates stated above, at common fixed H0. For snap=A''''/(A H^4), its highest-redshift-derivative coefficient is -18 x'''/x; all its lower-jet differences vanish at zero. Hence

    snap_a(0)-snap_reference(0)=-18d0=-6Omega-9Omega²/4.

At Omega=3/10 this is -801/400. The probe obtains the coefficient by repeated proper-time differentiation, not by assuming a cosmographic convention. This is a selected-initial-data discriminator; it does not establish growth, slip, local matter response or practical measurability. Altering initial velocity to suppress the initial layer must rederive the original00 constraint and source normalization.

## 4. Execute the finite-window consumer

For a fixed positive h with 3h<=S, the third forward difference of the history error is

    D3_h u=[u(3h)-3u(2h)+3u(h)-u(0)]/h³.

K2536 gives |D3_h u|<=8D/(a h³); it therefore tends to zero for every fixed window. The sharper decomposition gives the stronger useful inequality

    |D3_h u| <= sup|p'''|/a + 8Cw/(a^(3/2)h³).

The first term uses the exact triple-integral identity for finite differences; the second uses sup|w|<=Cw a^-3/2. A fixed positive lower gap in this statistic requires h=O(a^-1/2) as a grows. This is a necessary resolution scaling, not sufficient experimental sensitivity. If each of four sampled x values has absolute error at most epsilon, worst-case propagated error is exactly 8epsilon/h³: the alternating errors attain it. Retaining bounded error at h proportional to a^-1/2 therefore requires epsilon=O(a^-3/2). No actual instrument is claimed to supply this.

The shrinking-window behavior is itself computable. Put epsilon=a^-1/2, s=epsilon T, u=epsilon³ U(T). The exact rescaled equation has a smooth epsilon=0 extension on bounded T intervals, since f(s,0)=0 and h(0,0)=0. It tends to

    U''+c0 U=d0 T, U(0)=U'(0)=0, c0=1/27.

Local ODE continuous dependence proves

    U(T) -> (d0/c0)[T-sin(sqrt(c0)T)/sqrt(c0)]

in C2 on every fixed bounded T interval. Thus h=epsilon b gives a limiting D3_h u equal to the third forward difference of this explicit U at spacing b. It tends to d0 as b tends to zero, but VANISHES at b=2pi/sqrt(c0). Resolving a small scale is not enough if sampling aliases the oscillation. The finite-window construction is a conditional mathematical test design, not a direct snap measurement or universal parameter-family exclusion.

## Evidence and next question

The shifted-energy proof, exact initial jet and singularly rescaled ODE bear the continuum claims. The probe checks original-force derivatives, proper-time observable identities, energy coefficients and exact finite-difference controls; reporting counts are not proofs. Independent review checks the argument and its scope. No novelty, proof-assistant or external-expert certification is claimed.

The derivative question is now sharply split: C2 histories and their displayed curvature/jerk observables approach the reference; observer snap remains distinct for this initialization, but extracting it requires shrinking windows and increasingly precise data. A physical discrimination claim still needs a justified initial/source restriction and an actual joint measurement/noise model. Repeating fixed-width background forecasts cannot acquire the missing derivative information.
