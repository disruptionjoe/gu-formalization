---
title: "A7 -- background assembly inventory"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "INVENTORY_GATE_ADDED; FULL_BACKGROUND_EL_STILL_OPEN"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "explorations/threads/A3-constant-section-normal-curvature-2026-07-12.md"
  - "explorations/threads/A4-constant-section-rperp-ambient-projection-2026-07-12.md"
  - "explorations/threads/A5-constant-section-rperp-invariants-2026-07-12.md"
  - "explorations/threads/A6-constant-section-simons-stress-2026-07-12.md"
companion_test: "tests/threads/A7_background_assembly_inventory.py"
---

# A7 -- Background Assembly Inventory

Companion test: `tests/threads/A7_background_assembly_inventory.py` (inventory gate, exit 0).

## Question

A6 left the Thread A background computation in a useful but fragile state: several constant-section slots are
now computed exactly, but the full higher-codimension Willmore first variation is still not assembled.

A7 asks a narrower operational question:

```text
Which slots are actually computed, and which slots still block W(H)|s0 and the background-subtracted
M-linearization?
```

This is an inventory gate, not a new geometric computation.

## Computed Slots Now Guarded

The A7 test records four computed constant-background slots with companion tests and notes:

| slot | current boundary |
|---|---|
| A3 shape-operator commutator | commutator piece of `Rperp_0` computed nonzero; full `Rperp_0` still required ambient projection |
| A4 ambient normal projection | ambient half computed; it does not cancel the commutator |
| A5 `Rperp_0` invariant | full commutator-plus-ambient tensor is DeWitt-non-null; actual EL insertion still open |
| A6 Simons / `Q^TF(B0)` background | trace-free Simons stress vanishes; remaining background terms still open |

The gate checks that each slot has a live companion test and exploration note under the Thread A surface.

## Open Slots Kept Explicit

A7 also records the six slots that remain open before any honest full background conclusion:

1. `Delta^perp H0`: normal-connection Laplacian of the constant-section mean-curvature vector.
2. `Rperp_0` EL insertion: the coefficient/sign/slot where A5's tensor enters the Willmore EL.
3. Ambient `R^Y.H0/B0`: the background ambient-curvature term acting on the constant-section objects.
4. Full `W(H)|s0`: the complete `O(M^0)` background residual.
5. Background-subtracted `M`-linearization: `W(H)|s0+M ds - W(H)|s0`.
6. OQ2-A functional selection: H-class versus II-class source-action selection.

This preserves the ordering implied by A6: do not jump from A3-A6 to OQ2-A.

## Thread A Consequence

The immediate value is collision control for future hourly runs. A future Progress pass should pick one open
slot above, not repeat A3-A6 and not claim that the full first variation is closed.

The highest-information next computation remains small and local:

```text
compute Delta^perp H0, then assemble how the A5 Rperp_0 tensor and ambient R^Y.H0/B0 terms enter W(H)|s0.
```

Only after that does the background-subtracted `M`-linearization become honest.

## Honest Scope

A7 does not compute a new first-variation term and does not change the scientific status of Thread A. It only
turns the computed/open boundary into an executable guard.

No claim status, canon verdict, public posture, Lean proof surface, paper surface, or absorbed source-action
surface changes.

## Grade

Process / inventory grade. It improves run discipline and reduces duplicate or premature closure risk. The
underlying A3-A6 computations retain their own grades.
