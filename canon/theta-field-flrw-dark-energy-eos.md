---
title: "GU Theta Field Dark Energy — FLRW Equation of State and DESI DR1 Comparison"
status: canon
doc_type: canon
promoted_from:
  - "explorations/theta-field-flrw-eos-2026-06-23.md"
promoted_at: "2026-06-23"
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: "2026-06-26"
correction_de02: "CORRECTION DARK-ENERGY-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN. The 2026-06-23 re-elevation from OPEN rested on a PROCESS MILESTONE (the FLRW Klein-Gordon integration being complete), not on support — the integration WORSENED agreement (de Sitter w_a flipped to +1.17; the >2 failure-condition fired). The only parameter-free prediction, ratio w_a/(w_0+1)=+1.17, is SIGN-INCONSISTENT with DESI (w_a=-0.75), and the sign of w_a has two UNDISMISSED candidates (frozen IC w_a>0 vs slow-roll IC w_a<0; OQ3-A unresolved). By the UNDISMISSED-CANDIDATE rule the EOS-vs-DESI verdict is OPEN. The structural EOS machinery (dynamic theta DE field; oscillating+damped two-component w(z); Result 1 algebraically exact) stays reconstruction-grade; only the data-facing verdict is OPEN. Note w_0=-0.826 'matching DESI -0.827' is a FIT (f_0=0.125 tuned), not a prediction."
prior_verdict_history: "OPEN (pre-2026-06-23) -> CONDITIONALLY_RESOLVED (2026-06-23, OQ3) -> OPEN (2026-06-26, DARK-ENERGY-02)"
verdict_change_reason_2026_06_23: "OQ3 closed by theta-field-flrw-matter-era-ode-2026-06-23.md: full FLRW Klein-Gordon integration completed. Corrected values: phi_0=0.855 rad, w_B(0)=+0.388, ratio w_a/(w_0+1)=+1.17. De Sitter ratio -1.80 ruled out (factor 2.68, sign flip). Canon re-elevated with corrected numerical values and named failure conditions. NAMED FAILURE CONDITION: OQ3-A (IC-dependence of w_a sign) is a failure condition for CONDITIONALLY_RESOLVED. The sign of w_a is IC-sensitive (8% variation; frozen vs. slow-roll ICs); whether w_a > 0 or w_a < 0 requires extending the integration to z >> z_osc with proper slow-roll ICs. If that extension reverses the sign, the DESI comparison must be repeated and the current +1.17 ratio is not the GU prediction."
correction_oq3: "2026-06-23 (theta-field-flrw-matter-era-ode): Full Lambda-CDM RK4 integration. Corrected: phi_0=0.855 rad (was 1.94), w_B(0)=+0.388 (was +0.76), coefficient in w_0=-1+C*f_0 is C=1.39 (was 1.76), ratio w_a/(w_0+1)=+1.17 (was -1.80, sign reversed). Failure condition fires: factor 2.68 > 2 from de Sitter. Sign of w_a now positive (IC-sensitive; OQ3-A needed for robust sign). OQ3-A is a named failure condition: if slow-roll ICs from z >> z_osc reverse the sign of w_a, the ratio +1.17 is not the GU prediction and the DESI comparison must be rerun. The integration is RK4 numerical with no code shown and no error bound stated; quantitative claims are reconstruction-grade only."
---

# GU Theta Field Dark Energy — FLRW Equation of State and DESI DR1 Comparison

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

> **VERDICT: OPEN (CORRECTION DARK-ENERGY-02, 2026-06-26).** This document's EOS-vs-DESI comparison is an OPEN problem, not CONDITIONALLY_RESOLVED. Its only parameter-free prediction (ratio `w_a/(w_0+1)=+1.17`) is **sign-inconsistent with DESI** (`w_a=-0.75`); the sign of `w_a` itself has two undismissed candidates (frozen-IC `w_a>0` vs slow-roll-IC `w_a<0`, OQ3-A unresolved), so by the repo's UNDISMISSED-CANDIDATE rule the verdict is OPEN. The 2026-06-23 OPEN→CONDITIONALLY_RESOLVED re-elevation was driven by a process milestone (the integration being complete), not by data support. What IS reconstruction-grade and stands: the **structural** EOS machinery — theta as a dynamic dark-energy field, the oscillating+damped two-component `w(z)`, and the algebraically-exact Result 1. The `w_0=-0.826` "match" to DESI's `-0.827` is a **fit** (`f_0=0.125` tuned), not a prediction.

> **OQ3 CORRECTION (2026-06-23, theta-field-flrw-matter-era-ode):** Full Lambda-CDM Klein-Gordon integration is now complete (RK4, 300,000 steps, z=3 to z=0). Corrected values: phi_0 = 0.855 rad (de Sitter was 1.94 rad), w_B(0) = +0.388 (was +0.76), coefficient C = 1.39 (was 1.76 in w_0 = -1 + C*f_0), ratio w_a/(w_0+1) = +1.17 (was -1.80, sign reversed). The failure condition fires: ratio changed by factor 2.68 (> 2 threshold). The de Sitter ratio -1.80 and the negative-w_a prediction are ruled out at reconstruction grade. The sign of w_a is now +1.17*f_0 > 0 (from frozen IC at z=3), but this is IC-sensitive (8% variation between frozen and slow-roll ICs). Whether w_a > 0 or w_a < 0 requires extending the integration to z >> z_osc ~ 1.85 with proper slow-roll initial conditions from attractor (OQ3-A). Result 1 (oscillating+damped regime) remains algebraically exact. Results 2 and 3 are now updated with corrected FLRW values. See `explorations/theta-field-flrw-matter-era-ode-2026-06-23.md`.

## Scope

The GU dark energy sector is the distortion field theta = pi - epsilon^{-1} B epsilon (established as divergence-free and dynamic in canon/dark-energy-theta-divergence-free.md). This document establishes the equation of state w(z) for the cosmological theta mode on an FLRW background and the comparison to DESI DR1 (2024) constraints.

## Key Inputs

1. The theta field on a cosmological background satisfies the linearized Klein-Gordon equation with effective mass M_KK (from the fiber normal Laplacian on Y14).
2. M_KK = 2*sqrt(2) * H_0 (from the lowest eigenvalue lambda_{N,1} = 8/R_s^2 of the normal Laplacian on the GL(4,R)/O(3,1) fiber with R_s = c/H_0). `[reconstruction — rc3-delta-n-spectrum-gl4r-2026-06-23.md]`
3. The GU dark energy has a two-component structure: a constant umbilic Lambda_eff (w = -1) plus a dynamical oscillating theta mode (w_B depends on phase).

## Central Results

### Result 1 — Oscillation Regime (Algebraically Exact)

M_KK = 2.83 H_0 exceeds the de Sitter Breitenlohner-Freedman bound 3H_0/2. Therefore the theta zero-mode is in the OSCILLATING AND DAMPED regime, not slow-roll.

In de Sitter background the exact zero-mode solution is:

```
B(t) = A · e^{-3 H_0 t / 2} cos(omega_osc t + phi_0)
```

where omega_osc = sqrt(M_KK^2 - 9H_0^2/4) = (sqrt(23)/2) H_0 ~ 2.40 H_0.

Oscillation period: T_osc = 2pi/omega_osc ~ 37.7 Gyr.
Damping timescale: t_damp = 2/(3H_0) ~ 9.6 Gyr.

Time-averaged equation of state (by explicit energy/pressure averaging):

```
<w_B> = 0     (matter-like, oscillating massive scalar)
```

This is an algebraically exact consequence of omega_osc^2 = M_KK^2 - 9H_0^2/4:
<p_B> = (1/4)A^2 e^{-3H_0 t} [(3H_0/2)^2 + omega_osc^2 - M_KK^2] = 0. `[exact algebra]`

### Result 2 — Two-Component Dark Energy (Reconstruction Grade, FLRW-Corrected)

GU dark energy = umbilic Lambda_eff (w = -1) + oscillating theta (instantaneous w_B depends on phase phi_0). Full FLRW integration gives phi_0 = 0.855 rad at z=0. The effective total dark energy EOS at z = 0:

```
w_0 = w_{DE}^{eff}(z=0) ~ -1 + 1.39 f_0    [CORRECTED: was 1.76 f_0 in de Sitter approx]
```

where f_0 = rho_B(z=0) / rho_{Lambda_eff}(z=0) is the ratio of dynamical to constant dark energy density.

For f_0 ~ 0.125 (corresponding to initial amplitude B_i ~ 0.98 M_Pl, Planck-scale — natural for a geometrical connection field in GU):

```
w_0 ~ -0.826    [matches DESI w_0 = -0.827 to 3 decimal places at this f_0]
w_a ~ +0.20     [CORRECTED: positive, from full FLRW frozen IC at z=3]
```

Note: the sign of w_a is now POSITIVE with frozen ICs at z=3, which is INCONSISTENT with
DESI's w_a = -0.75. This is IC-sensitive; extending the integration from z >> z_osc with
proper slow-roll ICs (OQ3-A) is required before the sign of w_a can be stated as a GU prediction.
`[reconstruction — full Lambda-CDM RK4 integration; IC sensitivity unresolved]`

### Result 3 — Ratio Prediction (f_0-Independent, phi_0-Conditional, FLRW-Corrected)

The ratio w_a / (w_0 + 1) is independent of the unknown initial amplitude f_0:

```
w_a / (w_0 + 1) ~ +1.17    [CORRECTED: was -1.80 in de Sitter approx; SIGN REVERSED]
```

The de Sitter estimate -1.80 is ruled out by factor 2.68 (> 2 threshold from OQ3 failure condition).

**Status (2026-06-23, OQ3 correction):** The corrected ratio +1.17 is positive. The corrected
ratio is f_0-independent (f_0 cancels in leading order, same algebra as before). The ratio is
phi_0-dependent; the corrected phi_0 = 0.855 rad from full FLRW integration (not 1.94 rad from
de Sitter). The sign change from negative to positive reflects that the accumulated phase in
the matter era is substantially smaller than the de Sitter estimate.

DESI DR1 measured ratio: w_a / (w_0 + 1) = -0.75 / 0.173 ~ -4.3 (negative). The corrected
GU ratio +1.17 has the OPPOSITE sign from DESI. This is the primary open question for Candidate D:
whether GU predicts w_a < 0 with proper ICs (OQ3-A).

`[reconstruction grade, FLRW-corrected, IC-sensitive sign]`

### Result 4 — Sign and Qualitative Predictions (OQ3-CORRECTED)

> **SUPERSEDED BY OQ3 CORRECTION (2026-06-23).** The original Result 4 asserted `w_a < 0`
> and claimed agreement with DESI DR1. That sign was the de Sitter estimate and is RETRACTED.
> The full FLRW Klein-Gordon integration (theta-field-flrw-matter-era-ode-2026-06-23.md)
> reverses the sign: the corrected prediction is `w_a > 0` (ratio w_a/(w_0+1) = +1.17),
> which is INCONSISTENT with DESI's w_a = -0.75 < 0. See Results 2 and 3 and FC5 (OQ3-A).

Independent of f_0, GU Candidate D currently predicts (frozen IC at z=3, IC-sensitive per OQ3-A):
- w_a > 0 (CORRECTED: was w_a < 0 in the de Sitter estimate; full FLRW integration reverses
  the sign). This is OPPOSITE to DESI DR1, which finds w_a = -0.75 < 0. Whether the GU sign
  remains positive under proper slow-roll ICs from z >> z_osc is the open question OQ3-A; if
  OQ3-A reverses the sign, the +1.17 ratio is not the GU prediction and the DESI comparison
  must be rerun (see FC5).
- Transition redshift z_osc ~ 1.85: theta begins oscillating when H ~ M_KK. For z > z_osc the
  dark energy is indistinguishable from Lambda-CDM.
- Deviation from w = -1 DECREASES with time (dark energy approaches Lambda-CDM asymptotically as B decays).

## Assumptions

1. M_KK = 2*sqrt(2) H_0 from the fiber spectrum on GL(4,R)/O(3,1) with the GL(4,R)/SO_0(3,1) restricted root system. This is under revision (A_3 vs BC_1 root system — see OQ2).
2. De Sitter approximation for the background (H ~ H_0*sqrt(Omega_Lambda) ~ const for z << 1). Full FLRW evolution including matter era at z ~ 0.3 transition is not included.
3. Minimal non-minimal coupling: xi = 0 (no additional coupling to the 4D Ricci scalar R^{FLRW}).
4. Two-component dark energy structure: umbilic Lambda_eff (constant, w = -1) plus dynamical theta.
5. B is a scalar field in 4D when the section is pulled back. If s*(theta) is spin-2, the FLRW-KG equation must be replaced.

## Known Failure Modes

**F1.** DESI DR2 or Euclid measures w_a/(w_0+1) < -3.5 at 2-sigma. This requires B_i > 3 M_Pl, unphysical in GU.

**F2.** The effective mass M_KK is not 2*sqrt(2) H_0 but something different after correcting the fiber root system from BC_1 to A_3. If M_KK >> H_0 (much faster oscillation), the phase phi(t_0) shifts significantly.

**F3.** The umbilic Lambda_eff = 0 and all dark energy comes from the oscillating theta. Then the total w_0 ~ +0.76 (kinetic-dominated oscillating scalar at the present phase), which would be strongly ruled out by DESI.

**F4.** s*(theta) is spin-2, not scalar. Then the FLRW-KG equation does not apply.

**F5.** Lambda-CDM confirmed at high precision (|w_0+1| < 0.01, |w_a| < 0.03 at 2-sigma), requiring B_i < 0.21 M_Pl.

**F6 (OQ3-CORRECTED).** A measured ratio w_a/(w_0+1) inconsistent with the corrected GU slope
of +1.17 at 2-sigma falsifies the prediction. (The original F6 cited the de Sitter slope -1.80,
now RETRACTED by the OQ3 correction; the sign reversal means DESI's own negative ratio ~ -4.3
already sits on the opposite side of the corrected +1.17 prediction. See Result 3 and FC5.)

**F7 (FIRED, OQ3-CORRECTED).** Full FLRW Klein-Gordon integration (OQ3) yielded a phase phi_0 = 0.855 rad, substantially different from the de Sitter estimate of 1.94 rad. This O(1) shift moved the instantaneous w_B at z = 0 and reversed the sign of w_a (ratio -1.80 to +1.17). This failure mode has now fired: the de Sitter phi_0 ~ 1.94 rad and the negative-w_a prediction are RETRACTED. The corrected w_0 still lands inside the DESI DR1 window at f_0 ~ 0.125 (Result 2), but the sign of w_a is now opposite to DESI and remains IC-sensitive (OQ3-A / FC5).

**F8.** The ratio w_a/(w_0+1) is not bounded away from 0 as phi_0 varies. If the full phi_0-scan (required by THETA-01/OQ5) finds that the corrected +1.17 is near a node of the ratio function, the DESI comparison is not a robust prediction and Candidate D cannot be distinguished from Lambda-CDM on this observable.

**F9.** M_KK = 2*sqrt(2) H_0 is shifted by the A_3 root-system correction (OQ2). If the corrected M_KK places the field in the slow-roll regime (M_KK < 3H_0/2), the entire two-component structure of Result 1 is overturned and Results 2-3 do not apply.

**FC5 (OQ3-A — IC-dependence of w_a sign, named failure condition).** The current ratio w_a/(w_0+1) = +1.17 was computed from a frozen initial condition at z=3 (theta-field-flrw-matter-era-ode-2026-06-23.md, RK4, 300,000 steps). The sign of w_a is IC-sensitive: the file acknowledges 8% variation between frozen and slow-roll ICs, and whether w_a > 0 or w_a < 0 requires extending the integration to z >> z_osc ~ 1.85 with proper slow-roll initial conditions from the attractor (OQ3-A). If that extension reverses the sign of w_a from +1.17 to negative, then: (a) the FLRW-corrected ratio is not +1.17 but some phi_0-dependent negative value; (b) the DESI comparison must be repeated from scratch; (c) the statement that the de Sitter ratio -1.80 is "ruled out" must be revisited because the FLRW sign could restore compatibility with DESI's w_a < 0 at a different magnitude. The numerical integration has no code shown and no error bound stated; the quantitative claims in Results 2 and 3 are reconstruction-grade only and are explicitly conditional on OQ3-A. CONDITIONALLY_RESOLVED remains the correct verdict, but OQ3-A is a named failure condition: if OQ3-A resolves with sign reversal, the core quantitative prediction changes and a new DESI comparison is required.

## The Primary Gaps

**Gap 1:** GU does not yet derive B_i (the initial amplitude) from first principles. The variational principle (Willmore energy E[s]) selects the critical section but does not specify the initial phase or amplitude of normal-bundle perturbations. Without a GU-derivable B_i, the w_0 value is a fit (f_0 = 0.11), not a prediction.

**Gap 2 (THETA-01, 2026-06-23; OQ3-CORRECTED):** The ratio w_a/(w_0+1) = +1.17 depends on the
initial phase phi_0 = 0.855 rad from the full FLRW integration (the earlier de Sitter values
-1.80 and phi_0 ~ 1.94 rad are RETRACTED by the OQ3 correction). The phase is not yet derived
from first principles, and the full phi_0-dependence of the ratio has not been computed; it is
not known whether +1.17 is a minimum, maximum, or saddle point as phi_0 varies. The sign of
w_a is additionally IC-sensitive (8% frozen-vs-slow-roll variation; OQ3-A). Until the phi_0-scan
is done and OQ3-A (slow-roll ICs from z >> z_osc) is resolved, the ratio is a conditional
estimate, not a free structural prediction.

The ratio w_a/(w_0+1) = +1.17 is the most constrainable quantity from DESI/Euclid, but it
should be cited as "conditional on phi_0 = 0.855 rad and frozen IC at z=3 (OQ3-A unresolved)"
not as "independent of initial conditions."

## Falsification Condition (Sharpened)

The GU theta-field prediction (OQ3-corrected) is falsified if:

```
w_a - 1.17 * (w_0 + 1) significantly differs from 0,
```

specifically if |w_a - 1.17 * (w_0 + 1)| > 0.5 at 2-sigma (from future DESI/Euclid data with
precision ~0.05 on w_0 and ~0.1 on w_a). The coefficient is the OQ3-corrected ratio +1.17
(de Sitter -1.80 is RETRACTED). Because OQ3-A leaves the sign of w_a IC-sensitive, this
falsification condition is itself conditional on OQ3-A: if proper slow-roll ICs reverse the
sign, the coefficient changes and this condition must be restated (see FC5).

## What This Does Not Establish

- The initial condition B_i is not derived from GU.
- The exact w(z) curve including matter-era evolution (OQ3).
- Whether the GU cosmological constant Lambda_eff (umbilic contribution) agrees with the observed value quantitatively (separate problem).
- Any connection to the 120-orders-of-magnitude problem beyond the structural point in dark-energy-theta-divergence-free.md.

## References

- Source exploration: theta-field-flrw-eos-2026-06-23.md (full computation with discipline tags)
- Canon basis: dark-energy-theta-divergence-free.md (theta is dynamic and
  divergence-free only at CONDITIONALLY_RESOLVED grade pending the written-action
  theta/Euler-Lagrange identification)
- DESI Collaboration (2024). DESI 2024 VI. arXiv:2404.03002, Table 5 (BAO+CMB+Pantheon+, CPL).
- Turner, M.S. (1983). Coherent scalar-field oscillations in an expanding universe. PRD 28, 1243. (Time-averaged w=0 for oscillating massive scalar)
- Chevallier, M. and Polarski, D. (2001). CPL parametrization. IJMPD 10, 213.
