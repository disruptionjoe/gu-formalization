---
title: "Hostile review: split-A3 nonsemisimple transition atlas"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k78-rsap-a3-nonsemisimple-transition-atlas-2026-08-15.md
created: "2026-08-15"
verdict: PASS_WITH_OTHER_REAL_A3_FORMS_AND_GLOBAL_RSAP_OPEN
---

# Hostile review

## Exhaustion attack

Listing the partitions of four alone would miss the two mixed-eigenvalue
families and could double-count the `2+2` primary exchange. The certificate
enumerates partitions inside all real eigenvalue-multiplicity patterns and
quotients the exchange of equal-multiplicity primaries. That produces exactly
five singular nonsemisimple families. It separately weights irreducible
quadratic primaries by real degree two; every nonsemisimple complex-primary
case has minimal-polynomial degree four and is regular. The exhaustion claim
passes.

## Rank attack

Target centralizer dimension alone does not determine the moment differential.
The relevant defect is the intersection with the moving space for the selected
symmetrizer. The artifact computes both. The five pairs are

```text
(dim Z_sl4, dim Z_m) = (5,4), (7,5), (9,6), (5,4), (5,4),
```

giving factor ranks `14,13,12,14,14`. After adding the common leaf and zero
coordinates, every row saturates its pointwise `98D` bound. There is no hidden
rank failure in these representatives.

## Transition attack

An algebraic cocycle among arbitrary normalization matrices would not prove
that the corresponding target strata overlap. The artifact does not make that
claim. It constructs exact regular approach arcs in each moving fibre and
exact nilpotent-scaling paths to the banked semisimple or origin controls.
Those paths supply the admitted incidences. The rational congruences then show
that their coordinate changes are restrictions of the same global principal
cotangent factor. All pairwise primitive identities and triangular products
close exactly.

## New-model attack

Surjectivity from the predecessor alone was insufficient: a singular value
could still have exhibited the wrong pointwise rank or a transition-potential
defect. Both have now been checked. “No new local model” is therefore justified
inside this split-`A3` factor. It is not a global statement about deeper
`so(7,7)` strata, zero charge or other `A3` real forms.

## Comparator and same-sign guard

Nothing here revives the ordinary Higgs, family-index or chirality comparators.
They are outside this classical moment-map lane. The same-sign `SL2/SO2`
factor is also not rescued: it remains a partial hyperbolic sheet and is never
used as a locally surjective wall chart.

## Verdict

Accept the five-family exhaustion, exact pointwise rank schedules and complete
split-`A3` nonsemisimple cotangent transition closure. Permit the successor to
enter the other real `A3` forms. Keep deeper ambient strata, zero charge and
global all-strata RSAP open.
