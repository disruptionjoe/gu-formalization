---
title: "K1870: An effective balanced two-well Fisher density certificate"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit endpoint TV and local-profile bounds; no fixed-delta spectral gap, entropy modulus, sharp rate or GU physics
---

# Balanced two-well accuracy can be certified without a tunneling estimate

For any density p with raw second moment1 and fourth moment1+delta, finite
Fisher information, and 0<delta<=1/8, define eta=max(0,delta I(p)-4).
If p has mean zero, its distance from the actual even Fisher minimizer p_delta
satisfies

```
TV(p,p_delta) <= min(1,21 delta^(1/6)+sqrt(eta/2)).       (1)
```

Even p improves21 to20. This is a fully explicit **endpoint** estimate:
it tends to zero when delta and the scaled energy slack tend to zero.
It is conservative, and its additive delta term does not vanish when energy
excess alone tends to zero at fixed delta. It supplies the finite version of
K1868's qualitative balanced-well result without asserting a new spectral gap.

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
result: effective local Gaussian, balanced-well TV and finite precision consequences
carrier: real probability densities on the line with raw second moment1 and fourth moment1+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher energy 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative square roots; no physical real-form identification
grading: signs of X and local well coordinates only
action_owner: repository-construction -- constrained scalar Fisher functional
target: finite endpoint density accuracy, with balance explicitly supplied MAP-TYPE=evaluation
```

## 1. Prior results and the different proof route

[K1858](k1858-fisher-two-well-profile-2026-10-20.md) proves qualitative
local Gaussian profiles by compactness. [K1868](k1868-fisher-two-well-instability-2026-10-20.md)
proves that unbalanced wells can have exponentially small absolute excess.
[K1849](k1849-fisher-effective-gap-2026-10-20.md) supplies an effective
true-optimizer gap on a compact fourth-moment interval away from1. None is
a finite endpoint TV bound. No previous result is withdrawn.

Here a cutoff and the **ordinary Gaussian oscillator** replace the unknown
true-optimizer gap. Its spectrum is standard, not a novelty claim; the
normalization below follows by rescaling the Hermite operator in
[NIST DLMF, section1.18(v)](https://dlmf.nist.gov/1.18#v).
The constrained optimizer remains K1843's object, not this auxiliary oscillator.
All results are independent scalar mathematics. GU source assertions, the
88-active/91-stored physics ledger and canon remain unchanged.

We will also use a simple finite upper bound. An equal mixture of Gaussians
with means +/-sqrt(1-v) and common variance v=1-sqrt(1-delta/2) has exactly
second moment1 and fourth moment1+delta. Fisher convexity gives

```
F(1+delta) <= 1/v = 2(1+sqrt(1-delta/2))/delta <=4/delta. (2)
```

Thus for D=I(p)-F(1+delta)>=0, eta<=delta D. One may replace eta in every
upper bound below by delta D. The eta version needs only measured I and
the exact moments, so it avoids an unknown numerical value of F.

## 2. A quantitative cutoff with no extra moment assumption

Put s=sqrt(delta)/2, r=delta^(1/3)<=1/2 and T=(|X|-1)/s.
For sigma=+1,-1 let

```
q_sigma(t)=s p(sigma(1+s t)),  t>-1/s,
u_sigma=sqrt(q_sigma),       w_sigma=integral q_sigma.
```

Extend q by zero as a density, not u as an H1 function. Exactly,

```
sum integral ((2+s t)^2/4) t^2 q_sigma=1,
sum integral |u_sigma'|^2=delta I(p)/16.              (3)
```

Choose chi(y)=1 for |y-1|<=r/2, linear down to0 for
r/2<|y-1|<r, and0 outside. It has weak derivative bounded by2/r.
Set v_sigma(t)=chi(1+s t)u_sigma(t), extended by zero. Since the cutoff
vanishes in a neighborhood of y=0, these extensions belong to H1(R).
No artificial boundary jump appears. The moment identity
E(X^2-1)^2=delta and (y-1)^2<=(y^2-1)^2 imply

```
ell:=1-sum ||v_sigma||_2^2 <= 4delta/r^2=4r.          (4)
```

The same probability bound applies on the support of chi'. Using
|a+b|^2<=(1+r)|a|^2+(1+1/r)|b|^2 and s^2=delta/4 gives

```
K:=sum ||v_sigma'||_2^2
 <=(1+r)delta I(p)/16+4r+4r^2.                        (5)
```

Indeed the cutoff term before Young's factor is at most
s^2(4/r^2)(4delta/r^2)=4delta^2/r^4. This uses the small transition mass;
a bare derivative bound would be too expensive. On the retained support,
(2+s t)^2/4>=(1-r/2)^2, so

```
M:=sum integral t^2 v_sigma^2 <= (1-r/2)^(-2).        (6)
```

Only the given fourth moment has been used. Escaping sixth moments do not
invalidate this localized estimate.

## 3. The oscillator turns energy slack into profile distance

Let phi be the standard normal density and psi=sqrt(phi).
H0=-d^2/dt^2+t^2/4 has eigenvalues n+1/2, n=0,1,...,
with normalized ground state psi. Its gap above psi is1. With
N=sum||v_sigma||^2, the nonnegative form excess is

```
E0=K+M/4-N/2.
```

Equations(4)-(6) and delta I(p)<=4+eta give

```
E0 <= 9r+eta/8 =: e.                                  (7)
```

For an explicit check of constants, on 0<r<=1/2,

```
(14/9)r-[(1-r/2)^(-2)-1]
 =r(1-2r)(20-7r)/(9(2-r)^2) >=0.
```

The r coefficient is at most1/4+4+2+2+7/18=311/36<9;
(1+r)/16<=3/32<1/8. These bounds explain every rounding in(7).

Project each v_sigma onto psi: c_sigma=<v_sigma,psi>>=0.
The spectral gap gives sum||v_sigma-c_sigma psi||^2<=e.
Both the original cutoff vector and its projection have norm at most1,
so Cauchy--Schwarz yields

```
sum ||v_sigma^2-c_sigma^2 phi||_1 <=2sqrt(e).
```

Restoring the removed mass costs ell. Matching the true sign weights costs
at most the same L1 discrepancy again. Consequently, on the joint
(sign,local-coordinate) space,

```
TV(q, w tensor phi) <= b(delta,eta)
 :=min(1,4r+2sqrt(9r+eta/8)).                          (8)
```

This argument does not divide by a possibly zero projection coefficient.
For a well with w_sigma>=w0>0, its conditional local density has TV distance
at most min(1,b/w0) from phi. Vanishing-weight wells have no such uniform
conditional assertion.

## 4. Balance, actual optimizer and useful explicit proxies

For any finite mean mu=E_p X,

```
|w_+-1/2| <= (|mu|+sqrt(delta))/2.                    (9)
```

This is the triangle inequality applied to E sign X and E X, using
E||X|-1|<=sqrt(delta). Evenness gives w_+=1/2 exactly and needs no mean-error
term. The actual optimizer is even and satisfies eta=0 by(2).
The map x to(sign x,T) is one-to-one off the null point0; thus TV between
two original densities equals TV between their joint laws. The triangle
inequality through fair-sign tensor phi proves the sharper bound

```
TV(p,p_delta) <= min(1,
  8r+2sqrt(9r+eta/8)+6sqrt(r)+(|mu|+sqrt(delta))/2).   (10)
```

For even p omit the last term. Using sqrt(a+b)<=sqrt(a)+sqrt(b), r<=sqrt(r)
and sqrt(delta)<=delta^(1/6) yields(1), its even version, and the approximate-
mean version

```
TV(p,p_delta)<=min(1,21delta^(1/6)+sqrt(eta/2)+|mu|/2). (11)
```

There is also an explicit unconstrained proxy: choose a fair independent sign
S and Z~N(0,1), and set X0=S(1+sZ). Pushing(8) through this map contracts TV,
so balanced p is within b of that two-Gaussian law, with(9)'s term added
when only mean control is available. This proxy does **not** have the exact
prescribed moments and is not asserted to be a feasible optimizer. Its
Gaussian negative-radius tail is included in the pushforward; it is not
silently discarded or renormalized. The moment-exact trial used in(2) is a
different mixture.

## 5. Finite accuracy, products and claim boundaries

For a concrete conservative certificate, take a mean-zero density with

```
0<delta<=10^(-24),       delta I(p)<=4+1/50000000.
```

Equation(1) gives TV<=11/5000. Four independent copies have joint TV at most
44/5000<1/100 by product coupling. More generally n copies cost at most n
times the single-copy TV. A CDF or event probability differs by at most TV;
an observable with |f|<=M differs by at most2M TV. These are finite error
budgets, with a deliberately very small useful parameter window, not claims
of sharp constants or practical moderate-delta performance.

No entropy upper bound follows from TV alone. No high-moment control, sharp
tunneling law, even-sector spectral gap or fixed-delta deficit modulus has
been proved here. The additive endpoint error in(1) cannot be called a bound
that vanishes solely as D->0. K1868's arbitrary sign tilts remain valid:
without balance, the explicit |w_+-1/2| term survives. Thus this positive
result does not erase the negative unrestricted result.

## 6. Reproduction and hostile review

Run the k1870 producer and probe in tests/channel-swings. The producer checks
15 symbolic identities/inequalities and2 dependency pins. The separate Fraction
probe checks208 rational inequalities and8 reporting/dependency conditions;
8 mathematical-input and5 reporting faults fail genuine assertions after a
clean baseline. These checks establish finite algebra and harness detection.
The cutoff, spectral and measure arguments above own the continuum theorem.
No external expert, subagent or formal proof-assistant acceptance is claimed.

Preflight favored quantitative localization over fitting the unknown quartic
Hamiltonian. Hostile review checked the weak zero-extension boundary, every
Young/cutoff factor, the direction of the trial bound, raw versus central
moments, near-empty wells, sign balance, TV under the coordinate map and the
non-feasibility of the simple Gaussian proxy. A first symbolic draft had a
wrong factor in the displayed slack polynomial; the clean baseline rejected
it, and20-7r is the verified factor above. No mutation detection was counted
before that repair. The remaining stronger question is a fixed-delta even or
mean-zero stability modulus with substantially better constants; this needs
a genuine within-well/constraint coercivity theorem, not another use of(1).
