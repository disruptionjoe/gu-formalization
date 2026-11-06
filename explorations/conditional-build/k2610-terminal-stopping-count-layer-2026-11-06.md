---
title: "K2610 Terminal stopping layers and discrete third-order resource effects"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied fair stopping law, compact terminal scaling and small-multiplier rounding; no general third coefficient, exact finite-price ties or physical probability
scripts:
  - tests/channel-swings/k2610_terminal_stopping_count_layer_probe.py
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
result: K2610
carrier: original adaptive randomized fair stopping policies and their reduced finite deterministic schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original failure-inclusive leakage and positive-trial price ON=declared_carrier
real_structure: real positive price and score, constrained real actions and integer counts
grading: expected resource, integer stage count, terminal scaling and physical probability remain distinct
action_owner: repository-construction -- supplied fair stopping law
target: endpoint value/count/activation and discrete rounding corrections MAP-TYPE=evaluation
```

# Integer counts survive the terminal score limit

## Results and scope

Let price k=e², score S=e x, and multiplier lambda=2/3+e mu, with x in a fixed compact positive interval and mu bounded. The original all-policy priced value has the uniform expansion

    Q(e²;e x,2/3+e mu)=1-lambda e x/2
           +max_(n>=1){-e² A_n(x)+e³ B_n(x,mu)}+O(e4),
    A_n=2n+x²/(8n), h=x/n,
    L_(n,j)=3mu/2+h/12+h(n-j+1)/3,
    B_n=-3mu x²/(16n)-7x³/(144n²)
                       +(3h/16) sum_(j=1)^n (L_(n,j))_+².

Only a bounded set of counts participates on each such compact parameter set. Leading transitions are x_n=4sqrt(n(n+1)); section4 derives their first shifts and the actual constrained action profile. This resolves the endpoint excluded by K2608's positive-score margin. Randomized optimal policies may mix tied schedules; individual counts/actions below describe reduced deterministic optimizers.

Independently, K2577's exact small-multiplier tail yields a third resource coefficient that depends on the fractional part of M/2, and a third priced coefficient that oscillates with the nearest integer stage count. Thus there is generally NO single constant third coefficient even in that exactly solved regime. This is a mathematical limit of the supplied stopping law, not physical probability, native GU, novelty or empirical resource calibration. SC-META-53 remains UNCERTAIN; source, ledger0.263 LT-SM8/LT-GR6b and canon unchanged.

## 1. Localize all original policies before Taylor expansion

For a completed schedule, b_i>0, sum b_i=S, 0<=a_i<=b_i, define

    w(a,b)=log(1+(b-a)²/[2(a+b)(2-a-b)]),
    P_i=product_(j<=i)(1+a_j)^(-1),
    J_k=P_n-2sum_i P_i[lambda w(a_i,b_i)+k],
    R=2sum_i P_i.

K2571's resource-preserving reduction/attainment gives a finite deterministic optimum or abort for each k>0. The one-stage a=0 competitor has value 1-lambda S/2-O(e²), so abort is dominated uniformly. K2604's global generator comparison applies because lambda<4/5 for all sufficiently small e. Its unpriced value is

    V_lambda(e x)=1-lambda e x/2+O(e³).

Indeed v-3/2=O(e) on this interval, and the clipped generator q(v)=1/2+O(e²). Therefore every maximizing schedule obeys e²R<=V-Q=O(e²). Since sum a_i<=S, P_i>=exp(-S), so R>=2exp(-S)n and n is uniformly bounded. This bounds the reduced deterministic maximizing counts used to compute the all-policy value; no continuum mesh is assumed.

Every positive suffix value V_i lies between the overall value 1-O(e) and1: preceding positive-cost affine steps reduce a positive suffix. The exact stage derivative is

    partial_(a_i)V_i=[-2lambda w_a(a_i,b_i)-V_i]/(1+a_i).

Writing r=a/b, uniformly for r in[0,1], b=O(e),

    2w_a=g'(r)+O(b), g=(1-r)²/[2(1+r)],
    g'(0)=-3/2, g''=4/(1+r)^3>=1/2.

The derivative is negative whenever r>C e, for a fixed compact-set constant C. Hence every optimal stage has 0<=r_i<=C e; the upper action constraint is inactive. This uniform bound controls divisions by b in the expansion, including a candidate tiny stage.

## 2. The exact original-law cubic functional

Put b_i=e beta_i, a_i=e² alpha_i, sum beta_i=x, alpha_i<=C beta_i. The original logarithm gives

    2w=b/2-3a/2+2a²/b+3b²/16-ab/8+7b³/96+O(e³b).

With A_i=sum_(j<=i)a_j, P_i=1-A_i+O(e4). Using the actual prefixes and the bounded count, the objective becomes

    1-lambda e x/2-e²[2n+sum beta_i²/8]
                          +e³ G(beta,alpha)+O(e4),
    G=-3mu sum beta_i²/16-7sum beta_i³/144
      +sum_j alpha_j[3mu/2+beta_j/12+sum_(i>=j)beta_i/3]
      -(4/3)sum_j alpha_j²/beta_j.

The suffix sum arises from survival weighting. Omitting P_i changes stage ordering and the activation thresholds. At beta=0 interpret the constrained term continuously with alpha=0; alpha<=C beta makes the Taylor remainder uniform. Analytic expansion of the rational/log functions on the compact scaled cone supplies the bound; finite checks alone do not prove it.

For fixed beta, complete each constrained square:

    alpha_j*=(3beta_j/8)
       [3mu/2+beta_j/12+sum_(i>=j)beta_i/3]_+.

The optimized cubic coefficient is Lipschitz on the compact score simplex. Since

    sum beta_i²=x²/n+sum (beta_i-h)²,

comparison with the equal-score feasible schedule yields

    e²||beta-h||²/8 <= C e³||beta-h||+C e4.

Thus beta_i=h+O(e). Because n is bounded and x has a positive lower bound, every optimal beta_i is bounded away from zero for sufficiently small e. Substitution yields the stated B_n and value expansion, with O(e4) error. The explicit equal-score schedule with alpha_j=alpha_j*(h) supplies the matching lower bound. The cubic B_n stays bounded in n on the compact parameter set, while A_n>=2n, so writing max over all n introduces no spurious large-count optimum.

## 3. Actual action and activation consequences

The exact stage derivative, evaluated using the uniform expansion and beta_i=h+O(e), gives for every reduced deterministic optimizer of count n

    b_j=e h+O(e²), r_j/e=(3/8)(L_(n,j))_++O(e).

This conclusion comes from the actual constrained derivative and strict curvature, not from differentiating a value remainder. Below L_(n,j)=0 by a fixed margin the exact action is zero for sufficiently small e; above by a fixed margin it is positive. The first-stage threshold is

    mu_first=-2x/9-x/(18n).

L_(n,j) strictly decreases with j, so away from its thresholds the activated stages form an initial prefix. At the threshold the profile holds but a finer activation scale is unresolved. At x=1,mu=0 the unique leading count is1,

    A1=17/8, r1/e=5/32, B1=-37/2304.

The continuum coefficient at this endpoint would be x=1, an order-e² error of9/8. Thus K2608's S>=S0 condition cannot simply be removed even though its switch-uniform theorem is correct as stated.

## 4. Shifted integer-count transitions

Let Q_n denote the optimized fixed-count branch value. The same action and score localization applies near each relevant finite count; equal-score competitors keep the optimizer away from zero-score padding. Then A_n-A_(n+1)=-2+x²/[8n(n+1)], so adjacent counts tie at x_n=4sqrt(n(n+1)); convexity in positive real n leaves only adjacent minimizers. Away from these thresholds the unique minimizing n is the actual optimal count for small e. For x=x_n+e xi,

    Q_n-Q_(n+1)=e³[B_n(x_n,mu)-B_(n+1)(x_n,mu)
                              -xi/sqrt(n(n+1))]+O(e4).

A sign separated from zero selects the count. Equality of the cubic expression does not establish an exact finite-e tie; fourth-order information is then required. For n=1 versus2 and mu=-2 both action profiles are inactive, and the shift is

    xi*=6sqrt2-28/3.

This agrees with direct expansion of the EXACT zero-action logarithmic tie, providing a separate consumer and contrary control. Private randomization may mix genuinely tied counts; it does not create a fractional stage on a path.

## 5. Released third-order resource rounding in the exact tail

Now fix 0<S<=1/2 and 0<lambda<=2/5, independently of the terminal scaling. K2577 proves the exact all-policy frontier for M>=2:

    F(M)=1-2lambda[(1-a)H(n)+aH(n+1)],
    n=floor(M/2), a=M/2-n, H(t)=t log[(4-S/t)/(4-2S/t)].

The convergent logarithm series gives

    H(t)=S/4+A/t+B/t²+D/t³+O(t^-4),
    A=3S²/32, B=7S³/192, D=15S4/1024.

Expanding around t=M/2 cancels the linear interpolation error and gives, uniformly in a in[0,1],

    V-F(M)=C/M+B2/M²+T(a)/M³+O(M^-4),
    C=3lambda S²/8, B2=7lambda S³/24,
    T(a)=15lambda S4/64+(3lambda S²/2)a(1-a).

Uniformity follows from the absolutely convergent series for S/n<=1/2 and bounded interpolation offsets; one can bound the remaining geometric tail without numerically sampling M. At even budgets T=15lambda S4/64; at odd budgets it is larger by3lambda S²/8. Consequently M³[V-F-C/M-B2/M²] has distinct even/odd subsequential limits for positive lambda,S. A constant third coefficient is false. Expected-resource mixtures are essential: the oscillation is compatible with the continuous piecewise-linear frontier.

## 6. Released third priced coefficient and exact count centering

In the same exact-tail regime let

    a0=3lambda S²/16, b0=7lambda S³/96, d0=15lambda S4/512,
    t0=sqrt(a0/2)=sqrt(C)/2, c0=b0/a0=7S/18,
    nu(e)=t0/e+c0, delta(e)=dist(nu(e),integers),
    D0=d0/t0³-b0²/(2t0^5), Z=-7S/9.

The exact maximizing count minimizes 2e²n+2lambda H(n). Its smooth real minimizer is nu(e)+O(e), obtained by expanding its strictly monotone derivative. Strict convexity confines the integer optimizer to the two neighboring integers of the real minimizer. For n=nu(e)+z with bounded z, direct expansion gives

    V-J_n=2sqrt(C)e-Z e²+e³[D0+(2/t0)z²]+O(e4).

Taking the better integer, including near half-integer ties, proves uniformly in the rounding phase

    Q(e²)=V-2sqrt(C)e+Z e²
                -e³[D0+(2/t0)delta(e)²]+O(e4).

The O(e) error in the real minimizer shifts its squared nearest-integer distance by O(e), absorbed in O(e4). This does not assert exact nearest-nu selection at a near tie. The O(e³) coefficient oscillates between D0 and D0+1/(2t0). It cannot be replaced by one constant. This explains a concrete obstruction to extending the smooth second-corrector result by a naive third coefficient; it does not compute the third coefficient in the positive-action or switching regimes.

## Evidence, controls and remaining work

Exact probes expand original n=1 and n=2 logs/prefixes, recover constrained squares, verify the shifted inactive count tie and resource/price rounding identities. Rational feasible schedules are evaluated with Arb; their asymptotic residuals are illustrations, not global optimality certificates. The universal count localization, remainder and optimization proofs above carry the all-policy theorem. No external-expert or proof-assistant certification is claimed.

Next resolve the fourth-order endpoint tie/activation corners or positive-action third-order count phase, or the independent generator comparison above4/5. The terminal leading/cubic value, leading action profile and small-multiplier rounding obstruction are now available and should not be requeued as missing. Physically calibrated probability/resource and native source interfaces remain separate.

[K2608](k2608-switching-stopping-second-corrector-2026-11-06.md), [K2604](k2604-second-order-stopping-resource-bound-2026-11-06.md), [K2577](k2577-exact-resource-tail-2026-11-05.md), [K2571](k2571-stopping-resource-price-2026-11-05.md), [probe](../../tests/channel-swings/k2610_terminal_stopping_count_layer_probe.py), [report](../../lab/process/k2610-terminal-stopping-count-layer.json).
