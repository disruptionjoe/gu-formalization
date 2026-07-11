# Thread Group C -- discrimination + phenomenology: scoping + first swing

2026-07-11. First swing on Thread Group C (find confirmations that DISCRIMINATE GU from other geometric
theories, and push the phenomenology). The swing has two parts: (1) a computed, reproducible placement of
the theta-sector dark-energy prediction against the DESI DR2 CPL band (C2), and (2) a brief scoping of
C1/C3/C4/C5, each with the single most concrete computable discriminating observable and the first
computation that would produce it. C5 (do carriers A vs B predict different fermion content?) is scoped
against the repo's actual carrier definitions.

Discipline note: no target-loaded numbers are imported (no 24/8, no chi(K3), no fitting to a generation
count). The DESI central values are external published data used as a comparison target, flagged for
verification. "It fits" is not claimed anywhere -- the honest C2 verdict is a ~3-4 sigma TENSION.

---

## C2 (computed) -- theta-sector (w0, wa) vs DESI DR2 CPL band

**Artifact:** `tests/threads/C_dark_energy_wz_vs_desi.py` (exit 0, 5/5 checks). Built on
`tests/one-residual/dark_energy_desi_sign.py` (which established only the SIGN of wa); this test computes
the actual (w0, wa) and places it quantitatively.

**Model prediction (nominal f0 = 0.125, the value used across the one-residual sector):**
```
(w0, wa) = (-0.7677, -0.2733)
```
Solver-independent: the e-fold-Radau and redshift-RK45 formulations agree to <5e-3 in both components.

**DESI DR2 comparison (arXiv:2503.14738, w0waCDM/CPL marginals -- VERIFY digits before public cite; a
2026-07-11 web check confirmed the QUALITATIVE result -- favored quadrant w0>-1, wa<0; 3.1 sigma DESI+CMB,
2.8-4.2 sigma with SNe, DESY5 the 4.2 sigma combo -- but did NOT surface the exact digits):**

| combo | center (w0, wa) | model dw0 | model dwa | approx Mahalanobis (rho=-0.9/-0.8/-0.7) |
|---|---|---|---|---|
| DESI+CMB+DESY5 | (-0.752, -0.86) | -0.02 (-0.3s) | +0.59 (+2.7s) | 5.6 / 4.1 / 3.5 |
| DESI+CMB+Union3 | (-0.667, -1.09) | -0.10 (-1.1s) | +0.82 (+2.8s) | 4.3 / 3.4 / 3.0 |
| DESI+CMB+Pantheon+ | (-0.838, -0.62) | +0.07 (+1.3s) | +0.35 (+1.7s) | 6.6 / 4.6 / 3.8 |

The off-diagonal w0-wa correlation `rho` is NOT published as a single number; the DESI contours are
strongly anti-correlated, so `rho` is scanned over `[-0.9, -0.7]` and the Mahalanobis distance reported as
a RANGE. This is a declared assumption scanned over a band, not a fabricated covariance (diagonal =
published marginals). The ellipse test is therefore APPROXIMATE, pending the official DESI chain covariance.

**Where GU sits -- honest verdict: NEAR-but-in-TENSION (~3-4 sigma).**
- **w0 is an EXCELLENT match** (model -0.768 vs DESI -0.752, -0.3 marginal-sigma).
- **wa magnitude is TOO SMALL** at nominal f0 (model -0.273 vs DESI -0.86, +2.7 marginal-sigma). Right
  SIGN, right QUADRANT (w0>-1 AND wa<0 -- the DESI-favored quadrant), but **under-evolved**.
- **The f0-family is MISALIGNED with the DESI degeneracy.** f0 is the one free amplitude; sweeping it
  raises w0 toward 0 AND deepens wa *together*, tracing a curve in (w0,wa) that is not parallel to DESI's
  degeneracy direction. Consequently NO f0 brings the model inside ~3 sigma: closest approach is
  ~3.2-3.6 sigma (at f0 ~ 0.04-0.08, which then spoils w0). This is stronger than "the nominal point is
  4 sigma out" -- the *entire one-parameter family* stays >3 sigma from DESI+CMB+DESY5.

**What this discriminates:** the correct quadrant/sign already separates GU from LCDM (wa=0) and from
`w<-1` phantom-only models. The tension is a *near-falsifying handle*, not a fit: the single-B-component
slow-roll tail is too shallow to reach DESI's `|wa|~0.86` at the observed `w0~-0.75`. A genuine improvement
(a second component, a different M_KK, or a non-slow-roll IC) would have to bend the (w0,wa) locus toward
the DESI degeneracy -- a concrete, computable next target.

**Grade:** computation-grade for the model (w0,wa), solver-independence, and the raw offsets (exact,
reproducible, exit 0). Order/approx-grade for the ellipse placement (approximate reconstructed covariance;
DESI central digits pending verification against Table 3). NOT a claim of agreement -- an honest tension.

**Honest caveats / not done:** (i) DESI exact central values/errors are from recall, corroborated only
qualitatively by web search -- verify against the paper. (ii) The covariance off-diagonal is assumed. (iii)
The model background is pure LCDM (Om,OL fixed); a self-consistent fit would vary Om and the CMB priors,
which could shift the tension either way. (iv) f0=0.125 is an input, not pinned -- it is argued LINKED to
alpha_W via the shared theta but that link is gated on c_W/OQ2-A, so the "nominal" point has residual
freedom (captured by the f0 sweep).

---

## C1 -- confirmations that DISCRIMINATE GU (not just non-falsifications)

**Single most concrete computable discriminating observable:** the **specific non-monotone shape of
w_DE(z)** -- it rises to a shallow peak near `z ~ 0.2` then falls (established in
`dark_energy_desi_sign.py`, check 5). Monotone thawing/freezing quintessence (Caldwell-Linder) cannot
produce an interior peak; a detection of `dw/dz` changing sign near `z~0.2`, or equivalently a specific
`z_peak`, would discriminate GU's theta-field from single-field monotone quintessence and from CPL itself
(which is monotone in `z/(1+z)`).

**First computation that would produce it:** take the computed `w_DE(z)` curve, bin it at DESI-DR2 redshift
precision, and compute the reduced-chi^2 *improvement* of the GU non-monotone shape over the best-fit
monotone thawing model (and over best-fit CPL) on mock error bars. Output = the significance at which a
future survey could distinguish the peak. This is a direct extension of the existing curve; no new physics.

**Grade of the scoping:** structural/order -- the peak exists and is computed; the discriminating power
(chi^2 improvement at survey precision) is the unbuilt one-step computation.

---

## C3 -- correlation between cosmological EOS and strong-field gravity via the shared theta (II-class)

This is the sharpest GU-specific discriminator, because **no other dark-energy theory ties w(z) to a
black-hole/strong-field observable.** The `willmore_oq2a_functional_selection.py` result welds the II-class
functional to the theta-sector: an `|II|^2` GU has an `O(M^1)` ambient-curvature imbalance on the Psi=0
Schwarzschild section that ONLY the Branch-3 `theta ~ M/rho^2` source can cancel -- and that is the SAME
theta whose amplitude `f_0` dark energy sets. So the shared theta coupling `g` appears in both legs.

**Single most concrete computable discriminating observable:** the **quantitative relation
`f_0 <-> alpha_W`** (dark-energy amplitude <-> strong-field Willmore-residual coefficient) forced by the
shared theta. Eliminate the shared coupling `g` between (a) the DE amplitude `f_0` (which C2 shows DESI
wants near ~0.5 for |wa|, or ~0.06-0.13 for w0) and (b) the Branch-3 cancellation weight `alpha_W`. The
result is a PREDICTED strong-field correction (the coefficient of the leading `M^2/r^6` Willmore residual,
or a horizon-scale/PPN-type deviation) as a function of the DESI-measured EOS. A measurement of `wa`
predicts a black-hole observable, and vice versa -- a correlation absent from every non-geometric DE model.

**First computation:** write the shared-theta normalization explicitly -- `theta_DE` amplitude (Assumption
3, `f_0`) and `theta_grav ~ M/rho^2` (Branch-3) as functions of one coupling `g` -- then solve for
`alpha_W(f_0)` using the computed `Q^TF(B) ~ M^2/r^6` and `R^Y` from `willmore_curved_ambient_term.py`. The
lone gate is `c_W` (OQ2-A); everything else is already computed. Output = `alpha_W` (hence the strong-field
correction magnitude) as a function of the DESI `f_0`, up to `c_W`.

**Grade of the scoping:** structural -- the welding is established (order-grade in the OQ2-A doc); the
explicit `f_0 <-> alpha_W` map is the first computation, gated on `c_W`.

---

## C4 -- Yukawas / mixing / mass hierarchy (where unification dies; why is the top heavy?)

GU's stated mass mechanism (escape-corners campaign, `canon/escape-corners-campaign-RESULTS.md`, and draft
12.12) is severe: **all fermion masses ride a SINGLE VEV modulus** ("minimal coupling and Yukawa coupling
are the same thing"), and the spin-3/2 carrier has **NO invariant mass channel** (`16 x 16 = 10+120+126`,
singlet-free -- computed). The decrease of that one modulus is also the generation mechanism.

**Single most concrete computable discriminating observable:** the **fixed Yukawa RATIOS** implied by a
single-VEV mechanism. If every mass is one VEV times a representation-theoretic Clebsch-Gordan coefficient,
the ratios are FIXED with no free Yukawa matrix -- in particular the `m_t : m_b : m_tau` ratio at the
unification scale is a computable number. "Why is the top heavy?" becomes "which fermion has the
unsuppressed (order-1) CG coupling to the VEV rep?" -- and every other fermion's mass is a computed
suppression relative to it. This is exactly **where unification dies or lives**: a single `10`-Higgs SO(10)
famously forces `m_t = m_b = m_tau` at GUT scale (empirically wrong by O(30) for b/tau vs t), so a naive
single-VEV GU predicts the WRONG light spectrum unless the modulus couples through a non-`10` channel or
the generation-splitting mechanism breaks the degeneracy.

**First computation:** compute the `16 x 16 -> {10, 120, 126}` Clebsch-Gordan coefficients in GU's stated
Spin(10) embedding and read off the tree-level mass ratios each Higgs channel gives; compare `m_t:m_b:m_tau`
to observation. A clean mismatch (the `10`-only degeneracy) is a genuine discriminating prediction --
either GU's single modulus must sit in `126`/`120` (computably different ratios) or the theory is in
tension. This is standard SO(10)-Yukawa group theory, made GU-specific by the single-modulus constraint.

**Grade of the scoping:** structural -- the single-VEV constraint is repo-sourced; the CG-ratio computation
is standard and unbuilt here.

---

## C5 (scoped against actual carrier definitions) -- do carriers A vs B predict DIFFERENT fermion content?

**The carriers (from `canon/carrier-bit-decision-campaign-RESULTS.md`, `canon/escape-corners-campaign-RESULTS.md`,
and the located-not-forced paper Section 8):**

| | Carrier A | Carrier B |
|---|---|---|
| index density | `-42 = 21 sigma/8` | `-38 = 19 sigma/8` |
| order-3 class | `(0,0,0)` (ZERO) | `(0,2,1)/3` (NONZERO, `= 2 x class(Dirac)`) |
| field-space declaration | full vector-spinor **with** a local fermionic (gauge) invariance -> ghost subtraction (`-21`) | gamma-trace-**constrained** `ker(Gamma)`, **no** local fermionic invariance -> no ghost subtraction |
| physics reading | gauged gravitino (ghosts subtracted) | ungauged massive vectorlike spin-3/2 (Porrati-Rahman causal window; K3/Einstein arena) |
| order-3 arena | **DEAD** (zeroed) | **LIVE** (families `Z/3` escape becomes a computed live target) |

The `-42` vs `-38` difference is exactly one unit of ghost subtraction (`-21` vs `-20+1`) times the
`sigma/8` density -- i.e. whether the scalar-spinor ghost is subtracted. The carrier-bit campaign proved
symbol arithmetic CANNOT decide the bit (the `343.73` obstruction is a mutual-exclusion certificate); only
the built source action's field-space declaration (SG4) decides it.

**Assessment -- do the different classes plausibly imply different fermion content/couplings? YES,
structurally, in one specific and computable sense, with a hard caveat.**

- **The difference is not two different explicit spectra -- it is the AVAILABILITY of an odd-generation
  mechanism.** Under carrier B the order-3 class `(0,2,1)/3` is nonzero, so the CRT `Z/3` families-index
  arena is live: a net-chiral odd generation count is a *reachable* external target (`= 2 x class(Dirac)`
  is a concrete computed object). Under carrier A that class is identically zero, so the `Z/3` arena is
  dead and the only interior content is 2-primary / vectorlike (net chiral 0 by Theorem 2). So the carriers
  differ in **whether the theory can host an odd number of chiral generations at all** -- the single most
  physically consequential fork in the fermion sector.

- **This makes "located-not-forced" experimentally distinguishable in principle.** If nature has an odd
  generation count sourced geometrically (rather than by an external flux background), that is evidence for
  carrier B (order-3 live); a purely vectorlike / even-only geometric sector is carrier A. The carrier bit
  is therefore not just a bookkeeping choice -- it maps to a yes/no about the geometric origin of the
  three-ness.

- **Hard caveat (do not overclaim):** even under carrier B, `Hom(Z/3, Z) = 0` means the order-3 class
  cannot literally BE an integer count, and the count stays EXTERNAL and gated on the unbuilt source action
  (SG4). So carrier B does not by itself PRODUCE three generations -- it opens the arena where an odd count
  could live. The distinguishing observable is thus "is the geometric families-index arena nonzero
  (B) or zero (A)?", which is upstream of, not identical to, a measured generation number.

**Single most concrete computable discriminating observable:** the **true-`Y14`-bundle families-`Z/3`
pushforward** -- under carrier B it is a live nonzero target (`(0,2,1)/3`), under carrier A identically
zero. **First computation:** the `pi_! : ch(S)/Y14 -> ch(S_X)/X4` families pushforward on GU's actual
fiber, which is currently undefined because `GL(4,R)/O(3,1)` is non-convex (located-not-forced Section 8,
gate (iii)). The first step is not the full pushforward but the **SG4 field-space declaration** that
selects the carrier -- build the source action's gravitino sector and read whether it declares
`ker(Gamma)`-constrained-without-invariance (B) or full-vector-spinor-with-invariance (A). That single
declaration flips the entire order-3 arena on or off. Everything downstream (families index, generation
parity) is gated on it.

**Grade of the scoping:** structural -- the A/B class difference and its order-3 consequence are canon /
computed; the claim "different classes => different availability of odd chiral content" is a faithful
restatement of the repo's own bookkeeping, not a new computation. The distinguishing computation (SG4 /
families pushforward) is the standing gate, unbuilt.

---

## Summary of the first swing

- **C2 is the reproducible computational result:** `tests/threads/C_dark_energy_wz_vs_desi.py` (exit 0)
  places the theta-sector at `(w0,wa)=(-0.768,-0.273)` -- **w0 excellent, wa too shallow, joint ~3-4 sigma
  from DESI+CMB+DESY5 under approximate covariance, and the whole f0-family misses the DESI degeneracy by
  >3 sigma.** Honest verdict: right quadrant/sign (discriminates from LCDM and phantom models) but a real,
  near-falsifying tension. Approximate pending official covariance and verified DESI digits.
- **C1/C3/C4/C5 scoped**, each with one concrete computable discriminator: C1 = the non-monotone `w(z)`
  peak at `z~0.2` vs monotone quintessence; C3 = the `f_0 <-> alpha_W` map (EOS <-> strong-field, the
  GU-unique correlation via shared theta); C4 = fixed single-VEV Yukawa ratios (`m_t:m_b:m_tau`, where
  SO(10)-style unification lives or dies); C5 = the carrier bit flips the order-3 families arena on (B) or
  off (A), making "located-not-forced" a yes/no about the geometric origin of three-ness -- gated on SG4.
- **Highest-leverage next step:** the C3 `f_0 <-> alpha_W` computation -- it is the one observable that
  makes the C2 tension *discriminating* (a measured `wa` would predict a strong-field number), and it is
  computable now up to the single `c_W` (OQ2-A) datum that the whole source-action narrowing already
  isolates.
