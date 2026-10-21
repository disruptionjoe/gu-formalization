---
title: "K1880: Effective three-well Fisher localization in total variation"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit scalar finite-error Gaussian-mixture and conditional-cell TV bounds; no sextic spectral gap, sharp rate or GU claim
---

# A finite error bound for the actual density

Fix k>3 and a density p with raw moments E X²=1, E X4=k,
E X6<=k²+delta, delta>0, and finite Fisher information
I=4 integral |(sqrt(p))'|². Suppose U is a **proved upper bound on delta I**.
K1878 gives qualitative Gaussian profiles. Here localization and the Gaussian
Poincare inequality give explicit errors, without solving the sextic optimizer.

Let r_j=0,+sqrt(k),-sqrt(k), let p_j be the probabilities of their nearest-root
cells, and put A=k+1, a_0=k, a_+=a_-=2k. Define

```
G_p = sum_j p_j N(r_j, delta/(a_j A)).
e = 4 sqrt(delta)/(3k),
0<h<=sqrt(k)/4,  epsilon=13h/(4sqrt(k)),  tau=4e²/h²,
Ebound = U-A² + A²[(1-epsilon)^(-2)-1]
         +2A e(1+sqrt(k)) +4A k tau +40delta/h²,
T = min(1, tau + sqrt(max(0,Ebound)/(2kA))).              (1)
```

Then TV(p,G_p)<=T, with TV equal to one half the L1 distance.
For even p the fixed-weight mixture

```
G_even=(1-1/k)N(0,delta/[kA])
       +(1/[2k])N(+sqrt(k),delta/[2kA])
       +(1/[2k])N(-sqrt(k),delta/[2kA])
```

satisfies TV(p,G_even)<=min(1,T+e(1+sqrt(k))/k).
For k=4, delta=10^-12, U=25.002 and h=10^-4, this upper bound is
strictly below0.022. In particular it applies to the exact even optimizer
using K1876's rigorous value upper bound. This is a conservative finite
accuracy guarantee, not an optimal rate or a computed sextic spectral gap.

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
result: finite-error localization and Gaussian profile estimate from a Fisher upper bound
carrier: real densities with raw moments2=1,4=k>3,6<=k²+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher energy and real L2 square-root distance ON=real_H1_square_roots
real_structure: nonnegative real densities and real moments
grading: small-slack scale and three nearest-root labels
action_owner: repository-construction -- constrained Fisher functional
target: total variation error of actual density and conditional well profiles MAP-TYPE=evaluation
```

## 1. Moment and label control, independent of optimality

[K1870](k1870-fisher-effective-two-well-stability-2026-10-20.md) already
uses cutoff and oscillator estimates for the different fourth-moment endpoint
k approaching1. We reuse that method idea, not its two-well conclusion:
the present sixth-cap endpoint has three wells, unequal slopes and unrestricted
sign weights. K1878 identifies these three profiles but supplies no constants.
No claim of a new general oscillator method or of novelty is made.

Put g=x³-kx and d=distance(x,{r_j}). K1878 proves
`g² >= (9k²/16)d²` everywhere, hence E d²<=e².
For the nearest root R(X), let q=p_++p_-. Cauchy-Schwarz gives

```
|kq-1| = |E(R²-X²)| <= e ||R+X||_2 <= e(1+sqrt(k)).     (2)
```

Here ||X||_2=1 and ||R||_2=sqrt(kq)<=sqrt(k); no symmetry or first
moment is assumed. Also `|E X-sqrt(k)(p_+-p_-)|<=e`.
For even p the outer masses are equal; without evenness, K1878's asymmetric
near-minimizers preclude replacing them by1/(2k). A supplied mean-zero
condition bounds their imbalance by e/sqrt(k) but is not imposed here.

## 2. Smooth localization with its full cost

Choose a nonnegative Lipschitz cutoff chi_j equal to1 on |x-r_j|<=h/2,
zero on |x-r_j|>=h, and equal to
`cos(pi(|x-r_j|-h/2)/h)` in between. Their supports are disjoint and inside
the nearest-root cells. Complete them by
`chi_tail=sqrt(1-sum chi_j²)`. The transition is a sine, so all four
functions are Lipschitz and

```
sum chi²=1,       sum |chi'|² <= pi²/h².
```

With u=sqrt(p), u_j=chi_j u and m_j=||u_j||², the exact IMS product-rule
identity (expand derivatives and use sum chi chi'=0) gives

```
sum_j 4delta ||u_j'||² <= delta I +4pi²delta/h²
                         <= U+40delta/h².               (3)
```

The omitted tail energy is nonnegative. Its mass is at most
`P(d>=h/2)<=4e²/h²=tau`. Thus sum(p_j-m_j)<=tau, with each difference
nonnegative. Since a_j<=2k, (2) implies

```
sum a_j m_j >= A-e(1+sqrt(k))-2k tau.                    (4)
```

All u_j are genuine global H1 functions. We never extend a sharply
conditioned density by zero and incorrectly assign it finite Fisher energy.

For |x-r_j|<=h, expansion at the root gives

```
g(x)/(x-r_j)=g'(r_j)+3r_j(x-r_j)+(x-r_j)²,
|g(x)| >= a_j(1-epsilon)|x-r_j|.                         (5)
```

Indeed the error is at most3sqrt(k)h+h²<=13sqrt(k)h/4 and a_j>=k.
Since epsilon<=13/16<1, (5) and the cap give

```
sum a_j² integral (x-r_j)²u_j² <= delta/(1-epsilon)².     (6)
```

## 3. Oscillator deficit controls density error

For b_j=a_j A and normalized Gaussian square root phi_j of variance
delta/b_j, define

```
E_j=4delta||u_j'||²+(b_j²/delta)||(x-r_j)u_j||²-2b_j m_j.
```

Gaussian Poincare, or the harmonic oscillator gap, gives

```
E_j >= 4b_j ||u_j-<u_j,phi_j>phi_j||² >=0.              (7)
```

To check normalization explicitly, write u_j=phi_j f. Integration by
parts makes E_j=4delta integral |f'|² phi_j². Gaussian Poincare with
variance delta/b_j bounds this below by4b_j Var_(phi_j²)(f), exactly(7).
Cutoff approximation extends this from smooth f to the stated form domain.
The standard input is Gaussian Poincare, not a claim about the sextic
optimizer: see Chafai and Lehec, [Logarithmic Sobolev Inequalities Essentials](https://djalil.chafai.net/docs/M2/chafai-lehec-m2-lsie-lecture-notes.pdf), sections1.3 and2.2.

Because u_j and phi_j are nonnegative, c_j=<u_j,phi_j> lies between0 and
sqrt(m_j). Consequently

```
||u_j-sqrt(m_j)phi_j||²=2m_j-2sqrt(m_j)c_j
 <=2(m_j-c_j²) <= E_j/(2b_j).                            (8)
```

Equations(3),(4),(6) give sum E_j<=Ebound. In particular Ebound is
nonnegative for any valid U; the max in(1) does not license a guessed
energy upper bound. Cauchy-Schwarz and (8) then give

```
sum ||u_j²-m_j phi_j²||_1
 <=2 sqrt(sum m_j) sqrt(sum ||u_j-sqrt(m_j)phi_j||²)
 <=2 sqrt(Ebound/(2kA)).                                (9)
```

The discarded density has mass at most tau, and replacing m_j by p_j in
the Gaussian mixture adds at most tau in L1. Divide the total by2 to
obtain(1). For even p, discrete weight TV is |q-1/k|, bounded by(2)/k.
This proves the main theorem on all feasible densities, not just mixtures.

## 4. Effective consumers and exact limits

**Conditional well shapes.** Every component Gaussian puts at most
`lambda=4delta/(k²A)` outside its own nearest-root cell, by Chebyshev and
its variance at most delta/(kA). Restrict p-G_p to one cell, bound the
other components entering it and its own component leaving, and divide
by p_j>0. This gives

```
TV(law((X-r_j)/sqrt(delta) | cell j), N(0,1/(a_j A)))
 <= min(1,(T+lambda)/p_j).                              (10)
```

The factor1/p_j is essential. A vanishing-mass well has no uniform
conditional guarantee; this agrees with K1878, rather than overwriting it.

**An explicit rate given an energy excess.** For fixed k, choose h=delta^(1/3)
when it meets h<=sqrt(k)/4. If U<=A²+eta, eta>=0, (1) is
`T=O_k(sqrt(eta+delta^(1/3)))`. Thus eta=O(delta^(1/3)) gives
TV=O_k(delta^(1/6)). These exponents are proved upper bounds, not claimed
sharp. The actual even optimizer may use any rigorously established trial
upper bound U; the theorem does not assume a rate for that trial silently.
For the exact optimizer, K1876's analytic moment-matched trial has
U=A²+O_k(delta): its t(delta), weight and delta/t are analytic at zero.
Thus the stated O_k(delta^(1/6)) rate applies to that optimizer, although
this big-O statement alone does not supply a numerical threshold.
At k=4 and the values stated above, the rational verifier uses pi²<10
and proves Ebound<40(0.022-tau-e(1+sqrt(k))/k)².

**Finite accuracy planning.** A requested tolerance t is certified whenever
`tau+sqrt(Ebound/(2kA))+e(1+sqrt(k))/k <= t` for an even density.
This is a computable sufficient condition using a valid U. It can fail to
certify a good density; a failed inequality is not a counterexample to shape.
For a non-even density, use measured/certified cell weights instead.

**Comparison with the exact optimizer.** Let p_star be K1874's exact even
optimizer at the same k,delta. If p is even, its certified U also bounds
delta I(p_star). Both densities are within B=min(1,T+e(1+sqrt(k))/k)
of G_even, so TV(p,p_star)<=min(1,2B). The finite example gives a strict
0.044 bound for every such even competitor with delta I<=25.002.
This bound includes an endpoint localization error; it does not tend to zero
as the energy deficit tends to zero at fixed delta. It is therefore not a
fixed-delta spectral stability modulus. Without evenness, the actual cell
weight discrepancy must be retained; asymmetric near-minimizers prohibit
silently applying the balanced conclusion.

**Observables and products.** For |f|<=1, expectation error is at most2T;
for events it is at most T. Product measures have TV at most the sum of
component bounds by telescoping. No independence is inferred for a joint
physical model. These consumers require no sextic coefficients.

**Unscaled transport.** Coupling X to its nearest root proves W2(p,atomic
cell measure)<=e. Coupling each Gaussian to its center gives
`W2(p,G_p)<=e+sqrt(delta/(kA))`. This unscaled concentration estimate
is not an effective W2 estimate for the rescaled conditional profiles.
K1878's latter convergence remains qualitative. No global multiwell
Poincare gap or tunneling estimate follows from the three local oscillator
gaps used in(7).

## 5. Verification and remaining task

The producer checks exact identities and the finite rational budget.
A separate probe reconstructs localization/weight/allocation inequalities,
oscillator eigenfunctions and contrary controls, with coefficient faults
separated from reporting/pin faults. Continuum inequalities above carry the
all-density theorem; finite sampling is only a check. No external expert or
proof assistant is claimed. This is exploratory independent mathematics,
without novelty, native GU identification or source/ledger/canon change.
Next quantitative questions are sharper rates, effective rescaled W2, and
actual sextic spectral/entropy stability; this result does not settle them.
