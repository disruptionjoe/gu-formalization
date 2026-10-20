---
title: "K1866: Positive scalar spectra cannot hide an infrared trace-removal response at shorter scales"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional linear universal metric response with fixed massless tensor and positive scalar spectral measure; no native GU or constant-vacuum verdict
---

# A quantitative two-scale requirement on a specified metric response

A fixed massless Einstein tensor response supplemented by positive, universally
coupled scalar modes cannot approximately remove its curvature trace at a
nonzero long-wavelength static Fourier scale while approaching the Einstein
metric response at a shorter scale. The statement covers any finite positive
scalar spectral measure, not just one scalar mass. It is a conditional
response theorem, not an exclusion of nonlinear screening, massive/resonant
spin-two gravity, cross-readouts, contact terms or GU.

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
result: continuum positive-spectral two-scale metric-slip bound and explicit scope-exit controls
carrier: conserved symmetric sources and a supplied linear metric response on flat Lorentzian four-space LAYER=toy CHIRALITY=N/A
pairing: universal source-metric coupling with fixed positive Einstein residue and nonnegative scalar diagonal spectral weights ON=real_source_fields
real_structure: real Lorentzian fields; spacelike Fourier variable z=|k| squared positive
grading: tensor versus scalar response only
action_owner: repository-construction -- stated massless-tensor plus scalar exchange class; not source I1B
target: trace response and Fourier gravitational slip at two nonzero scales MAP-TYPE=evaluation
```

## 1. Actual question, custody and prior work

[K1864](k1864-causal-scalar-tensor-completion-2026-10-20.md) realizes the
retarded trace projector with a supplied omega-zero scalar-tensor action and
finds its extra scalar and weak-field cost. Adding one mass spoils its trace
projector. [K1844](k1844-screening-positive-response-2026-10-20.md) already
proves positive conjugate scalar susceptibility and healthy cross/contact
cancellations. Those are reused; raw susceptibility is not the new result.
The new consuming question is whether an arbitrary positive mass distribution
can repair the *same universal metric* at two scales without refitting.

SC-ACT-01/02 and SC-COS-50/51/54 remain ASSERTS; SC-META-53 remains UNCERTAIN.
The source owns augmented ad-valued distortion and a Shiab action, not this
spectral metric class. LT-GR2c/2d/6b and LT-SM8 remain unchanged. In particular,
there is no proved map from native distortion/observation/physical quotient
to the positive measure used here. K1861's equation-dual tensor is not that map.

The closest literature is Dvali, Hofmann and Khoury's degravitation analysis
[hep-th/0703027](https://arxiv.org/abs/hep-th/0703027), especially its distinction
between a fixed massless graviton and massive/resonant tensor response. That
paper studies a different tensor-filter class; it is not being excluded here.
Positive spectral representations and scalar-tensor slip are established
ideas. No novelty or empirical confrontation is claimed.

## 2. Freeze the response, readout and scale variable

Let eta have signature(-+++), k0=0 and z=|k|²>0. Sources obey k^a T_ab=0.
Up to pure gauge terms, assume the physical metric perturbation is

```
h_ab(k) = (2 kappa/z)[T_ab - (1-f(z)) eta_ab T/2],
f(z) = integral_[0,infinity) z/(z+lambda) dmu(lambda),
kappa>0, mu a finite nonnegative measure.                         (1)
```

Here lambda is scalar mass squared, and the *same* scalar coupling is used
in sourcing and measuring the metric. For a finite healthy canonical scalar
sector its weights are squares of real universal couplings after whitening.
The continuum positive-measure representation is an explicit assumption;
it is not inferred from the mere absence of an observed instability.
There are no direct contact subtractions or momentum-dependent couplings.
The tensor residue kappa and its massless pole stay fixed across both tests.

Contracting the linearized Ricci scalar gives

```
R^(1)(k) = -kappa [1-3f(z)] T(k).                               (2)
```

For a static negligible-pressure source, T00=rho, Tij=0, equation(1) gives
h00=kappa rho(1+f)/z and hij=kappa rho(1-f)delta_ij/z. Thus define

```
gamma_F(z) = (1-f(z))/(1+f(z)).                                (3)
```

This is Fourier slip in this translation-invariant linear model. A scale-
dependent Fourier ratio is not automatically the PPN parameter measured in
an extended-body experiment; source profile, inverse transform and nonlinear
regime must be supplied before using observational numbers. The massless
constant case f=1/3 recovers K1864's gamma=1/2 control.
Equation(2) tests a nonzero-momentum trace channel. It does not replace an
eternal vacuum stress by a freely variable pure-volume source, which would
violate conservation; nor does it define a retarded inverse at k=0.

## 3. Continuum theorem and sharp finite-tolerance tradeoff

For 0<x<y and every lambda>=0,

```
y/(y+lambda)-x/(x+lambda)
 =lambda(y-x)/[(y+lambda)(x+lambda)] >=0.                       (4)
```

Integration proves f(x)<=f(y), with strict inequality whenever mu has positive
mass away from lambda=0. Moreover f is concave and
`f'(z)=integral lambda/(z+lambda)² dmu`,
`f''(z)=-2 integral lambda/(z+lambda)³ dmu<=0`.
Differentiation is justified on compact positive-z intervals by finite measure
and bounded integrands. Thus arbitrary many healthy scalar masses cannot
reverse the relative response's scale ordering. This is about z times the
susceptibility: raw susceptibility in K1844 decreases instead.

Suppose at x the relative trace factor obeys `|1-3f(x)|<=delta`, 0<=delta<1.
Then at every y>=x,

```
f(y)>=(1-delta)/3,
gamma_F(y)<=(2+delta)/(4-delta),
1-gamma_F(y)>=2(1-delta)/(4-delta).                           (5)
```

Exact trace removal forces gamma_F(y)<=1/2. Conversely the requirement
`|1-gamma_F(y)|<=epsilon<2` implies f(y)<=epsilon/(2-epsilon), so

```
delta >= 1-3epsilon/(2-epsilon).                             (6)
```

A massless atom of weight(1-delta)/3 attains(5), proving sharpness in this
class. For an illustrative design tolerance epsilon=1/100, not an empirical
bound, delta>=196/199: the permitted trace attenuation is at most3/199.
No mass search or fitted mass continuum can improve this inequality while
preserving(1). The result eliminates that particular repair search.

There are additional checkable response-shape consequences:

```
1 <= f(y)/f(x) <= y/x                 if f(x)>0,
f(theta x+(1-theta)y)>=theta f(x)+(1-theta)f(y).
```

The finite infrared limit is the massless atom mu({0}), by dominated
convergence. Massive modes alone do not produce an infrared trace-removal
plateau. A massless atom does, but its shorter-scale contribution persists.
This limit is spectral bookkeeping, not a global cosmological solution.

## 4. Execute the contrary constructions without calling them GU repairs

The desired low-pass relative scalar response

```
f_cross(z)=c m²/(z+m²), c>0, m²>0,
f_cross(z)/z = c/z-c/(z+m²)                               (7)
```

falls outside the positive *diagonal* measure: it has a negative massive
residue. If(7) is demanded as the same-source propagating scalar exchange,
positive-residue representation forbids it; a two-pole diagonal realization
has a wrong-sign mode.

But negative cross-residues do not themselves prove a ghost. Two healthy
fields with K=I, M=diag(0,m²), source vector(1,1) and readout(c,-c) realize
exactly(7). Their complete source-response matrix is positive semidefinite;
the off-diagonal element can have either sign. Each retarded Klein-Gordon
kernel is causal, and so is their difference on zero-past sources. With c=1/3,
the cross readout tends to trace removal in the nonzero-spacelike infrared
limit and to zero scalar correction at high z. It is not the universal metric
readout/source pairing in(1), and it supplies no full nonlinear vacuum solution.
The source-conjugate response still has both positive residues.

A contact subtraction, derivative readout, changing matter couplings or
nonlinear/environment-dependent screening also exits explicit hypotheses.
Replacing the massless tensor by a massive/resonant spectrum is a different
class, as in the cited literature. None is rejected by(5), and none becomes
native GU by escaping it. A viable new candidate must freeze the common
source, physical readout, tensor response and domain before repeating tests.

## 5. Verification and result-dependent frontier

The symbolic producer checks tensor trace/slip, finite-tolerance algebra,
sharpness and signed/cross repair. The independent Fraction probe reconstructs
positive multi-pole measures, monotonicity/concavity, two-scale bounds and
healthy cross matrices without importing producer code. Planted input faults
must fail mathematical assertions after a clean baseline. These controls do
not prove the continuum theorem; the integrand argument above does.

Inline hostile review distinguished raw response from relative response,
Fourier slip from empirical PPN, diagonal from cross residues, finite-z
conserved sources from constant vacuum, and fixed versus massive tensor.
No independent person, proof assistant or external acceptance is claimed.
Reproduce both scripts named in lab/process/k1866-positive-scalar-screening-window.json.

The arbitrary-positive-scalar repair is answered under(1), so further mass
fitting is unnecessary. The next useful source-facing task is the actual
native physical source/readout and coupled distortion operator, or a supplied
nonlinear/tensor-changing realization with its own constraints. Repeating
ordinary scalar fits cannot fill the native pairing/observation debt.
