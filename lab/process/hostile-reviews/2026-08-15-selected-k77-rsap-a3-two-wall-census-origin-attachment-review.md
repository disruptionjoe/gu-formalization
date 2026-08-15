---
title: "Hostile review: split-A3 two-wall census and origin attachment"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k77-rsap-a3-two-wall-census-origin-attachment-2026-08-15.md
created: "2026-08-15"
verdict: PASS_WITH_NONSEMISIMPLE_TRANSITION_CENSUS_REQUIRED
---

# Hostile review

## Strongest classification attack

The four source-sign rows are not four target orbit types. Forgetting the
chosen `(2,2)` symmetrizer leaves only the `A2` and `A1 x A1` root-subsystem
orbits. Conversely, it is also wrong to erase the source-sign distinction:
the naive same-sign `SL2/SO2` face has a smaller moment image than the
opposite-sign `SL2/SO11` face. The artifact keeps both levels explicit.

## Strongest rescue attack

Routing through an opposite-sign preimage must not be described as proving
that `T*(SL2/SO2)` is surjective. It is not. Its annihilator consists of
symmetric traceless `2 x 2` matrices with determinant `-(a^2+b^2)` and misses
both elliptic and nonzero nilpotent targets. The principal `A2` and `A3`
factors survive because their zero fibres contain other base points with
alternating signatures whose wall restrictions are `SL2/SO11`. The partial
sheet remains partial.

## Strongest origin attack

Rank `85` at the `A3` origin is not an arbitrary allowed loss. The pointwise
RSAP inequality gives `s <= (98+72)/2=85`, and the principal cotangent factor
attains it because its zero-section differential has rank nine. This is an
origin attachment inside the local `A3` subsystem, not the zero covector of
`so(7,7)^*`; the common `72D` leaf is still present.

## Surjectivity attack

Regular and zero controls alone would not prove a neighborhood is covered.
The artifact supplies the missing all-Jordan symmetrizer census. Reverse
forms handle every real Jordan partition; neutral blocks handle complex pairs
and their size-two Jordan extension. All nine dimension-four real Jordan
configurations admit inertia `(2,2)`. The exact probe checks the identities.

## Cocycles and remaining scope

The four-chart cocycle is strict because every chart is normalized through
the same cotangent factor. That does not classify every nonsemisimple singular
transition inside the ambient `so(7,7)` atlas. Those overlaps, other `A3` real
forms, deeper ambient strata and zero charge remain separate gates.

## Verdict

Accept the complete two-wall target census, the exclusion of the naive
same-sign wall sheet, and the first alternating `A3` origin attachment at the
stated rank. Require the remaining split-`A3` nonsemisimple transition census
before broader singular-globalization language.
