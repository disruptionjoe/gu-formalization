---
title: "K1856: Above Gaussian kurtosis the Fisher infimum is unattained"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all-density phase classification and explicit tail and moment-cap bounds; no GU physics or novelty
---

# Above Gaussian kurtosis the Fisher infimum is unattained

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
result: exact tail construction, nonattainment, complete moment phase diagram and quantitative compactness obstruction
carrier: real probability densities with raw second moment1 and prescribed fourth moment LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial degree only; no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: unrestricted density problem on the real line MAP-TYPE=evaluation
```

## 1. Result and prior context

For densities p with E X²=1 and E X4=k define F(k)=inf I(p), where
I(p)=4 integral |(sqrt p)'|² and I=infinity outside H1. Moments are raw
about the stated origin; no mean-zero assumption is needed. With inf(empty)
=infinity, the complete classification is

| Fourth moment | Value and attainment |
| --- | --- |
| k<=1 | No density is feasible; F=infinity. |
| 1<k<3 | F>1, attained by the unique positive even quartic ground-state density. |
| k=3 | F=1, attained only by the standard Gaussian phi. |
| k>3 | F=1, but no density attains it. |

The middle open interval is reused from [K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md),
with unrestricted uniqueness established in K1851. The new point is the
entire k>3 regime and its consequences. A quartic Euler equation does not
produce a minimizer there. Extending the sub-Gaussian spectral branch across
k=3 would miss noncompactness. This is GU-independent mathematics.
Moment-constrained Fisher minimization already has a substantial literature,
including [Vignat and Bercher, 1998](https://www.sciencedirect.com/science/article/abs/pii/S0165168497002259).
Only its indexed topic/abstract is used here; no theorem or novelty claim is
attributed to unavailable full text. The following argument is self-contained.

## 2. Exact feasible escaping-tail sequence

Fix c=(k-3)/3>0. For any 0<t<1 let

```
v=1-t,  w=1+c/t,  epsilon=t²/(c+t²),
p_t=(1-epsilon) N(0,v)+epsilon N(0,w).                 (1)
```

Both variances and both weights are strictly positive. Exact identities give

```
(1-epsilon)v+epsilon w=1,
(1-epsilon)v²+epsilon w²=1+c,
E_(p_t) X4=3(1+c)=k.                                  (2)
```

Fisher convexity, or conditional expectation of the component score, yields

```
1 <= I(p_t) <= (1-epsilon)/v+epsilon/w
             =1+c t/[(1-t)(c+t)] ->1.                 (3)
```

The lower bound is Cauchy-Schwarz applied to E[X rho(X)]=-1, justified
by cutoff integration by parts, where rho=2(sqrt p)'/sqrt p on its nonzero
set. Its equality case requires rho=-x almost everywhere in p. Equivalently
u'+xu/2=0 weakly for u=sqrt p, whose normalized nonnegative solution is
sqrt(phi). Thus I=1 forces fourth moment3, excluding attainment for k>3.
The same identity proves Gaussian uniqueness at k=3. Jensen E X4>=
(E X²)²=1 excludes k<1; equality at k=1 forces support on {minus1,plus1},
which cannot be a density. No symmetry assumption has entered the lower bound.

The right side of (3) is an upper bound, not the exact mixture Fisher value.
The sequence is smooth, positive and even. Tiny mass with very large variance
is sufficient; fitting extra quartic stationary states is unnecessary.

## 3. Executed consequence: strong shape convergence with fourth-moment loss

[K1855](k1855-fisher-gaussian-endpoint-2026-10-20.md) gives for every
raw-second1 finite-Fisher density, with h=sqrt(p/phi),

```
E_phi h²=1,   4 E_phi |h'|²=I(p)-1,
TV(p,phi)<=sqrt(I(p)-1)/2.                              (4)
```

Hence **every** sequence at fixed k>3 with I->1 tends to phi in TV and its
h tends to1 in Gaussian H1. Poincare gives 1-(E_phi h)²<=E_phi|h'|²;
nonnegative h and normalization then give strong L2 convergence as well.
Second moments are exactly equal to the limiting Gaussian second moment,
so weak convergence plus moment convergence also gives W2 convergence.
This is compatible with failure of fourth-moment convergence.

For any such sequence, and each fixed R, TV convergence applies to the
bounded test x4 1_(|x|<=R), so

```
lim_n integral_(|x|>R) x4 p_n = k-integral_(|x|<=R) x4 phi,
lim_(R->infinity) lim_n integral_(|x|>R) x4 p_n = k-3>0. (5)
```

Thus its fourth moments are not uniformly integrable and it cannot converge
in W4. The order of limits in (5) matters. No contradiction with TV or W2
convergence exists: these do not control a fourth-power observable.
For the explicit sequence, epsilon w²->c and epsilon w³ diverges like c²/t;
the disappearing component carries fourth-moment excess3c. For every
0<r<4 its r-th absolute tail contribution tends0, while at r=4 it does not.
For r>=1 below4 this and weak convergence imply W_r convergence.

## 4. Executed consequence: an explicit higher-moment cap restores a gap

Suppose in addition E|X|^s<=M for some s>4, and let m_s=E_phi|Z|^s.
Write d=TV(p,phi), C=M+m_s, and Delta=|k-3|>0. For every R>0,

```
Delta <= 2 R4 d + C/R^(s-4).                            (6)
```

Split the fourth-moment difference at R. The bounded part is at most
R4 integral |p-phi|=2R4 d; bound each tail fourth moment by its s-th
moment/R^(s-4). Choose R=(2C/Delta)^(1/(s-4)). Then

```
I(p)-1 >= 4d² >= (Delta²/4) [Delta/(2C)]^(8/(s-4)).      (7)
```

In particular a sixth-moment cap M gives

```
I(p)-1 >= |k-3|^6/[64(M+15)^4].                         (8)
```

This conservative explicit bound proves that any fixed higher-moment cap
forbids the vanishing-cost sequence at k>3. It is a genuine quantitative
obstruction, not a claim that the constrained minimum is attained. A bound
on an s-th moment alone does not guarantee its own equality constraint is
closed. Equations (6)-(8) apply also for k<3 but are much weaker there than
K1855's rational dual. The same proof works with an explicitly supplied
uniform fourth-tail modulus instead of a power moment.

## 5. Scope, controls and next question

The full curve is strictly convex and decreasing on (1,3), then flat on
[3,infinity); strict convexity does not extend to the nonattained branch.
K1855 gives left slope0 at3; the right flat branch has slope0. These are
value statements, not differentiability of an optimizer across3. K1854's
k1 endpoint, both budget laws and all restricted-family claims are unchanged.

Run `sage -python tests/channel-swings/k1856_fisher_tail_phase.py` and
`python3 tests/channel-swings/k1856_fisher_tail_phase_probe.py`. Exact
algebra checks normalization, moments, reciprocal-variance bound, escaping
moments and the sixth-moment inequality constants; separate Fraction controls
challenge the construction and planted input/reference faults. The continuum
claims rely on the weak-score equality argument, Gaussian Poincare and the
explicit limit passages above, not on sampled controls. Inline hostile review
checks density versus atom feasibility, exact versus bounded mixture Fisher,
raw versus centered moments, tail orders and inequality direction. No separate
person, proof assistant, external acceptance or novelty is claimed.

A useful successor is an effective compact-tail optimizer theorem with an
explicit tail modulus. It must not assume the equality moment class is compact
merely because one particular approximating family is well behaved.
