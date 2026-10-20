---
title: "K1839: global Fisher merging and uniform skew coercivity"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: global endpoint merging and skew constraint; no compact optimal scaling, next global coefficient, uniqueness or effective onset
---

# Both radius displacements merge faster than the noise scale

For every global minimizing two-radius Gaussian mixture as delta=2-q tends
to zero, write r=c/z. Then

```
z/sqrt(delta) -> 0, r/sqrt(delta) -> 0,
c(z-r)/delta² -> 1/2.                                           (1)
```

A whole-line cubic score test excludes the last inward rare escape left by
K1837. A quadratic test then gives the skew constraint uniformly throughout
the remaining merging regime. This does not yet force K1835's compact
c/delta^(4/3), z/delta^(2/3) window. In particular its next coefficient and
window uniqueness are not promoted to global conclusions.

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
result: global endpoint scale exclusion, merging skew constraint and score saturation
carrier: symmetric unit-variance two-radius Gaussian mixtures as delta=2-q tends to zero LAYER=toy CHIRALITY=N/A
pairing: whole-line Fisher score integral and polynomial L2 projections ON=positive_real_densities
real_structure: real radii, Gaussian noise and positive mixture weights
grading: asymptotic radius and noise scales only
action_owner: repository-construction -- constrained scalar Fisher functional
target: global minimizing sequences in the declared two-radius family MAP-TYPE=evaluation
```

## 1. Inputs and exact moment inequalities

Use K1837's chart, repeated to fix all normalizations:

```
t=sqrt((2-delta)/(2-c)), v=1-t, r=c/z, p=r/(r+z),
A=sqrt(1-z) with probability p, sqrt(1+r) otherwise,
Y=eta sqrt(t) A+sqrt(v) Z, J=I(Y)-1.
```

eta is a fair sign and Z is standard Gaussian, independent. E Y²=1 and
E Y4=1+delta. Let Yplus=sqrt(t)A+sqrt(v)Z, X=Yplus-E Yplus, and
S=E X². Write mu_j=E X^j, kappa4=mu4-3S² and rho=f'/f for X's density.
The mixture is smooth and has Gaussian tails, so all following integration
by parts and finite polynomial moments are legitimate.

Set R=rho+X/S. Integration by parts gives E R²=I(Yplus)-1/S. With
g2=X²-S and g3=X³-3S X, E rho g2=E rho g3=0. Hence Cauchy-Schwarz gives

```
I(Yplus) >= 1/S + mu3²/[S²(mu4-S²)],                              (2)
I(Yplus) >= 1/S + kappa4²/[S² E(g3²)].                            (3)
```

These are lower bounds on the exact integral, not likelihood expansions.
The denominators are positive because v>0 gives full real support and the
polynomials are nonzero. A stronger two-by-two Gram inverse subtracts the
projection onto X; the simpler bounds suffice here. Score projection and the
Cramer-Rao variance bound are classical. See the
[Berkeley score and Fisher information notes](https://stat210a.berkeley.edu/fall-2024/reader/score-fisher.html)
for the underlying score/Cauchy-Schwarz method. Equations (2)-(3) follow from
the direct derivation above; no novelty claim.

For a centered two-atom latent variable with lower weight p and gap d>0,
plus independent N(0,v), exact identities are

```
S=v+p(1-p)d²,
mu3=p(1-p)(2p-1)d³,
kappa4=p(1-p)[1-6p(1-p)]d4,
mu6=15v³+45v² E(U²)+15v E(U4)+E(U6),
E(g3²)=mu6-6S mu4+9S³.                                         (4)
```

Here U is the centered latent variable, not the standardized observation.
These identities hold at arbitrary p in[0,1]; neither bound assumes a small
mixture weight or bounded separation.

## 2. Remove the last unbounded rare separation

Inherited results: K1831 gives c=o(delta); K1833 gives z->0 and the global
value J=4/delta-2+o(1) and eventual regular-interior minimizers; K1837 gives r=o(sqrt(delta)) and excludes every
finite positive accumulation of z/sqrt(delta). K1837 also gives an o(1)
upper bound on the Fisher loss from forgetting eta whenever positive means
stay at least1/2. That applies to all sequences considered below; its
whole-line Gaussian affinity estimate is uniform in the atom weights.
We reuse those proofs rather than Taylor-expand cross-sign tails.

Suppose, for contradiction, that a minimizing subsequence has
z/sqrt(delta)->infinity. Then r/z=c/z²->0 and p=r/(r+z)->0. Set
Lrad=sqrt(1-z)+sqrt(1+r), h=r-z and ell=c z/delta²>=0. Exact formulas are

```
S=1-sqrt(1-delta/2)(1-c/Lrad²)/sqrt(1-c/2),
kappa4=t² c[(r-z)²-2c]/Lrad4.                                  (5)
```

Thus S~delta/4 and kappa4~c z²/16. Taylor's theorem in (h,c), on one fixed
neighborhood of zero, gives

```
(1-c/Lrad²)/sqrt(1-c/2)=1+c h/8+O(c h²+c²).                     (6)
```

This is an ordinary analytic square-root expression with bounded derivatives;
its error is uniform in the relative sizes of r and z. With r/z->0 it implies
|S-v0|<=C c z, where v0=1-sqrt(1-delta/2). Since both variances are
comparable to delta,

```
1/S >= 1/v0-C ell.                                             (7)
```

The centered latent gap is O(z), variance O(c), and all its even moments
of order2j are O(c z^(2j-2)). From (4), v=O(delta), c=o(delta), and
z²>>delta, it follows that

```
E(g3²)<=C(delta³+c z4).                                        (8)
```

For example, the mixed term delta c z² is at most c z4 eventually; the
other Gaussian terms are O(delta³). Equations (3),(5),(7),(8), and the
uniform o(1) sign-forgetting loss give fixed constants C,k>0 such that

```
J-4/delta >= -3/2-C ell
             +k ell²/(delta/z²+ell z)-o(1).                    (9)
```

All constants are independent of the diverging noise-scaled separation.
If ell tends to zero, this lower bound is at least -3/2-o(1), already too
large. On any subsequence ell>=epsilon>0, the ratio of the positive term
to ell is at least k/[delta/(epsilon z²)+z], which tends to infinity.
It dominates the negative linear term, again contradicting the attained
constant -2. Every possible ell sequence has a subsequence of one of these
two forms. Therefore the divergent separation is excluded.

Together with K1837's finite-positive exclusion, this proves z/sqrt(delta)
->0 for all global minimizers. It is not an extrapolation of K1837's
exponentially growing likelihood remainder: the polynomial bounds (2)-(3)
have no such separation restriction. Both radii now merge faster than noise.

## 3. Released follow-through: a uniform global skew constraint

Now z,r=o(sqrt(delta)). Define the signed quantity

```
ell=c(z-r)/delta².
```

In this section ell can initially have either sign. Formula (6), the exact
variance (5), and v0=delta/4+delta²/32+O(delta³) imply

```
1/S=4/delta-1/2-2ell+o(1+|ell|).                               (10)
```

Here is the uniform error accounting. The numerator error after division
by delta² is bounded by a constant times
|ell|(|h|+delta)+(c/delta)². Expanding the reciprocal introduces a further
O(delta ell²)=o(1), because c=o(delta) and h=o(sqrt(delta)). Thus (10)
does not assume ell is bounded or assume the eventual minimizing powers.

Exact two-radius moments give

```
mu3=t^(3/2)c(r-z)/Lrad³=-(1+o(1))ell delta²/8,
kappa4=t² c[(r-z)²-2c]/Lrad4=o(delta²),
mu4-S²=2S²+kappa4=(1+o(1))delta²/8.                            (11)
```

These estimates remain valid at p near0,1 or1/2. The centered gap is
o(sqrt(delta)) on both sides; no small-weight expansion is used. Combining
(2),(10),(11) with sign-forgetting yields

```
J-4/delta >= -3/2-2ell+2(1+o(1))ell²+o(1+|ell|).               (12)
```

A minimizing sequence has bounded left side, so the quadratic term forces
ell bounded. With bounded ell, the right side is

```
-2+2(ell-1/2)²+o(1).
```

The global upper value is -2+o(1). Consequently ell->1/2, proving (1).
This is a uniform statement over global minimizers, not a compact parameter
window or a chosen trial family. It also proves eventual inward skew z>r.

## 4. Further consequences and the still missing next scale

The positive-lobe variance and Fisher excess now obey

```
S=v0+delta²/16+o(delta²)=delta/4+3delta²/32+o(delta²),
I(Yplus)-1/S -> 1/2.                                          (13)
```

The exact projection coefficient a=mu3/[S(mu4-S²)] satisfies delta a->-2.
The remainder of the quadratic score projection is nonnegative and equals

```
E[(rho+X/S-a(X²-S))²]
 = I(Yplus)-1/S-mu3²/[S²(mu4-S²)] -> 0.                         (14)
```

This is an L2 score-saturation statement for the centered positive lobe,
not a pointwise density expansion or a global density-ratio estimate.

Also put u=r/z. Since eventually0<u<1,

```
c(z-r)=z³ u(1-u), u(1-u)<=1/4,
liminf z/delta^(2/3) >= cube_root(2),
c/delta^(3/2) -> infinity.                                    (15)
```

The last limit follows from c(z-r)~delta²/2 and z=o(sqrt(delta)).
These are useful one-sided restrictions but not compactness of both scaled
parameters. In particular u may approach0 or1 while z/delta^(2/3) grows.
Those cases still satisfy the leading skew relation with suitable choices;
(1) by itself cannot exclude them. They are not asserted to be minimizers.

K1835's optimized compact-window value and unique local branch remain valid
inside their original hypotheses. To promote their delta^(2/3) coefficient
globally, control the fourth and higher cumulant cost against that sharper
upper bound uniformly as u->0 or1 and as the scaled radii escape. The present
lower bound loses precisely that next-order information. No actual global
powers, next coefficient, global uniqueness or effective onset are claimed.

## 5. Released instrument: an exact all-domain fifth-cumulant lower bound

The next-order question needs more than the separate inequalities above. A
joint score projection can retain their correlations without any asymptotic
expansion. Define four centered polynomials

```
q1=X,
q2=X²-S,
q3=X³-3S X-mu3,
q4=X4-6S X²+3S²-4mu3 X-kappa4.
```

Their score covariances are exactly (-1,0,0,0): the subtraction of4mu3 X
in q4 is essential. Let G_ij=E(qi qj). Each entry is an explicit polynomial
in the first eight Gaussian-mixture moments, serialized in the certificate.
G is strictly positive definite for v>0 because no nonzero linear combination
of these degree1-through4 polynomials vanishes on the real line. The full
score projection gives the exact bound

```
I(Yplus)>= (G^-1)_11 = det(G[2:4,2:4])/det(G).                  (16)
```

The indicated submatrix uses one-based inclusive indices. In particular,
G_14=mu5-10S mu3=kappa5. Unlike a compact-window score expansion, (16) is
valid for every mixture weight and separation with v>0. Enlarging the test
space cannot lower the bound. The independent controls include all centered
and derivative expectations and exact positive LDL pivots at rare, balanced,
and reversed weights. The full-support argument, not finite samples, proves
invertibility for all inputs.

This supplies an executable next-order lower-bound instrument without claiming
that its optimizing asymptotics have been solved. It must still be estimated
uniformly against K1835's sharper upper bound at escaping scales; merely
substituting a fixed minimizing family would not close that gap.

## 6. Reproduction and hostile review

```
sage -python tests/channel-swings/k1839_fisher_global_merging_coercivity.py
python3 tests/channel-swings/k1839_fisher_global_merging_coercivity_probe.py
```

The producer checks exact centered Gaussian-mixture moments, Gram inverse,
radius variance/cumulants, square completion and escape-rescaling identities.
A separate rational probe computes moments directly at several weights/noise
levels, including rare/reversed atoms, checks the positive Gram determinants,
and tests asymptotic bounds on rational radius sequences. Those finite controls
support the algebra; the written uniform estimates and subsequence argument
prove the continuum conclusion. Reporting mutations are separate and do not
certify a theorem. No old fixed-q numerical bank is replayed.

Hostile review checked score normalization I versus J, g3's nonzero mean,
positivity of the polynomial denominators, small-p versus arbitrary-p scope,
the ell->0 and ell-unbounded alternatives, uniform cross-sign loss, reciprocal
error without prior boundedness, and sharp one-sided radius constants. The
remaining compactness/next-order gap is explicit. No unresolved finding within
(1)-(15); no separate-agent or external review, scientific novelty claim,
source/physics ledger change or canon promotion. This result is GU-independent.
