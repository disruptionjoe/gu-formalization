# H3 (Condorcet-#2): DESI DR2 numbers VERIFIED, and the theta-intersection re-run with the corrected residual

2026-07-11. Two jobs on the theta-sector dark-energy leg, both honest:
(A) replace the **model-recall** DESI DR2 constraints (flagged "VERIFY before public cite" in
`tests/threads/C_dark_energy_wz_vs_desi.py`) with the **primary-source** values from arXiv:2503.14738;
(B) redo the gravity ∩ dark-energy order-compatibility test with the Willmore residual **corrected**
from `M^2/r^4` to `M^2/r^6`.

Test: `tests/wave1/H3_desi_verified_and_intersection.py` (exit 0, 17/17 checks).

---

## (A) DESI DR2 — VERIFIED from the primary source

The DESI DR2 PDF (arXiv:2503.14738, "DESI DR2 Results II: Measurements of BAO and Cosmological
Constraints") was downloaded and its text extracted on 2026-07-11. The `w0waCDM` (CPL) constraints appear
BOTH in the results table AND as the paper's marginalized posteriors, **Eqs. (26)-(28)**. Retrieved
verbatim:

| Combination | w0 | wa | LCDM preference |
|---|---|---|---|
| DESI+CMB+Pantheon+ | **-0.838 ± 0.055** | **-0.62 (+0.22/-0.19)** | 2.8σ |
| DESI+CMB+Union3    | **-0.667 ± 0.088** | **-1.09 (+0.31/-0.27)** | 3.8σ |
| DESI+CMB+DESY5     | **-0.752 ± 0.057** | **-0.86 (+0.23/-0.20)** | 4.2σ |

(DESI+CMB alone, no SNe: `w0 = -0.42 ± 0.21`, `wa = -1.75 ± 0.58`, 3.1σ.)

**Verification outcome — the recall was accurate.** Every `(w0, σ_w0, wa)` central value hard-coded in
`C_dark_energy_wz_vs_desi.py` matches the printed digits **exactly**. The *only* refinement is that the
published `wa` errors are **asymmetric**; the recall symmetrized them (DESY5 used 0.22 vs the true
+0.23/-0.20, etc.), a drift of ≤ 0.005 in σ_wa. So the earlier thread-C tension was **not** a
recall artifact — the numbers were right.

- **Retrieved, not invented:** yes. Primary PDF, table + Eqs. 26-28, reproduced in the test's PROVENANCE
  block.
- **Still unverified:** the **w0-wa correlation** ρ. DESI does not tabulate ρ as a single number (it lives
  in the MCMC chains / the published contour). We therefore **scan** ρ ∈ {-0.9, -0.8, -0.7} and report the
  Mahalanobis distance as a *range*, explicitly flagged. Diagonal = verified marginals; off-diagonal =
  declared assumption. This is not a fabricated covariance.

### Where GU actually sits

GU theta-sector point (fixed physics, `f0 = 0.125`): **(w0, wa) = (-0.7677, -0.2733)** — reproduced from
the KG integration, solver-independent.

Marginal-σ against the verified (asymmetric) bars:

| Combination | w0 (σ) | wa (σ) |
|---|---|---|
| DESI+CMB+DESY5 (strongest)  | **-0.28** (excellent) | **+2.55** (under-evolved) |
| DESI+CMB+Union3 | -1.14 | +2.63 |
| DESI+CMB+Pantheon+ | +1.28 | +1.58 |

Joint Mahalanobis (ρ-scanned): DESY5 **3.6-5.7σ**, Union3 3.0-4.3σ, Pantheon+ 3.8-6.6σ. No `f0` in the
one-parameter family reaches inside 3σ of DESY5 (closest approach **3.47σ at f0≈0.06**): the family's
locus is **misaligned** with the DESI degeneracy — raising `f0` deepens `|wa|` but simultaneously raises
`w0` toward 0, so the curve slides *along* rather than *into* the DESI ellipse.

**Verdict (A): a real, near-falsifying discriminator, unchanged by verification.** GU nails DESI's `w0`,
sits in the correct quadrant/sign (distinguishing it from ΛCDM and from `w<-1` phantom models), but
**under-evolves** — it predicts `|wa| ≈ 0.27` where DESI wants ≈ 0.86. The ~3-4σ tension is genuine and now
rests on **verified** data.

---

## (B) The theta ∩ gravity intersection, re-run with the corrected `M^2/r^6` residual

### The original claim
`explorations/source-action-constraint-intersection-2026-07-11.md` argued that `theta` is
**over-determined**: it must simultaneously (i) give the DESI-consistent EOS (dark energy, amplitude
`f0`) and (ii) supply the Branch-3 cancellation of the Willmore residual (gravity). If that holds, gravity
and dark energy collapse to one sector and **`f0` stops being a free fit** — closing dark energy's weakest
point. The stated *necessary condition* was an **order match**: `theta ~ M/ρ²`, so its quadratic stress
`theta² ~ M²/r⁴` matched the Willmore residual `W_s ~ M²/r⁴` — "same order, so a coefficient can cancel
them; different orders would be an immediate disproof."

That match used canon RFAIL-03's **estimate** `M²/r⁴`.

### What the correction changed
The residual has since been **corrected** (`tests/one-residual/willmore_geometric_ii_and_ambient_curvature.py`):
the principled geometric second fundamental form reduces to the graph Hessian `B ~ M/r³`, the mean
curvature is **harmonic** (`□h = 0`), and the leading Willmore residual is
**`Q^TF(B) = (M/r³)² = M²/r⁶`** — two powers of `r` faster than the old estimate (the intermediate
`M²/r²` was an unprincipled artifact).

### Re-run of the order arithmetic (exact integer M- and r-powers)

| object | M-power | r-power | source |
|---|---|---|---|
| `theta` (Branch-3 distortion) | 1 | 2 | source-action-intersection |
| `theta²` (quadratic stress) | 2 | 4 | `(M/r²)²` |
| `B` (principled section II) | 1 | 3 | geometric-II test |
| `R^Y` (ambient Riemann @ g=η) | 0 | 0 | curved-ambient test |
| `R^Y·B` (II-class ambient term) | 1 | 3 | product |
| **`W` OLD estimate** | 2 | **4** | RFAIL-03 (superseded) |
| **`W` CORRECTED** | 2 | **6** | geometric-II (current) |

Cancellation rule (a constant coefficient cancels two tensors iff they share **both** powers):

- **Quadratic-theta route:** `theta² (M²/r⁴)` vs corrected `W (M²/r⁶)` — M-power still matches (both `M²`,
  so still safe for `M/r ≪ 1`), but the **r-power no longer matches** (`r⁻⁴` ≠ `r⁻⁶`). No constant
  coefficient cancels terms with different radial profiles at all `r`. **The old "same order" match
  BREAKS.**
- **II-class linear route** (the post-correction framing): gravity would need an `O(M¹)` theta-source to
  cancel the `O(M¹)` ambient term `R^Y·B`. They share M-power (both `O(M¹)`), but `R^Y·B ~ M/r³` vs
  `theta ~ M/r²` **mismatch in r-power** — closing this needs the source-law inversion to supply an extra
  `r⁻¹`, which is exactly the **unbuilt** `L_theta_source` (OQ2-A).
- **H-class route:** the corrected residual *comes from* harmonic `H` (the principled normalization). In
  the H-class, gravity **self-closes intrinsically** at `O(M²)` (`Q^TF ~ M²/r⁶` balanced by
  `c_W R^Y·H`), with **no leading theta-source at all**. Independently, thread-D identified H-class GU with
  conformal/Bach gravity. In this direction the shared-theta over-determination **dissolves**.

### Verdict (B): the over-determination does NOT tighten — it WEAKENS
With the corrected residual, **both** cancellation routes that would weld `theta` to gravity fail the
r-power test, and the very computation that produced `M²/r⁶` (harmonic `H`) points toward the H-class,
in which gravity needs no `theta`. So the intersection that would have **pinned `f0`** is no longer robust:
it is now **contingent** on (a) GU being II-class *and* (b) an unbuilt source-law inversion supplying the
missing radial power. Consequently **`f0` is not fixed by gravity** — dark energy's weakest point (a free
amplitude) **stays open**, and the DESI tension of Part (A) stands on its own, with **no gravitational
lifeline** to deepen `wa`.

---

## Honest caveats

- **Assumption 3 unproved.** The whole intersection presupposes `theta = D_A*F_A` (the gauge-potential
  sector of the EL derivative). `canon/dark-energy-theta-divergence-free.md` carries this at
  reconstruction grade, explicitly *not* established. If it fails, there is no theta-source to weld to
  gravity at all.
- **Background co-variation not modelled.** The EOS is computed on a *fixed* ΛCDM background (Om=0.315).
  `f0` and `B_i` are fits, not GU predictions. A self-consistent background would move the CPL fit.
- **Covariance.** DESI's ρ is scanned, not retrieved; the Mahalanobis figures are ranges, not the official
  chain result.
- **r-scalings and the source-law inversion are reconstruction-grade / UNBUILT.** The `M/r^n` powers come
  from the exploration chain (symbolic), and how `theta` propagates into the metric stress (the `L_theta_source`
  carrier) is precisely the object not yet built. Part (B) is *order arithmetic given those scalings*, not a
  closed gravitational computation.

## Should this RE-RANK anything?

- **DESI leg (C/H3):** unchanged in strength — the tension survives verification (~3-4σ, under-evolved
  `wa`, correct quadrant). It remains a genuine, near-falsifying observational handle. No re-rank up or
  down from verification alone.
- **The "f0 closes via the intersection" hope:** should be **downgraded**. Pre-correction, the intersection
  looked like it might pin `f0` and close dark energy's weakest point. With `M²/r⁶`, that route does not
  robustly hold — it is contingent on II-class + an unbuilt inversion. Do **not** count the theta-sector
  over-determination as evidence that `f0` is fixed. This aligns with thread-E's brake ("stop counting
  'reduced to one X' passes as progress"): the corrected residual removes, not adds, a leg-coupling.
- **Net for H3's rank:** the observational discriminator is real and verified (keep it high as a
  *falsifier*), but the structural claim that dark energy is rescued by gravity is weaker than the
  pre-correction map implied. H3 should be read as "a clean way GU can be *excluded*," not "a place two
  legs *confirm* each other."

## Grade

Computation-grade for (A) (DESI digits retrieved from the primary PDF; GU point and σ/Mahalanobis
reproducible, exit 0). Order-arithmetic / structural grade for (B) (exact integer power comparisons on
reconstruction-grade scalings; the physics inputs — Assumption 3, the source-law inversion, the H/II
functional choice — remain unbuilt). No canon movement. Feeds WI-068 and the North Star. The single
highest-value next computation is unchanged from the thread pass: the **higher-codimension Willmore first
variation with a background-subtracted linearization**, which settles the H/II binary and therefore whether
the theta-sector over-determination exists at all.
