---
title: "A14 -- counter-slot normalization gate"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "PURE_TRACE_NORMALIZATION_CANNOT_CANCEL_A13_SHEAR"
depends_on:
  - "explorations/threads/A12-constant-background-coefficient-family-2026-07-13.md"
  - "explorations/threads/A13-constant-background-coefficient-supply-gate-2026-07-13.md"
companion_test: "tests/threads/A14_counter_slot_normalization_gate.py"
---

# A14 -- Counter-Slot Normalization Gate

Companion test: `tests/threads/A14_counter_slot_normalization_gate.py` (exact SymPy, exit 0).

## Construction Used

This gate stays inside the program-native GU construction already used by A11-A13:

```text
Y14 = Met(X4), with the gimmel / trace-reversed DeWitt metric on the symmetric-pair normal fiber.
```

It does not switch to a standard field-theory ambient substitute and does not inspect or promote any absorbed
source-action material.

## Question

A13 showed that the trace-free constant-background term clears only when the net full-B shear coefficient is
zero or when an exact opposite same-shape counter-slot is supplied:

```text
S = diag(3, 1, 1, 1) / 32.
```

A14 asks the narrow review question left by that result:

```text
Can a pure-trace background normalization, sign convention, or scalar prefactor cancel this shear?
```

## Exact Gate

The companion test decomposes the A11 full-B carrier as:

```text
diag(-1, 5, 5, 5) / 32
  = pure_trace_part + diag(3, 1, 1, 1) / 32.
```

The pure-trace part has zero trace-free projection. Therefore:

```text
TF(c_B * full_B + alpha * eta) = c_B * S.
```

Adding pure trace changes normalization only; it does not change the A13 shear.

Similarly:

```text
TF(beta * c_B * full_B) = beta * c_B * S.
```

Sign or scalar-prefactor choices only rescale the shear. They clear it only by making the net full-B
coefficient zero, not by canceling a nonzero trace-free term.

With a same-shape counter-slot:

```text
TF(c_B * full_B + alpha * eta + k * S) = 0 iff k = -c_B.
```

With an unconstrained generic diagonal counter and an independent pure-trace normalization term, the solution is
fixed only modulo pure trace:

```text
u0 = -c_B/8 - u3,  u1 = u3,  u2 = u3.
```

Once the counter itself is required to be trace-free, it must reduce exactly to:

```text
diag(-3 c_B, -c_B, -c_B, -c_B) / 32.
```

## Thread A Consequence

Future OQ2-A/source-action branches cannot clear the A13 review point by saying only "background
normalization," "sign convention," or "prefactor choice." The branch must state one of these load-bearing
conditions explicitly:

| branch behavior | A14 consequence |
|---|---|
| no net full-B ambient coefficient | trace-free background clears at this gate |
| nonzero net full-B coefficient | A13 shear survives, up to sign/prefactor |
| background-subtracted/counterterm branch | it must supply exactly the opposite A11 shear shape |

If a branch includes both a pure-trace normalization term and a diagonal counterterm, the diagonal counter is
determined only modulo that pure-trace freedom until the branch declares the counterterm itself trace-free.

## Honest Scope

A14 is a review-boundary gate, not the full higher-codimension Willmore first variation. It does not choose
OQ2-A, source-action supply, `c_W`, final sign, background subtraction, the `M`-linearization, claim status,
canon verdicts, scientific status, or public posture.

## Grade

Computation-grade for the algebraic normalization-vs-counter distinction implied by A11-A13. Structural only
for implications to the actual source-action/OQ2-A branch, which remains unbuilt and unselected.
