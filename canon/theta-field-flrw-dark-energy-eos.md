---
title: "GU Theta Field Dark Energy — FLRW Equation of State and DESI DR1 Comparison"
status: canon
doc_type: canon
promoted_from:
  - "explorations/dark-energy-cosmology/theta-field-flrw-eos-2026-06-23.md"
promoted_at: "2026-06-23"
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: "2026-06-26"
correction_de02: "CORRECTION DARK-ENERGY-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN. The 2026-06-23 re-elevation from OPEN rested on a PROCESS MILESTONE (the FLRW Klein-Gordon integration being complete), not on support — the integration WORSENED agreement (de Sitter w_a flipped to +1.17; the >2 failure-condition fired). The only parameter-free prediction, ratio w_a/(w_0+1)=+1.17, is SIGN-INCONSISTENT with DESI (w_a=-0.75), and the sign of w_a has two UNDISMISSED candidates (frozen IC w_a>0 vs slow-roll IC w_a<0; OQ3-A unresolved). By the UNDISMISSED-CANDIDATE rule the EOS-vs-DESI verdict is OPEN. The structural EOS machinery (dynamic theta DE field; oscillating+damped two-component w(z); Result 1 algebraically exact) stays reconstruction-grade; only the data-facing verdict is OPEN. Note w_0=-0.826 'matching DESI -0.827' is a FIT (f_0=0.125 tuned), not a prediction. [SUPERSEDED IN PART by DARK-ENERGY-03: the 'w_a>0, sign-inconsistent with DESI, clean falsification' red-flag is RETRACTED — see correction_de03.]"
    correction_de03: "CORRECTION DARK-ENERGY-03 (2026-06-30): RETRACT the 'w_a>0, sign-inconsistent-with-DESI' red-flag. Independent re-verification (tests/chase/MOVE-2/verify/indep_check.py: e-folds N=ln a formulation, second-order KG, Radau+RK45 cross-checked, CPL least-squares over the actual DESI window z<=2) gives the GLOBAL CPL fit w_0=-0.777, w_a=-0.248 -> w_a is NEGATIVE, the SAME sign as DESI (w_a=-0.75), ~3x smaller in magnitude. The earlier +w_a reading was a LOCAL-derivative artifact: the fitted w_a sign FLIPS with fit window (z<=0.5 gives w_a=+0.025>0; z<=1, z<=1.5, z<=2 all give w_a<0), because w_DE(z) is non-monotone (shallow peak near z~0.23 then falls). The canonical 'f_0-independent ratio +1.17' is CORRECTED: only the LOCAL-derivative ratio (~+2.4 in the f_0->0 limit) is f_0-independent; the +1.17 figure came from a hardcoded d ln rho/dz = 3 bug. OQ3-C is NUMERICALLY RESOLVED (phi_0 ~ 50 deg); OQ3-A's phi_0 ~ 90 deg estimate is REFUTED. Verdict STAYS OPEN, but the rationale is REPLACED: the model is LCDM-amplitude-DEGENERATE (the DESI-window CPL fit is neither a clean confirmation nor a clean falsification vs DESI). This is NOT a claim that GU predicts DESI. The source-action bottleneck is untouched; f_0 and B_i remain fits, not GU predictions."
prior_verdict_history: "OPEN (pre-2026-06-23) -> CONDITIONALLY_RESOLVED (2026-06-23, OQ3) -> OPEN (2026-06-26, DARK-ENERGY-02)"
verdict_change_reason_2026_06_23: "OQ3 closed by theta-field-flrw-matter-era-ode-2026-06-23.md: full FLRW Klein-Gordon integration completed. Corrected values: phi_0=0.855 rad, w_B(0)=+0.388, ratio w_a/(w_0+1)=+1.17. De Sitter ratio -1.80 ruled out (factor 2.68, sign flip). Canon re-elevated with corrected numerical values and named failure conditions. NAMED FAILURE CONDITION: OQ3-A (IC-dependence of w_a sign) is a failure condition for CONDITIONALLY_RESOLVED. The sign of w_a is IC-sensitive (8% variation; frozen vs. slow-roll ICs); whether w_a > 0 or w_a < 0 requires extending the integration to z >> z_osc with proper slow-roll ICs. If that extension reverses the sign, the DESI comparison must be repeated and the current +1.17 ratio is not the GU prediction."
correction_oq3: "2026-06-23 (theta-field-flrw-matter-era-ode): Full Lambda-CDM RK4 integration. Corrected: phi_0=0.855 rad (was 1.94), w_B(0)=+0.388 (was +0.76), coefficient in w_0=-1+C*f_0 is C=1.39 (was 1.76), ratio w_a/(w_0+1)=+1.17 (was -1.80, sign reversed). Failure condition fires: factor 2.68 > 2 from de Sitter. Sign of w_a now positive (IC-sensitive; OQ3-A needed for robust sign). OQ3-A is a named failure condition: if slow-roll ICs from z >> z_osc reverse the sign of w_a, the ratio +1.17 is not the GU prediction and the DESI comparison must be rerun. The integration is RK4 numerical with no code shown and no error bound stated; quantitative claims are reconstruction-grade only."
---

# GU Theta Field Dark Energy — FLRW Equation of State and DESI DR1 Comparison

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

> **VERDICT: OPEN (CORRECTION DARK-ENERGY-03, 2026-06-30).** This document's EOS-vs-DESI comparison is an OPEN problem, not CONDITIONALLY_RESOLVED. **The earlier "`w_a>0`, sign-inconsistent-with-DESI, clean-falsification" red-flag is RETRACTED.** Independent re-verification (`tests/chase/MOVE-2/verify/indep_check.py`) fits CPL over the actual DESI window `z<=2` and gets `w_0=-0.777, w_a=-0.248` — `w_a` is **NEGATIVE, the same sign as DESI** (`w_a=-0.75`), about 3x smaller in magnitude. The old `+w_a` reading was a **local-derivative artifact**: the fitted `w_a` sign flips with the fit window (`z<=0.5` gives `w_a>0`; `z<=1` and wider give `w_a<0`) because `w_DE(z)` is non-monotone. The canon's `w_a/(w_0+1)=+1.17` "f_0-independent ratio" is corrected: only the *local-derivative* ratio (`~+2.4` as `f_0->0`) is f_0-independent, and `+1.17` came from a hardcoded `d ln rho/dz = 3` bug. `OQ3-C` is numerically resolved (`phi_0 ~ 50 deg`); `OQ3-A`'s `phi_0 ~ 90 deg` estimate is refuted. The verdict stays OPEN, but the rationale is now: the model is **LCDM-amplitude-DEGENERATE** — the DESI-window fit is **neither a clean confirmation nor a clean falsification**. This does **NOT** mean GU predicts DESI. What IS reconstruction-grade and stands: the **structural** EOS machinery — theta as a dynamic dark-energy field, the oscillating+damped two-component `w(z)`, and the algebraically-exact Result 1. The `w_0=-0.826` "match" to DESI's `-0.827` is a **fit** (`f_0=0.125` tuned), not a prediction; the source-action bottleneck is untouched.

> **OQ3 CORRECTION (2026-06-23, theta-field-flrw-matter-era-ode):** Full Lambda-CDM Klein-Gordon integration is now complete (RK4, 300,000 steps, z=3 to z=0). Corrected values: phi_0 = 0.855 rad (de Sitter was 1.94 rad), w_B(0) = +0.388 (was +0.76), coefficient C = 1.39 (was 1.76 in w_0 = -1 + C*f_0), ratio w_a/(w_0+1) = +1.17 (was -1.80, sign reversed). The failure condition fires: ratio changed by factor 2.68 (> 2 threshold). The de Sitter ratio -1.80 and the negative-w_a prediction are ruled out at reconstruction grade. The sign of w_a is now +1.17*f_0 > 0 (from frozen IC at z=3), but this is IC-sensitive (8% variation between frozen and slow-roll ICs). Whether w_a > 0 or w_a < 0 requires extending the integration to z >> z_osc ~ 1.85 with proper slow-roll initial conditions from attractor (OQ3-A). Result 1 (oscillating+damped regime) remains algebraically exact. Results 2 and 3 are now updated with corrected FLRW values. See `explorations/dark-energy-cosmology/theta-field-flrw-matter-era-ode-2026-06-23.md`.

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
w_a ~ -0.25     [CORRECTED by DARK-ENERGY-03: NEGATIVE, global CPL fit over DESI window z<=2]
```

**CORRECTION DARK-ENERGY-03 (2026-06-30):** the previously-reported `w_a ~ +0.20` (a local-derivative reading) is RETRACTED.
Independent re-verification (`tests/chase/MOVE-2/verify/indep_check.py`, e-folds KG integration
with slow-roll attractor ICs at z=30, Radau+RK45 cross-checked) fits CPL over the actual DESI
window and gives `w_0=-0.777, w_a=-0.248` for z<=2 (`w_0=-0.786, w_a=-0.214` for z<=1.5;
`w_0=-0.801, w_a=-0.139` for z<=1). w_a is NEGATIVE — the SAME sign as DESI (w_a=-0.75) — at
about 1/3 the magnitude. The earlier "+w_a, sign-inconsistent with DESI" reading was a
LOCAL-derivative artifact: dw_DE/dz at z=0 is positive (~+0.29) because w_DE(z) rises to a
shallow peak near z~0.23 before falling, so the sign of the fitted w_a FLIPS with the fit window
(z<=0.5 gives w_a=+0.025>0; z<=1 and wider give w_a<0). The correct data-facing statement is
LCDM-amplitude-DEGENERATE: neither confirmation nor falsification vs DESI.
`[reconstruction — Lambda-CDM background assumed; f_0 and B_i are fits, not GU predictions]`

### Result 3 — Ratio Prediction (CORRECTED by DARK-ENERGY-03)

> **CORRECTION DARK-ENERGY-03 (2026-06-30).** The headline `w_a/(w_0+1) = +1.17` "f_0-independent
> ratio" is RETRACTED. Two distinct quantities were conflated:
> - The **global CPL fit** ratio (the DESI-comparable one) is NOT f_0-independent and is
>   NEGATIVE: over z<=2, `w_a/(w_0+1) = -0.248/0.223 = -1.11`; over z<=1, `-0.139/0.199 = -0.70`.
>   Same sign as DESI (`-4.3`), smaller magnitude.
> - Only the **local-derivative** ratio `dw_DE/dz|0 / (w_0+1)` is f_0-independent, and its
>   f_0->0 limit is `~+2.4` (verify/indep_check.py: +1.94 at f_0=0.1, +2.31 at f_0=0.01,
>   +2.35 at f_0=0.001), NOT +1.17. The canon's +1.17 traces to a hardcoded `d ln rho/dz = 3`
>   bug in the superseded exploration.
> The f_0-independent local ratio is positive (a local-slope fact); the DESI-window fitted ratio
> is negative. Neither is a clean prediction: the model is LCDM-amplitude-DEGENERATE.

The (retracted) prior claim was that the ratio w_a / (w_0 + 1) is independent of the unknown
initial amplitude f_0:

```
w_a / (w_0 + 1) ~ +1.17    [RETRACTED by DARK-ENERGY-03 — hardcoded d ln rho/dz = 3 bug]
```

DESI DR1 measured ratio: w_a / (w_0 + 1) = -0.75 / 0.173 ~ -4.3 (negative). The re-verified
GU global-fit ratio (z<=2) is `~-1.11` — SAME sign as DESI, ~4x smaller magnitude. This is not
a distinguishing prediction; it sits inside the LCDM-degenerate band.

`[reconstruction grade, re-verified 2026-06-30, tests/chase/MOVE-2/verify/indep_check.py]`

### Result 4 — Sign and Qualitative Predictions (OQ3-CORRECTED)

> **SUPERSEDED — see CORRECTION DARK-ENERGY-03 (2026-06-30).** Both the original `w_a < 0`
> claim AND the 2026-06-23 `w_a > 0` "sign-inconsistent-with-DESI" claim below are RETRACTED.
> Independent re-verification with proper slow-roll attractor ICs from z=30
> (`tests/chase/MOVE-2/verify/indep_check.py`) resolves OQ3-A: the DESI-window global CPL fit
> gives `w_a = -0.248 < 0` (z<=2), the SAME sign as DESI's `w_a = -0.75`, ~3x smaller. The
> `w_a > 0` reading was a local-derivative artifact that flips sign with fit window. OQ3-C is
> numerically resolved (phi_0 ~ 50 deg); the OQ3-A phi_0 ~ 90 deg estimate is refuted. Net:
> LCDM-amplitude-DEGENERATE — neither confirmation nor falsification. See Results 2 and 3.

Independent of f_0, GU Candidate D currently predicts (slow-roll attractor IC from z=30, OQ3-A resolved):
- w_a < 0 over the DESI window (`w_a = -0.248` for z<=2). SAME sign as DESI DR1's `w_a = -0.75`,
  ~3x smaller magnitude. This is a DEGENERACY with LCDM, not a distinguishing prediction: it is
  neither a clean confirmation nor a clean falsification (superseding the retracted `w_a > 0`
  red-flag). See CORRECTION DARK-ENERGY-03 and Results 2-3.
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

**F6 (DARK-ENERGY-03-CORRECTED, 2026-06-30).** The +1.17 slope this failure mode was rewritten
around is RETRACTED (hardcoded d ln rho/dz = 3 bug; see DARK-ENERGY-03 and Result 3). The
re-verified DESI-window global-fit ratio is NEGATIVE (`~-1.11` at z<=2), same sign as DESI's
`~-4.3`, so there is no sign-based falsification here — the model is LCDM-amplitude-DEGENERATE.
A future falsification would require the measured `w_a` to fall well outside the degenerate band,
which this model cannot yet predict sharply (f_0/B_i are fits). See Result 3 and FC5.

**F7 (FIRED, OQ3-CORRECTED).** Full FLRW Klein-Gordon integration (OQ3) yielded a phase phi_0 = 0.855 rad, substantially different from the de Sitter estimate of 1.94 rad. This O(1) shift moved the instantaneous w_B at z = 0 and reversed the sign of w_a (ratio -1.80 to +1.17). This failure mode fired against the de Sitter phi_0 ~ 1.94 rad, which is RETRACTED. **DARK-ENERGY-03 (2026-06-30) further corrects this:** the "sign of w_a is now opposite to DESI" clause is RETRACTED — the re-verified DESI-window global fit gives w_a NEGATIVE (`-0.248`, SAME sign as DESI), and OQ3-C resolves phi_0 ~ 50 deg. The corrected w_0 lands inside the DESI DR1 window at f_0 ~ 0.125 (a FIT), and the corrected w_a shares DESI's sign — i.e. LCDM-amplitude-DEGENERATE, neither confirmation nor falsification.

**F8.** The ratio w_a/(w_0+1) is not bounded away from 0 as phi_0 varies. If the full phi_0-scan (required by THETA-01/OQ5) finds that the corrected +1.17 is near a node of the ratio function, the DESI comparison is not a robust prediction and Candidate D cannot be distinguished from Lambda-CDM on this observable.

**F9.** M_KK = 2*sqrt(2) H_0 is shifted by the A_3 root-system correction (OQ2). If the corrected M_KK places the field in the slow-roll regime (M_KK < 3H_0/2), the entire two-component structure of Result 1 is overturned and Results 2-3 do not apply.

**FC5 (OQ3-A — RESOLVED by DARK-ENERGY-03, 2026-06-30).** OQ3-A (extend integration to z >> z_osc
with proper slow-roll ICs) is now DONE: `tests/chase/MOVE-2/verify/indep_check.py` integrates the
KG equation from z=30 on the slow-roll attractor and fits CPL over the DESI window. Result: the
sign of w_a is NEGATIVE (`w_a = -0.248` for z<=2), the SAME sign as DESI, NOT positive. The old
frozen-IC `w_a > 0` reading was a local-derivative artifact whose sign flips with fit window. OQ3-C
is resolved (phi_0 ~ 50 deg); the OQ3-A phi_0 ~ 90 deg estimate is refuted. The FLRW result does
NOT restore a clean DESI match — it lands in the LCDM-amplitude-DEGENERATE band (neither
confirmation nor falsification). The historical text below is retained for provenance.

**FC5 (OQ3-A — IC-dependence of w_a sign, named failure condition — HISTORICAL).** The current ratio w_a/(w_0+1) = +1.17 was computed from a frozen initial condition at z=3 (theta-field-flrw-matter-era-ode-2026-06-23.md, RK4, 300,000 steps). The sign of w_a is IC-sensitive: the file acknowledges 8% variation between frozen and slow-roll ICs, and whether w_a > 0 or w_a < 0 requires extending the integration to z >> z_osc ~ 1.85 with proper slow-roll initial conditions from the attractor (OQ3-A). If that extension reverses the sign of w_a from +1.17 to negative, then: (a) the FLRW-corrected ratio is not +1.17 but some phi_0-dependent negative value; (b) the DESI comparison must be repeated from scratch; (c) the statement that the de Sitter ratio -1.80 is "ruled out" must be revisited because the FLRW sign could restore compatibility with DESI's w_a < 0 at a different magnitude. The numerical integration has no code shown and no error bound stated; the quantitative claims in Results 2 and 3 are reconstruction-grade only and are explicitly conditional on OQ3-A. CONDITIONALLY_RESOLVED remains the correct verdict, but OQ3-A is a named failure condition: if OQ3-A resolves with sign reversal, the core quantitative prediction changes and a new DESI comparison is required.

## The Primary Gaps

**Gap 1:** GU does not yet derive B_i (the initial amplitude) from first principles. The variational principle (Willmore energy E[s]) selects the critical section but does not specify the initial phase or amplitude of normal-bundle perturbations. Without a GU-derivable B_i, the w_0 value is a fit (f_0 = 0.11), not a prediction.

**Gap 2 (THETA-01; DARK-ENERGY-03-CORRECTED, 2026-06-30):** The +1.17 ratio and phi_0 = 0.855 rad
figures in the historical text below are RETRACTED. Re-verification resolves the phase (OQ3-C:
phi_0 ~ 50 deg) and the DESI-window ratio (`~-1.11` at z<=2, negative). The remaining gap is real:
the amplitude f_0 (hence B_i) is a FIT, not a GU prediction, so the model cannot yet make a sharp
distinguishing w(z) prediction — it is LCDM-amplitude-DEGENERATE. Historical text follows.

**Gap 2 (THETA-01, 2026-06-23; OQ3-CORRECTED — HISTORICAL):** The ratio w_a/(w_0+1) = +1.17 depends on the
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

> **CORRECTION DARK-ENERGY-03 (2026-06-30):** the `w_a - 1.17*(w_0+1)` falsification form below
> is RETRACTED — the +1.17 coefficient came from a hardcoded `d ln rho/dz = 3` bug (see Result 3).
> There is currently NO sharp GU falsification coefficient. The DESI-window CPL fit
> (`w_0=-0.777, w_a=-0.248`) is LCDM-amplitude-DEGENERATE: neither confirmation nor falsification.
> A genuine falsification condition requires a GU-derived f_0/B_i (still a fit) so the amplitude,
> not just the sign, is predicted; until then the model cannot be sharply falsified on w(z).

The historical (retracted) sharpened condition read: the prediction is falsified if
`w_a - 1.17 * (w_0 + 1)` significantly differs from 0, specifically if
`|w_a - 1.17 * (w_0 + 1)| > 0.5` at 2-sigma. Both the +1.17 coefficient and the earlier de Sitter
-1.80 are RETRACTED (see DARK-ENERGY-03 and FC5).

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
