---
title: "K1842: conditional screening, causal response and admissible repairs"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-INSTANTANEOUS-MEAN-SCREENING
claim_ceiling: conditional scalar response and its explicit repairs; no source-owned GU response or physical falsification
---

# Exact mean subtraction can screen constants and transmit distant interventions

The instantaneous spatial-average implementation of the repository's
`Q=1-1 tensor ell` screening horn violates causal response when the admissible
sources include localized scalar interventions and the readout sees the
homogeneous mode. An explicit retarded wave example proves this without
assuming a future-dependent average. Restricting sources or readouts can
remove the response, and a local causal memory filter screens stationary
constants while giving up exact projection. These repairs are tested below.

This is a conditional implementation result. The source does not supply Q,
ell, this scalar action, its source space or its readout. SC-COS-50/51/54
and SC-ACT-01/02 remain ASSERTS; LT-GR2c/2d remain NEEDS. In particular this
is not a counterexample to every nonlocal completion of GU.

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
result: distant-response criterion, cylinder counterexample and causal-memory repair
carrier: real scalar sources and fields on R times a flat three-torus LAYER=toy CHIRALITY=N/A
pairing: real spacetime integral and normalized spatial average ON=scalar_fields
real_structure: ordinary real conjugation
grading: none; scalar nongauge model
action_owner: repository-construction -- linear wave response with explicitly projected external source
target: local scalar or spatial-derivative readouts of a retarded solution MAP-TYPE=evaluation
```

## 1. Native input and operational demand

The [August10 projector result](selected-k77-global-projector-amplitude-layer0-2026-08-10.md)
already proves static constant-shift screening and failure to select a nonzero
VEV amplitude. Reuse those facts. The new question is whether an implementation
can also satisfy the reverse-search local-intervention demand: changing a
permitted source outside a readout's causal past cannot change that readout.
This demand does not import a chiral bulk, a scalar Higgs or a GU action.

Structure fingerprint: real scalar trivial bundle, positive spatial measure,
flat Lorentzian cylinder, ordinary real structure, no internal grading,
no ambient GU embedding. This is a new conditional response object, not an
adapter identifying it with K77, I1B, a tensor stress or a physical BV quotient.
Variational altitude: Euler-admissible variations of the declared scalar
model. Globalization: global periodic spatial domain with retarded Cauchy data.
Commutation: spatial mean commutes with the flat wave operator; causal support
does not survive the source preprocessing. The canonical physics ledger is
unchanged because no source-owned realization or physical bridge is supplied.

Let Sigma be a flat three-torus of volume V and P=partial_t²-Delta_Sigma.
Use zero past data and G_ret, with smooth sources supported in t>0 and in a
bounded time interval. Define

```
bar f(t) = V^-1 integral_Sigma f(t,x) dx,
Q f(t,x) = f(t,x)-bar f(t),
phi = G_ret Q f.
```

All smooth compact-time scalar sources are admissible. There is no gauge
symmetry or Gauss constraint; phi and its derivatives are gauge-invariant
readouts in this nongauge model. A source-coupled wave action with term
`phi Q f` yields this equation with the appropriate kinetic sign convention.
This assumption must be replaced, not silently reused, for a conserved-tensor
or gauge theory.

## 2. Exact continuum counterexample

Choose disjoint spatial neighborhoods U and W, whose distance is d>0. Put
f(t,x)=eta(t)g(x), with g smooth, nonnegative, supported in W and nonzero,
and eta smooth, nonnegative, nonzero, supported in (0,a). Choose
`a<t<d` and observe at x in U (shrink U if necessary to retain the distance).
Finite propagation of the unprojected wave gives G_ret f(t,x)=0. The spatial
mean source is homogeneous, so its retarded response is the exact ODE solution

```
G_ret bar f(t,x) = bar g integral_0^t (t-s) eta(s) ds,
phi(t,x) = -bar g integral_0^t (t-s) eta(s) ds < 0.             (1)
```

The original intervention is outside the readout's causal past. Its projected
source is not. Zero initial data and all scalar equations are satisfied.
The nonzero response follows from a positive integral, not a lattice or a
floating-point precursor. A compact time/spatially smeared readout in the
same region is negative too, so point evaluation is not essential.

Q²=Q, Q1=0 and mean(Qf)=0 remain exact. Integrating the PDE gives
mean(phi)''=0, hence mean(phi)=0. That derived constraint is satisfied by (1)
and the compensating response near W; it does not forbid the original scalar
intervention. There is no contradiction with finite propagation for P,
because Q is spatially nonlocal.

## 3. Complete response criterion and real repairs

For any admissible linear source class A and readout C whose unprojected
response C G_ret is causal, the projected response on a source f outside the
readout's past is exactly

```
C G_ret Q f = -C G_ret [1 bar f].                              (2)
```

Thus absence of distant response on A is equivalent to vanishing of this
right-hand side for every such admissible f. For a single spacetime functional
ell instead of the time-indexed mean, it is the rank-one condition
`ell(f) C G_ret 1=0`, on a domain where G_ret1 is defined. An unrestricted
whole-history ell requires its own temporal-domain analysis; (1) already
fails using a mean at the current time only.

Two exact repairs show why the source/readout hypotheses matter:

1. **Source restriction:** if admissible interventions have bar f(t)=0 at
   every time, Qf=f. The response is causal. A nonnegative localized pulse
   is then forbidden and cannot serve as a counterexample. A local signed
   pulse with zero integral is allowed. Whether a real constraint enforces
   this must be derived from the actual action.
2. **Readout restriction:** C=partial_xj, or a spatially smeared difference
   with zero total weight at a fixed time, annihilates every homogeneous
   response. Then C G_ret Q=C G_ret, so its causal support is unchanged for
   all scalar interventions. Constant forcing was already invisible to this
   readout; this does not supply a new observable cancellation of an otherwise
   measurable constant response. The value readout in (1) is different.

On the mean-zero field space, the inverse uses the projected delta function.
Its apparent nonlocal kernel is harmless for the restricted source/readout
pair above. It is not legitimate to quotient the homogeneous mode after
claiming that phi itself was measurable: that changes C and its physical claim.
No constraint, quotient or readout is chosen for GU by this analysis.

## 4. Executed successor: causal memory instead of exact projection

Use a local auxiliary scalar with zero past data:

```
(partial_t² + gamma partial_t - c² Delta + mu²) chi = mu² f,
P phi = f-chi,                   gamma>0, mu>0, 0<c<=1.        (3)
```

Both equations are hyperbolic with speeds at most1. Retarded composition
therefore has causal support; damping is a lower-order term and changes no
propagation cone. This is an explicitly supplied response model. Damping,
parameters, initial data and auxiliary field are imported, not GU predictions
or a closed conservative action/quantum completion.

For Laplace variable s and spatial Fourier mode k the source filter is

```
Q_c(s,k)=(s²+gamma s+c²|k|²)/(s²+gamma s+c²|k|²+mu²).           (4)
```

It has zero static response at k=0 and tends to1 at high |s|. For a spatially
uniform step f0 at t=0, the critically damped choice gamma=2mu gives

```
chi=f0[1-(1+mu t)exp(-mu t)],
f-chi=f0(1+mu t)exp(-mu t).                                  (5)
```

The effective forcing decays to zero. The wave field need not return to zero:
its homogeneous velocity gains `2f0/mu` and generally retains memory. Thus
(3) screens the *late forcing*, not the full historical response, an absolute
VEV value or arbitrary time-dependent uniform shifts. Q_c² differs from Q_c
by `-mu² N/(N+mu²)²`, N=s²+gamma s+c²|k|². It is not an exact projector.
This is a concrete causal repair with explicit costs and a narrower promise.

A simple temporal obstruction explains this tradeoff: a scalar stable causal
transfer q(s), analytic on a connected right half-plane, satisfying q²=q there
is identically0 or1. Its image lies in the discrete set {0,1}, so continuity
on a connected domain suffices. It cannot both suppress the DC limit and
pass a high-frequency limit. This theorem concerns the homogeneous scalar
channel only, not matrix-valued projectors, constrained gauges, nonstationary
operators or all possible nonlocal theories.

## 5. Validation, contrary constructions and next evidence

The producer passes18 exact algebra groups; the independent probe passes99
rational controls and rejects5 reporting faults. The exact producer checks
Q identities, ODE response, critical-damping solution,
transfer defect, gain limits and the retained-velocity integral. The independent
standard-library probe uses rational polynomial pulse integration and a
separately constructed finite rank-one model for the algebraic criterion,
source/readout repairs and rational transfer values. The finite model is an
algebra control; (1) and finite propagation prove the continuum conclusion.
Reporting-scope mutations are separate from mathematical checks.

```
sage -python tests/channel-swings/k1842_screening_causal_response.py
python3 tests/channel-swings/k1842_screening_causal_response_probe.py
```

Inline preflight compared a whole-spacetime mean, instantaneous spatial mean
and action-constrained intervention. The spatial mean makes the strongest
simple counterexample without presuming future averaging. Inline hostile
postflight checks forbidden perturbations, gauge/readout dependence, derived
mean constraint, compact smearing and the repair's residual memory. It rejects
the overclaims that every nonlocal screening is acausal or that (3) removes
all response. No separate-agent review or novelty claim.

The classical Green-support background is [Bär, Green-hyperbolic operators](https://arxiv.org/abs/1310.0738).
The explicit flat-cylinder calculation above supplies the present application.
Next source-facing input is an actual admissible perturbation space and
observable response for the same GU action/domain. Equation (2) is its test;
free scalar interventions may not be imported into a constrained theory.
The causal filter needs a selected conservative reservoir/action and observed
readout before any physical credit. The static amplitude-selector debt remains.
