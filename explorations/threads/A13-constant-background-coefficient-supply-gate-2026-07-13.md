---
title: "A13 -- constant-background coefficient supply gate"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "TRACE_FREE_BACKGROUND_CLEARING_REQUIRES_ZERO_NET_FULL_B_OR_EXACT_COUNTERSHEAR"
depends_on:
  - "explorations/threads/A11-constant-background-ry-b0-contraction-2026-07-13.md"
  - "explorations/threads/A12-constant-background-coefficient-family-2026-07-13.md"
companion_test: "tests/threads/A13_constant_background_coefficient_supply_gate.py"
---

# A13 -- Constant-Background Coefficient Supply Gate

Companion test: `tests/threads/A13_constant_background_coefficient_supply_gate.py` (exact SymPy, exit 0).

## Construction Used

This gate stays inside the program-native GU construction already used by A11/A12:

```text
Y14 = Met(X4), with the gimmel / trace-reversed DeWitt metric on the symmetric-pair normal fiber.
```

It does not switch to a standard field-theory ambient substitute and does not inspect or promote any absorbed
source-action material.

## Question

A12 reduced the computed constant-background family to:

```text
F0 = (c_H / 8) eta + c_B * diag(-1, 5, 5, 5) / 32
```

and therefore:

```text
TF(F0) = c_B * diag(3, 1, 1, 1) / 32.
```

A13 asks the next bounded review question:

```text
What exact coefficient or counterterm condition must a future source-action/OQ2-A branch satisfy to clear this
trace-free background term?
```

## Exact Gate

The companion test proves:

```text
without an additional counter-slot:
  TF(F0) = 0  iff  c_B = 0

with a same-shape counter-slot k * diag(3,1,1,1)/32:
  TF(F0) = 0  iff  k = -c_B
```

Equivalently, an arbitrary diagonal trace-free counter must be exactly:

```text
diag(-3 c_B, -c_B, -c_B, -c_B) / 32.
```

This is the negative part of the gate: pure-trace/H-class terms cannot cancel the A11 shear, and sign or scalar
prefactor choices only scale it.

## Source-Action/OQ2-A Consequence

A future branch must state one of three things explicitly:

| branch behavior | A13 consequence |
|---|---|
| no full-B ambient slot | the A12 trace-free background term clears at this gate |
| nonzero raw full-B slot | the A11 shear survives with that sign/prefactor |
| background-subtracted or counterterm branch | the branch must supply the exact opposite A11 shear tensor |

This does not decide which branch is real. It only prevents the review point from remaining qualitative.

## Honest Scope

A13 is a coefficient-supply gate, not the final higher-codimension Willmore first variation. It does not choose
OQ2-A, source-action supply, `c_W`, final sign, background subtraction, the `M`-linearization, claim status,
canon verdicts, scientific status, or public posture.

## Grade

Computation-grade for the algebraic cancellation condition implied by A12. Structural only for implications to
the actual source-action/OQ2-A branch, which remains unbuilt and unselected.
