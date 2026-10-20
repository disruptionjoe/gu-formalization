---
title: "K1854: The unrestricted two-point endpoint has Fisher cost 4/(k-1)"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp leading unrestricted endpoint, explicit budget brackets and concentration; no subleading law, local Gaussian profile or GU physics
---

# The unrestricted two-point endpoint has Fisher cost 4/(k-1)

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
result: universal clipped-score lower bound, Gaussian-mixture upper bound, endpoint and inverse-budget law
carrier: real probability densities on the real line with raw second moment1 and fourth moment k in (1,3) LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial degree only, no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: unrestricted all-density moment problem MAP-TYPE=evaluation
```

## Result and scope

Let F(k) be the infimum of I(p)=4 integral |(sqrt p)'|² over normalized
real densities with E X²=1 and E X4=k, and set delta=k-1. The square root
must be in H1; otherwise I=infinity. No symmetry or mean-zero condition is
needed for the lower bound. Symmetrization preserves these raw even moments
and decreases Fisher information, so this infimum equals the even problem in
[K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md).
For 0<delta<2,

```
max{1, (2-3 sqrt(delta))_+²/delta} <= F(1+delta)
      <= 2(1+sqrt(1-delta/2))/delta.                         (1)
lim_(delta down to0) delta F(1+delta)=4.                     (2)
```

Here a_+=max(a,0). K1843 proved only divergence at this endpoint.
[K1841](k1841-fisher-global-scaling-2026-10-20.md) proves a sharper expansion
in a restricted two-radius mixture family. Equation(2) now proves its leading
coefficient is optimal over **all densities**, while K1843's strict
finite-k improvement survives. Equal leading coefficients do not imply equal
values or subleading coefficients. This is independent mathematics; no
source/physics claim, novelty, external acceptance or canon promotion.

## 1. A clipped score avoids an unbounded sixth moment

Let c(x)=max(-1,min(x,1)) and f(x)=(x²-1)c(x). These are locally Lipschitz;
f is continuous at x=+-1 and has no jump delta in its weak derivative. Almost
everywhere,

```
f'=2x c(x)+(x²-1) 1_(|x|<1),
f² <= (x²-1)²,                 E f² <= delta.               (3)
```

Pointwise x c(x)>=x²-|x²-1|. On |x|<=1 this follows from x c=x²;
on |x|>1 the right side is1 and x c=|x|>=1. Thus

```
E f' >= 2 E X² - 3 E |X²-1| >= 2-3 sqrt(delta).             (4)
```

For the weak score rho=2u'/u on {u=sqrt p>0}, put rho=0 on the zero set.
Then E rho²=I and integration by parts gives E rho f=-E f'. To justify
it, first use f chi_R with a smooth cutoff equal1 on[-R,R], zero outside
[-2R,2R], derivative O(1/R). Its boundary term tends0 since
E[f² 1_(|X|>R)] tends0 by the finite fourth moment, while the 1/R factor
only helps. The score term converges by Cauchy-Schwarz; f' is integrable
by(3) and the second moment. Approximation permits the two Lipschitz corners.
If I=infinity the conclusion is immediate. Hence Cauchy-Schwarz and(3)-(4)
give the nontrivial lower bound in(1) whenever 2-3 sqrt(delta)>0; otherwise
it is0. The independent lower bound I>=1 follows by the same argument with
f=x and E rho X=-1. No sixth moment or optimizer tail estimate is used.

Using f=x(x²-1) would put a sixth moment in the denominator. Using
sign(x)(x²-1) would introduce a jump at0 and an uncontrolled point-density
term. Clipping is the essential domain repair, not a numerical approximation.

## 2. An exactly feasible upper trial

Take a fair sign eta independent of Z~N(0,1), and define

```
v=1-sqrt(1-delta/2), a=sqrt(1-v), X=eta a+sqrt(v) Z.
E X²=1,   E X4=1+4v-2v²=1+delta.                            (5)
```

For a mixture of translated Gaussians with common variance v, the observed
score is the conditional expectation of the component score. Jensen gives
I(X)<=1/v. Rationalizing v yields the upper bound in(1). It is valid for
every 0<delta<2; no separation-of-components approximation is needed.
Multiplying both bounds by delta proves(2). In particular the lower error is
explicit: delta F>=4-12 sqrt(delta)+9delta for delta<4/9, whereas
delta F<=2(1+sqrt(1-delta/2))<=4. These are not matching next-order estimates.

## 3. Released consequence: exact concentration statement

For **every** feasible density, let S=sign(X) (the zero event has probability0).
Then

```
E (X-S)² = E (|X|-1)² <= E (X²-1)²=delta.                   (6)
```

Thus the squared Wasserstein-2 transport distance from p to the two-point law
of S is at most delta, by this explicit coupling. If p is even, S is a fair
sign and the limiting law is the Rademacher distribution. If merely E X=0,
|E S|<=sqrt(delta), so the sign weights also approach one half. Without
symmetry or mean zero, a balanced sign limit is **not** proved or true.
A single shifted Gaussian with the same a,v in(5) has the same two raw even
moments and concentrates at+1. It is an asymptotically leading-optimal
countercontrol to a universal balanced-profile claim. The exact minimizer is
even by the inherited uniqueness result, but all near-minimizers need not be.
No total-variation convergence to an atomic law is possible for these densities:
that distance is always1. The transport topology in(6) is indispensable.

For any eps>0, P(||X|-1|>=eps)<=delta/eps² by Markov. This does not establish
a Gaussian local profile, the mass in each well without the stated hypotheses,
or a subleading expansion of F.

## 4. Released consequence: high-budget inversion and restricted comparison

K1843 gives a unique delta_B in(0,2) such that F(1+delta_B)-1=B for every
B>0. From(1),

```
4/(sqrt(B+1)+3)² <= delta_B
 <= 4/(B+1)-2/(B+1)²,                 B delta_B ->4.        (7)
```

For the lower bracket, if delta_B<4/9 take the square root of the lower
Fisher bound; otherwise the bracket holds trivially because its right-hand
constant is at most1/4. For the upper bracket F<=1/v implies
v<=1/(B+1), and delta=4v-2v² is increasing on0<v<1. These are finite-B
inequalities, not numerical approximations to an optimizer.

K1841's restricted J minimum is 4/delta-2+o(1), while(2) gives
F(1+delta)-1~4/delta. Their ratio tends1 even though the unrestricted minimum
is strictly smaller for each delta by K1843. The difference may remain
subleading; no constant-term or absolute-gap law follows. Equivalently both
classes have the same leading high-budget deficit4/B. Do not transplant the
restricted powers delta^(2/3) or its budget correction into the all-density
problem.

## 5. Verification and contrary cases

Run `sage -python tests/channel-swings/k1854_fisher_concentration_endpoint.py`
and `python3 tests/channel-swings/k1854_fisher_concentration_endpoint_probe.py`.
The producer verifies piecewise polynomial identities, moment feasibility and
inversion algebra. The separate Fraction implementation evaluates rational
piecewise fixtures including tails, Gaussian moments and budget bounds, with
planted coefficient/input faults. Neither finite sampling nor an assertion
flag proves the weak integration-by-parts limit: sections1-4 own that proof.

Inline hostile review checked heavy tails with finite fourth but infinite
sixth moment, weak-score zeros, clip corners, I versus J, inequality inversion,
symmetry and the impossibility of TV convergence to atoms. No unresolved
analytic defect found in the stated leading law. No independent-person or
formal proof-assistant verification is claimed. Standard Cramer-Rao and
Fisher variational methods are established; the companion
[K1855](k1855-fisher-gaussian-endpoint-2026-10-20.md) cites prior context.
The next substantive endpoint question is a **uniform subleading** all-density
bound or blow-up-profile theorem; another two-radius jet cannot supply it.
