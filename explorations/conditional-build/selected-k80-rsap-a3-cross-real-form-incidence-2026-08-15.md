---
title: "Selected-K80 RSAP A3 cross-real-form ambient incidence"
status: active_research
doc_type: exact_orthogonal_embedding_relative_orbit_and_refinement_gate
created: "2026-08-15"
registry: lab/process/selected-k80-rsap-a3-cross-real-form-incidence.json
probe: tests/channel-swings/selected_k80_rsap_a3_cross_real_form_incidence_probe.py
grade: "INDIVIDUAL EMBEDDING CLASSES FIXED; RELATIVE AMBIENT ORBIT UNDERDETERMINED; NO CANONICAL CROSS-FORM REFINEMENT"
canon_verdict_change: none
---

# Selected-K80 RSAP `A3` cross-real-form ambient incidence

## Result first

The split and `SU(2,2)` principal factors have well-typed individual ambient
models,

```text
sl4(R)  ~= so(3,3),       su(2,2) ~= so(4,2),
```

embedded in `so(7,7)` by their six-dimensional orthogonal modules. Their
support signatures `(3,3)` and `(4,2)` are ambient-isometry invariants, so the
two embedded `A3` algebras are not `SO(7,7)`-conjugate. On the full-support
open set, the image of a rank-six target operator recovers its support plane;
therefore the generic split and `SU(2,2)` target loci do not overlap.

But the individual embedding classes do **not** determine their relative
placement. Three exact models with the same two individual conjugacy classes
have respectively

```text
dim(W_split intersect W_22) = 0, 4, 5,
signature                    = (0,0), (2,2), (3,2),
algebra intersection         = 0, so(2,2), so(3,2).
```

The last two yield inequivalent candidate common faces: the banked
`A1 x A1` algebra `so(2,2)` and a larger nonregular `B2` bridge
`so(3,2) ~= sp4(R)`. Dimension and signature of the support intersection are
joint-orbit invariants, so these pairs cannot be related by one ambient
orthogonal change of coordinates.

Consequently the current owner truth does not select a canonical common target
domain. The binding's if-and-only-if gate therefore stops the symplectic step:
no cross-form moment-map equality, tautological-primitive transition or triple
cocycle is licensed yet. Choosing the `A1 x A1` face merely because it is
already banked would silently add relative-placement data; choosing `B2` would
add a different datum. The honest result is a typed relative-orbit
underdetermination, not a failed individual factor and not a global RSAP
obstruction.

## Layer 0

This is a classical real-Lie-algebra and orthogonal-incidence calculation.
“Support,” “real form,” and “common face” refer to the six-dimensional
orthogonal module of the transverse `A3` algebra. They are unrelated to
particle families, ordinary Higgs fields, chirality or quantization.

## Individual ambient classes

Let `V=R^(7,7)`. A nondegenerate six-plane `W` defines an embedded
`so(W)` in `so(V)` by extending every endomorphism by zero on `W^perp`.
Witt's theorem makes the signature of `W` the complete individual
`O(7,7)` orbit label. Thus the exterior-square real modules give one split
class with signature `(3,3)` and one pseudo-unitary class with signature
`(4,2)`.

For any full-support `A in so(W)`, `im(A)=W`. If an ambient orthogonal map
conjugated a split control to a pseudo-unitary control, it would carry
`im(A)` to `im(gAg^-1)` and hence identify a `(3,3)` plane with a `(4,2)`
plane. That is impossible. This proves generic separation structurally; the
probe supplies exact invertible controls in both supports.

## Relative-orbit controls

Use an ambient diagonal form with seven plus and seven minus axes. Fix

```text
W_split = <e1,e2,e3,f1,f2,f3>.
```

The probe realizes three `SU(2,2)` supports:

| relative model | `W_22` contribution | common signature | algebra intersection |
|---|---|---:|---:|
| transverse | four new plus, two new minus | `(0,0)` | `0` |
| four-plane | `<e1,e2,f1,f2>` plus two new plus | `(2,2)` | `so(2,2)`, dimension `6` |
| five-plane | `<e1,e2,e3,f1,f2>` plus one new plus | `(3,2)` | `so(3,2)`, dimension `10` |

For coordinate supports, the embedded algebra intersection is exactly the
orthogonal algebra of the common support. Exact span calculations give
dimensions `0`, `6`, and `10`. The pairwise algebra-span ranks are distinct,
providing a second joint-conjugacy control.

The four-plane and five-plane models contain exact shared rank-four target
operators. Hence special incidence is possible. It is not forced: the
transverse model has the same individual factor classes and zero intersection.
Nothing in the completed factor census selects among these relative orbits.

## Why the symplectic construction stops here

The predecessor correctly required an **actual ambient common target domain**
before leaf transfer or cotangent gluing. The three controls show that the
individual real-form data do not supply one unique domain:

- transverse placement gives no common factor;
- `(2,2)` placement suggests the already banked `A1 x A1` factor;
- `(3,2)` placement suggests a larger `B2` factor not selected by the current
  `A3` construction.

These are alternative relative placements, not three charts of one proved
atlas. A cotangent lift is canonical only after the base incidence map is
owned. Therefore no primitive or moment defect can honestly be evaluated yet;
there is no selected transition on which to evaluate it.

## Claim ceiling and next gate

- The split and `SU(2,2)` individual ambient embedding classes are fixed by
  support signatures `(3,3)` and `(4,2)` and are not conjugate.
- Their generic full-support target loci are disjoint.
- Special lower-support intersections are possible, with exact `A1 x A1` and
  `B2` controls.
- The relative orbit is not determined by the individual principal-factor
  census; no canonical cross-form refinement is constructed.
- This does not retract any individual `A3` factor and does not obstruct a
  future source-owned relative embedding.
- Complete nonsplit singular atlases, deeper ambient strata, zero charge and
  global all-strata RSAP remain open. The `182D` cotangent parent remains the
  all-charge fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next derive the relative six-plane placement from the actual selected `D7`
root/source embedding. It must choose exactly one joint orbit—or prove the
components disjoint—before constructing an `A1 x A1`, `B2`, or any other
common symplectic factor.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k80_rsap_a3_cross_real_form_incidence_probe.py
```

The certificate uses exact integer and rational arithmetic only.
