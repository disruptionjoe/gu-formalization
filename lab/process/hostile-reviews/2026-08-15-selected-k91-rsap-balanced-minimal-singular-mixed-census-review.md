---
title: "Hostile review: K91 balanced minimal-singular mixed census"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k91-rsap-balanced-minimal-singular-mixed-census-2026-08-15.md
created: "2026-08-15"
verdict: PASS_COMPLETE_CENTRALIZER_9_MIXED_STRUCTURAL_LOCUS__CENTRALIZER_AT_LEAST_11_AND_ZERO_NEIGHBORHOOD_OPEN
---

# Hostile review

## A few convenient singular examples mistaken for exhaustion attack

The census derives the first singular layer from centralizer excess, rather
than selecting examples. Exhaustion of every GL/U partition through
multiplicity seven leaves only `[d,1]` at excess two. The orthogonal zero-
primary formula leaves only `(2,2)` and `[2m-3,3]`. Loxodromic excess is even
after realification and starts at four. These mechanisms are disjoint.

## Singular semisimple wall silently omitted attack

K91 counts mixed configurations only. It does not count a purely semisimple
wall as mixed. That locus is nevertheless already in the image: every real
semisimple element belongs to a real Cartan and K88 places every real Cartan
class in the balanced complement. The stated `714` is therefore not padded
with earlier semisimple rows.

## `[1,1]` is not mixed attack

Correct locally: the internal nilpotent on a repeated `[1,1]` primary is
zero. Such a collision enters K91 only when another regular primary has a
nonzero nilpotent part. The K90 predecessor families enforce that predicate.

## Imaginary sign characteristics erased attack

Both signs on the long chain and singleton are retained. The `378`
pure-imaginary configurations and all corresponding local collision controls
keep this data even when coarse form signatures coincide.

## Equal eigenvalues invalidate the reversing involution attack

Anticommutation is a matrix identity and does not require spectral
distinctness. The probe explicitly sets the two selected parameters equal and
checks `RX+XR=0`, `X^TQ+QX=0`, orthogonality and balanced restricted signature
on every assembled configuration.

## Zero-primary grading chosen to hide a fixed centralizer attack

The probe tests all `61` signed and graded local zero-primary controls. It
reports the adverse controls rather than discarding them silently: `30` are
nonoptimal. The remaining `31` have exactly one fixed centralizer direction,
every signed row has at least one such choice, and the global balanced search
then succeeds for all `124` zero-primary configurations.

## Local ranks extrapolated without a decomposition theorem attack

Distinct remaining primary polynomials are coprime, so their centralizers
split orthogonally. K90 certifies their regular centralizers as moving. K91
certifies the unique singular primary has centralizer excess two split one
fixed and one moving. Therefore the global centralizer is `9D`, its fixed part
is `1D`, and the moment rank is `91-1=90`.

## Structural configurations called adjoint orbits attack

The artifact explicitly calls `714` a signed structural count. Continuous
spectral parameters remain continuous. The coverage statement concerns every
canonical structural configuration and its parameter family, not a finite
number of individual adjoint orbits.

## First singular layer implies zero neighborhood attack

False. Higher partition excess, simultaneous collisions and higher-rank
semisimple centralizers produce mixed strata with centralizer dimension at
least `11`. Until those pass, one missed conic orbit still kills the balanced
horn's zero-neighborhood claim.

## Verdict

Accept complete centralizer-nine mixed structural coverage and sharp map rank
`90`. Advance to total centralizer excess at least four. Do not claim a zero
neighborhood, surjectivity, RSAP, source selection or physical consequence.
