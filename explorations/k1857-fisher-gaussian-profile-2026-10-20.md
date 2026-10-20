---
title: "K1857: Near-optimal Fisher densities have a universal Gaussian tangent"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: first-order Gaussian Sobolev density profile and bounded-observable responses; no uniform higher-moment response, quartic value coefficient or GU physics
---

# Near-optimal Fisher densities have a universal Gaussian tangent

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
result: universal first-order profile, sharp Hellinger and TV asymptotics, bounded observable response and exact-moment tail counterexample
carrier: real probability densities with raw second moment1 and prescribed fourth moment LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial degree only; no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: unrestricted density problem on the real line MAP-TYPE=evaluation
```

## 1. Result: the value law determines the first density response

Let q decrease to0 and let p_q be any densities with raw E X²=1,
E X4=3-q, finite Fisher I, and

```
[I(p_q)-1]/q² -> 1/6.                                    (1)
```

They need not be even or exact minimizers. The minimizers and any sequence
with I-F(3-q)=o(q²) satisfy (1) by [K1855](k1855-fisher-gaussian-endpoint-2026-10-20.md).
Let phi be standard Gaussian, H3=x³-3x, H4=x4-6x²+3, and h_q=sqrt(p_q/phi).
In the Gaussian weighted Sobolev norm ||f||²=E_phi f²+E_phi|f'|²,

```
(h_q-1)/q -> -H4/48 strongly in H1(phi),                   (2)
(p_q-phi)/q -> -H4 phi/24 strongly in L1(dx).              (3)
```

This proves the actual first-order profile, rather than assuming that the
squared-Hermite upper trial is the optimizer. It supplies bounded-observable
linear response and sharp Gaussian-distance constants. It does not control
unbounded high moments or the quartic coefficient of the Fisher value.
No physical GU identification or novelty claim is made. Classical
moment-constrained Fisher variational literature includes
[Vignat and Bercher, 1998](https://www.sciencedirect.com/science/article/abs/pii/S0165168497002259);
its indexed abstract is context, not a source for the theorem below.

## 2. The exact dual square forces the derivative profile

Reuse K1855's whole-line certificate, with a=q/6,

```
d_a=1+a x²/2,  g_a=x+a H3/d_a,
I=E_p(rho+g_a)²+E_p P_a+E_p R_a,
E_p P_a=1+q²/6+q³/18,   R_a>=0.                          (4)
```

All expectations in (4) exist with only a fourth moment: g_a has linear
growth for each a>0 and R_a grows at most quartically. The inherited weak
integration-by-parts identity therefore applies, including square-root zeros.
Under (1),

```
E_(p_q)(rho+g_(q/6))²/q² ->0.                            (5)
```

Since h'_q=(rho+x)h_q/2, equation (5) is equivalent to

```
|| h'_q/q + H3 h_q/[12(1+q x²/12)] ||_(L2(phi)) ->0.      (6)
```

K1855's Poincare bound gives h_q->1 in L2(phi). On each compact interval,
the rational coefficient in (6) converges uniformly to H3/12. Consequently
h'_q/q converges to -H3/12 locally in L2(phi). Globally,

```
||h'_q/q||² = [I(p_q)-1]/(4q²) ->1/24,
||H3/12||² = E_phi H3²/144 =6/144=1/24.                  (7)
```

Local strong convergence and the global norm bound give weak L2 convergence
(by approximating any L2 test with compactly supported tests). Equality of
the limiting norms upgrades it to global strong convergence. This norm
saturation is the missing tail step; replacing the rational denominator by1
under an unbounded whole-line integral is not used.

## 3. Normalization fixes the constant and yields strong H1

Put r_q=(h_q-1)/q. Poincare plus normalization gives a uniform L2 bound:
E(h_q-1)²=2(1-Eh_q)<=2[1-(Eh_q)²]<=2E|h'_q|²=O(q²).
The exact normalization identity is

```
2 E_phi r_q + q E_phi r_q²=0,    so E_phi r_q ->0.          (8)
```

The derivative of r_q+H4/48 tends to0 strongly by (7) and H4'=4H3.
Its Gaussian mean tends to0 because E_phi H4=0. Gaussian Poincare proves
its L2 norm tends to0, establishing (2) with no compactness assumption on
fourth or sixth moments. Since

```
(p_q/phi-1)/q = 2r_q+q r_q²,
```

the first term converges in L1(phi) and the second vanishes there. This proves
(3). The signed first-order tangent integrates to0, preserves the second
moment at the polynomial level, and changes the fourth by -q:
E H4=E X²H4=0 and E X4 H4=24. These identities check the normalization;
the proof does not infer unbounded-moment convergence from (3).

## 4. Executed successors: sharp distances and observable response

For every bounded measurable f,

```
E_(p_q) f = E_phi f - (q/24) E_phi[f H4]+o(q),             (9)
```

uniformly over ||f||_infinity<=1 in the sense that the L1 remainder controls
the supremum. In particular nonsymmetric leading-optimal families have odd
bounded-observable response o(q). No claim of exact symmetry is made for them.
Using E H4²=24, the squared square-root distance and affinity are

```
integral (sqrt(p_q)-sqrt(phi))² = q²/96+o(q²),
integral sqrt(p_q phi) = 1-q²/192+o(q²).                   (10)
```

If the convention Hellinger²=(1/2) integral(square-root difference)² is used,
its coefficient is1/192, not1/96. From the L1 limit,

```
TV(p_q,phi)/q -> E_phi|H4|/48
 = (sqrt(6)/12)[alpha phi(alpha)+beta phi(beta)],
alpha=sqrt(3-sqrt(6)), beta=sqrt(3+sqrt(6)).               (11)
```

To check the absolute integral, H4 is negative only for alpha<|x|<beta,
(d/dx)(H3 phi)=-H4 phi, and E H4=0. Thus E|H4|=
4[H3(beta)phi(beta)-H3(alpha)phi(alpha)] with
H3(beta)=sqrt(6)beta and H3(alpha)=-sqrt(6)alpha.
Unlike the earlier general TV bound, (11) is sharp for the stipulated
near-optimal sequences; it is not a finite-q error estimate.

The bounded-observable result also gives explicit diagnostics without a new
unbounded-moment assumption. Uniformly in real frequency t and threshold z,

```
chi_q(t)=exp(-t²/2)[1-q t4/24]+o(q),
CDF_q(z)=Phi(z)+(q/24)H3(z)phi(z)+o(q).                   (11a)
```

Here the first remainder is uniform in t, not a uniform relative error after
dividing by exp(-t²/2). The Fourier identity follows from four Gaussian
integrations by parts; the CDF identity follows from the same primitive used
in (11). Uniformity is supplied by the L1 error in (3), not pointwise Taylor
expansion. Consequently the Kolmogorov distance divided by q tends to
sup_z |H3(z)phi(z)|/24. Its supremum occurs among z=+-alpha,+-beta;
the function vanishes at infinity. For quantile levels u in any fixed compact
subinterval of (0,1), with z=Phi^(-1)(u),

```
Q_q(u)=z-q H3(z)/24+o(q),                                (11b)
```

uniformly in u. The positive Gaussian derivative on that compact interval
and the uniform CDF expansion justify inverse expansion, including generalized
inverses if a competitor has density zeros. There is no tail-quantile claim
when u approaches0 or1 with q.

For the exact minimizers the sharper K1855 cubic value and its positive
residual also imply E_p(rho+g_(q/6))²=o(q³). Indeed the residual expectation
has liminf/q³>=7/36, and E P already accounts for q³/18; together these
exhaust the proved cubic coefficient1/4. Both the square and any excess of
the residual are nonnegative in the limiting comparison. This improves the
score defect but still supplies no quantitative rate for unbounded tests.

## 5. Contrary construction: leading optimality allows divergent sixth moment

The limit theorem cannot be used to exchange derivatives of every polynomial
moment. Here is an exact-moment, smooth even counterexample. For 0<q<=1/100
let

```
epsilon=q^10, w=q^(-4), v=(1-q^6)/(1-q^10),
k0=(3-q-3q²)(1-q^10)/(1-q^6)²,  q0=3-k0.
```

Then 1<k0<3 and q0/q->1 (indeed q0=q+3q²+O(q6)). Let r_q0 be the actual
unit-second-moment optimizer with fourth moment k0 from K1843, let r_v be
its dilation to variance v, and define

```
p_q=(1-epsilon)r_v+epsilon N(0,w).                       (12)
```

Its second moment is exactly1 and its fourth exactly3-q. The domain checks
can be made without numerical sampling: k0>2 since
3-q-3q²>2.98 and the remaining factor>(1-10^-20); and

```
3(1-q6)²-(3-q-3q²)(1-q10)
 = q+3q²-6q6+(3-q-3q²)q10+3q12 >0
```

for the stated q window (6q6<q). Thus k0<3. Fisher convexity gives

```
I(p_q) <= (1-q10) F(k0)/v + q14 =1+q²/6+o(q²).           (13)
```

The lower bound K1855 gives the matching asymptotic. In (13),
(1-q10)/v=1+O(q6), and F(k0)=1+q0²/6+O(q0³). Hence (1)-(11)
all hold for this family. Nevertheless

```
E_(p_q) X6 >=15 epsilon w³ =15/q² ->infinity.             (14)
```

All sixth moments are individually finite because the core is a confining
quartic ground state, but there is no uniform sixth-moment control. This
explicitly refutes the inference from first-order L1/Gaussian H1 response to
polynomial moment response. It is not a statement that exact optimizers have
such tails; (12) consists of near-optimal competitors. Controlling the exact
optimizer's unbounded residual at next order remains a distinct task.

## 6. Verification and scope review

Run `sage -python tests/channel-swings/k1857_fisher_gaussian_profile.py` and
`python3 tests/channel-swings/k1857_fisher_gaussian_profile_probe.py`.
The producer verifies the dual identity, Hermite norms and derivatives,
profile/metric constants, exact contamination moments and endpoint orders.
A separate Fraction polynomial implementation and rational fixtures check
these without importing the producer. Planted mathematical input/reference
faults follow a passing clean baseline; reporting flags are checked separately.
No finite algebra checks prove the Sobolev convergence theorem: sections2-3
supply its local-to-global and normalization proof.

Inline hostile review covers weak derivatives at zeros, compact versus global
convergence, norm saturation, raw-moment constraints, TV/Hellinger conventions,
exact versus approximate minimizers, and the sixth-moment counterexample.
No separate expert, proof assistant or external acceptance is claimed. The
new results leave actual source metric/observation ownership and physics
ledger verdicts unchanged. Next-order Gaussian value certification requires
optimizer-specific unbounded-tail and second-response estimates; it cannot
reuse (9) for x6 or x8 without new proof.
