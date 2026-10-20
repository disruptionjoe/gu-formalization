---
title: "K1827: sharp Fisher growth at the two-point endpoint"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: uniform Fisher endpoint asymptotic and sufficiently-high-q Rademacher-face exclusion; no explicit transition threshold, full minimizing shape or unrestricted-density attainment
---

# The endpoint cost is 4/(2-q), with bounded additive error

Let V(q) be K1825's minimum relative Fisher information in the symmetric
unit-variance two-radius Gaussian-channel family, including its boundary
faces, and put delta=2-q. For every 0<q<2,

```
4/delta - 551/27 <= V(q) <= 4/delta - 3/2.                 (1)
```

The lower bound may be negative away from the endpoint; replace it by its
maximum with zero if desired. In particular

```
V(q)=4/(2-q)+O(1),   (2-q)V(q) -> 4 as q increases to 2.  (2)
```

This is uniform over q-dependent shapes, including rare or merging atoms.
The Rademacher channel is asymptotically optimal in value ratio, but is
**not a local minimum for every sufficiently high q<2**: a feasible inward
atom perturbation lowers its Fisher value. The threshold is existential,
not computed. The same leading constant
and bounded additive error hold for the infimum over **all centered
unit-variance densities with fourth moment 3-q and finite weak-score Fisher
information**. No finite-q minimizing density or attainment theorem for that
larger class is asserted.

If V(q_B)=B>0, the immediate inverse consequence is

```
4/(B+551/27) <= 2-q_B <= 2(1+2B)/(1+B)^2.                 (3)
```

Thus `2-q_B=4/B+O(B^-2)`. This scalar information constraint supplies no
GU physical observable. Source, physics-ledger, grade and canon statuses
remain unchanged.

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
result: sharp endpoint Fisher-value growth and uniform inverse-budget bracket
carrier: real centered unit-variance densities with fourth moment 1+delta; two-radius Gaussian outputs as subclass LAYER=toy CHIRALITY=N/A
pairing: ordinary and Gaussian-relative Fisher integrals against Lebesgue measure ON=real_observation_line
real_structure: real scalar variables and real weak score
grading: moment order and parameter asymptotic; no physical grading
action_owner: repository-construction -- moment-constrained scalar variational functional; no source action
target: endpoint minimum-value asymptotic, not minimizing-shape classification MAP-TYPE=evaluation
```

## 1. Question and prior inputs

K1825 gives all-q existence and strict value monotonicity for the two-radius
family. Its entropy collar proves divergence at q=2 with a logarithmic lower
rate. The question here is the actual rate, uniformly over changing shapes.
A fixed-shape small-noise expansion cannot answer it: c<2-q forces c to zero,
while z may shrink at a related rate.

K1825's chart gives

```
E X=0, E X^2=1, E X^4=1+c,
Y=sqrt(t)X+sqrt(1-t)Z, t=sqrt(q/(2-c)),
E Y=0, E Y^2=1, E Y^4=3-q=1+delta.
```

Every such output has a smooth positive density and finite Fisher information.
Write ordinary score s=rho'/rho, ordinary Fisher I=E s^2, and relative
Fisher J=E(s+Y)^2. Integration by parts gives `E[Ys]=-1`, hence `J=I-1`.

The score integration-by-parts identity is classical. See
[Nourdin, Peccati and Swan (2014), Definition II.1, equation (1), and
Definition II.3](https://orbi.uliege.be/bitstream/2268/192581/1/NPS14-formatIEEE.pdf)
for weak-score and Fisher conventions. Cauchy--Schwarz gives the usual
score-test information inequality below. This note supplies the explicit
clipped test and endpoint consequences; it makes no literature novelty or
external acceptance claim. K1825 is reused for the family minimum and its
unique inverse parameter. No earlier numerical q0 certificate or quadrature
bank is needed here.

## 2. A uniform fourth-moment bound

Assume a density with weak score s, finite `I=E s^2`, `E Y^2=1` and
`E Y^4=1+delta`, delta>0. Centering is retained in the applications, although
this calculation itself only needs the second moment. Define

```
g(y)=clip(2y,-1,1),   f(y)=(y^2-1)g(y)/2.
E f^2 <= E(Y^2-1)^2/4 = delta/4,
f'(y)=|y|       for |y|>1/2,
f'(y)=3y^2-1    for |y|<1/2.                             (4)
```

f is continuous and locally Lipschitz. Its junction values are -3/8 at
+1/2 and +3/8 at -1/2, so its weak derivative has no point masses.
Equation (4) is an almost-everywhere statement; f is not differentiable
at those junctions. For `0<=x<=1/2`,

```
x-(3x^2-1)=13/12-3(x-1/6)^2 <= 13/12.
P(|Y|<1/2) <= (16/9)delta,
E(|Y|-1)^2 <= E(Y^2-1)^2=delta,
E|Y| >= 1-delta/2.
```

The probability bound uses `(Y^2-1)^2>9/16` on the central interval.
Consequently

```
E f' >= 1-A delta,   A=1/2+(13/12)(16/9)=131/54.          (5)
```

For weak-score integration, multiply f by smooth cutoffs chi_R and
approximate the corners locally. Fourth-moment finiteness gives `f in L2`
and the derivative bound gives `f' in L1`. The cutoff derivative term tends
to zero, bounded by a constant times `R^-1 E[|f| 1_(|Y|>R)]`; Cauchy--Schwarz
handles the score term as `chi_R f -> f` in L2. Local mollification has no
boundary term because f is continuous. Therefore `E[sf]=-E[f']` and

```
I E f^2 >= (E f')^2,
I >= 4[1-A delta]_+^2/delta,
J >= max(0,4[1-A delta]_+^2/delta-1).                     (6)
```

Here `[x]_+=max(0,x)`. One cannot square a negative lower bound on E f'
as a bound on its absolute value; the probe plants that error on a Gaussian.
Since `[1-A delta]_+^2>=1-2A delta` for every delta>0, (6) implies

```
J >= 4/delta-C,   C=8A+1=551/27.                        (7)
```

The proof uses no sixth moment, support bound, atom separation, fixed noise
floor or fixed-shape limiting argument. Infinite Fisher satisfies the lower
bound trivially; the stated finite class makes the weak-score proof explicit.

## 3. Upper bound and sharp unrestricted-density envelope

The Rademacher signal R is allowed with `t0=sqrt(q/2)=sqrt(1-delta/2)`.
For `Y0=sqrt(t0)R+sqrt(1-t0)Z`, the conditional Gaussian score and Jensen give

```
I(Y0)<=1/(1-t0),
V(q)<=J(Y0)<=t0/(1-t0),
delta V(q)<=2t0(1+t0)<=4-(3/2)delta.                    (8)
```

The last step uses `sqrt(1-delta/2)<=1-delta/4`. Equations (7)-(8) prove
(1)-(2). Their additive constants are conservative, not a constant-term
asymptotic expansion. They do not prove `V=4/delta-3/2+o(1)`.

Let U(delta) be the infimum over all centered unit-variance densities with
fourth moment 1+delta and finite weak-score Fisher. For 0<delta<2, the
Rademacher Gaussian channel is in this class and the two-radius family is a
subclass, so

```
max(0,4[1-A delta]_+^2/delta-1)
    <= U(delta)<=V(2-delta)<=J(Y0)<=4/delta-3/2.
```

Thus U, V and J(Y0) all have leading term 4/delta with bounded additive
error, and `J(Y0)/V(2-delta)->1`. No finite-delta equality, existence,
uniqueness or optimizer characterization for U follows. At delta=0 the
moments force Y^2=1 almost surely, outside the density class.

## 4. Exact inverse bounds

K1825 gives exactly one q_B with V(q_B)=B for each B>0. Equation (7) gives
`delta_B>=4/(B+C)`. K1825's Rademacher bound gives
`q_B>=2[B/(1+B)]^2`, yielding (3). These rational bounds hold for every
positive B, without a small-delta assumption. Moreover

```
0<4/B-delta_B<=4C/[B(B+C)].                              (9)
```

The upper bound in (3) is strictly below 4/B, and (9) proves the inverse
O(B^-2) rate. The full bound (6) can tighten individual exclusions further.

## 5. Concentration does not select a minimizing shape

For any symmetric unit-variance W with fourth moment 1+eta, couple W to
its Rademacher sign (randomize the sign at zero). Then

```
W2(law(W),R)^2<=E(|W|-1)^2<=eta.
```

Every admissible signal has eta=c<delta and every output has eta=delta.
They all approach Rademacher in W2 as q increases to 2, whether optimal or
not. This does not determine z, split weights, c/delta, a local blowup profile
or exact boundary attainment.

For an exact contrary family let Z have density proportional to
`(1-z^2)^m` on (-1,1), integer m>=2, and let S be an independent Rademacher.
For 0<h<1 put

```
v=E Z^2=1/(2m+3), E Z^4=3/[(2m+3)(2m+5)],
Y_h=S(1+hZ)/sqrt(1+h^2 v),
I(Z)=m(2m+1)/(m-1), I(Y_h)=(1+h^2 v)I(Z)/h^2.
```

The two supports are disjoint. Exact moments give delta_h tending to zero
and `delta_h I(Y_h)->4v I(Z)>4`; at m=2 the limit is 40/7. These symmetric
density laws converge to Rademacher but are not asymptotically optimal in
Fisher ratio. Their weak score is valid at the support endpoints: the
density vanishes and m>=2 makes Fisher finite. The probe integrates their
polynomial moments and score-square numerator exactly. They are controls
on the unrestricted estimate, not asserted members of the two-radius
Gaussian-channel family.

## 6. High-q Rademacher instability despite ratio optimality

There exists q_star<2 such that for every q in (q_star,2), the Rademacher
face c=0 is not a local minimum in the two-radius family. Therefore every
attained family minimum there has c>0. This does not exclude the other
face z=1 or prove uniqueness or full open-chart attainment.

Fix z=3/4 and differentiate at c=0 from within `0<c<2-q`. Write
`t=sqrt(q/2)`, `m=sqrt(t)`, `v=1-t`, and let phi_v(y-mu) denote the
Gaussian density with mean mu and variance v. The baseline is
`rho0=[phi_v(y-m)+phi_v(y+m)]/2`. Differentiating the chart gives

```
p'(0)=16/9,  t'(0)=t/4,  v'(0)=-t/4,
outer_mean'(0)=19m/24,  inner_mean(0)=m/2.
```

The derivative of its positive-half mixture, whose reflection supplies the
negative half, is

```
h_plus=(16/9)[phi_v(y-m/2)-phi_v(y-m)]
       +(19m/24) partial_m phi_v(y-m)
       -(t/4) partial_v phi_v(y-m).                     (10)
```

For each fixed q<2, one-sided differentiation of Fisher is legitimate.
The noise stays positive in a small c-neighborhood, the inward component
lies between the two outer means, and component derivatives are bounded
by Gaussian densities times polynomials. The inward-to-baseline density
ratio at c=0 is bounded; nearby equal-variance component ratios and the
narrowing noise give local Gaussian domination. No common positive
c-neighborhood as q increases to 2 is asserted or needed.

The ordinary Fisher first variation is

```
partial_c I|_0 = integral G(y) h_plus(y) dy,
s0(y)=-y/v+(m/v)tanh(my/v),   G=-2s0'-s0^2.              (11)
```

G is even, so the two reflected halves have identical integrals. For the
single positive Gaussian set `G_plus=2/v-(y-m)^2/v^2`. Exact Gaussian
moments give

```
integral G_plus h_plus
  = -(16/9)(m/2-m)^2/v^2 + 0 + t/(4v^2)
  = -7t/(36v^2).                                       (12)
```

The zero term is the mean derivative: the centered square has zero first
mean derivative at the baseline. This strictly negative isolated-lobe
answer alone is not the two-lobe theorem; the overlap must be controlled.
Putting T=tanh(my/v), direct subtraction gives

```
G-G_plus=(T-1)[2my+m^2(T+1)]/v^2.                       (13)
```

For m>=1/2, split the line at y=m/4. Above that point,
`1-T<=2exp(-2my/v)`, so the integral of (13) against each term of (10)
is bounded by a polynomial in 1/v times `exp(-1/(8v))`.
Below it, both Gaussian means in (10) are at least m/2, at distance
at least m/4>=1/8 from the split. Absorb half their Gaussian exponent
into this distance and integrate the remaining polynomial moments.
Since G-G_plus is bounded by `C(1+y^2)/v^2` on the whole line and the
Gaussian derivatives add at most two inverse powers of v, this gives

```
|integral (G-G_plus)h_plus| <= C0 v^-4 exp(-1/(256v))      (14)
```

for some finite C0 independent of v in a sufficiently small interval.
The means remain in [1/4,1], so the required Gaussian moments are uniformly
bounded. This is a Gaussian-tail estimate, not a sampled quadrature claim.
The exponential in (14) dominates every power of v. Combining (12)-(14),

```
partial_c J|_0 = partial_c I|_0
              = -7t/(36v^2)+O(v^-4 exp(-1/(256v)))<0
```

for all sufficiently small positive v. The equality of J and I derivatives
uses the exactly preserved second moment; (10) independently gives
`partial_c E Y^2=-4t/3+19t/12-t/4=0`. A negative one-sided derivative
gives a feasible c>0 with lower value for each such q; choose c small enough
to satisfy c<2-q. This proves the face exclusion, with no explicit q_star
or uniform c step. It does not determine the size or ratio of the improvement.
The simultaneous ratio-optimality result is consistent: both values have
the same divergent leading term while their difference is subleading.

## 7. Verification, bookends and next question

```
python3 tests/channel-swings/k1827_endpoint_fisher_asymptotic.py
python3 tests/channel-swings/k1827_endpoint_fisher_asymptotic_probe.py
```

The producer records rational endpoint/inverse bounds and pins K1825. The
independent probe checks the clipped derivative, continuity at corners,
moment constants, ordinary/relative Fisher subtraction, negative-bound
Gaussian counterexample, exact compact-bump Fisher/moments, inverse
orientation, exact Gaussian first-variation coefficients and overlap identity,
and reporting mutations. Finite checks support the analytic
proof; they neither integrate V nor reprove K1825's attainment theorem.

**Preflight.** Information theory selected a uniform score test over a
fixed-shape expansion. The variational lens required rare/merging-atom
uniformity; weak analysis checked corners and cutoff; exact arithmetic
eliminated the need for a numerical bank. Duplicate search found earlier
small-q expansions, K1823's local continuation and K1825's logarithmic
endpoint, not this bound. The source lens classified the question as
independent scalar mathematics. Effective uniqueness and boundary stability
remain different questions with different quantitative inputs.

**Postflight.** The strongest overclaim is an explicit high-q transition
threshold, full shape uniqueness or a constant-term expansion; none is
asserted. The double-bump family
shows that the same limiting law can have a larger leading Fisher constant.
The decisive transfer seams are the nonsmooth test, fixed-q differentiation
at zero inward-atom weight, and the uniform two-lobe overlap bound.
Continuity, cutoff, local Gaussian domination and tail estimates are
explicit. Independent mathematical review found no defect in those
transfers. These results remain active research, without novelty,
canon, physics or source promotion.

Follow-through provides a global rational inverse bracket, the sharp
unrestricted-density asymptotic envelope, the nonoptimal-concentration
counterexample and an actual high-q boundary instability theorem. The next
scalar shape question is a **subleading** minimization or a quantitative
transition bound. It requires explicit overlap constants and a controlled
second c-variation, or a uniformly justified rescaled shape functional;
the first-variation sign alone cannot select the minimizing displacement.
An effective q0 uniqueness radius still requires its separate exterior gap
and q-Hessian bounds. Full minimizing-shape classification remains open.
