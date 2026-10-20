---
title: "K1835: next Fisher endpoint coefficients and a unique compact-window branch"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: uniform compact scaling windows and explicit global upper bounds; no exclusion of escaping scales or global shape uniqueness
---

# The best fixed merging family can be improved again

Put delta=2-q and e=delta^(1/6). K1833's fixed improved family has

```
J=4/delta-2+(3/8)delta^(2/3)+(3/10)delta+O(delta^(4/3)).
```

An explicit moving-parameter family improves this to

```
J=4/delta-2+(3/8)delta^(2/3)-(6/5)delta+O(delta^(4/3)).  (1)
```

This supplies a global upper bound, and excludes the earlier fixed family
from exact optimality sufficiently near the endpoint. We also prove a unique
minimizing branch inside any fixed compact positive scaling window containing
the limiting parameters in its interior. Its value has expansion(1).
Whether the unrestricted global minimizers remain in such a window is open.
Thus neither the next *global* coefficient nor global minimizing powers are
proved. The model is the repository's scalar Gaussian-mixture problem, with
no source-physics interpretation or novelty claim.

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
result: uniform next endpoint expansion, improving witness and unique compact-window minimizer
carrier: symmetric unit-variance two-radius Gaussian channels at delta=2-q tending to0 LAYER=toy CHIRALITY=N/A
pairing: Fisher score integral and Gaussian Hermite inner product ON=real_observation_line
real_structure: positive real mixture densities and exact real algebraic parameters
grading: endpoint asymptotic powers; no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: compact scaling-window minimum and global upper bound MAP-TYPE=evaluation
```

## 1. Same chart, with the scaling assumption explicit

Use K1833's chart, without changing the moment constraint:

```
c=a e8, z=b e4, p=a/(a+b²), h=a/b-b,
t=sqrt((2-e6)/(2-c)), v=1-t,
A=sqrt(1-z) with weight p, sqrt(1+c/z) with weight1-p,
Y=eta sqrt(t) A+sqrt(v) Z, J=I(Y)-1.
```

Here eta is a symmetric sign and Z standard Gaussian. Fix (a,b) in a compact
subset of (0,infinity)². Uniformly on that set, the parameters are admissible
for sufficiently small e>0. The exact constraints E Y²=1 and E Y4=1+e6
hold. K1833 proves the global value4/delta-2+o(1), eventual interior minimizers
and z->0; it does not give compactness of a=c/delta^(4/3) and b=z/delta^(2/3).
That is the sole scaling hypothesis for the window theorem below.

Define

```
x=a h, y=a(h²-2a), w=a h(h²-8a).
```

The uniform expansion is

```
J=4/e6-2+2(x+1/2)²+(2/3)y² e2+C(a,h)e4+O(e6),       (2)
C=-(5a h²+2a²)/4-3a²h³+w²/6-5x²y.                  (3)
```

The remainder is uniform with any fixed finite number of parameter derivatives
on a smaller compact set. This derivative assertion is used below, and is
justified in section3 rather than inferred from formal coefficients.

## 2. Exact coefficient derivation

Write Yplus=sqrt(t)A+sqrt(v)Z, m=E Yplus, s²=Var Yplus,
and U=(Yplus-m)/s. The centered latent squared-radius variable W takes
values -b,a/b, has mean0, and satisfies W²=hW+a. Thus
E W²=a, E W³=x, E W4=a(h²+a), and its fifth cumulant is w.
Expanding sqrt(1+e4 W) gives

```
s²=e6/4+(1/32-x/8)e12+(5a h²+2a²)e16/64+O(e18),
kappa3(U)=x e3-(3/4)a h² e7+O(e9),
kappa4(U)=y e4+O(e8), kappa5(U)=w e5+O(e9).
```

Let H_n denote probabilists' Hermite polynomials. For f the density of U,
write R=f/phi. Its leading terms are x e3 H3/6+y e4 H4/24+w e5 H5/120.
There are additional H6,H7 terms, but orthogonality removes their linear
cross terms with the lower Hermites at the orders used here. The exact score
integral D=integral phi (R')²/R has

```
D=(x²/2)e6+(y²/6)e8+
  [-(3/4)a h² x+w²/24-(5/4)x²y]e10+O(e12).          (4)
```

The last term is the reciprocal-density correction. It uses
E[H2 H3²]=36 and E[H2² H4]=24; omitting the denominator in Fisher's
integrand would miss it. Because I(U)=1+D, I(Yplus)=(1+D)/s².
Combining(4) and the reciprocal variance yields(2)-(3).
All odd powers vanish: changing e to -e reflects the standardized density,
leaving D and the Fisher value unchanged.

At a0=1/2,h0=-1,b0=(1+sqrt(3))/2, x=-1/2 and y=0. Exact higher jets give

```
s²=e6/4+3e12/32+3e16/64-e18/128+O(e20),
D=e6/8+9e10/32-e12/20+O(e14),
J=4/e6-2+3e4/8+3e6/10+O(e8).                       (5)
```

These are exact rational coefficients even though b0 and the atom weights
are algebraic. The independent probe obtains them entirely over Q using the
recurrence for W moments, without the producer's explicit two-atom shifts.

## 3. Why these are Fisher expansions, uniformly with derivatives

On a compact positive (a,b) set, both weights are bounded away from0.
After dividing s by e3, the standardized component means and common noise
variance extend smoothly and analytically in e near0; the means are O(e)
and variance1+O(e2). They and any fixed number of parameter derivatives are
uniformly bounded. Restrict e so the variance lies in[3/4,5/4]. Derivatives of
each Gaussian density divided by itself, including mixed spatial, e and
parameter derivatives, are polynomials in the standardized variable with
uniformly bounded coefficients. A derivative of the positive mixture divided
by that mixture inherits a polynomial bound by summing the component ratios.
The mixture itself is bounded by C exp(-u²/4). Consequently all derivatives
needed in integral (f'+u f)²/f are dominated by an integrable polynomial
times that Gaussian. Taylor expansion under the integral is valid uniformly,
including parameter derivatives. Through order14 and parity it gives the
remainders in(4)-(5), after division by s². Increasing the finite derivative
order justifies the smooth remainder needed for the implicit function theorem.

The symmetric two-lobe Fisher value differs from the positive-lobe value
by a flat term, uniformly with these derivatives. Each positive mean stays
in[1/2,3/2], the variance v is comparable to e6, and the cross-sign Fisher
mixing deficit has integrand

```
[f_plus f_minus/(2(f_plus+f_minus))] (score_plus-score_minus)².
```

The bracket is at most sqrt(f_plus f_minus)/4. Each fixed derivative adds
only polynomial powers of u and e^-1: component logarithmic derivatives
have that bound, and mixture logarithmic derivatives are weighted averages
or finite products of such terms. Gaussian affinity between opposite-sign
components is bounded by exp(-k/e6), with k>0 uniform on the compact set.
Polynomial-weighted affinities have the same bound with a smaller positive k.
Thus every fixed derivative of the deficit is O(e^-N exp(-k/e6)), flat at0.
The full symmetric value has a smooth extension after its explicit leading
pole is removed. It need not be analytic; smoothness suffices below.
No uniform relative-density Taylor approximation at arbitrarily large u is
being asserted. No sampled quadrature supplies the remainder.

## 4. The next coefficient in every nondegenerate scaling window

For any sequence (a_e,b_e) staying in a fixed compact positive set,

```
liminf [J-4/e6+2]/e4 >=3/8.                          (6)
```

To prove it, take a subsequence with finite liminf. Formula(2), bounded C
and nonnegative squares force x+1/2=O(e2) and y=O(e).
Every accumulation point then has x=-1/2,y=0. Solving these equations with
a>0 gives a=1/2,h=-1 and the unique positive b=b0. Hence C->3/8.
The nonnegative remaining squares prove(6). More precisely, if
(x+1/2)/e2->alpha and y/e->beta, the limit equals
3/8+2alpha²+(2/3)beta². If the compact set contains(a0,b0), the fixed
witness attains the upper limit3/8. This proves the sharp window coefficient.
It is not a proof of the same coefficient for sequences escaping every such
compact set. K1833's c=o(delta), z->0 does not imply the required compactness.

## 5. Follow-through: unique window optimizer and a strict explicit improvement

Use u=x+1/2,y as local coordinates near(a0,h0). Their Jacobian in(a,h) is
[[-1,1/2],[-1,-1]], with determinant3/2, so this is a nonsingular chart.
Taylor expansion through the next even order gives, uniformly with derivatives,

```
J-4/e6+2=2u²+(2/3)e2 y²+e4 C(u,y)+e6 K(u,y)+O(e8),
C(0,0)=3/8, C_u(0,0)=-4, C_y(0,0)=-2, K(0,0)=3/10.
```

The Hessian is diag(4,(4/3)e2)+O(e4), hence positive definite throughout a
fixed sufficiently small convex (u,y) neighborhood for all small e>0.
Set u=e4 U,y=e2 Y. Divide the two first-derivative equations by e4.
At e=0 they become 4U-4=0 and (4/3)Y-2=0, with invertible Jacobian.
The smooth implicit function theorem supplies a unique critical branch with

```
u=e4+O(e6), y=(3/2)e2+O(e4),
a=1/2-e2/2+O(e4), h=-1-e2+O(e4).                    (7)
```

It is a strict minimum. For any fixed compact positive scaling window
containing(a0,b0) in its interior, minimizers exist; comparing with(5) and
using(2) forces all of them into this neighborhood. Strict convexity there
proves uniqueness within the window, and(7) applies. This does not assume or
prove that unrestricted global minimizers stay in the window.

Substitution gives its value(1). The gain at order e6 is the exact square
completion

```
3/10-2 beta+(2/3)beta² = -6/5+(2/3)(beta-3/2)²,
```

where beta is now y/e2 (distinct from the y/e scaling in section4).
The u optimization first affects order e8. An explicit admissible family
attains the value through e6 without solving the implicit equations:

```
a(e)=(1-e2)/2, h(e)=-1/(1-e2),
b(e)=(-h(e)+sqrt(h(e)²+4a(e)))/2,
c=a(e)e8, z=b(e)e4.
```

Here x=-1/2 exactly and y=(3/2)e2+O(e4). Direct exact Gaussian jets also
verify(1), independently of the local optimization argument. The fixed
K1833 family loses to this one by (3/2)delta+O(delta^(4/3)), a strictly
positive amount for small delta. Neither family is asserted to be the exact
global optimizer; the implicit branch differs from the explicit witness at
higher orders. The value in(1) is a rigorous asymptotic upper bound on V.

## 6. Verification, scope and next decisive test

```
sage -python tests/channel-swings/k1835_fisher_next_endpoint_coefficient.py
sage -python tests/channel-swings/k1835_fisher_next_endpoint_coefficient_probe.py
```

The producer integrates shifted-Gaussian Hermite score jets in an exact
quadratic field and tests(2)-(3) at distinct rational parameters. The separate
probe reconstructs standardized moments from W²=hW+a over Q, then obtains
Hermite coefficients from raw moments; it independently verifies the fixed
and improved values, the Fisher denominator terms and the optimizing squares.
Reporting fault tests are labeled separately. The written uniform derivative
bounds, compactness argument and implicit-function proof are essential analytic
evidence; polynomial controls alone do not prove those steps.

Inline hostile review checked the mixture normalization, Fisher versus relative
Fisher, the two different beta scalings, flat cross-lobe derivatives, the singular
Hessian's e2 order, and the compact-window hypothesis. No second-agent review,
physical interpretation, source/ledger change or canon promotion. The earlier
sharp global constant and eventual interior/merging theorems remain intact.

The decisive next question is scale tightness: can an unrestricted minimizer
escape a=c/delta^(4/3),b=z/delta^(2/3) compactness while matching or beating(1)?
A uniform rare/merging-atom lower bound at order delta^(2/3), not another
fixed-family Taylor coefficient, would settle that premise. Conversely a
verified escaping-scale witness would refute this branch's global optimality.
Finite-q uniqueness and effective endpoint onset remain separate open questions.
