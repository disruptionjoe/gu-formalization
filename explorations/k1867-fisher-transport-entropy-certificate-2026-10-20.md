---
title: "K1867: Effective Fisher entropy, transport and quadratic-observable certificates"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: small-q actual optimizer strong log concavity and one-sided entropy/W2/quadratic-loss stability; no unrestricted higher-moment transfer or GU physics
---

# The energy certificate also controls quantile transport and quadratic losses

Let p_q minimize Fisher information among real-line probability densities with
raw second moment1 and fourth moment3-q. For 0<q<=1/100 and any exactly feasible
p of finite Fisher information, put D=I(p)-I(p_q). Then

```
KL(p || p_q) <= D/sqrt(2),
W2(p,p_q)² <= 2D.                                             (1)
```

W2 here uses cost |x-y|², without a factor one-half. In one dimension this is
an integrated squared quantile error. For every locally absolutely continuous
f with |f'(x)|<=L|x|,

```
|E_p f-E_pq f| <= L sqrt(2D).                                 (2)
```

This admits unbounded quadratic-growth losses. It does not assert a bound
on arbitrary higher polynomial moments or the reverse relative entropy.
Applied to K1865's exact feasible density t_s, 0<s<=1/200, the existing dual
error E_s gives KL<=E_s/sqrt(2), W2²<=2E_s and (2) with D replaced by E_s.
No new quasimode order or optimizer fitting is needed.

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
result: actual optimizer uniform log concavity and effective information-to-transport and quadratic-observable bounds
carrier: real-line probability densities with raw second moment1 and fourth moment3-q, 0<q<=1/100 LAYER=toy CHIRALITY=N/A
pairing: Fisher integral, relative entropy and optimal quadratic transport ON=real_probability_densities
real_structure: positive real optimizer; competitors may have zeros and no sixth moment
grading: scalar polynomial degree only
action_owner: repository-construction -- moment-constrained scalar Fisher functional
target: entropy to actual optimizer, RMS quantile displacement and quadratic-growth loss MAP-TYPE=evaluation
```

## 1. New consumer, reused evidence and the load-bearing hypotheses

[K1865](k1865-fisher-effective-trial-certificate-2026-10-20.md) supplies a
rigorous finite energy deficit E_s but reports bounded-observable/TV consumers.
[K1862](k1862-fisher-second-density-response-2026-10-20.md) supplies the actual
full-line quartic ground state and gap; [K1859](k1859-fisher-optimizer-tail-response-2026-10-20.md)
proves on 0<q<=1/100 that its coefficients obey a_q>=1/2 and b_q>0.
The new issue is whether finite energy certifies RMS sample displacement and
unbounded quadratic loss, where a TV estimate alone is insufficient at the
same rate. The optimizer is the reference, not a possibly nodal trial.

This is independent scalar mathematics. No source, ledger or canon verdict
changes. Searches of preceding Fisher artifacts found endpoint W2 limits and
TV/weighted asymptotics, not this effective entropy/transport certificate.
The functional inequalities used below are classical, and no novelty is
claimed. The double-well k=2 reference of K1847 need not be log-concave;
we do not transfer this small-q argument to that interval.

## 2. Prove strong log concavity before using a transport inequality

Write psi=sqrt(p_q)>0 and H=-4d²+a x²+b x4, H psi=E psi, with a>=1/2,b>0.
We claim U=-log p_q satisfies

```
U'' >= sqrt(a) >= 1/sqrt(2).                                (3)
```

First take the positive Dirichlet ground state on(-R,R). The convex-potential
log-concavity theorem applies to H/4: its potential(a x²+b x4)/4 is convex.
See Andrews--Clutterbuck, [Theorem1.5](https://arxiv.org/abs/1006.1686), with
zero comparison potential; in particular w=-log psi_R has w''>=0.
This imported theorem is about a positive Dirichlet ground state, not an
arbitrary oscillator eigenfunction or a squared-polynomial trial.

There is a short additional ODE argument for the quantitative constant.
Set m=w''. From 4w''-4(w')²+V=E, differentiate twice:

```
4m''-8w'm'-8m²+V''=0.                                    (4)
```

At either regular Dirichlet endpoint psi_R has a simple zero, so
m=distance^(-2)+O(1) tends to+infinity. Its global minimum is attained inside.
There m'=0,m''>=0, whence 8m²>=V''>=2a. Since m>=0,
m>=sqrt(a)/2 everywhere. Therefore U_R''=2m>=sqrt(a).

Let R increase to infinity. Dirichlet eigenvalues decrease to the full-line
lowest eigenvalue by the quadratic-form variational principle and density of
compactly supported form functions. Confinement gives compactness of normalized
ground states; local ODE estimates give C² convergence to the unique positive
full-line ground state. Positivity on compact intervals passes the logarithmic
second-derivative bound to the limit. This proves(3) without assuming a
large-x WKB expansion or differentiating an asymptotic value series.

## 3. Exact ground-state transform supplies relative information

For u=sqrt(p), the ground-state transform gives, first on a form core and
then by form closure,

```
4 integral psi² |(u/psi)'|²
 =4 integral |u'|² + integral(V-E)u²
 =I(p)-I(p_q)=D.                                         (5)
```

The last equality uses the same mass, second and fourth moments, since
V=a x²+b x4. The left side is relative Fisher information
`I_rel(p|p_q)=integral p |(log p-log p_q)'|²` in its weak square-root sense.
Finite fourth moment and finite kinetic form ensure applicability; no sixth
moment is required. Local positivity of psi makes the weighted weak derivative
well-defined; form-core closure handles zeros and tails without inserting a
pointwise score assumption. With imperfect moments the exact right side is
I(p)-I(p_q)+a(E_p X²-1)+b(E_p X4-(3-q)); raw energy difference alone then
is not relative information. That is an explicit input gate, not a robustness
claim for incorrectly normalized experimental data.

## 4. Functional inequalities and normalization audit

For a probability reference exp(-U) with U''>=rho>0, the logarithmic Sobolev
inequality gives KL(p|p_q)<=I_rel/(2rho), and its quadratic transport consequence
is W2²<=2KL/rho. A primary proof and constants are in Bobkov--Gentil--Ledoux,
[Theorem4.1 and equations1.1/1.13](https://www.math.univ-toulouse.fr/~ledoux/HamiltonJacobi.pdf).
Their W2 uses one-half the squared-distance cost; converting it is essential.
Approximation and lower semicontinuity extend these inequalities to the form
domain in(5). Combining them with rho>=1/sqrt(2) proves(1).
The sharper coefficient-dependent statements are KL<=D/(2sqrt(a)) and
W2²<=D/a. We keep the weaker uniform constants to avoid estimating a numerically.

Pinsker also yields `TV²<=D/(2sqrt(2))`, improving the earlier gap-only bound
on this small-q interval. This is a derived consumer, not a new independent
arc. None of these inequalities reverses the arguments of KL. A nodal or
compactly supported feasible trial can have infinite KL(p_q|trial), even when
its forward entropy is finite and its Fisher deficit is small.

## 5. Quantiles, quadratic losses and explicit error budgets

The monotone coupling of two real-line laws gives

```
integral_0^1 |F_p^(-1)(u)-F_pq^(-1)(u)|² du = W2² <=2D.    (6)
```

This certifies RMS quantile displacement; it is not a pointwise extreme-
quantile bound. It also bounds expectation error of every1-Lipschitz observable
by sqrt(2D). For |f'|<=L|x|, integration along a segment gives
`|f(x)-f(y)|<=(L/2)|x-y|(|x|+|y|)`. Under the optimal coupling, Cauchy-Schwarz
and both raw second moments equal1 give E(|X|+|Y|)²<=4. This proves(2).
It covers f(x)=(|x|-R)_+², R>=0, with L=2, uniformly in the clipping threshold.
This is an actual tail-sensitive quadratic loss, even though the raw second
moment itself is fixed exactly. Its discrepancy is at most2sqrt(2D).

For the exact trial t_s, K1865 gives E_s<384s6/5. Consequently

```
KL(t_s|p_q(s)) <55s6,
W2(t_s,p_q(s)) <13s³,
|E_t_s (|X|-R)_+²-E_pq(s) (|X|-R)_+²| <26s³.             (7)
```

At s=1/1000 its exact rational E_s satisfies 2E_s<(13/10^9)²,
and E_s/sqrt(2)<55/10^18. Thus RMS quantile error is below1.3e-8;
every tail-quadratic loss error is below2.6e-8. Bounds are certified rational
comparisons after squaring positive quantities, not decimal quadrature.

If another exactly feasible p satisfies I(p)<=I(t_s)+eta, eta>=0, substitute
E_s+eta throughout(1),(2),(6). A desired RMS transport tolerance epsilon
is guaranteed by E_s+eta<=epsilon²/2. A desired quadratic-loss tolerance
zeta for slope bound L is guaranteed by E_s+eta<=zeta²/(2L²).
For squared Euclidean cost on m independent coordinates, the product-law
W2² is m times the one-dimensional value; product KL is also additive.
These quantify finite ensemble errors, not uniform-in-m accuracy.

## 6. Contrary routes and finite-hypothesis controls

Gaussian translations test sharp normalizations: for phi(x-t), relative
Fisher=t², KL=t²/2 and W2²=t². The raw Fisher deficit is zero, because its
second moment is1+t² rather than1. Formula(5)'s moment correction gives t²
exactly. This rejects any attempt to omit the moment hypotheses or the factor4
in the square-root energy. Gaussian variance controls independently test the
entropy/transport constants and the half-cost convention.

The preceding rare-tail feasible competitors with divergent sixth moments
remain valid. Neither strong log concavity of the *reference* nor finite
forward entropy makes a competitor log-concave or supplies its sixth moment.
A reference density vanishing on a positive-measure set would give infinite
reverse KL from the everywhere-positive optimizer. This is a warning about
entropy direction, not a claim that the particular K1865 trial has infinite
reverse KL: isolated polynomial zeros alone do not establish that. No reverse-
KL rate is asserted or needed by any consumer.

## 7. Reproduction, review and frontier

The producer verifies the differentiated Riccati identity, moment-corrected
Gaussian transform, exact certificate arithmetic and positive-constant
conversions. The independent standard-library probe reconstructs the rational
K1865 polynomials and deficit, tests independent Gaussian controls and planted
coefficient/scope faults. Arithmetic scripts do not certify the continuum
log-concavity, exhaustion or functional-inequality theorems; the proof and
primary references above own those steps. No separate agent, independent
human, proof assistant or external acceptance is claimed.
Reproduce scripts named in lab/process/k1867-fisher-transport-entropy-certificate.json.

The named entropy/RMS/quadratic consumers are now certified without another
series coefficient. Extension to the two-well window requires a different
functional inequality; global positive curvature is not available there.
High polynomial loss needs additional tail assumptions, and native GU
response still needs its own action/observation/physical-domain construction.
