---
title: "K2489 Occupation bounds and certified score-state stopping"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematical result on the stated original or supplied carrier; no native GU or measured implementation claim"
---

# K2489 Occupation bounds and certified score-state stopping

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
result: K2489
carrier: original fresh half-test half-use absorbing experiment with one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation as explicitly distinguished below ON=declared_carrier
real_structure: complex adjoint for quantum matrices; real probabilities for classical laws
grading: target and complement or absorbing classical trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: All-policy occupation inequality, practical bracket and continuum residual certificate MAP-TYPE=evaluation
```

## Result and Layer 0

A new all-policy occupation inequality gives a practical, rigorous bracket for
a nondyadic original stopping problem without enumerating K2487's huge library.
For target s=1/2 in log2 units and expected leakage K=1/1000,

    500/731 <= F_(1/2)(1/1000) < 62171/90000,
    bracket width =447001/65790000 <17/2500 =0.0068.

The bounds are about0.683995 and0.690789. The lower bound is an explicit lawful
one-stage schedule; the upper bound covers every allowed adaptive policy,
including private initial randomization, using actual failure-inclusive cost.
This is a fixed-target/budget bracket, not a sharp fixed-confidence constant.
A finite score-state Bellman recursion and an all-control residual certificate
also provide a reusable numerical route without a separate horizon dimension.

The law is exactly K2483/K2485: fresh fair test/use routing, expected one-sided
leakage, absorbing failure and termination at the target. Imported classical
probabilities and positive-Hilbert operational motivation are conditional
mathematics. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b native domain and
physical quotient debts, source polarities, ledger0.263 and canon are unchanged.
No novelty, measured physics, hardware or external-certification claim.

## 1. An exact global leakage lower bound

For 0<=a<=b<=1 let d=b-a,u=a+b, and
w=log(1+d^2/[2u(2-u)]), continuously zero at diagonal corners. For d>0,

    w >= d^2/[2u(2-u)+d^2] >= d^2/(4u),              (1)

because log(1+x)>=x/(1+x), d<=u and
2u(2-u)+d^2=4u-2u^2+d^2<=4u. The first inequality is strict for d>0.
For original controls a>b the one-sided cost is zero; universally (1) holds
with d replaced by (b-a)_+. This avoids treating a zero-cost a>b trial as
positive leakage. a=b=0 or1 has zero cost by continuous extension.

## 2. All adaptive policies, with failed paths included

Let p be hit probability, f failure probability, A=E sum_reached a and
B=E sum_reached b under the actual law. Fresh fair routing gives A=2f and
B=2E sum_use b. Before first target hit, accumulated used score is below s;
one final use adds at most1. Thus B<=2(s+1), and B>=2sp. Also
A=2f<=2(1-p). These are identities/inequalities of occupation measure,
not successful-path costs. Aborting or never terminating contributes to
1-p-f and cannot invalidate them.

For the countable reached-trial occupation measure, Cauchy--Schwarz and (1)
give, with the zero denominator convention0,

    K >= [E sum (b-a)_+]^2/[4(A+B)]
      >= (B-A)_+^2/[4(A+B)].                         (2)

All needed first moments are finite by the preceding score/failure identities;
finite partial sums and monotone convergence justify the countable form. If
K is infinite the claim is vacuous. If p>=1/(s+1), then 2sp>=2(1-p),
and the ratio (B-A)^2/(A+B) increases with B and decreases with A on B>=A.
Consequently

    K >= ((s+1)p-1)^2/[2((s-1)p+1)].                 (3)

For smaller p the upper bound below is automatic. Inverting the increasing
branch yields, for all s>0,K>=0,

 F_s(K) <= min(1, [(s+1)+K(s-1)
              +sqrt(K^2(s-1)^2+4Ks(s+1))]/(s+1)^2). (4)

At s=1 this is min(1,1/2+sqrt(K/2)). It reaches1 at K=s/2, consistent with
K2485's exact saturation/nonattainment theorem; it does not prove equality
below saturation. For s<=1 the zero-budget endpoint equals Q(s)=1/(1+s).
For s>1 it can be weaker than exact Q(s). Take the minimum with independently
proved prior bounds; do not overwrite Q or claim uniform dominance.

In particular the K2471 entropy bound may beat (4) at integer targets (e.g.
s=1,K=.1). Its baseline2^-s is weaker than Q at strictly nondyadic s<1,
which is the practical use of the following example.

## 3. Concrete certified nondyadic frontier bracket

Set s=1/2,K=1/1000. Formula(4) becomes

    p <= (5998+2sqrt(12001))/9000 <62171/90000,

since (2191/20)^2=12001.2025>12001. K2485's zero-budget-continuity bound is
2/3+1/sqrt500>0.711; its linear saturation bound is (3+2/1000)/(7/2)>0.857.
The K2471 entropy upper is at least2^-1/2>0.707, even at zero cost.
Thus the new0.691 upper genuinely improves all those available comparisons
at this specified target and budget, though not uniformly across targets.

For a feasible original-law policy, repeat the single control
(a,b)=(231/500,1/2) until either failure or the first use. It has

    P(hit)=1/(1+a)=500/731,
    K_actual=1000/731 *log(499639/499278)
      <361000/364972218 <1/1000.

The exact last comparison is361000000<364972218. It includes every reached
pass-loop and the failed terminal trial. Trial count has unbounded support
but finite expectation2/(1+a). Hence this is a lawful positive-budget lower
bound, not a limit policy. No numerical optimizer or finite-grid claim is
needed for the stated bracket.

## 4. Score-state Bellman computation with no length coordinate

For lambda>=0, on grid a=l/M,b=k/M, 0<=l<=k<=M,k>=1, put J=ceil(Ms), assumed certified
(e.g. rational s). A schedule necessarily hits after at most J successful
use stages, since each advances score by at least1/M. All deterministic
complete grid schedules are therefore covered by

    D(j)=1 for j<=0;
    D(j)=max(0,max_l,k [D(j-k)-2lambda*w(l/M,k/M)]/(1+l/M)), j>=1. (5)

Compute increasing j through J. For integer-grid target, clipping permits
k<=min(M,j), so all dependencies have lower j. D(J) is the exact grid
support value sup(P-lambda K). Geometric pass loops still have unbounded
trial duration; no deterministic trial cap is asserted. A finite action grid
alone supplies a lower approximation, not a continuum upper bound.

For continuum support, K2487's length-N compressed schedules lie within this
all-length grid class. Thus its same error E gives
D(J)<=V_lambda(s)<=D(J)+lambda E, with target rounding as in K2487.
For numerical evaluation, enclose the maximum by the maximum of lower and
upper interval endpoints; keep one actual policy for a lower witness. No
exact ordering of logarithmic expressions is assumed. The probe separately
compares (5) with exhaustive tiny schedules and evaluates a modest grid.
It does not spend K2487's impractical tolerance parameters or claim grid
convergence rates without that proof.

## 5. All-control residual certificate, including arbitrarily small stages

Fix lambda>=0. Let U be continuous nonnegative piecewise affine on[0,S], U(0)=1. Suppose
for every0<s<=S,0<b<=min(1,s),0<=r<=1,

 [U(s-b)-(1+rb)U(s)-2lambda*w(rb,b)]/b <=delta, delta>=0. (6)

Then Ubar(s)=U(s)+delta*s is a stage supersolution: its added contribution
to the numerator is -delta*(b+rb*s)<=-delta*b. Free abort is bounded since
Ubar>=0; target value is1. Original overshoots reduce by K2485 clipping,
and a>b is dominated, so K2483's least-supersolution theorem applies:

    F_S(K)<=min(1,U(S)+delta*S+lambda*K).             (7)

A sampled residual is insufficient. The b normalization prevents a fixed
per-stage error from accumulating over arbitrarily many tiny stages.
Here is a finite certification procedure, rather than a sampled one.

Define h(r,b)=2w(rb,b)/b and extend h(r,0)=(1-r)^2/[2(1+r)]. For r<1,

 A(r)=(1+6r+r^2)/(4(1+r)), B(r)=(1+r)/2,
 h(r,b)=2 integral_[A(r),B(r)] dt/(1-tb).

This follows by factoring the original log ratio. h is nondecreasing in b.
It is nonincreasing in r at fixed b since the original positive-part leakage
is nonincreasing in a; direct differentiation gives
x_a=-d*(3b+a-2ab-2b^2)/[u^2*(2-u)^2]<=0.
Use the direct expression3b+a-2ab-2b^2=b*(3-2b)+a*(1-2b):
if b<=1/2 it is nonnegative; if b>1/2 its minimum over0<=a<=b is
4b*(1-b)>=0. At r=1, h=0 including the cornerb=1 by continuous extension.

Partition x=s-b and y=s at all U knots, intersect each rectangle with
0<=y-x<=1. On the resulting rational polygon C, the chord quotient
H(x,y)=[U(x)-U(y)]/(y-x) has affine numerator/denominator. Its maximum is
at positive-denominator vertices, with diagonal limits bounded by the
negative slopes of the touching affine pieces. This is the linear-fractional
convex-combination rule; diagonal vertices have zero numerator by continuity.
Let H_C be that upper bound, u_C=min_C U(y), and b_C=min_C(y-x).
For each rational ratio bin[r0,r1], the whole-cell residual is bounded by

    H_C-r0*u_C-lambda*h(r1,b_C).                    (8)

Use a certified LOWER enclosure for h in (8), and take delta as the maximum
of0 and all resulting UPPER bounds. All pieces are finite rational geometry
and interval logs. Refinement is allowed; no convergence assertion is made
for arbitrary raw grid-interpolated U. In particular the first grid interval
admits only a=0 or b and can leave a nonvanishing small-stage residual.
The implementation certifies a uniform rational partition for S<=1; the
polygon recipe describes the extension beyond that implemented domain.

A simple analytic check is S=1,U(s)=1-cs. Since h>=g(r)=(1-r)^2/[2(1+r)],
the residual is at most c-r(1-c)-lambda*g(r). With
c=lambda/2 for0<lambda<=1/2 and c=1/2-1/(8lambda) forlambda>=1/2,
this is<=0: substituting t=(1-r)/(1+r) reduces the constraint to
c<=min over t in[0,1] of (1-t+lambda*t^2)/2. At lambda9/8,c7/18 it yields the exact
rational certificate F_1(1/10)<=521/720. This is a verification fixture;
it does not beat K2471's entropy bound at that point.

## Evidence and next question

Universal proofs are the occupation, moment monotonicity, clipping and residual
arguments above. Exact polynomial/rational controls, actual-log intervals,
exhaustive tiny-library agreement and finite all-cell residual verification
check the implementation separately. Independent probability and adversarial
review check overclaims, one-sided cost, small-stage and endpoint seams.
No finite test count is a theorem count.

General Bellman background is [Bertsekas, Noncontractive Total Cost Problems](https://www.mit.edu/~dimitrib/DP2_Chapter%204_UPDATED.pdf).
Its general theory does not substitute for the original-cost inequalities here.
Next: optimize a genuinely all-control certified U and compare it with the
occupation and entropy bounds; the global sharp fixed-confidence coefficient
and exact optimal policies remain unresolved. The concrete nondyadic bracket
is already useful without that larger claim.

[Probe](../../tests/channel-swings/k2489_certified_stopping_grid_probe.py) and
[report](../../lab/process/k2489-certified-stopping-grid.json).
