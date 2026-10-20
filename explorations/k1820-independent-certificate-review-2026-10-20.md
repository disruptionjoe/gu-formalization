---
title: "K1820 independent exact certificate review"
status: active_research
doc_type: verification_report
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
---

# Independent replay supports the fixed-q optimizer composition

A separate rational evaluator, importing no K1820 producer code, confirms
**79 signed-gradient terminal boxes, one positive-Hessian terminal box, and
zero unresolved boxes**. The sole positive terminal is the entire necessary
root rectangle in leaf50. This supports the new correlated Taylor and
single-convex-box argument. It is not a fresh numerical integration or a full
independent reconstruction of all predecessor certificates, and it does not
promote the theorem to canon.

Classification: `INTERNAL_STRUCTURAL_ONLY`. This is GU-independent scalar
variational mathematics; no physical pairing, action, state or observation map
is supplied. It does not alter source claims or physics-ledger verdicts.

```gu-typed-objects
result: independent exact correlated Taylor certificate replay
carrier: fixed q=1/1024 symmetric unit-variance two-radius scalar parameter chart LAYER=toy CHIRALITY=N/A
pairing: scalar Fisher objective integrated against Lebesgue measure ON=real_observation_line
real_structure: real parameters and exact rational interval endpoints
grading: normalized parameter jets through degree eight; no physical grading
action_owner: repository-construction -- scalar variational model only
target: signed-gradient exclusion and convex-root uniqueness MAP-TYPE=evaluation
```

## Independent instrument

The new `k1820_independent_certificate_audit.py` does not import the producer,
its Bernstein transform, its derivative routine, or its adaptive subdivision.
For each univariate degree five or six, it forms the Bernstein basis evaluation
matrix at rational nodes `i/n`, inverts it exactly, and reconstructs the
Bernstein coefficients of every affine-shifted monomial by interpolation.
Tensor products give the bivariate transform. Interval coefficients are
combined only after these exact linear weights are known; avoiding the
producer's intermediate interval expansion can tighten the result. Every new
enclosure lies inside the corresponding saved terminal enclosure.

The evaluator derives normalized gradient/Hessian Taylor coefficients from
factorial ratios. It applies the degree-seven or degree-six integral remainder
on the complete anchor-to-box hull, respectively, and adds whole-line tail
errors with absolute weights. The derivative combination's terms have the
same order, hence the same Taylor segment and kernel. Combining the highest
coefficients before taking absolute values is valid; treating separately
bounded tail errors as canceling would not be.

The audit verifies complete jets, ordered endpoints, payload hashes, positive
chart hulls, anchor containment, every root-polygon bounding rectangle,
nonnegative tails, and complete disjoint leaf identities. It traverses the
saved binary split tree, derives both closed child rectangles from the shared
midpoint, and independently evaluates the terminal sign or Hessian condition.
It rejects any unresolved terminal. The single convex rectangle check is
separate from checking local positive Hessians: multiple disconnected convex
boxes would not establish uniqueness.

The normalized jet/quadrature production machinery itself is **reused**.
The observation cells have width 1/4 and local radius 1/8 despite the legacy
`cell_half_width` parameter name. The proof requires the hull jet to enclose
the whole segment from the expansion point to each target point; a leaf-only
hull would not suffice. All four saved packets satisfy the geometric inclusion.
This audit does not reconstruct the numerical integral to independently prove
that the supplied jet intervals enclose its derivatives.

## Mathematical composition review

1. Previously certified derivative transport supplies necessary-root polygons,
   not existence. Its edge integrations stay within a common convex closed
   leaf; affine corner constraints follow by integrating Hessian component
   bounds along in-leaf coordinate paths. Disconnected cover gaps must not be
   bridged. This unchanged transport algorithm and its earlier controls are
   reused, not counted as newly independently replayed.
2. The new correlated certificates exclude every polygon except leaf50.
   Its whole bounding rectangle has positive transformed Hessian. The basis
   `(1,-8),(0,1)` is constant and invertible with determinant one; Sylvester's
   criterion and determinant transport apply. The verified lower bounds exceed
   `3.1587695861e-9` for A and `1.1883377946e-16` for the determinant.
3. For distinct x,y in that convex rectangle, integrate
   `(x-y)^T H(y+s(x-y))(x-y)>0`; the gradient is injective. K1787 certifies a
   stationary point inside the original leaf50. Since the polygons are
   necessary constraints for every root, that point belongs to the retained
   rectangle even though the entire Krawczyk box need not be contained in it.
4. On the compact retained union, a minimum exists. The complete exposed
   boundary and 26 value leaves lie strictly above T, while K1787's root value
   lies strictly below T. Thus a minimizing point is an interior stationary
   point and must be the unique point above. No assumption of global convexity
   on the retained union is needed. No uniqueness of higher stationary points
   in value-excluded regions follows.
5. The domain composition reuses K1760 collars and its residual compact chart,
   K1769's degree-seven outer sublevel cover, K1777's lower strip exclusion,
   K1792/K1809's first-two-slab exclusions, and K1791/K1796 pruning. The new
   audit checks exact threshold order and compares K1787's value upper endpoint
   with K1763's old candidate lower endpoint, so reuse of incumbent-relative
   collars has the correct direction. It also checks the 26/52 partition covers
   all 78 retained boxes. It does not replay the old outer-cover computations.

The connected Jz-zero graph is an additional result, not a needed premise of
this simpler proof. K1819's 114 faces and vertices belong to slab three;
K1804's 122 counts include slab two as well. These counts must not be mixed.

## Controls, findings and limits

The independent transform reproduces all monomials through degree five/six at
four exact evaluation points on a shifted interval. Analytic controls test a
rank-one quadratic's complete directional cancellation and the nonzero
highest-degree remainder of `x^8`. After the clean native replay, a missing
packet fails total leaf coverage; a maliciously rehashed hull fails anchor
containment with the intended assertion. These tests are distinct from an
independent numerical quadrature.

- **Mathematical defect found in the reviewed correlated transfer:** none.
- **Overclaim risk:** reporting this as independent validation of all numerical
  and transitive predecessor evidence, unrestricted channel optimality, or a
  uniform-q family theorem.
- **Strongest contrary construction:** disconnected root rectangles or an
  omitted terminal could defeat the uniqueness proof; the saved cover has
  neither. Positive curvature only at isolated candidates would not suffice.
- **Weakest remaining verification seam:** upstream numerical jet/tail
  enclosures and global cover proofs are reused. A full canon review must
  explicitly accept or independently reproduce those dependencies and review
  wording. This report alone does not declare that review complete.

## Reproduction and next condition

```
python3 tests/channel-swings/k1820_independent_certificate_audit.py --selftest
```

The manifest pins the original K1820 bytes and stores the exact rational
bounds. No old numerical evidence is changed. The fixed-q result needs no new
Bernstein bank. A parameter-family result would require uniform collar and
outer-sublevel bounds as q varies; a local implicit-function theorem alone
cannot exclude a remote competing minimum. Compare that concrete cost with
K1821's action-derived, degeneracy-resolving coupling question before selecting
the next calculation.
