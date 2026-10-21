---
title: "K1868: Exponentially cheap sign imbalance in the Fisher two-well endpoint"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact feasible imbalance, asymptotic instability and spectral upper bound; no effective onset, sharp tunneling law or GU physics
---

# Absolute Fisher accuracy does not certify balanced wells

For the actual even optimizer p_delta with raw second moment1 and fourth
moment1+delta, there are exactly feasible densities whose Fisher excess is
exponentially small in1/delta while their total variation, relative entropy
and transport distance from p_delta stay nonzero. This strengthens K1858's
leading-order asymmetry statement: even **absolute** energy convergence does
not give uniform density stability at this endpoint. Every even observable
is nevertheless exactly unchanged by the construction.

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
result: exactly feasible sign tilts, absolute Fisher excess, spectral and statistical consequences
carrier: real probability densities on the line with raw second moment1 and fourth moment1+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher energy 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: even and odd reflection sectors only
action_owner: repository-construction -- constrained scalar Fisher functional
target: uniform endpoint stability of the actual unrestricted optimizer MAP-TYPE=evaluation
```

## 1. Scope, dependencies and the decisive change

[K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md) supplies
the even positive optimizer, quartic equation and ground-state transform.
[K1858](k1858-fisher-two-well-profile-2026-10-20.md) supplies F(1+delta)
=4/delta-1+o(1) and the small-delta potential barrier. Its arbitrary sign
weights concern leading-optimal families and do not yet imply absolute
excess tending to zero. [K1867](k1867-fisher-transport-entropy-certificate-2026-10-20.md)
works at the other, Gaussian endpoint. Its uniform convexity is unavailable here.
The present results are independent mathematics, with no novelty claim.
No source assertion, physics ledger, canonical wording or public posture changes.

Write p=p_delta=u², F=I(p), and
-4u''+(a x²+b x4)u=Eu. Reuse only the following proved K1858 input: for
all sufficiently small delta,

```
a x²+b x4-E >= 1/delta²,  0<=x<=1/2.                 (1)
```

The onset is not numerically certified. Every finite bound below is conditional
on (1) at its chosen delta; no quoted asymptotic supplies an effective onset.

## 2. An interval barrier, not just a point value

Evenness gives u'(0)=0. Equation(1) implies u''>=u/(4delta²), hence u'>=0
on[0,1/2]. Starting at any x in[0,1/4], positive-kernel ODE comparison gives

```
u(1/2)>=u(x) cosh((1/2-x)/(2delta)).
```

The H1 bound sup u²<=2||u||2||u'||2=sqrt(F) and cosh z>=exp(z)/2 yield

```
p(x)<=4 sqrt(F) exp(-1/(4delta)),  |x|<=1/4,
m:=P_p(|X|<=1/4)<=2 sqrt(F) exp(-1/(4delta)).          (2)
```

In particular m tends to zero exponentially. The exponent is a conservative
upper estimate, not the sharp tunneling exponent or a two-sided gap law.

## 3. Exact feasible tilts, including a one-sided density

Set a0=1/4 and define the odd C1 function

```
f(x)=-1 (x<=-a0), sin(2pi x) (|x|<a0), +1 (x>=a0),
p_theta(x)=p(x)(1+theta f(x)),    -1<=theta<=1.        (3)
```

The function f is C1 at the join and Lipschitz globally. Oddness and even p
show that every integrable even moment/observable is unchanged, including
normalization, raw second and fourth moments. For |theta|<1 the square root
is H1 directly. At theta=+1 it vanishes on the left exterior interval and
rises linearly in its square root at -a0; its weak derivative is square
integrable. The negative endpoint is reflected. Thus the endpoints are valid
finite-Fisher competitors, not divisions by an identically zero density.

Expand the Fisher integrand where p_theta>0. The odd terms integrate to zero:
int f p'^2/p=0 and int p'f'=0. Pair x with -x to get

```
D_theta:=I(p_theta)-F
 =theta² int p f'^2/(1-theta² f²)
 <=4pi² theta² m
 <=8pi² theta² sqrt(F) exp(-1/(4delta)).              (4)
```

The integral is zero outside the transition interval; at |theta|=1 interpret
its removable endpoint values there. Inside, f'^2=4pi²(1-f²), so the
inequality follows from 1-f²<=1-theta²f². At theta=+/-1 the first upper
bound is equality. This also proves endpoint passage without a hidden
regularity assumption. D_theta>0 for theta!=0, as required by uniqueness.
All fixed theta therefore have absolute excess tending to zero faster than
any power of delta, while they can put almost all mass in one well.

## 4. What fails, and what survives exactly

Let A_delta=E_p|f|. Since f=sign outside the middle interval,
1-m<=A_delta<=1. Direct integration gives

```
TV(p_theta,p)=|theta| A_delta/2 -> |theta|/2,
P_theta(X>0)=(1+theta A_delta)/2.                    (5)
```

The mean is theta E_p[X f(X)]. Moment concentration E(X²-1)²=delta
implies E||X|-1|<=sqrt(delta), and
|E[Xf]-E|X||<=a0 m. Hence E_theta X -> theta. Jensen applied to any
coupling first gives W2(p_theta,p)>=|E_theta X|. The exact transport limit
is stronger and follows without solving a continuous transport equation.
Collapse each density by X -> sign X. Each collapse costs at most delta in
squared Wasserstein distance, since (|x|-1)²<=(x²-1)² and every even moment
is preserved. The two collapsed laws differ by |theta| A_delta/2 mass,
which must move distance2 between -1 and+1. Therefore

```
|W2(p_theta,p)-sqrt(2|theta| A_delta)|<=2sqrt(delta),
W2(p_theta,p)² -> 2|theta|.                           (5a)
```

The finite error follows from the triangle inequality in both directions.
It shows that the limiting transport cost is linear in the imbalance magnitude,
not its square; the mean lower bound alone misses this discrete mass transfer.

Forward relative entropy has the limit

```
KL(p_theta|p) -> h(theta)
 =[(1+theta)log(1+theta)+(1-theta)log(1-theta)]/2.     (6)
```

This follows from bounded continuous extension of z log z at0, paired
reflection and middle mass m->0. In particular h(1)=log2. Reverse entropy
is infinite at |theta|=1, because p_theta is zero on a positive-p-mass
half-line. For any fixed beta>0 and any constant growing at most polynomially in
1/delta, a bound of the form distance<=constant*D_theta^beta fails for
TV, forward KL and W2 at this endpoint.

Conversely, every even observable remains exactly equal under(3), even
when its expectation is unbounded as delta varies. This is a custody statement
for these competitors, not an all-competitor stability theorem. If an
additional mean-zero condition is imposed on ANY feasible density q, then

```
|E_q sign X|<=E_q||X|-1|<=sqrt(delta),
|P_q(X>0)-1/2|<=sqrt(delta)/2.                       (7)
```

Densities have no atom at0. Equation(7) removes macroscopic sign imbalance
but does not itself prove a full mean-zero TV, entropy or gap estimate.
Symmetry and moment constraints are different assumptions.

### The available mean-zero repair: qualitative TV and finite transport

There is a useful positive successor that requires no new gap estimate.
Let q_delta be exactly feasible, mean zero, and satisfy

```
delta [I(q_delta)-F(1+delta)] ->0.                    (7a)
```

Then TV(q_delta,p_delta)->0. To prove it, apply K1858's joint sign/local-
coordinate Gaussian theorem to q_delta and p_delta: both are leading-optimal
by(7a), the former sign weights tend to one half by(7), and the latter are
exactly one half. The two joint laws therefore approach the same product
of a fair sign and a standard Gaussian in TV. The coordinate map
x -> (sign x,2(|x|-1)/sqrt(delta)) is invertible away from a null point, so
TV is preserved and the triangle inequality proves the claim. This is a
new consumer of K1858, not a repeated compactness proof. No effective TV
modulus or numerical onset is obtained.

Even without(7a), ANY exactly feasible mean-zero q satisfies

```
W2(q,p_delta)<=2sqrt(delta)+sqrt(2) delta^(1/4).       (7b)
```

Reuse K1854's moment-only sign-collapse coupling for both laws. The two
atomic sign laws cost 4|P_q(X>0)-1/2|<=2sqrt(delta), and the two collapses
cost at most sqrt(delta) each. This proves(7b); it is not an energy-based
rate or a sharp exponent claim. Even q improves the bound to2sqrt(delta)
because its sign law is exactly fair. Thus mean-zero repairs qualitative
near-optimal TV stability and moment-only transport, while a finite TV/entropy
certificate still needs new within-well control. The nonzero-mean tilt does
not refute these genuinely different assumptions.

## 5. The actual oscillator gap becomes exponentially small

Let H=-4d²/dx²+a x²+b x4, with its confining self-adjoint realization, and
lambda1 its first eigenvalue above E. The odd test uf is orthogonal to u;
the ground-state transform and Rayleigh principle give

```
0<lambda1-E <= 4 int p f'^2 / int p f²
             <=16pi² m/(1-m).                       (8)
```

This applies once m<1. The test belongs to the quadratic-form domain:
f is bounded Lipschitz and u has the required quartic moment. No parity
claim about all higher eigenfunctions is needed. For the diffusion Dirichlet
form int p |g'|², the optimal Poincare constant is at least
(1-m)/(4pi²m). The factor4 between this form and H-E is explicit. This
explains why the Gaussian-endpoint functional-inequality argument cannot
be continued with a uniform constant. It gives an upper gap bound, not a
matching lower bound, Arrhenius prefactor or effective numerical threshold.

## 6. Verification, contrary cases and next question

Preflight chose an exact odd tilt over approximate Gaussian mixtures because
it preserves all constraints without a moment repair. An interval barrier,
not p(0) alone, is essential. Endpoint square-root regularity was checked
rather than silently excluding the one-sided competitor. Hostile checks target
absolute versus relative excess, missing factor4 in the gap, incorrect
balanced-weight inference, entropy direction and mean-zero scope.

The producer checks symbolic Fisher pairing, the sine derivative identity,
barrier constants, gap factors and binary-entropy differentiation. The separate
probe uses exact rational stand-ins satisfying derivative²=1-f², paired
moments and independent arithmetic, with numerical quadrature labeled only
as illustrative evidence. Planted mathematical-input faults must fail an
assertion after clean baselines; metadata checks are reported separately.
The continuum result is the argument above, not finite sampled controls.
No external expert or proof-assistant verification is claimed.

Reproduce with the two k1868 scripts in tests/channel-swings. Next useful
work is a two-sided effective barrier/gap law or a finite mean-zero/even-sector TV or entropy
stability certificate. The tilt already settles the unrestricted uniform
stability question, so another coefficient or repeated imbalance example
cannot resolve those different analytic burdens.
