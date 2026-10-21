---
title: "K1878: Sharp atomic Fisher cost forces Gaussian well profiles"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: asymptotic TV and W2 profiles at positive-mass wells; no effective rate, spectral gap, multiplier enclosure or GU prediction
---

# The actual three-well profiles, beyond the minimum value

Fix k>3. Let p_delta be any probability density on R with raw second moment1,
fourth moment k, sixth moment at most k²+delta, and finite Fisher information
I(p)=4 integral |(sqrt(p))'|². Suppose delta decreases to0 and

```
delta I(p_delta) -> (k+1)².
```

Partition R into the nearest-atom cells for r=0,+sqrt(k),-sqrt(k).
Along any subsequence on which their masses converge, the limiting masses are
p0=1-1/k, p++p-=1/k. In every cell with limiting mass strictly positive,
the conditional law of (X-r)/sqrt(delta) converges in both total variation
and W2 to a centered Gaussian with variance

```
s0=1/[k(k+1)],       s+=s-=1/[2k(k+1)].                 (1)
```

The exact even minimizer from K1874 therefore has these three profiles and
outer masses1/(2k). Nearly optimal densities need not have equal outer masses.
This is independent scalar mathematics. No finite-delta error rate, sextic
coefficient, spectral gap, physical observable or novelty claim follows.

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
result: Gaussian local-profile rigidity at sharp three-atom Fisher cost
carrier: real line probability densities with raw moments2=1,4=k>3,6<=k²+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher energy4 integral |u'|² and weak measure duality ON=real_H1_square_roots
real_structure: real nonnegative densities and finite real moments
grading: moment degree and positive small-slack scaling
action_owner: repository-construction -- constrained scalar Fisher energy
target: rescaled conditional distributions in nearest-atom cells MAP-TYPE=evaluation
```

## 1. Inputs and exact localization

[K1876](k1876-fisher-atomic-boundary-cost-2026-10-20.md) proves the sharp
value and an exactly feasible asymptotically optimal unequal-width mixture.
Here the density is unrestricted; we do not assume it is a mixture.
[K1831](k1831-fisher-endpoint-gaussian-blowup-2026-10-20.md) treats a
different two-radius family and supplies no three-well theorem.

Put g(x)=x³-kx, d(x)=distance(x,{0,+sqrt(k),-sqrt(k)}). Then

```
E g(X)² = E X6-k² <= delta,
g(x)² >= (9k²/16) d(x)².                               (2)
```

For the second inequality set z=x/sqrt(k). In the central cell |z|<=1/2,
|(z³-z)/z|=1-z²>=3/4. On z>=1/2, the nearest root is1 and
|(z³-z)/(z-1)|=z(z+1)>=3/4; use reflection for the other side.
The limiting values at roots are understood. Thus E d²<=16delta/(9k²).

Let L be the nearest-atom label. The measures of (L,Y), with
Y=(X-r_L)/sqrt(delta), have uniformly bounded second moment, hence are
tight. Their label masses have convergent subsequences. Equation(2) forces
the unscaled weak limit onto the three atoms. The sixth-moment bound implies
uniform integrability of X² and X4, so the second and fourth moments pass
to that limit. They give p++p-=1/k and p0=1-1/k; no first-moment constraint
fixes the sign split. For any positive limiting mass p_j, the conditional
laws have weak subsequential limits q_j with finite second moments s_j.
Cells with vanishing limiting mass do not define a required limiting profile.

## 2. The limiting budget and Fisher inequality

Write a_j=|g'(r_j)|, namely k,2k,2k. On every bounded y interval,
g(r_j+sqrt(delta)y)/sqrt(delta) tends uniformly to g'(r_j)y.
Fatou with compact cutoffs in the label charts gives

```
S := sum_j p_j a_j² s_j <= 1.                            (3)
```

Only positive-mass labels enter these sums. For any compactly supported
smooth test f, integration by parts and completion of the score square give

```
I(q) = sup_f integral(-2 f'-f²)dq.                       (4)
```

For a general measure the right side defines the extended information; finite
value implies an H1 square-root density. This follows equivalently from
the weak derivative characterization and the same quadratic duality. Place
one test at each r_j, scaled by1/sqrt(delta). Their supports are disjoint
for small delta. Pass to the weak limit before taking the suprema. This proves

```
liminf delta I(p_delta) >= sum_j p_j I(q_j).              (5)
```

The standard compact-test/weak-derivative framework has a primary reference
in [Ruckdeschel, Fisher Information in Group-Type Models (2010)](https://arxiv.org/abs/1005.1027).
We use its general context, not an asserted theorem about this three-well
problem. The inequalities and equality transfer needed here are explicit.

For each probability q with finite second moment s and finite information,
cutoff integration by parts gives E[Y rho(Y)]=-1. Cauchy-Schwarz gives
I(q)s>=1. Equality forces rho=-Y/s, hence q=N(0,s). Using variance instead
of second moment gives the familiar stronger Cramer-Rao form; equality in
the second-moment form also forces zero mean. Atomic limits have infinite
information and cannot occur at a positive-mass well under(5).

Apply weighted Cauchy-Schwarz again:

```
(k+1)² >= sum p_j I(q_j) >= sum p_j/s_j
        >= (sum p_j a_j)²/S = (k+1)²/S >= (k+1)².        (6)
```

All inequalities are equalities. Therefore S=1, each q_j is centered
Gaussian, and a_j s_j is the same positive constant. Equation(3) fixes
that constant to1/(k+1), proving(1). This identifies every subsequential
limit and therefore the full conditional sequence when the label masses
converge. It also proves E g²/delta ->1: an asymptotically optimal sequence
uses all the available sixth-moment slack, even though feasibility allowed
an inequality cap.

## 3. Why convergence is TV and W2, not just weak

Equality in(3) rules out escaped slack. More explicitly choose compact
cutoffs increasing to1 in each label chart. The integrals of
g(r_j+sqrt(delta)y)²/delta against them converge, and their limiting sum
increases to1. The total integral is at most1, so the omitted nonnegative
tail integrals vanish uniformly as the chart radius tends to infinity.
Equation(2) bounds y² by16/(9k²) times this integrand. Thus second moments
are uniformly integrable in the charts. This establishes W2 convergence
at every positive-mass well. It also shows vanishing-mass cells carry no
asymptotic slack; their normalized shape is still unconstrained.

For total variation, define the unnormalized chart density on its expanding
cell by f_delta,j(y)=sqrt(delta)p_delta(r_j+sqrt(delta)y).
On every fixed compact interval its square root has bounded H1 norm:
the derivative energy is bounded by delta I(p_delta)/4 and its L2 norm
by1. One-dimensional local Rellich compactness gives strong local L2
convergence of the square roots along subsequences, hence local L1
convergence of densities. The already established tightness supplies the
tails. Divide by the converging positive cell mass to get TV convergence.
We do not extend the conditional density by zero and incorrectly assign it
finite global Fisher information; jumps at cell boundaries are irrelevant
to this compact-interior argument.

The same exhaustion in(5) shows the energy allocated to each positive-mass
cell tends to p_j a_j(k+1) after multiplying by delta. There is no spare
leading energy in tails or vanishing-mass cells. No quantitative rate follows
from these compactness arguments.

## 4. Executed consumers and contrary controls

**Actual optimizer.** K1874's unique even minimizer meets the sharp value
law, so all three cells have positive limiting mass. At k=4 the central
mass is3/4 and each outer mass1/8; the rescaled variances are1/20 and1/40.
The central variance is twice either outer variance. K1876 found this ratio
inside a trial family; the present result proves it for the exact optimizer.

**Asymmetric near-minimizers.** In K1876's exactly matched trial, replace the
equal outer weights w/2,w/2 by eta*w,(1-eta)*w for any fixed eta in[0,1].
All even moments are unchanged exactly, as is the mixing upper bound
(1+w)/t. The sharp lower bound then proves the same optimal leading cost.
The limiting outer masses are eta/k and(1-eta)/k. Thus ratio-optimality
does not imply asymptotic evenness. At eta=0 or1 one outer well disappears.
A mean-zero constraint would force equal limiting outer masses, but it is
not among the present constraints. This prevents an overstrong universal
Gaussian-mixture claim while preserving the exact even optimizer result.

**General simple-well transfer.** The proof of(3)-(6) applies to a finite
set of simple zeros r_j of a C1 function g, provided a global bound
g²>=c distance² holds, the label masses converge to prescribed p_j, and
E g²<=delta. Let A=sum p_j|g'(r_j)|>0. If delta I -> A², every
positive-mass local profile is N(0,1/[A|g'(r_j)|]), with TV and W2
convergence by the same compactness and no-loss argument. This is a
conditional rigidity theorem; it does not assert that every extra moment
constraint admits a sequence attaining A². Multiple zeros, uncontrolled
tails, or a vanishing slope fall outside its assumptions.

**Qualitative stability.** For the fixed even three-well problem, there
exists a modulus tending to0 for the sum of the three TV and W2 profile
errors as delta and |delta I-(k+1)²| tend to0. Otherwise a violating
sequence contradicts the theorem. This supplies no computable modulus,
finite precision budget or spectral gap. Those require a new effective
localization/deficit argument rather than another leading value calculation.

## 5. Verification and limits

The producer checks17 symbolic identities and2 upstream pins. The separate
probe uses rational allocation/distance/variance controls and deliberate
coefficient/reference faults, with mathematical checks separated from
reporting. Sampling supplements, but does not prove, the continuum result.
The analytic compact-test, compactness, moment-tail and equality arguments
above carry the theorem; no proof assistant or external expert is claimed.
Hostile review specifically tests non-even competitors, missing sign weights,
rare wells, escaped second moments, equality versus cap inequality, truncated
density boundary jumps and qualitative versus effective convergence.
Source, physics-ledger and canon verdicts do not change.
