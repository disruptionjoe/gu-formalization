---
title: "Hostile review: A3 real-form principal-factor census"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k79-rsap-a3-real-form-principal-factor-census-2026-08-15.md
created: "2026-08-15"
verdict: PASS_AT_FACTOR_GRADE_WITH_CROSS_REAL_FORM_GLUING_REQUIRED
---

# Hostile review

## Real-form classification attack

Complex `A3` has five real forms, not merely split, compact and one mixed
form. The artifact includes `sl4(R)`, `su(4)`, `su(3,1)`, `su(2,2)` and
`su*(4)`. The first was closed by the predecessor. Exact bases verify the
remaining four symmetric pairs have dimensions `6+9=15` and `18D` cotangent
factors.

## Quaternionic-isotropy attack

The obvious Cartan quotient `SU*(4)/Sp(2)` is the wrong principal candidate:
`dim Sp(2)=10`, so its cotangent bundle is only `10D` and cannot cover a
`15D` regular target. The artifact correctly uses `SO*(4)`, the transpose-
skew part of the quaternionic real form. Its dimension is six and its
transpose-symmetric complement has dimension nine. Both are built directly,
not inferred from naming conventions.

## Coverage attack

Finite controls alone would not prove orbit coverage. The unitary cases use
the standard pseudo-Hermitian canonical-form theorem and exhaust the possible
Gram signatures block by block. The quaternionic case uses the quaternionic
Jordan classification in dimension two and supplies complex-symmetric
representatives for all six spectral/Jordan families. This remains
reconstruction grade because the global step imports those canonical-form
theorems; the executable certificate instantiates every block family, checks
all six full/moving centralizers and verifies the adversarial rank controls
exactly.

## Nonsemisimple-rank attack

Semisimple diagonal samples would be inadequate. `SU(3,1)` is tested on a
regular `J3+J1` control, `SU(2,2)` on a regular `J4`, and `SU*(4)` on paired
size-two non-real Jordan blocks. Each has full centralizer dimension three,
moving centralizer dimension three and factor rank fifteen. Compact `SU(4)`
has no nonsemisimple controls by normality, so that gate is vacuous rather
than skipped.

## Singular-rank attack

Every new form also has an exact centralizer-five control. In each case the
moving centralizer has dimension four, giving factor rank fourteen and the
full `82/90` target/map schedule. Thus no candidate hides a first-wall rank
defect.

## Scope attack

Constructing four factors is not constructing their common refinements. The
artifact claims no cross-real-form primitive or moment cocycle. Complete
nonsplit singular atlases, deeper ambient strata, zero charge and global RSAP
remain open. The same-sign rank-one sheet remains partial.

Even “common refinement” is conditional: shared complexification does not
prove two real subsystem strata meet inside the selected `so(7,7)` target.
The successor must classify their ambient embeddings and incidence before it
is allowed to write a transition map.

## Verdict

Accept all five real `A3` principal factors at exact factor/rank plus
canonical-form reconstruction grade. Require an explicit common domain and
cotangent transition before any cross-real-form atlas claim.
