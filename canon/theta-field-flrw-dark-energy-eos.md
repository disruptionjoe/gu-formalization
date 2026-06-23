---
title: "GU Theta Field Dark Energy — FLRW Equation of State and DESI DR1 Comparison"
status: canon
doc_type: canon
promoted_from:
  - "explorations/theta-field-flrw-eos-2026-06-23.md"
promoted_at: "2026-06-23"
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: "2026-06-23"
verdict_change_reason: "THETA-03 correction: Results 2 and 3 (w_0, w_a, ratio) are unreliable by O(1) due to de Sitter approximation only. Cannot support CONDITIONALLY_RESOLVED with all quantitative outputs at O(1) uncertainty. Pending OQ3 (full FLRW matter-era evolution)."
---

# GU Theta Field Dark Energy — FLRW Equation of State and DESI DR1 Comparison

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

> **WARNING (2026-06-23, CR-01 / THETA-03):** All numerical values in Results 2 and 3 (w_0 ~ -0.80, w_a ~ -0.35, ratio w_a/(w_0+1) ~ -1.80) are unreliable by O(1) per THETA-03. The de Sitter approximation (H ~ H_0 sqrt(Omega_Lambda) ~ const) was used throughout, but the matter-dominated phase at z > 0.3 has H >> H_0 sqrt(Omega_Lambda) and was not integrated. The accumulated phase phi_0 ~ 1.94 rad and the instantaneous w_B ~ +0.76 both depend on this uncomputed matter-era evolution. Only Result 1 (oscillation regime classification: theta is oscillating and damped, M_KK > BF bound) is firm — it is algebraically exact and independent of the background approximation. This entry must not be cited for quantitative DESI comparison until OQ3 (full FLRW matter-era evolution via numerical Klein-Gordon integration in Lambda-CDM H(z)) is complete. The verdict has been demoted from CONDITIONALLY_RESOLVED to OPEN for this reason.

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

### Result 2 — Two-Component Dark Energy (Reconstruction Grade)

GU dark energy = umbilic Lambda_eff (w = -1) + oscillating theta (instantaneous w_B depends on phase phi_0). The effective total dark energy EOS at z = 0:

```
w_0 = w_{DE}^{eff}(z=0) ~ -1 + 1.76 f_0
```

where f_0 = rho_B(z=0) / rho_{Lambda_eff}(z=0) is the ratio of dynamical to constant dark energy density.

For f_0 ~ 0.11 (corresponding to initial amplitude B_i ~ 0.92 M_Pl, Planck-scale — natural for a geometrical connection field in GU):

```
w_0 ~ -0.80,     w_a ~ -0.35.
```

These are consistent with DESI DR1 68% C.L. for w_0 and within 2-sigma for w_a. `[reconstruction — phase calculation with de Sitter approximation]`

### Result 3 — Ratio Prediction (f_0-Independent, phi_0-Conditional, Reconstruction Grade)

The ratio w_a / (w_0 + 1) is independent of the unknown initial amplitude f_0:

```
w_a / (w_0 + 1) ~ -3.17 f_0 / (1.76 f_0) = -1.80
```

**Correction (2026-06-23, THETA-01):** This ratio is independent of f_0 (correct: f_0 cancels
in the leading-order ratio). It is NOT independent of the initial phase phi_0. The numerator
-3.17 f_0 comes from dw_B/dz at z=0, which was computed for phi_0 ~ 1.94 rad (from the de
Sitter tracker in Section 5.3 of the source exploration). A different phi_0 gives a different
dw_B/dz and a different ratio. The denominator 1.76 f_0 also depends on phi_0 through the
instantaneous w_B(phi_0) at the present epoch.

The phi_0-dependence of the full ratio has not been computed. Until this is done, -1.80 must
be treated as a reconstruction-grade estimate conditional on phi_0 ~ 1.94 rad from the de
Sitter tracker, not a phi_0-independent structural prediction of GU.

Correct description: "independent of f_0 but dependent on phi_0 ~ 1.94 rad (de Sitter tracker estimate)."

`[reconstruction grade, conditional on phi_0 — see OQ5 in source exploration]`

DESI DR1 measured ratio: w_a / (w_0 + 1) = -0.75 / 0.173 ~ -4.3, with uncertainty ~3.2. The GU
estimate -1.80 is within 0.8 sigma of the DESI DR1 data at the current phi_0 estimate.

### Result 4 — Sign and Qualitative Predictions

Independent of f_0, GU Candidate D predicts:
- w_a < 0 (dark energy was more negative in the past, approaching w = -1 from above as the theta field decays). DESI DR1 also finds w_a < 0.
- Transition redshift z_osc ~ 2: theta begins oscillating when H ~ M_KK. For z > 2 the dark energy is indistinguishable from Lambda-CDM.
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

**F6.** The ratio w_a/(w_0+1) > -1.0 at 2-sigma. This would contradict the GU Hubble-friction slope prediction of -1.80.

**F7.** Full FLRW Klein-Gordon integration (OQ3) yields a phase phi_0 substantially different from 1.94 rad. If phi_0 shifts by O(1), the instantaneous w_B at z = 0 changes by O(1), moving w_0 outside the DESI DR1 window without any adjustment of f_0. This is the primary quantitative threat from THETA-03.

**F8.** The ratio w_a/(w_0+1) is not bounded away from 0 as phi_0 varies. If the full phi_0-scan (required by THETA-01/OQ5) finds that -1.80 is near a node of the ratio function, the DESI comparison is not a robust prediction and Candidate D cannot be distinguished from Lambda-CDM on this observable.

**F9.** M_KK = 2*sqrt(2) H_0 is shifted by the A_3 root-system correction (OQ2). If the corrected M_KK places the field in the slow-roll regime (M_KK < 3H_0/2), the entire two-component structure of Result 1 is overturned and Results 2-3 do not apply.

## The Primary Gaps

**Gap 1:** GU does not yet derive B_i (the initial amplitude) from first principles. The variational principle (Willmore energy E[s]) selects the critical section but does not specify the initial phase or amplitude of normal-bundle perturbations. Without a GU-derivable B_i, the w_0 value is a fit (f_0 = 0.11), not a prediction.

**Gap 2 (THETA-01, 2026-06-23):** The ratio w_a/(w_0+1) ~ -1.80 depends on the initial phase
phi_0 ~ 1.94 rad, which was estimated from the de Sitter tracker approximation and is not
derived from first principles. The full phi_0-dependence of the ratio has not been computed;
it is not known whether -1.80 is a minimum, maximum, or saddle point as phi_0 varies. Until
this scan is done and OQ3 (matter-era evolution) is computed, the ratio is a conditional
estimate, not a free structural prediction.

The ratio w_a/(w_0+1) ~ -1.80 is the most constrainable quantity from DESI/Euclid, but it
should be cited as "conditional on phi_0 ~ 1.94 rad" not as "independent of initial conditions."

## Falsification Condition (Sharpened)

The GU theta-field prediction is falsified if:

```
w_a + 1.80 * (w_0 + 1) significantly differs from 0,
```

specifically if |w_a + 1.80 * (w_0 + 1)| > 0.5 at 2-sigma (from future DESI/Euclid data with precision ~0.05 on w_0 and ~0.1 on w_a).

## What This Does Not Establish

- The initial condition B_i is not derived from GU.
- The exact w(z) curve including matter-era evolution (OQ3).
- Whether the GU cosmological constant Lambda_eff (umbilic contribution) agrees with the observed value quantitatively (separate problem).
- Any connection to the 120-orders-of-magnitude problem beyond the structural point in dark-energy-theta-divergence-free.md.

## References

- Source exploration: theta-field-flrw-eos-2026-06-23.md (full computation with discipline tags)
- Canon basis: dark-energy-theta-divergence-free.md (theta is dynamic and D_A*theta = 0)
- DESI Collaboration (2024). DESI 2024 VI. arXiv:2404.03002, Table 5 (BAO+CMB+Pantheon+, CPL).
- Turner, M.S. (1983). Coherent scalar-field oscillations in an expanding universe. PRD 28, 1243. (Time-averaged w=0 for oscillating massive scalar)
- Chevallier, M. and Polarski, D. (2001). CPL parametrization. IJMPD 10, 213.
