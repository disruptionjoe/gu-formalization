---
artifact_type: exploration_result
created: 2026-08-08
status: KERNEL_NONZERO_BY_HOLONOMY_WITHOUT_ANY_INDEX_THEOREM__CLOSURE_CONDITIONAL_ON_THE_TWIST
grade: "EXACT representation theory for the untwisted statement: parallel spinors
  are counted as trivial summands of the spinor rep restricted to the holonomy
  group. The step from untwisted to tau-twisted is stated as a CONTAINMENT and is
  conditional on the twist admitting a parallel section; that condition is NOT
  checked here and is the one remaining gap."
run_id: GUH-20260808T060000Z-register-side-track
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/window-decider-reduces-to-the-count-chain-2026-08-08.md
---

# The kernel, by holonomy — bypassing the broken index formula

## Why this route

The previous artifact showed the window-index decider and the generation-count
chain share one blocker: both need `ker D_tang != 0`, and the available route to
it runs through the `A-hat`-times-rank index formula whose premise `M-C1` refuted.

**Holonomy gives the kernel directly, and never touches that formula.**

## The computation

`Spin(4) = SU(2)_+ x SU(2)_-`, with `S^+ = (2,1)` and `S^- = (1,2)`. Parallel
spinors are the holonomy-invariant ones, i.e. the trivial summands of the spinor
representation restricted to `Hol`.

```text
Hol = SU(2)_+ :  parallel in S^+ = 0,  in S^- = 2   total 2
Hol = SU(2)_- :  parallel in S^+ = 2,  in S^- = 0   total 2
```

K3 is hyperkähler, so `Hol(K3) = SU(2)` sitting as one factor. Either way the
count is **2**, concentrated in one chirality half. A parallel spinor satisfies
`D psi = 0`, so

```text
dim ker D >= 2 > 0  on K3
```

**established from holonomy alone — no index theorem, no `A-hat`, no `ch_2`.**

`A-hat(K3) = 2` agrees, and that agreement is a **cross-check only**: the `A-hat`
route goes through the refuted formula and is not what carries this result.

## Base dependence, and the repository's own two candidates both work

`X^4 = K3` is a working hypothesis, not canon.

| base | holonomy | parallel spinors |
|---|---|---|
| K3 | `SU(2)`, hyperkähler | **2** |
| `T^4` | trivial | **4** |
| generic spin `X^4` | `SO(4)` irreducible | 0 |

The repository considers K3 and `T^4`. **Both give a nonzero untwisted kernel.**
Only a generic-holonomy base would not, and the program has never proposed one.

## The remaining gap, stated rather than papered over

`D_tang` is `tau`-**twisted**, not the bare Dirac operator. What holonomy gives is
a containment:

```text
ker D_tang  ⊇  (parallel spinors) ⊗ (parallel sections of the twist)
```

So `ker D_tang != 0` follows **if the twist admits a parallel section** — immediate
for a flat or trivial twist, and not established otherwise. That condition is not
checked here.

**This is the whole remaining distance.** Everything else in the chain is now
exact:

```text
twist has a parallel section   [ONLY THIS IS OPEN]
  => ker D_tang != 0                         [containment, exact]
  => 0 in spec(-Gamma^r D_tang)              [Gamma^r invertible, exact]
  => delta = 0 is an indicial root           [filed indicial family, exact]
  => Windows 0 and 1 are separated           [both declared natural choices]
  => the index differs between them          [root crossing, multiplicity >= 1]
  => with U14 SOURCE-SILENT, GU supplies no rule to choose
  => the index is a property of the WEIGHT CHOICE, an import
```

If that one condition holds, **the count question is malformed as a GU question
and the row closes** — and it closes without ever using the index formula that
`M-C1` broke.

## What to do next, precisely

Check whether the `tau` twist admits a parallel section. That is a holonomy
question about the twist bundle, of the same kind and cost as the computation
above, and it is the last step of a chain now exact everywhere else.

Note the shape of what this achieved: the problem was blocked behind a broken
index formula, and the repair was not to fix the formula but to find a route that
does not need it. The remaining question is smaller and of a different kind.

## Fences

- The untwisted count is exact representation theory. The twisted statement is a
  containment, and its hypothesis is unverified.
- `PRE-WAVE` q1: the b-parametrix data derives from `Cl(9,5)`, the demoted
  comparator horn. The holonomy argument is about `X^4` and its spin bundle, so it
  is horn-independent; the surrounding indicial-family data is not.
- Nothing here computes `dim ker D_tang` exactly. It establishes a positive lower
  bound conditional on the twist, which is all the window argument needs.
