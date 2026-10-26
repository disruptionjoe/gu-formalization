---
title: "K2086: State symmetry, ground selection and detector error"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2086_ground_state_selection.py
  - tests/channel-swings/k2086_ground_state_selection_probe.py
---

# K2086: State symmetry, ground selection and detector error

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
result: explicit stationary real-compatible rivals, conditional ground selector and thermal detector budget
carrier: massive complex Dirac1408 CAR on R3 with gap m positive LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: imported positive Hilbert metric and gauge-invariant quasifree states ON=declared_complex_completion
real_structure: inherited b antiunitary with b squared minus identity and b H b inverse equals minus H
grading: fermion parity and positive/negative energy, separately typed
action_owner: repository-construction -- imported CAR dynamics and optional ground spectrum condition
target: covariance selection and local paired click probabilities MAP-TYPE=intertwiner
```

[Conditional mathematical result; accepted after independent internal specialist review. No external or proof-assistant certification.]

## 1. What is inherited and what is tested

[K2082](k2082-charge-conjugate-detectors-2026-10-26.md) fixes a compatible
anti-involution and a low-noise detector in the supplied sea Q. Compatibility
is not selection. [K1892](k1892-causal-observation-algebra-2026-10-21.md) already
exposes arbitrary positive covariance freedom; older [K87](k87-observed-stationary-polarization-constraint-descent-wave-2026-09-01.md) and [K97](k97-observed-local-fermionic-reservoir-record-wave-2026-09-02.md) respectively
supply a ground selector on a different bosonic carrier and imported thermal
CAR reservoir states. Here compose these standard ideas on the actual massive
1408 carrier with b²=-I and quantify the local detector consequence. No claim
of a first ground theorem or a first thermal CAR construction is made.

Let H be the fixed self-adjoint massive generator, spectrum outside(-m,m),
Q=1_(H<0), P=I-Q. CAR, the positive Hilbert metric, time orientation, and H are
supplied. The source has not selected this completion: SC-OP-04 ASSERTS candidate
grammar, SC-OP-05 and SC-META-53 are UNCERTAIN; SC-META-56 DISAVOWS an odd-action
prerequisite. LT-SM8/GR6b and every source/physics/canon verdict remain unchanged.

## 2. Symmetry, even with purity, does not select the sea

For beta>=0 define C_beta=(I+exp(beta H))^-1 by bounded functional calculus.
It is a positive contraction, commutes with H, and

    b C_beta b^-1=I-C_beta.

Thus its gauge-invariant quasifree state is stationary and invariant under
K2082's linear particle-hole CAR automorphism. For finite beta it differs from Q.
It is generally mixed, but imposing purity still does not select Q: for any R>m,

    C_R=Q 1_(|H|>R)+P 1_(|H|<=R)                    (1)

is a projection, commutes with H and has the same particle-hole complement
identity. It reverses a bounded band of occupations. It has finite excitation
energy density but is not a ground state. No spatially integrated finite
excitation energy over infinite R3 is asserted. These are explicit controls
on the very same carrier, not differently fitted Hamiltonians or metrics.

## 3. The exact extra selector

Impose the full CAR ground spectrum condition: an invariant state's GNS
implementer G is nonnegative and annihilates its cyclic vector. This is stronger
than stationarity or passivity. For A in the dynamics derivation domain,

    omega(A* [G,A])=<A Omega,G A Omega> >=0.

In the gauge-invariant quasifree class, stationarity gives [C,H]=0. For f in a
bounded positive spectral interval, take A=a(f); [G,a(f)]=-a(Hf), so the condition
forces -<f,C Hf>>=0. Since H>=m there and C>=0, C vanishes on that interval.
For a bounded negative interval take A=a*(f); [G,a*(f)]=a*(Hf) gives
<f,(I-C)Hf>>=0, forcing I-C to vanish there. Increasing bounded intervals exhaust
P and Q. Positivity eliminates off-diagonal blocks (also excluded by stationarity),
and there are no zero modes. Hence C=Q. Wick's rule then fixes the state in this
class; the known sea representation attains the ground condition. This is a
conditional selector after the imported H and time orientation, not a selection
by GU geometry. No theorem about an interacting physical quotient follows.

If only even, parity-preserving apparatus operations are admitted, the full-CAR
hypothesis must not be silently weakened. The proof explicitly tests a(f) and
a*(f); no automatic transfer to an even-observable-only variational condition
is made. A zero spectral subspace would also retain arbitrary covariance there.

## 4. Quantitative detector consequence

Let d_beta(x)=1/(1+exp(beta x)) and delta=d_beta(m). Functional calculus yields

    ||C_beta-Q|| <= delta,
    |nu_beta-nu| <=delta,  nu_beta=<f,C_beta f>, nu=<f,Qf>.  (2)

For K2082's untouched orthogonal multiplicity pair the cross covariance is zero
also for C_beta, and the two defect occupations are independent with the same
mean nu_beta. Thus the complete coarse projection E has

    p_beta=2nu_beta-nu_beta²,
    |p_beta-p_sea|<=2delta,
    p_beta<=2(tau²+delta)                             (3)

when the inherited compact cutoff gives nu<=tau². It is the same positive
projection E; no vacuum subtraction or refined measurement is introduced.
For tau<1/500 and beta*m>=log(249999), delta<=1/250000 and

    p_beta < 1/62500.                                (4)

This is a background-click budget in the specified state, not a bound on
thermal signal fidelity, detector implementation time or apparatus work.
Thermal noise need not increase relative to sea noise for every f: a negative
energy f has nu=1 while nu_beta<1. There is no positive uniform thermal floor
from the mass gap alone, since modes can run to arbitrarily high positive energy.

A graph-norm bound supplies a meaningful floor. For normalized f in Dom H,
C_beta>=d_beta(|H|) and I-C_beta>=d_beta(|H|). The scalar d_beta is decreasing
and convex on[0,infinity); Jensen and <|H|><=||Hf|| give

    nu_beta, 1-nu_beta >= d_beta(||Hf||).

Consequently p_beta>=2d-d² with d=d_beta(||Hf||). If ||Hf||<=M uniformly,
replace d by d_beta(M). The K2080 cutoff bound M=201m/100 supplies a concrete
strictly positive finite-temperature lower floor for that energy-limited family.
This is consistent with(4), and exposes the temperature/energy/localization
tradeoff instead of promising exact vacuum silence.

## 5. Density and representation boundary

For H²=(|p|²+m²)I of rank1408, the thermal particle-plus-hole excitation density is
1408 integral d_beta(sqrt(p²+m²)) d³p/(2pi)³; its energy density inserts
sqrt(p²+m²). For beta>0, exponential decay makes both finite. A nonzero constant
density integrates to infinite total excitation on R3. At beta=0 even density
diverges. Therefore the thermal state is not being treated as a finite-energy
vector over the infinite-volume sea. K2082's sea-vector postmeasurement energy
formula cannot be transferred here without a new relative-energy argument.
The bounded local CAR probabilities and norm estimates(2)--(3) require no such
transfer. The band-flip control(1) has finite density by bounded momentum support.

## Verification and next decision

The exact finite probe independently constructs thermal product states and
particle-hole matrices, tests pure flipped controls, ground-energy signs,
paired click formulas and the rational temperature budget, and plants actual
coefficient/state faults. The written spectral argument carries the infinite
dimensional selector and density claims; finite checks are not physical validation.
Next test which operational ground/passivity criterion survives a genuinely
source-selected observation/action map, or quantify thermal relative measurement
energy. Do not requeue the already supplied local R0/R1 maps or confuse these
conditional state choices with source attribution.
