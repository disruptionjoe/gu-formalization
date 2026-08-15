---
title: "Hostile review: K89 balanced nilpotent-orbit census"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k89-rsap-balanced-nilpotent-orbit-census-2026-08-15.md
created: "2026-08-15"
verdict: PASS_FULL_NILPOTENT_CONE__ALL_99_POINTWISE_RANK_SATURATING__MIXED_JORDAN_AND_ZERO_NEIGHBORHOOD_OPEN
---

# Hostile review

## Strongest overclaim

Nilpotent-cone coverage is not a zero-neighborhood theorem. A neighborhood
also contains semisimple-plus-nilpotent mixed primary types. The result is
narrowed to the nilpotent cone, one complete principal rank certificate and
two explicitly non-exhaustive regular-nonsemisimple controls.

## Missed real signs attack

Enumerating complex partitions alone would be incomplete. The probe enumerates
all odd-block form signs compatible with total signature `(7,7)`: `99`
signed-form allocations over `43` orthogonal partitions. Every allocation is
tested independently. Even blocks use the required paired symplectic
multiplicity space rather than an illicit single even chain.

## Very-even and connected-group attack

There is no very-even partition of `14`, because its size would be divisible
by four. The criterion constructs an involution on each real signed-form
representative itself. Both eigenspaces are indefinite, so disconnected
orientation choices can be corrected inside the block stabilizer without
changing `R` or `X`; the result is not silently enlarged from `Spin_0(7,7)`
to an `O(7,7)`-only statement.

## Principal rank attack

Existence of an involution does not imply submersivity. The principal matrix is
checked separately against the complete `91D` `so(Q)` basis. Its ambient,
`h`, and `p` adjoint ranks are exactly `84`, `42`, and `42`, so the
`h`-centralizer is zero and the moment rank is `91`.

## Principal rank extrapolated to singular nilpotents attack

The hardened certificate no longer extrapolates. It constructs the full
`91D` orthogonal Lie-algebra basis separately for every signed diagram, splits
each basis into dimensions `42+49`, and row-reduces both adjoint maps. For
centralizer dimension `c(lambda)`, both ranks are
`(91-c(lambda))/2`, giving map rank `(189-c(lambda))/2`. Thus all `99`
connected classes—not just the principal controls—saturate the pointwise
`98D` bound; zero supplies the opposite endpoint at map rank `49`.

## Regular-nonsemisimple extrapolation attack

The `[5,1]` and `[3,1]` direct sums prove only that two mixed regular families
pass. They are planted positive controls for the next census, not an
exhaustion. Complete regular-nonsemisimple and singular mixed-Jordan coverage
remains open.

## Reproducibility seam

The main seam is the finite allocator itself. Mutation controls deliberately
admit a forbidden singleton even block, remove one odd-block sign allocation,
and demand an impossible eigenspace signature; all three change the expected
counts or create a failure. The K88 `104/104` predecessor also replays.

## Verdict

Accept complete nilpotent-cone membership and pointwise rank saturation on all
`99` connected real orbit classes. Keep zero-neighborhood coverage,
surjectivity and RSAP existence open pending the complete mixed-primary
census.
