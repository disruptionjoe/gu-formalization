---
title: "K2204 Infinite detector stability from an energy completion and certified residuals"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: closed quadratic-form extension of finite-support detector variations under certified strict-monotone whole-tail bounds; no global optimization claim
scripts:
  - tests/channel-swings/k2204_detector_infinite_stability_certificate_probe.py
---

# K2204 Infinite detector stability certificate

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: K2204 coercive energy completion, infinite two-score Schur criterion and residual certificates
carrier: supplied positive scalar Fock vacuum with binary diagonal occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form; Q-completion of finite-support profile variations ON=declared_carrier
real_structure: real effects, positive square-root Kraus, one real squeeze per outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and output-field energy
target: certified whole-tail second-variation sign MAP-TYPE=intertwiner
```

## Result and limits

K2201's finite-prefix two-by-two test extends to a precise Hilbert completion
when the profile has certified strictly increasing effects and a uniformly
contracting complementary tail. K2198 supplies these hypotheses at the true optimizers for fixed positive
rational squeezes and rational interior positive contrasts it covers, after resolving
finitely many strict coordinate inequalities. No joint optimizer is required.

The new quantitative result is an explicit diagonal lower bound for the
fixed-squeeze quadratic form Q. It makes the contrast and both squeeze scores
continuous, defines the infinite two-score susceptibility by Riesz
representation, and bounds its error using arbitrary finite rational trial
vectors and certified whole-tail residuals. A finite positive certificate
therefore covers ALL finite-support exact-contrast variations and their energy
completion. No finite cutoff is silently substituted for the half-line.

This is a quadratic-form extension of the finite-support Hessian. The cap
constraints have no asserted open neighborhood in this topology. Arbitrary
elements of the completion need not generate feasible two-sided effect paths;
the theorem is not a Frechet-smoothness theorem on an open feasible set.
At minimizing squeezes the form extends K2201's reduced-energy Hessian. At
other squeezes it is the algebraic Schur residual of the JOINT Hessian, not
the reduced-energy Hessian. A nonstationary effect profile with positive
curvature is not a local or global minimizing detector.

No apparatus/preparation/reset cost, joint uniqueness, improved energy bracket,
GU physics, source verdict, ledger change, canon promotion, proof-assistant or
external-expert certification follows.

## 1. A usable coercivity estimate

Use K2201's p_n=(3/4)4^-n, C=40/3, x_n=p_n e_n,
y_n=p_n f_n, f_n=1-e_n, and positive squeezes s1,s0. Assume for EVERY n

    e_n >= L > 0,
    0 < sigma <= r_n=sqrt(f_(n+1)/f_n) <= rho < 1.       (1)

In particular the effects are strictly increasing and interior. Put

    R=rho²,
    kappa=C min(s1 L,s0 sigma)(1-R)²/32 > 0.

Then on finite-support v, retaining its final boundary edge,

    Q(v) >= kappa sum_(n>=0) (n+1)v_n²/p_n.             (2)

Proof: on one edge write u=v_n/sqrt(p_n), u'=v_(n+1)/sqrt(p_(n+1)),
e=e_n, e'=e_(n+1), f=f_n and t=r_n², so f'=tf. Set

    X=u/e-2u'/e',    w=u-2u'/t.

That edge of Q is exactly

    C(n+1)/8 [s1 sqrt(ee') X² + s0(sqrt(t)/f) w²].     (3)

Both coefficients inside brackets are at least m=min(s1 L,s0 sigma).
Solving the two linear equations gives

    u  = [ee' X - t e w]/(1-t),
    u' = [t ee' X - t e' w]/[2(1-t)].                  (4)

Since e,e'<=1 and t<=R, the inverse matrix has squared Frobenius norm at most
(1+3R²/2)/(1-R)² <= (5/2)/(1-R)² < 4/(1-R)². Therefore
X²+w² >= (1-R)²(u²+u'²)/4. Summing (3) proves (2), even after dropping
the nonnegative second copy of each u_n². These are uniform half-line bounds,
not positive numerical nodes.

For a true fixed-squeeze optimizer, K2194 gives e_n>0 and e_(n+1)>e_n;
K2198 gives sigma<=r_n<=rho on a tail n>=N. Refine its convergent finite
coordinate boxes until every edge n<N has separated positive endpoints and
0<r_n<1. Take the minimum L, minimum sigma and maximum rho over this finite
prefix and the tail certificate. This proves existence and gives finite data
certifying (1). This procedure does not claim a useful complexity bound.

### Stronger complementary-weight coercivity

The vanishing complementary tail supplies a stronger bound, needed for
convergence of the certifier. Put f0=1-e0>0 and

    kappa_y=(1-rho²)/[1/(kappa f0)+8rho/(C s0)].

Then

    Q(v) >= kappa_y sum_(n>=0)(n+1)v_n²/y_n.          (2b)

For proof set a_n=v_n/sqrt(y_n), h_n=sqrt(y_(n+1)/y_n)=r_n/2
and d_n=a_(n+1)-h_n a_n. The complementary branch alone gives
Q(v)>=Cs0/(2rho) sum(n+1)d_n². With W=sum(n+1)a_n²,
the inequality a_(n+1)²<=2h_n²a_n²+2d_n² gives

    W-a0² <= rho² W+4 sum(n+1)d_n².

By (2), a0²=v0²/(p0 f0)<=Q(v)/(kappa f0). Substitution proves (2b).
These manipulations are finite for finite-support v and then extend by
completion. A certified positive LOWER bound on f0 gives a conservative
computable kappa_y when the actual profile is enclosed rather than exact.

Arbitrary positive profiles from K2201 need not satisfy (1). For the constant
effect e_n=a, the formal nonzero vector v=p has Q(v)=0, and its finite
truncations have Q tending to zero. Thus the weighted-coordinate embedding
in (2) cannot be assumed merely from coordinatewise interiority.

## 2. The constrained energy space

Let H be the completion of finite-support real sequences under inner product
Q(v,w), obtained by polarizing K2201's fixed-squeeze form. Estimate (2) embeds
H continuously and injectively in the weighted sequence space with norm
sum(n+1)v_n²/p_n. The edge-difference map also embeds its completion into the
corresponding edge l² space; if all coordinates vanish, all limiting edge
differences vanish. This ensures injectivity, not only continuity of the
coordinate map. Q is the norm defining H; no unbounded Hessian inverse in an
unspecified ambient l² is used.

For a coefficient sequence a_n, Cauchy--Schwarz and (2) give

    |sum a_n v_n|² <= Q(v)/kappa * sum p_n a_n²/(n+1). (5)

The contrast q_n=3n-1 and the scores b1,b0 are therefore continuous. Indeed,
with A(s)=41s²/6+3/(2s²), the coefficients of DT(z) are

    g_(z,n)=[n sqrt(z_(n-1)/z_n)
                   +(n+1)sqrt(z_(n+1)/z_n)]/2,

where the first term is absent at n=0. Under (1),

    g_(x,n) <= n+(n+1)/(4sqrt(L)),
    g_(y,n) <= n/sigma+(n+1)rho/4.

Consequently |b_(j,n)| <= M_j(n+1), where

    M1=|A'(s1)|+C[1+1/(4sqrt(L))],
    M0=|A'(s0)|+C[1/sigma+rho/4].                      (6)

The infinite sums converge absolutely on H by (5).
Define H_c=ker q in H. This is exactly the closure of finite-support
contrast-zero variations: approximate v in H by finite w_k and repair
w_k to w_k-q(w_k)e_0/q(e_0), where q(e_0)=-1. The repair tends to zero.

## 3. Exact infinite two-by-two criterion

Let g_j in H_c be the unique Riesz representative of b_j restricted to H_c,
so Q(g_j,v)=b_j(v). Let K_ij=Q(g_i,g_j) and D=diag(d1,d0), with
d_j=R(z_j)A''(s_j)>0 as in K2201. The bounded quadratic form

    h(v)=Q(v)-b1(v)²/d1-b0(v)²/d0                     (7)

has the same negative index and kernel dimension as the real symmetric matrix

    S=D-K.                                          (8)

To prove this, let U:H_c->R² have components b_j(v)/sqrt(d_j). Then
h is represented in the Q inner product by I-U*U. The nonzero eigenvalues
of U*U and UU* agree with multiplicity: apply U or U* on each nonzero
eigenspace. UU*=D^(-1/2)KD^(-1/2), so the negative index and zero eigenspace
of I-U*U match those of I-UU*, and the latter is congruent to S. On the
orthogonal complement of span(g1,g0), h=Q. This also covers dependent or
zero scores. Thus h>=0 iff S>=0, and h is uniformly positive in the energy
norm iff S is positive definite. Its negative index is at most two.

Finite constrained prefixes are dense in H_c, so their exact K_m increase
in the Loewner order to K. A strictly negative direction in H_c has a
finite-support contrast-zero negative approximation; that finite direction
generates a feasible small two-sided path at an interior profile. Zero modes
in the completion need not generate such paths. Even strict positivity does
not establish nonlinear local optimality or global uniqueness.

## 4. A finite residual certifier with an infinite tail

Choose ANY finite-support contrast-zero vectors v1,v0 and ANY real numbers
lambda1,lambda0. Write L for the tridiagonal coefficient operator of Q,
interpreted on finite-support vectors, and define

    r_(j,n)=b_(j,n)-lambda_j q_n-(Lv_j)_n,
    T_ij=b_i(v_j)+b_j(v_i)-Q(v_i,v_j).                (9)

Let eps_j² be any certified bound on

    (1/kappa_y) sum_(n>=0) y_n r_(j,n)²/(n+1).       (10)

Since lambda_j q vanishes on H_c, the Riesz error g_j-v_j has energy norm
at most eps_j. The exact identity

    K_ij-T_ij=Q(g_i-v_i,g_j-v_j)

therefore yields

    0 <= K-T <= delta I_2,   delta=eps1²+eps0²,
    D-T-delta I_2 <= S <= D-T.                       (11)

This identity is why rational approximate solves suffice: v_j need not be
an exact Galerkin solution, and coefficient intervals do not invalidate
the error certificate. The lambda_j are freely chosen for smaller residuals;
they are not assumed to be optimization multipliers.

For support 0..m, Lv_j has support 0..m+1. Enclose each r_j through m+1,
INCLUDING the junction r_(j,m+1). For n>=m+2, (6) and |q_n|<=3(n+1) give
|r_(j,n)|<=(M_j+3|lambda_j|)(n+1). Put h=rho²/4, N=m+2 and

    Y_N=y_N[(N+1)/(1-h)+h/(1-h)²]
       >= sum_(n>=N)(n+1)y_n.

The bound follows from y_(N+k)<=y_N h^k and the two geometric sums.
An upper enclosure of y_N is sufficient. Hence a fully finite bound is

    eps_j² := [sum_(n=0)^(m+1) y_n sup|r_(j,n)|²/(n+1)
            +(M_j+3|lambda_j|)² Y_(m+2)]/kappa_y.    (12)

The right side is used AS the chosen eps_j² in (10); it is an upper bound
on the actual error, not a claimed exact residual norm. All quantities can
be outward-enclosed rationally. The last geometric factor bounds the full
complementary weighted tail. An incorrect junction deletion invalidates (12).

For exact coefficients K2201's three tridiagonal solves produce Galerkin
v_j and lambda_j. For interval coefficients, midpoint solves and rational
rounding followed by exact q repair produce valid trial vectors, and (9)--(12)
certify their actual error. This avoids treating an interval midpoint as
the true profile or squeeze.

Return STABLE if D-T-delta I_2 is certified positive definite. Return
UNSTABLE if an explicit rational two-vector has strictly negative quadratic
form for D-T. Otherwise return INDETERMINATE and retain the enclosure.
The positive branch covers the entire energy space; the negative branch
implies a finite feasible negative-curvature direction by density. At an
effect-stationary profile it is instability; otherwise it is curvature only.

### Why the refined certificate terminates at strict signs

The p-weight version from (2) is valid but does not by itself prove
convergence of its junction error. Bound (2b) resolves this seam. Let v_j^m
be the EXACT constrained Galerkin solution. Density gives v_j^m->g_j in Q,
and hence in the stronger y-weight norm. The prefix residual through m is
zero. For m>=1, its n=0 equation gives
lambda_j^m=(Lv_j^m)_0-b_(j,0), so lambda_j^m converges and is bounded.
The only nonzero L contribution to the remaining residual is at m+1.

The off-diagonal coefficient obeys

    |L_(m+1,m)| <= B(m+1)/y_m,
    B=(C/2)(s1/L+s0/sigma).

Indeed sqrt(x_m x_(m+1))>=L p_m/2 and
sqrt(y_m y_(m+1))>=sigma y_m/2 in K2201's off-diagonal formula.
Since y_(m+1)<=rho² y_m/4, the squared junction contribution from Lv
in (10) is at most B²rho²(m+1)(v_(j,m)^m)²/(4kappa_y y_m). This tends to zero:

    (m+1)(v_(j,m)^m)²/y_m
      <=2(m+1)g_(j,m)²/y_m
          +2 sum_n(n+1)(v_(j,n)^m-g_(j,n))²/y_n -> 0.

The score part at the junction and the whole tail in (12) tend to zero
geometrically, since the multipliers are bounded. Using (a+b)²<=2a²+2b²
for the complete junction residual proves eps_j²->0. Therefore both sides
of (11) converge to S.

Finite rational trial rounding and coefficient intervals can be refined at
each prefix until their finitely many residual perturbations are arbitrarily
small. For a computably enclosed profile satisfying (1), dovetailing prefix
growth and refinement terminates if S is positive definite or has a strictly
negative eigenvalue. In particular, it decides every nonsingular S; singular
positive-semidefinite cases may remain indeterminate. No rate, bit-complexity,
joint optimizer or practical performance theorem is asserted. The supplied
probe has a declared finite list of trial cutoffs and reports INDETERMINATE
if none certifies; that bounded implementation is not the unbounded dovetail.

## 5. Reproducible non-optimizer control

Use the exact monotone profile

    t_n=2^(-n-1),
    sqrt(e_n)=(1-t_n²)/(1+t_n²),
    sqrt(f_n)=2t_n/(1+t_n²).

All profile entries, square-root edge factors and local coefficient factors
are rational. It has e0=9/25 and
r_n=(1/2)(1+t_n²)/(1+t_n²/4), so (1) holds with
L=9/25, sigma=1/2, rho=10/17. It is not asserted to be a fixed-squeeze or
joint optimizer. Each branch moment and coherence is enclosed by a rational
prefix plus a positive geometric tail; the actual unique minimizing squeeze
is enclosed using the strictly increasing stationarity equation. Thus the
curvature test uses true minimizing squeezes, not s1=s0=1 by assumption.

The released exact interval certificate uses support0..4 and proves

    S > 6 I_2,    eps1²+eps0² < 53/50.

In particular the reduced curvature is positive on the entire constrained
energy completion. The minimizing squeezes are approximately1.0483718181
and0.8622962442; these decimal displays are not the certification inputs.
The rigorous Schur lower matrix has diagonal intervals above9.9334 and6.6915
and off-diagonal absolute value below0.2763. Exact rational diagonal dominance
proves the stated6I margin. This does not confer stationarity or minimality
on the supplied profile.

The companion probe reports the finite trial support, true-squeeze intervals,
residual bounds and final whole-tail decision. It distinguishes a successful
whole-tail certificate from an indeterminate enclosure. Finite exact controls
and planted mutations check the transformation, contrast projection, final
boundary edge, residual Gram identity, tail sum, and squeeze bracket.
The written proof, interval fixture and finite algebraic controls are separate
evidence kinds. This fixture is a reproducible consumer of the theorem, not
an energy optimum, a new energy bracket or an independent physical prediction.

## Reproducibility seam and next useful work

K2201's tridiagonal implementation is checked against an independent small
matrix, while its actual detector witness certifies negative curvature in a
single supplied direction. That work accurately disclaims a full infinite
inverse and all-prefix positivity. The present residual construction closes
the mathematical infinite-domain seam under explicit stronger profile
hypotheses and creates an actual-profile all-tail verification route.
The complementary-weight bound additionally proves convergence of the
residual certificate under refinement. Remaining seams are singular Schur
matrices and practical conditioning/complexity, followed by nonlinear and
global optimization. K2196's terminating dual enumeration and K2176's energy
bracket remain separate results.
