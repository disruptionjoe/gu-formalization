---
artifact_type: hostile_review
created: 2026-08-14
target: explorations/conditional-build/selected-k77-sr1c-parallel-two-jet-qualification-gate-2026-08-14.md
verdict: SURVIVES__SHORTCUT_REJECTED_WITHOUT_REJECTING_PARALLEL_CANDIDATE
---

# Hostile review: SR-1C parallel-two-jet qualification

## Verdict

`SURVIVES__SHORTCUT_REJECTED_WITHOUT_REJECTING_PARALLEL_CANDIDATE`.

The gate correctly separates simple-root rigidity of the scalar amplitude from
the still-unconstructed second field jet. It rejects only the inference from a
zero derivative of the restricted fourteen-cell value to a zero spatial first
jet of the local Euler momentum.

## Strongest attacks

### The branch polynomial forces every derivative to vanish

Rejected. Square-free rigidity forces `dt=0`. The field first jet includes the
independent symmetric `DT` correction and moving geometric coefficients; their
spatial derivatives are not coordinates of the quadratic root algebra.

### The fourteen serialized coefficients are the complete local operator

Rejected. They are values after the action equation and the correction have
been substituted. The unreduced Euler reconstruction retains the exact
rank-195 correction map and has nonzero differential `d_s p=A`.

### The planted live response disproves a parallel solution

Rejected. The planted column changes the differentiated action row. It is a
determinacy control showing that zero cannot be inferred from point data, not
a compatible two-jet or a no-go theorem.

### Parallel DeWitt curvature should automatically parallelize the field jet

Rejected as an inference. `nabla R=0` is a property of the canonical vertical
curvature module. The nonzero-`T` field, its symmetric first-jet correction and
their Ricci/Spencer identities require their own explicit second-jet witness.

### The required successor is too broad

Rejected. Each listed check is load-bearing: differentiated action and Bianchi
rows enforce prolongation, Ricci/Spencer enforces field-jet compatibility,
local Euler differentiation prevents restriction-before-differentiation, and
the adjoint contraction produces the claimed primitive row.

## Remaining exposure

The qualification does not compute the compatible second-jet solution space or
the rank of its image in `D_B^!p`. A genuine parallel witness could still make
that image zero. Conversely, a compatibility obstruction or a forced nonzero
primitive row could kill one or both roots. Both outcomes remain open.
