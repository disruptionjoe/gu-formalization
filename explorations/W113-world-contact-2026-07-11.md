---
artifact_type: exploration
status: exploration (WORLD-CONTACT pair, two half-swings run 2026-07-13: (A) the exceptional-point-photonics translation of the Observer Structure Theorem, (B) the carried DESI DR2 BAO run -- H46 reproduction + the (f0, amplitude) delta-chi^2 profile)
created: 2026-07-13
hypothesis: "A: H61/H61a world-contact (does the Observer Structure Theorem's mathematics land in a lab-adjacent system?); B: H46/DARK-ENERGY-03 (the carried raw-H(z) vs DESI DR2 BAO likelihood firm-up)"
title: "A-VERDICT = TRANSLATABLE-NO-NEW-SIGNATURE: the theorem translates EXACTLY into an EP-approaching array of PT-symmetric resonator dimers (the W52/W98 metric eta(r) IS the PT dimer's intertwiner, machine-checked; all three clauses computed in transmission variables), but every finite-array observable is known physics -- the Petermann-factor / mode-nonorthogonality divergence at exceptional points plus Siegl-Krejcirik unbounded-metric (no bounded similarity to Hermitian) behavior; the per-state/sup dichotomy has no finite-array witness beyond the known K ~ 1/(1-r) EP scaling law. B-VERDICT = MARGINAL (reproduced + sharpened): H46 reproduces exactly (chi^2_GU 52.26 vs LCDM 30.68, delta +21.58 canonical; shape-marg -3.17); the NEW joint (f0, A) profile gives min delta = -3.27 at f0 = 0.10 (-1.27 AIC-corrected), GU-better window f0 ~ [0.005, 0.25], and -- correcting this swing's own pre-registered expectation -- the canonical f0 = 0.125 is INSIDE the Delta-chi^2<=1 band: H46's f0-tension (0.05 vs 0.125) was a fixed-amplitude-slice artifact. The entire canonical-point exclusion is carried by ONE direction: GU needs the BAO amplitude +1.8% above the CMB calibration (pinning A costs chi^2 = +41.3). No public DESI DR3 BAO exists as of 2026-07; DR2 remains current."
grade: "exploration / triage. A: exact model-level translation (tests/W113 A0-A4, machine-checked dictionary), literature read-only 2026-07-13; the honesty gate was computed, not asserted. B: reproduction-grade + one honest extension on the actual DESI DR2 likelihood (the H46 in-file official Cobaya bao_data vectors, unchanged). No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture change; H43/H44 CPL falsification untouched; H61/H61a remain OPEN."
depends_on:
  - explorations/observer-structure-theorem-assembly-2026-07-11.md
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - explorations/per-state-sup-separation-2026-07-11.md
  - explorations/wave29/H46-de-raw-bao-likelihood-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W109_observer_structure_theorem.py
  - tests/W98_break_sectorial_closure.py
  - tests/wave29/H46_de_raw_bao_likelihood.py
scripts:
  - tests/W113_world_contact.py
external_refs:
  - "K. Petermann, IEEE J. Quantum Electron. 15 (1979) 566 -- the Petermann excess-noise factor: eigenmode non-orthogonality enhances linewidth/noise; K diverges at eigenvector coalescence."
  - "H. Wang, Y.-H. Lai, Z. Yuan, M.-G. Suh, K. Vahala, Nature 576 (2019) 65 (arXiv/PMC 'Petermann-factor sensitivity limit near an exceptional point in a Brillouin ring laser gyroscope') -- EP-enhanced responsivity is exactly compensated by Petermann-enhanced noise: the divergence is real, measured, and NOT a free lunch."
  - "'Generalized Petermann factor of non-Hermitian systems at exceptional points', Phys. Rev. Research (2025; arXiv:2506.15807) -- K_j ~ eps^-(N-1) divergence at higher-order EPs; bulk/edge EP detection via Petermann factors in ARRAYS -- the array-EP regime is actively discussed."
  - "P. Siegl, D. Krejcirik, Phys. Rev. D 86 (2012) 121702 -- bounded metric with unbounded inverse: no bounded similarity to a self-adjoint operator (the imaginary cubic oscillator is not quasi-Hermitian) -- the mathematical name of clause 3's content."
  - "D. Krejcirik, P. Siegl, M. Tater, J. Viola, J. Math. Phys. 56 (2015) 103513 -- pseudospectra in non-Hermitian quantum mechanics: the measurable shadow of the unbounded-metric regime (transient/response instability), with optics named as the near-experimental home."
  - "DESI Collaboration, arXiv:2503.14738 (DESI DR2 Results II: BAO) + CobayaSampler/bao_data desi_bao_dr2 -- the 13-dim mean + covariance used (verbatim, via the H46 in-file copy)."
  - "Planck 2018, arXiv:1807.06209 Table 2 -- the CMB prior (Om=0.3153, H0=67.36, r_d=147.09) setting the BAO amplitude A_CMB=30.258."
  - "data.desi.lbl.gov/doc/releases -- DR2 (Mar 2025) is the current public release; no DR3 BAO as of 2026-07."
---

# W113 -- World-contact pair: EP-photonics translation + the carried DESI DR2 BAO run

**Role.** Two half-swings at the program's world-contact surface. (A) The Observer Structure
Theorem (`W109`) is model-grade mathematics on a Krein doublet tower approaching an exceptional
point -- which is verbatim the mathematics of non-Hermitian photonics. Translate the three
clauses into a concrete photonic array and determine honestly whether the theorem's dichotomy
has a measurable signature or is known physics. (B) The H46 result (raw GU H(z) vs the actual
DESI DR2 BAO likelihood) was carried three passes: reproduce it, then extend it one honest step
-- the delta-chi^2 profile over the full (f0, amplitude) freedom.

**Artifacts:** this file + deterministic `tests/W113_world_contact.py` (12/12, exit 0,
run 2026-07-13; numpy + the H46/H44 import chain). **Not committed by this run. No claim-status
change.** Exploration-grade.

---

## HALF-SWING A -- the EP-photonics translation

### A.1 The dictionary is exact, not analogical (computed)

The photonic system: an array of coupled PT-symmetric resonator dimers (gain site + loss site,
coupling `kappa_k`, gain/loss rate `gamma_k`), channel `k = 1..N`, with

```
r_k = gamma_k/kappa_k  =  g_k/(g_k + Dw_k/2),   g_k = G k^p,  Dw_k = |m1^2-m2^2|/(w1+w2)
```

i.e. the array's gain/loss-to-coupling ratio programmed to the W98 tower's exceptional-point
parameter (instance: `m1=0, m2=0.3, G=0.1, p=1` -- the same instance the theorem was proven on).
Every channel is PT-unbroken (`r_k < 1`, real split supermodes, propagating), and `r_k -> 1`
across the array: the array approaches the EP channel-by-channel, never reaching it.

Machine-checked dictionary (`W113` A0):

| Theorem object | Photonic object | check |
|---|---|---|
| Krein doublet at mode k | PT dimer `H_k = [[+i gamma, kappa],[kappa, -i gamma]]` | -- |
| the W52/W98 metric `eta(r_k)` | the dimer's **intertwiner** (`H^dag eta = eta H`) | exact, err 5.6e-17 |
| metric conditioning `cond(eta) = (1+r)/(1-r)` | **measurable**: per-channel Petermann factor `K = 1/(1-r^2)` (linewidth/excess-noise enhancement); `cond = 2K/(1+K^{-1}...)` -- same `1/(1-r)` divergence | K rel err 3.6e-11 |
| approach to non-definitizability | approach to the EP (eigenvector coalescence) | `r_2048 = 0.999999+` |

### A.2 The three clauses in transmission variables (computed, `W113` A1-A3)

1. **Per-state finiteness.** Total Petermann-weighted response of an input wavepacket
   `R[c] = sum_k |c_k|^2 K_k` (excess-noise-weighted transmitted power). `K_k ~ k^(p+1)`, so any
   input whose spectral envelope decays faster than `k^-(p+2)/2` (the photonic image of the
   W106 sharp class) has **finite, cutoff-convergent** response: octave ratio 0.66 at N=2048
   (R = 5.34, saturating). The outside-class control diverges (ratio 1.52), and the worst-case
   sup over unit-power inputs grows x4.00 per octave (= `2^(p+1)`, exactly the predicted rate):
   sup K = 9.3e6 at N=2048. **Any finite wavepacket propagates with finite response even as the
   array approaches EP degeneracy; the worst case over inputs is unbounded.**
2. **Interface coherence.** Two overlapping sub-arrays with regional coupling weights (1.0,
   0.45): the metric classes cohere -- `||eta(r^1_k)-eta(r^2_k)|| -> 0` (6.7e-5 -> 3e-8 over
   the probe range) and both null out the **same** EP line `e_null = (1,-i)/sqrt(2)` (the shared
   EP-topology invariant) -- while the operator-level J-data the two observers would apply (the
   inverse-metric maps `eta^{-1/2}`) diverge from each other (44 -> 2843). One shared invariant,
   no shared bounded map. *(Computed correction to the naive reading: the FORWARD maps
   `eta^{1/2}` converge to the same singular limit and their mismatch cond tends to a constant
   set by the weight ratio; the divergent disagreement lives in the inverse maps -- which is
   what `J = S Delta^{-1/2}` actually consumes.)*
3. **No global Hermitianization.** For every channel, conjugation by `S_k = eta(r_k)^{1/2}`
   renders the dimer **exactly Hermitian** (err 2.4e-13) -- every finite truncation of the array
   is similar to a Hermitian (reciprocal, lossless-equivalent) array -- but the similarity cost
   `cond(S_N) = sqrt(cond(eta(r_N)))` grows without bound (763 -> 6106, x2/octave): **no bounded
   global similarity transform to a Hermitian array exists, though every truncation has one.**

### A.3 The honesty gate: is there a NEW measurable signature? (computed + literature)

**No.** Computed (`W113` A4): at every finite N the worst-case response is *attained* by a
legitimate unit-power single-channel drive and equals `K_N = 1/(1-r_N^2)` -- i.e. the
finite-array content of "sup divergence" is exactly the **known per-channel Petermann-factor
divergence at an exceptional point** (Petermann 1979; measured, e.g. Wang et al., Nature 576
(2019) 65, where EP-enhanced gyroscope responsivity is exactly cancelled by Petermann-enhanced
noise). The "no bounded global similarity though every truncation has one" clause is the known
mathematical regime **quasi-Hermiticity failure / bounded metric with unbounded inverse**
(Siegl-Krejcirik PRD 86 (2012) 121702), whose measurable shadow is pseudospectral/transient
response instability (Krejcirik-Siegl-Tater-Viola JMP 2015, which itself names optics as the
near-experimental home). The per-state/sup split is the standard Reed-Simon unbounded-form
dichotomy; its photonic image -- class-input response saturation vs worst-case growth across an
EP-approaching array -- is a *scaling corollary* of the known `K ~ 1/(1-r)` law, not a new
observable. Arrays/lattices of EPs with channel-resolved Petermann factors are already an
active literature (generalized Petermann factors at bulk/edge EPs, PRResearch 2025 /
arXiv:2506.15807). The array-uniformity split as such (which input CLASS keeps the response
finite as the EP approach sharpens) is the one facet we did not find stated as a class boundary
`alpha*(p)` in the photonics literature -- but a finite experiment can only ever measure the
two growth curves, both of which are known physics, so it earns no signature claim.

**A-VERDICT: TRANSLATABLE-NO-NEW-SIGNATURE.** The known-physics names: **Petermann-factor /
eigenmode-nonorthogonality divergence at exceptional points** (per-channel, the sup half) and
**Siegl-Krejcirik unbounded-metric / non-quasi-Hermiticity with pseudospectral instability**
(the no-global-J half). What the translation IS good for: the theorem's clauses are not exotic
-- they are the standing mathematics of a mature experimental field, which raises confidence
that the model-grade structure is physically sensible, while honestly conceding it predicts
nothing that field does not already know.

---

## HALF-SWING B -- the carried DESI DR2 BAO run

### B.1 Reproduction (computed, `W113` B1)

`tests/wave29/H46_de_raw_bao_likelihood.py` re-run 2026-07-13: **exit 0, verdict MARGINAL,
numbers identical** to the 2026-07-11 record. Independent recomputation inside `W113` (importing
the H46 module's data + H44 solver): chi^2_GU = 52.256, chi^2_LCDM = 30.678, delta = +21.578
(canonical f0=0.125, CMB-pinned amplitude); shape-marginalized delta = -3.167. All within 0.05
of the recorded values. **NOT irreproducible.**

### B.2 The extension: the (f0, A) delta-chi^2 profile (new, computed, `W113` B2)

At each f0 the amplitude A is analytically marginalized (exact -- all 13 observables are linear
in A); LCDM gets the same marginalization (chi^2_LCDM(A-marg) = 14.154, dof 12).

| f0 | chi^2_GU(A-marg) | A* | delta vs LCDM |
|---|---|---|---|
| 0.005 | 13.76 | 29.97 | -0.40 |
| 0.02 | 12.78 | 30.10 | -1.38 |
| 0.05 | 11.54 | 30.33 | -2.62 |
| 0.08 | 10.99 | 30.54 | -3.17 |
| **0.100** | **10.89** | 30.66 | **-3.27** |
| 0.125 (canonical) | 10.99 | 30.81 | -3.17 |
| 0.150 | 11.27 | 30.94 | -2.88 |
| 0.25 | 13.51 | 31.38 | -0.64 |
| 0.30 | 14.96 | 31.56 | +0.81 |

- **Profile minimum:** delta-chi^2 = **-3.27** at f0 = 0.10 (**-1.27 AIC-corrected** for GU's
  extra free parameter). Delta-chi^2<=1 interval: **f0 in [0.04, 0.15]** (grid resolution).
  GU-beats-LCDM window: f0 ~ [0.005, 0.25].
- **The corrected finding (this swing's pre-registered expectation was the opposite and the
  test's first run falsified it):** the canonical f0 = 0.125 sits **inside** the
  Delta-chi^2<=1 band (Delta = +0.10 from the minimum). H46's "f0 tension" (BAO optimum ~0.05
  vs CPL-tuned 0.125) was an artifact of the **fixed-CMB-amplitude slice**; on the joint
  profile the distance data are perfectly content with the canonical f0.
- **Where the exclusion actually lives:** entirely in the amplitude direction. At canonical f0
  the data want A* = 30.806 vs A_CMB = 30.258 -- a **+1.81%** amplitude pull; pinning A to the
  CMB calibration costs **chi^2 = +41.3**. (LCDM is pulled the *other* way, A* = 29.92, -1.1%
  -- the two models sit on opposite sides of the Planck-DESI amplitude tension.)

### B.3 Honest verdict and uncertainty

**B-VERDICT: MARGINAL (reproduced; sharpened).**

- Viable as a raw distance **model**: on the full (f0, A) profile GU fits the actual DESI DR2
  BAO likelihood better than LCDM by 3.3 chi^2 (1.3 after AIC), with a broad f0 basin that
  **includes the canonical 0.125**.
- Excluded only at the **CMB-pinned amplitude** (+41.3 chi^2 at canonical f0): the honest
  statement is that GU's raw H(z) needs the dimensionless BAO amplitude ~1.8% above the
  Planck-2018 calibration. Whether that is fatal depends on the H46-named open item (a full
  theta_star re-solve of GU's h with its own D_M(z*), expected <1% shift) -- so the verdict
  stays MARGINAL, not VIABLE-CONFIRMED and not EXCLUDED. The uncertainty band: delta-chi^2
  ranges from -3.3 (amplitude free) to +21.6 (amplitude CMB-pinned); everything between is a
  statement about the amplitude calibration, not about the H(z) shape.
- H43/H44's CPL falsification is a distinct observable and is untouched.
- **DESI DR3:** no public DR3 BAO release exists as of 2026-07 (data.desi.lbl.gov lists DR2,
  Mar 2025, as current; literature through mid-2026 still analyses DR2). The comparison would
  not change qualitatively today; DR3-era BAO (5+ year data) will shrink the covariance and is
  the natural re-run trigger.

---

## What this means for the world-contact story

- **A:** the theorem's mathematics already lives in a lab -- as *known* physics. That is
  world-contact of the confidence-building kind (the structure is physical, its divergences are
  measured phenomena with names), not of the falsifiable-prediction kind. No photonics
  experiment is proposed; none should be, on this evidence.
- **B:** GU dark energy survives its best available raw-data test as a shape, sharper than
  before: the residual exclusion is now localized to a single calibration direction (the BAO
  amplitude vs Planck), with the f0 freedom no longer in tension. The falsification frontier is
  the theta_star amplitude re-solve, then DR3.

## What this does NOT do

No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change; no external
action (literature and DESI release pages read-only). H61/H61a remain OPEN; H43/H44 stand; the
H46 record stands (this swing confirms and sharpens it, changing nothing recorded). Reproducible:
`python -u tests/W113_world_contact.py` (12/12, exit 0, run 2026-07-13).
