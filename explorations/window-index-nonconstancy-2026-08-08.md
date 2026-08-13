---
artifact_type: exploration_result
created: 2026-08-08
status: INDEX_NOT_CONSTANT_ACROSS_THE_FREDHOLM_ADMISSIBLE_SET__NATURAL_PAIR_BLOCKED_ON_AN_UNENUMERATED_ROOT_SET
grade: "ANALYSIS over filed data, with an exact arithmetic check of the window
  structure. The multiplicity argument is definitional -- an indicial root is a
  delta where the indicial family fails to be invertible, so its kernel is
  nonzero -- and is not a numerical multiplicity computation. No multiplicity is
  computed here and none is filed."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/five-lens-analytic-council-2026-08-08.md
---

# The window index is not constant, and the natural pair is blocked

## PRE-WAVE

1. **Fork.** The source file derives its spinor data from `Cl(9,5) ~ M(64,H)`
   (`:149`) — the **demoted comparator horn**. Multiplicities are therefore
   horn-dependent. The *existence* of nonzero multiplicity is not, so the
   structural conclusion below survives the fork while any number would not.
2. **Search space.** Finite and computed wholesale: the filed root set and the
   windows between consecutive roots.
3. **New un-owned object.** None.
4. **What dies if this succeeds.** If the index is choice-dependent, `GC-FC4`'s
   typing changes from "standard theorems do not apply" toward "the count is a
   property of the import", and `U14`'s silence becomes load-bearing rather than
   incidental.

## Result

The filed indicial roots, in units of `1/R_s`, all distinct:

```text
-9/2      = -4.500000   (continuum threshold)
-sqrt(20) = -4.472136
-3sqrt(2) = -4.242641
-sqrt(14) = -3.741657
-2sqrt(2) = -2.828427
```

The source states that **any `delta` in the interior of a window avoids all
indicial roots and the continuum threshold, giving a Fredholm operator.** So every
window interior is admissible.

An indicial root is, by definition, a `delta` at which the indicial family fails
to be invertible — its kernel is nonzero, so its multiplicity is at least one, and
crossing it changes the relative index by a **nonzero** amount.

**Therefore the index is not constant across the Fredholm-admissible set.**
Windows 1 and 2 are both admissible interiors and are separated by the enumerated
root at `delta = -2sqrt(2)/R_s`.

Combined with `U14` being `SOURCE-SILENT` — GU supplies no rule to select a
window — the index is a property of the **weight choice**, which is an import.

## What blocks the full closure

Lens 2 proposed comparing **Window 0** (`delta > 0`) and **Window 1**
(`-2sqrt(2)/R_s < delta < 0`), which the source calls the two *natural* choices.
Whether those two specifically differ depends on whether `delta = 0` is an
indicial root. That would come from

> "the discrete tau-shifted spectrum of `-Gamma^r D_tang` on the horizontal `X^4`
> part"

which the source lists among the forbidden values and **does not enumerate**.

So the general statement is established and the specific natural-pair comparison
is not. That distinction matters: a program can live with an index that varies
across exotic weights if the physically natural ones agree. It cannot live with
one that varies between its own two declared natural choices.

**The next step is therefore precise and bounded: enumerate the horizontal
tau-shifted spectrum of `-Gamma^r D_tang` and check whether `0` is in it.** That is
a finite eigenvalue computation on the horizontal part, and it converts this
partial result into either the closure or its refutation.

## Fences

- No multiplicity is computed. The argument is definitional, and any *numerical*
  index difference would additionally be horn-dependent via the `Cl(9,5)` spinor
  data.
- "Admissible" means Fredholm-admissible in the source's own sense. It does not
  mean physically selected; nothing here says which weight GU should want.
- This does not close the count row. It establishes that the index depends on a
  choice GU does not make, for at least one adjacent admissible pair.
- The continuum threshold `9/(2R_s)` inherits the `BC_1 (7,1)` reduction that
  canon records as superseded, flagged during the same session. The sign of the
  gap likely survives; the value does not. That affects the lowest window's
  boundary, not the structural conclusion.
