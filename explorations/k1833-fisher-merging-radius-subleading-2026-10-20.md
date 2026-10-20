---
title: "K1833: the sharp additive Fisher endpoint constant and merging minimizers"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp additive asymptotic and qualitative interior/merging shape for the two-radius scalar family; no unique shape, effective onset or physical interpretation
---

# The global value is 4/delta minus2, up to a vanishing error

For K1825's symmetric unit-variance two-radius Gaussian-channel family,
with delta=2-q decreasing to0,

```
V(2-delta)=4/delta-2+o(1).                             (1)
```

Every global minimizer has z->0 and is in the regular interior for all
sufficiently small delta. Thus the central-atom face z=1 is eventually
excluded. An explicit merging-radius family attains the sharp additive
constant; this does not select a unique minimizer or its actual rates.
K1831's leading criterion c=o(delta) remains necessary and sufficient for
ratio optimality, while the present result distinguishes additive optimality.

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
result: sharp additive global endpoint asymptotic, explicit attaining sequences and eventual interior minimizers
carrier: symmetric unit-variance two-radius Gaussian channels with delta=2-q decreasing to0 LAYER=toy CHIRALITY=N/A
pairing: ordinary and relative Fisher information, centered Gaussian density expansion and weak score test ON=real_observation_line
real_structure: positive real densities and real scalar moments
grading: endpoint powers and asymptotic error orders; no physical grading
action_owner: repository-construction -- moment-constrained Fisher functional, not a source action
target: global scalar minimum and every choice of its minimizers MAP-TYPE=evaluation
```

## 1. Chart and inherited facts

Use exactly the chart of K1831:

```
p=c/(c+z²), A=sqrt(1-z) with weight p,
A=sqrt(1+c/z) with weight1-p,
t=sqrt((2-delta)/(2-c)), v=1-t,
Y=eta sqrt(t) A+sqrt(v) Z, 0<=c<delta, 0<z<=1.
```

Here eta is an independent uniform sign and Z is standard Gaussian.
E Y²=1 and E Y4=1+delta. Write I=int rho'^2/rho and J=I-1.
K1825 proves boundary-inclusive existence, with its artificial z=0 face
dominated by the c=0 competitor. K1827 proves delta V->4. K1831 proves
for every ratio-optimal sequence c=o(delta), v/delta->1/4 and
2(|Y|-1)/sqrt(delta)->N(0,1) in W2. K1829 proves c=0 is not locally
minimizing near the endpoint. These results are reused, not recomputed.
The present result is independent mathematics; no GU row or source grade moves.

## 2. A two-parameter merging family

Fix a,b>0, let e=delta^(1/6), and set

```
c=a e8, z=b e4, x=a(a/b-b), p=a/(a+b²).
```

For sufficiently small e these are admissible. Consider the positive latent
lobe Yplus=sqrt(t)A+sqrt(v)Z with mean m and variance s². Expanding the
actual square roots, including the q-dependent t, gives

```
s²=e6/4 + (1/32-x/8)e12 + O(e16),
E[(Yplus-m)^3]=x e12/8+O(e16),
1/s²=4/e6-1/2+2x+o(1).                                (2)
```

The discrete fourth cumulant is O(e16). Standardize U=(Yplus-m)/s.
Its centered component means are O(e), its common noise variance is
1-O(e²), its third cumulant is x e3+O(e7), and higher cumulants begin at
order e4. Consequently its density f_e, relative to standard Gaussian phi,
has the first nonzero perturbation

```
f_e/phi=1+(x/6)e3 H3+O(e4), H3(u)=u³-3u.              (3)
```

This is an expansion for calculating integrals, not a uniform relative
error on the entire real line. The following domination supplies the needed
justification. The two weights are fixed positive constants; the two means
and their common variance extend analytically in e near0 after cancelling
the powers e3. Take that neighborhood small enough that the variance is in
[3/4,5/4] and means are bounded. Every derivative through order7 of a
component density divided by that component is a polynomial in u with
uniformly bounded coefficients. Thus |partial_e^k f_e|/f_e and the analogous
mixed u derivative ratios are bounded by C(1+|u|^N). Also f_e is bounded
above by C exp(-u²/4). Differentiating

```
D(e)=integral (f'_e+u f_e)²/f_e
```

through order7 is therefore dominated by an integrable polynomial times
exp(-u²/4). At e=0 the first nonzero numerator derivative is
(x/2)e3 H2 phi, H2=u²-1. Taylor's theorem under this domination yields

```
D(e)=x² e6/2+O(e7),                                  (4)
```

since int H2² phi=2. One may obtain(3) by expanding each shifted Gaussian;
zero mean and unit variance cancel H1,H2, the third centered moment gives
H3, and all fourth-and-higher cumulants start at order e4. The argument
controls the score integral, not just weak convergence or a formal moment list.
For a mean-zero unit-variance density, I(U)=1+D(e) by integration by parts.
Hence I(Yplus)=s^-2[1+D(e)].

Passing from Yplus to the symmetric output changes Fisher information by
an exponentially small quantity. All positive component means tend to1,
so for small e they lie in[1/2,3/2]. The score difference between positive
and negative clusters is bounded by3/v. The exact Fisher mixing deficit
is bounded by a constant times v^-2 times their Gaussian affinity; every
cross-sign pair has separation at least1. Thus the deficit is
O(v^-2 exp(-1/(8v)))=o(1). Combining(2)-(4),

```
J(2-delta,a delta^(4/3),b delta^(2/3))
 =4/delta-3/2+2x+2x²+o(1)
 =4/delta-2+2(x+1/2)²+o(1).                           (5)
```

Choose a=1 and b=(1+sqrt(17))/4, so x=-1/2. This proves
limsup [V-4/delta]<=-2. For a rational check, a=1,b=5/4 gives x=-9/20
and constant -399/200, already strictly better than -3/2. This is a
constructive asymptotic upper bound; a matching lower bound is still required.

## 3. No separated-radius face can attain that improvement

Fix epsilon>0. Uniformly for z>=epsilon, c<delta and small delta, the
outer means have absolute value at least1/2 and the gap between an outer
and inner mean on the same side is at least

```
d_epsilon=(1-sqrt(1-epsilon))/2>0.
```

All means have absolute value at most2 after taking delta<=epsilon and
small enough. The opposite outer-inner and outer-outer pairs also have
at least this separation. Only the two inner means can merge at0.
The exact Gaussian-mixture identity is I=1/v-MMSE(M|Y)/v², where
M=eta sqrt(t)A. Bound the inner-inner posterior-variance contribution
by p v: using rho>=p rho_inner reduces it to p times the two-point
Gaussian-channel MMSE, and the estimator Y bounds that MMSE by v.
All other pairs are bounded by Gaussian affinity as in K1831. Thus

```
I >= (1-p)/v -48 v^-2 exp(-d_epsilon²/(8v)).            (6)
```

The constant48 is deliberately loose: there are at most6 pairs, each
squared separation at most16 and affinity coefficient at most1/2.
Let v0=1-sqrt(1-delta/2). For small delta, dt/dc=t/[2(2-c)]>=1/8,
so v0-v>=c/8; also p<=c/epsilon². If v0<=epsilon²/8,

```
(1-p)/v >= 1/v0.
```

For v<=v0<d_epsilon²/16, the exponential error in(6) is bounded by
48 v0^-2 exp(-d_epsilon²/(8v0)), which tends0. Therefore

```
inf_(z>=epsilon,0<=c<delta) J >=4/delta-3/2-o(1).      (7)
```

This proof includes the central-atom face and c approaching delta; it does
not assume separated inner signs. Comparison with(5) proves that **every
choice of global minimizers has z->0**. No numerical onset is inferred.
Together with K1829, positive noise and K1825's artificial-face dominance,
all minimizers are eventually at 0<c<delta and 0<z<1. There is still no
finite-q uniqueness theorem or optimizing-rate classification.

## 4. A matching lower bound, including the jump at zero

For any smooth Gaussian-mixture density in this chart put

```
g(y)=sign(y)(y²-1), m1=E|Y|.
```

Its squared norm is exactly E g²=delta. Integration by parts separately
on the two half-lines gives

```
E[(rho'/rho)g]=-2m1+2rho(0),
I >=4(m1-rho(0))²/delta.                              (8)
```

The jump of g at0 is -2. Omitting the density term is wrong: for a
standard Gaussian the resulting incorrect bound would be4/pi>1, whereas
its Fisher information is1. There is no smooth-test approximation that may
silently discard that jump.

Choose arbitrary exact minimizers as delta->0. Their ratio optimality and
K1831's W2 theorem give

```
E(|Y|-1)²=delta/4+o(delta),
m1=1-delta/8+o(delta),                                (9)
```

where the second identity also uses E Y²=1 exactly. Section3 gives z->0,
and K1831 gives t->1 and v~delta/4. Every positive latent mean is therefore
eventually at least1/2, even if c/z is large. Accordingly
rho(0)<=(2*pi*v)^(-1/2) exp(-1/(8v))=o(delta).
Substitute(9) into(8): I>=4/delta-1+o(1), hence

```
liminf [V-4/delta]>=-2.
```

With the explicit upper bound this proves(1). The order is essential:
upper bound -> separated-face exclusion -> negligible rho(0) -> matching
lower bound. No circular assumption that the minimizer merges was used.
An arbitrary sequence of minimizers was allowed at every step, so the
conclusion is not limited to a selected branch.

## 5. Follow-through: the optimizing score and inverse budget

Let a_delta=2(m1-rho(0))/delta for an exact minimizer. Completing the square
in(8) and using the now matched asymptotics proves

```
E[(rho'/rho+a_delta sign(Y)(Y²-1))²]=o(1),
a_delta=2/delta-1/4+o(1).                             (10)
```

This necessary score-shape condition is stronger than leading Gaussian
convergence, but does not identify a finite-q density or a unique c,z.
In particular, the powers4/3 and2/3 in the constructive family are sufficient
for additive optimality; they have not been proved necessary for exact
minimizers. Many fixed a,b satisfying a(a/b-b)=-1/2 achieve the same constant.

K1825's global value transfer gives a unique q_B for each positive Fisher
budget B. As B->infinity, let delta_B=2-q_B. Inverting(1) gives

```
delta_B=4/(B+2)+o(B^-2)=4/B-8/B²+o(B^-2).             (11)
```

This refines the earlier leading inverse bound without requiring uniqueness
of the minimizing shape. It is an asymptotic statement, not a certified
finite-budget error interval.

## 6. Released refinement: the first shape-dependent remainder

The same analytic domination can be taken through order9. Set
h=a/b-b and y=a(h²-2a). The standardized fourth cumulant is
 y e4+O(e8), while the third remains x e3+O(e7). At order e5 the
only additional Hermite term is H5 (from the fifth cumulant). Orthogonality
of H2,H3,H4 makes the order e7 cross term and the order e8 H2/H4 cross
term vanish in the score integral. The reciprocal-density correction begins
at order e9. Thus the more precise version of(4) is

```
D(e)=(x²/2)e6+(y²/6)e8+O(e9),
J=4/delta-3/2+2x+2x²+(2/3)y² delta^(1/3)+O(delta^(1/2)). (12)
```

The variance term in(2) has remainder O(e16), which contributes O(e4)
to its reciprocal and is smaller than the displayed O(e3) remainder.
This refinement is for fixed a,b; it is not uniform when they diverge.

Within the additive-optimal family x=-1/2, the nonnegative next penalty
vanishes exactly when y=0. Since a>0, these two equations give

```
a=1/2, h=-1, b=(1+sqrt(3))/2.                          (13)
```

This improved explicit family satisfies
J=4/delta-2+O(delta^(1/2)). The earlier a=1 example has y=-7/4 and
positive next cost (49/24)delta^(1/3). It therefore cannot consist of exact
global minimizers eventually, despite attaining the sharp additive constant.
More generally any fixed a,b with x=-1/2 and y!=0 loses to(13) for small
delta. This discriminates the formerly tied fixed-parameter families.
It does NOT prove exact minimizers have these powers or coefficients:
other scaling regimes and parameter-dependent corrections remain open.

## 7. Verification and limitations

```
sage -python tests/channel-swings/k1833_fisher_merging_radius_subleading.py
python3 tests/channel-swings/k1833_fisher_merging_radius_subleading_probe.py
```

The producer expands the actual chart over a rational function field,
checks the variance and cumulant cancellations, completes the additive
square and tests16 rational parameter pairs. Independent rational controls
use two-atom central moments and Hermite generating coefficients, test the
score-jump counterexample and separated-face inequalities, and keep reporting
mutations separate. These checks support the written analytic argument;
they are not a substitute for dominated differentiation, uniform face
estimates or the inherited W2 theorem. No old numerical bank was replayed.

Inline hostile review checked rare outer means, central merging signs,
normalization I versus J, both symmetric lobes, positivity of density
weights, all exchanges of limits/integrals, the sign of the score jump and
quantifier order. The weakest seam is the small-parameter score expansion;
section2 supplies explicit derivative domination rather than claiming
moment convergence implies Fisher convergence. No unresolved finding in the
stated scope, no separate-agent review, no canon promotion and no literature
novelty claim. The general score Cauchy--Schwarz and Gaussian-mixture identities
are classical; the scoped theorem is given in full for scrutiny.

Next: obtain an effective error/onset for(1), or analyze the remaining
scaling regimes and next correction around the improved family(13).
The unique finite-q shape and actual c,z rates remain open. Repeating the
central-face exponential witness or leading ratio criterion is unnecessary.
