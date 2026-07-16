---
title: "Gate 0/1 -> Gate 3 pipeline results for the live/dark observer sheaf"
status: exploration
doc_type: results-log
created: 2026-07-15
grade: "running results log for the four-gate falsifier. Gate 0/1 = PASS (assumption-light, no dynamics). Gates 2-3 pending. Moves no ledger; asserts no identity; the generation NUMBER stays behind the unwritten source action throughout."
provenance: "Joe, chat 2026-07-15: run the reordered check; start with the assumption-light gates."
depends_on:
  - explorations/time-as-finality-crosswalk/live-dark-observer-sheaf-existence-as-issuance-2026-07-15.md
  - explorations/time-as-finality-crosswalk/ten-persona-steelman-live-dark-observer-sheaf-2026-07-15.md
runnable:
  - explorations/time-as-finality-crosswalk/gate01_observer_nerve.py
verdict: "Gate 0/1 PASS (necessary, not sufficient). Gate 2 is the discriminator and is assumption-heavy (requires positing sign-selection dynamics = the unwritten source action); it is a Joe-gated modeling fork, not auto-run."
---

# Gate pipeline results

## The reordered check (from the ten-persona synthesis, corrected)

Not four co-equal gates: **one artifact** (a dynamically-issued observer nerve) with a decisive
readout plus cheap instrumentation.

- **Gate 0/1 — b1 forced/extensive/deletion-stable (assumption-light, no dynamics).** Best-first: tests the
  oldest wall (forced-not-stipulated) with zero modeling. Read off the nerve alone.
- **Gate 2 — unique-sign vs domains under churn (THE discriminator, assumption-HEAVY).** Requires positing
  the sign-selection dynamics, which *is* the unwritten source action. Any "unique basin" result is
  conditional on the toy dynamics being faithful. Decisive in principle; model-dependent in practice.
- **Gate 3 — redundancy R_delta (records vs discardable redundancy).** Conditional tail: only meaningful if
  Gate 2 yields a unique surviving sign.

## Gate 0/1 — PASS (2026-07-15)

Script: `gate01_observer_nerve.py` (pure Python, no deps). 20 seeds x sizes {50,100,200,400} x three
issuance models. `b1 = E - V + C` (independent loops of the 1-skeleton).

Controls behaved: ring -> b1=1, tree -> b1=0.

| model | b1/N (N=50 -> 400) | frac seeds b1>0 | b1 after 20% node deletion | deletion-stable |
|---|---|---|---|---|
| ER (avg_deg=4) | 0.98 -> 1.05 | 1.00 all N | ~half retained, all >0 | yes |
| BA (m=2) | 0.94 -> 0.99 | 1.00 all N | ~half retained, all >0 | yes |
| RGG (avg_deg~6) | 1.54 -> 1.84 | 1.00 all N | ~half retained, all >0 | yes |

**Verdict: PASS.** The observer nerve carries loops that are **generic** (100% of seeds), **extensive**
(b1/N sustained as N grows -> structural, not marginal), and **deletion-stable** (survives random 20% stalk
removal, still positive and extensive). The specific "no non-vacuous home" wall that killed the spatial-`S^3`
reading (`S^3` is 2-connected, no 1-cycles) is **cleared** for the H1 / pi_1-holonomy reading.

**Honest weighting.** This is the necessary-but-easy gate. `b1 > 0` for a connected graph above the
giant-component threshold is nearly automatic; the genuine content is (i) it concretely removes the `S^3`
objection and (ii) deletion-stability held (not guaranteed a priori). It tests **H1** (1-cycles), **not** the
**H3** 2-gerbe reading E054 used (that needs the full Cech nerve with triple+ overlaps) and **not** the
sign's uniqueness. The weight of the falsification always sat on Gate 2.

## Gate 2 — PENDING (Joe-gated modeling fork)

Gate 2 cannot be auto-run without inventing the sign-selection dynamics, which front-runs the unwritten GU
source action. The modeling choice determines whether a result means anything, so it pauses for Joe. Options
recorded in the chat handoff; the guard is that whatever dynamics is chosen must be declared in advance
(not tuned to the answer) and any pass reported as conditional on that dynamics.

## Gate 3 — PENDING (conditional on Gate 2).
