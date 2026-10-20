---
title: "K1837: rare-component Fisher boundary and uniform amplitude exclusion"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite separation exclusion and all-domain outward variance bound; inward divergent separation and global optimizer powers remain open
---

# A whole rare-component endpoint regime loses to the merging family

Write delta=2-q and s=sqrt(delta). For z=b s and c=k s³ with fixed b>0,
k>=0, the two-radius Fisher value has the rigorous expansion

```
J=4/delta-3/2-2bk+4H(b)k²+o(1),
H(b)=(exp(b²)-1-b²)/b².                             (1)
```

Optimizing over k gives a constant strictly larger than-2. A uniform argument
also excludes unbounded k whenever b stays in a fixed positive compact
interval. The opposite rare-atom orientation has +2bk instead and cannot
improve the Rademacher constant-3/2. Thus no exact global minimizer has a
finite positive accumulation value of either z/sqrt(delta) or
(c/z)/sqrt(delta). A further exact variance bound proves (c/z)=o(sqrt(delta))
and eventual r-z<c/2, with r=c/z, for every global minimizer. This does not yet
prove K1835's compact a,b scaling or global uniqueness.

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
result: uniform rare-component Fisher expansion and endpoint scale exclusion
carrier: symmetric unit-variance two-radius Gaussian mixtures near delta=2-q=0 LAYER=toy CHIRALITY=N/A
pairing: Fisher score integral with Gaussian likelihood moments ON=real_observation_line
real_structure: positive real densities; one-sided rare mixture weights
grading: asymptotic noise and radius scales; no physical grading
action_owner: repository-construction -- scalar constrained Fisher functional
target: competing endpoint parameter regimes MAP-TYPE=evaluation
```

## 1. Same constrained chart and exact likelihood identity

Use K1833's chart

```
t=sqrt((2-delta)/(2-c)), v=1-t, p=c/(c+z²),
A=sqrt(1-z) with probability p, sqrt(1+c/z) with probability1-p,
Y=eta sqrt(t) A+sqrt(v) Z, J=I(Y)-1.
```

The sign eta is fair, Z is standard Gaussian, and both are independent.
E Y²=1 and E Y4=1+delta exactly. All results below are GU-independent
mathematics; no source action, observable or physics ledger row moves.
K1831 proves c=o(delta) for global minimizers, and K1833 proves their
value4/delta-2+o(1), z->0. K1835 provides a sharper upper bound but does
not exclude the rare regimes considered here.

First remove the symmetric sign and translate the dominant positive mean to
zero, then divide by sqrt(v). The positive-lobe density is

```
f(x)=phi(x)[1+p(L(x)-1)], L(x)=exp(d x-d²/2),
d=sqrt(t)[sqrt(1-z)-sqrt(1+c/z)]/sqrt(v).
```

Its score is -x+pdL/[1+p(L-1)]. Since E_phi L=1 and E_phi xL=d,
exact integration gives

```
I(f)=1-pd²+p²d² F(p,d),
F(p,d)=E_phi[L²/(1+p(L-1))].                        (2)
```

This identity does not Taylor-expand the likelihood uniformly in x.
Gaussian completion of the square gives E_phi L^j=exp(j(j-1)d²/2), hence

```
|F(p,d)-exp(d²)|
 <= p/(1-p) [exp(3d²)+exp(d²)], 0<=p<1.             (3)
```

Indeed 1+p(L-1)>=1-p and |L-1|<=L+1. Formula(3) is uniform for d in
any fixed bounded interval. It gives a controlled integral expansion even
though the likelihood is unbounded in a tail. The Gaussian score/MMSE
identity is classical; see Guo, Shamai and Verdu,
[Gaussian-channel information and estimation](https://arxiv.org/abs/cs/0412108),
and Guo, Wu, Shamai and Verdu,
[MMSE properties](https://arxiv.org/abs/1004.3332).
The direct proof(2)-(3) is the actual argument used here; no novelty claim.

## 2. Fixed and compact moving parameters

Set z=b s,c=k s³. Uniformly for b in[epsilon,M] and k in[0,K],

```
p=(k/b²)s+O(s²), d²=b²+O(s),
(1-pd²)/v=4/s²-1/2-2bk-4k²-4k²/b²+O(s),
p²d²/v=4k²/b²+O(s).                               (4)
```

These follow by expansion of the actual square roots and are verified exactly
in the producer and independently by binomial coefficients. Combine(2)-(4)
and subtract1 to obtain(1), with O(s) error uniform on those compact sets.
For k=0 the rare atom disappears and the formulas extend continuously.

Passing from a positive lobe to Y costs a flat cross-sign Fisher deficit.
For these parameters all positive component means tend to1 and v~s²/4.
The exact two-mixture deficit is bounded by a polynomial in v^-1 times the
cross-sign Gaussian affinities. Opposite means stay separated by a fixed
positive amount, so the difference is O(s^-N exp(-a/s²)) for some a>0.
Thus(1) is an expansion of the full symmetric Fisher integral, not only a
single lobe or a sampled quadrature.

Since H(b)>b²/2 for every b>0, completing the square yields

```
k_*(b)=b/(4H(b))=b³/[4(exp(b²)-1-b²)],
min_k>=0 [-3/2-2bk+4H(b)k²]
 =-3/2-b4/[4(exp(b²)-1-b²)] > -2.                  (5)
```

Strictness is the positive exponential-series remainder beyond b4/2.
It is uniform on[epsilon,M]. The gap above-2 is
b²/6-b4/72+O(b6) as b->0. This explains why this exclusion cannot simply
be extended uniformly to b=0: its gap collapses precisely at the merging
boundary. The optimal k then diverges as1/(2b), and matching formal powers
alone is not a proof through that joint limit.

## 3. Released follow-through: unbounded amplitudes are excluded too

A bounded-k statement would leave a real loophole. Suppose b stays in
[epsilon,M], c=o(delta), and define lambda=c/delta=k s->0. Now use
(s,lambda,b) as the small-parameter chart. Its exact quantities satisfy

```
p=lambda/(lambda+b²),
v=s² vbar(s,lambda), vbar(0,lambda)=(1-lambda)/4,
d(0,lambda)=-(b+lambda/b)/sqrt(1-lambda).
```

After removal of their displayed s factors, the square-root quantities are
analytic with bounded derivatives in a fixed neighborhood of(s,lambda)=0,
uniformly in b. Formula(3) is uniform there. The leading coefficient of
(1-pd²)/v at order s^-2 is exactly

```
4(1-2lambda-lambda²/b²)/(1-lambda)²
 =4-4(1+1/b²)lambda²+O(lambda³).                   (6)
```

Its linear lambda coefficient vanishes; this cancellation is essential.
The coefficient at order s^-1 is -2b lambda+O(lambda²), and the bounded
term tends to-1/2. Also the likelihood correction at leading order is
4 exp(b²)lambda²/(b² s²)+O((lambda³+s lambda²)/s²).
Taylor remainders and(3), with lambda=k s, therefore give

```
J-4/s²=-3/2-2bk+4H(b)k²+R,
|R| <= C [s+lambda+s k²+lambda k²].                (7)
```

One may enlarge C on the fixed compact b interval. Cross-sign error remains
flat because vbar is bounded above and below and both means tend to1.
Equation(7) is equivalently R=o(1+k²) along every such sequence. It does
not require k bounded, and no uniform assertion is made for b diverging.

If J-4/s² is bounded above, H has a strictly positive minimum on the
interval. For k->infinity, the positive quadratic term in(7) dominates the
linear term and the o(k²) remainder, a contradiction. Thus k is bounded.
Now the compact expansion(1) and the uniform gap(5) apply. In particular,
no global minimizer, or any sequence with J=4/delta-2+o(1), can have b in
that fixed interval along a sequence tending to the endpoint.

## 4. The opposite rare orientation and remaining scale alternatives

Set the upper squared-radius displacement c/z=b s instead, with c=k s³;
then z=k s²/b and the rare upper weight is z²/(c+z²). Translate the now
dominant lower mean. The identical likelihood argument gives

```
J=4/delta-3/2+2bk+4H(b)k²+o(1).                    (8)
```

The same uniform amplitude bound(7), with +2bk, holds. Here the minimum
over k>=0 is-3/2, at k=0; there is no inward-skew gain. This is a useful
contrary control on signs, not a relabeling that could erase the distinction
between lower and upper radii in the original fourth-moment chart.

For exact global minimizers, c/delta->0. If z/s has a finite positive
subsequential limit, (c/z)/s tends to0 and sections2-3 apply. If (c/z)/s
has a finite positive limit, z/s tends to0 and(8) applies. Both contradict
the sharp global constant. Hence neither scaled displacement has a finite
positive accumulation point. This by itself would leave a divergent rare
separation on either side. The following structural bound removes the entire
outward case, without extending the nonuniform likelihood remainder.

## 5. Further structural resolution: the upper displacement is o(sqrt(delta))

Put r=c/z, a=sqrt(1-z), b=sqrt(1+r), and L=a+b. These a,b are
unscaled radii and distinct from the separation parameter b in sections2-4.
The exact positive-lobe variance is

```
Var(A)=c/L², S=Var(Yplus)=1-t(1-c/L²).
```

Let h=r-z. Direct algebra gives

```
(1-c/L²)²-(1-c/2)
 = c [L4-4L²+2c]/(2L4),
L4-4L²+2c=2h L²-h²-2c.                             (9)
```

Since L²=2+h+2sqrt(1+h-c)>=2+h, whenever h>=c/2 the last numerator
is at least4h+h²-2c>=0. Both square-root sides are positive. Consequently

```
(1-c/L²)/sqrt(1-c/2)>=1,
S<=1-sqrt(1-delta/2)=v0, I(Yplus)>=1/S>=1/v0.        (10)
```

The middle inequality is the usual score Cauchy--Schwarz variance bound.
This is exact and applies even when r is unbounded; no small rare-weight
series is used. To transfer it to Y uniformly, use the already-proved z->0
for global minimizers. Every positive mean is then at least1/2, and v<=v0.
For opposite-sign components i,j let their mean separation be D_ij>=1.
The Fisher loss from forgetting the sign equals the conditional variance
of the two posterior means divided by v². Conditional Jensen bounds that
variance by the sum over opposite-sign atom pairs. Gaussian affinity and
rho>=2sqrt(w_i w_j phi_i phi_j) bound each integrated contribution by

```
(1/2) sqrt(w_i w_j) D_ij² exp(-D_ij²/(8v)).
```

For small v, this is at most a fixed constant times exp(-1/(16v)),
uniformly for ALL D_ij>=1, including unbounded radii. There are only four
opposite-sign pairs. Thus the full loss is bounded by
C v^-2 exp(-1/(16v))<=C v0^-2 exp(-1/(16v0))=o(1).
Combining with(10), every candidate satisfying h>=c/2 on such a minimizing
sequence has

```
J>=4/delta-3/2-o(1),
```

contradicting the attained constant-2. Therefore every exact global minimizer
satisfies, eventually,

```
r-z<c/2=zr/2, hence r<z/(1-z/2).
```

Multiplying by r and using c=zr gives r²<c/(1-z/2)=o(delta), by K1831.
We have proved **r=c/z=o(sqrt(delta))**. This conclusion also applies to
additively optimal sequences for which the inherited merging conclusion z->0
holds; the global-minimizer claim needs no extra assumption.

Only the inward displacement z can now have a divergent noise-scaled limit.
Finite positive z/sqrt(delta) limits are excluded by sections2-3. Remaining
subsequences have z/sqrt(delta)->0 or infinity, with r/sqrt(delta)->0 in
either case; oscillation is not ruled out. The divergent inward case needs
a uniform lower bound beyond(3), whose exponential constants grow. The
both-o(sqrt(delta)) case still contains noncompact K1835 parameters and needs
uniform cumulant coercivity. No next global coefficient, actual optimizing
powers, uniqueness, effective onset or finite-budget bound is claimed.

## 6. Evidence and hostile review


```
sage -python tests/channel-swings/k1837_fisher_rare_component_boundary.py
sage -python tests/channel-swings/k1837_fisher_rare_component_boundary_probe.py
```

The producer verifies the constrained chart constants in both orientations
over a rational function field, the exact likelihood remainder and square
completion. The separate probe derives the score identity by algebra,
computes Gaussian likelihood moments by completing squares, and reconstructs
chart coefficients independently from low-order binomial expressions. It
checks the zero linear lambda term, gap series and strict positive exponential
remainder. Separate exact controls verify the two-point variance, threshold
factorization and sign condition in(9)-(10). Reporting-fault tests are separate. The uniform remainder proof
and amplitude coercivity in sections1-4 are analytic evidence, not consequences
of assertion counts. No old fixed-q bank was replayed.

Inline hostile review checked I versus J, p versus1-p, the rare inward sign,
noise-scaled gap versus squared-radius displacement, lambda=k s, uniformity
when k diverges, the full two-lobe correction the nonuniform b->infinity
limit, and the replacement of that invalid extension by the uniform
opposite-sign affinity and exact variance argument. No unresolved issue in the stated scope; no separate-agent review,
canon promotion, source/ledger change or scientific novelty claim.

Next compare an unbounded-separation polynomial-score lower bound with a
uniform small-displacement cumulant bound. Both must control the actual
Fisher integral before importing K1835's unique window branch. The strongest
independent source-facing alternative is the local differential observation
and coefficient identification in K1836, which remains conditional as well.
