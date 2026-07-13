---
title: "A9 -- post-A8 background inventory"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "POST_A8_INVENTORY_CURRENT; RPERP_AND_AMBIENT_ASSEMBLY_STILL_OPEN"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "explorations/threads/A7-background-assembly-inventory-2026-07-13.md"
  - "explorations/threads/A8-constant-section-delta-perp-h0-2026-07-13.md"
companion_test: "tests/threads/A9_post_a8_background_inventory.py"
---

# A9 -- Post-A8 Background Inventory

Companion test: `tests/threads/A9_post_a8_background_inventory.py` (inventory gate, exit 0).

## Question

A7 made the background-assembly boundary executable before A8. A8 then computed the first open slot:

```text
Delta^perp H0 = 0
```

A9 asks a process-critical question for the next scheduled Thread A pass:

```text
What is the current computed/open boundary after A8, and what should not be duplicated?
```

## Current Computed Slots

The A9 gate records six computed or inventory-guarded Thread A slots:

| slot | current boundary |
|---|---|
| A3 shape-operator commutator | commutator piece of `Rperp_0` computed nonzero; full `Rperp_0` still required ambient projection |
| A4 ambient normal projection | ambient half computed; it does not cancel the commutator |
| A5 `Rperp_0` invariant | full commutator-plus-ambient tensor is DeWitt-non-null; actual EL insertion still open |
| A6 Simons / `Q^TF(B0)` background | trace-free Simons stress vanishes; remaining background terms still open |
| A7 background inventory | pre-A8 executable slot map; useful history, no new first-variation term |
| A8 `Delta^perp H0` | normal Laplacian slot vanishes; full background EL still open |

The key update is that `Delta^perp H0` is no longer an open frontier item.

## Remaining Open Slots

The executable frontier is now:

1. `RPERP_EL_INSERTION`: the coefficient/sign/slot where A5's `Rperp_0` tensor enters the Willmore EL.
2. `AMBIENT_RY_H0_B0`: the ambient `R^Y` contribution acting on `H0`/`B0`.
3. `FULL_BACKGROUND_EL`: the complete `O(M^0) W(H)|s0` background residual.
4. `BACKGROUND_SUBTRACTED_LINEARIZATION`: the `s0 + M ds` minus `s0` leading-order computation.
5. `OQ2A_FUNCTIONAL_SELECTION`: the H-class versus II-class selection, only after the upstream assembly.

## Thread A Consequence

Future Progress passes should not recompute A8's normal-connection gate. The next honest mathematical move is
to pin the actual Willmore-EL insertion formula for `Rperp_0` and the ambient `R^Y.H0/B0` background term.

That formula/sign choice remains open. A9 does not select it.

## Honest Scope

This is a post-A8 inventory guard only. It does not compute a new first-variation term, choose a sign
convention, move OQ2-A, change claim status, change canon verdicts, alter public posture, touch Lean proof
files, touch absorbed source-action material, or touch paper surfaces.

## Grade

Process / inventory grade. It reduces duplicate scheduled work and preserves the remaining mathematical
frontier exactly enough for the next Thread A run to select a real computation instead of repeating A8.
