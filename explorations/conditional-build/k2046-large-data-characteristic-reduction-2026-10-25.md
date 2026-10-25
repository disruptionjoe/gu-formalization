---
title: "K2046: Large-data two-sided continuation on the phase-locked sextic planes"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: phase-locked finite-charge data and fixed-support complex neighborhoods; unrestricted complex data and physical source interpretation remain open
scripts:
  - tests/channel-swings/k2046_large_data_characteristic_reduction.py
  - tests/channel-swings/k2046_large_data_characteristic_reduction_probe.py
---

# K2046: Large-data two-sided continuation on the phase-locked sextic planes

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
result: large-data real-plane continuation and complex fixed-support neighborhoods with exact scattering
carrier: two complex eigenlines in K2038 real1408 graph restricted to real phase planes LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Euclidean graph norm and conserved charge ON=declared_graph
real_structure: real commuting fields in fixed complex phase planes
grading: even sextic polynomial; no Grassmann-statistics inference
action_owner: repository-construction -- K2038 action and K2040 sextic
target: global characteristic domain MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Every smooth, bounded phase-locked initial
profile of finite charge, with bounded derivatives, has a unique global smooth
solution in both time directions. No smallness is required. This closes the
backward-domain gap of [K2042](k2042-sextic-transport-instability-2026-10-25.md)
on this class; it does not remove the arbitrary-phase smallness hypothesis of
[K2044](k2044-arbitrary-phase-characteristic-control-2026-10-25.md). The new
argument uses a scalar repulsion at zero reciprocal density, including a
separate treatment of zeros of the initial field.

## 1. Exact object and the unresolved direction

Retain K2044's actual complex two-speed system

    Dplus z = 2i conjugate(z) w^4,
    Dminus w = 2i z^2 conjugate(w)^3,
    Dplus = partial_t+partial_x, Dminus = partial_t-partial_x.

Take CONSTANT phases theta,phi with cos(2theta-4phi)=0 and put
z=exp(i theta) X, w=exp(i phi) Y for real X,Y. Set
sigma=sin(2theta-4phi), which is +1 or -1. The plane is invariant and

    Dplus X = 2 sigma X Y^4,
    Dminus Y = -2 sigma X^2 Y^3.                         (1)

Signs of X,Y may vary in space and zeros are allowed. With a=X^2,b=Y^2,

    Dplus a = 4 sigma a b^2, Dminus b = -4 sigma a b^2,
    partial_t(a+b)+partial_x(a-b)=0.                     (2)

Assume smooth real initial data with all derivatives bounded and
M=integral_R(a0+b0)<infinity. Write A=sup a0, B=sup b0 and
L=sup |b0prime|. B=0 gives free transport and is handled separately.
No periodic profile is declared to have finite line charge. The theorem also
embeds in R x T2 with no transverse dependence and charge per unit area.

For sigma=+1, b<=B forward, and positive current on characteristic triangles
bounds the integral of b along each right-moving ray by M/2. Thus

    a <= A exp(2 M B), b <= B, t>=0.                    (3)

K2042 already proved forward continuation on this plane without finite charge,
with a time-dependent bound. The question here is the opposite transfer sign,
which also controls the previously unresolved backward direction.

## 2. Exact scalar reduction for sigma=-1

Let u=x-t and v=x+t, so Dplus=2 partial_v and
Dminus=-2 partial_u. In the future triangle u<=v,

    a_v = b_u = -2 a b^2.

On any strip where b0(v)>0, uniqueness preserves Y's nonzero sign along its
left-moving characteristic. Therefore c=1/b is well defined and

    c_u = 2a,
    c_uv = -2 c_u/c^2 = partial_u(2/c).

For each fixed v, the quantity c_v-2/c is independent of u. Evaluate it on
the initial diagonal u=v: differentiating c(v,v)=c0(v) gives
c_v(v,v)=c0prime(v)-2a0(v). Hence

    c_v = 2/c + f(v),
    f(v)=c0prime(v)-2rho0(v), rho0=a0+b0.                (4)

The positive singular term 2/c is essential. A supremum estimate on the
original quintic equation discards it and does not prove this theorem.
Integrating c_u from u to v gives the second exact identity

    c(u,v)=c0(v)-2 integral_u^v a(s,v) ds
           >= c0(v)-2M.                               (5)

The last step is the null flux estimate: along the left-moving ray v fixed,
its time integral of a is at most M/2, and du=-2dt. It holds throughout local
existence, before using the desired global conclusion. The conservation law
and finite propagation justify the finite-charge limit using triangles, with
no unproved boundary value of the current at infinity.

## 3. A global barrier that survives zeros

A direct bound on f is inadequate: c0prime=-b0prime/b0^2 can diverge near a
zero of b0. Instead bound it only at a potential first crossing of a positive
barrier. Define

    H=1/(2B),
    K=L(H+2M)^2+2(A+B),
    m=1/(2B+K)>0.                                     (6)

We have m<=H and c0>=1/B>m wherever c0 exists. At any point with c=m,
(5) implies c0<=m+2M<=H+2M. Consequently

    f >= -L c0^2-2(A+B) >= -K,
    c_v >= 2/m-K = 4B+K > 0.                           (7)

For fixed u, follow v forward in any connected interval where b0(v)>0.
If that interval starts at u, its initial value exceeds m. If it starts at
a finite zero v0>u, continuity gives c0(v)->infinity as v decreases to v0,
and (5) gives c(u,v)->infinity as well. Thus a below-barrier value cannot
enter through a zero endpoint. In either case a first downward crossing of
m contradicts (7). An interval with no finite left endpoint necessarily
contains the finite starting point u. This covers every component of the
positive set of b0, even with infinitely many components or accumulating
zeros. On its complement, Y remains identically zero on its own ray.

It follows that throughout every local future solution

    a<=A, b<=1/m=2B+K.                                (8)

This is a uniform-in-time amplitude estimate for sigma=-1. It is not obtained
by assuming a positive lower bound on Y0, and it remains valid for smooth
compact profiles. Finite charge and bounded b0prime, rather than a small
charge or a small squared supremum, are the additional inputs.

## 4. Continuation, reverse time and released scattering

The two characteristic integral equations are locally contractive on a
bounded-amplitude ball. The right sides of(1) are polynomial and locally
Lipschitz. Once the amplitudes obey(3) or(8), spatial differentiation gives a
linear highest-derivative system with bounded coefficients on each finite
time interval; lower derivatives form the forcing. The usual integral
inequality, proved by iterating the linear integral bound, controls the first
derivative and then every higher derivative. Therefore no finite future
endpoint obstructs smooth continuation.

The map Xtilde(t,x)=X(-t,-x), Ytilde(t,x)=Y(-t,-x) exchanges sigma with -sigma.
Its initial A,B,L,M are unchanged. Applying the established future result to
the reflected data proves backward continuation for either plane. Thus both
planes are globally complete for this finite-charge smooth class. Uniform
amplitude bounds do not assert uniform derivative bounds or stability of
K2042's nonzero homogeneous equilibrium.

Local uniqueness preserves the zero sets of each field along its own speed.
If both initial supports lie in [l,r], their transported supports are in
[l+t,r+t] and [l-t,r-t]. For |t|>(r-l)/2 the supports are disjoint and the
nonlinear terms vanish exactly. There are smooth incoming and outgoing free
profiles, with the same total L2 charge. This proves TWO-SIDED exact finite-time
scattering for arbitrarily large compact phase-locked data. Individual charges
can transfer; this is neither identity scattering nor a quantum S-matrix.

Equation(4) also supplies a scalar reconstruction route on strips with
nonzero initial Y: solve the scalar initial-value equation on each fixed-u
ray and use c_u=2a and the transported signs. At zeros use the original
characteristic system and the proved barrier, rather than treating infinity
as an ordinary initial value for an ODE. The argument is an a priori proof;
no numerical solution or infinite-value solver is required.

## 5. Exact obstruction to silently adding arbitrary phases

For general nonzero complex fields define delta=2arg(z)-4arg(w). Then

    a_v=b_u=2ab^2 sin(delta), c_u=-2a sin(delta),
    c_uv-partial_u(-2sin(delta)/c)
        =2cos(delta)(b delta_u-a delta_v).               (9)

The last expression need not vanish. At z=w=1 choose the free jets
z_u=0,w_v=0. The field equations impose z_v=i,w_u=-i. Hence
delta_u=4, delta_v=2; differentiating the w equation gives w_uv=2,
c_uv=-4, whereas partial_u(-2sin(delta)/c)=-8. The defect is exactly4.
These are locally admissible characteristic jets, not independent gradients
inconsistent with the PDE. Therefore(4) is unavailable for arbitrary phases.
This refutes only that proposed shortcut. It proves no blowup and does not
exclude a different phase-sensitive global argument.

## 6. Released successor: open sets of large complex interacting data

The phase-defect obstruction does not force a return to globally small data.
Finite interaction time gives a different route around it. Fix one compact
phase-locked reference solution from sections1--4, with both initial supports
in [l,r]. Let R0 bound both reference complex amplitudes for all time; the
explicit bounds above provide one. Choose an amplitude allowance eta>0 and
a time T>(r-l)/2. Put R=R0+eta. The original complex nonlinearities obey, on
the max-amplitude ball R,

    max(|Fz(z,w)-Fz(zprime,wprime)|,
        |Fw(z,w)-Fw(zprime,wprime)|)
      <= 10 R^4 max(|z-zprime|,|w-wprime|).              (10)

This follows by telescoping powers, using conjugation as an isometry:
the first row has coefficients2(1+4), the second2(2+3). It is a bound on
the actual complex forces, not on the restricted phase plane.

Take any smooth complex initial data supported in THE SAME [l,r], with
bounded derivatives and initial max-norm distance

    epsilon < (eta/2) exp(-10 R^4 T)                    (11)

from the reference. The two characteristic integral equations, in either
time direction, give e(t)<=epsilon exp(10R^4|t|) as long as e<=eta.
On [-T,T] the right side is strictly below eta/2. A first-exit bootstrap
therefore prevents e=eta and proves existence throughout this interval;
amplitude control supplies all smooth derivative continuation as before.
At both ends the component supports have separated. The nonlinearities then
vanish exactly, so the solution continues as free transport for t>=T and
t<=-T. Its global amplitudes remain bounded by R, and it has exact two-sided
finite-time scattering. No bound on the size of the reference charge is used.

This gives open neighborhoods, in the relative uniform topology of smooth
data with fixed compact support, around EVERY compact phase-locked reference.
They contain genuinely variable complex phases, not only constant rotations.
Choosing overlapping reference profiles of arbitrarily large amplitude gives
arbitrarily large interacting complex data in these neighborhoods. The
neighborhood radius may be extremely small as charge or support grows. This
is not a charge-only theorem, not global existence for all complex data, and
not an open-neighborhood statement allowing arbitrary tails or wider support.
Small nonzero tails would invalidate the exact finite-interaction argument.
The test of the phase defect remains useful: it separates a failed exact
integrability shortcut from the successful finite-time perturbation route.

## 7. Validation, source boundary and next question

The producer verifies the reduction, diagonal data, repulsion and phase defect
symbolically. A separate Gaussian-rational implementation differentiates the
original complex forces on ten exact real-plane fixtures, checks three
initial diagonals and three barriers, and constructs the actual complex jet
above. Five changed mathematical coefficients are rejected after a clean
baseline: reciprocal derivative, repulsion sign, initial-density coefficient
and phase-defect coefficient. A fifth fault changes the complex Lipschitz coefficient,
checked against the original force derivative at a maximizing direction. The universal theorem rests on sections2--4,
including the zero-set argument, not these finite fixtures. Inherited graph,
Clifford and action-lift results are pinned K2038/K2042 reuse.

A related reference is [Zhang, arXiv:1205.4568, assumptions A1--A2](https://arxiv.org/pdf/1205.4568).
Its potential depends on the two modulus squares and its additional terms are
cubic with a bilinear-density bound. The present phase-sensitive quintic
forces do not satisfy that stated split. That theorem therefore is not an
automatic large-data result for this system. This limited applicability check
is not an exhaustive prior-art review or a novelty claim.

The strongest overclaim is dropping the phase hypothesis;(9) prevents it.
The strongest contrary case for the barrier is a zero or arbitrarily small
initial Y, covered by(5)--(7). The weakest transfer seam is the factor2 between
null coordinate and physical time; it is carried explicitly in(5). No exterior
specialist, formal proof assistant or novelty certification is claimed.

SC-OP-04 ASSERTS a candidate four-field operator; SC-OP-05 is UNCERTAIN about
its southeast rival. SC-META-53 remains UNCERTAIN about physical positivity;
SC-META-56 DISAVOWS an odd-action prerequisite. These real commuting fields do
not supply source fermionic parity, an independent-dual identification or an
observed physical quotient. LT-SM8/LT-GR6b and canon remain unchanged. The next
substantive test is to control the phase-defect term in one shared PDE domain,
beyond these fixed-support neighborhoods, or construct an actual arbitrary-phase obstruction; genuine transverse
couplings and the source degree-dual/observation bridge remain separate.
