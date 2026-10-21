---
title: "K1886: Sharp support-bounded observation approximation"
status: active_research
doc_type: exploration
scripts:
  - tests/channel-swings/k1886_support_bounded_observation_approximation.py
  - tests/channel-swings/k1886_support_bounded_observation_approximation_probe.py
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact L2 approximation infimum for the fixed conditional observation with source support inside a box; no source-energy, causal or native GU claim
---

# K1886: Sharp support-bounded observation approximation

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
result: sharp target error under a fixed compact source-support region
carrier: K1840 real16 source and real4 target in an open rectangular box in R3 LAYER=toy CHIRALITY=N/A
pairing: Euclidean target L2 and positive source H ON=smooth_compactly_supported_fields
real_structure: real coefficients and real exponential charge duals
grading: compact range versus its bounded-domain Hilbert closure
action_owner: repository-construction -- fixed conservative first-order observation
target: quantitative preparation error and support growth MAP-TYPE=quotient
```

## 1. Question and exact answer

[K1883](k1883-compact-support-observation-range-2026-10-21.md) proves that
all four actual coordinate types satisfy

```
O = sum T_i partial_i + R S1,
S1=24 K T1, K=diag(1,-1,-1,1), rank stack(T_i)=12.
```

On the whole space its compact smooth range is exactly four vanishing
exponential charges. That range is dense in whole-space L2. Density alone
leaves unanswered the error when preparation must remain inside a fixed
bounded region. K1869's spectral energy-budget approximation concerns a
massless wall on R2, not this spatial support constraint in R3.

Let Omega=(-L,L)^3, L>0, kappa=24R and W(x)=exp(kappa K x1).
For any target y in L2(Omega,R4), define

```
q=integral_Omega W(x)y(x) dx,
g=(2L)^2 sinh(2 kappa L)/kappa       if kappa !=0,
g=(2L)^3                           if kappa =0.
```

The quotient is even in kappa and strictly positive. Then

```
inf_{psi in Cc-infinity(Omega,R16)} ||O psi-y||_L2(Omega)
                         = ||q||_R4 / sqrt(g).                 (1)
```

This is an infimum over all compact smooth sources, with no source norm
budget. If y is smooth and compactly supported with q!=0, the infimum is
NOT attained. If y is smooth and compact with q=0, a compact exact lift exists.
For arbitrary L2 y, zero infimum means approximability, not exact smooth
representability.

The result is a quantitative preparation constraint for an internal model.
SC-OP-04 ASSERTS candidate four-field grammar; SC-MAS-01 and SC-CHI-02
ASSERTS a stylized mass/decoupling toy. SC-OP-05 and SC-META-53 remain
UNCERTAIN. These statements do not identify the present matrices with an
actual native full20 operator, injection, pairing or observed domain.
RA-F1, AC-F1, LT-SM8, source, physics-ledger and canon verdicts do not change.

## 2. Lower bound, sharpness and nonattainment

For i=1,...,4 let h_i(x)=W(x)e_i. Integration by parts in K1883 gives
< h_i,O psi >=0 for every admitted compact source. The h_i are orthogonal
in L2(Omega), each of squared norm g. Thus the orthogonal projection of y
onto their span is

```
r_star(x)=W(x)q/g,       z_star=y-r_star.
```

For every z orthogonal to the four h_i,

```
||y-z||^2 = ||q||^2/g + ||z_star-z||^2.                        (2)
```

This proves the lower bound, and also proves uniqueness of the minimizer in
the Hilbert closure. It is not a claim that z_star is a smooth compact target.

To prove sharpness for the actual source class, approximate z_star by smooth
compact z_n in L2(Omega). Their charges tend to zero because h_i are now
bounded-domain L2 vectors. Fix a nonnegative smooth compact bump rho in
Omega, not identically zero, and let

```
v_i(x)=rho(x)e_i / integral_Omega exp(kappa K_ii x1)rho(x) dx.
```

The denominators are positive and Q(v_i)=e_i. Therefore
w_n=z_n-sum_i Q(z_n)_i v_i is smooth compact, exactly charge-zero, and
w_n tends to z_star in L2. K1883's explicit weighted-divergence primitive
lifts each w_n: choose its one-dimensional bumps inside a closed rectangle
strictly contained in Omega and containing the support. Hence w_n=O psi_n
with psi_n smooth compact in Omega. This proves (1), including the passage
from closed-subspace projection to genuinely admissible sources.

If y itself is compact and q!=0, r_star is nonzero on every open boundary
collar in at least one component. Thus z_star cannot be compact in Omega.
Equality in (2) would force O psi=z_star almost everywhere, impossible for
compact psi. This explains why the best error can be approached but never
reached. No claim about the growth of ||psi_n||_H is licensed.

## 3. General rectangles and covariance

For Omega=product_i(c_i-L_i,c_i+L_i), define

```
g0=(2L2)(2L3) sinh(2 kappa L1)/kappa,
G=diag(exp(2 kappa K_ii c1) g0),
```

with g0=8L1 L2 L3 at kappa=0. The exact squared error is
q^T G^-1 q and the residual is W G^-1 q. The same proof applies. Translating
both the target and its preparation box by a in the x1 direction sends
q to exp(kappa K a)q and G to exp(2 kappa K a)G. The error is unchanged.
Moving a box while leaving the target fixed is a different operation.

This is not an assertion for disconnected domains: each connected component
can carry separate constraints. Rectangular geometry is sufficient for the
explicit compact primitive used here; no unproved domain theorem is needed.

## 4. Optimal accuracy versus available support

Fix a compact target y, and let all sufficiently large centered cubes contain
its support. Its q is then independent of L. If q!=0, the exact optimal error
at each L is positive, even though it tends to zero as L grows.

For R=0,

```
error_inf(L)=||integral y||/(2L)^(3/2).
```

Consequently the sharp infimum is at most epsilon exactly when
L >= (||integral y||/epsilon)^(2/3)/2, subject to containing supp y.
At equality only the infimum reaches epsilon: for a nonzero-charge smooth
compact target every actual compact lift has strictly larger error. If the
inequality is strict, the density construction gives a lift below epsilon.

For R!=0, let a=|kappa|. The exact expression is equivalently

```
error_inf(L)=||q|| sqrt(a/2) exp(-a L)
                 / [L sqrt(1-exp(-4a L))].                    (3)
```

Thus it is asymptotic to ||q|| sqrt(a/2) exp(-aL)/L. It is strictly
decreasing: d(log g)/dL=2/L+2a coth(2aL)>0. For aL>=1, replacing the
square-root denominator by 1 or sqrt(1-exp(-4)) brackets the error.
This quantifies K1883's whole-space density mechanism. It neither supplies
an exact compact lift for q!=0 at any finite L nor gives a finite-energy cost.
The zero-mass limit of g is (2L)^3, so there is no discontinuity at fixed L;
the exponential large-box asymptotic is not uniform as R tends to zero.

## 5. Rotating repaired frames and dynamics

At a fixed time use K1879's actual repaired observation
O_theta=U O V^-1, with smooth invertible source frame V and pointwise
orthogonal target frame U. Multiplication by either frame preserves compact
support; U preserves target L2. Hence (1) holds with

```
q_theta(y)=integral_Omega W U^-1 y,
r_theta=U W G^-1 q_theta.
```

This conclusion uses the repaired map and its actual connection. It supplies
no pure-mass rotating lift, and no identification with K1885's still-conditional
factorization question. In the constant unrepaired system, charges of compact
target solutions are conserved by K1883. Therefore a target evolution staying
inside a fixed cube has the same lower error bound there. A moving finite
propagation cone can be enclosed by an expanding cube and then uses (3) with
its actual L(t). This is a preparation approximation bound, not a signalling
speed, causal Green operator, or ability to reset sources during evolution.

## 6. Controls, verification and remaining questions

The producer rechecks the actual four-type matrix factorization from pinned
K1883/K1840/K1836 inputs, computes the Gram integral and its massless limit,
and verifies rectangle/translation and residual formulas. The independent
probe uses different discrete weighted Hilbert spaces to check the universal
projection identity for multiple data and an actual zero-charge compact
polynomial primitive at kappa=0. These finite controls do not replace the
analytic density and compact-lift proof in section2. Coefficient and
normalization faults are checked separately from report/pin faults.

Strongest contrary examples: nonzero-charge compact data have a positive
fixed-box floor but arbitrarily small whole-space error; zero-charge compact
data admit exact lifts; a Hilbert projection generally loses compactness.
No energy, positivity of target components, spectral cutoff, native physical
quotient, novelty or external expert validation is asserted. The next distinct
question is simultaneous fixed support AND source-energy control, which
requires a bounded-domain variational inverse rather than (1) alone.
