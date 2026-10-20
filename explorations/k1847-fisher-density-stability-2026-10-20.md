---
title: "K1847: certified Fisher score error controls density distance"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit reference-density total variation bound only; no GU physics or identification with the exact optimizer
---

# The Fisher score certificate gives an explicit density-distance theorem

K1845's rational score defines a positive normalized reference density pi on
the entire real line. An elementary tail bound and the one-dimensional Stein
identity prove

```
d_TV(p,pi) <= (91/24) sqrt(J_g(p)),
J_g(p)=integral (2u'+g u)², p=u².                            (1)
```

For every feasible even density with variance1, fourth moment2, and
`I(p)<=U=1.752673`, the previous certificate implies

```
d_TV(p,pi) < 637/4800 < 0.133.                              (2)
```

This includes the unique unrestricted minimizer p*. The reference pi is
specified explicitly by a rational-score integral; it is **not** asserted to
have the prescribed moments or to equal p*. The inequality supplies the
missing density control in the preceding score certificate without assuming
convexity of its double-well reference or a numerical spectral gap. It does
not quantify the restricted-family improvement or determine endpoint scaling.
A released spectral argument also gives a vanishing true-optimum bound
with the positive, as yet unevaluated, quartic spectral gap. The explicit
reference constant is conservative; the purpose is a certified conversion, not
more digits in F(2). No GU physics, novelty or external acceptance is claimed.

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
result: explicit total-variation control from the rational-score certificate and near-optimizer diameter bound
carrier: real probability densities p=u² with u in H1(R) and finite second moment LAYER=toy CHIRALITY=N/A
pairing: L2(dx) square-root derivative norm and L2(p dx) relative score ON=real_Sobolev_functions
real_structure: real nonnegative density; positive even reference
grading: none; polynomial degree only
action_owner: repository-construction -- scalar Fisher functional
target: total variation between a density and an explicit score-reference probability law MAP-TYPE=evaluation
```

## 1. Reference and exact global shape bounds

Reuse K1845's exact coefficients, not rounded fitted data:

```
N(y)=-26379/25000+(12003/10000)y+(137193/500000)y²,
D(y)=1+(266879/500000)y+(43447/2000000)y²,
g(x)=x N(x²)/D(x²),
V(x)=integral_0^x g(t)dt,
pi(x)=exp(-V(x))/Z, Z=integral_R exp(-V(x))dx.
```

D>0 on y>=0, and N is strictly increasing there with N(0)<0<N(1).
There is one r in(0,1) with N(r²)=0. V is even, decreasing on[0,r] and
increasing on[r,infinity). The following exact polynomial facts hold:

- every coefficient of `N+(11/10)D` is positive;
- every coefficient of `(N-D)(y+9/4)` is positive.

Hence `g(x)>=-11x/10` for x>=0 and `g(x)>=x` for x>=R=3/2.
The total decrease of V is at most11/20. For any0<=x<=y,
`V(x)-V(y)<=11/20`. For y>=R, `V(y)-V(R)>=(y²-R²)/2`.
These prove integrability and positivity of Z and all reference moments;
no quadrature, log-concavity or normalization estimate is imported.
They also prove g has at most linear growth and g' is bounded, as is clear
from the rational degrees and D>0. Its slope at the origin is negative, so
uniform strict log-concavity would be a false premise.

## 2. Tail-to-density ratio and Stein factor

For x>=0 put

```
T(x)=(integral_x^infinity pi(y)dy)/pi(x)
    =integral_x^infinity exp(V(x)-V(y))dy.
```

If x>=R, the tail inequality gives
`T(x)<=integral_x^infinity exp(-(y²-x²)/2)dy<=1/x<=2/3`.
The second step follows from `(y²-x²)/2>=x(y-x)`.
If0<=x<=R, split at R and use the maximum decrease11/20:

```
T(x) <= exp(11/20) (R-x+1/R)
     < (7/4)(3/2+2/3) =91/24.                              (3)
```

The rational Taylor sum through degree8 with geometric bound on the remaining
positive terms certifies `exp(11/20)<7/4`. Symmetry handles x<0 with the lower
tail. This is a complete line bound, not a finite-grid estimate.

Let F be the CDF of pi and h an indicator of any measurable set. The bounded
solution of the density Stein equation is

```
f_h(x)=pi(x)^-1 integral_(-infinity)^x (h(y)-E_pi h)pi(y)dy,
f_h'-g f_h=h-E_pi h.
```

Splitting conditional expectations on either side of x proves
`|f_h(x)|<=F(x)(1-F(x))/pi(x)`; the difference of the two conditional
probabilities is at most1. In particular(3) and symmetry yield
`||f_h||_infinity<=91/24`. This step works for arbitrary measurable sets,
not just half-lines, so the result is total variation rather than only CDF
error. Total variation is `sup_A |P(A)-Pi(A)|=1/2 integral|p-pi|`.

## 3. Weak score identity including zeros of p

For p=u², u>=0 in H1 and finite second moment, J_g is finite because g has
linear growth. Using the Stein equation and integration by parts,

```
E_p h-E_pi h = - integral f_h (2u'+g u)u.
```

To justify this without positivity of p, first use compact cutoffs. Bounded
f_h and `p'=2u u' in L1` control the derivative term; `f_h'=g f_h+h-E_pi h`
has at most linear growth, hence is integrable against p. The cutoff derivative
error is bounded by a constant times the probability tail and vanishes. Smooth
approximation or the absolutely continuous Stein solution admits measurable h.
Cauchy--Schwarz and integral u²=1 now give(1). No division by p at its zeros
is needed. For positive smooth p, J_g is the familiar
`E_p[(p'/p+g)²]`.

The method is classical; see [Ley and Swan, Stein's density approach and
information inequalities](https://arxiv.org/abs/1210.3921). Here the explicit
rational tail certificate supplies a usable constant for this particular
non-log-concave reference; no general novelty is claimed.

## 4. Execute the consuming bound and its consequences

K1845 proves on the declared moment class

```
I(p)-L = J_g(p)+E_p[P(X²)/D(X²)²],
L=875729/500000, P(y)>0 for y>=0.
```

For finite-Fisher p, strict positivity of P gives J_g(p)<I(p)-L. Therefore
I(p)<=U implies `J_g(p)<U-L=243/200000<(7/200)²`, which inserted into(1)
gives(2). For an energy tolerance eta>=0,

```
I(p)<=U+eta  => d_TV(p,pi) <= min(1,(91/24)sqrt(243/200000+eta)).  (4)
```

The exact p* exists by K1843 and has I(p*)<U. For two feasible densities
p,q with energy<=U, the triangle inequality supplies
`d_TV(p,q)<637/2400<0.266`. Thus any certified feasible near-minimizer is
within that bound of p*. More generally replace the two terms by their
individual square-root energy bounds in(4). These are coarse but rigorous
shape-diameter controls; they are not a theorem that distance to p* tends to
zero at the rate sqrt(I(p)-F(2)), since the fixed dual/primal gap remains.
The following released consequence supplies that vanishing modulus implicitly;
its effective numerical constant is a separate spectral enclosure problem.

For every event A, the probability error against pi is bounded by(2).
For any bounded observable h, the expectation error is at most
`2||h||_infinity d_TV`. These do not control unbounded moment errors without
additional tail estimates. In particular the result must not be used to
assert pi's variance or fourth moment is exactly correct, or to silently
replace the true optimizer by pi in a constrained calculation.

## 4a. Released consequence: stability relative to the actual optimizer

The gap exists already in K1843's variational characterization; it need not
be assumed as an additional physical or numerical input. For any fixed k in
(1,3), let u*=sqrt(p*) be its unique positive normalized even minimizer and

```
H=-4 d²/dx²+a x²+b x4, b>0, H u*=E0 u*.
```

The confining quartic has compact resolvent on its form domain
`H1(R) intersect L2(x4 dx)`: on bounded intervals use Rellich compactness,
and outside them the growing potential controls L2 tails. A lower constant
shift makes the form coercive. The simple positive ground state and compact
resolvent imply a strictly positive gap gamma_k to the next eigenvalue in the
even subspace. This is not necessarily the full-space first excited gap;
using the smaller full-space gap would also be valid. Its numerical size is
not supplied by K1845's ground-energy bracket.

For any feasible even p=u², u>=0, its fixed moments give exactly

```
Delta=I(p)-F(k)=<u,(H-E0)u>.
```

Write u=c u*+v, v perpendicular to u*. Both square roots are nonnegative,
so0<=c<=1 and ||v||²=1-c². The spectral theorem gives
`Delta>=gamma_k(1-c²)`. Cauchy--Schwarz applied to
`|u²-u*²|=|u-u*||u+u*|` gives the sharper probability estimate

```
d_TV(p,p*) <= sqrt(1-c²) <= min(1,sqrt(Delta/gamma_k)),       (5)
||sqrt(p)-sqrt(p*)||² <= 2 Delta/gamma_k.                    (6)
```

This is a true vanishing stability modulus for each fixed k, not only a
coarse diameter around a convenient reference. It is non-effective until a
lower bound on gamma_k for the **actual moment-selected** quartic is proved.
No optimizer coefficients from a fitted or merely feasible dual are substituted.
In particular a low residual for K1845's rational-score reference does not
identify gamma_k or prove its value by an eigenvalue grid.

The same decomposition also controls Sobolev convergence. Put
`a_-=max(-a,0)` and `C=a_-²/(2b)`. Pointwise
`a x²+b x4 >= (b/2)x4-C`. For w=u-u*, the ground-state form identity yields
`<w,Hw>=Delta+E0||w||²`, hence

```
4||w'||²+(b/2)||x² w||² <= Delta+(E0+C)||w||².              (7)
```

Here E0+C>=0 follows from the lower form bound. Combining(6),(7) proves
strong H1 and weighted L2(x4 dx) convergence of every feasible minimizing
sequence. This closes qualitative shape stability without assuming that
fourth-moment equality survives arbitrary weak limits. The equality constraints
enter the exact energy identity before the gap is applied. For approximate
moments that identity gains `a(E X²-1)+b(E X4-k)` and must be changed; (5)
may not be copied unchanged.

## 5. Review, reproduction and remaining question

Run `sage -python tests/channel-swings/k1847_fisher_density_stability.py`
and `python3 tests/channel-swings/k1847_fisher_density_stability_probe.py`.
The producer verifies exact polynomial shape/tail certificates, the exponential
bound, square completion and constants. The independent probe rederives the
polynomial inequalities with Fraction arithmetic, checks positive/negative
fixtures and analytic Gaussian controls for the score identity, and corrupts
the certificate inputs. It does not import the producer. Manifest truth flags
are reporting checks only; finite tests do not replace the weak integration
and all-measurable-set argument above. K1845's whole-line Sturm/primal proof
is reused by exact dependency hash, not counted as newly rerun.

Inline hostile review found and fenced the main hazards: a reference with
wrong moments is not the optimizer; nonconvexity precludes a blanket strongly
log-concave inequality; a CDF estimate alone is weaker than total variation;
finite score bounds alone do not imply a vanishing true-optimum modulus;
the separate exact moment/ground-state identity supplies it in section4a. No
independent-agent or proof-assistant verification is claimed.

Next useful scalar work is a certified numerical lower bound for gamma_k,
a quantitative restricted-family gap at the same k, or a genuinely uniform
unrestricted endpoint theorem. Improving this conservative constant alone does
not close those questions. The fixed named-k Fisher value remains the K1845
interval and source/ledger/canon stay unchanged.
