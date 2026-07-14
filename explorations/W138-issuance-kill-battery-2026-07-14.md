---
title: "W138: the issuance kill battery -- six invariant gates any issuance-type proposal must survive"
status: exploration
doc_type: research_note
updated_at: "2026-07-14"
verdict: "BATTERY BUILT AND COMPUTED. Six gates, each with a quantitative pass criterion and a computed bound, executed in parallel with the W135/W136/W137 issuance proposals so the wave ships with its adversarial pass built in. Headline numbers: uniform DE-scale issuance clears the solar-system ephemeris bound by ~1.2e19 (the gate bites only on local enhancement >= ~1e19 or non-metric coupling); the W129 mimic band translates to an issuance-schedule bound |d ln rho / d ln a| < 0.3 per e-fold (the DESI signal itself needs 0.744, 2.5x outside); any issuance-scale = mu_DW identification at c_L ~ O(1) is excluded by >= 4.78x (envelope) / 6.77-15.18x (central); the rate-identity reading is dead on arrival by the standing B2/rate-independence kill; E_Lambda = T_dS S_dS to a computed factor 1.46, so a normalization landing there is a relabeling (novelty kill, not truth kill); the Landauer budget at T_dS saturates the horizon entropy exactly (same 1.46), while at T_CMB it over-pays plausible record creation by ~1.3e6. No canon change; no proposal is scored here (siblings unread by design)."
construction_used: "standard-field throughout for the gates (GR conservation, PPN, FRW continuity, de Sitter thermodynamics, Landauer); program-native inputs only as CITED repo results (H10 Cassini floor, H50/H52 mu_DW floors, W129 mimic band, B2 rate-independence). Stated per GEOMETER-VS-PHYSICS-OBJECTS.md; the gates deliberately live on the standard-field side so they bind ANY construction."
test: "tests/W138_issuance_kill_battery.py (deterministic, 26/26, exit 0)"
depends_on:
  - "tests/wave22/H10_ppn_weak_field.py"
  - "explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md"
  - "explorations/wave32/H52-alpha13-boundary-cited-2026-07-13.md"
  - "tests/W129_oq2_m2_band_sweep.py"
  - "explorations/path4-branchC-observerse-bridge-2026-07-11.md"
  - "explorations/time-as-finality-crosswalk/rate-independence-negative-finding-2026-06-22.md"
  - "explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md"
---

# W138: the issuance kill battery

**Role in the wave.** W135 (issuance-structure taxonomy), W136 (assume-and-propagate through the
source-action spec), and W137 (per-observer-slice structure) are PROPOSING issuance-type readings
concurrently. This team is the standing adversarial machinery, run in parallel by design: the
battery below is the INVARIANT set of computable checks any issuance-type proposal must survive,
derived without reading the siblings' unfinished work, so their outputs can be scored against it
immediately next wave. "Issuance-type proposal" means any reading in which dark energy (or any
bulk sector) is a genuine source, nabla_mu T^{mu nu} = Q^nu != 0 in the bulk, possibly tied to
observers or records.

Two verdict types are kept strictly separate throughout: a TRUTH kill (the proposal contradicts a
bound or a standing repo falsification) and a NOVELTY kill (the proposal is a relabeling of a
known identity). A proposal can survive one and die by the other.

All numbers below are computed in `tests/W138_issuance_kill_battery.py` (26/26, exit 0), with
positive controls first (SI constants reproduce rho_crit, the 2.3 meV DE scale, R_H, l_p).

---

## Persona 1: GR theorist -- GATE 1 (CONSERVATION)

**The structure.** The Bianchi identity nabla_mu G^{mu nu} = 0 is not negotiable. With
G^{mu nu} = 8 pi G T_total^{mu nu}, a genuine bulk issuance Q^nu in the matter/DE sector must be
balanced by an equal and opposite flux somewhere on the ledger: a running Lambda(t) (as in
unimodular gravity, where Lambda is the integration constant that absorbs the non-conservation),
an explicit reservoir field, or a modified Einstein-side term. A proposal that writes
nabla_mu T^{mu nu} = Q^nu with an unmodified Einstein tensor and no ledger sector is internally
inconsistent, full stop. This is the first, purely structural check.

**Isotropy/homogeneity.** At FRW background level the only rotation-invariant vector in R^3 is
zero, so Q^nu = q(t) u^nu exactly: the issuance current must be purely timelike and comoving at
background level. Any proposal with a background spatial issuance flux fails immediately.

**The quantitative solar-system number.** The baseline issuance reading of a cosmological
constant (holding rho_L fixed in expanding space costs dE = rho_L c^2 dV) gives a local rate
q ~ 3 H rho_L. The DE-equivalent mass inside 1 AU is 8.18e7 kg against M_sun = 1.99e30 kg, so
uniform issuance at that rate drifts the effective GM of the inner solar system by

    |dot(GM)/GM| ~ 8.5e-33 per year.

The planetary-ephemeris bound is |dot(GM_sun)/GM_sun| < ~1e-13 per year (Pitjeva and Pitjev 2013,
MNRAS 432, 3431, report (-6.3 +/- 4.3)e-14/yr; we use 1e-13 as the conservative envelope; this
bound is cited from the literature, not repo-derived). The margin is

    **1.2e19.**

So the conservation gate does NOT kill a uniform metric-only issuance at the DE density scale;
that instinct is quantitatively wrong by nineteen orders of magnitude. What the gate DOES do is
fix the kill criterion exactly: a proposal fails here iff it locally ENHANCES the issuance by a
factor >= ~1e19 over uniform (for example a density-coupled or curvature-coupled q(x) that tracks
matter), or couples through a non-metric channel, in which case:

- **Cassini channel (repo H10, computed):** any metric-coupled Yukawa mediator needs
  m > ~1.4e-17 eV (range < ~0.1 AU) from |gamma - 1| < 2.3e-5
  (`tests/wave22/H10_ppn_weak_field.py`; Bertotti, Iess, Tortora 2003).
- **Sub-mm channel (repo H52, cited):** any matter-coupled scalar mediator at gravitational
  strength needs range < 38.6 um at |alpha| = 1 (Lee 2020, PRL 124, 101101) and < 47.6 um at
  alpha = 1/3 (the H52-cited boundary). These are the channels the repo has already paid for;
  an issuance proposal that re-enters them inherits the exclusions unchanged.

## Persona 2: cosmologist -- GATE 2 (MIMIC, from W129, binding)

W129 (`tests/W129_oq2_m2_band_sweep.py`, 13/13, exit 0; CORRECTION DARK-ENERGY-06) established
band-wide: everything allowed at any admissible (M^2, ansatz) point is an LCDM mimic with
|w0 + 1| < 0.1, and every DESI-CPL-matched amplitude is excluded at dchi^2 >= +33.5 (softest
point M^2 = 3: +14.9 profiled); f0 bounds 0.027 (BC_1) / 0.039 (A_1) / 0.208 (S^3).

**The independent bound derivation (cross-checking W135's fits from the published W129 numbers,
not from a refit).** The FRW continuity equation with a source, dot(rho) + 3H(1+w) rho = q, means
the effective equation of state simply reads the issuance schedule:

    d ln rho / d ln a = -3 (1 + w_eff).

So the W129 mimic band |w0 + 1| < 0.1 is EXACTLY the schedule bound

    **|d ln rho / d ln a| < 0.3 per e-fold**

near z ~ 0. Cumulatively over the DESI window (z <= 2, Delta ln a = ln 3), the allowed total
density drift is < ~39% (upper envelope with w pinned at the bound). And the DESI CPL signal
itself (w0 = -0.752) requires a schedule deviation of 3 x 0.248 = 0.744 per e-fold, a factor
**2.48x outside** the allowed band: any issuance schedule tuned to BE the DESI signal is the
already-excluded reading. This is the same conclusion as W129's dchi^2 >= +33.5, reached through
the continuity equation instead of the likelihood, so the two computations cross-check. Pass
criterion for a proposal: its predicted schedule deviation must sit inside 0.3 per e-fold, i.e.
the proposal must be an LCDM mimic and must NOT claim to explain the DESI w0-wa signal.

## Persona 3: phenomenologist -- GATES 3 and 4 (NON-REIMPORT, exact numbers)

### GATE 3: the H36 non-reimport gate

The falsified thing, precisely: H36 identified rho_Lambda = c_L mu_DW^4 with c_L ~ O(1)
(native horizontal-sectional value 3/8). H50 showed this self-falsifies at face value (the locked
sub-mm Yukawa lands in the excluded region); H52 CITED the boundary and resolved the floor:

    mu_DW >= 3.71 meV (m2_eff = 5/4) to 4.54 meV (m2_eff = 5/6) central,
    envelope [3.4, 4.7] meV,   vs   rho_Lambda^{1/4} = 2.3 meV.

**Exact exclusion factors** (fourth power of the scale ratio, computed):

| floor | (mu_floor / 2.3)^4 | equivalent c_L cap |
|---|---|---|
| 3.4 meV (envelope min) | **4.775** | 0.209 |
| 3.71 meV (central) | 6.770 | 0.148 |
| 4.54 meV (central) | 15.181 | 0.066 |
| 4.7 meV (envelope max) | 17.437 | 0.057 |

The gate, mechanically: any claimed relation between the issuance rate/scale and mu_DW (or any
DeWitt-curvature scale) must EITHER respect the floor (so it cannot set rho_Lambda ~ mu_DW^4 at
c_L ~ O(1); the identification is excluded by >= 4.78x at minimum, 6.77-15.18x central) OR route
through a different scale entirely. A proposal that quietly writes "the issuance scale is the
DeWitt scale" and normalizes it to the observed dark energy has re-imported H36 and dies by the
standing sub-mm citation (H52), not by anything new.

### GATE 4: the B2 non-reimport gate

**What exactly died, with the artifact.** The kill lives in
`explorations/path4-branchC-observerse-bridge-2026-07-11.md` (Path 4, Branch C, candidate B2),
referee section: the literal reading "f_0 (DE amplitude) is an issuance/admissibility RATE" is
FALSE on internal evidence. The mechanism, from two standing artifacts:

- `explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md`: "the issuance
  rate" is four distinct objects, and the bare rate lambda / lambda_max is ABSORBED; it enters
  no structural theorem.
- `explorations/time-as-finality-crosswalk/rate-independence-negative-finding-2026-06-22.md`:
  the signed-readout monotonicity criterion (the program's active theorem lane) has NO
  lambda-dependence; the criterion is purely structural (weights on generators), with no
  reference to any cadence or throughput parameter.
- Path 5 Branch B upgraded this to theorem form: in the Connes Radon-Nikodym cocycle bijection
  {F_tau} <-> Sect, the rate is the QUOTIENTED FIBER; the section is the rate-invariant content
  (`explorations/path5-branchB-filtration-section-map-2026-07-11.md`).

The exact quote of the kill (Branch C, referee): "A rate would be rate-independent and drop out;
these manifestly do not. So f_0 is not a rate. Verdict: the literal identity is refuted by the
repo's own result."

**Mechanical form of the gate** so any new rate claim can be checked without judgment: for a
proposed identification "X = issuance rate", look up whether X appears in any structural
(rate-quotiented) equation in the repo: the Willmore EL coefficient, the DE amplitude, a beta
function, a field equation. If yes, the identification is dead on arrival: a rate is the
quotiented fiber and cannot appear in rate-invariant content. This is exactly how f_0, c_L, and
alpha_W all failed. What the gate does NOT forbid: identifying the issuance with the FILTRATION
{F_tau} (structural, explicitly allowed by Branch C's own closing note) or with a structural
schedule rho(a); those are not rates in the killed sense.

## Persona 4: thermodynamicist -- GATES 5 and 6

### GATE 5: the de Sitter relabeling gate (novelty, not truth)

Computed at the actual background values (H0 = 67.36 km/s/Mpc, Omega_L = 0.6847):

    T_dS = H/(2 pi)         = 2.65e-30 K
    S_dS = pi R_H^2 / l_p^2 = 2.27e122 k_B
    E_Lambda = rho_L c^2 V_H = 5.69e69 J
    T_dS * S_dS             = 8.31e69 J
    ratio T_dS S_dS / E_Lambda = **1.46**

So the dark-energy content of a Hubble volume EQUALS T_dS S_dS to a computed O(1) factor: this is
the Gibbons-Hawking de Sitter equilibrium / Cai-Kim apparent-horizon first law, standard physics
since 1977. **The relabeling criterion:** a proposal whose issuance NORMALIZATION (the number
that sets how much is issued) is derivable from this identity alone, with no new degree of
freedom, is a relabeling of the known de Sitter equilibrium statement. That is a kill of
NOVELTY: the proposal is not wrong, it is not a hypothesis. Kept strictly separate from a kill of
truth; a sibling proposal can pass gates 1-4 and still die here as content-free. The check is
mechanical: derive the proposal's normalization identity and test whether it reduces to
rho_L V_H ~ T_dS S_dS (equivalently, issuance per Hubble time ~ T_dS dS/dt).

### GATE 6: the record-cost gate (Landauer, for the W137 leg)

If observers consume issuance to create records, the floor is k_B T ln 2 per bit. The budget,
taking issuance per Hubble time per Hubble volume as dE = rho_L c^2 dV integrated over one
Hubble time (= 3 E_Lambda):

    budget = 1.71e70 J per Hubble time per Hubble volume.

| temperature | Landauer cost per bit | bits payable per Hubble time |
|---|---|---|
| T_CMB = 2.725 K | 2.61e-23 J | **6.5e92** |
| T_dS = 2.65e-30 K | 2.54e-53 J | **6.7e122** |

Two honest readings, opposite directions:

- **At T_dS the budget exactly saturates the horizon.** 6.7e122 bits = (3/ln 2) S_dS divided by
  the SAME factor 1.46 from gate 5; bits/S_dS = 2.96. So "the issuance pays for records at the
  de Sitter temperature" is not a discovery a proposal can claim: it is gate 5 resurfacing
  (the Landauer-at-T_dS capacity IS the horizon entropy, automatically). Novelty kill if claimed.
- **At T_CMB the budget over-pays any plausible record-creation rate by orders of magnitude.**
  The stellar output of a Hubble volume per Hubble time (luminosity density ~2e8 L_sun/Mpc^3,
  cited order) is 1.3e64 J, i.e. a record-writing ceiling of ~5e86 bits at T_CMB; the DE budget
  exceeds it by a factor **~1.3e6** (and by far more against realistic, far-above-Landauer
  record costs). So the DE budget is NOT fine-tuned to observer record creation at any physical
  temperature between T_dS and T_CMB.

Per the brief, the mismatch is reported as informative structure, not a kill: a W137-type
proposal only dies here if it REQUIRES record creation the budget cannot pay (no such regime
found: the budget is generous at every temperature considered) or if it claims a budget/record
fine-tuning these numbers refute (the ~1e6 gap at T_CMB refutes fine-tuning claims at that
temperature; the exact saturation at T_dS is the relabeling case).

---

## Persona 5: synthesis judge -- THE SCORECARD

Run every issuance-type proposal (W135/W136/W137 outputs, next wave) through this table in
order. G1-G4 are truth gates; G5 is a novelty gate; G6 emits structure. Each check is
computable; the bounds are frozen in `tests/W138_issuance_kill_battery.py`.

| # | gate | check (mechanical) | pass criterion | computed bound |
|---|---|---|---|---|
| G1a | conservation: structure | does the proposal name its Bianchi ledger sector (running Lambda / unimodular constant / reservoir), and is background Q^nu purely q(t) u^nu? | ledger named; Q^i = 0 at background | structural (no number) |
| G1b | conservation: solar system | compute the proposal's local issuance enhancement over uniform 3 H rho_L | local enhancement < ~1e19 over uniform | uniform drift 8.5e-33 /yr vs ephemeris 1e-13 /yr: margin 1.2e19 |
| G1c | conservation: metric Yukawa | if the issuance has a metric-coupled mediator, its mass | m > 1.4e-17 eV (range < 0.1 AU) | repo H10, Cassini gamma 2.3e-5 |
| G1d | conservation: matter coupling | if the issuance couples to matter (any non-metric channel) | range < 38.6 um at alpha = 1; < 47.6 um at alpha = 1/3 | repo H52, Lee 2020 cited |
| G2 | LCDM mimic (W129, binding) | compute the proposal's issuance schedule d ln rho / d ln a over z <= 2 | < 0.3 per e-fold (cumulative < ~39% over the window); must NOT claim to be the DESI signal | DESI signal needs 0.744 = 2.48x outside; W129 dchi^2 >= +33.5 |
| G3 | H36 non-reimport | does the proposal relate its scale to mu_DW with rho_Lambda ~ c_L mu_DW^4? | either respects mu_DW >= 3.4-4.7 meV (=> c_L <= 0.209-0.057, i.e. NOT the DE normalizer at O(1)) or uses a different scale | identification excluded >= 4.775x (envelope min), 6.77-15.18x central |
| G4 | B2 non-reimport | does any proposed "rate" appear in a structural (rate-quotiented) equation? | no structural constant (f_0, c_L, alpha_W, theta-couplings) read as a rate; filtration/schedule readings allowed | kill artifact: path4-branchC (B2); rate = quotiented Connes fiber |
| G5 | de Sitter relabeling (novelty) | derive the proposal's normalization identity | must NOT reduce to rho_L V_H ~ T_dS S_dS with no new degree of freedom | E_Lambda = T_dS S_dS / 1.46 (computed) |
| G6 | record cost (structure) | if records consume issuance: budget vs Landauer at the proposal's stated temperature | no required record rate above budget; no fine-tuning claim the gap refutes | 6.5e92 bits/t_H at T_CMB (over-pays stars by 1.3e6); 6.7e122 at T_dS (= 2.96 S_dS: saturation = G5) |

**Order of severity for scoring:** a G3 or G4 failure is a re-import of a standing repo kill
(cite the artifact, no new computation needed). A G1 or G2 failure is a fresh quantitative kill
(show the number). A G5 failure alone downgrades the proposal to "known physics relabeled"
without touching its truth. G6 annotates.

**What this battery does NOT do:** it does not score any sibling proposal (unread by design),
does not decide whether issuance-type readings are the right direction, and adds no canon or
verdict movement. It is the wave's pre-committed adversarial pass, frozen before the proposals
land so the scoring cannot be bent around them.

**Honest limits.** (i) The ephemeris bound (Pitjeva-Pitjev) and the luminosity density are
external citations at CITED-ORDER grade, not repo-derived; the repo-native channels are H10 and
H52. (ii) The G2 translation uses the continuity equation at background level; a proposal with
strong perturbation-level effects needs the full W129 likelihood, which exists and is the
cross-check. (iii) G6's stellar ceiling is a proxy for "plausible record creation"; any sibling
with a sharper record model should recompute the gap, not the gate.
