---
artifact_type: exploration
status: exploration (W141; five-team full-roster steelman sweep, FAMILY TEAM 3: observational / experimental / data; 12 personas inline, 24 stories, scored against the W138 battery and the W136 kill list)
created: 2026-07-14
wave: W141
hypothesis: "Joe's framing, steelmanned assumption-first: IF the dark-energy / cosmological-constant channel is a SET ISSUANCE RATE, it gets DISTRIBUTED THROUGH THE OBSERVERS somehow. Find the FUNCTION F describing that rate / distribution as an ASSUMPTION LEG (what it pins: source action, spec FIT rows, observer-slice structure), and give every candidate F its sharpest OBSERVATIONAL discriminant. Kills only after generation."
title: "W141: the observational-family steelman sweep of the set-issuance distribution function F. 12 personas (slice E roster), 24 stories generated, 5 canonical F-shapes killed at generation by the W138 gates (matter-tracking F fails G1b by a factor ~2400 past the 1e19 margin; dust-like schedule fails G2 by 10x; horizon-thermodynamic normalization fails G5 as a dS relabeling; any rate-read structural constant fails G4; any mu_DW-normalized F fails G3), 4 persona stories killed at generation for zero defensible observational purchase. TOP SURVIVORS: S1 uniform set-rate F (exact-LCDM as the PREDICTION, pre-registered DESI DR3 regression call, K5 wire, 2026-27); S2 neutrino-anchored issuance floor (m_lightest ~ 2.3 meV, normal ordering, sum m_nu ~ 61 meV, m_bb <= ~5.4 meV null at ton scale; JUNO + DESI DR3 + CMB, K8 wire, 2026-28); S3 two-scale sub-mm story (fork-B escape band forces the Yukawa signal into the 42-58 um window just below current bounds; next-gen torsion balances close it); S4 record-scheduled wiggle inside the mimic band (SFH-templated w(z), live window eps in [0.03, 0.3] per e-fold, W129 pipeline reusable, must NOT claim the DR2 wiggle); S5 clustered issuance (c_s ~ 0 observer-tracking DE perturbations; ISW x galaxy + CMB lensing, partly runnable on existing data). Everything conditional on the issuance declaration; nothing asserted."
grade: "exploration / conditional-theorem register throughout. Every story is a property of a DECLARED conditional theory (the W136 issuance declaration plus the story's own F-assumption), never of GU. COMPUTED (deterministic, tests/W141_steelman_observational_scoring.py, 14/14 exit 0): the scoring arithmetic (matter-tracking enhancement 2.4e22 vs the 1e19 gate; the S6 edge window [1.2e18, 1.2e19]; the schedule ratios 0.744/0.3 = 2.48 and 3.0/0.3 = 10; the two-scale band-to-floor loop closure and the 42-58 um Yukawa window; the K8 stretch factor 43.5; the S2 neutrino numbers sum ~61.3 meV and m_bb <= 5.35 meV). CITED, binding, not re-derived: W136 (cc227b0) beta/alpha* = 2, f0 = 0 natural point, K1-K8; W138 (ec00fbd) gates G1-G6 with frozen bounds; W129 DE exclusion machinery (verified, reusable); W137 (9cb9f4c) C1/C3 conjectures; H36 dead, B2 rate identity FALSE, both honored everywhere. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change; no spec FIT row moves."
construction: "standard-field throughout for every F and every discriminant (FRW continuity, ephemerides, sub-mm Yukawa phenomenology, neutrino mass observables), per GEOMETER-VS-PHYSICS-OBJECTS.md, so the stories bind any construction; program-native objects enter only as CITED repo results (the a0 = 2 constant, the (B_i, f0) determined pair, the C-operator compression of W137 C1). Forks named where they bite: S3 lives entirely on W136 fork B (two-scale escape, keep branch) and carries its H24-revision cost; S1/S4 live on the W136 baseline (keep branch, measure-stable)."
depends_on:
  - explorations/W136-issuance-declaration-propagation-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - explorations/W137-observer-slice-structure-2026-07-14.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/two-track-persona-sweep-2026-07-11/E-pragmatic-experimental.md
  - explorations/two-track-persona-sweep-2026-07-11/SYNTHESIS.md
scripts:
  - tests/W141_steelman_observational_scoring.py
---

# W141: the observational-family steelman sweep of the set-issuance distribution function F

**Posture.** Assumption-first, kills after, per the wave brief. The framing being steelmanned
(Joe, direct chat): IF the dark-energy / cosmological-constant channel is a SET ISSUANCE RATE,
it gets DISTRIBUTED THROUGH THE OBSERVERS somehow; the deliverable is the FUNCTION F describing
that rate / distribution, treated as an ASSUMPTION LEG from which to back into the rest (the
source action, the spec FIT rows, the observer-slice structure). This is NOT the falsified naive
record-cost claim (the W137 positive-ledger reading is dead; the SIGNED ledger survives), and it
is NOT the B2 rate identity (FALSE, binding): "set issuance rate" below always means a fixed
dimensionful supply datum with a SCHEDULE rho_iss(a) and a spatial ALLOCATION weight, which is
exactly the reading W138 G4 explicitly allows (filtration / schedule readings permitted; only
structural constants read as rates are forbidden).

**Conditional register.** Every statement of the form "X" below reads "X under the issuance
declaration (W136) plus the story's own declared F." Nothing is asserted. No spec FIT row moves.

**Sibling discipline.** W136 (cc227b0), W137 (9cb9f4c), W138 (ec00fbd), W129 are read and
binding. W135 is in flight and its artifact is not in the tree; it is not cited. W139/W140 and
the parallel family teams are unread by design.

## 0. Family coverage

The two-track persona sweep partitions the roster into five families (A orthodox/rigor,
B geometric/structural, C foundations/observer, D wild frontier, E pragmatic/experimental).
The OBSERVATIONAL / EXPERIMENTAL / DATA family of this brief is slice E, taken whole: all 12
personas, run inline in one context, no sub-agents.

1. Commercial scientist. 2. Observational cosmologist (DESI/CMB, BAO distances).
3. Gravitational-wave phenomenologist. 4. Collider / particle phenomenologist.
5. Precision-tests experimentalist (solar-system PPN, fifth force, EP). 6. Model-builder (BSM).
7. Forecaster / Bayesian model-comparison. 8. Science-strategy / portfolio lens.
9. Referee for a flagship journal. 10. Data analyst / likelihood specialist.
11. Numerical / strong-field relativist. 12. Neutrino / flavor phenomenologist.

## 1. The shape of F, fixed by the gates before any story is told

W138 G1a forces the background form: F factorizes as

    Q^nu(x, t) = q(t) u^nu * f(x | observer data),   with <f> = 1 at background,

q(t) the set schedule (baseline q = 3 H rho_L, the exact-Lambda bookkeeping rate), f the
distribution weight over observer slices. The gates then bind the two factors separately:

- the SCHEDULE q(t): G2 caps |d ln rho_iss / d ln a| < 0.3 per e-fold; and any schedule tuned
  to BE the DESI w0-wa signal needs 0.744 per e-fold, 2.48x outside, already excluded (binding:
  no story below claims the DR2 wiggle as evidence);
- the ALLOCATION f(x): G1b caps local enhancement at ~1e19 over uniform; non-metric couplings
  inherit H10/H52 unchanged;
- the NORMALIZATION: G5 kills (as novelty) any story whose issuance total reduces to
  rho_L V_H ~ T_dS S_dS with no new degree of freedom; G3 kills any mu_DW-normalized total;
  G4 kills any story whose "rate" is a structural constant (f0, c_L, alpha_W).

## 2. Canonical kills at generation (shared across personas, one line each)

| # | F-shape | Kill |
|---|---|---|
| CK-1 | Comoving-dilution F (issuance fixed per comoving volume, rho ~ a^-3) | G2: schedule 3.0 per e-fold, 10x outside the band. KILLED-AT-GENERATION. |
| CK-2 | Horizon-thermodynamic F (issuance per Hubble time = T_dS dS/dt, no new dof) | G5: reduces to the Gibbons-Hawking identity (factor 1.46), relabeling. KILLED-AT-GENERATION (novelty). |
| CK-3 | Matter-tracking F (f proportional to local matter density) | G1b: solar-system enhancement rho(1 AU sphere)/rho_L = 2.4e22, a factor ~2400 past the 1e19 gate. KILLED-AT-GENERATION (computed). |
| CK-4 | Rate-read F (f0 or c_L or alpha_W "is" the issuance rate) | G4: standing B2 kill, rates are quotiented fibers and enter no structural equation. KILLED-AT-GENERATION (cited). |
| CK-5 | mu_DW-normalized F (issuance total set by c_L mu_DW^4 at O(1)) | G3: H36 non-reimport, excluded >= 4.775x at the envelope minimum. KILLED-AT-GENERATION (cited). |

Persona stories that reduced to a canonical kill are marked below and not double-counted.

## 3. The persona pass (12 personas, 2 stories each, inline)

Format per story: (i) F, specific; (ii) the assumption leg (what it pins); (iii) the persona's
sharpest observational discriminant with timeline. Generation-kills get one line.

### Persona 1: Commercial scientist

**1A (converges with 7A/9A into survivor S1).** (i) F = the trivial allocation: q(t) = 3 H rho_L
exactly, f = 1 everywhere; the set rate is the exact-Lambda bookkeeping rate and the
distribution through observers is uniform per unit volume of every slice. (ii) Assumption leg:
this IS the W136 baseline; it pins SA-G3/SA-G4 to the determined pair (B_i = 0, f0 = 0) and
rides the SA-G5 = 2 bulk-flatness selection; exact LCDM is the PREDICTION, not the
embarrassment. (iii) Discriminant: the K5 wire, run forward as a pre-registered call: the DESI
DR2 CPL preference must REGRESS toward LCDM in DR3 + SNe + CMB joint analysis. Timeline
2026-2027. A confirmed non-mimic signal |w0 + 1| > 0.1 at joint signal level kills the whole
reading (K5).

**1B (merged with 11B into survivor S6).** (i) F = record-density allocation with saturation:
f = min(n_rec(x)/n_rec_mean, A), with the saturation A declared at the detection edge
A in [1.2e18, 1.2e19] (the one computed decade between "invisible" and the G1b kill).
(ii) Assumption leg: pins F's coupling amplitude to the edge window; the tuning is the counted
cost, flagged at full strength. (iii) Discriminant: solar-system ephemerides
(|dot(GM_sun)/GM_sun|, current envelope 1e-13/yr, best fits ~6e-14/yr) plus binary-pulsar
Gdot/G bounds (~1e-12 to 1e-13/yr): the predicted drift A x 8.5e-33/yr sits between 1e-14 and
1e-13/yr, i.e. inside the improvement reach of INPOP/EPM updates and pulsar timing over the
next ~10 years. Either detected or the window closes.

### Persona 2: Observational cosmologist (DESI/CMB)

**2A (converges with 10A/7B into survivor S4).** (i) F uniform in space, scheduled by the
collective record rate: rho_iss(a) = rho_0 [1 + eps s(a)], s(a) the normalized integrated
record-creation proxy (star-formation-history template: rises to the SFR peak at z ~ 2, flattens
after), |eps| < 0.3 by G2. Growing rho_iss means w slightly phantom (w + 1 = -(1/3) d ln
rho/d ln a < 0) during the growth epoch, relaxing toward -1 as the record rate saturates.
(ii) Assumption leg: replaces the SA-G4 natural point f0 = 0 with a one-parameter TEMPLATE
f0 = f(eps; SFH shape); the shape is fixed by astrophysics, only the amplitude eps is the
declaration. (iii) Discriminant: DESI DR3 BAO + Rubin/LSST SNe + CMB lensing fit of the
template amplitude inside the mimic band: DR3-era joint precision sigma(w0) ~ 0.02-0.05 makes
the live window eps in [0.03, 0.3]; below 0.03 the story is undetectable at this generation
(honest window statement), above 0.3 it is already dead. Binding: the story may NOT be fit to
DR2 as evidence; pre-register the template, score on DR3. Timeline 2026-2028.

**2B (converges with 9B into survivor S5).** (i) F clustered at perturbation level: the
allocation weight tracks observer (record) density, so the issuance component carries
perturbations delta_iss that trace weighted matter clustering; effective sound speed c_s^2 ~ 0
instead of the quintessence c_s^2 = 1. Background exactly uniform (G1a respected); the spatial
structure is O(delta) ~ 1e-5 to 1e-1, astronomically below the G1b margin. (ii) Assumption leg:
pins the observer-slice structure to gravitationally relevant allocation, the first F with a
per-slice degree of freedom that data can see; requires w != -1 by a small margin (pairs with
2A's schedule) or the perturbations are unsourced. (iii) Discriminant: clustered (c_s ~ 0) vs
smooth (c_s = 1) DE is distinguishable in ISW x galaxy cross-correlation and CMB lensing
amplitude at |1 + w| ~ 0.05 with DESI x Planck/ACT now and CMB-S4-era data later; part of the
test is runnable on EXISTING public data. Timeline: now to early 2030s.

### Persona 3: GW phenomenologist

**3A.** (i) F distributed through the effective Planck-mass normalization of each slice: the
issuance exchange with the a0 channel shows up as a cosmological drift of the graviton coupling,
alpha_M(a) proportional to the schedule d ln rho_iss/d ln a (bounded < 0.3 by G2). (ii)
Assumption leg: pins W137 C3 to "varies" (per-slice coupling normalization drifts with the
background section), the first observational face of C3. (iii) Discriminant: standard sirens:
d_L^GW / d_L^EM = exp(-1/2 integral alpha_M d ln a); LVK O5 with ~unity-redshift dark sirens
constrains |alpha_M| ~ O(1), Einstein Telescope / LISA reach ~0.1-0.3, exactly the band edge.
Timeline: O5 2027+, ET/LISA 2030s. K7 discipline: nothing touches the massless TT pole locally;
the drift is a background normalization. SURVIVES gates; ranked mid (discriminant matures late).

**3B (folded into survivor S3, the scale leg).** (i) F routed through the massive spin-2 /
Yukawa mode at mu_DW as mediator of the local allocation. (ii) Assumption leg: the W136 fork-B
two-scale escape (mu_emb = 1.93 meV, geometric ratio mu_emb/mu_DW in [0.41, 0.57]). (iii)
Discriminant: sub-mm gravity, see persona 5. (Same object as 5A; counted once.)

### Persona 4: Collider phenomenologist

**4A.** (i) F normalized through the Majorana spurion channel (SA-Y8): the issuance datum sets
the seesaw conversion v^2/rho^(1/4) = 1.3e16 GeV, read as the heavy-Majorana / unification
scale. (ii) Assumption leg: pins the SA-Y8 declaration row to the issuance datum (the one
dimensionally reachable spurion, W136). (iii) Discriminant: proton decay at Hyper-Kamiokande:
a gauge-coupled scale at 1.3e16 GeV (low side of the GUT band) puts tau(p -> e+ pi0) within
roughly an order of magnitude of the Hyper-K 2030s reach. OOM-on-OOM (the seesaw click is
itself OOM tier); SURVIVES gates but ranked last of survivors, flagged as the weakest
discriminant on the board.

**4B.** (i) F with a vectorlike mirror condensate as the G1a ledger sector. (ii/iii) The mirror
mass is a free modulus; collider absence never falsifies, no near-term kill exists.
KILLED-AT-GENERATION (no defensible observational discriminant; the persona's own W-sweep Q3).

### Persona 5: Precision-tests experimentalist

**5A (survivor S3, with 3B).** (i) F two-scale: the issuance total is set by the embedding scale
mu_emb = (rho_obs/c)^(1/4) = 1.93 meV (c = 2 chart), distributed locally through the mu_DW
Yukawa channel, with the geometric ratio mu_emb/mu_DW in [0.41, 0.57] (W136 K3, fork B, keep
branch; the H24 one-scale revision is the counted cost). (ii) Assumption leg: pins SA-G2's
escape branch to a computable O(1) geometric ratio; backing into the source action, the ratio
is a new geometric datum the action must produce. (iii) Discriminant, computed: the ratio band
maps mu_DW into [3.39, 4.71] meV, which IS the H52 floor envelope (the loop closes exactly,
verified in the test; honest reading: the band was computed at the floor, so the story's
content is that the Yukawa deviation must sit JUST BELOW current sub-mm bounds, in the
lambda = hbar c / mu_DW window of 42-58 um). Next-generation torsion-balance and Casimir-regime
experiments (Eot-Wash upgrades, HUST) probing 20-50 um must DETECT the deviation; every
null result that raises the floor eats the band from the 58 um side, and a floor above
4.7 meV closes fork B entirely (then only the ratio-less baseline S1 survives). Timeline: the
sharpest bench discriminant on the board, ongoing now, decisive within ~5 years of floor
improvement by a factor ~1.4 in mu.

**5B.** (i) F curvature-coupled locally (q tracks matter density). Reduces to CK-3: enhancement
2.4e22 > 1e19. KILLED-AT-GENERATION (computed).

### Persona 6: Model-builder

**6A.** (i) F as the minimal nested model "issuance-LCDM": parameters (rho_0 input; eps
schedule amplitude with SFH shape; optional c_s ~ 0 switch), i.e. the S4 + S5 union as ONE
declared conditional model. (ii) Assumption leg: converts SA-G3/G4/G5 into determined-or-
templated rows at the price of exactly one new declaration row (eps). (iii) Discriminant: the
model is one-parameter nested over LCDM; DESI DR3 + Rubin gives a proper Bayes factor
(the forecaster's persona owns the number). SURVIVES; counted inside S4/S5 rather than as a
separate survivor.

**6B.** (i) F through the W137 C1 compression: allocation weight w(sigma) proportional to the
trace of the compressed positive metric P_sigma eta_+ P_sigma, so the collective object C
distributes the set rate to slices by how much admissible record space each slice compresses
out of H_C+. (ii) Assumption leg: pins C1 true AND gives the C1 conjecture its first
quantitative job (the distribution function is the compression trace); K4 route discipline
honored (linear C only). (iii) Discriminant: weak and indirect: per-environment drift of the
compressed normalization shows up as an environment-correlated Gdot/G; lunar laser ranging and
pulsar timing bound Gdot/G < few e-13/yr but the story does not pin the magnitude. SURVIVES
gates; ranked low (assumption leg sharp, discriminant unpinned). Cheapest sharpener is
W137 K2's compressed-metric test, which is a computation, not an observation.

### Persona 7: Forecaster / Bayesian

**7A (survivor S1, the sharp form).** (i/ii) Same F as 1A. (iii) The Bayesian discriminant
stated as a pre-registered call: under S1 the DR2 w0-wa preference is a fluctuation, so the
DR3 posterior must SHRINK toward w = -1; under the rival (dynamical DE real) it strengthens
past |w0 + 1| > 0.1 joint and K5 fires. Either way the reading pays out within ~18 months.
This is the single sharpest near-term discriminant of the sweep.

**7B (inside S4).** (i/ii) Same as 2A. (iii) The forecast arithmetic that defines the live
window: template amplitudes near the band edge give |w0 + 1| ~ 0.1 (about 3 sigma at DR3-era
joint precision); below eps ~ 0.03 the story is indistinguishable from S1 at this data
generation. Honest statement: S4 is falsifiable-now only in eps in [0.03, 0.3]; outside it,
S4 collapses into S1's wire.

### Persona 8: Portfolio lens

**8A (survivor S2, joint form with persona 12).** (i) F uniform in space (CNB-channel
allocation: the issuance reaches every slice through the relic-neutrino background, uniform to
1e-5, trivially inside G1b), with the NORMALIZATION anchored in the neutrino sector:
rho_obs^(1/4) = kappa m_lightest, kappa = O(1) declared. (ii) Assumption leg: pins SA-Y8 and
the issuance datum to one number, the lightest neutrino mass ~ 2.3 meV; this is the W136 OOM
click promoted to an assumption leg with three independent kill wires. (iii) Discriminant:
triple, all near-term, computed in the test: (a) mass ordering must be NORMAL with a light
lightest state: JUNO resolves ordering 2027-2028 (inverted ordering pushes m_bb and sum m_nu
up and strains the anchor); (b) sum m_nu ~ 61.3 meV near-minimal: DESI DR3 + CMB already bound
sum m_nu < ~70-100 meV and CMB-S4-era reaches sigma ~ 20-30 meV; a measured sum >= 100 meV is
the K8 kill (stretch factor 43.5 > 40, wire live); (c) neutrinoless double beta: the anchor
predicts m_bb <= ~5.4 meV, BELOW ton-scale reach (LEGEND-1000, nEXO, ~10-20 meV): any 0nubb
DETECTION this generation implies quasi-degenerate or inverted and kills the anchor. The
anti-correlated portfolio structure (S1's K5 wire and S2's K8 wire fire on different data) is
the portfolio persona's contribution: the pair cannot both die on the same release.

**8B.** (i) Two-proxy schedule (SFR vs black-hole accretion history) with shape discrimination.
(ii/iii) Shape separation needs post-DR3 precision (Rubin + Roman, early 2030s). SURVIVES;
ranked low inside S4 as its 2030s extension, not counted separately.

### Persona 9: Referee

**9A.** The referee's demand ("one number predicted before you saw it") is satisfied only by
pre-registration; converges into S1: publish the exact-LCDM regression call BEFORE DR3.
Counted inside S1.

**9B (inside S5).** The referee's kill-first order: run the clustered-issuance (c_s ~ 0)
template against EXISTING DESI x Planck ISW / lensing cross-correlations before proposing new
data; the W129 machinery (theta_star calibration, raw BAO likelihood, verified reusable) plus
public lensing likelihoods make this a computation, not a proposal. If the template at the
band edge is already excluded, S5 dies today at zero telescope cost. Counted inside S5 as its
execution order.

### Persona 10: Data analyst

**10A (inside S4).** The implementable object: rho_iss(a) = rho_0 [1 + eps s(a)] dropped into
the W129/H46C pipeline; deliverable is the eps posterior against DESI DR2 BAO + theta_star now
(as a BOUND, never as evidence) and against DR3 on release. The single most immediately
computable forecast in the sweep; named as the successor-wave computation.

**10B (inside S4, the discipline check).** The covariance trap: the DR2 CPL pull (phantom
crossing, w0 > -1 with wa < 0) is nearly orthogonal to the thawing-shaped SFH template, so a
schedule fit to DR2 should return eps consistent with zero; if instead DR2 strongly prefers
nonzero eps WITH the right shape, that is exactly the claim G2 forbids making from DR2 alone,
and the pre-registered DR3 test inherits it. This check enforces W138's "must not claim the
DESI wiggle" clause mechanically.

### Persona 11: Strong-field relativist

**11A.** (i) F record-weighted near horizons (black holes carry no records, so holes get zero
allocation, a local Lambda deficit). (ii/iii) At rho_L density the deficit is ~40 orders below
any strong-field observable. KILLED-AT-GENERATION (no observational purchase at any horizon
scale).

**11B (inside S6).** The enforcement arm of 1B: binary-pulsar timing (orbital-period drift,
Gdot/G) closes the same [1.2e18, 1.2e19] edge window from an independent systematics family;
jointly with ephemerides the window is fully closable within ~10 years. Counted inside S6.

### Persona 12: Neutrino / flavor phenomenologist

**12A (survivor S2, owner).** As 8A; the persona's own sharpening is the 0nubb NULL prediction
(m_bb <= ~5.4 meV, computed with free Majorana phases at PDG-scale angles): a ton-scale
detection is a kill, not a confirmation, which makes S2 unusual among neutrino-anchored DE
stories (most predict signals; this one forbids one).

**12B.** (i) Seesaw-GUT leg alone (leptogenesis normalization). (ii/iii) No clean near-term
discriminant beyond the OOM ledger already recorded in W136. KILLED-AT-GENERATION.

## 4. The scoring pass (battery table)

Gates from W138 (frozen bounds); kill wires from W136 K1-K8. Arithmetic in
`tests/W141_steelman_observational_scoring.py` (14/14, exit 0).

| Story | G1a/b | G2 | G3 | G4 | G5 | K5 wire | K8 wire | Verdict |
|---|---|---|---|---|---|---|---|---|
| S1 uniform set-rate (1A/7A/9A) | pass (f = 1) | pass (schedule 0) | pass | pass (schedule reading) | pass (rho_0 is an input, not T_dS S_dS) | LIVE (its discriminant) | n/a | SURVIVES |
| S2 neutrino-anchored (8A/12A) | pass (CNB uniform) | pass | pass (different scale) | pass | pass (new dof: m_lightest) | inherits S1's | LIVE (its discriminant) | SURVIVES |
| S3 two-scale sub-mm (5A/3B) | pass | pass | pass (ratio band, not c_L ~ O(1); H24 cost counted) | pass | pass | inherits | n/a | SURVIVES (fork B only) |
| S4 scheduled wiggle (2A/10A/7B/6A/8B) | pass | pass by construction (eps <= 0.3); DR2-claim forbidden and enforced (10B) | pass | pass (schedule) | pass | LIVE at window edge | n/a | SURVIVES (window [0.03, 0.3]) |
| S5 clustered issuance (2B/9B) | pass (background uniform; perturbative allocation) | pass (needs small nonzero w + 1) | pass | pass | pass | LIVE | n/a | SURVIVES |
| S6 edge-window enhancement (1B/11B) | pass ONLY in [1.2e18, 1.2e19]; the tuning is the cost | pass | pass | pass | pass | n/a | n/a | SURVIVES, ranked low (tuned) |
| S7 C-compression allocation (6B) | pass | pass | pass | pass (K4 honored) | pass | n/a | n/a | SURVIVES, ranked low (discriminant unpinned) |
| S8 Majorana-GUT proton decay (4A) | pass | pass | pass | pass | pass | n/a | partial | SURVIVES, ranked last (OOM-on-OOM) |
| CK-1 comoving dilution | -- | FAIL 10x | -- | -- | -- | -- | -- | KILLED |
| CK-2 horizon-thermodynamic | -- | -- | -- | -- | FAIL (relabel, 1.46) | -- | -- | KILLED (novelty) |
| CK-3 matter-tracking | FAIL 2.4e22 | -- | -- | -- | -- | -- | -- | KILLED |
| CK-4 rate-read constant | -- | -- | -- | FAIL (B2) | -- | -- | -- | KILLED |
| CK-5 mu_DW-normalized | -- | -- | FAIL (>= 4.775x) | -- | -- | -- | -- | KILLED |
| 4B mirror reservoir | -- | -- | -- | -- | -- | -- | -- | KILLED (no discriminant) |
| 11A horizon deficit | -- | -- | -- | -- | -- | -- | -- | KILLED (no purchase) |
| 12B leptogenesis leg | -- | -- | -- | -- | -- | -- | -- | KILLED (no near-term discriminant) |

G6 (record cost) annotates rather than kills: every survivor's record budget is generous at any
temperature between T_dS and T_CMB (W138), and no survivor claims budget/record fine-tuning.

## 5. Ranked survivors (by discriminant sharpness, then assumption-leg sharpness, then novelty vs the dS relabeling line)

1. **S1: the uniform set-rate F.** F: q = 3 H rho_L, f = 1. Assumption leg: the W136 baseline
   itself; pins (B_i, f0) = (0, 0) and rides SA-G5 = 2. Discriminant: pre-registered DESI DR3
   regression of the DR2 CPL preference; K5 is the kill wire. Timeline ~2026-2027. Novelty:
   modest as a story (it is the declaration's natural point) but maximal as a WIRE, and it is
   the only survivor whose prediction (exact LCDM) is already the computed natural point of the
   declared theory rather than an added structure.
2. **S2: the neutrino-anchored issuance floor.** F: uniform CNB-channel allocation,
   normalization rho^(1/4) = kappa m_lightest. Assumption leg: pins SA-Y8 + the issuance datum
   to m_lightest ~ 2.3 meV. Discriminants: JUNO normal ordering (2027-2028); sum m_nu ~ 61 meV
   near-minimal vs the DESI/CMB bound trajectory (K8 fires at >= 100 meV, stretch 43.5 > 40);
   ton-scale 0nubb must see NOTHING (m_bb <= ~5.4 meV; detection = kill). Three independent
   near-term wires; clearly novel vs the dS line (the normalization is a lab number).
3. **S3: the two-scale sub-mm story.** F: total set by mu_emb = 1.93 meV, local channel at
   mu_DW, geometric ratio in [0.41, 0.57]. Assumption leg: pins SA-G2's fork-B escape to a
   computable O(1) ratio the source action must produce (plus the counted H24 revision).
   Discriminant: the Yukawa deviation is FORCED into the 42-58 um window just below current
   sub-mm bounds; next-gen torsion balances either detect it or close fork B (a floor above
   4.7 meV kills the escape and collapses this branch into S1). Decisive within ~5 years of a
   1.4x floor improvement.
4. **S4: the record-scheduled wiggle inside the mimic band.** F: rho_iss(a) = rho_0
   [1 + eps s(a)], SFH-shaped template, live window eps in [0.03, 0.3]. Assumption leg: replaces
   f0 = 0 with a one-parameter astrophysically shaped template (one new declaration row).
   Discriminant: pre-registered template fit to DESI DR3 + Rubin SNe + CMB lensing; the W129
   pipeline is verified and reusable, and the DR2 fit is run only as a bound (10B discipline).
   Timeline 2026-2028; below eps = 0.03 it collapses into S1.
5. **S5: clustered issuance.** F: background-uniform, perturbation-level allocation tracking
   observer density; c_s^2 ~ 0 DE. Assumption leg: the first F with a data-visible per-slice
   degree of freedom; pairs with S4's schedule. Discriminant: ISW x galaxy + CMB lensing
   amplitude, partly runnable on existing public data (9B execution order); full separation at
   |1 + w| ~ 0.05 with CMB-S4-era data.

Ranked low, kept on the ledger: S6 (edge-window enhancement; ephemerides + pulsar timing close
the last decade within ~10 years; tuned), S7 (C-compression allocation; sharp assumption leg
into W137 C1, discriminant unpinned; cheapest sharpener is the K2 compressed-metric
computation), S8 (Majorana-GUT proton decay; Hyper-K 2030s; OOM-on-OOM).

## 6. What this hands back to the assumption-first program

The family's answer to "find the function": the gates leave F essentially two-factored,
q(t) x f(x), with the schedule confined to a thin band around exact-Lambda and the allocation
confined to perturbation level or a tuned edge decade. Within that space the five survivors
back into the rest as follows: S1 pins the spec's DE rows at their W136 natural point; S2 pins
the issuance datum to a laboratory number (the lightest neutrino mass); S3 pins the fork-B
geometric ratio as a source-action deliverable; S4/S5 pin the first per-observer degrees of
freedom (schedule shape, allocation clustering) that near-future data can actually see. The
convergence worth recording: every sharp discriminant in the family lands in 2026-2028 data
(DESI DR3, JUNO, sub-mm floor improvements, existing ISW/lensing), so the assumption-first
posture is cheaply supervised; nothing here requires waiting for 2030s instruments except the
low-ranked tail.

## Honest limits

- Everything is conditional on the W136 issuance declaration plus each story's own declared F;
  no verdict, canon item, spec FIT row, count, or posture moves.
- The issuance VALUE stays an input in every survivor except S2, where it is traded for a
  different input (m_lightest) rather than predicted.
- S3's band-to-floor loop closure is a consistency of W136's own construction (the band was
  computed at the floor), not an independent coincidence; the test records it as loop closure.
- The S4 window floor (eps = 0.03) is a forecast-grade estimate from quoted DR3-era joint
  precision, not a computed Fisher forecast; the named successor computation is 10A's pipeline
  run.
- Timelines (DESI DR3, JUNO, LEGEND-1000/nEXO, LVK O5, ET/LISA) are cited at
  community-schedule grade.
- Tri-repo gating: "issuance" is a local postulate label per W136; the issuance concept is
  owned by the temporal-issuance repo; no cross-repo identity claim is made (R5 kill stands);
  capability measures belong to TaF; nothing here supports or is supported by either repo
  (one-way rule). The B2 rate identity is FALSE and no structural constant is read as a rate
  anywhere above.
- W135 is in flight; its artifact is not present and is not cited. Parallel family teams
  (W139-W143 others) unread by design.

*Filed 2026-07-14. FAMILY TEAM 3 (observational / experimental / data), 12 personas inline in
one session, no sub-agents. Reproducible:
`python -u tests/W141_steelman_observational_scoring.py` (14/14, exit 0). Exploration grade;
no canon movement.*
