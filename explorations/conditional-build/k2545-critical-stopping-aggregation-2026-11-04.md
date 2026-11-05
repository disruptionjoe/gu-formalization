---
title: "K2545 Uniform critical stopping aggregation"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional all-policy small-score cubic asymptotic and concentration; no exact finite-score optimality or GU claim
scripts:
  - tests/channel-swings/k2545_critical_stopping_aggregation_probe.py
---

# K2545 Arbitrarily many stages do not improve the critical cubic coefficient

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
result: K2545
carrier: original finite adaptive fresh fair test-use schedules, initial mixtures and admitted limits with total score S LAYER=toy CHIRALITY=N/A
pairing: original failure-inclusive prefix-weighted probability cost ON=declared_carrier
real_structure: real ratios and probabilities
grading: ordered stages, asymptotic score and mixtures remain distinct
action_owner: repository-construction -- supplied stochastic law
target: uniform critical cubic value, concentration and moving-multiplier boundary MAP-TYPE=evaluation
```

## Result and scope

At the critical multiplier lambda*=4sqrt(3)/3, one stage attains the optimal cubic coefficient over ALL original policies, including arbitrarily many stages and splits that degenerate with the score. The error is uniform O(S^4); the number of stages is not fixed. Near-optimal finite schedules put all but O(S^2) score in one stage when their value deficit is O(S^4). Mixtures obey an expected concentration bound, not a statement about every component.

A released successor identifies the sharp moving-multiplier cubic boundary and an actual two-stage advantage below it. This closes the multistage/degenerating-split cubic question explicitly left by [K2517](k2517-small-score-stopping-transition-2026-11-02.md). It does **not** establish exact finite-S optimality, an S=1/2 budget frontier or a physical probability law. An O(S)-fraction satellite changes the value only at fourth order, precisely where this theorem has a remainder. SC-META-53 remains UNCERTAIN about indefinite-spectrum treatment; source polarities and ledger0.263 are unchanged. This is independent probability mathematics, with no GU, empirical, hardware or novelty claim.

## 1. Original law and critical constants

Reuse K2483/K2485's finite-completed-schedule reduction, with its original adaptive, initial-mixture and admitted-limit scope. For b_i>=0, sum b_i=S, 0<=a_i<=b_i,

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]), w(0,0)=0,
    P_i=product_(j<=i)(1+a_j)^(-1),
    G=P_n-2lambda sum_i P_i w(a_i,b_i).

Let V(S)=sup G at lambda=lambda*. Zero-score stages have a_i=0 and can be removed. Put b_i=S x_i, sum x_i=1, a_i=r_i b_i. Define

    alpha(r)=(1-r)^2/[4(1+r)], beta(r)=(1+r)/2,
    c(r)=beta-alpha, g=2alpha,
    q=alpha beta-alpha^2/2,
    t=alpha beta^2-alpha^2 beta+alpha^3/3,
    f(r)=r+lambda*g(r).

Critical constants, with lambda fixed in derivatives, are

    r*=2sqrt(3)-3,
    A=f(r*)=3-4sqrt(3)/3,
    B=r*A/2=5sqrt(3)-17/2,
    F=f''(r*)=3/2+5sqrt(3)/6,
    Bprime=[d/dr(r^2+lambda*g*r-2lambda*q)]_(r*)
          =1/4+7sqrt(3)/12,
    C_one=-1097/16+5707sqrt(3)/144.                 (1)

The theorem is

    V(S)=1-A S+B S^2+C_one S^3+O(S^4), S -> 0+.    (2)

The constant and score neighborhood in (2) work for every finite stage count, every partition and the inherited mixtures/limits. They depend only on the fixed supplied law, not an optimizer search.

## 2. Uniform fourth-order remainder from the original cost

The exact identity

    w(rb,b)=log(1-cb)-log(1-beta b)

is useful because 0<=c<=beta<=1. Its coefficient of b^m is (beta^m-c^m)/m. For b<=1/4,

    w=alpha b+q b^2+t b^3+R_w, 0<=R_w<=b^4/3.     (3)

The bound follows by summing the m>=4 geometric tail with 1/m<=1/4. In particular alpha<=1, q<=1/2, t<=1/3, deliberately loose bounds sufficient below.

For a prefix with A_i=sum_(j<=i)a_j, let h_d be the complete homogeneous polynomial of degree d in that prefix's a_j. Taylor expansion in a common scale gives

    P_i=1-A_i+h_2-h_3+R_P, |R_P|<=A_i^4,
    |P_i-(1-A_i+h_2)|<=A_i^3,
    |P_i-(1-A_i)|<=A_i^2, |P_i-1|<=A_i.

For every d, h_d<=A_i^d; alternatively the d-th derivative bound is d! A_i^d since all positive denominators at scale>=0 only reduce it. This is independent of prefix length.

For the normalized actions y_i=r_i x_i, write A_i^x=sum_(j<=i)y_j and h_d^i=h_d(y_1,...,y_i). Exact multiplication yields

    G=1-S sum_i x_i f(r_i)+S^2 Q(r,x)+S^3 C(r,x)+R,
    Q=h_2^n+2lambda sum_i alpha_i x_i A_i^x
                 -2lambda sum_i q_i x_i^2,
    C=-h_3^n-2lambda sum_i[t_i x_i^3-q_i x_i^2 A_i^x
                                         +alpha_i x_i h_2^i],
    |R|<=(1+13lambda/3)S^4.                       (4)

Indeed each cost remainder is bounded by
alpha_i b_i A_i^3+q_i b_i^2 A_i^2+t_i b_i^3 A_i+R_w,
and their sum is <=(1+1/2+1/3+1/3)S^4=13S^4/6. Multiply by 2lambda and add the success remainder. Neither expansion silently removes prefix weights.

## 3. Localize EVERY stage ratio uniformly, including tiny stages

For each fixed finite positive partition x, continuity on [0,1]^n ensures a global ratio maximizer. Let G_suffix be the dual value of the stages strictly after stage i, normalized to its start. Exact differentiation of the original law gives

    dG/da_i=P_i/(1+a_i) [lambda M(a_i,b_i)-G_suffix],
    M(a,b)=2w(a,b)-2(1+a) w_a(a,b).                (5)

Since w<=b/3, prefix probabilities <=1 and product(1+a)^(-1)>=1-sum a,

    1-(1+2lambda/3)S <=G_suffix<=1.               (6)

Furthermore, uniformly in r in[0,1] and b<=1/4,

    M0(r)=2/(1+r)^2-1/2,
    |M(rb,b)-M0(r)|<=16b.                         (7)

For detail, |alpha'|<=3/4, beta'=1/2 and |c'|<=5/4. Differentiating the logarithmic representation gives
|w_r-alpha'b|<=(7/3)b^2 and |w|<=b/3. Therefore the error in M is at most
[2/3+3/2+2(5/4)(7/3)]b=8b, already stronger than (7).

For all sufficiently small S (S<=1/1000 suffices at lambda*), the derivative in (5) is strictly positive at r_i=0 and strictly negative at r_i=1, by (6)-(7). Thus every positive stage of every global maximizer is interior. Since f'=1-lambda M0 and f''=4lambda/(1+r)^3>=lambda/2,

    |r_i-r*| <= [32+2/lambda+4/3]S <35S<36S.       (8)

The cancellation of b_i in (5) is essential. A bound on a weighted average alone would not control a vanishingly small stage. Zero-score stages were already removed; nothing divides by a positive lower bound for x_i.

## 4. Complete the squares uniformly over every partition

Write r_i=r*+S u_i and T_i=sum_(j>=i)x_j. At criticality, K2517's H=0 gives Q(r*,x)=B for all partitions. Differentiating its ordered Q gives

    q_i^grad=x_i[A T_i+(Bprime-A)x_i]=x_i ell_i.

The cubic maximization is therefore

    C_common(x)+sum_i x_i[ell_i u_i-(F/2)u_i^2],

with optimizer u_i=ell_i/F and gain sum_i x_i ell_i^2/(2F). The ell_i are uniformly bounded, including as x_i->0, so this supplies a legal lower-witness ratio for small S. The actual global maximizers satisfy (8), so |u_i|<=36 gives a common upper expansion.

Here is the precise uniformity argument. Each f,alpha,q,t and its derivatives through the needed order is bounded on the fixed compact interval [0,1]. Taylor's third-order error in the linear term is bounded by
(S/6) sup|f third derivative| max_i|r_i-r*|^3. Every monomial in Q has at most two x weights and normalized absolute weight sum bounded by a fixed constant: h_2 weights sum<=1, sum_i x_i A_i^x<=1 and sum_i x_i^2<=1. Its second derivative along any bounded ratio direction is consequently bounded by a constant times that direction's squared sup norm. Every monomial in C has at most three x weights, also with total weight bounded independently of n: h_3<=1, sum x_i^3<=1, sum x_i^2 sum_(j<=i)x_j<=1 and sum x_i h_2^i<=1. Its first directional derivative is bounded by a constant times the direction's sup norm. Thus the three Taylor errors in (4) are O(S^4), uniformly in n,x, by (8). This argument also bounds the explicit lower witness. There is a common finite C0 such that the optimized value U_x satisfies

    |U_x-[1-A S+B S^2+C_opt(x)S^3]|<=C0 S^4.       (9)

This is a weighted derivative proof, not a fixed-dimensional implicit-function theorem. The exact finite probes below check algebraic coefficients; they do not replace this uniform estimate.

## 5. Reduce arbitrary ordered partitions to two moments

Let s3=sum_i x_i^3 and L=sum_(i<j)x_i^2 x_j. Exact algebra gives

    C_opt(x)=C_one+c3(s3-1)+cL L,
    c3=(7619sqrt(3)-13185)/144>0,
    cL=(249sqrt(3)-431)/2>0,
    d=c3-cL/3=(1643sqrt(3)-2841)/144>0.            (10)

For a direct arbitrary-n reduction, set X_i=sum_(j<=i)x_j and s2=sum x_i^2. The prefix identities are

    h3(x)=(1+3s2+2s3)/6,
    Z=sum_i x_i^2 X_i=s2-L,
    sum_i x_i T_i^2=1/3+2s3/3+L,
    sum_i x_i^2 T_i=s3+L,
    sum_i x_i h2(x_1,...,x_i)=h3(x).

These follow by sorting ordered triples (or telescoping complete homogeneous polynomials). Consequently C_common=-r*^2 A h3-2lambda*t*s3+2lambda*r*q*Z. With E=Bprime-A the square gain is
[A^2(1/3+2s3/3+L)+2AE(s3+L)+E^2 s3]/(2F).
The s2 coefficient -r*^2 A/2+2lambda*r*q is exactly zero; the remaining constant, s3 and L coefficients give (10).

An independent way to verify the identity for every n is to group the degree-three monomials into x_i^3, x_i^2 x_j, x_i x_j^2 and x_i x_j x_k. The exact cubic C in (4), plus its square-completion term, has only those four order types; their coefficients give (10) after sum x_i=1. A finite three-stage symbolic check covers the coefficient types, not merely three sampled partitions. In particular the apparent sum x_i^2 coefficient cancels.

With R=sum_(i<j)x_i x_j^2 and T=sum_(i<j<k)x_i x_j x_k,

    1-s3=3(L+R)+6T, so L<=(1-s3)/3.

All terms are nonnegative. Hence

    C_opt(x)<=C_one-d(1-s3)<=C_one.                (11)

Exact sign certificates are
3*7619^2-13185^2=303258,
3*249^2-431^2=242,
3*1643^2-2841^2=27066.
They avoid rounding the small positive constants. One stage has s3=1,L=0 and attains C_one. Combining (9)-(11), taking the supremum over all finite schedules, and then applying the original reduction proves (2). Initial mixtures preserve the upper bound by linearity; admitted limits preserve it by their defining value convergence. No infinite policy is claimed to attain the supremum.

## 6. Released consumer: score concentration, with the mixture boundary

For any finite schedule within eta>=0 of V(S), use its per-shape upper bound and the one-stage lower bound. With a common constant C0 enlarged if necessary,

    1-s3 <=eta/(d S^3)+(2C0/d)S,
    S-max_i b_i <=eta/(d S^2)+(2C0/d)S^2.          (12)

Indeed s3<=max_i x_i (in fact <=max_i x_i^2), so 1-max x_i<=1-s3. Thus an eta=O(S^4) near-optimum must aggregate all but O(S^2) of its score. This is a quantitative stability statement about the original-law value, not only a sign of a coefficient.

For initial mixtures of schedules with the SAME total score, (12)'s first inequality holds in expectation. It does not constrain every component: mix a diffuse schedule with probability O(S) into a one-stage optimizer. Its loss is only O(S^4), yet the diffuse component remains diffuse. Likewise a two-stage split x=S,1-S has 1-s3=3S(1-S) and only O(S^4) cubic loss. A positive uniform cubic gap for every nontrivial split is false. These countercontrols explain exactly why fourth-order or genuine finite-score Bellman work remains necessary.

## 7. Released successor: the sharp moving-multiplier cubic boundary

Now let lambda(S)=lambda*+mu S with fixed real mu, and denote the optimized one-stage value by U_lambda(S). The preceding estimates are uniform with lambda in a compact neighborhood of lambda*: the minimizer r_lambda stays strictly interior, derivative bounds remain finite and the endpoint margins stay positive. Thus they apply to the moving multiplier without treating a fixed-lambda remainder as automatically uniform.

K2517's common-r quadratic shape coefficient H satisfies

    Hprime=[dH/dlambda]_(lambda*)=(141-81sqrt(3))/8>0.

Expanding around r_lambda, all partition-independent coefficients cancel in comparison with U_lambda. For every shape, uniformly,

    U_shape,lambda(S)-U_lambda(S)
       =S^3 D_mu(x)+O_mu(S^4),
    D_mu(x)=Delta0(x)-mu Hprime(1-s2),
    Delta0=c3(s3-1)+cL L.                           (13)

The change in cubic coefficients caused by lambda-lambda*=O(S) contributes only O(S^4). Put

    c0=(13185-7619sqrt(3))/48,
    c1=(2841-1643sqrt(3))/48.

The exact ordered-triple identity is

    Delta0-(c1/2)(1-s2)
       =-cL sum_(i<j)x_i x_j^2+(2c0-3c1)T <=0,    (14)
    2c0-3c1=(17847-10309sqrt(3))/48<0.

The sign has the integer witness 3*10309^2-17847^2=311034. Equality of the supremum ratio Delta0/(1-s2) with c1/2 follows by two stages x1=1-y,x2=y and y->0+. Order matters: the large stage comes first.

Therefore the sharp first-order asymptotic boundary for **cubic comparison** is

    mu0=c1/(2Hprime)=37/66-257sqrt(3)/396.           (15)

For every fixed mu>=mu0,

    0<=V_lambda(S)-U_lambda(S)<=O_mu(S^4).

For every fixed mu<mu0, take a fixed two-stage split with its first fraction sufficiently close to one. Then D_mu>0, and the explicit ratios
r_i=r_lambda+S[A T_i+(Bprime-A)x_i]/F provide an actual original-law policy strictly better than the optimized one-stage policy for every sufficiently small positive S. The O(S^4) bound is uniform, so a positive fixed cubic coefficient dominates it.

A concrete witness is mu=-1, x1=3/4,x2=1/4:

    D_-1=(7119-4109sqrt(3))/256>0,
    7119^2-3*4109^2=28518.

This gives an actual policy advantage along lambda=lambda*-S, not a numerical comparison or an assertion about a fixed finite score. At mu=mu0, the two-stage gap is -cL(1-y)y^2, more degenerate than the critical-lambda concentration bound. Section6's concentration rate is not transferred to this boundary. Fourth-order corrections and an exact finite-score phase curve remain open.

## Evidence and next question

The probe derives the logarithmic coefficients, exact stage derivative, ordered cubic coefficient types, square completion, signs, order sensitivity and collapsing-split/mixing controls. Saved-report equality is reporting consistency. The universal claims rely on sections2-7 and independent internal mathematical review; there is no proof-assistant or external-expert certification.

Next: determine the fourth-order optimal satellite behavior at the sharp moving-multiplier boundary or a finite-score original-law certificate, retaining arbitrary-stage uniformity. K2517's strictly subcritical finite witness remains valid. Another fixed split, a numerical optimum or a changed cost convention cannot establish exact one-stage optimality.

[Probe](../../tests/channel-swings/k2545_critical_stopping_aggregation_probe.py), [report](../../lab/process/k2545-critical-stopping-aggregation.json), [K2517](k2517-small-score-stopping-transition-2026-11-02.md), [original reduction K2485](k2485-constrained-stopping-frontier-2026-11-01.md), [K2483](k2483-adaptive-stopping-bellman-2026-11-01.md).
