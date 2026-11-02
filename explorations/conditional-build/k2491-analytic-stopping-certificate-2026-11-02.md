---
title: "K2491 A practical exact certificate for the nondyadic stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematics on the declared supplied model; no native GU or measured implementation claim"
---

# K2491 A practical exact certificate for the nondyadic stopping frontier

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2491
carrier: original fresh half-test half-use absorbing experiment with failure-inclusive one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace for quantum states or actual-law expectation for classical trials ON=declared_carrier
real_structure: complex adjoint or real classical probability as specified
grading: target and complement or absorbing trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Jensen cost reduction, exact positive-polynomial bounds and a full-control stopping bracket MAP-TYPE=evaluation
```

## Result and Layer 0

For the original stopping law and target s=1/2, expected budget K=1/1000,

    5000/7309 <= F_(1/2)(1/1000) <= 684885741753/10^12.

The interval is approximately [0.6840881105,0.6848857418], width below .000798,
versus K2489's width below .0068. The upper bound covers EVERY admissible
adaptive policy, initial randomization, arbitrarily short stages, and failed
paths. The lower bound is an actual one-stage policy. This is neither an exact
optimum nor proof that one stage is optimal.

A reusable rational certificate obtains this improvement without the huge
schedule library: Jensen reduces the logarithmic stage cost to a rational
lower bound, and a cubic polynomial proves each continuum control bound.
The finite certificate has32896 score rectangles and685970 Bernstein tree
nodes. These counts describe proof coverage, not independent theorem counts.

The model imports classical fair routing and positive-Hilbert operational
motivation. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b still owe
native quotient/domain constructions. Source polarity, ledger, canon and
physical credit remain unchanged. No novelty or hardware claim.

## 1. Original law and inherited all-policy transfer

Use K2483/K2485/K2489 without changing the one-sided cost:

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]) for a<b,
    w(a,b)=0 for a>=b.

For fresh fair test/use routing, a test fails with probability a and a use
advances score b. Repeating a fixed stage until failure or use gives survival
1/(1+a) and failure-inclusive expected cost2w/(1+a). Clipping and dominance
allow b<=s and0<=a<=b. K2483's least-supersolution theorem covers arbitrary
policies; this proof is reused, not re-counted.

Let U be continuous, nonnegative and piecewise affine on[0,S], U(0)=1, S<=1/2.
Set r=a/b and h(r,b)=2w(rb,b)/b, continuously extended at b0. If

    [U(s-b)-U(s)]/b - r U(s) - lambda h(r,b) <= delta

for all0<b<=s<=S and0<=r<=1, lambda,delta>=0, then Ubar=U+delta*s satisfies
the stage supersolution inequality: the correction subtracts
at least delta*b from its numerator. Hence

    F_S(K)<=U(S)+delta*S+lambda*K.

A numerical residual maximum alone does not prove this inequality.

## 2. Logarithmic cost to a rational lower bound

K2489 factors the exact cost as

    h(r,b)=2 integral_A^B dt/(1-tb),
    A=(1+6r+r^2)/(4(1+r)), B=(1+r)/2,
    g(r)=2(B-A)=(1-r)^2/(2(1+r)).

Convexity of t ->1/(1-tb) gives Jensen's bound

    h(r,b)>=g(r)/(1-C(r)b)
           =4(1-r)^2/D(r,b),
    C=(A+B)/2=(3+10r+3r^2)/(8(1+r)),
    D=8(1+r)-b(3+10r+3r^2).

Equality holds at b0 and r1; it is strict for b>0,r<1. For b<=1/2, D is
concave in r, so its minimum is at an endpoint and D>=13/2>0. The lower
bound increases in b. This proof replaces costly interval logarithm searches;
it does not change the original cost or claim Jensen is exact away from its
equality cases.

## 3. Full score rectangles and exact cubic certificates

Put x=s-b,y=s. Partition both coordinates by the rational knots of U.
For each nonempty rectangle x in[x_l,x_h], y in[y_l,y_h] with y>x, let H be
the maximum chord quotient [U(x)-U(y)]/(y-x) over its vertices, with diagonal
limits given by minus the adjacent slopes. This bounds the entire rectangle:
on each affine pair the quotient is linear-fractional with positive denominator;
level sets are half-planes, and the diagonal limits cover the remaining edge.
Set u to the minimum U(y) on that y interval and b0=max(0,y_l-x_h).

To prove mu<=r*u+lambda*h(r,b0) for ALL r in[0,1], it suffices to prove

    P(r)=(u*r-mu)D(r,b0)+4lambda(1-r)^2 >=0.

This is a cubic with exact rational coefficients:

    p0=4lambda-mu(8-3b0),
    p1=u(8-3b0)-mu(8-10b0)-8lambda,
    p2=u(8-10b0)+3mu*b0+4lambda,
    p3=-3u*b0.

Its degree-three Bernstein coefficients on[0,1] are
p0, p0+p1/3, p0+2p1/3+p2/3, p0+p1+p2+p3. Nonnegative coefficients prove
nonnegativity because Bernstein basis functions are nonnegative and sum to1.
Otherwise exact midpoint de Casteljau subdivision covers both child intervals.
A depth limit means unproved, never accepted. Strict downward rational slack
in mu makes the concrete positive certificates terminate; numerical minimization
only proposes mu and cannot bypass this exact test.

For the score rectangle the residual is at most H-mu: rU(y)>=ru and the
Jensen bound increases with actual b>=b0. Taking the maximum over all rectangles
and0 gives delta, including every tiny-stage and kink limit. No ratio grid or
minimum b is imposed. All accepted rational cell bounds are saved in the report
and replayed by the default check without invoking numerical optimization.
Only candidate generation with --write uses SciPy; malformed, missing or forged
saved bounds fail exact verification.

## 4. Executed certificate and actual lower witness

The frozen candidate uses256 equal score intervals on[0,1/2], rational values
with denominator dividing10^12, and lambda9. Numerical one-stage optimization
proposed these values only; every claim rests on the independent exact
certificate. It proves

    delta=769539/488281250,
    U(1/2)+delta/2+9/1000=684885741753/10^12.

The worst conservative rectangle is x in[0,1/512], y in[1/512,2/512]. The
nonzero residual is real certificate slack; it is not evidence for a sharp
frontier or a proof that this rectangle contains the true optimum.

For the lower witness take a=2309/5000,b=1/2, repeating until failure or use:

    P(hit)=5000/7309,
    E cost=2w(a,b)/(1+a)
          in [0.00099934248921898893049 +/- 1e-23] <1/1000.

The saved Arb192 enclosure is much narrower. Geometric pass loops have finite
expected trial count2/(1+a) and unbounded support; no finite deterministic
trial cap is asserted. The width is exactly5829886472677/7309000000000000.

## 5. A structural rejected shortcut

For U(s)=(1+A*s)/(1+s),0<=A<=1,S<=1, put c=1-A. Its residual is

    c/[(1+s-b)(1+s)]-r U(s)-lambda h(r,b).

At fixed b,r it decreases with s: its derivative is
c/(1+s)^2 times r-(2+2s-b)/(1+s-b)^2, which is nonpositive because the latter
ratio is at least2/(1+s)>=1. Along s=b the rational part decreases with b,
with derivative -c(1-r)/(1+b)^2; h increases. Therefore its supremum is the
origin/tiny-stage limit. The family is a zero-residual supersolution exactly
when c<=the minimum of r+lambda*g(r). It cannot tune the endpoint independently
of that initial-slope restriction. This explains the switch to flexible
piecewise candidates; it does not exclude other nonlinear analytic families.

## Evidence, corrections and next question

Independent review checked the all-policy transfer, rectangle geometry,
Jensen factors and exact cubic proof. Controls execute a wrong U through the
certifier, reject negative endpoints and negative interiors despite positive
endpoints, reject invalid domains, and treat subdivision exhaustion as failure.
Universal proofs, exact finite certificate and interval policy evidence remain
distinct. Early a=.461 failed the actual budget check and was discarded;
a128-interval candidate failed the intended .001-width check, prompting the
verified256-interval construction. Failed candidates are not accepted evidence.

The certificate is useful without one-stage optimality. Further decimal
refinement of this same rectangle method does not settle the global structure.
The substantive successor is a merge inequality or analytic supersolution
that decides whether multi-stage adaptation can improve this small-budget
frontier, or extends a practical certificate to another target/budget. Tiny-stage
origin behavior and the exact nondyadic zero-budget boundary must remain intact.

[Probe](../../tests/channel-swings/k2491_analytic_stopping_certificate_probe.py),
[report](../../lab/process/k2491-analytic-stopping-certificate.json).
The original all-policy proof and clipping are in
[K2485](k2485-constrained-stopping-frontier-2026-11-01.md) and
[K2489](k2489-certified-stopping-grid-2026-11-02.md).
