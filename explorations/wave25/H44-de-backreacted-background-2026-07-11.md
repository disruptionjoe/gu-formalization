---
title: "H44 -- the DE backreacted-background test: does a self-consistent theta-backreacted background rotate GU's (w0,wa) locus INTO the DESI DR2 degeneracy (rescue), or does GU's dark energy stay falsified? Verdict: FALSIFIED-FULL-STOP. The sole freedom H43 left open (LCDM background) is now closed: the backreacted-background global closest approach is 3.22 sigma, essentially identical to H43's fixed-LCDM 3.20 sigma. Backreaction deforms H(z) by a few percent but shifts the locus AMPLITUDE, not its DIRECTION."
artifact_type: exploration
status: exploration
created: 2026-07-12
wave: 25
grade: "FALSIFICATION HARDENED (of the (w0,wa)-locus comparison). Deterministic reproduction, exit 0, 8/8. The coupled Friedmann + theta Klein-Gordon system is integrated to self-consistency (fixed-point on H^2(N), converged delta ~1e-13); the (w0,wa) locus is computed source-first from each admissible normal-Laplacian M^2 and compared to the H3-verified DESI DR2 digits ONLY in the comparison half. M^2 values are root-system eigenvalues (never tuned to data). The f0->0 -> LCDM background limit is checked to 3.5e-6 as a bug guard."
depends_on:
  - "tests/wave25/H44_de_backreacted_background.py"
  - "tests/wave20/H43_de_shape_falsifier.py"
  - "explorations/wave20/H43-de-shape-falsifier-2026-07-11.md"
  - "tests/wave19/H42_f0_prereg.py"
  - "tests/wave11/H_DE_actual_wz_floating_bg.py"
  - "tests/wave1/H3_desi_verified_and_intersection.py"
  - "canon/theta-field-flrw-dark-energy-eos.md"
verdict: "FALSIFIED-FULL-STOP (at the (w0,wa)-comparison level). H43 falsified GU's source-first dark-energy (w0,wa) locus against DESI DR2 on a FIXED LCDM background and named exactly one untested freedom: a self-consistent background where the theta field's own density sources H(z) (H43 Honest limit 2). H44 builds that background (coupled Friedmann + theta KG, solved to self-consistency) and re-runs the falsifier. Result: the backreacted-background GLOBAL closest approach over the full (M^2 in [1,25], f0 in [0.01,6]) plane is 3.22 sigma (at M^2=2.0, f0=1.04), vs H43's fixed-LCDM 3.20 sigma -- a +0.02 sigma move. Per-root-system closest approaches are unchanged to hundredths: BC_1 M^2=8 -> 3.46 sigma (H43 3.47), A_1 M^2=7 -> 3.41 (3.42), S^3 M^2=3 -> 3.25 (3.25), continuum 20.25 -> 4.29 (4.32). The background genuinely moves (H_backreacted/H_LCDM differs by up to +3.6% at z~1), but the deformation shifts the locus AMPLITUDE, not its DIRECTION: the locus still tracks ACROSS the DESI degeneracy, not into it. So the H43 falsification was NOT a fixed-background artifact. GU's dark-energy CPL shape is falsified against DESI DR2 with NO remaining background freedom. NAMED SCOPE (unchanged from H43, computed not asserted): at the fixed-Omega_m raw-distance level the backreacted model still mimics a DESI-CPL H(z) to ~1.3% at the plane-best point (H43 1.27%), the LCDM-amplitude-degeneracy canon DARK-ENERGY-03. H44 hardens the falsification of the (w0,wa) CPL-parameter comparison DESI headlines; it does not independently kill the raw expansion history."
---

# H44 -- the DE backreacted-background test

H43 (Wave 20) **falsified** GU's source-first dark-energy `(w0,wa)` locus against DESI DR2's
`DESI+CMB+DESY5` CPL contour: no admissible root-system `M^2`, no point in the free
`(M^2,f0)` plane (global closest `3.20 sigma`), and no ansatz variant rotates GU's locus
**into** the DESI degeneracy. It is a robust shape/direction miss. But H43 rode the theta
field on a **fixed LCDM background**: `rho_theta` had no backreaction on `H(z)`. H43 named
this as its single untested freedom (Honest limit 2):

> *"A backreacted background could in principle rotate the locus; this is the one freedom
> H43 does not close."*

H44 closes it. **The question:** does self-consistent theta backreaction rotate the
`(w0,wa)` locus into the DESI degeneracy (RESCUE), or does GU's dark energy stay FALSIFIED
with no remaining background freedom (FALSIFIED-FULL-STOP)?

Reproduction: `python -u tests/wave25/H44_de_backreacted_background.py` (deterministic, exit 0, 8/8).

---

## The object and the coupled system

GU dark energy (canon `theta-field-flrw-dark-energy-eos.md`) is a constant DeWitt-Lambda
(`w=-1`, density `rho_L`) plus a dynamical Klein-Gordon theta field `B` of mass `M^2`
(units `H0^2`; `M^2=8` is the `BC_1` canonical ground eigenvalue
`lambda_{N,1}=(9/2)^2-(7/2)^2` on `GL(4,R)/O(3,1)`). The combined EOS is
`w_DE = (-1 + f w_theta)/(1+f)`, `f = rho_theta/rho_L`, and `f0 = rho_theta(0)/rho_L(0)` is
the sole amplitude knob (H42).

The **only** change from H43 is the background:

```
H43 (LCDM):        H^2 = Om a^-3 + OL                    (FIXED; rho_theta does NOT enter H)
H44 (this test):   H^2 = Om a^-3 + rho_L + rho_theta(a)  (SELF-CONSISTENT)
```

with `Om + rho_L + rho_theta(0) = 1` exactly (flat, `H(0)=H0`), `rho_L = OL/(1+f0)`,
`rho_theta(0) = OL f0/(1+f0)`, `OL = 0.685`. The theta KG equation on the backreacted
background is

```
B'' + (3 + H'/H) B' + (M^2/H^2) B = 0,
H'/H = -3/2 (rho_m + rho_theta(1+w_theta)) / H^2
```

The `H'/H` friction now carries a `rho_theta(1+w_theta) = 2 KE_theta` term (the Lambda
piece contributes `0` because `w=-1`); as `rho_theta -> 0` it reduces **exactly** to the
H43 LCDM friction `-3/2 Om a^-3/H^2`. The coupled system is solved by fixed-point iteration
on `H^2(N)` (`N=ln a`): integrate the linear KG field from the slow-roll IC `B=1` at `z=30`
on the current `H^2`, rescale its density so `rho_theta(0)` hits the target, rebuild `H^2`,
repeat. Because KG is linear in `B` the rescaling is exact and the map is a contraction
(`rho_theta` is a modest fraction of `H^2`); it converges to `delta ~ 1e-13` in a handful of
iterations. The integrator is a deterministic fixed-step RK4 (no adaptive/random state).

---

## Bug guards (adversarial, run FIRST)

**`f0 -> 0` MUST reduce to LCDM** (guard against an ODE-integration bug driving a spurious
verdict). At `f0=1e-6`: `max|H2_backreacted - H2_LCDM|` over `z in [0,30]` is `3.5e-6`, and
`rho_L -> 0.68499932` (LCDM `OL=0.685`). **PASS** (`< 1e-4`). The falsifier is not an
integration artifact.

**Canonical point stays continuous.** On the backreacted background the canonical
`(M^2=8, f0=0.125)` gives `(w0,wa)=(-0.7922, -0.2450)`, joint `3.89 sigma` -- a small
rotation from the H43 LCDM-background `(-0.768, -0.273)` (`4.19 sigma`), shift
`dw0=-0.024, dwa=+0.028`. **PASS** (within `0.15`; a rotation, not a discontinuity).

---

## Q1 -- the self-consistent background: `w(z)` and the locus (COMPUTED)

The backreaction is **real, not a null op**. At canonical `(M^2=8, f0=0.125)`,
`rho_theta(0)/rho_crit = 0.076` and the self-consistent `H(z)` differs from LCDM:

```
H_backreacted / H_LCDM - 1:   z=0  +0.00%    z=1  +3.63%    z=2  +1.64%
```

(`H(0)` is pinned by flatness; the field's slightly-non-Lambda density raises `H` at
intermediate `z`). The combined `w_DE(z)` on this background:
`w(0)=-0.853, w(0.5)=-0.855, w(1)=-0.910, w(2)=-0.966` -- the same shallow, non-monotone
evolution as H43, riding a background that now moves with it.

The `(w0,wa)` **locus** as `f0` varies (backreacted, `M^2=8`):

| `f0` | `(w0,wa)` backreacted | Mahalanobis |
|---|---|---|
| `0.020` | `(-0.9567, -0.0456)` | `3.90 sigma` |
| `0.125` | `(-0.7922, -0.2450)` | `3.89 sigma` |
| `0.500` | `(-0.5310, -0.6170)` | `8.05 sigma` |
| `1.000` | `(-0.3965, -0.8254)` | `10.61 sigma` |
| `2.000` | `(-0.2895, -0.9969)` | `12.69 sigma` |

Raising `f0` deepens `|wa|` but drives `w0` up toward `0` -- **exactly the H43 tracking
across the DESI degeneracy**, not into it. Backreaction did not bend the locus toward the
`(-0.752, -0.86)` degeneracy direction.

---

## Q2 -- closest Mahalanobis on the backreacted background vs H43's 3.20 sigma (COMPUTED)

`M^2` is a root-system eigenvalue in every row; **no `M^2` is tuned to DESI**. DESI digits
enter only in the Mahalanobis.

| `M^2` (`H0^2`) | assignment | **backreacted** closest | H43 LCDM-bg | shift |
|---|---|---|---|---|
| `8` | BC_1 | `3.46 sigma` (f0=0.060) | `3.47 sigma` | `-0.01` |
| `7` | A_1 | `3.41 sigma` (f0=0.085) | `3.42 sigma` | `-0.01` |
| `3` | S^3 | `3.25 sigma` (f0=0.436) | `3.25 sigma` | `-0.00` |
| `20.25` | continuum | `4.29 sigma` | `4.32 sigma` | `-0.03` |

**Q2-decisive -- the whole `(M^2, f0)` plane:**

```
BACKREACTED GLOBAL min Mahalanobis = 3.22 sigma   at M^2 = 2.00, f0 = 1.043  ->  (-0.8534, -0.2085)
H43 FIXED-LCDM GLOBAL min           = 3.20 sigma   at M^2 = 1.50, f0 = 2.04   ->  (-0.854, -0.211)
```

**Backreaction moves the global closest approach by `+0.02 sigma`.** Even with `M^2` and
`f0` both free and the background solved self-consistently, the nearest the locus gets to
DESI is `3.22 sigma`.

- **COMPUTED:** backreacted per-assignment `{3.46, 3.41, 3.25, 4.29} sigma`; global plane
  minimum `3.22 sigma`. No admissible `M^2` moves the backreacted locus within `2 sigma`
  (or `3`) of DESI.
- **ARGUED (high confidence):** backreaction is a few-percent deformation of `H(z)` that
  rescales the theta roll rate roughly uniformly; it moves the locus along its own
  amplitude direction (`f0`-like) rather than rotating its slope `dwa/dw0`. The slope is set
  by the KG shape, which the background barely touches. Hence the near-invariance.

---

## Q3 -- verdict

| case | `(w0,wa)` | joint Mahalanobis |
|---|---|---|
| canonical `f0=0.125, M^2=8` (backreacted) | `(-0.7922, -0.2450)` | `3.89 sigma` |
| BC_1 best `M^2=8` (backreacted) | `(-0.8835, -0.1298)` | `3.46 sigma` |
| S^3 best `M^2=3` (backreacted) | `(-0.8573, -0.1976)` | `3.25 sigma` |
| **global (free `M^2`, free `f0`) backreacted** | `(-0.8534, -0.2085)` | **`3.22 sigma`** |
| *(H43 fixed-LCDM global, for reference)* | `(-0.854, -0.211)` | *`3.20 sigma`* |

**VERDICT: FALSIFIED-FULL-STOP** (at the `(w0,wa)`-comparison level). Self-consistent theta
backreaction does **not** rotate GU's locus into the DESI degeneracy. The one freedom H43
left open is now closed. Backreaction is a real but small deformation of `H(z)` that shifts
the locus **amplitude**, not its **direction**; the global closest approach is essentially
unchanged (`3.22` vs `3.20 sigma`). With the LCDM-background assumption removed, the H43
`(w0,wa)` falsification was **not** a fixed-background artifact. GU's dark-energy CPL shape
is falsified against DESI DR2 with **no remaining background freedom**.

---

## Q4 -- the raw-`H(z)` scope check (CPL-comparison vs raw-distance)

The scope is identical to H43 and is **computed, not asserted**. DESI headlines a CPL
`(w0,wa)` contour; GU's `w_DE(z)` is non-CPL. Two honest metrics, both on the backreacted
models:

```
canonical (M^2=8, f0=0.125):
   (w0,wa) joint 3.89 sigma   |   raw-distance RMS (shape, fixed OM_DESI) 2.26%
   strict backreacted expansion (Om=0.315 baked in) raw-distance RMS 2.88%
(w0,wa)-plane best (M^2=2.0, f0=1.04):  3.22 sigma  |  raw-distance RMS 1.29%
H43 LCDM-bg reference:  canonical 2.63% ; plane-best 1.27% ; distance-own-best 0.99% (BAO ~1.5%)
```

**Backreaction changes the raw-distance agreement by only `~0.4 pt`.** At the plane-best
point the backreacted `H(z)` still mimics a DESI-CPL `H(z)` to `1.29%` (H43: `1.27%`) -- the
canon `DARK-ENERGY-03` LCDM-amplitude-degeneracy. So the two metrics **still disagree**: the
`(w0,wa)` locus misses DESI's published CPL ellipse robustly, yet the non-CPL `H(z)` can
mimic DESI **distances** to `~1%`. **H44 hardens the falsification of the `(w0,wa)`
CPL-parameter comparison DESI reports; it does not independently kill the raw expansion
history.** That boundary is the disciplined content of the result.

---

## COMPUTED vs ARGUED

- **COMPUTED:** the coupled Friedmann+KG system solved to self-consistency
  (`delta ~ 1e-13`); the `f0->0 -> LCDM` limit (`3.5e-6`); the backreacted `w(z)`, locus,
  per-assignment and global Mahalanobis (`3.22 sigma`); the raw-distance RMS on the
  backreacted models; the canonical rotation (`dw0=-0.024, dwa=+0.028`).
- **ARGUED (high confidence):** backreaction moves the locus along its amplitude direction,
  not its slope, which is why the closest approach is invariant to `0.02 sigma`; this is a
  property of any few-percent background deformation acting on a KG-shape-fixed locus.

---

## Honest limits

1. **The falsification is of the `(w0,wa)` comparison, not the raw expansion history.**
   Unchanged from H43 and re-confirmed here: at the fixed-`Omega_m` distance level the
   backreacted models still reach `~1.3%` (near BAO precision). The kill is clean for the
   CPL-parameter comparison DESI headlines, which is how GU's DE prediction has always been
   stated. A reader who privileges distances over CPL parameters should read this as "the
   CPL shape is wrong," not "dark energy is dead at every level."
2. **The strict-expansion distance metric conflates `Omega_m`.** The `2.88%` "strict
   backreacted expansion" number bakes in `Om=0.315` against DESI's `OM_DESI=0.3069`, so
   part of it is the `Om` offset, not pure DE shape. The cleaner apples-to-apples number is
   the shape-only reconstruction at `OM_DESI` (`2.26%` canonical, `1.29%` plane-best), which
   is what the H43-vs-H44 comparison uses.
3. **`f0 = rho_theta/rho_L` two-component split.** H44 keeps the two-component structure to
   define the backreaction cleanly. H43's 1-component result (`3.18 sigma`, no separate
   Lambda) already showed the miss survives removing the split; H44 did not re-run the
   1-component locus on a backreacted background, but the amplitude-not-direction finding
   makes a different outcome there very unlikely.
4. **Reconstruction-grade `M^2`.** The eigenvalues rest on `rc3-delta-n-spectrum-gl4r` /
   `rc3-root-multiplicity-bc1` (CAS Iwasawa verification F6 still open). H44, like H43,
   scans the whole `M^2` band rather than trusting one value, so the verdict does not hinge
   on the exact eigenvalue.
5. **This test builds no new physics.** It builds a self-consistent background from the
   already-built theta sector and re-runs the H43 comparison. It does not compute the source
   action (`B_i`, `mu_DW` remain unbuilt; H42) -- that bottleneck is untouched.

---

## RE-RANK signal

**FALSIFIED-FULL-STOP** (at the `(w0,wa)` comparison). This converts H43's "FALSIFIED, with
one untested background freedom" into a falsification with **no remaining background
freedom**. The backreacted background -- the sole lever H43 named -- moves the global
closest approach by `0.02 sigma`. Every DE-rescue route nominated across Waves 18-20 is now
spent: the amplitude `f0` (H42), the OQ2 root-system `M^2` (H43), the component count and IC
(H43), and now the self-consistent background (H44). None rotates GU's dark-energy CPL locus
into the DESI DR2 degeneracy.

- **Precise scope:** the falsification is of the **CPL `(w0,wa)` comparison** DESI publishes.
  The **raw `H(z)`** is NOT independently killed -- the non-CPL expansion history still mimics
  DESI distances to `~1%` (DARK-ENERGY-03 degeneracy), computed on the backreacted models.
  Anyone re-opening GU dark energy must attack it at the raw-distance / full-BAO+CMB
  likelihood level, not the CPL projection, because the CPL projection is closed.
- **Single next object:** the **raw-distance / full-likelihood test** -- fit the backreacted
  GU `H(z)` to the actual DESI DR2 BAO table plus a CMB `Omega_m` prior (not the CPL proxy).
  This is the only comparison the `(w0,wa)` falsification does not already settle, and it is
  where the `~1%` distance degeneracy would either finally break the model or expose that
  GU's DE is observationally LCDM-degenerate at the distance level. It is a data-comparison
  object, not a source-action object; the source action (`B_i`, `mu_DW`) remains the separate
  upstream bottleneck (H42) and is unaffected by this result.
- **Do NOT** re-spend effort on `f0`, OQ2 `A_3`-vs-`BC_1`, the two-component ansatz, or the
  background as `(w0,wa)`-rescue routes: Waves 19-20 and H44 show all four are exhausted.

---

*Filed 2026-07-12. Wave 25, the DE backreacted-background test (H44). Reproduced:
`python -u tests/wave25/H44_de_backreacted_background.py` (exit 0, 8/8). Discipline: the
coupled Friedmann+KG system is solved to self-consistency (`delta ~ 1e-13`); `M^2` values
are root-system eigenvalues (never tuned to DESI); DESI digits enter only in the comparison
half and are the H3-verified primary-source values; the `f0->0 -> LCDM` limit is checked as
a bug guard; the raw-distance scope is computed, not asserted. FALSIFIED-FULL-STOP is a
success of the test -- an honest, hardened negative that closes the last background freedom.*
