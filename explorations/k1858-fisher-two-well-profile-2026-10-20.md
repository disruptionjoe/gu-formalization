---
title: "K1858: Universal two-well profiles and the unrestricted Fisher constant"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unrestricted endpoint profile, optimizer barrier and constant term; no effective onset, higher-order expansion, high-moment profile or GU physics
---

# Universal two-well profiles and the unrestricted Fisher constant

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
result: universal sign-resolved Gaussian blowup, quartic barrier, unrestricted constant, budget and score consequences
carrier: real probability densities with raw second moment1 and fourth moment1+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial degree and asymptotic order only; no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: unrestricted real-line moment problem MAP-TYPE=evaluation
```

## 1. Results, prerequisites and semantic boundary

Write F(k) for the minimum of I(p)=4 integral |(sqrt p)'|² under
normalization, raw E X²=1 and E X4=k. The [K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md)
even positive optimizer also realizes the unrestricted value; its quartic
Euler equation, dual inequality and virial identities are reused below.
[K1854](k1854-fisher-concentration-endpoint-2026-10-20.md) proves
(delta)F(1+delta)->4 as delta decreases to0. This paper proves:

1. For **any** feasible family with delta I(p_delta)->4, put
   S=sign(X), T=2(|X|-1)/sqrt(delta), and w_sigma=P(S=sigma).
   The joint law of (S,T) converges in total variation to
   law(S) times the standard Gaussian law. The marginal T converges also in
   Wasserstein-2. The sign weights need not converge or be balanced.
2. After a fixed physical-space cutoff near X=0, the H1 distance of each
   well square root to sqrt(w_delta,sigma)*sqrt(phi) tends to0. This uses the
   actual varying weights, without assuming they converge. Without this cutoff,
   zero extension across
   the moving endpoint can have a jump and is **not** asserted to lie in H1.
3. For the exact optimizer, its density at0 is exponentially small. This
   closes the jump term in the sharp half-line score inequality and proves

```
F(1+delta)=4/delta-1+o(1),
F(1+delta)-1=4/delta-2+o(1).                         (1)
```

4. The associated budget inverse and exact optimizer score follow in section6.
   A smooth, exactly feasible leading-optimal family in section7 has divergent
   rescaled fourth and original sixth moments. Profile convergence alone
   cannot provide the next value coefficient.

These are independent scalar mathematics. No GU source assertion, physics
ledger verdict, canonical status, external acceptance or novelty is changed.
The compactness and equality argument uses the classical Cramer--Rao/Heisenberg
inequality, proved directly below. The Fisher-to-quartic-oscillator connection
is inherited from K1843, not claimed as new. Search by endpoint, blowup,
Gaussian wells, subleading and 4/delta found K1831/K1833/K1841 only for the
restricted two-radius family; K1854 explicitly left this all-density question
open. K1857's Gaussian endpoint is k->3, a different limit.

## 2. Uniform compactness without a sixth moment

Set s=sqrt(delta)/2, y=|X| and D_delta=(-1/s,infinity). For sigma=+,- define
subdensities and their square roots

```
q_delta,sigma(t)=s p_delta(sigma(1+s t)),  t in D_delta,
u_delta,sigma=sqrt(q_delta,sigma).
```

The two masses are w_delta,sigma, whose sum is1. The exact constraints and
energy transformation give

```
(sum_sigma) integral t² (2+s t)²/4 q_delta,sigma(t) dt=1,
(sum_sigma) integral t² q_delta,sigma(t) dt<=4,
(sum_sigma) integral |u'_delta,sigma|² dt=s² I(p_delta)/4 ->1/4. (2)
```

The second inequality uses (y+1)²>=1. The first is exactly
E(X²-1)²=delta, not a fourth-order Taylor approximation. No sixth moment is
used. Tightness follows uniformly from the second inequality.

Here is an explicit boundary repair. Fix a Lipschitz chi on [0,infinity)
with 0<=chi<=1, chi=0 on[0,1/4], chi=1 on[1/2,infinity), and bounded
weak derivative. Put

```
v_delta,sigma(t)=chi(1+s t)u_delta,sigma(t) on D_delta,
                  0 otherwise.
```

These functions belong to H1(R). Since
P(y<=1/2)<=16delta/9, their total lost squared mass is at most16delta/9.
The extra derivative is s chi'(1+s t)u_delta,sigma, whose combined L2 norm
is O(s). Therefore their combined derivative norm squared has limsup<=1/4.
They remain tight in L2 and locally bounded in H1.

Along any sequence delta->0, pass to a subsequence with w_delta,sigma->w_sigma.
Local Rellich compactness, a diagonal subsequence and L2 tightness give
v_delta,sigma->v_sigma strongly in L2(R), and weakly in H1. Their masses are
w_sigma and their combined mass is1. On every fixed compact interval the
cutoff is eventually1 and (2+s t)²/4 converges uniformly to1. Hence

```
M=(sum_sigma) integral t² v_sigma² <=1,
K=(sum_sigma) integral |v'_sigma|² <=1/4.              (3)
```

This is a liminf argument on compact intervals followed by monotone
exhaustion. It does not exchange an unbounded polynomial with a weak limit.

## 3. Equality forces both profiles and exhausts the tails

For the limit vector v=(v_+,v_-), integration by parts with cutoffs yields

```
(sum_sigma) integral t v_sigma v'_sigma=-1/2.
```

Indeed the total squared norm is1, t v belongs to L2 by(3), and the cutoff
boundary error vanishes by L2 tightness. Thus Cauchy--Schwarz gives

```
1/4 <= M K <=1/4.                                    (4)
```

Every inequality is equality. The equality condition in vector L2 is
v'_sigma=-t v_sigma/2 for both components, with the same coefficient. The
nonnegative solutions and their masses are

```
v_sigma(t)=sqrt(w_sigma) sqrt(phi(t)),
phi(t)=(2pi)^(-1/2) exp(-t²/2).                       (5)
```

In particular M=1 and K=1/4. Weak derivative convergence plus equality of
limiting norms upgrades the cutoff convergence to strong H1. This proves
Gaussian shape in both wells; it does not force their weights to agree.
The original subdensities differ from v_delta,sigma² by total L1 mass O(delta).
Consequently

```
(sum_sigma) ||q_delta,sigma-w_delta,sigma phi||_L1 ->0. (6)
```

The statement holds for the entire family, even if its weights oscillate:
otherwise a failing subsequence has a weight-convergent subsequence to which
the preceding argument applies. Conditional profiles converge in TV for
any well whose weight stays bounded away from0. No conditional assertion is
made for a vanishing-mass well.

There is also genuine second-moment convergence. In(2) call the positive
weight A_delta(t)=(2+s t)²/4; on D_delta it is at least1/4. For fixed R,
the weighted second integral over[-R,R] converges to
integral_[-R,R] t² phi(t)dt. Its total is exactly1. Therefore

```
limsup_delta (sum_sigma) integral_(|t|>R) t²q_delta,sigma
 <=4[1-integral_[-R,R] t²phi].                         (7)
```

Let R increase to infinity. This establishes uniform integrability of T²,
so E T²->1 and T converges to N(0,1) in W2 as well as TV. The energy in(2)
is likewise exhausted by the limiting profiles. The interior derivatives
u'_delta,sigma, extended by0 as L2 functions, converge strongly to the
corresponding Gaussian derivatives; this statement about derivative vectors
does not identify them with the distributional derivative of a discontinuous
zero extension of u_delta,sigma.

## 4. Released moment consequences and asymmetric controls

The exact second constraint gives 2s E T+s²E T²=0. Combining it with(7),

```
E(|X|-1)²=delta/4+o(delta),
E|X|=1-delta/8+o(delta),
Var(|X|)=delta/4+o(delta).                             (8)
```

No third or sixth moment was used to obtain these coefficients. Uniform
integrability of |T| and the joint convergence also imply E(S T)->0, hence
E X=(w_+-w_-)+o(sqrt(delta)). Thus mean-zero leading-optimal families have
w_+-w_-=o(sqrt(delta)); even families have exactly balanced signs.

A single shifted Gaussian from K1854 is feasible and leading-optimal, but
concentrates only at+1. It is a contrary control to universal balanced signs.
A density remains at TV distance1 from every two-point atomic law: (6) concerns
the **rescaled local coordinate**, not TV convergence of X to atoms.
Uniform bounded-observable and CDF convergence of the local profiles follow
from(6). No rate or unbounded-observable response beyond(7)-(8) is inferred.

## 5. Optimizer-specific barrier closes the unrestricted constant

Let p_delta=u_delta² be the even positive optimizer supplied by K1843. Its
parameters satisfy

```
-4u''+(a x²+b x4)u=E u, b>0,
F=a+2b(1+delta), E=2F-b(1+delta).                     (9)
```

The dual inequality says -b is a subgradient of the convex value F as a
function of k. For fixed 0<eta<1, applied at k=1+delta,

```
[F(1+delta)-F(1+(1+eta)delta)]/(eta delta) <= b
 <=[F(1+(1-eta)delta)-F(1+delta)]/(eta delta).          (10)
```

Using only K1854's leading value, multiplying by delta², taking liminf and
limsup and then eta->0 gives

```
b delta²->4, a delta²->-8, E delta²->-4.              (11)
```

No differentiation of an unspecified o(1) term or assumed differentiability
of F is involved. These limits and(9) give uniform convergence on[0,1/2]:

```
delta²(a x²+b x4-E)->4(x²-1)² >=9/4.
```

For all sufficiently small delta the left side is at least1, so
u''>=u/(4delta²) on that interval. Evenness gives u'(0)=0. Comparison with
the solution u(0)cosh(x/(2delta)) yields

```
u(1/2)>=u(0)cosh(1/(4delta)).
```

One direct justification subtracts that solution and uses the nonnegative
Green kernel for d²/dx²-(2delta)^(-2) with zero initial data. The H1 bound
sup u²<=2||u||_2||u'||_2=sqrt(F)=O(delta^(-1/2)) therefore gives

```
p_delta(0)=O(delta^(-1/2) exp(-1/(2delta)))=o(delta).   (12)
```

There is no certified numerical onset or constant hidden in this asymptotic
barrier. It applies to the actual quartic optimizer, not arbitrary
leading-optimal competitors.

For a smooth density let g(x)=sign(x)(x²-1) and m1=E|X|. Its jump at0
is -2. Separate integration by parts on the half-lines gives

```
E[rho g]=-2m1+2p(0), E g²=delta,
I>=4(m1-p(0))²/delta.                                (13)
```

The finite fourth moment and finite Fisher justify truncation at infinity;
the point term must be retained. Omitting it would already fail for a standard
Gaussian. Apply(8) and(12) to the optimizer to get
F>=4/delta-1+o(1).

For the matching upper bound, reuse the explicit feasible two-radius trial
from [K1833, section2](k1833-fisher-merging-radius-subleading-2026-10-20.md):
c=delta^(4/3), z=((1+sqrt(17))/4)delta^(2/3). Its verified Gaussian-mixture
score expansion gives J=4/delta-2+o(1), hence I=4/delta-1+o(1).
This trial belongs to the unrestricted feasible class. Together these bounds
prove(1). Only the trial upper bound is imported, not a restricted-family
lower bound or an unproved transfer of its later fractional powers.

## 6. Executed score, budget and restricted-gap consequences

Put A_delta=m1-p_delta(0) and c_delta=2A_delta/delta. Completing the square
in(13), with the now matched upper and lower asymptotics, proves

```
E_(p_delta)[rho+c_delta sign(X)(X²-1)]²=o(1),
c_delta=2/delta-1/4+o(1).                             (14)
```

This is a global optimizer score statement with a finite-fourth-moment test.
It is not an assertion that its cusp-shaped comparison score is the exact
smooth optimizer or that arbitrary competitors have an exponentially small
central density.

Let delta_B be the unique inverse F(1+delta_B)-1=B from K1843. Then

```
delta_B=4/(B+2)+o(B^(-2))
       =4/B-8/B²+o(B^(-2)).                           (15)
```

The first equality follows by inversion of B=4/delta_B-2+o(1), not by
reversing a one-sided bound. The restricted two-radius value V from K1841
has the same first two terms as F-1, so

```
0 < V(2-delta)-[F(1+delta)-1] = o(1).                 (16)
```

Strictness for each delta is K1843's finite-mixture descent. Thus strict
finite-parameter superiority coexists with a vanishing absolute endpoint
gap. Neither its rate nor the unrestricted next coefficient follows from
K1841's restricted delta^(2/3) expansion. Inverse budget differences are
likewise o(B^(-2)), with strict ordering inherited from K1843.

## 7. Exact-moment contrary family: higher profile moments can diverge

Let 0<t<=1/100, delta=t², epsilon=t19 and w=t^(-8), and set

```
v=(1-t11)/(1-t19),
k0=(1+t²-3t³)(1-t19)/(1-t11)².
```

Then k0-1=t²-3t³+o(t³)>0 and k0<3. These domain statements also follow
directly on the stated interval: the numerator of k0-1 is

```
t²-3t³+2t11-t19(1+t²-3t³)-t22,
```

whose negative last two terms have magnitude less than2t19, whereas
its first two terms are at least(97/100)t²; its denominator is positive.
An upper bound k0<2 follows from 1+t²<1.001 and (1-t11)²>0.99.
Let r_k0 be the unit-second optimizer and r_v its dilation to variance v.
Define

```
p_delta=(1-epsilon)r_v+epsilon N(0,w).                (17)
```

The second moment is exactly (1-epsilon)v+epsilon w=1; the fourth is
exactly (1-epsilon)v²k0+3epsilon w²=1+delta. Fisher convexity gives

```
I(p_delta)<=(1-epsilon)F(k0)/v+epsilon/w,
delta I(p_delta)->4,                                 (18)
```

because (k0-1)/delta->1 and (1-epsilon)/v->1; K1854 supplies the matching
lower bound. Thus every profile result above applies. Nevertheless

```
E X6>=15 epsilon w³=15t^(-5)->infinity.
```

For |x|>=2, (|x|-1)^4>=x4/16. The Gaussian component satisfies
E[X4 1_(|X|>=2)]>=3w²-16. Therefore its local coordinate T obeys

```
E T4 >= epsilon(3w²-16)/delta² =3/t-16t15 ->infinity. (19)
```

This is compatible with W2 convergence and strong cutoff square-root H1;
neither controls fourth moments. It directly blocks using the profile as an
unbounded-moment Taylor theorem. It does not ascribe these tails to the exact
optimizer. The barrier in section5 is the extra optimizer-specific input
that permits the constant term despite this contrary construction.

## 8. Verification, review and remaining exact question

Run:

```
python3 tests/channel-swings/k1858_fisher_two_well_profile.py
python3 tests/channel-swings/k1858_fisher_two_well_profile_probe.py
```

The producer verifies exact scaling, vector equality constants, secant limits,
virial/barrier coefficients, jump-score and budget algebra, trial constant and
contamination moments. A separate Fraction/polynomial implementation checks
those identities on independent rational fixtures. Mathematical-input faults
must fail a printed assertion after a clean baseline; reporting-field faults
are counted separately. Neither finite controls nor an accepted JSON schema
proves compactness, norm saturation, ODE comparison or the asymptotic
statements: sections2-7 contain the analytic proof.

Preflight lenses: variational analysis selected equality saturation over a
new high-order numerical search; concentration-compactness checked escaping
moment mass; ODE analysis identified the central-density barrier; statistical
scope kept raw moments separate from symmetry; hostile construction sought
an exact-moment heavy-tail counterexample. The initial profile-only route did
not itself settle the constant: K1843's dual subgradient and quartic equation
provided the independent missing input and released that successor.

Two independent analytic reviews found no blocking defect in the
profile proof, imported trial, subgradient argument or optimizer barrier. The
serialized controls passed13 exact groups and90 independent rational checks;
10 mathematical-input and5 reporting faults were assertion-detected after a
clean baseline. The final probe prints every fault and its caught assertion.
These reviews are not external specialist acceptance.

Postflight hostile review checked moving-domain boundary jumps, vector mass
normalization, vanishing sign weights, second-moment uniform integrability,
point-density terms, derivative versus subgradient limits, optimizer versus
competitor scope, I versus I-1, and inversion signs. No unresolved analytic
defect was found in the stated results. The explicit contrary family rejects
higher-moment transfer. This is an analytic derivation with exact arithmetic
controls, not a formal proof-assistant certificate or external acceptance.

The next value question is a uniform next-order optimizer estimate after
4/delta-1; it requires a quantitative barrier/profile remainder or a globally
signed dual with matching trial. The generic leading-optimal profile cannot
supply that estimate, and the restricted delta^(2/3) term cannot be imported.
