---
title: "K2050: Local conservation laws, positive densities and sign-sensitive continuation"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all C2 field-only conservation laws of the declared matched polynomial family; no general complex large-data theorem
scripts:
  - tests/channel-swings/k2050_local_conservation_classification.py
  - tests/channel-swings/k2050_local_conservation_classification_probe.py
---

# K2050: Local conservation laws, positive densities and sign-sensitive continuation

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: complete density classification, even-power phase-plane continuation and changed-sign blowup
carrier: two complex classical commuting fields in one space dimension LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: weighted positive density exactly in the classified positive-sign cases ON=declared_graph
real_structure: complex coordinates for real commuting components
grading: polynomial degree, not fermionic parity
action_owner: repository-construction -- K2048 matched polynomial extension
target: local conservation and classical continuation MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] In K2048's matched polynomial family,
all autonomous real C2 conservation laws whose density AND flux depend only
on the fields are classified. A nonconstant such law exists precisely for a
shifted pure power. Its density is positive definite precisely for positive
coupling. The actual sextic has only its known mass density in this entire
class, including nonpolynomial candidates. This closes one proposed route
to a new amplitude estimate, not the large-data problem itself.

The classification releases two substantial consequences: global two-sided
phase-plane continuation for every positive-coupling even power, including
zeros; and exact finite-time blowup for a negative-coupling control that still
has the same characteristic phase current. That control is a changed PDE.
It is NOT a blowup solution of the actual positive-coupling sextic.

## 1. Object, quantifiers and full local-law classification

Use u=x-t, v=x+t and the fixed family

    z_v = i conjugate(z) F(w),
    w_u = -i lambda z^2 conjugate(Fprime(w)),             (1)

where F is a nonconstant complex polynomial and lambda is real and nonzero.
K2048 proves J=Im(conjugate(z) z_u) has J_v=0 throughout this family.
Consider real C2 functions H,K on ALL of C^2, with no explicit x,t and no
field derivatives, satisfying H_t+K_x=0 for every local smooth solution.
Constants in H and K are immaterial. Then a nonconstant law exists iff

    F(w)=A(w-w0)^n, A!=0, integer n>=1.                 (2)

All such laws, modulo constants, are real multiples of

    H=|z|^2+|w-w0|^2/(lambda n),
    K=|z|^2-|w-w0|^2/(lambda n).                       (3)

Thus a positive definite quadratic density centered at (0,w0) exists iff
lambda>0. With lambda<0 every nonconstant density is indefinite. These
statements classify this exact local-law class, not derivative, nonlocal,
explicit-coordinate or nonsmooth conservation laws. Constant F and lambda=0
are excluded; they have free-field exceptions.

### Proof without a polynomial ansatz for H or K

Arbitrary spatial first jets are allowed by the semilinear Cauchy problem.
Their coefficients give, in real component coordinates,

    K_z=H_z, K_w=-H_w, and the conjugate equations.

Equality of mixed derivatives forces H=h(z,bar z)+k(w,bar w) and
K=h-k plus a constant. The remaining identity is h_v=k_u. Write
q(z)=bar z h_z using Wirtinger derivatives. Substituting (1) gives

    -Im(q(z) F(w))
      =lambda Im(z^2 conjugate(Fprime(w)) k_w(w)).     (4)

A nonconstant holomorphic polynomial has two values independent over R.
Evaluate (4) at corresponding w values. It follows that q(z), as a complex
function, lies in the complex span of z^2 and bar z^2:

    q(z)=a z^2+b bar z^2, with constant complex a,b.

For z!=0, h_z=a z^2/bar z+b bar z. Since h is real C2,
h_(z bar z)=-a z^2/bar z^2+b must be real for every phase of z.
Hence a=0 and b is real; continuity at zero gives h=b|z|^2+constant.
If b=0, (4) makes k_w=0 away from the finite zero set of Fprime,
so continuity makes the whole law constant. Otherwise comparison of the
z^2 coefficients gives

    k_w=(b/lambda) conjugate(F/Fprime).                (5)

On the complement of the zeros of Fprime, reality of k_(w bar w)
requires (F/Fprime)' to be real. This holomorphic function is therefore a
real constant c. The punctured plane is connected, so F/Fprime=cw+d
there. This is a polynomial identity F=(cw+d)Fprime everywhere, not an
assumption about cancelling poles. Leading coefficients give c=1/n,
n=degree F. The identity implies F=A(w-w0)^n, w0=-nd.
Equation (5) now integrates to (3); direct substitution proves sufficiency.
This covers all C2 laws, and does not infer completeness from finite tests.

For the actual sextic F=w^4, lambda=1/4, (3) is exactly H=|z|^2+|w|^2.
For example F=w^4+w^2 preserves J but admits no nonconstant field-only H,K
of this class. Merely matching the phase current does not preserve a positive
local density.

## 2. An additional derivative law for the actual sextic

Return to lambda=1/4 and F=w^4. Let

    P=Re(z^2 conjugate(w)^4), K_wphase=Im(conjugate(w) w_v).

Differentiating the actual PDE gives

    (K_wphase)_u + P_v/2 = 0.                          (6)

Indeed w_uv=2|z|^2 w|w|^6-3i z^2 conjugate(w)^2 conjugate(w_v).
The imaginary part of conjugate(w_u)w_v+conjugate(w)w_uv
is -2 Re(conjugate(z)^2 w^3 w_v), whereas P_v is four times
that real part. In physical coordinates, K_wphase=Im(bar w w_x)+P.
Thus compact smooth solutions conserve

    D=integral [Im(bar w w_x)+P/2] dx.                 (7)

The local flux is -Im(bar w w_x)-3P/2. This derivative-dependent law is
outside section1's classification and cannot be excluded by it. No coercivity
or positive Hamiltonian interpretation follows from (7).

## 3. Exact noncoercivity of these conserved data

Choose a nonzero real C-infinity bump phi of compact support and, for A>0,
set initial data

    z_A(x)=exp(i*pi/4) A phi(A^2 x),
    w_A(x)=A phi(A^2 x).                               (8)

Their total mass is the SAME number 2 integral phi^2 dx for every A.
Their full characteristic current is identically zero: K2048's Cauchy
formula is J=Im(bar z z_x)-P, and both terms vanish. The integral D is
also zero. Nevertheless their supremum grows linearly in A, their squared
H1 seminorm grows as A^4, and the spatial integral of |z|^2|w|^4 grows
as A^4. Thus mass, the entire function J, and D together cannot bound any
of these quantities uniformly. This is a precise failure of coercivity;
it does not forbid estimates that also use initial supremum or derivatives.
These are actually globally complete phase-plane data by K2046, so the
example must not be presented as blowup or as a counterexample to global
existence.

## 4. Released positive-sign theorem for all even powers

The classified pure powers support a generalization of K2046, not merely
another quartic fixture. Take F=w^(2m), lambda>0, integer m>=1 and
write gamma=2m lambda>0. On constant phase planes
z=exp(i theta)X, w=exp(i phi)Y with real X,Y and
cos(2theta-2m phi)=0, put sigma=sin(2theta-2m phi)=+1 or -1.
Then, allowing zeros and either sign of X,Y,

    Dplus X=2 sigma X Y^(2m),
    Dminus Y=-2 gamma sigma X^2 Y^(2m-1).

Set a=X^2, b=Y^2. The positive conserved density is a+b/gamma.
Every smooth bounded initial profile with bounded derivatives and finite
M=integral(a0+b0/gamma) dx has a unique global smooth solution in BOTH
time directions. For m=1 no finite-charge assumption is needed for the
finite-time amplitude bounds below; retaining it gives one uniform class.

For sigma=+1, b<=B=sup b0 forward. The positive null flux estimate gives
integral b dt<=gamma M/2 on each right ray, so

    a<=A exp(2 gamma M B^(m-1)), A=sup a0.              (9)

For sigma=-1, a<=A. If m=1, b<=B exp(4 gamma A t), enough for every
finite-time continuation. Suppose m>=2 and B>0, and set L=sup|b0prime|.
On each strip where b0(v)>0 define c=b^(1-m). In u<=v,

    a_v=-2ab^m, b_u=-2gamma ab^m,
    c_u=2gamma(m-1)a,
    c_v=2(m-1)/c^(1/(m-1))+f(v),
    f=c0prime-2(m-1)(gamma a0+b0).                     (10)

The last identity follows by differentiating c_u in v and comparing with
partial_u[2(m-1)b], then evaluating on the initial diagonal. The conserved
null flux also gives

    c>=c0-2gamma(m-1)M.                               (11)

Let C=2gamma(m-1), h=B^(1-m)/2 and choose the explicit finite bounds

    K=(m-1)L max(1,h+CM)^2+2(m-1)(gamma A+B),
    epsilon=min(h,[(m-1)/(K+1)]^(m-1))>0.              (12)

At a hypothetical first downward crossing c=epsilon, (11) gives
c0<=h+CM. Since m/(m-1)<=2,
|c0prime|=(m-1)L c0^(m/(m-1)) is bounded by the first term of K.
Thus f>=-K, while the repulsive term in (10) is at least2(K+1).
Consequently c_v>=K+2>0, contradicting that first crossing.
At an initial zero of Y, c0 tends to infinity from each positive component;
(11) prevents entry below the barrier from such an endpoint. On the zero
ray Y stays zero by ODE uniqueness. The same connected-component argument
as K2046 covers accumulating zeros. Hence b<=epsilon^(-1/(m-1)) globally
forward. B=0 is free transport and is handled separately.

Polynomial local existence and the amplitude bounds give all derivative
bounds on each finite time interval by differentiating the characteristic
integral equations and iterating the linear inequality. The reflection
(t,x)->(-t,-x) exchanges sigma signs, proving backward completeness.
Compact supports then separate after half their initial support width,
giving exact two-sided free scattering. This is a theorem on the phase
planes, not all complex phases or transverse dynamics.

It also releases fixed-support complex neighborhoods for every even power.
On the max-amplitude ball R, the actual complex force has Lipschitz constant
at most L_R=2(2m+1)max(1,gamma)R^(2m). For a compact reference bounded
by R0, choose eta>0, R=R0+eta, and T greater than half the common support
width. Initial uniform perturbations smaller than (eta/2)exp(-L_R T),
with the SAME compact support, stay within eta through [-T,T] by a first-exit
Gronwall argument. Then supports are disjoint and motion is free. This proves
global, generally variable-phase neighborhoods at arbitrary reference size;
it makes no assertion about added tails or unrestricted complex data.

## 5. Released negative-sign blowup control

Keep F=w^n but CHANGE lambda to -1/n. On the invariant real-amplitude plane
z=exp(i*pi/4)r, w=r, independent of x, both equations reduce to

    r_t=2r^(n+1),
    r(t)=(r0^(-n)-2nt)^(-1/n),
    t_star=r0^(-n)/(2n).                              (13)

For r0>0 this blows up at finite t_star. It is a smooth finite-charge
solution on a circle before t_star. Its signed density (3) and characteristic
current J are identically zero. On the line, choose compact smooth initial
data equal to these constants on [-L,L] with L>t_star. Domain-of-dependence
uniqueness forces the same growing solution in |x|<L-t for as long as the
line solution exists; hence its maximal smooth lifespan is no later than
t_star (an earlier failure outside the cone is not ruled out).

This is an actual finite-energy counterexample to treating J_v=0 alone as
a global-existence criterion for K2048's whole matched family. It changes
the sign of the coupling; it does not falsify positive-coupling completeness.
The positive versus negative distinction comes from the same classified
density rather than a separately fitted norm.

## 6. Evidence, hostile review and retained next questions

The producer symbolically checks the derivative identity, seven finite
polynomial density censuses and eight power balances. A separate sparse
rational coefficient implementation checks those censuses plus a higher-degree
nonpower control; Gaussian-rational jets test (6) and weighted balances.
Exact scalar controls cover the blowup clock, concentration scaling and
higher-power reciprocal/barrier formulas. The universal C2 classification,
all-power theorem, zero-set transfer and compact localization are WRITTEN
proofs; finite controls are not substitutes. Seven planted coefficient faults
are checked only after a clean baseline. No external expert, proof assistant
or novelty certification is claimed.

Hostile checks: arbitrary spatial jets force density separation; reality of
the mixed Wirtinger derivative rules out hidden nonpolynomial densities;
zeros of Fprime are handled by polynomial identity and continuity; the
concentration family is globally regular and does not imply blowup; the
blowup sign is different; scalar repulsion is used only on fixed phase
planes; m=1 and B=0 have separate arguments; finite charge is weighted by
gamma; all support-neighborhood conclusions keep the same support.
No unresolved contradiction was found in these stated scopes. Original
arbitrary-phase large-data continuation remains open and now needs a genuinely
derivative/nonlocal estimate or a different direct construction.

SC-OP-04 ASSERTS a candidate four-field operator, SC-OP-05 is UNCERTAIN about
its rival, SC-META-53 is UNCERTAIN about physical positivity, and SC-META-56
DISAVOWS an odd-action prerequisite. These classical commuting two-field
models do not supply a source dual, fermionic statistics or observed physical
quotient. LT-SM8/LT-GR6b, the physics ledger and canon do not move.

Related literature was checked at the scope level. Zhang and Zhao's
[arXiv:1407.4221](https://arxiv.org/abs/1407.4221) establishes a global result
for a stated cubic Dirac class; its abstract does not establish an all-power
transfer to (1). K2046 retains the more detailed applicability boundary for
Zhang's arXiv:1205.4568. This limited comparison is not a novelty search
certificate or a substitute for the proof above.

Huh and Pelinovsky's [arXiv:1810.10365, equations1.1--1.2 and
Theorem1.1](https://arxiv.org/html/1810.10365v1) concerns a symmetric,
common-phase-invariant real-potential family with the same canonical sign
in both equations. The negative-sign control here lacks its positive-charge
structure; the actual quartic-in-w coupling also fails common-phase covariance.
Thus the explicit control does not contradict that nonexistence theorem.
No general nonlinear-Dirac blowup claim is inferred from either comparison.
