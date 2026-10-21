---
title: "K1915: Sharp short- and long-duration scalar pulse costs"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1915_scalar_pulse_duration_limits.py
  - tests/channel-swings/k1915_scalar_pulse_duration_limits_probe.py
---

# K1915: Sharp short- and long-duration scalar pulse costs

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
result: sharp duration asymptotics with exact endpoint controls and plateau consumers
carrier: fixed massless one-dimensional two-direction characteristic system LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginal pairing ON=finite_moving_tube
real_structure: real scalar potential and fixed real phase lift
grading: propagation directions only, not source chirality
action_owner: repository-construction -- supplied common scalar drive
target: final phase pair (phi,0) and peak control norm MAP-TYPE=intertwiner
```

## 1. Fixed-profile question and complete asymptotic answer

Reuse [K1914](k1914-scalar-control-transport-cuts-2026-10-21.md)'s moving tube,
speed c>0, spatial interval (-L,L), duration T and real phase labels. Fix
phi in C-infinity compactly supported in (-L,L), with integral zero. Set

    F(u)=integral_(-L)^u phi(v)dv, A=||F||_infinity,
    P=||phi||_infinity.

Let M_*(T) be the infimum of ||V||_infinity over smooth pulses compactly
supported in the OPEN tube with exact right phase phi and exact left phase0.
K1914 identifies this with the attained measurable cut optimum; smooth
attainment at equality is not implied. For every T>0,

    max(P/T, 2A/(c T^2)) <= M_*(T)
                         <= 2A/(c T^2)+2P/T.             (1)

For T>L/c there is the additional bound

    M_*(T) <= P/(T-L/c).                                 (2)

Consequently the two sharp limits for this FIXED phase are

    lim_(T->0) T^2 M_*(T)=2A/c,
    lim_(T->infinity) T M_*(T)=P.                         (3)

These are global optimal leading constants, not a sampled-cut conjecture
or optimization only within a pulse ansatz. Finite-T equality, phase-lift
optimization, derivative constraints and joint phase-energy minimization
are separate. The zero phase has M_*=0 and is included.

## 2. Lower bounds: all half-line cuts, not only the central cut

The pointwise row integral immediately gives |phi(u)|<=MT.
For any s in[-L,L] use A_s=[-L,s] in K1914's cut theorem. Put d=2cT.
The minimized crossing capacity is

    C_s=integral min(length(I intersect[z-d,z] intersect(-infinity,s]),
                     length(I intersect[z-d,z] intersect(s,infinity))) dz.

It vanishes outside z in[s,s+d]. Within that interval, the two lengths
are at most d-(z-s) and z-s respectively. Truncation by I can only reduce
each length. Thus for ALL T and s, including cuts near the boundary,

    C_s <= integral_0^d min(d-y,y)dy=d^2/4.

The cut constraint |F(s)|<=M C_s/(2c) implies the second lower bound in(1)
after taking the supremum over s. No assumption d<=L is needed for this
inequality. Equality of the geometric cut area holds when its interaction
window is untruncated; the upper estimate suffices even otherwise.

## 3. Matching short-time construction

Set f=-F/(2c). For any smooth g compact in(0,T) with integral1, the actual
pulse

    V(t,x)=g'(t) f(x-ct)+g(t) phi(x-ct)                   (4)

has the required two exact phases. Along a right characteristic the first
term integrates to zero and the second to phi. Along a left characteristic
x=z-ct, the integrand is d/dt[g(t) f(z-2ct)], because -2c f'=phi.
Endpoint g=0 gives exactly zero left phase. Zero area of phi makes f compact
in the same spatial interval. No approximate endpoint is substituted.

Take the triangular probability density on[0,T], with height2/T and
slopes+/-4/T^2. Shrink its support into(0,T), convolve with a nonnegative
compact smooth probability mollifier within the remaining margin, and retain
integral1. As the shrink tends to zero,

    limsup ||g||_infinity <= 2/T,
    limsup ||g'||_infinity <= 4/T^2.

Convolution does not increase either Lipschitz or sup norm. Equation(4)
therefore proves the upper INFIMUM in(1). Every amplitude strictly above
that upper expression admits a smooth exact endpoint pulse. The triangle
itself is only Lipschitz, so it is not claimed as a smooth minimizer.

The slope constant4 is sharp within nonnegative temporal densities with
zero endpoints: if ||g'||<=K then g(t)<=K min(t,T-t), and integral g=1
forces K>=4/T^2. This alone would prove only ansatz optimality; the independent
cut lower bound is what proves the full short-time assertion(3).

## 4. Matching long-time construction

In (u,z) coordinates the strip contains the common rectangle
I x[L,d-L] whenever d>2L. Choose smooth h compact in(L,d-L), integral1,
with sup norm approaching1/(d-2L), and put

    w(u,z)=phi(u) h(z), V=2c w.

Its row marginal is exactly phi; its column marginal is h times integral
phi=0. Since phi has support strictly inside I, this is a smooth pulse
strictly inside the open strip, hence the open moving tube. It proves(2).
Combine with P/T to prove the second limit(3). This construction uses a
long common-characteristic overlap, unlike the cancellation pulse(4).
It supplies a better upper bound than(1) at large duration.

## 5. Released duration, plateau and energy consumers

If a budget M>0 can realize the fixed profile, necessarily

    T >= max(P/M, sqrt(2A/(cM))).                        (5)

A sufficient condition for exact smooth realization is

    T > [P+sqrt(P^2+2MA/c)]/M,                           (6)

by solving the strict quadratic upper bound in(1). For long pulses the
alternative sufficient condition T>L/c+P/M follows from(2). These are
explicit duration brackets, not a finite-T optimum.

For K1902's symmetric fixed-support energy-minimizing piecewise-linear
profile of contrast theta>0 and plateaux[-b,-a],[a,b],

    P=theta/2, A=theta(L+b-a)/4,
    lim T^2 M_*(T)=theta(L+b-a)/(2c).                    (7)

Here M_* for the nonsmooth profile means the measurable optimum. Formula(4)
still gives a bounded measurable pulse, so the same bracket and limit apply.
The profile is H1, not C-infinity; no exact smooth pulse can have a nonsmooth
marginal. For smooth compact approximating profiles, F and phi converge
uniformly, so A and P converge and the asymptotic constants converge too.
Taking that profile limit is distinct from asserting a smooth minimizer.
For any one fixed smooth profile, the endpoint phase-gradient energy in the
supplied free model stays fixed as T changes: its dependence is on integral
|phi'|^2, while the required DRIVE peak diverges like T^-2. This separates
endpoint excitation from control amplitude; it is no total apparatus-work law.

A reusable exact control is F=(1-u^2)^3 on[-1,1], extended by zero, with
phi=-6u(1-u^2)^2. It has A=1, P=96/(25 sqrt5), integral phi=0 and finite
H1 phase energy. This compact polynomial is not C-infinity; it checks the
finite algebra/measurable statements and is not used to certify smoothness.

## 6. Released phase-optimized short-time plateau theorem

Let 0<a<b<L and prescribe constant phase values alpha on[-b,-a] and
beta on[a,b], with alpha-beta=theta>0. Allow the common phase and all
transitions to vary, but retain smooth compact phi, zero area and left
phase0. No gradient-energy or derivative bound is imposed. Define the
infimum peak control over this entire class as M_plateau(T), and ell=b-a.
Then the EXACT optimized short-time constant is

    lim_(T->0) T^2 M_plateau(T)=theta*ell/(2c).           (8)

Proof of the lower bound: on each plateau F changes by alpha ell or beta ell.
Since F lies between -A and A, 2A>=ell max(|alpha|,|beta|)>=ell theta/2.
Equation(1) gives M>=theta ell/(2c T^2), uniformly over all profiles,
even T-dependent choices. Pointwise amplitudes also give M>=theta/(2T).

For the upper bound choose alpha=theta/2, beta=-theta/2. For any epsilon>0
small enough to fit in the three transition gaps, construct an even continuous
piecewise-linear primitive F_e as follows: it rises with slope theta/2 over
[-b-epsilon,-a+epsilon], is constant on[-a+epsilon,a-epsilon], falls with
slope-theta/2 over[a-epsilon,b+epsilon], and connects linearly to zero in
the two outer gaps, becoming zero strictly before +/-L. Center the plateau
rise between -A_e and A_e, where

    A_e=theta*(ell+2epsilon)/4.

The connector slopes have no bound; the entire primitive stays in[-A_e,A_e].
Convolve with an even nonnegative smooth probability kernel of radius less
than epsilon and the outer support margin. F becomes smooth compact and
retains exactly the two desired slopes on the original plateaux. Its derivative
phi has zero integral, and ||F||<=A_e. For each fixed epsilon this profile has
finite P, so(3) implies limsup T^2 M_plateau(T)<=2A_e/c. Let epsilon->0.
Together with the uniform lower bound this proves(8). It does not exchange
an uncontrolled limit or assume a common bound on profile derivatives.

At the limiting primitive bound A=theta ell/4 a smooth profile cannot attain
it. Equality forces alpha=-beta=theta/2 and the rising plateau endpoints
to be -A and A, but positive derivative at its right endpoint forces F>A
immediately afterward. Thus the optimal primitive value is an infimum.
This statement does not rule out a finite-T optimizer at a larger cost.

The K1902 energy-minimizing profile has short-time coefficient
 theta*(L+ell)/(2c), larger than(8) by factor(L+ell)/ell. Therefore the
energy optimum is not the peak-drive asymptotic optimum. The construction
uses compensating phase outside the plateaux; it is an allowed repair when
only contrast and support are fixed. Gradient energy of an infimizing family
is not uniformly controlled: if it were, one-dimensional H1 compactness and
the fixed plateau data would give a continuous limiting phi attaining the
impossible primitive minimum. A joint energy budget must price this loss.
This identifies a real incompatibility of the two optima without claiming
the full amplitude-energy Pareto frontier.

## 7. Released quantitative finite-energy obstruction

The loss of gradient energy above can be quantified without a mesh. Keep
CENTERED plateau values +/-h with h=theta/2, let E=int |phi'|^2, and write
A=h ell/2+epsilon. For any smooth admissible profile epsilon>0, and

    E >= 16 h^3/(9 epsilon)=2 theta^3/(9 epsilon).        (9)

Proof: on a transition from value0 to h (or h to0), stop at the nearest
zero so phi has one sign. Let B be its unsigned phase area and E_i its
gradient energy. Integrating the derivative of |phi|^(3/2) and applying
Cauchy-Schwarz gives

    h^(3/2) <= (3/2) sqrt(B E_i), E_i B>=4h^3/9.

For the positive plateau, the areas B1 and B2 in the adjoining positive
transitions sum to at most2A-h ell=2epsilon: they consume the primitive
headroom before and after the plateau's fixed rise. Thus
E1+E2>= (4h^3/9)(1/B1+1/B2)>=8h^3/(9epsilon).
Apply the same argument to the negative plateau. The four nearest-zero
transition interiors are disjoint, so their energies can be added to obtain(9).
The bound does not assume monotone transitions; the signed derivative identity
and Cauchy-Schwarz already permit reversals. Zero transition area cannot
connect the nonzero continuous endpoint and is handled by the infinite bound.

Each individual transition constant4/9 is sharp: phi(t)=h(1-t/tau)^2
has area h tau/3 and energy4h^2/(3tau). Global simultaneous attainment must
also satisfy the spatial gaps, primitive alignment and boundary connectors;
(9) is not asserted to be the full joint optimum.

For a finite budget E<=E0 in this centered class, necessarily

    A >= theta ell/4+2theta^3/(9E0),
    M >= theta ell/(2cT^2)+4theta^3/(9cE0 T^2).          (10)

This is a concrete amplitude-energy obstruction beyond the phase-only
optimum. Noncentered plateau values require their separate h1/h2 bookkeeping;
no symmetric coefficient is silently transferred to that larger class.

## 8. Hostile review and evidence

Strongest overclaim: a finite-T all-cut formula evaluated for every profile,
a joint energy optimum or attained smooth threshold. None follows from(3).
Strongest contrary case: nonzero total phase is impossible with left phase0;
changing phi with T can invalidate the fixed-profile limits. Sharp pulses
may have nonsmooth g, while smooth strict-budget approximants preserve both
endpoints exactly. Weakest seams: factor2c, truncated half-cut capacity and
the sign in the opposite-characteristic derivative. Exact probes independently
integrate a nontrivial polynomial pulse and cut capacities, with actual sign
and coefficient faults. Universal limits rest on(1)-(2), not finite samples.
The constructions specialize the previously recorded transport and control
arguments; no claim of new optimal-control theory or expert acceptance.


## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN
about indefinite spectra. None selects the positive Hilbert pairing, bath,
scalar drive, observable algebra or physical units here. LT-SM8, LT-GR6b
and AC-F1 remain unchanged. Full20 injection, separate K/C, physical domain
and accessible-algebra identification remain independent construction debts.
No source-register, physics-ledger or canon verdict changes. No GU prediction,
novelty, external expert acceptance or formal proof is claimed. Analytic
arguments carry general scope; exact finite probes test the actual algebra
and countercontrols. Report and dependency-pin checks establish only
consistency and provenance, separately from mathematical-input faults.
