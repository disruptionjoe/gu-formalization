---
artifact_type: exploration_result
created: 2026-08-08
status: TWO_INDEPENDENT_OPEN_PROBLEMS_REDUCE_TO_ONE__WINDOW_DECIDER_IS_THE_COUNT_CHAIN
grade: "REDUCTION, exact at each step. Step 1 is algebra on the filed indicial
  family and is exact. Step 2 is the standard index-kernel inequality. Step 3
  cites M-C1, verified the same day against the repository's own certificate. No
  index, kernel dimension or spectrum is computed here, and the artifact's value
  is the reduction, not a number."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/window-index-nonconstancy-2026-08-08.md
---

# The window-index decider and the generation-count chain are one question

## The chain

**Step 1 — exact.** The b-parametrix file writes the indicial condition as
`(i lambda - delta) psi = -(Gamma^r)^{-1} D_tang psi`, and `Gamma^r` is invertible
because `(Gamma^r)^2 = +1` at the dilaton end. Therefore

```text
delta = 0 is an indicial root  <=>  0 in spec(-Gamma^r D_tang)  <=>  ker D_tang != 0.
```

**Step 2 — standard.** `ind D = dim ker D - dim ker D*`, so a nonzero index is a
*sufficient* condition for the kernel this needs.

**Step 3 — and here it meets today's other result.** The repository computes the
horizontal index as `ind_H = A-hat(K3) * rank = 2 * 4 = 8`. `M-C1`, verified
2026-08-08, establishes that the `A-hat`-times-rank form of the bulk term is valid
**only when `ch_2` of the twisting bundle vanishes** — and the repository's own
certificate reports `ch2(S_X)[K3] = -5376`, nonzero.

So the index *value* is not established, a corrected index could in principle
vanish, and Step 2's sufficient condition is unavailable.

## The result

```text
delta = 0 is a root  <=>  ker D_tang != 0  <=  ind != 0  <=  the index formula
                                                            ^^^^^^^^^^^^^^^^^^
                                              exactly the chain M-C1 showed broken
```

**The window-index decider and the generation-count chain are the same question.**
Both hinge on whether the horizontal twisted Dirac operator has a kernel, and both
are blocked at the same `A-hat`-times-rank step.

This is not vicious circularity — it is informative. Two problems the repository
records as independent, one analytic (which weight window, `U14`) and one
arithmetic (the generation count, `16 + 8 = 24`), reduce to a single object.

## Why that is worth more than a conditional answer

The tempting move was to note that `A-hat(K3) = 2` is an exact topological fact,
conclude `ind != 0`, hence `ker != 0`, hence `delta = 0` is a root, hence the two
natural windows are separated, hence **the count is a property of the import and
the row closes as malformed**.

That conclusion is not available, and the reason is the result. The index that
would justify it is computed by the formula whose premise is false. Taking the
shortcut would have produced a confident closure resting on the one step this
session had already shown to be broken.

Note also that `X^4 = K3` is a **working hypothesis, not canon**
(`canon/no-go-class-relative-map.md:38`), so even a valid index argument would
have been base-conditional. On a base with `A-hat = 0` — `T^4`, for instance — the
argument would not fire at all.

## What this changes

- **`U14`'s weight-window question is not independently answerable.** It inherits
  the count chain's blocker. Recording it as a separate open analytic problem
  overstates the number of distinct obstructions the program faces.
- **`M-C1`'s value goes up.** It was graded provenance-tier once its "unrecorded"
  premise proved false. It is now the gate on two problems, not one.
- **The single highest-value computation is unchanged in identity but larger in
  consequence:** establish whether the horizontal twisted Dirac operator has a
  kernel — either by computing the corrected index including the `ch_2` term, or
  by computing `dim ker` directly and bypassing the index entirely.

The second route is worth naming because it **avoids the broken formula
completely**. A direct kernel computation needs no index theorem, and it answers
both problems at once.

## Fences

- Nothing here computes an index, a kernel dimension, or a spectrum.
- Step 1 is exact and rests only on `(Gamma^r)^2 = +1` at the dilaton end and the
  filed indicial family.
- The reduction says the two problems share a blocker. It does **not** say they
  are the same problem in every respect — the count additionally needs `pi_!`,
  which the window question does not.
- `PRE-WAVE` q1: the b-parametrix file derives spinor data from `Cl(9,5)`, the
  demoted comparator horn. The reduction is structural and survives, but any
  eventual numerical kernel dimension would be horn-conditional.
