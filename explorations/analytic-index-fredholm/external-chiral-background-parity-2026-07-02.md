---
title: "Where the odd chiral count enters: closed/interior is forced even; the odd count is an external topological index"
date: 2026-07-02
status: exploration
doc_type: exploration_note
work_card: WC-FUNCTION-SPACE-EXT
---

# External chiral background parity (boundary/APS swing)

## Question

The v2.8 conditional theorem: the cross-chirality Krein-Dirac interior has net chiral spectral
flow 0 (chirality-balanced, 2-primary). The paper concludes the odd generation count is "external
on present evidence -- supplied by a net-self-dual chiral background." This note asks the sharp
parity question at the interface: is the odd count 2-primary-constrained too, or is the boundary /
external background exactly where an odd count can enter?

## What was computed (honest, exploration-grade)

`tests/function-space-ext/external_chiral_background_odd_count.py` (8 hard asserts, exit 0), on a
closed 1D Krein-Dirac circle:

- **Trivial and REAL-mass backgrounds (2, 4, 6 domain walls): net chiral count = 0 (EVEN).** A real
  background's mass zeros / domain walls come in opposite-chirality pairs; a closed 1D manifold
  hosts no odd net count.
- **A genuinely chiral (complex, sigma_2-channel) background breaks Krein-self-adjointness**
  (violation ~1.28) -- producing a chiral asymmetry requires leaving the interior class, exactly
  the necessary condition the interior no-go already identified.

## Finding (confirms + localizes; does NOT close)

The interior 2-primary balance is an **interior** phenomenon: the closed/interior net chiral count
is forced **even**. An actual **odd** count is a **topological index** -- an instanton / magnetic-
flux number (a 2D+ statement) or an APS boundary eta -- which is **external** to the interior
sector. That external index is **any integer** (odd or even): it is **NOT 2-primary-constrained**,
and it does **NOT single out 3**. This confirms and localizes the paper's "external on present
evidence" route to the external topological datum (instanton zero-modes, flux, K3/CY -- the
mechanisms the paper already names), and is consistent with the paper explicitly not claiming three.

## Honest scope / what remains open

This is a **confirmation and localization, not a closure.** A clean numerical demonstration that
the external datum genuinely carries an odd count needs a **2D magnetic-flux Dirac** (index = flux
number, e.g. flux 1 -> one chiral zero mode) or a proper **APS boundary-condition** setup -- the
1D closed model provably cannot host it (the winding-mass is gapped; interval Dirichlet BC pair the
wall mode away). That 2D/APS computation is the genuine remaining analytic frontier of
WC-FUNCTION-SPACE-EXT. No paper edit, no `CANON.md` promotion, no claim-status change: this is an
exploration-grade parity note that supports (without strengthening beyond) the existing "external"
framing. The v2.8 conditional interior theorem stands; the APS/end + family-index residual remains
open.
