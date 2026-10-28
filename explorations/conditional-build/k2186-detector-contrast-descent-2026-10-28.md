---
title: "K2186 Outcome-noise obstruction to detector energy descent"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2186_detector_contrast_descent_probe.py
---

# K2186 Outcome-noise obstruction to detector energy descent

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
result: K2186 exact noise counterexample and failure of radial quasiconvexity
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

Fair binary outcome noise can strictly increase the optimized vacuum output
field energy while strictly decreasing positive contrast. An explicit
infinite-occupation profile has derivative greater than 1/64 along this noise
path and an exact finite noisy successor with larger energy. The same path
ends at the uninformative fair detector of energy zero. Consequently the
profile energy is not quasiconvex on that segment and its sublevel sets need
not be star-shaped about the fair detector.

More generally, no fixed constant-output replacement probability beta in
[0,1] gives a universal energy-nonincreasing contraction of absolute contrast.
This excludes a family of proposed global monotonicity proof methods. It
does not disprove monotonicity of the optimized exact-contrast frontier F,
threshold saturation F=V, or uniqueness of its optimizers. The constructed
profiles are not claimed optimal. Adaptive profile-dependent noise and
minimizer-specific descent remain distinct possibilities.

This is GU-independent mathematics of the supplied positive free scalar Fock
binary diagonal square-root instrument with one real squeeze per reported
outcome. The cost is vacuum output FIELD energy, not apparatus, clock,
preparation, switching, reset or total work. SC-META-53 remains UNCERTAIN;
ledger0.263, LT-SM8/LT-GR6b, canon and physical quotient do not change.
K2162/K2166 already own the weak-contrast coefficient353/170 and its uniform
asymptotics; K2168 already owns the lower moment envelope. Those are reused,
not rediscovered. K2182's endpoint theorem and K2176's numerical bracket are
also unchanged. No novelty or external certification is asserted.

## Instrument and directional derivative

Use the exact model of [K2184](k2184-global-detector-structure-2026-10-28.md):

    p_n=(3/4)4^-n, q_n=3n-1, 0<=x_n<=p_n, y=p-x,
    R(x)=sum(n+1/2)x_n, T(x)=sum(n+1)sqrt(x_n x_(n+1)),
    C=40/3, A(s)=41s^2/6+3/(2s^2),
    g(x)=min_s [R(x)A(s)-CsT(x)], H(x)=g(x)+g(y)+35/18.

Every nonzero branch has a unique minimizing squeeze in S=[2/3,113/100].
Write it s_x; it solves A'(s_x)=C T(x)/R(x). Define

    Ep(s)=(5/6)A(s)-(2C/3)s+35/18.

This is the energy of the geometric profile p at a fixed squeeze.
Ep''=(5/6)A''>0, Ep'(1)=0 and Ep(1)=0. Hence Ep>=0,
and it is strictly decreasing below1.

For a positive profile z let D(z)=DT(z)[p]. If
r_n=sqrt(z_(n+1)/z_n), direct differentiation gives

    D(z)=1/2 sum(n+1)p_n [r_n+1/(4r_n)].             (1)

The profiles below have a positive geometric tail, so the derivative sum is
absolutely convergent. Their noise paths reduce to explicit finite formulas
plus an exact geometric tail; differentiability is not inferred from a
formal exchange at a zero coordinate.

For fixed beta in[0,1], let

    z_t=(1-t)z+t beta p, y_t=(1-t)y+t(1-beta)p.

It is capped and d(z_t)=(1-t)d(z), since sum q_n p_n=0. Positive homogeneity
of g and the envelope derivative yield

    H'(0)=beta Ep(s_z)+(1-beta)Ep(s_y)
       -C[beta s_z(D(z)-2/3)+(1-beta)s_y(D(y)-2/3)]-H(z).  (2)

This describes recomputing the allowed square-root Kraus operators and
optimizing one squeeze per new binary outcome. It is not free relabeling of
an already completed feedback process; that latter operation retains hidden
conditional operations and can belong to a larger instrument class.

## Exact softened-tail counterexample

Choose integer N>=1, r=2^-N, L=r^2/(1+r^2), U=1/(1+r^2), and set

    z_n=L p_n (n<=N), z_n=U p_n (n>N).

Its complement exchanges L and U. Every coordinate of both branches is
positive. Define the geometric tail and interface quantities

    tau=4^-(N+1), e=(N+1)p_N/2,
    Rt=tau(N+11/6), Tt=tau(N/2+7/6).

Here Tt includes all edges n>=N+1. The exact moments are

    Rz=L(5/6-Rt)+U Rt,
    Tz=L(2/3-e-Tt)+[r/(1+r^2)]e+U Tt,
    Ry=5/6-Rz,
    Ty=U(2/3-e-Tt)+[r/(1+r^2)]e+L Tt,
    d(z)=(U-L)3(N+1)tau>0.

Only the interface ratio differs from1/2, so (1) gives the same derivative
for both branches:

    D(z)=D(y)=2/3+delta, delta=e(r+r^-1-2)/2.        (3)

At common squeezes1 the sole coherence loss is the interface. Optimization
can only lower that value, so

    H(z)<=Hu=C e(1-r)^2/(1+r^2).                    (4)

For N=10, all of the following are rational:

    L=1/1048577, U=1048576/1048577,
    Rz=95420345/26388304232448,
    Tz=6959471/3298538029056,
    d(z)=34602975/4398050705408,
    D(z)=34463344739/51539607552,
    Hu=57559095/1099512676352.

Further,

    A'(9/10)-C Tz/Rz=18784071701/46374287670>0,
    Ep(9/10)=649/6480.

Thus s_z<9/10 and Ep(s_z)>Ep(9/10). In the fair case beta=1/2,
use Ep(s_y)>=0, both squeezes<=113/100 and (4) in (2):

    H'(0)>Ep(9/10)/2-(226/15)delta-Hu
          =72000341772103349/3647919177093611520
          >1/64.                                  (5)

No floating-point optimization is needed for (5). The strict lower bound
comes from exact moment identities and monotonicity of A'. The independent
probe also brackets the actual optimizing squeezes with rational arithmetic,
proving H(z)>1/20000 and evaluating a concrete finite noise step t=10^-8.
That step has smaller positive contrast and strictly larger optimized energy.

At t=1, z_t=p/2 and H=0. Since H(z)>0 and H'(0)>0, sufficiently small
positive t has H(z_t)>max(H(z),H(p/2)). This disproves quasiconvexity on this
line. The sublevel set at H(z) contains z and p/2 but not the entire segment,
so it is not star-shaped about p/2. K2184's fixed-contrast nonconvexity did
not itself imply this stronger radial obstruction.

## Every fixed neutral replacement has a counterexample

For the same sequence as N tends to infinity,

    Rz ~ N4^-N/4, Tz ~ N4^-N/8, Tz/Rz ->1/2,
    Ry ->5/6, Ty ->2/3, delta=O(N2^-N), H(z)->0.

The last convergence follows directly from the moments and continuity of g;
no unproved lower bound is needed. Let a be the unique positive solution
A'(a)=C/2. Since A'(1)=32/3>C/2, a<1 and Ep(a)>0.
The minimizing squeezes therefore satisfy s_z->a and s_y->1. Equation(2)
now gives, for each fixed beta>0,

    lim H'_beta(0)=beta Ep(a)>0.

Hence every such fixed replacement probability fails universal energy
monotonicity on some positive-contrast softened-tail profile. For beta=0,
use the complementary profile and outcome-exchange symmetry: replacement
by0 there is replacement by1 for z, with the same energy and decreasing
absolute contrast. This last case has negative signed contrast; it does not
claim the beta=0 counterexample also has positive signed contrast.

The quantifiers are: for each fixed beta there exists a counterprofile.
There is no claim of one profile defeating all beta, and no exclusion of an
adaptive beta chosen from the full profile. In particular this result does
not determine behavior at energy-minimizing profiles on a contrast slice.

## Verification and next question

The executable proof sums both geometric tails independently, checks (1)--(5),
and encloses the actual full-tail optimized energies before and after the
finite fair-noise step. Genuine faults change the tail offset, interface,
contrast weights, optimization stationarity or noise derivative coefficient;
a clean baseline precedes every fault. Universal asymptotics and quantifier
scope are written proofs, not conclusions drawn from finite samples.
Independent internal review must inspect the positive-tail condition and the
fixed-instrument versus hidden-label distinction.

The failed route has useful consequences: neither generic profile convexity,
radial quasiconvexity, nor a fixed classical-neutral-noise contraction can
prove the global exact frontier theorem. Remaining useful routes are an
adaptive or minimizer-specific descent, a rigorous global nonconvex solver,
or a physically complete controller with a new cost model. The weak-contrast
and near-maximal-contrast results remain constraints on any proposed global
answer. None of the present profiles changes the certified minimum at
contrast1/2 or supplies missing apparatus accounting.
