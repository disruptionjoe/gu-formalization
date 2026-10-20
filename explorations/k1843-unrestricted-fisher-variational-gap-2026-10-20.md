---
title: "K1843: unrestricted Fisher minimization and the finite-mixture gap"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-FINITE-MIXTURE-UNRESTRICTED-OPTIMALITY
claim_ceiling: all-density moment-constrained Fisher theorem; no effective numerical gap, endpoint asymptotics or GU physics
---

# The two-radius optimizer is not the unrestricted Fisher optimizer

For each 1<k<3, among even probability densities with E X²=1 and E X4=k,
the minimum Fisher information is attained by a unique, smooth, strictly
positive density. Its square root is the positive ground state of a confining
quartic oscillator with multipliers selected by those two moments. No
non-Gaussian finite common-variance Gaussian mixture is even stationary in
this larger class. A compactly supported perturbation preserves all three
moments exactly and strictly lowers its Fisher information.

Consequently K1820 and K1841 retain their exact restricted-family results,
but their optimizer is strictly beaten in the unrestricted density class at
each admissible q=3-k in (0,2). The result supplies no uniform quantitative
gap and does not transfer or refute K1841's endpoint expansion outside its
stated class. This is independent mathematics, not a physical GU claim.

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
result: unrestricted existence, uniqueness, quartic dual characterization and exact moment-preserving descent
carrier: even real probability densities with second moment1 and fourth moment k in (1,3) LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |u'|² with p=u² ON=real_Sobolev_functions
real_structure: real nonnegative square roots and real densities
grading: none; polynomial moment degree only
action_owner: repository-construction -- scalar Fisher variational functional
target: all densities with the stated moments, including outside finite Gaussian mixtures MAP-TYPE=evaluation
```

## 1. Object, retained result and prior-art boundary

Define I(p)=integral p'²/p=4 integral |(sqrt p)'|², with value infinity if
sqrt p is not H1(R). The moment problem is

```
F(k)=inf { I(p): p even, integral p=1, integral x²p=1,
                         integral x4 p=k },  1<k<3.           (1)
```

For K1841, k=1+delta=3-q and J=I-1. Its finite two-radius Gaussian mixtures
are feasible. Its restricted existence/uniqueness theorem does not claim (1).
Search before selection found no earlier all-density stationarity result in
the native scalar chain; covariance-only Fisher inequalities address a
different constraint. The Fisher-to-Schrödinger variational connection is
classical; see [Flego, Plastino and Plastino](https://arxiv.org/abs/1106.2078).
No novelty is claimed for that connection or the results here. The proof below
explicitly handles fourth-moment loss, positivity and the finite-mixture gap.

## 2. Existence without silently assuming fourth-moment compactness

First minimize over the relaxed constraint integral x4 p<=k. The class is
nonempty with finite I: let X=eta a+sqrt(v)Z, where eta is a fair sign,
a4=(3-k)/2, v=1-a²>0. Then E X²=1 and E X4=3-2a4=k.

For a minimizing sequence u_n=sqrt(p_n)>=0, its H1 norms are bounded.
Local Rellich compactness and the uniform bound integral x²u_n²=1 give
strong L2 compactness after a subsequence: tails of mass are at most R^-2.
The fourth-moment bound also gives uniformly vanishing second-moment tails,
`integral_|x|>R x²u_n² <= k/R²`. Therefore the limit u>=0 has norm1,
second moment1, is even, and by Fatou fourth moment m<=k. Dirichlet energy
is lower semicontinuous. A relaxed minimizer exists. One cannot conclude
m=k from compactness alone; fourth moment can escape in tails.

If m<k, let Y_t=exp(-t)X+sqrt(1-exp(-2t))Z, independently. It preserves
variance1 and evenness and has

```
E Y_t4 = 3 + exp(-4t)(m-3).                                  (2)
```

There is t>0 making this equal k. The relative score r_X=rho_X+X satisfies
`r_Y=exp(-t) E[r_X | Y]`; Jensen gives

```
I(Y_t)-1 <= exp(-2t)[I(X)-1].                                (3)
```

This identity follows by Gaussian integration by parts, including the weak
score of any finite-Fisher X. Cauchy/integration by parts gives I(X)>=1;
equality requires rho_X=-X and hence the standard Gaussian, whose fourth
moment is3. Since m<k<3, I(X)>1. Equation (3) strictly reduces I and
contradicts relaxed minimality. Thus m=k. This proves attainment in (1).

## 3. Euler equation, positivity and uniqueness

Work with real even u in H1 and weighted L2(x4 dx), not with a positivity
constraint on u; replacing u by |u| preserves constraints and energy.
At the nonnegative minimizer, the three derivatives of the moment functionals
are linearly independent: a combination would give
`(a0+a2 x²+a4 x4)u=0`. The continuous nonzero u is positive on some interval,
so this polynomial must vanish. Compactly supported even test variations on
that interval already witness independence. They also give a constraint
qualification direction decreasing the active fourth moment with norm and
second moment fixed. The inequality multiplier is therefore nonnegative.
The ordinary local multiplier argument gives, in distributions and then
classically,

```
-4u'' + (a x²+b x4)u = E u,             b>=0.                 (4)
```

Local regularity makes u smooth. If nonnegative u vanished at a finite point,
its derivative there would be zero, and uniqueness for this linear ODE would
force u identically zero. Hence u>0 everywhere. This also justifies all local
density variations used below.

In fact b>0. Suppose b=0. For a<=0 the equation has no positive L2
solution: when a=0 its exponential, affine or trigonometric solutions cannot
be nonzero, smooth and square-integrable at both ends; when a<0 Sturm
comparison forces zeros arbitrarily far out. For a>0 it is a confining
harmonic oscillator, whose only positive L2 eigenfunction is its Gaussian
ground state. Variance1 then forces fourth moment3, a contradiction. This
argument does not use unproved decay to justify a virial identity.
Thus b>0 makes (4) a confining self-adjoint Schrödinger problem. Its positive
L2 eigenfunction is the ground state. The form domain is
`H1(R) intersect L2(x4 dx)`; no unspecified boundary extension is selected.

I is convex in p by pointwise Cauchy-Schwarz. For two positive minimizers,
equality at their midpoint requires equality of their scores everywhere:
`p1'/p1=p2'/p2`. They are proportional, and normalization makes them equal.
The feasible moment set is convex, so the minimizer is unique. Its square
root is uniquely chosen positive. The coefficient triple (a,b,E) is also
unique: subtracting two versions of (4), and dividing by positive u, gives
a polynomial identity. Symmetrization cannot increase I and preserves both
even moments, so dropping the evenness restriction cannot lower the value.
Uniqueness is asserted here for the declared even class.

## 4. Executed successor: exact dual problem and virial check

Let E0(a,b) be the bottom eigenvalue of `-4d²/dx²+a x²+b x4`, for real a
and b>0. For every feasible p=u²,

```
I(p) >= E0(a,b)-a-bk.                                       (5)
```

At the multipliers in (4) equality holds. Therefore

```
F(k)=max_(a real,b>0) [E0(a,b)-a-bk].                        (6)
```

No guessed oscillator parameters are enough: the maximizing ground state
must have the two prescribed moments. At that state the dilation identity
is `I=a+2bk`; also `E=I+a+bk=2a+3bk`. These follow by differentiating the
Rayleigh energy of u_lambda(x)=sqrt(lambda)u(lambda x), and give independent
normalization checks for a future spectral certificate. This dual route
replaces unrestricted mixture enumeration with a two-parameter ground-state
problem. It is an exact characterization, not a numerical evaluation.

## 4a. Released consequence: global value and inverse-budget ordering

F is strictly convex on (1,3). For distinct k1,k2, mix their positive unique
minimizers with weight theta in (0,1). The mixture has the interpolated fourth
moment and variance1. Strict score convexity gives a value strictly below the
interpolation of F(k1),F(k2), because the two densities cannot be proportional.
F is finite, hence continuous on this interval.

It is strictly decreasing: for k1<k2<3 the OU transformation of the k1
minimizer reaches k2 at some t>0 and strictly lowers I by (3).
As k approaches3, the explicit two-point Gaussian trial in section2 has
v approaching1 and I<=1/v, while I>=1; thus F(k) approaches1.
As k approaches1, a bounded-Fisher subsequence would, by the same compactness
argument as section2, give a density with E X²=1 and E X4<=1. Equality in
Jensen would force support on {minus1,plus1}, impossible for a density.
Thus F(k) diverges to infinity.

Every relative Fisher budget B>0 consequently has exactly one unrestricted
k_B in (1,3) with F(k_B)-1=B. At K1825's restricted budget root k_R=3-q_R,
section6 gives F(k_R)-1<B. Strict decrease implies k_B<k_R, or
`q_unrestricted(B)>q_two_radius(B)`. This is a strict ordering for every
positive budget, without a certified size for the improvement. It supplies
no unrestricted endpoint exponent. The feasible density class, rather than
precision in a restricted certificate, changes the attainable budget frontier.

## 5. Finite common-variance mixtures cannot be stationary

At a smooth positive density, the first variation against compact h is

```
dI(p+epsilon h)/d epsilon at0 = integral R_p h,
R_p = -2p''/p + (p'/p)² = -4(sqrt p)''/sqrt p.               (7)
```

Stationarity under integral h=integral x²h=integral x4h=0 requires
R_p in span{1,x²,x4}. For even compact tests this is a distributional
annihilator statement; R_p is even, so it is the same polynomial identity.

Take a symmetric finite mixture with positive weights and common variance v>0,
and at least one nonzero mean. Let M>0 be its largest distinct mean. In the
right tail, grouping any repeated largest means,

```
p(x)=C exp(-(x-M)²/(2v))[1+O(exp(-d x))], d>0,
R_p(x)=2/v-(x-M)²/v² + O(poly(x)exp(-d x)).                   (8)
```

The derivative errors have the same exponential decay. An even quartic
polynomial agreeing with (8) would have quartic coefficient0, quadratic
coefficient -1/v², and a nonzero linear coefficient 2M/v². This is impossible.
All means zero give a single Gaussian, excluded by k<3. Thus every feasible
finite common-variance Gaussian mixture has a strict descending direction
in the unrestricted class. This statement does not assert a rate for its gap
or address all infinite mixtures or mixtures with arbitrary unequal variances.

## 6. Constructive, exactly moment-preserving descent

The even real-analytic R_p in (8) is not a polynomial of degree at most4,
so its sixth derivative is not identically zero. Choose a compact open
interval in (0,infinity) where R_p^(6) has one strict sign. Let psi>=0 be a
nonzero smooth bump there and phi(x)=psi(x)+psi(-x). Define

```
h=-sign(R_p^(6) on that interval) phi^(6).
```

It is even and compactly supported. Six integrations by parts give
`integral x^j h=0` for j=0,2,4, exactly, and
`D=integral R_p h<0`. For sufficiently small epsilon>0,
p_epsilon=p+epsilon h remains positive and has all the same moments.
This is an analytic construction of a better density, not a fitted sample.

It also has a finite-step guarantee. Put

```
A=sup |h|/p on supp h,
C=integral (h'p-hp')²/p³ >0.
```

For 0<=s<=epsilon<=1/(2A), direct differentiation yields

```
I''(p+s h)=2 integral (h'p-hp')²/(p+s h)³ <=16 C.
```

Hence every `0<epsilon<=min{1/(2A),-D/(16C)}` obeys
`I(p_epsilon)<=I(p)+epsilon D/2<I(p)`. All constants are finite on compact
support. Their numerical values and an explicit k-dependent gap have not
been certified. The method works at each restricted minimizer without knowing
its closed-form parameters. Consequently unrestricted F(k)-1 is strictly
less than the restricted two-radius minimum wherever that finite-noise
minimizer is available, for every 0<q<2. [K1825](k1825-global-q-fisher-transfer-2026-10-20.md)
supplies all-q boundary-inclusive attainment with positive noise. Its
Rademacher and three-point faces remain finite common-variance Gaussian
mixtures, so the strict descent applies there too. This citation is essential:
pointwise improvement of every member alone would not prove a gap of infima.

## 7. Validation and hostile review

```
sage -python tests/channel-swings/k1843_unrestricted_fisher_variational_gap.py
python3 tests/channel-swings/k1843_unrestricted_fisher_variational_gap_probe.py
```

Producer passes21 exact algebra groups; the independent probe passes114
rational controls and rejects6 reporting faults. Producer algebra checks the
first/second variations, mixture-tail polynomial,
OU moments, virial/dual coefficients and compact polynomial moment controls.
The independent standard-library probe checks moment annihilation with exact
rational polynomial integration, the Fisher second-variation identity on
rational jets, strict convexity equality defect, OU feasible moments and the
tail obstruction. The polynomial control bump has sufficient boundary
vanishing for six integrations; the theorem uses a smooth bump. These checks
do not computationally prove compactness, ODE regularity or ground-state
uniqueness. The arguments in sections2-6 own those conclusions.

Inline preflight compared larger-mixture searches, effective endpoint constants
and the Euler structural test; the latter decides a whole class first.
Inline hostile review specifically checks loss of fourth moment in weak limits,
constraint qualification at zeros, sign of b, score-convexity equality,
compact support, positive perturbations, distinction between pointwise descent
and a uniform gap, and the restricted-versus-unrestricted domain. No
separate-agent or proof-assistant review, external acceptance, novelty claim,
source/ledger/canon change or physical interpretation is claimed.

Next is a rigorous dual/primal spectral enclosure at a named k, or an analytic
endpoint study of (4). K1841's restricted powers do not determine that answer.
A broader finite-mixture numerical search alone is now a dominated proof route
for unrestricted optimality; mixtures remain useful trial upper bounds.
