---
title: "K2606 Interior stopping second corrector and inverse resource offset"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: second coefficient on compact strictly interior multiplier intervals; no switch-uniform expansion or exact optimal count
scripts:
  - tests/channel-swings/k2606_interior_stopping_second_corrector_probe.py
---

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
result: K2606
carrier: original adaptive randomized fair test/use stopping law, positive-trial resource and finite completed schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original leakage and price per positive trial ON=declared_carrier
real_structure: real probabilities and logarithmic costs; compact strictly interior multiplier intervals
grading: asymptotic value coefficient, finite schedule construction, count ties and physical probability remain distinct
action_owner: repository-construction -- supplied fair stopping law
target: priced second corrector and constrained/inverse resource asymptotics MAP-TYPE=evaluation
```

# A second coefficient with the endpoint cell controlled

## Result and boundary

Fix a compact rectangle 0<S0<=S<=1/2 and 2/3<lambda0<=lambda<=4/5. Write V=V_lambda(S), C=C(S,lambda) from K2602. The actual original-policy priced value has the expansion

    Q(k)=V-2sqrt(Ck)+Z(S)k+O(k^(3/2)).                 (1)

The explicit corrector Z below therefore gives

    V-F(M)=C/M-C Z(S)/M²+O(M^-3),
    R_min(eta)=C/eta-Z(S)+O(eta).                     (2)

Constants are uniform on the declared compact rectangle. Every optimizer at price k has R=sqrt(C/k)-Z(S)+O(1), without differentiability or a unique optimal count. Its bounded error does NOT identify a convergent constant resource offset.

K2604 supplies only an O(M^-2) error bound; this result identifies the coefficient on a narrower parameter domain. K2577 already settles the subcritical coefficient and K2597/K2599 settle their fixed-count activation questions. Neither is claimed anew. The action ratio here stays uniformly strictly inside (0,1); no assertion across lambda=2/3 or a switching curve follows.

This is GU-independent mathematics of a supplied probability law. SC-META-53 remains UNCERTAIN; source, ledger0.263 LT-SM8/LT-GR6b and canon remain unchanged. No physical detector, native probability, novelty, external-expert or proof-assistant certification.

## 1. Actual law and smooth coefficients

For 0<=a=rb<=b<=s, reuse

    w=log(1-alpha(r)b)-log(1-beta(r)b),
    alpha=(1+6r+r²)/(4(1+r)), beta=(1+r)/2,
    g=(1-r)²/[2(1+r)], B=beta²-alpha²,
    v'=-q(v), v(0)=1/lambda,
    q(v)=2sqrt(1+2v)-2-v, r(s)=q'(v(s)),
    G=g''(r)=4/(1+r)^3, D=B-qr/2, L=lambda D,
    c=sqrt(2/L), W'+rW=2sqrt(2lambda D), W(0)=0.

W(S)=2sqrt C. All quantities and every fixed derivative are bounded uniformly on the rectangle, with D and r bounded away from zero and r bounded away from one. This follows from the explicit smooth interior flow, K2604's D bounds, and compactness; the lower lambda margin is essential. The original residual is d_V=(1+a)V(s)+2lambda w-V(s-b).

Define derivatives in s, while B_r denotes derivative in its argument:

    r'=q/G, D'=D_r q/G,
    v_third=-qr²+q²/G,
    E=2(beta³-alpha³)/3+v_third/6,
    W''=sqrt(2lambda)D'/sqrtD-r'W-rW'.

The new linear ODE is

    Z'+rZ=(c lambda B_r-W)²/(2lambda G)
                         -c²lambda E-c W''/2, Z(0)=0.    (3)

Thus Z is explicitly determined by the same smooth scalar flow; it introduces no free fitted parameter. The usual integrating factor gives Z(S)=integral_0^S exp(-integral_s^S r) times the right-hand side of(3) ds.

## 2. Actual Bellman residual, including all actions

Set k=e² and U=V-eW+e²Z. For positive b the residual is

    Delta=(1+rb)U(s)+2lambda w(rb,b)+2e²-U(s-b).       (4)

The factor TWO prices the actual expected positive trials. Zero-score padding is deleted and pays no such charge. A fourth-order Taylor expansion of the actual logarithm and smooth potentials is uniform for small b,e. For fixed b>0, its derivative in the actual action ratio, divided by b, is

    lambda[v+g'(r_actual)]-eW+lambda b B_r(r_actual)
                                            +O((b+e)²).

Strong convexity g''>=1/2 on[0,1] and the strict interior minimum imply the global minimizer of this expression remains interior and is smooth for small b,e. The implicit-function theorem yields

    r_actual=r+(eW-lambda bB_r)/(lambda G)+O((b+e)²).

This minimizes the actual residual over all actions; it does not assume a policy is nearoptimal. Substitution gives

    min_r Delta = L(b-ec)²
      + b[e²(Z'+rZ)+ebW''/2+lambda E b²
                    -(lambda B_r b-eW)²/(2lambda G)]
      + Remainder,
    |Remainder| <= K b(b+e)^3.                        (5)

The cubic bracket vanishes at b=ec precisely by(3).

For completeness, the uniform global lower estimate in(5) is obtained as follows. For b>=delta, K2561's positive global original residual d_V>=c0 b² dominates the O(eb) change. For K1 e<=b<=delta, choose K1>2 max c, then delta small; the leading quadratic dominates O(b³+eb²+e²b). For b<=e min(c)/2, the square is at least a fixed multiple of e² and the other terms are O(e³). On the remaining compact range b/e comparable to one, the cubic term is e³h_s(b/e), with h_s(c)=0 and bounded derivative. Hence it is bounded in magnitude by K e²|b-ec|. Young's inequality absorbs half the leading square, leaving -K'e^4. In this range b>=c1 e, this is bounded below by -K''e³b. Thus globally Delta>=-K e³b.

Adding K e³s to U adds K e³(b+as)>=K e³b to its residual. It is an actual positive bounded supersolution with terminal value1. The original-law telescope and clipping argument of K2604 apply to every adaptive/randomized policy, including abort, overshoots and nonabsorption. Therefore Q(e²)<=U(S)+O(e³). All inequalities concern the original law; the asymptotic minimizer alone is not the verification theorem.

## 3. A finite policy with no bad final cell

A clipped final cell can cost O(e²), which would erase the coefficient in(1). Use instead

    T(s)=integral_0^s 1/c(z) dz,
    n=nearest(T(S)/e), tau=T(S)/n,
    T(s_i)=(n-i+1)tau, i=1,...,n+1.

For small e, n>=1, tau=e+O(e²), s1=S and s_(n+1)=0. By Taylor's theorem every step, including the last, obeys b_i=s_i-s_(i+1)=e c(s_i)+O(e²). Set

    a_i=b_i[r(s_i)+e (W(s_i)-c(s_i)lambda B_r)/(lambda G)].

The uniform interior margin makes every action legal for sufficiently small e. The cubic coefficient in(5) vanishes and the step displacement is O(e²), so the exact per-stage residual is O(e^4). There are O(e^-1) stages. With the ACTUAL prefixes P_i=product_(j<=i)(1+a_j)^-1, the exact telescope is

    J-e²R=U(S)-sum_i P_i Delta_i=U(S)+O(e³),
    R=2sum_i P_i, J=P_n-2lambda sum_i P_i w(a_i,b_i).

This is a finite completed original-law policy and proves the matching bound. Nearest integer rounding first affects the priced O(e³) remainder, not Z. No exact optimal count or third coefficient is asserted.

## 4. Executed dual, inverse and optimizer consequences

K2571 section5 proves exact strong duality F(M)=min_(e>=0)[Q(e²)+Me²]. A minimizing e has e²<=V/M since Q>=0; hence e tends to zero. The local bound Q(e²)>=V-We-K0e² then gives e<=W/(M-K0)=O(M^-1), since its objective is at most V. The remainder in(1) is therefore O(M^-3) at every minimizer. Completing the quadratic, and testing its unconstrained minimum, proves

    F(M)=V-W²/[4(M+Z)]+O(M^-3)=V-C/(M+Z)+O(M^-3).

No derivative of a big-O remainder has been taken. Strict increase and attainment inherited from K2571 allow inversion by bracketing M=C/eta-Z plus or minus K eta, proving(2).

For any price optimizer, its supporting affine line bounds Q at prices k(1 plus or minus sqrt(k)). Secants of -2sqrt(Ck) differ from its derivative by O(1) on these scales; the O(k^(3/2)) value remainder divided by k^(3/2) is also O(1), while Zk contributes exactly Z. Thus R=sqrt(C/k)-Z+O(1), including nondifferentiable count ties. Together with exp(-S)<=P_i<=1 it preserves the deterministic n=Theta(k^-1/2) law without selecting a unique count.

## 5. The inverse offset is strictly positive

The corrector has a rigorous sign, not merely the sign of the numerical examples. Set H=W/sqrt(2lambda) and z=H/sqrtD. Equation(3) simplifies exactly to

    Z'+rZ=(D/G)z²+A(r)z+K(r),
    A=(q-2B_r)/G-r²,
    K=B_r²/(DG)-2E/D-D'/D+2r.

Explicitly,

    A=-(3r^4+14r³+24r²-22r-3)/16,
    K=(27r^7+279r^6+1151r^5+2939r^4+641r³
          -1451r²-91r+89)/[48(r+1)(3r+1)(r²+6r-3)].

Exact rational Bernstein certificates in the probe prove on the WHOLE interval 0<=r<=1/6 that 0<=A<=3/8, D/G<=1/16, 0<=K_r<=11/4 and r'=q/G<=1/5. Denominator signs are checked, not presumed. Also K(0)=-89/144 and K(7/100)<-47/100. For lambda<=4/5, r(0)=2/sqrt(1+2/lambda)-1<7/100, whence

    K(r(s)) <= -47/100+11s/20 <0, 0<=s<=1/2.

Since H'+rH=2sqrtD and H(0)=0, 0<=H<=2s sqrt(3/16). With D>=1/10 this gives 0<=z<=11s/4. The integrating factor P(s)=exp(-integral_s^S r) lies in[11/12,1]. Bound the positive quadratic/linear terms with P<=1, and the negative K upper bound with P>=11/12. Direct integration yields

    Z(S)<=-517S/1200+737S²/960+121S³/768
          <=-583S/76800 < -S/200.

Conversely the right side of the Z equation is at least K>=-89/144; its weighted integral is at least -89S/144. Therefore

    -89S/144 <= Z(S) <= -583S/76800.                 (6)

The M^-2 gap coefficient -CZ is strictly positive, between 583CS/76800 and 89CS/144. The additive inverse-resource overhead -Z is strictly positive in the corresponding interval. This rules out zero or negative overhead at this order within the proved interior model, and supplies quantitative bounds without evaluating the corrector ODE. The rational coefficient inequalities include r=0 as an algebraic endpoint; the asymptotic theorem still requires the stated strict interior multiplier margin.

## Evidence and next condition

The probe checks the original log cubic term, action-square completion, actual reduced cubic cancellation, a rational initial coefficient, original finite prefix telescope, dual/inverse series, and bad-clipping/wrong-price controls. It constructs finite equal-clock policies and evaluates their original costs. The ODE/clock computation is labeled numerical illustration, with tighter-tolerance agreement; it is not an interval proof of the universal expansion. The uniform analytic argument above supplies that result and receives independent specialist review.

A useful exact fixture has r(0)=1/16, lambda=578/735 and v(0)=735/578. At W(0)=Z(0)=0,

    Z'(0)=B_r²/(DG)-2E/D-D'/D+2r,

which is rational and independently checks(3). The constrained corrector through r=0, actual switch layers and the next integer-rounding term remain open. Do not import this interior minimizer into a boundary KKT problem. Beyond lambda=4/5 the global generator comparison is a separate prerequisite.

[K2604](k2604-second-order-stopping-resource-bound-2026-11-06.md), [K2602](k2602-continuum-stopping-resource-law-2026-11-06.md), [K2571](k2571-stopping-resource-price-2026-11-05.md), [probe](../../tests/channel-swings/k2606_interior_stopping_second_corrector_probe.py), [report](../../lab/process/k2606-interior-stopping-second-corrector.json).
