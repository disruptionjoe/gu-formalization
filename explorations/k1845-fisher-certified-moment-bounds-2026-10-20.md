---
title: "K1845: a certified unrestricted Fisher interval at fourth moment two"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: rigorous unrestricted scalar moment bound and score residual; no GU physics or quantified restricted-family gap
---

# The unrestricted Fisher minimum at k=2 lies in a rational interval

For the even all-density problem in K1843, with second moment1 and fourth
moment2, exact rational certificates prove

```
1.751458 < F(2) < 1.752673.                                  (1)
```

The lower endpoint is a whole-line rational score certificate, also a rigorous
quartic ground-energy lower bound. The upper endpoint is an exactly feasible
positive polynomial-times-Gaussian density with an algebraically specified
coefficient. No numerical quadrature, mesh or truncated spectral matrix is
used in the final proof. An independent standard-library implementation
replays the polynomial root counts and Gaussian moment bounds.

This quantifies the unrestricted value, not the gap from the two-radius
optimizer. K1843 proves that gap is strictly positive, but no restricted value
at k=2 is certified here. K1820 and K1841 remain valid in their stated classes.
There is no GU physics, novelty, canon promotion or external acceptance claim.

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
result: strict rational interval for unrestricted F(2), a global affine dual bound and quantitative score residual
carrier: even probability densities on the real line with second moment1 and fourth moment2 LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |u'|² where p=u² ON=real_Sobolev_functions
real_structure: real positive density and square root
grading: none; polynomial degree only
action_owner: repository-construction -- scalar Fisher functional and quartic dual operator
target: unrestricted moment-constrained Fisher infimum MAP-TYPE=evaluation
```

## 1. Why an exact algebra certificate replaces a spectral computation

K1843 supplies attainment, uniqueness and the exact quartic dual. It does not
supply a numerical eigenvalue, a moment fit or a truncation error. Before
building those, test a factorization bound valid on the entire line. A rational
score can make that test a polynomial nonnegativity certificate. A polynomial
Gaussian square gives moments and Fisher energy by exact Gaussian integration.
The classic Fisher/Schrodinger connection is described by
[Flego, Plastino and Plastino](https://arxiv.org/abs/1106.2078); no novelty is
claimed. The coefficients and full-domain certificate below are explicit.

An initial analytic trial p proportional to exp(-x6), rescaled to variance1,
has kurtosis2: Gamma(1/6)Gamma(5/6)=2pi and Gamma(1/2)²=pi. Its Fisher value is
60 pi^(3/2)/Gamma(1/6)^3, approximately1.9372 (display only). This already
produces an exact feasible density, but is substantially improved below.
The recurrence/reflection identities are standard
[NIST DLMF5.5](https://dlmf.nist.gov/5.5). This preliminary trial is not needed
by the final rational enclosure.

Numerical optimization discovered candidate coefficients only. Its grids,
objective values and solver success flags do not enter the proof. The final
inputs are the exact rational strings in the manifest; no optimization is
rerun by the certificate. Object searches found no existing named-k unrestricted
certificate; prior restricted Gaussian banks are not reused as unrestricted
lower bounds.

## 2. Whole-line lower certificate

Let y=x², and define

```
N(y)=a+b y+d y²,       D(y)=1+c y+e y²,
g(x)=x N(x²)/D(x²),
(a,b,d,c,e)=(-26379/25000, 12003/10000, 137193/500000,
             266879/500000, 43447/2000000).
(A,B,C)=(-84469/40000, 9487187/1000000, -1406001/500000).
```

D is strictly positive on y>=0. Direct differentiation gives

```
2g'-g² = H(y)/D(y)²,
H=2ND+4y(N'D-ND')-yN²,
P=H-(A+B y+C y²)D².                                       (2)
```

The exact coefficient list of P, in increasing degree, is

```
281/200000
-902460897/50000000000
733987487174629/10000000000000000
-49665576022693809/500000000000000000
230091322477253189/4000000000000000000
-2328629824747307/160000000000000000
2654026271095809/2000000000000000000
```

Exact Sturm division gives zero roots on (0,infinity); P(0)=281/200000>0.
Hence P(y)>0 for every y>=0. This is a full half-line root count, not sampled
positivity or a claim that all coefficients are positive. The two implementations
compute the polynomial independently and agree on its rational coefficients.

For any admissible finite-Fisher density p=u², integration by parts yields

```
I(p) = integral (2u'+g u)² + integral (2g'-g²)p
     >= A+B E X²+C E X4.
```

g grows at most linearly and g' is bounded. H1 regularity of u, its finite
second moment and cutoff integration justify the identity without requiring
p to be positive or its classical score to exist everywhere. The boundary
cutoff term is controlled by the second-moment tail; Cauchy bounds the cross
term. Infinite-Fisher densities obey the lower bound trivially. In particular,

```
F(2) >= A+B+2C = 875729/500000 = 1.751458.                    (3)
```

K1843's attained minimizer and strictly positive P make this inequality strict.
Equivalently the confining quartic operator
`-4d²/dx²-Bx²-Cx4` has bottom energy at least A, by the same square-completion
form inequality. Its natural form domain is H1 intersect L2(x4 dx).
Thus(3) is a genuine dual certificate despite never solving the eigenproblem.
It is not an assertion that these are the optimal dual multipliers.

## 3. Exactly feasible upper certificate

Let Z0 be a standard Gaussian variable, and set

```
p_t(y)=1+t y+(713/20000)y²+(63623/20000000)y³
          +(58657/1000000000)y4+(75509/10000000000)y5.
P_t(x)=p_t(x²),
Z(t)=E[P_t(Z0)²],       M(t)=E[Z0² P_t(Z0)²],
Q(t)=E[Z0^4 P_t(Z0)²], E(t)=E[(2P_t'(Z0)-Z0 P_t(Z0))²].
```

All expectations are exact polynomials in t, using E Z0^(2j)=(2j-1)!!.
Define t to be the unique root of

```
T(t)=Q(t)Z(t)-2M(t)²=0
```

inside the rational interval

```
522063/1765921 < t < 313828/1061549.                         (4)
```

The two endpoints have opposite T signs; Sturm counting gives exactly one
root between them. No rounded coefficient is substituted for t. All
coefficients of P_t are positive, so it never vanishes. Define Y with density
P_t(y)² times the standard Gaussian density divided by Z(t), let m=M(t)/Z(t),
and let X=Y/sqrt(m). Then X is even, smooth, strictly positive, variance1,
and exactly fourth moment2 by T=0. Its Fisher information is exactly

```
I(X)= E(t) M(t)/Z(t)².                                     (5)
```

This follows by differentiating the Gaussian square root, then using
I(Y/sqrt(m))=m I(Y). The producer evaluates rational termwise interval bounds
on(4); the independent replay uses rational Horner interval arithmetic.
Both certify(5) < 1752673/1000000. Decimal display of the producer's much
narrower trial interval is [1.75267253958317,1.75267253959254], but the rational
endpoints in the manifest, not those rounded displays, are the evidence.
The manifest also stores T's exact coefficients for independent comparison.

This trial is not the optimum. Its square root is a positive degree10
polynomial times a Gaussian, with a variance rescaling. Its Euler ratio
-4u''/u grows quadratically, whereas K1843's optimizer has a nonzero confining
quartic coefficient. Thus the two cannot coincide. This is a strict upper
bound by exact feasibility, not a fitted near-stationary solution.

## 4. Executed consequences: budget and score certificates

Equation(2) proves the reusable affine dual bound

```
F(k) >= A+B+C k,       1<k<3.                               (6)
```

The single tangent candidate is not the global value curve. Together with
K1843's monotonicity, (1) implies the relative Fisher budget needed for q=1
(k=3-q=2) lies strictly between0.751458 and0.752673. Budget at or below the
lower endpoint cannot achieve q=1; the displayed trial achieves q=1 at a
budget strictly below the upper endpoint. This does not compare two-radius
and unrestricted budget roots quantitatively.

Let p* be K1843's unique minimizer, rho*=p*'/p*. Keeping the completed square
rather than discarding it gives

```
I(p*)-L = E_p*[(rho*+g)²] + E_p*[P(X²)/D(X²)²],
L=875729/500000.
```

The positive residual and upper trial bound imply

```
E_p*[(rho*+g)²] < 243/200000 = 0.001215,
sqrt(E_p*[(rho*+g)²]) < 0.035.                              (7)
```

The same non-strict bound applies to any feasible p with I(p)<=U, using the
weak square-root formulation at zeros. This is an explicit weighted score
approximation, not a total-variation, density-error or spectral-gap theorem.
It is a useful consequence of the existing two bounds and needs no fitted
moment multipliers. A density distance would require an additional stability
inequality on the declared reference domain.

## 5. Validation, hostile review and remaining work

```
sage -python tests/channel-swings/k1845_fisher_certified_moment_bounds.py
python3 tests/channel-swings/k1845_fisher_certified_moment_bounds_probe.py
```

Producer:17 exact algebra/root/interval groups. Independent replay:31 rational
controls, including5 genuine certificate-input faults and3 separate reporting
faults. The replay implements polynomial arithmetic, Sturm division and Horner
intervals using only Fraction and standard-library code; it does not import the
producer, Sympy or Sage. It first checks planted positive-root polynomials and
the clean certificate, then corrupts score/minorant coefficients, primal
coefficients, the root bracket and the asserted upper bound. Failing inputs
must fail mathematical predicates; crashes are not counted as detection.

Inline hostile review checks normalization and scaling, positivity at infinity,
zero handling in Sturm variations, root existence rather than a small residual,
weak integration by parts, exact moment equality, rational versus rounded
endpoints, and the distinction between a certified value bracket and a
restricted-family gap. K1843 attainment is used only to make the lower bound
strict and identify p*. No independent-agent or formal-proof verification.

Next useful scalar question is a certified restricted optimum at the same k
if the consumer needs a quantitative enlargement gain, or a new unrestricted
endpoint theorem. More decimals in(1) alone do not supply either result. A
spectral-gap/functional-inequality construction would be needed to convert(7)
into a density-distance theorem. Source/ledger/canon remain unchanged.
