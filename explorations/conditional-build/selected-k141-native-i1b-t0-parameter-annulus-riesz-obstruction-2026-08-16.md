---
title: "Selected-K141 native I1B T=0 parameter-annulus Riesz obstruction"
status: active_research
doc_type: exact_compact_parameter_graph_and_characteristic_riesz_gate
created: "2026-08-16"
registry: lab/process/selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction.json
probe: tests/channel-swings/selected_k141_native_i1b_t0_parameter_annulus_riesz_obstruction_probe.py
grade: "K141 CONSTRUCTS A UNIFORMLY BOUNDED SMOOTH ACTION-DERIVED GRAPH FAMILY ON THE EXPLICIT COMPACT ANNULUS 13 <= |MU| <= 14, WHICH IS SEPARATED FROM MU=0 AND ALL TWENTY-SEVEN SPACELIKE SHELL RATIOS. THE GRAPH IDEMPOTENT P_MU=R_MU E AND ITS PARAMETER DERIVATIVE ARE EXACT AND COVARIANT AT THE TEN-DIMENSIONAL METRIC-GRAPH GRADE. THIS DOES NOT PRODUCE THE REQUIRED CHARACTERISTIC PROJECTOR. THE NULL SCHUR FORM IS -48 ELL_N ELL_N^T; AFTER RAISING AN INDEX WITH THE NATIVE DEWITT FORM ITS RANK-ONE ENDOMORPHISM N HAS N^2=0 AND SPECTRUM {0}. THE RIESZ PROJECTOR AROUND ZERO IS THEREFORE THE IDENTITY ON ALL TEN METRIC DIRECTIONS, NOT THE NINE-DIMENSIONAL RADICAL PROJECTOR. SELECTING THAT RADICAL REQUIRES A COMPLEMENT TO ELL_N, AND DESCENDING TO FIVE CLASSES ALSO REQUIRES A DIFFEOMORPHISM SLICE OR KT/BV DATA, NONE OF WHICH THE CURRENT ACTION OWNS. THE BAND-LIMITED GRAPH ELIMINATION SURVIVES; A FIVE-BY-FIVE GREEN/SUBPRINCIPAL OPERATOR REMAINS UNDEFINED."
target_claim: K140_NEXT_GATE__COMPACT_PARAMETER_ANNULUS_GRAPH_GREEN_RIESZ_PROJECTOR_COVARIANCE_AND_SUBPRINCIPAL_TEST
target_verdict: COMPACT_ANNULUS_GRAPH_UNIFORMLY_BOUNDED_AND_SMOOTH__GRAPH_IDEMPOTENT_EXACT__NATIVE_NULL_SCHUR_ENDOMORPHISM_RANK_ONE_SQUARE_ZERO__ZERO_RIESZ_PROJECTOR_IS_IDENTITY_NOT_RADICAL__FIVE_CLASS_GREEN_SUBPRINCIPAL_DESCENT_REQUIRES_UNOWNED_COMPLEMENT_AND_GAUGE_SLICE
canon_verdict_change: none
---

# Selected-K141 native I1B T=0 parameter-annulus Riesz obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, mixed-order parameter-symbol and
> indefinite-metric projector calculation. Ordinary Einstein, Higgs/VEV,
> family-index, chirality, anomaly, symmetry-breaking and familiar particle-
> spectrum constructions do not adjudicate it without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K141 binds the selected displayed `comm/symi/symi` `I1B` Hessian at
`T=0`, the complete real `Omega1(Cl(7,7))` carrier, K138's smooth horizontal
null stratum and the separate joint family `kappa_1=rho mu`. It studies only
the normalized compact band `13 <= |mu| <= 14`. It is not an ultraviolet
equivalence theorem for the original fixed-`kappa_1` action.

## Result in plain English

K140 left one mathematically valid effective object: on a compact parameter
region away from zero and every distortion shell, eliminate distortion by

```text
C_mu=i C_1(n)+mu K,
D_mu=C_mu^(-1) A,
R_mu g=(g,-D_mu g).                                      (1)
```

The annulus

```text
13 <= |mu| <= 14,       169 <= mu^2 <= 196              (2)
```

lies strictly above the largest exceptional squared ratio `168`. Together
with the exact absence of timelike roots and invertibility for nonzero `mu` on
the null packet, (2) gives a compact shell-free normalized family. Continuity
then gives uniform bounds for `C_mu^-1`, `D_mu` and all finite parameter
derivatives. This is the positive K141 result.

The natural graph idempotent is also exact:

```text
E(g,T)=g,
P_mu=R_mu E = [[I,0],[-D_mu,0]],
P_mu^2=P_mu,
d_mu D_mu=-C_mu^(-1) K C_mu^(-1) A.                    (3)
```

Because `A`, `C`, `R` and `E` are action-derived intertwiners, (3) is covariant
at its legitimate grade: it projects the full coefficient space onto the
ten-dimensional graph over all metric directions. It does **not** project onto
the characteristic radical or its gauge quotient.

The obstruction is exact and smaller than a dense eigensolve. K138's null
metric Schur form is

```text
S_n=-48 ell_n ell_n^T,       ell_n(h)=h(n_sharp,n_sharp). (4)
```

Raise one index with the native DeWitt form `G`. Since `n` is null,

```text
ell_n^T G^(-1) ell_n = 0,
N=G^(-1)S_n,
rank N=1,       N^2=0,       spec(N)={0}.                (5)
```

Thus a Riesz contour around zero encloses the entire ten-dimensional metric
space. Its projector is `I_10`, not the rank-nine kernel of `ell_n`. A
projector onto that kernel needs a choice of `u` with `ell_n(u)=1`; changing
`u` changes the projector. The action supplies no such complement. Removing
the four diffeomorphism directions then additionally requires a gauge slice or
KT/BV resolution. The five-class quotient is exact as a quotient, but not as
an action-owned spectral subbundle.

Consequently the smooth derivative in (3) cannot be sandwiched into a
canonical five-by-five Green/subprincipal connection. Compact shell avoidance
repairs the distortion inverse; it does not repair the nilpotent
characteristic spectrum or choose quotient representatives.

## 0. Pre-wave answers

1. **Construction fork.** The smooth ten-dimensional graph and the
   nine-dimensional characteristic radical are different bundles; the
   five-dimensional object is a further quotient by four diffeomorphisms.
2. **Cheapest decisive condition.** A Riesz projector needs an isolated
   spectral cluster. Equation (5) decides that condition exactly.
3. **Positive route.** The compact annulus gives a uniform band-limited graph
   elimination and smooth parameter derivatives.
4. **Negative route.** The native null Schur endomorphism is nonzero nilpotent,
   so spectral calculus cannot select its ordinary kernel.
5. **Claim ceiling.** No statement about the original fixed-mass ultraviolet
   equations, closed domains, physical modes, positivity or cohomology.

## 1. Exact annulus and uniform graph

K134 and K140 give the complete squared shell set

```text
1,2,3,4,5,6,7,8,9,10,11,12,13,16,25,36,48,49,64,81,
88,100,120,121,144,160,168.                              (6)
```

The closest point of (2) to (6) is separated in squared parameter by one.
The annulus is also separated from zero by thirteen. Since the normalized
covector directions and (2) are compact and `det C_mu` has no zero there,
the inverse and graph norms attain finite maxima. No ultraviolet conclusion
follows: fixed nonzero `kappa_1` still has `mu=kappa_1/rho -> 0`.

The graph projector in (3) is not orthogonal and needs no added positive
metric. Its range is the exact solution graph of the distortion equation over
the full metric carrier. This avoids the false choice between rejecting a
valid elimination and importing an unowned Hilbert structure.

## 2. Why Riesz calculus cannot extract the radical

In the ordered symmetric slots

```text
(00),(01),(02),(03),(11),(12),(13),(22),(23),(33),
```

use the DeWitt bilinear form

```text
G(h,k)=h_ab k^ab -(1/2) tr(h) tr(k).                    (7)
```

For `n=(1,0,0,1)`, exact rational arithmetic gives

```text
det G=64,
ell_n^T G^(-1) ell_n=0,
rank(G^(-1) ell_n ell_n^T)=1,
rank((G^(-1) ell_n ell_n^T)^2)=0,
charpoly=lambda^10.                                     (8)
```

Lorentz covariance carries (8) across K138's smooth null stratum. The
algebraic generalized zero eigenspace has dimension ten while the ordinary
kernel has dimension nine. Holomorphic spectral calculus sees generalized
eigenspaces, so its zero projector is `I_10`. It cannot distinguish the
ordinary radical inside a single nilpotent spectral block.

An algebraic kernel projector can be written only after selecting a transverse
`u`:

```text
Q_u=I-u ell_n,       ell_n(u)=1.                        (9)
```

Neither the displayed action nor its four metric Noether directions selects
`u`. Equation (9) is therefore a family of possible splittings, not an
action-owned Riesz projector.

## 3. Green and subprincipal consequence

The graph derivative in (3) is smooth and uniformly bounded on (2). It can be
used in calculations that retain the complete metric graph. A characteristic
transport connection, however, needs a smooth owned projector onto the
characteristic bundle, and a five-class matrix needs a compatible
diffeomorphism quotient/slice. Equations (8)--(9) show both choices are still
missing.

The finite Schur form and K138's quotient geometry remain exact. What remains
undefined is an action-specific representative-level Green/subprincipal
endomorphism on five classes. It is not zero, and compactness alone cannot
define it.

## 4. Route reassessment

The materially distinct routes were:

- parameter-elliptic compactness: succeeds for the full graph;
- orthogonal projection: rejected because it imports an unowned positive
  metric;
- native Riesz projection: fails exactly by the square-zero spectrum;
- algebraic complement: possible only after the unowned choice (9);
- KT/BV quotient: unavailable because the action owns no distortion complex;
- boundary/Green selection: remains a later route only when an explicit
  action-owned boundary functional or domain is supplied.

The structural nilpotence route dominates a broad numerical eigenscan: it is
exact, covariant and exposes why every sampled spectrum would collapse at
zero. Computation is used only to replay the shell inventory and certify the
small DeWitt packet.

## 5. Reverse scaffold and next gate

```text
R0 physical propagation needs a closed action-owned reduced operator.
R1 K138: exact covariant five-class finite-frequency null quotient.
R2 K139: not the complete homogeneous DN principal module.
R3 K140: exact graph; fixed-kappa ultraviolet reduction is nonuniform.
R4 K141: compact parameter annulus gives a uniform smooth graph family.
R5 K141: native Riesz calculus cannot isolate the characteristic radical;
   a complement and gauge slice remain unowned.
R6 K142: classify whether a covariant quotient connection can be defined
   intrinsically without representatives, or prove that an explicit gauge/
   boundary owner is necessary before any effective closed-domain test.
```

K142 must not choose (9), add a gauge fixing or infer a physical domain. It
may test quotient-connection well-definedness directly from the action-induced
derivative modulo the diffeomorphism image. Joe input is not required.

## K142 successor classification

K142 now proves that the fixed split itself supplies a representative-free
intrinsic quotient connection, but no action-specific amplitude term. Since
`E R_mu=I` with fixed `E`, differentiation gives `E dR_mu=0` and therefore
`P_mu dR_mu=0`. All nonzero `dD_mu` data are the graph's extrinsic second
fundamental form. K138's natural transport preserves both `ker ell_n` and the
diffeomorphism image, so it descends directly to their quotient without the
complement rejected here. The resulting connection is independent of `D_mu`
and cannot be promoted to the missing five-by-five Green/subprincipal
endomorphism. K143 must derive the actual lower-order action coefficient and
test radical/gauge basicness before any representative matrix or domain claim.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k141_native_i1b_t0_parameter_annulus_riesz_obstruction_probe.py
```
