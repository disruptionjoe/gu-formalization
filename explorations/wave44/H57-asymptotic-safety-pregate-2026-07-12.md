---
artifact_type: exploration
status: exploration
created: 2026-07-12
wave: 44
title: "H57 asymptotic-safety pre-gate: turn the elected UV-flow route into an executable contract. Result: READY_FOR_FRG_BUILD / FIXED_POINT_NOT_COMPUTED. Power counting and gravity-only AS scans are explicitly rejected as H57 results; the next H57 flow must compute beta functions for the full GU truncation, find fixed-point residuals, and count finite critical exponents while keeping Krein loop positivity separate."
grade: "exploration / executable pre-gate (tests/wave44/H57_asymptotic_safety_pregate.py, deterministic contract checks, exit 0). No beta functions or fixed point computed; no H57 verdict; no canon/status/public-posture movement."
depends_on:
  - attention/gu_priority_condorcet.py
  - explorations/wave42/renormalization-landscape-scan-2026-07-11.md
  - explorations/wave43/renormalization-carve-2026-07-11.md
  - tests/wave42/W42_power_counting.py
  - tests/wave43/renormalization_carve.py
scripts:
  - tests/wave44/H57_asymptotic_safety_pregate.py
---

# Wave 44 -- H57 asymptotic-safety pre-gate

## Question

H56 already answered the renormalization carve: GU is **RENORMALIZABLE-BUT-POSITIVITY-OPEN** at
power-counting grade, and the binding UV-completeness obstruction is loop positivity/source-action data, not
spin-3/2 power counting. The current Condorcet re-rank elects H57 as the next higher-upside UV route:

> Is GU asymptotically safe, via a non-perturbative UV fixed point for its coupling flow?

This note does not answer H57. It turns the elected flow into a small executable gate so the next swing cannot
confuse a weaker result for an asymptotic-safety result.

## Result

`tests/wave44/H57_asymptotic_safety_pregate.py` returns:

```text
H57 PRE-GATE VERDICT: READY_FOR_FRG_BUILD / FIXED_POINT_NOT_COMPUTED
Binding next move: compute beta functions for the full GU truncation, then search fixed points.
```

The gate makes three distinctions explicit:

1. **Power counting is not H57.** H56/H43 power counting is rejected as an H57 result because it has no computed
   beta functions, fixed-point residuals, or stability-matrix exponents.
2. **Gravity-only asymptotic safety is not GU asymptotic safety.** A scan that keeps only
   `dimensionless_newton_coupling`, `cosmological_coupling`, and `weyl_squared_coupling` is rejected because it
   drops the constrained RS carrier, the curvature-RS nonminimal coupling, and the Krein separation.
3. **A valid H57 work packet is not a demonstrated fixed point.** The minimal packet is ready only as a next flow
   build: operator basis and required outputs are present, but beta functions and fixed-point residuals remain
   owed.

## Minimal GU truncation required for H57

The next H57 flow must include at least:

| required object | reason |
|---|---|
| `dimensionless_newton_coupling` | ordinary Reuter-style gravitational coupling; without it there is no AS gravity flow |
| `cosmological_coupling` | needed for the gravity fixed-point surface and for comparison with the existing scale discussion |
| `weyl_squared_coupling` | GU's fourth-order/Stelle sector; the H56 pass lives here |
| `rs_ker_gamma_kinetic` | GU is not a pure-gravity theory; the constrained spin-3/2 carrier is load-bearing |
| `curvature_rs_nonminimal_coupling` | the Wave 42 AS candidacy specifically routes through curvature-fermion couplings |
| `krein_parity_separation` | AS can at most complete the coupling flow; it does not by itself prove loop positivity |

The required outputs are:

- beta-function targets for every running coupling above;
- a fixed-point search plan;
- a stability-matrix plan;
- a relevant-direction count plan;
- an explicit note separating AS coupling-flow UV completion from Krein loop positivity.

## Failure conditions for a future H57 claim

A future H57 result fails this pre-gate if it:

- cites H56/H43 power counting as an asymptotic-safety fixed point;
- runs a gravity-only truncation and calls it a GU truncation;
- omits the constrained RS carrier or curvature-RS nonminimal coupling;
- claims loop positivity from an AS fixed point alone;
- reports a fixed point without residuals for every required coupling;
- reports a fixed point without finite stability-matrix critical exponents.

## Current status

H57 is **open**. The pre-gate makes the next unit precise:

```text
Build the full GU truncation beta system -> solve for fixed points -> compute stability exponents.
```

If that flow finds a fixed point with a finite-dimensional critical surface, H57 advances. If it finds no fixed
point under the required truncation, H57 receives a real negative result. Either way, the Krein loop-positivity
question remains separate unless the source-action/S-matrix problem is also built.

No claim status, canon verdict, public posture, source-action truth, generation-count result, or H57 verdict is
changed by this wave.
