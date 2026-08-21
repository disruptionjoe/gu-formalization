---
title: "B5 flat-product minimal domain: one common closed strict realization"
status: active_research
doc_type: exact_unbounded_operator_domain
created: "2026-08-20"
registry: lab/process/b5-flat-product-minimal-domain.json
probes:
  - tests/channel-swings/b5_flat_product_minimal_domain_probe.py
grade: "ON THE REPOSITORY-CONSTRUCTED FLAT B5 HALF-CYLINDER WITH NON-NULL COFLIP-FIXED NORMAL, THE ACTION-OWNED STRICT FOLDED EXPRESSION IS CLOSABLE AND ITS MINIMAL GRAPH CLOSURE IS ONE COMMON CLOSED COFLIP-COMPATIBLE DOMAIN FOR THE FORMAL ANTI-ADJOINT AND EVERY BOUNDED LOWER-ORDER DEFORMATION. THIS ADMITS THE STRICT FIVE-FIELD PACKET AT THE DECLARED MINIMAL-REALIZATION GRADE. IT IS NOT A MAXIMAL-ISOTROPIC, SELF-ADJOINT, FREDHOLM, CALDERON OR PHYSICAL DOMAIN, AND IT IS NOT THE SOURCE-SELECTED GLOBAL MET(X) GEOMETRY."
target_verdict: B5_STRICT_PACKET_ADMITS_MINIMAL_CLOSED_PRODUCT_END_DOMAIN
target_claim: internal target B5-COMMON-AMBIENT-DOMAIN-ON-NAMED-END-MODEL; verdict one minimal closed coflip-compatible realization constructed on the named flat product end
canon_verdict_change: none
---

# B5 flat-product minimal domain

## Continuation update — closed polarized realizations constructed

Every constant coflip-fixed maximal-isotropic trace graph now promotes to a
closed global Fourier-modal realization on this same flat half-cylinder. Two
opposite-component graphs give distinct closed domains, and an explicit
bounded coflip-compatible deformation has a decaying zero mode in one but not
the other. The minimal graph closure remains the common extension-stable core;
the new theorem adds nonminimal closed domains without selecting one. Strict
massless extension dependence and every physical/positivity claim remain open.

## Continuation update — regular-boundary polarization verdict

The stronger boundary question is now classified at pointwise trace grade in
`explorations/b5-boundary-extension-verdict-2026-08-21.md`. The non-null
rank-1920 Green form has inertia `(960,960,0)`, and its coflip-fixed maximal-
isotropic trace polarizations form `O(960)`, with real dimension `460320` and
two components. The quadratic bulk action admits all of them and selects none;
the filed primary source remains silent.

This does not weaken the minimal realization. Its existence, common graph
domain and strict five-field admission are extension-stable. It does block any
upgrade from that minimal grade to a unique physical domain. Promotion of a
pointwise polarization to a closed global ultrahyperbolic realization is the
next analytic discriminator.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the repository-owned standard strict B5
Rarita--Schwinger BV expression on one explicit flat complexified `(9,5)`
product end. It is not Weinstein's unreleased cyclic two-connection action,
the graph-mixing Stage-B family, the K77 boundary campaign, the actual global
geometry of `Y=Met(X)`, or a physical Hilbert-space realization.

```gu-typed-objects
result: the strict B5 folded expression has one common minimal closed coflip-compatible realization on the flat non-null product end and therefore passes the literal five-field ingress contract at that declared grade
carrier: L2 sections of U0 plus U1 with fibre ranks 128 plus 1792 over M_plus=[0,infinity) times T13 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: auxiliary positive L2 topology for graph closure together with the program-native (9,5) Krein form for the formal adjoint and Green identity ON=independent-B5-curved-strict-carrier
real_structure: relative Gamma-natural antilinear coflip covering the integral base/fibre sign involution; absolute phase remains a local-system trivialization
grading: linear abelian BV ghost/field fold on the repository-constructed massless flat product end
action_owner: repository-construction quadratic strict Rarita--Schwinger action; historical source-preferred nonlinear action remains unowned
target: inclusion of the common minimal graph domain into the maximal distributional domain and strict packet ingress MAP-TYPE=inclusion
```

## Result first

Freeze the geometric model

```text
M_plus = [0,infinity)_r x T^13,
g = dr^2 + sum_(i=1)^8 dy_i^2 - sum_(i=9)^13 dy_i^2.
```

Use the periodic spin structure and the positive unit conormal `n=dr`. The
tangential torus has signature `(8,5)`, so the ambient product has the exact
`(9,5)` B5 signature. The Gamma-natural relative coflip covers the integral
coordinate sign involution induced by `t=N eta`. Because `t n=n`, it fixes
the half-cylinder, its boundary and its non-null normal. Integral coordinate
signs preserve the torus lattice and periodic spin structure.

Let `D_0` be the already-constructed folded strict expression on

```text
C = C_c^infinity(interior(M_plus); U0 plus U1)
```

inside an auxiliary positive `L2` completion. The auxiliary Hilbert metric is
used only to define graph closure; the formal adjoint and Green form remain
the program-native Krein objects. Define

```text
D_min = closure(D_0),
Dom(D_min) = completion of C in ||u|| + ||D_0 u||.
```

Then `D_min` is a densely defined closed operator. This is a genuine closed
unbounded-operator realization, not a relabeling of the formal compact-core
calculation.

## Why the closure exists

The prior strict action gives `D_0^formal=-D_0` in the no-`i` convention.
The same compact-interior core `C` lies in the Hilbert adjoint domain: for
`u,v in C`, integration by parts has no boundary contribution and produces a
smooth compactly supported section. Since `C` is dense, `Dom(D_0^*)` is
dense. The elementary closability theorem therefore applies: a densely
defined operator is closable exactly when its adjoint is densely defined.

No ellipticity, hyperbolicity, energy estimate or Bär--Ballmann theorem is
used. That is load-bearing because the tangential signature is
ultrahyperbolic and the generic elliptic boundary literature does not cover
this ambient object.

Because the formal expression is anti-adjoint on the same core,
`closure(D_0^formal)=-D_min`; the formal adjoint expression therefore has
the same minimal domain.

## Commonality under lower-order terms

Let `M` be any bounded zero-order bundle endomorphism. On the common core,

```text
||u|| + ||(D_0+M)u|| <= (1+||M||)(||u||+||D_0 u||),
||u|| + ||D_0 u|| <= (1+||M||)(||u||+||(D_0+M)u||).
```

The graph norms are equivalent, so their completions are the same and

```text
closure(D_0+M) = D_min + M,
Dom(closure(D_0+M)) = Dom(D_min).
```

Thus the minimal domain is common to the strict massless expression and every
bounded lower-order deformation. On the flat Ricci branch itself the action
closure selects `alpha=m=0`; this artifact does not pretend that the flat
metric realizes a nonzero-curvature Einstein branch.

## Coflip compatibility

The product involution and its Gamma-natural fibre lift map `C` onto itself.
The prior exact covariance gives, on the core,

```text
C_fold overline(D_0) C_fold^-1 = D_0
```

for the real massless branch. An antiunitary graph isometry maps Cauchy
sequences to Cauchy sequences, so it extends to `Dom(D_min)` and preserves
the closed graph. Changing the absolute coflip trivialization multiplies the
lift by `-1` and changes neither the core nor its completion. The same common
domain also carries conjugate bounded deformation pairs, although only the
massless member is geometrically action-closed on this flat model.

## Five-field packet consequence

The strict action-owned branch now supplies all five fields:

1. the actual carrier induces the vector-spinor Krein stage pairing and its
   relative slot phases, up to the irrelevant overall scale;
2. the coflip is Gamma-natural and antilinear, with all relative phases equal
   and only the absolute local-system trivialization left conventional;
3. the formal sign is `ANTI` at principal-symbol/action-closed grade;
4. the program-native Green coefficient is
   `B_n=[[0,A_n^vee],[A_n,K_n]]`;
5. `Dom(D_min)` is one common closed coflip-compatible domain on the named
   end.

The fail-closed certificate admits this strict packet and continues to reject
missing fields, a positive-Hilbert Green substitution and domains that are
not closed, common to the formal adjoint, or symmetry-compatible.

This does not normalize the separate graph-mixing full-nine Euler family.
Its multiplicity Gram remains `EXTERNAL-VIA-GRAM`; it has no admission by
inheritance from the strict branch.

## Hostile boundary: what was not constructed

The minimal domain is deliberately smaller than any boundary-polarized
self-adjoint realization. It supplies no maximal-isotropic trace subspace,
maximal extension, self-adjointness, maximal dissipativity, Fredholm estimate,
Calderon projector, boundary spectrum or scattering theory. The adjoint of
the minimal realization is the maximal realization, not the minimal one in
general; “formal adjoint on the same core/domain” must not be rewritten as
“operator self-adjoint.”

The null conormal radical from the prior result is untouched. The chosen
boundary is non-null, and compact-interior minimal closure simply excludes
boundary traces; it does not quotient or cure characteristic classes. No
global cohomology, physical state space, source action, particle result or GU
verdict follows.

## Reproduction and continuation

`tests/channel-swings/b5_flat_product_minimal_domain_probe.py` passes `38/38`.
It replays the exact non-null inverse, checks the product/coflip geometry,
certifies the graph-norm equivalence argument, admits the complete strict
packet and rejects adverse domain and Green substitutions.

The literal minimal-domain ingress gate is closed. Any next B5 domain work
must name the stronger endpoint it needs. The most informative continuation
is `B5-BOUNDARY-POLARIZED-EXTENSION-VERDICT`: either supply a source/action-
owned maximal-isotropic polarization and analyze its closed realization, or
prove downstream verdict stability across the admissible extension moduli.
That is a stronger question than the five-field contract and is not smuggled
into this result.
