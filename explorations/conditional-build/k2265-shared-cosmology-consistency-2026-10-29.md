---
title: "K2265 One shared action constrains the whole expansion history"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2265_shared_cosmology_consistency_probe.py
---

# K2265 One shared action constrains the whole expansion history

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2265 One shared action constrains the whole expansion history
carrier: positive C3 expansion history on a connected redshift interval LAYER=toy CHIRALITY=N/A
pairing: real scalar integration and metric contraction ON=declared_carrier
real_structure: real scalar histories and real metric coefficients
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: global fixed-coefficient vacuum metric compatibility MAP-TYPE=evaluation
```

## Result and scope

The fixed quadratic metric vacuum family has an exact nontrivial expansion-history test: a computed quantity Q must be one affine function of H² on the entire interval. Two distinct expansion values identify the two coefficient ratios; every remaining value tests that same pair. The full 00 equation suffices, with its differential identity, to recover the trace and spatial equations. Constant expansion and constant curvature need separate treatment. In particular a non-de-Sitter constant-curvature branch exists only with F=0 (vanishing Ricci coefficient).

This advances the [October27 local-horn calculation](../../lab/active-research/joe-directed/prediction-kickoff/late-time-finite-node-identifiability-2026-10-27.md). It does not repeat that note's unbounded-slope result or infer arbitrary data fitting from local existence. Its action is the supplied observed four-dimensional metric model, not the source-native connection-distortion theory. SC-COS-50/51/54 ASSERTS their stated dark-energy demands; none supplies the model-to-GU bridge here. LT-GR2e remains NEEDS, ledger0.263 unchanged. The earlier local horn's radiative-screening failure remains in force.

## 1. Fixed object, full constraint and exact elimination

Use flat FLRW, signature (-,+,+,+), standard physical-metric redshift x=1+z>0, H>0 and vacuum metric variation of

    f(R)=alpha R-b R²/2-rho, b!=0, F=alpha-bR.

Coefficients are constant across the interval. They may be specified in advance or jointly inferred; the latter tests family membership, not prediction. Define a=alpha/b, r=rho/b, y=H² and primes=d/dx. The overall nonzero b is invisible to these vacuum background equations, although its sign matters for F. Standard redshift gives dot=-x sqrt(y) d/dx and

    R=12y-3xy', P=dot R,
    C=3(alpha-bR)y+bR²/4-rho/2-3bHP,
    C/b = 3ay-r/2+Q,
    Q=-3Ry+R²/4+3xyR'
     =18xyy'+(9/4)x²(y')²-9x²yy''.                 (1)

Assume y is positive C3 on a connected interval. There is one shared pair (a,r) if and only if Q lies in span{1,y} with the stated coefficients throughout the interval. If y(x1)!=y(x2), the unique candidate is

    a=-(Q1-Q2)/(3(y1-y2)), r=2(Q1+3ay1).          (2)

It is accepted only if Q(x)+3ay(x)-r/2=0 for ALL x. Equivalently the determinant with rows (1,y1,Q1),(1,y2,Q2),(1,y(x),Q(x)) vanishes everywhere, using that fixed nonconstant pair. This tests shared coefficients and shared initial history without dividing by y'. An isolated stationary point is harmless. The local ratio -Q'/(3y') must not be used across zero y' without matching constants.

If y=y0>0 globally, Q=0 and r=6ay0. The coefficient pair is unidentifiable along this line. The correct finite design condition is rank[X|-Q]=rank X, X=(3y,-1/2). Merely requiring augmented rank<=2 fails when X has rank1: equal y with unequal Q is inconsistent. Actual constant histories of course have Q=0, but noisy or sampled jets need the proper rank test.

## 2. Why the whole metric equation follows

Reconstruct cosmic time using dt/dx=-1/(x sqrt y). Define

    T=dot P+3HP-(aR-2r)/3.

Direct differentiation, using only dot H=R/6-2H² and dot R=P, gives the OFF-SHELL identity

    dot C=-4HC-3bHT.                              (3)

Thus global C=0 implies T=0 when b!=0 and H>0. The actual spatial covariant-equation residual is E_ii/g_ii=C/3+bT; hence it vanishes too. The alternate acceleration residual E_ii/g_ii+C equals 4C/3 after T=0; these two residuals are not interchangeable. The proof never divides by F. This establishes equivalence to every homogeneous isotropic vacuum component, not just the trace.

If positive effective coupling is part of the model, impose

    F=b(a-12y+3xy')>0                             (4)

on the WHOLE interval. Positivity at finitely many nodes is insufficient. If b is free, a-R must have one nonzero sign throughout, and b must have that sign. Positive F alone does not certify scalar/perturbative stability. Smooth local existence is not fixed survey-interval extension.

## 3. Degeneracy classification

Constant R=R0 integrates to y=R0/12+D x^4. If D=0, expanding de Sitter requires R0>0 and r=aR0/2; F=b(a-R0) can be positive for suitable prescribed coefficients. If D!=0, substituting (1) forces

    a=R0, r=R0²/2, F(R0)=f(R0)=0.

These are genuine degenerate vacuum solutions wherever y>0, because all terms in the metric equation vanish. They fail strictly positive F. Constant R therefore cannot silently be called de Sitter, and these branches cannot be discarded before division.

For an explicit NONCONSTANT positive-F solution on any compact x>0 interval, choose the fixed pure-R² member b=-1, a=r=0 and

    y=C0(x³+D0)^(4/3), C0,D0>0.

Direct calculation gives Q=0 and R=12C0D0(x³+D0)^(1/3)>0, hence F=R>0. C0,D0 are initial-data parameters, not coefficients refitted along the interval. This exhibits a nonempty common finite domain and prevents the test from being an empty-family obstruction.

## 4. An exact excluded expansion family

For y=A+B x^n,

    Q=9n(3-n)AB x^n +(27/4)n(4-n)B² x^(2n).

In particular y=A+B x³ with B!=0 has Q=(81/4)B²x^6. Functions 1,x³,x^6 are independent on every nonempty interval, so NO finite shared a,r makes this a vacuum solution of the fixed b!=0 family. This excludes an exact dust-plus-constant SHAPE when tested as vacuum quadratic gravity. It does not exclude a matter-coupled quadratic theory, observationally approximate shapes, general f(R), or GU. Taking b→0 changes the family and cannot be treated as a finite parameter solution. Ordinary Einstein gravity with dust and a cosmological constant is a distinct countercontrol, not a rescue of this vacuum action.

This is a structural exclusion, not parameter counting or numerical search. It removes the need to fit this exact shape in the declared vacuum family. Nearby approximate fits need a norm/error model, developed in [K2266](k2266-windowed-cosmology-test-2026-10-29.md).

## 5. Identification and the observational ceiling

The transformation y→s²y maps Q→s⁴Q and preserves (1) when a→s²a and r→s⁴r. For fixed b, F→s²F. Jointly scaling the nuisance ruler r_d→r_d/s preserves H r_d and distance/ruler observables. This is a degeneracy of the family with free dimensionful coefficients and ruler, not generally a symmetry when independently fixed numerical alpha,b,rho already supply a scale. Pure R² is an exception with a=r=0. Action normalization and amplitude calibration are distinct freedoms.

A finite set of sampled residuals cannot certify a continuum identity. K2266 gives a stronger counterconstruction preserving expansion and distance nodes simultaneously, as well as a weak/windowed implementation and shared-domain forward equations. No DESI numbers, fit significance, native prediction, or cosmological novelty is claimed.

## Verification and prior art

Metric f(R) field equations and reconstruction from H(z) are established background: [De Felice and Tsujikawa, equations2.4 and2.15–16](https://arxiv.org/html/1002.4928v2), [Capozziello, Cardone and Troisi](https://doi.org/10.1103/PhysRevD.71.043503). The contribution here is the exact shared-constant specialization with degeneracy, full-equation and scope controls; no literature-exhaustion or novelty claim.

The accompanying probe checks independent symbolic substitutions, off-shell propagation and spatial residual, constant branches, the nonconstant positive control, exact finite determinant obstructions, scaling and changed-equation faults. Universal equivalence and interval assertions rest on the written proof, not finite sampling. Internal specialist review is separate from external expert, Lean or remote CI certification. Run the listed probe; --write creates its hash-bound report.
