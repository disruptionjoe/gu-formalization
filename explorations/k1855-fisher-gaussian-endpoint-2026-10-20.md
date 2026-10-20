---
title: "K1855: A rational score proves the sharp unrestricted Gaussian endpoint"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: whole-line dual bound and sharp Gaussian endpoint with effective window; sharp cubic asymptotic and budget correction; no exact optimizer, quartic law or GU physics
---

# A rational score proves the sharp unrestricted Gaussian endpoint

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
result: exact rational dual, feasible squared-Hermite trial, effective endpoint brackets, inverse budgets and Gaussian shape control
carrier: real probability densities on the real line with raw second moment1 and fourth moment k in (1,3) LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial degree only, no physical grading
action_owner: repository-construction -- constrained scalar Fisher functional
target: unrestricted all-density moment problem MAP-TYPE=evaluation
```

## Result and known context

Use K1854's all-density F(k), put q=3-k in(0,2), and J=I-1. Then

```
F(k)-1 >= (3-k)²/(2k),                                      (1)
F(3-q)-1 = q²/6 + q³/4 + o(q³)  as q down to0.               (2)
```

A fully explicit useful window is

```
q²/[2(3-q)] <= F(3-q)-1 <= (q²/6)(1+2q),  0<q<=1/25.       (3)
```

Unlike a polynomial score expansion, the lower bound needs no uncontrolled
sixth moment. Unlike a signed Hermite density perturbation, the upper trial
is a nonnegative density with the prescribed moments exactly. Both arguments
range over the unrestricted class; no mixture optimum or fitted quartic
Hamiltonian is substituted. The Fisher-to-Schrodinger connection is classical
([Flego et al.](https://arxiv.org/abs/1106.2078)); Gaussian Poincare via Hermite
expansion is standard ([Ledoux](https://perso.math.univ-toulouse.fr/ledoux/files/2024/01/GB-hermite-v1.pdf)).
No novelty, external acceptance, formal proof or GU physics is claimed.

## 1. Exact whole-line dual certificate

For a>=0 define

```
d=1+a x²/2,
g=x+a(x³-3x)/d,
P=2-x²+a(-2x4+12x²-6)-2a²x4.
```

Direct differentiation and a common denominator give the identity

```
2g'-g²-P = a³ x4 [ (1+a)x4-2x²+3 ]/(2d²)
          = a³ x4 [ (x²-1)²+2+a x4 ]/(2d²) >=0.             (4)
```

For finite-Fisher p with E X²=1, g has at most linear growth and g' is bounded
for each fixed a. Cutoff integration by parts is justified by the second
moment and score Cauchy-Schwarz. Completing the square yields

```
I(p)=E(rho+g)²+E(2g'-g²) >= E P
     =1+2a(3-k)-2a²k.                                     (5)
```

The nonnegative remainder in(4) grows at most quartically, so its expectation
exists under the assumed fourth moment. Maximize the final quadratic at
a=q/(2k) to obtain(1). It holds for nonsymmetric densities too. Equality is
not asserted: for a>0 the remainder is strictly positive off x=0 and every
feasible density gives it positive mass. For the attained minimum in K1843,
the inequality is strict. We retain the non-strict version as the useful bound.

The denominator coefficient1/2 is important: it cancels the order-a² x6
term while leaving a nonnegative exact residual. Truncating g=x+aH3 would
leave a negative x6 term; substituting a Gaussian sixth moment would not be
an all-density proof. This identity replaces the proposed endpoint spectral
calculation entirely at leading order.

## 2. Exact nonnegative upper trial with a moment-matching inverse

Let phi be the standard Gaussian density, H4=x4-6x²+3, and for s>=0 set

```
h_s=1-s H4,
N=E_phi h_s²=1+24s²,
p_s=phi h_s²/N,
M2=(1+216s²)/(1+24s²),
M4=(3-48s+2952s²)/(1+24s²).                                (6)
```

This is a nonnegative normalized density, even though h_s changes sign and
p_s has isolated zeros. Its nonnegative square root |h_s|sqrt(phi/N) belongs
to H1 and has the same derivative energy as the signed h_s sqrt(phi/N).
Thus zeros do not invalidate the trial or produce delta energies. We do not
claim this nodal trial is the strictly positive optimizer.

Hermite orthogonality or exact Gaussian moments gives
`E_phi (h_s')²=96s²` and `I(p_s)=M2`. The latter follows from
`I+M2-2=4 E_phi (h_s')²/N`. Standardize X=Y/sqrt(M2), Y~p_s.
The density of X has raw second moment1, Fisher information M2², and

```
q(s)=3-M4/M2²
 = (48s-1728s²+1152s³+69120s4)/(1+216s²)²,
J_trial(s)=384s²(1+120s²)/(1+24s²)².                         (7)
```

Since q(0)=0 and q'(0)=48, the inverse-function theorem supplies one smooth
s(q)>0 for all sufficiently small q>0. Equations(6)-(7) meet the fourth
moment **exactly**, not only through a series. They give
J_trial(s(q))/q² ->384/48²=1/6. Combine with(1) to prove(2).

## 3. Executed successor: a rational finite window

For 0<=s<=1/1000, exact polynomial lower bounds certify

```
q'(s)>0,  46s<=q(s)<=48s,
6 J_trial(s) <= q(s)² [1+2q(s)],
q(1/1000)=103288440/2233107247 >1/25.                        (8)
```

These are whole-interval inequalities. Clear the positive denominators;
divide the last difference by s³ before evaluating its s=0 limit, and the
q lower/upper differences by s and s². For each resulting polynomial
P(s)=sum c_i s^i, use

```
P(s) >= c_0 + sum_(i>=1,c_i<0) c_i /1000^i.
```

All four right sides are strictly positive; the symbolic producer and a
separate rational polynomial implementation reproduce them. Endpoint s=0 is
handled by continuity. The derivative numerator has lower bound
44.516351751168; the normalized upper-bound numerator exceeds32335.
Those decimals are explanatory only; executable Fraction results are exact.
Every q<=1/25 is therefore covered by one exact trial. This proves(3), not
just an asymptotic big-O assertion. No sixth-moment bound on competitors was
introduced to make the window effective.

## 3a. Released successor: the sharp cubic term without an eighth-moment bound

The positive residual in(4) contains more information than its sign. Let p_q
be the actual minimizer whose existence is proved in K1843, and set a=q/6
(the maximizer used in(1) is not needed here). Equations(3) and(11) imply
p_q tends to phi in total variation. On every compact x-interval,

```
R_a/a³ := (2g'-g²-P)/a³
    -> r_0(x)=x4[(x²-1)²+2]/2,
E_phi r_0 = (105-2*15+3*3)/2=42.                           (8a)
```

Every R_a is nonnegative on the full line. Restrict its expectation to a
fixed compact interval, use uniform convergence there and TV convergence of
p_q, then increase the interval to the full line. Monotone convergence gives

```
liminf_(q down to0) E_(p_q) R_(q/6)/q³ >=42/216=7/36.
```

This lower semicontinuity argument needs **no uniform eighth moment** for
p_q. Replacing it by a formal Taylor expansion under an uncontrolled full-line
integral would be unjustified. The exact polynomial part at a=q/6 is
`E P=1+q²/6+q³/18`. Dropping the nonnegative square in(5) consequently gives

```
liminf [F(3-q)-1-q²/6]/q³ >=1/18+7/36=1/4.
```

On the upper side, the explicit trial has
`q(s)=48s-1728s²+O(s³)` and `J_trial(s)=384s²+O(s4)`, hence
`[J_trial-q(s)²/6]/q(s)³ ->1/4`. Exact moment matching gives the matching
limsup. This proves the cubic equality(2). It is a released consequence of
the already proved leading bound, shape convergence and exact positive
residual, not a new spectral or fitted-density assumption. The result is
non-effective at the little-o order; (3) remains the effective finite window.

## 4. Executed successor: low-budget law and effective inversion

Let q_B in(0,2) solve F(3-q_B)-1=B, uniquely by K1843. From(2),

```
q_B = sqrt(6B) - (9/2)B + o(B) as B down to0.                (9)
```

Substitute q=sqrt(6B)+cB+o(B) into(2): the order-B^(3/2) coefficient
is sqrt(6)(c/3+3/2), giving c=-9/2. Standard asymptotic inversion is
justified by the leading law and strict monotonicity; no derivative of the
little-o remainder is assumed.

For 0<B<=1/4000, (1) ensures q_B<1/25: at q=1/25 the lower
bound is1/3700, and F(3-q) increases with q. Then(3) gives

```
sqrt(6B/[1+2sqrt(6B)]) <= q_B <= sqrt(B²+6B)-B.              (10)
```

The upper expression solves q²+2Bq-6B<=0 and is less than sqrt(6B).
For the lower bracket use B<=q_B²(1+2q_B)/6 and then q_B<=sqrt(6B).
The high-budget counterpart follows independently from
[K1854](k1854-fisher-concentration-endpoint-2026-10-20.md). Together the two
results characterize both leading ends of the unrestricted budget frontier,
without claiming its complete finite-budget curve or restricted-family gap.

## 5. Executed successor: Gaussian shape control and scaling

For any density p with raw second moment1 and finite I, put
h=sqrt(p/phi). Then E_phi h²=1 and

```
E_phi |h'|²=(I-1)/4.
```

Gaussian Poincare, valid on the weighted H1 space, implies
`1-(E_phi h)²<= (I-1)/4`. Cauchy-Schwarz applied to
`|sqrt p-sqrt phi|(sqrt p+sqrt phi)` gives

```
TV(p,phi) <= sqrt[1-(integral sqrt(p phi))²]
          <= (1/2)sqrt(I-1).                               (11)
```

The Poincare step follows from expanding h in the complete probabilists'
Hermite basis: its derivative energy weights the degree-n squared coefficient
by n>=1; truncation/density extends to weighted H1. It is not a claim about
a finite sampled basis. Formula(11) needs no symmetry. For the exact optimizer,
(3) gives TV<=q sqrt(1+2q)/(2sqrt6) on the stated window. More generally add
an actual value excess e=I-F to the right-hand Fisher budget. This is a
Gaussian-reference bound, not an optimizer-distance estimate at fixed k;
K1853 supplies the latter at k=2.

For a nonzero raw second moment m2 and raw fourth moment m4, rescaling gives
`I(p)>=m2^(-1)[1+(3-m4/m2²)²/(2m4/m2²)]` whenever 1<m4/m2²<3.
These are raw moments about the declared origin. They become variance and
central kurtosis only after translating to the mean; Fisher information is
translation-invariant, but the moment constraints are not. This fence is
needed when applying the inequality to asymmetric data.

## 6. Verification, scope review and remaining questions

Run `sage -python tests/channel-swings/k1855_fisher_gaussian_endpoint.py`
and `python3 tests/channel-swings/k1855_fisher_gaussian_endpoint_probe.py`.
The producer derives the rational residual, Hermite moments/energy, standardized
curve and positive interval numerators. The independent Fraction implementation
uses polynomial convolutions, Gaussian recurrence and separately evaluated
rational jets plus exact interval coefficient bounds. Planted input faults
change score, Hermite, moment, kinetic or remainder data; reporting flags are
checked separately. Written functional analysis supplies weak integration,
nonnegative-square-root handling and Poincare applicability. Finite algebra
alone is not a proof of those steps.

Inline hostile review checked whole-line remainder sign, denominator positivity,
large tails, nodal H1 admissibility, exact moment inverse, variance rescaling,
I versus I-1, explicit window coverage, both budget inequality directions,
Hellinger/TV constants, compact localization of the nonnegative residual,
and cubic liminf/limsup matching. No unresolved defect remains in this scope; no
separate-agent/expert or proof-assistant review is claimed. The quartic and higher
Gaussian coefficients remain open; the cubic coefficient is now proved by
section3a without assuming higher-moment convergence. At k down to1, K1854 does not prove the restricted
constant term. Genuine next work is a uniform next-order theorem, a
quantitative restricted global comparison at a named k, or a source-owned
metric/observation adapter. Scalar results do not alter SC-COS-50/51/54,
SC-ACT-01/02 ASSERTS, SC-META-53 UNCERTAIN, or any physics ledger verdict.
