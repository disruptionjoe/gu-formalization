---
title: "K1874: Attainment and sharp cost under a sixth-moment cap"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: attained capped Fisher minimum and sharp large-cap cost; positive unique sextic optimizer; no computed coefficients/gap, GU physics or novelty claim
---

# A finite tail budget restores a Fisher minimizer, with a sharp cost

For fixed k>3, let V(k,M) minimize Fisher information over real-line densities
with raw moments E X²=1, E X4=k and E X6<=M. The feasible domain is exactly
M>k². On this domain the minimum is attained, every minimizer uses the entire
sixth-moment budget, and

```
1+(k-3)²/(M-k²) < V(k,M) <= 1/(1-t),
M=(k-3)²/t+15(k-2)-9(k-3)t-6t³,     0<t<1.             (1)
```

The equation for t has exactly one solution. In particular
`lim_(M->infinity) M[V(k,M)-1]=(k-3)²`.
This replaces K1856's conservative M^-4 cap gap by the sharp M^-1 leading
law and proves the previously open attainment statement. The optimizer is unique, even, smooth and positive, and its Euler operator
has a strictly positive sextic coefficient. Its coefficients and spectral gap
are not computed here; no novelty is claimed.

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
result: sixth-moment feasibility, attained minimum, saturation and sharp large-cap Fisher cost
carrier: real densities on R with raw moments second1 fourth k>3 sixth<=M LAYER=toy CHIRALITY=N/A
pairing: Fisher energy4 integral |u'| squared for u=sqrt(p) ON=real_H1_functions
real_structure: nonnegative real densities; no physical real-form identification
grading: polynomial moment degree only
action_owner: repository-construction -- constrained scalar Fisher functional
target: super-Gaussian moment problem with a supplied tail cap MAP-TYPE=evaluation
```

## 1. Scope and reused evidence

[K1856](k1856-fisher-tail-phase-2026-10-20.md) proves the uncapped infimum1
is unattained for k>3 and constructs escaping tails. It also proves a finite
sixth cap creates a gap, but does not prove attainment. We keep those results
and strengthen the cap analysis. K1872 concerns k<3 and does not answer this
question. No source claim or physics-ledger row changes: this is independent
probability/variational mathematics. Fisher convexity follows directly from
Cauchy-Schwarz on mixture scores; the proof below is self-contained apart from
standard one-dimensional H1 weak compactness and local compact embedding.
Related literature includes [Bercher, generalized Cramér-Rao inequalities
(2012)](https://arxiv.org/abs/1206.0567), concerning generalized information
and q-moments, and [Minimizing Fisher information with absolute moment
constraints (2017)](https://www.sciencedirect.com/science/article/abs/pii/S0167715217301906).
Only the former abstract and the latter indexed abstract/topic were available;
the latter full page returned403. These establish nearby literature, not the
specific cap theorem, and do not support a novelty claim here.

## 2. A sharper lower bound by projecting the score

Let u=sqrt(p) in H1, rho=2u'/u where u>0, and define the score as zero on
its p-null set. Integration by parts with cutoffs, using E X6<infinity and
finite Fisher, gives E[rho X]=-1 and E[rho X³]=-3. The tails vanish by
Cauchy-Schwarz; cutoff derivative errors are dominated by the finite moments.
Consequently, for r=rho+X and g=X³-kX,

```
E r²=I(p)-1,   E[rX]=0,
E[rg]=k-3=Delta,   E g²=E X6-k².                      (2)
```

Cauchy-Schwarz gives `I-1 >= Delta²/(E X6-k²)` and hence the lower
bound in (1). The denominator is positive for every density: equality in
`E X6 E X² >= (E X4)²` forces X³=kX almost surely, supported on the
three points {0,+sqrt(k),-sqrt(k)}, not an absolutely continuous density.
This also excludes every M<=k².

The Fisher inequality is STRICT for k>3. Equality would force
`rho+x=c(x³-kx)`, with c=Delta/(E X6-k²)>0, thus

```
u(x)=A exp(c x4/8-(ck+1)x²/4).
```

This is not square integrable unless A=0. The differential equation holds
weakly; its locally continuous coefficient makes u locally absolutely
continuous with the stated unique solution. Disconnected support cannot
rescue equality. The argument excludes equality for each admissible density;
attainment below then makes the minimum itself strictly above the lower bound.

## 3. Exact feasible trials for every allowed budget

Put Delta=k-3>0, 0<t<1, v=1-t, B=Delta+3t²,
`a²=B/t`, and `w=t²/B`. Define the smooth positive even density

```
p_t=(1-w) N(0,v)+(w/2) N(+a,v)+(w/2) N(-a,v).          (3)
```

Here 0<w<1. Elementary Gaussian moments give

```
E X² = v+w a² =1,
E X4 =3v²+6v w a²+w a4 =3+Delta=k,
E X6 =15v³+45v² w a²+15v w a4+w a6
      =Delta²/t+15(1+Delta)-9Delta t-6t³ = M(t).         (4)
```

M'(t)=-Delta²/t²-9Delta-18t²<0. Its limits are infinity at0 and
(Delta+3)²=k² at1. Thus every M>k² has a unique t and an explicitly feasible
finite-Fisher trial. Fisher convexity bounds `I(p_t)<=1/v`; this is an upper
bound, never the exact Fisher information of the mixture.
For convenient rational trials one may choose any t with M(t)<=M rather than
solve the equation numerically. As t tends0, `M(t)t->Delta²`, and the upper
bound and (2) squeeze the sharp limit in (1).

## 4. Attainment, cap saturation and compactness

Take a minimizing sequence p_n and nonnegative u_n=sqrt(p_n). Normalization
and bounded Fisher make u_n bounded in H1. A weak-H1/local-strong-L2
subsequence exists. The second-moment bound gives uniform L2 tail control
`integral_(|x|>R) u_n²<=1/R²`, so the convergence is strong in L2 on R
and preserves normalization. The sixth cap gives uniform integrability of
fourth moments, with tail <=M/R², and of second moments. Thus the exact
second and fourth equalities pass to the limit. Fatou preserves the sixth
INEQUALITY; it need not preserve an arbitrary sixth equality. Weak lower
semicontinuity of the derivative norm proves attainment.

Every minimizer saturates E X6=M. If a minimizer had slack, use K1856's
finite-sixth-moment escaping sequence to choose a density q with the same
second/fourth moments and I(q) smaller than the minimum, which exceeds1.
A sufficiently small convex mixture with q remains within the slack cap and
strictly lowers Fisher by convexity, a contradiction. This argument does
not assume a Lagrange multiplier or differentiability of V.

There exists an even minimizer: averaging p(x) and p(-x) preserves all
constraints and cannot increase Fisher. Convexity alone does not establish uniqueness. The positivity argument below
supplies the missing step and therefore proves every minimizer is even. For any minimizing
sequence, the above subsequence converges to some minimizer in H1 at the
square-root level: energies converge to the minimum, giving derivative norm
convergence as well as weak convergence. Densities converge in TV and W4
(the sixth cap gives fourth-moment uniform integrability). The uniqueness proved below upgrades subsequential compactness to convergence
of every minimizing sequence.

## 5. Executed value and accuracy consumers

For fixed k>3, V is convex in M by mixing feasible densities. It is strictly
decreasing: start with a minimizer at M1 and mix with a finite-moment q of
smaller Fisher; for any M2>M1 a sufficiently small positive mixture fits M2.
It is continuous on (k²,infinity), diverges as M decreases to k² by (1),
and decreases to1 at infinity with the sharp coefficient Delta².

For any desired Fisher excess eta>0:

```
I(p)-1<=eta  requires  M>k²+Delta²/eta.
t=eta/(1+eta), M>=M(t) suffices via (3).                (5)
```

Both budgets have leading Delta²/eta as eta tends0. At k=4,M=100 the
rational trial t=1/70 has M(t)<100, yielding
`1+1/84 < V(4,100) <= 1+1/69`.
At k=4, eta=1/100, M>116 is necessary and M=131 suffices with t=1/101.
These are rigorous brackets and supplied feasible densities, not numerical
solutions of the optimizer. K1856's Gaussian control gives
`TV(p,phi)<=sqrt(I(p)-1)/2`, so the latter trial is within1/20 in TV while
retaining fourth moment4. For N independent copies, TV of the products is
at most N times that bound, capped at1. For |f|<=L, expectation error is at
most2L TV; event/CDF error is at most TV. These controls deliberately do not
bound fourth-power error, which stays exactly k-3.

As M tends infinity, any chosen minimizers tend to the Gaussian in TV by
the upper bound and K1856, yet their fourth-moment excess escapes to infinity.
As M decreases to k², any weak subsequential limit has moments second1,
fourth k and sixth<=k², hence is supported on {0,+sqrt(k),-sqrt(k)}.
The total outer mass is1/k and central mass1-1/k. For chosen even minimizers
the outer weights are1/(2k) each, so the weak limit is unique in that even
class. Even moments alone do not fix the left/right division, but uniqueness and
reflection invariance do so for the actual minimizers proved below.
The diverging Fisher cost is consistent with this atomic limit.

## 6. Executed successor: the unique positive sextic ground state

Put u=sqrt(p) for a minimizer. Work in the real energy space
H1 intersect L2((1+x6)dx); signed square roots are allowed, since passing
to |u| preserves moments and derivative energy. The four moment-constraint
derivatives are independent: if `(a0+a2 x²+a4 x4+a6 x6)u=0` as a
functional on compactly supported smooth variations, the polynomial vanishes
on a positive-measure set and hence identically. One may therefore choose
four compactly supported variation directions whose moment matrix is
invertible. The implicit function theorem gives the usual equality corrections
and a direction reducing the sixth moment. The inequality multiplier has its
proper sign, and ordinary constrained variation yields real a,b,E and c>=0:

```
-4u''+(a x²+b x4+c x6)u=E u.                          (6)
```

This is a normal multiplier argument, not an assumption that moment equalities
form a compact set. Local ODE regularity makes u smooth. Nonnegative u cannot
vanish at a finite point: a zero is a minimum with u'=0, and uniqueness for
the smooth second-order ODE would give u identically0. Thus u is positive.

In fact c>0. Otherwise the positive solution of the quartic-or-lower equation
would give the ground-state identity for every compact smooth h:

```
4 integral |h'|²+integral (a x²+b x4-E)h²
 =4 integral u² |(h/u)'|² >=0.                        (7)
```

Cutoff and smooth approximation extend the inequality to every finite-Fisher
density with the same finite second/fourth moments. For those competitors it
says I>=E-a-bk=I(p). That would attain the uncapped k>3 minimum, contradicting
K1856. No sign assumption on b was needed. Hence the cap has a strictly
positive multiplier and the actual polynomial is confining sextic.

Now let p,q be two minimizers. They are both strictly positive by the same
argument. Equality is required in Fisher convexity for their midpoint.
The exact nonnegative convexity defect is the weighted square of the score
difference, so their scores agree everywhere almost surely. Thus p/q is
constant; normalization proves p=q. Reflection invariance makes this unique
optimizer even. This repairs the missing condition in the tempting but invalid
argument that Fisher is always strictly convex regardless of support.

## 7. Executed successor: actual-optimizer accuracy and budget slack

For the selected sextic operator H in (6), the confining potential gives a
compact resolvent (local compact embedding plus the sextic tail bound).
The positive ground state is simple by (7); hence its next eigenvalue gives
a gap gamma>0. For any feasible density q, let D=I(q)-V(k,M) and
m6=E_q X6. The exact quadratic-form excess is

```
G=<sqrt(q),(H-E)sqrt(q)>=D-c(M-m6),
0<=G<=D,    D>=c(M-m6),
TV(q,p)<=sqrt(G/gamma)<=sqrt(D/gamma).                 (8)
```

The overlap estimate uses normalized nonnegative square roots and
`TV<=sqrt(1-<sqrt(q),u>²)`. If a computed certificate later supplies a lower
gap g<=gamma and c, then D<=g epsilon² is a sufficient TV tolerance and
cap underspend cannot exceed D/c. Event/CDF error<=epsilon, bounded-observable
error<=2L epsilon and N-product TV<=N epsilon follow. These are usable
conditional formulas, not a claim that gamma or c has been enclosed here.
The Gaussian comparison in section5 is a different target and cannot replace
the actual-optimizer gap in (8). No uniform endpoint or practical numerical
gap is inferred from compact resolvent alone.

## 8. Verification and hostile review

The producer checks exact symbolic mixture moments, projection norm, signs,
endpoint constants and budget examples. A separate Fraction implementation
recomputes moments from Gaussian components over a rational grid, checks
score orthogonalization and challenges corrupted input moments/weights and
reference coefficients. Reporting assertions are counted separately.
Finite checks support the algebra; the compactness, strictness, ODE equality
and limit arguments above own the continuum results. No proof assistant,
external reviewer, rigorous computed optimizer or novelty is claimed.

Hostile review specifically challenges equality versus inequality closure,
raw versus centered moments, mixture Fisher bound versus exact value,
nonintegrable equality case, the limit order, cap saturation and unjustified
strict-convexity/uniqueness. No unresolved flaw is known in these stated proofs. The existence, normal
multiplier, positivity and ground-state arguments are analytic, not certified
by the rational checks. Exact coefficients and a practical spectral enclosure
remain uncomputed; uniqueness alone supplies neither.
