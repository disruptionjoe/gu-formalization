---
title: "K2547 Fifth-order terminal-satellite instability and finite clouds"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied-law finite-policy counterexamples and asymptotic lower bound; no global optimum, physical probability law or GU claim
scripts:
  - tests/channel-swings/k2547_nearcritical_satellite_instability_probe.py
---

# K2547 The sharp cubic boundary is already unstable at fifth order

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
result: K2547
carrier: finite ordered stopping schedules for the inherited scalar score law LAYER=toy CHIRALITY=N/A
pairing: ordinary real expected supplied reward and cost ON=declared_carrier
real_structure: real nonnegative scores and interior real action ratios
grading: supplied stochastic law; no Clifford or physical grading
action_owner: repository-construction -- original weighted stopping law of K2483 and K2485
target: collapsing terminal satellites and local insertion phase MAP-TYPE=evaluation
```

## Result and scope

At [K2545](k2545-critical-stopping-aggregation-2026-11-04.md)'s sharp moving-multiplier cubic boundary, an actual two-stage policy beats the optimized one-stage policy by a positive term of order S^5. Its satellite score is of order S². Splitting the tail among several stages improves that coefficient further. We derive a locally analytic insertion curve and an all-policy liminf lower bound using fixed finite satellite clouds, with the limits in their proved order.

This resolves the prior shrinking-satellite question in the direction of a counterpolicy. It does not give a matching upper bound, exact finite-score global phase curve, infinite-stage attainment or the budget-S=1/2 frontier. K2545's uniform cubic theorem is unchanged: fifth-order advantage is consistent with its O(S^4) uncertainty. SC-META-53 remains UNCERTAIN; source polarities and ledger0.263 are unchanged. This is independent probability mathematics under a supplied law, with no GU, physical realization, empirical or novelty claim.

## 1. The original law and its analytic optimizer

Keep the inherited finite-completed-schedule reduction, its original adaptive/mixture/admitted-limit scope and prefix weights:

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    P_i=product_(j<=i)(1+a_j)^(-1),
    G=P_n-2lambda sum_i P_i w(a_i,b_i),
    b_i>=0, sum b_i=S, 0<=a_i<=b_i.

Let U_lambda(b)=max_a [1-2lambda w(a,b)]/(1+a), and let V_lambda(S) be the full inherited policy supremum. The exact original stationary equation for a stage with normalized suffix value Y is

    lambda M(rb,b)=Y,
    M=2w-2(1+a)w_a,
    M(r,0)=2/(1+r)^2-1/2,
    partial_r M(r,0)=-4/(1+r)^3.                           (1)

Use the analytic extension at b=0, with w(rb,b)=log(1-cb)-log(1-beta b), alpha=(1-r)^2/[4(1+r)], beta=(1+r)/2, c=beta-alpha. At zero score and Y=1, the ratio is

    r_lambda=2/sqrt(1+2/lambda)-1,
    A(lambda)=r_lambda+2lambda alpha(r_lambda).

Near lambda*=4sqrt(3)/3 this ratio is interior. The nonzero derivative in (1) gives a unique analytic ratio in b,Y,lambda. On r in[0,1], M_r remains strictly negative for sufficiently small b, and endpoint stationary signs persist for suffix values near one. Hence this ratio is the unique global stage optimizer for small scores, not merely a formal critical point. Backward induction yields an analytic optimized value for each fixed finite number of stages, extending through zero-score stages. No uniform-in-stage-count analytic neighborhood is asserted.

## 2. Differentiate a genuinely optimized terminal insertion

For main score S-t and terminal score t, the exact optimized two-stage value is

    W_lambda(S,t)=max_a [U_lambda(t)-2lambda w(a,S-t)]/(1+a).

At t=0 the value is U_lambda(S). Let a_lambda(S)=S rho_lambda(S). Differentiating at the main optimum gives

    L(S,lambda)=partial_t W_lambda(S,0)
      =[2lambda w_b(a_lambda(S),S)-A(lambda)]/(1+a_lambda(S)). (2)

The derivative w_b holds a fixed. The main action is reoptimized in W; freezing its ratio for nonzero t would omit a contribution at the order of interest. Equation(2) follows from the exact suffix law and the envelope theorem, not a guessed additive stage cost.

We calculate L=L1 S+L2 S²+L3 S³+O(S^4), with lambda fixed in each coefficient. All coefficients are analytic near lambda*. K2517's H gives L1=-2H(lambda). At criticality put

    r*=2sqrt(3)-3,
    Hp=(141-81sqrt(3))/8>0,
    Hpp=(6021-3477sqrt(3))/64,
    c1=(2841-1643sqrt(3))/48<0,
    cL=(249sqrt(3)-431)/2>0,
    mu0=37/66-257sqrt(3)/396.

The exact coefficient evaluation is

    L2(lambda*)=c1,
    dL2/dlambda=(-105583+60963sqrt(3))/128,
    L3(lambda*)=211309/96-40665sqrt(3)/32,
    gamma=L3+mu0*dL2/dlambda-Hpp*mu0²
          =(202353685-116818417sqrt(3))/371712>0.            (3)

The sign is certified by 202353685²-3*116818417²=7386181921558>0; both integers are positive. gamma is approximately0.0491011757. We use gamma to distinguish this coefficient from the unrelated geometric kappa.

For lambda(S)=lambda*+mu0 S+nu S², the S² term cancels because c1=2Hp mu0, and

    L(S,lambda(S))=(gamma-2Hp nu)S³+O(S^4).                 (4)

## 3. A controlled shrinking-satellite theorem

The analytic function W-U vanishes at t=0, so it has an exact factor t:

    W-U=t L(S,lambda)+t² Q(S,lambda)+O(t³).

For the same moving multiplier, K2545's explicitly optimized cubic polynomial yields

    Q(S,lambda(S))=-cL S+O(S²).                            (5)

To justify using its polynomial here, take the Taylor series in the independent small stage scores, which exists by section1, and compare its homogeneous degree-three coefficients with K2545. The remainder used here is the analytic Taylor remainder for the finite two-stage optimized value, not K2545's generic all-partition O(S^4) bound. The latter alone could not decide this result.

For t=zS², fixed z in a bounded nonnegative interval and nu in a compact interval,

    W_lambda(S,zS²)-U_lambda(S)
      =S^5[(gamma-2Hp nu)z-cL z²]+O(S^6).                  (6)

Uniformity in these bounded parameters follows from analyticity on a fixed small polydisc. The discarded contributions t O(S^4), t² O(S²) and O(t³) are each O(S^6). All scores and optimized actions are admissible for sufficiently small S>0.

At nu=0 choose z=gamma/(2cL), approximately0.1749545197. Then the actual original policy has advantage

    gamma² S^5/(4cL)+O(S^6),
    gamma²/(4cL) approximately0.0042952363>0.               (7)

Thus one-stage optimality fails for every sufficiently small positive score at the cubic boundary. This is not merely a numerical witness or an assertion that a formal Taylor series is positive at arbitrary finite S. Existence of a sufficiently small interval follows from the controlled positive leading coefficient; an explicit rational interval endpoint is not supplied.

## 4. Released successor: the local terminal-insertion curve

Since L(0,lambda)=0, L/S extends analytically. Its lambda derivative at S=0,lambda* is -2Hp!=0. The implicit-function theorem gives a unique local curve L(S,lambda_c(S))=0:

    lambda_c(S)=lambda*+mu0 S+nu0 S²+O(S³),
    nu0=gamma/(2Hp)
       =(24165709-13458052sqrt(3))/3066624
       approximately0.2790296969.                        (8)

For small positive S the insertion derivative decreases with lambda. Below this curve a sufficiently small positive terminal insertion improves the one-stage value; above it an infinitesimal insertion is unfavorable. This is a local insertion curve, not the global all-policy transition: finite splits and more complicated tails remain independent competitors. At equality still higher terms decide finite insertions.

## 5. Released successor: finite satellite clouds improve the coefficient

Take fixed m>=1, main score S-S²Z, followed by m scores t_j=z_jS², Z=sum z_j, with bounded nonnegative z_j. Optimize every stage ratio by the original backward recursion. Every first derivative in a tail score at the zero-tail point equals L, since a zero-score stage does nothing. The degree-three optimized polynomial from K2545 gives the quadratic tail terms. Its sharp-boundary defect is -cL R+(2c0-3c1)T, where c0=c1-cL, R=sum_(i<j)x_i x_j² and T=sum_(i<j<k)x_i x_j x_k. Substitute x0=1-SZ and xj=Szj:

    R=S² sum z_j²+O_m(S³),
    T=S² sum_(i<j)z_i z_j+O_m(S³).

Finite-dimensional analytic Taylor expansion, as in section3, yields

    W_m-U=S^5[k_nu Z-cL sum z_j²
                    -(c1+2cL)sum_(i<j)z_i z_j]+O_m(S^6),
    k_nu=gamma-2Hp nu.                                    (9)

The subscript m is essential. No uniform remainder as m grows with S follows from this argument. Rewriting the penalty gives

    Kinf Z²-(c1/2)sum z_j²,
    Kinf=cL+c1/2=(10309sqrt(3)-17847)/96>0.

The sign witness is 3*10309²-17847²=311034>0. Because c1<0, equal tail scores minimize this quadratic penalty at fixed Z. Put

    Km=Kinf-c1/(2m)>0.

For k_nu>0 choose Z=k_nu/(2Km) and z_j=Z/m; otherwise the zero tail gives the lower witness zero. Therefore an actual fixed finite policy gives leading gain (k_nu)_+²/(4Km). In particular K1=cL, K2<K1, and at nu=0

    gamma²/(4K2)-gamma²/(4K1)
         =-c1 gamma²/(16K1 K2)>0.                          (10)

This is the decisive contrary control to any claim that (7) is the sharp all-policy coefficient. It also supplies a stronger executed successor rather than stopping after the first counterpolicy.

For each fixed m the full policy supremum dominates the finite witness. First take S->0 with m fixed, then the supremum over m:

    liminf_(S->0+) [V_lambda(S)(S)-U_lambda(S)(S)]/S^5
       >= (gamma-2Hp nu)_+²/(4Kinf).                       (11)

Notation V_lambda(S)(S) means V at multiplier lambda(S) and total score S. No limit exchange, infinite-policy attainment or matching upper bound is used. A stage count depending on S is not certified by the fixed-m remainders.

## 6. Reproducible algebra and evidence boundary

The probe derives coefficients from the original logarithm. Set q=(beta²-c²)/2, t3=(beta³-c³)/3, h4=(beta^4-c^4)/4 and

    f=r+2lambda alpha, B=r f-2lambda q,
    C=-r B-2lambda t3, D4=-r C-2lambda h4,
    F=f_rr, v=B_r/F,
    v2=(B_rr v+C_r-f_rrr v²/2)/F.

Then rho_lambda(S)=r_lambda+vS+v2S²+O(S³). For the insertion calculation use

    H1=4lambda q-r f, H2=6lambda t3+r B, H3=8lambda h4+r C,
    N2=F v²/2+H1_r v+H2,
    N3=F v v2+f_rrr v³/6+H1_r v2+H1_rr v²/2+H2_r v+H3,
    L2=N2-r H1,
    L3=N3-r N2+(r²-v)H1.

All r derivatives hold lambda fixed; only afterward substitute lambda=2(1+r)²/[(1-r)(r+3)]. This substitution order is load-bearing. Independently differentiating the original rational logarithm at fixed a and multiplying its score series checks the insertion numerator before the stationary relation is imposed. Exact cloud polynomial checks include order and two-satellite improvement; high-precision original-law backward optimization is supplemental numerical evidence, not the theorem or an interval certificate.

Analytic arguments above establish existence, fixed-m remainder and scope. Exact symbolic algebra establishes the displayed constants and polynomial identities; stored report equality establishes reproducibility. Independent internal review is required. No external-expert or proof-assistant certification is claimed.

Next: a uniform-in-stage-count fifth-order upper bound or genuine finite-score Bellman certificate. It must control tail distributions and possible nonterminal satellites, not simply repeat the one-satellite derivative. K2545's O(S^4) bound cannot supply that upper bound; fixed-m analyticity cannot be treated as uniform for m(S).

[Probe](../../tests/channel-swings/k2547_nearcritical_satellite_instability_probe.py), [report](../../lab/process/k2547-nearcritical-satellite-instability.json), [K2545](k2545-critical-stopping-aggregation-2026-11-04.md), [original reduction](k2485-constrained-stopping-frontier-2026-11-01.md).
