---
title: "K2201 Joint detector instability has rank at most two"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite-support variations of the supplied interior Fock detector profile with output field energy only
scripts:
  - tests/channel-swings/k2201_detector_joint_variational_structure_probe.py
---

# K2201 Joint detector variational structure

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2201 rank-two joint detector instability and finite Schur criterion
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and precise scope

After optimizing the two outcome squeezes, every finite-dimensional Hessian
of the detector profile energy has negative index at most TWO. The
fixed-squeeze Hessian is strictly positive on nonzero finite-support
variations, and squeeze relaxation subtracts exactly two nonnegative rank-one
forms. On any finite contrast-preserving variation space, positivity reduces
to an explicit two-by-two Schur complement. This bounds the dimension of every negative-definite variation space and
supplies a finite criterion without asserting joint convexity or uniqueness.

The theorem concerns the supplied positive Fock binary diagonal square-root
instrument with one real squeeze per outcome and output FIELD energy as cost.
It supplies neither apparatus/preparation/reset accounting nor GU physics.
SC-META-53 remains UNCERTAIN. Source, ledger0.263, LT-SM8/LT-GR6b, canon,
physical quotient and existing contrast frontier results remain unchanged.

K2184 already supplies the scalar envelope-curvature identity and a nonsmooth-boundary chord. The new results are the full vector Hessian and finite stability criterion, a smooth strictly interior full-tail witness, and a controlled tail prefactor.

## 1. The full-tail energy and allowed derivatives

Use [K2188](k2188-detector-variational-structure-2026-10-28.md) and
[K2194](k2194-detector-optimizer-structure-2026-10-28.md):

    p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n-x_n,
    R(z)=sum(n+1/2)z_n, T(z)=sum(n+1)sqrt(z_n z_(n+1)),
    A(s)=41s²/6+3/(2s²), C=40/3,
    E(x,s1,s0)=A(s1)R(x)+A(s0)R(y)-C[s1T(x)+s0T(y)]+35/18.

Assume every x_n,y_n is positive. At every nonzero branch the squeeze
minimizer is unique because A''(s)=41/3+9/s^4>0, the energy diverges at
s->0 and s->infinity, and its derivative has exactly one root. Denote the
roots s1(x),s0(x); they solve A'(sj)R(zj)=CT(zj). Set H(x)=min_s E.

All variations v below have finite support. Thus the modified edge sums and
all their derivatives are finite; the unchanged tail is retained exactly.
The implicit function theorem applies to each scalar squeeze stationarity
equation because dj=R(zj)A''(sj)>0. No exchange of an infinite derivative sum
or inverse of an infinite Hessian is assumed. Exact-contrast variations
satisfy sum(3n-1)v_n=0. Imposing a separate probability constraint is optional
and gives a smaller subspace; it is not part of the original problem.

## 2. All nonconvexity is a rank-two relaxation

For a positive branch z,

    DT(z)[v]=1/2 sum(n+1)sqrt(z_n z_(n+1))
                         [v_n/z_n+v_(n+1)/z_(n+1)].

Differentiating once more gives

    -D²T(z)[v,v]=1/4 sum(n+1)sqrt(z_n z_(n+1))
                         [v_n/z_n-v_(n+1)/z_(n+1)]².

Consequently the fixed-squeeze Hessian is

    Q(v)=C/4 sum(n+1){s1 sqrt(x_n x_(n+1))
                   [v_n/x_n-v_(n+1)/x_(n+1)]²
                 +s0 sqrt(y_n y_(n+1))
                   [v_n/y_n-v_(n+1)/y_(n+1)]²}.             (1)

It is strictly positive for every nonzero finite-support v. If even the first
branch sum vanishes, v_n/x_n is constant on every adjacent pair of the
connected half-line, and is zero outside the support; hence v=0. This argument
retains the final edge joining the varied prefix to its fixed positive tail.
Deleting that edge changes the claim.

Define the two squeeze scores

    b1(v)=A'(s1)R(v)-C DT(x)[v],
    b0(v)=-A'(s0)R(v)+C DT(y)[v],
    d1=R(x)A''(s1), d0=R(y)A''(s0).

Implicit differentiation gives s'_j[v]=-b_j(v)/d_j. Substitution yields

    H''(x)[v,v]=Q(v)-b1(v)²/d1-b0(v)²/d0.                 (2)

The full joint second variation, with squeeze variations t1,t0, is exactly

    E''[(v,t),(v,t)]=H''[v,v]+sum_j dj(tj+bj(v)/dj)².     (3)

Away from squeeze stationarity the same square completion describes the
joint Hessian with the algebraic residual Q-sum b_j²/d_j; only at the
minimizing squeezes is that residual the reduced-energy Hessian H''.
In particular Q is positive on ker b1 intersect ker b0. Every subspace on
which H'' is negative definite has dimension at most two: a subspace of
dimension three would contain a nonzero vector in that intersection. This
is an algebraic Morse-index bound on the finite-support tangent space,
not a spectral assertion about an unconstructed closed infinite operator.

## 3. Exact two-by-two test on any finite variation space

Choose any independent finite-support directions spanning a space V, with
contrast constraint already imposed. Let P be the positive-definite matrix
of Q on V, let B have the two rows b1,b0 evaluated on that basis, and
D=diag(d1,d0). The reduced Hessian matrix is

    M=P-B^T D^-1 B,
    S=D-B P^-1 B^T.                                    (4)

The symmetric block matrix [[P,B^T],[B,D]] has two congruence decompositions:
M direct-sum D and P direct-sum S. Since P,D are positive definite,
M and S have the same negative index and the same nullity. Thus M is positive
definite (respectively semidefinite) exactly when S is. This is a COMPLETE
criterion on V, including zero eigenvalues, not a determinant-only heuristic.
For a real symmetric two-by-two S, PSD means both diagonal entries and the
determinant are nonnegative; PD may use its first diagonal and determinant.

To test all finite-support variations, increase the varied prefix while
retaining its boundary edge and impose the same contrast constraint.
Every finite-support direction eventually occurs. An S with a negative eigenvalue provides negative finite-support curvature;
at an effect-stationary profile this is a genuine instability. Otherwise it
is a curvature statement; PSD of every prefix proves nonnegativity
on their algebraic union. No finite prefix proves all prefixes without
additional tail control, and even universal nonnegativity alone is not joint
uniqueness or a global minimum certificate. This supplies a precise consumer
for K2198's profile/tail enclosures rather than claiming that solver already
exists.

### Linear-arithmetic finite-prefix stability test

The two-by-two test does not require a dense contrast-projected matrix.
Vary coordinates0 through m and set v_(m+1)=0. Write L for the tridiagonal
matrix of the positive form Q before imposing contrast. For branch j define

    h_(j,n)=C s_j(n+1)sqrt(z_(j,n)z_(j,n+1))/4,
    L_nn=sum_j [h_(j,n-1)+h_(j,n)]/z_(j,n)^2,
    L_(n,n+1)=-sum_j h_(j,n)/(z_(j,n)z_(j,n+1)),

with h_(j,-1)=0. The last diagonal includes h_(j,m), the edge into the fixed
tail. Let q=(-1,2,5,...,3m-1)^T and B_raw be the two score rows on these
unconstrained coordinates. Since L is positive definite, q^T L^-1 q>0.
The inverse on the contrast-constrained space, represented in full coordinates,
is

    G=L^-1-L^-1 q (q^T L^-1 q)^-1 q^T L^-1.

If V is any basis matrix for q-perp, then G=V(V^T L V)^-1 V^T. To see this,
G b has q^T G b=0 and L G b-b is a multiple of q; it is the unique minimizer
of v^T L v/2-b^T v on q-perp. Parametrizing v=V a gives the stated identity.
Consequently the same complete two-by-two criterion is

    S=D-B_raw G B_raw^T.

Only THREE tridiagonal solves are needed: u=L^-1 q and the two columns of
Y=L^-1 B_raw^T. Then

    S=D-B_raw Y+(B_raw u)(B_raw u)^T/(q^T u).

For diagonal d_n and off-diagonal a_n, exact LDL elimination uses
pivot_0=d_0, ell_n=a_(n-1)/pivot_(n-1), and
pivot_n=d_n-a_(n-1)^2/pivot_(n-1). All pivots are strictly positive by L>0.
For each right-hand side b, forward substitute y_0=b_0,
y_n=b_n-ell_n y_(n-1), divide z_n=y_n/pivot_n, and backward substitute
x_m=z_m, x_n=z_n-ell_(n+1)x_(n+1).

This takes O(m) arithmetic operations and storage for a fixed three right-hand
sides, followed by scalar and two-by-two contractions. It is an arithmetic
operation count, not a bit-complexity bound. Exact or outward-certified input
coefficients must still be supplied; rational profile data need not make the
optimizing squeezes rational. It is a finite-prefix stability verifier, not
an optimizer, a global certificate, or a replacement for infinite-tail control.

The exact probe compares the three solves and constrained inverse against a
direct projected inverse for L=[[2,-1,0],[-1,3,-1],[0,-1,4]], q=(-1,2,5),
B_raw=[[1,2,3],[-2,3,1]], and V=[[2,5],[1,0],[0,1]]. The full comparison
and a planted omitted-constraint fault distinguish the constrained test from
an accidentally unconstrained susceptibility matrix. This fixture checks the
algorithm independently of detector-profile certification.

## 4. A released consequence: the exact optimizer tail has a power prefactor

This result concerns the true fixed-squeeze optimizer of K2194 and K2198,
not the arbitrary interior profiles of sections 1--3. Every joint optimizer
inherits it at its own squeezes. For positive interior contrast set

    f_n=1-e_n, b_n=sqrt(f_n), r_n=b_(n+1)/b_n,
    k=[5s1/4-(DeltaA-3eta)/C]/s0>5/4,
    c=s1/(4s0)-(DeltaA/2+eta)/(Cs0),
    r=2k-2sqrt(k²-1) in (0,1),
    a=r²(r-4c)/(4-r²), gamma=a/r.

Then a strictly positive finite constant L_infinity exists such that

    r_n=r+a/n+O(n^-2),
    1-e_n=L_infinity r^(2n) n^(2gamma)(1+O(1/n)).       (5)

K2194 supplied the limiting geometric ratio and K2198 supplied whole-tail
geometric envelopes. Neither determines the polynomial factor in (5).
In particular f_n/r^(2n) tends to infinity if gamma>0 and to zero if gamma<0;
it tends to a positive constant only if gamma=0. No optimizer or joint squeeze
is computed by this asymptotic statement.

Here is an explicit remainder argument. Take any K2198 whole-tail certificate
e_N>=L0>0, f_N<=F and r_n<=rho<1 for all n>=N. Put theta=rho² and
q=(1+1/(N+1))/4. K2198's exact recurrence is

    1/r_(n-1)+(1+1/n)r_n/4=k+c/n+d_n,
    |d_n|<=D theta^(n-N-1), n>=N+1,
    D=(s1/s0)F(1+q)/[sqrt(L0)(1+sqrt(L0))].

Indeed a_n=sqrt(e_n) is increasing and its backward and forward relative
increments are bounded by f_(n-1)/[sqrt(L0)(1+sqrt(L0))]. The geometric
second-moment sum therefore gives |d_n|<=D2/n², where

    D2=D[(N+1)²/(1-theta)+2(N+1)theta/(1-theta)²
                              +theta(1+theta)/(1-theta)³].

Set t_n=r+a/n. The coefficient a is forced by the 1/n equation
-a/r²+(r+a)/4=c. There is an exact rational residual identity:

    R_n:=1/t_(n-1)+(1+1/n)t_n/4-k-c/n
       =a(a-r)/[r² n(r(n-1)+a)]+a/(4n²).

Choose integer n0 at least N+1, 2, 2|a|/r and 2|a|/(1-r). For m>=n0,
r/2<=t_m<1, and for n>=n0+1 the residual satisfies |R_n|<=R0/n² with
R0=4|a(a-r)|/r³+|a|/4. Subtracting the two recurrences exactly, and using
0<r_(n-1),t_(n-1)<1, gives

    |r_(n-1)-t_(n-1)|
      <=(3/8)|r_n-t_n|+(D2+R0)/n².

Backward iteration from an arbitrarily remote actual ratio eliminates its
bounded terminal error. Thus for m>=n0,

    |r_m-r-a/m|<=K/(m+1)²<=K/m², K=(8/5)(D2+R0).      (6)

This uses the true infinite optimizer and backward contraction; it certifies
no guessed finite shooting prefix.

For the prefactor put B0=(|a|+K)/r and choose integer M>=n0,2,2B0. For n>=M,
z=(r_n-r)/r obeys |z|<=B0/n<=1/2. The elementary inequalities
|log(1+z)-z|<=z² and |log(1+1/n)-1/n|<=1/(2n²) imply

    |log(b_(n+1)/(r^(n+1)(n+1)^gamma))
                   -log(b_n/(r^n n^gamma))|<=E/n²,
    E=K/r+B0²+|a|/(2r).

The logarithms converge to a finite real limit. Exponentiation and squaring
prove L_infinity>0 and (5). More quantitatively,

    |log(L_infinity/[f_n/(r^(2n)n^(2gamma))])|
                          <=2E/(n-1), n>=M.            (7)

All constants may be conservatively enclosed. Actual numerical use of (7)
requires directed rigorous enclosures of its powers and logarithms; there
is no claim that this consumer uses only rational operations or has practical
complexity. The included rational residual controls check the asymptotic
algebra, not numerical computation of the true L_infinity.

## 5. A smooth full-tail negative-curvature control

Start from K2184's fixed-probability, fixed-contrast chord u,v, where
u1=42/5120, u6=33/5120, v3=3/256, v4=3/1024 and all other entries vanish.
Put epsilon=1/10000, delta=10^-20, x=delta p+epsilon(u+v)/2 and
w=epsilon(v-u). All x_n and p_n-x_n are positive, including the entire
geometric tail. The direction preserves probability, R and contrast;
d(x)=129epsilon/1024>0. The exact interval probe encloses both minimizing
squeezes using the full-tail R,T and verifies H''[w,w]<0. This is an actual
branch-optimized interior profile with negative curvature, not an
effect-stationary profile or a global optimizer. The numerical sign is accepted
only after the rational interval check; the chosen delta is not an assumed
continuity radius.

## Verification and useful next calculation

The exact probe differentiates original square-root edges independently,
checks the complementary-branch signs, completes the joint squares, and
verifies both Schur congruences, including positive, zero and two-negative
cases. Finite rational profiles are derivative controls and are explicitly
not asserted to be joint optimizers. The proof establishes the universal
rank bound; finite tests do not establish that a physical optimizer has a
negative direction. Existing nonconvexity witnesses remain compatible with
this bound. No new numerical energy bracket, practical complexity, external
specialist acceptance, proof-assistant certification or novelty is claimed.
