---
title: "K1841: global Fisher endpoint scaling and eventual unique optimizer"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: global endpoint asymptotics and eventual uniqueness in the two-radius scalar family; no effective onset, all-q uniqueness or physical interpretation
---

# The compact-window optimizer is eventually the global optimizer

For the symmetric unit-variance two-radius Gaussian-mixture family, put
delta=2-q. There is a delta0>0 such that, for every 0<delta<delta0, the
global minimizing shape (c,z) is unique. Its parameters and value satisfy

```
c = (1/2)delta^(4/3) - (1/2)delta^(5/3) + O(delta²),
z = ((1+sqrt(3))/2)delta^(2/3) + (1/2)delta + O(delta^(4/3)),
V(2-delta) = 4/delta - 2 + (3/8)delta^(2/3)
                         - (6/5)delta + O(delta^(4/3)).             (1)
```

The new step is uniform scale tightness. A cubic score projection excludes
both escaping shape ratios without a likelihood expansion or a compact-window
assumption. It places every global minimizer inside the hypotheses of K1835,
whose existing local optimization theorem then applies globally. The onset
delta0 and the constants hidden in O are not numerically certified. This is
GU-independent mathematics, not a source-physics result or a novelty claim.

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
result: global endpoint scale tightness, eventual unique optimizer, value and inverse-budget asymptotics
carrier: symmetric unit-variance two-radius Gaussian mixtures as delta=2-q tends to zero LAYER=toy CHIRALITY=N/A
pairing: whole-line Fisher score integral and polynomial L2 projection ON=positive_real_densities
real_structure: positive real weights and noise, real radius parameters
grading: endpoint asymptotic powers only; no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: all global minimizers in the declared scalar family MAP-TYPE=evaluation
```

## 1. Inputs, object and noncircular proof order

Use the existing chart, with r=c/z:

```
t=sqrt((2-delta)/(2-c)), v=1-t, p=r/(r+z),
A=sqrt(1-z) with probability p, sqrt(1+r) otherwise,
Y=eta sqrt(t) A+sqrt(v) Z, J=I(Y)-1.
```

The sign eta is fair and independent of standard Gaussian Z and A.
The constraints E Y²=1 and E Y4=1+delta hold exactly. The domain is
0<=c<delta, 0<z<=1, with the boundary-inclusive interpretation of K1825.
That result supplies existence. K1833 supplies eventual regular-interior
minimizers; K1839 supplies, for every selection of exact global minimizers,

```
c=o(delta), z,r=o(sqrt(delta)),
H=z-r>0 eventually, ell=cH/delta² -> 1/2.                       (2)
```

These are the only global localization inputs. In particular, neither
c=O(delta^(4/3)) nor z=O(delta^(2/3)) is assumed.
K1835's explicit trial family supplies the global upper bound

```
V(2-delta)-4/delta+2 <= M delta^(2/3)                            (3)
```

for one fixed M and all sufficiently small delta. We use this upper bound,
prove compactness, and only then use K1835's compact-window derivative,
convexity and implicit-function theorem.

Let Yplus=sqrt(t)A+sqrt(v)Z, X=Yplus-E Yplus, S=E X² and
L=sqrt(1-z)+sqrt(1+r). Exact identities inherited from K1839 are

```
S=1-sqrt(1-delta/2) F(H,c),
F(H,c)=(1-c/L²)/sqrt(1-c/2),
L²=2-H+2sqrt(1-H-c),
mu3=E X³=-t^(3/2)cH/L³,
kappa4=t²c(H²-2c)/L4.                                         (4)
```

We need a stronger sign-forgetting estimate than an unspecified o(1).
Under (2) the positive component means eventually lie in[1/2,3/2] and
v~delta/4. The exact Gaussian-mixture Fisher deficit, bounded by the
sum of opposite-sign pair affinities as in K1837 section5, is at most
C v^-2 exp(-1/(16v)). There are only four pairs, and no lower bound on
the mixture weights is required. Consequently fixed C,N,k>0 give

```
0 <= I(Yplus)-I(Y) <= C delta^(-N) exp(-k/delta).                (5)
```

This is smaller than every power used below. We do not obtain (5) merely
by reusing the weaker o(1) conclusion of K1839.

## 2. A uniform cubic score lower bound

Standardize W=X/sqrt(S). Denote its cumulants of orders3,4,5,6 by
alpha,beta,gamma,xi. Write rho for its score, and R=rho+W. Then
E R W=0 and D=E R²=I(W)-1. Consider

```
q2=W²-1-alpha W,
q3=W³-3W-alpha-beta W.
```

Both are centered and orthogonal to W. Integration by parts gives
E R q2=alpha and E R q3=beta. Their exact Gram entries are

```
A2=2+beta-alpha²,
B2=6alpha+gamma-alpha beta,
C2=6+9beta+9alpha²+xi-beta².                                   (6)
```

The Gram matrix is positive definite: the density has full real support,
and independent polynomials of degrees2 and3 cannot vanish almost surely.
Projecting R onto their span and completing the square gives

```
D >= alpha²/A2
       + (beta-alpha B2/A2)²/(C2-B2²/A2).                      (7)
```

This is an exact all-domain inequality. The centered latent two-point
variable has standardized gap sqrt(t)(z+r)/(L sqrt(S))=o(1) under (2).
Its fixed-order cumulants of orders at least3 therefore tend to0, and
independent Gaussian noise has no such cumulants. Thus beta,xi=o(1).
More sharply, the exact fifth-to-third cumulant ratio is

```
gamma/alpha = t(H²-8c)/(L² S) = o(1).                         (8)
```

Here alpha is nonzero eventually because cH>0. Also (2),(4) and S~delta/4
give alpha²=O(delta). Consequently A2->2, B2=O(alpha), and
C2-B2²/A2->6. Fixed bounds on these quantities give

```
alpha²/A2 >= alpha²/2-C alpha²(|beta|+alpha²).
```

For the other term of (7), use (b-d)²>=b²/2-d², positive upper and
lower bounds on its denominator and alpha B2/A2=O(alpha²). Thus

```
D >= alpha²/2 + k beta² - C(alpha²|beta|+alpha4)                 (9)
```

for fixed k,C>0. The exact gamma/alpha bound matters: convergence of the
Gram matrix alone would leave an uncontrolled error at the required scale.
This argument uses the fifth cumulant to control a correlation, not as a
separate fifth-order expansion of the Fisher integral.

For an explicit eventual inequality, once A2>=1,
3<=C2-B2²/A2<=9 and |B2|<=8|alpha|, the same proof gives
D>=alpha²/2+beta²/18-alpha²|beta|/2-(64/3)alpha4.
These conditions eventually hold by the established limits. This specifies
usable constants in this step, not an effective delta at which they hold.

## 3. Uniform variance errors, including escaping ratios

F in (4) is analytic on a fixed neighborhood of H=c=0. Its value at
c=0 is1, its first c derivative at the origin is0, and its mixed H,c
coefficient is-1/8. Taylor's theorem, retaining the factor c, gives

```
F(H,c)=1-cH/8+O(cH²+c²).                                      (10)
```

Because ell is bounded and c=o(delta),

```
S=delta/4+delta²/32+cH/8+O(delta³+delta² H+c²),
S-delta/4=O(delta²),
1/S=4/delta-1/2-2ell+O(delta+H+c²/delta²).                     (11)
```

The second line follows before expanding the reciprocal: cH=O(delta²),
H=o(1), and c²=o(delta²). The squared reciprocal error is then O(delta).
The exact third moment also gives

```
alpha²/(2S)=t³ ell² delta4/(2 L6 S4)
           =2ell²+O(H+delta).                                (12)
```

Indeed t=1+O(delta), L²=4+O(H+c), c=o(delta), and
S=(delta/4)(1+O(delta)). No optimizing power has been assumed.
Divide (9) by S, use alpha²=O(delta), combine (5),(11),(12), and
subtract1. After changing constants if necessary,

```
J-4/delta+2 >= 2(ell-1/2)² + k beta²/delta
                         - C(H+c²/delta²+|beta|+delta).        (13)
```

This holds along every minimizing sequence under (2), including r/z tending
to0 or1. The retained c² term is essential near the latter boundary.

## 4. Elementary coercivity forces compactness

The exact fourth cumulant in (4) gives

```
beta=Q ell(H-2c/H), Q=t² delta²/(L4 S²) ->1.                   (14)
```

Both ell and Q are eventually bounded above and away from0. Set x=H and
y=c/H, so x²y=ell delta². Since min(x,2y)³<=2x²y,

```
x+2y=|x-2y|+2min(x,2y)
    <=|x-2y|+2(2ell)^(1/3)delta^(2/3).
```

Also c²/delta²=ell y. Consequently (14) implies

```
H+c²/delta² <= C(delta^(2/3)+|beta|).                          (15)
```

Use (15) in (13), compare with (3), discard the nonnegative square,
and absorb C|beta| into (k/2)beta²/delta+C' delta by Young's inequality.
It follows that

```
beta² <= C delta^(5/3),
H+c²/delta² = O(delta^(2/3)).                                 (16)
```

Therefore H=O(delta^(2/3)) and c=O(delta^(4/3)). Their matching lower
bounds follow from cH=ell delta² and ell bounded away from0. This proves
compact positive scaling without assuming r/z stays away from either end.

Moreover beta/delta^(2/3)->0. Put hbar=H/delta^(2/3) and
abar=c/delta^(4/3). Every accumulation point satisfies

```
abar hbar=1/2, abar(hbar²-2abar)=0, abar>0, hbar>0.
```

The unique solution is hbar=1, abar=1/2. Since the scaled quantities are
compact, the whole collection converges. From z=(H+sqrt(H²+4c))/2,

```
H/delta^(2/3)->1, c/delta^(4/3)->1/2,
z/delta^(2/3)->(1+sqrt(3))/2,
r/delta^(2/3)->(sqrt(3)-1)/2.                                 (17)
```

We began with an arbitrary sequence of exact minimizers. Failure of uniform
eventual localization would give a violating sequence and contradict (17).
Thus all global minimizers eventually lie in any fixed positive compact
scaling window containing this limit in its interior.

## 5. Released consequence: global uniqueness and sharp value

Apply K1835 on one such fixed window. With e=delta^(1/6), a=c/e8,
b=z/e4, h=a/b-b, define u=ah+1/2 and y=a(h²-2a). K1835 proves,
uniformly with the needed parameter derivatives near the limit,

```
J-4/e6+2=2u²+(2/3)e2 y²+e4 C(u,y)+e6 K(u,y)+O(e8),
C(0,0)=3/8, C_u(0,0)=-4, C_y(0,0)=-2, K(0,0)=3/10.
```

Its Hessian is diag(4,4e2/3)+O(e4), positive definite on a fixed
sufficiently small convex (u,y) neighborhood for all small positive e.
The rescaled stationarity equations have an invertible limiting Jacobian.
The implicit-function theorem gives the unique minimizing branch

```
u=e4+O(e6), y=(3/2)e2+O(e4),
a=1/2-e2/2+O(e4), h=-1-e2+O(e4).                              (18)
```

By (17) all global minimizers eventually enter that neighborhood, and they
are interior by the inherited theorem. They must equal its unique critical
point. This proves eventual global uniqueness and (1). K1835's derivative
domination and flat cross-sign estimates are used only after compactness;
no expansion has been extended to an escaping window.

Direct substitution in (18) additionally gives

```
r=((sqrt(3)-1)/2)delta^(2/3)-(1/2)delta+O(delta^(4/3)),
p=(1-1/sqrt(3))/2-delta^(1/3)/(2sqrt(3))+O(delta^(2/3)),
v=delta/4-delta^(4/3)/8+delta^(5/3)/8+O(delta²).                (19)
```

These are optimizer parameters, not a fitted trial family. Uniqueness refers
to the lower/upper-radius chart; permuting mixture labels does not create
another distribution. It is an eventual endpoint statement, not all-q
uniqueness or a numerical value of delta0.

## 6. Further follow-through: inverse budget and local stability

K1825 supplies the monotone value transfer and unique q_B for a positive
Fisher budget B. Inverting (1), with delta_B=2-q_B, gives

```
delta_B=4/(B+2)+3*cube_root(2)/(B+2)^(8/3)
                   -96/[5(B+2)³]+O(B^(-10/3))
       =4/B-8/B²+3*cube_root(2)/B^(8/3)
                   -16/(5B³)+O(B^(-10/3)).                    (20)
```

This is an asymptotic scalar budget formula, not a certified finite-B interval.
For example, in w=B+2, substituting delta=4/w+Aw^(-8/3)+Dw^-3 gives
A=(3/8)4^(5/3)=3*cube_root(2) and D=16(-6/5)=-96/5.

On the fixed small convex (u,y) neighborhood above, the same Hessian bound
also supplies fixed positive k,K such that

```
k[(u-u*)²+e2(y-y*)²] <= J(u,y)-V
                     <= K[(u-u*)²+e2(y-y*)²].                 (21)
```

Taylor's integral-Hessian formula and stationarity prove both bounds; the
order-e4 mixed terms are absorbed by the two diagonal scales. A value error
epsilon inside this neighborhood therefore gives |u-u*|<=C sqrt(epsilon)
and |y-y*|<=C delta^(-1/6)sqrt(epsilon). The neighborhood is a hypothesis:
we have not silently extended the exact-minimizer localization theorem to
arbitrary near-minimizers or all finite-q perturbations.

## 7. Evidence, contrary routes and limitations

```
sage -python tests/channel-swings/k1841_fisher_global_scaling.py
python3 tests/channel-swings/k1841_fisher_global_scaling_probe.py
```

The producer checks exact Gram, cumulant, variance-jet and scaling identities.
The separate probe constructs rational Gaussian-mixture moments directly,
computes polynomial projections, checks positive Schur pivots and the
coercivity inequality in both extreme ratio regimes, and tests the budget
coefficients. Reporting mutations are separate. These algebraic controls do
not alone prove uniform estimates or uniqueness; sections2-5 supply the
analytic argument.

The producer passes41 exact algebraic identity groups. The independent probe
passes498 rational controls, including36 Gaussian-mixture fixtures, and
rejects8 reporting faults. These are different evidence kinds and are not
combined into a theorem-verification percentage.

Preflight rederived the useful work from the open condition. A degree-four
Gram determinant, a full uniform density expansion and more fixed-family
jets were considered. The cubic projection is sufficient because an exact
fifth/third cumulant ratio controls its correlation, and its fourth-cumulant
cost already forces compactness. It removes both escaping regimes without
the higher-degree optimization. Those two ratio limits are the substantive
contrary constructions, not cases excluded by a window assumption.

Postflight examined I versus J, polynomial centering and orthogonality, Gram
positivity, gamma/alpha, the c² variance error, flat sign-forgetting loss,
sequential-to-uniform quantifiers and using K1835 only inside its proven
window. A separate mathematical review independently rederived the Gram
bound, error scaling, coercivity and transfer, including the derivative and
strict-convexity hypotheses, and found no unresolved issue in the stated
theorem. That review is an argument check, not an additional computational
reproduction or a proof-assistant check. Earlier notes'
open global-compactness/endpoint-uniqueness statements are historical and
superseded by this scoped proof. No effective threshold, all-q uniqueness,
larger mixture-family optimality, source/physics inference, novelty, external
acceptance or canon promotion is claimed.

Next scalar work is effective onset/error control or behavior away from this
endpoint. Further fixed-family jets or repeated escape exclusions would not
address either question.
