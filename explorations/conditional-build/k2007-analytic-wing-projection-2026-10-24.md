---
title: "K2007: Analytic full-wing projection and a strict capped norm certificate"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2007_analytic_wing_projection.py
  - tests/channel-swings/k2007_analytic_wing_projection_probe.py
---

# K2007: Analytic full-wing projection and a strict capped norm certificate

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
result: explicit actual full-wing uncapped minimum, strict capped norm certificate and weighted marginal inverse
carrier: K1991 triangular wing of the fixed width9 scalar strip LAYER=toy CHIRALITY=N/A
pairing: Lebesgue marginal integrals and real L2 norm ON=actual_wing
real_structure: real L2 functions; cap imposed on comparison pulses, expressly relaxed for projection
grading: triangular and rectangular column ranges, not source chirality
action_owner: repository-construction -- unchanged conditional scalar transport problem
target: full-wing analytic projection and certified whole-pulse lower norm MAP-TYPE=intertwiner
```

## Result and dependency check

The actual full wing has an elementary integral formula for its unique
minimum-L2 pulse when its amplitude cap is relaxed. Its primitive is rational
plus logarithms on the three actual phase pieces. Both continuum marginals
are exact, and its squared norm reduces to one nonsingular one-dimensional
rational integral. An integrated positive-area wedge proves a strict extra
norm cost for every capped wing.

A separate, stronger consumer restricts the existing K1989 additive dual to
the two wings and replaces its forced/central contributions by their exact
regional values. This raises the certified whole-pulse squared-norm lower
bound from 2.34940177149 to **2.361527**, while retaining K2003's upper:

    2.361527 < ||v_dagger||^2 < 2.739952052817663.          (0)

The producer and independent probe both prove the displayed lower threshold.
The [machine-readable report](../../lab/process/k2007-analytic-wing-projection.json)
contains rational enclosures, including the improvement exceeding 0.012125.
The explicit projection and its scaled clipped duals are useful but weaker
bounds; they are not credited with the final numerical improvement.

This is a full-wing lower certificate, not an amplitude-feasible primal wing
or the full capped optimizer. A weighted contraction also supplies an explicit
stable inverse for compatible marginal errors. It does not preserve the cap.
The already optimal scalar phase and its Dirichlet energy do not change.

[K1986](k1986-pulse-primal-dual-certificates-2026-10-23.md) already solved the
uncapped *whole-strip* problem through a convergent Neumann construction.
Here the tighter feasible class forced by the saturated cuts of
[K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md) is used: forced
values are retained, and only each residual wing's cap is relaxed. The
one-dimensional elementary solution and its factorized norm consumer are new
within this sequence; orthogonal projection itself is an established method.
K2003's central optimizer and the nonlinear corner construction remain distinct.
Neither a local corner formula nor a global uncapped projection supplies the
missing globally capped wing. K1993's H1 obstruction remains intact.

## 1. Actual full-wing data

Let t be the same root in (9/20,23/50) of

    101t^4-102t^3-168t^2+392t-138=0.

Put M=23/100, L=3-t, W=3+4t. The actual left wing is

    Omega = {(x,y): 0<x<L, x<y<2L}.

For q=v/M its row and column integrals must be

    R(x)=2phi(x-3)/M-9+2L-x,
    C(y)=0                 for 0<y<L,
         y-L               for L<y<2L.                  (1)

The actual phase, including its plateau, is retained. If lambda is the K1969
positive contact multiplier, its left-side pieces are

    phi(x-3)=(1-lambda/2)x+(lambda/2)x^2                 on [0,1],
             1                                         on [1,2],
             3+lambda(3-t^2)
              +[-1+lambda(t^2-5)/2]x+(lambda/2)x^2     on [2,L].

The identities int_0^L R=L^2/2 and R(L)=-L follow from the actual contact
relations and are verified separately. All equalities are Lebesgue a.e.;
continuous endpoint representatives are used only for the uncapped formula.

## 2. Exact rational/logarithmic solution

Define

    I(x)=xR(x)-int_0^x R(s)ds,
    u'(x)=I(x)/[x^2(2L-x)],   u(0)=0,
    a(x)=u(x)+xu'(x),
    b(y)=-u(y)                       for 0<y<L,
          y/L-1-u(L)                 for L<y<2L,
    q0(x,y)=a(x)+b(y).                                   (2)

Near zero I(x)=O(x^2), so u' has a finite limit. The potential u is continuous
on [0,L] and piecewise smooth. Every integral in (2) is proper after removing
this endpoint factor. Since R is piecewise quadratic, I is piecewise cubic
with no linear term, and u is explicitly rational plus logarithms.

The exact prefix primitive is int_0^x a(s)ds=xu(x). Consequently a lower
column has integral

    int_0^y q0(x,y)dx = yu(y)-yu(y)=0,

and an upper column has integral y-L. There is no sampled-column assumption.

For the row, differentiating the desired integral gives

    (2L-x)a'(x)-a(x)+u(x)=R'(x).

Substituting (2) makes this exactly

    [x^2(2L-x)u'(x)]'=xR'(x),                            (3)

which holds because I'=xR'. At the terminal row, compatibility gives
I(L)=-3L^2/2 and u'(L)=-3/(2L). Its row integral is therefore
L^2u'(L)+L/2=-L=R(L). Equation (3) and continuity across x=1,2 now prove
all rows. This checks the integration constant, not just the differentiated
equation.

For every other L2 function q with the same two marginals, d=q-q0 has zero
marginals. Fubini gives <a(x)+b(y),d>=0. Thus

    ||q||^2=||q0||^2+||q-q0||^2.                         (4)

The formula is the unique global uncapped minimum over all L2 competitors.
Additivity is a certificate, not a restriction on competitors.

## 3. Exact norm and whole-pulse consumer

The column-only solution q_b is zero on y<L and y/L-1 on y>L. Its norm is
L^2/3. The difference q0-q_b has zero columns, so the two terms are
orthogonal. Put r=R-L/2 and J(x)=int_0^x r. Then int r=0 and I=xr-J.
Using the row marginal and integrating by parts gives

    ||q0-q_b||^2 = int_0^L [u+xu']r dx
                 = int_0^L u'(xr-J)dx.

Hence

    Q0 := ||q0||^2
       = L^2/3 + int_0^L I(x)^2/[x^2(2L-x)]dx.          (5)

No numerical quadrature is needed. Each piece of the integrand is a rational
function with denominator x^2(2L-x). Polynomial division gives a polynomial
plus A/x+B/x^2+C/(2L-x); A=B=0 on the first piece. Rational root isolation,
outward interval arithmetic and an atanh-series logarithm bound enclose (5)
at the actual algebraic parameters. The independent probe uses monomial
integral recurrence instead of the producer's partial fractions.

The fixed forced area is 54-3L^2-2tW. If N_C is K2003's exact physical
central minimum, every capped whole pulse therefore satisfies

    ||v||^2 >= M^2[54-(7/3)L^2-2tW
                       +2 int_0^L I(x)^2/[x^2(2L-x)]dx] + N_C.       (6)

This retains the exact forced support, unlike the earlier whole-strip
uncapped relaxation. The additional positive cost below strengthens (6).

## 4. A strict cap cost from an integrated wedge

The terminal trace of (2) is universal for these endpoint marginals:

    q0(L,y)=y/L-5/2,                  L<y<2L.            (7)

In particular the cap is violated on an open set adjacent to that row.
To price a positive-area set, write s=L-x. On 0<=s<=1/9 the actual terminal
phase gives

    R(L-s)=-L+(2kappa-1)s+2eta*s^2,
    kappa=W/(2t),  eta=lambda/(2M).

Here kappa<=16/3 and eta<7/46. Thus |R'|<=29/3+14/207=:B_R,
and R'<0. Since I'=xR',

    -3L^2/2 <= I(x) <0

throughout this strip: the upper estimate is at most
-3L^2/2+LB_R/9<0. With L>127/50=:L_min,

    |a'(x)| = |R'(x)+xu'(x)|/(2L-x)
      <= [B_R+(3/2)/(1-1/(81L_min^2))]/L_min <9/2.      (8)

All inequalities are checked with exact rationals. Consequently q0(x,y) is
at most y/L-5/2+(9/2)s. On the whole wedge

    0<s<1/9,   L<y<L[3/2-(9/2)s]

its distance below -1 is at least 1/2-(9/2)s-(y-L)/L. Integrating the
square of that affine deficit gives exactly

    int_wedge (|q0|-1)_+^2 >= L/864.                    (9)

For every capped feasible q, (4) therefore yields

    ||q||^2 >= Q0+L/864.                               (10)

Adding 2M^2L/864 to (6) gives a valid whole lower bound near 2.31425487,
which is weaker than the inherited K1989 lower and is retained as a comparison.
The wedge
is a sufficient region, not the complete clipped active set or sharp cap cost.
Equivalently, q0 is an additive dual potential: the squared-norm cap conjugate
is H(p)=p^2 for |p|<=1 and 2|p|-1 otherwise. Its dual value is
Q0+int_Omega(|q0|-1)_+^2. Equation (9) rigorously underestimates that dual
improvement. Clipping q0 itself does not preserve its marginals.

## 5. Full-domain dual comparison and the improved bound

A larger positive cost can be priced without identifying the clipped active
set exactly. Put d(x)=a(x)-u(L). On the upper rectangle q0=d(x)+y/L-1.
For an additive dual p=gamma*q0 with gamma>0 its normalized wing certificate is

    (2gamma-gamma^2)Q0 + int_Omega (|gamma*q0|-1)_+^2.     (11)

The upper-rectangle excess at each x is exactly

    L/(3gamma) [(-1-gamma*d)_+^3-(-1-gamma*(d+1))_+^3
                 +(gamma*(d+1)-1)_+^3-(gamma*d-1)_+^3].

The actual R has |R'|<=10. Since I=int_0^x sR'(s)ds, |u'|<=5/(2L-x).
Equation (3) then gives |a'|<=15/L<6 and |b'|<2 on lower columns.
These are whole-interval bounds, not derivative samples. The producer evaluates
analytic d and e(y)=u(L)-u(y) at the midpoints of 48 cells per actual phase
piece. It expands the potential enclosures by 3 times the row width and,
for lower triangular cells, one column width. Upper excess is minimized on
each resulting d interval; lower excess uses the distance of the full q
interval from [-1/gamma,1/gamma]. Complete off-diagonal rectangles are
integrated, and diagonal triangles are omitted with a nonnegative remainder.
Every accepted contribution is therefore a continuum lower bound.

Seven rational scales from 1 through 2 are executed. The best certified
scaled-projection result here is gamma=5/4 and a whole lower bound about
2.33913928. This remains below the earlier K1989 certificate: neither the
uncapped projection nor clipping it is quietly reported as the new optimum.

For the stronger comparison, restrict the *already published* K1989 physical
potentials to the actual wing and divide them by M. In left-wing coordinates
x=u+3,y=z+3 write these constant-on-cell normalized potentials A_i,B_j. For
right-wing reflection use x=3-u,y=12-z and negate the corresponding reversed
potentials, because the pulse itself changes sign. Evaluate each wing's
normalized certificate exactly as

    D_w = 2 sum_i A_i int_cell_i R(x)dx
          +2 sum_j B_j int_cell_j C(y)dy
          -sum_ij area(Omega intersect cell_ij) H(A_i+B_j),
    H(p)=p^2 for |p|<=1, otherwise 2|p|-1.               (12)

There are 11 row cells and 21 column cells per wing, with exact triangular
areas and the actual algebraic terminal cuts. All coefficients A_i,B_j and
conjugate values are rational. The row integrals are the true polynomial
phase integrals; no surrogate forcing or sampled marginal is substituted.
Both left and reflected-right certificates are evaluated. Their best proven
lower bound is mirrored, a valid operation because the two actual wing
problems have equal minima. This does not assume that K1989's rounded
potential arrays were exactly reflection symmetric.

Combining D_w with the exact forced area and central optimum gives

    ||v_dagger||^2 >= M^2(54-3L^2-2tW)+N_C+2M^2 D_w,

whose certificate lies near 2.361527248366888. The exact lower endpoint exceeds
the common displayed threshold in (0). The independent probe reconstructs
the region areas and integrals and independently clears that threshold.
This is a stronger feasible *dual* certificate, not a new capped primal wing.

## 6. A stable unrestricted marginal inverse

Let P,Q be the orthogonal row and column conditional expectations in L2(Omega).
On row functions the natural norm is int_0^L (2L-x)f(x)^2dx. The operator
K=PQP is positive and self-adjoint in this weighted space; its invariant mean
is the (2L-x)-weighted mean, not the unweighted x mean.

The common rectangle L<y<2L supplies

    <f,(I-K)f> >= L int_0^L (f-mean_x f)^2dx
      >= (1/2) min_c int_0^L (2L-x)(f-c)^2dx.           (13)

The first inequality is the nonnegative conditional-variance decomposition
restricted to that rectangle. The second uses 2L-x<=2L and the variational
characterization of the weighted mean. Thus K has norm at most 1/2 on
weighted-mean-zero rows. The inverse (I-K)^-1=sum_(j>=0)K^j has norm at most2
there, with a geometric L2 truncation bound.

For compatible marginal residuals deltaR,deltaC define d(y)=min(y,L),
c(y)=deltaC(y)/d(y), g(x)=deltaR(x)/(2L-x)-Pc(x). Assume these belong to
the indicated weighted L2 spaces; equality of the two total residual masses
makes g weighted-mean-zero. Put

    a=(I-K)^-1 g,   e=c+(I-Q)a.

Then e has exactly the requested residual marginals, and orthogonality gives

    ||e||^2=||c||^2+<a,g> <= ||c||^2+2||g||^2.          (14)

This is an effective error-to-correction bound for the *unrestricted* problem.
It does not assert that adding e to a capped approximation preserves the cap,
that a finite iterate is feasible, or that K1980's capped strong-limit error
now has an effective modulus.

## 7. Verification, adverse controls and next boundary

The producer passes nine exact parameter/norm/wedge control groups, evaluates
seven full-domain scaled certificates, and independently evaluates both
restrictions of the inherited witness. The separate probe passes 22
symbolic/rational groups, verifies four provenance hashes separately, and
rejects six mathematical corruptions after its
green baseline. Its independently computed lower also exceeds 2.361527.
Production replay and the separate probe use the saved certificate; neither
passing count substitutes for the continuum arguments.

The producer encloses actual algebraic parameters, exact rational/log norm
integrals, the derivative bound, region-restricted duals and whole-pulse consumer. The separate probe
reconstructs the phase pieces and uses a distinct antiderivative recurrence, reconstructs the selected inherited
dual restriction independently, and checks the ODE, integration constants, column primitive, norm normalization
and wedge integral. Six mathematical faults fail after a green baseline: wrong ODE denominator,
terminal column slope, norm multiplier, wedge cost, normalized cap conversion
and truncated triangular cell area. The last two corrupt the decisive
inherited-dual consumer and are rejected against its independently recomputed
actual certificate. Provenance hash checks are reporting checks, not mathematics.
Continuum projection and the weighted inverse rely on the written proofs,
not finite passing controls.

Strongest overclaim: calling the analytic projection a capped feasible wing.
Equation (7) directly refutes it. Strongest boundary case: the vanishing
triangular columns near zero; both the endpoint cancellation in (2) and the
weighted spaces in (13)-(14) retain those columns. The remaining problem is a
nonmonotone global capped construction or an attained global dual, with the
already constructed local corner data correctly matched to the other boundary.
An improved lower certificate does not identify the full minimizer.

The preflight retained the actual K1991 phase and all prior cap, monotonicity,
rank and H1 obstructions. The closing interpretation leaves source,
physics-ledger and canon verdicts unchanged. SC-META-53 remains UNCERTAIN.
This is conditional internal mathematics, with no novelty, external expert
acceptance or proof-assistant certification claimed.
