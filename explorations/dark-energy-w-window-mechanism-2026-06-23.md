---
title: "GU Dark Energy w_a Window: Mechanism Search for the DESI Sign — Non-Minimal Coupling Reaches, Modified Potential and Back-Reaction Do Not"
date: 2026-06-23
problem_label: "dark-energy-w-window-mechanism"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# GU Dark Energy w_a Window: Mechanism Search for the DESI Sign

## 1. Problem Statement

Two dark-energy computations completed earlier today both found `w_a > 0` for the GU theta
field, the opposite sign from DESI DR1 (`w_a = -0.75`):

- `dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md` — slow-roll attractor IC from `z >> z_osc`
  gives `w_a > 0` (ratio `+2.53` analytic estimate). The sign mismatch is not an IC artifact.
- `dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md` — orthogonal divergence-free leg;
  unrelated to the sign but confirms the same theta-field setup.

The minimal-coupling, frozen-IC and slow-roll-IC integrations all land the present-day
oscillation phase `phi_0` in `[49, 90] deg`, **outside** the negative-`w_a` window. This
computation is the distinct **mechanism-search** leg: enumerate candidate GU-admissible
mechanisms that modify the theta-field dynamics, and test each numerically for whether it
places the field in the `w_a < 0` window matching DESI.

**Clean falsification target (from the problem statement):** if NO mechanism reaches the
window, the GU dark-energy sign mismatch with DESI is structural (a GENUINE_OBSTRUCTION for
Candidate D on this observable). If SOME mechanism reaches it, the question becomes whether
that mechanism is GU-admissible.

**Three candidate mechanisms tested:**
1. Non-minimal coupling to curvature: `xi R B^2` (theta is a geometric connection field; a
   coupling to the FLRW Ricci scalar is the most natural geometric modification).
2. Modified / anharmonic potential: Willmore-type quartic `(1/4) lam B^4` (the Willmore
   energy `E[s] = integral |II_s|^2` is quartic in the second fundamental form, so cubic /
   quartic self-interaction of the normal-bundle amplitude is GU-motivated).
3. Back-reaction: self-consistent Friedmann equation with `rho_B` contributing to `H(z)`.

## 2. Established Context

- `canon/theta-field-flrw-dark-energy-eos.md` (CONDITIONALLY_RESOLVED): two-component dark
  energy `w_DE = -1 + f_0 (1 + w_B) + O(f_0^2)`; `M_KK = 2 sqrt(2) H_0` (so `M_KK^2 = 8 H_0^2`),
  oscillating+damped regime, `z_osc ~ 1.85`. Named failure condition FC5/OQ3-A is the sign of `w_a`.
- `theta-field-flrw-matter-era-ode-2026-06-23.md`: full Lambda-CDM RK4 integration. Frozen IC
  `z=3`: `phi_0 = 0.855 rad (49 deg)`, `w_B(0) = +0.388`, ratio `+1.17`.
- `dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md`: the negative-`w_a` window derived as
  `phi in (0, 58 deg)` (equivalently oscillation phase `phi' = 2 phi in (0, 116 deg)`), and
  the convention-free criterion `dw_B/dz + 3(1 + w_B) < 0`.
- `rc3-delta-n-spectrum-gl4r-2026-06-23.md`: `M_KK` from fiber normal Laplacian.

## 3. The Convention-Free Window Criterion

The CPL parameter is `w_a = dw_DE/dz|_{z=0} = f_0 [3 (1 + w_B(0)) + dw_B/dz|_{z=0}]` (derivation
in the matter-era ODE file, §6). The `f_0`-independent ratio is

```
ratio := w_a / (w_0 + 1) = 3 + (dw_B/dz) / (1 + w_B).
```

The sign of `w_a` is therefore controlled by the single inequality

```
CRIT := dw_B/dz + 3 (1 + w_B)        <  0   <=>   w_a < 0   (DESI sign).
```

The first term `dw_B/dz` is the oscillation contribution (negative when the field is moving
toward kinetic dominance); the second `3(1 + w_B)` is the matter-dilution contribution (always
positive since `w_B > -1`). For the DESI sign, the oscillation term must overwhelm the dilution
term.

**Reconciliation note (a subtlety in the oq3a window).** The oq3a file phrased the window as
`phi in (0, 58 deg)` using the *idealized de Sitter relations* `w_B = -cos(phi')` and
`dphi'/dz = -2 omega`. With those relations the boundary is exactly `phi' = 58 deg + 58 deg`,
reproduced here:

```
omega_osc/H_0 = sqrt(8 - 9/4) = 2.3979
R = sqrt(9 + (2 omega)^2) = 5.6569,  offset = atan2(2 omega, 3) = 57.97 deg
phi' window = (0, 115.94 deg)   =>   phi window = (0, 57.97 deg).         [reproduces oq3a]
```

But the **actual integrated** `dw_B/dz` is weaker than the idealized `-2 omega sin(phi')`
because matter-era Hubble friction slows the phase advance: at the baseline phase the
idealization predicts `dw_B/dz = -4.37` whereas the integration gives `-2.54`. Consequently
the phase angle `phi_0` alone is NOT a faithful proxy for the sign — the convention-free
criterion `CRIT < 0` on the *integrated* pair `(w_B, dw_B/dz)` is the correct test, and is the
one used throughout this mechanism search. This is why the baseline `phi_0 ~ 50 deg` (nominally
"inside `(0,58)`") nonetheless yields `w_a > 0`: the idealized phase-window mislabels it, the
integrated criterion does not.

## 4. Numerical Method

Klein-Gordon equation in cosmic time with all three mechanisms:

```
B_ddot + 3 H(t) B_dot + M_KK^2 B + lam B^3 + xi R(t) B = 0,
R(t) = 6 (H_dot + 2 H^2),   H_dot = -(3/2) rho_m   (units 8 pi G / 3 = 1, H_0 = 1).
```

Integrated in redshift via `dB/dz = Pi/(-(1+z)H)`, `dPi/dz = B_ddot/(-(1+z)H)`, RK4,
`N = 3-4 x 10^5` steps, from `z_i` (deep matter era) to `z = 0`. Initial condition is the
**slow-roll attractor** `Pi_i = -(V'(B_i) + xi R B_i)/(3 H_i)` at `B_i = 1` — the physically
preferred IC, mechanism-consistent. `dw_B/dz` evaluated as `(w_B(0.05) - w_B(0))/0.05`.

**Baseline (minimal, `xi = 0`, `lam = 0`):**

```
phi_0 = 50.1 deg,  w_B(0) = +0.410,  dw_B/dz = -2.540,  CRIT = +1.689,  ratio = +1.198.
```

This matches the matter-era ODE file's frozen-IC result (`phi_0 = 49 deg`, ratio `+1.17`) to
within rounding, and is **stable against the starting redshift**: `z_i in {10,20,30,50,100}`
all give `CRIT = +1.689`, `ratio = +1.198` (slow-roll attractor convergence confirmed). The
oq3a analytic `+2.53` estimate was a de Sitter over-estimate of `phi_0`; the careful
integration corrects it to `+1.20` and confirms `w_a > 0`.

## 5. Mechanism 1 — Non-Minimal Coupling `xi R B^2`: REACHES THE WINDOW

Slow-roll-attractor integration, scanning `xi` (coefficient of `R B` in the EOM):

```
 xi       phi_0(deg)   w_B(0)    dw_B/dz   CRIT       ratio
-0.60      334.8      -0.966     -0.243    -0.142     -4.197    <== w_a < 0
-0.55      337.8      -0.934     -0.371    -0.172     -2.598    <== w_a < 0
-0.50      341.3      -0.889     -0.516    -0.182     -1.634    <== w_a < 0
-0.45      345.2      -0.829     -0.681    -0.169     -0.990    <== w_a < 0
-0.40      349.5      -0.755     -0.865    -0.129     -0.528    <== w_a < 0
-0.35      354.5      -0.664     -1.066    -0.060     -0.178    <== w_a < 0
-0.32 (xi_c1, boundary)                     0.000      0.000
-0.30        0.2      -0.557     -1.283    +0.044     +0.100
-0.20       13.8      -0.293     -1.748    +0.371     +0.525
-0.10       30.7      +0.033     -2.206    +0.894     +0.865
 0.00       50.1      +0.410     -2.540    +1.689     +1.198    (baseline)
+0.10       71.1      +0.801     -2.388    +3.014     +1.674
+1.00       52.9      +0.463     -4.438    -0.050     -0.034    <== w_a < 0 (marginal)
+1.0016 (xi_c2, boundary)                   0.000      0.000
+1.10       72.7      +0.827     -2.847    +2.634     +1.442
```

**Result: the negative-`w_a` window IS reachable by non-minimal coupling.** `CRIT < 0` for all
`xi < xi_c1 = -0.319` (a one-sided, open region of negative coupling), and there is a second
isolated crossing at `xi_c2 = +1.002`. The crossing is robust against `z_i` (the `xi = -0.5`
result gives `CRIT = -0.182`, `ratio = -1.63` for every `z_i in {10,...,100}`).

**DESI magnitude match.** DESI DR1 measures `ratio = -0.75 / 0.173 = -4.3`. This is reached at

```
xi = -0.60:  ratio = -4.20      xi = -0.62:  ratio = -5.17
xi = -0.58:  ratio = -3.45      (DESI -4.3 bracketed at xi ~ -0.605)
```

So a single non-minimal coupling `xi ~ -0.6` reproduces both the DESI sign and the DESI
magnitude of `w_a/(w_0+1)`.

**Is `xi ~ -0.3 to -0.6` GU-admissible? This is the crux.** The natural reference values are:

```
xi = 0       (minimal):       ratio = +1.20   (baseline, wrong sign)
xi = +1/6    (conformal):     ratio = +2.40   (wrong sign, more positive)
xi = -1/6:                    ratio = +0.64   (wrong sign)
xi = +1/12, -1/12:           ratio = +1.57, +0.92  (wrong sign)
```

Neither the minimal nor the conformal coupling reaches the window. The required value is a
sizable **negative** non-minimal coupling `xi ~ -0.3 to -0.6` (with `R > 0` in the accelerating
era, a negative `xi R B` is a tachyonic-type, anti-restoring curvature coupling). GU does not
currently supply the sign or magnitude of any `xi R theta^2` term from first principles. The
two-component canon explicitly sets `xi = 0` (Assumption 3 of the canon EOS file). Whether the
GU action, when fully reduced, generates a curvature coupling of this sign and size is an open
structural question, NOT settled here. The mechanism *exists* dynamically; its *GU provenance*
is unestablished.

## 6. Mechanism 2 — Anharmonic Willmore Potential `(1/4) lam B^4`: DOES NOT REACH

Slow-roll-attractor integration, scanning the quartic coupling `lam`:

```
 lam       phi_0(deg)   w_B(0)    dw_B/dz   CRIT       ratio
-2.0        38.1      +0.183     -2.421    +1.127     +0.953
-1.0        44.6      +0.304     -2.497    +1.415     +1.085
-0.5        47.5      +0.359     -2.522    +1.554     +1.144
 0.0        50.1      +0.410     -2.540    +1.689     +1.198    (baseline)
+0.5        52.6      +0.457     -2.551    +1.820     +1.249
+1.0        55.0      +0.502     -2.557    +1.949     +1.298
+2.0        59.2      +0.583     -2.550    +2.200     +1.389
+5.0        69.6      +0.774     -2.402    +2.919     +1.646
```

**Result: the quartic potential CANNOT reach the window.** Over `lam in [-2, +5]` (and the
monotone trends show this persists outside the scanned range), `CRIT` stays firmly positive
(`+0.95` to `+2.92`) and the ratio stays positive (`+0.95` to `+1.65`). The quartic shifts
`phi_0` monotonically but never drives the oscillation term `dw_B/dz` negative enough to beat
the dilution term. Intuitively: an anharmonic correction changes the oscillation *frequency*
and amplitude-dependence but does not change the qualitative fact that, released on the
slow-roll attractor, the field arrives at `z = 0` moving *into* kinetic dominance with
`w_B(0) > 0`. The quartic is structurally blocked from the DESI sign.

## 7. Mechanism 3 — Back-Reaction (Self-Consistent `H`): DOES NOT REACH

Self-consistent Friedmann `H^2 = Omega_m (1+z)^3 + Lambda_eff + kappa rho_B`, with `kappa`
shot so that `rho_B(0)/rho_DE(0) = f_0` and `H(0) = 1`; `H_dot` includes the `rho_B` pressure.
Scanning the dynamical fraction `f_0`:

```
 f_0       phi_0(deg)   w_B(0)    dw_B/dz   CRIT       ratio    kappa
0.125       45.3      +0.317     -2.515    +1.435     +1.090    0.116   (DESI-matching f_0)
0.250       41.9      +0.250     -2.492    +1.257     +1.006    0.212
0.400       38.7      +0.188     -2.468    +1.097     +0.923    0.314
0.600       35.5      +0.125     -2.441    +0.935     +0.831    0.434
0.800       32.9      +0.075     -2.417    +0.809     +0.752    0.543
0.950       31.3      +0.044     -2.402    +0.730     +0.699    0.620
```

**Result: back-reaction CANNOT reach the window.** Even at the unphysical extreme `f_0 = 0.95`
(theta accounting for 95% of dark energy, far beyond the `f_0 ~ 0.125` needed to match DESI's
`w_0`), `CRIT` stays positive (`+0.73`) and the ratio positive (`+0.70`). Back-reaction
monotonically *reduces* the ratio toward zero (the extra friction from `rho_B` in `H` slows
the phase advance and lowers `w_B(0)`), but it never reverses the sign. The DESI-relevant value
`f_0 = 0.125` gives ratio `+1.09`, essentially unchanged from baseline. Back-reaction is
structurally blocked from the DESI sign.

## 8. Synthesis

| Mechanism | GU motivation | Reaches `w_a < 0`? | Best ratio | Required value |
|---|---|---|---|---|
| Non-minimal `xi R B^2` | geometric connection coupling | **YES** | `-4.3` (DESI) at `xi ~ -0.6` | `xi < -0.319` or `xi ~ +1.0` |
| Quartic `(1/4) lam B^4` | Willmore `|II_s|^2` energy | NO | `+0.95` (lam=-2) | none in `[-2,+5]` |
| Back-reaction (self-cons. `H`) | `rho_B` in Friedmann | NO | `+0.70` (f_0=0.95) | none up to `f_0=0.95` |

The clean falsification target ("if NO mechanism reaches the window, the mismatch is
structural") is **NOT triggered**: one of the three mechanisms — non-minimal curvature
coupling — does reach the window, and at `xi ~ -0.6` reproduces the DESI sign *and* magnitude.
Therefore the GU dark-energy sign mismatch with DESI is **not structurally forced** at the level
of the FLRW theta-field dynamics. It is forced only under the canon's `xi = 0` assumption.

The mismatch reduces to a single sharp structural question: **does the GU action, fully reduced
to the FLRW theta mode, generate a non-minimal curvature coupling `xi R theta^2` with
`xi <~ -0.3`?** The minimal (`xi = 0`) and conformal (`xi = +1/6`) values do not; only a
sizable negative coupling does. This relocates the open problem from cosmology (phase-space
dynamics, now fully mapped) to GU geometry (the coefficient of the curvature-squared cross-term
in the reduced action).

## 9. Verdict and Failure Conditions

**Verdict: CONDITIONALLY_RESOLVED.**

The mechanism enumeration is complete at reconstruction grade. Two of three mechanisms
(modified potential, back-reaction) are demonstrably blocked from the DESI sign across wide
parameter ranges; the third (non-minimal coupling) reaches it for `xi < -0.319` and matches
DESI's magnitude at `xi ~ -0.6`. The result that the mismatch is *not* a uniform structural
obstruction is reconstruction-grade and robust (stable against `z_i`, reproduces the baseline,
reproduces the oq3a window boundary). The verdict is not RESOLVED because the GU provenance of
the working coupling is not derived, and because the numerics are RK4 reconstruction-grade
(consistent with the prior dark-energy files) with no independent error bound.

Trigger self-check: the draft contains the word "reconstruction" (status/grade tags), it
contains an explicit "X gives Y and Z, not W"-shaped contrast (minimal/conformal `xi` give the
wrong sign), and §3 names an internal subtlety (the phase-window label vs. the convention-free
criterion). Per the discipline rules these force the verdict to at most CONDITIONALLY_RESOLVED.

**Explicit failure conditions (each a specific mathematical statement that would falsify the result):**

**FC1 — The GU action generates no `xi R theta^2` term, or one with `xi >= -0.319`.** If the
fully reduced GU action contains no non-minimal curvature coupling for the FLRW theta mode, or
one whose coefficient is minimal (`xi = 0`), conformal (`xi = +1/6`), or any value
`xi in [-0.319, +1.002)`, then the only mechanism that reaches the window is GU-inadmissible and
the sign mismatch IS structural after all (the verdict would shift toward GENUINE_OBSTRUCTION).
Falsification test: derive the coefficient of `R |theta|^2` from the dimensional reduction of
the GU action on `Y^14`; check whether `xi < -0.319`.

**FC2 — `M_KK != 2 sqrt(2) H_0`.** The window boundary `xi_c1 = -0.319` and the DESI-matching
`xi ~ -0.6` depend on `omega_osc = sqrt(M_KK^2 - 9/4) H_0 = 2.40 H_0` and on `z_osc = 1.85`.
If the BC1-vs-A3 fiber root-system correction (OQ2) shifts `M_KK`, both the boundary and the
DESI-matching `xi` move. A large enough downward shift (`M_KK < 3 H_0 / 2`) would put the field
in the slow-roll regime and overturn the entire oscillating two-component structure. Falsification
test: recompute `xi_c1` with the corrected `M_KK`.

**FC3 — The quartic or back-reaction conclusion is an artifact of the linear-IC release.** The
mechanism-2 and mechanism-3 null results were computed releasing the field on the slow-roll
attractor with `B_i = 1`. If the GU-preferred IC at `z_osc` is far from the attractor (e.g. a
kinetic-dominated primordial release, `B_dot_i >> M_KK B_i`, from a specific inflationary
sector), the phase at `z = 0` could differ and the quartic / back-reaction null results would
need re-checking. Falsification test: re-run mechanisms 2 and 3 with a non-attractor IC and
check whether `CRIT < 0` becomes reachable.

**FC4 — `s*(theta)` is spin-2, not a scalar.** The entire FLRW-KG treatment (all three
mechanisms) assumes the pulled-back theta mode is a homogeneous scalar. If the section pullback
delivers a spin-2 (Fierz-Pauli) field, the mechanism analysis must be redone with the tensor
equation of motion, and the curvature coupling takes a different form. Falsification test: the
4D-reduction spin character of `s*(theta)` (open in the VZ / section-pullback chain).

**FC5 — Nonlinear regime invalidates the quadratic baseline.** For `B_i ~ M_Pl` the quartic and
higher Willmore terms are O(1), not perturbative, and the mechanism-2 scan (treating `lam` as a
small added coupling) may not capture the true nonlinear trajectory. If the full nonlinear
Willmore potential reaches the window where the perturbative quartic scan did not, mechanism 2's
null result is falsified. Falsification test: integrate with the full Willmore `V(B)` rather than
a `lam B^4` perturbation.

## 10. Open Questions

**OQ-W1.** Derive the coefficient of `R |theta|^2` (if any) from the GU action reduced to the
FLRW theta mode. This is the single quantity that decides whether the DESI sign is GU-reachable
(FC1). It is a geometry computation, not a cosmology one.

**OQ-W2.** If `xi ~ -0.6` is required and the geometry does not supply it, is there a *fourth*
mechanism not enumerated here (e.g. a derivative coupling `(partial theta)^2 R`, a disformal
coupling, or a coupling to the GU torsion `H^{(i)}` sector) that reaches the window with a
GU-natural coefficient? The enumeration here is three mechanisms, not exhaustive.

**OQ-W3.** Cross-check the `xi ~ -0.6` model against the *full* DESI likelihood (not just the
`w_a/(w_0+1)` ratio): does the same `xi` that fixes the ratio also keep `w_0` in the DESI window
at the GU-natural `f_0 ~ 0.125`, or does fixing the sign break the `w_0` match? A two-parameter
(`xi, f_0`) fit to (`w_0, w_a`) is the decisive observational test.

## 11. References

- `canon/theta-field-flrw-dark-energy-eos.md` — two-component EOS, `M_KK`, FC5/OQ3-A.
- `explorations/dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md` — window derivation, criterion.
- `explorations/theta-field-flrw-matter-era-ode-2026-06-23.md` — full FLRW baseline, ratio formula.
- `explorations/dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md` — orthogonal divergence-free leg.
- `explorations/rc3-delta-n-spectrum-gl4r-2026-06-23.md` — `M_KK` from fiber spectrum.
- DESI Collaboration (2024). DESI 2024 VI. arXiv:2404.03002 (`w_0 = -0.827`, `w_a = -0.75`).
- Turner, M.S. (1983). PRD 28, 1243 (time-averaged `w = 0` for oscillating scalar).
- Chevallier & Polarski (2001), IJMPD 10, 213 (CPL parametrization).
