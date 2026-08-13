---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger: lab/process/conditional-physics-ledger-v0.218.json
status: CURRENT_APPEND_ONLY_LEDGER_V0_218
---

# Conditional physics ledger v0.218

```text
Ledger v0.218 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 3 conditions closed · 1 opened · 2 remain
```

## What changed

The current conditional observer-completed `SC-ACT-04` principal action now
has an exact constrained-observer equation on the complete 16-coordinate live
response.  Writing

```text
A = x0^2 + x1^2 + x2^2 + x3^2,
B = x4^2 + ... + x15^2,
```

the mixed observer blocks vanish and

```text
C00 = diag(-8 I4, +8 I12),
C11 = C22 = C33 = -8 I16.
```

After raising an observer index, the timelike and triple spatial eigenvalues
are `-8A+8B` and `8A+8B`; their gap is exactly `-16A`.  Therefore:

- on `A>0`, the equation selects a simple **timelike line**, with constrained
  observer-fibre Hessian `-16A I3`;
- on `A=0`, the action is exactly observer-flat even when `B>0`, so it selects
  no line;
- the action is even under `u -> -u`, so it never selects a time arrow.

The co-moving Lorentz Ward identity is exact.  This is distinct from the
fixed-field constrained-`u` Euler equation; treating one as the other would
erase the selection mechanism.

## What the result does not establish

`H_u` is still a conditional observer completion, not a source-selected field.
The calculation is the exact current principal response, not yet the full
moving metric/Hodge/Shiab/projector/section contact of `SC-ACT-04`.  It neither
proves a global common line nor controls transitions through `A=0`, the arrow,
BV/domain closure, the preboundary class or the physical spectrum.

The negative Hessian sign is a local extremum statement on the observer fibre,
not a positivity or stability theorem.  No datum has been supplied.  No
verdict, residue, fork, quotient, parameter count, P1/P2/P3, canon or public
posture changes.

## Layer-0 fence

A state-dependent eigenline, an externally supplied observer field, a
co-moving Ward identity, a fixed-field Euler equation, a time orientation and
a time arrow are different objects.  The exact `A>0` line theorem does not
promote any of them into another.

Keep source `C^(32,32)+C^(32,32)` carrier halves distinct from a derived
`U(32,32)xU(32,32)` subgroup, the full `U(64,64)` parent and independent
connection fields.

## Next gate

Compose the full current `SC-ACT-04` moving metric/Hodge/Shiab/projector/section
contact and recompute its observer tensor.  Test whether the coupled physical
stress/current remains in the `A>0` stratum and supplies a global common line;
keep the `A=0` transition and the arrow as separate gates.  Only after that
should the Green/preboundary and analytic-domain work inherit the line.
