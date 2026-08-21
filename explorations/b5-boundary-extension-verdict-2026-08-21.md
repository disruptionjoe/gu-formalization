---
title: "B5 boundary-extension verdict: O(960) coflip-fixed local polarizations, no action/source selector"
status: active_research
doc_type: exact_boundary_trace_classification
created: "2026-08-21"
registry: lab/process/b5-boundary-extension-verdict.json
probes:
  - tests/channel-swings/b5_boundary_extension_verdict_probe.py
grade: "ON THE REPOSITORY-CONSTRUCTED FLAT B5 HALF-CYLINDER, THE REGULAR NON-NULL BOUNDARY GREEN FORM HAS INERTIA (960,960,0), AND ITS COFLIP-FIXED MAXIMAL-ISOTROPIC TRACE POLARIZATIONS FORM O(960), OF REAL DIMENSION 460320 WITH TWO COMPONENTS. THE QUADRATIC BULK ACTION ADMITS EVERY MEMBER AND SELECTS NONE; THE FILED PRIMARY SOURCE IS SILENT. LOCAL/FORMAL AND MINIMAL-DOMAIN VERDICTS ARE EXTENSION-STABLE, WHILE GLOBAL SPECTRAL, COHOMOLOGICAL, POSITIVITY AND PHYSICAL VERDICTS ARE NOT. THIS DOES NOT PROMOTE EVERY POINTWISE POLARIZATION TO A CLOSED GLOBAL ULTRAHYPERBOLIC REALIZATION."
target_verdict: B5_REGULAR_BOUNDARY_POLARIZATION_MODULI_O960_ACTION_SOURCE_UNSELECTED
target_claim: internal target B5-BOUNDARY-POLARIZED-EXTENSION-VERDICT; verdict local regular-boundary polarization moduli classified and ownership absent
canon_verdict_change: none
---

# B5 boundary-extension verdict

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the pointwise regular-boundary trace of the
repository-owned strict B5 Rarita--Schwinger BV expression at `r=0` on the
flat half-cylinder. It is not Weinstein's unreleased source action, the global
geometry of `Y=Met(X)`, the noncompact-fibre C1/collar calculation, the K77
boundary campaign, a positive physical Hilbert space or the graph-mixing
Stage-B family.

```gu-typed-objects
result: the regular B5 boundary Green form is split (960,960), coflip-fixed maximal-isotropic trace polarizations form O(960), and neither the quadratic bulk action nor current source selects one
carrier: boundary trace of U0 plus U1 with complex rank 128 plus 1792 at r=0 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: program-native Hermitian Green form induced by the (9,5) Krein stage pairing and B_n ON=independent-B5-curved-strict-carrier
real_structure: relative Gamma-natural antilinear involution at the coflip-fixed positive normal
grading: linear abelian BV ghost/field fold on the repository-constructed flat product end
action_owner: repository-construction quadratic strict Rarita--Schwinger bulk action; boundary polarization and historical source action remain unowned
target: classification of coflip-fixed maximal-isotropic pointwise trace subspaces and partition of extension-stable versus extension-sensitive verdicts MAP-TYPE=evaluation
```

## Result first

At the positive unit conormal `n=dr`, the prior exact Clifford certificate gives
an inverse for

```text
B_n = [[0,A_n^vee],[A_n,K_n]]
```

on the complex boundary trace carrier

```text
E = S plus (V* tensor S),       dim_C(E)=128+1792=1920.
```

Let `h_n` be the corresponding program-native Hermitian Green form. The form
is nondegenerate. Conormal linearity gives `B_-n=-B_n`. Gamma-natural Pin
covariance supplies an invertible fibre map covering normal reversal and
congrues `h_n` to `h_-n=-h_n`. Therefore positive and negative inertia are
equal. Since the radical is zero and the total dimension is 1920,

```text
inertia(h_n) = (960,960,0).
```

The normal-reversal lift is used only to certify inertia. It exchanges the two
sides of the boundary and is not a symmetry selecting a boundary condition on
the half-cylinder.

## Coflip-fixed maximal isotropics

At the chosen normal, the relative Gamma-natural coflip `C` fixes `n`, is an
antilinear involution and preserves the Green form. Its real fixed space
`E_R=Fix(C)` therefore carries a real split symmetric form of signature
`(960,960)`. Choose any coflip-real fundamental decomposition

```text
E_R = E_R^+ plus E_R^-.
```

Every coflip-fixed complex maximal isotropic is the complexification of a real
maximal isotropic. In the decomposition above it is the graph

```text
L_U = {(x,Ux): x in E_R^+},       U in O(960).
```

Conversely every `U in O(960)` gives such a graph. Thus the local
coflip-compatible polarization space is

```text
O(960),       dim_R = 960*959/2 = 460320,
```

with two connected components. The exact probe embeds rational `O(2)` rotation
families and a reflection, verifies isotropy exactly, and rejects a
nonorthogonal graph. This proves continuity and both components without
materializing a 1920-by-1920 matrix.

The choice of fundamental decomposition is a coordinate choice on the moduli,
not a preferred polarization. Changing it reparametrizes the same set.

## What the action and source own

For fields and variations whose boundary traces lie in `L_U`, the quadratic
bulk variation has boundary term `h_n(psi,delta psi)=0`. This holds for every
maximal-isotropic `L_U`. The bulk action therefore **admits** the whole family
and selects no member. Vanishing boundary flux is a compatibility condition,
not an action-owned selector.

The filed primary-source extraction already returned `SOURCE-SILENT` for the
endpoint/isotropic relation, the noncompact asymptotic domain and the real/Krein
closure. No new source evidence has appeared in the current state. Hence the
current owner verdict is:

```text
ACTION-UNSELECTED / SOURCE-SILENT / LOCAL-POLARIZATION-MODULI-O960.
```

This is not the old compact-collar `T^2` claim. The hostile review of that
claim correctly showed that freedom at a noncompact end depends on its
limit-point/limit-circle class. Here the classified trace is at the actual
**regular boundary `r=0`** of the named half-cylinder. Its local polarization
freedom is distinct from, and coexists with, the separate asymptotic question
at `r=infinity`.

## Exact extension-stability partition

The following conclusions precede any maximal extension and therefore survive
every later compatible extension choice:

- the native strict principal symbol and Einstein action closure;
- the `ANTI` formal-adjoint sign;
- the complete program-native Green coefficient `B_n`;
- relative Gamma-natural coflip covariance;
- existence of the minimal closed realization, its formal-expression
  commonality and bounded-perturbation graph-domain commonality;
- the null-conormal transverse nongauge radical; and
- strict five-field packet admission at the declared **minimal-realization**
  grade.

The following are not fixed by those local data and cannot be propagated
uniformly across the extension family without a separate theorem:

- global kernel, spectrum, eta invariant or index;
- global BV/BRST cohomology and characteristic quotient;
- positivity, probability rule and physical state space; and
- Fredholm, Calderon, scattering or propagator data.

The exact stable conclusion is therefore the minimal-grade packet and its
local/formal inputs—not a physical extension verdict.

## Analytic boundary and continuation

This result classifies pointwise maximal-isotropic trace subspaces. For an
elliptic Dirac operator, standard boundary-triple or Calderon machinery would
often promote appropriate polarizations to closed realizations. The current
tangential signature is ultrahyperbolic, so that import is unavailable without
a proof. The artifact therefore does **not** assert that all `O(960)` points are
closed global operator domains.

The next honest owner is
`B5-POLARIZED-CLOSED-REALIZATION-DISCRIMINATOR`: on the named flat product,
construct at least one coflip-compatible closed boundary realization and one
contrary realization or prove a trace/graph obstruction, then test whether any
global cohomological or positivity datum differs. A source/action-owned
selector remains a separate reopen condition. Do not guess APS, positive-
Hilbert or physical boundary data.
