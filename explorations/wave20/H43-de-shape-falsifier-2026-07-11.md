---
title: "H43 -- the DE-shape falsifier: is GU's source-first dark-energy (w0,wa) locus-miss of DESI DR2 robust, or an artifact of the reconstruction-grade M^2 (OQ2 A_3-vs-BC_1) and the two-component theta ansatz? Verdict: FALSIFIED at the (w0,wa) comparison -- the locus misses DESI at EVERY admissible root-system M^2 (BC_1=8, A_1=7, S^3=3, continuum=20.25), at the full (M^2,f0)-plane global minimum, under a 1-component ansatz, and under IC variation. Named limit: at the fixed-Omega_m DISTANCE level the model is degenerate (~1%), so this kills the CPL-shape comparison DESI publishes, not the raw H(z)."
artifact_type: exploration
status: exploration
created: 2026-07-12
wave: 20
grade: "FALSIFICATION (of the (w0,wa)-locus comparison). Deterministic reproduction, exit 0, 8/8, nothing imported: the (w0,wa) locus is computed source-first from each admissible normal-Laplacian M^2 and compared to the H3-verified DESI DR2 digits ONLY in the comparison half. M^2 values are root-system eigenvalues (never tuned to data). The distance-metric cross-check is computed, not asserted."
depends_on:
  - "tests/wave20/H43_de_shape_falsifier.py"
  - "tests/wave19/H42_f0_prereg.py"
  - "explorations/wave19/H42-f0-preregistration-2026-07-11.md"
  - "explorations/representation-theory-noncompact/rc3-delta-n-spectrum-gl4r-2026-06-23.md"
  - "explorations/representation-theory-noncompact/rc3-root-multiplicity-bc1-2026-06-23.md"
  - "tests/wave11/H_DE_prediction_vs_fit.py"
  - "tests/wave11/H_DE_combined_dewitt_theta_desi.py"
  - "tests/wave1/H3_desi_verified_and_intersection.py"
  - "canon/theta-field-flrw-dark-energy-eos.md"
verdict: "FALSIFIED (at the (w0,wa)-comparison level). The Wave-19 latent falsifier fires: GU's source-first dark-energy (w0,wa) LOCUS misses DESI DR2 at EVERY admissible root-system M^2 -- BC_1 (7,1) M^2=8 (closest 3.47 sigma), A_1 no-long-root M^2=7 (3.42 sigma), S^3/no-Z2 M^2=3 (3.25 sigma), continuum threshold 20.25 (4.32 sigma) -- and the GLOBAL minimum over the FULL (M^2 in [1,25], f0 in [0.01,6]) plane is still 3.20 sigma (at M^2=1.5, f0=2.04). The miss survives a 1-component ansatz (3.18 sigma), and IC/evolution-factor variation (3.47 sigma). The locus tracks ACROSS the DESI degeneracy; no admissible M^2 rotates it INTO the ellipse. So the DESI tension is NOT an OQ2 artifact and NOT an ansatz artifact: it is a robust shape/direction miss, independent of amplitude f0. NAMED LIMIT (not hand-waved -- computed): at the fixed-Omega_m DISTANCE metric the same models are only ~1-1.3% from a DESI-CPL H(z) (LCDM-amplitude-degeneracy; canon DARK-ENERGY-03), so H43 falsifies the (w0,wa) CPL-parameter comparison DESI headlines, not the raw expansion history. The one untested freedom is the LCDM background (the locus is computed on a non-self-consistent background)."
---

# H43 -- the DE-shape falsifier

Wave-19 (H42) sharpened a latent falsifier: GU's source-first dark-energy `(w0,wa)`
**family** misses DESI DR2 at **every** amplitude `f0` (closest Mahalanobis `3.47 sigma`),
because the locus tracks **across** the DESI `(w0,wa)` degeneracy rather than **into** it.
H42 flagged that the only things softening this were (i) the reconstruction-grade mass
`M^2 = 8 H0^2` (the OQ2 `A_3`-vs-`BC_1` root-system caveat) and (ii) the two-component
theta ansatz. H43 stress-tests **both**: is the miss robust, or an artifact?

Reproduction: `python -u tests/wave20/H43_de_shape_falsifier.py` (deterministic, exit 0, 8/8).

---

## The object and the model

GU's built theta-sector dark energy (canon `theta-field-flrw-dark-energy-eos.md`;
`tests/one-residual/dark_energy_desi_sign.py`): a constant DeWitt-Lambda (`w=-1`) plus a
dynamical Klein-Gordon theta field `B` of mass `M^2`, integrated on an LCDM background
from a slow-roll IC at `z=30`:

```
B'' + (3 + H'/H) B' + (M^2/H^2) B = 0
w_DE(z) = (-1 + f wB)/(1+f),   f = f0 rhoB(z)/rhoB(0),   wB = (KE-PE)/(KE+PE)
```

`f0` is the amplitude knob (Wave-18/19: GU's sole data-facing fit); `M^2` is the **shape**
knob, the lowest discrete normal-Laplacian eigenvalue `lambda_{N,1}` on the fiber
`GL(4,R)/O(3,1)`. The `(w0,wa)` **locus** is the CPL least-squares fit of `w_DE(z)` over the
DESI window `z<=2`, traced as `f0` varies.

---

## Q1 -- M^2 for each admissible root system, and its locus

`M^2` is `lambda_{N,1} = rho^2 - nu_1^2` (units `H0^2`, `R_s=c/H0`), where `rho` is the
half-sum of positive restricted roots and `nu` indexes the discrete-series poles below the
continuum. **Every value below is a root-system eigenvalue -- none is chosen by appeal to
DESI** (the source-first discipline; the audit is in Q4).

| Root-system assignment | `rho` | pole spacing | discrete spectrum (`H0^2`) | **ground `M^2`** |
|---|---|---|---|---|
| **BC_1** `(m1,m2)=(7,1)` [canonical] | `9/2` | half-integer (long root present) | `{8,14,18,20}` | **`8`** |
| **A_1** `m=8` (no long root) | `4` | integer | `{7,12,15}` | **`7`** |
| **S^3 / no-`Z_2`** (full-sphere dual, `l=1`) | -- | `l(l+2)` | `{3,8,15}` | **`3`** |
| continuum threshold (upper anchor) | `9/2` | -- | `rho^2` | `20.25` |

- The canonical `BC_1` value `M^2 = (9/2)^2 - (7/2)^2 = 8` is the RC3 result
  (`rc3-delta-n-spectrum-gl4r`, `rc3-root-multiplicity-bc1`), which the OQ2 caveat flags as
  reconstruction-grade.
- `A_1 -> M^2 = 7`: if the long root is absent (`m_2=0`), `rho=4`, integer poles, ground at
  `nu=3` gives `16-9=7`.
- `S^3 -> M^2 = 3`: if the fiber is the spin cover `S^3` (no `Z_2` quotient by the reflection
  component of `O(3,1)`), the odd harmonic `l=1` survives, `l(l+2)=3`. The `RP^3=S^3/Z_2`
  reduction keeps only even `l`, whose ground `l=2` recovers `M^2=8`.

The three discrete assignments `{3, 7, 8}` **bracket** the admissible ground-state band.

**Closest approach of the locus to DESI, per assignment (COMPUTED):**

| `M^2` (`H0^2`) | assignment | closest Mahalanobis | at `f0` | `(w0,wa)` there |
|---|---|---|---|---|
| `8` | BC_1 | **`3.47 sigma`** | `0.063` | `(-0.870, -0.145)` |
| `7` | A_1 | **`3.42 sigma`** | `0.083` | `(-0.868, -0.156)` |
| `3` | S^3 | **`3.25 sigma`** | `0.396` | `(-0.859, -0.196)` |
| `20.25` | continuum | `4.32 sigma` | `0.010` | `(-0.955, +0.068)` |

Lowering `M^2` (slower theta roll) flattens the locus (less `|wa|`); raising it steepens
`|wa|` but drives `w0` up toward `0`. **In every case the locus passes on the wrong side of
the DESI ellipse.** No admissible `M^2` reaches even `3 sigma`, let alone `2`.

### Q1-decisive -- the whole (M^2, f0) plane

Rather than trust the discrete list, scan the **entire** plane `M^2 in [1,25]`,
`f0 in [0.01,6]` (this subsumes every admissible `M^2`, tuned or not) and take the global
closest CPL point to DESI:

```
GLOBAL min Mahalanobis = 3.20 sigma   at M^2 = 1.50 H0^2, f0 = 2.04  ->  (-0.854, -0.211)
```

Even with `M^2` **and** `f0` both free, the nearest the locus gets to DESI's
`(-0.752, -0.86)` is `3.20 sigma`. **This is a shape/direction miss, not an amplitude miss
and not an `M^2`-magnitude miss.**

- **COMPUTED:** per-root-system closest approaches `{3.47, 3.42, 3.25, 4.32} sigma`; global
  plane minimum `3.20 sigma`. No admissible `M^2` moves the locus within `2 sigma` (or `3`).
- **ARGUED (high confidence):** the direction of the miss is structural -- the theta locus
  slope `dwa/dw0` is set by the KG evolution shape and does not align with the DESI
  degeneracy for any `M^2` in the admissible band.

---

## Q2 -- ansatz robustness

**1-component ansatz** (dark energy is the theta field alone; no separate DeWitt-Lambda;
`w_DE = wB(z)`, so there is **no** `f0` knob -- the shape is fixed by `M^2` alone):

```
1-component closest Mahalanobis over M^2 in [1,25]  =  3.18 sigma  at M^2 = 1.0  ->  (-0.860, -0.204)
   (M^2=3: (-0.565,-0.638), 6.91 sigma;  M^2=8: (+0.263,-1.883), 23.8 sigma)
```

The 1-component model misses by essentially the same `~3.2 sigma` at its best, and much
worse at the canonical `M^2`. **The across-the-degeneracy tracking is NOT a two-component
artifact.**

**IC / evolution-factor variant** (two-component, `M^2=8`, slow-roll IC moved to
`z_start in {10, 30, 100}`): closest approach `3.47 sigma` at `f0~0.055` in all three cases
-- **the miss is not an initial-condition artifact.** (The prior H_DE_combined test already
showed adding a constant Lambda component moves **both** marginals away from DESI, so that
route does not help either.)

- **COMPUTED:** 1-component best `3.18 sigma`; two-component global best `3.20 sigma`;
  IC-variant best `3.47 sigma`. All three families miss at `> 3 sigma`.
- **ARGUED (high confidence):** the miss is a property of ANY GU theta-sector CPL locus in
  the admissible `M^2` band, not of a specific component count or IC.

---

## Q3 -- verdict (marginal and joint sigmas)

| case | `(w0,wa)` | marginal `w0` | marginal `wa` | joint Mahalanobis |
|---|---|---|---|---|
| canonical `f0=0.125, M^2=8` | `(-0.768, -0.273)` | `-0.28 sigma` | `+2.55 sigma` | **`4.19 sigma`** |
| BC_1 best (`M^2=8`) | `(-0.870, -0.145)` | -- | -- | `3.47 sigma` |
| A_1 best (`M^2=7`) | `(-0.868, -0.156)` | -- | -- | `3.42 sigma` |
| S^3 best (`M^2=3`) | `(-0.859, -0.196)` | -- | -- | `3.25 sigma` |
| **global (free `M^2`, free `f0`)** | `(-0.854, -0.211)` | -- | -- | **`3.20 sigma`** |
| 1-component ansatz best | `(-0.860, -0.204)` | -- | -- | `3.18 sigma` |

**VERDICT: FALSIFIED** (at the `(w0,wa)`-comparison level). The Wave-19 latent falsifier
fires. GU's source-first dark-energy `(w0,wa)` locus robustly misses DESI DR2 -- at every
admissible root-system `M^2`, at the full-plane global minimum, under a 1-component ansatz,
and under IC variation. The `~3-4 sigma` DESI tension is **not** softened by freeing the
amplitude (H42), and now shown **not** softened by the OQ2 root-system freedom or by the
ansatz. The locus tracks across the degeneracy; nothing admissible rotates it in.

---

## Q4 -- adversarial

**DESI values (guard against a data bug).** The comparison uses the H3-verified DESI DR2
`DESI+CMB+DESY5` digits (`arXiv:2503.14738`, Eq. 28): `w0 = -0.752 +/- 0.057`,
`wa = -0.86 (+0.23/-0.20)`, `rho = -0.8`. The test asserts these against the verified values
(PASS) and reproduces the canonical GU point `(-0.768, -0.273)` to `< 3e-3` (PASS) -- **no
integration bug, no imported-target drift.**

**M^2 was not tuned (guard against a clearing bug).** Every `M^2` used is a root-system
eigenvalue `{3, 7, 8}` (asserted, PASS). The test explicitly reports that even if one **had**
tuned `M^2` to the data, the plane-scan best (`M^2=1.5`) is still `3.20 sigma` -- **no
`M^2` chosen by appeal to DESI could clear the fit, so no RED tuning is even possible.** This
is a falsification, not a manufactured one.

**The one honest limit, COMPUTED not asserted -- the distance metric disagrees.** DESI
headlines a **CPL `(w0,wa)`** contour, but GU's `w_DE(z)` is **non-CPL**; the Mahalanobis
compares GU's own CPL projection to DESI's ellipse. A different, equally-honest comparison is
the actual expansion history (RMS fractional distance residual vs a DESI-CPL `H(z)` at the
CMB-required `Omega_m`, the fair metric of `H_DE_prediction_vs_fit`). H43 computes both on
the same models:

```
canonical (M^2=8, f0=0.125):     (w0,wa) joint 4.19 sigma   |  distance RMS 2.63%
(w0,wa)-plane best (M^2=1.5):     3.20 sigma                |  distance RMS 1.27%
distance-metric own best:         (0.99% at M^2=1.0, f0=1.85)  (BAO ~ 1.5%)
```

The two metrics **disagree at low `M^2` / high `f0`**: the `(w0,wa)` locus misses DESI's
published CPL ellipse, yet the non-CPL `H(z)` can mimic DESI **distances** to `~1%`. This is
the canon `DARK-ENERGY-03` LCDM-amplitude-degeneracy. **So H43 falsifies the `(w0,wa)`
CPL-parameter comparison DESI reports; it does not independently kill the raw `H(z)`.** That
is the disciplined boundary of this result and it is stated in the verdict, not buried.

---

## Honest limits

1. **The falsification is of the `(w0,wa)` comparison, not the raw expansion history.**
   Computed above: at the fixed-`Omega_m` distance level the same models reach `~1%` (near
   BAO precision). The kill is clean **for the CPL-parameter comparison DESI headlines**,
   which is the standard way GU's prediction has always been stated -- but a reader who
   privileges distances over CPL parameters should read this as "the CPL shape is wrong,"
   not "dark energy is dead at any level."
2. **LCDM background (the single untested freedom).** The locus is computed on a fixed LCDM
   `H(z)`, not a self-consistent background where theta backreacts. A backreacted background
   could in principle rotate the locus; this is the one freedom H43 does **not** close.
3. **The two-component-vs-vacuum double-counting question is still open** (H42 limit 1 /
   `H_DE_combined`): `f0 = rho_theta/rho_Lambda` is only well-defined if the DeWitt-Lambda and
   the theta field are independent. H43's 1-component result (which removes the separate
   Lambda entirely and still misses at `3.18 sigma`) largely defuses this: the miss does not
   require the two-component split.
4. **Reconstruction-grade `M^2`.** The eigenvalues rest on `rc3-delta-n-spectrum-gl4r` /
   `rc3-root-multiplicity-bc1` (CONDITIONALLY_RESOLVED; the CAS Iwasawa verification F6 is
   still open). H43 handles this by scanning the **whole** `M^2` band rather than trusting one
   value, so the verdict does not hinge on the exact eigenvalue.
5. **This test builds nothing new.** It is a robustness audit plus a deterministic
   reproduction. It does not compute the source action, a self-consistent background, or the
   backreaction.

---

## RE-RANK signal

**FALSIFIED** (at the `(w0,wa)` comparison). This is a real, valuable negative: it converts
the Wave-19 "latent, soft only because `f0` is free" tension into a robust falsification of
GU's dark-energy **CPL shape** -- one that survives the amplitude `f0`, the OQ2 root-system
freedom (`M^2 in {3,7,8,...}` and everything between), the component count, and the IC. The
cheap discriminators H42 nominated (resolve OQ2; settle Lambda/theta independence) are now
**spent**: neither rescues the fit. Freeing them was the hope; the hope is closed.

- **Single next object: redo the locus on a SELF-CONSISTENT (theta-backreacted) background.**
  This is the one remaining freedom (Honest limit 2) that could rotate the locus into the
  DESI degeneracy. It is cheaper than the full source action and is the only untested lever.
  If the backreacted locus **also** misses, the `(w0,wa)` falsification hardens toward an
  unconditional kill; if it moves into the ellipse, the miss was a background artifact. Until
  then, GU's dark-energy CPL-shape prediction is **falsified against DESI DR2**, robustly and
  independent of amplitude and `M^2`.
- **Do NOT** re-spend effort on `f0`, on OQ2 `A_3`-vs-`BC_1`, or on the two-component ansatz
  as DE-rescue routes: H43 shows all three are exhausted.

---

*Filed 2026-07-12. Wave 20, the DE-shape falsifier (H43). Reproduced:
`python -u tests/wave20/H43_de_shape_falsifier.py` (exit 0, 8/8). Discipline: `M^2` values are
root-system eigenvalues (never tuned to DESI); DESI digits enter only in the comparison half
and are the H3-verified primary-source values; the distance-metric limit is computed, not
asserted. FALSIFIED is a success of the test, not a failure -- an honest, robust negative.*
