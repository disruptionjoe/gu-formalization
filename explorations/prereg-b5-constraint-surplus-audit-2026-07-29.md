---
artifact_type: preregistration
status: preregistration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
probe: tests/channel-swings/b5_constraint_surplus_audit_probe.py
follows:
  - explorations/b5-phase-sum-forcing-audit-2026-07-29.md
  - explorations/b5-chirality-orientation-audit-2026-07-29.md
kill_conditions_declared_before_computation: true
canon_verdict_change: none
---

# Prereg: the constraint-surplus audit — is positing the residual a test or a fit?

## The question, and why it is not a philosophical one

Joe's argument, which this investigation takes as correct and makes measurable: when a
geometry is highly over-determined and the missing piece is small, **building the
piece that makes the rest fit is not curve-fitting.** Finding that a piece exists
at all is a result, and its shape is then interrogable.

The orthodox objection — "shaped to fit teaches nothing" — is true only when free
parameters are greater than or equal to independent constraints, because then
success is guaranteed and therefore uninformative. It is false under **surplus
constraint**, where success was not guaranteed. Standard Model hypercharges were
fit to observed particles and then found to cancel six independent anomaly
conditions with no freedom left; that surplus is why the fit was informative.

So the disagreement resolves into one number:

```text
surplus = (independent constraints expressible on the residual)
          - (free parameters of the residual)
```

Positive surplus: the posit is a **test**. Zero or negative: it is a **fit**.

This investigation computes that number instead of arguing about it.

## Free-parameter side (exact, already established)

From the phase-sum audit: the ten antilinear phases span `2^10 = 1024`
assignments but their entire effect on the real coefficient dimension is a
function of the signed sum, giving **11 observable values**. From the orientation
audit: nothing in the ledger orients any of the ten, so all ten remain free.

Free parameters: **1 integer with 11 admissible values** at the observable level;
`10` bits at the underlying level. Both are reported; the observable count is the
one that enters the surplus.

## Constraint side, and the honest risk

The eight FORCED rows are `SA-Y1`, `SA-Y7a`, `SA-G9`, `SA-C2`, `SA-C4`, `SA-U1`,
`SA-U3`, `SA-U4`. A row constrains the residual only if it is **expressible on
the same objects**. Several are visibly about other arenas — spinor-module Hom
spaces, the spin-2 sector, loop dynamics that "cannot even be POSED without the
source action."

**Expressibility proxy, declared before computation:** a FORCED row is treated as
potentially expressible iff its cited test file shares certified objects with the
B5 observer-symbol ledger. Sharing no objects means no bridge exists and the row
cannot constrain the residual without one being built. This is a **proxy, not a
proof of inexpressibility**, and will be reported as such.

## Pre-registered terminal outcomes

- **`SURPLUS-POSITIVE`** — two or more independent constraints are expressible
  and rank exceeds free parameters. The posit is a genuine test; enumerate and
  report survivors.
- **`SURPLUS-UNCOMPUTABLE`** — fewer than two FORCED rows are expressible on the
  residual. The meter reads *unknown*, not *low*. Joe's epistemics stand; the
  check simply cannot run yet, and the reopener becomes precise: **make one
  FORCED row expressible against the phase sum.**
- **`SURPLUS-NEGATIVE`** — constraints are expressible but fewer than the free
  parameters. Positing would be accommodation with freedom to spare, and the
  orthodox objection would apply *in this instance*.

## Kill conditions, declared before computation

1. If the residual's free-parameter count does not reproduce **11 observable
   values from 1024 assignments**, the input disagrees with the prior two runs
   and the audit aborts.
2. If the expressibility test cannot distinguish a **planted expressible row**
   from an inexpressible one, the test cannot fire and the investigation is void.
3. If any row is classified expressible **without** a named shared object, the
   classification is unsound and that row is voided.

## Controls, positive first

- **P1** reproduce 1024 assignments and 11 observable values.
- **P2** reproduce the certified ledger object inventory.
- **N1** a planted row citing a B5 test must classify as expressible.
- **N2** a planted row citing an unrelated test must classify as not expressible.

## What this investigation cannot earn

It cannot freeze a packet field, select a phase, build an operator, or establish
that the source action is constructible. A `SURPLUS-UNCOMPUTABLE` outcome is
**not** evidence against Joe's argument — it locates precisely what is missing
for that argument to become runnable, which is a bridge, not a proof.
