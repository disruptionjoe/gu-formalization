---
title: "H42 -- Pre-registered test of f0, GU's sole data-facing knob: can the theta-sector dark-energy amplitude be derived SOURCE-FIRST, DESI-blind? Recorded finding: NO -- f0 is the ratio of two unbuilt amplitudes (B_i and mu_DW), so it stays a FIT. Verdict NO-TEST-YET (loops to the H41 source action)."
artifact_type: exploration
status: exploration
created: 2026-07-12
wave: 19
grade: "PRE-REGISTRATION (Part A recorded DESI-blind, then Part B compared). No new physics built; a disciplined derivability audit of f0 against the built machinery, with a deterministic reproduction. All numbers reproduced in tests/wave19/H42_f0_prereg.py (exit 0, 5/5); nothing imported."
depends_on:
  - "tests/wave19/H42_f0_prereg.py"
  - "canon/theta-field-flrw-dark-energy-eos.md"
  - "tests/one-residual/dark_energy_desi_sign.py"
  - "tests/wave11/H_DE_prediction_vs_fit.py"
  - "tests/wave11/H_DE_combined_dewitt_theta_desi.py"
  - "tests/wave6/H24_RY_normalization.py"
  - "explorations/wave6/H24-RY-normalization-2026-07-11.md"
  - "tests/wave1/H3_desi_verified_and_intersection.py"
  - "explorations/representation-theory-noncompact/rc3-delta-n-spectrum-gl4r-2026-06-23.md"
  - "explorations/wave18/H34-predictive-content-audit-2026-07-11.md"
verdict: "NO-TEST-YET. f0 is NOT source-first derivable with current machinery: it is the amplitude ratio rho_theta(0)/rho_Lambda(0), and BOTH amplitudes are set by unbuilt source-action inputs -- B_i (theta initial amplitude; the Willmore principle selects the section, not the perturbation amplitude, canon Gap 1) and mu_DW (DeWitt overall scale; the scale-covariant gimmel geometry fixes only dimensionless ratios, H24). f0 stays a FIT; no parameter-free prediction is possible until the source action (H41) fixes the overall normalization. A latent falsifier is sharpened: the source-first f0-FAMILY locus (derived M^2 = 8 H0^2) misses DESI at EVERY f0 (closest 3.47 sigma), so a forced f0 would falsify on the amplitude regardless -- but the locus rests on the reconstruction-grade two-component ansatz, so it does not fire cleanly now."
---

# H42 -- Pre-registered test of f0 (the theta-sector dark-energy amplitude)

The Wave-18 audit (H34) established that GU currently has ZERO parameter-free
predictions and exactly one data-facing FIT: `f0`, the theta-sector dark-energy
amplitude, which slides GU's `(w0,wa)` along a one-parameter family. This test runs
the single most consequential gate the program can run right now: **can `f0` be
derived SOURCE-FIRST from GU's built structure, DESI-blind?** A yes that matches DESI
is GU's first prediction; a yes that misses is a clean falsification; a no keeps it a
fit. The discipline is a strict A/B pre-registration split, enforced in the code: the
derivation function `derive_f0_source_first()` takes no DESI argument and references no
DESI number; only `compare_to_desi()` loads the data.

Reproduction: `python -u tests/wave19/H42_f0_prereg.py` (deterministic, exit 0, 5/5).

---

## PART A -- Derive and record f0, DESI-blind

### What f0 is

From the built two-component dark-energy model (canon
`theta-field-flrw-dark-energy-eos.md`, Result 2; `tests/one-residual/dark_energy_desi_sign.py`):

```
GU dark energy  =  constant DeWitt-Lambda (w = -1)  +  dynamical theta field (KG)
w_DE(z) = (-1 + f wB)/(1 + f),     f = f0 * rho_theta(z)/rho_theta(0)
f0 = rho_theta(z=0) / rho_Lambda(z=0)
```

`f0` is an **amplitude ratio of two energy densities today** -- not a shape datum, not
a spectral eigenvalue. This is the crux: an amplitude ratio needs both amplitudes.

### Step-by-step source-first walk

**A2 -- The theta SHAPE is derived (but the shape is not f0).** The theta mass is
`M^2 = M_KK^2 = 8 H0^2`, the lowest normal-Laplacian eigenvalue `lambda_{N,1} = 8/R_s^2`
on `GL(4,R)/O(3,1)` with `R_s = c/H0` (`rc3-delta-n-spectrum-gl4r-2026-06-23.md`). This
is genuinely source-first (modulo the OQ2 `A_3`-vs-`BC_1` root-system caveat the file
itself flags). It fixes the theta TRAJECTORY, hence the SHAPE of `w(z)` and the `(w0,wa)`
LOCUS as `f0` varies -- but it does **not** fix the amplitude `f0`.

**A3 -- rho_theta(0) needs B_i, which is UNBUILT.** `rho_theta(0) ~ (1/2) M^2 B_i^2`
times the (built) evolution factor. The overall amplitude is set by `B_i`, the theta
initial/vacuum displacement -- a misalignment amplitude, the integration constant of the
KG equation. Canon **Gap 1** is explicit: "GU does not yet derive `B_i` from first
principles. The variational principle (Willmore energy `E[s]`) selects the critical
section but does not specify the initial phase or amplitude of normal-bundle
perturbations. Without a GU-derivable `B_i`, the `w0` value is a fit, not a prediction."

**A4 -- rho_Lambda(0) needs mu_DW, which is UNBUILT.** The constant piece is the DeWitt
`O(M^0)` term (H15 Part D / H24). Its dimensionless coefficient is geometry-fixed (the
pure-horizontal ambient sectional, a constant), but its MAGNITUDE carries the overall
DeWitt scale `mu_DW`. H24's verdict is explicit: the scale-covariant gimmel geometry
"fixes all DIMENSIONLESS ratios ... but NOT the overall DIMENSIONFUL scale `mu_DW`, which
is the source action's normalization (unbuilt)."

**A5 -- Therefore f0 is the ratio of two unbuilt amplitudes.** `f0 = rho_theta(0)/rho_Lambda(0)`
depends on `B_i` (A3) and `mu_DW` (A4). Neither is fixed by the built geometry, and no
built dimensionless ratio pins the combination.

**A6 -- Adversarial DERIVABLE-NOW steelman, and its rejection.**
- *The 1/8 coincidence.* `f0 = 0.125 = 1/8`, and the gimmel off-diagonal sectional is
  `-1/8`. It is tempting to "derive" `f0 = |offdiag sectional|`. **REJECTED.** There is
  no built identity linking an amplitude RATIO to a sectional CURVATURE; the canonical
  `0.125` traces (canon Result 2) to "`B_i ~ 0.98 M_Pl`, natural" and is explicitly
  **DESI-tuned** ("`f0=0.125` tuned"). Adopting `1/8` would tune toward the
  DESI-matching value -- exactly the RED leakage the pre-registration forbids. Not
  source-first.
- *Naturalness.* `B_i ~ M_Pl` with a Planckian DeWitt vacuum gives `f0 ~ O(1)`, an
  order-of-magnitude band, not a number. Recorded as a weak band, not a committed value.

### RECORDED finding (the pre-registration record)

| Quantity | Source-first status |
|---|---|
| `f0` value | **None -- no source-first number exists** |
| `f0` status | **GENUINELY-FREE now / DERIVABLE-ONLY-AFTER-H41** |
| `f0` naturalness band | `(0, O(few))`; `O(1)` point IF theta-misalignment and DeWitt-vacuum share the gimmel scale |
| FIXED source-first | `M^2 = 8 H0^2` -> the `w(z)` SHAPE / the `(w0,wa)` locus |
| Blocking unbuilt inputs | `B_i` (canon Gap 1) and `mu_DW` (H24) |
| Blocker object | the source action (H41) overall normalization |

Source-first `(w0,wa)` LOCUS as `f0` varies (derived `M^2`, NO DESI used):

```
f0=0.020 -> (-0.9556, -0.0466)      f0=0.250 -> (-0.6107, -0.4883)
f0=0.057 -> (-0.8816, -0.1309)      f0=0.500 -> (-0.4101, -0.7849)
f0=0.125 -> (-0.7677, -0.2733)      f0=1.000 -> (-0.2012, -1.1122)
                                    f0=2.000 -> (-0.0249, -1.3991)
```

### Leakage self-audit

"Did any choice in this derivation reference or get tuned toward the DESI value?"
Per step: **A1 no, A2 no, A3 no, A4 no, A5 no, A6 no** -- every step is green. The one
tempting DESI-ward route (`f0 = 1/8`) was raised and REJECTED precisely because it would
tune toward the data. The recorded finding (f0 not derivable) uses no DESI input. The
committed number is deliberately empty, because the honest source-first answer is that no
number exists yet.

---

## PART B -- Compare to DESI (only after Part A recorded)

Verified DESI DR2 `DESI+CMB+DESY5` (arXiv:2503.14738, Eq. 28; H3-verified digits):
`(w0, wa) = (-0.752 +/- 0.057, -0.86 +0.23/-0.20)`.

**B1 -- The canonical (DESI-tuned) f0 = 0.125 point, as a FIT-comparison.**
`(w0, wa) = (-0.7677, -0.2733)`; marginal `w0 = -0.28 sigma`, `wa = +2.55 sigma`; joint
Mahalanobis (rho = -0.8) `= 4.19 sigma`. Because Part A recorded `f0` as NOT derivable,
this is a FIT comparison, not a parameter-free test: `w0` is nailed only because `f0` was
tuned to nail it, and `wa` is under-evolved at `+2.55 sigma`.

**B2 -- The source-first f0-FAMILY closest approach.** Scanning `f0` at the derived
`M^2`, the minimum Mahalanobis is `3.47 sigma` at `f0 = 0.057` -> `(-0.8808, -0.1318)`.
**No `f0` brings the family within 3 sigma of DESI.** Raising `f0` deepens `|wa|` toward
DESI's `-0.86` but simultaneously drives `w0` up toward `0`, off the DESI degeneracy
direction -- the locus is misaligned with the DESI ellipse, so the family cannot reach it
at any amplitude.

### Verdict

- **Q1 -- Is f0 derivable source-first?** **DERIVABLE-ONLY-AFTER-H41** (equivalently,
  genuinely free now). Fixing `f0` requires the unbuilt source action to set `B_i` and
  `mu_DW`; no built normalization pins it.
- **Q2 -- Recorded value/range.** `f0 = FREE` -- no committed number. Source-first fixes
  the SHAPE (`M^2 = 8 H0^2`) but not the amplitude. Naturalness band `f0 ~ O(1)`; the
  canonical `0.125` is a DESI-tuned fit and is explicitly NOT adopted.
- **Q3 -- Part B verdict.** **NO-TEST-YET.** `f0` stays a FIT. The illustrative fit
  comparison sits at `wa +2.55 sigma` marginal, joint `4.19 sigma`; the source-first
  family's closest approach is `3.47 sigma`. No prediction can be made until the source
  action is built.
- **Q4 -- Adversarial robustness.** For a NO-TEST-YET, the blocker is named exactly: the
  source action (H41) must fix the overall normalization pair `{B_i, mu_DW}`. The
  tempting DERIVABLE-NOW route (`f0 = 1/8` from the `-1/8` sectional) is rejected as
  numerology / back-fit toward the DESI-matching value; the naturalness route gives only
  an order-of-magnitude band. The two blocking inputs are independently sourced (Gap 1
  and H24), so the blocker is not an artifact of one weak claim.

---

## Honest limits

1. **The two-component ansatz is reconstruction-grade.** `f0` is only well-defined as
   `rho_theta/rho_Lambda` IF the DeWitt-Lambda and the theta field are INDEPENDENT
   components. `H_DE_combined_dewitt_theta_desi.py` flags the double-counting caveat: if
   the `O(M^0)` DeWitt background is actually the theta VACUUM VALUE (not a separate
   fluid), the ratio is not even the right object. Settling this needs the built theta
   dynamics.
2. **The "family misses at all f0" latent falsifier is NOT clean.** It rests on the
   reconstruction-grade ansatz AND on `M^2 = 8 H0^2` (OQ2 root-system caveat) AND on an
   LCDM background (not self-consistent). So the locus-miss is a real latent falsifier but
   cannot fire cleanly now; it would harden to a kill only once the ansatz and `M^2` are
   built and the source action forces some `f0`.
3. **This test does not build anything.** It is a derivability audit plus a deterministic
   reproduction. It does not compute the source action, `B_i`, or `mu_DW`.
4. **The recorded "None" is the point.** An empty committed value is the correct
   pre-registration record: it certifies that GU's dark-energy sector has no source-first
   number to test yet, which is a real and honest result, not a failure of effort.

---

## RE-RANK signal

**NO-TEST-YET.** This is not GU's first prediction, and it is not a falsification. It
confirms and sharpens the Wave-18 audit: dark energy stays the sole FIT, and the reason is
now pinned to a specific unbuilt pair `{B_i, mu_DW}`, both of which are the source action's
overall normalization.

- **Single next object: the source action (H41), specifically its overall normalization.**
  This is the one object that would convert the sole FIT into a real test -- a
  source-derived `f0` recorded before DESI comparison. Until then, no dark-energy
  prediction is possible.
- **Sharpened standing falsifier.** The DESI `~3-4 sigma` tension was "soft only because
  `f0` is free." H42 shows the free-`f0` FAMILY itself cannot reach DESI at ANY amplitude
  (closest `3.47 sigma`), because the locus is misaligned with the DESI degeneracy. So the
  softness is narrower than it looked: freeing `f0` does not rescue the fit; only a change
  of SHAPE (a different `M^2`, i.e. the OQ2 correction, or abandoning the two-component
  ansatz) could. This raises the value of (a) resolving OQ2 (`A_3` vs `BC_1`, which moves
  `M^2` and hence the locus) and (b) settling the double-counting question (independent
  Lambda vs theta vacuum) -- both cheaper than the full source action and both able to move
  the locus.
- **Priority order (unchanged in rank, sharper in reason):** the source action normalization
  remains the terminal build; but the cheap discriminators that move the SHAPE (OQ2; the
  Lambda/theta independence question) now rank above further synthesis, because the amplitude
  `f0` provably cannot fix the fit on its own.

---

*Filed 2026-07-12. Wave 19, the f0 pre-registration (H42). Reproduced:
`python -u tests/wave19/H42_f0_prereg.py` (exit 0, 5/5). Pre-registration discipline: Part
A recorded DESI-blind (committed value: None), leakage self-audit all-green, then Part B
compared. The recorded finding is NO-TEST-YET -- an honest "not derivable now," which the
methodology counts as a success of the test, not a failure.*
