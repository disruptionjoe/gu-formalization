---
title: "K1834: characteristic cones, locality and compatible lower-order evolution"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: corrected compressed constant-coefficient fixture only; no source action, physical speed or covariant quotient
---

# Two cones admit a Fourier split, with no constant pure-speed field sector

The corrected E512 fixture has two characteristic cones. They can be separated
by bounded Fourier projectors, but no nonzero invariant constant field sector
carries just one speed. A single Lorentz metric cannot describe both cones.
This is a property of the conditional compression, not a statement that GU
violates Lorentz invariance. Source descent, stationary background and physical
field identification are still missing.

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
result: characteristic variety, nonlocal sector decomposition and full compatible coefficient space
carrier: corrected E512 constant principal fixture, 32 equivalent real16 modules LAYER=toy CHIRALITY=N/A
pairing: K1832 common positive energy ON=compressed_constant_coefficient_fields
real_structure: real rational matrices; complex Fourier transform with real-field conjugation
grading: first-order principal symbol versus zero-order evolution coefficient
action_owner: repository-construction -- conditional compression, no source action
target: simultaneous cone and coefficient compatibility MAP-TYPE=evaluation
```

## 1. Reused input and the actual new question

K1822 already computes one-direction speeds and rational projectors. K1824
proves the joint algebra M8(C) on 32 equivalent real16 modules and the full
polynomial identity

```
576 A(xi)^4 - 577 |xi|² A(xi)² + |xi|^4 I = 0.
```

K1832 supplies one positive H with H A_j=A_j^T H. We reuse these exact
certificates. We ask whether the directionwise speed decomposition is a local
field decomposition, and which constant lower-order coefficients preserve it.
SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 is UNCERTAIN about
the southeast rival. SC-ACT-01/02/06 ASSERTS their action/equation claims;
SC-META-53 remains UNCERTAIN. RA-F1, AC-F1 and LT-SM8 do not change.
A compression is not an invariant restriction of the original source operator.

## 2. Full characteristic variety and the common-coordinate test

For xi!=0, H symmetry makes A(xi) diagonalizable, with eigenvalues among
+/-|xi| and +/-|xi|/24. On the unit sphere those four eigenvalues stay separated;
their multiplicities are continuous integer functions, hence constant. The
one-direction certificate therefore proves, for every xi,

```
det(tau I + A(xi))=(tau²-|xi|²)^192 (tau²-|xi|²/576)^64.
```

At xi=0 this follows directly. Each real16 module has multiplicities 6,6,2,2.
The principal determinant has two distinct irreducible quadratic factors, not
one repeated Lorentz quadratic. Nonsingular constant changes of fields or
of equation rows multiply that determinant by a nonzero constant. An invertible
common spacetime-coordinate change cannot identify distinct quadratic cones.
Zero-order coefficients cannot change the principal characteristic variety.
These statements exclude a common single-cone Dirac principal equivalence of
this fixed fixture; they do not exclude changing its derivation or quotient.

There is a stronger common-coordinate calculation. Write
G1=diag(1,-1,-1,-1), G2=diag(1,-1/576,-1/576,-1/576).
A real invertible T preserving both null cones has
T^T G1 T=alpha G1 and T^T G2 T=beta G2. A nondegenerate real quadratic in
four variables with the same null cone is proportional; this also follows
by evaluating (1,n) on the unit sphere to remove linear and anisotropic terms.
Both proportionality factors are positive by inertia. Similarity of
G1^-1 G2 and (beta/alpha)G1^-1 G2 forces beta/alpha=1, since its two positive
eigenvalues have different multiplicities 1 and3. Thus T preserves the time
line and spatial three-plane and is lambda diag(sign,R), R orthogonal.
The identity component is positive dilations times SO(3), with no boosts.
Even allowing cone permutation does not help for this determinant, whose
factor multiplicities are different. A claimed covariant physical completion
must explain how these conditional cones change, descend or acquire their
physical interpretation; no such completion is selected here.

## 3. Exact nonlocal repair and the limit of local extraction

For xi!=0 define

```
F(xi)=(576 A(xi)²/|xi|²-I)/575,
G(xi)=576(I-A(xi)²/|xi|²)/575.
```

These are complementary H-orthogonal projectors of ranks384 and128,
commuting with A(xi). Their degree-zero symbols are smooth on the sphere and
bounded, so Plancherel defines bounded orthogonal projections on every H^s
on R³. The value at xi=0 is immaterial there; on a torus assign the spatial
zero mode separately. Both ranges are invariant under the constant-coefficient
principal evolution. Fast components solve u_tt=Delta u; slow components
solve u_tt=Delta u/576. The converse wave solutions still need the first-order
constraint. All components of the full system satisfy the product of these
two wave operators. This is an exact Fourier repair of sector separation.

It is not a finite-order differential projection. For example on each
real16 block rank(F(e1)-F(e2))=8. A translation-invariant finite-order
differential operator has polynomial symbol; a bounded homogeneous degree-zero
polynomial is constant. These F,G are not constant. On R³ a distribution
kernel supported only at the origin is a finite sum of derivatives of delta,
so their kernels are not supported there. Applying a speed projector can
introduce spatial tails even though the unsplit first-order solution has finite
propagation speed. No local support statement follows for projected initial data.

There is also no alternative nonzero constant invariant *pure-speed* sector.
Any invariant real subspace for all A_j is a module for M8(C), hence a sum of
real16 simple modules. Each simple module contains both speeds with ratio
12:4. A constant invariant subspace can select multiplicity copies, not one
cone. A tempting contrary construction does exist: the intersection of all
fast eigenspaces of A(xi)² has real dimension4 in each module. But A_j takes
it outside itself (the span with its image has dimension8 for every j).
This is a concrete failure of identifying a squared-symbol subspace with a
first-order invariant field.

Local differential extraction is possible after losing invertibility:

```
wF=(576 A(partial)²-Delta I)u =575 Delta F(D)u,
wG=576(Delta I-A(partial)²)u =575 Delta G(D)u.
```

They obey the corresponding wave equations and sum to575 Delta u. Recovering
u requires the inverse Laplacian and separate zero-mode information. This is
a legitimate local derivative consequence, not a local invertible field split.

## 4. Released follow-through: all constant compatible potentials

For u_t+sum A_j partial_j u+C u=0, a constant C preserves both Fourier
sectors iff [C,F(xi)]=0 for every nonzero xi. Polynomial coefficients make
this equivalent to the finite exact system

```
[C,A_i²]=0, [C,A_i A_j+A_j A_i]=0 for i<j.             (1)
```

On one real16 module this solution space has dimension20. Its H-symmetric
and H-skew parts have dimensions11 and9. All four rational coordinate types
are checked separately. The supplied certificate gives a complete rational
basis and a nonzero H-skew member that fails to commute with some A_j.
Thus commuting with the full first-order algebra is unnecessarily restrictive
for speed preservation. This is a useful repair to that stronger hypothesis.

The32 modules are equivalent by K1824's fixed exact intertwiners. Every
ordered multiplicity pair contributes20 real parameters to(1), so the full
coefficient space has dimension20*32²=20,480. For the direct-sum reference
energy transported to identical modules, H-skewness contributes9 on each
diagonal and20 on each unordered off-diagonal pair: dimension10,208.
The corresponding H-symmetric dimension is10,272. No positivity or source
selection is implied by these parameter counts.

If C is in that H-skew space, E'=0 and the Fourier sectors are invariant:
the constant bounded perturbation -C is skew-adjoint in H and commutes with
the sector multipliers. Energy estimates still give propagation speed at
most1 for the full unsplit system, because zero-order skew terms add no
energy source. C need not commute with A(xi), so its full dispersion need not
be the free two-wave dispersion. Generic C outside(1) couples the sectors
while leaving the two principal characteristic cones unchanged. Arbitrary
nilpotent auxiliary differentials remain subject to K1832's dissipation
obstruction. No source coefficient, barred Riesz map or stationary background
has been inferred from this available class.

## 5. Verification and next decision

```
sage -python tests/channel-swings/k1834_k77_characteristic_cones.py
sage -python tests/channel-swings/k1834_k77_characteristic_cones_probe.py
```

The producer solves(1) exactly over Q; the separate probe checks modular
constraint rank against rational solution independence, reconstructs the
all-direction projector equations, and tests deliberately wrong transfers.
The inherited all-direction quartic and exact module equivalence are cited
inputs, not claimed as new tests. Written arguments establish the continuity,
Fourier/locality and common-coordinate conclusions. Reporting mutations are
separate from mathematical controls. Inline review checked the xi=0 exception,
wave-versus-first-order converse, constant versus direction-dependent sectors,
and skew-adjoint evolution versus a differential complex. No second-agent
review, novelty claim or canon promotion.

Next compare an actual supplied stationary coefficient with(1), and test
whether a source-owned observation/constraint reduction changes the characteristic
variety. The full same-background mixed variation and Riesz relation remain
unbuilt. Repeating projector existence or fitting a commuting coefficient
would not supply them. The separate scalar next-order question remains an
independent mathematics route.
