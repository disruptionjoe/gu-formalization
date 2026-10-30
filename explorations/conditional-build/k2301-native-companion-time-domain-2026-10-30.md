---
title: "K2301 Native companion time-domain realization"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction only; no native physical acceptance
scripts:
  - tests/channel-swings/k2301_native_companion_time_domain_probe.py
---

# K2301 Native companion time-domain realization

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: K2301
carrier: selected K77 ambient one-form distortion and horizontal metric profile LAYER=ambient CHIRALITY=N/A
pairing: native trace/Hodge indefinite form; explicitly auxiliary positive norm ON=declared_carrier
real_structure: real coefficients; complex Fourier or Hilbert representation only where stated
grading: stated native Clifford grades or ordinary scalar/number grading; no identification
action_owner: repository-construction -- selected flat T0 I1B Shiab quadratic germ
target: complete companion and induced metric source MAP-TYPE=evaluation
```

## Result and prior evidence

[K2298](k2298-enlarged-native-companion-2026-10-30.md)'s polynomial inverse extends to a concrete Schwartz or periodic time-profile domain. Its bounded inverse is two-sided: for a nonnegative nonzero compact metric profile the retarded companion grows exponentially. This is a genuine domain distinction, not a new full spacetime causal theorem. [K134](selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil-2026-08-16.md) already excludes nonzero real timelike Fourier roots, and [K135](selected-k135-native-i1b-t0-coupled-shell-green-domain-2026-08-16.md) already identifies squared radii4 and121 on the metric-image sector; the new result is an explicit reducing profile block, closed domain, source map and causal-tail test. No new spectral roots or nonresonance discovery is claimed.

SC-ACT-01/02 ASSERTS their action/equation and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita. We retain the selected Shiab and real K77 fork, not a unique source-selected operator or physical matter coupling. Ledger0.263 remains unchanged.

## 1. Exact reducing sector

Use K2298 eta=(+---,++++++,----), C=kappa K+E(D), L=K^-1 E_0. All coefficients are constant and kappa is real nonzero. Define

    W=dx1 gamma1, V=sum(i=2..13) dxi gamma_i,
    U=dx1 gamma01, Z=sum(i=2..13) dxi gamma0i.

Every ambient output is included in the exact identities

    LW=-U+Z, LV=12U+10Z, LU=-W+V, LZ=12W+10V.

In ordered basis(W,V,U,Z), L=[[0,B],[B,0]], B=[[-1,12],[1,10]]. The native K Gram is diag(1,12,-1,-12); L is K-skew. Nondegeneracy and invariance imply the K-orthogonal complement is invariant, so other Clifford/form components cannot alter the projected equation for time-only fields. In the auxiliary positive Gram G+=diag(1,12,1,12), L is self-adjoint, with eigenvalues ±11,±2 and minimal polynomial (L²-121)(L²-4). G+ does not supply physical positivity.

For h11=H(t), the complete companion equation is

    (kappa+L d/dt)T=-H'' V.                              (1)

The native curvature calculation, not a substituted Einstein action, supplies this right side.

## 2. Closed realization and exact source

On L²(R,G+) take domain H¹(R)^4. Fourier multiplication by kappa+i omega L has inverse of norm at most1/|kappa|; omega times its inverse is bounded, so it maps L² to H¹. The operator is closed and bijective. Smooth rational multipliers preserve Schwartz space. The same statement on a circle gives a unique smooth periodic solution. The scalar resolvents

    f11=(kappa²-121 d²/dt²)^-1 H'',
    f2 =(kappa²-4 d²/dt²)^-1 H''

give q=(12 f11(1,1)+f2(-12,1))/13, with

    (a,b)=-kappa q, (u,z)=B q', T=aW+bV+uU+zZ.           (2)

Thus a=-12kappa(f11-f2)/13 and b=-kappa(12f11+f2)/13. Direct native curvature pairing gives all ten metric entries:

    J11=12 b'', J22=J33=a''+11b'', J0mu=0,
    all remaining offdiagonal entries zero.              (3)

This source is divergence-free for time-only profiles, but not physical matter: zero energy density and general nonzero stress need a separately selected source action. Equation(2) solves the full companion; (3) defines the necessary metric source. It is not an inverse of the complete coupled Hessian for arbitrary prescribed Jg.

## 3. Retarded versus tempered

Each eigenmode solves (kappa+lambda d/dt)y=f. Its retarded kernel is

    G_ret(t)=1_(t>=0) exp(-kappa t/lambda)/lambda.

If kappa/lambda<0 it grows exponentially. The unique tempered kernel instead is

    G_temp(t)=-1_(t<=0) exp(-kappa t/lambda)/lambda

for that sign; the positive sign uses G_ret. Both have the correct unit jump. V has nonzero projection onto all four eigenvalues: V=(12/13)(W+V)+(1/13)(-12W+V), and each grade-one vector splits between the two signs.

For nonnegative nonzero H in C_c∞, each growing future tail coefficient contains

    integral exp(kappa s/lambda) H''(s) ds
      =(kappa/lambda)² integral exp(kappa s/lambda) H(s) ds>0.

Consequently no retarded tempered companion exists for this source in the full time-only carrier. The two-sided inverse is Schwartz but anticipates the source. This is not a contradiction: initial-value existence and tempered full-line invertibility ask different questions. At kappa=0 the inverse bound and uniqueness fail, including constant periodic kernels.

Time-Schwartz functions constant in space are not finite norm on R^13. On an explicitly supplied flat spatial13-torus, the same sector is finite spatial norm and averaging commutes with the complete constant-coefficient operator. Its forced average proves that adding nonzero spatial modes cannot restore a retarded tempered companion. This auxiliary torus is neither physical causality nor source-selected GU geometry. A coupled causal problem with h solved rather than prescribed, noncompact localized sources, changed boundary data, variable backgrounds and physical readout all remain distinct constructions.

## 4. Restricted joint metric-source response

Let D=d/dt and Delta=(kappa²-121D²)(kappa²-4D²). Eliminating the companion in this SAME profile class gives

    J11=-12kappa D^4 (kappa²-13D²)/Delta H,
    J22=J33=-kappa D^4 (11kappa²-35D²)/Delta H.            (4)

Thus 12(kappa²-13D²)J22=(11kappa²-35D²)J11. Supplying J11 alone does not independently set the other metric equations. The formal inverse transfer is

    H=-Delta/[12kappa D^4(kappa²-13D²)] J11.             (5)

Its nonzero Laplace poles are ±kappa/sqrt13, with no numerator cancellation, plus a fourth-order zero-frequency pole. These are restricted source-response poles, not new roots of the complete Hessian. On Schwartz space the Fourier multiplier in(4) has exactly a fourth-order zero at omega=0 and no other real zeros. Hence a unique Schwartz H exists exactly when integral t^j J11(t)dt=0 for j=0,1,2,3. Division by omega^4 after these vanishing jets preserves Schwartz regularity; at infinity the inverse has only polynomial behavior.

The moment and causal constraints are independent. Take J11=D^4 psi for nonnegative nonzero psi in C_c∞. Its first four moments vanish, but the retarded inverse in(5) has a nonzero growing tail because the weighted moment of psi is positive and Delta does not cancel that pole. This does not forbid compact compatible source tuples: choose H=Delta psi instead. Both scalar denominators in(2) cancel, so T and every source entry are compact differential expressions in psi. Such matched sources supply an exact countercontrol to a universal causal impossibility claim. Physical sources cannot be freely reverse-selected without changing the problem; a physical matter/readout and full coupled realization remain open.

## Verification and consuming next condition

The probe reuses only parsed function definitions from the pinned K2298 probe, avoiding its unrelated grade5 census. It recomputes native columns, both Grams, four eigenprojectors, all ten metric-source entries, Fourier residual, and the polynomial control. Written Fourier and positive-moment arguments establish continuum claims; finite numerical fixtures are not their proof. Altered coefficients/signs and deleted even blocks give genuine failed checks. Independent agent review is internal, not Lean, novelty or external-expert certification.

The result shows that polynomial solvability does not by itself provide a causal bounded realization. Next extend beyond the solved scalar metric profile to a full coupled metric/source/readout and temporal boundary prescription; test whether that larger coupled system removes the growing response modes. Do not repeat the known spectral roots or call the auxiliary torus physical spacetime.
