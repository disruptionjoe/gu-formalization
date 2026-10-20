---
title: "K1823: uniform collars and local persistence of the global scalar optimizer"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: scalar two-radius Gaussian channels; explicit compactness interval and existential uniqueness neighborhood only
---

# A common compact domain extends the fixed-q theorem

For the symmetric unit-variance two-radius scalar family including its
continuous three-point and Rademacher faces, every
`q in Q=[1/1024-10^-13,1/1024+10^-13]` has an attained global minimum in one
explicit common compact rectangle. Its minimum value is continuous, Lipschitz
and strictly increasing on Q. Combining this compactness with K1820's unique
nondegenerate global minimum proves a unique smooth global minimizing branch
on **some smaller open neighborhood** of `q=1/1024`. Its radius is not
quantified. Uniqueness throughout all of Q is **not** proved. On all Q the
boundary-inclusive minimum equals the infimum over the regular open chart;
attainment in that strict interior is proved only on the smaller neighborhood.

This is repository-derived scalar variational mathematics. It supplies no GU
action, physical state, quotient, observation map, prediction or confirmation.
The proof reuses the fixed-q numerical certificates, performs no new quadrature
or global numerical cover, and makes no novelty or canon claim.

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
result: uniform-q compactness, monotone minimum value and qualitative global optimizer persistence
carrier: symmetric unit-variance two-radius scalar input laws and Gaussian output densities LAYER=toy CHIRALITY=N/A
pairing: relative Fisher integral against Lebesgue measure ON=real_observation_line
real_structure: real scalar variables, positive mixture probabilities and positive Gaussian noise
grading: parameter differentiation and boundary collars; no physical grading
action_owner: repository-construction -- scalar trial functional; no source action
target: parameter-dependent global minimum in the declared scalar chart MAP-TYPE=evaluation
```

## Inputs and new question

[K1751--K1755](k1751-k1755-two-radius-rectangular-domain-wave-2026-10-13.md)
give the chart and fixed rational candidate:

```
p=c/(c+z^2), a=1-z, b=1+c/z, u=2-c,
P(X=+/-sqrt(a))=p/2, P(X=+/-sqrt(b))=(1-p)/2,
t=sqrt(q/u), v=1-t, Y=sqrt(t)X+sqrt(v)Z.
```

The regular interior is `0<c<2-q`, `0<z<1`; the effective Rademacher face
`c=0` and three-point face `z=1` are included by their continuous laws.
`E X^4=1+c`, and the output fourth cumulant is exactly `-q`. Define
`J(q,c,z)=integral (rho'+y rho)^2/rho dy`.

[K1756--K1760](k1756-k1760-two-radius-boundary-collar-wave-2026-10-13.md)
give the fixed-q named gap, rare-atom variational estimate and zero-noise
entropy estimate. [K1820](k1816-k1820-full-fisher-slab-three-leafwise-wave-2026-10-13.md)
gives the unique interior global optimizer at q0 with positive Hessian. Its
[independent transfer review](k1820-independent-certificate-review-2026-10-20.md)
supports the correlated transfer while reusing upstream numerical quadrature,
tails and outer covers. The new manifest pins these inherited input bytes.

The new question is whether minimizers can escape as q varies, and whether a
remote competing minimum defeats local continuation. K1731's local expansion
and the fixed-q theorem alone do not settle that question.

## 1. Parameter derivative using fourth moments

Let `r=(log(rho/gamma))'` be the relative score. With OU time `s` and
`t=exp(-2s)`, Fisher dissipation gives

```
dJ/ds=-2J-2 E[(r')^2],
J_q=(J+E[(r')^2])/(2q).                           (1)
```

The second equality uses `ds/dq=-1/(4q)` at fixed `(c,z)`. The first is the
one-dimensional Gaussian specialization in Fathi, Indrei and Ledoux,
*Quantitative logarithmic Sobolev inequalities*,
[equation (2.13), page 7](https://www.normalesup.org/~mfathi/docs/LSI14.pdf).
Finite Gaussian mixtures with positive noise justify the integrations and
differentiations by Gaussian decay. Direct conditional differentiation yields

```
r'=-t/v+t Var(X|Y)/v^2.
```

The score conditional-expectation inequality gives `J<=t/v`, using unit
output variance and `J=I(rho)-1`. Jensen gives
`E[Var(X|Y)^2]<=E[(E[X^2|Y])^2]<=E[X^4]<=3`.
Expand the square and drop its nonpositive cross term to obtain

```
0<=J_q<=(t/v+t^2/v^2+3t^2/v^4)/(2q).              (2)
```

This uses a fourth moment, not an uncontrolled sixth moment or a support bound
uniform in the disappearing rare atom. Its positive-noise and moment
hypotheses cannot be dropped.

## 2. Explicit interval and uniform collars

Set `h=10^-13`, `q_-=q0-h`, `q_+=q0+h`. The fixed rational candidate has
`u*=691835097/2000000000`, `c*=2-u*`, `z*=1127044207/2000000000`.
Exact checks give `q_->q0/2`, `256q_+<u*`, `256q_+<2`. Both named signals
therefore have `t<1/16`, `v>15/16` on Q. Equation (2) bounds each derivative by

```
1024*(1/15+1/225+768/50625)=1490944/16875<89.
```

K1756's outward decimal ball has lower endpoint greater than `2.20e-10`.
The mean-value bound applied to the two named channels gives, on all Q,

```
J(R;sqrt(q/2))-J(q,c*,z*)>2.20e-10-178h=2.022e-10. (3)
```

Now split the entire domain at `t=31/32`:

- For `t>=31/32`, K1758 gives `J>=-log(v)-2log(4)>=log(2)>1/2`.
  The exact inequality `289q_+<u*` keeps the candidate below `1/16`.
  This excludes the zero-noise collar including its joint rare corner.
- For `t<=31/32`, `z<=10^-34`, K1757 gives
  `J(q,c,z)>=J(R;t)-400000 sqrt(2z)`. Rademacher OU monotonicity and
  `t>=sqrt(q/2)` allow (3). Squaring positive rational quantities bounds the
  loss strictly below `6e-12`. The gap remains greater than `1.962e-10`.

Because `t>=31/32` means `c>=2-(1024/961)q`, every minimizer belongs to

```
K=[0,C] x [10^-34,1],
C=2-(1024/961)q_-=18759765625001/9384765625000.      (4)
```

Using **q_-** makes K contain all q-dependent residual rectangles. Exact
inequalities give `C<2-q_+` and `q_+/(2-C)<(32/33)^2`, so K lies inside
every admissible chart and has `v>1/33`. Do not claim `v>=1/32` on this
larger common rectangle. The rational candidate lies strictly inside K.
Outside K one of the strict collar comparisons excludes every competitor
to that candidate.

## 3. Attainment, continuity and monotonicity on all Q

On `Q x K` all component means are bounded because `z>=10^-34` bounds b,
although the bound is enormous. Noise stays uniformly positive. The density
and its y derivative are continuous even at `c=0` and `z=1`. The posterior
score gives `|r(y)|<=A+B|y|` uniformly on this compact parameter set.
Gaussian tails with bounded means then dominate `rho(y)r(y)^2` by one
integrable function. Dominated convergence proves joint continuity of J.
This does not identify arbitrary weak convergence with Fisher continuity.

Thus `V(q)=min_K J(q,c,z)` exists and equals the boundary-inclusive family
minimum. Continuity and density of regular interior points show that it also
equals the infimum over `0<c<2-q, 0<z<1`. No uniform exclusion of the
three-point face `z=1` has been proved on all Q, so strict-interior attainment
on all Q is not asserted. On K,
equation (2) gives

```
0<=J_q<=L=(32+1024+3*1024*1089)/(2q_-)
          =5577440000000000000/3255208333.         (5)
```

Evaluating at the two endpoint minimizers proves
`|V(q2)-V(q1)|<=L|q2-q1|`. This is a conservative uniform continuity bound,
not a practical sensitivity estimate.

The fourth cumulant of Y is `-q`, so its density is not standard Gaussian.
Zero relative Fisher would force precisely that Gaussian density; hence
`J>0` and (1) gives `J_q>0`. For `q2>q1`, choose a minimizer x2 at q2:

```
V(q2)=J(q2,x2)>J(q1,x2)>=V(q1).                   (6)
```

Strict monotonicity uses the same common K and does not assume uniqueness
of the minimizer throughout Q.

## 4. Qualitative unique global branch and its sensitivities

K1820's x0 is an interior, unique global minimum at q0. Its positive Hessian
is in `(t,z)` coordinates. At a stationary point the `(c,z)` Hessian is its
congruence by the coordinate Jacobian; `t_c=t/(2(2-c))` is nonzero, so it
too is positive definite. This coordinate argument is made at the root,
not for a nonstationary point where extra Hessian terms would appear.

Near x0 the atom probabilities and squared radii are strictly positive.
Local Gaussian domination permits smooth parameter differentiation. The
implicit function theorem supplies a unique smooth stationary branch x(q).
Choose a small closed convex ball B around x0 inside the interior of K.
Hessian continuity makes the x-Hessian positive on B for q sufficiently near
q0; x(q) stays inside B.

The global step is the strictly positive exterior gap

```
g=min_{x in K\int(B)} J(q0,x)-J(q0,x0)>0.          (7)
```

Its existence follows from compactness and K1820's **unique global** minimum,
not just its local Hessian. Joint continuity, or (5) together with continuity
of x(q), preserves a positive exterior gap for q sufficiently near q0.
Inside B strict convexity gives the unique minimum x(q). Outside K the
uniform collars exclude all competitors. Consequently some
`0<delta<=10^-13` gives a unique smooth global minimum whenever
`|q-q0|<delta`.

No numerical g, quantitative delta, or uniqueness on all Q is supplied. This
qualitative composition avoids a new numerical outer-sublevel bank; a useful
quantified uniqueness interval still needs quantitative exterior-gap and
local parameter/Hessian control. On the smooth branch,

```
V'(q)=J_q(q,x(q))>0,
x'(q)=-[H_x J(q,x(q))]^-1 grad_x J_q(q,x(q)).       (8)
```

These are sensitivity formulas, not computed sensitivities. They imply no
sign for the individual coordinate derivatives and no convexity of V.

## Controls, review and reproduction

```
python3 tests/channel-swings/k1823_uniform_q_collar.py
python3 tests/channel-swings/k1823_uniform_q_collar_probe.py
```

The producer checks thirteen rational inequalities, inherited identities,
input hashes and the exact manifest. The probe independently differentiates
Gaussian closed forms with rational dual numbers for eighteen cases, tests
three fourth cumulants and checks boundary constants. Non-unit Gaussian
variances in these controls test the OU identity only; they do not enter the
unit-variance chart theorem.

Contrary constructions test necessary proof hypotheses. On the noncompact
line `F(q,x)=x^2(1-qx)^2-q^2x^2`, zero is the unique nondegenerate global
minimum at q=0 and remains a strict local minimum for small q. Nevertheless
`F(q,1/q)=-1`, so local IFT alone misses an escaping competitor. On a compact
interval containing +/-1, `(x^2-1)^2+qx` has two nondegenerate minima at q=0;
the q term immediately distinguishes their values. Compactness cannot
replace baseline uniqueness. Ten manifest mutations reject stronger
uniqueness, wrong constants, omitted inputs and scope claims. Such reporting
checks are not ten independent mathematical proofs.

Preflight selected OU/moment control over a new numerical bank, compactness
over a merely local IFT argument, and scalar scope over a physical claim.
Duplicate search found K1731's local expansion and K1820's open family
condition, not this common-compactness composition. Postflight's strongest
overclaim is a quantitative uniqueness interval; its strongest contrary
route is an escaping or tied minimum, excluded by the explicit hypotheses.
The weakest inherited seam remains the fixed-q quadrature, tails and outer
cover. These are reused, so the new result earns no stronger acceptance grade
than its inputs. Source/physics ledgers, canon and arbitrary-law optimization
remain unchanged.
