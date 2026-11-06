---
title: "K2614 Quartic terminal stopping value and count selection"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: compact positive terminal scaling of supplied stopping law; no exact tie from finite asymptotic truncation or physical probability
scripts:
  - tests/channel-swings/k2614_quartic_terminal_stopping_probe.py
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
result: K2614
carrier: original fair stopping policies reduced to finite deterministic schedules LAYER=toy CHIRALITY=N/A
pairing: success minus original prefix-weighted leakage and reached-trial price ON=declared_carrier
real_structure: real small positive e with exact rational symbolic coefficients and outward interval controls
grading: integer count, score allocation, action activation and expected resource are distinct
action_owner: repository-construction -- supplied fair stopping law
target: quartic terminal value and discrete count/activation decisions MAP-TYPE=evaluation
```

# Resolve the next terminal count and action decisions

## Result

Reuse K2610's original law, price k=e², score S=e x, and multiplier lambda=2/3+e mu, with x in a compact subset of (0,infinity) and mu in a fixed bounded interval. For sufficiently small e>0 the all-policy optimum is

    Q=1-lambda e x/2
       +max_(n in N){-e² A_n(x)+e³ B_n(x,mu)+e4 D_n(x,mu)}+O(e5).

Here N is a sufficiently large FIXED finite count set obtained by K2610's uniform count localization, not all positive integers. A_n and B_n are K2610's coefficients. We give D_n explicitly below, including action activation boundaries. This resolves the next nonzero count-selection signal when the cubic tie vanishes. We also compute the exact one-stage activation curve and its finer corner action, and actual active/inactive adjacent-count transition consumers.

The scope is independent mathematics of the supplied law. No native GU, physical probability, global fluid/atomic phase diagram, exact finite-e tie from truncation, infinite-count uniformity or external certification is claimed. Source polarities, ledger0.263 LT-SM8/LT-GR6b and canon remain unchanged.

## 1. Expand the original logarithm and survival prefixes

For n stages write b_i=e beta_i, a_i=e² alpha_i, sum beta=x, and

    P_i=product_(j<=i)(1+a_j)^(-1),
    J=P_n-2 sum_i P_i[lambda w(a_i,b_i)+e²],
    w(a,b)=log(1+(b-a)²/[2(a+b)(2-a-b)]).

K2610 proves that maximizing counts are uniformly bounded, alpha_i<=C beta_i, beta_i=h+O(e) with h=x/n>0, and abort is dominated. Thus expansion can now take place on a compact set bounded away from beta_i=0. It is not a continuum-mesh assumption.

Set T_i=sum_(j<=i)alpha_j. The exact coefficient expansion of 2w is

    c1=beta/2,
    c2=-3alpha/2+3beta²/16,
    c3=2alpha²/beta-alpha beta/8+7beta³/96,
    c4=-2alpha³/beta²-13alpha²/16+3alpha beta²/32+15beta4/512.

The original objective becomes

    J=1-lambda e x/2-e²[2n+sum beta_i²/8]
                              +e³ G(beta,alpha)+e4 H(beta,alpha)+O(e5),
    G=-3mu sum beta_i²/16-7sum beta_i³/144
      +sum_j alpha_j[3mu/2+beta_j/12+sum_(i>=j)beta_i/3]
      -(4/3)sum_j alpha_j²/beta_j,
    H=sum_i[-(2/3)c4_i-mu c3_i
                       +T_i(beta_i²/8+mu beta_i/2+2)].

In H, the order-e4 contribution from P_n cancels the sum T_i alpha_i arising from weighted c2. Dropping the survival prefixes changes H and gives an incorrect stage-allocation correction. Taylor remainder and its first two derivatives are uniformly bounded on this compact domain because the factored log argument is analytic near e=0. Exact finite probes check coefficient identities; this analytic fact controls the universal remainder.

## 2. Optimize the actions and scores in the right order

Define

    L_j(beta)=3mu/2+beta_j/12+sum_(i>=j)beta_i/3,
    alpha_j^0(beta)=(3beta_j/8)(L_j(beta))_+,
    Gbar(beta)=-3mu sum beta_i²/16-7sum beta_i³/144
                         +(3/16)sum_j beta_j(L_j(beta))_+².

The negative quadratic action curvature is uniformly bounded away from zero. The exact constrained action maximizer therefore differs from alpha^0 by O(e), uniformly including L_j=0: the gradient perturbation is O(e) and the lower orthant projection is nonexpansive in the equivalent curvature norm. Its maximized contribution is

    Gbar(beta)+e H(beta,alpha^0(beta))+O(e²).

No differentiability of positive-part itself is assumed: Gbar is C1 with Lipschitz gradient; H composed with alpha^0 is Lipschitz. These properties suffice for the value theorem across activation corners.

At beta=h1 let g=gradient_beta Gbar and let Pg=g-mean(g)1 be its projection onto sum-zero score perturbations. Write beta=h1+e d. Uniform Taylor estimates give the order-e4 score functional

    -||d||²/8+g.d+H(h1,alpha^0(h1)).

Completing the square yields

    d*=4Pg,
    D_n=H(h1,alpha^0(h1))+2||Pg||².

For clarity the explicit gradient is

    g_k=-3mu h/8-7h²/48+(3/16)(L_k)_+²
          +(3h/8)sum_j (L_j)_+ (1_(k=j)/12+1_(k>=j)/3),
    L_j=3mu/2+h/12+h(n-j+1)/3.

All constants are uniform on the fixed compact x,mu set and fixed bounded counts. For the value proof, score strong concavity and the Lipschitz perturbation first give beta=h+O(e); expanding Gbar with its Lipschitz gradient and H with its Lipschitz bound then leaves O(e5). Maximizing the quadratic supplies matching upper/lower values. Actual score correction beta=h+4e Pg+O(e²) also follows from the differentiated constrained equations and uniformly O(e) perturbed action maximizer, rather than from differentiating a value remainder. The score constraints are interior for small e; upper action a<=b stays inactive.

Counts beyond N are excluded by the original all-policy resource bound, not by extrapolating the polynomial D_n to large n. Taking the maximum over the finite set preserves the uniform O(e5). Randomized optimizers can mix genuinely tied branches; count/profile statements refer to reduced deterministic optimizers.

## 3. Released quartic count transitions

At x0=4sqrt(n(n+1)), let Delta B=B_n-B_(n+1) and Delta D=D_n-D_(n+1), evaluated at (x0,mu). Other counts remain separated at leading order. Put

    x=x0+e xi+e² zeta,
    xi*=sqrt(n(n+1)) Delta B.

When xi=xi*, the next difference is

    Q_n-Q_(n+1)=e4 [Delta D+xi* partial_x Delta B
          -(xi*)²/(8n(n+1))-zeta/sqrt(n(n+1))]+O(e5).

A sign separated from zero determines the globally maximizing count for small e. Define zeta* by setting the bracket to zero. This is a second asymptotic shift; equality of this bracket still does not assert an exact finite-e tie. Even if an L_j vanishes, B_n is C1 with Lipschitz derivative and D_n is Lipschitz, so this expansion remains valid at fixed mu.

For n=1 versus2 and mu=0 both branches have active actions:

    xi*=-65/12, zeta*=20837sqrt(2)/2304.

For mu=-2 both branches are inactive at x0:

    xi*=6sqrt(2)-28/3, zeta*=-28+209sqrt(2)/9.

The inactive result can be checked independently against the exact branch values

    Q_n=1-2lambda n log[(4-S/n)/(4-2S/n)]-2e²n.

This inactive consumer has a genuine exact local tie curve, not only a formal shift. Write w0(t)=log[(4-t)/(4-2t)]. The exact equality is

    lambda [w0(S)-2w0(S/2)]=e²,
    (4-S)^3=exp(e²/lambda)(4-2S)(4-S/2)^2.

The left logarithmic difference is strictly increasing for S>0 because w0 is strictly convex. With lambda=2/3-2e, divide its equation by e² and set S=e x. The resulting analytic equation has at e=0 the simple positive root x=4sqrt(2). The implicit-function theorem gives a unique nearby exact tie with x=x0+e xi*+e² zeta*+O(e³) as above. Both branches have strictly inactive action margins near this point; score convexity gives their equal-score schedules, and global count localization excludes other counts. Thus it is an actual local global count transition for sufficiently small e. The probe brackets its two exact branch values at a specified rational e; the analytic argument supplies the asymptotic neighborhood, not a claimed explicit numerical global-validity radius.

For active count2, the score correction is (x²/64,-x²/64); equal scores miss part of the quartic gain. At count1, x=1,mu=0,

    B1=-37/2304, D1=1315/4096.

The probe derives these numbers from the formula, and separately expands original one/two-stage objectives. Certified evaluations of explicit rational feasible policies illustrate the predicted error order; they are not independent global optimizer certificates.

## 4. Released exact activation and a finer corner

For one stage with b=S, the derivative numerator of

    J(a)=[1-2lambda w(a,b)-2e²]/(1+a)

at a=0 equals lambda M(0,b)-(1-2e²), where M(0,b)=2(w-w_a)|_(a=0). Its derivative with respect to a is -2lambda(1+a)w_aa<0. Therefore, for the present small-score/positive-price regime, the one-stage optimum is a=0 precisely when lambda<=lambda_c, with

    lambda_c(e,x)=(1-2e²)/M(0,e x)
      =2/3-5ex/18+e²(2x²/27-4/3)
                       +e³(-5x³/648+5x/9)+O(e4).

When lambda>lambda_c the unique interior root gives a positive action; the derivative at a=b is negative here because the unpenalized numerator 1-2e² remains positive. For x in a compact subset of (0,4sqrt(2)), count1 remains the globally preferred count near this activation corner, by its separated leading A_n.

On the finer scale mu=-5x/18+e nu, the actual action satisfies

    a/e³=(3x/8)[3nu/2+2-x²/9]_+ + O(e).

This follows by expanding the exact derivative and its strictly negative curvature; it is not obtained by differentiating the quartic value theorem. At x=1,nu=0, a/e³ ->17/24. Thus the cubic leading action zero did not imply exact inactivity. The exact lambda_c formula, not its truncated series, decides a finite-e threshold; at the finer equality still higher order may decide positive action.

## Evidence and remaining work

The probe verifies the original-log coefficients, actual prefix series, constrained completion and gradient, active/inactive count-shift consumers, exact one-stage threshold derivative and a certified small-e action bracket. It plants wrong equal-score, wrong prefix, and false zero-leading-action controls. The all-policy reduction and count localization are reused from K2610; the uniform constrained-optimization proof above supports the new theorem. Checks of saved report hashes establish provenance, not the theorem.

The complete intermediate fluid/atomic phase boundary, positive-action large-count rounding, uniform count-to-infinity terminal transitions and physical calibration remain separate. A fifth-order tie or finer equality is a new decision only when parameters genuinely land there; routine coefficient generation is not a claim of resolving the global phase diagram.

[K2610](k2610-terminal-stopping-count-layer-2026-11-06.md), [K2612](k2612-extended-diffuse-stopping-phase-2026-11-06.md), [probe](../../tests/channel-swings/k2614_quartic_terminal_stopping_probe.py), [report](../../lab/process/k2614-quartic-terminal-stopping.json).
