---
artifact_type: exploration
label: "Wave A-2 (anchor council queue): DE-12 + the +19.3 inverse problem (incl. JP4) + the W230 c_kin<->FLRW mapping"
created: 2026-08-03
status: exploration
posture: adversarial; truth-seeking; preregistered before computation; no verdict movement
title: "DE pipeline internal-consistency check, proxy shape inverse problem, and the open W230-to-FLRW native mapping"
grade: "DETERMINISTIC NUMERICAL PROXY / hostile-review rebase / claim_status_change: none"
canon_verdict_change: none
hostile_review_status: "MUST-FIX findings absorbed; A2 disposition OPEN_REBASE_REQUIRED"
verdict_gate: "No bar, verdict, canon claim, count, H59, C10, M-H13, or LANE-STATE entry moves. DE-12 is in-sample consistency only; rho_X is a proxy; the native W230-to-FLRW map remains unbuilt."
kill_conditions_declared_before_computation: true
depends_on:
  - lab/process/anchor-council-2026-08-03/seat2-cosmology.md
  - lab/process/anchor-council-2026-08-03/seat4-envelope.md
  - lab/process/anchor-council-2026-08-03/adjudication.md
  - lab/process/CURRENT-RESEARCH-CONTEXT.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - explorations/W230-close-a4-derive-w154-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W158-promotion-gate-boundary-term-C3-2026-07-14.md
  - explorations/W154-reverse-engineered-source-action-2026-07-14.md
  - tests/wave25/H44_de_backreacted_background.py
  - tests/wave29/H46_de_raw_bao_likelihood.py
  - tests/wave45/H46B_referee_grade_desi_verification.py
  - tests/wave46/H46C_theta_star_cmb_calibration.py
scripts:
  - tests/de-certification/de12_theta_star_positive_control.py
  - tests/de-certification/mh13_shape_inverse_feasibility.py
  - tests/de-certification/w230_ckin_flrw_mapping_check.py
---

# DE pipeline certification, the +19.3 inverse problem, and the c_kin bridge test

> **Hostile-review correction (2026-08-03; controls this artifact).** The
> preregistration below is retained as provenance, but three assumptions did not
> survive review. First, the reported DESI `w0wa` row was selected using the same
> data, so DE-12 is an in-sample internal-consistency check, not an independent
> positive control, an unbiasedness proof, or C10 certification. Second, `rho_X`
> is an external proxy family rather than the unbuilt GU record law; positive
> witnesses prove proxy feasibility, while failed local searches could not prove
> global infeasibility. Third, the equality between W230's full connection
> distortion and H44's scalar mode, including pullback, projection, normalization,
> and shared coefficients, is `UNCERTAIN`. The finite W230 fixture and separable
> KK/FLRW toys therefore do not close the native bridge or move M-H13.

Anchor-council Wave A-2 (adjudication Section 3). The preregistration below was
written BEFORE any of the three scripts was written or run. It is retained as
provenance; the Layer-0 row whose premise failed review is tagged inline, and the
controlling correction/results are appended after it.

## 0. Layer-0 typing (before use; per the standing rule)

| Term | Type | Ruling for THIS artifact |
|---|---|---|
| theta | **SUPERSEDED PREMISE: UNCERTAIN** | The preregistration treated the FLRW magnitude mode `B` and W230's connection distortion as the same object. Hostile review found the observation, pullback, projection, normalization, and equation map unbuilt; the top correction controls. |
| r vs Lambda | **HOMONYM pair, reciprocal** | `r` is the self-energy coupling ratio (W187, bar-b selection), not a DE coefficient; `Lambda=c/sqrt(N)` is the candidate DE-native fade. The proxy feasibility check does not bind every native instantiation; it only shows that the sampled external shape families contain realizers. |
| N | **PROXY / NATIVE MAP UNCERTAIN** | The script implements `N_bulk ∝ integral a^3 dt` on the calibrated background and the homogeneous reparameterization `N_conf=pi sqrt(N_bulk)`. It does not construct the promoted-record count or prove equality with the causal/X4-shadow four-volume. |
| c_kin | **PLACEHOLDER / NATIVE COEFFICIENT MAP UNCERTAIN** | W203 leaves `Z_U=|D_AU|²` unbuilt. In the finite ultralocal fixture `c_kin=0` is sufficient for the displayed target ray, but the planted nonzero `L=M` witness refutes the universal finite-fixture iff. The native action coefficient and its base/fibre reduction remain unconstructed. |
| "monotone low-z-growing" | **DEFINED HERE** | A deformation rho_X(z) with rho_X non-increasing in z (the record-accretion direction: grows toward today). "Fade direction" = non-decreasing in z (the Lambda = c/sqrt(N) direction, W154 RE1). |
| N_K | **DEFINED (W158 RISEb)** | The Krein-graded frontier trace N_K = 9 f_+ - 5 f_-, f_+/f_- the confirmed/unconfirmable accretion schedules, weights pinned by the (9,5) trace (q = 5). "Accretion-restricted reachability" (JP4) is operationalised in Section 2 preregistration P4. |
| "+19.3" | **DEFINED (DE-07 item 3)** | gap = chi2_marg(GU shape at its OWN theta*-calibrated cosmology, M^2 = 8, f0 = 0.125) - chi2_marg(LCDM shape at the source Om = 0.315), both amplitude-marginalised on the byte-verified DESI DR2 13x13 likelihood. The on-disk provenance is a session transcript (VERIFIED_REPO_DISCONNECT, seat2 2.2); T0 below recomputes it on-disk. |

Construction fork (GEOMETER-VS-PHYSICS-OBJECTS.md): everything below is the
standard-field late-time likelihood apparatus (theta_star calibration + DESI DR2
BAO Gaussian likelihood) wrapped around the program-native two-component theta
background (H44), i.e. exactly the wave45/46 construction being certified. No
new GU-native object is built. Hygiene honored: nothing under
tests/channel-swings/pw2*, the two named explorations, or papers/candidates/ is
touched; nothing is committed by this agent.

## 1. PREREGISTRATION (written before computing)

### 1.1 DE-12 — pipeline positive control (script: de12_theta_star_positive_control.py)

Push DESI's own best-fit w0waCDM through the H46C theta_star machinery: at fixed
omega_m h^2 = 0.1430 solve theta_star(h) = 1.04110 for h (same A1 radiation
treatment, same A3 ratio correction, same frozen early physics), compute the
BAO chi^2 at the calibrated amplitude A = (c/H0)/r_drag, and compare it to the
same shape's own amplitude-marginalised optimum. (w0, wa) come from the
H46B-verified P1_CPL block (arXiv:2503.14738 Section VII displayed equations);
no network.

Operationalisation of "dAIC ~ 0 vs itself": for a model that DESI's own joint
fit says reconciles the CMB acoustic scale with the DR2 BAO distances, the
theta_star-calibrated amplitude must essentially BE the BAO-preferred amplitude
for that shape. dAIC_self = [chi2(A_cal) + 0] - [chi2_marg + 2] (k = (0,1)).

Preregistered checks (hard asserts; exit couples):
- **PC-F1/PC-F2 (machinery certificate).** The fresh general-rho_DE(z)
  integrator reproduces H46C's LCDM theta_star at h = 0.6736 to < 1e-4
  relative, and its LCDM calibration recovers h = 0.6736 to < 0.2%. Its LCDM
  BAO chi^2 at the Planck amplitude matches H46's 30.68 to < 0.1.
- **CONTROL-1 (primary; DESI+CMB, w0 = -0.42, wa = -1.75 — the no-SNe combo,
  the right control for a BAO+theta_star pipeline).** PASS iff
  chi2(A_cal) - chi2_marg < 4 (amplitude gap < 2 sigma_A, dAIC_self in
  (-2, +2), i.e. ~ 0). PASS => the pipeline is unbiased: it does NOT
  manufacture a spurious amplitude/shape exclusion for a dynamical-DE model
  known to fit; C10 (the envelope's quantitative hook) is certified.
  FAIL (>= 9) => the wave45/46/W129 chain is suspect and EVERY exclusion
  number in seat2 1.2 moves — to be reported loudly, not papered over.
  4..9 = MARGINAL: investigate before certifying.
- **CONTROL-2 (headline combo; DESI+CMB+DESY5, w0 = -0.752, wa = -0.86).**
  Report the same numbers; soft assert chi2(A_cal) - chi2_marg < 9 (this best
  fit includes SNe pulls, so a somewhat larger BAO-only gap is admissible).
  The other two combos (Pantheon+, Union3) are reported unasserted.
- **CONTROL-3 (direction).** Calibrated w0waCDM (DESI+CMB) beats calibrated
  LCDM on the raw BAO chi^2 (the DR2 dynamical-DE preference survives the
  pipeline with the right sign).
- **CONTRAST (context).** GU (M^2 = 8, f0 = 0.125) through the identical fresh
  machinery reproduces the H46C overshoot (gap > 3 sigma_A; H46C row-2 detail:
  +5.74 sigma_A, A_cal = 31.9714, A* = 31.4709).

### 1.2 The +19.3 inverse-problem feasibility check (script: mh13_shape_inverse_feasibility.py)

Setup: the deformed model adds a DE channel rho_X(z) on top of the canonical
theta background (M^2 = 8, f0 = 0.125), re-partitioning today's flat budget
(Om + rho_L + rho_theta(0) + rho_X(0) = 1 with f0 = rho_theta(0)/rho_L held)
and re-running the FULL theta_star calibration per candidate (the deformation
moves D_M(z_star), hence h_cal, hence Om_cal — the mechanism seat2 1.2 names).
Named approximation: rho_X does not enter the theta KG friction (second order:
rho_X and rho_theta are each < ~12% of the budget where they overlap). Metric:
S(v) = amplitude-marginalised shape chi^2 at the deformed model's own
calibrated cosmology; gap = S(0) - S_LCDM; recovery fraction
phi = [S(0) - S(v)] / gap. Basis: piecewise-linear nodes at
z = {0, 0.2, 0.4, 0.65, 0.95, 1.35, 1.85, 2.5}, constant beyond, guarded
negligible at z = 30 (the H46C early-physics condition, re-asserted per seat2
2.1.iii).

Preregistered checks and decision rules:
- **T0 (anchor; hard assert).** gap = 19.3 +/- 2.0 recomputed on-disk (the
  DE-07 number currently lives only in a session transcript). Outside the
  band => loud fail; every phi below rescales to the recomputed gap.
- **T1 (witness; hard assert).** Some unconstrained 8-node deformation reaches
  phi >= 0.8: the space of low-z channels supplying the +19.3 is NONEMPTY
  (the CPL row is the independent witness; its marg chi2 is computed
  alongside, expected ~ -22.8 vs S(0) per DE-07 item 3). If the optimizer
  cannot reach 0.8 the claim "a completion must supply +19.3" has no
  realizer in this space and the E1 export language must be revisited — loud
  fail either way.
- **T2 (the M-H13 question; decision rule preregistered, outcome open).**
  phi_mono = best phi over monotone low-z-growing deformations
  (v non-increasing in z, v >= 0).
  phi_mono < 0.5 => NO monotone accretion-shaped channel can supply even half
  the required shape: M-H13's refit target is INFEASIBLE IN PRINCIPLE and the
  item dies at feasibility, before the M-effort refit is scheduled — the
  valuable cheap kill. phi_mono >= 0.8 => feasible; M-H13 stays schedulable
  IF AND ONLY IF the Section-3 bridge survives. Between: PARTIAL — M-H13
  re-scoped to at most phi_mono of the target. The fade direction
  (v non-decreasing in z) is run as the W154-RE1 cross-check; expected
  phi ~ <= 0.
- **T3 (N^p family; hard assert only for consistency phi_Np <= phi_mono +
  0.05).** N(z) = past 4-volume on the calibrated background (bulk
  normalisation; N_conf = pi*sqrt(N_bulk) covered by p -> p/2, asserted);
  rho_X = eps*(N(z)/N_0)^p, p in {0.25, 0.5, 1, 2, 4, 8}, eps optimised.
  Report best phi_Np. This is the sharpest form of "does ANY N^p-shaped
  deformation lie in the space" (seat2 2.1, CHEAP_NEW_COMPUTATION).
- **T4 (JP4 extension; seat4 Section 5).**
  (i) LEMMA (machine-witnessed over random admissible schedules): under
  accretion-restricted reachability — f_+, f_- non-decreasing AND the
  unconfirmable sector lagging (f_-' <= f_+' pointwise; the W158
  "permanently harder to confirm" reading) — with the pinned weights (9,5):
  N_K' = 9 f_+' - 5 f_-' >= 4 f_+' >= 0, so EVERY reachable N_K is monotone
  and every monotone readout of it lies inside the T2 cone: phi <= phi_mono.
  The negative cone being nonempty (w_- = 5 != 0) does NOT enlarge the
  reachable deformation space. This is the RISEb generalisation JP4 asked
  for.
  (ii) ESCAPE TEMPLATE: the unique way a signed readout leaves the monotone
  cone is rate-dominance, 5 f_-' > 9 f_+' at some epoch (weight-dominance is
  excluded by the (9,5) pin). Fit an inverted-lag schedule (u = f_-'/f_+'
  ramping above 9/5 at low z) to the required deformation; report phi_esc.
  phi_esc >= 0.5 => the JP4 counterexample template SUCCEEDS and the precise
  cost is named: the unconfirmable cone must OUTPACE the confirmed cone at
  low z, inverting W158's lag reading (REFEREE_CONJECTURE-grade escape).
  phi_esc < 0.5 => signed readouts are dead on this leg entirely.

### 1.3 The c_kin <-> FLRW mapping question (script: w230_ckin_flrw_mapping_check.py)

The question (seat2 1.4, XS-S, gates A6/C11/M-H13): does W230's
gradient-stiffness L map to the FLRW time-kinetic term (bridge FAILS as
stated) or vanish at k = 0 homogeneous (tension dissolves)? Answered in
Section 3 by reading + derivation; the script supplies the machine-checked
witnesses. Preregistered witnesses (hard asserts):
- **[PC]** W230's [NEC] anchors reproduce on the same seeds: alignment
  1.00000000 / 0.99654503 / 0.70318085 at c_kin = 0 / 1 / 100.
- **[BLK]** With L split into base-block and fiber-block pieces
  (L = c_b P_b L P_b + c_f P_f L P_f), the identity theta ~ M^{-1}J holds iff
  c_b = c_f = 0; every assignment with either coefficient nonzero breaks it
  (alignment < 1). An indefinite-time-block variant is run as the signature
  fence.
- **[KK]** M^2 = 8 = (9/2)^2 - (7/2)^2 is the fiber normal-Laplacian ground
  eigenvalue (canon lines 80-81) — a gradient-operator eigenvalue, so the
  reduced mass scales with the fiber stiffness: c_f = 0 => M_eff^2 = 0
  (checked on an explicit KK toy).
- **[PIPE]** The H44 pipeline degenerates under the bridge's own axiom:
  solve_backreacted with M^2 -> 0 reduces to LCDM H(z) at f0 = 0.125
  (max |dH^2| < 1e-6): with c_kin = 0 the theta sector has NO distance-level
  phenomenology and the object M-H13 would refit does not exist.

Three-way failure split (seat2 4.1) held in view throughout: (a) bridge fails
as stated; (b) bridge holds, refit fails to recover the shape (exclusion
strengthened, rescue spent); (c) saturation. Section 2 informs (b)'s
feasibility; Section 3 decides (a). A DE-side failure is NOT a bar-b failure
(the two uses of r are typed apart; seat2 4.1 asymmetry protected).

<!-- RESULTS APPENDED BELOW AFTER THE RUNS; PREREGISTRATION TEXT ABOVE UNEDITED -->

## 2. Results after hostile-review repair

All three repaired probes exit zero under pinned `numpy`/`scipy` execution.

### 2.1 DE-12: internal reproduction, not an independent positive control

The DESI+CMB reported `w0wa` shape gives an amplitude-fixed/freed difference
`Δχ² = +0.368`, an amplitude gap `+0.61 σ_A`, and the amplitude-only diagnostic
`ΔAIC_amp = -1.632`. The canonical GU contrast reproduces the stored H46C row:
`h = 0.63749`, `χ²_cal = 66.46`, `χ²_marg = 33.50`, and `+5.74 σ_A`.

This is a useful same-frame consistency check. It is not independent because the
`w0wa` shape was selected from the same DESI data, and the displayed AIC diagnostic
does not charge the selection/complexity cost of the `w0wa` shape. Consequently:

- internal likelihood reproduction: **CONFIRMED**;
- pipeline unbiasedness: **OPEN**;
- C10 certification: **OPEN**.

### 2.2 The corrected proxy inverse problem

Applying the same H46C A3 ratio correction to every candidate repairs the original
calibration mismatch. The high-resolution undeformed row is now `S(0)=33.500`, the
LCDM row is `14.154`, and the on-disk gap is `19.346`.

The numerical searches produced explicit proxy witnesses:

| proxy family | recovered fraction `φ` |
|---|---:|
| unrestricted eight-node | 1.607 |
| monotone low-z-growing | 1.478 |
| best `N^p`, `p=0.25` | 1.098 |
| signed inverted-lag template | 1.382 |
| fade-direction cross-check | 0.662 |

Thus the sampled proxy families are not shape-starved; even the monotone and simple
`N^p` families contain witnesses. The next burden is constructive: derive an actual
record law and its coefficients from the external datum/source action, then ask
whether that low-dimensional family reaches one of these shapes with positive
constraint surplus. No M-H13 status moves from proxy feasibility alone.

### 2.3 W230 fixture and conditional reduction toys

For a fixed target `t=M^{-1}J`, a nonzero operator preserves its direction whenever
`L t` is proportional to `M t`. The planted nonzero witness `L=M` has alignment one
and zero ray residual. This refutes the draft's universal inference that every
nonzero stiffness destroys the relation. The original random W230 fixture and each
tested nonzero base/fibre table entry do rotate the target direction, but only for
that fixture.

The separate KK toy verifies `M²=8=(9/2)²-(7/2)²` and the conditional relation
`ω²=(c_f/c_b)λ₁`. The H44 massless-fibre run keeps the normalized `B''` term while
taking `M²→0`, so it models `(c_b,c_f)=(1,0)`, not simultaneous coefficient removal.
It becomes LCDM to `1.56×10^-10`, as expected for that toy.

The actual native observation/pullback/projection/normalization map, the action's
Euler dual, and the shared coefficient assignment remain unbuilt. Therefore
`W230-NATIVE-BRIDGE = OPEN/BLOCKED`; there is no bridge-failure or M-H13 no-go here.

## 3. Wave-A-2 disposition

`A2 = OPEN_REBASE_REQUIRED`. What survives is useful and directs construction:
the stored likelihood is internally reproducible, the `+19.3` shape target has
simple proxy realizers, and the native coefficient map now has an exact planted
counterexample guarding its future theorem statement. What remains is the GU-native
record law and the connection-to-FLRW reduction. No external datum is selected,
consumed, or changed by this artifact.
