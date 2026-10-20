---
title: "K1825: global parameter attainment and Fisher value transfer"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all-q attainment including scalar boundary faces and value inequalities; no all-q interior attainment or uniqueness
---

# Every admissible positive parameter has a scalar minimum

For every `0<q<2`, the symmetric unit-variance two-radius Gaussian-channel
family, including its Rademacher and three-point faces, has an attained global
minimum `V(q)>0`. Its value is continuous and locally Lipschitz throughout this
interval. Moreover,

```
W(q) = V(q)/(1+V(q))/sqrt(q)
```

is strictly increasing. The fixed-q K1820 certificate therefore gives explicit
lower bounds at every larger q and upper bounds at every smaller q, together
with inverse exclusions for a prescribed Fisher budget. V maps (0,2)
continuously and strictly increasingly onto (0,infinity), so each positive
Fisher budget has exactly one threshold parameter. This uniqueness concerns
the parameter, not the minimizing shape. The proof needs no
new quadrature, exterior-gap computation or stationary-point cover.

This extends K1823's boundary-inclusive attainment beyond its small explicit
interval. It does **not** extend K1823's local uniqueness result: a boundary
face may minimize at other q, and multiple minimizers or nonsmooth changes of
minimizing shape are not excluded. The regular open chart has the same
infimum, but its attainment for all q is not asserted. Neither endpoint q=0
nor q=2 is included.

These are repository-derived scalar variational results. They supply no GU
action, state, physical observable, prediction, confirmation, arbitrary-input
optimizer or canon promotion. Source and physics-ledger dispositions remain
unchanged.

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
result: global-q attainment and normalized Fisher-value inequalities
carrier: centered unit-variance symmetric two-radius scalar laws and their Gaussian outputs LAYER=toy CHIRALITY=N/A
pairing: relative Fisher integral against Lebesgue measure ON=real_observation_line
real_structure: real scalar variables, nonnegative atom weights and strictly positive noise
grading: parameter differentiation and boundary faces; no physical grading
action_owner: repository-construction -- scalar variational functional; no source action
target: minimum-value function on 0<q<2 MAP-TYPE=evaluation
```

## 1. Objects, prior results and the structural choice

Use the existing chart

```
p=c/(c+z^2), a=1-z, b=1+c/z,
P(X=+/-sqrt(a))=p/2, P(X=+/-sqrt(b))=(1-p)/2,
u=2-c, t=sqrt(q/u), v=1-t, Y=sqrt(t)X+sqrt(v)Z.
```

The boundary-inclusive shape domain is
`D_q={0<=c<2-q, 0<z<=1}`. At c=0 this is the same Rademacher input
regardless of z; at z=1 the central two atoms coalesce. These are laws, not
four distinct atoms by assumption. Each output has mean zero, variance one
and fourth cumulant `-q`. Set `J(q,c,z)=integral (rho'+y*rho)^2/rho dy` and
`V(q)=inf_{D_q} J` initially, without assuming attainment.

K1757 supplies the same-sign coupling estimate and Fisher variational formula.
K1758 supplies the finite-support entropy collar. K1820 supplies the unique
interior global minimum at `q0=1/1024`, with the K1787 whole-line value ball.
K1823 supplies the OU derivative identity and fourth-moment derivative bound.
These dependencies are pinned by digest in the new manifest; their numerical
integrations and global cover are reused, not independently rerun.

The structural alternative to another parameter-dependent numerical bank is
compactification plus the classical Fisher convolution inequality. The
underlying inequalities are established mathematics, not a novelty claim:
[Stam (1959)](https://doi.org/10.1016/S0019-9958(59)90348-1) is the original
Fisher-information convolution reference. The score and scaling conventions
are also given in [Itoh (1989), pp. 9-10](https://www.ism.ac.jp/editsec/aism/pdf/041_1_0009.pdf).
The OU dissipation identity is the one-dimensional Gaussian case of
[Fathi, Indrei and Ledoux, equation (2.13)](https://www.normalesup.org/~mfathi/docs/LSI14.pdf).
The new work here is their explicit composition with this chart, its
noncompact boundary, and the inherited certified scalar value. No literature
novelty or specialist acceptance has been established.

## 2. A compactification for each q

Fix any `0<q<2`. The Rademacher input c=0 has
`t0=sqrt(q/2)<1` and relative Fisher at most `t0/(1-t0)`. Choose

```
B=4/(2-q), N=ceil(2B+10), epsilon=2^(-N),
C=2-q/(1-epsilon)^2.                                      (1)
```

Since `1/(1-t0)=2(1+t0)/(2-q)<B`, B strictly exceeds the Rademacher
candidate value. Also `2^N>=N+1>B+1`, so
`epsilon<1/(B+1)<1-t0`. Consequently `0<C<2-q`.

Every channel here has at most four input atoms, even when some coincide.
K1758's entropy argument gives

```
J >= -log(v)-2log(4).
```

For `v<=epsilon`, this is at least `(N-4)log(2)>(N-4)/2>=B+3`.
Here `log(2)>1/2` follows directly by integrating 1/x from 1 to 2.
Thus every competitor to the Rademacher candidate has `c<C`. The
zero-noise face and its joint rare-atom corner are excluded without taking
a density at v=0.

Compactify the remaining rectangle to `[0,C] x [0,1]`. On z=0, define the
output law to be the Rademacher channel at the limiting `t(c)=sqrt(q/(2-c))`.
K1757's same-sign coupling gives

```
W2(X_(c,z),R)^2 <= z+z^2 <= 2z.                          (2)
```

This proves weak convergence to that face, uniformly in c. At c=0 with
z>0, the vanishing inner weight and outer radius tending to one give the same
weak continuity. Away from these faces the finite mixture depends
continuously on its parameters, including the coalescing atoms at z=1.
The positive noise floor is uniform on the compact rectangle.

**The artificial z=0 face does not preserve the prescribed fourth moment
when c>0.** For example, along c=1 and z tending to zero,
`E X^4=2` while the weak limit is Rademacher with fourth moment one. No
fourth-moment continuity is used. This face is a compactness device and is
removed from the minimizing conclusion below.

For any probability law mu define the extended relative Fisher functional by

```
J(mu)=sup_{f in C_c^infty(R)} integral [2yf-2f'-f^2] dmu.   (3)
```

Each test integrand is bounded and continuous, so the supremum is lower
semicontinuous under weak convergence. For the smooth positive Gaussian
mixture densities here, integration by parts and density of smooth compactly
supported tests in L2(rho) identify (3) with the ordinary score integral.
Therefore the compactified objective attains a minimum. This argument uses
lower semicontinuity, not an assertion of Fisher continuity under arbitrary
weak convergence.

A minimizer on z=0 with c>0 cannot win: it is a Rademacher output with
`t(c)>t0`, and Rademacher relative Fisher strictly increases in t. This
follows already from OU dissipation, since the smoothed Rademacher law is
non-Gaussian. Its value strictly exceeds the allowed c=0 candidate. A point
c=0,z=0 is the same law as any allowed c=0,z>0 point. The compactified
minimum is therefore attained in D_q itself. Its value is positive because
an actual D_q output has fourth cumulant -q, while zero relative Fisher
would force the standard Gaussian.

Approximate any minimizing c=0 or z=1 face by regular shapes with c>0,z<1
and positive noise. At a fixed such face the component means stay bounded,
and ordinary Gaussian domination gives Fisher continuity along these
approximations. Hence the attained boundary-inclusive minimum equals the
infimum of the regular open chart. This gives no interior-attainment theorem
for all q.

## 3. Local Lipschitz continuity without a rare-support bound

Fix a compact parameter neighborhood `[a,b]` inside (0,2). The Rademacher
candidate is uniformly bounded by `4/(2-b)`. Use (1) with that upper bound
and one common N,epsilon. Every minimizer throughout the neighborhood has
noise at least epsilon and hence

```
u=2-c >= q/(1-epsilon)^2.
```

If q and q' are sufficiently close, specifically

```
|q'-q| < a*[((1-epsilon/2)/(1-epsilon))^2-1],              (4)
```

then a minimizing shape at either parameter is also admissible at the other,
and along the parameter interval its noise stays above epsilon/2.
This cross-admissibility is needed because D_q shrinks as q grows.

With `r=(log(rho/gamma))'`, K1823 gives

```
J_q=(J+E[(r')^2])/(2q),
J_q <= [t/v+t^2/v^2+3t^2/v^4]/(2q).                     (5)
```

The last bound uses `E X^4=1+c<=3`, not a support bound or a sixth-moment
bound. On the comparisons allowed by (4), it is at most

```
L=[2/epsilon+4/epsilon^2+48/epsilon^4]/(2a).
```

Evaluate J at each endpoint's minimizing shape and apply (5) along the
comparison interval. This gives `|V(q')-V(q)|<=L|q'-q|` locally.
The constant is conservative and can be huge; it proves local Lipschitz
continuity and thus continuity, not a practically tight sensitivity estimate.
This proof remains valid when the minimizing shape is not unique or changes
between a boundary and the interior.

## 4. Strict normalized transfer on the whole interval

For a centered unit-variance output, integration by parts gives

```
I(rho)=J+1,
E[r'] = 1-I(rho) = -J.                                   (6)
```

Jensen and (5) now imply

```
J_q >= J(1+J)/(2q).                                      (7)
```

Equality in Jensen would make r' constant everywhere, since rho is positive.
Then log rho is quadratic. Normalizability, zero mean and unit variance
would force rho=gamma, contrary to fourth cumulant -q. Thus (7) is strict
for every allowed shape at q>0. Equivalently,

```
d/dq [ J/(1+J)/sqrt(q) ] > 0.                            (8)
```

For `q1<q2`, the domains are nested: `D_q2 subset D_q1`. Take any attained
minimizer x2 at q2. Applying (8) to its fixed input law gives

```
V(q2)/(1+V(q2))/sqrt(q2)
  > J(q1,x2)/(1+J(q1,x2))/sqrt(q1)
  >= V(q1)/(1+V(q1))/sqrt(q1).                            (9)
```

This proves strict increase of W globally, without differentiating a
minimizer or assuming a unique branch. In particular V is strictly
increasing. By local Lipschitz continuity it is differentiable almost
everywhere, and at those points

```
V'(q) >= V(q)(1+V(q))/(2q).                              (10)
```

Strict increase does not justify replacing this almost-everywhere inequality
by a strict derivative inequality everywhere. Nor does it imply convexity or
smoothness of V.

For `lambda=sqrt(q2/q1)`, define

```
T_lambda(x)=lambda*x/[1+(1-lambda)*x].                    (11)
```

Equation (9) yields `V(q2)>T_lambda(V(q1))`. Its denominator is positive:
(9) places `lambda*V(q1)/(1+V(q1))` strictly below
`V(q2)/(1+V(q2))<1`. This is the relative-information form of the classical
Gaussian convolution/Stam comparison. Directly, if
`Y1=sqrt(theta)Y2+sqrt(1-theta)Z`, ordinary Fisher satisfies
`I1<=I2/[theta+(1-theta)I2]`; substituting I=1+J yields
`J1<=T_theta(J2)`. The two derivations provide a normalization check.

## 5. Consuming the fixed-q certificate

Let L0 and U0 be the exact rational endpoints of K1787's ball

```
[1.5917864530497670077445861802075968567e-7 +/- 3.19e-24].
```

K1820 proves that this is the global value V(q0), q0=1/1024. Then

```
q0<q<2:   V(q)>T_sqrt(q/q0)(L0),
0<q<q0:   V(q)<T_sqrt(q/q0)(U0).                          (12)
```

The second inequality may be seen by flowing the actual q0 optimizer to
lower q. That fixed shape remains admissible. There is no need to know its
coordinates more accurately. The first applies to all competitors at higher
q, not just a continuation of that optimizer. Its denominator stays positive
through q<2: `sqrt(2/q0)<46` and `45L0<1`.

The manifest saves six exact lower bounds at q=q0*n^2, n=2,4,8,16,32,45,
and six exact upper bounds at q=q0/n^2, n=2,4,8,16,32,64. For orientation,
the q=1 lower bound exceeds `5.0937e-6`; the q=1/4096 upper bound is below
`7.9590e-8`. These are global value bounds, not new optimizer certificates.

For an allowed budget Bf and q>q0, `V(q)<=Bf` implies

```
q < q0 * [ (Bf/(1+Bf))/(L0/(1+L0)) ]^2.                 (13)
```

Thus an entire parameter range can be excluded without solving its optimizer.
For Bf=10^-6 the exact rational cap is approximately
0.0385415968592, conservatively below 0.039. For Bf=2L0 it is strictly below
1/256. The endpoint q=q0 is handled separately; a low budget does not turn
(13) into an unsupported lower-q exclusion. These necessary conditions are
not claims that a budget is achievable below the cap.

## 6. A unique budget parameter, without shape uniqueness

For every q, the allowed Rademacher candidate and the universal entropy
bound give

```
0<V(q)<=t0/(1-t0),
V(q)>=-log(1-t0)-log(16),   t0=sqrt(q/2).                 (14)
```

For the second inequality, every shape has t>=t0, so v<=1-t0. The lower
bound may be negative at small q; its useful consequence is near q=2.
Equation (14) proves

```
lim_(q down to 0) V(q)=0,   lim_(q up to 2) V(q)=infinity.
```

Together with continuity and strict increase, this makes V a bijection
from (0,2) onto (0,infinity), with a continuous strictly increasing inverse.
For each budget Bf>0 there is one q_Bf with V(q_Bf)=Bf, and precisely the
parameters q<=q_Bf meet that budget at their minima. This is not a uniqueness
claim about the minimizer at q_Bf.

Inverting (14) gives the global analytic bracket

```
2*[Bf/(1+Bf)]^2 <= q_Bf <= 2*[1-exp(-Bf)/16]^2.           (15)
```

The bracket is conservative; both endpoints lie inside (0,2). Its left
endpoint follows by evaluating the Rademacher upper bound there. Its right
endpoint follows by evaluating the entropy lower bound. It is not a fitted
parameter or a physical observable.

The inherited value adds useful stronger bounds. For 0<Bf<U0, set

```
lambda_B = Bf*(1+U0)/[U0*(1+Bf)] < 1.
```

Then (12) gives V(q0*lambda_B^2)<Bf, so
`q_Bf>q0*lambda_B^2`. The manifest saves three exact examples. For Bf>=L0,
(13) supplies the complementary upper exclusion whenever q_Bf>q0;
the equality and below-q0 cases are kept separate. No newly sampled
parameter-dependent optimizer is needed for either bound.

## 7. Verification, limits and follow-through

```
python3 tests/channel-swings/k1825_global_q_fisher_transfer.py
python3 tests/channel-swings/k1825_global_q_fisher_transfer_probe.py
```

The producer checks seven exact rational compactification examples, twelve
certified-value transfers, six inverse-budget bounds and inherited
input digests. The mathematical probe checks the transfer independently via
ordinary Fisher convolution/scaling, semigroup composition and inverses;
independently checks chart normalization, cumulants and same-sign coupling on
rational-radius laws; tests a valid Gaussian equality case and a shifted
Gaussian counterexample to dropping centering; checks endpoint sequences for (14), and rejects malformed
constants, q-scaling and reporting claims. These finite controls do not
replace the analytic compactness and strictness proofs. Upstream numerical
quadrature, tails, local existence and fixed-q global composition are reused.

Preflight lenses chose weak compactification over a new global derivative
bank, and nested-domain comparison over an unjustified differentiation of
argmin. The optimizer and information-theory lenses agree on (11) through
different formulas. The contrary construction is the fourth-moment loss at
z=0,c>0; the proof explicitly removes that artificial face using Rademacher
monotonicity. A shifted Gaussian exposes the centering hypothesis in (6).
Duplicate search found K1757/K1758's fixed-q collar and K1823's local interval,
not the all-q attainment and nested-domain composition. The strongest
unresolved alternative remains a **useful** effective uniqueness interval;
it needs quantitative exterior-gap and q-dependent local derivative control.

Postflight's strongest overclaim is all-q uniqueness or interior attainment.
Neither follows from this proof. Its weakest inherited numerical seam is the
fixed-q value certificate used only by (12)-(13); the all-q attainment,
continuity and normalized monotonicity proof does not depend on that numerical
result. The global shape can change, and these value bounds do not identify
which shape minimizes. Immediate follow-through supplies (12)-(15), the unique inverse-value
parameter theorem and the almost-everywhere sensitivity restriction (10). Effective uniqueness, a
sharp parameter phase diagram, arbitrary-law optimization and physical
interpretation remain separate questions.


The strongest next scalar question is a useful quantitative uniqueness
interval for the minimizing **shape**, or a decisive boundary/interior
transition test. The inequalities above cannot answer either: a strictly
monotone value function can have multiple minimizers. The former requires
an effective exterior objective gap plus q-dependent root/Hessian control;
the latter requires a certified competing face value or stability condition.
The fixed-q certificates and all-q scalar value theorem remain reusable inputs.
Repeating rational transfers or shrinking a formal radius without those
quantitative inputs would not settle another independent scientific question.
