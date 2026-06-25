---
title: "Signed-Readout Record-Graph Test"
status: exploration
doc_type: specification
updated_at: "2026-06-25"
---

# Signed-Readout Record-Graph Test

This is the best bounded test for whether Time as Finality adds usable formal structure to GU.

## Target

Apply the observer-finality layer to the signed-readout boundary theorem:

> monotone provenance can coexist with non-monotone, signed, phase-sensitive, or cancellation-bearing readout.

The test asks whether a minimal causal record graph can represent signed additive evidence while keeping evidence order, causal order, finality, and scalar readout distinct.

## Construction

Define a toy system with:

- record events `e_i`,
- signs or weights `w(e_i) in {-1, +1}` or in an ordered abelian group,
- an evidence monoid `E`,
- a causal accessibility relation `<=_c`,
- a finality relation `F(O, r)` saying observer `O` can safely build on record `r`,
- a scalar readout `R(sum e_i) = sum w(e_i)`.

Then construct two cases:

1. a monotone positive-only case where evidence growth, finality growth, and readout growth align;
2. a signed case where evidence and finalized records grow while scalar readout decreases or cancels.

## Required Separation

The test must explicitly state four relations:

| relation | what it orders | must not be conflated with |
|---|---|---|
| evidence order | added input or provenance | causal order |
| causal order | accessibility or influence | scalar readout |
| finality relation | stable records an observer may build on | mathematical truth of the invariant |
| readout order | decoded semantic/scalar value | record stability |

## Sheafification Refinement

The companion bridge note (`sheafification-as-observer-finality-bridge-v0.1.md`) suggests a stricter version of this test: treat local record assignments as a presheaf over causally closed observer-accessible neighborhoods, then ask whether the associated sheaf or descent completion stabilizes provenance without forcing the signed scalar readout to become monotone.

Required separation remains:

```text
record gluing / finality through eta_F
  is not the same as
scalar readout monotonicity of R
```

If sheafification erases the negative or phase-sensitive data needed by `R`, that is not a success; it is a `Lose[K]` event that must be recorded in the loss profile.

## Success Criteria

The test succeeds if it produces a diagram and definitions where:

- `E` grows monotonically,
- finalized records grow or stabilize monotonically for the observer,
- signed readout can be non-monotone,
- the non-monotone readout is not mistaken for failed propagation,
- no primitive global time or global commit order is assumed.

## Failure Criteria

The test fails if:

- finality is defined using the temporal order it is meant to reconstruct,
- a global ledger or universal present is silently introduced,
- the scalar readout is identified with the record-finality relation,
- the model cannot represent signed cancellation without breaking record propagation,
- the result does not clarify the signed-readout theorem beyond existing PN/Jordan factorization.

## Expected Payoff

If successful, this becomes a reusable GU test object:

```text
monotone provenance
  -> observer-final record graph
  -> non-monotone signed readout
```

That would give contributors a concrete way to test whether observerse/rendering language is doing formal work.

If unsuccessful, the conclusion is still valuable: Time as Finality remains a philosophical or essay frame, not a GU formalization component.
