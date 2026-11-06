---
title: "K2608 Uniform second stopping coefficient through the constrained action switch"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied fair stopping law on compact positive S and multiplier rectangles through the switch; no third coefficient or physical probability
scripts:
  - tests/channel-swings/k2608_switching_stopping_second_corrector_probe.py
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
result: K2608
carrier: original adaptive randomized fair test/use stopping policies, finite positive trials and score0<S<=1/2 LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original leakage and positive-trial price ON=declared_carrier
real_structure: real constrained action ratios0<=r<=1 and multiplier0<lambda<=4/5
grading: continuum value, constrained corrector, activation layer, stage count and physical probability remain distinct
action_owner: repository-construction -- supplied fair stopping law
target: all-policy second resource coefficient across action switching MAP-TYPE=evaluation
```

# A continuous corrector with a derivative jump

## Result

Uniformly on compact rectangles 0<S0<=S<=1/2 and 0<lambda0<=lambda<=4/5, including the action-switch curves, the original-policy priced and resource values satisfy

    Q(k)=V-2sqrt(Ck)+Z(S)k+O(k^(3/2)),
    V-F(M)=C/M-C Z(S)/M²+O(M^-3),
    R_min(eta)=C/eta-Z(S)+O(eta).

Every price optimizer has R=sqrt(C/k)-Z(S)+O(1), including ties. The corrector defined below obeys

    -7S/9 <= Z(S) <= -583S/76800 < -S/200.

Hence the second gap coefficient and additive inverse-resource overhead are positive on the whole certified multiplier range. The theorem extends K2606 beyond its strictly interior action domain. It reuses K2602's C and K2604's global generator comparison. K2577's small-multiplier exact frontier is retained, not rediscovered.

For a fixed switch strictly inside (0,S), section5 also identifies the leading small-price activation layer of every optimal positive first stage. No endpoint-uniform activation profile, exact optimal count, third coefficient, beyond4/5 generator comparison or physical probability is claimed. This is independent mathematics of a supplied law, not native GU. SC-META-53 remains UNCERTAIN; source, ledger0.263 LT-SM8/LT-GR6b and canon remain unchanged.

## 1. Piecewise coefficients of the actual law

Reuse the original logarithm and ratio a=rb:

    w=log(1-alpha(r)b)-log(1-beta(r)b),
    alpha=(1+6r+r²)/(4(1+r)), beta=(1+r)/2,
    g=(1-r)²/[2(1+r)], B=beta²-alpha², G=g''=4/(1+r)^3.

The value is V=lambda v, with v(0)=1/lambda, v'=-q(v),

    q(v)=1/2, r(v)=0                         if v>=3/2,
    q(v)=2sqrt(1+2v)-2-v,
    r(v)=2/sqrt(1+2v)-1                     if v<3/2.

On the declared compact parameter region q stays bounded below by9/20 and above1/2. There is at most one switch s*=2/lambda-3 if this lies in[0,S]. Define D=B-qr/2, c=sqrt(2/(lambda D)),

    W'+rW=2sqrt(2lambda D), W(0)=0, W(S)=2sqrt C.

D and c are positive continuous Lipschitz, W is C1 with Lipschitz derivative, uniformly on the compact rectangle. They are smooth with bounded one-sided derivatives on each side of the switch.

Set Z(0)=0 and require Z continuous. On the constrained zero branch put

    Z'=-7/9.

On the interior branch use exactly K2606's ODE

    Z'+rZ=(c lambda B_r-W)²/(2lambda G)
                        -c²lambda E-c W''/2,
    E=2(beta³-alpha³)/3+(-qr²+q²/G)/6.

On the zero branch V is affine, D=3/16, W'=sqrt(3lambda/2), W''=0 and E=7/96. Its cubic cancellation is Z'=-c²lambda E=-7/9. Thus Z=-7s/9 until the switch; if lambda<=2/(3+S), Z(S)=-7S/9 exactly. The interior ODE starts with this value, not with zero at the switch.

Z is generally NOT C1. At an interior switch, W*=sqrt(3lambda/2)s*, B_r=-1/8, G=4, D'_+=-3/64, E_+=1/12. Exact substitution gives

    Z'_+=-89/144+3s*/8+3s*²/16,
    Z'_-=-7/9,
    Z'_+-Z'_- =23/144+3s*/8+3s*²/16>0.

Demanding derivative matching or using the interior coefficient in the whole zero branch is false. This derivative jump is why the prior smooth proof does not suffice.

## 2. Uniform all-policy verification with a localized barrier

Write e=sqrt k and U=V-eW+e²Z. For positive stages the ORIGINAL residual is

    Delta_U=(1+rb)U(s)+2lambda w(rb,b)+2e²-U(s-b).

The two prices are the actual fair-trial count; zero-score padding is removed. K2604 supplies d_V>=gamma lambda b²/2 for all admissible actions. Uniform Lipschitz bounds on W,Z imply

    Delta_U>=gamma lambda b²/2-C1 e b-C2 e²b+2e².

Thus b>=K e has nonnegative residual for fixed sufficiently large K, and b<=c_low e has positive residual for fixed sufficiently small c_low. Only c_low e<=b<=K e needs the delicate expansion. Constants here are uniform on the stated compact parameter rectangle, not as lambda0 tends to zero.

Choose a core band |v-3/2|<=A e, with fixed A large enough to contain all possible O(e) KKT shifts. If [s-b,s] avoids it on the zero side, the exact ratio derivative at zero is positive: lambda(v-3/2) dominates the bounded e,b perturbations. Strong convexity keeps the residual minimum at r=0. The zero-branch expansion is

    lambda D(b-e c)² + b[e²Z'+lambda E b²]+O(b(b+e)^3),

and its cubic bracket vanishes at b=e c. If the segment avoids the core band on the interior side, the minimizer stays interior; K2606's uniform square completion and implicit-function estimate apply. The same cubic cancellation and Young bound give Delta_U>=-C e³ b on both sides. Although the interior action tends to zero, its distance A e from the constraint exceeds its O(e) shift; all derivative bounds of the unconstrained formulas remain finite at r=0.

When the segment intersects the core band, use V with Lipschitz V'', W with Lipschitz W', and Lipschitz Z. Expand only far enough to get the leading square and a remainder bounded C e²b in the comparable-step range. Strong convexity first confines the minimizing ratio to r(s)+O(e); a ratio farther away has positive quadratic excess. No derivative of Z through the switch is taken. Hence Delta_U>=-C e²b in this band.

Because |v'|<=1/2, a segment of length b<=K e intersecting the core band lies wholly in the enlarged band |v-3/2|<=(A+K/2)e. Define its occupation primitive

    B_e(s)=integral_0^s 1_{enlarged band}(t) dt.

Since -v'>=9/20, B_e is nondecreasing and sup B_e<=C e. Add

    U_bar=U+C3 e² B_e+C4 e³s.

For a crossing segment, B_e(s)-B_e(s-b)=b; the action term rb B_e(s) is nonnegative. This pays C3 e²b. Other segments receive nonnegative correction, and C4 e³s pays the outside-band remainder. Thus Delta_Ubar>=0 for EVERY action, while ||U_bar-U||infinity=O(e³). The original-policy verification/telescope of K2604, including abort, overshoot and nonabsorption, yields Q(e²)<=U(S)+O(e³). A start-state-only indicator would miss crossing steps and is not used.

## 3. A matching finite original-law policy

Use the global clock T(s)=integral_0^s1/c(z)dz, n=nearest(T(S)/e), tau=T(S)/n and T(s_i)=(n-i+1)tau. Positivity and Lipschitz c give b_i=s_i-s_(i+1)=e c(s_i)+O(e²) uniformly, INCLUDING the final cell. For each state/step select the actual residual-minimizing legal ratio (or an approximation to O(e²) in ratio); away from the band this is the zero ratio or the K2606 interior correction, and in the band it is its constrained KKT version.

A concrete first-order ratio usable throughout is

    r_i=max(0, r(s_i)+e[W-c lambda B_r]/(lambda G)
                         -(v(s_i)-3/2)_+/G),

clipped above at1 if needed. On the core band it is O(e) from the true minimizer and yields O(e³) stage residual; away from the band it equals the correct zero branch or the interior first-order solution to O(e²). On each smooth side the residual is O(e4). The band has length O(e), and b_i>=c0e, so only O(1) stages meet it; all other O(e^-1) stages contribute O(e4). The actual weighted telescope, P_i=product_(j<=i)(1+a_j)^-1, is

    J-e²R=U(S)-sum_i P_i Delta_i=U(S)+O(e³),
    R=2sum_i P_i, J=P_n-2lambda sum_i P_i w(a_i,b_i).

This proves the matching lower bound. S>=S0>0 ensures a nonempty finite clock mesh uniformly as e tends to zero. Rounding the stage count and either endpoint switch affects the O(e³) remainder, not Z. The probe constructs rational policies in tail, endpoint-switch, interior-switch, critical-initial and strictly interior regimes, and evaluates their exact original logarithmic costs with Arb. The computed ODE/clock approximations are illustrations, not a uniform proof.

## 4. Dual, inverse and sign consequences

K2571's exact strong duality gives F(M)=min_e[Q(e²)+Me²]. K2606's no-differentiation argument localizes every minimizing e to O(M^-1); completing the quadratic gives V-F(M)=C/(M+Z)+O(M^-3), then bracketing gives R_min(eta)=C/eta-Z+O(eta). Price secants at k(1 plus or minus sqrt k) give R=sqrt(C/k)-Z+O(1) for every optimizer. None of these arguments differentiates the value remainder or selects a unique count.

The sign proof can also cross the switch, with a corrected lower bound. On the interior branch write z=W/sqrt(2lambda D). K2606 proves exactly on0<=r<=1/6

    Z'+rZ=(D/G)z²+A(r)z+K(r),
    0<=A<=3/8, D/G<=1/16, K>=-89/144,
    K(r(s))<=-47/100+11s/20,
    0<=z<=11s/4, 0<=r<=1/6.

These coefficient inequalities include r=0, and r'<=1/5 remains true with the clipped zero branch. On the zero branch the forcing is -7/9, which is smaller than the same upper forcing bound and at least -7/9. Integrating with11/12<=exp(-integral_s^S r)<=1 gives the same upper calculation as K2606,

    Z<=-517S/1200+737S²/960+121S³/768
      <=-583S/76800.

The global lower forcing bound is -7/9, so Z>=-7S/9. The earlier interior lower bound -89S/144 is FALSE on the pure zero branch and is not transferred. On that branch C=3lambda S²/8, so -CZ=7lambda S³/24, agreeing with the direct original-log expansion in K2577. The positive inverse overhead is therefore quantified without an ODE solve.

## 5. The actual local activation layer

Fix lambda with s*=2/lambda-3 strictly inside (0,S), and examine state s=s*+e x with x in a fixed bounded interval. Let (a,b) be any optimal positive first stage at price e², and r=a/b. First Q<=V, Q(s)>=V(s)-Ce and the global d_V bound give b=O(sqrt e) from the original Bellman equality. Therefore s-b stays in a compact positive score interval for small e; the value expansion is applicable at BOTH states. The uniform value theorem and the leading residual square now imply b=e c0+O(e^(3/2)), where c0=sqrt(32/(3lambda)). Indeed the optimal Bellman equality gives Delta_U=O(e³); strong convexity and the square lower estimate force the bound. Large and tiny b have already been excluded by the global residual bounds. The first stage cannot be an abort for small e at this positive state.

The actual first-action derivative is

    Q(e²;s)+2lambda w_r(r,b)/b,

not a derivative of the asymptotic remainder. Using V(s)=3lambda/2-lambda e x/2+O(e²), W(s)=W*+O(e), B_r(0)=-1/8 and G(0)=4, its constrained zero is

    r/e = (x/2+(3s*+1)/sqrt(6lambda))_+/4 + O(sqrt e).

Thus the switch shifts into the continuum zero-action side by

    x*=-2(3s*+1)/sqrt(6lambda).

For x below x* by a fixed positive margin, the actual optimal first action is zero for sufficiently small e; above it by a fixed margin it is positive. The uniform profile error covers the corner itself but does not resolve a finer transition scale. This is a price-dependent optimal first-stage result at a fixed interior switch; it is neither an endpoint-uniform profile nor the already-known fixed-count activation threshold. It releases a concrete policy-selection consequence without claiming an exact stage count or third coefficient.

## Evidence and next condition

Exact controls distinguish zero/interior cubic coefficients and their genuine derivative jump; original-law price, telescope and dual identities are replayed. Ten rational policies exercise both switch endpoints and an interior crossing, with Arb cost intervals. Numerical residual ratios support the construction but cannot prove universal optimality. Independent review checks the enlarged-band barrier, constrained action derivative and count/endpoint claims.

Next resolve the next-order count rounding or endpoint activation layer, or the separate generator comparison above4/5. The second coefficient and leading fixed-interior-switch activation profile are no longer missing. Native physical probability, preparation/reset and complete apparatus resource accounting remain unbuilt.

[K2606](k2606-interior-stopping-second-corrector-2026-11-06.md), [K2604](k2604-second-order-stopping-resource-bound-2026-11-06.md), [K2577](k2577-exact-resource-tail-2026-11-05.md), [probe](../../tests/channel-swings/k2608_switching_stopping_second_corrector_probe.py), [report](../../lab/process/k2608-switching-stopping-second-corrector.json).
