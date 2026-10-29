---
title: "K2225 Positive additive detector controls with physical drift retained"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite-chain energy-constrained instrument approximation; no continuum optimizer, autonomous apparatus or GU realization
scripts:
  - tests/channel-swings/k2225_positive_drift_detector_control_probe.py
---

# K2225 Positive additive detector controls with physical drift retained

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
result: K2225 positive additive finite-chain detector control theorem
carrier: finite M oscillator sites with full infinite Fock space and one record qubit LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and physical free-energy form ON=declared_carrier
real_structure: real canonical q,p and complex Hilbert adjoint
grading: site occupation and binary record; not spinor grading
action_owner: repository-construction -- supplied local time-dependent controls
target: complete recorded channel with arbitrary reference MAP-TYPE=intertwiner
```

## Result, target and unchanged physical drift

For the finite oscillator model of [K2154](k2154-uncompensated-detector-control-2026-10-27.md),
any prescribed real mode f, bounded diagonal effect 0<=e(n_f)<=1, and finite
positive outcome squeezes s0,s1 have a complete recorded implementation whose
energy-constrained error tends to zero with increasing control speed. Every
ADDITIVE control is positive, hence every active total Hamiltonian H_W+K is
semibounded. H_W is retained throughout. The controls act on adjacent sites or
on site1 and the record. If W² is dense, the free dynamics is not spatially
local; local total dynamics additionally requires finite-range W².

This removes K2154's possible unstable beam plateaus and adds outcome squeezing;
it removes K2223's replacement of the entire free drift, on this FINITE-CHAIN
model. It does not implement the continuum K2219 optimizer, prove convergence
of its energy, or supply an autonomous clock, easy spectral control or free
reset. The mode, frequency scale, pure record and switching schedule are
explicitly supplied. No physical GU claim follows (SC-META-53 stays UNCERTAIN).

## 1. Same target instrument from positive ideal pulses

Use M>=1, real W=W^t>0, nu>0 and the K2154 notation

    H_W=(p^t p+q^t W²q)/2-Z>=0, Z=tr(W)/2,
    c_j=(sqrt(nu)q_j+i p_j/sqrt(nu))/sqrt(2), G=N_nu+M/2,
    C=max(1/nu,nu/w_min²), D=max(nu,w_max²/nu),
    G<=C(H_W+Z), H_W+Z<=DG, kappa=||nu I-W²/nu||.

A real unit vector f defines b_f=sum f_j c_j. The existing adjacent real
Givens gather B sends this mode to site1. For any required signed beam angle
write J=+/- i(c_j^*c_k-c_k^*c_j), N_jk=n_j+n_k. The one-particle J has
spectrum {-1,1}; thus 0<=N_jk+J<=2N_jk on full Fock space. For
0<=theta<2pi, use positive plateaus N_jk+J for duration theta and N_jk
for duration 2pi-theta. Since [J,N_jk]=0 and N_jk is integer-valued,

    exp(-i(2pi-theta)N_jk) exp(-i theta(N_jk+J))=exp(-i theta J).

Zero-angle gates can be omitted. This includes the inverse gather using the
opposite sign J. No occupation cutoff or negative number pulse is used.
The original real gather needs at most M-1 adjacent gates in each direction.

At site1 use H_m=arcsin(sqrt(e(n1))) tensor sigma_y+(pi/2)I for duration1.
It lies between0 and pi and produces the positive-root instrument, up to a
common phase. Keep the record coherent. In outcome r, apply
h_(s_r)/s_r=(P1²/s_r+s_r Q1²)/2 for duration pi/2, then h1 for duration
3pi/2, with Q1=sqrt(nu)q1 and P1=p1/sqrt(nu). These are positive oscillator
Hamiltonians. In chronological order the Heisenberg product is

    [[0,1],[-1,0]]³ [[0,1/s_r],[-s_r,0]]=diag(s_r,1/s_r).

Ungather and read the record. The ideal recorded Kraus maps are precisely
S_r sqrt(e_r(n_f)), e1=e, e0=1-e, where S_r squeezes b_f and leaves its
orthogonal modes unchanged. Outcome-dependent metaplectic phases disappear
after record pinching. The equality holds with arbitrary reference systems.

Let K_l be these unscaled positive plateaus, duration d_l. Use Lambda K_l
for duration d_l/Lambda. Then T=T0/Lambda, with

    T0<=4pi(M-1)+1+2pi.

Physical evolution uses H_W+Lambda K_l; ideal evolution uses Lambda K_l.
This comparison does not cancel or transform away H_W in the actual model.

## 2. Number growth and complete-record error

All ideal plateaus except the first conditional squeeze commute with G.
For that squeeze, direct quadratic commutation gives

    -mu G <= i[K_l,G] <= mu G,
    mu=max_r |s_r-1/s_r|.

The integrated ideal growth rate is at most gamma=(pi/2)mu. Put L=exp(gamma).
The free commutator has the K2154 bound +/-kappa G. Therefore at every time

    <G>_ideal,t<=L<G>_0,
    <G>_actual,t<=exp(kappa t)L<G>_0,
    <H_W>_actual,t<=D exp(kappa t)L C(E+Z)-Z

for marginal initial mean H_W energy at most E. These estimates hold with
record and reference entanglement; each conditional squeeze is a finite direct
sum of positive forms. They are not bounds on an arbitrarily rare outcome.

Purify the input and use the same initial record. The common controls cancel
in the derivative of the ideal/actual overlap. Positivity of H_W gives

    |d<psi_ideal,psi_actual>/dt|
      <=sqrt(<H_W>_ideal <H_W>_actual)
      <=D L exp(kappa t/2)<G>_0.

Consequently the half trace-norm error of the COMPLETE recorded output,
including any reference, is at most

    delta(E,Lambda)=min(1,sqrt(2DLC(E+Z) I(T))),
    I(T)=2(expm1(kappa T/2))/kappa if kappa>0, and T otherwise.

At fixed M,W,nu,f,s0,s1 and E it tends to zero as Lambda tends to infinity.
No energy-variance assumption occurs. Trace-norm convergence alone does NOT
imply convergence of unbounded energy expectations to the ideal energy;
only the displayed actual-energy upper bound is proved.

## 3. Operator and form-domain justification

Each plateau is a positive finite-mode real quadratic form, with a bounded
number-diagonal field/record term where needed. Finite-particle vectors are
analytic vectors for its quadratic part: it changes number by at most2 with
norm bounded by a(n+b) on number<=n sectors. Bounded measurement preserves
those sectors. Thus each segment has a unique self-adjoint closure and its
closure is positive. Record projectors commute with field operators and give
finite direct sums. Positivity of total H_W+Lambda K_l survives closure;
we do not assert equality of all operator domains. Each actual plateau has
a form norm equivalent to G, since G/C<=H_W+Z and
H_W+Lambda K_l+Z<=(D+Lambda a_l)G. Spectral conservation therefore
preserves the common G form domain on that plateau.

For estimates take total-number cutoffs P_N. They commute with G, but NOT
with squeezing. The correct identity is

    [G,P_N K_l P_N]=P_N[G,K_l]P_N.

It preserves the two-sided growth estimate. Compressed H_W remains positive
and <=DG. Finite-dimensional Gronwall and overlap inequalities follow,
including both actual and ideal squeezed evolutions. The compressed operators
converge on the common finite-particle core, hence strongly in resolvent and
unitary sense to the self-adjoint closures. Pass finite segment products and
overlap bounds by strong convergence and number bounds by lower
semicontinuity. Approximate arbitrary finite-mean-energy inputs in G form
norm; the free-energy/number inequalities make this approximation valid.
This is proof approximation, not a physical truncation.

## 4. Work and reusable reset composition

At a sudden control change define mean work as <Delta K>. All controls are
zero before and after the schedule. Conservation on each constant plateau
and the unchanged state at a switch yield

    W_signed=<H_W>_out-<H_W>_in.

Choose 0<=K_l<=a_l G: valid coefficients are2 for each shifted beam,1 for
each phase repair,2pi/M for measurement,max_r(s_r,1/s_r) for first squeeze,
and1 for final rotation. Let A=sum_l a_l, counting all gather/ungather
plateaus. Each plateau appears at most twice in the triangle inequality, so

    sum_switches |<Delta K>|<=2 Lambda A exp(kappa T)L C(E+Z).

Form-norm approximation justifies conservation and switching expectations
for finite-mean-G states. This is an upper bound on absolute MEAN exchanges,
not stochastic absolute work, a necessary optimum, clock expense, or reservoir
renewal. Increasing Lambda makes the sufficient error bound smaller while
this work bound grows. Instantaneous control remains an external resource.

A fresh thermal-register reset with uniform half-diamond error epsilon from
[K2226](k2226-thermal-register-reset-2026-10-28.md) can replace the supplied
pure-bit reset after the instrument. Channel contractivity and a telescoping
comparison give error at most delta+epsilon for one instrument/reset cycle,
or sum_j(delta_j+epsilon_j) for k cycles. This applies to the retained quantum
systems and reset record; an already copied classical outcome is not erased.
The j-th energy-constrained delta_j needs a uniform energy bound for the
corresponding ideal input at that comparison. The displayed energy recursion
provides one for finite schedules. Do not multiply a fixed first-cycle energy
budget by k without checking later inputs. Fresh bath registers are consumed;
this is not a cyclic finite reservoir.

## 5. A concrete joint error and resource consumer

Take M=2, nu=1, W²=[[2,-1],[-1,2]], f=(1,1)/sqrt(2),
e(n)=n/(n+1), s0=2/3, s1=7/5 and the free vacuum E=0.
Then C=1,D=3,kappa=2,Z=(1+sqrt(3))/2<3/2, mu=5/6,
L=exp(5pi/12)<4, A<12 and T0<=6pi+1<20. At Lambda=10^12,
T<2*10^-11. Using I(T)<=T exp(T)<2T proves

    delta²<1440/10^12 < (1/25000)²,
    delta<0.00004.

With a fresh101-cell bath at p=1/4, the uniform reset error is below
0.000000032581, so the complete instrument-plus-reset error is below
0.000040032581, including arbitrary reference correlations. Actual mean
free field energy stays below36 in these dimensionless units. The conservative
absolute mean switching-work bound is below2.88*10^14, before any bath reset
work, clock or renewal cost. This is a sufficient existence certificate with
large supplied strength, not an efficient or optimal implementation.

The bounds are rational: pi<22/7 follows from the positive integral
integral_0^1 x^4(1-x)^4/(1+x²) dx=22/7-pi. For 0<=x<3,
exp(x)<=1+x+x²/[2(1-x/3)] by k!>=2*3^(k-2) for k>=2;
at x=55/42 this is below4. The remaining exponentials use exp(x)<=1/(1-x)
for 0<=x<1. The reset number is freshly computed from its exact binomial sum.

This example is not a continuum limit. For fixed nu=1, the allowed family
W=rI as r tends to infinity has D=r², kappa=r²-1 and Z=Mr/2;
at E=0 the sufficient error coefficient 2DLC(E+Z)=LMr³ diverges.
The present estimate thus supplies no fixed-speed uniform guarantee over
that family. Failure of an upper bound to tend to zero is NOT an error lower
bound or a no-go theorem; a continuum extension needs a genuinely uniform
energy/mode construction or a stated scaling of resources.

## Evidence, prior work and ceiling

The explicit probe checks one-particle positivity/phase repair, exact squeeze
order, commutator growth constants, noncommuting cutoff identity and work
algebra; genuine faults alter the beam shift, phase sign, measurement shift,
pulse order and cutoff commutator. These finite exact controls support the
written full-Fock/domain proof; they are not proof-assistant certification.
K2154 supplies the finite-chain energy-comparison framework; K2223 supplies
positive oscillator pulses. Their old limitations are preserved as history.
The energy-constrained channel concept is standard; see
[Shirokov](https://arxiv.org/abs/1706.00361). No novelty claim is made.
[Certificate](../../lab/process/k2225-positive-drift-detector-control.json).

The remaining physical tasks are a continuum limit with uniform mode/domain
control, an achievable spectral interaction and clock, and bath renewal costs.
A finite-chain conditional implementation does not supply a source action,
source observation, physical quotient, local continuum optimum or GU forecast.
