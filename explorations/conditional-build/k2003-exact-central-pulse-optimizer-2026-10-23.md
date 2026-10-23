---
title: "K2003: Exact central minimum-norm pulse by a renewal distribution"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2003_exact_central_pulse_optimizer.py
  - tests/channel-swings/k2003_exact_central_pulse_optimizer_probe.py
---

# K2003: Exact central minimum-norm pulse by a renewal distribution

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
result: explicit infinite-convolution formula for the unique central minimum-norm pulse, attained dual certificate and effective strong approximation
carrier: actual K1991 central rectangle in the width9 scalar strip LAYER=toy CHIRALITY=N/A
pairing: normalized Lebesgue row/column marginals and real L2 norm ON=central_rectangle
real_structure: real measurable controls bounded by amplitude23/100
grading: convolution order and characteristic coordinates, not source chirality
action_owner: repository-construction -- unchanged conditional scalar transport problem
target: exact central optimization and cap-preserving constructive approximation MAP-TYPE=intertwiner
```

## Result and dependency check

The central problem left open by
[K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md) and
[K1995](k1995-central-marginal-cycle-improvement-2026-10-23.md) is solved:
an explicit geometric series of uniform-convolution densities, inverse cumulative
distribution functions and clipping gives its UNIQUE minimum-L2 pulse. Both
continuum marginals and the amplitude cap are exact. This is a definition of an
actual function, not an unspecified optimizer oracle or finite-grid solution.

Its squared norm is given by an absolutely convergent series of exact rational
coefficients at the actual algebraic parameter. A finite-convolution construction
also has an explicit geometric strong-error bound, preserves the cap and its
column marginal exactly, and honestly retains a small row residual at finite
order. This closes central optimization, not explicit wing construction or the
whole-strip minimum-norm problem. The improved whole-pulse upper bound still
uses the already proved existence of feasible wings.

The prerequisite is K1991's exact forced-support factorization. No new phase,
test marginal, source pairing, or GU physics verdict is introduced. K1997's
infinite-rank theorem and K1993's corner H1 obstruction remain intact.

## 1. Actual central rectangle and normalized problem

Let t be the same root of

    101t^4-102t^3-168t^2+392t-138=0,   9/20<t<23/50,

and put M=23/100, W=3+4t and alpha=4t/W. In K1991 coordinates x=u/t,
reverse the row variable to r=-x. The two ramp coordinates y cover [-1,1]
with physical measure dz=2t dy; the middle strip 3<=z<=6 is represented by
one atom y=0 of weight 3. Consequently the normalized column measure is

    nu=(1-alpha) delta_0 + alpha Uniform[-1,1],
    mu=Uniform[-1,1] on r.

A pulse q=v/M has precisely these constraints:

    |q|<=1,   int q(r,y)dnu(y)=r,   int q(r,y)dmu(r)=y.       (1)

At the middle atom, the column target is zero. Working with one middle value
loses no optimizer: averaging over the physical middle interval preserves
every row marginal, replaces its zero column marginals by zero, preserves the
cap, and weakly decreases the squared norm by Jensen. Equality requires
middle-column independence a.e. The unique minimum therefore lies in this
reduced representation. Conversely every solution of (1) expands to a genuine
central pulse constant across the middle interval.

## 2. Explicit densities and inverse distribution functions

Let k(s)=1/2 for |s|<1 and zero otherwise. Write k^{*d} for its d-fold
convolution. Define probability densities on the real line by

    p_A=(1-alpha) sum_(n>=0) alpha^n k^{*(2n+1)},
    p_B=k*p_A=(1-alpha) sum_(n>=0) alpha^n k^{*(2n+2)}.       (2)

These are nonnegative, integrate to one, and converge in L1, since the weights
sum to one. They are even. Each is positive everywhere: at any finite s,
one sufficiently high convolution order is positive there. On every compact
interval they have a strictly positive continuous lower bound furnished by
one such term. Let F_A,F_B denote their cumulative distribution functions and
define for -1<r,y<1

    A(r)=F_A^{-1}((1+r)/2),   B(y)=F_B^{-1}((1+y)/2).        (3)

The inverses are unambiguous, continuous, odd, locally Lipschitz, and finite
on the open interval. They diverge only at the endpoints. Put B(0)=0 at the
middle atom. Endpoint representatives have measure zero and may be arbitrary.

The required optimizer is

    q_star(r,y)=clip_[-1,1](A(r)+B(y))       on the ramps,
    q_star(r,0)=clip_[-1,1](A(r))            on the middle.   (4)

In physical coordinates use r=-u/t and K1991's y=(z-3)/(2t) on the left
ramp, y=(z-6)/(2t) on the right. Multiply (4) by M.

## 3. Both continuum marginals are exact

The geometric series gives the renewal equations in L1,

    p_B=k*p_A,     p_A=(1-alpha)k+alpha k*p_B.               (5)

For a real number b, define C(b)=int clip(a+b)p_A(a)da. Bounded dominated
differentiation gives, a.e.,

    C'(b)=int_(-1-b)^(1-b) p_A(a)da=2p_B(b).

Evenness gives C(0)=0. Both sides are locally absolutely continuous, hence
C(b)=2F_B(b)-1 for every b. Inserting b=B(y) proves the exact column mean y.
At the middle atom b=0 the column mean is exactly zero.

Similarly let R(a)=(1-alpha)clip(a)+alpha int clip(a+b)p_B(b)db. Then

    R'(a)=(1-alpha)1_(|a|<1)+2alpha(k*p_B)(a)=2p_A(a).

R(0)=0, so R(a)=2F_A(a)-1. Inserting a=A(r) proves the exact row mean r.
The proof uses all continuum coordinates, including tails of the inverse CDFs;
no sampled row, finite spline truncation or approximate marginal is substituted.

## 4. Attained dual certificate and unique global central optimum

The potentials are square-integrable. If G has distribution
P(G=n)=(1-alpha)alpha^n, then p_A is the law of a sum of 2G+1 independent
uniform[-1,1] variables. Conditioning on G gives

    int A(r)^2 dmu(r)=(1+alpha)/(3(1-alpha)),
    int B(y)^2 dUniform(y)=2/(3(1-alpha)).                   (6)

Thus p(r,y)=A(r)+B(y), with B=0 at the atom, lies in L2(mu x nu).
For any feasible q, Fubini and (1) imply <p,q-q_star>=0. Pointwise projection
onto [-1,1] gives

    (q_star-p)(q-q_star)>=0.

After integration, <q_star,q-q_star>>=0, so

    ||q||^2 >= ||q_star||^2 + ||q-q_star||^2.                (7)

This proves both global optimality and uniqueness on the entire central feasible
set. It does not restrict competitors to an additive or monotone ansatz: only the
certificate is clipped additive; every bounded feasible competitor is covered.

For an explicit dual identity put H(s)=s^2 when |s|<=1 and H(s)=2|s|-1
otherwise. The pointwise equality H(p)=2p q_star-q_star^2 and the exact
marginals show that the attained dual value

    2 int A(r)r dmu + 2 int B(y)y dnu - int H(A+B)dmu dnu

equals ||q_star||^2. Equation (6) makes every term integrable. There is no
unstated bounded-dual-potential or finite-dimensional duality assumption.

## 5. Exact norm series and whole-pulse consumer

Let S_d be a sum of d independent uniform[-1,1] variables and
c_d=E[min(1,S_d^2)]. These are rational numbers for odd d. Pushforward by
(3), followed by convolution in (2), gives

    N_star:=||q_star||^2
      =(1-alpha)^2 sum_(n>=0) (n+1)alpha^n c_(2n+1).       (8)

To see the multiplicity, the middle contributes
(1-alpha)^2 sum alpha^n c_(2n+1). The ramps contribute
alpha(p_A*p_B), and p_A*p_B=(1-alpha)^2 sum_(j>=0)(j+1)alpha^j
k^{*(2j+3)}. Reindexing combines the coefficients into (n+1).
In particular c_1=1/3, c_3=8/15 and c_5=391/630.

For odd d, on -1<s<1 the convolution density is the single polynomial

    k^{*d}(s)=sum_(j=0)^((d-1)/2)
       (-1)^j binom(d,j)(s+d-2j)^(d-1)/(2^d(d-1)!).

This formula follows directly by scaling each uniform variable to [0,1],
applying inclusion-exclusion to the simplex cut out of the unit cube, and
differentiating its volume. It introduces no approximation to the density.
Thus c_d=1-int_-1^1(1-s^2)k^{*d}(s)ds is computed exactly. If terms
n=0,...,N are retained, the omitted norm is nonnegative and at most

    alpha^(N+1)[(N+2)-(N+1)alpha],                       (9)

the exact omitted total weight, since 0<=c_d<=1. No numerical quadrature
error occurs. The producer isolates t rationally, encloses alpha, evaluates
48 terms with outward rational rounding and adds (9). Its machine-readable
[certificate](../../lab/process/k2003-exact-central-pulse-optimizer.json)
contains the resulting rigorous intervals and tail bound.

The physical central minimum is 2t W M^2 N_star. It is less than 0.115.
The certified interval is approximately 0.11439655863919339; the exact rational
endpoints, not this rounded display, carry the certificate.
The uncapped additive optimizer r+y has normalized squared norm
(1+alpha)/3. It exceeds the cap on a positive-measure set, so the exact cap
cost is strictly positive. Equation (8) computes that cost, rather than merely
bounding it: the physical central squared-norm increase lies between 0.008
and 0.009. These inequalities are checked on the actual algebraic root.
Keeping any feasible wings and their forced regions gives the rigorous
whole-strip upper bound

    ||v_dagger||^2 <= M^2(54-2tW)+2t W M^2 N_star
                   < 2.739952052817663.                  (10)

This improves K1995's upper 2.7541718523. The inherited K1989 lower
2.34940177149 still applies, and its strong Fenchel inequality transfers the
new upper into a distance certificate to its fixed witness. Equation (10)
uses wing existence, not their formula or minimum norm. The scalar phase
energy was already optimal and has not changed.

## 6. Explicit finite-convolution approximants with a strong-error modulus

For N>=0 stop the geometric variable at N:

    p_(A,N)=(1-alpha)sum_(n=0)^(N-1)alpha^n k^{*(2n+1)}
              +alpha^N k^{*(2N+1)},
    p_(B,N)=k*p_(A,N).                                  (11)

Use their inverse CDFs in (4) to define q_N. The finite densities are
piecewise polynomials; their CDFs and inverse brackets can be evaluated by
exact polynomial arithmetic and bisection. At the actual algebraic alpha,
algebraic-number arithmetic or outward root intervals give certified values.
This is an executable finite construction, not an appeal to a transport solver.

Every q_N respects the cap and has its column means EXACT, because the first
identity in (5) remains exact. The second has the precise defect

    p_(A,N)-(1-alpha)k-alpha k*p_(B,N)
       =alpha^(N+1)(k^{*(2N+1)}-k^{*(2N+3)}).             (12)

Consequently the absolute row residual is uniformly at most 2epsilon_N,
where epsilon_N=alpha^(N+1). It is not zero in general. This construction does
not claim an exact finite pulse, plateau, or phase-energy certificate.

The total variation distance of p_(A,N) from p_A is at most epsilon_N:
only the original mass after G=N is reassigned. Convolution is a contraction
for total variation, so the same holds for p_B. The clipped-square integrand
lies in [0,1], giving

    | ||q_N||^2-||q_star||^2 | <=(1+alpha)epsilon_N.        (13)

Here the middle uses one density and the ramps use a product of two, whose
total variation distance is at most 2epsilon_N. Importantly, this norm
calculation uses the quantile pushforward; it does not assume the quantiles
are uniformly close near their endpoints.

Apply the pointwise projection inequality to q_N. The column residual vanishes,
and the row residual pairs only with A. Cauchy-Schwarz and (6), followed by
(13), yield the effective strong bound

    ||q_N-q_star||^2 <= [1+alpha+4sqrt((1+alpha)/(3(1-alpha)))]epsilon_N
                      < (27/5)alpha^(N+1)               (14)

for the actual alpha<2/5. Thus the construction converges geometrically in
normalized squared L2 error. Multiplication by 2t W M^2 converts it to
physical central squared error. This resolves the previously missing
effective central strong-norm approximation without asserting a rate for
K1980's whole-strip iteration.

Finite convolution order is NOT separation rank. The inverse-CDF/clipping
kernel need not have finite rank, so (14) does not contradict K1997 or K2001.
The exact optimizer is locally Lipschitz on every compact subset of the open
central rectangle, since the densities have positive compact lower bounds;
global H1 still fails at the already identified tight-cut corner. No global
smoothness, finite-rank representation or exact finite-iterate feasibility is
claimed.

## 7. Why the monotone central construction cannot simply supply the wings

The central solution has a common increasing column potential B. The actual
wing admits NO feasible pulse whose rows all share a nondecreasing column
direction. This excludes a direct monotone clipped-additive extension of (4),
independently of the row potential or smoothness.

Use K1991's wing variables x in [0,L], x<=y<=2L, where L=3-t, and
h=(q+1)/2 in [0,1]. The exact column and row masses are

    int_0^min(y,L) h(x,y)dx=y/2,
    H(x):=int_x^(2L) h(x,y)dy=phi(x-3)/M+2L-9/2-x.

If h(x,.) is nondecreasing for almost every x, then for a column y0<L,
H(x)>=(2L-y0)h(x,y0) whenever x<=y0. Integrating gives the necessary
inequality int_0^y0 H(x)dx >=(2L-y0)y0/2. But the ACTUAL outer phase is
phi(x-3)=x[1-lambda(1-x)/2]<=x for 0<=x<=1, with lambda>0. At y0=1/2,
the actual integral minus the necessary lower bound is at most

    (L-9/2)/2+1/(8M) < -397/920 <0,                      (15)

because t>9/20 gives L<51/20 and M=23/100. Column identities hold a.e.;
choose good columns tending to 1/2. The integrated H and the required bound
are continuous, and the strict inequality persists. Thus the contradiction
does not assume a pointwise value of an a.e. marginal.

A common nonincreasing direction for all rows is also impossible: on
L<y<2L the column domain is the fixed interval [0,L], so such column
integrals could only decrease, while their required value y/2 increases.
Neither argument excludes mixed monotonic directions chosen separately for
different rows, a nonmonotone column potential, or the feasible wings already
proved to exist. The result identifies an exact limitation of this central
construction; it is not a new all-wing obstruction or a repeated smoothness test.

### A compatible leading corner model, with exact restricted traces

The failure above does not make a nonmonotone potential construction
implausible. One concrete boundary discriminator succeeds. Near the terminal
corner put s=L-x and delta=2L-y. K1969's actual phase gives, for 0<s<1-t,

    H(L-s)=kappa*s+eta*s^2,
    kappa=W/(2t)>2,   eta=lambda/(2M)>0.

The terminal column deficit is delta/2. These leading linear coefficients
are compatible with the explicit singular boundary model

    h_c(s,delta)=clip_[0,1](d+c log(s/delta)),
    4c^2 sinh^2(1/(2c))=kappa/2,
    d=(1+c log(2kappa))/2.                              (16)

There is exactly one c>0: writing z=1/(2c), the left side is
(sinh(z)/z)^2, strictly increasing from 1 to infinity as z increases.
Indeed z cosh(z)-sinh(z) has derivative z sinh(z)>0 and value zero at 0.
The exact rational sinh-series bounds in the certificate locate c in (1/4,1/3).

Set a=exp((d-1)/c) and b=exp(d/c), so b>a>0. The ramp of h_c has
a<delta/s<b. Direct integration gives

    int_0^infinity h_c(s,delta)d delta = c(b-a)s=kappa*s,
    int_0^infinity [1-h_c(s,delta)]ds = c(1/a-1/b)delta=delta/2.

The coefficients have product 4c^2 sinh^2(1/(2c)) and ratio ab=2kappa,
which proves both equalities. On a rectangle of width S and height D these
are exact only for the RESTRICTED traces b*s<D and delta/a<S. They cannot
cover every row and column of that rectangle: that would require
b*S<=D<=a*S, impossible because b>a. In the actual wing the corresponding
row cutoff is b*s<L+s. For actual terminal columns additionally require
delta<L, so their domain is the full interval 0<s<L; their combined
restrictions are delta<L and delta/a<L.

Thus (16) is a leading half-plane boundary model and an explicit compatibility
test for restricted inner traces, NOT a feasible local wing, full corner
rectangle or gluing certificate. It misses the actual eta*s^2 row term and
all global matching. The logarithmic potentials have finite L2 norm on every
finite interval because int_0^S log^2(s)ds is finite; this does not provide a
global wing dual potential. A global successor still has to construct actual
nonmonotone potentials satisfying both full marginal equations, justify their
active sets and endpoint matching, and prove the needed global integrability.

One tempting repair fails an independent requirement. Let beta=eta/kappa>0
and replace s by chi(s)=s+beta*s^2 in (16). This gives EXACT actual inner-row
mass kappa*chi(s)=H(L-s), provided b*chi(s)<L+s. But for inner terminal
columns delta<L and delta/a<chi(L), the substitution r=chi(s) changes the column deficit to

    int_0^infinity [1-h_c(r,delta)] / sqrt(1+4beta*r) dr
       < delta/2.

The inequality is strict because the deficit integrand is positive on an
interval and the Jacobian is strictly below one for r>0. Thus this explicit
row-only nonlinear correction fails the exact column constraint. The
restricted linear model cannot be promoted to an actual wing by that repair;
a coupled correction is still necessary.

## 8. Validation, contrary controls and remaining boundary

The producer passes 186 exact controls on renewal coefficients, norm weights, symmetry and
finite-approximation residuals, and encloses the actual algebraic norm with
48 rational convolution terms. The separate probe reconstructs polynomial
density pieces and integrates the clipped function directly across all spline
and clipping breakpoints. It checks the column identity, row defect, all 48
norm coefficients, finite stopped-mixture norm bounds, the norm enclosure and
projection/dual identities, the exact wing inequality and restricted corner integrals:
285 independent exact/symbolic controls pass. After a
green baseline it rejects four genuine mathematical corruptions: reversed
column sign, wrong cubic clipped moment, wrong renewal tail exponent, and
omitted norm multiplicity. The test controls concern exact mathematics; they
do not turn a count of passing samples into the continuum theorem.

Strongest overclaim: calling (4) the explicit whole-pulse optimizer. It covers
the central rectangle only. Strongest contrary case: q_N has exact columns
but generally nonzero rows; (12) exposes that residual rather than calling the
finite approximation feasible. The source/native-object preflight retained
the actual algebraic phase and all prior counterexamples. Postflight leaves
the wing problem as the unresolved construction, with central optimization
and its numerical strong-error question now removed from that queue.

The proof is self-contained and uses no newly imported theorem. Same-author
separate implementations are internal checks, not external expert acceptance,
proof-assistant verification or evidence of novelty. Source, physics-ledger
and canon verdicts remain unchanged; SC-META-53 remains UNCERTAIN.
