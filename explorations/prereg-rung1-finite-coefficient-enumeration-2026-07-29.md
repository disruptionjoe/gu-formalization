---
artifact_type: preregistration
status: preregistration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
probe: tests/channel-swings/rung1_finite_coefficient_enumeration_probe.py
implements: lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md
kill_conditions_declared_before_computation: true
canon_verdict_change: none
---

# Prereg: Rung 1 — the finite coefficient enumeration

## Why this, now

`CURRENT-STATE.yaml` (2026-07-26) names two options and this is the bounded one:

> Build a target-blind dynamical source/topological selector **or complete the
> Rung-1 finite coefficient enumeration** before mirror or exactness testing

It also builds a bridge the constraint-surplus audit found missing: a finite
coefficient space is a place where a forced condition **can** be expressed.

## The model, fixed before any computation

```text
H_toy = (T (x) E+)  +  (T (x) E-)  +  X,        dim T = 3
```

with declared grading (chirality), a Krein form that is **purely
cross-chirality** (the GU-native structure, not a positive Hilbert pairing), a
mirror involution, a real source coordinate `phi`, and a finite operator
`D(phi)`.

`X` is the completion sector carrying its own grading, so the whole carrier is
vectorlike unless a declaration says otherwise. Its dimensions are a **declared
input**, varied as a control, never tuned toward a target.

## Construction fork (per `GEOMETER-VS-PHYSICS-OBJECTS.md`)

The Krein pairing is program-native and cross-chirality. A positive-Hilbert
pairing is run only as an explicitly typed hostile control and may never
substitute. The triplet is **supplied**, per the ladder's own statement that any
result here "would still inherit the factor of three from the located triplet."

## The binding discipline

**Enumerate the symmetry-permitted coefficient space FIRST, then compute what
indices it can produce.** Searching the space for a matrix that yields a
favourable answer, and reporting that matrix, is the failure mode this rung
exists to avoid. The enumeration is target-blind by construction: the coefficient
space is fixed by the declared symmetries alone.

## The four questions (from the ladder, unmodified)

1. Can a source coordinate open a protected gap for the mirror sector **without
   setting a rank-three projector by hand**?
2. **Which term first breaks the index-zero pairing?**
3. Does the selected subspace remain stable under admissible perturbations?
4. Is the result **global index three** or only **accessible rank three**?

## Pre-registered terminal outcomes

- **`COEFFICIENT-BREAKS-PAIRING`** — some symmetry-permitted term changes the net
  chiral index away from zero at fixed grading. Report which term, first.
- **`GRADING-ONLY`** — no permitted coefficient changes the index; only an
  unbalanced grading does, and that is a **field-space declaration, not an
  operator term**. This would be an exact scoped no-go and would independently
  reproduce the "Krein-isometric moment-map source has exact net chiral index
  zero" warning from the ladder's own preamble.
- **`GAP-WITHOUT-PROJECTOR`** / **`GAP-NEEDS-PROJECTOR`** — separate axis,
  reported independently of the index outcome.

## Kill conditions, declared before computation

1. If the enumerated coefficient space is **empty**, the declared symmetries are
   inconsistent and the model is void.
2. If the index is not integer-valued and grading-determined on the **positive-
   Hilbert hostile control**, the index computation is wrong and the investigation is void.
3. If a **planted unbalanced grading** does not move the index, the index
   estimator cannot detect what it must and the investigation is void.
4. If any reported matrix was found by searching for a favourable index rather
   than drawn from the pre-enumerated space, the result is void by construction.

## Controls, positive first

- **P1** the coefficient space is nonempty and its dimension is reported.
- **P2** exhaustive or dense sampling of that space, stated which.
- **N1** planted unbalanced grading must move the index (kill 3).
- **N2** positive-Hilbert hostile control must give the same grading-determined
  index, isolating what is genuinely Krein-specific.

## What this investigation cannot earn

Not locality, anomaly inflow, a physical boundary, GU-native operator status, a
derivation of three, or any packet field. Per the ladder, at most an exact
algebraic feasibility theorem or a scoped no-go.
