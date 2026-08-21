---
title: "B5 polarized closed realizations: Fourier-modal graph theorem and extension-sensitive kernel witness"
status: active_research
doc_type: exact_unbounded_operator_domain
created: "2026-08-21"
registry: lab/process/b5-polarized-closed-realization.json
probes:
  - tests/channel-swings/b5_polarized_closed_realization_probe.py
grade: "ON THE REPOSITORY-CONSTRUCTED FLAT B5 HALF-CYLINDER, EVERY CONSTANT COFLIP-FIXED MAXIMAL-ISOTROPIC TRACE GRAPH DEFINES A CLOSED GLOBAL FOURIER-MODAL REALIZATION OF THE STRICT CONSTANT-COEFFICIENT EXPRESSION. TWO GRAPHS IN OPPOSITE COMPONENTS GIVE DISTINCT CLOSED COFLIP-COMPATIBLE REALIZATIONS. FOR ONE EXPLICIT BOUNDED COFLIP-COMPATIBLE DEFORMATION, A DECAYING ZERO-MODE LIES IN THE KERNEL OF ONE REALIZATION AND NOT THE OTHER, SO GLOBAL KERNEL DATA ARE GENUINELY EXTENSION-SENSITIVE IN THE BOUNDED-DEFORMATION FAMILY. THIS DOES NOT COMPUTE THE STRICT MASSLESS KERNEL OR SELECT A PHYSICAL OR SOURCE-OWNED DOMAIN."
target_verdict: B5_POLARIZED_CLOSED_REALIZATIONS_EXIST_AND_BOUNDED_DEFORMATION_KERNEL_IS_EXTENSION_SENSITIVE
target_claim: internal target B5-POLARIZED-CLOSED-REALIZATION-DISCRIMINATOR; verdict graph-trace obstruction absent for constant polarizations on the named flat product
canon_verdict_change: none
---

# B5 polarized closed realizations

## Continuation update — strict massless kernel dependence constructed

The bounded deformation is no longer the only global kernel discriminator.
For the undeformed action-owned massless expression, the positive tangential
mode `xi=-e0+i e4` is complex-null and coflip-fixed. An exact transverse
nongauge trace gives the decaying zero mode `exp(-r) exp(i y4) v`. A real Witt
polarization containing its Green-null trace and a second polarization
replacing that Witt line define two closed coflip-compatible realizations; the
mode lies in the first kernel and is excluded from the second domain.

This proves strict `M=0` operator-kernel extension dependence, not BV/BRST
cohomology or positivity. See
`explorations/b5-strict-massless-extension-dependence-2026-08-21.md`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the constant-coefficient strict B5 folded expression
on the repository-constructed flat half-cylinder. It is not Weinstein's
unreleased source action, the global geometry of `Y=Met(X)`, an elliptic Dirac
boundary problem, a positive physical Hilbert space or the graph-mixing
Stage-B family.

```gu-typed-objects
result: every constant coflip-fixed maximal-isotropic trace graph yields a closed global Fourier-modal strict B5 realization, two opposite-component graphs give distinct domains, and a bounded-deformation zero mode witnesses extension-sensitive kernel data
carrier: L2 sections of the rank-1920 complex folded carrier E=S plus V* tensor S over [0,infinity) times T13 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: auxiliary positive L2 graph topology plus the program-native split Hermitian Green form B_n on boundary traces ON=independent-B5-curved-strict-carrier
real_structure: relative Gamma-natural antilinear coflip covering the integral torus sign involution and fixing n=dr
grading: linear abelian BV ghost-field fold on the repository-constructed flat product end
action_owner: repository-construction strict massless bulk action; the kernel discriminator uses a separately declared bounded coflip-compatible deformation and selects no source or physical domain
target: inclusion of constant maximal-isotropic trace graphs into closed Fourier-modal operator domains and comparison of two resulting global kernels MAP-TYPE=inclusion
```

## Result first

Let `E` be the complex rank-1920 strict folded carrier and let `B=B_dr` be the
invertible normal coefficient on

```text
M_plus=[0,infinity)_r x T^(8,5).
```

For every constant coflip-fixed maximal-isotropic trace graph `L_U`, with
`U in O(960)`, the modewise boundary condition

```text
u_k(0) in L_U,       k in Z^13,
```

defines a closed realization `D_U` of the strict constant-coefficient folded
expression. No ellipticity, Calderon projector or APS construction is used.

Taking `U=I` and the reflection

```text
R=diag(-1,1,...,1)
```

gives two distinct closed coflip-compatible realizations. Their parameters
lie in the two components of `O(960)` because `det(I)=+1` and `det(R)=-1`.
Thus the prior pointwise moduli is not merely formal: at least these—and in
fact every constant member—promote to global closed domains on the named flat
product.

## Fixed-mode closedness

Fourier series on the tangential torus diagonalizes the constant-coefficient
expression:

```text
L2(M_plus;E) = direct_sum_(k in Z^13) L2(R_plus;E),
D_k = B d/dr + C(k).
```

For fixed `k`, `C(k)` is a finite-dimensional constant endomorphism and `B` is
invertible. Therefore

```text
u' = B^-1(D_k u-C(k)u).
```

The graph norm of `D_k` and the `H^1` norm are equivalent, with constants
allowed to depend on `k`. The trace map `H^1(R_plus;E)->E` is continuous, so

```text
Dom(D_(k,U))={u in H^1(R_plus;E):u(0) in L_U}
```

is graph-norm closed and `D_(k,U)` is closed. This argument uses only the
noncharacteristic normal coefficient. The tangential symbol may remain
ultrahyperbolic.

## Global direct sum

Define

```text
D_U = direct_sum_k D_(k,U),
Dom(D_U) = {u=(u_k): sum_k (||u_k||^2+||D_(k,U)u_k||^2)<infinity}.
```

A Hilbert direct sum of closed operators is closed. Compact-interior smooth
sections lie in every `Dom(D_U)`, so each `D_U` extends the minimal
realization. The boundary condition means that every Fourier coefficient of
the distributional trace lies in the same finite-dimensional subspace `L_U`.
The torus sign involution permutes Fourier modes, and the relative coflip fixes
`L_U`; hence the domain and closed graph are coflip-compatible. On finite-mode
cores, the Green boundary term vanishes because `L_U` is isotropic, and the
identity passes to every trace pair for which that pairing is defined.

The proof deliberately does not claim a `k`-uniform elliptic estimate. None is
needed for closedness of the direct-sum operator with its natural graph domain.

## Contrary realization and global kernel discriminator

Let `L_I=graph(I)` and `L_R=graph(R)`. Choose a nonzero coflip-real

```text
v=(e_1,e_1) in L_I but not in L_R.
```

Fix a coflip-invariant auxiliary positive fibre metric, let `P_v` be the
orthogonal projection onto `Rv`, and define the bounded constant zero-order
endomorphism

```text
M=B P_v.
```

Because `v`, the auxiliary metric and `B` are coflip-real at the fixed normal,
`M` is coflip-compatible. For the tangential zero mode,

```text
u(r,y)=exp(-r)v,
(D+M)u=(-Bv+BP_v v)exp(-r)=0.
```

The section is square-integrable and belongs to `Dom(D_I+M)`. It does not
belong to `Dom(D_R+M)` because its boundary trace is not in `L_R`. Therefore
the two global kernel subspaces are different. This is an exact extension-
sensitivity witness inside the already admitted family of bounded lower-order
deformations.

The witness is not the action-owned flat massless member: that branch has
`M=0`. It proves that the prior “global kernel is extension-sensitive” row is
substantive for the bounded-deformation family, but it does not determine the
strict massless kernel, cohomology or positivity.

## Ownership and claim ceiling

The bulk action still admits every maximal-isotropic graph and selects none.
The filed primary source still supplies no endpoint, asymptotic or real/Krein
selector. Closedness removes the graph-trace obstruction on this explicit
flat model; it does not turn mathematical availability into action or source
ownership.

No Hilbert self-adjointness, maximal dissipativity, Fredholmness, Calderon
data, strict massless spectrum/cohomology, positivity, physical state space,
source-selected global `Met(X)` geometry, particle result or GU verdict is
claimed.

## Reproduction and continuation

`tests/channel-swings/b5_polarized_closed_realization_probe.py` certifies the
split-graph construction, opposite components, exact rank/dimension formulas,
fixed-mode graph estimate, direct-sum norm and bounded-deformation zero-mode
witness using rational arithmetic.

The next honest B5 discriminator is
`B5-STRICT-MASSLESS-EXTENSION-DEPENDENCE`: compute or obstruct a difference
in kernel/cohomology between two named closed `D_U` realizations for the
undeformed action-owned massless expression. Positivity remains downstream of
that result and a separate Krein-to-probability rule. A source/action selector
remains a distinct reopen condition.
