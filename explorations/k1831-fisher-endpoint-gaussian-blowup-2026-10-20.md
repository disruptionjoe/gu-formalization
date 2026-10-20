---
title: "K1831: endpoint Fisher optimality forces Gaussian local profiles"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete leading-order optimality criterion and Gaussian blowup for the two-radius family; no subleading optimum or physical interpretation
---

# Exactly which endpoint sequences are optimal to leading order

Set delta=2-q. In K1825's symmetric unit-variance two-radius Gaussian
family, for every sequence q increasing to2,

```
delta J(q,c,z) -> 4   if and only if   c/delta -> 0.     (1)
```

Equivalently, the value ratio J/V tends to1 exactly under that condition.
It holds for arbitrary moving z in(0,1], including rare and merging atoms.
Then v/delta tends to1/4 and

```
2(|Y|-1)/sqrt(delta) -> N(0,1) in Wasserstein distance W2. (2)
```

Every global minimizer therefore satisfies(1)-(2). K1829 separately proves
c>0 sufficiently near the endpoint. There is no conflict: the optimizing
c is positive and o(delta), with its finer scale still unknown.
These are GU-independent scalar results, not a physical observable,
subleading constant, actual transition, unique z or canonical promotion.

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
result: necessary and sufficient ratio-optimal shape scaling and Gaussian local-profile convergence
carrier: symmetric unit-variance two-radius Gaussian outputs with q increasing to2 LAYER=toy CHIRALITY=N/A
pairing: ordinary and relative Fisher integrals, compact test-function duality ON=real_observation_line
real_structure: real densities, weak probability limits and positive Gaussian noise
grading: endpoint scaling and scalar moments; no physical grading
action_owner: repository-construction -- moment-constrained Fisher functional, not a source action
target: all moving admissible shape sequences, including exact minimizers MAP-TYPE=evaluation
```

## 1. Inputs and the question

Use the actual chart, not a fixed-shape limiting surrogate:

```
p=c/(c+z²), A=sqrt(1-z) with probability p,
A=sqrt(1+c/z) with probability 1-p,
X=epsilon A, epsilon independent uniform sign,
t=sqrt((2-delta)/(2-c)), v=1-t, Y=sqrt(t)X+sqrt(v)Z.
```

The domain is 0<=c<delta, 0<z<=1. The c=0 law is Rademacher,
including redundant z coordinates. The artificial z=0 compactification
from K1825 is not in this domain; its lost fourth moment is never used.
K1827 supplies delta V->4 and the uniform lower bound J>=4/delta-551/27.
Conditional Gaussian-score Jensen gives I(Y)<=1/v, with J=I-1.
No q0 numerical bank is needed.

The classical compact-test formula and its weak lower semicontinuity are
reused from K1757/K1825. A primary reference for the general variational
Fisher-information approach is [Ruckdeschel, Fisher Information in Group-Type
Models (2010)](https://arxiv.org/abs/1005.1027); the specific one-dimensional
argument needed here is provided below. The Gaussian information equality
is the elementary score Cauchy--Schwarz identity. No literature novelty or
external specialist acceptance is claimed.

## 2. Blow up both lobes, retaining rare atoms

Take a subsequence on which lambda_n=c/delta tends to lambda in(0,1]
and b_n=z/sqrt(delta) tends in the compactified interval[0,infinity].
The positive latent lobe is Y_plus=sqrt(t)A+sqrt(v)Z; put
U_plus=2(Y_plus-1)/sqrt(delta). Exactly

```
4v/delta = 4(delta-c)/[delta(2-c)(1+t)] -> 1-lambda.      (3)
```

If 0<b<infinity, its limit is

```
H_(lambda,b)=D_(lambda,b)+sqrt(1-lambda) Z,
D=-b with weight lambda/(lambda+b²),
D=lambda/b with weight b²/(lambda+b²).                  (4)
```

Taylor expansion of the two square roots proves the means in(4), with
bounded parameters on this interior case; E D=0 and E D²=lambda.
If b=0, the inner weight tends1, its rescaled mean tends0; the outer
weight tends0 even if its rescaled mean escapes. If b=infinity, the outer
weight tends1, its rescaled mean tends0, and the inner weight tends0.
In either case the weak limit is N(0,1-lambda). For b=infinity use
c/z=O(sqrt(delta)/b_n), and for b=0 use z=o(sqrt(delta)); no uniform
Taylor expansion is applied to an escaping rare mean. The missing second
moment at these endpoints is retained as lost moment, not equated to zero.
If lambda=1 these limits are finite atomic measures (two atoms in the
interior, one at either endpoint).

The reflected lobe must also be counted. Define
r_delta(u)=(sqrt(delta)/2) rho(1+sqrt(delta)u/2).
On compact u sets this tends vaguely to half the measure H above.
The negative latent lobe contributes zero locally: its means are <=0,
while positive y near1 is separated by a fixed distance and v->0.
The possible atom at A=0 has vanishing weight when it matters here.
The analogous negative chart has the reflected half-limit.

For a smooth density f and a compactly supported test g,

```
I(f) >= integral [-2g'-g²] f,
I(f)=sup_(g in C_c^infty) integral [-2g'-g²] f.          (5)
```

Integration by parts and completing the square prove the inequality;
L2(f) approximation to the score proves equality for the smooth positive
limits. Place any fixed compact test in each rescaled lobe. For small
delta their supports in y are disjoint, so the two test energies add.
Each half-limit contributes half its Fisher test value. Taking the supremum
AFTER the limit yields

```
liminf delta I(Y)/4 >= I(H).                           (6)
```

This uses local test convergence, not Fisher continuity, and does not lose
the factor of two from the lobes. For an atomic limit the same supremum is
infinite: prescribe a test with zero value and arbitrarily negative
derivative at one atom, supported away from the others. Thus lambda=1
forces an infinite liminf, including the b endpoints.

## 3. A strict and quantitative limiting information gap

For 0<lambda<1, finite positive b, H has mean0 and variance1. The score
identity gives I(H)>=1, with equality only for a standard Gaussian. H is
not Gaussian: its characteristic function divided by the nonvanishing
noise factor would require the nondegenerate two-atom D to be Gaussian.
This already supplies the strict gap needed for(1).

A useful follow-through makes a conservative gap explicit. Write m_j=E H^j
and k=b²/lambda+lambda/b²-2>=0. Exact moments give

```
m3²=lambda³ k, m4-3=lambda²(k-2).
I(H)-1 >= m3²/(m4-1),
I(H)-1 >= (m4-3)²/(m6-6m4+9).                          (7)
```

To derive(7), apply Cauchy--Schwarz to score+u against u²-1 and u³-3u.
Their score pairings are m3 and m4-3; E(score+u)²=I-1.
The Gaussian tails justify these polynomial integrations by parts.
For k>=1 the first bound is at least lambda³/(2-lambda²)>=lambda³/2.
For k<=1, b²/lambda and its reciprocal are below3, so |D|²<=3.
Then E D6<=27, E D4<=9, E D²=lambda<=1. With noise variance<=1,
m6<=27+135+45+15=222, hence m6-6m4+9<=231. Also |m4-3|>=lambda².
Both regimes yield

```
I(H) >= 1+lambda^4/231.                               (8)
```

At b=0 or infinity the limit has Fisher1/(1-lambda), which is larger
than the bound in(8). At lambda=1 the infinite limit again dominates.
Therefore whenever c/delta->lambda>0,

```
liminf delta J/4 >= 1+lambda^4/231 >1.                 (9)
```

The constants are conservative. In particular, for every fixed epsilon>0,
there exists delta_epsilon>0 such that all admissible shapes with
delta<delta_epsilon and c/delta>=epsilon satisfy

```
delta J >= 4(1+epsilon^4/462).                         (10)
```

If not, a violating sequence has compactified subsequences above, contradicting
(9). The gap coefficient is explicit; this compactness proof does NOT compute
delta_epsilon. A sampled onset is not promoted to an effective bound.

## 4. The converse and a complete leading-order criterion

If c/delta->0, (3) gives v/delta->1/4. Gaussian-score Jensen and K1827 give

```
4-(551/27)delta <= delta J <= delta/v-delta ->4.
```

This proves sufficiency uniformly in z. Conversely, if delta J->4 but
c/delta does not tend0, some subsequence has lambda>=epsilon>0; the
subsequence classification and(9) contradict this. This proves(1).
Since delta V->4, it also proves the value-ratio formulation. Exact minimizers
exist by K1825, so every choice of minimizers, including nonunique choices,
has c=o(delta). No minimizer compactness/uniqueness assertion is smuggled in.

## 5. Follow-through: the actual Gaussian profile in W2

For the positive amplitude A, E(A²-1)²=c and
(A-1)²<=(A²-1)². If c=o(delta), couple U_plus to the same Z. Then

```
E[ (2(sqrt(t)A-1)/sqrt(delta))² ]
 <= 8[c+(1-sqrt(t))²]/delta ->0,
2sqrt(v/delta)->1.
```

Thus U_plus tends to Z in L2 under this coupling, hence in W2.
By symmetry, |Y| has the same law as |Y_plus|. The map
F_delta(u)=2(|1+sqrt(delta)u/2|-1)/sqrt(delta) is1-Lipschitz,
and F_delta(Z)->Z in L2 by Gaussian tail domination. Applying it to the
coupling proves(2). It also gives the positive conditional-lobe law because
Y is symmetric with a continuous density. No separation assumption on the
original four atoms is needed.

Different z sequences and many positive c=o(delta) sequences all satisfy
leading optimality. K1829's strictly positive minimizing c near2 and its
conservative exponentially tiny improvement remain valid. Neither (1) nor(2)
selects the smaller displacement scale, a subleading constant, the best z,
or all-q shape uniqueness. In particular c=delta² with z=delta,1/2 or1
is leading-optimal by the theorem; leading optimality cannot choose among them.

## 6. A smaller-scale discriminator on the central-atom face

The leading criterion alone allows a divergent additive error. This can be
proved without quadrature on z=1, where the signal after scaling has three
means M in {0,+m,-m}, m²=t(1+c), with weights p=c/(1+c) and
(1-p)/2. For delta<=1/4, m²>=1/2 and m²<=5/4.

For any common-variance Gaussian mixture, conditioning its noise score gives

```
I(Y)=1/v-MMSE(M|Y)/v².
```

If phi_i is the density of N(m_i,v), direct posterior variance gives

```
MMSE=sum_(i<j) w_i w_j (m_i-m_j)² integral phi_i phi_j/rho,
MMSE<= (1/2) sum_(i<j) sqrt(w_i w_j) (m_i-m_j)²
                     exp(-(m_i-m_j)²/(8v)).             (11)
```

The inequality uses rho>=2sqrt(w_i w_j phi_i phi_j), then the exact
Gaussian affinity integral. Zero-weight terms are omitted. On this face,
the minimum nonzero separation is m, the sum of the three squared
separations is6m², and sqrt(w_i w_j)<=1. Consequently the deliberately
loose uniform bound is

```
0<=1/v-I(Y)<=6 v^-2 exp(-1/(32v)).                     (12)
```

For c=kappa delta², fixed kappa>=0, expansion of the exact expression
1/v=(2-c)(1+t)/(delta-c) and (12) gives

```
J(2-delta,kappa delta²,1)=4/delta-3/2+4kappa+o(1).      (13)
```

Thus every kappa>0 is leading-optimal but has a strictly worse additive
constant than the Rademacher competitor. More sharply, c=delta^(3/2), z=1
is still leading-optimal, but J-4/delta is asymptotic to4/sqrt(delta)
and diverges. This prevents mistaking (1) for additive near-optimality.

A useful conditional face bound follows. If a global minimizer lies on z=1,
it has c=o(delta) by (1), so v>=v0/2 eventually, where v0=1-sqrt(1-delta/2).
For fixed delta, d(1/v)/dc=t/[2(2-c)v²]>=1/(8v0²).
Comparison with the Rademacher candidate and (12) implies

```
c/(8v0²)<=6v^-2 exp(-1/(32v)),
c<=192 exp(-1/(32v0))                                 (14)
```

for sufficiently small delta. The onset is not computed. This is a
necessary bound for a minimizer IF it is on that face, not proof that the
face wins or loses, not the true optimizing exponential rate, and not a
uniform bound for unrestricted z. K1829's positive-c theorem still applies.
This follow-through discriminates additive value and restricts one surviving
face while leaving the actual smaller-scale variational problem open.

## 7. Reproduction and hostile review

```
sage -python tests/channel-swings/k1831_fisher_endpoint_gaussian_blowup.py
python3 tests/channel-swings/k1831_fisher_endpoint_gaussian_blowup_probe.py
```

The producer checks chart moments, rescaled means/variance/weights, exact
third/fourth-moment identities, 25 rational profile cases and two-lobe
scaling. The separate Fraction-based probe computes Gaussian moments from
a binomial sum, checks15 different cases and symmetric/rare/coordinate
counterexamples. Reporting mutations test manifest wording separately.
These controls do not prove weak-limit compactness; sections2-5 give that
analytic proof. An initial control caught a wrong -6lambda² transcription
in one fourth-cumulant check; it was corrected to -4lambda² before acceptance.
No old quadrature or complete fixed-q bank was rerun.

Preflight selected compact-test lower semicontinuity over fixed-shape
asymptotics. Postflight checked both lobes, escaping moment mass, noise
collapse, the symmetric zero-skewness case, and sufficiency uniformly in z.
The cubic witness is essential when m3=0; skewness alone cannot establish
the strict gap. The posterior-variance identity, Gaussian affinity factor1/2, three-component weights and conditional face-minimizer bound were also checked. No unresolved gap was found in this stated proof scope.
No independent-agent review or canon acceptance is claimed.

Next: determine the subleading variational cost inside c=o(delta), where
the theorem deliberately stops discriminating. A quantitative convergence
rate or effective delta_epsilon would require new uniform estimates; the
explicit gap in(9) alone does not supply them. Source, physics ledger and
public claims are unchanged.
