---
title: "K2164 Feedback changes the saturation tie"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: binary diagonal scalar-mode instruments with one real squeeze per reported outcome; vacuum field energy
scripts:
  - tests/channel-swings/k2164_feedback_saturation_tie_probe.py
---

# K2164 Feedback changes the saturation tie

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
result: K2164 exact saturation-tie counterexample, global energy enclosure and compact-smear existence transfer
carrier: positive scalar Fock vacuum and photon-added signal for a fixed oscillator, with finite spectral fixture LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and vacuum output field energy ON=declared_carrier
real_structure: real mode, positive diagonal Kraus and deterministic real squeeze per reported outcome
grading: oscillator occupation, not source chirality or global particle parity
action_owner: repository-construction: supplied positive free Hamiltonian and instrument class
target: minimum vacuum output energy attaining maximal detection contrast MAP-TYPE=intertwiner
```

## Result and scope

K2156's half-tie minimizes the diagonal nondemolition saturation cost. It cannot be imported
into [K2162](k2162-feedback-detector-frontier-2026-10-27.md)'s outcome-feedback class.
Here an exactly realizable positive two-frequency model has strictly positive derivative
at half-tie, and an explicit different tie costs less than EVERY optimized half-tie detector.
A rational branch-and-bound certificate encloses the GLOBAL saturation energy, rather than
only a stationary point. A separate continuity construction transfers strict failure of
half-tie to some genuine real smooth compact smears in the massive continuum model; it gives
no explicit support size or quantitative approximation rate.

All effects are binary diagonal in the named local oscillator, with one real squeeze per
REPORTED outcome and positive square-root Kraus. K2160 establishes their optimality over
hidden diagonal Kraus at fixed effects in this class. Changing the tie preserves maximal
contrast, but changes the separate false-positive and true-positive probabilities. Squeezing
at a fixed tie preserves both. Vacuum output field energy is neither signal-averaged cost
nor preparation, stable apparatus, switching or reset work. This imported positive model
settles no GU positivity or physical quotient: SC-META-53 remains UNCERTAIN; LT-SM8/GR6b,
source, ledger and canon are unchanged.

## 1. Exact derivative and global endpoint structure

Use K2160 constants nu,N,z=N/(N+1), C=2 sqrt(N(N+1)) E_sum and
A(x)=m2 x²/(2nu)+nu/(2x²). At integer N=ell>=1, all maximal-contrast effects are
0 for n<ell, tie e_ell=t, and1 for n>ell. Let

    p=(1-z)z^ell, P=p(ell+1/2), tau=p sqrt(ell(ell+1)),
    R1=R1(0)+Pt, R0=Rbar-R1,
    T1=T1(0)+tau sqrt(t), T0=T0(1)+tau sqrt(1-t).

The sum of complement terms d_r is constant across every complete instrument. Each branch
R_r A(x)-C T_r x+d_r is strictly convex and coercive in x>0; R_r>0 even at endpoints.
Write its unique minimizer x_r(t), and let J(t) be the sum of optimized branch energies.
On (0,1), implicit differentiation/envelope differentiation gives

    J'(t)=P[A(x1)-A(x0)]
           -(C tau/2)[x1/sqrt(t)-x0/sqrt(1-t)].                 (1)

Uniform compact positive squeeze bounds imply J' tends to minus infinity at0+ and plus
infinity at1-. Thus every global saturation minimizer is interior. At half-tie,

    J'(1/2)=P[A(x1)-A(x0)]-(C tau/sqrt2)(x1-x0).               (2)

Equal adjacent edge weights do not force equal conditional moments or equal x_r.
Fixed-squeeze strict convexity in t does not prove optimized J convex or uniquely minimized.
We make neither claim, nor any universal direction of the optimal shift.

## 2. A realizable two-frequency counterexample

Take W=diag(3-2sqrt2,3+2sqrt2), f=(1,1)/sqrt2. Both frequencies are strictly positive.
The actual moments are m1=m_-1=3, m2=17, so nu=1,N=1,z=1/2, E_h=E_j=3,
C=12sqrt2. These data are not arbitrary independent moments. They define an exact two-mode
positive Fock model. They are not themselves a spatially compact continuum smear.
For this model A(x)=(17x²+x^-2)/2, and the COMPLETE energy is

    E(t,x0,x1)=[(5-3t)/8]A(x0)+[(7+3t)/8]A(x1)
               -6sqrt(1-t)x0-(12+6sqrt(t))x1+21/2.           (3)

At t=1/2 the unique roots satisfy

    17x0-x0^-3=48sqrt2/7,
    17x1-x1^-3=(192+48sqrt2)/17.

Since h(x)=17x-x^-3 is strictly increasing, exact rational sqrt2 bounds prove
.724<x0<.726 and .964<x1<.966. Factoring(2),

    J'(1/2)=(x1-x0){(3/16)(x1+x0)[17-1/(x0²x1²)]-3sqrt2}.

Rational interval substitution gives 11/100<J'(1/2)<13/100. Half-tie is not stationary.
The concrete detector t=49/100,x0=3627/5000,x1=4827/5000 has

    E=(353/800)A(x0)+(847/800)A(x1)
       -(3sqrt51/5)x0-(81/5)x1+21/2 <3.1006.

Convex tangent lower bounds at the half-tie branch roots prove J(1/2)>3.1013.
This finite strict comparison needs no floating numerical optimizer. Both ties achieve
maximal contrast1/2 and equal-prior error1/4, but half-tie has (alpha,eta)=(3/8,7/8),
while the new witness has (149/400,349/400). The ROC point is NOT unchanged.

## 3. Rigorous global saturation certificate

The companion script covers the entire t interval[0,1] by rational intervals and uses only
Fraction arithmetic and integer square-root bounds. For [a,b], lower-bound the branch
energies separately by using

    R0_min=(5-3b)/8, k0_max=6sqrt(1-a),
    R1_min=(7+3a)/8, k1_max=12+6sqrt(b).

Here k=C T, and each sqrt is replaced by a rational UPPER enclosure. Because A(x)>0 and
x>0, min_x[Rmin A(x)-kmax x] is a valid lower bound over every t in[a,b]. Separate branch
extrema need not be attained at the same t; that weakens the bound but preserves it.
Each convex minimum is bracketed by its monotone derivative on[1/4,2]. This interval
works uniformly: R0>=1/4,k0<=6, R1>=7/8,k1<=18; h(1/4)<0 and h(2)=271/8>24. Outward rational square-root rounding adds at most
6e-18 to k, far below this bracket margin; the code checks the actual rounded bracket.
A tangent line evaluated over the root bracket gives an exact lower bound. Feasible upper
bounds use actual rational t,x0,x1 and LOWER sqrt enclosures in the negative terms.

Start with [0,1], bisect the interval having the smallest lower bound, and keep the best
feasible upper bound. Prune only when the interval lower bound exceeds that upper bound.
Previous prunings remain valid when the upper bound decreases. Thus the heap minimum and
best witness bound the global J minimum, with no stationary-point or uniqueness assumption.
The deterministic report records the resulting rational energy interval, actual witness,
subdivision count and tolerance1e-6. The actual run uses15031 subdivisions and proves
3.1003864 < min J < 3.1003875; its stored rational endpoints have width below1e-6. It is reproducible from the probe; finite samples do
not substitute for interval coverage. Continuity ensures interval refinement converges when square-root precision and root
bisection depth also increase as needed. The present certificate fixes18 digits and42
root bisections for its stated1e-6 tolerance; arbitrary finer tolerances require revisiting
those settings. No full general K2162 squeeze/effect grid is being claimed.

## 4. Compact continuum smears also have counterexamples

This is an existence transfer, separate from the finite certificate. Fix a massive one-dimensional
free scalar dispersion omega(k)=sqrt(m²+k²), m>0. Choose lambda>m/(3-2sqrt2), set
omega_-=lambda(3-2sqrt2), k_-=sqrt(omega_-²-m²), and let omega_+(r)=r omega_-,
k_+(r)=sqrt(omega_+(r)²-m²). Choose any nonzero real chi in C_c^infinity and normalize

    f_(L,r)(x)=chi(x/L)[cos(k_- x)+cos(k_+(r)x)].

For r near r0=17+12sqrt2 and L tending to infinity, its Fourier transform has four
separated peaks. Smooth compact chi has rapidly decreasing Fourier transform. Peak
concentration, vanishing cross terms and dominated tail estimates yield, uniformly on a
small closed r neighborhood, m_j(L,r) tending to
[omega_-^j+omega_+(r)^j]/2 for j=-1,1,2. The negative moment is bounded because m>0;
the positive moments require the Schwartz tail bound. This does not assert exact finite-L
spectral support.

The limiting m1 m_-1=(r+1)²/(4r) equals9 at r0 and is strictly increasing near r0.
Continuity in r and uniform convergence give r_L tending to r0 with EXACT m1 m_-1=9 for
sufficiently large L: values on opposite sides bracket9, and any chosen zeros converge
to the unique limiting zero after restricting the neighborhood. Thus N=1 exactly.
The tuple tends to the finite model scaled by lambda: (m1,m_-1,m2) tends to
(3lambda,3/lambda,17lambda²). Strict branch convexity makes x_r and derivative(2)
continuous in these moments. Its limiting positive derivative is lambda times the finite
one. Hence genuine real smooth compact smears with N=1 also have J'(1/2)>0. The strict
finite witness gap persists by continuity as well. Support radius grows with L; neither
an explicit finite L nor a fixed-region performance guarantee is supplied. This avoids
silently identifying a finite spectral toy with a localized field.

## Evidence and next work

Exact checks cover realized moments, geometric threshold sums, derivative brackets, changed
ROC, actual energy comparison, rational outward bounds and interval lower controls. Real
altered frequencies, branch moments, effects, derivatives and feedback inputs must fail after
a green baseline. The global branch-and-bound enclosure is rigorous arithmetic. General
interior-minimizer, envelope and compact-smear convergence arguments rely on the written
proof and independent specialist review, not finite sampling.

K2156 half-tie remains correct for its unsqueezed operation class. K2162's general integer-tie
variational statement is now consumed by a globally certified concrete example and an
existence transfer; arbitrary ell/moment optima remain unsolved. The sharp global weak-budget
asymptote still needs uniform rare-branch and occupation-tail control. A stable autonomous
controller with preparation/reset changes the resource problem and remains open. No
proof-assistant, external-expert, novelty or GU recovery claim is made.
